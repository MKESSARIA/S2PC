# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.addons.s2pc_base.models.tools import amount_to_text_fr
from collections import defaultdict


class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_total_text = fields.Char('Amount total text', compute='compute_amount_to_text')

    def compute_amount_to_text(self):
        for rec in self:
            rec.amount_total_text = amount_to_text_fr(rec.amount_total, rec.currency_id.currency_unit_label)

    def get_lot_number(self, name_origin, product_id_origin):
        """
            get LOT id
        """
        id_bl = []
        lot = ""

        bc = self.env['sale.order'].search([('name', '=', name_origin)])
        pc = self.env['pos.order'].search([('name', '=', name_origin)])

        if len(bc) > 0:
            bl = self.env['stock.picking'].search([('origin', '=', bc.name)])
        else:
            bl = self.env['stock.picking'].search([('origin', '=', pc.name)])

        for i in bl:
            id_bl.append(i)
        if len(id_bl):
            for line in id_bl[0].move_ids_without_package:
                if line.product_id == product_id_origin:
                    lot = line.lot_ids[0].name
        else:
            lot = ""

        return lot

    # @api.onchange("ville")
    # def get_lot_pos(self):
    #     if self.pos_order_ids:
    #         print(self.pos_order_ids[0].lines[0].pack_lot_ids[0].lot_name)


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    weight = fields.Float('Total weight', compute='compute_weight')

    def compute_weight(self):
        for rec in self:
            rec.weight = rec.product_id.weight or 0 * rec.quantity

    prod_lot_ids = fields.Many2many(
        comodel_name="stock.production.lot",
        compute="_compute_prod_lots",
        string="Production Lots",
    )

    @api.depends("move_line_ids")
    def _compute_prod_lots(self):
        for line in self:
            line.prod_lot_ids = line.mapped("move_line_ids.move_line_ids.lot_id")

    def lots_grouped_by_quantity(self):
        lot_dict = defaultdict(float)
        for sml in self.mapped("move_line_ids.move_line_ids"):
            if sml.lot_id:
                lot_dict[sml.lot_id.name] += sml.qty_done
        return lot_dict


