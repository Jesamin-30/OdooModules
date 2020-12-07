from odoo import api, fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = "Doctor"

    name = fields.Char(string="Nombre y Apellido")
    descripcion = fields.Text(string="Descripcion")
    id_hospital = fields.Many2one('hospital.hospital', "Hospital")
