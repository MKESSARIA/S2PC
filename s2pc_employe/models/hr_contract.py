from odoo import fields, models, api


class HrContractInherit(models.Model):
    _inherit = "hr.contract"
    contrat_categorie = fields.Selection(
        [('cdi', 'CDI'),
         ('cdd', 'CDD'),
         ('stagiaire', 'Stagiaire')], string='Categorie de contrat', default="cdi",
        required=True, )
    hour_per_week = fields.Float(
        string="Nombre d'heures travaillé par semaine",
        required=True)
    base_salary = fields.Monetary('Salaire de base mensuel')
    hourly_salary = fields.Monetary('Salaire horaire ', compute='_get_hourly_salary')
    extra_hours = fields.Monetary('Rémunération des heures supplémentaires')
    allow_meal = fields.Monetary('Indemnité cantine')
    allow_transport = fields.Monetary('Indemnité transport')
    allow_houssing = fields.Monetary('Indemnité logement')

    @api.depends('hour_per_week')
    def _get_hourly_salary(self):
        for rec in self:
            if rec.hour_per_week:
                rec.hourly_salary = rec.base_salary / ((rec.hour_per_week * 40) / 12)
            else:
                rec.hourly_salary = 0
