# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.006.

## Summary

The release will implement a notification system that alerts users when engagement with a country has significantly decreased, with specific safeguards around sensitive diplomatic relationships. Users will receive alerts when no contact has been made with a country for 90 days, and a dashboard feature will display engagement metrics. Final decisions around user adherence to protocols will require ongoing oversight from management.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users will receive alerts when no contact has been made with a country for a defined period.  
  Users will receive alerts when no contact has been made with a country for a defined period, ensuring notifications are timely and relevant.
- **V2** The system will provide a dashboard feature to display engagement metrics and recent interactions.  
  The system will provide a dashboard feature to display engagement metrics and recent interactions, supporting user awareness of relationship status.

**In scope**

- **S1** The system will track engagement as interactions such as emails, meetings, and official correspondence recorded by users.  
  The system will track engagement as interactions such as emails, meetings, and official correspondence recorded by users, capturing a comprehensive interaction history.
- **S2** An alert will be triggered when there are no recorded interactions with a country for 90 days.  
  An alert will be triggered when there are no recorded interactions with a country for 90 days, ensuring the notification system is built around a clear metric that users understand. _(C1)_
- **S3** S3: Regional coordinators and project managers will receive email notifications regarding cold relationships, only when there are no ongoing diplomatic negotiations or sensitive discussions related to the country. Access to engagement history for each country will be limited to the user's designated team, with appropriate permissions required to view engagements from other teams.  
  Access to engagement history for each country will be limited to the user's designated team, with appropriate permissions required, preventing unauthorized exposure of sensitive information. _(C4)_
- **S4** A dashboard will be implemented that displays engagement history with each country, including last interaction date.  
  A dashboard will be implemented that displays engagement history with each country, including the last interaction date, offering a visual representation of engagement.
- **S5** S5: The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators. If a user changes roles or leaves the organization, a designated manager will be assigned to maintain the records associated with that user's engagements, ensuring data is properly updated to reflect active diplomatic relationships.  
  The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators, thus enhancing accountability in data management. _(C3, C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not involve changing how user interactions are recorded in the CRM.
- **X2** Real-time engagement assessments based on live data will not be included in this release.
- **X3** The alerts will not include recommendations for re-engagement strategies.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to a history of interactions and will be able to log new ones, which depends on their existing permissions. | Kept | never challenged |
| A2 | Email notifications can be sent from the CRM system, which depends on the organization's email infrastructure. | Kept | never challenged |
| A3 | Users understand the importance of logging engagements, which depends on their training and organizational culture. | Kept | never challenged |
| A4 | The CRM data reflects accurate engagement activities, which depends on user diligence in recording. | Kept | never challenged |

## Definitions

- **D1** D1: 'cold relationship' means no recorded engagement interaction with a country for 90 consecutive days, without any ongoing diplomatic negotiations or sensitive discussions occurring during that time. The system will restrict alerts for cold relationships in situations where sensitive discussions are taking place, ensuring that alerts do not expose the organization to confidentiality breaches.  
  The definition of 'cold relationship' clarifies that ongoing diplomatic negotiations invalidate the cold relationship status, preventing misinterpretation of alert significance. _(C2)_
- **D2** "alert" means a notification sent by email to designated users informing them of a cold relationship.  
  'Alert' is clearly defined as a notification sent by email to designated users informing them of a cold relationship, which is crucial for user understanding.
- **D3** "dashboard" means a visual interface within the CRM that displays metrics related to engagement with countries, including last engagement date and total interactions.  
  'Dashboard' is defined as a visual interface within the CRM that displays metrics related to engagement, ensuring clarity in functionality for users.

## Success criteria

- **K1** At least 75% of users report the alerts are timely and useful, measured through a post-release survey after three months of operation.  
  Success criterion is established to evaluate the system, aiming for at least 75% of users to report that alerts are timely and useful, creating accountability for the system's effectiveness.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main disagreement centered on how to ensure that sensitive diplomatic engagements were safeguarded while implementing the alert system. Positions settled over rounds as the Proposer revised the proposal to include explicit conditions for alerting users, which the Critic ultimately accepted, enhancing clarity and protecting sensitive data.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 3 | 3 | 0 | 0.46 | 75 | 70 | CONTINUE | continue |
| 3 | 6 | 0 | 6 | 0 | 0.00 | 80 | 75 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring users adhere to the updated protocols around permission and ownership could be challenging.
- Critic's remaining worry (75/100): Future alerts might still lead to miscommunication if user engagement logs are not diligently maintained.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | CONCEDED | 0 | The proposal does not explain how the alert for cold relationships protects against exposing sensitive diplomatic engagements. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'cold relationship' is ambiguous and could allow for misinterpretation regarding its implications. |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not clarify who is responsible for maintaining and validating the accuracy of the engagement interaction recordings. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal does not address what specific permissions users have to access engagement history for other teams, raising the risk of unauthorized exposure of diplomatic relationships. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not explain how the notification process will be handled when users change roles or leave the organization, which could disrupt the data integrity. |
| C6 | MAJOR | COMPLIANCE | GAP | R2 | REVISED | 0 | The proposal does not clarify the privacy implications of alerting users about cold relationships, especially regarding sensitive diplomatic data. |
