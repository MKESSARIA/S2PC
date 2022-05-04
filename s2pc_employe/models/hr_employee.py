# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    cnaps_number = fields.Char('Numero CNAPS', store=1)
    team_employee_ids = fields.Many2many('hr.employee', 'hr_employee_team_rel', 'manager_id', 'employee_id', 'Team')
    langue = fields.Selection(
        [('english', 'Anglais'),
         ('french', 'Français'),
         ('malgace', 'Malagasy')],
        'Langue')
    partner_name = fields.Char('Epoux/Epouse', store=1)
    tutor = fields.Char('Tuteur/Tutrice', store=1)
    father_name = fields.Char('Nom du père', store=1)
    mother_name = fields.Char('Nom de la mère', store=1)
    partner_name_urgence_contact = fields.Char('Téléphone Epoux/Epouse', store=1)
    tutor_urgence_contact = fields.Char('Téléphone Tuteur/Tutrice', store=1)
    parent_urgence_contact = fields.Char('Téléphone Parent', store=1)
    child_urgence_contact = fields.Char('Téléphone Enfant', store=1)
    children_ids = fields.One2many('hr.child', 'employe_id', string="Enfants à charge", store=1)
    certificate_level = fields.Selection([
        ('primaire', 'Etudes primaires'),
        ('secondaire', 'Etudes secondaires'),
        ('bachelier', 'Bachelier'),
        ('licence', 'Licence'),
        ('master', 'Master'),
        ('docteur', 'Doctorat'),
        ('professorat', 'Professorat'),
        ('other', 'Autre'),
    ], "Niveau d'études", default='other', groups="hr.group_hr_user", tracking=True)

    @api.depends('parent_id')
    def _compute_leave_manager(self):
        for employee in self:
            manager = employee.parent_id.user_id
            if manager:
                employee.leave_manager_id = manager
            else:
                employee.leave_manager_id = False


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'
    cnaps_number = fields.Char(readonly=True)
    langue = fields.Selection(
        [('english', 'Anglais'),
         ('french', 'Français'),
         ('malgace', 'Malagasy')],
        'Langue', readonly=True)
    partner_name = fields.Char(readonly=True)
    tutor = fields.Char(readonly=True)
    father_name = fields.Char(readonly=True)
    mother_name = fields.Char(readonly=True)
    partner_name_urgence_contact = fields.Char(readonly=True)
    tutor_urgence_contact = fields.Char(readonly=True)
    parent_urgence_contact = fields.Char(readonly=True)
    child_urgence_contact = fields.Char(readonly=True)
