# -*- coding: utf-8 -*-
{
    'name': "s2pc_employe",

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
    'depends': ['base', 'hr_contract',
                'hr',
                'hr_holidays',
                's2pc_base'],

    # always loaded
    'data': [
        # report

        # security
        'security/ir.model.access.csv',
        'security/res_groups.xml',

        # views
        'views/hr_leave_team_views.xml',

        'views/menu_views.xml',
        'views/hr_employee_views_val_inherit.xml',

        'views/hr_employee.xml',
        'views/hr_contract_view.xml',
    ],
    'assets': {
        'web._assets_primary_variables': [

        ],
        'web.assets_backend': [
            's2pc_employe/static/src/js/gantt_model.js',
            's2pc_employe/static/src/js/gantt_view.js',
        ],
        'web.assets_frontend': [

        ],
        'web.assets_tests': [

        ],
        'web.qunit_suite_tests': [

        ],
        'web.assets_qweb': [

        ],
    },
    # only loaded in demonstration mode
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
