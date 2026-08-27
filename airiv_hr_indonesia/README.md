# Indonesia HR Geofencing Attendance & Depnaker Overtime Engine

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo: 18.0 Community](https://img.shields.io/badge/Odoo-18.0%20Community-purple.svg)](https://www.odoo.com)
[![Price: Free ($0.00)](https://img.shields.io/badge/Price-%240.00%20(Free)-green.svg)](https://airiv.id)
[![Compliance: Kemnaker PP 35/2021](https://img.shields.io/badge/Compliance-Kemnaker%20PP%2035%2F2021-amber.svg)](https://airiv.id)

A specialized human resources and attendance extension for **Odoo 18.0 Community Edition**. Built for Indonesian enterprises, clinics, factories, retail outlets, and SMBs requiring **Mobile GPS Geofencing Attendance** and statutory **Depnaker Overtime (*Perhitungan Lembur Kemnaker*)** compliance according to **PP No. 35/2021 & UU Cipta Kerja**.

---

## Detailed Capabilities

### 1. Workplace GPS Geofencing Attendance
* **Multi-Branch Geofencing Zones**: Configure latitude, longitude, and custom tolerance radius (meters) for head offices, branch clinics, and warehouses.
* **Haversine Distance Verification**: Real-time geodesic distance calculation upon employee mobile check-in.
* **Geofence Status Tagging**: Automatically flags attendance records as `Valid (Dalam Radius)`, `Diluar Radius Kerja (Out of Bounds)`, or `Manual`.

### 2. Depnaker Statutory Overtime Engine (*Perhitungan Lembur Kemnaker*)
* **Statutory Hourly Rate (1/173 Formula)**:
  $$\text{Upah Sejam} = \frac{1}{173} \times (\text{Gaji Pokok} + \text{Tunjangan Tetap})$$
* **Workday Overtime Multiplier (*Hari Kerja*)**:
  * 1st Hour: $1.5\times$ hourly wage.
  * 2nd & Subsequent Hours: $2.0\times$ hourly wage.
* **Weekend & Holiday Overtime Multiplier (*Hari Istirahat / Libur Resmi*)**:
  * Hours 1 to 8: $2.0\times$ hourly wage.
  * 9th Hour: $3.0\times$ hourly wage.
  * 10th Hour & Beyond: $4.0\times$ hourly wage.
* **SPKL Approval Workflow**: Complete drafting, manager review, and approval flow for *Surat Perintah Kerja Lembur*.

### 3. PPh 21 TER Payroll Integration Feeder
* Approved overtime compensation and attendance deductions feed directly into `airiv_payroll_indonesia` payslips for automated monthly PPh 21 TER (Tarif Efektif Rata-rata) processing.

---

## Validated Commercial Benchmark (Tested & Audited)

The module was verified under live Odoo 18.0 Community conditions:

1. **GPS Geofence Validation**:
   - Geofence Zone: Center $(-6.2750000, 106.7650000)$ with 100m radius.
   - Check-in A (15.68m distance): Status $\rightarrow$ `VALID`.
   - Check-in B (778.36m distance): Status $\rightarrow$ `OUT_OF_BOUNDS`.
2. **Depnaker Statutory Wage Benchmark**:
   - Employee Basic Salary: Rp 5.190.000,00 $\rightarrow$ Hourly Rate (1/173): **Rp 30.000,00 / hour**.
3. **Workday Overtime Calculation (3 Hours)**:
   - Multiplier Hours: $1.0 \times 1.5 + 2.0 \times 2.0 = \mathbf{5.5\text{ jam}}$.
   - Total Overtime Compensation: $5.5 \times \text{Rp } 30.000,00 = \mathbf{\text{Rp } 165.000,00}$.
4. **Weekend / Holiday Overtime Calculation (9 Hours)**:
   - Multiplier Hours: $8.0 \times 2.0 + 1.0 \times 3.0 = \mathbf{19.0\text{ jam}}$.
   - Total Overtime Compensation: $19.0 \times \text{Rp } 30.000,00 = \mathbf{\text{Rp } 570.000,00}$.
5. **SPKL Approval**: Verified batch transition to `approved` accumulating 12.0 total verified overtime hours for payroll processing.

---

## Installation & Odoo Configuration Guide

1. **Deploy Module**:
   Place `airiv_hr_indonesia` inside your Odoo `custom_addons` directory (requires `hr`, `hr_attendance`, and `airiv_payroll_indonesia`).

2. **Activate Module**:
   * Navigate to **Apps > Update Apps List**.
   * Search for `Indonesia HR Geofencing Attendance & Depnaker Overtime Engine` and click **Activate**.

3. **Setup GPS Geofence & Wages**:
   * Open **HR & Kehadiran > Zona Geofencing GPS** to register company GPS coordinates.
   * Enter monthly basic salary in the Employee profile to automatically compute the 1/173 Depnaker hourly rate.
   * Manage and approve overtime forms under **HR & Kehadiran > Lembur Karyawan (SPKL)**.

---

## Module Specifications

| Specification | Details |
| :--- | :--- |
| **Framework Version** | Odoo 18.0 Community Edition (OWL & App Drawer compliant) |
| **License** | GNU Lesser General Public License v3.0 (LGPL-3) |
| **Price** | Free ($0.00) |
| **Dependencies** | `base`, `hr`, `hr_attendance`, `airiv_payroll_indonesia` |
| **Regulatory Standards** | Kemnaker PP No. 35/2021, UU Cipta Kerja, Formula Lembur 1/173 |
| **Server Overhead** | Zero (Native ORM, direct SQL aggregation) |
