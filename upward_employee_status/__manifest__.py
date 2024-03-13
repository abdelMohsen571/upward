# -*- coding: utf-8 -*-
{
    'name': "upward_employee_status",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/employee_status_view.xml',
        'reports/employee_status_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
}

