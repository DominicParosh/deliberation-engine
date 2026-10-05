# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.010.

Challenges: 8 raised · 4 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

This release will implement an automatic logging feature for meetings with government officials to preserve engagement history in the Government CRM. However, it will not include the ability to edit or delete logged meetings, nor will it integrate with external calendar applications in this initial release. Decisions are still needed regarding the management of contact classifications and user permissions to prevent potential data breaches.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automatically log meetings with government officials in the Government CRM.
- **V2** Enhance engagement history tracking for users without requiring manual entries.

**In scope**

- **S1** Meetings will be automatically logged in the system whenever a meeting is scheduled or completed with contacts classified as government officials.
- **S2** A notification will be sent to meeting participants and their respective supervisors confirming that the meeting has been logged automatically.  
  Notifications will confirm logged meetings, ensuring all relevant parties are informed and reducing communication breakdowns. _(C6)_
- **S3** Log entries will include details such as the date, time, duration, meeting participants (both internal and external), and a summary of the discussion points, while excluding sensitive topics or details deemed confidential by the meeting participants or by regulations.  
  Log entries will exclude sensitive details to protect confidentiality and adhere to regulations, addressing concerns about privacy. _(C3)_
- **S4** This feature will be available for users with roles of regional coordinators and project managers, specifically granting access to automatically logged meetings to these roles only.  
  Restricting access to logged meetings based on user roles will help safeguard sensitive information. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include the ability to edit or delete automatically logged meetings.
- **X2** The feature will not integrate with external calendar applications or other event management systems in this initial release.
- **X3** Meetings that are not classified under government officials will not be auto-logged.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have the appropriate permissions to access and view log entries. | Kept | C5 → escalated; C8 → escalated |
| A2 | Meeting details such as participants and summaries can be accurately retrieved from the system during the logging process. | Kept | never challenged |
| A3 | The classification of contacts as government officials is already established in the system. | Kept | C2 → escalated; C7 → escalated |

## Definitions

- **D1** "Meetings" means scheduled events occurring between internal users and external contacts defined as government officials.  
  Defining meetings clearly as events with government officials prevents ambiguity in logging processes.
- **D2** "Automatically logged" means the system records meetings without requiring user interaction after the meeting is held.
- **D3** "Engagement history" means a chronological record of interactions and meetings with contacts, stored within the CRM.
- **D4** "Government officials" means contacts that are classified in the system as belonging to government entities or representatives of a government agency, including but not limited to ministers, diplomats, and government employees.  
  Providing a clear definition for 'government officials' mitigates the risk of misclassification during logging. _(C1)_

## Success criteria

- **K1** At least 90% of meetings with government officials are successfully logged within the system over a three-month period, measured by CRM usage reports.

## Open questions for humans

### C2 · MAJOR · blocks the build

**How will the system manage changes to a contact's classification over time?**

- Why it matters: This will ensure that meetings are logged based on the most accurate and current classification to avoid operational risks.
- Decision owner: Data Governance Lead
- Options: Establish a protocol for regular updates to contact classifications / Allow users to flag changes that require review / Create an automated system for classification updates based on user input
- Proposer's last word (R2, defend, needs human decision): Only the organization can determine how the classification of contacts is maintained and updated as individuals' statuses change, which is outside the scope of this release.
- Critic's last word (R2, escalate): The system's management and updating of contact classifications need clarification.

### C7 · MAJOR · blocks the build

**What specific process is in place for maintaining and updating the classification of contacts as their statuses change?**

- Why it matters: Clarifying this process is crucial to ensure accurate logging and the protection of sensitive information.
- Decision owner: CRM Administrator
- Options: Regular review by the data management team / User notifications for classification changes / Automated updates based on external factors
- Proposer's last word (R3, defend, needs human decision): The classification of contacts as government officials and the process of maintaining that classification is dependent on organizational policies and procedures, which must be established by the organization responsible for the CRM.
- Critic's last word (R3, escalate): The proposal does not specify how updates are handled for contact classifications, which could lead to outdated information being used.

### C8 · MAJOR · blocks the build

**What processes are in place for managing user permissions related to accessing meeting logs?**

- Why it matters: Understanding these processes will inform how sensitive information is safeguarded within the system.
- Decision owner: IT Security Manager
- Options: Conduct user access reviews periodically / Assign clear responsibilities for permission management / Create a detailed user access log
- Proposer's last word (R3, defend, needs human decision): Managing user permissions related to accessing meeting logs is contingent upon existing organizational policies regarding role-based access control and user management, which need to be defined by the organization.
- Critic's last word (R3, escalate): There is no detail in the proposal regarding how user permissions will be managed or what safeguards will prevent unauthorized access.

### C5 · MINOR · does not block the build

**What processes exist for managing and auditing user permissions related to meeting logs?**

- Why it matters: Clear processes are essential to prevent unauthorized access and ensure sensitive information is protected.
- Decision owner: Head of Data Protection
- Options: Implement regular audits of user access / Create role-based access controls / Establish a protocol for revoking access immediately after role changes
- Proposer's last word (R2, defend, needs human decision): Only the organization can decide how user permissions are managed and monitored to comply with data protection standards, which is outside the scope of this release.
- Critic's last word (R2, escalate): Details about managing and auditing user permissions are still needed.

## Tension report

The main disagreement emerged over how to manage and update classifications for contacts and permissions for user access. While the Proposer maintained that responsibility for these aspects lay outside the immediate scope, the Critic raised significant concerns about potential breaches due to inadequate management, leading to multiple escalated issues requiring resolution.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 35 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.50 | 80 | 60 | CONTINUE | continue |
| 3 | 8 | 0 | 4 | 4 | 0.50 | 70 | 40 | CONTINUE | converged |

- Proposer's remaining worry (70/100): There is a risk of relying on manual processes for updating classifications and managing user permissions, which could lead to data breaches.
- Critic's remaining worry (40/100): Unclear management of contact classifications and user permissions could lead to significant data breaches and exposure of sensitive information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'government officials' lacks clear criteria for classification, risking inappropriate logging of meetings with non-government contacts. |
| C2 | MAJOR | OWNERSHIP | A3 | R1 | ESCALATED | 0 | The proposal assumes the classification of contacts is established but does not explain who maintains this classification or what happens when an individual's status changes. |
| C3 | MAJOR | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | The proposal does not specify safeguards for protecting sensitive information discussed during logged meetings, potentially leading to unintended disclosures. |
| C4 | MINOR | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | There is no clarity on which users can view automatically logged meetings, which could lead to unauthorized access to sensitive information. |
| C5 | MINOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | The assumption that users will have appropriate permissions offers no detail on how permission settings are managed or monitored, which could lead to data breaches. |
| C6 | MINOR | DEFINITIONS | S2 | R1 | REVISED | 0 | The notification sent to users confirming that a meeting has been logged does not define who receives these notifications, risking important alerts being missed. |
| C7 | MAJOR | OWNERSHIP | A3 | R2 | ESCALATED | 0 | The proposal does not specify how the classification of contacts is updated over time, which could lead to using outdated information for meeting logs. |
| C8 | MAJOR | OWNERSHIP | A1 | R2 | ESCALATED | 0 | Lack of clarity on how user permissions for accessing meeting logs will be managed poses a risk of unauthorized access to sensitive information. |
