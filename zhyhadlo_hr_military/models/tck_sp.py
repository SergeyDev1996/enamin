from odoo import models, fields


class TckSp(models.Model):
    _name = "tck.sp"
    _description = "TCK and SP"

    name = fields.Char(string="ТЦК та СП", required=True)
    code = fields.Char(string="Код")
    phone = fields.Char(string="Телефон")
