from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.onchange('product_template_id')
    def _onchange_product_id(self):
        for record in self:
            a = 1