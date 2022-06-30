# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountBankStatement(models.Model):
    _inherit = "account.bank.statement"

    need_validation = fields.Boolean(
        "Nécessite une validation", default=False, tracking=True, copy=False
    )

    def action_need_validation(self):
        for rec in self:
            rec.need_validation = True

    def button_validate_or_action(self):

        res = super(AccountBankStatement, self).button_validate_or_action()

        for rec in self:
            rec.need_validation = False
        return res

    def button_reopen(self):
        super(AccountBankStatement, self).button_reopen()
        for rec in self:
            rec.need_validation = False

    @api.model_create_multi
    def create(self, values):
        res = super(AccountBankStatement, self).create(values)
        validators = (
            self.env.ref("s2pc_account.group_confirm_payment")
            .mapped("users")
            .filtered(lambda user: user != self.env.user)
            .mapped("partner_id")
        )
        res.message_subscribe(partner_ids=validators.ids)
        return res
