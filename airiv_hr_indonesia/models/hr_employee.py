# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrEmployeeOvertime(models.Model):
    _inherit = 'hr.employee'

    workplace_zone_id = fields.Many2one('hr.workplace.zone', string="Zona Lokasi Kerja Utama")
    basic_salary = fields.Float(string="Gaji Pokok + Tunjangan Tetap (Rp)", default=5000000.0,
                                help="Dasar perhitungan upah lemur standar Depnaker (PP 35/2021)")
    depnaker_hourly_rate = fields.Float(string="Upah Sejam Depnaker (1/173)", compute="_compute_depnaker_hourly_rate", store=True)
    overtime_ids = fields.One2many('hr.overtime.indonesia', 'employee_id', string="Riwayat Lembur")
    total_overtime = fields.Float(string="Total Jam Lembur", compute="_compute_total_overtime", store=True)

    @api.depends('basic_salary')
    def _compute_depnaker_hourly_rate(self):
        for emp in self:
            # Standar UU Ketenagakerjaan: Upah Sejam = 1/173 x Upah Sebulan
            if emp.basic_salary > 0:
                emp.depnaker_hourly_rate = round(emp.basic_salary / 173.0, 2)
            else:
                emp.depnaker_hourly_rate = 0.0

    @api.depends('overtime_ids.duration', 'overtime_ids.duration_hours', 'overtime_ids.state')
    def _compute_total_overtime(self):
        for emp in self:
            approved_records = emp.overtime_ids.filtered(lambda r: r.state == 'approved')
            emp.total_overtime = sum(approved_records.mapped('duration_hours'))
