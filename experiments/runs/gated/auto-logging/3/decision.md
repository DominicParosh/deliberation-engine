# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.008.

Challenges: 8 raised · 4 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

This release will implement an automated system for logging meetings with government officials in the Government CRM, focusing on capturing essential engagement history while ensuring data security and compliance measures are in place. It will benefit regional coordinators and project managers by enhancing the visibility and accuracy of interactions with government representatives. However, issues regarding data protection compliance protocols and user training requirements remain unresolved and need further deliberation.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automatically log meetings with government officials in the CRM.

**In scope**

- **S1** Meetings will be logged automatically whenever a user inputs meeting details into the CRM, including meeting date, time, location, participants (both internal and external), agenda, and minutes. Access to logged meetings will be restricted based on user roles; only users with 'regional coordinator' or 'executive-level staff' roles will have access to all meeting logs, while 'project managers' will only access logs relevant to their projects.  
  Automatic logging of meetings with defined access restrictions was included to mitigate risks of unauthorized access to sensitive information. _(C1)_
- **S2** The system will allow users to indicate the participants from the government side by selecting from a list of government officials that have been pre-loaded in the CRM.
- **S3** Automated logging will also include a status indicator (e.g., completed, canceled, rescheduled) for each meeting entry.
- **S4** Regional coordinators and project managers will have access to view the logged meeting data in the engagement history section of the CRM. Access permissions for meeting logs will be routinely updated and revoked as necessary when personnel change roles or exit the organization, ensuring that sensitive information remains secure.  
  The inclusion of regular updates to access permissions addresses accountability in maintaining meeting logs. _(C2)_
- **S5** Users will receive automated reminders to log meeting details immediately after a meeting has concluded.  
  Automated reminders encourage prompt logging of details, improving overall engagement tracking.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external calendar applications for automatic meeting logging.
- **X2** This release will not allow for the modification or deletion of logged meeting entries by users.
- **X3** This release will not implement advanced analytics or reporting features related to meeting history.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The system has existing access to all official government contacts and their details that can be logged during meetings. | Kept | never challenged |
| A2 | Users of the CRM are trained and authorized to input meeting information and have the authority to log engagements with government officials. | Kept | C6 → escalated; C8 → escalated |
| A3 | All users have access to the engagement history section of the CRM. | Kept | never challenged |
| A4 | Meeting information gathered will comply with relevant data protection regulations regarding sensitive government interactions. | Kept | C4 → escalated; C7 → escalated |

## Definitions

- **D1** "Meetings with government officials" means scheduled engagements between CRM users and representatives from government entities that are documented and logged within the CRM, specifically when the meeting addresses topics related to organizational projects, involving at least one member from the government side.  
  Defining 'meetings with government officials' reduces ambiguity and establishes clear logging criteria. _(C5)_
- **D2** "Engagement history" means the record of all interactions between CRM users and government officials, including logged meetings, correspondence, and any relevant notes.

## Success criteria

- **K1** At least 90% of scheduled meetings with government officials, defined as meetings that occur with at least one government representative present in which topics related to ongoing projects are discussed, are logged automatically, as measured by user input in the CRM over the first 6 months after release.  
  Clarifying the success criteria for logged meetings addresses concerns about measurement inconsistencies. _(C3)_

## Open questions for humans

### C7 · BLOCKER · blocks the build

**What detailed data protection protocols are in place for handling sensitive information logged in the CRM?**

- Why it matters: This is critical to ensure that any logged sensitive information complies with applicable laws and regulations.
- Decision owner: Head of Data Protection
- Options: Define protocols now / Delay protocol definition
- Proposer's last word (R3, defend, needs human decision): The data protection compliance protocols that govern the handling of sensitive information need to be defined by the relevant organizational authorities. This item must remain as is to allow for adherence to established compliance protocols.
- Critic's last word (R3, escalate): The proposal does not specify how compliance will be achieved, relying instead on human-defined protocols.

