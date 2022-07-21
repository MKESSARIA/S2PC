from odoo import fields, models, _, api


class TypeHsAlpha(models.Model):
    _name = "type.hs"

    name = fields.Char()
