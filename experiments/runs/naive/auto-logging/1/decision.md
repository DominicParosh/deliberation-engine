# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 4 rounds (policy `naive`) · $0.011.

Challenges: 10 raised · 9 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

An automatic logging feature for meetings with government officials will be implemented in the Government CRM to enhance engagement history tracking. This feature will require careful handling of user roles and data integrity measures. However, clarifications are still needed regarding user permission mechanisms to ensure compliance with data protection standards.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable automatic logging of meetings with government officials in the CRM.  
  The decision to enable automatic logging directly addresses the need for accurate engagement history tracking, responding to stakeholder concerns about lost data.

**In scope**

- **S1** Implement a feature that automatically logs meetings held with government officials, including date, time, duration, participants, and agenda; establish a process for users to report inaccuracies in logged meeting data, which involves submitting a correction request to a designated administrator who will review and verify the report before any changes are made.  
  The inclusion of a process for users to report inaccuracies in logged meeting data ensures that data integrity is maintained, which was a critical concern during deliberations. _(C3, C10)_
- **S2** Provide functionality for users (regional coordinators and project managers) to view and edit logged meeting details within the CRM.  
  Functionality for viewing and editing meeting details is in scope, empowering users to manage their records effectively without compromising data integrity.
- **S3** Ensure only users with the roles of regional coordinators and project managers can view and edit meeting logs; access enforcement will be managed through role-based access control (RBAC) mechanisms, ensuring no other roles will have access to this information.  
  User access to meeting logs will be restricted to regional coordinators and project managers to safeguard sensitive information; this was made explicit to address confidentiality concerns. _(C1, C6, C7)_
- **S4** Integrate the feature with existing contact and engagement history modules in the CRM, ensuring that logged meetings are associated with the relevant government official records using unique identifiers that link each record to a corresponding government official.  
  Integrating the feature with existing CRM modules ensures accurate association of logged meetings with corresponding government officials, addressing ownership and data quality issues. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not implement real-time notifications for users about logged meetings.  
  Real-time notifications were deemed unnecessary for this release, allowing focus on core functionality without overcomplicating the system.
- **X2** This release will not log other types of engagement (such as emails or phone calls) with government officials.  
  Logging of other engagement types was excluded to maintain a clear scope and ensure the feature meets its primary objective of logging meetings.
- **X3** This release does not include any analytics or reporting features related to engagement history.  
  Analytics or reporting on engagement history is out of scope, ensuring the initial implementation remains straightforward and focused on logging functionality.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The CRM currently has the capability to track meetings, and user roles are defined within the system. | Kept | never challenged |
| A2 | User permission settings are already in place to restrict access to sensitive meeting logs, ensuring compliance with data protection regulations. | Kept | C5 → escalated; C7 → revised |
| A3 | The users (regional coordinators and project managers) are trained and familiar with the existing functionalities of the CRM. | Kept | never challenged |

## Definitions

- **D1** "automatic logging" means capturing meeting information without manual input by the user, based on predefined parameters set in the system; these parameters include that the meeting is scheduled in advance, involves at least one government official who is a participant, and is conducted through approved channels of communication. Informal meetings and unscheduled meetings will not be automatically logged.  
  The definition of 'automatic logging' was refined to clarify conditions, mitigating the risk of incorrect logging and ensuring user understanding. _(C4, C9)_
- **D2** "government officials" means individuals representing member countries, including country representatives, ministry contacts, and mission delegates.  
  'Government officials' is clearly defined to specify the types of individuals involved, avoiding ambiguity during the logging process.

## Success criteria

- **K1** Achieve at least 90% of meetings that meet the criteria defined in D1 as 'logged' automatically within the first quarter after release, measured by comparing the total number of meetings tagged with the status 'logged' to the number of authorized meetings held in the same period.  
  Success criteria were adjusted to provide clear parameters for measuring effectiveness, ensuring alignment with the defined logging conditions. _(C2, C8)_

## Open questions for humans

### C5 · MAJOR · blocks the build

**What specific mechanisms ensure only authorized users can access sensitive meeting logs?**

- Why it matters: This is crucial to prevent unauthorized access and maintain confidentiality within the CRM.
- Decision owner: Head of Data Protection
- Options: Implement role-based access control (RBAC) policies / Define clear user role scopes and permissions / Utilize logging and auditing for access

## Tension report

The main disagreement centered around the clarity and specifics of user permissions and automatic logging conditions. The Proposer expressed concerns that any ambiguity could lead to misinterpretation, while the Critic raised significant alarms about potential unauthorized access to sensitive information. This tension was partially resolved regarding most elements but remains open in relation to user permission specifications.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 7 | 1 | 5 | 1 | 0.27 | 80 | 70 | CONTINUE | continue |
| 3 | 10 | 3 | 6 | 1 | 0.38 | 80 | 70 | CONTINUE | continue |
| 4 | 10 | 0 | 9 | 1 | 0.10 | 70 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (70/100): The clarity of automatic logging conditions and reporting of inaccuracies might still lead to misinterpretation among users.
- Critic's remaining worry (85/100): Misconfigured user role settings could still lead to unauthorized access to sensitive meeting logs.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | The proposal does not specify which user roles have access to view and edit logged meeting data, posing a risk of sensitive information being exposed to unauthorized personnel. |
| C2 | MAJOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The success criteria defined as achieving 90% of meetings logged lacks clarity on how automatic logging effectiveness will be measured and what constitutes a logged meeting. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | REVISED | 0 | The proposal does not clarify how data integrity will be maintained if there are inaccuracies in the logged meeting data. |
| C4 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'automatic logging' is not sufficiently defined, lacking clear parameters on how the system determines which meetings to log. |
| C5 | MAJOR | CONFIDENTIALITY | A2 | R1 | ESCALATED | 0 | Assumption A2 on user permission settings does not clarify the mechanisms used to restrict access to sensitive meeting logs, introducing potential risks. |
| C6 | MAJOR | OWNERSHIP | S4 | R1 | REVISED | 0 | The proposal does not outline the process for linking logged meetings to the correct government officials, risking incorrect data association. |
| C7 | MAJOR | CONFIDENTIALITY | A2 | R2 | REVISED | 0 | The proposal does not specify the mechanisms employed to enforce the user permission settings for sensitive meeting logs, which could allow potential breaches. |
| C8 | MAJOR | DEFINITIONS | K1 | R3 | REVISED | 0 | The success criteria K1 for meeting logging effectiveness lacks clarity on how 'logged' is defined and measured. |
| C9 | MAJOR | DEFINITIONS | D1 | R3 | REVISED | 0 | The term 'automatic logging' is still not sufficiently specific regarding the conditions that trigger logging beyond the current definitions provided. |
| C10 | MAJOR | DATA_QUALITY | S1 | R3 | REVISED | 0 | The proposal does not fully outline how inaccuracies in logged meeting data are addressed, which raises concerns about data integrity. |
