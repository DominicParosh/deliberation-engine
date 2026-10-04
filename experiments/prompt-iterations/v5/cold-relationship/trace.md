# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **consensus** after 3 rounds · 8 model calls (1 repairs)

## Round 1

### Proposer · confidence 70

_This release will implement a notification system that alerts users when engagement with a specific country has significantly decreased. The alerts will be designed for regional coordinators and project managers to help maintain active communication with government counterparts._

**Core commitments**
- V1: Users will receive alerts when no contact has been made with a country for a defined period.
- V2: The system will provide a dashboard feature to display engagement metrics and recent interactions.

**In scope**
- S1: The system will track engagement as interactions such as emails, meetings, and official correspondence recorded by users.
- S2: An alert will be triggered when there are no recorded interactions with a country for 90 days.
- S3: Regional coordinators and project managers will receive email notifications regarding cold relationships.
- S4: A dashboard will be implemented that displays engagement history with each country, including last interaction date.

**Out of scope**
- X1: This release will not involve changing how user interactions are recorded in the CRM.
- X2: Real-time engagement assessments based on live data will not be included in this release.
- X3: The alerts will not include recommendations for re-engagement strategies.

**Assumptions**
- A1: Users will have access to a history of interactions and will be able to log new ones, which depends on their existing permissions.
- A2: Email notifications can be sent from the CRM system, which depends on the organization's email infrastructure.
- A3: Users understand the importance of logging engagements, which depends on their training and organizational culture.
- A4: The CRM data reflects accurate engagement activities, which depends on user diligence in recording.

**Definitions**
- D1: "cold relationship" means no recorded engagement interaction with a country for 90 consecutive days.
- D2: "alert" means a notification sent by email to designated users informing them of a cold relationship.
- D3: "dashboard" means a visual interface within the CRM that displays metrics related to engagement with countries, including last engagement date and total interactions.

**Success criteria**
- K1: At least 75% of users report the alerts are timely and useful, measured through a post-release survey after three months of operation.

Biggest worry: There's a risk that the alert system may generate false alarms or overwhelm users with notifications.

### Critic · confidence 40

Pre-mortem: A year after launch, the notification system caused significant confusion and breaches of confidentiality. Several regional coordinators and project managers received alerts about cold relationships with countries that were still actively engaged in sensitive negotiations, leading to embarrassment and diplomatic fallout. In response, some country representatives expressed concerns about the organization's internal processes, and meetings were mismanaged due to the premature alerting.

Questions the request leaves open:
- What specific permissions do users have to access engagement history for other teams?
- What happens to the notification process when users change roles or leave the organization?
- How will the system handle countries with sensitive diplomatic considerations?
- How is the system ensuring that all user engagements are logged accurately prior to alert generation?
- What are the privacy implications of alerting users about cold relationships?
- What thresholds will be in place to determine if an alert is sent for multiple teams or stakeholders?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S2
- Challenge: The proposal does not explain how the alert for cold relationships protects against exposing sensitive diplomatic engagements.
- Failure scenario: A regional coordinator receives an alert about a cold relationship, not knowing that sensitive negotiations are underway, leading them to withdraw prematurely.
- Resolution test: How does the system prevent notifying users in situations where ongoing diplomatic discussions could be negatively affected by perceived inaction?

**C2** · MAJOR · DEFINITIONS · targets D1
- Challenge: The definition of 'cold relationship' is ambiguous and could allow for misinterpretation regarding its implications.
- Failure scenario: A project manager mistakenly assumes that because they haven't recorded any interactions in 90 days, it's acceptable to act on the alert without checking ongoing verbal communications or informal discussions.
- Resolution test: What criteria are used to assess whether a relationship is truly 'cold' beyond just the metric of recorded interactions?

**C3** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify who is responsible for maintaining and validating the accuracy of the engagement interaction recordings.
- Failure scenario: Data becomes stale due to a lack of assigned accountability, resulting in too many false alerts being sent and confusion among the teams.
- Resolution test: Who is designated as the data owner responsible for ensuring the accuracy of engagement records that drive this alerting system?

