# models/student.py
from odoo import models, fields, api
from datetime import date


class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birth_date = fields.Date(string='Birth Date')
    age = fields.Integer(string='Age', compute='_compute_age', store=True)
    final_exam_grade = fields.Float(string='Final Exam Grade')
    subject_ids = fields.Many2many('school.subject', string='Subjects')

    @api.depends('birth_date')
    def _compute_age(self):
        for student in self:
            if student.birth_date:
                today = date.today()
                student.age = today.year - student.birth_date.year
            else:
                student.age = 0
