# -*- coding: utf-8 -*-

from openerp import models, fields, api
from openerp import exceptions

class sparkit_budget_xchange_rate_wizard(models.TransientModel):
    _name = 'sparkit.budget_xchange_rate_wizard'

    project_ids = fields.Many2many('sparkit.sparkproject', string="Community Budgets")
    amount = fields.Float(string="Updated Exchange Rate Amount")

    @api.multi
    def do_mass_update(self):
        self.ensure_one()
        # else:
        self.project_ids.write({'exchange_rate': self.amount})
        return True

    @api.multi
    def do_reopen_form(self):
        self.ensure_one()
        return {'type': 'ir.actions.act_window',
                'res_model': self._name, # this model
                'res_id': self.id,  # the current wizard record
                'view_type': 'form',
                'view_mode': 'form',
                'target': 'new'}
