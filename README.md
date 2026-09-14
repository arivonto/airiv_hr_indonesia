# AIRIV HR Indonesia - UU Cipta Kerja & Ketenagakerjaan

Manajemen Ketenagakerjaan Sesuai UU Cipta Kerja

## Odoo Apps Store

This repository contains the Odoo 18 module package for `airiv_hr_indonesia`.

Required store assets are maintained in:

```text
airiv_hr_indonesia/static/description/
  icon.png
  banner.png
  index.html
```

## Technical

- Odoo version: `18.0.1.0.0`
- License: `LGPL-3`
- Author: `AIRIV`
- Website: `https://airiv.id`

## Quality Gate

GitHub Actions runs the AIRIV Odoo Apps Store CI audit on branch `18.0`.

## Core Capabilities & Architecture

- Employee identity, employment status, department, position, contract, and manager context.
- Attendance, leave requests, approvals, and workforce availability operations.
- Structured employee and work-activity context for payroll-ready review.

The module connects people and organization records to an AIRIV workforce operations and payroll handoff layer.

## Feature & Workflow Automation

1. Configure departments, positions, locations, managers, and policies.
2. Register employees, contracts, identity details, and lifecycle status.
3. Record attendance, submit leave, and process approvals.
4. Validate HR records before payroll handoff.

## Installation Guidance

Clone branch `18.0` into the Odoo addons path, restart Odoo, update the Apps list, and install the module. Configure organization and HR policies before use.

## Configuration Checklist

- Verify employee identity, employment status, contract, and manager.
- Confirm department, position, location, and approval responsibility.
- Review attendance and approved leave before payroll handoff.
- Restrict sensitive employee data to authorized HR roles.

## Repository Layout

```text
airiv_hr_indonesia/
  models/                 Employee and HR domain models
  views/                  HR operations and menus
  security/               Access rules and groups
  static/description/     Apps Store assets
  __manifest__.py         Odoo metadata
```

## Contact Info

- Author: AIRIV
- Website: https://airiv.id
- GitHub: https://github.com/arivonto
- Repository: https://github.com/arivonto/airiv_hr_indonesia
- Odoo series: `18.0`
