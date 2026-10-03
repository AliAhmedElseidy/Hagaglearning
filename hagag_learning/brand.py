import hashlib
import os
import re

import frappe

NAME = "Hagag Learning"
BASE = os.path.join(os.path.dirname(__file__), "public")
CACHE = {}


def ver(rel):
    if rel not in CACHE:
        try:
            with open(os.path.join(BASE, rel), "rb") as f:
                CACHE[rel] = hashlib.md5(f.read()).hexdigest()[:8]
        except Exception:
            CACHE[rel] = "0"
    return CACHE[rel]


def rewrite(html):
    html = html.replace("<!-- Built on Frappe. https://frappeframework.com/ -->", "")
    html = html.replace('<meta name="generator" content="frappe">', "")
    logo = "/assets/hagag_learning/images/logo.svg?v=" + ver("images/logo.svg")
    html = html.replace("/assets/frappe/images/frappe-framework-logo.svg", logo)
    html = html.replace("/assets/frappe/images/frappe-favicon.svg", logo)
    html = re.sub(r"<title>.*?</title>", "<title>" + NAME + "</title>", html, count=1, flags=re.S)
    manifest = "/assets/hagag_learning/manifest/manifest.webmanifest?v=" + ver("manifest/manifest.webmanifest")
    html = html.replace("/api/method/lms.lms.api.get_pwa_manifest", manifest)
    css = '<link rel="stylesheet" href="/assets/hagag_learning/css/hagag_learning.css?v=' + ver("css/hagag_learning.css") + '">'
    return html.replace("</head>", css + "</head>", 1)


def inject(response, request):
    try:
        if not (request.path == "/login" or request.path.startswith("/lms")):
            return
        if response.status_code != 200 or response.mimetype != "text/html":
            return
        html = response.get_data(as_text=True)
        if "hagag_learning.css" in html or "</head>" not in html:
            return
        response.set_data(rewrite(html))
    except Exception:
        frappe.logger("hagag_learning").exception("brand inject failed")
