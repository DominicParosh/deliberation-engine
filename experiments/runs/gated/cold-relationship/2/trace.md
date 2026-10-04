# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 3 rounds · 9 model calls (2 repairs)

## Round 1

### Proposer · confidence 75

_This release will implement an alert system that notifies users when engagement with a specific country decreases, indicating a 'cold' relationship. It is designed for regional coordinators and project managers who maintain contact with government counterparts._

**Core commitments**
- V1: Users will receive alerts when there is no engagement recorded with a country for over six months.

**In scope**
- S1: An alert system will be built to notify regional coordinators and project managers via email when there is no engagement activity logged in the CRM for a country over a period of six months.
- S2: The alert will include the country name, last engagement date, and a suggestion to re-engage.
- S3: Users will be able to set preferences for receiving alerts weekly or monthly.
- S4: Only users with access to the government contact records will receive these alerts.

**Out of scope**
- X1: This release will not include any additional features for re-engagement strategies or monitoring user interactions.
- X2: Historical engagement records prior to the implementation of this alert system will not be included.
- X3: Development of a dashboard for visualizing engagement metrics will not be considered in this release.

**Assumptions**
- A1: Users are trained to log engagement activities accurately in the CRM, which the alert system depends on.
- A2: All engaged users possess an email account registered with their CRM profile, as the alert system relies on this.
- A3: The CRM can access and process engagement data without performance issues, which is necessary for a timely alert system.
- A4: There are no legal restrictions on sending email alerts based on engagement activity, ensuring compliance with privacy standards.

**Definitions**
- D1: 'Cold relationship' means a lack of recorded engagement activity for a period exceeding six months.
- D2: 'Engagement activity' means any logged interaction between the users and the government contacts in the CRM, including meetings, emails, and official communications.

**Success criteria**
- K1: At least 80% of users receive the alerts successfully without any technical failures, measured by system logs and user feedback within the first month after launch.

Biggest worry: The accuracy of identifying engagement activities may be compromised if users do not consistently log their interactions.

### Critic · confidence 40

Pre-mortem: A year after launch, several regional coordinators received alerts about cold relationships with governments they had not engaged with, but the alerts included contacts that were actually engaged. This caused confusion for the senior staff receiving the alerts, and some key diplomatic relationships suffered as a result. Additionally, an alert was sent to a coordinator who had left the organization months prior, leading to sensitive information about diplomatic relations reaching the wrong hands.

Questions the request leaves open:
- What happens when a user responsible for logging engagement leaves the organization?
- How is 'engagement activity' verified to prevent false alerts?
- What are the privacy safeguards in place for the content of the alerts being sent out?
- What defines acceptable engagement actions beyond meetings and emails?
- How will users be informed of the criteria for receiving alerts?
- Who has final authority on updating or modifying the thresholds for what constitutes a 'cold relationship'?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S4
- Challenge: S4 states only users with access to government contact records will receive alerts, but it does not specify how sensitive data is protected in the email alerts.
- Failure scenario: An alert detailing a cold relationship is emailed to a former regional coordinator who has access to sensitive government records, exposing confidential information to the wrong recipient.
- Resolution test: What measures are in place to ensure that alerts do not expose sensitive data to unauthorized users?

**C2** · MAJOR · DEFINITIONS · targets S1
- Challenge: S1 triggers alerts after six months of no recorded engagement, but it does not define what constitutes engagement logging, potentially leading to ambiguity.
- Failure scenario: A regional coordinator misinterprets an informal phone call as engagement while neglecting to log formal emails, resulting in missed alerts and consequences for diplomatic relations.
- Resolution test: What specific actions need to be logged as engagement activity to avoid false alerts?

**C3** · MAJOR · OWNERSHIP · targets A1
- Challenge: A1 assumes users will log engagement activities accurately but does not address accountability if they fail to do so, which could lead to inaccurate alerts.
- Failure scenario: A project manager forgets to log an important engagement, receiving a cold relationship alert incorrectly, and fails to follow up on a critical government contact due to the inaccurate impression that engagement is lacking.
- Resolution test: What processes or roles exist to ensure logging of engagement activities is monitored and enforced?

