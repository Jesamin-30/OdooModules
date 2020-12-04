from odoo import api, fields, models


class HospitalHospital(models.Model):
    _name = "hospital.hospital"
    _description = "Hospital"
    
    name = fields.Char(required=True)
    descripcion = fields.Text('Descripcion')
