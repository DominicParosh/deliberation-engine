# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.008.

Challenges: 7 raised · 5 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

This release will implement a feature that enables users to categorize contacts by their influence levels, thereby allowing prioritization in engagements. It will not include automated assessments or changes to privacy policies. Key decisions remain regarding the consistency in user training and the organizational understanding of influence.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to categorize contacts by influence level to prioritize engagements.
- **V2** Provide a visual interface to quickly assess and filter contacts based on their influence.

**In scope**

- **S1** Add a field in the contact profile to rate 'Influence Level' on a scale of 1-5, with 1 being lowest and 5 being highest.  
  A new field for Influence Level will be added, ensuring clarity in how contacts are rated for prioritization.
- **S2** Create a dashboard that displays all contacts sorted by their Influence Level, ensuring that access to this dashboard is restricted to authorized users defined by their role, specifically regional coordinators and project managers.  
  The dashboard will display contacts by Influence Level, with strict access controls to protect sensitive relationships. _(C3)_
- **S3** Allow users to filter contacts based on specific Influence Level ratings while ensuring that access to sensitive information is restricted based on user roles and explicit permissions.  
  Users will be able to filter contacts by Influence Level, with filtering measures ensuring role-based access to sensitive data. _(C5)_
- **S4** Provide access to this feature for users, specifically including regional coordinators and project managers, and designate a primary role (e.g., regional coordinators) responsible for maintaining and updating the 'Influence Level' ratings.  
  Regional coordinators will be designated to maintain the Influence Level ratings, providing clear ownership and responsibility. _(C2)_
- **S5** Implement user training sessions to ensure efficient usage of the new influence tracking feature.
- **S6** Implement a review process for validating 'Influence Level' ratings, where each contact's assigned rating must be reviewed and approved by a designated authority, such as a senior project manager or regional coordinator, on a quarterly basis. This review process aims to mitigate risks related to inflated or biased ratings.  
  A review process for Influence Level ratings will be established, allowing for oversight and correctness in the ratings assigned. _(C7)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not provide automated assessments of influence based on external data sources.
- **X2** This release will not change the existing data privacy or user access policies.
- **X3** This release will not address historical engagement data for analyzing past influence.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The organization has defined criteria for determining the 'Influence Level' of contacts. This assumption is critical for coding and testing the ranking scale. | Kept | never challenged |
| A2 | Users are able to provide subjective ratings without extensive training or guideline documentation. This assumption underpins user adoption of the new feature. | Kept | C4 → escalated |
| A3 | Regional coordinators and project managers have a shared understanding of what constitutes influence in the context of their roles. This assumption directly affects how users implement and utilize the new categorization. | Kept | C6 → escalated |

## Definitions

- **D1** 'Influence Level' means a numeric rating from 1 (lowest influence) to 5 (highest influence) assigned to contacts based on established criteria, which include: role within the government, historical collaboration with our organization, perceived relationship strength, and influence on decision-making processes.  
  The definition of 'Influence Level' provides a standardized numeric rating, mitigating subjectivity and protecting data integrity. _(C1)_
- **D2** 'User Roles' means defined positions within the CRM system that have varying levels of access and capabilities, specifically including regional coordinators and project managers.

## Success criteria

- **K1** Achieve at least a 75% user satisfaction rate with the new influence tracking feature, measured through user feedback surveys within one month of release.
- **K2** Ensure that at least 80% of contacts have their Influence Level rated within the first two months of feature launch.

## Open questions for humans

### C4 · MAJOR · blocks the build

**What specific training or guidelines will the organization provide to ensure consistent and objective ratings of influence levels?**

- Why it matters: This decision is critical to maintain data quality and prevent biased ratings.
- Decision owner: Head of User Training
- Options: Develop comprehensive training materials / Utilize existing guidelines for similar features / No additional training or guidelines
- Proposer's last word (R2, defend, needs human decision): This edit assigns the development of training and guidelines to the organization, as it needs to decide how to ensure consistent ratings from users.
- Critic's last word (R2, escalate): The proposal still relies on unconfirmed organizational decisions on training and guidelines.

### C6 · MINOR · does not block the build

**How will the organization ensure all users have a consistent understanding of what constitutes influence?**

- Why it matters: A consistent definition of influence is vital for accurate and objective ratings.
- Decision owner: Head of Data Protection
- Options: Create a formalized definition of influence / Conduct workshops to align understanding / Assume existing knowledge is sufficient
- Proposer's last word (R2, defend, needs human decision): This revision indicates that the organization is responsible for creating a definition of influence, which is essential for consistency in ratings.
- Critic's last word (R2, escalate): The proposal still lacks a definitive framework for understanding 'influence'.

## Tension report

The primary disagreement revolved around concerns of data quality and user bias in assigning influence ratings. While mechanisms for oversight were established, there remained unresolved questions about the adequacy of user training and shared definitions of influence.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 7 | 1 | 4 | 2 | 0.43 | 80 | 60 | CONTINUE | continue |
| 3 | 7 | 0 | 5 | 2 | 0.21 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring consistent application of the review process by all designated authorities.
- Critic's remaining worry (85/100): Bias in assigning 'Influence Level' ratings could still lead to non-objective assessments despite the review process.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | S1 | R1 | REVISED | 0 | The proposal does not provide clear, objective criteria for determining the 'Influence Level' of contacts, risking subjective bias in ratings. |
| C2 | MAJOR | OWNERSHIP | S1, S4 | R1 | REVISED | 0 | The proposal does not define who will maintain or update the 'Influence Level' ratings, leading to inconsistencies over time. |
| C3 | MAJOR | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | The dashboard displaying contacts by 'Influence Level' may expose sensitive relationships to users who should not access this information. |
| C4 | MAJOR | OWNERSHIP | A2 | R1 | ESCALATED | 0 | The proposal assumes that users can provide subjective ratings without guidance, which raises concerns about data quality and ownership. |
| C5 | MINOR | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | The filtering feature may allow users to inadvertently access sensitive information based on influence ratings. |
| C6 | MINOR | CONFIDENTIALITY | A3 | R1 | ESCALATED | 0 | The proposal relies on a shared understanding of 'influence,' which can vary significantly among users, presenting confidentiality risks. |
| C7 | BLOCKER | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal does not account for the potential risk of users inflating ratings or rating based on bias without oversight, which could lead to significant inaccuracies in 'Influence Level'. |
