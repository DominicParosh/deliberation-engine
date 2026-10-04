# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.006.

## Summary

This release will implement an alert system that notifies designated users when no engagement has occurred with a country for 90 days, including defined permissions for access and processes for ownership. It will send alerts to users, track engagement history, and maintain logs of alerts, while users can configure alert thresholds. The system will not analyze reasons for cold relationships or suggest actions based on them, and there are unresolved decisions around adjusting the alert threshold based on diplomatic context.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** The system will send alerts to users when relationships with countries have no recorded engagement for 90 days.  
  The decision to send alerts after 90 days of inactivity ensures a clear, measurable threshold for engagement while enabling users to respond promptly.

**In scope**

- **S1** The system will track engagement history defined as any logged communication or interaction with government contacts.  
  This item was included because tracking engagement history is vital for the overall function of the alert system.
- **S2** The system will send automated email notifications to designated regional coordinators and project managers after 90 days of inactivity.  
  Automated email notifications are necessary to ensure that responsible users are informed in real-time about cold relationships.
- **S3** Users will have the capability to configure the alert threshold (defaulting to 90 days) within their user settings.  
  Allowing users to configure alert thresholds acknowledges the diverse operational contexts while maintaining a default setting for consistency.
- **S4** The system will maintain a log of alerts sent, including timestamps and recipients, for audit purposes.  
  Maintaining a log of alerts supports transparency and accountability within the organization regarding diplomatic engagement.
- **S5** The system will assign permissions for users to access engagement history and receive cold alerts based on their role. Only users with a clearance level defined as 'Regional Coordinator' or 'Project Manager' will be eligible to receive alerts and view related engagement history.  
  Defining permissions for alert access reduces the risk of sensitive information exposure to unauthorized individuals, addressing confidentiality concerns. _(C1)_
- **S6** The system will have an automated process that reassigns alert responsibilities to a designated backup user within the same team when a primary user leaves the organization or changes roles. The administrator will be notified to confirm the reassignment.  
  The automated process for reassigning alert responsibilities ensures continuity in oversight and mitigates risks from personnel changes. _(C2)_
- **S7** If a designated user is unavailable, alerts will be escalated to their immediate supervisor or assigned backup user who will be responsible for following up on the alert.  
  This process maintains responsibility for alerts even when designated users are unavailable, ensuring that no critical engagements fall through the cracks. _(C4)_
- **S8** The system will validate existing engagement records for completeness and accuracy before sending alerts. Alerts based on incomplete or inaccurate records will be flagged for review, and only validated accounts will trigger notifications.  
  Establishing safeguards against alerts based on incomplete data protects against possible breaches of sensitive information and promotes data validity. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not provide a way to analyze reasons for the cold relationship.  
  The decision not to analyze reasons for cold relationships keeps the scope focused and manageable, focusing on engagement tracking instead.
- **X2** The release will not include features to automatically re-engage or suggest actions based on cold relationships.  
  Excluding automatic re-engagement suggestions allows the team to maintain a direct human approach in managing diplomatic relationships, which could be sensitive.
- **X3** The system will not alert on relationships with countries where no past engagement history exists.  
  Not alerting on relationships with no past history prevents unnecessary notifications concerning unknown contexts.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users are responsible for logging their engagements with government contacts promptly, which is crucial for maintaining accurate engagement history. | Kept | never challenged |
| A2 | The organization has existing protocols for user email notifications that must be adhered to, which underpins the alert system. | Kept | never challenged |
| A3 | Designated users will have access to the CRM system with necessary permissions to configure alert settings. | Kept | never challenged |

## Definitions

- **D1** 'Goes cold' means a period of 90 consecutive days without any recorded engagement in the system.  
  Defining 'goes cold' as 90 days sets a clear expectation for engagement inactivity, contributing to consistent application of the alert system.
- **D2** 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM.  
  Clarifying 'engagement' aligns the definition with expected operational practices ensuring consistent documentation across users. _(C3)_
- **D3** 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM, including the date, participants, communication method (e.g., email, call, meeting), and summary of the discussion.  
  This detailed definition of engagement prevents ambiguity and reduces the likelihood of incorrect logging of interactions. _(C3)_

## Success criteria

- **K1** At least 80% of the alerts should be acknowledged by the relevant users within 48 hours of receipt, measured by log records of user engagement.  
  Setting a success criterion of 80% acknowledgment of alerts within 48 hours ensures that the system maintains effectiveness and responsiveness.

## Open questions for humans

### C4 · MAJOR · does not block the build

**What procedures will be established for addressing alerts if a designated user is unavailable?**

- Why it matters: This is crucial to ensure that cold relationships are monitored and acted upon, maintaining diplomatic ties without gaps in oversight.
- Decision owner: Regional Managers
- Options: Define specific roles for follow-up / Establish a team-based alert follow-up process

### C6 · MINOR · does not block the build

**Is there a process to review and potentially adjust the default alert threshold of 90 days based on specific diplomatic contexts?**

- Why it matters: Adjusting this threshold may be vital in sensitive situations, ensuring that alerts remain relevant and do not prompt unnecessary escalations.
- Decision owner: Head of Operations
- Options: Establish a review committee / Set a protocol for threshold adjustments

## Tension report

The main disagreement arose over how to manage alerts during periods of user unavailability and the need for a flexible alert threshold due to the sensitivity of diplomatic contexts. The critic emphasized the necessity for a defined process for the threshold adjustment, while the proposer maintained that discretion was essential, leading to unresolved open questions.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 0 | 4 | 2 | 0.25 | 85 | 75 | CONTINUE | converged |

- Proposer's remaining worry (85/100): I am concerned about how effectively the responsibilities will be reassigned when users leave or change roles.
- Critic's remaining worry (75/100): The lack of a defined process for adjusting the alert threshold could lead to inappropriate notifications in sensitive diplomatic situations.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There are no defined permissions for who can see engagement history or receive alerts, risking exposure of sensitive diplomatic information to unauthorized personnel. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | There is no clear process in place detailing what happens when designated users change roles or leave the organization, potentially losing oversight of cold engagement alerts. |
| C3 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The term 'engagement' is vaguely defined and does not specify the required documentation style or level of detail needed for proper logging, which can lead to inconsistencies. |
| C4 | MAJOR | OPERATIONS | GAP | R1 | ESCALATED | 0 | The proposal does not address how ongoing engagement initiatives will be managed, especially concerning users who may be unavailable when alert notifications are sent. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There are no defined safeguards to prevent sending alerts based on incomplete or inaccurate engagement records that could expose sensitive information. |
| C6 | MINOR | DEFINITIONS | GAP | R1 | ESCALATED | 0 | The proposal does not specify how the default alert threshold of 90 days may pose risks in situations where rapid diplomatic engagement is critical. |
