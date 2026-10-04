# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 3 rounds · 9 model calls (2 repairs)

## Round 1

### Proposer · confidence 75

_This release implements an alert system that notifies users when engagement with country contacts remains inactive for a specified duration. It is intended for regional coordinators and project managers engaged with government counterparts in various countries._

**Core commitments**
- V1: Implement an alert system for detecting inactive relationships with country contacts.

**In scope**
- S1: Define "cold relationship" as a lack of recorded engagement activities for 90 days.
- S2: Allow users to receive alerts via email regarding cold relationships.
- S3: Enable users to filter and view a list of contacts with cold relationships in the CRM.
- S4: Provide options for users to set customized thresholds for inactivity alerts, ranging from 30 to 120 days.

**Out of scope**
- X1: This release will not include relationship-building suggestions based on contacts' engagement history.
- X2: This release will not integrate with external systems for engagement history tracking.

**Assumptions**
- A1: Users have sufficient privileges to set alert preferences and view engagement history; this depends on existing user role management capabilities.
- A2: Engagement activities are logged in the CRM; this depends on current CRM functionality for tracking such activities.
- A3: Users understand what constitutes a "cold relationship" based on the defined thresholds; this assumes adequate training and documentation is provided.

**Definitions**
- D1: "cold relationship" means a lack of recorded engagement activities with a country contact for 90 consecutive days.
- D2: "engagement activities" means any logged interaction or correspondence with a country contact, such as meetings, emails, or calls.

**Success criteria**
- K1: Achieve at least a 75% user satisfaction rate with the new alert system, measured through user surveys within one month of release.

Biggest worry: The definition of a 'cold relationship' might not align with all users' expectations, potentially leading to dissatisfaction with the alert system.

### Critic · confidence 30

Pre-mortem: A year after launch, the alert system for cold relationships triggered an alert about a diplomatic contact that had recently undergone a significant change in government. Instead of providing useful information to the relevant project manager, the alert inadvertently reached the country representative’s office, causing undue tension and diplomatic strain. Following this, there were complaints from both country representatives and project managers about receiving irrelevant alerts, leading to increased operational fatigue regarding the alert system and strained relationships.

Questions the request leaves open:
- Who decides when a relationship is truly 'cold'?
- What are the minimum engagement activities that can trigger a re-engagement alert?
- What happens to alerts if a user changes roles or leaves the organization?
- How will privacy and confidentiality be maintained in the alert process, especially with sensitive contacts?
- Who has the authority to override or customize alert thresholds, and how is this managed?
- What happens if engagement activities are inaccurately logged, affecting cold relationship status?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1
- Challenge: The definition of 'cold relationship' does not address the risk of exposing sensitive diplomatic contacts to the wrong individuals if the alert system triggers inaccurately.
- Failure scenario: A false alert is sent about a cold relationship to an unauthorized user, leading to potential diplomatic issues.
- Resolution test: What safeguards are in place to ensure sensitive diplomatic contacts remain confidential and alert notifications only reach authorized personnel?

**C2** · MAJOR · DEFINITIONS · targets S4
- Challenge: The thresholds for engagement inactivity alerts are vague regarding what constitutes valid engagement activities and may become untestable depending on user behavior.
- Failure scenario: Users set inappropriate custom threshold values, leading to irrelevant alerts that contribute to alert fatigue and undermine the system’s credibility.
- Resolution test: What specific engagement activities must be logged for the alert system to consider a relationship active?

**C3** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify ownership of the alert system or the responsibility for managing engagement activity logging or oversight of alerts.
- Failure scenario: When a user leaves the organization, their alerts continue to be sent out, but no one is responsible for monitoring or adjusting the effectiveness of these alerts.
- Resolution test: Who is responsible for maintaining the alert system, monitoring engagement logs, and managing user preferences when roles change?

**C4** · MAJOR · CONFIDENTIALITY · targets S2
- Challenge: The proposal does not define how alerts are handled with respect to sensitive contacts, risking inappropriate disclosures.
- Failure scenario: An alert about a cold diplomatic contact is accidentally sent to a broader user base, resulting in diplomatic embarrassment.
- Resolution test: What protocols are in place to ensure that alerts regarding diplomatic contacts are sent only to authorized personnel?

**C5** · MINOR · OPERATIONS · targets GAP
- Challenge: The proposal lacks insight into the operational workload required to manage alerts, including potential for false positives and alert fatigue.
- Failure scenario: The alert system floods users with notifications for numerous cold relationships, leading to users ignoring critical alerts and operational inefficiencies.
- Resolution test: What measures will be put in place to ensure users can manage and filter alerts effectively so they do not become overwhelmed?

**C6** · MINOR · DATA_QUALITY · targets GAP
- Challenge: There is a lack of clarity on the accuracy and freshness of the engagement activities tracked, which can affect the reliability of the alert system.
- Failure scenario: Inaccurate logging leads to alerts incorrectly suggesting cold relationships, causing confusion and frustration among project managers.
- Resolution test: What processes will be implemented to ensure engagement activities logged in the CRM are accurate and up to date?

