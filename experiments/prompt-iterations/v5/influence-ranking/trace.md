# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 4 rounds · 11 model calls (2 repairs)

## Round 1

### Proposer · confidence 70

_This release will enable users to identify and prioritize their most influential contacts in the Government CRM based on specific influence criteria. It will primarily benefit regional coordinators and project managers who need to focus their engagement efforts effectively._

**Core commitments**
- V1: Users can view a list of contacts sorted by influence score.
- V2: Users can input and update influence criteria for each contact.

**In scope**
- S1: Regional coordinators and project managers can see a list of contacts with an assigned influence score calculated based on the criteria.
- S2: The system allows users to define 'influence' with three criteria: position in government (high, medium, low), project relevance (high, medium, low), and previous engagement level (high, medium, low).
- S3: The influence score will be calculated using a weighted average of the chosen criteria based on user input, with default weights applied if not specified.
- S4: Users will have the ability to update their selected influence criteria for any contact at any time.

**Out of scope**
- X1: This release will not include automated external data sources to assess influence.
- X2: This release will not provide a detailed analysis report on engagement outcomes based on influence levels.
- X3: This release will not enable role-based access controls for viewing the influence scores.

**Assumptions**
- A1: Users have access to sufficient and up-to-date information for assessing their contacts' influence, which is critical for the scoring.
- A2: The users have at least basic knowledge of what constitutes influence in their context, which affects how they input and assess criteria.
- A3: Users are willing to regularly update and maintain the influence criteria for their contacts in order to keep the scores relevant.

**Definitions**
- D1: 'Influence score' means a numerical representation calculated using the defined influence criteria that allows users to rank contacts.
- D2: 'Influence criteria' means the parameters used to determine a contact's influence including position, project relevance, and engagement level.
- D3: 'High', 'medium', and 'low' refer to qualitative assessments of each criterion, which can be operationally defined by the users.

**Success criteria**
- K1: At least 75% of targeted users can successfully input and update influence criteria within their first month of use, as measured through user feedback and training sessions.

Biggest worry: Ensuring that the influence criteria are accurately defined and effectively utilized by users could be challenging.

### Critic · confidence 40

Pre-mortem: A year after launch, the influence scoring feature caused significant issues when an incorrect influence score led to a regional coordinator prioritizing a contact with low relevance to ongoing diplomatic projects. This resulted in wasted engagement resources, and the wrong contact was contacted, exposing sensitive project information. The failure to define and regulate the influence criteria allowed subjective assessments to misguide key decisions, damaging relationships with government counterparts and leading to a public relations incident.

Questions the request leaves open:
- Which roles can view the influence scores and associated criteria for a contact?
- How is the influence score calculated and what specific weightings are applied to each criterion?
- What happens if a user evaluates a contact after a significant role change (e.g., a minister changes positions)?
- What processes are in place to ensure the quality and trustworthiness of the information used to assess influence?
- Who is responsible for maintaining the definitions of 'high', 'medium', and 'low' for each criterion?
- What are the data security measures to protect potentially sensitive information when sharing influence scores?

New challenges:

**C1** · BLOCKER · DEFINITIONS · targets S3, D1, D2, D3
- Challenge: The criteria for determining 'influence score' lacks explicit definitions, particularly the weightings of the criteria and operational definitions for high, medium, and low; these need to be standardized to avoid subjective assessments that could lead to significant misjudgments.
- Failure scenario: A project manager inputs influence scores based on gut feeling rather than standardized parameters, inadvertently causing a contact with a low influence to gain a high score and receive prioritized engagement, wasting resources.
- Resolution test: What are the defined weightings for each influence criterion and how are 'high', 'medium', and 'low' operationally defined?

**C2** · MAJOR · CONFIDENTIALITY · targets S1, X3
- Challenge: The proposal does not address role-based access controls for viewing influence scores, which could lead to sensitive information being accessed by inappropriate personnel.
- Failure scenario: An executive accidentally views influence scores and detailed criteria for contacts unrelated to their projects, leading to sensitive diplomatic relations being compromised.
- Resolution test: What roles are explicitly granted access to view influence scores and how are inappropriate accesses prevented?

**C3** · MAJOR · DATA_QUALITY · targets A1, S1, S4
- Challenge: The proposal assumes users will maintain up-to-date information for assessing influence but does not outline a strategy to ensure data accuracy and mitigate risks of outdated or incorrect contact information being used for scoring.
- Failure scenario: A regional coordinator uses stale information about a key contact, leading to an inaccurate influence score and prioritizing engagement with a contact who has no current relevance, resulting in public embarrassment and wasted efforts.
- Resolution test: What process is established to verify that contact information is up-to-date and reliable for influence scoring?

Biggest worry: Undefined criteria and lack of access controls increase the risk of misjudgments and security breaches.

