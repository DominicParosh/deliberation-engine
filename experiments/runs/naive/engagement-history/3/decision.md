# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 6 rounds (policy `naive`) · $0.018.

Challenges: 20 raised · 16 settled between the agents · 3 handed to humans · 1 still open when it ended.

## Summary

The feature will allow project managers to access a detailed engagement history for each country, with mechanisms in place to filter sensitive information and ensure data accuracy. However, the retention of engagement history and the technical feasibility of retrieving data efficiently under load remain unresolved issues that still need human decisions.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can access a detailed engagement history for each country.  
  Project managers can access a detailed engagement history for each country, which is key for informed decision-making.

**In scope**

- **S1** Engagement history will be subject to a quarterly review process to ensure data accuracy and relevance. Designated data stewards will validate the information against original records, and data quality checks will involve verifying existing records at least once every quarter, updating the database as necessary, and documenting changes for accountability.  
  Engagement history will undergo quarterly reviews to verify its accuracy and relevance, addressing concerns over data quality. _(C3, C19)_
- **S2** Project managers are defined as users with a role of 'Project Manager' in the Government CRM system, and they will only gain access to engagement history that falls within the limits of their assigned permission levels. The system will implement a role-based access control mechanism that filters out sensitive or confidential information based on established criteria, using metadata tagging for records to ensure only non-confidential records are displayed to Project Managers.  
  The filtering mechanism for access based on role and permission levels was clarified, ensuring project managers only access non-sensitive engagement records. _(C1, C9, C10)_
- **S3** The system shall display engagement history for a selected country in a user-friendly interface, accessible within 2 clicks from the country profile, and all access will be logged for compliance tracking. Access logs will include user details, timestamps of access, nature of records accessed, and specific engagement history records viewed. Logs will be retained for a minimum of 5 years to ensure compliance monitoring and enable auditing.  
  Access to engagement history is logged for compliance tracking, enhancing transparency and accountability. _(C4, C12)_
- **S4** The engagement history will be retained for a period of 6 years from the date of the last interaction, ensuring compliance with data retention policies. After this period, data will be archived or deleted according to the organizational data handling policy.  
  A clear retention period of six years for engagement history was established to comply with data handling policies. _(C13)_
- **S5** Users will have the ability to filter the engagement history by date range, contact, or project to find specific information quickly.  
  Users will have filtering capabilities to quickly find specific engagement information by date range, contact, or project.
- **S6** Access to engagement history will automatically be revoked when a Project Manager changes roles or leaves the organization. The HR department is responsible for managing and revoking access rights, ensuring that this is completed within 24 hours of the change being processed to prevent unauthorized access to sensitive data.  
  Access revocation processes linked to role changes or employee exit have been defined, with HR responsible for timely management. _(C2, C10)_
- **S7** The system shall be designed to retrieve engagement history data for five years in under 5 seconds for 95% of requests, utilizing optimized database queries and caching mechanisms to ensure efficiency.  
  The system must retrieve engagement history data efficiently, with an expected response time set for quick access. _(C7, C14)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include the ability for project managers to edit engagement history.  
  Project managers will not be able to edit engagement history, maintaining the integrity of records.
- **X2** This release does not allow access to sensitive or confidential notes associated with engagements unless the user has explicit permissions, which must be validated based on their role and current permissions.  
  Project managers will not have access to confidential notes unless explicitly permitted, ensuring confidentiality is upheld.
- **X3** The integration with external systems for historical data retrieval is not included in this release.  
  Integration with external systems for historical data retrieval was not included in this release to focus on internal processes.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The current CRM already stores engagement history in a retrievable format; this is necessary for project managers to access it. | Kept | never challenged |
| A2 | Users with the 'Project Manager' role have permissions to access the relevant engagement history features. | Kept | never challenged |
| A3 | There are no legal or organizational restrictions that would prevent sharing engagement history with project managers. | Kept | C2 → revised; C10 → revised; C17 → revised |

## Definitions

- **D1** Engagement history means a chronological record of all interactions with contacts from the country, including meeting dates, participants, topics discussed, and action items. This is essential for project managers to understand prior dealings.  
  Engagement history is defined to provide essential context for project managers, encompassing various interaction records.
- **D2** Project Manager means a user who has been assigned the role of 'Project Manager' in the Government CRM system, with the ability to manage projects and access related data.  
  Project Manager is explicitly defined to clarify user capabilities within the system.

## Success criteria

- **K1** At least 80% of project managers report that they can successfully access and utilize the engagement history before initiating a new mission, measured through a user satisfaction survey conducted after the implementation.  
  A success metric has been defined to ensure project managers can effectively access and utilize the engagement history.
- **K2** The expected response time for retrieving a five-year engagement history will be defined as no longer than 5 seconds for 95% of all requests, measured through system logging and usage statistics after deployment.  
  A performance target ensures that retrieval of five-year histories meets user satisfaction requirements.

## Open questions for humans

### C5 · MAJOR · blocks the build

**What is the established retention period for engagement history, and what policies govern this storage?**

- Why it matters: Defining a retention period is essential for compliance with data protection regulations.
- Decision owner: Head of Data Management
- Options: Define a retention period / Maintain indefinite retention / Establish periodic review for retention

### C8 · MAJOR · blocks the build

**What is the defined retention period for engagement histories, and how will that be enforced?**

- Why it matters: Specifying a retention period is crucial for ensuring compliance and avoiding excessive data storage.
- Decision owner: Compliance Officer
- Options: Establish a strict retention period / Define exceptions for certain records / Review regularly for compliance

### C18 · MAJOR · blocks the build

