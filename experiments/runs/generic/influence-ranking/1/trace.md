# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 4 rounds · 10 model calls (1 repairs)

## Round 1

### Proposer · confidence 80

_This release will introduce a feature to categorize government contacts by their level of influence, allowing users to prioritize interactions accordingly. It is aimed at regional coordinators, project managers, and executive-level staff who engage with government counterparts._

**Core commitments**
- V1: Users can view the influence level of each contact in the Government CRM.
- V2: Users are able to sort and filter contacts based on their influence level.

**In scope**
- S1: A new field called 'Influence Level' will be added to each contact record in the Government CRM.
- S2: Influence Level will be categorized into three levels: 'High', 'Medium', and 'Low'.
- S3: Users will be able to filter the contacts list to show only those with 'High' influence.
- S4: Training materials will be developed to guide users on how to utilize the influence categorization feature.
- S5: Users can view the influence status directly on the contact detail pages.

**Out of scope**
- X1: This release will not include automatic determination of influence levels; these will be manually assigned by designated team members.
- X2: This release will not add any predictive analytics or algorithms to determine future influence.
- X3: The feature will not include influence tracking over time; it will focus solely on current influence levels.

**Assumptions**
- A1: It is assumed that designated team members will have the authority to classify influence levels, based on their knowledge of contacts.
- A2: It is assumed that users will have adequate training to understand how to use the new influence categorization feature.
- A3: It is assumed that there are existing procedures for updating contact information, which will include the new influence level field.
- A4: It is assumed that existing security and privacy regulations on sensitive data handling will be adhered to in the feature deployment.

**Definitions**
- D1: 'Influence Level' means a classification assigned to a contact based on their ability to affect decisions or outcomes related to the organization's activities.
- D2: 'High', 'Medium', 'Low' influence means the following: 'High' indicates significant decision-making power or authority, 'Medium' indicates moderate influence without decision-making power, and 'Low' indicates minimal influence on decision-making.

**Success criteria**
- K1: At least 75% of users report that the influence categorization has improved their prioritization of contacts, measured through user feedback surveys.

Biggest worry: The manual classification of influence levels may lead to inconsistencies if not managed properly.

### Critic · confidence 40

Pre-mortem: A year after launch, the influence categorization feature resulted in significant backlash when a sensitive government contact with a potentially low influence score was mistakenly categorized as low by a team member. This led to the neglect of their requests and relationship deterioration, exacerbated by the fact that this contact was privy to confidential information crucial to the organization, causing diplomatic tensions.

Questions the request leaves open:
- What process ensures that influence levels are accurate and reflect true relationships?
- What safeguards are in place to prevent unauthorized users from viewing or assigning influence levels?
- What happens when a designated team member who assigns influence levels leaves or changes roles?
- How is influence level maintained and updated over time, considering the dynamic nature of relationships?
- What specific criteria define 'High', 'Medium', and 'Low' influence, and who is responsible for defining them?
- How will users be alerted about potential changes in a contact's influence status?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1
- Challenge: The influence categorization could lead to decisions being made on outdated or incorrect influence assessments, especially as relationships change over time.
- Failure scenario: A project manager disregards a contact categorized as 'Low' influence when they could have provided critical support for a sensitive project, damaging the project's success and relationships.
- Resolution test: What process is in place to ensure that influence levels are regularly reviewed and updated?

**C2** · MAJOR · DEFINITIONS · targets S2
- Challenge: The terms 'High', 'Medium', and 'Low' for influence are vague without established criteria, potentially leading to inconsistent or subjective assignments.
- Failure scenario: A regional coordinator assigns a 'High' influence level to a contact based on personal bias rather than objective criteria, leading to misplaced prioritization of interactions.
- Resolution test: What specific criteria define 'High', 'Medium', and 'Low' influence, and who is responsible for defining them?

**C3** · MAJOR · OWNERSHIP · targets A3
- Challenge: The assumption that there are existing procedures for updating contact information must include explicit ownership for maintaining the accuracy of the influence level.
- Failure scenario: When a designated team member leaves, there is no clear process or person responsible for updating or maintaining the influenced levels, leading to outdated and potentially harmful data.
- Resolution test: Who is explicitly responsible for maintaining and updating the influence levels in contacts?

**C4** · MINOR · OPERATIONS · targets S4
- Challenge: The effectiveness of training materials is uncertain; how will it ensure all users understand the influence categorization process?
- Failure scenario: Users struggle to utilize the new influence categories effectively due to inadequate training, leading to inconsistent communication with contacts based on misinterpretation of influence levels.
- Resolution test: What measures will be taken to ensure that users are adequately trained to understand and apply influence classifications?

