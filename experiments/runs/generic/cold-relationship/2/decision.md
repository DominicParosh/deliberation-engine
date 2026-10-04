# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.014.

Challenges: 9 raised · 7 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

This release will implement an alert system to notify users when engagement with a country has been inactive for six months, including confidentiality measures and error correction protocols. It will not provide alerts for decreased engagement frequency or detailed historical analyses of cold relationships. The usability and management of alerts will depend on user adherence to the configured settings.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users receive alerts when no engagement activities have occurred with a specific country for a period of six months.  
  Users will receive alerts for inactive engagements after six months to prompt re-engagement.

**In scope**

- **S1** The system will define 'engagement activities' as any logged communication or meeting with a country representative, ministry contact, project lead, or mission delegate. All logged engagement activities must undergo an internal review process every six months, including checks for completeness, accuracy, and relevance. If errors are identified during the review, the designated authorized user must correct these discrepancies within five business days and document the corrective actions taken in a corrections log. Access to sensitive information will be restricted to authorized personnel only, and a two-factor authentication protocol will be implemented to access sensitive logs. Additionally, all reviews will be tracked through an access log.  
  Defines engagement activities and includes a review process to ensure accuracy, though the specific metrics for these checks remain a point of contention. _(C3)_
- **S2** An alert will be generated and sent via email to the designated regional coordinator and project manager when a relationship goes cold as defined in V1.  
  Specifies that alerts will be sent to coordinators and project managers, ensuring relevant stakeholders are informed.
- **S3** The CRM will include a configuration option that allows only regional coordinators and project managers to set the duration for alerts related to inactive relationships, allowing for customization between three to twelve months. If a user who has set configurations leaves or changes their role, their alert settings will be reset, and the new user assigned to their role will need to establish new alert configurations.  
  Defines which roles are authorized to set alert durations, addressing ownership concerns about misconfiguration when users change roles. _(C1, C2)_
- **S4** A dashboard will display a summary of all countries with cold relationships, indicating the country name and the last date of engagement.  
  Includes a dashboard overview of cold relationships to facilitate quick visibility on engagement health.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include alerts for relationships that have simply decreased in frequency but still have some ongoing engagement.  
  Will not include alerts for relationships with decreased engagement frequency to focus specifically on complete inactivity.
- **X2** This release will not cover any changes to the underlying CRM system architecture or any complex user-defined rules beyond the specified duration for alert settings.  
  No changes to CRM architecture or complex user-defined alert rules will be made, keeping the implementation straightforward.
- **X3** The CRM will not provide detailed historical data analysis on the reasons for the cold relationship in this release.  
  Historical reasons for cold relationships are outside the scope of this release to maintain focused objectives.
- **X4** This release will ensure all alerts regarding cold relationships are only accessible to regional coordinators and project managers, and sensitive engagement data will be protected by role-based access controls.  
  Alerts for cold relationships will be accessible only to regional coordinators and project managers, ensuring proper confidentiality. _(C5)_
- **X5** This release will ensure alerts regarding cold relationships are retained for a maximum of six months before automatic deletion from the system.  
  A maximum retention policy of six months for cold relationship alerts ensures compliance with data management regulations. _(C6)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to the CRM and be trained on how to interpret alerts about cold relationships. | Kept | never challenged |
| A2 | Users understand and agree on what constitutes a relationship being 'cold', based on engagement activity, per S1. | Kept | never challenged |
| A3 | It is assumed that the CRM has the necessary permissions and data structures to track and log engagement activities. | Kept | never challenged |

## Definitions

- **D1** "cold relationship" means a relationship with a country that has not recorded any engagement activity for six months as per V1.  
  Defines a 'cold relationship' based on the absence of engagement activities for six months.
- **D2** "engagement activities" means any recorded form of communication, meeting, or project interaction between users of the CRM and government representatives from member countries.  
  Clarifies what constitutes 'engagement activities' to avoid confusion and ensure comprehensive tracking.
