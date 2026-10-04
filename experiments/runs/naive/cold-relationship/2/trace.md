# Deliberation trace: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Policy `naive` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 2 rounds · 5 model calls (0 repairs)

## Round 1

### Proposer · confidence 70

_This release will implement an alert system that notifies users when their engagement with a country representative has not been updated for a specified duration. The primary users will be regional coordinators and project managers responsible for maintaining relationships with country counterparts._

**Core commitments**
- V1: Implement an alert system to notify users when engagement records are inactive for a period of time.
- V2: Allow users to customize the duration that defines 'cold' relationships.

**In scope**
- S1: Users will receive an email notification if no engagement has been recorded for a specified duration of 90 days.
- S2: Regional coordinators and project managers will have the ability to set the 'inactive duration' for alerts between 30 to 120 days.
- S3: An 'engagement record' will be defined as any update made to a country contact's record in the CRM, including emails, project updates, or meeting minutes.
- S4: The system will have a dashboard view for users to see a list of 'cold' relationships based on their customizable thresholds.

**Out of scope**
- X1: This release will not include historical data analytics or thresholds beyond 120 days.
- X2: The system will not track communication methods outside the CRM (e.g., personal emails or calls).
- X3: No functionality will be provided to automatically re-engage with 'cold' countries, only notifications.

**Assumptions**
- A1: Users will regularly update engagement records within the CRM to ensure accurate tracking of relationships.
- A2: Users have access to email notifications and check their inbox for alerts regarding cold relationships.
- A3: Engagement records include updates to projects or meetings with country contacts; this is necessary to define cold relationships.
- A4: The users' roles allow them to set alert durations but not to modify system-level settings.

**Definitions**
- D1: 'Cold' means a lack of engagement record updates for a specified duration of time.
- D2: 'Engagement record' means any documented interaction, update, or note added to the contact's record in the CRM.

**Success criteria**
- K1: At least 75% of users report that they received timely alerts for cold relationships within the first month after implementation, measured by user feedback surveys.

Biggest worry: Users may not consistently update engagement records, leading to unreliable alerts.

### Critic · confidence 40

Pre-mortem: A year after launch, the alert system erroneously triggered notifications to all regional coordinators about cold relationships that were unrelated to their responsibilities. As a result, country representatives were bombarded with inquiries from multiple users, leading to confusion and diplomatic strain with key partners. This situation deteriorated relationships further and caused a significant incident report that highlighted a lack of clarity in user roles and permissions regarding engagement records.

Questions the request leaves open:
- Which roles are restricted from seeing alerts about other country's engagements?
- How is the definition of 'cold' relationship enforced and monitored?
- What specific conditions lead to a false alert being sent?
- What happens if a user leaves the organization or their role changes?
- How are users held accountable for updating engagement records?
- What measures are in place to protect sensitive or confidential diplomatic data when sending alerts?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not specify which roles are restricted from seeing alerts about each other's engagements, creating the risk of sensitive information being exposed to unauthorized users.
- Failure scenario: A regional coordinator receives alerts for cold relationships regarding countries outside their responsibility, leading to potential diplomatic breaches as they contact counterparts without proper context or authority.
- Resolution test: Which roles are restricted from seeing alerts about other project teams' engagement records?

**C2** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The definition of 'cold' relationship is ambiguous and only time-based. There is no mention of the types or significance of engagements needed, nor how they relate to ongoing projects or diplomatic status.
- Failure scenario: A country could be categorized as 'cold' despite active diplomatic discussions that do not produce formal updates, leading to a false sense of urgency in engagement.
- Resolution test: What specific engagement activities must occur to prevent a relationship from being deemed 'cold'?

**C3** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal lacks clarity on accountability for users who fail to update engagement records, leading to reliance on users to self-report their engagement activities without oversight.
- Failure scenario: A project manager neglects to update records, resulting in multiple false alerts. Other team members are confused about whether the relationship is indeed cold, damaging collaboration efforts.
- Resolution test: What actions will be taken if users do not update their engagement records regularly?

**C4** · MAJOR · OPERATIONS · targets GAP
- Challenge: The impact of false alerts has not been considered, particularly regarding alert fatigue among users, which could lead to missed important notifications.
- Failure scenario: Users become desensitized to alerts because of frequent false notifications of cold relationships, missing actual alerts for significant engagement failures.
- Resolution test: What procedures are in place to minimize false alerts and manage user alert fatigue?

