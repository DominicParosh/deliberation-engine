# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.020.

## Summary

The release will implement an alert system within the Government CRM notifying users when there's been no engagement with a country contact for over 90 days. The feature will ensure that only authorized project managers and regional coordinators can view alerts and dashboard data to maintain confidentiality. However, clarity around data validation processes for engagement history remains to be decided by the appropriate authority.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users will receive automatic alerts when there is no engagement with a country contact for more than 3 months.  
  Users will receive alerts when there is no engagement with a country contact for more than 3 months, which meets the proposal's objective for monitoring relationships.

**In scope**

- **S1** Implement a notification system that triggers an alert when the last engagement date with a country is older than 90 days.  
  A notification system will trigger alerts for engagements not occurring within 90 days, ensuring timely awareness for users responsible for relationship management. _(C1)_
- **S2** Provide a dashboard widget displaying a list of countries with 'cold' relationships, defined as no engagements in the past 90 days, which can only be viewed by project managers and regional coordinators to ensure confidentiality.  
  A dashboard widget will only be visible to project managers and regional coordinators, ensuring the protection of sensitive information regarding diplomatic relationships. _(C7)_
- **S3** Include user-defined settings to customize the duration (threshold) for what is considered a 'cold' relationship up to 180 days, which can only be configured by project managers and regional coordinators.  
  User-defined settings for customizing cold relationship duration will be limited to project managers and regional coordinators, preserving data integrity. _(C4)_
- **S4** Allow notifications to be sent via email and in-app messages.  
  Notifications will be sent via both email and in-app messages to support various user preferences for alerts.
- **S5** Ensure that only users with appropriate access to country contact data can receive these alerts, specifically project managers and regional coordinators responsible for those countries. Users' access to alerts will be automatically revoked when they leave the organization or change roles.  
  Access to alerts will be revoked for users who leave or change roles, enhancing data confidentiality management. _(C5)_
- **S6** Implement a logging system that records when alerts are triggered, including time and user details, with the data management team responsible for monitoring and maintaining this log. The engagement history data will be subject to a validation process conducted by the data management team to ensure its accuracy and completeness before triggering alerts. A validation process includes verification that engagement logs are complete and properly formatted.  
  A logging system will be implemented to monitor alert notifications, with the data management team ensuring accuracy of these logs prior to alert triggers. _(C3, C9)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include the ability to automate follow-up actions based on alerts.
- **X2** This release will not alter existing user permissions related to contact data access.
- **X3** This release will not provide insights or analytics on the nature of engagements.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users will have consistent engagement logs for country contacts that can be analyzed for the last engagement date. | The feature relies on the availability of accurate and timely logs of engagements. | Accepted (never challenged) |
| A2 | Users have a clear understanding of what constitutes an engagement event. | Alerts are triggered based on specific engagement criteria that must be defined and understood by users. | Accepted (never challenged) |
| A3 | There is an existing method in the CRM for tracking the engagement history of country contacts. | The alerting functionality must be based on historical data that is already collected. | Accepted (never challenged) |
| A4 | Users are willing to configure their settings regarding what duration they consider 'cold' for relationships. | The feature includes user-defined thresholds which rely on user willingness to interact with settings. | Accepted (never challenged) |
| A5 | There will be a defined set of guidelines from the data management team to establish what constitutes complete and accurate engagement history data. | This is essential to validate the engagement data used in the alerting functionality. | Accepted (never challenged) |

## Definitions

- **D1** "cold relationship": A relationship is defined as 'cold' if there have been no engagements logged with a specific country contact in the past 90 days and those engagements meet the criteria of a recorded interaction, such as meetings, emails, or phone calls.  
  The definition of 'cold relationship' was updated to include specific criteria for recorded engagements, alleviating ambiguities around alert triggers.
- **D2** "engagement event": An engagement event refers to any recorded interaction with a country contact, including meetings, emails, or calls.  
  An engagement event is defined to include specific interaction types, promoting uniformity in how engagements are considered.
- **D3** "alert notification": An alert notification is an automated message sent to users indicating that a specified action needs attention, in this case, a cold relationship alert.  
  An alert notification is characterized as an automated message for user attention regarding cold relationships.
