# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 3 rounds (policy `naive`) · $0.008.

Challenges: 7 raised · 6 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

An alert system will be implemented to notify users when engagement with country representatives falls below a defined threshold. This system will not include analytics or dashboards, and will only focus on improving the alert notifications based on user interaction with defined criteria. Human decision-makers must still clarify the flexibility of engagement thresholds based on different countries or contexts.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Implement an alert system that notifies users of declining engagement with country representatives.  
  The commitment to implement the alert system is based on the need for proactive monitoring of diplomatic engagements.

**In scope**

- **S1** Users will receive an alert when there have been no recorded engagements with a country representative for 90 days.  
  An alert will trigger after 90 days of no recorded engagements, establishing a clear inactivity threshold for monitoring.
- **S2** The alert will be sent via email to the registered email addresses of the regional coordinators and project managers associated with that country.  
  The alert notification will target registered emails of relevant personnel to ensure that appropriate team members receive timely information. _(C2)_
- **S3** The system will log all user engagements, defined as any documented interactions with country representatives that are officially recorded in the CRM, including emails, meetings, phone calls, and notes. There will also be a mechanism in place to regularly review logged engagements to ensure compliance and accuracy.  
  The logging of engagements will include various forms of documented interactions to ensure a comprehensive record is maintained. _(C1, C7)_
- **S4** Users will have the option to customize the alert threshold to be notified after 30, 60, or 90 days of inactivity, but all thresholds must adhere to a maximum of 90 days across the organization to ensure consistency in engagement monitoring.  
  While users can set custom thresholds for inactivity alerts, the maximum is capped at 90 days to maintain consistency across the organization. _(C5)_
- **S5** The CRM will include functionality that automatically removes users from the alert subscription list when they change roles or leave the organization, based on HR data.  
  An automated process will be implemented to manage alert subscriptions based on HR updates, enhancing relevance. _(C2)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not provide analytics or dashboards on engagement metrics or any auditing mechanism related to logged engagements.  
  The exclusion of analytics or dashboards allows focus on the alert system without complicating the release with additional features.
- **X2** The system will not notify users about relationships going cold with organizations other than country representatives.  
  Relationship notifications are limited to country representatives, which clearly scopes the alert system's functionality.
- **X3** No modifications to the existing user interface beyond the alert settings will be included.  
  No changes to the user interface beyond alert settings were included to streamline the implementation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to the CRM system and appropriate permissions to configure alert settings. | Kept | never challenged |
| A2 | There exists a clear definition of what constitutes an engagement, specifically what types of interactions are tracked in the CRM. | Kept | never challenged |
| A3 | The email notification system is functioning and able to deliver alerts to users. | Kept | never challenged |
| A4 | Users understand the importance of monitoring their engagements and will actively use the alert system. | Kept | never challenged |

## Definitions

- **D1** "cold relationship" means a lack of recorded engagement with a country representative for a specified duration, requiring that all engagements which contribute to this classification are documented in the CRM regardless of the type of interaction; these include emails, meetings, phone calls, or official notes.  
  The refined definition of a cold relationship clarifies the engagement tracking requirements, reducing the possibility of misclassification. _(C1, C6)_
- **D2** "alert" means a notification system that sends an email to users when a specified threshold of inactivity is met.  
  The definition of an alert is straightforward, ensuring users understand what to expect when notifications are triggered.

## Success criteria

- **K1** Success will be measured by a 70% user adoption rate of the alert system within three months of release.  
  A user adoption target of 70% within three months is measurable and ensures accountability in engagement monitoring.

## Open questions for humans

### C3 · MAJOR · blocks the build

**How were the thresholds of 30, 60, and 90 days determined to be appropriate, and is there flexibility to adjust them based on countries or regions?**

- Why it matters: Finding the right thresholds is essential for ensuring that the alert system is sensitive to the varying contexts of diplomatic relations.
- Decision owner: Head of Operations
- Options: Maintain current thresholds / Allow adjustments based on regional input
- Proposer's last word (R2, defend, needs human decision): Determining appropriate thresholds may require input from diplomatic teams to understand regional contexts and nuances, which we cannot decide at this stage.
- Critic's last word (R2, escalate): The defense highlights that thresholds require diplomatic input, making this uncertain for implementation as it cannot be decided here.

## Tension report

The main disagreement centered around the definition and thresholds for classifying a cold relationship, with concerns about their appropriateness in different diplomatic contexts. The proposer favored a standardized approach, while the critic argued for the need for flexibility and input from diplomatic teams, leaving an unresolved question regarding threshold adaptation.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 0 | 0 | 1.00 | 75 | 25 | - | continue |
| 2 | 7 | 4 | 2 | 1 | 0.73 | 80 | 65 | CONTINUE | continue |
| 3 | 7 | 0 | 6 | 1 | 0.13 | 80 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): If users do not log engagements consistently, it may undermine the system's effectiveness.
- Critic's remaining worry (80/100): Despite recent improvements, the system may still suffer from misclassifications due to informal engagements not recorded in the CRM.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | D1 | R1 | REVISED | 1 | There is a risk that sensitive diplomatic interactions are misclassified as 'cold' due to the lack of clear definitions for what constitutes an engagement, potentially leading to alerts being sent out indiscriminately. |
| C2 | MAJOR | OWNERSHIP | S2, S4 | R1 | REVISED | 0 | It is unclear who is responsible for managing alert subscriptions and ensuring that users who are no longer relevant to certain country relationships are removed from the notification list. |
| C3 | MAJOR | DEFINITIONS | D1 | R1 | ESCALATED | 0 | The definition of a 'cold relationship' relies on a generic 90-day inactivity threshold but lacks clarity on whether this is sufficient or appropriate for different countries and contexts. |
| C4 | MAJOR | COMPLIANCE | X1 | R1 | CONCEDED | 0 | Without providing analytics or dashboards, there may be no clear compliance or audit mechanism for engagement activity which could lead to issues in accountability or tracking of diplomatic relations. |
| C5 | MINOR | OPERATIONS | S3, S4 | R1 | REVISED | 1 | The option for users to customize alert thresholds might lead to inconsistency in definitions of engagement and how 'cold relationships' are treated across teams. |
| C6 | BLOCKER | DEFINITIONS | D1 | R2 | REVISED | 0 | The current definition of a 'cold relationship' is too vague; it does not clarify what types or contexts of engagements must be recorded to avoid misclassification. |
| C7 | MAJOR | DATA_QUALITY | S3 | R2 | REVISED | 0 | There are potential gaps in data quality and accuracy regarding recorded engagements, which can lead to alerts being poorly informed. |