### C8 · BLOCKER · blocks the build

**What are the mandatory training or authorization processes for users who will log meetings in the CRM?**

- Why it matters: Establishing these processes is vital to ensure only qualified personnel log sensitive information.
- Decision owner: Project Management Office
- Options: Define training and authorization / Do not implement a training requirement
- Proposer's last word (R3, defend, needs human decision): The training and authorization processes for users must be established by the organization to ensure that all personnel are adequately prepared to log meeting details. This remains open for the organization to address.
- Critic's last word (R3, escalate): The specifics of training and authorization processes are not defined, and they must be established by the organization.

### C4 · MAJOR · blocks the build

**What specific data protection protocols will be implemented to ensure compliance in logging sensitive meeting information?**

- Why it matters: Clarifying data protection measures is critical to avoid legal violations and ensure sensitive information is handled appropriately.
- Decision owner: Head of Data Protection
- Options: Define security protocols now / Establish protocols later
- Proposer's last word (R2, defend, needs human decision): The specifics of data protection compliance protocols must be determined by the organization according to legal requirements and best practices.
- Critic's last word (R2, escalate): The specifics of data protection protocols require an organizational decision.

### C6 · MAJOR · blocks the build

**What are the mandatory training requirements and processes for allowing users to log meetings in the CRM?**

- Why it matters: Defining training processes is essential for ensuring data integrity and accountability across the system.
- Decision owner: Project Management Office
- Options: Establish specific training programs / Require no additional training
- Proposer's last word (R2, defend, needs human decision): The specifics of mandatory training and authorization processes for users logging meetings must be established by the organization as part of their compliance and operational procedures.
- Critic's last word (R2, escalate): The specifics of training and authorization processes must be established by the organization.

## Tension report

The primary disagreement focused on the lack of clear data protection compliance and user training protocols, which both parties recognized as critical yet unresolved aspects. The Proposer expressed confidence in implementing the feature but acknowledged the risks, while the Critic stressed the necessity for defined protocols to avoid legal and data integrity issues.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 85 | 40 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.53 | 70 | 40 | CONTINUE | continue |
| 3 | 8 | 0 | 4 | 4 | 0.53 | 70 | 40 | CONTINUE | converged |

- Proposer's remaining worry (70/100): The lack of defined compliance and training protocols raises significant risks for data integrity and security.
- Critic's remaining worry (40/100): Data protection and training processes remain undefined, risking legal violations and data inaccuracies.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S4 | R1 | REVISED | 0 | The proposal does not specify how to safeguard sensitive information captured about government officials during logged meetings, which could lead to unauthorized access. |
| C2 | MAJOR | OWNERSHIP | S4, S5 | R1 | REVISED | 0 | The proposal does not clarify ownership and accountability for maintaining and updating meeting logs especially when personnel change roles or leave, running the risk of outdated or inaccessible records. |
| C3 | MAJOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The success criteria of '90% of meetings logged automatically' uses a vague metric that could be misinterpreted or manipulated without clear definitions of what constitutes a logged meeting. |
| C4 | MAJOR | COMPLIANCE | A4 | R1 | ESCALATED | 0 | The assumption about compliance with data protection regulations is vague and does not outline how the system will adhere to these requirements during data capture and storage. |
| C5 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'Meetings with government officials' is vague and does not specify the circumstances under which these meetings should be logged, leaving room for interpretation. |
| C6 | MAJOR | OWNERSHIP | A2 | R1 | ESCALATED | 0 | The proposal does not specify how users are to be trained and authorized to input meeting information, leaving a potential gap in data integrity and accountability. |
| C7 | BLOCKER | COMPLIANCE | A4 | R2 | ESCALATED | 0 | Data protection compliance protocols are undefined, which risks legal violations when logging sensitive information. |
| C8 | BLOCKER | OWNERSHIP | A2 | R2 | ESCALATED | 0 | Training and authorization processes for users are unspecified, risking mismanagement or incorrect logging of meetings. |
