# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 4 rounds · 12 model calls (3 repairs)

## Round 1

### Proposer · confidence 70

_This release will implement an alert system in the Government CRM that notifies users when engagement with a country contact has not occurred within a defined time frame. It is aimed at operational and project team members who manage relationships with country representatives._

**Core commitments**
- V1: The system will send an alert to designated users when there has been no engagement with a country contact for 6 months.

**In scope**
- S1: Users will receive email alerts if there is no recorded engagement (defined as contacts or meetings logged) with a country contact for a period of 6 months.
- S2: The alert will include the country name, contact details, and the last date of recorded engagement.
- S3: The system will allow users to configure the engagement tracking period (defaulting to 6 months) within the CRM settings.
- S4: Regional coordinators and project managers will be the primary users receiving these alerts.
- S5: An audit log will be maintained to track when alerts are sent and to which users.

**Out of scope**
- X1: The release will not include proactive actions or suggestions for following up with the country contacts after the alert is received.
- X2: The system will not analyze reasons for decreased engagement or categorize types of engagements.
- X3: The release will not implement alerts for individual team members, only for designated roles (regional coordinators and project managers).

**Assumptions**
- A1: It is assumed that engagement is tracked through logged calls, meetings, or emails in the CRM; the request depends on having a clear definition of 'engagement'.
- A2: It is assumed that the organization has a standard protocol for relationship management that justifies the need for cold alerts; the request assumes familiarity with this protocol.
- A3: It is assumed that users of the CRM have necessary permissions to access contact histories; the request depends on current user permissions being appropriate.

**Definitions**
- D1: 'Cold' means a period of 6 months without any recorded engagement (contacts or meetings) logged in the CRM.
- D2: 'Engagement' means any logged interaction, such as meetings, phone calls, or emails with country contacts.
- D3: 'Users' refers specifically to regional coordinators and project managers who manage country relationships within the CRM.

**Success criteria**
- K1: At least 80% of users report receiving alerts in a timely manner (measured through user feedback surveys conducted 1 month after release).

Biggest worry: The definition of 'engagement' might be too broad or vague, potentially leading to confusion in tracking.

### Critic · confidence 40

Pre-mortem: A year after launch, regional coordinators received alerts for countries that had no engagements for over 6 months. However, these alerts mistakenly included sensitive contacts that shouldn’t have been viewed by all regional coordinators due to confidentiality restrictions, leading to breaches of trust and diplomatic relations. Consequently, some countries withdrew cooperation, severely impacting ongoing operations.

Questions the request leaves open:
- What other roles might need access to the alert system that are not covered in the proposal?
- How is 'engagement' validated to ensure only relevant interactions trigger alerts?
- What happens to alerts when users change roles, leave the organization, or their permissions change?
- What criteria define a 'sensitive' contact within the system that might restrict alert visibility?
- How will the system ensure that reminders do not lead to alert fatigue among users?
- What is the protocol for dealing with alerts sent to users who should not have received them?

New challenges:

**C1** · MAJOR · CONFIDENTIALITY · targets S4
- Challenge: The proposal does not address who else might potentially need access to the alert system beyond regional coordinators and project managers, potentially exposing sensitive information to unauthorized users.
- Failure scenario: A project manager receives alerts that include sensitive contacts from a country representative who is supposed to be restricted due to the nature of diplomatic engagements, leading to a confidentiality breach.
- Resolution test: Who else besides regional coordinators and project managers can access the alert system?

**C2** · MAJOR · DEFINITIONS · targets D1
- Challenge: The definition of 'cold' engagement could lead to misunderstandings; there is no clear distinction of what constitutes a valid engagement that can be logged, impacting the accuracy of alerts.
- Failure scenario: A user receives an alert for a 'cold' relationship, but discovers that emails or informal meetings were not recorded, leading to unnecessary escalations and strained relationships with country representatives.
- Resolution test: What specific types of interactions count as valid 'engagement' to avoid misclassification?

**C3** · MAJOR · OWNERSHIP · targets S1
- Challenge: The proposal does not specify what happens to alerts when users change roles; alerts may continue to be sent to former users who no longer manage those relationships.
- Failure scenario: A regional coordinator leaves the organization but the system continues to send engagement alerts to them, confusing their successor and jeopardizing communications with key contacts.
- Resolution test: What process is in place to update alert recipients when users change roles or leave?

