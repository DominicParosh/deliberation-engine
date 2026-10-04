# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 6 rounds · 19 model calls (8 repairs)

## Round 1

### Proposer · confidence 70

_This release will enable users to identify and prioritize their most influential contacts by tracking influence metrics associated with each contact. It is designed for regional coordinators and project managers in the Government CRM system._

**Core commitments**
- V1: Establish a system for categorizing contacts based on a defined 'influence score'.
- V2: Provide users with the ability to filter and sort contacts based on their influence score.

**In scope**
- S1: Create a rating system where each contact can be assigned an 'influence score' ranging from 1 to 10, where 10 indicates the highest level of influence.
- S2: Allow users to view the influence scores of contacts in the contact details section of the CRM.
- S3: Enable filtering of contact lists by influence score for regional coordinators and project managers.
- S4: Provide a report feature that lists contacts sorted by influence score for 10 or more entries.

**Out of scope**
- X1: This release will not include automated updates of the influence scores based on external data or events.
- X2: The influence scoring system will not incorporate any social media metrics.
- X3: This release does not include training or educational materials on how to utilize influence scores.

**Assumptions**
- A1: Users have the necessary permissions to view and modify contact records; this is necessary for them to be able to assign and change influence scores.
- A2: The organization has established criteria for defining and calculating an influence score; without this, the scoring system cannot be implemented.
- A3: There is a clear understanding and agreement on what factors contribute to a contact's influence score; without this, the accuracy of scores will vary.

**Definitions**
- D1: 'Influence score' means a numerical value between 1 and 10 assigned to each contact, representing their level of influence based on criteria defined by the organization.
- D2: 'Regional coordinators' means users in the CRM who manage relationships and engagements for specific geographic areas.
- D3: 'Project managers' means users in the CRM responsible for overseeing and executing projects involving government contacts.

**Success criteria**
- K1: At least 80% of users report that the influence score feature helps them prioritize contacts effectively, measured through a user feedback survey after 3 months of deployment.

Biggest worry: The lack of established criteria for calculating influence scores may lead to inconsistencies in how contacts are prioritized.

### Critic · confidence 40

Pre-mortem: A year after the launch of the 'influence score' feature, it was discovered that the scoring system was based on inaccurate factors and was applied inconsistently across different regions. Consequently, certain high-risk contacts were mistakenly deemed less influential due to subjective inputs, resulting in sensitive communications being ignored during key negotiations. This failure led to a diplomatic breach with significant ramifications for international relations.

Questions the request leaves open:
- What factors contribute to a contact's influence score and how are they defined?
- What safeguards are in place to ensure that influence scores are assigned consistently and accurately?
- Who has the authority to modify the influence scores and what processes are in place to prevent misuse of this power?
- How will influence scores impact alerts or notifications?
- What happens when the designated users (regional coordinators, project managers) change roles or leave?
- What measures are in place to protect the sensitive data associated with influence scoring from unauthorized access or exposure?

New challenges:

**C1** · BLOCKER · OWNERSHIP · targets A1, D3
- Challenge: The proposal does not clarify who specifically has the authority to assign and modify influence scores, creating risks for misuse.
- Failure scenario: A project manager leaves the organization without updating the influence scores for critical contacts. The new project manager is unaware of the importance of these contacts due to incorrect scores, leading to a series of missed diplomatic opportunities.
- Resolution test: Who in the organization is authorized to assign and modify influence scores?

**C2** · MAJOR · DEFINITIONS · targets D1, A2
- Challenge: The criteria for what constitutes an influence score and how it is calculated are not defined, leading to inconsistent scoring across different users.
- Failure scenario: Multiple users assign influence scores based on personal judgment rather than a standardized method, resulting in conflicting scores for the same contacts. This discrepancy results in misalignment on who should be prioritized in engagements, complicating the decision-making process.
- Resolution test: What are the agreed-upon criteria and factors used to calculate the influence score?

**C3** · MAJOR · CONFIDENTIALITY · targets S1
- Challenge: The scoring system could lead to potential confidentiality breaches, as the influence scores might reveal sensitive assessments of contacts that should be protected.
- Failure scenario: A report generated based on influence scores is shared with an unintended audience, exposing sensitive evaluations of key contacts, damaging relationships with diplomatic counterparts.
- Resolution test: What measures are in place to restrict access to influence scores to authorized users only, and how is this enforced?

