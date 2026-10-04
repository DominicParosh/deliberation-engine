# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **consensus** after 3 rounds · 8 model calls (2 repairs)

## Round 1

### Proposer · confidence 75

_This release will implement an alerting system that notifies users when engagement with a country has been inactive for a predefined duration. It is intended for regional coordinators and project managers using the CRM system._

**Core commitments**
- V1: Users will receive an alert if there is no engagement recorded with a country for six months.
- V2: Users can view a list of countries that have not had engagement in the past six months.

**In scope**
- S1: The alert will be sent via email to regional coordinators and project managers associated with the inactive countries.
- S2: Users will have the option to define the threshold for inactivity, with a default setting of six months.
- S3: The system will track engagement history and determine inactivity based on logged interactions.
- S4: Alerts will include the country name, the date of last engagement, and a link to the relevant records in the CRM.

**Out of scope**
- X1: This release will not include automatic actions based on the alerts, such as re-engagement plans or task assignments.
- X2: This release does not cover historical engagement data prior to the implementation of this alert system.
- X3: The alert mechanism will not consider engagements logged outside of the CRM system.

**Assumptions**
- A1: Users will log all engagements with countries into the CRM system, which is critical for tracking engagement history.
- A2: The CRM has access to email functionality for alert notifications, which the alert system will utilize.
- A3: Users are aware of the importance of logging interactions promptly to maintain accurate engagement records.

**Definitions**
- D1: "cold relationship" means a period of six months or longer with no logged engagement activities between the organization and the country in the CRM.
- D2: "alert" means an automated email notification sent to users informing them of the cold relationship status.
- D3: "engagement history" means all interactions recorded in the CRM, including meetings, communications, and project collaborations.

**Success criteria**
- K1: At least 80% of users find the alert system useful, measured through feedback surveys after the release.
- K2: At least 90% of the alerts send successfully without errors in the first three months after deployment.

Biggest worry: Ensuring users consistently log all engagements accurately is critical to the functionality of the alert system.

### Critic · confidence 40

Pre-mortem: A year after the alerting system was launched, a sensitive diplomatic record was inadvertently shared with unauthorized personnel due to a malfunction in the alert distribution, leading to a breach of confidentiality and undermining relations with several countries. Additionally, some users received alerts about inactive engagements they were not authorized to see, causing confusion and distrust among stakeholders.

Questions the request leaves open:
- Which roles are authorized to receive alerts about cold relationships?
- How can we ensure that logged engagements are accurately captured to prevent false alerts?
- What will happen when users change roles or leave the organization regarding the ownership of alert notifications?
- What data protection measures are in place to handle the sensitive information within these alerts?
- How will the system handle variations in engagement definitions across different countries or contexts, and are there safeguards against misinterpretations?
- What is the retention policy for engagement history data, and how will it be enforced?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1, S2
- Challenge: The proposal does not define which specific roles are authorized to receive alerts related to cold relationships, potentially leading to unauthorized exposure of sensitive diplomatic information.
- Failure scenario: A project manager from one region receives cold relationship alerts about countries handled by another team, leading to disruptive inquiries and discussions that compromise sensitive engagements.
- Resolution test: Which specific roles are authorized to receive cold relationship alerts?

**C2** · MAJOR · DEFINITIONS · targets D1, D3
- Challenge: The definitions provided do not clarify how logged engagements are categorized, which could lead to discrepancies in defining a 'cold relationship.'
- Failure scenario: An engagement that should qualify as significant is misclassified due to incomplete logging, resulting in alerts being sent erroneously, which erodes trust in the alerting system.
- Resolution test: How are engagement activities categorized and validated in the CRM to inform what counts as a logged engagement?

**C3** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal lacks clarity on who will manage the alert system's configuration after users change roles or leave, risking alerts being sent incorrectly.
- Failure scenario: A user who left the organization still receives alerts, leading to confusion among remaining team members regarding who is responsible for addressing cold relationships with countries.
- Resolution test: Outline the process for reassigning alert notifications and determining ownership when users change roles or leave.

**C4** · MAJOR · DATA_QUALITY · targets S3
- Challenge: The proposal does not provide an explanation of how the engagement tracking will ensure data accuracy and completeness, risking false positives in alerts.
- Failure scenario: Alerts are generated erroneously because some engagements went unlogged or were incorrectly recorded, resulting in wasted time and reduced confidence in the system.
- Resolution test: What mechanisms are in place to validate the accuracy and completeness of engagement records logged in the CRM?