**Ledger:** raised 3 · open 3 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed D1, D3]: These edits provide explicit weightings for each influence criterion to standardize assessments and operational definitions for influence levels to ensure clarity and consistency in scoring.
- **C2** REVISE (missing decision) [changed S1, X3]: The revisions clarify access controls, ensuring that only designated roles can view influence scores, thereby addressing confidentiality concerns.
- **C3** REVISE (missing decision) [changed A1]: This edit establishes a strategy for data accuracy by introducing a quarterly review process, helping to mitigate risks associated with outdated contact information.

Proposal changes: edited S1, X3, A1, D1, D3
- S1 now reads: Regional coordinators and project managers can see a list of contacts with an assigned influence score calculated based on the criteria, while executives can only view influence scores of contacts they are directly engaged with.
- X3 now reads: This release will include role-based access controls to limit viewing of influence scores to specifically designated roles, ensuring sensitive information is appropriately handled.
- A1 now reads: Users have access to sufficient and up-to-date information for assessing their contacts' influence, which is critical for the scoring; the organization will implement a quarterly review process to verify contact information accuracy.
- D1 now reads: 'Influence score' means a numerical representation calculated using the defined influence criteria that allows users to rank contacts, with the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30%).
- D3 now reads: 'High', 'medium', and 'low' refer to qualitative assessments of each criterion, operationally defined as: 'High' indicates a significant influence or connection, 'Medium' indicates some influence or connection, and 'Low' indicates minimal or no influence.

Biggest worry: The effectiveness of the implementation of role-based access controls and their adherence in practice.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT:  Evidence: "the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30%)"
- **C2** ACCEPT:  Evidence: "This release will include role-based access controls to limit viewing of influence scores to specifically designated roles, ensuring sensitive information is appropriately handled."
- **C3** ACCEPT:  Evidence: "the organization will implement a quarterly review process to verify contact information accuracy."

New challenges:

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal lacks clarity on who is responsible for maintaining the definitions of influence criteria and ensuring they remain relevant over time.
- Failure scenario: If a user updates an influence criterion based on outdated definitions, it could lead to inconsistent scoring and prioritization, resulting in resource misallocation and potential diplomatic incidents.
- Resolution test: Who is responsible for maintaining and updating the definitions of 'high', 'medium', and 'low' for each criterion?

**C5** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not specify what measures are in place to protect the sensitive information contained in influence scores during sharing and communication of these scores.
- Failure scenario: Sensitive information related to a contact's influence score is unintentionally leaked to contacts unrelated to the project, damaging trust and diplomatic relations.
- Resolution test: What security measures are implemented to protect the influence scores and related information during sharing?

Biggest worry: Lack of clarity on who is responsible for maintaining influence criteria poses a significant risk for data integrity and could lead to misleading contact prioritization.

**Ledger:** raised 5 · open 2 · resolved 3 · escalated 0 · disagreement 0.36 → **continue**

## Round 3

### Proposer · confidence 80

- **C4** REVISE (missing decision) [changed A4]: This establishes a clear ownership for maintaining the influence criteria, ensuring that updates are systematic and reliable.
- **C5** REVISE (missing decision) [changed S5]: This detail clarifies the approach to protecting sensitive information relating to influence scores while addressing confidentiality concerns.

Proposal changes: added S5, A4
- S5 now reads: S5: Access to influence scores will be secured through role-based access control mechanisms, requiring all users to authenticate via multi-factor authentication, and allowing only authorized personnel to view or share sensitive influence score information.
- A4 now reads: A4: A designated team within the organization, referred to as the 'Data Governance Team', is responsible for maintaining and updating the definitions of influence criteria over time to ensure they remain relevant and accurate.

Biggest worry: The effectiveness of the Data Governance Team in maintaining defined criteria and their relevance over time.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C4** ACCEPT:  Evidence: "A designated team within the organization, referred to as the 'Data Governance Team', is responsible for maintaining and updating the definitions of influence criteria over time to ensure they remain relevant and accurate."
- **C5** ACCEPT:  Evidence: "Access to influence scores will be secured through role-based access control mechanisms, requiring all users to authenticate via multi-factor authentication, and allowing only authorized personnel to view or share sensitive influence score information."

New challenges:

**C6** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The proposal does not provide clarity on how the influence score is calculated and what specific weightings are applied to each criterion beyond the initial definitions.
- Failure scenario: If the scoring method and weightings are not clearly defined, users may apply different interpretations leading to inconsistent scoring, resulting in prioritization errors and potentially diplomatic tensions.
- Resolution test: What is the exact calculation method for the influence score and the specific weightings applied to each of the defined criteria?

**C7** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The proposal lacks a defined process to ensure the quality and trustworthiness of the information used to assess influence, specifically how outdated or incorrect information will be managed.
- Failure scenario: If users evaluate contacts based on inaccurate or outdated information, it may lead to the prioritization of the wrong contacts, resulting in diplomatic missteps and resource misallocation.
- Resolution test: What processes will be implemented to ensure the quality and accuracy of the information used in the influence scoring?

