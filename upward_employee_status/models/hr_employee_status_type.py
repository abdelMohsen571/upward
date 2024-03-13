from odoo import models, fields, api
from datetime import date, datetime, timedelta


class HrEmployeeStatusType(models.Model):
    _name = 'hr.employee.status.type'
    _description = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name = fields.Char(string='Name', required=True,tracking=True)