**C5** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not address how alerts will protect sensitive diplomatic data especially when communicated via email notifications.
- Failure scenario: An alert containing sensitive information is sent to the wrong user due to misconfigured permissions, leading to a leak of confidential information.
- Resolution test: What specific items are included in the email alerts, and how are sensitive details excluded from notifications?

**C6** · MINOR · DEFINITIONS · targets GAP
- Challenge: The term 'engagement record' is broad and could lead to misinterpretation. Specific examples of what constitutes valid engagement are needed.
- Failure scenario: A user updates a record incorrectly, marking it as engagement, while crucial interactions go unrecorded, leading to misclassifying a relationship as cold.
- Resolution test: What specific types of documentation count as valid engagement records for the purposes of this alert system?

Biggest worry: The ambiguity in roles, definitions, and accountability measures could lead to significant diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S5]: This edit specifies the restriction on alert visibility, preventing unauthorized users from accessing sensitive information about engagements.
- **C2** REVISE (missing decision) [changed D1]: This revision clarifies that not only is the time period a factor in determining a 'cold' relationship, but regular engagements are also required to maintain an active status.
- **C3** REVISE (missing decision) [changed S6]: This new item introduces a structured oversight mechanism to ensure users maintain engagement records and sets a protocol for escalation in cases of neglect.
- **C4** REVISE (missing decision) [changed S7]: This measure puts in place a strategy to mitigate false alerts and manage user alert fatigue by controlling how often notifications can be sent.
- **C5** REVISE (missing decision) [changed S8]: This edit specifies what information will be shared in the alerts while ensuring that no sensitive details are included, thus safeguarding diplomatic data.
- **C6** REVISE (missing decision) [changed D3]: This definition provides clear guidelines on what can be classified as an engagement record to eliminate ambiguity and prevent misclassifications.

Proposal changes: added S5, S6, S7, S8, D3; edited D1
- S5 now reads: Users with roles of 'executive-level staff' and 'other project managers' will not receive alerts about cold relationships from teams outside their own. Only regional coordinators will receive alerts pertaining to their direct country responsibilities.
- S6 now reads: The CRM will include a system prompt to remind users to update engagement records if no updates have been made for 30 days. Failure to update records will flag users for a review process by their supervisor every quarter.
- S7 now reads: Alerts will be governed by a threshold management mechanism in the system, which will track user engagement frequency to limit alerts to once per week for any individual user, to minimize alert fatigue.
- S8 now reads: Email alerts will only contain the country name, the date of the most recent engagement update, and a reminder to check the CRM for further details. No sensitive content from the engagement records will be included.
- D3 now reads: 'Engagement record' means any documented interaction, such as email correspondence, meeting notes, project updates, or any formal record that reflects a discussion or negotiation with a country contact added to the CRM, excluding non-official communications.
- D1 now reads: 'Cold' means a lack of engagement record updates for a specified duration of 90 days, and at least one documented interaction must occur every 30 days to prevent a relationship from being deemed cold.

Biggest worry: Changes to alerts and record definitions may introduce complexity that users might find challenging to navigate.

### Critic · confidence 90 · CONCLUDE

