from odoo import api, fields, models
from datetime import datetime


class HospitalCita(models.TransientModel):
    _name = 'hospital.cita.wizard'
    _description = "Cita Reporte Wizard"

    fecha_inicio = fields.Date(string='Fecha de Inicio', default=datetime.now())
    fecha_fin = fields.Date(string='Fecha de Fin', default=datetime.now())
    formato = fields.Selection(
        [('pdf', ('Pdf'))], string="Formato")
    id_hospital = fields.Many2one('hospital.hospital', "Hospital")

    def action_cita_reporte(self):
        domain = [
            ('fecha', '>', self.fecha_inicio),
            ('fecha', '<', self.fecha_fin),
            #('id_hospital', '=', self.id_hospital)
        ]

        cita_fields = [
            'name',
            'descripcion',
            'doctor_id',
            'paciente_id'
        ]

        records = self.env['hospital.cita'].search_read(domain, cita_fields)
        data = {
            'records': records,
            'fecha_inicio': self.fecha_inicio,
            'fecha_fin': self.fecha_fin,
            #'id_hospital': self.id_hospital,
        }
        return self.env.ref('odoo-hospital.hospitalCitaReporte').report_action(self, data=data)
