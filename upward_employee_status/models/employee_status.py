from odoo import models, fields, api
from datetime import date, datetime, timedelta


class upward_sale_support(models.Model):
    _name = 'employee.status'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name',required=True,tracking=True)
    description = fields.Text(string='Description')
    employee_id=fields.Many2one('hr.employee','Employee',tracking=True)
    status_id=fields.Many2one('hr.employee.status.type','Status',tracking=True)
    start_date = fields.Date(string='Start Date',default=date.today(), tracking=True)
    end_date = fields.Date(string='End Date', tracking=True,)

