/**
 * OT Application Portal — Calculation Logic
 * Extracted from the low-code app's template.json
 *
 * These formulas run client-side as reactive expressions bound to
 * form fields / display widgets. Reproduced here as plain JS functions
 * for readability and version control.
 */

/**
 * Parse a time value into decimal hours.
 * Supports "HH:MM", "HHMM" (4-digit), or a plain number.
 */
function parseTimeToHours(t) {
  if (!t) return 0;
  const s = String(t).trim();
  if (s.includes(':')) {
    const [h, m] = s.split(':');
    return Number(h || 0) + Number(m || 0) / 60;
  }
  if (s.length === 4) {
    return Number(s.slice(0, 2)) + Number(s.slice(2, 4)) / 60;
  }
  return Number(s) || 0;
}

/**
 * 1. OT Hours calculation
 * OT hours = end time - start time - break time
 * Rounded to 2 decimal places, never negative.
 */
function calculateOtHours(ot_start_time, ot_end_time, break_time) {
  const raw = parseTimeToHours(ot_end_time) - parseTimeToHours(ot_start_time) - Number(break_time || 0);
  return Math.max(0, Math.round(raw * 100) / 100);
}

/**
 * 2. OT Pay calculation
 * OT pay = OT hours × hourly rate × overtime multiplier
 * Rate/multiplier default to 20 and 1.5 if not found in the user's LDAP profile.
 */
function calculateOtPay(otHours, ldapProfile = {}) {
  const hourlyRate = ldapProfile.hourlyRate ?? ldapProfile.hourly_rate ?? 20;
  const overtimeMultiplier = ldapProfile.overtimeMultiplier ?? ldapProfile.overtime_multiplier ?? 1.5;
  return otHours * hourlyRate * overtimeMultiplier;
}

/**
 * 3. Remaining OT Hours Balance (monthly)
 * Balance = 104 (fixed monthly cap) − sum of OT hours already
 * approved/paid/pending-payout for the current month, for this employee.
 *
 * NOTE: This is a *display-only* calculation bound to a text widget.
 * It reads from a query (`my_approved_ot_this_month`) that pulls the
 * employee's OT ticket records for the month. It is NOT enforced as a
 * submission-time validation — nothing currently blocks a user from
 * submitting a new OT request that would exceed this balance.
 *
 * Two slightly different versions exist in the source file across
 * different pages/widgets (different status filters) — reconciled here
 * into one function with the status list as a parameter.
 */
const MONTHLY_OT_CAP_HOURS = 104;

function calculateRemainingOtBalance(monthlyOtRecords, currentUserId, countedStatuses) {
  const used = (monthlyOtRecords || [])
    .filter(item => {
      const belongsToUser =
        !currentUserId ||
        item.createdBy === currentUserId ||
        item.createdByUser?.id === currentUserId;
      return belongsToUser && countedStatuses.includes(item.currentStatusName);
    })
    .reduce((sum, item) => {
      // handle both flat fields and nested tableRecords structure
      const fields = (item.tableRecords || []).reduce(
        (acc, r) => Object.assign(acc, r.value || {}),
        {}
      );
      const hours = parseFloat(fields.ot_hours ?? item.ot_hours ?? 0) || 0;
      return sum + hours;
    }, 0);

  return MONTHLY_OT_CAP_HOURS - used;
}

// Example usage:
// const balance = calculateRemainingOtBalance(
//   monthlyOtRecords,
//   currentUser.id,
//   ['Approved', 'Awaiting Payroll Confirmation', 'Pending Payment', 'Paid']
// );

module.exports = {
  parseTimeToHours,
  calculateOtHours,
  calculateOtPay,
  calculateRemainingOtBalance,
  MONTHLY_OT_CAP_HOURS,
};