Biggest worry: The proposal could lead to sensitive diplomatic situations being mishandled due to alerts sent without context.

**Ledger:** raised 3 · open 3 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 75

- **C1** CONCEDE (should not build) [changed S3]: The edited item clarifies the conditions under which alerts will be sent, ensuring that sensitive diplomatic engagements are not mistakenly revealed.
- **C2** REVISE (missing decision) [changed D1]: The revised definition clarifies that ongoing diplomatic negotiations invalidate the cold relationship status, preventing misunderstandings regarding the implications of the alert.
- **C3** REVISE (missing decision) [changed S5]: This new scope item defines the accountability for data accuracy, enhancing the reliability of the alert system and ensuring that users can trust the engagement metrics provided.

Proposal changes: added S5; edited S3, D1
- S5 now reads: The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators.
- S3 now reads: Regional coordinators and project managers will receive email notifications regarding cold relationships, only when there are no ongoing diplomatic negotiations or sensitive discussions related to the country.
- D1 now reads: "cold relationship" means no recorded engagement interaction with a country for 90 consecutive days, without any ongoing diplomatic negotiations or sensitive discussions occurring during that time.

Biggest worry: Ensuring that the alert system effectively differentiates between cold relationships and ongoing diplomatic efforts.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** ACCEPT:  Evidence: "Regional coordinators and project managers will receive email notifications regarding cold relationships, only when there are no ongoing diplomatic negotiations or sensitive discussions related to the country."
- **C2** ACCEPT:  Evidence: "'cold relationship' means no recorded engagement interaction with a country for 90 consecutive days, without any ongoing diplomatic negotiations or sensitive discussions occurring during that time."
- **C3** ACCEPT:  Evidence: "The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators."

New challenges:

**C4** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not address what specific permissions users have to access engagement history for other teams, raising the risk of unauthorized exposure of diplomatic relationships.
- Failure scenario: A project manager in one team accesses engagement history from another team without proper permissions, leading to sensitive information being improperly shared or misinterpreted, potentially damaging diplomatic ties.
- Resolution test: What permissions do users have to view engagement history for other teams?

**C5** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not explain how the notification process will be handled when users change roles or leave the organization, which could disrupt the data integrity.
- Failure scenario: A regional coordinator retires and no one is assigned to maintain relationship data, leading to outdated engagements triggering alerts, causing confusion among project managers about active diplomatic relationships.
- Resolution test: What process is in place to manage the ownership of engagement records when users change roles or leave the organization?

**C6** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal does not clarify the privacy implications of alerting users about cold relationships, especially regarding sensitive diplomatic data.
- Failure scenario: A project manager receives an alert about a cold relationship, exposing their inability to accurately discern ongoing discussions, which impacts the organization's trust with key government counterparts.
- Resolution test: What privacy protocols are in place to ensure compliance when alerting users about cold relationships?

Biggest worry: Alerting users without clear permissions and privacy protocols could lead to serious diplomatic breaches.

**Ledger:** raised 6 · open 3 · resolved 3 · escalated 0 · disagreement 0.46 → **continue**

## Round 3

### Proposer · confidence 80

- **C4** REVISE (missing decision) [changed S3]: The edit clarifies user permissions around accessing engagement history, establishing clear limits on which team can view sensitive diplomatic relationships.
- **C5** REVISE (missing decision) [changed S5]: This edit specifies a process for updating ownership of engagement records when personnel changes occur, thereby ensuring data integrity and clarity on responsibility.
- **C6** REVISE (missing decision) [changed D1]: The revision defines how confidentiality will be maintained when users receive alerts about cold relationships, reducing the risks related to sensitive diplomatic data.

