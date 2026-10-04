# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.016.

## Summary

This feature release will introduce an 'Influence Rating' tool that categorizes government contacts by influence level, aiming to assist regional coordinators and project managers in prioritizing their outreach efforts. However, it will not include features for user editing or commenting on influence ratings, nor will it directly track justification for ratings. Clarity on responsibilities for maintaining data accuracy and ownership of engagement data still needs to be established by organizational policy.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to view an influence rating for each government contact.  
  Users will be enabled to view an influence rating for each government contact, as it meets the need for prioritization in outreach efforts.
- **V2** Provide a way to prioritize outreach based on influence rating.  
  A method for prioritizing outreach based on influence rating will be provided to enhance efficiency in engagements with government contacts.

**In scope**

- **S1** Create an 'Influence Rating' field that categorizes contacts as 'High', 'Medium', or 'Low' based on predefined criteria that include; seniority level (not less than department head or equivalent for 'High'), their role in decision-making processes related to our projects, and documented engagement history (at least three engagements for 'High', two for 'Medium', and one for 'Low'). Additionally, each engagement record must be verified by a regional coordinator for accuracy before categorization, with quarterly reviews of engagement data conducted by a designated manager to ensure ongoing reliability and address discrepancies.  
  An 'Influence Rating' field will categorize contacts based on clear criteria, ensuring that confidentiality is respected and engagement data is accurate. _(C1, C3, C4, C5, C9, C10)_
- **S2** Implement a dashboard view for regional coordinators to see a list of contacts sorted by influence rating.  
  Implementation of a dashboard view ensures that regional coordinators can easily access and utilize the influence ratings for their outreach strategies.
- **S3** Allow users to qualitatively adjust the influence ratings based on additional factors, while requiring a justification for each adjustment documented in a secure manner to protect sensitive opinions and ensure transparency.  
  Users will have the ability to qualitatively adjust influence ratings with strict documentation requirements for justifications, safeguarding sensitive opinions. _(C3)_
- **S4** Ensure the influence rating mechanism is reviewed by the data protection officer to comply with sensitivity standards.  
  A review by the data protection officer is mandated to maintain compliance with confidentiality standards.
- **S5** Provide training materials for users on how to interpret and use the influence ratings effectively.  
  Training materials will support users in understanding and utilizing the new influence ratings effectively, ensuring smooth adoption.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include a feature for users to edit or comment on the influence ratings.  
  Editing or commenting features on influence ratings were excluded to prevent conflicts and maintain data integrity.
- **X2** This release will not directly track or analyze the reasons behind each influence rating.  
  The capability to track or analyze reasons behind each influence rating was not included as it could complicate the safeguarding of sensitive information.
- **X3** This release will not provide automated influence ratings based on external data sources.  
  Automatically generated influence ratings based on external data were deemed out of scope to maintain accuracy and avoid potential data quality issues.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The influence of contacts can be reliably categorized into 'High', 'Medium', or 'Low', which allows for effective prioritization. | Kept | never challenged |
| A2 | Users require a clear method to understand and utilize influence ratings for effective engagement. | Kept | never challenged |
| A3 | Regional coordinators and project managers have the ability to consistently input data related to engagement that influences ratings. | Kept | C2 → escalated; C7 → escalated |
| A4 | Data protection regulations allow the use of influence ratings without overriding confidentiality concerns. | Kept | never challenged |

## Definitions

- **D1** 'Influence Rating' means a categorized assessment of a contact's potential impact on decisions, defined as follows: 'High' for contacts influencing major policy decisions (requires documented evidence of participation in at least two major initiatives), 'Medium' for contacts with significant involvement in relevant projects (must have contributed to at least one project decision), and 'Low' for contacts with limited or no decision-making authority (historical engagement record must be noted).  
  The definition of 'Influence Rating' has been revised to incorporate measurable criteria, addressing past subjective interpretations and ensuring standardization. _(C4, C9)_
- **D2** 'Predefined criteria' means set standards based on the contact's role within governmental structures, their historical engagement frequency in relevant projects, and their access to critical information regarding policy developments.  
  The term 'predefined criteria' was detailed to eliminate ambiguity, ensuring uniform understanding and application among users. _(C5)_

