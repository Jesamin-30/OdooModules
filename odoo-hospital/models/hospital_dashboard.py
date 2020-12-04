from odoo import api, fields, models


class HospitalDashboard(models.Model):
    _name = "hospital.dashboard"
    _description = "Dashboard"

    name = fields.Char(required=True)
    model = fields.Char()
    tipo = fields.Char()
    total = fields.Integer(compute='_generate_count')

    def _generate_count(self):
        for record in self:
            model = record.model
            if model:
                count = self.env[str(model)].search_count([('id_hospital', '!=', False)])
                record.total = count
            else:
                record.total = 0