Biggest worry: The proposal lacks safeguards to ensure that alerts do not risk exposing sensitive diplomatic relationships to unauthorized personnel.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S1]: This edit aims to establish safeguards that prevent unauthorized users from receiving alerts about sensitive diplomatic contacts, thus protecting confidentiality.
- **C2** REVISE (missing decision) [changed S4]: This definition makes the threshold criteria clearer by specifying what counts as valid engagement activities, mitigating the risk of users setting inappropriate custom values.
- **C3** REVISE (missing decision) [changed S5]: This decision clarifies ownership of the alert system and establishes accountability for monitoring and managing alerts, addressing potential issues with changes in user roles.
- **C4** REVISE (missing decision) [changed S2]: This edit introduces specific protocols for alert distribution to prevent unauthorized disclosures related to sensitive contacts, addressing confidentiality concerns.
- **C5** DEFEND (acceptable risk): While the potential for false positives and alert fatigue is acknowledged, the implementation of user customization options for alert filtering is deemed sufficient to manage the volume and relevance of notifications.
- **C6** DEFEND (acceptable risk): Ensuring data accuracy for engagement activities will rely on existing logging practices and user accountability; this risk is acceptable for the first release as the system can be refined based on user feedback.

Proposal changes: added S5; edited S1, S2, S4
- S5 now reads: Assign the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role.
- S1 now reads: Define 'cold relationship' as a lack of recorded engagement activities for 90 consecutive days, with an additional requirement that alerts are sent only to users who have authorization to view information regarding that country.
- S2 now reads: Allow users to receive alerts via email regarding cold relationships, with protocols in place that ensure alerts regarding diplomatic contacts are sent exclusively to authorized personnel as designated in their role settings.
- S4 now reads: Provide options for users to set customized thresholds for inactivity alerts, ranging from 30 to 120 days, with the stipulation that valid engagement activities must include documented interactions such as meetings, emails, or official communications logged in the CRM.

Biggest worry: The implementation of confidentiality measures must robustly ensure that alerts about sensitive contacts are strictly controlled.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: The measure directly addresses confidentiality concerns by limiting alert distribution to authorized personnel. Fact: Alerts are only sent to authorized users. Evidence: "with an additional requirement that alerts are sent only to users who have authorization to view information regarding that country."
- **C2** ACCEPT: The specification of valid engagement activities mitigates the risk of inappropriate custom thresholds. Fact: Valid engagement activities are specified to include meetings, emails, or official communications. Evidence: "valid engagement activities must include documented interactions such as meetings, emails, or official communications logged in the CRM."
- **C3** ACCEPT: Ownership of the alert system is now clearly defined, addressing operational risks. Fact: Responsibility for the alert system is assigned to the CRM administrator role. Evidence: "Assign the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role."
- **C4** MAINTAIN: While protocols are mentioned, there is vagueness over the specific roles or limits on the distribution of alerts.
- **C5** MAINTAIN: While some mitigation strategies exist, the potential for alert fatigue remains a concern that was not fully addressed.
- **C6** MAINTAIN: Reliance on user accountability presents a risk that may affect reliability and lead to erroneous alerts.

New challenges:

**C7** · MAJOR · OPERATIONS · targets GAP
- Challenge: The proposal lacks detailed measures to manage the volume of alerts effectively, which could overwhelm users and affect critical alert visibility.
- Failure scenario: Users become inundated with irrelevant cold relationship alerts, causing them to overlook critical notifications, leading to missed engagement opportunities and deteriorating relationships.
- Resolution test: What mechanisms will specifically be put in place to streamline alert notifications for users utilized in high-pressure environments?

**C8** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The reliance on existing logging practices and user accountability for maintaining accurate engagement records poses significant risks to the integrity of the alert system.
- Failure scenario: Users log incomplete or inaccurate engagement data, leading to premature alerts about cold relationships and frustration among staff attempting to manage diplomatic relations effectively.
- Resolution test: What specific processes will ensure that logged engagement activities are validated for accuracy before alerts are triggered?

Biggest worry: The potential for user alert fatigue and inaccurate alerts compromising diplomatic relationships is significant.

**Ledger:** raised 8 · open 5 · resolved 3 · escalated 0 · disagreement 0.53 → **continue**

## Round 3

### Proposer · confidence 75

- **C4** REVISE (missing decision) [changed S2]: This edit specifies the role responsible for receiving alerts about diplomatic contacts, thereby addressing the confidentiality concerns raised.
- **C5** DEFEND (acceptable risk): The risk of alert fatigue is acknowledged but managed with customization options for alerts, enabling users to filter out less relevant notifications.
- **C6** DEFEND (acceptable risk): While reliance on user accountability is a risk, dialogue with stakeholders post-release will establish a basis for refining data accuracy measures based on user experience.
- **C7** REVISE (missing decision) [changed S5]: This revision clarifies the management of alert notifications by including operational support from regional coordinators in filtering alerts, addressing the need for effective management in high-pressure environments.
- **C8** REVISE (missing decision) [changed S4]: This edit introduces a review process to ensure engagement activities are accurate and up-to-date, reducing the risk of triggering premature alerts about cold relationships.