**C4** · MAJOR · DATA_QUALITY · targets A3, S4
- Challenge: The proposal lacks clarity on how influence scores will be validated and maintained for accuracy, raising concerns about data quality.
- Failure scenario: Users based their outreach on outdated or incorrect influence scores because there was no system in place to regularly reassess the scores, resulting in wasted efforts and strained relationships.
- Resolution test: What process will be established to routinely validate and update the influence scores for accuracy?

**C5** · MINOR · OPERATIONS · targets A1
- Challenge: The proposal does not consider the impact on users' workload in maintaining and assigning influence scores, potentially leading to user fatigue.
- Failure scenario: Regional coordinators may become overwhelmed with the responsibility of constantly updating influence scores, leading to burnout and potential neglect of important diplomatic engagements.
- Resolution test: How much time and effort are expected from users in managing and updating influence scores on a regular basis?

**C6** · MINOR · COMPLIANCE · targets GAP
- Challenge: The proposal does not address how long influence data will be retained or the legal basis for processing this personal data, raising compliance issues.
- Failure scenario: Personal data connected to influence scores is retained longer than necessary, creating a legal risk for the organization if it is challenged regarding data retention practices.
- Resolution test: What is the defined retention policy for influence score data, and how is compliance with data protection regulations ensured?

Biggest worry: The undefined criteria and lack of safeguards for influence scores risk severe diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed A1]: This edit clarifies who has the authority to assign and modify influence scores, ensuring a clear process to mitigate risks associated with incorrect scores.
- **C2** REVISE (missing decision) [changed A2]: This edit ensures that there is a standardized method for scoring that all users will follow, which addresses the risk of inconsistency.
- **C3** REVISE (missing decision) [changed S1]: This change restricts access to influence scores, which protects sensitive assessments and reinforces confidentiality.
- **C4** DEFEND (needs human decision): The process to routinely validate and update influence scores relies on organizational policies and user feedback mechanisms that need to be defined by the stakeholders.
- **C5** DEFEND (acceptable risk): (No usable answer: its edits broke the rules twice; the proposal stands.)
- **C6** REVISE (missing decision) [changed A4]: This decision establishes a retention policy for influence score data, addressing compliance risks associated with personal data retention.

Proposal changes: added A4; edited S1, A1, A2
- A4 now reads: Influence score data will be retained for a period of 3 years, after which it will be reviewed and either archived or deleted in compliance with data protection regulations.
- S1 now reads: Create a rating system where each contact can be assigned an 'influence score' ranging from 1 to 10, where 10 indicates the highest level of influence. Access to view influence scores will be limited to authorized users including regional coordinators and project managers only.
- A1 now reads: The authority to assign and modify influence scores is limited to regional coordinators and project managers, who must document any changes made to maintain transparency and accountability.
- A2 now reads: The criteria for defining an influence score will be established in collaboration with stakeholders and documented, outlining factors such as engagement history, seniority, and recent interactions.

Biggest worry: Keeping influence scores accurate and up-to-date may still depend heavily on user engagement and organizational policies.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C1** ESCALATE: While the access to viewing influence scores is noted, the authority to assign and modify influence scores is based on an assumption that does not provide a direct commitment.
- **C2** ESCALATE: While it mentions tracking influence metrics, specific criteria for scoring are still dependent on stakeholder collaboration and are not defined in the proposals.
- **C3** ACCEPT: This directly addresses the confidentiality concern, ensuring that sensitive information is protected. Fact: Only authorized users can see influence scores, protecting sensitive assessments. Evidence: "Access to view influence scores will be limited to authorized users including regional coordinators and project managers only."
- **C4** ESCALATE: This does not provide a concrete process for ensuring the accuracy of influence scores, which is required to maintain quality.
- **C5** ESCALATE: The proposal fails to adequately address the workload implications for users in managing and assigning scores, which could lead to fatigue.
- **C6** ESCALATE: This answer does not provide a clear legal basis for processing personal data nor establish a timeline for data retention as it is currently told in an assumption.

New challenges:

