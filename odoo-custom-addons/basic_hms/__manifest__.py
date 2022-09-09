# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{

    "name": "Basic Hospital Management System in Odoo",
    "version": "14.0.0.1",
    "currency": 'EUR',
    "summary": "Apps basic Hospital Management system Healthcare Management Clinic Management apps manage clinic manage Patient hospital manage Healthcare system Patient Management Hospital Management Healthcare Management Clinic Management hospital Lab Test Request",
    "category": "Industries",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps
    This module is used to manage Hospital and Healthcare Management and Clinic Management apps. 
    manage clinic manage Patient hospital in odoo manage Healthcare system Patient Management, 
    Odoo Hospital Management odoo Healthcare Management Odoo Clinic Management
    Odoo hospital Patients
    Odoo Healthcare Patients Card Report
    Odoo Healthcare Patients Medication History Report
    Odoo Healthcare Appointments
    Odoo hospital Appointments Invoice
    Odoo Healthcare Families Prescriptions Healthcare Prescriptions
    Odoo Healthcare Create Invoice from Prescriptions odoo hospital Prescription Report
    Odoo Healthcare Patient Hospitalization
    odoo Hospital Management System
    Odoo Healthcare Management System
    Odoo Clinic Management System
    Odoo Appointment Management System
    health care management system
    Generate Report for patient details, appointment, prescriptions, lab-test

    Odoo Lab Test Request and Result
    Odoo Patient Hospitalization details
    Generate Patient's Prescriptions

    
""",

    "depends": ["base", "sale_management", "stock", "account","mail"],
    "data": [
        'security/company_access.xml',
        'security/hospital_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/assets.xml',
        'views/labscan.xml',
        'views/file_room.xml',
        'views/scan_test.xml',
        'report/diet_plan.xml',
        'report/header.xml',
        'report/lab_bill.xml',
        'report/scan_bill.xml',
        'report/prescription_bill.xml',
        'report/registration_bill.xml',
        'views/set_fruits.xml',
        'views/set_veg.xml',
        'views/picking_inherit.xml',
        'security/doctor_access.xml',
        'views/set_protein.xml',
        'views/set_rice.xml',
        'report/bills_report.xml',
        'views/login_page.xml',
        'views/main_menu_file.xml',
        'wizard/medical_appointments_invoice_wizard.xml',
        'wizard/create_prescription_invoice_wizard.xml',
        'wizard/create_prescription_shipment_wizard.xml',
        'wizard/whatsapp_wizard.xml',
        'views/medical_medicament.xml',
        'views/medical_drug_route.xml',
        'wizard/medical_lab_test_create_wizard.xml',
        'wizard/medical_lab_test_invoice_wizard.xml',
        'views/medical_prescription_order.xml',
        'views/medical_directions.xml',
        'views/medical_dose_unit.xml',
        'views/medical_patient_evaluation.xml',
        'views/medical_family_disease.xml',
        'views/medical_inpatient_registration.xml',
        'views/medical_inpatient_medication.xml',
        'views/medical_insurance_plan.xml',
        'views/medical_appointment.xml',
        'views/medical_insurance.xml',
        'views/medical_patient_lab_test.xml',
        'views/medical_lab_test_units.xml',
        'views/medical_lab.xml',
        'views/medical_feedback.xml',
        'views/medical_neomatal_apgar.xml',
        'views/medical_pathology_category.xml',
        'views/medical_pathology_group.xml',
        'views/medical_pathology.xml',
        'views/medical_patient_disease.xml',
        'views/medical_patient_medication.xml',
        'views/medical_patient_medication1.xml',
        'views/medical_patient_pregnancy.xml',
        'views/medical_patient_prental_evolution.xml',
        'views/medical_patient.xml',
        'views/medical_physician.xml',
        'views/medical_preinatal.xml',
        'views/medical_prescription_line.xml',
        'views/medical_puerperium_monitor.xml',
        'views/medical_rcri.xml',
        'views/medical_rounding_procedure.xml',
        'views/medical_test_critearea.xml',
        'views/medical_test_type.xml',
        'views/medical_vaccination.xml',
        'views/res_partner.xml',
        'views/medical_doctor.xml',
        'report/report_view.xml',
        'report/appointment_recipts_report_template.xml',
        'report/medical_view_report_document_lab.xml',
        'report/medical_view_report_lab_result_demo_report.xml',
        'report/newborn_card_report.xml',
        'report/patient_card_report.xml',
        'report/patient_diseases_document_report.xml',
        'report/patient_medications_document_report.xml',
        'report/patient_vaccinations_document_report.xml',
        'report/prescription_demo_report.xml',
        'report/patient_ebook.xml',
        'report/doctor_ebook.xml',
        'report/diet_report.xml',
        'views/diet_for.xml',
        'views/set_diets.xml',
        'views/medical_habit.xml',
        'views/patient_document.xml',
        'views/medical_document.xml',
        'views/prescribe_diet.xml',
        'views/test_unit.xml',
        'views/medical_symptoms.xml',
        'views/res_city.xml',
        'views/treatment_for.xml',
        'views/register_payment.xml',
        'views/float.xml',
        'wizard/register_wizard.xml',
        'views/patient_bills.xml',
        'views/account_payment_inherit.xml',
        'views/product_product.xml',
        'report/reg_barcode.xml',
        
    ],
    "author": "BrowseInfo",
    "website": "https://www.browseinfo.in",
    "installable": True,
    "application": True,
    "auto_install": False,
    "images": ["static/description/Banner.png"],
    "live_test_url": 'https://youtu.be/fk9dY53I9ow',

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
