from odoo import api, fields, models
from datetime import datetime


class HospitalCita(models.Model):
    _name = 'hospital.cita'
    _description = "Cita"

    name = fields.Char(string='Nro Cita', default='/')
    activo = fields.Boolean(string='Activo', default=True)
    fecha = fields.Date(string='Fecha Cita', default=datetime.now())
    descripcion = fields.Text(string="Descripcion")

    doctor_id = fields.Many2one('hospital.doctor', 'Doctor')
    paciente_id = fields.Many2one('hospital.paciente', 'Paciente')
    id_hospital = fields.Many2one('hospital.hospital', "Hospital")


class HospitalCitaReporte(models.Model):
    _name = 'hospital.cita.reporte'
    _description = "Reporte de Cita"

    name = fields.Char(string='Nro Cita', default='/')
    descripcion = fields.Text(string="Descripcion")
    doctor_id = fields.Many2one('hospital.doctor', 'Doctor')
    paciente_id = fields.Many2one('hospital.paciente', 'Paciente')
