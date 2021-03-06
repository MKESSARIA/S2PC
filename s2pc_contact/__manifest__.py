# -*- coding: utf-8 -*-
{
    'name': "s2pc_contact",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Valisoa RAMILIJAONA",
    'website': "https://www.valisoaramilijaona.ml",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'sale'],

    # always loaded
    'data': [
        'views/res_partner.xml',
        'views/templates.xml',
    ],

    'assets': {
        'web.assets_backend': [
            "s2pc_contact/static/src/scss/theme.scss",
        ],
    },
    'images': [
        'static/img/background.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
