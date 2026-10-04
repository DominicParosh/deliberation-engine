# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 3 rounds · 9 model calls (3 repairs)

## Round 1

### Proposer · confidence 70

_This release will provide a feature to identify and track the influence level of contacts within the Government CRM system, enabling users to prioritize engagement. It will be designed for regional coordinators and project managers involved in government relationship management._

**Core commitments**
- V1: Enable users to categorize contacts by influence level to prioritize engagements.
- V2: Provide a visual interface to quickly assess and filter contacts based on their influence.

**In scope**
- S1: Add a field in the contact profile to rate 'Influence Level' on a scale of 1-5, with 1 being lowest and 5 being highest.
- S2: Create a dashboard that displays all contacts sorted by their Influence Level.
- S3: Allow users to filter contacts based on specific Influence Level ratings.
- S4: Provide access to this feature for users with roles including regional coordinators and project managers.
- S5: Implement user training sessions to ensure efficient usage of the new influence tracking feature.

**Out of scope**
- X1: This release will not provide automated assessments of influence based on external data sources.
- X2: This release will not change the existing data privacy or user access policies.
- X3: This release will not address historical engagement data for analyzing past influence.

**Assumptions**
- A1: The organization has defined criteria for determining the 'Influence Level' of contacts. This assumption is critical for coding and testing the ranking scale.
- A2: Users are able to provide subjective ratings without extensive training or guideline documentation. This assumption underpins user adoption of the new feature.
- A3: Regional coordinators and project managers have a shared understanding of what constitutes influence in the context of their roles. This assumption directly affects how users implement and utilize the new categorization.

**Definitions**
- D1: 'Influence Level' means a numeric rating from 1 (lowest influence) to 5 (highest influence) assigned to contacts based on established criteria.
- D2: 'User Roles' means defined positions within the CRM system that have varying levels of access and capabilities, specifically including regional coordinators and project managers.

**Success criteria**
- K1: Achieve at least a 75% user satisfaction rate with the new influence tracking feature, measured through user feedback surveys within one month of release.
- K2: Ensure that at least 80% of contacts have their Influence Level rated within the first two months of feature launch.

Biggest worry: The subjective nature of influence ratings may lead to inconsistencies in contact categorization.

### Critic · confidence 40

Pre-mortem: One year after launch, a regional coordinator mistakenly assigned a high 'Influence Level' rating to a contact based on a personal bias rather than objective criteria. As a result, this contact received priority access to sensitive government meetings and information, leading to a leak that severely damaged the organization's relationships with other countries, prompting a diplomatic incident.

Questions the request leaves open:
- What objective criteria determine the 'Influence Level' of contacts?
- How will the influence ratings be managed to prevent bias or misuse by users?
- What will happen if a user trained to rate 'Influence Level' leaves the organization?
- Who will update or maintain the influence ratings over time?
- How will conflicts be resolved if different users rate the same contact differently?
- What specific safeguards are in place to protect sensitive data exposed through this influence ranking system?

New challenges:

**C1** · BLOCKER · DEFINITIONS · targets S1
- Challenge: The proposal does not provide clear, objective criteria for determining the 'Influence Level' of contacts, risking subjective bias in ratings.
- Failure scenario: A project manager assigns inflated ratings based on personal relationships rather than a standard, causing the organization to misallocate resources and privileges.
- Resolution test: What are the specific, objective criteria used to measure and categorize a contact's 'Influence Level'?

**C2** · MAJOR · OWNERSHIP · targets S1, S4
- Challenge: The proposal does not define who will maintain or update the 'Influence Level' ratings, leading to inconsistencies over time.
- Failure scenario: After a regional coordinator leaves, their assigned influence levels are never reviewed or updated, resulting in outdated contact prioritization.
- Resolution test: Who is responsible for maintaining and updating the 'Influence Level' ratings over time?

**C3** · MAJOR · CONFIDENTIALITY · targets S2
- Challenge: The dashboard displaying contacts by 'Influence Level' may expose sensitive relationships to users who should not access this information.
- Failure scenario: A project manager accesses the dashboard and learns about relationships that are confidential, leading to inappropriate engagement actions.
- Resolution test: What access controls are in place to ensure that only authorized users can view the 'Influence Level' dashboard?

**C4** · MAJOR · OWNERSHIP · targets A2
- Challenge: The proposal assumes that users can provide subjective ratings without guidance, which raises concerns about data quality and ownership.
- Failure scenario: Users rate contacts based on personal opinions rather than consistent standards, leading to unreliable influence ratings and poor decision-making.
- Resolution test: What specific training or guidelines will be provided to ensure users can accurately assess contact influence?

