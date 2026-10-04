# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.011.

## Summary

This release will enable project managers to view the full engagement history with a country before starting a new mission, which will include detailed engagement records aimed at enhancing decision-making. However, unresolved issues regarding access control for sensitive data and the specific types of records included in the engagement history remain. Human decisions are required to finalize these aspects before implementation can begin.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable project managers to view engagement history with countries.  
  This commitment is to provide project managers access to engagement histories which was necessary for better mission preparation.
- **V2** Present comprehensive context for project managers to facilitate better mission planning.  
  The commitment to present comprehensive context facilitates informed decision-making for mission planning.

**In scope**

- **S1** Project managers can access a dedicated engagement history section within the CRM for each country.  
  Project managers will have a dedicated section for engagement history, enhancing their ability to access relevant information.
- **S2** Engagement history will include records of past missions, meetings, correspondence, informal communications, and detailed email interactions with each country.  
  The inclusion of various engagement records ensures a holistic view of past interactions with each country.
- **S3** Engagement records will display dates, participants, types of engagement (mission, meeting, correspondence), and summary notes of previous engagements.  
  This item highlights the need for specific details of engagements which can aid in comprehensive preparation.
- **S4** Access to engagement history is restricted to project managers and regional coordinators, with additional enforced data protection measures for highly sensitive records.  
  Access restrictions aim to protect sensitive data, addressing confidentiality concerns raised during deliberations. _(C1)_
- **S5** The engagement history will be available in a user-friendly format that allows filtering by date and type of engagement, with sensitive records being encrypted and only displayed to authorized users. Filtering will only allow the display of engagement records that the user is authorized to view.  
  Filtering functionality was updated to safeguard sensitive data, addressing worries about unauthorized access to engagement histories. _(C5)_
- **S6** When a project manager changes roles or leaves the organization, their access to engagement history will be immediately revoked.  
  Clarifying access rights when project managers change roles or leave mitigates risks around unauthorized data access. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** This release does not include features for automated engagement summaries or recommendations.
- **X2** It will not integrate with external tools for engagement tracking beyond the CRM.
- **X3** There will be no changes to user roles or permissions beyond specifying access for project managers and regional coordinators.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users accessing the engagement history are familiar with the CRM interface and functions. | The request implies that project managers will be using the CRM to view engagement histories. | Accepted (never challenged) |
| A2 | The data regarding past engagements is complete and up-to-date in the CRM, with a verification process implemented to maintain data accuracy. | The feature relies on the availability of accurate and comprehensive engagement data. | C3 → escalated |
| A3 | Sensitive data within the engagement history has appropriate access control measures in place and high sensitivity records are flagged accordingly. | Given the sensitivity of the data, proper security measures must exist for access. | Accepted (never challenged) |
| A4 | The organization has a process in place to manage user access rights effectively. | The feature requires clarity on maintaining access rights to prevent unauthorized access. | Accepted (never challenged) |

## Definitions

- **D1** "full history of engagement": A detailed log that includes all recorded interactions such as meetings, emails, informal correspondence, mission details, diplomatic communications, and a specification of filtered categories for types of engagement.  
  The definition was revised to establish clarity on the types of engagement records included, aligning user expectations with available data.
- **D2** "engagement record": A record that lists dates, participants, types of engagement (mission, meeting, correspondence), and summary notes for any interaction related to the country.  
  The definition of engagement records aims to standardize how interactions are logged and viewed in the CRM.

## Success criteria

- **K1** Percentage of project managers accessing the engagement history feature.: target At least 75% of project managers should access the feature within the first month of release. (Measured by survey and usage analytics.)  
  Success criteria were set to measure adoption of the feature by project managers, guiding future assessments.

## Open questions for humans

### C1 · MAJOR · blocks the build

**What specific data protection measures are needed to ensure the confidentiality of highly sensitive engagement records?**

- Why it matters: This is crucial to prevent unauthorized access and potential diplomatic breaches.
- Decision owner: Head of Data Protection
- Options: Define clear access controls for sensitive records. / Implement additional encryption methods. / Establish a review process for sensitive data access requests.

### C3 · MAJOR · blocks the build

**What processes will ensure and verify the accuracy and completeness of engagement records before they are accessed?**

- Why it matters: This ensures that project managers are working with reliable data prior to missions.
- Decision owner: Data Quality Officer
- Options: Implement regular data audits. / Establish a data stewardship role. / Require updates from engagement owners.

### C5 · MAJOR · blocks the build

**What mechanisms will ensure project managers cannot filter engagement history to view sensitive records they are unauthorized to see?**

- Why it matters: This is crucial to prevent unauthorized viewing of sensitive diplomatic communications.
- Decision owner: Head of Data Protection
- Options: Implement role-based access control. / Enhance filtering functionalities based on user roles. / Create automated alerts for unauthorized access attempts.

### C6 · MAJOR · blocks the build

**What specific types of records will be included in the 'full history of engagement'?**

- Why it matters: Clarifying this will manage user expectations and enhance preparation for missions.
- Decision owner: Product Owner
- Options: List all types of records explicitly in documentation. / Categorize engagement records for clarity. / Confirm inclusions with user feedback.

## Tension report

The real disagreement centered around access to sensitive data and the handling of engagement records. The Proposer expressed confidence in the proposed features but acknowledged risks with sensitivity handling, while the Critic raised concerns about the clarity of access permissions, leading to unresolved questions that could affect data security.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 80 | 45 | - | continue |
| 2 | 4 | 1 | 1 | 2 | 0.75 | 85 | 70 | CONTINUE | continue |
| 3 | 6 | 2 | 2 | 2 | 0.67 | 80 | 70 | CONTINUE | continue |
| 4 | 6 | 2 | 2 | 2 | 0.67 | 85 | 60 | CONTINUE | continue |
| 5 | 6 | 0 | 2 | 4 | 0.67 | 75 | 50 | CONTINUE | converged |

- Proposer's remaining worry (75/100): There is still a risk of misinterpretation regarding the engagement history access permissions and sensitivity handling.
- Critic's remaining worry (50/100): Key decisions on data access control and specific record types remain unaddressed, risking unauthorized data exposure.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S4 | R1 | ESCALATED | 0 | Access to engagement history is restricted to project managers and regional coordinators, but doesn't specify what happens to records that contain highly sensitive or diplomatic information. This lack of clarity can lead to unauthorized exposure of sensitive data. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'full history of engagement' appears vague and unbounded. It is unclear if it encompasses all types of records or only selected interactions, which could lead to inconsistencies in what users expect to see. |
| C3 | MAJOR | DATA_QUALITY | A2 | R1 | ESCALATED | 0 | Assumptions regarding the completeness and accuracy of past engagement data are not robustly defined, leaving open the possibility of outdated or missing records, which can misinform project managers. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not specify what happens to access rights for project managers if they leave or change roles, which could lead to unauthorized access to sensitive information. |
| C5 | MAJOR | CONFIDENTIALITY | S1, D1 | R3 | ESCALATED | 1 | The scope does not specify how the filtering functionality will prevent unauthorized viewing of sensitive engagement records when project managers access the engagement history for a country. |
| C6 | MAJOR | DEFINITIONS | D1 | R3 | ESCALATED | 1 | The definition of 'full history of engagement' lacks clarity regarding the specific types of records that are included, which can lead to inconsistent user expectations. |