**C4** · MINOR · DEFINITIONS · targets D1
- Challenge: D1 specifies that 'cold relationship' refers to a lack of recorded engagement for over six months but does not clarify what 'engagement' includes (just logging or also other activities).
- Failure scenario: If the system does not count certain informal engagements (like phone conversations), alerts will be missed, leading to wrong assumptions about the level of relationship with a country.
- Resolution test: Does engagement activity include all types of logged interactions, such as informal communications and meetings?

**C5** · MINOR · OPERATIONS · targets X1
- Challenge: X1 excludes features for re-engagement strategies which could help mitigate cold relationships initiated by alerts, potentially overloading project managers with follow-up responsibilities.
- Failure scenario: Project managers receive alerts but have no guidance or tools to effectively re-engage with the government contacts, leading to frustration and a strained workflow on top of managing existing duties.
- Resolution test: What alternative measures are in place to assist project managers with re-engagement after receiving an alert?

**C6** · BLOCKER · COMPLIANCE · targets A4
- Challenge: A4 states there are no legal restrictions on sending email alerts based on engagement activity, but this is not substantiated and could pose legal risks if not properly vetted.
- Failure scenario: An alert breaches privacy laws due to a lack of consent from the government representatives being contacted, resulting in legal action against the organization.
- Resolution test: What specific legal guidelines exist regarding email alerts based on engagement activity and how are these being adhered to?

Biggest worry: The alerts may expose sensitive diplomatic information through mismanagement of user access and engagement definitions.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S4]: The edit specifies that only non-sensitive information will be included in the alerts, addressing potential confidentiality concerns.
- **C2** REVISE (missing decision) [changed D2]: This revision clearly defines engagement activity to include all relevant interactions, reducing ambiguity and ensuring users know what to log.
- **C3** DEFEND (needs human decision): The organization must specify the processes in place to ensure that engagement logging is monitored and enforced, as accountability for logging is crucial for the system's effectiveness.
- **C4** DEFEND (already covered): The definition provided in D2 already covers the types of engagements that count towards 'engagement activity', addressing this concern.
- **C5** CONCEDE (should not build) [changed X1]: While helpful, re-engagement strategies distract from the core functionality of the alert system and could complicate this initial release.
- **C6** DEFEND (needs human decision): The organization must specify the legal guidelines and processes to ensure compliance with privacy and data protection standards for sending email alerts.

Proposal changes: edited S4, X1, D2
- S4 now reads: Only users with access to government contact records will receive these alerts, and email alerts will only include non-sensitive information such as country name and last engagement date, ensuring confidentiality is maintained.
- X1 now reads: This release will not include any additional features for re-engagement strategies or monitoring user interactions as part of the alert system.
- D2 now reads: 'Engagement activity' means any logged interaction between the users and the government contacts in the CRM, including meetings, emails, official communications, and other documented interactions relevant to the relationship.

Biggest worry: Unclear legal compliance regarding data privacy could lead to significant issues if robust measures are not established.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: This assurance satisfies the confidentiality concern raised. Fact: Alerts will only include non-sensitive information, ensuring confidentiality is maintained. Evidence: "only users with access to government contact records will receive these alerts, and email alerts will only include non-sensitive information such as country name and last engagement date, ensuring confidentiality is maintained."
- **C2** ACCEPT: The definition eliminates ambiguity regarding what needs to be logged as engagement. Fact: Engagement logging includes all relevant interactions such as meetings and emails. Evidence: "'Engagement activity' means any logged interaction between the users and the government contacts in the CRM, including meetings, emails, official communications, and other documented interactions relevant to the relationship."
- **C3** ESCALATE: The proposal does not define how to ensure users log activities, leaving it open to human decision-making.
- **C4** ACCEPT: The definition in D2 suffices for the requirements. Fact: 'Cold relationship' is defined but does not address informal interactions. Evidence: "'Cold relationship' means a lack of recorded engagement activity for a period exceeding six months."
- **C5** ACCEPT: This addresses the concern but acknowledges the limitations of the current proposal. Fact: Re-engagement strategies are excluded from this release. Evidence: "This release will not include any additional features for re-engagement strategies or monitoring user interactions as part of the alert system."
- **C6** ESCALATE: The proposal did not provide sufficient compliance details, necessitating human input.