- **D4** "engagement history data": Engagement history data consists of logs that include the type, date, and details of all interactions with the country contact, forming the basis for evaluating the relationship status.  
  Engagement history data must consist of component logs that assist in evaluating relationship statuses, providing clarity on required data to validate.

## Success criteria

- **K1** Percentage of cold relationship alerts acknowledged by users: target 80% (This will be tracked through CRM notification response metrics.)  
  The success criterion aims for 80% acknowledgment of alerts by users, ensuring they are engaging with the important notifications.

## Open questions for humans

### C2 · MAJOR · blocks the build

**What specific criteria must engagements meet to be considered valid for determining a cold relationship?**

- Why it matters: To ensure that alerts are triggered accurately and prevent misleading alerts that could cause confusion.
- Decision owner: Data Management Team Lead
- Options: Define specific interaction types / Use existing criteria without changes

### C6 · MAJOR · blocks the build

**What process will be established for validating engagement history data for accuracy and completeness?**

- Why it matters: A defined process is essential to maintain the integrity of the alert system and prevent erroneous alerts.
- Decision owner: Data Management Team Lead
- Options: Implement automated checks / Manual review by designated staff

### C7 · MAJOR · blocks the build

**Which specific users or roles will have access to view the cold relationship dashboard widget?**

- Why it matters: Ensuring appropriate access is critical to maintaining confidentiality and aligning with diplomatic protocols.
- Decision owner: Project Management Director
- Options: Limit to project managers / Include additional roles based on criteria

### C3 · MINOR · blocks the build

**Who is responsible for maintaining and monitoring the alert logging system?**

- Why it matters: Clarifying ownership will ensure accurate and accountable management of alert logs.
- Decision owner: Project Management Director
- Options: Assign to Data Management Team / Create a new accountability team

## Tension report

The main disagreement centered on clarity around data validation processes and ownership of logging responsibilities. While the proposer aimed to define clear parameters and ownership, the critic raised concerns over potential ambiguities and implications for data integrity, leading to unresolved issues needing managerial decisions.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 80 | 60 | - | continue |
| 2 | 6 | 5 | 1 | 0 | 0.82 | 85 | 50 | CONTINUE | continue |
| 3 | 8 | 4 | 2 | 2 | 0.73 | 75 | 60 | CONTINUE | continue |
| 4 | 9 | 2 | 4 | 3 | 0.53 | 80 | 60 | CONTINUE | continue |
| 5 | 9 | 0 | 5 | 4 | 0.41 | 80 | 80 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Data validation processes need to be robust to avoid erroneous alerts.
- Critic's remaining worry (80/100): There could still be ambiguities in terms of the completeness of engagement logs and how they are defined.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | S1 states that users will receive alerts when there has been no engagement for more than 3 months, but it does not specify who can see these alerts, potentially exposing sensitive diplomatic relationships to unauthorized users. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | ESCALATED | 2 | D1 defines cold relationships as no engagements in 90 days, but needs to clarify whether engagement logs must meet a specific criteria or format to count, leaving the threshold vague and potentially untestable. |
| C3 | MINOR | OWNERSHIP | S6 | R1 | ESCALATED | 2 | S6 mentions implementing a logging system that records alerts, but does not clarify who is responsible for maintaining and monitoring this log. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not specify who can configure the user-defined settings for the cold relationship duration, which is critical for maintaining proper access controls and data integrity. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | DEFENDED | 1 | The proposal does not address what happens when a user leaves the organization or changes roles in relation to alert access, creating a gap in data confidentiality management. |
| C6 | MAJOR | DATA_QUALITY | GAP | R2 | ESCALATED | 2 | The proposal lacks a clear method for how engagement history data will be validated for accuracy and completeness, which is crucial for the alerts to function correctly. |
| C7 | MAJOR | CONFIDENTIALITY | GAP | R3 | ESCALATED | 1 | The proposal does not specify which specific users or roles will have access to view the cold relationship dashboard widget, potentially exposing sensitive diplomatic relationships to unauthorized users. |
| C8 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The interface currently lacks a clear definition of the 'engagement history data' to be validated, creating ambiguity regarding its completeness and accuracy. |
| C9 | MAJOR | DATA_QUALITY | GAP | R4 | REVISED | 0 | There is no clear method defined for how engagement history data will be validated, which is necessary for alerts to function correctly. |