**C7** · MAJOR · DATA_QUALITY · targets A3
- Challenge: The proposal lacks clarity on how influence scores will be validated and maintained after the initial assignment, raising concerns about data quality.
- Failure scenario: Influence scores reflect outdated or irrelevant factors, leading to significant misjudgment in prioritizing contacts, resulting in missed diplomatic opportunities.
- Resolution test: What ongoing process will be defined to ensure influence scores are regularly updated and remain accurate?

**C8** · MAJOR · OPERATIONS · targets A1
- Challenge: There is no clarity on the expected workload and time commitment for users to maintain the influence scoring system, which could lead to fatigue and inefficiency.
- Failure scenario: A regional coordinator receives an overwhelming number of contacts to rate, leading to inconsistent scores and missed opportunities due to neglect of important relationships.
- Resolution test: What is the expected time commitment for users to manage and update influence scores?

Biggest worry: There are still critical gaps regarding data quality management and user workload impacts that could lead to serious operational issues.

**Ledger:** raised 8 · open 2 · resolved 1 · escalated 5 · disagreement 0.87 → **continue**

## Round 3

### Proposer · confidence 85

- **C7** REVISE (missing decision) [changed A3]: My edit establishes a regular review process for maintaining the accuracy of influence scores, ensuring they remain relevant and reflect current factors affecting influence.
- **C8** REVISE (missing decision) [changed A1]: This edit clarifies the expected time commitment for users, helping to mitigate potential fatigue and establish clear expectations for managing influence scores.

Proposal changes: edited A1, A3
- A1 now reads: The authority to assign and modify influence scores is limited to regional coordinators and project managers, who must document any changes made, with an expected workload of up to 2 hours per month on average for maintaining and updating the influence scores.
- A3 now reads: There is a clear understanding and agreement on what factors contribute to a contact's influence score; these factors will be reviewed quarterly to maintain the relevance and accuracy of the scores assigned, with required documentation of the reviews provided by the regional coordinators and project managers.

Biggest worry: Ensuring the defined review processes for influence scores are adequately followed to avoid data quality issues.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C7** MAINTAIN: The proposal still lacks a concrete ongoing process for ensuring that influence scores remain accurate, as it only outlines a review based on assumptions.
- **C8** MAINTAIN: The workload and time commitment for users is defined, but this is based on an assumption rather than a decision made in the proposal.

New challenges:

**C9** · BLOCKER · DATA_QUALITY · targets GAP
- Challenge: The proposal does not provide a clear mechanism for validating or updating influence scores post-assignment, which could lead to outdated or incorrect scores being used.
- Failure scenario: Influence scores are never updated or reviewed consistently, leading to key diplomatic contacts being misprioritized, compromising important negotiations.
- Resolution test: What specific process will be implemented to validate and update influence scores regularly?

**C10** · BLOCKER · OPERATIONS · targets GAP
- Challenge: There is no defined governance structure to manage the influence scoring process over time, which is essential for consistent application and accountability.
- Failure scenario: With multiple users assigning scores independently, there is no consistent method leading to confusion about score assignment, resulting in potentially damaging diplomatic oversights.
- Resolution test: What governance measures are in place to oversee the assignment and maintenance of influence scores?

Biggest worry: Without a defined validation and governance process, influence scores may remain inconsistent and unreliable.

**Ledger:** raised 10 · open 4 · resolved 1 · escalated 5 · disagreement 0.90 → **continue**

## Round 4

### Proposer · confidence 75

- **C7** REVISE (missing decision) [changed A3]: This edit establishes a clear ongoing review process for maintaining the accuracy of influence scores after their initial assignment, ensuring that they remain relevant and reflective of current factors affecting influence.
- **C8** REVISE (missing decision) [changed A1]: This edit clarifies the decision regarding the expected time commitment for users, helping to prevent fatigue and establishing explicit expectations for managing influence scores.
- **C9** REVISE (missing decision) [changed A4]: This edit introduces a governance structure and defines the process for validating and updating influence scores, ensuring they remain accurate and relevant.
- **C10** REVISE (missing decision) [changed A3]: This edit provides a governance structure to manage the influence scoring process over time, ensuring consistency and accountability in the assigning and updating of influence scores.