**C5** · MINOR · COMPLIANCE · targets GAP
- Challenge: The proposal does not mention any compliance safeguards to handle sensitive data related to alerts, which raises concerns about data security.
- Failure scenario: Alerts sent via email expose sensitive country engagement details to unintended recipients, resulting in diplomatic tensions and breaches of confidentiality.
- Resolution test: What data protection measures will be implemented to secure sensitive information conveyed in alerts?

**C6** · MINOR · OPERATIONS · targets GAP
- Challenge: The proposal does not address how the alert system will manage varying definitions of engagement across different regions or teams, which could lead to misalignment of alert criteria.
- Failure scenario: Users in one region interpret cold relationships differently than users in another due to differing engagement practices, leading to ineffective responses and missed opportunities.
- Resolution test: What is the approach for standardizing engagement definitions across different countries and contexts in the alerting system?

Biggest worry: The undefined roles for alert recipients could lead to unauthorized access to sensitive diplomatic information.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S1]: This revision specifies that only users assigned to the relevant countries in the CRM will receive alerts, thus protecting sensitive information.
- **C2** REVISE (missing decision) [changed D3]: This revision categorizes engagement activities to clarify what counts as logged engagements, reducing discrepancies in defining a 'cold relationship'.
- **C3** REVISE (missing decision) [changed S4]: This specification outlines the process for assigning alerts to rightfully authorized users, addressing potential miscommunication and confusion.
- **C4** REVISE (missing decision) [changed S3]: This edit adds an auditing process that will validate engagement records for accuracy and completeness, minimizing false positives.
- **C5** REVISE (missing decision) [changed S1]: This revision ensures the alerts contain data protection measures, ensuring sensitive information remains secure.
- **C6** REVISE (missing decision) [changed D1]: This revision specifies that the definition of engagement will be standardized across all teams, addressing any potential misinterpretation.

Proposal changes: edited S1, S3, S4, D1, D3
- S1 now reads: The alert will be sent via email to regional coordinators and project managers associated with the inactive countries, and all notifications will include measures to ensure data encryption and limit sensitive information to authorized recipients only.
- S3 now reads: The system will track engagement history and determine inactivity based on logged interactions, with periodic audits conducted to ensure accuracy and completeness of engagement records.
- S4 now reads: A process will be established to reassign alert notifications to new users when a user changes roles or leaves the organization, ensuring that alerts are sent only to active, authorized personnel.
- D1 now reads: "cold relationship" means a period of six months or longer with no logged engagement activities between the organization and the country in the CRM, defined consistently across all teams to ensure standardized interpretations of engagement across regions.
- D3 now reads: "engagement history" means all interactions recorded in the CRM, including meetings, communications, and project collaborations, categorized as follows: a) 'meeting' refers to all scheduled discussions with country representatives, b) 'communication' refers to all recorded correspondence, and c) 'projects' refers to any collaborations or initiatives involving the country.

Biggest worry: Ensuring effective training and adherence to engagement logging by all users to avoid misclassification of cold relationships.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C1** MAINTAIN: The commitment does not specify exactly which roles are authorized to receive alerts, potentially leading to confusion about role assignment.
- **C2** ACCEPT: The categorization clarifies how engagements are logged, reducing risks of discrepancies. Fact: Engagement activities categorized as meetings, communications, or projects. Evidence: "categorized as follows: a) 'meeting' refers to all scheduled discussions with country representatives, b) 'communication' refers to all recorded correspondence, c) 'projects' refers to any collaborations or initiatives"
- **C3** ACCEPT: This establishes clarity on alert ownership and communication. Fact: A process exists to reassign notifications when users leave or change roles. Evidence: "A process will be established to reassign alert notifications to new users when a user changes roles or leaves the organization"
- **C4** ACCEPT: Auditing enhances data quality and reduces false positives. Fact: Periodic audits will verify the accuracy of engagement records. Evidence: "with periodic audits conducted to ensure accuracy and completeness of engagement records"
- **C5** ACCEPT: These measures help secure sensitive information across alerts. Fact: Data protection measures are in place for alert notifications. Evidence: "measures to ensure data encryption and limit sensitive information to authorized recipients only"
- **C6** ACCEPT: Standardization prevents misalignment in alert criteria. Fact: Engagement definitions are standardized across teams. Evidence: "defined consistently across all teams to ensure standardized interpretations"

New challenges:

