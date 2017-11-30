# -*- coding: utf-8 -*-
{
    'name': "Sparkit Finance Exchange Rate Updates Module",

    'summary': """
        Updates exchange rates and also community budget exchange rates.""",

    'description': """
        Two wizards: 1. update exchange rates listed under currency profiles,
        2. choose budget exchange rates to update with new rate.
    """,

    'author': "Spark MicroGrants",
    'website': "http://www.sparkmicrogrants.org",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sparkit'],

    # always loaded
    'data': [
        'views/cmty_budget_exchange_rate_wizard.xml',
    ],

}
