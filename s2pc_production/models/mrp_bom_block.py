from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ModelName(models.Model):
    _inherit = 'mrp.bom'
    product_qty = fields.Float(
        'Quantity', default=100,
        digits='Unit of Measure', required=True)

    @api.constrains('bom_line_ids')
    def block_bom(self):
        for rec in self:
            total = 0
            for qtt in rec.bom_line_ids:
                total = total + qtt.product_qty
            if not total == 100:
                raise ValidationError(_("La somme des quantités des produits doit être à 100 au lieu de {}").format(
                    total))
        return True