## Success criteria

- **K1** Achieve an influence rating definition acceptance by at least 75% of users in the first month of rollout, measured through user feedback surveys.  
  Achieving a 75% acceptance rate for the influence rating definition within the first month ensures the tool's relevance and user acceptance.
- **K2** 80% of regional coordinators find the influence rating useful for prioritizing outreach actions, assessed via a follow-up survey within three months.  
  Having 80% of regional coordinators find the influence rating useful is critical as it validates the tool's effectiveness in outreach prioritization.

## Open questions for humans

### C2 · MAJOR · blocks the build

**Who will be responsible for the ongoing monitoring and ensuring the accuracy of engagement data used in influence ratings?**

- Why it matters: This decision impacts the reliability of the influence ratings derived from the data provided by users.
- Decision owner: Head of Data Management
- Options: Assign responsibility to regional coordinators / Establish a dedicated data quality oversight committee

### C7 · MAJOR · blocks the build

**What specific policies will be implemented to designate responsibility for ensuring the accuracy of engagement data?**

- Why it matters: Undefined ownership can lead to inconsistencies in the data used, directly affecting the influence ratings accuracy.
- Decision owner: Head of Data Governance
- Options: Define data stewardship roles for regional coordinators / Create a shared responsibility model with periodic audits

## Tension report

A notable disagreement exists over the accountability and process for ensuring the accuracy of engagement data, with the Proposer highlighting the need for organizational input while the Critic stresses the risk associated with reliance on regional coordinators. The discussion remains unresolved on how these responsibilities will be codified.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 30 | - | continue |
| 2 | 7 | 1 | 5 | 1 | 0.29 | 85 | 60 | CONTINUE | continue |
| 3 | 9 | 2 | 5 | 2 | 0.47 | 80 | 30 | CONTINUE | continue |
| 4 | 10 | 2 | 6 | 2 | 0.43 | 75 | 60 | CONTINUE | continue |
| 5 | 10 | 0 | 8 | 2 | 0.19 | 80 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring that engagement data remains accurate and confidential throughout the process.
- Critic's remaining worry (85/100): The process for ensuring the accuracy and reliability of the engagement history is still heavily reliant on regional coordinators, which can introduce variability.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The proposal does not specify how the predefined criteria for influence ratings will respect the confidentiality of sensitive diplomatic contacts. |
| C2 | MAJOR | OWNERSHIP | A3 | R1 | ESCALATED | 0 | There is insufficient clarity on who is responsible for ensuring the accuracy and consistency of the data used in determining influence ratings. |
| C3 | MAJOR | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | The proposal does not clarify how qualitative adjustments made by users to influence ratings will be protected, potentially exposing sensitive opinions or biases. |
| C4 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definitions provided regarding influence ratings are subjective and lack clear, measurable criteria that can be tested or evaluated objectively. |
| C5 | MAJOR | DEFINITIONS | D2 | R1 | REVISED | 0 | The term 'predefined criteria' is not sufficiently defined, leading to potential inconsistencies in how different users apply these criteria without a standard framework. |
| C6 | MINOR | OWNERSHIP | X1 | R1 | DEFENDED | 0 | The proposal does not outline how conflicts arising from disagreements over influence ratings will be handled, leading to potential disputes among users. |
| C7 | MAJOR | OWNERSHIP | A3 | R2 | ESCALATED | 0 | A process for monitoring and ensuring the accuracy of the engagement data necessary for influence ratings is undefined, risking incorrect prioritization. |
| C8 | BLOCKER | CONFIDENTIALITY | GAP | R3 | REVISED | 1 | The proposal does not clarify how the predefined criteria for influence ratings will respect the confidentiality of sensitive diplomatic contacts, risking exposure of sensitive information. |
| C9 | MAJOR | DEFINITIONS | S1 | R3 | REVISED | 0 | The criteria for influence ratings are still too vague and subjective, which could lead to inconsistent application across different users. |
| C10 | MAJOR | DATA_QUALITY | GAP | R4 | REVISED | 0 | The proposal does not define how discrepancies in engagement history data are handled, risking incorrect influence ratings if engagement data is inaccurate or incomplete. |
