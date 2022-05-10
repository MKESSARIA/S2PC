# -*- coding: utf-8 -*-
from odoo import api, models, fields, _
from odoo.addons.s2pc_base.models.tools import amount_to_text_fr


class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_total_text = fields.Char('Amount total text', compute='compute_amount_to_text')

    def compute_amount_to_text(self):
        for rec in self:
            rec.amount_total_text = amount_to_text_fr(rec.amount_total, rec.currency_id.currency_unit_label)

    def get_lot_number(self, name, product_id):
        """
            get LOT id
        """
        id_bl = []
        lot = ""

        bc = self.env['sale.order'].search([('name', '=', name)])
        pc = self.env['pos.order'].search([('name', '=', name)])

        if bc[0]:
            bl = self.env['stock.picking'].search([('origin', '=', bc.name)])
        else:
            bl = self.env['stock.picking'].search([('origin', '=', pc.name)])

        for i in bl:
            id_bl.append(i)
        if id_bl[0]:
            for line in id_bl[0].move_ids_without_package:
                if line.product_id == product_id:
                    lot = line.lot_ids[0].name
        else:
            lot = ""

        return lot


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    weight = fields.Float('Total weight', compute='compute_weight')

    def compute_weight(self):
        for rec in self:
            rec.weight = rec.product_id.weight or 0 * rec.quantity
