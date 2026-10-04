# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 4 rounds (policy `gated`) · $0.011.

Challenges: 10 raised · 7 settled between the agents · 3 handed to humans · 0 still open when it ended.

## Summary

This release will implement an alert system in the Government CRM to notify users when engagement with a country contact has not occurred for 6 months. However, the system will not include proactive follow-up actions, engagement analysis, or alerts for individual team members. Decisions still need to be made regarding user access to the alert system and how to ensure compliance with data protection laws.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** The system will send an alert to designated users when there has been no engagement with a country contact for 6 months.  
  The alert threshold was set at 6 months of no recorded engagement to effectively monitor relationships without overwhelming users with frequent alerts.

**In scope**

- **S1** The system will automatically update alert recipients when users change roles or leave the organization, ensuring alerts are sent only to current managers of that country contact.  
  Revised to specify that the system will automatically update alert recipients based on user role changes, addressing concerns about outdated alert recipients. _(C3)_
- **S2** The alert will include the country name, contact details, and the last date of recorded engagement.  
  The alert will include essential information such as the country name and last engagement date, ensuring users have relevant context without compromising sensitive data.
- **S3** The system will include a mechanism for users to establish threshold triggers based on the number of engagement alerts received, minimizing alert fatigue by consolidating alerts for less critical situations.  
  A mechanism for minimizing alert fatigue was added, allowing users to establish threshold triggers for alerts, thus ensuring important alerts are more noticeable. _(C5)_
- **S4** Regional coordinators and project managers will be the primary users receiving these alerts.  
  Regional coordinators and project managers were identified as primary users to effectively manage country relationships without unnecessary exposure of sensitive contacts, which is a concern. _(C1)_
- **S5** An audit log will be maintained to track when alerts are sent and to which users, and the responsibility for maintaining data quality of engagement logs will lie with designated project managers for their respective country contacts.  
  It clarifies that designated project managers are responsible for maintaining the quality of engagement logs, ensuring accurate alert generation. _(C7)_

## What it will not do

**Out of scope for this release**

- **X1** The release will not include proactive actions or suggestions for following up with the country contacts after the alert is received, leaving follow-up actions to the discretion of users.  
  The decision not to include follow-up actions clarifies that follow-up responsibility lies with users, establishing clear expectations for engagement. _(C6)_
- **X2** The system will not analyze reasons for decreased engagement or categorize types of engagements.  
  The system will not analyze reasons for engagement decline to limit scope and complexity, focusing instead on alert generation based on user-defined periods of inactivity.
- **X3** The release will not implement alerts for individual team members, only for designated roles (regional coordinators and project managers).  
  Deciding not to implement alerts for individual team members keeps the system focused on key relationship managers, preventing unnecessary complexity.
- **X4** The alert system will not include sensitive country contacts in alerts, ensuring that alerts are restricted to non-sensitive country contacts only as defined by designated project managers.  
  Out of scope to include sensitive contacts in alerts was established to maintain confidentiality and avoid potential breaches of sensitive information. _(C9)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that engagement is tracked through logged calls, meetings, or emails in the CRM; the request depends on having a clear definition of 'engagement'. | Kept | never challenged |
| A2 | It is assumed that the organization has a standard protocol for relationship management that justifies the need for cold alerts; the request assumes familiarity with this protocol. | Kept | never challenged |
| A3 | It is assumed that users of the CRM have necessary permissions to access contact histories; the request depends on current user permissions being appropriate. | Kept | never challenged |

## Definitions

- **D1** 'Cold' means a period of 6 months without any recorded engagement (contacts or meetings) logged in the CRM, excluding informal communications such as internal discussions or unlogged emails.  
  Changed to clarify that 'cold' engagement consists of no logged interactions for 6 months, thus preventing confusion over what counts as engagement. _(C2)_
- **D2** 'Engagement' means any logged interaction, such as meetings, phone calls, or emails with country contacts.  
  'Engagement' was defined specifically as logged interactions, which addresses potential misunderstandings and ensures clarity.