New challenges:

**C7** · BLOCKER · COMPLIANCE · targets A4
- Challenge: A4 does not specify how the organization will ensure compliance with privacy standards, leaving the process ambiguous and potentially non-compliant.
- Failure scenario: An alert about cold diplomatic relations is sent without legal clearance, causing legal ramifications for the organization due to breach of privacy laws.
- Resolution test: What specific legal guidelines exist regarding the email alerts sent based on engagement activity, and how will compliance be ensured?

Biggest worry: The reliance on human enforcement of logging could lead to critical alerts being missed or misrepresented.

**Ledger:** raised 7 · open 1 · resolved 4 · escalated 2 · disagreement 0.53 → **continue**

## Round 3

### Proposer · confidence 85

- **C7** DEFEND (needs human decision): The organization must clarify the specific legal guidelines regarding email alerts triggered by engagement activity to ensure compliance. Since ensuring compliance with privacy standards depends on organizational policies and laws, this is not something the proposal can decide.

Proposal changes: none

Biggest worry: Unclear legal guidelines for sending email alerts could lead to compliance risks.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C7** ESCALATE: The lack of specific legal guidelines leaves compliance ambiguous and requires clarification from a human decision-maker.

Biggest worry: The proposal lacks clear legal guidelines and compliance measures for the alert system, posing significant risks.

**Ledger:** raised 7 · open 0 · resolved 4 · escalated 3 · disagreement 0.53 → **converged**

## Final proposal

_This release will implement an alert system to notify users when engagement with a specific country decreases, indicating a 'cold' relationship. The alert will trigger when there is no recorded engagement activity for over six months, providing users with relevant information while maintaining confidentiality._

**Core commitments**
- V1: Users will receive alerts when there is no engagement recorded with a country for over six months.

**In scope**
- S1: An alert system will be built to notify regional coordinators and project managers via email when there is no engagement activity logged in the CRM for a country over a period of six months.
- S2: The alert will include the country name, last engagement date, and a suggestion to re-engage.
- S3: Users will be able to set preferences for receiving alerts weekly or monthly.
- S4: Only users with access to government contact records will receive these alerts, and email alerts will only include non-sensitive information such as country name and last engagement date, ensuring confidentiality is maintained.

**Out of scope**
- X1: This release will not include any additional features for re-engagement strategies or monitoring user interactions as part of the alert system.
- X2: Historical engagement records prior to the implementation of this alert system will not be included.
- X3: Development of a dashboard for visualizing engagement metrics will not be considered in this release.

**Assumptions**
- A1: Users are trained to log engagement activities accurately in the CRM, which the alert system depends on.
- A2: All engaged users possess an email account registered with their CRM profile, as the alert system relies on this.
- A3: The CRM can access and process engagement data without performance issues, which is necessary for a timely alert system.
- A4: There are no legal restrictions on sending email alerts based on engagement activity, ensuring compliance with privacy standards.

**Definitions**
- D1: 'Cold relationship' means a lack of recorded engagement activity for a period exceeding six months.
- D2: 'Engagement activity' means any logged interaction between the users and the government contacts in the CRM, including meetings, emails, official communications, and other documented interactions relevant to the relationship.

**Success criteria**
- K1: At least 80% of users receive the alerts successfully without any technical failures, measured by system logs and user feedback within the first month after launch.
