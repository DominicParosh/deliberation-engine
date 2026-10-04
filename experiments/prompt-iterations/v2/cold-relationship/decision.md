# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.009.

## Summary

The release will build an alert system to notify users when engagement with a country representative has not occurred for three months. It will provide features for users to take action based on these alerts. However, the actual processes for managing assignments and ensuring compliance with data protection remain points of concern that still need addressing.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide timely alerts to users about cold relationships with country representatives.  
  Provides timely alerts regarding cold relationships with country representatives, ensuring users are promptly informed.
- **V2** Enable users to take action based on the alerts to rekindle relationships.  
  Enables users to take necessary action based on alerts to revive relationships with counterparts.

**In scope**

- **S1** Define a 'cold' relationship as a lack of engagement (no recorded communication) for 3 months.  
  Defined a 'cold' relationship as a lack of engagement for 3 months, making the alert system proactive and actionable for users. _(C2)_
- **S2** Implement an automated alert notification system that sends email alerts to regional coordinators and project managers about cold relationships, instructing them to initiate follow-up communications.  
  An automated alert notification system will send alerts specifically to authorized users only, thus protecting sensitive information. _(C1, C7)_
- **S3** Users will receive alerts every month for each country deemed to have a cold relationship.  
  Users will receive monthly alerts about countries with cold relationships, ensuring ongoing awareness.
- **S4** Create a dashboard view that lists countries with cold relationships along with the last engagement date and designate regional coordinators to maintain it.  
  Clarified the responsibility for maintaining the dashboard, ensuring accurate information for users regarding cold relationships. _(C3)_
- **S5** Establish a process that automatically reassigns alert notifications and access rights to a specified backup user or team when users change roles or exit the organization.  
  Included a process for reassigning alerts when users change roles or exit the organization, addressing potential data security risks. _(C5, C9)_
- **S6** Implement a process for identifying and managing duplicate engagement records in the CRM.  
  Implemented a process for managing duplicate engagement records, enhancing data quality and alert accuracy. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include customizable alert thresholds for what counts as a cold relationship.
- **X2** This release will not track individual user engagements or notifications based on specific user actions.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users maintain accurate and up-to-date engagement records in the CRM. | The alert system relies on the correctness of engagement data to trigger alerts. | Accepted (never challenged) |
| A2 | Emails can be sent from the CRM system without compliance issues or technical barriers. | The alert system proposed involves email notifications, which require an operational email function. | Accepted (never challenged) |
| A3 | Users have regular access to email notifications and the dashboard to respond to alerts in a timely manner. | The effectiveness of alerts assumes users will notice and act on the notifications received. | Accepted (never challenged) |

## Definitions

- **D1** "cold relationship": A relationship with a country representative that has no recorded engagement for a period of 3 months.  
  Defined 'cold relationship' as no engagement for a period of 3 months, allowing for timely interactions with counterparts.
- **D2** "alert notification system": An automated system that sends email notifications to designated users about events defined as cold relationships.  
  An 'alert notification system' is defined as an automated system for sending notifications about cold relationships to users.
- **D3** "engagement record": Any logged interaction within the CRM that signifies communication or meeting with a country representative.  
  Defined 'engagement record' as any logged interaction within the CRM ensuring clarity on what constitutes engagement.

## Success criteria

- **K1** Number of alert notifications sent: target At least 80% of country representatives with cold relationships trigger alerts per month. (Measured by the number of alerts logged in the system against the total count of countries with cold relationships; records must be retained for a maximum of 1 year after being classified as cold.)  
  Introduced a compliance measure defining record retention for engagement data after being classified as cold, addressing data privacy concerns.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement centered on the clarity of roles and responsibilities in managing alerts, particularly regarding who can view alerts and what actions should follow upon receiving them. Although the final proposal addresses many concerns, both the Proposer and the Critic expressed lingering worries about the practical enforcement and tracking of reassignments.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 6 | 2 | 4 | 0 | 0.33 | 80 | 70 | CONTINUE | continue |
| 3 | 8 | 2 | 6 | 0 | 0.25 | 80 | 60 | CONTINUE | continue |
| 4 | 9 | 1 | 8 | 0 | 0.11 | 85 | 70 | CONTINUE | continue |
| 5 | 9 | 0 | 9 | 0 | 0.00 | 75 | 75 | CONTINUE | converged |

- Proposer's remaining worry (75/100): There may still be ambiguities regarding how reassignments will be tracked and enforced in practice.
- Critic's remaining worry (75/100): Still unclear who can view alerts and what actions are required after receiving them.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | S1 defines a 'cold' relationship based on no engagement for 6 months but does not specify who can access information about these cold relationships. |
| C2 | BLOCKER | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'cold relationship' as having no engagement for 6 months may not provide a clear or actionable threshold for users. |
| C3 | MAJOR | OWNERSHIP | S4 | R1 | REVISED | 0 | S4 states that a dashboard view will be created, but it lacks clarity on who is responsible for maintaining and updating the dashboard information. |
| C4 | MINOR | COMPLIANCE | K1 | R1 | REVISED | 0 | K1 introduces a criterion based on alert notifications sent but does not address compliance with data retention policies for engagement records. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not address the implications of users changing roles or leaving the organization regarding access to alerts and data. |
| C6 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal does not specify how the system will handle duplicate engagement records or inaccuracies in records. |
| C7 | MAJOR | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal does not define who can view the alerts about cold relationships, which poses a risk of unauthorized access to sensitive information. |
| C8 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not specify what actions users should take upon receiving an alert about a cold relationship, which is crucial for ensuring timely and effective follow-up. |
| C9 | MAJOR | OWNERSHIP | GAP | R4 | REVISED | 0 | The proposal does not clarify how alerts will be reassigned to others when users change roles or leave the organization, which may lead to missed alerts and unaddressed cold relationships. |