Proposal changes: edited A1, A3, A4
- A1 now reads: The authority to assign and modify influence scores is limited to regional coordinators and project managers. Each regional coordinator and project manager is expected to dedicate no more than 2 hours per month to review, assign, and modify influence scores, ensuring that their workload remains manageable.
- A3 now reads: The criteria for defining an influence score will be established in collaboration with stakeholders and documented, outlining factors such as engagement history, seniority, and recent interactions. A governance team composed of designated regional coordinators will be created to oversee the influence scoring process, ensuring consistent application and accountability in assigning and updating scores.
- A4 now reads: Influence score data will be retained for a period of 3 years, after which it will be reviewed for accuracy and relevance, and either archived or deleted in compliance with data protection regulations. A governance structure will be established to oversee the regular updating of influence scores, including responsibilities for regional coordinators and project managers to validate scores at least bi-annually.

Biggest worry: The ongoing governance structure may not be consistently adhered to, leading to discrepancies in influence score evaluations.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C7** MAINTAIN: The clarity on maintaining accuracy does not provide a specific process or metrics for how scores will be validated or updated consistently.
- **C7** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C8** MAINTAIN: The time commitment is cited, but as it’s based on an assumption, it may not reflect the actual workload after implementation. [Not counted as answered: no concrete fact, or no evidence in a decided item.]
- **C8** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C9** MAINTAIN: The process for validation and updating scores lacks specifics, which could result in inconsistent applications.
- **C10** MAINTAIN: While a governance structure is mentioned, it does not provide details on how it will function, leading to potential inconsistencies.

New challenges:

**C11** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The proposal does not adequately define what criteria are used to assign the initial influence scores, creating ambiguity.
- Failure scenario: Regional coordinators applying their subjective criteria lead to drastically different influence scores for the same contact across regions, compromising the effectiveness of contact prioritization.
- Resolution test: What specific metrics or criteria will be used to assign the initial influence scores?

Biggest worry: The influence scoring lacks a clear and consistent framework for validating and applying scores, risking significant diplomatic missteps.

**Ledger:** raised 11 · open 3 · resolved 1 · escalated 7 · disagreement 0.91 → **continue**

## Round 5

### Proposer · confidence 70

- **C9** REVISE (missing decision) [changed A4]: This edit introduces a quarterly governance process for regular validation of influence scores, ensuring they remain accurate and relevant.
- **C10** REVISE (missing decision) [changed A3]: This edit clarifies the role of the governance committee, ensuring a structured approach to managing the influence scoring process for consistency and accountability.
- **C11** REVISE (missing decision) [changed A2]: This edit specifies the metrics and criteria for assigning influence scores, providing clarity on the scoring process to avoid inconsistencies in score assignment.

Proposal changes: edited A2, A3, A4
- A2 now reads: The criteria for defining an influence score will encompass factors such as engagement history (e.g., frequency of meetings, communication), seniority (e.g., position within government organization), and recent interactions (e.g., outreach made or received in the past six months), all documented and reviewed by the governance committee.
- A3 now reads: The governance structure will include a committee comprised of selected regional coordinators and project managers responsible for determining scoring criteria, approving changes to influence scores, and conducting quarterly audits to ensure consistent application across the CRM.
- A4 now reads: Influence score data will be retained for a period of 3 years, after which it will be reviewed for accuracy and relevance, and either archived or deleted in compliance with data protection regulations. A governance structure composed of regional coordinators and project managers will oversee the regular updating of influence scores, including responsibilities for reviewing scores that should be validated at least quarterly.

Biggest worry: The effectiveness of the governance structure relies heavily on user compliance and timely updates, which may vary.

### Critic · confidence 30 · CONTINUE

Rulings:
- **C9** ESCALATE: While there is a mention of a governance structure, it does not detail how scores are validated or updated, leading to potential inconsistencies.
- **C10** ESCALATE: The governance structure does not provide clear operational details or accountability measures for the scoring process.
- **C11** MAINTAIN: No valid evidence provided to define the criteria for influence scores as it rests on an assumption.

Biggest worry: The governance structure lacks clear operational details, which may lead to inconsistent application of influence scores.

**Ledger:** raised 11 · open 1 · resolved 1 · escalated 9 · disagreement 0.91 → **continue**

