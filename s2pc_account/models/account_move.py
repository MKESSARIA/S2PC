# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    advised_pricelist_id = fields.Many2one(
        "product.pricelist", "Advised pricelist", compute="_compute_advised_pricelist"
    )
    reglement_mode = fields.Selection(
        string="Mode de règlement",
        selection=[
            ("bnq", "BNQ"),
            ("esp", "ESP"),
            ("chk", "CHQ"),
        ],
        default="esp",
    )

    ville = fields.Selection(
        [
            ("tana", "Tananarive"),
            ("tamatave", "Tamatave"),
        ],
        string="La ville de facturation",
        help="Pour mieux faire les recherches il faut  completér ce champs Ville.",
        # readonly=False,
        # compute="_compute_ville"
    )

    # def _compute_ville(self):
    #     for record in self:
    #         if self.env.user.has_group('s2pc_securite.group_s2pc_antananarivo') and self.env.user.has_group('s2pc_securite.group_s2pc_tamatave'):
    #             record.ville = None
    #         elif self.env.user.has_group('s2pc_securite.group_s2pc_antananarivo'):
    #             record.ville = "tana"
    #         elif self.env.user.has_group('s2pc_securite.group_s2pc_tamatave'):
    #             record.ville = "tamatave"
    #         else:
    #             record.ville = None

    def _compute_advised_pricelist(self):
        for rec in self:
            partner = rec.partner_id
            parent = partner.parent_id
            pricelist = partner.advised_pricelist_id or parent.advised_pricelist_id
            if pricelist:
                rec.advised_pricelist_id = pricelist.id
            else:
                rec.advised_pricelist_id = False


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    advised_price_unit = fields.Monetary(
        "Advised price unit", compute="_compute_advised_price_unit"
    )
    advised_ratio = fields.Float(
        "Advised price ratio", compute="_compute_advised_ratio"
    )

    def _compute_advised_price_unit(self):
        for rec in self:
            advised_pricelist = rec.move_id.advised_pricelist_id
            if advised_pricelist:
                rec.advised_price_unit = advised_pricelist.price_get(
                    rec.product_id.id, rec.quantity
                ).get(advised_pricelist.id)
            else:
                rec.advised_price_unit = 0

    def _compute_advised_ratio(self):
        for rec in self:
            if rec.price_unit and rec.advised_price_unit:
                rec.advised_ratio = (
                        (rec.advised_price_unit - rec.price_unit)
                        * 100
                        / rec.advised_price_unit
                )
            else:
                rec.advised_ratio = 0
