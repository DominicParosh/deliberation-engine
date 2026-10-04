# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.005.

Challenges: 6 raised · 3 settled between the agents · 3 handed to humans · 0 still open when it ended.

## Summary

This release will enable project managers to view the complete history of engagement with selected countries while ensuring confidentiality through defined access controls. Features include access to engagement records, filtering options, and a clear presentation format. However, the specifics of permission granting and data verification processes require further decision-making.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable project managers to view the complete history of engagement with selected countries.  
  Enable project managers to view engagement history to support informed decision-making about new missions.
- **V2** Ensure data on engagement history is presented in a clear, accessible format.  
  Ensure that the data is presented clearly to enhance usability for project managers.

**In scope**

- **S1** Allow project managers to access engagement history records for any of the ~100 member countries.  
  Project managers will access engagement history for all member countries to ensure comprehensive insights.
- **S2** Display engagement history that includes past projects, meeting notes, and communications related to the country.  
  Engagement history will include detailed records of past projects and communications to provide full context.
- **S3** Implement a filter option that allows project managers to search engagement history by date range or project type.  
  Implementing filters allows project managers to customize their search, improving efficiency.
- **S4** Ensure that only authorized project managers and regional coordinators, as defined by the organization’s access control policies, can access this engagement history data.  
  Access will be restricted to authorized personnel as defined by the organization’s access control policies to protect sensitive data. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** Do not include a feature for editing engagement history records in this release.  
  Editing engagement records is deemed unnecessary and could pose data integrity risks if included in this release.
- **X2** Do not provide analytics or insights derived from engagement history data in this release.  
  Analytics from the engagement data are excluded to focus on core access features without complicating initial build.
- **X3** Do not include integration with external databases or systems to fetch additional records.  
  Integration with external systems is not planned for this release to prevent complications in data handling.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Project managers have the necessary permissions to view engagement history data, which is essential for them to access this feature. | Kept | C3 → escalated |
| A2 | All engagement history data is maintained accurately within the CRM, relying on previous data entry processes. | Kept | C5 → escalated |
| A3 | Users have prior knowledge of how to navigate to the engagement history section in the CRM. | Kept | never challenged |

## Definitions

- **D1** "Engagement history" means a chronological record of all documented interactions, meetings, projects, and communications related to a specific country stored within the CRM. This includes written communications such as emails and official reports, as well as notes from meetings. Access to engagement histories will vary based on their sensitivity, and more sensitive diplomatic records will have stricter access thresholds.  
  Definition of 'engagement history' has been refined to specify documented interactions, reducing ambiguity for users. _(C2)_
- **D2** "Project managers" means individuals responsible for planning and executing missions who require full context regarding a country's past engagements to make informed decisions.  
  Clarifies that 'project managers' are defined as individuals involved in mission planning requiring historical context.

## Success criteria

- **K1** Achieve an 80% satisfaction rate from project managers regarding accessibility and clarity of engagement history within the first three months of release.  
  Success will be measured by a satisfaction rate, ensuring the release meets users' needs for accessing engagement history effectively.

## Open questions for humans

### C3 · MAJOR · blocks the build

**What is the process for granting and revoking access permissions for project managers?**

- Why it matters: Clarifying permission processes is essential to mitigate risks of unauthorized access and ensure data protection.
- Decision owner: Head of Data Protection
- Options: Define specific role-based access controls / Regularly review and update access permissions / Implement a formal access request and tracking system

### C4 · MINOR · does not block the build

**What system performance benchmarks are set to handle simultaneous requests for engagement histories?**

- Why it matters: Establishing performance benchmarks is crucial to ensure the system can support multiple project managers accessing data concurrently without failure.
- Decision owner: IT Operations Manager
- Options: Implement load balancing technologies / Conduct stress testing before release / Set user access limits during peak times

### C5 · MINOR · does not block the build

**What processes are in place to regularly verify and update the accuracy of engagement history data?**

- Why it matters: Ensuring data accuracy is vital to prevent project managers from making decisions based on obsolete or incorrect information.
- Decision owner: Data Quality Assurance Lead
- Options: Schedule regular audits of engagement data / Develop a user feedback mechanism for data inaccuracies / Establish clear data entry protocols

## Tension report

The main disagreement arose around the specifics of user access permissions and data quality assurance processes, both of which need to be defined by organizational policy. While the proposer recognized these concerns, the critic emphasized the risks posed by unclear protocols, necessitating further input from decision-makers.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 0 | 3 | 3 | 0.40 | 80 | 60 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring the integrity and accuracy of sensitive data access in compliance with data protection standards.
- Critic's remaining worry (60/100): Unclear processes for granting and revoking user permissions leave the system vulnerable to unauthorized access.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | S4 states that only authorized project managers and regional coordinators can access engagement history data, but it does not specify how 'authorized' is determined, which is crucial for data protection. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | D1 defines 'engagement history' as a chronological record but does not clarify what types of communications or interactions are included or excluded, potentially leading to inconsistencies. |
| C3 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | A1 assumes that project managers have the necessary permissions without detailing how permissions are granted or managed, creating risks of unauthorized access. |
| C4 | MINOR | OPERATIONS | S1 | R1 | ESCALATED | 0 | S1 allows project managers to access engagement history for any of the ~100 member countries but does not address how to manage system load or data retrieval during high demand. |
| C5 | MINOR | DATA_QUALITY | A2 | R1 | ESCALATED | 0 | A2 relies on the assumption of accurate data maintenance within the CRM but does not outline how data quality will be monitored and verified. |
| C6 | MINOR | CONFIDENTIALITY | D1 | R1 | REVISED | 0 | D1 does not clarify whether there are any thresholds for what types of engagement histories can be accessed, particularly concerning more sensitive diplomatic records. |
