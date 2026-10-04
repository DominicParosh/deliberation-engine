# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.016.

Challenges: 9 raised · 7 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

This release will implement an automated logging feature for meetings with government officials in the Government CRM system, ensuring accurate engagement history through controlled logging and verification protocols. However, it will not include integrations with third-party applications or allow for manual edits of logged meetings. Open questions regarding ownership transfer processes and user access controls still need to be addressed by decision-makers.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automate the logging of meetings with government officials in the Government CRM system.  
  Automating the logging of meetings was established to improve engagement tracking and accountability.
- **V2** Provide users a clear history of engagement with government officials through the automated logging feature.  
  Providing a clear history of engagement through the automated logging feature supports users' ability to track interactions effectively.

**In scope**

- **S1** Automatically log meetings in the CRM when users input the meeting details into a designated form. Access to these logs will be restricted to regional coordinators and project managers only, ensuring that sensitive information is not accessible to unauthorized personnel.  
  Access control measures were clarified to limit visibility of logged meetings to only regional coordinators and project managers, addressing confidentiality concerns. _(C1)_
- **S2** Provide an interface for regional coordinators and project managers to view logged meetings with government officials.  
  An interface for viewing logs was included to facilitate easy access for authorized users.
- **S3** Ensure that the logs include essential details such as date, time, participants, agenda, meeting outcomes, and implement a comparison mechanism to check for duplicate entries within a specified timeframe.  
  The detail inclusion requirement enhances data quality and addresses potential duplication of meeting logs. _(C3)_
- **S4** Implement data validation to ensure only correctly formatted entries for meeting logs are accepted. Specific criteria for data validation include mandatory fields for date, time, participants, and agenda, with strict checks for non-empty values, correct date formats, and email format validation for participants prior to submission.  
  Data validation criteria were clearly defined to prevent incomplete or inaccurate meeting logs, reinforcing data integrity. _(C4, C5, C6, C8)_
- **S5** Notifications will be sent to users if any required fields are missing upon submission of meeting logs.  
  Notifications for missing fields enhance user promptness and the quality of submissions.
- **S6** A defined process will automatically transfer the ownership of logged meeting records from departing users to designated personnel within the same team or role, ensuring continuity in engagement history. When a user departs or changes roles, the system will notify the designated personnel and require them to confirm the transfer of ownership within 48 hours of the notification.  
  Ownership transfer procedures were established to minimize gaps in engagement history when users change roles, although the specifics on personnel designation remain unresolved. _(C2, C9)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any integration with third-party calendar or meeting scheduling applications.
- **X2** The release will not allow manual editing or deletion of logged meetings by users.
- **X3** This feature will not cover meetings that do not involve government officials.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have access to a designated form for logging meetings, which enables them to input meeting details. | Kept | never challenged |
| A2 | Users are trained on how to use the new automated logging feature and understand the importance of logging meetings. | Kept | never challenged |
| A3 | Data security and privacy policies will allow automated logging of sensitive government engagements. | Kept | never challenged |

## Definitions

- **D1** "Meetings with government officials" means any scheduled discussions involving representatives from government bodies recognized by the organization.  
  Clarifying meetings with government officials ensures all logged interactions are appropriately defined and consistent.
- **D2** "Logging automatically" means the system will capture and create records of meetings without requiring user intervention after initial entry of meeting details.  
  Defining automatic logging clarifies the interaction process without requiring manual intervention after details are entered.
- **D3** "Engagement history" means a chronological record of all interactions between users and government officials that are tracked for transparency and accountability, including the minimum required fields of date, time, participants, agenda, and outcomes for compliance with data handling regulations.  
  Outlining minimum data fields aligns the system requirements with compliance considerations, enhancing legal adherence. _(C4)_
- **D4** "Data quality checks" means a verification process that reviews all logged meeting records to ensure accuracy and completeness, including confirmation of required fields and checking for consistency with existing records, and is to be conducted within 48 hours after a meeting is logged.  
  Establishing a verification process for data quality checks assures users that logged data will be accurate post-entry. _(C7)_

