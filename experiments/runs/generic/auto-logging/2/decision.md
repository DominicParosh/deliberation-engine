# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 4 rounds (policy `gated`) · $0.011.

Challenges: 9 raised · 8 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will automate the logging of meetings with government officials in the Government CRM for regional coordinators and project managers, enhancing data quality and user efficiency. Users will receive notifications confirming successful logging, and a designated data steward will oversee the accuracy of logged information. However, clarity on how meeting confirmations will be documented for audit and compliance purposes remains unresolved.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automated logging of meetings with government officials in the CRM system.  
  Automated logging of meetings with government officials will be implemented to maintain accurate engagement histories as requested by users.
- **V2** User notifications will be sent to confirm successful logging of each meeting.  
  User notifications for confirming successful logging were added to enhance user experience and accountability.

**In scope**

- **S1** The system will automatically log meetings when a user enters meeting details through a designated interface, capturing date, time, attendees, and key discussion points defined as actionable items or decisions made during the meeting.  
  The scope was clarified to ensure that key discussion points are defined as actionable items or decisions made during meetings, which will improve consistency in logging. _(C3)_
- **S2** Regional coordinators and project managers will be the primary users of the automated logging feature. A designated data steward will be responsible for maintaining the accuracy of logged information, which includes reviewing logs for errors, correcting inaccuracies, and ensuring adherence to data quality standards.  
  A designated data steward's role in maintaining the accuracy of logged information was explicitly included to address ownership and accountability issues. _(C2)_
- **S3** Users will receive notifications via the system to confirm the logging of their meetings.  
  Notifications confirming meeting loggings were integrated into the system to ensure users are informed about the status of their entries.
- **S4** All logged meetings will be associated with the relevant government officials' profiles in the CRM.  
  Linking logged meetings to government officials' profiles in the CRM supports easier tracking and engagement monitoring.
- **S5** The system will ensure that only users with appropriate access rights, specifically regional coordinators, project managers, and designated data stewards with Level 2 security clearance or higher, can log meetings involving sensitive or confidential information. These access levels will be determined by the organization's data governance policy.  
  Access rights were firmly established to include only regional coordinators and project managers with Level 2 security clearance to manage confidentiality and security concerns. _(C1, C8)_
- **S6** The system will archive all confirmations of scheduled meetings, which includes the method of logging confirmation, such as email confirmations or digital acknowledgment by participants, as evidence to maintain compliance.  
  The archiving method for meeting confirmations was revised to meet compliance standards for documentation and audits. _(C7)_

## What it will not do

**Out of scope for this release**

- **X1** The feature will not include automatic logging of informal meetings or conversations, such as phone calls or casual discussions, which will be classified as meetings not requiring prior scheduling or formality.  
  Clarification on the classification of informal vs. formal meetings was added to prevent misclassifications and ensure accurate records. _(C4)_
- **X2** Integration with external calendar systems for automatic meeting logging is not included in this release.  
  Integration with external calendar systems was deemed out of scope, as it was not essential for the initial release of the logging feature.
- **X3** User role management and security clearance updates are outside the scope of this release.  
  User role management updates remain outside this release, as they are governed by separate organizational processes.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to a designated interface for entering meeting details in the CRM, which the proposal depends on. | Kept | never challenged |
| A2 | Meetings must be scheduled and confirmed beforehand by all parties involved for this feature to work effectively. | Kept | C6 → escalated; C7 → revised |
| A3 | The organization has existing policies regarding data sensitivity and confidentiality, which will dictate how meeting details are logged and accessed. | Kept | never challenged |

## Definitions

- **D1** "Automated logging" means the functionality within the CRM that captures meeting details without manual input once the meeting is scheduled and confirmed.  
  The definition of 'automated logging' was kept concise to ensure understanding of the functionality's core purpose.
- **D2** "Meeting details" means the specific information regarding the meeting, including the date, time, attendees (individuals involved), and an outline of key discussion points.  
  Defining 'meeting details' ensures all users have a consistent understanding of what information should be logged, enhancing clarity.

## Success criteria

- **K1** At least 90% of scheduled meetings with government officials are successfully logged within 24 hours of the meeting, with a requirement for logged meetings to be reviewed by a designated data steward if not entered within 24 hours, to ensure data quality is maintained.  
  Success criteria now mandates review of meetings logged later than 24 hours to maintain data quality, addressing earlier concerns around data integrity. _(C5)_

## Open questions for humans

### C6 · MINOR · does not block the build

**How will the system document the confirmation of scheduled meetings for compliance and audit purposes?**

- Why it matters: This documentation is essential to demonstrate that meetings occurred as reported, especially under audit scrutiny.
- Decision owner: Head of Compliance
- Options: Specify a method for documentation (e.g., emails, digital acknowledgments) / Utilize existing confirmation systems within the organization / Leave documentation methods ambiguous

## Tension report

The primary tension centered around the clarity of roles concerning data accuracy and security, particularly regarding who can access and log sensitive information. Throughout the discussions, the proposer worked to clarify responsibilities, while the critic raised concerns over potential gaps in data protection protocols, leading to some revisions but leaving an open question regarding compliance documentation.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 7 | 1 | 5 | 1 | 0.25 | 85 | 50 | CONTINUE | continue |
| 3 | 9 | 2 | 6 | 1 | 0.31 | 85 | 65 | CONTINUE | continue |
| 4 | 9 | 0 | 8 | 1 | 0.06 | 85 | 95 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): The delineation of roles and processes for data correction may evolve as organizational policies are clarified.
- Critic's remaining worry (95/100): Potential for unauthorized access to sensitive meeting details due to the classification of access rights.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | S5 states that only users with appropriate access rights can log and view meetings involving sensitive information, but it does not specify which roles have these rights or how those access levels are determined. |
| C2 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | S2 designates regional coordinators and project managers as primary users, but it doesn't clarify who is responsible for maintaining the accuracy of logged information or addressing errors in the logged details. |
| C3 | MAJOR | DEFINITIONS | S1 | R1 | REVISED | 0 | S1 defines automated logging but does not specify what constitutes 'key discussion points', leaving it open to interpretation and potential inconsistencies. |
| C4 | MINOR | OPERATIONS | X1 | R1 | REVISED | 0 | X1 states that informal meetings will not be logged, but it does not clarify how informal meetings will be distinguished from formal ones in the eyes of the system. |
| C5 | MINOR | DATA_QUALITY | K1 | R1 | REVISED | 0 | K1 sets a success criteria of 90% logging of meetings within 24 hours, but does not specify what happens when meetings are not logged within that timeframe and how that affects data quality assessments. |
| C6 | MINOR | COMPLIANCE | A2 | R1 | ESCALATED | 0 | A2 states that meetings must be scheduled and confirmed beforehand, but does not specify how this confirmation will be documented and maintained for compliance and audit purposes. |
| C7 | MAJOR | COMPLIANCE | A2 | R2 | REVISED | 0 | The proposal does not outline how to retain documentation regarding the confirmation of scheduled meetings, which is critical for compliance. |
| C8 | MAJOR | CONFIDENTIALITY | S5 | R3 | REVISED | 0 | The proposal still lacks clarity on the specific roles that have access to view logged meetings and the process for determining these access levels. |
| C9 | MAJOR | OWNERSHIP | S2 | R3 | REVISED | 0 | The proposal does not clarify the responsibility of the designated data steward in ensuring the accuracy of logged meeting information or how errors will be addressed. |
