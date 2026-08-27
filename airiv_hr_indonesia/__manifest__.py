# -*- coding: utf-8 -*-
{
    'name': 'Indonesia HR Geofencing Attendance & Depnaker Overtime Engine',
    'version': '18.0.1.0.0',
    'category': 'Human Resources/Attendances',
    'summary': 'GPS Geofencing Mobile Clock-In, Depnaker Overtime (Kemnaker 1/173 Formula), and PPh 21 TER Payroll Feeder for Odoo 18',
    'description': """
Comprehensive Indonesian HR Attendance & Statutory Overtime Suite for Odoo 18 Community Edition.
Compliant with Indonesian Ministry of Manpower (Kemnaker) PP No. 35/2021 & UU Cipta Kerja.

Core Capabilities:
1. Workplace Geofencing & GPS Mobile Attendance:
   - Branch office, clinic, and warehouse GPS radius definition (Haversine distance calculation)
   - Real-time coordinate validation and geofence breach tagging (Valid / Out of Bounds)
2. Depnaker Statutory Overtime Engine (Perhitungan Lembur Kemnaker):
   - Standard Hourly Rate calculation based on statutory 1/173 formula (Gaji Pokok + Tunjangan Tetap)
   - Workday Overtime: 1.5x for the 1st hour, 2.0x for subsequent hours
   - Weekend / National Holiday Overtime: 2.0x for hours 1-8, 3.0x for the 9th hour, 4.0x thereafter
   - Automated approval and overtime compensation calculation
3. Direct PPh 21 TER Payroll Integration:
   - Feeds approved overtime pay and attendance deductions into airiv_payroll_indonesia payslips
4. Zero External Server Overhead - 100% Odoo 18 Community Native - Always Free ($0.00).
""",
    'author': 'Riv Cloud Management',
    'website': 'https://airiv.id',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'base',
        'hr',
        'hr_attendance',
        'airiv_payroll_indonesia'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_workplace_zone_views.xml',
        'views/hr_attendance_views.xml',
        'views/hr_overtime_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_indonesia_menu_views.xml',
    ],
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