**C5** · MINOR · CONFIDENTIALITY · targets S3
- Challenge: The filtering feature may allow users to inadvertently access sensitive information based on influence ratings.
- Failure scenario: A user filters and accesses details of a contact marked as highly influential and acts on that information without clearance.
- Resolution test: What measures are in place to prevent users from accessing or acting on sensitive information related to high-influence contacts?

**C6** · MINOR · CONFIDENTIALITY · targets A3
- Challenge: The proposal relies on a shared understanding of 'influence,' which can vary significantly among users, presenting confidentiality risks.
- Failure scenario: Confusion among users leads to inconsistent ratings, potentially exposing confidential engagements to unintended audiences.
- Resolution test: How will the organization ensure that all users have a consistent understanding of what constitutes influence?

Biggest worry: The potential for subjective bias in influence ratings could lead to significant risks in engagement and data exposure.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed D1]: The new wording provides clear, objective criteria for assessing 'Influence Level', thus reducing subjective biases in ratings.
- **C2** REVISE (missing decision) [changed S4]: The revision specifies that regional coordinators are responsible for maintaining the 'Influence Level' ratings, which addresses concerns of inconsistencies.
- **C3** REVISE (missing decision) [changed S2]: The new wording clarifies that access to the dashboard will be controlled, reducing the risk of unauthorized exposure to sensitive relationships.
- **C4** DEFEND (needs human decision): This edit assigns the development of training and guidelines to the organization, as it needs to decide how to ensure consistent ratings from users.
- **C5** REVISE (missing decision) [changed S3]: The edit specifies that filtering will be role-based, which addresses the concern around unauthorized access to sensitive information.
- **C6** DEFEND (needs human decision): This revision indicates that the organization is responsible for creating a definition of influence, which is essential for consistency in ratings.

Proposal changes: edited S2, S3, S4, D1
- S2 now reads: Create a dashboard that displays all contacts sorted by their Influence Level, ensuring that access to this dashboard is restricted to authorized users defined by their role, specifically regional coordinators and project managers.
- S3 now reads: Allow users to filter contacts based on specific Influence Level ratings while ensuring that access to sensitive information is restricted based on user roles and explicit permissions.
- S4 now reads: Provide access to this feature for users, specifically including regional coordinators and project managers, and designate a primary role (e.g., regional coordinators) responsible for maintaining and updating the 'Influence Level' ratings.
- D1 now reads: 'Influence Level' means a numeric rating from 1 (lowest influence) to 5 (highest influence) assigned to contacts based on established criteria, which include: role within the government, historical collaboration with our organization, perceived relationship strength, and influence on decision-making processes.

Biggest worry: How effectively the organization can implement the required training and guidance for users.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: The proposal now defines clear, objective criteria for determining 'Influence Level', addressing the concern. Fact: Defined criteria for 'Influence Level' based on role, collaboration, relationship strength, and influence. Evidence: "D1: 'Influence Level' means a numeric rating from 1 (lowest influence) to 5 (highest influence) assigned to contacts based on established criteria, which include: role within the government, historical collaboration with our organization, perceived relationship strength, and influence on decision-making processes."
- **C2** ACCEPT: The proposal now specifies who is responsible for updating 'Influence Level' ratings. Fact: Regional coordinators are responsible for maintaining the 'Influence Level' ratings. Evidence: "S4: Provide access to this feature for users, specifically including regional coordinators and project managers, and designate a primary role (e.g., regional coordinators) responsible for maintaining and updating the 'Influence Level' ratings."
- **C3** ACCEPT: Access controls are clarified, reducing the risk of unauthorized exposure. Fact: Access to the dashboard is restricted to regional coordinators and project managers. Evidence: "S2: Create a dashboard that displays all contacts sorted by their Influence Level, ensuring that access to this dashboard is restricted to authorized users defined by their role, specifically regional coordinators and project managers."
- **C4** ESCALATE: The proposal still relies on unconfirmed organizational decisions on training and guidelines.
- **C5** ACCEPT: Filtering measures are defined, reducing risk of unauthorized access to sensitive data. Fact: Filtering will be role-based, ensuring access is controlled. Evidence: "S3: Allow users to filter contacts based on specific Influence Level ratings while ensuring that access to sensitive information is restricted based on user roles and explicit permissions."
- **C6** ESCALATE: The proposal still lacks a definitive framework for understanding 'influence'.

New challenges:

**C7** · BLOCKER · DATA_QUALITY · targets GAP
- Challenge: The proposal does not account for the potential risk of users inflating ratings or rating based on bias without oversight, which could lead to significant inaccuracies in 'Influence Level'.
- Failure scenario: A project manager, possibly seeking to favor certain contacts, inflates their 'Influence Level', resulting in critical misallocation of resources and subsequent diplomatic fallout.
- Resolution test: What validation or review process is established for influence ratings to ensure their accuracy and reliability?