## Success criteria

- **K1** Ensure 90% of scheduled meetings are logged automatically within 24 hours of occurrence, measured through CRM analytics.  
  Setting success criteria based on logging performance measures ensures accountability and effectiveness of the automated system.
- **K2** Ensure that 90% of scheduled meetings are logged automatically within 24 hours of occurrence and reviewed for data integrity within 48 hours, measured through CRM analytics.  
  The criteria for data integrity checks build upon K1 by incorporating a review mechanism. _(C5)_

## Open questions for humans

### C2 · BLOCKER · blocks the build

**What specific process will govern the ownership transfer of logged meeting records when users change roles or leave the organization?**

- Why it matters: Clarifying this process will ensure continuity in engagement history and prevent data loss.
- Decision owner: Project Management Team
- Options: Establish a designated role for ownership transfer / Create automatic notifications for transfers / Require confirmation from new role holders

### C9 · MAJOR · blocks the build

**How will designated personnel for the ownership transfer of meeting logs be chosen and what criteria will be applied?**

- Why it matters: This impacts the clarity and effectiveness of maintaining engagement history post-user transitions.
- Decision owner: Human Resources
- Options: Based on seniority / By team consensus / Random assignment

## Tension report

The primary disagreement centered on the ownership and accountability for logged meeting records, particularly when users change roles or leave the organization. While a process was suggested, specific details on implementation remain unresolved, resulting in a need for further human decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 1 | 5 | 0 | 0.21 | 75 | 60 | CONTINUE | continue |
| 3 | 8 | 2 | 5 | 1 | 0.39 | 70 | 40 | CONTINUE | continue |
| 4 | 9 | 1 | 7 | 1 | 0.25 | 75 | 60 | CONTINUE | continue |
| 5 | 9 | 1 | 7 | 1 | 0.25 | 80 | 70 | CONTINUE | continue |
| 6 | 9 | 0 | 7 | 2 | 0.25 | 85 | 80 | CONTINUE | converged |

- Proposer's remaining worry (85/100): The implementation may still face challenges in ensuring that all users effectively confirm ownership transfers in a timely manner.
- Critic's remaining worry (80/100): Insufficient clarity in user access may still pose risks of unauthorized information access.
- ⚠ Proposer reported 85/100 confidence while blocker(s) C2 remain unsettled.
- ⚠ Critic reported 80/100 confidence while blocker(s) C2 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | S1 does not specify who can see the logged meetings, creating a risk of sensitive information reaching unauthorized personnel. |
| C2 | BLOCKER | OWNERSHIP | GAP | R1 | ESCALATED | 1 | The proposal does not address the maintenance and ownership of automatically logged meeting records, particularly when users change roles or leave the organization. |
| C3 | MAJOR | DATA_QUALITY | S3 | R1 | REVISED | 0 | S3 does not address how the system will prevent or handle duplicate or erroneous entries in logged meeting records, which could affect the quality of engagement history. |
| C4 | MAJOR | COMPLIANCE | D3 | R1 | REVISED | 0 | D3 does not specify the minimum information required to ensure compliance with data handling regulations regarding sensitive engagement records. |
| C5 | MAJOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | The proposal does not clarify how often the system will check for data integrity and correctness after automatically logging meetings. |
| C6 | MAJOR | FEASIBILITY | S4 | R1 | REVISED | 0 | S4 does not outline how the data validation process will function, potentially leading to uncertainty about meeting log completion and accuracy. |
| C7 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not clarify how the system will ensure data quality checks after logging meetings, creating a potential risk for incorrect or outdated records. |
| C8 | MAJOR | DEFINITIONS | S4 | R3 | REVISED | 0 | The absence of clear details in the data validation process could lead to incorrect entries being logged, affecting engagement history quality. |
| C9 | MAJOR | OWNERSHIP | GAP | R4 | ESCALATED | 2 | The proposal lacks a defined process for maintaining ownership and accountability for logged meeting records when users change roles or leave the organization, which could lead to loss of crucial engagement history. |