Proposal changes: edited S2, S4, S5
- S2 now reads: Allow users to receive alerts via email regarding cold relationships, with protocols in place ensuring that alerts regarding diplomatic contacts are sent exclusively to users with the 'diplomatic_security' role in the CRM, who have clearance to handle sensitive information.
- S4 now reads: Provide options for users to set customized thresholds for inactivity alerts, ranging from 30 to 120 days, with the stipulation that valid engagement activities must include documented interactions such as meetings, emails, or official communications logged in the CRM, which will be reviewed monthly for accuracy by the CRM administrator.
- S5 now reads: Assign the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role, who will work with regional coordinators to filter and prioritize alerts based on urgency.

Biggest worry: The potential for inaccurate logging of engagement activities leading to premature alerts still remains a concern.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C4** ACCEPT: This statement clarifies the role authorized to receive alerts for diplomatic contacts, addressing confidentiality concerns. Fact: Only users with the 'diplomatic_security' role will receive alerts regarding diplomatic contacts. Evidence: "with protocols in place ensuring that alerts regarding diplomatic contacts are sent exclusively to users with the 'diplomatic_security' role in the CRM, who have clearance to handle sensitive information."
- **C5** MAINTAIN: While there is user customization, the concern of alert fatigue remains significant and was not fully mitigated.
- **C5** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C6** ACCEPT: This process significantly improves data quality and reliability, mitigating future risks of inaccurate alerts. Fact: Engagement activities will be reviewed monthly for accuracy to reduce premature alerts. Evidence: "which will be reviewed monthly for accuracy by the CRM administrator."
- **C7** ACCEPT: This collaborative approach to alert management provides necessary oversight to mitigate operational overload. Fact: Regional coordinators will assist the CRM administrator in filtering and prioritizing alerts. Evidence: "the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role, who will work with regional coordinators to filter and prioritize alerts based on urgency."
- **C8** ACCEPT: The creation of a review process establishes mechanisms to ensure accuracy of logged activities, reducing errors in alerts. Fact: Logged engagement activities will face monthly accuracy reviews. Evidence: "which will be reviewed monthly for accuracy by the CRM administrator."

Biggest worry: The risk of alert fatigue remains significant, as user customization alone may not be sufficient to prevent irrelevant alerts from overwhelming important notifications.

**Ledger:** raised 8 · open 0 · resolved 7 · escalated 1 · disagreement 0.07 → **converged**

## Final proposal

_This release implements an alert system that notifies users when engagement with country contacts remains inactive for a specified duration while establishing protocols to manage confidentiality and responsibility. Core enhancements clarify definitions, ownership, and protocols to minimize risks associated with alert distribution and user management, now including a formal monthly review for data accuracy._

**Core commitments**
- V1: Implement an alert system for detecting inactive relationships with country contacts.

**In scope**
- S1: Define 'cold relationship' as a lack of recorded engagement activities for 90 consecutive days, with an additional requirement that alerts are sent only to users who have authorization to view information regarding that country.
- S2: Allow users to receive alerts via email regarding cold relationships, with protocols in place ensuring that alerts regarding diplomatic contacts are sent exclusively to users with the 'diplomatic_security' role in the CRM, who have clearance to handle sensitive information.
- S3: Enable users to filter and view a list of contacts with cold relationships in the CRM.
- S4: Provide options for users to set customized thresholds for inactivity alerts, ranging from 30 to 120 days, with the stipulation that valid engagement activities must include documented interactions such as meetings, emails, or official communications logged in the CRM, which will be reviewed monthly for accuracy by the CRM administrator.
- S5: Assign the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role, who will work with regional coordinators to filter and prioritize alerts based on urgency.

**Out of scope**
- X1: This release will not include relationship-building suggestions based on contacts' engagement history.
- X2: This release will not integrate with external systems for engagement history tracking.

**Assumptions**
- A1: Users have sufficient privileges to set alert preferences and view engagement history; this depends on existing user role management capabilities.
- A2: Engagement activities are logged in the CRM; this depends on current CRM functionality for tracking such activities.
- A3: Users understand what constitutes a "cold relationship" based on the defined thresholds; this assumes adequate training and documentation is provided.

**Definitions**
- D1: "cold relationship" means a lack of recorded engagement activities with a country contact for 90 consecutive days.
- D2: "engagement activities" means any logged interaction or correspondence with a country contact, such as meetings, emails, or calls.

**Success criteria**
- K1: Achieve at least a 75% user satisfaction rate with the new alert system, measured through user surveys within one month of release.
