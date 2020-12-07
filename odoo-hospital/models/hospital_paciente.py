from odoo import api, fields, models


class HospitalPaciente(models.Model):
    _name = 'hospital.paciente'
    _description = "Paciente"

    name = fields.Char(string="Nombre y Apellido")
    genero = fields.Selection(
        [('femenino', 'Femenino'), ('masculino', 'Masculino')], string="Género")
    id_hospital = fields.Many2one('hospital.hospital', "Hospital")
    sintomas = fields.Text(string="Síntomas")
