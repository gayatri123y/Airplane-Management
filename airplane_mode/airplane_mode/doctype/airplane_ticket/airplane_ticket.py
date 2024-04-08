# Copyright (c) 2024, Gayatri Yeole and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe import _
from frappe.model.document import Document


 
 

class AirplaneTicket(Document):
    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw(("Airplane Ticket cannot be submitted unless the status is 'Boarded'."))