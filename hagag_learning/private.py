import frappe
from frappe import _

PRIV_ROLES = {"Moderator", "System Manager"}


def _orig(name):
    from lms.lms import utils

    return getattr(utils, name)


def _is_priv(user):
    return user == "Administrator" or bool(PRIV_ROLES & set(frappe.get_roles(user)))


def _is_private(course):
    try:
        return bool(frappe.db.get_value("LMS Course", course, "is_private"))
    except Exception:
        return False


def _manages(course, user):
    if not user or user == "Guest":
        return False
    if _is_priv(user):
        return True
    if frappe.db.get_value("LMS Course", course, "owner") == user:
        return True
    return bool(frappe.db.exists("Course Instructor", {"parent": course, "instructor": user}))


def can_view(course, user=None):
    user = user or frappe.session.user
    if not course or not _is_private(course):
        return True
    if user == "Guest":
        return False
    if _manages(course, user):
        return True
    return bool(frappe.db.exists("LMS Enrollment", {"course": course, "member": user}))


def _check(course):
    if not can_view(course):
        frappe.throw(_("هذا الكورس غير متاح"), frappe.PermissionError)


def _name(row):
    if isinstance(row, dict):
        return row.get("name") or row.get("course")
    return row


@frappe.whitelist(allow_guest=True)
def get_courses(filters=None, start=0, limit_page_length=None):
    rows = _orig("get_courses")(filters, start, limit_page_length)
    return [r for r in rows if can_view(_name(r))]


@frappe.whitelist(allow_guest=True)
def get_course_details(course):
    _check(course)
    return _orig("get_course_details")(course)


@frappe.whitelist(allow_guest=True)
def get_course_outline(course, progress=False):
    _check(course)
    return _orig("get_course_outline")(course, progress)


@frappe.whitelist(allow_guest=True)
def get_lesson(course, chapter, lesson):
    _check(course)
    return _orig("get_lesson")(course, chapter, lesson)


@frappe.whitelist()
def enroll_in_course(course, payment_name=None):
    if _is_private(course) and not _manages(course, frappe.session.user):
        frappe.throw(_("هذا الكورس خاص ولا يمكن التسجيل فيه ذاتيا"), frappe.PermissionError)
    return _orig("enroll_in_course")(course, payment_name)


@frappe.whitelist()
def can_manage(course):
    return _manages(course, frappe.session.user)


@frappe.whitelist()
def add_student(course, email):
    if not _manages(course, frappe.session.user):
        frappe.throw(_("غير مسموح"), frappe.PermissionError)
    if not frappe.db.exists("User", email):
        frappe.throw(_("المستخدم غير موجود"))
    if not frappe.db.exists("LMS Enrollment", {"course": course, "member": email}):
        frappe.get_doc({"doctype": "LMS Enrollment", "course": course, "member": email}).insert(
            ignore_permissions=True
        )
    return "ok"


def course_query(user=None):
    user = user or frappe.session.user
    if _is_priv(user) or not frappe.db.has_column("LMS Course", "is_private"):
        return ""
    u = frappe.db.escape(user)
    return (
        "(IFNULL(`tabLMS Course`.is_private,0)=0 or `tabLMS Course`.owner={u} "
        "or `tabLMS Course`.name in (select course from `tabLMS Enrollment` where member={u}) "
        "or `tabLMS Course`.name in (select parent from `tabCourse Instructor` where instructor={u}))"
    ).format(u=u)


def ensure_field():
    from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

    create_custom_fields(
        {
            "LMS Course": [
                dict(
                    fieldname="is_private",
                    label="كورس خاص (مخفي)",
                    fieldtype="Check",
                    default="1",
                    insert_after="published",
                    description="لا يظهر إلا للطلاب المضافين",
                )
            ]
        }
    )


def _need_manage(course):
    if not _manages(course, frappe.session.user):
        frappe.throw(_("غير مسموح"), frappe.PermissionError)


@frappe.whitelist()
def get_settings(course):
    _need_manage(course)
    row = frappe.db.get_value("LMS Course", course, ["published", "is_private"], as_dict=True)
    return {
        "published": int(row.published or 0),
        "is_private": int(row.is_private or 0),
        "can_publish": _is_priv(frappe.session.user),
    }


@frappe.whitelist()
def get_students(course):
    _need_manage(course)
    rows = frappe.get_all(
        "LMS Enrollment", filters={"course": course}, fields=["member"], order_by="creation desc"
    )
    for r in rows:
        r["full_name"] = frappe.db.get_value("User", r["member"], "full_name")
    return rows


@frappe.whitelist()
def remove_student(course, email):
    _need_manage(course)
    for n in frappe.get_all("LMS Enrollment", filters={"course": course, "member": email}, pluck="name"):
        frappe.delete_doc("LMS Enrollment", n, ignore_permissions=True)
    return "ok"


@frappe.whitelist()
def set_visibility(course, is_private):
    _need_manage(course)
    frappe.db.set_value("LMS Course", course, "is_private", 1 if int(is_private) else 0)
    return "ok"


@frappe.whitelist()
def set_published(course, published):
    if not _is_priv(frappe.session.user):
        frappe.throw(_("النشر للإدارة فقط"), frappe.PermissionError)
    frappe.db.set_value("LMS Course", course, "published", 1 if int(published) else 0)
    return "ok"
