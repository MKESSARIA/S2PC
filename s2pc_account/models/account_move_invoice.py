# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, _
from odoo.exceptions import UserError


class AccountInvoiceReport(models.AbstractModel):
    _name = "report.s2pc_account.temp"
    _description = "Invoice Report"

    @api.model
    def _get_report_values(self, docids, data=None):
        moves = self.env["account.move"].sudo().browse(docids)
        lines = moves.mapped("invoice_line_ids")
        range = len(lines) if len(lines) > 12 else 12

        return {
            "docs": moves,
            "line_range": range,
            "invoice_lines": lines,
            "invoice_count": len(lines),
            "qr_code_urls": self.env["report.account.report_invoice"]
            .sudo()
            ._get_report_values(docids)["qr_code_urls"],
        }
