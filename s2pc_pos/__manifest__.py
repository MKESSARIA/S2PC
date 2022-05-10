# -*- coding: utf-8 -*-
{
    'name': "s2pc_pos",

    'summary': """ S2PC Pos""",

    'description': """

	""",

    'author': "Alpha conseils",
    'website': "https://www.alphamada.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'point_of_sale',
        's2pc_base',
        's2pc_contact',
        's2pc_product',
        'sale_stock',
    ],

    # always loaded
    'data': [
        # security

        # views
        'views/account_invoice_pos_template.xml',
        'views/account_invoice_pos_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'point_of_sale.assets': [
            's2pc_pos/static/src/js/models.js',

        ],
        'web.report_assets_common': [
            's2pc_pos/static/src/css/account_invoice_pos.css',
        ],
    },
    'license': 'LGPL-3',
}
