# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 2 rounds · 7 model calls (2 repairs)

## Round 1

### Proposer · confidence 75

_This release will deliver a contact influence scoring feature to help users prioritize government contacts based on their influence level. It will be available for regional coordinators and project managers to improve engagement efficiency and strategy._

**Core commitments**
- V1: Enable users to assign and view an influence score for each contact.
- V2: Provide a filtering option to display contacts based on their influence score.

**In scope**
- S1: Create an 'influence score' field in the contact records, ranging from 1 (low influence) to 10 (high influence).
- S2: Develop a user interface that allows regional coordinators and project managers to assign an influence score to each contact.
- S3: Implement a sorting feature that allows users to filter and sort contacts by their influence score.
- S4: Provide a way to visualize the distribution of influence scores across contacts in a number of reports available to users.
- S5: Establish role-based access control so only authorized users (regional coordinators and project managers) can assign influence scores.

**Out of scope**
- X1: This release does not include predictive analytics or recommendations for influence scoring.
- X2: This release will not handle the historical data of influence scores, only the current values will be recorded.
- X3: This release does not include integration with external databases or influence measurement tools.

**Assumptions**
- A1: Users will have background knowledge of their contacts and the ability to assess their influence. This assumption is necessary for assigning accurate influence scores.
- A2: There are no legal or regulatory constraints preventing the use of influence scores in the government CRM. This affects the implementation of the feature.
- A3: Users have defined criteria for determining influence, which will guide the scoring process.
- A4: The current architecture of the CRM can accommodate new data fields and filtering features without significant redesign.

**Definitions**
- D1: 'influence score' means a numerical value assigned to a contact representing their perceived ability to impact decisions or actions within the context of government relations.
- D2: 'authorized users' means regional coordinators and project managers who have system access to assign influence scores.

**Success criteria**
- K1: By the end of the quarter, at least 70% of contacts have assigned influence scores by regional coordinators and project managers, measured via system usage logs.

Biggest worry: The subjective nature of influence scoring may lead to inconsistencies in how scores are assigned.

### Critic · confidence 30

Pre-mortem: A year after launch, the influence scoring feature has caused a diplomatic incident when a regional coordinator mistakenly assigned high scores to contacts who were not influential, but rather controversial. The influence scores were shared in a report that was accessed by unauthorized personnel, leading to diplomatic tensions with a member country. This breach of confidentiality not only damaged relationships but also led to an investigation into data handling practices within the CRM.

Questions the request leaves open:
- How will influence scores be defined to ensure consistency and fairness in their assignment?
- What happens to influence scores when a contact leaves a role or when their relationship with the government changes?
- What training or guidelines will users receive to ensure that influence scores are assigned accurately and fairly?
- How will the system handle discrepancies in assigned influence scores, or if users disagree on their validity?
- Is there a mechanism to audit or review influence score assignments for accountability and accuracy?
- What safeguards are in place to prevent unauthorized access to influence scores, and how are these scores handled in reports?

New challenges:

**C1** · BLOCKER · DEFINITIONS · targets D1
- Challenge: The term 'influence score' is ambiguous and lacks a defined and measurable criterion for assignment. Without clear definitions, scores may vary significantly across users, resulting in inaccuracies and potential misuse.
- Failure scenario: A regional coordinator assigns influence scores based on personal biases rather than objective measures, leading to unfair prioritization of contacts in diplomatic interactions.
- Resolution test: What specific criteria or definitions will be used to consistently assign influence scores to contacts?

**C2** · MAJOR · CONFIDENTIALITY · targets S5
- Challenge: The proposal does not outline sufficient safeguards against unauthorized access to influence scores. Given the sensitivity of the contacts involved, improper access could lead to breaches of confidentiality.
- Failure scenario: A project manager inadvertently shares a report with influence scores that includes sensitive contacts, leading to leaks that create political backlash.
- Resolution test: What measures are in place to prevent unauthorized access to influence scores and ensure data confidentiality?

**C3** · MAJOR · OWNERSHIP · targets D2
- Challenge: The assignment of influence scores appears to lack a clear ownership model, raising questions on who is accountable for score accuracy and consistency over time.
- Failure scenario: As regional coordinators and project managers come and go, there is no clear process for maintaining the integrity of influence scores, resulting in outdated or inaccurate assessments being used.
- Resolution test: Who is responsible for regularly reviewing and updating the influence scores, and what process ensures this is done?

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: There is no mention of a process for handling disputes or discrepancies in influence score assignments, which could create inconsistencies in prioritization.
- Failure scenario: Two project managers disagree on the influence score of the same contact, leading to conflicting engagement strategies and public embarrassment for the organization.
- Resolution test: What formal process is in place to resolve disputes over influence score assignments?

**C5** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The proposal does not address how influence scores will be kept up to date, potentially leading to outdated information being used.
- Failure scenario: A contact's influence score is based on outdated information, causing staff to prioritize contacts who are no longer influential, leading to strategic failures.
- Resolution test: How frequently will influence scores be reviewed and updated to ensure they reflect the current state of relationships?

