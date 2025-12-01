from odoo import fields, models


class HrEmployeePPE(models.Model):
    _name = "hr.employee.ppe"
    _description = "Employee Personal Protective Equipment"
    _order = "assign_date desc, employee_id"

    name = fields.Char(string="Description", required=True)
    employee_id = fields.Many2one(
        comodel_name="hr.employee",
        string="Employee",
        required=True,
        ondelete="cascade",
    )
    product_id = fields.Many2one(
        comodel_name="product.product",
        string="Equipment",
        required=True,
        domain=[("type", "=", "product")],
    )
    quantity = fields.Float(string="Quantity", default=1.0)
    assign_date = fields.Date(string="Assigned On", default=fields.Date.context_today)
    company_id = fields.Many2one(
        comodel_name="res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
    )
    active = fields.Boolean(default=True)

    def name_get(self):
        result = []
        for record in self:
            name = record.name or record.product_id.display_name
            if record.employee_id:
                name = f"{name} - {record.employee_id.name}"
            result.append((record.id, name))
        return result

    def action_view_product(self):
        self.ensure_one()
        return {
            "name": self.product_id.display_name,
            "type": "ir.actions.act_window",
            "res_model": "product.product",
            "view_mode": "form",
            "target": "current",
            "res_id": self.product_id.id,
        }


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    ppe_ids = fields.One2many(
        comodel_name="hr.employee.ppe",
        inverse_name="employee_id",
        string="PPE Items",
    )