## Round 6

### Proposer · confidence 75

- **C11** REVISE (missing decision) [changed A2]: This edit specifies the criteria to be used for assigning influence scores, addressing the ambiguity in the proposal and providing a structured approach to ensure consistency across regions.

Proposal changes: edited A2
- A2 now reads: The criteria for defining an influence score will encompass the following factors: 1) engagement history, which includes frequency of meetings and other communications with the contact; 2) seniority, determined by the contact's position within the government organization; and 3) recent interactions, specifically outreach made or received in the past six months. These criteria will be documented and reviewed by the governance committee prior to initial score assignment.

Biggest worry: The successful implementation of this feature hinges on user adherence to the defined criteria, which may vary in interpretation.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C11** MAINTAIN: The criteria for defining an influence score are still defined through an assumption rather than being committed to an explicit item in the proposal, leading to ambiguity.
- **C11** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.

Biggest worry: The criteria for influence scores remain ambiguous and untested, risking inconsistent scoring and potential diplomatic breaches.

**Ledger:** raised 11 · open 0 · resolved 1 · escalated 10 · disagreement 0.91 → **converged**

## Final proposal

_This release will enable users to identify and prioritize their most influential contacts by tracking influence metrics associated with each contact, clarifying authority and establishing a governance structure for maintaining influence scores. It introduces clear criteria for influence scoring that will enhance consistency and manageability for users._

**Core commitments**
- V1: Establish a system for categorizing contacts based on a defined 'influence score'.
- V2: Provide users with the ability to filter and sort contacts based on their influence score.

**In scope**
- S1: Create a rating system where each contact can be assigned an 'influence score' ranging from 1 to 10, where 10 indicates the highest level of influence. Access to view influence scores will be limited to authorized users including regional coordinators and project managers only.
- S2: Allow users to view the influence scores of contacts in the contact details section of the CRM.
- S3: Enable filtering of contact lists by influence score for regional coordinators and project managers.
- S4: Provide a report feature that lists contacts sorted by influence score for 10 or more entries.

**Out of scope**
- X1: This release will not include automated updates of the influence scores based on external data or events.
- X2: The influence scoring system will not incorporate any social media metrics.
- X3: This release does not include training or educational materials on how to utilize influence scores.

**Assumptions**
- A1: The authority to assign and modify influence scores is limited to regional coordinators and project managers. Each regional coordinator and project manager is expected to dedicate no more than 2 hours per month to review, assign, and modify influence scores, ensuring that their workload remains manageable.
- A2: The criteria for defining an influence score will encompass the following factors: 1) engagement history, which includes frequency of meetings and other communications with the contact; 2) seniority, determined by the contact's position within the government organization; and 3) recent interactions, specifically outreach made or received in the past six months. These criteria will be documented and reviewed by the governance committee prior to initial score assignment.
- A3: The governance structure will include a committee comprised of selected regional coordinators and project managers responsible for determining scoring criteria, approving changes to influence scores, and conducting quarterly audits to ensure consistent application across the CRM.
- A4: Influence score data will be retained for a period of 3 years, after which it will be reviewed for accuracy and relevance, and either archived or deleted in compliance with data protection regulations. A governance structure composed of regional coordinators and project managers will oversee the regular updating of influence scores, including responsibilities for reviewing scores that should be validated at least quarterly.

**Definitions**
- D1: 'Influence score' means a numerical value between 1 and 10 assigned to each contact, representing their level of influence based on criteria defined by the organization.
- D2: 'Regional coordinators' means users in the CRM who manage relationships and engagements for specific geographic areas.
- D3: 'Project managers' means users in the CRM responsible for overseeing and executing projects involving government contacts.

**Success criteria**
- K1: At least 80% of users report that the influence score feature helps them prioritize contacts effectively, measured through a user feedback survey after 3 months of deployment.

## Orchestrator warnings

- R2: the Proposer's turn still broke these rules after a repair, so illegal edits were dropped and mislabelled moves corrected: C5: there is no S5 to remove.
- R2: Proposer's CONCEDE of C5 had no legal edit; recorded as DEFEND.
- R4: Critic accepted C8 without a concrete fact or evidence in a decided item; recorded as not accepted.