**C4** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: There is no mention of handling sensitive contacts that should not appear in alerts, which can lead to situations where confidential information is inadvertently exposed.
- Failure scenario: A regional coordinator receives an alert about a sensitive ministry contact, breaching confidentiality and damaging trust with that country.
- Resolution test: What criteria will be used to filter out sensitive contacts from alerts?

**C5** · MAJOR · OPERATIONS · targets S3
- Challenge: The system does not address the potential for alert fatigue, risking complacency and unresponsiveness to important alerts.
- Failure scenario: Users receive too many alerts about cold engagements due to the configuration settings, leading them to ignore all alerts and miss significant opportunities for re-engagement.
- Resolution test: What measures will be included to mitigate alert fatigue and ensure users are engaged with meaningful alerts?

**C6** · MINOR · OPERATIONS · targets X1
- Challenge: While the proposal outlines the alert feature, it does not provide a process for following up on alerts, which could leave users without clear next steps.
- Failure scenario: Users receive an alert indicating a cold relationship but lack guidance on how to act on it, leading to missed opportunities for re-engagement with country contacts.
- Resolution test: What is the proposed process for users on how to respond after receiving a cold engagement alert?

Biggest worry: The lack of clarity on who receives alerts raises serious confidentiality concerns that could lead to diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 75

- **C1** DEFEND (needs human decision): Access to the alert system and the criteria for role designation must be defined by organizational policies regarding user permissions and data security. The organization must address who qualifies for alerts and what confidential information is protected.
- **C2** REVISE (missing decision) [changed D1]: The edited definition clarifies that only logged interactions contribute to defining 'cold' engagement, preventing misunderstandings that could lead to unnecessary alerts.
- **C3** REVISE (missing decision) [changed S1]: The revised scope item specifies a process for managing changes in user roles, ensuring that alerts are correctly assigned to active users and avoiding potential confusion.
- **C4** DEFEND (needs human decision): The criteria for filtering sensitive contacts from alerts must be determined based on existing organizational privacy policies and practices. These decisions should be made by the organization to ensure compliance with confidentiality standards.
- **C5** REVISE (missing decision) [changed S3]: The revised scope item introduces a configurable feature to manage alert frequency, aiming to ensure that alerts remain meaningful and help prevent user complacency.
- **C6** REVISE (missing decision) [changed X1]: The revised out-of-scope item clarifies that the responsibility for following up on alerts rests with the users, establishing clear expectations for user action.

Proposal changes: edited S1, S3, X1, D1
- S1 now reads: The system will automatically update alert recipients when users change roles or leave the organization, ensuring alerts are sent only to current managers of that country contact.
- S3 now reads: The system will include a mechanism for users to establish threshold triggers based on the number of engagement alerts received, minimizing alert fatigue by consolidating alerts for less critical situations.
- X1 now reads: The release will not include proactive actions or suggestions for following up with the country contacts after the alert is received, leaving follow-up actions to the discretion of users.
- D1 now reads: 'Cold' means a period of 6 months without any recorded engagement (contacts or meetings) logged in the CRM, excluding informal communications such as internal discussions or unlogged emails.

Biggest worry: The reliance on organizational policies for managing confidential information could lead to inconsistent implementations of the alert system.

### Critic · confidence 45 · CONTINUE

