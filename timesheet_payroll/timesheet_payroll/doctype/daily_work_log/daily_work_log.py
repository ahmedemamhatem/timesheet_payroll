# Copyright (c) 2023, Ahmed Emam and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import add_to_date, flt, get_datetime, getdate, time_diff_in_hours
from erpnext.controllers.queries import get_match_cond
from erpnext.setup.utils import get_exchange_rate
from frappe.model.document import Document
from frappe.utils import getdate, now_datetime, nowdate, flt, cint, get_datetime_str, nowdate
from frappe import _

from datetime import datetime, date, time
import json
from dateutil.relativedelta import relativedelta
# import frappe
from frappe.model.document import Document

class DailyWorkLog(Document):
	@frappe.whitelist()
	def before_insert(self, method=None):
		pass
	@frappe.whitelist()
	def after_insert(self, method=None):
		pass
	@frappe.whitelist()
	def onload(self, method=None):
		pass
	@frappe.whitelist()
	def before_validate(self, method=None):
		pass
	@frappe.whitelist()
	def validate(self, method=None):
		pass
	
	@frappe.whitelist()
	def on_submit(doc, method=None):
		salary_component = frappe.db.get_value(
				"Activity Cost",
				filters={
					"employee": doc.employee,
					"activity_type": doc.activity_type
				},
				fieldname="salary_component"
			)
		payroll_rate = frappe.db.get_value(
				"Activity Cost",
				filters={
					"employee": doc.employee,
					"activity_type": doc.activity_type
				},
				fieldname="payroll_rate"
			)
		extra_doc = frappe.get_doc(dict(
			doctype='Extra Salary',
			employee=doc.employee,
			salary_component=salary_component,
			amount=(doc.amount * payroll_rate) ,
			payroll_date=doc.date,
			timesheet=doc.name,
			overwrite_salary_structure_amount=1
		))
		extra_doc.insert(ignore_permissions=True)
		extra_doc.submit()