**C6** · MAJOR · OPERATIONS · targets GAP
- Challenge: The proposal lacks a clear outline of training or guidelines for users to assign influence scores accurately, which is vital for effective implementation.
- Failure scenario: Without proper training, users assign influence scores haphazardly, leading to the majority of contacts having incorrect scores that hinder effective engagement.
- Resolution test: What training will be provided to users to ensure they understand how to assign influence scores consistently?

Biggest worry: The influence scoring system lacks clear definitions, safeguards, and accountability, risking both confidentiality and fairness.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed D1]: The revised definition for 'influence score' now includes specific criteria that can be used consistently for assigning scores, which helps mitigate the risks of personal biases in scoring.
- **C2** REVISE (missing decision) [changed S5]: Adding regular audits to the access control will ensure ongoing compliance and protect against unauthorized access to sensitive influence scores.
- **C3** DEFEND (needs human decision): The assignment of responsibility for regularly reviewing and updating influence scores involves organizational policies and roles that must be defined by the organization.
- **C4** DEFEND (needs human decision): Creating a formal dispute resolution process requires organizational input and is subject to existing protocols that the team should establish.
- **C5** DEFEND (needs human decision): The frequency of reviewing and updating influence scores is governed by organizational policies and must be determined by management.
- **C6** DEFEND (needs human decision): User training protocols for assigning influence scores must be developed by the organization to ensure proper implementation and adherence to guidelines.

Proposal changes: edited S5, D1
- S5 now reads: Establish role-based access control so only authorized users (regional coordinators and project managers) can assign influence scores and view influence score reports. Regular audits will be conducted to ensure compliance.
- D1 now reads: 'influence score' means a numerical value assigned to a contact representing their perceived ability to impact decisions or actions within the context of government relations, based on criteria such as historical engagement, position within the government, and perceived effectiveness.

Biggest worry: Ensuring all users consistently understand and apply the scoring criteria effectively.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C1** ACCEPT: This definition clarifies how influence scores should be assigned, addressing the ambiguity. Fact: The definition includes specific criteria for scoring. Evidence: "'influence score' means a numerical value assigned to a contact representing their perceived ability to impact decisions or actions within the context of government relations, based on criteria such as historical engagement, position within the government, and perceived effectiveness."
- **C2** ACCEPT: The proposal includes safeguards for data confidentiality and unauthorized access. Fact: Role-based access control is in place, and regular audits will ensure compliance. Evidence: "Establish role-based access control so only authorized users (regional coordinators and project managers) can assign influence scores and view influence score reports. Regular audits will be conducted to ensure compliance."
- **C3** ESCALATE: The ownership model remains unresolved as it requires internal decision-making.
- **C4** ESCALATE: The absence of a dispute process necessitates organizational involvement.
- **C5** ESCALATE: Frequency of updates is not established and requires human authority.
- **C6** ESCALATE: Training protocols remain undetermined and need organizational input.

Biggest worry: The lack of a defined ownership model and processes for disputes leaves the system vulnerable to inconsistencies and errors.

**Ledger:** raised 6 · open 0 · resolved 2 · escalated 4 · disagreement 0.62 → **converged**

## Final proposal

_This release will deliver a contact influence scoring feature to help users prioritize government contacts based on their influence level, with enhancements to definitions and access control. The feature will be available for regional coordinators and project managers to improve engagement efficiency and strategy._

**Core commitments**
- V1: Enable users to assign and view an influence score for each contact.
- V2: Provide a filtering option to display contacts based on their influence score.

**In scope**
- S1: Create an 'influence score' field in the contact records, ranging from 1 (low influence) to 10 (high influence).
- S2: Develop a user interface that allows regional coordinators and project managers to assign an influence score to each contact.
- S3: Implement a sorting feature that allows users to filter and sort contacts by their influence score.
- S4: Provide a way to visualize the distribution of influence scores across contacts in a number of reports available to users.
- S5: Establish role-based access control so only authorized users (regional coordinators and project managers) can assign influence scores and view influence score reports. Regular audits will be conducted to ensure compliance.

**Out of scope**
- X1: This release does not include predictive analytics or recommendations for influence scoring.
- X2: This release will not handle the historical data of influence scores, only the current values will be recorded.
- X3: This release does not include integration with external databases or influence measurement tools.

**Assumptions**
- A1: Users will have background knowledge of their contacts and the ability to assess their influence. This assumption is necessary for assigning accurate influence scores.
- A2: There are no legal or regulatory constraints preventing the use of influence scores in the government CRM. This affects the implementation of the feature.
- A3: Users have defined criteria for determining influence, which will guide the scoring process.
- A4: The current architecture of the CRM can accommodate new data fields and filtering features without significant redesign.

**Definitions**
- D1: 'influence score' means a numerical value assigned to a contact representing their perceived ability to impact decisions or actions within the context of government relations, based on criteria such as historical engagement, position within the government, and perceived effectiveness.
- D2: 'authorized users' means regional coordinators and project managers who have system access to assign influence scores.

**Success criteria**
- K1: By the end of the quarter, at least 70% of contacts have assigned influence scores by regional coordinators and project managers, measured via system usage logs.