Biggest worry: The lack of clarity on the calculation of influence scores may lead to subjective assessments and inconsistent prioritization.

**Ledger:** raised 7 · open 2 · resolved 5 · escalated 0 · disagreement 0.27 → **continue**

## Round 4

### Proposer · confidence 75

- **C6** REVISE (missing decision) [changed D1]: The edit specifies the formula for calculating the influence score, along with the weighting of each criterion. This adds clarity to how the score will be determined and ensures consistency among users.
- **C7** DEFEND (needs human decision): The process for ensuring information quality and accuracy pertains to existing organizational policies and practices. This must be defined by the organization’s leadership or relevant teams, as they have the authority to implement any necessary procedures.

Proposal changes: edited D1
- D1 now reads: 'Influence score' means a numerical representation calculated using the defined influence criteria that allows users to rank contacts, calculated as follows: Influence Score = (Position Weight * Position Score + Project Relevance Weight * Project Relevance Score + Engagement Level Weight * Engagement Level Score) / Total Weights, with the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30).

Biggest worry: The lack of a defined quality assurance process for maintaining accurate contact information could lead to reliance on outdated data.

### Critic · confidence 40 · CONTINUE

Rulings:
- **C6** ACCEPT:  Evidence: "Influence Score = (Position Weight * Position Score + Project Relevance Weight * Project Relevance Score + Engagement Level Weight * Engagement Level Score) / Total Weights, with the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30)."
- **C7** ESCALATE: The proposal does not specify which organizational policies or leadership decisions will define the processes to ensure data quality and accuracy in influence scoring.

Biggest worry: Without a clear process to ensure data quality, outdated information may still lead to misjudgment and sensitive diplomatic issues.

**Ledger:** raised 7 · open 0 · resolved 6 · escalated 1 · disagreement 0.13 → **converged**

## Final proposal

_This release will enable users to identify and prioritize their most influential contacts in the Government CRM based on specific influence criteria, ensuring an ownership structure for maintaining influence definitions and implementing security measures for sensitive data. It will benefit regional coordinators and project managers primarily, with improved clarity on influence score calculations and the need for organizational policy on data accuracy._

**Core commitments**
- V1: Users can view a list of contacts sorted by influence score.
- V2: Users can input and update influence criteria for each contact.

**In scope**
- S1: Regional coordinators and project managers can see a list of contacts with an assigned influence score calculated based on the criteria, while executives can only view influence scores of contacts they are directly engaged with.
- S2: The system allows users to define 'influence' with three criteria: position in government (high, medium, low), project relevance (high, medium, low), and previous engagement level (high, medium, low).
- S3: The influence score will be calculated using a weighted average of the chosen criteria based on user input, with default weights applied if not specified.
- S4: Users will have the ability to update their selected influence criteria for any contact at any time.
- S5: S5: Access to influence scores will be secured through role-based access control mechanisms, requiring all users to authenticate via multi-factor authentication, and allowing only authorized personnel to view or share sensitive influence score information.

**Out of scope**
- X1: This release will not include automated external data sources to assess influence.
- X2: This release will not provide a detailed analysis report on engagement outcomes based on influence levels.
- X3: This release will include role-based access controls to limit viewing of influence scores to specifically designated roles, ensuring sensitive information is appropriately handled.

**Assumptions**
- A1: Users have access to sufficient and up-to-date information for assessing their contacts' influence, which is critical for the scoring; the organization will implement a quarterly review process to verify contact information accuracy.
- A2: The users have at least basic knowledge of what constitutes influence in their context, which affects how they input and assess criteria.
- A3: Users are willing to regularly update and maintain the influence criteria for their contacts in order to keep the scores relevant.
- A4: A4: A designated team within the organization, referred to as the 'Data Governance Team', is responsible for maintaining and updating the definitions of influence criteria over time to ensure they remain relevant and accurate.

**Definitions**
- D1: 'Influence score' means a numerical representation calculated using the defined influence criteria that allows users to rank contacts, calculated as follows: Influence Score = (Position Weight * Position Score + Project Relevance Weight * Project Relevance Score + Engagement Level Weight * Engagement Level Score) / Total Weights, with the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30).
- D2: 'Influence criteria' means the parameters used to determine a contact's influence including position, project relevance, and engagement level.
- D3: 'High', 'medium', and 'low' refer to qualitative assessments of each criterion, operationally defined as: 'High' indicates a significant influence or connection, 'Medium' indicates some influence or connection, and 'Low' indicates minimal or no influence.

**Success criteria**
- K1: At least 75% of targeted users can successfully input and update influence criteria within their first month of use, as measured through user feedback and training sessions.
