# -*- coding: utf-8 -*-
{
    'name': 'AIRIV HR Indonesia - UU Cipta Kerja & Ketenagakerjaan',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Localizations',
    'summary': 'Manajemen Ketenagakerjaan Sesuai UU Cipta Kerja',
    'description': 'Modul Sumber Daya Manusia dan Ketenagakerjaan Indonesia.',
    'author': 'AIRIV',
    'website': 'https://airiv.id',
    'url': 'https://github.com/arivonto/airiv_hr_indonesia/blob/18.0/static/description/index.html',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'hr',
        'hr_attendance',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