**C5** · MINOR · FEASIBILITY · targets X1
- Challenge: If the influence levels are to be manually assigned, what is the fallback process if designated team members are unavailable?
- Failure scenario: A key contact needs an urgent update to their influence status but the designated team member is on leave, resulting in delays that affect important negotiations.
- Resolution test: What is the procedure if a designated team member responsible for assigning influence levels is unavailable?

**C6** · MAJOR · COMPLIANCE · targets A4
- Challenge: The assumption about adhering to existing security and privacy regulations does not specify which regulations apply to the data being handled, particularly in terms of influence categorization.
- Failure scenario: Sensitive information about contacts is mishandled due to a lack of clarity on privacy regulations, leading to breaches of confidentiality agreements and potential legal repercussions.
- Resolution test: Which specific security and privacy regulations will govern the handling of influence level data?

Biggest worry: Lack of clear definitions and ownership for influence levels raises serious risks for miscommunication and mismanagement of sensitive relationships.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 70

- **C1** DEFEND (needs human decision): The process for regularly reviewing and updating influence levels must be determined by the organization to ensure data accuracy and responsiveness to changing relationships.
- **C2** DEFEND (needs human decision): The establishment of specific criteria for 'High', 'Medium', and 'Low' influence and the appointment of responsible parties must be defined by the organization to avoid subjective bias.
- **C3** DEFEND (needs human decision): Explicit ownership for maintaining and updating the influence levels must be assigned by the organization to prevent outdated data following personnel changes.
- **C4** REVISE (missing decision) [changed S4]: The proposal now commits to implementing assessments in the training materials to ensure effective understanding and application of the influence classifications.
- **C5** DEFEND (needs human decision): The organization must define a fallback process for when designated team members are unavailable to assign or update influence levels.
- **C6** DEFEND (needs human decision): Specific security and privacy regulations impacting the handling of influence level data need to be clarified by the organization to ensure compliance.

Proposal changes: edited S4
- S4 now reads: Training materials will be developed and include assessments to ensure all users demonstrate understanding of the influence categorization process.

Biggest worry: The clarity of ownership and processes for maintaining accurate influence assessments remains uncertain.

### Critic · confidence 20 · CONTINUE

Rulings:
- **C1** ESCALATE: The proposal needs a specific process for regularly updating influence levels, which requires organizational input.
- **C2** ESCALATE: Criteria for 'High', 'Medium', and 'Low' influence assignments must be specified by the organization.
- **C3** ESCALATE: There needs to be clear ownership defined for updating and maintaining influence levels.
- **C4** MAINTAIN: The effectiveness of training materials in ensuring understanding remains unclear.
- **C5** ESCALATE: A clear fallback process needs to be defined for absent team members who assign influence levels.
- **C6** ESCALATE: The applicable regulations regarding data handling are not specified and need human decision.

Biggest worry: The inability to define clear criteria and processes for influence assignment could lead to a breakdown in relationships with sensitive contacts.

**Ledger:** raised 6 · open 1 · resolved 0 · escalated 5 · disagreement 1.00 → **continue**

## Round 3

### Proposer · confidence 80

- **C4** REVISE (missing decision) [changed S4]: The revised training requirement ensures that users must actively demonstrate their understanding of the influence levels, enhancing the effectiveness of the training materials.

Proposal changes: edited S4
- S4 now reads: Training materials will be developed and must include clear guidelines, practical examples, and assessments that require users to demonstrate their understanding and application of the influence categorization process.

Biggest worry: Users may still misinterpret influence levels despite training, leading to inconsistent engagement.

### Critic · confidence 35 · CONTINUE

Rulings:
- **C4** MAINTAIN: While the proposal commits to assessments in the training materials, it remains unclear how effective these measures will be in truly ensuring user understanding and application of influence classifications.
- **C4** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.

New challenges:

**C7** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal lacks clear guidelines on who can assign and alter the 'Influence Level' for contacts, raising risks of unauthorized or inconsistent changes to sensitive contact information.
- Failure scenario: A regional coordinator wrongly assigns a low influence to a sensitive contact without proper authority, leading to diplomatic friction due to the mismanagement of sensitive relationships.
- Resolution test: Who is authorized to categorize and update the influence levels of contacts?