- **D3** 'Users' refers specifically to regional coordinators and project managers who manage country relationships within the CRM.  
  Defined 'users' specifically to eliminate ambiguity about who will receive alerts, which are only the designated role holders.
- **D4** 'Engagement logs' mean any documented record of an interaction with a country contact that is formally logged in the CRM, including entries that detail date, type, and subject of communication such as meetings, phone calls, or emails.  
  Clarified what constitutes an engagement log to ensure that only formal interactions are counted, reducing potential errors in the alert system. _(C10)_

## Success criteria

- **K1** At least 80% of users report receiving alerts in a timely manner (measured through user feedback surveys conducted 1 month after release).  
  Success criteria of timely alerts were established to evaluate user satisfaction and system effectiveness after release.

## Open questions for humans

### C1 · MAJOR · blocks the build

**Who else besides regional coordinators and project managers can access the alert system?**

- Why it matters: This is crucial to prevent unauthorized access to sensitive information, which could lead to potential confidentiality breaches.
- Decision owner: Head of User Access Management
- Options: Define access criteria for additional roles / Limit access to only designated roles

### C4 · MAJOR · blocks the build

**What criteria will be used to filter out sensitive contacts from alerts?**

- Why it matters: Establishing filtering criteria is essential to maintain confidentiality and prevent risks associated with sensitive information exposure.
- Decision owner: Head of Data Protection
- Options: Create a list of sensitive contacts / Implement a tagging system for sensitive interactions

### C8 · MAJOR · blocks the build

**What measures are in place to ensure compliance with data protection laws?**

- Why it matters: Ensuring compliance with data protection is critical to safeguard personal data and avoid legal repercussions for the organization.
- Decision owner: Chief Compliance Officer
- Options: Conduct a data protection impact assessment / Develop a compliance checklist for the alert system

## Tension report

The primary disagreement centered around the need for clear filtering mechanisms for sensitive contacts to prevent possible confidentiality breaches. While the Proposer focused on implementing the alert system efficiently, the Critic expressed concern about the unresolved issues related to data protection compliance and user access, which were elevated to open questions.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.53 | 75 | 45 | CONTINUE | continue |
| 3 | 10 | 2 | 5 | 3 | 0.53 | 75 | 60 | CONTINUE | continue |
| 4 | 10 | 0 | 7 | 3 | 0.32 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): The implementation must ensure that sensitive contacts are effectively filtered to prevent confidentiality breaches.
- Critic's remaining worry (85/100): There are unresolved escalated challenges surrounding data protection compliance that could impact user trust.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S4 | R1 | ESCALATED | 0 | The proposal does not address who else might potentially need access to the alert system beyond regional coordinators and project managers, potentially exposing sensitive information to unauthorized users. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'cold' engagement could lead to misunderstandings; there is no clear distinction of what constitutes a valid engagement that can be logged, impacting the accuracy of alerts. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | REVISED | 0 | The proposal does not specify what happens to alerts when users change roles; alerts may continue to be sent to former users who no longer manage those relationships. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R1 | ESCALATED | 0 | There is no mention of handling sensitive contacts that should not appear in alerts, which can lead to situations where confidential information is inadvertently exposed. |
| C5 | MAJOR | OPERATIONS | S3 | R1 | REVISED | 0 | The system does not address the potential for alert fatigue, risking complacency and unresponsiveness to important alerts. |
| C6 | MINOR | OPERATIONS | X1 | R1 | REVISED | 0 | While the proposal outlines the alert feature, it does not provide a process for following up on alerts, which could leave users without clear next steps. |
| C7 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The responsibilities for maintaining data quality of engagement logs are not mentioned, which could lead to incorrect firing of alerts. |
| C8 | MAJOR | COMPLIANCE | GAP | R2 | ESCALATED | 0 | The proposal lacks detail on how the alert system will comply with data protection laws regarding personal data from country representatives. |
| C9 | MAJOR | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal does not address how to prevent sensitive contacts from being included in alerts, risking confidentiality breaches. |
| C10 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal lacks a clear definition of engagement logs and the specific actions that qualify as engagements, which could lead to misunderstandings and inaccuracies in alert causation. |
