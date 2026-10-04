# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.012.

Challenges: 10 raised · 8 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

This release will introduce an automated logging feature for meetings with government officials, aimed primarily at regional coordinators and project managers. The feature will log meetings automatically while implementing safeguards for access control to protect sensitive information. However, unresolved questions regarding the management of user access rights during role transitions need to be addressed before further progress can be made.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automatically log meetings with government officials in the system.  
  This commitment reflects the need to automate the logging of meetings to prevent loss of engagement history.

**In scope**

- **S1** Implement an integration that automatically logs meetings held by regional coordinators and project managers with government officials into the CRM. In case of a failure in automated logging, users will receive a prompt to manually log the relevant meetings.  
  Inclusion of a manual logging prompt ensures that important meetings are not lost if automated logging fails. _(C5)_
- **S2** Provide a user interface for regional coordinators and project managers to view automatically logged meetings. Users will also have the option to confirm the accuracy of logged details through a verification process.  
  The addition of a verification process allows users to confirm the accuracy of logged details, enhancing data quality. _(C6)_
- **S3** Ensure that logged meetings include contact details of government officials, date, time, and meeting summary. Access to view contact details will be restricted to only regional coordinators, project managers, and executive-level staff, where access rights will be assigned based on user roles. Access rights associated with a user will be revoked automatically when the user leaves the organization, and a manager will review and update access rights whenever a user changes roles.  
  The outlined access restrictions comply with confidentiality requirements by specifying who can view sensitive information. _(C1, C8, C10)_

## What it will not do

**Out of scope for this release**

- **X1** The feature will not include logging meetings that are informal or not formally scheduled by regional coordinators and project managers, such as casual discussions without a defined purpose.  
  Informal meetings are excluded from logging to maintain clarity and relevance in engagement history. _(C3)_
- **X2** The feature will not integrate with other calendar or scheduling tools in this release.  
  Integration with other tools is excluded to keep the release focused on the core functionality.
- **X3** This release does not include notifications or alerts related to the logged meetings.  
  Notifications related to logged meetings are out of scope at this time to prioritize essential features.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have the necessary access rights to log meetings in the CRM, which is needed for successful logging. | Kept | C2 → escalated; C7 → escalated |
| A2 | All meetings with government officials will be conducted either in person or virtually, as the logging will depend on meeting type. | Kept | never challenged |
| A3 | Data privacy policies allow automatic logging of meetings with government officials. | Kept | never challenged |

## Definitions

- **D1** "Automatically log" means that the system will capture and store meeting information without manual input required from the user at the time of the meeting.  
  The definition clarifies the level of automation in meeting logs to set expectations for users.
- **D2** "Engagement history" means the record of all interactions with government officials, including meetings, contacts, and activities, as stored in the CRM.  
  Defining 'engagement history' emphasizes the importance of maintaining detailed records of interactions.
- **D3** "Formal scheduled meeting" means a meeting that is planned in advance, has a clear agenda, and is documented in the CRM system or a similar scheduling platform, ensuring that it is recognized as an official engagement.  
  The revised definition of formal meetings reduces the risk of logging informal discussions, clarifying what can be logged. _(C9)_

## Success criteria

- **K1** By the end of the quarter, the system should successfully log at least 95% of scheduled meetings, defined as meetings that are formally scheduled on the calendar and have a specified agenda, as confirmed through user checks.  
  The success criterion was revised to ensure clear measurement of logging success based on scheduled meetings. _(C4)_

## Open questions for humans

### C2 · MAJOR · blocks the build

**What specific organizational policies will govern the management of user access rights during role changes?**

- Why it matters: Clarifying these policies is crucial to prevent unauthorized access to sensitive information post-role transitions.
- Decision owner: Head of Data Protection
- Options: Define a process with clear roles and responsibilities / Allow IT department to manage access rights automatically / Review access rights on an ad-hoc basis

### C7 · MAJOR · blocks the build

**How will access rights be specifically assigned and managed when users change roles?**

- Why it matters: Without a defined process, there is a risk of unauthorized logging or access to sensitive information.
- Decision owner: Head of Data Protection
- Options: Create a structured role transition protocol / Implement automatic revocation of access during transitions / Regular audits of user access rights

## Tension report

The primary disagreement between the Proposer and Critic centered on the clarity and management of user access rights during role changes. While safeguards were improved in the proposal, the Critic highlighted potential risks that remain unresolved and depend on further policy definitions.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 7 | 1 | 5 | 1 | 0.27 | 80 | 70 | CONTINUE | continue |
| 3 | 9 | 2 | 5 | 2 | 0.45 | 80 | 40 | CONTINUE | continue |
| 4 | 10 | 1 | 7 | 2 | 0.27 | 70 | 60 | CONTINUE | continue |
| 5 | 10 | 0 | 8 | 2 | 0.18 | 85 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring that user access rights are effectively managed during transitions could present operational challenges.
- Critic's remaining worry (80/100): While safeguards have improved, there is still a risk of unauthorized access if role transitions aren't managed perfectly.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | S3 states that logged meetings will include contact details, but it does not specify who can see this sensitive information and what safeguards are in place to protect it. |
| C2 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | A1 assumes users will have access rights necessary for logging meetings, but it does not specify how access rights are managed or are granted, especially in the event of role changes. |
| C3 | MAJOR | DEFINITIONS | X1 | R1 | REVISED | 0 | X1 excludes logging meetings not conducted by regional coordinators and project managers, but does not define how these roles are determined and what the threshold is for an official meeting. |
| C4 | MAJOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The success criteria K1 mentions logging 95% of meetings but does not clarify the definition of 'scheduled meetings' and how this is measured accurately. |
| C5 | MAJOR | OPERATIONS | S1 | R1 | REVISED | 0 | S1 states that the system will log meetings automatically, but does not address what happens if the automated logging fails or does not occur due to technical issues. |
| C6 | MAJOR | DATA_QUALITY | S2 | R1 | REVISED | 0 | S2 provides a user interface for viewing logged meetings but does not specify how users can verify the accuracy of these logs. |
| C7 | MAJOR | OWNERSHIP | A1 | R2 | ESCALATED | 0 | A1 states users will have the necessary access rights, but it does not detail how these rights are assigned. This could lead to unauthorized logging or access after role transitions. |
| C8 | BLOCKER | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The access control for sensitive meeting logs lacks definitive guidelines, raising concerns on who can view potentially sensitive information. |
| C9 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The term 'scheduled meetings' is vague and needs extra definition to avoid ambiguity in what constitutes a formal meeting. |
| C10 | MAJOR | OWNERSHIP | GAP | R4 | REVISED | 0 | The proposal does not clarify how access rights are assigned, particularly regarding scenarios when users change roles or leave. This could lead to unauthorized access or logging of meetings by individuals who no longer hold the relevant position. |
