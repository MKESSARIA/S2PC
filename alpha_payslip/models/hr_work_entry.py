from odoo import fields, models, _, api


class HrWorkEntryInherit(models.Model):
    _inherit = "hr.work.entry"

    type_hs_ids = fields.Many2many(
        comodel_name="type.hs",
        string=" Type heure supplémentaire",
    )
    is_hs = fields.Boolean(compute="_compute_is_hs", defualt=False)

    @api.onchange("work_entry_type_id")
    def _compute_is_hs(self):
        for rec in self:
            print(rec.work_entry_type_id)
            print(self.env.ref("alpha_payslip.hr_work_type_hs").id)
            if (
                rec.work_entry_type_id.id
                == self.env.ref("alpha_payslip.hr_work_type_hs").id
            ):
                rec.is_hs = True
            else:
                rec.is_hs = False
