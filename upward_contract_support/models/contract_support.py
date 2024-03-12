from odoo import models, fields,api
from datetime import date, datetime, timedelta

class ContractSupport(models.Model):
    _name = 'contract.support'
    _description = 'upward_contract_support'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    state = fields.Selection([('draft', 'Draft'),
                              ('progress', 'In Progress'),
                              ('cancel', 'Canceled ')], default='draft', tracking=True)
    date_to = fields.Date(string='Date To',default=date.today(), tracking=True)
    date_from = fields.Date(string='Date From', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Partner', tracking=True)
    contract_id = fields.Many2one('hr.contract', string='Contract', tracking=True)

    def action_progress(self):
        for rec in self:
            rec.state = 'progress'


    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'
    @api.onchange('date_to')
    def cancel_contract(self):
        for rec in self:
            state=rec.state
            if rec.date_to > fields.Date.today():
                rec.state = 'cancel'
            else:
                rec.state=state
    def _test_cron(self):
        for rec  in self:
            print('fsad;jf;adsj')

