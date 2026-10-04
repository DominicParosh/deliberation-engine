# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 2 rounds · 6 model calls (1 repairs)

## Round 1

### Proposer · confidence 75

_This release will implement an alert system that notifies designated users when no engagement has occurred with a country for a specified period. The primary users will be regional coordinators and project managers responsible for maintaining these relationships._

**Core commitments**
- V1: The system will send alerts to users when relationships with countries have no recorded engagement for 90 days.

**In scope**
- S1: The system will track engagement history defined as any logged communication or interaction with government contacts.
- S2: The system will send automated email notifications to designated regional coordinators and project managers after 90 days of inactivity.
- S3: Users will have the capability to configure the alert threshold (defaulting to 90 days) within their user settings.
- S4: The system will maintain a log of alerts sent, including timestamps and recipients, for audit purposes.

**Out of scope**
- X1: This release will not provide a way to analyze reasons for the cold relationship.
- X2: The release will not include features to automatically re-engage or suggest actions based on cold relationships.
- X3: The system will not alert on relationships with countries where no past engagement history exists.

**Assumptions**
- A1: Users are responsible for logging their engagements with government contacts promptly, which is crucial for maintaining accurate engagement history.
- A2: The organization has existing protocols for user email notifications that must be adhered to, which underpins the alert system.
- A3: Designated users will have access to the CRM system with necessary permissions to configure alert settings.

**Definitions**
- D1: 'Goes cold' means a period of 90 consecutive days without any recorded engagement in the system.
- D2: 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM.

**Success criteria**
- K1: At least 80% of the alerts should be acknowledged by the relevant users within 48 hours of receipt, measured by log records of user engagement.

Biggest worry: The assumption that users will log all engagements consistently may not hold, leading to inaccurate alerts.

### Critic · confidence 40

Pre-mortem: A year after launch, the alert system mistakenly sent cold engagement notifications to regional coordinators regarding countries with ongoing sensitive diplomatic discussions. Because the system only considered logged engagements, critical communications were not recorded in the CRM, leading to severe diplomatic misunderstandings and damaging relationships. The alerts reached personnel who were not authorized to act on such sensitive matters, causing a potential breach of confidentiality and trust.

Questions the request leaves open:
- What specific permissions are required to access engagement history and alerts?
- How are roles defined for who receives alerts, and what happens when users change roles or leave?
- What are the criteria for determining which country engagements are logged correctly, especially in sensitive contexts?
- How will the system handle situations where a designated user is not available to respond to a cold relationship alert?
- What safeguards are in place to ensure alerts are not sent based on inaccurate or incomplete engagement records?
- What happens if the default alert threshold of 90 days leads to inappropriate notifications in fragile diplomatic contexts?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: There are no defined permissions for who can see engagement history or receive alerts, risking exposure of sensitive diplomatic information to unauthorized personnel.
- Failure scenario: A regional coordinator receives an alert about a cold relationship with a sensitive country but lacks the clearance to handle that information, leading to a potential breach if acted upon by someone uninformed.
- Resolution test: What are the defined permissions for accessing engagement records and receiving cold alerts?

**C2** · MAJOR · OWNERSHIP · targets GAP
- Challenge: There is no clear process in place detailing what happens when designated users change roles or leave the organization, potentially losing oversight of cold engagement alerts.
- Failure scenario: When a regional coordinator leaves, their alerts and dashboards are not reassigned, leaving a gap in responsibility to follow up on cold relationships, which could further erode diplomatic ties.
- Resolution test: What processes exist for reassigning alert responsibilities when users change roles or leave?

**C3** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The term 'engagement' is vaguely defined and does not specify the required documentation style or level of detail needed for proper logging, which can lead to inconsistencies.
- Failure scenario: A project manager incorrectly logs a short email correspondence as engagement, leading to false alerts and decisions made based on perceived coldness in relationships that are in fact active.
- Resolution test: What level of detail is required for an engagement to be considered valid in the alert system?

