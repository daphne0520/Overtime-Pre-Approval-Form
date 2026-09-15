"""
ot_notifications.py

Extracted, working copy of the two Code/Python nodes from the Overtime
Pre-Approval Form app (V-ONE), workflows:

    1. "OT Application Status Update Notification" -> Code/Python#1
    2. "OT Application Created Notification"        -> Code/Python#1

Both functions below are 1:1 ports of the original node source (verbatim
logic, just translated from the platform's parameter[]/output[] convention
into normal function arguments and a normal return value), so you can run,
import, and test them locally without V-ONE.

Run directly to see both in action with sample data:

    python ot_notifications.py
"""

from __future__ import annotations


def build_status_update_notification(
    record_id,
    status: str,
    prev_status: str,
    value: dict | None,
    user_id,
) -> tuple[str, str]:
    """Port of Code/Python#1 in the "OT Application Status Update
    Notification" workflow.

    Original:
        record_id = parameter[1]
        status = parameter[2]
        prev_status = parameter[3]
        value = parameter[4] or {}
        user_id = parameter[5]
        ...
        output[1] = title
        output[2] = body

    Returns (title, body) instead of writing to output[1]/output[2].
    """
    value = value or {}

    emp_name = value.get("employee_name", "Employee")
    dept = value.get("department", "Department")
    ref_id = value.get("referenceId", str(record_id))

    title = ""
    body = ""

    if status == "Awaiting HR Review":
        title = "[CALL FOR ACTIONS] YOU HAVE AN OT APPLICATION TO REVIEW"
        body = f"OT Application (Ref: {ref_id}) for {emp_name} has been approved by Manager and is awaiting HR review."
    elif status == "Awaiting Payroll Confirmation":
        title = "[CALL FOR ACTIONS] YOU HAVE AN OT APPLICATION TO CONFIRM"
        body = f"OT Application (Ref: {ref_id}) for {emp_name} has been reviewed by HR and is awaiting Payroll confirmation."
    elif status == "Rejected":
        title = "Your Pre-OT Application Has Been Rejected"
        body = f"Your Pre-OT Application (Ref: {ref_id}) has been rejected, please check with your manager for more details."
    elif status == "Returned for Amendment":
        title = "Your Pre-OT Application Has Been Returned"
        remarks = value.get("manager_remarks") or value.get("hr_comments") or value.get("payroll_comments") or "Please check remarks"
        body = f"Your Pre-OT Application (Ref: {ref_id}) has been returned, please resubmit by considering the comments: {remarks}"
    else:
        title = f"OT Application Status: {status}"
        body = f"OT Application (Ref: {ref_id}) status updated to {status}."

    return title, body


def build_created_notification(
    record_id,
    status: str,
    value: dict | None,
    user_id,
) -> tuple[str, str]:
    """Port of Code/Python#1 in the "OT Application Created Notification"
    workflow.

    Original:
        record_id = parameter[1]
        status = parameter[2]
        value = parameter[3] or {}
        user_id = parameter[4]
        ...
        output[1] = title
        output[2] = body
    """
    value = value or {}

    emp_name = value.get("employee_name", "Employee")
    dept = value.get("department", "Department")
    ref_id = value.get("referenceId", str(record_id))

    title = "[CALL FOR ACTIONS] YOUR EMPLOYEE HAVE SUBMITTED A NEW OT APPLICATION!"
    body = f"Employee {emp_name} ({dept}) has submitted a new OT application (Ref: {ref_id})."

    return title, body


if __name__ == "__main__":
    print("=== OT Application Created Notification ===")
    title, body = build_created_notification(
        record_id=142,
        status="Awaiting Manager Approval",
        value={
            "employee_name": "Nur Aina Binti Zulkifli",
            "department": "Warehouse Operations",
            "referenceId": "OT-000142",
        },
        user_id="mgr-001",
    )
    print("Title:", title)
    print("Body: ", body)

    print()
    print("=== Status Update: Awaiting HR Review ===")
    title, body = build_status_update_notification(
        record_id=142,
        status="Awaiting HR Review",
        prev_status="Awaiting Manager Approval",
        value={
            "employee_name": "Nur Aina Binti Zulkifli",
            "department": "Warehouse Operations",
            "referenceId": "OT-000142",
        },
        user_id="hr-001",
    )
    print("Title:", title)
    print("Body: ", body)

    print()
    print("=== Status Update: Returned for Amendment ===")
    title, body = build_status_update_notification(
        record_id=142,
        status="Returned for Amendment",
        prev_status="Awaiting HR Review",
        value={
            "employee_name": "Nur Aina Binti Zulkifli",
            "referenceId": "OT-000142",
            "hr_comments": "Please attach manager's email approval as supporting document.",
        },
        user_id="emp-2291",
    )
    print("Title:", title)
    print("Body: ", body)

    print()
    print("=== Status Update: Rejected ===")
    title, body = build_status_update_notification(
        record_id=135,
        status="Rejected",
        prev_status="Awaiting HR Review",
        value={"employee_name": "Rajesh K.", "referenceId": "OT-000135"},
        user_id="emp-3010",
    )
    print("Title:", title)
    print("Body: ", body)