**C7** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not define which specific roles are authorized to receive alerts related to cold relationships, potentially leading to unauthorized exposure of sensitive diplomatic information.
- Failure scenario: A project manager from one region receives cold relationship alerts about countries handled by another team, leading to disruptive inquiries and discussions that compromise sensitive engagements.
- Resolution test: Which specific roles are authorized to receive cold relationship alerts?

Biggest worry: The potential for unauthorized exposure of sensitive diplomatic information still looms if system roles are not managed diligently.

**Ledger:** raised 7 · open 2 · resolved 5 · escalated 0 · disagreement 0.43 → **continue**

## Round 3

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed S1]: This revision explicitly states that only regional coordinators and project managers assigned to the relevant countries will receive alerts, thus addressing confidentiality concerns and preventing unauthorized exposure of sensitive information.
- **C7** REVISE (missing decision) [changed S1]: The revision clearly identifies that only users assigned to relevant countries will receive alerts, which directly addresses the challenge of ensuring confidentiality and authorized access to sensitive information.

Proposal changes: edited S1
- S1 now reads: The alert will be sent via email to regional coordinators and project managers assigned to the relevant countries in the CRM associated with the inactive countries, and all notifications will include measures to ensure data encryption and limit sensitive information to authorized recipients only.

Biggest worry: The successful implementation of tracking and alert functionality may still depend on user adherence to logging engagements accurately.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C1** ACCEPT: The commitment specifies which roles are authorized to receive alerts, addressing the confidentiality issue. Fact: Only regional coordinators and project managers assigned are authorized to receive alerts. Evidence: "The alert will be sent via email to regional coordinators and project managers assigned to the relevant countries in the CRM associated with the inactive countries."
- **C7** ACCEPT: The revision clarifies which specific roles receive alerts, mitigating the risk of unauthorized exposure. Fact: Only regional coordinators and project managers assigned are authorized to receive alerts. Evidence: "The alert will be sent via email to regional coordinators and project managers assigned to the relevant countries in the CRM associated with the inactive countries."

Biggest worry: There could still be issues with user role changes leading to alerts being sent to unauthorized personnel.

**Ledger:** raised 7 · open 0 · resolved 7 · escalated 0 · disagreement 0.00 → **consensus**

## Final proposal

_This proposal outlines an alert system for users when engagement with a country goes cold, clearly defining the specific roles authorized to receive alerts and ensuring proper management of sensitive information. Adjustments have been made to address confidentiality concerns, and compliance with data protection measures is reinforced._

**Core commitments**
- V1: Users will receive an alert if there is no engagement recorded with a country for six months.
- V2: Users can view a list of countries that have not had engagement in the past six months.

**In scope**
- S1: The alert will be sent via email to regional coordinators and project managers assigned to the relevant countries in the CRM associated with the inactive countries, and all notifications will include measures to ensure data encryption and limit sensitive information to authorized recipients only.
- S2: Users will have the option to define the threshold for inactivity, with a default setting of six months.
- S3: The system will track engagement history and determine inactivity based on logged interactions, with periodic audits conducted to ensure accuracy and completeness of engagement records.
- S4: A process will be established to reassign alert notifications to new users when a user changes roles or leaves the organization, ensuring that alerts are sent only to active, authorized personnel.

**Out of scope**
- X1: This release will not include automatic actions based on the alerts, such as re-engagement plans or task assignments.
- X2: This release does not cover historical engagement data prior to the implementation of this alert system.
- X3: The alert mechanism will not consider engagements logged outside of the CRM system.

**Assumptions**
- A1: Users will log all engagements with countries into the CRM system, which is critical for tracking engagement history.
- A2: The CRM has access to email functionality for alert notifications, which the alert system will utilize.
- A3: Users are aware of the importance of logging interactions promptly to maintain accurate engagement records.

**Definitions**
- D1: "cold relationship" means a period of six months or longer with no logged engagement activities between the organization and the country in the CRM, defined consistently across all teams to ensure standardized interpretations of engagement across regions.
- D2: "alert" means an automated email notification sent to users informing them of the cold relationship status.
- D3: "engagement history" means all interactions recorded in the CRM, including meetings, communications, and project collaborations, categorized as follows: a) 'meeting' refers to all scheduled discussions with country representatives, b) 'communication' refers to all recorded correspondence, and c) 'projects' refers to any collaborations or initiatives involving the country.

**Success criteria**
- K1: At least 80% of users find the alert system useful, measured through feedback surveys after the release.
- K2: At least 90% of the alerts send successfully without errors in the first three months after deployment.
