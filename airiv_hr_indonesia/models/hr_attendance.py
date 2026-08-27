# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrAttendanceGeofence(models.Model):
    _inherit = 'hr.attendance'

    workplace_zone_id = fields.Many2one('hr.workplace.zone', string="Zona Lokasi Kerja")
    check_in_latitude = fields.Float(string="Check-in Latitude", digits=(10, 7))
    check_in_longitude = fields.Float(string="Check-in Longitude", digits=(10, 7))
    check_in_distance = fields.Float(string="Jarak ke Titik Pusat (m)", compute="_compute_geofence_status", store=True)
    
    is_within_geofence = fields.Boolean(string="Absensi Valid (Dalam Radius)", compute="_compute_geofence_status", store=True)
    geofence_status = fields.Selection([
        ('valid', 'Valid (Dalam Radius)'),
        ('out_of_bounds', 'Diluar Radius Kerja'),
        ('manual', 'Manual / Tanpa GPS'),
    ], string="Status Validitas Lokasi", compute="_compute_geofence_status", store=True)

    @api.depends('check_in_latitude', 'check_in_longitude', 'workplace_zone_id')
    def _compute_geofence_status(self):
        for rec in self:
            if rec.workplace_zone_id and rec.check_in_latitude and rec.check_in_longitude:
                dist = rec.workplace_zone_id.calculate_distance_meters(rec.check_in_latitude, rec.check_in_longitude)
                rec.check_in_distance = dist
                if dist <= rec.workplace_zone_id.allowed_radius_meters:
                    rec.is_within_geofence = True
                    rec.geofence_status = 'valid'
                else:
                    rec.is_within_geofence = False
                    rec.geofence_status = 'out_of_bounds'
            else:
                rec.check_in_distance = 0.0
                rec.is_within_geofence = True
                rec.geofence_status = 'manual'
