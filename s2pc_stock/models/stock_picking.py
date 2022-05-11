# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
	_inherit = 'stock.picking'

	need_validation = fields.Boolean('Need validation', default=False, tracking=True, copy=False)

	def action_need_validation(self):
		for rec in self:
			rec.need_validation = True

	def action_done(self):
		super(StockPicking, self).action_done()
		for rec in self:
			if rec.state == 'done':
				rec.need_validation = False

	def action_cancel(self):
		res = super(StockPicking, self).action_cancel()
		for rec in self:
			if rec.state == 'canceled':
				rec.need_validation = False
		return res

	@api.depends('state')
	def _compute_show_validate(self):
		super(StockPicking, self)._compute_show_validate()
		for picking in self:
			if not self.env.user.has_group('s2pc_stock.group_confirm_picking') and picking.picking_type_code in ['internal', 'incoming'] and picking.state == 'assigned':
				picking.show_validate = False

	@api.model
	def get_moves_report_values(self):
		result = {}
		for move in self.move_ids_without_package:
			result[move] = {}
			if move.picking_code == 'incoming' and move.purchase_line_id:
				result[move]['price_unit'] = move.purchase_line_id.price_unit
				result[move]['price_subtotal'] = move.purchase_line_id.price_subtotal
			elif move.picking_code == 'outgoing' and move.sale_line_id:
				result[move]['price_unit'] = move.sale_line_id.price_unit
				result[move]['price_subtotal'] = move.sale_line_id.price_subtotal
			elif move.price_unit:
				result[move]['price_unit'] = move.price_unit
				result[move]['price_subtotal'] = move.price_unit * move.product_uom_qty
			else:
				result[move]['price_unit'] = 0
				result[move]['price_subtotal'] = 0
			result[move]['package_count'] = len(list(set(move.move_line_ids.mapped('result_package_id'))))
			result[move]['weight'] = move.product_id.weight
			total_amount = 0
		total_package_count = 0
		total_weight = 0
		for key in result.keys():
			total_amount += result[key]['price_subtotal']
			total_package_count += result[key]['package_count']
			total_weight += result[key]['weight']
		result['total_amount'] = total_amount
		result['total_package_count'] = total_package_count or ''
		result['total_weight'] = total_weight or ''
		return result

	@api.model
	def get_parent_partner(self):
		if self.partner_id.parent_id:
			return self.partner_id.parent_id
		return self.partner_id




