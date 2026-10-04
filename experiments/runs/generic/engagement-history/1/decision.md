# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.007.

Challenges: 6 raised · 5 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

The upcoming release will enable project managers to view the complete engagement history for each country they oversee, enhancing their decision-making with necessary context. However, it will not include integration with external databases or historical data beyond the last five years. An unresolved issue regarding compliance with changing data protection policies remains open for further decision-making.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can view the complete engagement history for each country they are responsible for.  
  Project managers will be allowed to view the complete engagement history to provide necessary context for mission planning.

**In scope**

- **S1** A feature will be developed to display the full engagement history, and protocols will be implemented to regularly identify and resolve any duplicate or inaccurate engagement records before presenting them to project managers.  
  The feature will incorporate protocols to manage duplicate or inaccurate engagement records to maintain data quality for project managers. _(C6)_
- **S2** Access to the engagement history will be granted specifically to users with the role of project manager.  
  Access will be restricted to users with the project manager role, ensuring that engagement data is viewed only by authorized personnel.
- **S3** The engagement history will include records from the last 5 years to ensure recent context is available.  
  Restricting the engagement history to the last 5 years will ensure that relevant and recent context is available for project managers.
- **S4** The feature will ensure that only authorized project managers can view sensitive engagement history data, and that access rights for project managers will be revoked automatically within 24 hours of a role change or exit from the organization, to prevent unauthorized access.  
  Clarifications added to specify how access control measures will prevent unauthorized access to sensitive engagement data, thereby addressing previously raised concerns. _(C1, C2)_
- **S5** The system will include mechanisms to verify and validate the accuracy and completeness of engagement history records prior to being made accessible to project managers, ensuring that all available data from the last 5 years is both accurate and complete.  
  Measures for verifying and validating the accuracy and completeness of engagement records were defined to ensure high data quality before access. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any integration with external databases or records beyond the Government CRM system.
- **X2** Historical data prior to the last 5 years will not be included in the engagement history.
- **X3** Real-time notifications or alerts regarding engagement history updates will not be implemented in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that the CRM system has current and accurate records of engagement history for all countries, which this proposal relies on to function. | Kept | never challenged |
| A2 | It is assumed that project managers have been clearly defined as a user role with specific permissions regarding access to sensitive data. | Kept | never challenged |
| A3 | It is assumed that the organization has established confidentiality and data protection policies that will govern how engagement histories are accessed and viewed by project managers. | Kept | never challenged |

## Definitions

- **D1** "engagement history" means the record of all interactions and communications between the organization and a country, including mission details, contact records, meeting notes, and any documented correspondence.  
  The definition of 'engagement history' was accepted to clarify the scope of interactions included in the records.
- **D2** "project manager" means an individual within the organization with the designated responsibility for overseeing missions and projects related to a specific country or region.  
  The definition of 'project manager' was accepted to ensure clarity around the responsibilities and permissions associated with this role.
- **D3** "sensitive engagement history data" means any information that contains personal, confidential, or classified elements, including but not limited to negotiation records, personal-identifiable information of contacts, and internal communications, which are subject to organizational confidentiality rules.  
  The revised definition of 'sensitive engagement history data' clarifies what information is subject to confidentiality, helping to avoid misinterpretation. _(C3)_

## Success criteria

- **K1** Within three months of the feature release, at least 80% of project managers report satisfaction with their ability to access and use the engagement history feature, measured via a user feedback survey.  
  The success criterion focuses on user satisfaction post-release, establishing a clear metric to evaluate the feature's effectiveness.

## Open questions for humans

### C5 · MAJOR · blocks the build

**How will the system ensure that changes to data protection policies are implemented in access and data handling protocols?**

- Why it matters: This is crucial to maintain compliance with evolving data protection standards and avoid potential violations that could arise from policy changes.
- Decision owner: Head of Data Protection
- Options: Implement stricter access controls based on new policies / Conduct regular reviews of access protocols / Remain static until polices are explicitly outlined

## Tension report

Disagreement focused on compliance with changing data protection policies, particularly regarding access and management of sensitive data. The Proposer revised protocols to address relevant concerns, but the Critic escalated compliance issues as unresolved, highlighting a gap in assurance for adherence to evolving policies.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 30 | - | continue |
| 2 | 6 | 0 | 5 | 1 | 0.17 | 80 | 70 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring all defined protocols are effectively implemented and adhered to during development and after release.
- Critic's remaining worry (70/100): The challenge regarding compliance with changing data protection policies is escalated, leaving a potential gap in access control enforcement.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | S4 states that only authorized project managers can view sensitive engagement history data but does not specify the measures or thresholds in place to enforce this access control. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not clarify what happens to the access rights of project managers who change roles or leave the organization, potentially leaving sensitive data accessible to unauthorized users. |
| C3 | MAJOR | DEFINITIONS | D3 | R1 | REVISED | 0 | D3 defines 'sensitive engagement history data' but does not specify which specific categories of information are classified as sensitive, leading to potential inconsistencies in data access. |
| C4 | MAJOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | The proposal does not address how the accuracy and completeness of engagement history records will be ensured, particularly given the limitation to the last 5 years. |
| C5 | MAJOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | The proposal does not address how changes to the organization's data protection policies will impact the access and management of engagement history. |
| C6 | MINOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | There is no mention of how duplicate records or inaccuracies in engagement data will be handled, which could affect the quality of information available to project managers. |
