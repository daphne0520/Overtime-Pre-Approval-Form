```mermaid
flowchart TD
    A([Employee]) --> B[Submit OT Application]
    B --> C[OT Calculation]
    C --> D[Manager Approval]
    
    D -->|Approve| E[HR Review]
    D -->|Reject| X[Rejected]
    D -->|Amend| B
    
    E -->|Approve| F[Payroll Confirmation]
    E -->|Reject| X
    E -->|Amend| B
    
    F -->|Confirm| G[Pending Payment]
    F -->|Amend| B
    F -->|Reject| X
    
    G --> H([Payment Completed])