Biggest worry: The reliance on subjective ratings without a defined review process risks data quality and could lead to significant operational failures.

**Ledger:** raised 7 · open 1 · resolved 4 · escalated 2 · disagreement 0.43 → **continue**

## Round 3

### Proposer · confidence 85

- **C7** REVISE (missing decision) [changed S6]: The edits establish a clear review process to validate the 'Influence Level' ratings, ensuring accuracy and reliability. This decision directly addresses the challenge by requiring oversight to prevent biased or inflated ratings.

Proposal changes: added S6
- S6 now reads: Implement a review process for validating 'Influence Level' ratings, where each contact's assigned rating must be reviewed and approved by a designated authority, such as a senior project manager or regional coordinator, on a quarterly basis. This review process aims to mitigate risks related to inflated or biased ratings.

Biggest worry: Ensuring consistent application of the review process by all designated authorities.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C7** ACCEPT: The established review process effectively addresses the concerns about inflated ratings. Fact: A review process will validate 'Influence Level' ratings quarterly. Evidence: "Implement a review process for validating 'Influence Level' ratings, where each contact's assigned rating must be reviewed and approved by a designated authority, such as a senior project manager or regional coordinator, on a quarterly basis."

Biggest worry: Bias in assigning 'Influence Level' ratings could still lead to non-objective assessments despite the review process.

**Ledger:** raised 7 · open 0 · resolved 5 · escalated 2 · disagreement 0.21 → **consensus**

## Final proposal

_This release will provide a feature to identify and track the influence level of contacts within the Government CRM system, enabling users to prioritize engagement. It is designed for regional coordinators and project managers, with clear criteria, defined responsibilities, and access controls in place, along with a validation process for influence ratings._

**Core commitments**
- V1: Enable users to categorize contacts by influence level to prioritize engagements.
- V2: Provide a visual interface to quickly assess and filter contacts based on their influence.

**In scope**
- S1: Add a field in the contact profile to rate 'Influence Level' on a scale of 1-5, with 1 being lowest and 5 being highest.
- S2: Create a dashboard that displays all contacts sorted by their Influence Level, ensuring that access to this dashboard is restricted to authorized users defined by their role, specifically regional coordinators and project managers.
- S3: Allow users to filter contacts based on specific Influence Level ratings while ensuring that access to sensitive information is restricted based on user roles and explicit permissions.
- S4: Provide access to this feature for users, specifically including regional coordinators and project managers, and designate a primary role (e.g., regional coordinators) responsible for maintaining and updating the 'Influence Level' ratings.
- S5: Implement user training sessions to ensure efficient usage of the new influence tracking feature.
- S6: Implement a review process for validating 'Influence Level' ratings, where each contact's assigned rating must be reviewed and approved by a designated authority, such as a senior project manager or regional coordinator, on a quarterly basis. This review process aims to mitigate risks related to inflated or biased ratings.

**Out of scope**
- X1: This release will not provide automated assessments of influence based on external data sources.
- X2: This release will not change the existing data privacy or user access policies.
- X3: This release will not address historical engagement data for analyzing past influence.

**Assumptions**
- A1: The organization has defined criteria for determining the 'Influence Level' of contacts. This assumption is critical for coding and testing the ranking scale.
- A2: Users are able to provide subjective ratings without extensive training or guideline documentation. This assumption underpins user adoption of the new feature.
- A3: Regional coordinators and project managers have a shared understanding of what constitutes influence in the context of their roles. This assumption directly affects how users implement and utilize the new categorization.

**Definitions**
- D1: 'Influence Level' means a numeric rating from 1 (lowest influence) to 5 (highest influence) assigned to contacts based on established criteria, which include: role within the government, historical collaboration with our organization, perceived relationship strength, and influence on decision-making processes.
- D2: 'User Roles' means defined positions within the CRM system that have varying levels of access and capabilities, specifically including regional coordinators and project managers.

**Success criteria**
- K1: Achieve at least a 75% user satisfaction rate with the new influence tracking feature, measured through user feedback surveys within one month of release.
- K2: Ensure that at least 80% of contacts have their Influence Level rated within the first two months of feature launch.

## Orchestrator warnings

- R2: the Proposer's turn still broke these rules after a repair (illegal edits dropped, mislabelled moves corrected, the rest recorded as given): C4: grounds NEEDS_HUMAN_DECISION mean DEFEND, which leaves the proposal as it is, so `edits` must be empty. If an item has to change, the grounds are MISSING_DECISION or SHOULD_NOT_BUILD. C6: grounds NEEDS_HUMAN_DECISION mean DEFEND, which leaves the proposal as it is, so `edits` must be empty. If an item has to change, the grounds are MISSING_DECISION or SHOULD_NOT_BUILD.
