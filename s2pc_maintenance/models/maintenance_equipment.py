# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MaintenanceEquipmentInherited(models.Model):
    _inherit = 'maintenance.equipment'
    etalon = fields.Char(string="Etalon / Standard", index=1)
    internal_ref_equipment = fields.Char(string="Référence interne de l'équipement")
