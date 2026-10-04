# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.008.

Challenges: 7 raised · 4 settled between the agents · 3 handed to humans · 0 still open when it ended.

## Summary

This release will implement an alert system to notify users when engagement with a country decreases, indicating a 'cold' relationship, specifically when there is no recorded engagement activity for over six months. Additional features for re-engagement strategies or visualization of engagement metrics will not be included in this release. However, open questions regarding accountability for logging engagements and ensuring compliance with legal guidelines for email alerts remain unresolved and need to be addressed.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users will receive alerts when there is no engagement recorded with a country for over six months.  
  Users will receive alerts when there is no engagement recorded with a country for over six months, providing timely informational support while maintaining confidentiality with non-sensitive details.

**In scope**

- **S1** An alert system will be built to notify regional coordinators and project managers via email when there is no engagement activity logged in the CRM for a country over a period of six months.  
  An alert system will be built to notify regional coordinators and project managers via email when there is no engagement activity logged in the CRM for a country over a period of six months, focusing on critical relationship management.
- **S2** The alert will include the country name, last engagement date, and a suggestion to re-engage.  
  The alert will include the country name, last engagement date, and a suggestion to re-engage, ensuring users have the relevant information needed for follow-ups.
- **S3** Users will be able to set preferences for receiving alerts weekly or monthly.  
  Users will be able to set preferences for receiving alerts weekly or monthly, enhancing user control over their notifications and engagement processes.
- **S4** Only users with access to government contact records will receive these alerts, and email alerts will only include non-sensitive information such as country name and last engagement date, ensuring confidentiality is maintained.  
  Only non-sensitive information will be included in the alerts to maintain confidentiality, addressing concerns about data exposure and unauthorized access. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any additional features for re-engagement strategies or monitoring user interactions as part of the alert system.  
  This release will not include any additional features for re-engagement strategies or monitoring user interactions as part of the alert system, focusing instead on the primary alert functionality. _(C5)_
- **X2** Historical engagement records prior to the implementation of this alert system will not be included.  
  Historical engagement records prior to the implementation of this alert system will not be included to streamline the process and focus on future engagements.
- **X3** Development of a dashboard for visualizing engagement metrics will not be considered in this release.  
  Development of a dashboard for visualizing engagement metrics will not be considered in this release, as it complicates the primary objective of the alert system.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users are trained to log engagement activities accurately in the CRM, which the alert system depends on. | Kept | C3 → escalated |
| A2 | All engaged users possess an email account registered with their CRM profile, as the alert system relies on this. | Kept | never challenged |
| A3 | The CRM can access and process engagement data without performance issues, which is necessary for a timely alert system. | Kept | never challenged |
| A4 | There are no legal restrictions on sending email alerts based on engagement activity, ensuring compliance with privacy standards. | Kept | C6 → escalated; C7 → escalated |

## Definitions

- **D1** 'Cold relationship' means a lack of recorded engagement activity for a period exceeding six months.  
  The definition of a 'cold relationship' indicates a lack of recorded engagement for over six months, ensuring clarity for users regarding the alert conditions. _(C4)_
- **D2** 'Engagement activity' means any logged interaction between the users and the government contacts in the CRM, including meetings, emails, official communications, and other documented interactions relevant to the relationship.  
  Engagement activity is defined to include all logged interactions, minimizing ambiguity about what should be recorded to maintain relationship quality. _(C2)_

## Success criteria

- **K1** At least 80% of users receive the alerts successfully without any technical failures, measured by system logs and user feedback within the first month after launch.  
  Success will be measured by ensuring that at least 80% of users receive alerts successfully without any technical failures in the first month after launch, establishing a clear performance benchmark for the system.

## Open questions for humans

### C6 · BLOCKER · blocks the build

**What specific legal guidelines exist regarding email alerts based on engagement activity, and how are these being adhered to?**

- Why it matters: Defining legal compliance is crucial to avoid potential legal risks associated with the alert system.
- Decision owner: Legal Compliance Officer
- Options: Conduct a legal review of the alert system / Incorporate existing data protection policies / Seek external legal consultation

### C7 · BLOCKER · blocks the build

**What specific legal guidelines exist regarding the email alerts sent based on engagement activity, and how will compliance be ensured?**

- Why it matters: Clarifying compliance protocols is vital to prevent breaches of privacy laws and potential legal issues.
- Decision owner: Data Protection Officer
- Options: Develop a compliance framework for alerts / Provide user consent documentation / Set up a legal review process for future updates

### C3 · MAJOR · blocks the build

**What processes or roles exist to ensure that engagement logging is monitored and enforced?**

- Why it matters: Clear accountability is essential to ensure the effectiveness of the alert system and avoid inaccurate alerts.
- Decision owner: Operations Manager
- Options: Establish regular audits of engagement logs / Implement user training sessions / Designate accountability roles for logging

## Tension report

The primary disagreement centered on ensuring proper accountability for logging engagement activities and establishing compliance with legal guidelines for sending alerts. While the Proposer advocated for proceeding with the implementation pending clarification, the Critic raised significant concerns about potential compliance risks that require resolution before moving forward.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 7 | 1 | 4 | 2 | 0.53 | 80 | 60 | CONTINUE | continue |
| 3 | 7 | 0 | 4 | 3 | 0.53 | 85 | 60 | CONTINUE | converged |

- Proposer's remaining worry (85/100): Unclear legal guidelines for sending email alerts could lead to compliance risks.
- Critic's remaining worry (60/100): The proposal lacks clear legal guidelines and compliance measures for the alert system, posing significant risks.
- ⚠ Proposer reported 85/100 confidence while blocker(s) C6, C7 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | S4 states only users with access to government contact records will receive alerts, but it does not specify how sensitive data is protected in the email alerts. |
| C2 | MAJOR | DEFINITIONS | S1 | R1 | REVISED | 0 | S1 triggers alerts after six months of no recorded engagement, but it does not define what constitutes engagement logging, potentially leading to ambiguity. |
| C3 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | A1 assumes users will log engagement activities accurately but does not address accountability if they fail to do so, which could lead to inaccurate alerts. |
| C4 | MINOR | DEFINITIONS | D1 | R1 | DEFENDED | 0 | D1 specifies that 'cold relationship' refers to a lack of recorded engagement for over six months but does not clarify what 'engagement' includes (just logging or also other activities). |
| C5 | MINOR | OPERATIONS | X1 | R1 | CONCEDED | 0 | X1 excludes features for re-engagement strategies which could help mitigate cold relationships initiated by alerts, potentially overloading project managers with follow-up responsibilities. |
| C6 | BLOCKER | COMPLIANCE | A4 | R1 | ESCALATED | 0 | A4 states there are no legal restrictions on sending email alerts based on engagement activity, but this is not substantiated and could pose legal risks if not properly vetted. |
| C7 | BLOCKER | COMPLIANCE | A4 | R2 | ESCALATED | 0 | A4 does not specify how the organization will ensure compliance with privacy standards, leaving the process ambiguous and potentially non-compliant. |
