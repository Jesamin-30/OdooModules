# -*- coding: utf-8 -*-
{
    'name': "Odoo-Hospital",

    'summary': "Odoo hospital",

    'description': "",
    'author': "Jesamin Zevallos",
    'version': '0.1',
    # always loaded
    'data': [
        'data/hospital_navbar.xml',
        'security/ir.model.access.csv',
        'views/hospital_hospital.xml',
        'views/hospital_doctor.xml',
        'views/hospital_paciente.xml',
        'views/hospital_cita.xml',
        'views/hospital_dashboard.xml',
        'wizard/hospital_cita.xml',
        'report/hospital_cita.xml',
    ],
}
