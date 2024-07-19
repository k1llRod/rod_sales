from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    readonly_user = fields.Boolean(string='Readonly User', store=True, compute='_compute_readonly_user')

    @api.depends('partner_id', 'create_uid')
    def _compute_readonly_user(self):
        for record in self:
            record.readonly_user = record.create_uid.has_group("rod_sales.group_cost_readonly")
