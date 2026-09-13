# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class HrWorkplaceZone(models.Model):
    _name = 'hr.workplace.zone'
    _description = 'Zona Lokasi Kerja / Geofence'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Nama Zona", required=True, tracking=True)
    code = fields.Char(string="Kode Zona", tracking=True, index=True)
    latitude = fields.Float(string="Latitude", digits=(10, 7), tracking=True)
    longitude = fields.Float(string="Longitude", digits=(10, 7), tracking=True)
    radius_meters = fields.Float(string="Radius Geofence (Meter)", default=100.0, tracking=True)
    active = fields.Boolean(string="Aktif", default=True, tracking=True)
    company_id = fields.Many2one('res.company', string="Perusahaan", default=lambda self: self.env.company, required=True)
