# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    workplace_zone_id = fields.Char(string="Zona Lokasi Kerja / Geofence", tracking=True)
    check_in_distance = fields.Float(string="Jarak Check-in (Meter)", default=0.0, tracking=True)
    check_out_distance = fields.Float(string="Jarak Check-out (Meter)", default=0.0, tracking=True)
    
    overtime_status = fields.Selection(
        selection_add=[
            ('pending', 'Menunggu Persetujuan Lembur'),
            ('approved', 'Lembur Disetujui'),
            ('refused', 'Lembur Ditolak'),
        ],
        ondelete={
            'pending': 'set null',
            'approved': 'set null',
            'refused': 'set null',
        },
        string="Status Lembur",
        tracking=True,
    )

    def action_approve_overtime(self):
        self.write({'overtime_status': 'approved'})

    def action_refuse_overtime(self):
        self.write({'overtime_status': 'refused'})
