# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "dark_mode"
app_title = "Dark Mode"
app_publisher = "Alkuhlani"
app_description = "Dark Mode for Frappe"
app_icon = "oction oction-book"
app_color = "gray"
app_email = "aalkuhlani95@gmail.com"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/dark_mode/css/dark_mode.css"
#app_include_css = "/assets/dark_mode/public/css/dark_mode.css"

# app_include_js = "/assets/dark_mode/js/dark_mode.js"

# include js, css files in header of web template
# web_include_css = "/assets/dark_mode/css/dark_mode.css"
# web_include_js = "/assets/dark_mode/js/dark_mode.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "dark_mode.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "dark_mode.install.before_install"
# after_install = "dark_mode.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dark_mode.notifications.get_notification_config"

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
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dark_mode.tasks.all"
# 	],
# 	"daily": [
# 		"dark_mode.tasks.daily"
# 	],
# 	"hourly": [
# 		"dark_mode.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dark_mode.tasks.weekly"
# 	]
# 	"monthly": [
# 		"dark_mode.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "dark_mode.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dark_mode.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dark_mode.task.get_dashboard_data"
# }

