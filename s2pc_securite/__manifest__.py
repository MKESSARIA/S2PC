# -*- coding: utf-8 -*-
{
    'name': "s2pc_securite",

    'summary': """For security purpose and menu access""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Valisoa RAMILIJAONA",
    'website': "http://www.alphamada.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 's2pc_base', 's2pc_product', 'sale', 'sales_team', 'hr', 'purchase', 'mass_mailing',
                'maintenance', 'hr_appraisal', 'stock', "account", 'mrp', 'point_of_sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/res_groups.xml',
        'views/menu_access.xml',
        'views/model_access.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
