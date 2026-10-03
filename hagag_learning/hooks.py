app_name = "hagag_learning"
app_title = "Hagag Learning"
app_publisher = "Hagag"
app_description = "Hagag Learning customizations"
app_email = "info@hagagco.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "hagag_learning",
# 		"logo": "/assets/hagag_learning/logo.png",
# 		"title": "Hagag Learning",
# 		"route": "/hagag_learning",
# 		"has_permission": "hagag_learning.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hagag_learning/css/hagag_learning.css"
# app_include_js = "/assets/hagag_learning/js/hagag_learning.js"

# include js, css files in header of web template
# web_include_css = "/assets/hagag_learning/css/hagag_learning.css"
# web_include_js = "/assets/hagag_learning/js/hagag_learning.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hagag_learning/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hagag_learning/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hagag_learning.utils.jinja_methods",
# 	"filters": "hagag_learning.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hagag_learning.install.before_install"
# after_install = "hagag_learning.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hagag_learning.uninstall.before_uninstall"
# after_uninstall = "hagag_learning.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hagag_learning.utils.before_app_install"
# after_app_install = "hagag_learning.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hagag_learning.utils.before_app_uninstall"
# after_app_uninstall = "hagag_learning.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "hagag_learning.build.after_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hagag_learning.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["hagag_learning.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hagag_learning.tasks.all"
# 	],
# 	"daily": [
# 		"hagag_learning.tasks.daily"
# 	],
# 	"hourly": [
# 		"hagag_learning.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hagag_learning.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hagag_learning.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hagag_learning.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "hagag_learning.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hagag_learning.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hagag_learning.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hagag_learning.utils.before_request"]
# after_request = ["hagag_learning.utils.after_request"]

# Job Events
# ----------
# before_job = ["hagag_learning.utils.before_job"]
# after_job = ["hagag_learning.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hagag_learning.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


after_request = ["hagag_learning.brand.inject"]

app_include_css = "/assets/hagag_learning/css/hagag_learning.css"
app_include_js = "/assets/hagag_learning/js/hagag_learning.js"

override_whitelisted_methods = {
    "lms.lms.utils.get_courses": "hagag_learning.private.get_courses",
    "lms.lms.utils.get_course_details": "hagag_learning.private.get_course_details",
    "lms.lms.utils.get_course_outline": "hagag_learning.private.get_course_outline",
    "lms.lms.utils.get_lesson": "hagag_learning.private.get_lesson",
    "lms.lms.utils.enroll_in_course": "hagag_learning.private.enroll_in_course",
}
permission_query_conditions = {"LMS Course": "hagag_learning.private.course_query"}
after_migrate = ["hagag_learning.private.ensure_field"]
