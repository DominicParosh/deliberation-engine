# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.007.

## Summary

An alert system will be built to notify users when engagement with a country goes cold after six months of inactivity, allowing regional coordinators and project managers to receive these alerts securely. Features like user-defined inactivity thresholds and a management process for alert recipients will also be implemented. Concerns about data protection and compliance have been addressed, but ongoing worries about user adherence to logging engagements and role changes remain for future attention.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users will receive an alert if there is no engagement recorded with a country for six months.  
  Users will receive alerts for cold relationships after six months of inactivity to ensure timely engagement. _(C1, C4)_
- **V2** Users can view a list of countries that have not had engagement in the past six months.  
  A list of countries with no engagement in the past six months will be accessible to authorized users for better oversight. _(C1)_

**In scope**

- **S1** The alert will be sent via email to regional coordinators and project managers assigned to the relevant countries in the CRM associated with the inactive countries, and all notifications will include measures to ensure data encryption and limit sensitive information to authorized recipients only.  
  Alerts will be sent only to regional coordinators and project managers assigned to the relevant countries, minimizing confidentiality risks. _(C1, C7)_
- **S2** Users will have the option to define the threshold for inactivity, with a default setting of six months.  
  Users can choose their inactivity thresholds, which allows for flexibility within the system.
- **S3** The system will track engagement history and determine inactivity based on logged interactions, with periodic audits conducted to ensure accuracy and completeness of engagement records.  
  The system will conduct audits to ensure that engagement records are accurate, addressing concerns about false positives in alerting. _(C4)_
- **S4** A process will be established to reassign alert notifications to new users when a user changes roles or leaves the organization, ensuring that alerts are sent only to active, authorized personnel.  
  A process for reassigning alerts when users change roles will maintain clarity on responsible users and protect sensitive data. _(C3)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automatic actions based on the alerts, such as re-engagement plans or task assignments.  
  Automatic actions based on alerts are not included in this release to focus on alert functionality first.
- **X2** This release does not cover historical engagement data prior to the implementation of this alert system.  
  Historical engagement data is excluded to prioritize new alert implementations, simplifying initial deployment.
- **X3** The alert mechanism will not consider engagements logged outside of the CRM system.  
  Engagements outside the CRM are not considered to avoid discrepancies and ensure data integrity within the alert system.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will log all engagements with countries into the CRM system, which is critical for tracking engagement history. | Kept | never challenged |
| A2 | The CRM has access to email functionality for alert notifications, which the alert system will utilize. | Kept | never challenged |
| A3 | Users are aware of the importance of logging interactions promptly to maintain accurate engagement records. | Kept | never challenged |

## Definitions

- **D1** "cold relationship" means a period of six months or longer with no logged engagement activities between the organization and the country in the CRM, defined consistently across all teams to ensure standardized interpretations of engagement across regions.  
  The definition of a 'cold relationship' is standardized to prevent inconsistencies across users and regions. _(C2, C6)_
- **D2** "alert" means an automated email notification sent to users informing them of the cold relationship status.  
  An 'alert' is clearly defined to ensure all users understand the nature of the notifications they will receive.
- **D3** "engagement history" means all interactions recorded in the CRM, including meetings, communications, and project collaborations, categorized as follows: a) 'meeting' refers to all scheduled discussions with country representatives, b) 'communication' refers to all recorded correspondence, and c) 'projects' refers to any collaborations or initiatives involving the country.  
  Engagement activities are categorized to clarify what constitutes a logged engagement, reducing future misinterpretations. _(C2)_

## Success criteria

- **K1** At least 80% of users find the alert system useful, measured through feedback surveys after the release.  
  User feedback will measure usefulness to ensure the alert system meets user needs.
- **K2** At least 90% of the alerts send successfully without errors in the first three months after deployment.  
  Success criteria include a high percentage of successfully sent alerts to ensure system reliability post-implementation.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement centered on how to protect sensitive data while implementing the alert system, particularly which roles would be authorized to receive alerts. This was ultimately resolved through revisions that clearly defined roles and addressed data protection concerns, but there remains tension regarding user adherence to proper engagement logging.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 7 | 2 | 5 | 0 | 0.43 | 85 | 80 | CONTINUE | continue |
| 3 | 7 | 0 | 7 | 0 | 0.00 | 75 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (75/100): The successful implementation of tracking and alert functionality may still depend on user adherence to logging engagements accurately.
- Critic's remaining worry (85/100): There could still be issues with user role changes leading to alerts being sent to unauthorized personnel.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S2 | R1 | REVISED | 1 | The proposal does not define which specific roles are authorized to receive alerts related to cold relationships, potentially leading to unauthorized exposure of sensitive diplomatic information. |
| C2 | MAJOR | DEFINITIONS | D1, D3 | R1 | REVISED | 0 | The definitions provided do not clarify how logged engagements are categorized, which could lead to discrepancies in defining a 'cold relationship.' |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal lacks clarity on who will manage the alert system's configuration after users change roles or leave, risking alerts being sent incorrectly. |
| C4 | MAJOR | DATA_QUALITY | S3 | R1 | REVISED | 0 | The proposal does not provide an explanation of how the engagement tracking will ensure data accuracy and completeness, risking false positives in alerts. |
| C5 | MINOR | COMPLIANCE | GAP | R1 | REVISED | 0 | The proposal does not mention any compliance safeguards to handle sensitive data related to alerts, which raises concerns about data security. |
| C6 | MINOR | OPERATIONS | GAP | R1 | REVISED | 0 | The proposal does not address how the alert system will manage varying definitions of engagement across different regions or teams, which could lead to misalignment of alert criteria. |
| C7 | BLOCKER | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal does not define which specific roles are authorized to receive alerts related to cold relationships, potentially leading to unauthorized exposure of sensitive diplomatic information. |