Proposal changes: edited S3, S5, D1
- S3 now reads: S3: Regional coordinators and project managers will receive email notifications regarding cold relationships, only when there are no ongoing diplomatic negotiations or sensitive discussions related to the country. Access to engagement history for each country will be limited to the user's designated team, with appropriate permissions required to view engagements from other teams.
- S5 now reads: S5: The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators. If a user changes roles or leaves the organization, a designated manager will be assigned to maintain the records associated with that user's engagements, ensuring data is properly updated to reflect active diplomatic relationships.
- D1 now reads: D1: 'cold relationship' means no recorded engagement interaction with a country for 90 consecutive days, without any ongoing diplomatic negotiations or sensitive discussions occurring during that time. The system will restrict alerts for cold relationships in situations where sensitive discussions are taking place, ensuring that alerts do not expose the organization to confidentiality breaches.

Biggest worry: Ensuring users adhere to the updated protocols around permission and ownership could be challenging.

### Critic · confidence 75 · CONCLUDE

Rulings:
- **C4** ACCEPT:  Evidence: "Access to engagement history for each country will be limited to the user's designated team, with appropriate permissions required to view engagements from other teams."
- **C5** ACCEPT:  Evidence: "If a user changes roles or leaves the organization, a designated manager will be assigned to maintain the records associated with that user's engagements, ensuring data is properly updated to reflect active diplomatic relationships."
- **C6** ACCEPT:  Evidence: "The system will restrict alerts for cold relationships in situations where sensitive discussions are taking place, ensuring that alerts do not expose the organization to confidentiality breaches."

Biggest worry: Future alerts might still lead to miscommunication if user engagement logs are not diligently maintained.

**Ledger:** raised 6 · open 0 · resolved 6 · escalated 0 · disagreement 0.00 → **consensus**

## Final proposal

_The release will implement a notification system that alerts users when engagement with a specific country has significantly decreased while safeguarding sensitive diplomatic relationships and ensuring clear protocols for data access and ownership. The alerts are designed for regional coordinators and project managers to help maintain active communication with government counterparts, with defined processes for ensuring data integrity and confidentiality._

**Core commitments**
- V1: Users will receive alerts when no contact has been made with a country for a defined period.
- V2: The system will provide a dashboard feature to display engagement metrics and recent interactions.

**In scope**
- S1: The system will track engagement as interactions such as emails, meetings, and official correspondence recorded by users.
- S2: An alert will be triggered when there are no recorded interactions with a country for 90 days.
- S3: S3: Regional coordinators and project managers will receive email notifications regarding cold relationships, only when there are no ongoing diplomatic negotiations or sensitive discussions related to the country. Access to engagement history for each country will be limited to the user's designated team, with appropriate permissions required to view engagements from other teams.
- S4: A dashboard will be implemented that displays engagement history with each country, including last interaction date.
- S5: S5: The responsibility for maintaining and validating the accuracy of engagement interaction recordings will lie with designated regional coordinators. If a user changes roles or leaves the organization, a designated manager will be assigned to maintain the records associated with that user's engagements, ensuring data is properly updated to reflect active diplomatic relationships.

**Out of scope**
- X1: This release will not involve changing how user interactions are recorded in the CRM.
- X2: Real-time engagement assessments based on live data will not be included in this release.
- X3: The alerts will not include recommendations for re-engagement strategies.

**Assumptions**
- A1: Users will have access to a history of interactions and will be able to log new ones, which depends on their existing permissions.
- A2: Email notifications can be sent from the CRM system, which depends on the organization's email infrastructure.
- A3: Users understand the importance of logging engagements, which depends on their training and organizational culture.
- A4: The CRM data reflects accurate engagement activities, which depends on user diligence in recording.

**Definitions**
- D1: D1: 'cold relationship' means no recorded engagement interaction with a country for 90 consecutive days, without any ongoing diplomatic negotiations or sensitive discussions occurring during that time. The system will restrict alerts for cold relationships in situations where sensitive discussions are taking place, ensuring that alerts do not expose the organization to confidentiality breaches.
- D2: "alert" means a notification sent by email to designated users informing them of a cold relationship.
- D3: "dashboard" means a visual interface within the CRM that displays metrics related to engagement with countries, including last engagement date and total interactions.

**Success criteria**
- K1: At least 75% of users report the alerts are timely and useful, measured through a post-release survey after three months of operation.
