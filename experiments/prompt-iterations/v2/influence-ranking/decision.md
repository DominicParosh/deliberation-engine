# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.008.

## Summary

This release will implement a scoring system to evaluate the influence of contacts, enabling users to identify and prioritize key contacts in the Government CRM system. It will include the visibility of influence scores exclusively for regional coordinators and project managers. The human aspect of ensuring compliance with data protection and maintaining data accuracy remains a significant concern that will require ongoing management.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to see a list of their most influential contacts based on specific influence criteria.  
  This item establishes the functionality that allows users to view their most influential contacts based on set criteria, facilitating better prioritization.
- **V2** Allow users to filter and sort contacts by influence score.  
  This item ensures users can filter contacts by their influence score, aiding in the identification of key relationships.

**In scope**

- **S1** Define three influence criteria: position (organizational rank), engagement level (frequency of contact in the last year), and reach (number of key decisions influenced). Each criterion will be scored from 1 to 5.  
  Defining three specific influence criteria enables consistent scoring and evaluation across users, which is critical for reliability. _(C2)_
- **S2** Create an influence score for each contact by averaging the individual scores across the three criteria. Influence scores will be deleted when a contact is modified or removed from the CRM.  
  A structured approach to influence score retention when contacts are modified supports compliance with data management standards. _(C6)_
- **S3** Implement a user interface that displays the influence score next to each contact record, accessible only to regional coordinators and project managers. Access will be managed via role-based access controls.  
  Restricting access to influence scores through role-based controls mitigates risks associated with the exposure of sensitive information. _(C1, C4, C5)_
- **S4** Enable filtering options for users to list contacts by influence score (high to low or low to high).  
  Providing filtering options enhances user experience, enabling effective prioritization of contacts based on influence.
- **S5** Provide an export option for the contact list filtered by influence score to CSV format.  
  Exporting contact lists filtered by influence score allows for greater flexibility in user data management.

## What it will not do

**Out of scope for this release**

- **X1** The system will not provide a dynamic method for influence scoring adjustments based on real-time data.  
  Dynamic influence scoring adjustments based on real-time data would complicate data integrity and privacy considerations and are therefore excluded.
- **X2** Integration with external data sources for influence analysis will not be included in this release.  
  Integration with external sources for influence analysis introduces security and data protection complexities, thus deemed out of scope.
- **X3** Historical engagement analysis or influence prediction features will not be developed in this release.  
  Historical engagement analysis is not included as it requires advanced capabilities that the current system does not support.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | It is assumed that users have the necessary data about contacts’ positions, engagement levels, and reach. | The influence scoring relies on the availability and accuracy of these attributes in the CRM. | Accepted (never challenged) |
| A2 | It is assumed that users are familiar with the concepts of influence and how to assess it based on the defined criteria. | Stakeholders must understand the rationale behind influence scoring to use the feature effectively. | Accepted (never challenged) |
| A3 | It is assumed that the CRM data governance team is responsible for maintaining and updating historical engagement data specifically to ensure accuracy of influence scores. | Accurate historical data is essential for generating reliable influence scores. | C3 → revised |

## Definitions

- **D1** "influence criteria": Factors used to evaluate the influence level of a contact, specifically: 'position' (organizational rank), 'engagement level' (frequency of contact in the last year), and 'reach' (number of key decisions influenced).  
  Defining influence criteria ensures consistency in scoring across the user base, reducing potential discrepancies in interpretation.
- **D2** "influence score": A numeric representation of a contact's influence, calculated as the average of scores assigned to each of the three influence criteria.  
  Providing a clear definition of influence score supports users in understanding how influence is calculated, promoting correct usage.

## Success criteria

- **K1** Percentage of users: target At least 75% (Measured by user login tracking and feature interaction logging in the CRM system over the first three months post-launch.)  
  Setting a user percentage target post-launch establishes a measurable success criterion, allowing performance assessment of the new feature.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary tension was around ensuring the accuracy and confidentiality of the influence scoring system, with the Proposer advocating for operational usability while the Critic focused on data protection concerns. This tension was addressed through revisions that established clear user access roles, safeguards for sensitive data, and clarified ownership responsibilities for data accuracy.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 4 | 2 | 0 | 0.67 | 75 | 45 | CONTINUE | continue |
| 3 | 6 | 0 | 6 | 0 | 0.00 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring compliance with data protection is complex and needs constant oversight.
- Critic's remaining worry (85/100): There is still uncertainty about the accuracy of influence scoring due to assumptions around data availability.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S1, D1 | R1 | REVISED | 0 | The proposal does not clearly define who has access to the influence scores and how it mitigates risks of exposing sensitive information about influential contacts. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definitions of 'position', 'engagement level', and 'reach' are vague and subjective, making it difficult to reliably evaluate and score influence across contacts. |
| C3 | MAJOR | OWNERSHIP | A3 | R1 | REVISED | 1 | The proposal assumes historical data about contacts is accessible without defining who is responsible for maintaining and updating this data to ensure ongoing accuracy of influence scores. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal lacks clarity regarding the procedures for handling sensitive data associated with influential contacts and what safeguards are in place to prevent unauthorized sharing beyond the defined user roles. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not address how changes in user roles will affect access to influence scoring and sensitive contact data after personnel transitions or changes in role. |
| C6 | MAJOR | COMPLIANCE | GAP | R2 | REVISED | 0 | There is no mention of a data retention policy for influence scores once contacts are modified or removed from the CRM, which raises compliance risks regarding data management. |
