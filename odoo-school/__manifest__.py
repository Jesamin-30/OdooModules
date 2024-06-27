# __manifest__.py
{
    'name': 'Odoo School',
    'version': '1.0',
    'summary': 'Module for managing a school',
    'category': 'Education',
    'author': 'Jesamin Zevallos',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/subject_view.xml',
        'views/school_menu.xml',
    ],
}