**What has been validated regarding the system's performance under load for retrieving extensive engagement history?**

- Why it matters: This will help to identify potential bottlenecks and ensure timely access for project managers.
- Decision owner: Development Team
- Options: Define performance metrics / Conduct stress testing / Review past performance data

### C6 · MINOR · does not block the build

**What are the expected performance metrics for efficiently retrieving a five-year historical engagement record?**

- Why it matters: Understanding performance will ensure the system meets operational requirements and user expectations.
- Decision owner: Technical Lead
- Options: Set performance benchmarks / Conduct performance testing post-implementation / Review system capacity

## Tension report

The key disagreement revolved around the technical feasibility of retrieving historical engagement records and ensuring robust filtering mechanisms for sensitive data. The Proposer expressed confidence in the proposed systems but acknowledged dependence on HR for timely data management, while the Critic raised concerns about potential operational risks due to reliance on these mechanisms.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 8 | 3 | 4 | 1 | 0.44 | 80 | 70 | CONTINUE | continue |
| 3 | 12 | 4 | 5 | 3 | 0.56 | 75 | 40 | CONTINUE | continue |
| 4 | 14 | 2 | 9 | 3 | 0.31 | 80 | 50 | CONTINUE | continue |
| 5 | 20 | 6 | 11 | 3 | 0.43 | 80 | 35 | CONTINUE | continue |
| 6 | 20 | 1 | 16 | 3 | 0.17 | 85 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): The reliance on HR for timely access revocation may introduce delays and risks if not managed efficiently.
- Critic's remaining worry (80/100): Although there are improvements, the filtering of sensitive records and the operational efficiency of the system under heavy load still raise concerns about potential data breaches.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2, X2 | R1 | REVISED | 0 | There is no clarity on how the system will filter engagement history to prevent unauthorized access to sensitive or confidential records by Project Managers. |
| C2 | MAJOR | OWNERSHIP | S2, A3 | R1 | REVISED | 0 | The proposal does not clarify what happens when a Project Manager changes roles or leaves the organization; will their access be revoked and how is that managed? |
| C3 | MAJOR | DATA_QUALITY | S1, D1 | R1 | REVISED | 0 | There's a lack of clarity on how the system ensures that the engagement history is accurate, current, and relevant; what checks are in place to maintain data quality? |
| C4 | MAJOR | COMPLIANCE | S3 | R1 | REVISED | 0 | The proposal does not define how engagement history access will be logged for auditing purposes, raising compliance concerns on data access and monitoring. |
| C5 | MAJOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | The proposal does not mention how long engagement history will be retained and what policies dictate this retention. |
| C6 | MINOR | FEASIBILITY | GAP | R1 | ESCALATED | 1 | The proposal does not provide any information on the technical feasibility of retrieving a five-year historical engagement record efficiently. |
| C7 | MAJOR | FEASIBILITY | GAP | R2 | REVISED | 0 | There is no defined performance metric for the retrieval time of five-year engagement records, leading to uncertainty in its usability. |
| C8 | MAJOR | COMPLIANCE | GAP | R2 | ESCALATED | 0 | The proposal does not specify any retention period for engagement history, creating potential legal and compliance risks. |
| C9 | BLOCKER | CONFIDENTIALITY | S2, X2 | R3 | REVISED | 0 | The proposal lacks clear mechanisms for filtering sensitive or confidential records when making engagement history available to Project Managers. |
| C10 | MAJOR | OWNERSHIP | S2, A3 | R3 | REVISED | 0 | The proposal does not outline who is responsible for managing access rights when a Project Manager changes roles or leaves the organization. |
| C11 | MAJOR | DATA_QUALITY | S1, D1 | R3 | REVISED | 0 | The proposal does not specify how the accuracy of engagement history data will be verified and maintained over time. |
| C12 | MAJOR | COMPLIANCE | S3 | R3 | REVISED | 0 | There is insufficient clarity on how access to engagement history will be logged, which raises compliance concerns regarding auditing and monitoring. |
| C13 | MAJOR | COMPLIANCE | GAP | R4 | REVISED | 0 | The proposal does not specify how long engagement history will be retained and what policies dictate this retention. |
| C14 | MAJOR | FEASIBILITY | GAP | R4 | REVISED | 0 | There is no information on the technical feasibility of retrieving engagement history efficiently, especially given the five-year scope. |
| C15 | BLOCKER | CONFIDENTIALITY | S2, X2 | R5 | REVISED | 0 | The proposal does not specify how the system will filter engagement history to prevent unauthorized access to sensitive or confidential records by Project Managers. |
| C16 | MAJOR | COMPLIANCE | S3 | R5 | REVISED | 0 | The proposal does not define how engagement history access will be logged for auditing purposes, raising compliance concerns on data access and monitoring. |
| C17 | MAJOR | OWNERSHIP | S2, A3 | R5 | REVISED | 0 | The proposal does not outline who is responsible for managing access rights when a Project Manager changes roles or leaves the organization. |
| C18 | MAJOR | FEASIBILITY | GAP | R5 | UNRESOLVED | 1 | The proposal does not provide evidence of technical feasibility for retrieving five years of historical engagement records efficiently. |
| C19 | MAJOR | DATA_QUALITY | S1, D1 | R5 | REVISED | 0 | The proposal does not specify how the accuracy of engagement history data will be verified and maintained over time. |
| C20 | MAJOR | COMPLIANCE | S3 | R5 | DEFENDED | 0 | There is insufficient clarity on how access to engagement history will be logged, which raises compliance concerns regarding auditing and monitoring. |