Rulings:
- **C1** ESCALATE: The criteria for who else can access alerts must be defined by organizational policies, which are not addressed in the proposal.
- **C2** ACCEPT: The revision clarifies what constitutes valid engagement, reducing potential misunderstandings. Fact: Engagement is defined as logged interactions only, excluding informal communications. Evidence: "D1: 'Cold' means a period of 6 months without any recorded engagement (contacts or meetings) logged in the CRM, excluding informal communications such as internal discussions or unlogged emails."
- **C3** ACCEPT: This adequately outlines the process for updating alert recipients. Fact: Alerts will be updated to reflect current users when roles change or users leave. Evidence: "S1: The system will automatically update alert recipients when users change roles or leave the organization, ensuring alerts are sent only to current managers of that country contact."
- **C4** ESCALATE: Human decision-makers will need to establish filtering criteria for sensitive contacts, which is critical to prevent breaches.
- **C5** ACCEPT: This addresses the alert fatigue challenge effectively. Fact: Users can establish triggers for consolidating alerts to reduce fatigue. Evidence: "S3: The system will include a mechanism for users to establish threshold triggers based on the number of engagement alerts received, minimizing alert fatigue by consolidating alerts for less critical situations."
- **C6** ACCEPT: This establishes expectations that follow-up is the user's responsibility, although it may leave users without clear next steps. Fact: Follow-up actions are not included in this release and are left to users. Evidence: "X1: The release will not include proactive actions or suggestions for following up with the country contacts after the alert is received, leaving follow-up actions to the discretion of users."

New challenges:

**C7** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The responsibilities for maintaining data quality of engagement logs are not mentioned, which could lead to incorrect firing of alerts.
- Failure scenario: Inaccurate or incomplete engagement logs result in alerts being triggered incorrectly, alarming users without reason and damaging relationships with country contacts.
- Resolution test: Who is responsible for maintaining and ensuring the accuracy of engagement records?

**C8** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal lacks detail on how the alert system will comply with data protection laws regarding personal data from country representatives.
- Failure scenario: Personal data from country representatives is mishandled because the alert system does not adhere to applicable data protection regulations, leading to legal repercussions for the organization.
- Resolution test: What measures are in place to ensure compliance with data protection laws?

Biggest worry: The lack of defined criteria for filtering sensitive contacts may lead to significant confidentiality breaches.

**Ledger:** raised 8 · open 2 · resolved 4 · escalated 2 · disagreement 0.53 → **continue**

## Round 3

### Proposer · confidence 75

- **C7** REVISE (missing decision) [changed S5]: The edits clarify that project managers will be responsible for ensuring the accuracy of engagement logs, thus addressing the ownership of data quality and ensuring that alerts are triggered correctly.
- **C8** DEFEND (needs human decision): While it is crucial to ensure compliance with data protection laws, the specifics of those measures must be determined by the organization, which is outside the scope of this proposal.

Proposal changes: edited S5
- S5 now reads: An audit log will be maintained to track when alerts are sent and to which users, and the responsibility for maintaining data quality of engagement logs will lie with designated project managers for their respective country contacts.

Biggest worry: There remains a risk that the implementation will not sufficiently address data integrity and compliance concerns.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C7** ACCEPT: This addresses the challenge regarding ownership and ensures that alerts are triggered correctly. Fact: Designated project managers are responsible for maintaining data quality of engagement logs. Evidence: "the responsibility for maintaining data quality of engagement logs will lie with designated project managers for their respective country contacts."
- **C8** ESCALATE: While the importance of compliance is acknowledged, the lack of specifics leaves the proposal vulnerable without human decision-making.

New challenges:

**C9** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not address how to prevent sensitive contacts from being included in alerts, risking confidentiality breaches.
- Failure scenario: An alert is sent to all regional coordinators, including sensitive country contacts that are not supposed to be exposed, leading to diplomatic fallout and damaged relations.
- Resolution test: What safeguards are in place to ensure sensitive contacts do not appear in alerts?

**C10** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The proposal lacks a clear definition of engagement logs and the specific actions that qualify as engagements, which could lead to misunderstandings and inaccuracies in alert causation.
- Failure scenario: If 'engagement' is ambiguously defined, alerts may trigger prematurely or not at all due to varying interpretations of what counts as an engagement, leading to operational issues.
- Resolution test: What specific actions are required to be logged as engagement in the CRM?

Biggest worry: The lack of clarity on sensitive contacts being included in alerts poses a risk to confidentiality.

**Ledger:** raised 10 · open 2 · resolved 5 · escalated 3 · disagreement 0.53 → **continue**

## Round 4

### Proposer · confidence 85

- **C9** REVISE (missing decision) [changed X4]: This new out-of-scope item prevents sensitive country contacts from being included in alerts to address potential confidentiality risks.
- **C10** REVISE (missing decision) [changed D4]: The new definition clarifies what constitutes an engagement log, ensuring that alerts are triggered based on a clear understanding of logged interactions.

