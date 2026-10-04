# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.010.

Challenges: 8 raised · 8 settled between the agents · 0 handed to humans · 0 still open when it ended.

## Summary

This release will provide project managers access to the full engagement history with a country, ensuring informed decision-making prior to starting new missions. Enhancements will clarify controls around access, data quality, and compliance, establishing accountability structures and security measures for sensitive information. No features for editing or deleting engagement history or providing additional analytics are included in this release; the implementation of security and compliance measures remains an area of concern for human decision-makers.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can view the complete engagement history with each country.  
  Project managers can view the complete engagement history with each country, addressing the need for informed decision-making as outlined in the initial feature request.

**In scope**

- **S1** Provide project managers with a feature to access and view the engagement history of a selected country.  
  Project managers will have a feature to access and view the engagement history of a selected country, directly supporting their need for full visibility before mission planning.
- **S2** Display engagement history that includes contact dates, involved personnel, and summary of activities. Data quality will be maintained through a tiered auditing process, where a designated data quality officer will validate information before access is granted to project managers, ensuring accuracy and consistency.  
  Engagement history will include validated contact details and summaries, with a data quality officer designated to maintain accuracy and consistency before access is granted to project managers. _(C2)_
- **S3** Limit access to engagement history to only project managers and authorized regional coordinators. The Data Steward will implement access control measures that include authentication protocols, logging of access attempts, and a notification system for unauthorized access attempts.  
  Access is limited to project managers and authorized coordinators, with the Data Steward implementing strict authentication and monitoring measures to prevent unauthorized access and ensure compliance. _(C1, C4, C7)_
- **S4** Ensure that engagement history complies with data privacy and sensitivity protocols, including adherence to GDPR, national confidentiality laws, and organizational policies. All access will require justification and will be documented, maintaining a compliance check process.  
  Engagement history will comply with GDPR and national confidentiality laws, outlining specific data privacy protocols to avoid legal breaches and maintain compliance, which is critical for handling sensitive information. _(C3, C8)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include features for editing or deleting engagement history.  
  Editing or deleting engagement histories is excluded to maintain data integrity and protect sensitive information.
- **X2** This release will not provide additional analytics or insights into engagement history beyond what is displayed.  
  Additional analytics beyond the displayed engagement history are not included to keep the focus on essential access features for project managers.
- **X3** This release will not allow access to engagement history for users other than project managers and authorized coordinators.  
  Access restrictions are firmly set, with no allowance for users outside the specified project managers and authorized regional coordinators, ensuring the security of sensitive data.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that project managers need the engagement history to make informed decisions before new missions, which is the basis for this feature request. | Kept | never challenged |
| A2 | It is assumed that engagement histories are stored in the CRM system and are up to date. | Kept | never challenged |
| A3 | It is assumed that there are no existing legal or organizational barriers preventing project managers from accessing historical engagement data. | Kept | never challenged |

## Definitions

- **D1** "engagement history" means a record of all interactions between the organization and the government counterpart, including dates of contact, participants, and summaries of discussions or activities.  
  The definition of 'engagement history' has been clarified to delineate what information will be available to project managers regarding interactions with government counterparts.
- **D2** "project managers" means designated personnel responsible for overseeing specific missions or projects within the organization.  
  The definition of 'project managers' ensures clarity on who will have access, aligning with expectations of personnel responsible for missions.
- **D3** "relevant authorized regional coordinators" means regional coordinators designated by the Data Steward based on their involvement in or necessity for accessing a specific country’s engagement history.  
  This definition formalizes criteria for 'relevant authorized regional coordinators', reducing ambiguity in access rights and responsibilities. _(C5)_

## Success criteria

- **K1** Successfully providing access to engagement history to 100% of project managers as measured by system access logs within one month of the release.  
  The success criterion emphasizes that 100% of project managers must access the engagement history within a month, focusing on monitoring system access logs as a measure of success.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary tension revolved around the clarity and robustness of access controls and compliance measures related to sensitive data. While the Proposer was confident in the defined mechanisms, the Critic remained concerned about the possibility of mishandling sensitive information despite improvements in monitoring and compliance protocols.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 8 | 6 | 2 | 0 | 0.88 | 80 | 50 | CONTINUE | continue |
| 3 | 8 | 0 | 8 | 0 | 0.00 | 65 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (65/100): Ensuring effective implementation of security and compliance measures in a timely manner.
- Critic's remaining worry (80/100): Despite clarifying mechanisms for access and monitoring, there remains a concern about the potential for mishandling of sensitive data.
- ⚠ C6 was settled by wording a later edit removed; the final proposal no longer says: "Ensure that engagement history complies with data privacy and sensitivity protocols, with a retention policy stating engagement histories will be accessible for a period of three years from the last engagement, subject to yearly reviews for relevance and compliance."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | REVISED | 1 | S3 limits access to engagement history to project managers and relevant authorized regional coordinators but does not define how unauthorized access is prevented, nor how to ensure those designated as authorized are appropriate. |
| C2 | MAJOR | DATA_QUALITY | S2 | R1 | REVISED | 1 | S2 states the engagement history will display contact dates, involved personnel, and summaries of activities but does not confirm how the quality, accuracy, and consistency of this data will be maintained. |
| C3 | MAJOR | COMPLIANCE | S4 | R1 | REVISED | 1 | S4 mentions compliance with data privacy and sensitivity protocols, but does not specify what those protocols are or outline the necessary steps to comply with legal requirements for accessing personal data. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 1 | There is no clear ownership delineation for the engagement history data among project managers and regional coordinators, raising concerns about data maintenance and access governance. |
| C5 | MINOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The term 'relevant authorized regional coordinators' is vague and lacks definition, leading to uncertainty about access rights. |
| C6 | MINOR | OPERATIONS | GAP | R1 | REVISED | 0 | It is unclear how long engagement histories will be kept accessible to project managers and if there are any limitations or guidelines post-access. |
| C7 | BLOCKER | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | There is no indication of the specific protocols or mechanisms in place to prevent unauthorized access to sensitive engagement histories. |
| C8 | MAJOR | COMPLIANCE | GAP | R2 | REVISED | 0 | The proposal lacks clear definitions of the existing data privacy and sensitivity protocols which are critical to ensuring compliance with legal requirements. |
