# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrOvertimeIndonesia(models.Model):
    _name = 'hr.overtime.indonesia'
    _description = 'Pengajuan & Perhitungan Lembur Standar Kemnaker'
    _order = 'date desc, id desc'

    name = fields.Char(string="Nomor SPKL", required=True, copy=False, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string="Karyawan", required=True)
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company)
    
    date = fields.Date(string="Tanggal Lembur", default=fields.Date.today, required=True)
    overtime_type = fields.Selection([
        ('workday', 'Hari Kerja Biasa'),
        ('holiday', 'Hari Istirahat Mingguan / Libur Resmi'),
    ], string="Jenis Hari Lembur", default='workday', required=True)

    duration_hours = fields.Float(string="Durasi Lembur (Jam)", required=True, default=2.0)
    duration = fields.Float(string="Durasi (Jam)", related='duration_hours', readonly=False, store=True)
    
    hourly_rate = fields.Float(string="Upah Lembur per Jam (1/173)", related='employee_id.depnaker_hourly_rate', readonly=True)
    overtime_multiplier_hours = fields.Float(string="Bobot Jam Lembur Depnaker", compute="_compute_overtime_pay", store=True)
    total_overtime_pay = fields.Float(string="Total Upah Lembur (Rp)", compute="_compute_overtime_pay", store=True)
    
    reason = fields.Text(string="Uraian Pekerjaan / Alasan Lembur", required=True)
    state = fields.Selection([
        ('draft', 'Pengajuan (Draft)'),
        ('approved', 'Disetujui Manajer'),
        ('paid', 'Dibayarkan via Payroll'),
        ('rejected', 'Ditolak'),
    ], string="Status SPKL", default='draft', required=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hr.overtime.indonesia') or f"SPKL-{fields.Date.today().strftime('%Y%m')}-0001"
        return super(HrOvertimeIndonesia, self).create(vals_list)

    @api.depends('duration_hours', 'duration', 'overtime_type', 'hourly_rate')
    def _compute_overtime_pay(self):
        for rec in self:
            hours = rec.duration_hours or rec.duration or 0.0
            mult_hours = 0.0

            if rec.overtime_type == 'workday':
                # Kemnaker Rule Hari Kerja: Jam pertama 1.5x, Jam berikutnya 2.0x
                if hours <= 1.0:
                    mult_hours = hours * 1.5
                else:
                    mult_hours = (1.0 * 1.5) + ((hours - 1.0) * 2.0)
            else:
                # Kemnaker Rule Hari Libur: Jam 1-8 x 2.0, Jam 9 x 3.0, Jam 10+ x 4.0
                if hours <= 8.0:
                    mult_hours = hours * 2.0
                elif hours <= 9.0:
                    mult_hours = (8.0 * 2.0) + ((hours - 8.0) * 3.0)
                else:
                    mult_hours = (8.0 * 2.0) + (1.0 * 3.0) + ((hours - 9.0) * 4.0)

            rec.overtime_multiplier_hours = round(mult_hours, 2)
            rec.total_overtime_pay = round(mult_hours * rec.hourly_rate, 2)

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'rejected'})