Proposal changes: added X4, D4
- X4 now reads: The alert system will not include sensitive country contacts in alerts, ensuring that alerts are restricted to non-sensitive country contacts only as defined by designated project managers.
- D4 now reads: 'Engagement logs' mean any documented record of an interaction with a country contact that is formally logged in the CRM, including entries that detail date, type, and subject of communication such as meetings, phone calls, or emails.

Biggest worry: The implementation must ensure that sensitive contacts are effectively filtered to prevent confidentiality breaches.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C9** ACCEPT: The addition of X4 adequately addresses the confidentiality concern regarding sensitive contacts. Fact: Sensitive contacts will not be included in alerts. Evidence: "X4: The alert system will not include sensitive country contacts in alerts, ensuring that alerts are restricted to non-sensitive country contacts only as defined by designated project managers."
- **C10** ACCEPT: The updated definition clarifies what constitutes an engagement log, addressing the previous ambiguity. Fact: Engagement logs are formally logged records detailing interactions like meetings or calls. Evidence: "D4: 'Engagement logs' mean any documented record of an interaction with a country contact that is formally logged in the CRM, including entries that detail date, type, and subject of communication such as meetings, phone calls, or emails."

Biggest worry: There are unresolved escalated challenges surrounding data protection compliance that could impact user trust.

**Ledger:** raised 10 · open 0 · resolved 7 · escalated 3 · disagreement 0.32 → **consensus**

## Final proposal

_This release will implement an alert system in the Government CRM that notifies users when engagement with a country contact has not occurred within a defined time frame. It is aimed at operational and project team members who manage relationships with country representatives, improving their capacity to monitor relationships effectively while safeguarding sensitive information. Key updates include filtering alerts for sensitive contacts and a clearer definition of engagement logs._

**Core commitments**
- V1: The system will send an alert to designated users when there has been no engagement with a country contact for 6 months.

**In scope**
- S1: The system will automatically update alert recipients when users change roles or leave the organization, ensuring alerts are sent only to current managers of that country contact.
- S2: The alert will include the country name, contact details, and the last date of recorded engagement.
- S3: The system will include a mechanism for users to establish threshold triggers based on the number of engagement alerts received, minimizing alert fatigue by consolidating alerts for less critical situations.
- S4: Regional coordinators and project managers will be the primary users receiving these alerts.
- S5: An audit log will be maintained to track when alerts are sent and to which users, and the responsibility for maintaining data quality of engagement logs will lie with designated project managers for their respective country contacts.

**Out of scope**
- X1: The release will not include proactive actions or suggestions for following up with the country contacts after the alert is received, leaving follow-up actions to the discretion of users.
- X2: The system will not analyze reasons for decreased engagement or categorize types of engagements.
- X3: The release will not implement alerts for individual team members, only for designated roles (regional coordinators and project managers).
- X4: The alert system will not include sensitive country contacts in alerts, ensuring that alerts are restricted to non-sensitive country contacts only as defined by designated project managers.

**Assumptions**
- A1: It is assumed that engagement is tracked through logged calls, meetings, or emails in the CRM; the request depends on having a clear definition of 'engagement'.
- A2: It is assumed that the organization has a standard protocol for relationship management that justifies the need for cold alerts; the request assumes familiarity with this protocol.
- A3: It is assumed that users of the CRM have necessary permissions to access contact histories; the request depends on current user permissions being appropriate.

**Definitions**
- D1: 'Cold' means a period of 6 months without any recorded engagement (contacts or meetings) logged in the CRM, excluding informal communications such as internal discussions or unlogged emails.
- D2: 'Engagement' means any logged interaction, such as meetings, phone calls, or emails with country contacts.
- D3: 'Users' refers specifically to regional coordinators and project managers who manage country relationships within the CRM.
- D4: 'Engagement logs' mean any documented record of an interaction with a country contact that is formally logged in the CRM, including entries that detail date, type, and subject of communication such as meetings, phone calls, or emails.

**Success criteria**
- K1: At least 80% of users report receiving alerts in a timely manner (measured through user feedback surveys conducted 1 month after release).
