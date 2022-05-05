from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ModelName(models.Model):
    _inherit = 'mrp.bom'
    product_qty = fields.Float(
        'Quantity', default=100, required=True)

    @api.constrains('bom_line_ids')
    def block_bom(self):
        for rec in self:
            list_qtt = [0]
            for qtt in rec.bom_line_ids:
                qtt_round = round(qtt.product_qty, 4)
                list_qtt.append(qtt_round)
            total = sum(list_qtt)
            if total not in [0, 100]:
                raise ValidationError(_("La somme des quantités des produits doit être à 100 au lieu de {}").format(
                    total))
        return True