**C4** · MAJOR · OPERATIONS · targets GAP
- Challenge: The proposal does not address how ongoing engagement initiatives will be managed, especially concerning users who may be unavailable when alert notifications are sent.
- Failure scenario: An alert is sent to a project manager who is out of office, and no one else on the team is aware of the cold relationship status, resulting in a failure to act.
- Resolution test: What procedures are in place for addressing alerts if the designated user is unavailable?

**C5** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: There are no defined safeguards to prevent sending alerts based on incomplete or inaccurate engagement records that could expose sensitive information.
- Failure scenario: An alert based on missing logged engagements prompts a response from an unauthorised individual, leading to decisions being taken in sensitive situations based on incorrect assumptions.
- Resolution test: What safeguards are implemented to ensure that alerts are based on accurate and complete engagement history?

**C6** · MINOR · DEFINITIONS · targets GAP
- Challenge: The proposal does not specify how the default alert threshold of 90 days may pose risks in situations where rapid diplomatic engagement is critical.
- Failure scenario: An alert is erroneously sent to regional coordinators about a country deemed cold during a subtle but ongoing political dialogue, prompting unnecessary escalations or miscommunications.
- Resolution test: Is there a process to review and potentially adjust the default alert threshold based on specific diplomatic contexts?

Biggest worry: The proposal lacks proper definitions and ownership guidelines, which could lead to exposing sensitive information and mismanagement of cold relationship alerts.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S5]: This edit defines the permissions around access to sensitive information and ensures that only authorized personnel can view engagement history and receive alerts.
- **C2** REVISE (missing decision) [changed S6]: This defines a clear process for handling changes in user roles or exits, ensuring that responsibility for cold relationship alerts is maintained within the team.
- **C3** REVISE (missing decision) [changed D3]: The edit clarifies the definition of engagement, ensuring that logs contain sufficient detail to prevent inconsistencies in logging practices.
- **C4** REVISE (missing decision) [changed S7]: This establishes a clear procedure for handling alerts when designated users are unavailable, maintaining oversight of cold engagement alerts.
- **C5** REVISE (missing decision) [changed S8]: This edit establishes safeguards to ensure alerts are based on accurate data, helping to prevent unauthorized actions prompted by incorrect assumptions.
- **C6** DEFEND (needs human decision): The threshold adjustment based on political context requires human oversight and alignment with diplomatic strategy, which can’t be predetermined in this proposal.

Proposal changes: added S5, S6, S7, S8, D3
- S5 now reads: The system will assign permissions for users to access engagement history and receive cold alerts based on their role. Only users with a clearance level defined as 'Regional Coordinator' or 'Project Manager' will be eligible to receive alerts and view related engagement history.
- S6 now reads: The system will have an automated process that reassigns alert responsibilities to a designated backup user within the same team when a primary user leaves the organization or changes roles. The administrator will be notified to confirm the reassignment.
- S7 now reads: If a designated user is unavailable, alerts will be escalated to their immediate supervisor or assigned backup user who will be responsible for following up on the alert.
- S8 now reads: The system will validate existing engagement records for completeness and accuracy before sending alerts. Alerts based on incomplete or inaccurate records will be flagged for review, and only validated accounts will trigger notifications.
- D3 now reads: 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM, including the date, participants, communication method (e.g., email, call, meeting), and summary of the discussion.

Biggest worry: I am concerned about how effectively the responsibilities will be reassigned when users leave or change roles.

### Critic · confidence 75 · CONTINUE

