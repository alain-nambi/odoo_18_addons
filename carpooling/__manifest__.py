# -*- coding: utf-8 -*-

{
    'name': 'Carpooling Apps',
    'version': '1.0',
    'author': 'Alain Nambii',
    'description': 
    """
        Helps you to find a carpooling partner
    """,
    'depends': ['base', 'mail'],
    'category': 'Custom Tools',
    'license': 'LGPL-3',
    'data': [
        'security/groups.xml',
        'security/access_carpooling_manager.xml',
        'security/ir.rule.xml',
        'views/carpooling_views.xml',
        'wizard/carpooling_wizard_views.xml',
        'views/carpooling_menus.xml',
        'views/res_partner_views.xml',
        'views/website_template.xml',
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'report/car_report.xml'
    ]
}