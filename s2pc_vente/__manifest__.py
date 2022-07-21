# -*- coding: utf-8 -*-
{
    'name': "s2pc_vente",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['s2pc_base', 's2pc_product', 'base', 'sale', 'sales_team'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hide_report.xml',
        'views/pro_format_report.xml',
        'views/view_order_form_inherit.xml',
        'views/company_external_layout.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
