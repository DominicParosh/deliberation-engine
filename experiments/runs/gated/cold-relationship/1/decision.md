# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.010.

Challenges: 6 raised · 5 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will implement an alert system notifying users when engagement with a country drops below a specified activity threshold. However, the precise exclusion criteria for alert recipients to safeguard sensitive communications remain unresolved and will need further clarification. Thus, while the core functionality will proceed, the specification around who receives alerts is an open question that must be resolved before building can start.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Implement an alert system for users when engagement with a country is considered 'cold.'  
  An alert system for users will be implemented to signal when engagement with a country is considered 'cold', allowing for a better response to declining interactions.

**In scope**

- **S1** Define 'cold' engagement as a lack of recorded communication or updates for 90 days.  
  'Cold' engagement is defined as lack of recorded communication or updates for 90 days to provide a clear threshold for alerts.
- **S2** Develop a notification system that sends alerts to regional coordinators and project managers, excluding users who do not have the 'engagement management' role and those who are on leave or have left the organization. Alerts will be reassigned to users actively maintaining the relationship when someone changes roles.  
  The notification system will include specific criteria excluding alert recipients, addressing confidentiality concerns that arose during discussions. _(C1, C6)_
- **S3** Alerts will be sent via email to the primary user responsible for the country contact in the CRM, determined by the role assigned to that contact. If the primary user is on leave or has left the organization, the alert will be directed to an alternate user specified as a backup, based on the organizational hierarchy or prior assignment protocols.  
  Alerts will be sent to the primary user responsible for the country contact and can be reassigned to ensure timely engagement management without compromising accountability. _(C2, C4)_
- **S4** Incorporate a dashboard feature that displays a list of countries with 'cold' engagements for easier monitoring.  
  Incorporating a dashboard feature will facilitate monitoring of 'cold' engagements for users, which is essential for managing communications effectively.
- **S5** Allow users to customize their alert settings for engagement thresholds (e.g., 30, 60, 90 days) within the system.  
  Customization of alert settings will empower users to adjust thresholds according to their needs, enhancing user engagement with the system.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated outreach strategies or templates for re-engaging 'cold' contacts.
- **X2** The feature will not incorporate user history analysis beyond the defined threshold for engagement.
- **X3** No alerts will be generated for historical data on engagements prior to the implementation of this feature.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to the engagement history and contact records required to determine if the engagement is 'cold,' as this relies on current data. | Kept | never challenged |
| A2 | All users are trained in how to update engagement records to ensure the alert system remains accurate. | Kept | never challenged |
| A3 | The organization will allow email communications for alerts as a preferred form of notification. | Kept | never challenged |

## Definitions

- **D1** 'cold' engagement means there have been no recorded communications or valid engagements, as defined by logged interactions within the CRM, for a period of 90 days.
- **D2** 'engagement' means any logged interactions between the organization and the government counterparts within the CRM.
- **D3** 'alert' means a notification sent via email to designated users when 'cold' engagement is detected.

## Success criteria

- **K1** Achieve a 75% user satisfaction rate regarding the timely and relevance of alerts, measured through a user survey within one month of implementation.
- **K2** Ensure at least 80% of alerts generated lead to users logging one of the following actions to qualify as 'taking action': 1) sending an email, 2) scheduling a meeting, or 3) documenting a phone call with the cold contact, all within 30 days of receiving the alert, measured by follow-up interactions logged in the CRM.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What specific criteria will clearly define which users are excluded from receiving alerts about 'cold' engagements?**

- Why it matters: Clarifying who receives alerts is crucial to prevent unauthorized disclosures and ensure sensitive communications are managed appropriately.
- Decision owner: Head of Data Protection
- Options: Define users excluded based on role / Specify criteria for recipients based on clearance or context

## Tension report

The main disagreement centered around the sender list for alerts regarding 'cold' engagements, particularly around clarity for role exclusions to protect sensitive information. The Proposer sought a system that prevented unauthorized access, but the Critic maintained that the definitions and re-assignment processes needed further specification, particularly in regards to roles involved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 50 | - | continue |
| 2 | 3 | 1 | 2 | 0 | 0.43 | 80 | 80 | CONTINUE | continue |
| 3 | 5 | 2 | 2 | 1 | 0.64 | 85 | 60 | CONTINUE | continue |
| 4 | 6 | 1 | 4 | 1 | 0.43 | 75 | 60 | CONTINUE | continue |
| 5 | 6 | 0 | 5 | 1 | 0.21 | 80 | 75 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring that clarity around role-based access to alerts prevents unauthorized disclosures.
- Critic's remaining worry (75/100): The definition of 'cold' engagement may lead to misclassification due to a lack of context in interactions.
- ⚠ Proposer reported 80/100 confidence while blocker(s) C1 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | ESCALATED | 2 | The proposal fails to specify who is excluded from receiving alerts about 'cold' engagements, risking sensitive communications reaching unauthorized personnel. |
| C2 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | The proposal does not clarify what happens when users change roles or leave the organization regarding alert notifications, which could compromise accountability. |
| C3 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | Defining 'cold' engagement as simply a lack of communication for 90 days is insufficient and does not account for the nature of interactions, leading to potential incorrect classifications. |
| C4 | MAJOR | OWNERSHIP | S3 | R3 | REVISED | 0 | The proposal does not address who processes alerts if multiple users oversee the same country or if re-assignment fails, which could lead to critical engagement gaps. |
| C5 | MAJOR | DEFINITIONS | K2 | R3 | REVISED | 0 | The success criteria's definition of 'taking action' is vague and lacks measurable parameters for what constitutes an action taken by the user to re-engage. |
| C6 | BLOCKER | CONFIDENTIALITY | GAP | R4 | REVISED | 0 | The proposal does not specify which users are excluded from receiving alerts about 'cold' engagements, risking sensitive communications reaching unauthorized personnel. |
