# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncannycs LLP
#    Copyright (C) 2022 Uncannycs LLP (<http://uncannycs.com>).
#
##############################################################################
{
    'name': "POS LOT Selection",
    'summary': """
        Select lots and choose qty from multiple lots, show expiry date""",
    'description': """
        Select lots and choose qty from multiple lots, show expiry date
    """,
    'license': 'Other proprietary',
    'author': 'Uncanny Consulting Services LLP',
    'maintainer': 'Uncanny Consulting Services LLP',
    'website': "http://www.uncannycs.com",
    'category': 'Sales/Point of Sale',
    'version': '15.0.0.0.0',
    'depends': ['point_of_sale','product_expiry'],
    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'pos_lot_selection_ucs/static/src/js/models.js',
            'pos_lot_selection_ucs/static/src/js/EditListPopup.js',
            'pos_lot_selection_ucs/static/src/js/ProductScreen.js',
            'pos_lot_selection_ucs/static/src/js/Orderline.js',
        ],
        'web.assets_qweb': [
            'pos_lot_selection_ucs/static/src/xml/EditListPopup.xml',
        ],
    },
    'images': ['static/description/banner.gif'],
    'support': 'support@uncannycs.com',
    'installable': True,
    'application': True,
    'auto_install': False,
    'demo': [
    ],
    'price': 30,
    'currency': 'USD',
}
