# -*- coding: utf-8 -*-
{
    "name": "s2pc_account",
    "summary": """ S2PC Account""",
    "description": """
    """,
    "author": "Alpha conseils",
    "website": "https://www.alphamada.com/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Uncategorized",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": [
        "s2pc_base",
        "s2pc_contact",
        "s2pc_product",
        "account",
        "stock_picking_invoice_link",
    ],
    # always loaded
    "data": [
        # security
        "security/res_groups.xml",
        # views
        "views/res_partner_views.xml",
        "views/report_invoice.xml",
        "views/account_move_views.xml",
        "views/account_bank_statement_views.xml",
        "views/account_move_invoice_report.xml",
    ],
    # only loaded in demonstration mode
    "demo": [],
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
    "assets": {
        "web.report_assets_common": [
            "s2pc_account/static/src/css/account_move_invoice_report.css",
        ],
    },
}
