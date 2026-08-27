# -*- coding: utf-8 -*-
import math
from odoo import models, fields, api, _

class HrWorkplaceZone(models.Model):
    _name = 'hr.workplace.zone'
    _description = 'Zona Geofencing Lokasi Kerja (GPS)'
    _order = 'name asc'

    name = fields.Char(string="Nama Lokasi / Kantor / Cabang", required=True, default="Kantor Pusat")
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)
    
    latitude = fields.Float(string="Garis Lintang (Latitude)", digits=(10, 7), required=True, default=-6.2000000)
    longitude = fields.Float(string="Garis Bujur (Longitude)", digits=(10, 7), required=True, default=106.8166667)
    allowed_radius_meters = fields.Integer(string="Radius Maksimal (Meter)", default=100, required=True,
                                           help="Jarak maksimal toleransi absensi dari titik pusat")
    active = fields.Boolean(string="Aktif", default=True)

    def calculate_distance_meters(self, user_lat, user_lon):
        self.ensure_one()
        # Haversine Formula for exact geodesic distance
        r = 6371000.0  # Earth radius in meters
        phi1 = math.radians(self.latitude)
        phi2 = math.radians(user_lat)
        delta_phi = math.radians(user_lat - self.latitude)
        delta_lambda = math.radians(user_lon - self.longitude)

        a = (math.sin(delta_phi / 2.0) ** 2 +
             math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2.0) ** 2))
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(r * c, 2)
