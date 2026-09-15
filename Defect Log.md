# Defect Log

This document records defects identified during functional testing of the Overtime Pre-Approval Form and their subsequent resolution and re-validation.

## Defect Summary

| Bug ID | Module | Severity | Defect | Status |
|---|---|---|---|---|
| BUG-001 | Manager OT Portal | Medium | `NaN` values were displayed for OT Hours Requested and Calculated OT Pay for some Rejected / Returned for Amendment records in the Past OT Applied (MY) table. | Fixed & Re-tested |
| BUG-002 | Payroll & OT Dashboard | Medium | OT Reason categories were displayed inconsistently, causing equivalent or similar values to be fragmented into separate chart categories. | Fixed & Re-tested |

---

## BUG-001 — `NaN` Displayed for Historical OT Records

**Module:** Manager OT Portal  
**Detected:** 14 September 2026  
**Severity:** Medium  
**Status:** Fixed & Re-tested

### Issue

The **Past OT Applied (MY)** table displayed `NaN` in the **OT Hours Requested** and **Calculated OT Pay** columns for several Rejected / Returned for Amendment records.

Affected examples included:

- T202608-0030
- T202608-0029
- T202608-0028
- T202608-0027
- T202608-0026

### Expected Behaviour

Historical OT records should display meaningful OT Hours and Calculated OT Pay values, such as the originally requested values or an appropriate zero value, rather than `NaN`.

### Resolution

The affected data handling / display logic was corrected so that historical records with Rejected or Returned statuses no longer produce `NaN` values.

### Re-validation

The affected historical records were reviewed again after the correction to verify that the OT Hours Requested and Calculated OT Pay fields display valid values.

**Result:** PASS

---

## BUG-002 — Inconsistent OT Reason Categories in Dashboard

**Module:** Payroll & OT Dashboard  
**Detected:** 14 September 2026  
**Severity:** Medium  
**Status:** Fixed & Re-tested

### Issue

The **OT Reasons Breakdown** chart contained inconsistent category labels, causing similar reason values to be treated as separate categories.

Examples identified during testing included variations such as:

- `Business Trip` vs `business trip`
- `customer project`
- `CUSTOMER request`
- `Customer Service`

This fragmented the reporting and reduced the clarity of the dashboard analysis.

### Expected Behaviour

Equivalent OT reason values should be standardised so that the dashboard presents consistent categories without unnecessary duplication.

### Resolution

The OT reason values used for dashboard aggregation were standardised so that inconsistent labels are consolidated into consistent reporting categories.

### Re-validation

The OT Reasons Breakdown chart was reviewed again after the correction to verify that the displayed categories are consistent and that unnecessary duplicate categories no longer fragment the visualization.

**Result:** PASS

## Testing Cycle

The defect resolution process followed the cycle below:

**Defect Identified → Root Cause / Logic Reviewed → Fix Implemented → Re-tested → PASS**

These defects were identified during functional testing and addressed before the system was considered ready for implementation. Testing covered the Employee, Manager, HR, Payroll, and Dashboard modules.