Rulings:
- **C1** ACCEPT: The proposal now specifies which roles will receive alerts, addressing the challenge. Fact: Only regional coordinators will receive alerts pertaining to their direct country responsibilities, preventing unauthorized access to sensitive information. Evidence: "S5: Users with roles of 'executive-level staff' and 'other project managers' will not receive alerts about cold relationships from teams outside their own. Only regional coordinators will receive alerts pertaining to their direct country responsibilities."
- **C2** ACCEPT: The definition of 'cold' now includes both time and interaction criteria, thereby clarifying the determination of cold relationships. Fact: A relationship can be deemed 'cold' if no engagement records are updated for 90 days without at least one documented interaction every 30 days. Evidence: "D1: 'Cold' means a lack of engagement record updates for a specified duration of 90 days, and at least one documented interaction must occur every 30 days to prevent a relationship from being deemed cold."
- **C3** ACCEPT: The addition of a review process ensures accountability for record maintenance. Fact: Users who do not update their engagement records regularly will be flagged for a review process by their supervisor every quarter. Evidence: "S6: The CRM will include a system prompt to remind users to update engagement records if no updates have been made for 30 days. Failure to update records will flag users for a review process by their supervisor every quarter."
- **C4** ACCEPT: This limit on alert frequency appropriately addresses the concern about alert fatigue. Fact: Alerts will be limited to once per week for each individual user. Evidence: "S7: Alerts will be governed by a threshold management mechanism in the system, which will track user engagement frequency to limit alerts to once per week for any individual user, to minimize alert fatigue."
- **C5** ACCEPT: This adequately addresses confidentiality concerns around email notifications. Fact: Email alerts will not include sensitive content, only basic information about the country and last engagement date. Evidence: "S8: Email alerts will only contain the country name, the date of the most recent engagement update, and a reminder to check the CRM for further details. No sensitive content from the engagement records will be included."
- **C6** ACCEPT: This clarification helps to eliminate ambiguity around what constitutes an engagement record. Fact: Valid engagement records include formal documented interactions. Evidence: "D3: 'Engagement record' means any documented interaction, such as email correspondence, meeting notes, project updates, or any formal record that reflects a discussion or negotiation with a country contact added to the CRM, excluding non-official communications."

Biggest worry: While clarity has improved, any role misconfiguration could still cause the system to alert inappropriate users.

**Ledger:** raised 6 · open 0 · resolved 6 · escalated 0 · disagreement 0.00 → **consensus**

## Final proposal

_This release will implement an alert system that notifies users when their engagement with a country representative has not been updated for a specified duration. The alerts will be restricted based on user roles and will ensure that sensitive information is not exposed, with added oversight mechanisms to maintain the accuracy of engagement records._

**Core commitments**
- V1: Implement an alert system to notify users when engagement records are inactive for a period of time.
- V2: Allow users to customize the duration that defines 'cold' relationships.

**In scope**
- S1: Users will receive an email notification if no engagement has been recorded for a specified duration of 90 days.
- S2: Regional coordinators and project managers will have the ability to set the 'inactive duration' for alerts between 30 to 120 days.
- S3: An 'engagement record' will be defined as any update made to a country contact's record in the CRM, including emails, project updates, or meeting minutes.
- S4: The system will have a dashboard view for users to see a list of 'cold' relationships based on their customizable thresholds.
- S5: Users with roles of 'executive-level staff' and 'other project managers' will not receive alerts about cold relationships from teams outside their own. Only regional coordinators will receive alerts pertaining to their direct country responsibilities.
- S6: The CRM will include a system prompt to remind users to update engagement records if no updates have been made for 30 days. Failure to update records will flag users for a review process by their supervisor every quarter.
- S7: Alerts will be governed by a threshold management mechanism in the system, which will track user engagement frequency to limit alerts to once per week for any individual user, to minimize alert fatigue.
- S8: Email alerts will only contain the country name, the date of the most recent engagement update, and a reminder to check the CRM for further details. No sensitive content from the engagement records will be included.

**Out of scope**
- X1: This release will not include historical data analytics or thresholds beyond 120 days.
- X2: The system will not track communication methods outside the CRM (e.g., personal emails or calls).
- X3: No functionality will be provided to automatically re-engage with 'cold' countries, only notifications.

**Assumptions**
- A1: Users will regularly update engagement records within the CRM to ensure accurate tracking of relationships.
- A2: Users have access to email notifications and check their inbox for alerts regarding cold relationships.
- A3: Engagement records include updates to projects or meetings with country contacts; this is necessary to define cold relationships.
- A4: The users' roles allow them to set alert durations but not to modify system-level settings.

**Definitions**
- D1: 'Cold' means a lack of engagement record updates for a specified duration of 90 days, and at least one documented interaction must occur every 30 days to prevent a relationship from being deemed cold.
- D2: 'Engagement record' means any documented interaction, update, or note added to the contact's record in the CRM.
- D3: 'Engagement record' means any documented interaction, such as email correspondence, meeting notes, project updates, or any formal record that reflects a discussion or negotiation with a country contact added to the CRM, excluding non-official communications.

**Success criteria**
- K1: At least 75% of users report that they received timely alerts for cold relationships within the first month after implementation, measured by user feedback surveys.