- **D3** "authorized users" means users who have been granted permission to configure alert settings within the CRM.  
  Defines 'authorized users' as those permitted to set alert configurations, ensuring clarity on responsibilities.

## Success criteria

- **K1** At least 80% of users report receiving timely alerts when relationships go cold, with 'timely' defined as alerts received within 48 hours of a relationship becoming inactive, measured via user feedback surveys two months post-release.  
  Specifies that 'timely' alerts are those received within 48 hours, thus providing a measurable criterion for success. _(C4)_

## Open questions for humans

### C8 · BLOCKER · blocks the build

**What specific measures and protocols are in place to protect sensitive engagement data during the internal review process?**

- Why it matters: To mitigate risks of confidentiality breaches during the review of engagement activities.
- Decision owner: Head of Data Protection
- Options: Implement stricter access controls / Define protocols for information handling during reviews

### C3 · MAJOR · blocks the build

**What specific metrics and data quality checks are in place to ensure the accuracy of logged engagement activities?**

- Why it matters: Ensuring logged engagement activities are accurate is critical for the reliability of the alert system.
- Decision owner: Product Owner
- Options: Define specific quality metrics / Rely on existing generic review processes

## Tension report

The primary disagreement was around ensuring effective data quality and confidentiality during the alert process. While the proposer included protocols for review and access control, the critic raised concerns that specifics were lacking, leading to unresolved issues that require further definition before moving forward.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 1 | 5 | 0 | 0.15 | 80 | 85 | CONTINUE | continue |
| 3 | 8 | 2 | 5 | 1 | 0.39 | 85 | 65 | CONTINUE | continue |
| 4 | 9 | 2 | 6 | 1 | 0.38 | 75 | 60 | CONTINUE | continue |
| 5 | 9 | 0 | 7 | 2 | 0.24 | 80 | 75 | CONTINUE | converged |

- Proposer's remaining worry (80/100): There may be additional unforeseen challenges regarding user adherence to the new protocols.
- Critic's remaining worry (75/100): The alert requirements may still lead to misconfigurations when users change roles, affecting data accuracy.
- ⚠ Proposer reported 80/100 confidence while blocker(s) C8 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | OWNERSHIP | S3 | R1 | REVISED | 0 | The proposal does not specify which roles are authorized to set the duration for alerts related to cold relationships, potentially leading to inconsistencies in alert configurations. |
| C2 | MAJOR | OWNERSHIP | S3 | R1 | REVISED | 0 | The proposal does not clarify what happens to alert configurations when users leave or change roles, risking ongoing misconfigurations of alert settings. |
| C3 | MAJOR | DEFINITIONS | S1 | R1 | ESCALATED | 2 | The scope includes 'engagement activities' but lacks clarity on what happens if a communication is logged incorrectly or entries are missed, affecting the alert system's reliability. |
| C4 | MAJOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The acceptance of 80% user positive feedback measured via surveys is vague and potentially untestable, lacking concrete criteria to confirm 'timely alerts.' |
| C5 | BLOCKER | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There is no mention of how sensitive data regarding country engagements is handled or who can access this information, which could lead to breaches of confidentiality. |
| C6 | MAJOR | COMPLIANCE | GAP | R1 | REVISED | 0 | The proposal does not address data retention policies for alerts that are generated regarding cold relationships, leaving the potential for non-compliance with data management regulations. |
| C7 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not clearly define the metrics or quality checks used in determining engagement activity accuracy, leaving potential for logging errors. |
| C8 | BLOCKER | CONFIDENTIALITY | S1 | R3 | ESCALATED | 2 | The description of the internal review process for engagement activities lacks details on how sensitive information is protected during this review, posing risks to confidentiality. |
| C9 | BLOCKER | DATA_QUALITY | GAP | R4 | REVISED | 0 | The proposal fails to address what specific actions are taken if errors are found in the logged engagement activities during the internal review process, which could allow inaccuracies to persist uncorrected. |
