# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **converged** after 4 rounds (policy `gated`) · $0.009.

## Summary

This release will enable users to identify and prioritize their most influential contacts in the Government CRM based on specific influence criteria. Users will be able to view a list of contacts sorted by influence score and define influence criteria for each contact. However, a defined process to ensure data quality and accuracy remains unresolved, which requires further decision-making.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can view a list of contacts sorted by influence score.  
  Users can view a list of contacts sorted by influence score to facilitate prioritization of influential contacts.
- **V2** Users can input and update influence criteria for each contact.  
  Users can input and update influence criteria to tailor influence assessments specifically for their context.

**In scope**

- **S1** Regional coordinators and project managers can see a list of contacts with an assigned influence score calculated based on the criteria, while executives can only view influence scores of contacts they are directly engaged with.  
  Regional coordinators and project managers have visibility into influence scores while executive views are limited to their direct engagements, ensuring appropriate access levels. _(C2)_
- **S2** The system allows users to define 'influence' with three criteria: position in government (high, medium, low), project relevance (high, medium, low), and previous engagement level (high, medium, low).  
  Influence is defined by three criteria: government position, project relevance, and previous engagement level, standardizing assessments. _(C1)_
- **S3** The influence score will be calculated using a weighted average of the chosen criteria based on user input, with default weights applied if not specified.  
  The influence score is calculated using specific weightings for each criterion, ensuring consistency in scoring among users. _(C6)_
- **S4** Users will have the ability to update their selected influence criteria for any contact at any time.  
  Users can update influence criteria at any time, allowing for adaptability and relevance of the scoring.
- **S5** S5: Access to influence scores will be secured through role-based access control mechanisms, requiring all users to authenticate via multi-factor authentication, and allowing only authorized personnel to view or share sensitive influence score information.  
  Access to influence scores is secured through role-based access control and multi-factor authentication, enhancing data confidentiality. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated external data sources to assess influence.
- **X2** This release will not provide a detailed analysis report on engagement outcomes based on influence levels.
- **X3** This release will include role-based access controls to limit viewing of influence scores to specifically designated roles, ensuring sensitive information is appropriately handled.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have access to sufficient and up-to-date information for assessing their contacts' influence, which is critical for the scoring; the organization will implement a quarterly review process to verify contact information accuracy. | Kept | C3 → revised |
| A2 | The users have at least basic knowledge of what constitutes influence in their context, which affects how they input and assess criteria. | Kept | never challenged |
| A3 | Users are willing to regularly update and maintain the influence criteria for their contacts in order to keep the scores relevant. | Kept | never challenged |
| A4 | A4: A designated team within the organization, referred to as the 'Data Governance Team', is responsible for maintaining and updating the definitions of influence criteria over time to ensure they remain relevant and accurate. | Kept | C4 → revised |

## Definitions

- **D1** 'Influence score' means a numerical representation calculated using the defined influence criteria that allows users to rank contacts, calculated as follows: Influence Score = (Position Weight * Position Score + Project Relevance Weight * Project Relevance Score + Engagement Level Weight * Engagement Level Score) / Total Weights, with the weightings specified as follows: position in government (40%), project relevance (30%), and previous engagement level (30).  
  An explicit formula for calculating influence scores has been defined, detailing weightings for clarity and consistency in scoring. _(C6)_
- **D2** 'Influence criteria' means the parameters used to determine a contact's influence including position, project relevance, and engagement level.  
  The term 'influence criteria' is clearly defined to specify the elements that determine a contact’s influence.
- **D3** 'High', 'medium', and 'low' refer to qualitative assessments of each criterion, operationally defined as: 'High' indicates a significant influence or connection, 'Medium' indicates some influence or connection, and 'Low' indicates minimal or no influence.  
  Operational definitions for 'high', 'medium', and 'low' influence levels have been provided to standardize assessments. _(C1)_

## Success criteria

- **K1** At least 75% of targeted users can successfully input and update influence criteria within their first month of use, as measured through user feedback and training sessions.  
  Success is defined by user training and feedback, aiming for a target of 75% successful user engagement in the first month of use.

## Open questions for humans

### C7 · MAJOR · blocks the build

**What processes will be implemented to ensure the quality and accuracy of the information used in the influence scoring?**

- Why it matters: It is crucial for maintaining the integrity of contact influence assessments and avoiding misjudgments that can lead to diplomatic issues.
- Decision owner: Leadership Team
- Options: Define specific organizational policies / Create a committee for oversight / Implement an automated data verification process

## Tension report

The main disagreement centered around the process for ensuring the quality and accuracy of contact information used to calculate influence scores. While the Proposer emphasized user responsibility with periodic reviews, the Critic raised concerns about the potential for outdated data leading to significant misjudgments, highlighting a need for clear organizational processes.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 5 | 2 | 3 | 0 | 0.36 | 85 | 60 | CONTINUE | continue |
| 3 | 7 | 2 | 5 | 0 | 0.27 | 80 | 50 | CONTINUE | continue |
| 4 | 7 | 0 | 6 | 1 | 0.13 | 75 | 40 | CONTINUE | converged |

- Proposer's remaining worry (75/100): The lack of a defined quality assurance process for maintaining accurate contact information could lead to reliance on outdated data.
- Critic's remaining worry (40/100): Without a clear process to ensure data quality, outdated information may still lead to misjudgment and sensitive diplomatic issues.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | S3, D1, D2, D3 | R1 | REVISED | 0 | The criteria for determining 'influence score' lacks explicit definitions, particularly the weightings of the criteria and operational definitions for high, medium, and low; these need to be standardized to avoid subjective assessments that could lead to significant misjudgments. |
| C2 | MAJOR | CONFIDENTIALITY | S1, X3 | R1 | REVISED | 0 | The proposal does not address role-based access controls for viewing influence scores, which could lead to sensitive information being accessed by inappropriate personnel. |
| C3 | MAJOR | DATA_QUALITY | A1, S1, S4 | R1 | REVISED | 0 | The proposal assumes users will maintain up-to-date information for assessing influence but does not outline a strategy to ensure data accuracy and mitigate risks of outdated or incorrect contact information being used for scoring. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal lacks clarity on who is responsible for maintaining the definitions of influence criteria and ensuring they remain relevant over time. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal does not specify what measures are in place to protect the sensitive information contained in influence scores during sharing and communication of these scores. |
| C6 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not provide clarity on how the influence score is calculated and what specific weightings are applied to each criterion beyond the initial definitions. |
| C7 | MAJOR | DATA_QUALITY | GAP | R3 | ESCALATED | 0 | The proposal lacks a defined process to ensure the quality and trustworthiness of the information used to assess influence, specifically how outdated or incorrect information will be managed. |
