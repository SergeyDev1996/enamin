from odoo import models, fields


class HREmployee(models.Model):
    _inherit = "hr.employee"

    booking = fields.Boolean(string="Бронювання")
    mobilized = fields.Boolean(string="Мобілізований")
    tck_sp_id = fields.Many2one("tck.sp", string="ТЦК та СП")
    edrpvr_number = fields.Char(string="№ в ЄДРПВР")
