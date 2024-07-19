from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    standard_price = fields.Float(string='Costo')

    @api.onchange('product_template_id')
    def _onchange_product_id(self):
        for record in self:
            record.standard_price = record.product_id.standard_price