# Overtime-Pre-Approval-Form
The Overtime Pre-Approval Form is a ticket-driven app on the V-ONE low-code platform that digitizes OT approval. A single ticket moves through Employee, Manager, HR, and Payroll before closing as Paid, Rejected, or Returned. This document covers the app after issues from the initial review were fixed and re-verified.

# Problem Statement
Overtime approval at most sites still runs on email threads, paper forms, or ad-hoc chat messages between an employee, their manager, HR, and payroll. This creates several concrete problems:

1. Fragmented source of truth. OT hours, the applicable hourly rate, and the final payable amount exist somewhere across emails and spreadsheets, but there's no single, transparent record showing the calculated amount and how it moved through each stage.

2. Limited audit visibility. A trail technically exists across email threads and forwarded messages, but it isn't consolidated. When a dispute arises over how an OT payment was calculated or who approved what, there's no single timestamped view of each decision, the multi-level verification behind it, and the remarks at each stage.

3. Inconsistent OT pay calculation. Without a standardized formula, different managers or HR staff may apply different hourly rates or overtime multipliers to the same employment type, leading to pay disparities.

4. No visibility for management. There's no consolidated view of how many OT hours are being applied for, approved, or paid out across departments in a given period.

5. Slow, unclear routing. Requests can sit unnoticed in someone's inbox with no automatic escalation or notification to the next approver in line.

# Objective
1. Replace manual/paper-based OT requests with a single digital ticket that moves through a defined approval chain: Employee → Manager → HR → Payroll.

2. Standardize how OT pay is calculated (hourly rate × OT hours × overtime multiplier) so the same inputs always produce the same payable amount, at every stage of approval.

3. Give each role (Manager, HR, Payroll) a dedicated portal showing only the requests relevant to them, with the ability to approve, reject, or return a request for amendment with remarks

4. Automatically notify the correct next responsible party by email whenever a request changes status, so nothing sits idle waiting to be noticed.

5. Track each employee's remaining OT hours balance against a statutory/company cap.

6. Give management a consolidated dashboard: total requests, approved count, total OT hours applied, total payout, and a breakdown by department and by reason for overtime

# Methodology
1. Requirement Analysis. Identified the requirements and current processes involved in OT application, approval, review, and payment.

2. System & Workflow Design. Designed the OT application process, approval stages, data fields, calculations, and status flow.

3. System Development. Developed the OT Application Portal using the V-One Platform, including application forms, approval interfaces, chatbot, and data visualization.

4. Workflow Automation. Implemented automated approval workflows and status update notifications to streamline the OT application process.

5. Testing & Validation. Tested the system functions, calculations, workflow transitions, and notifications to ensure they work as intended.

6. Evaluation & Refinement. Reviewed the system based on identified findings and refined the application to improve usability and process efficiency.

# Technologies Used
1. V-One Platform. Main development platform used to design and implement the OT Application Portal, including workflow automation, chatbot/AI functions, and data visualization.

2. Python. Used to implement custom logic for automated status update notifications.

# Solution Architecture & Platform Portability

### Current Implementation

The Overtime Pre-Approval Form is currently implemented on the V-ONE low-code platform, with workflow automation, role-based approval interfaces, business-rule calculations, notifications, and management-level data visualization.

### Potential Enterprise Implementation

The solution concept can be adapted to other enterprise platforms depending on the organization's existing technology ecosystem:

- **Microsoft Power Platform** :Power Apps, Power Automate, Dataverse / SharePoint, and Power BI
- **ServiceNow** :Request/ticket management and multi-stage approval workflows
- **Custom Web Application** :Front-end application with backend business logic, database, notification services, and analytics

### Platform-Independent Core

Regardless of the implementation platform, the core solution consists of:

**Approval Workflow + Business-Rule Calculation + Role-Based Access + Automated Notifications + Management Analytics**

The current V-ONE implementation demonstrates the business process and solution design, while the underlying workflow and business logic can be adapted to other platforms.

# Pre-Implementation Findings
Based on the completed development and pre-implementation testing of the OT Application Portal, several key findings were identified regarding the system’s functionality and readiness for implementation:

1. Approval Workflow. The system incorporates four main approval stages, namely Manager Approval, HR Review, Payroll Confirmation, and Payment, providing a structured flow for processing OT applications.

3. Application Management. The portal consists of three main application sections: New OT Application, Pending Approvals, and Past OT Applied, allowing users to submit, manage, and track their OT applications.

4. Automated Calculation. OT hours and OT payment are automatically calculated based on the submitted OT timing, break time, and hourly rate, reducing the need for manual calculations.

5. Automated Notifications. The system provides automated status-based notifications for different stages of the OT application process, including HR review, payroll confirmation, rejection, and amendment.

6. OT Information Capture. The application captures 7 or more key OT-related inputs, including OT date, start time, end time, break time, reason, claim type, and hourly rate, supporting the calculation and processing of OT applications.

7. User Assistance and Data Monitoring. The integrated chatbot supports OT-related enquiries and application status checking, while data visualization provides a visual representation of OT application data for monitoring and analysis.