Rulings:
- **C1** ACCEPT: The permissions for accessing sensitive information are clearly defined. Fact: Only defined roles can access engagement history and receive alerts. Evidence: "Only users with a clearance level defined as 'Regional Coordinator' or 'Project Manager' will be eligible to receive alerts and view related engagement history."
- **C2** ACCEPT: Clear processes exist to handle user role changes and ensure oversight. Fact: Alert responsibilities are reassigned to a backup user when a primary user leaves or changes roles, and administrators are notified. Evidence: "The system will have an automated process that reassigns alert responsibilities to a designated backup user within the same team when a primary user leaves the organization or changes roles."
- **C3** ACCEPT: The definition now provides clarity on the details required for engagement. Fact: Engagement records must include specific details such as date, participants, method, and summary to be valid. Evidence: "'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM, including the date, participants, communication method (e.g., email, call, meeting), and summary of the discussion."
- **C4** ESCALATE: No definition of roles or processes for alert follow-up is clearly stated, leaving potential oversight gaps.
- **C5** ACCEPT: Safeguards prevent unauthorized alerts based on incomplete records. Fact: Alerts will only be sent based on validated engagement records to prevent misinformation. Evidence: "The system will validate existing engagement records for completeness and accuracy before sending alerts. Alerts based on incomplete or inaccurate records will be flagged for review, and only validated accounts will trigger notifications."
- **C6** ESCALATE: The process for reviewing the alert threshold is determined by human discretion, which is outside of the proposal's scope.

Biggest worry: The lack of a defined process for adjusting the alert threshold could lead to inappropriate notifications in sensitive diplomatic situations.

**Ledger:** raised 6 · open 0 · resolved 4 · escalated 2 · disagreement 0.25 → **converged**

## Final proposal

_This release will implement an alert system that notifies designated users when no engagement has occurred with a country for a specified period, with defined permissions for access and clear processes for ownership and reassignment. New decisions made clarify the definitions of engagement and set safeguards against sending incorrect alerts._

**Core commitments**
- V1: The system will send alerts to users when relationships with countries have no recorded engagement for 90 days.

**In scope**
- S1: The system will track engagement history defined as any logged communication or interaction with government contacts.
- S2: The system will send automated email notifications to designated regional coordinators and project managers after 90 days of inactivity.
- S3: Users will have the capability to configure the alert threshold (defaulting to 90 days) within their user settings.
- S4: The system will maintain a log of alerts sent, including timestamps and recipients, for audit purposes.
- S5: The system will assign permissions for users to access engagement history and receive cold alerts based on their role. Only users with a clearance level defined as 'Regional Coordinator' or 'Project Manager' will be eligible to receive alerts and view related engagement history.
- S6: The system will have an automated process that reassigns alert responsibilities to a designated backup user within the same team when a primary user leaves the organization or changes roles. The administrator will be notified to confirm the reassignment.
- S7: If a designated user is unavailable, alerts will be escalated to their immediate supervisor or assigned backup user who will be responsible for following up on the alert.
- S8: The system will validate existing engagement records for completeness and accuracy before sending alerts. Alerts based on incomplete or inaccurate records will be flagged for review, and only validated accounts will trigger notifications.

**Out of scope**
- X1: This release will not provide a way to analyze reasons for the cold relationship.
- X2: The release will not include features to automatically re-engage or suggest actions based on cold relationships.
- X3: The system will not alert on relationships with countries where no past engagement history exists.

**Assumptions**
- A1: Users are responsible for logging their engagements with government contacts promptly, which is crucial for maintaining accurate engagement history.
- A2: The organization has existing protocols for user email notifications that must be adhered to, which underpins the alert system.
- A3: Designated users will have access to the CRM system with necessary permissions to configure alert settings.

**Definitions**
- D1: 'Goes cold' means a period of 90 consecutive days without any recorded engagement in the system.
- D2: 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM.
- D3: 'Engagement' means any documented communication, meeting, or interaction with a country representative logged in the CRM, including the date, participants, communication method (e.g., email, call, meeting), and summary of the discussion.

**Success criteria**
- K1: At least 80% of the alerts should be acknowledged by the relevant users within 48 hours of receipt, measured by log records of user engagement.
