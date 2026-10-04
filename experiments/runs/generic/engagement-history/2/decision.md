# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 2 rounds (policy `gated`) · $0.005.

Challenges: 5 raised · 5 settled between the agents · 0 handed to humans · 0 still open when it ended.

## Summary

The feature to be developed will allow project managers and regional coordinators to access the complete history of engagements with each country, ensuring appropriate access restrictions are in place. The final proposals include a user interface for viewing engagement histories, with data managed and verified for accuracy, while compliance with data retention policies is strictly maintained. There are unresolved concerns regarding specific cross-access roles and management processes as project personnel change.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can access the full history of engagements with each country.  
  Project managers will have access to the full history of engagements with each country, which ensures they are informed before starting new missions.

**In scope**

- **S1** Implement a user interface for project managers that displays engagement history with countries, including dates, descriptions of interactions, and associated personnel.  
  A new user interface will be created for project managers that displays detailed engagement history, enhancing transparency and accessibility.
- **S2** Gather and aggregate relevant historical data from existing records related to each country's engagements into a unified view, with a designated data owner responsible for maintaining and updating access as project managers transition roles.  
  Historical data will be aggregated from existing records with a designated data owner responsible for accuracy verification. _(C3, C4)_
- **S3** Ensure that the engagement history includes data only from the last 5 years in accordance with the organization's data retention policy, while records older than 5 years will be archived and accessible only with special permission to ensure compliance and historical context.  
  The engagement history will include only the last 5 years of data to comply with retention policies, addressing potential data loss and compliance issues. _(C5)_
- **S4** Restrict access to this engagement history feature to project managers and regional coordinators only. Access by regional coordinators allows for appropriate oversight and ensures that sensitive information is more securely managed.  
  Access is strictly allowed for project managers and regional coordinators to help manage sensitive information effectively. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any functionality for editing or deleting historical engagement records.  
  No editing or deleting of historical engagement records will be allowed in this release to maintain data integrity.
- **X2** This release will not cover engagement data older than 5 years.  
  Data older than 5 years will not be included in this release to adhere to retention policies.
- **X3** This release will not include access for users outside of the project management role.  
  Access will not be extended beyond project managers and regional coordinators to maintain strict control over sensitive information.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that historical engagement data is already available in the system and can be aggregated without major technical challenges. | Kept | never challenged |
| A2 | It is assumed that project managers are already established as a distinct user role within the Government CRM. | Kept | never challenged |
| A3 | It is assumed that the sensitivity of the data will be appropriately managed according to existing organizational policies. | Kept | never challenged |

## Definitions

- **D1** "engagement history" means a chronological record of all interactions with a country, excluding sensitive diplomatic communications, confidential internal memos, and any records designated as restricted access.  
  The revised definition of 'engagement history' now explicitly excludes sensitive communications, improving data safety. _(C2)_
- **D2** "project managers" means individuals assigned within the organization whose responsibilities include overseeing specific projects and missions.  
  The definition of 'project managers' accurately describes their role and functions to clarify feature access.
- **D3** "full history" means all records of engagement for a country within the last 5 years.  
  The definition of 'full history' specifies it as the last 5 years of records, ensuring compliance with policies.

## Success criteria

- **K1** At least 80% of project managers report satisfaction with the new engagement history feature based on a user survey conducted within three months of release.  
  Satisfaction of project managers with the new feature will be measured to gauge its effectiveness and usability.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement revolved around the management of sensitive data and clarity of access roles. Over the deliberation rounds, the Proposer and Critic worked towards defining clear access and management stipulations, ultimately achieving a consensus that addressed confidentiality concerns while providing necessary access.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 5 | 0 | 5 | 0 | 0.00 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring sensitive information remains protected while providing adequate access for project managers and regional coordinators.
- Critic's remaining worry (85/100): Ensuring that access control remains strict and effectively managed as project managers change roles.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | S4 restricts access to the engagement history feature to project managers without clarifying who else may access this data or how cross-functional access is managed. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | D1 describes "engagement history" but does not specify which records are excluded from this definition, risking the inclusion of sensitive communications. |
| C3 | MAJOR | DATA_QUALITY | S2 | R1 | REVISED | 0 | S2 lacks detail about the source of historical engagement data and how the accuracy of this data will be ensured during aggregation. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not clarify who maintains the engagement history data or how it is managed when project managers transition or leave. |
| C5 | MAJOR | COMPLIANCE | S3 | R1 | REVISED | 0 | S3 states engagement history will only include data from the last 5 years, but does not address retention policies for older data or compliance aspects related to sensitive information. |
