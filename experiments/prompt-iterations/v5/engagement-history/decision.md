# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.005.

## Summary

The proposal will allow project managers to access a comprehensive history of engagement with a country before starting a new mission, with an added approval process for access to sensitive information. It will not modify the engagement data input process, change data retention policies, or permit the export of engagement histories outside the Government CRM. Key outstanding questions remain regarding data ownership and access revocation protocols that require human decision-making.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers will have access to the full history of engagement with a country.  
  Project managers will have access to the full history of engagement with a country to inform their mission decisions.
- **V2** The engagement history will be displayed in a clear and organized manner for each country.  
  The engagement history will be displayed clearly for each country to facilitate easy understanding for project managers.

**In scope**

- **S1** The system will compile engagement history that includes meeting dates, attendees, discussion topics, and outcomes for every country.  
  The system will compile engagement history to include essential details like meeting dates and outcomes, aiding project managers in their missions. _(C1, C2)_
- **S2** Project managers will have a dedicated interface to view engagement histories for the 100 member countries.  
  A dedicated interface will provide project managers with easy access to engagement histories across member countries.
- **S3** S3: The engagement history will be filtered to show only interactions relevant to the specific project manager's prior missions, defined as interactions within the last five years that include topics related to the current mission's objectives. Each engagement history accessed will trigger an approval process requiring the project manager to document the mission purpose before data retrieval.  
  Engagement history will be filtered to show only relevant interactions based on defined criteria, ensuring data relevance and context for project managers. _(C2)_
- **S4** Access to this engagement data will be restricted to project managers with security clearance level 3 and authorized regional coordinators with security clearance level 2.  
  Access restrictions ensure only authorized project managers and regional coordinators can retrieve sensitive engagement history data, protecting confidentiality. _(C1, C4)_
- **S5** The engagement history will include a date range filter to select relevant interactions.  
  A date range filter will allow project managers to focus on relevant interactions, further refining their access to important data.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include modifications to the engagement data input process.  
  Modifications to the engagement data input process are not required for this release.
- **X2** This release will not address changes to data retention policies for engagement history.  
  Changes to data retention policies were deemed unnecessary for this proposal, focusing instead on current data access.
- **X3** This release will not allow for exporting engagement histories outside the Government CRM.  
  Not allowing the export of engagement histories prevents potential leaks of sensitive information.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Project managers require access to historical engagement data to make informed decisions about new missions, as stated in the request. | Kept | never challenged |
| A2 | Historical engagement data is reliably recorded within the Government CRM for all countries. | Kept | never challenged |
| A3 | Users accessing engagement histories will have the appropriate security clearances to view sensitive information. | Kept | never challenged |
| A4 | The Government CRM currently supports displaying filtered lists of data based on user roles. | Kept | never challenged |

## Definitions

- **D1** 'Engagement history' means a record of all interactions with a specific country that includes meeting dates, attendees, discussion topics, and outcomes, with relevance defined by interactions within the last five years related to the current mission's objectives.  
  Clarified to detail 'engagement history' which includes all relevant interactions to guide project managers accurately. _(C2)_
- **D2** 'Project manager' means a user role in the system responsible for leading missions and projects involving designated countries.  
  Defined 'project manager' to specify roles involved in mission leadership and context within the system.

## Success criteria

- **K1** At least 80% of project managers report satisfaction with the ease of use of the engagement history interface, measured through a user feedback survey within one month of release.  
  Success is gauged by user satisfaction with the new interface, validating the need for effective usability amid these changes.

## Open questions for humans

### C3 · MAJOR · does not block the build

**Who is accountable for the integrity and accuracy of the engagement history data within the Government CRM?**

- Why it matters: This decision impacts how reliable the engagement history data is for project managers' decision-making.
- Decision owner: Organizational governance body
- Options: Assign a designated data steward / Create a rotating responsibility among team members / Use external audits for quality assurance

### C5 · MAJOR · does not block the build

**What processes are in place to ensure the ongoing maintenance and verification of engagement history data quality?**

- Why it matters: Failure to maintain data quality could lead to poor decision-making by project managers.
- Decision owner: Organizational policy committee
- Options: Establish periodic review procedures / Implement automated data quality checks / Assign specific roles for data quality control

### C6 · MAJOR · does not block the build

**What protocols exist to revoke access for project managers to engagement history data when their roles change or they leave the organization?**

- Why it matters: Unmonitored access revocation poses security risks for sensitive engagement data.
- Decision owner: Data protection officer
- Options: Implement a role change notification system / Develop a distinct offboarding process for access permissions / Regularly audit current data access permissions

## Tension report

The primary disagreement revolved around the responsibilities for maintaining the accuracy and security of engagement history data, as well as procedures for access revocation. While some issues were resolved around access controls, key questions remain unresolved regarding ownership and data integrity.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 35 | - | continue |
| 2 | 6 | 3 | 2 | 1 | 0.64 | 80 | 45 | CONTINUE | continue |
| 3 | 6 | 0 | 3 | 3 | 0.43 | 75 | 70 | CONTINUE | converged |

- Proposer's remaining worry (75/100): There is a significant risk surrounding data integrity and access control due to existing organizational policies that we cannot modify directly.
- Critic's remaining worry (70/100): There are unresolved issues regarding data access revocation procedures and data maintenance responsibilities that could lead to unauthorized access or use of sensitive information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | Access to engagement history for project managers and regional coordinators must be clearly defined to ensure sensitive data is not exposed to unauthorized users. |
| C2 | MAJOR | DEFINITIONS | S3, D1 | R1 | REVISED | 0 | The definition of 'relevant interactions' for project managers is vague and might lead to inconsistencies in what data is displayed. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | ESCALATED | 0 | It is unclear who is responsible for maintaining and ensuring the accuracy of the engagement history data housed in the CRM. |
| C4 | BLOCKER | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | There are no defined safeguards or access controls stated in the proposal to prevent project managers from seeing confidential engagement data outside their project scope. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 0 | The proposal does not specify who is responsible for ensuring the accuracy and integrity of the engagement history data as it is maintained in the CRM. |
| C6 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 0 | The proposal does not address what happens to a project manager's access to engagement history data when they change roles or leave the organization. |