**C8** · BLOCKER · DEFINITIONS · targets GAP
- Challenge: The proposal does not define the criteria or process by which influence levels are assigned, leading to potential inconsistencies and subjective judgments.
- Failure scenario: Two team members categorize a contact differently due to lack of clear definitions, resulting in conflicting engagement strategies and damage to relationships.
- Resolution test: What specific criteria must be used to assign each 'Influence Level'?

Biggest worry: The categorization of influence levels may be inconsistent without proper definitions and controls, risking diplomatic relationships.

**Ledger:** raised 8 · open 2 · resolved 0 · escalated 6 · disagreement 1.00 → **continue**

## Round 4

### Proposer · confidence 80

- **C7** REVISE (missing decision) [changed S6]: This edit defines who is authorized to categorize and update influence levels, addressing the concern of unauthorized or inconsistent changes.
- **C8** REVISE (missing decision) [changed D3]: This edit specifies the process by which influence levels are assigned, ensuring a consistent and objective framework for classification.

Proposal changes: added S6, D3
- S6 now reads: Only designated team members, such as regional coordinators and project managers, will have the authority to assign and alter the 'Influence Level' for contacts.
- D3 now reads: The criteria for assigning 'Influence Level' will be based on the contact's role, previous engagement history, and demonstrated ability to influence decisions related to the organization's activities.

Biggest worry: There may still be ambiguity in how influence levels are maintained and updated over time.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C7** ACCEPT: This clearly defines who can authorize changes in influence levels, addressing the original concern. Fact: Designated team members (regional coordinators and project managers) have authority to assign and alter influence levels. Evidence: "S6: Only designated team members, such as regional coordinators and project managers, will have the authority to assign and alter the 'Influence Level' for contacts."
- **C8** ACCEPT: The specific criteria provided help ensure a consistent and objective framework for influence categorization. Fact: The criteria for assigning influence levels will include role, engagement history, and demonstrated ability to influence decisions. Evidence: "D3: The criteria for assigning 'Influence Level' will be based on the contact's role, previous engagement history, and demonstrated ability to influence decisions related to the organization's activities."

Biggest worry: Inaccurate influence assessments could still arise from subjective evaluations despite clearer criteria.

**Ledger:** raised 8 · open 0 · resolved 2 · escalated 6 · disagreement 0.69 → **consensus**

## Final proposal

_This release will introduce a feature to categorize government contacts by their level of influence, allowing users to prioritize interactions accordingly, while ensuring training and process clarity for maintaining influence assessments. It is aimed at regional coordinators, project managers, and executive-level staff who engage with government counterparts, with clear authorization and criteria established for assigning influence levels._

**Core commitments**
- V1: Users can view the influence level of each contact in the Government CRM.
- V2: Users are able to sort and filter contacts based on their influence level.

**In scope**
- S1: A new field called 'Influence Level' will be added to each contact record in the Government CRM.
- S2: Influence Level will be categorized into three levels: 'High', 'Medium', and 'Low'.
- S3: Users will be able to filter the contacts list to show only those with 'High' influence.
- S4: Training materials will be developed and must include clear guidelines, practical examples, and assessments that require users to demonstrate their understanding and application of the influence categorization process.
- S5: Users can view the influence status directly on the contact detail pages.
- S6: Only designated team members, such as regional coordinators and project managers, will have the authority to assign and alter the 'Influence Level' for contacts.

**Out of scope**
- X1: This release will not include automatic determination of influence levels; these will be manually assigned by designated team members.
- X2: This release will not add any predictive analytics or algorithms to determine future influence.
- X3: The feature will not include influence tracking over time; it will focus solely on current influence levels.

**Assumptions**
- A1: It is assumed that designated team members will have the authority to classify influence levels, based on their knowledge of contacts.
- A2: It is assumed that users will have adequate training to understand how to use the new influence categorization feature.
- A3: It is assumed that there are existing procedures for updating contact information, which will include the new influence level field.
- A4: It is assumed that existing security and privacy regulations on sensitive data handling will be adhered to in the feature deployment.

**Definitions**
- D1: 'Influence Level' means a classification assigned to a contact based on their ability to affect decisions or outcomes related to the organization's activities.
- D2: 'High', 'Medium', 'Low' influence means the following: 'High' indicates significant decision-making power or authority, 'Medium' indicates moderate influence without decision-making power, and 'Low' indicates minimal influence on decision-making.
- D3: The criteria for assigning 'Influence Level' will be based on the contact's role, previous engagement history, and demonstrated ability to influence decisions related to the organization's activities.

**Success criteria**
- K1: At least 75% of users report that the influence categorization has improved their prioritization of contacts, measured through user feedback surveys.
