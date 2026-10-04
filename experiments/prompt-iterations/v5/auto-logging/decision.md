# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.005.

## Summary

This release will automate the logging of meetings with government officials in the Government CRM, ensuring that engagement history is accurately captured and easily accessible for users while clarifying confidentiality roles, retention policy, and handling of user transitions. Key commitments include automating meeting logs and providing a user-friendly interface for interactions. However, the question of compliance with data protection laws remains unresolved and will need further clarification before implementation can begin.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automate the logging of meetings with government officials into the engagement history.  
  Automating meeting logging is essential for accurately capturing engagement history, addressing the initial feature request while optimizing user experience through automation.
- **V2** Provide an easy-to-use interface for users to view, edit, and confirm logged meetings.  
  Providing an easy-to-use interface ensures that users can effectively manage their meeting records, aligning with user needs for access and verification of stored information.

**In scope**

- **S1** Automatically log meetings when a user inputs meeting details through a standardized form, allowing only users with the roles of regional coordinator, project manager, and executive-level staff to view the automatically logged meetings. Meetings flagged as sensitive include those marked as diplomatic or confidential by authorized users in the CRM, ensuring that only users with appropriate clearance can access these logs.  
  Access restrictions were clarified to include only specified roles, thus addressing confidentiality concerns about who can view sensitive meetings. _(C1, C4)_
- **S2** Enable users to select government officials from the CRM database when creating meeting logs.  
  Enabling selection of government officials from the CRM is critical for seamless logging and maintaining engagement accuracy.
- **S3** Implement a user interface that allows users to view and confirm automatically logged meetings.  
  An interface for viewing and confirming meetings supports user engagement and reliability of logged data.
- **S4** Ensure that logged meetings include relevant details such as date, time, participants, and agenda. Additionally, a process will be established to transfer or archive meeting logs contributed by users leaving the organization, ensuring continuity and accountability.  
  Proactive measures to manage user transitions help maintain historical data integrity and accountability when team members leave. _(C6)_
- **S5** Notify users of successful logging of meetings via an in-system notification.  
  User notifications upon successful logging promote transparency and user engagement with the system.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integrations with third-party calendar applications for automatic logging.  
  Third-party calendar integrations were excluded to maintain focus on core functionality and data security issues.
- **X2** The release will not implement any analytics on engagement history at this stage.  
  Analytics capabilities were dropped due to prioritization of essential logging features in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to the Government CRM and permission to log meetings. | Kept | never challenged |
| A2 | Government officials' contact details and engagement history are already stored in the CRM. | Kept | never challenged |
| A3 | Users are comfortable with using digital forms to log meetings. | Kept | never challenged |
| A4 | The organization's data retention policies dictate that meeting logs will be retained for a period of 5 years, after which they will be archived or deleted unless otherwise specified by regulatory requirements. | Kept | C2 → escalated; C5 → revised |

## Definitions

- **D1** "Automatically log meetings" means that once a user inputs meeting details into the system, the meeting is recorded in the engagement history without additional manual input. If meeting details are not inputted correctly, an error notification will inform the user to correct the information. In the event a meeting is canceled, no record will be created in the engagement history.  
  Clarifying the conditions under which meetings are logged prevents inaccuracies, protecting sensitive information and engagement history integrity. _(C3)_
- **D2** "Engagement history" means a chronological record of all interactions and meetings with government officials and their respective details stored in the CRM.  
  Defining engagement history ensures all pertinent interactions are systematically recorded and retrievable within the CRM system.

## Success criteria

- **K1** At least 90% of meetings logged within 24 hours of occurrence, measured by system logs.  
  Setting a success criterion for timely logging ensures the system is effectively capturing meeting occurrences as intended.
- **K2** User satisfaction rating of 85% or higher regarding the ease of logging meetings after the feature release, measured through a post-release survey.  
  A user satisfaction standard reflects the effectiveness and usability of the new logging feature, emphasizing user experience post-release.

## Open questions for humans

### C2 · MAJOR · blocks the build

**What legal and policy checks are in place to govern the logging of meetings, particularly regarding compliance with data protection laws?**

- Why it matters: Clarifying ownership for compliance checks is essential to prevent potential legal violations that could arise from logging meetings improperly.
- Decision owner: Head of Data Protection
- Options: Establish clear compliance protocols / Identify responsible roles for compliance checks / Integrate compliance checks into the logging process

## Tension report

The main disagreement centered on ownership and compliance with data protection laws, particularly regarding the assumption of legal constraints in logging meetings. While the proposer focused on the feature's implementation, the critic emphasized the necessity for clear accountability in compliance, which currently remains unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 3 | 2 | 1 | 0.64 | 80 | 60 | CONTINUE | continue |
| 3 | 6 | 0 | 5 | 1 | 0.14 | 80 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring compliance with legal and data retention requirements may be challenging without clear feedback mechanisms.
- Critic's remaining worry (85/100): The definition of sensitive meetings and the process for user transitions must be clear to prevent unauthorized access.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | S1 does not clarify which roles can view automatically logged meetings, risking exposure of sensitive information to unauthorized users. |
| C2 | MAJOR | OWNERSHIP | A4 | R1 | ESCALATED | 0 | The assumption A4 states there are no legal or policy constraints, but does not clarify who is responsible for ensuring compliance with data protection laws regarding meeting logging. |
| C3 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | D1's definition of "automatically log meetings" is unclear; it does not specify what happens if meeting details are not inputted correctly or if the meeting is canceled. |
| C4 | BLOCKER | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | There is no clarification on how sensitive meetings are identified and protected, risking exposure of sensitive information to unauthorized users. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | There is no answer regarding how long meeting logs are retained in the system, posing risks to data retention policies. |
| C6 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not outline the process for ensuring contributions to meeting logs from users who leave the organization are preserved or transferred. |
