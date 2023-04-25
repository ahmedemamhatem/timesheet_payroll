// Copyright (c) 2023, Ahmed Emam and contributors
// For license information, please see license.txt

frappe.ui.form.on('Daily Work Log', {
	// refresh: function(frm) {

	// }
});


frappe.ui.form.on('Daily Work Log', {
    refresh: function(frm) {
        if (frm.doc.docstatus == 1) {
            frm.add_custom_button(__('Create New'), function() {
				frappe.new_doc('Daily Work Log');
				
            });
        }
    }
});

frappe.ui.form.on('Daily Work Log', {
    after_save: function(frm) {
        if (frm.doc.docstatus == 1) {
            frappe.new_doc('Daily Work Log');
        }
    }
});
