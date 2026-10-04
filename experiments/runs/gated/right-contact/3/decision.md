# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 2 rounds (policy `gated`) · $0.007.

Challenges: 6 raised · 5 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This feature will enhance the Government CRM by enabling users to efficiently view and update key contact information for government representatives in member countries, with appropriate validations on role definitions. However, there will be no automated alerts for updates or changes to existing data retention policies at this time. A decision is still required on implementing a structured verification process for user-inputted contact information to maintain quality.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to view and update key contact information for each member country.  
  This commitment ensures users can view and update important contact information, addressing the core need of the proposal.
- **V2** Allow users to categorize contacts by role and relevance to their specific projects or missions.  
  This commitment allows categorization of contacts, making it easier for users to prioritize engagement based on project relevance.

**In scope**

- **S1** Implement a new data entry form for users to input and update contact information, including fields for name, title, organization, phone number, email address, and role.  
  Implementation of a data entry form is essential for capturing and managing updated contact details effectively.
- **S2** Add a categorization feature that allows users to tag contacts based on their relevance (e.g., primary contact, secondary contact, etc.).  
  A tagging feature enhances usability by allowing users to categorize contacts by relevance, supporting better project engagement.
- **S3** Provide users with a dashboard view that displays key contacts for each country, showing their assigned roles (validated by an authorized data steward) and the status of their projects. Only regional coordinators and project managers can edit roles, while all users can view them.  
  The dashboard view will assist users in tracking key contacts efficiently while establishing clear editing permissions for authorized personnel. _(C1)_
- **S4** Establish user roles so that only regional coordinators and project managers can edit contact details, while all users can view them. Define access permissions to ensure only authorized roles can view sensitive contact information relevant to their assigned projects or countries.  
  Clear definitions of user roles and permissions prevent unauthorized access to sensitive contact information, ensuring compliance with data protection protocols. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated alerts or reminders for contact updates.  
  Automated alerts for updates are seen as unnecessary at this stage and will not be included in this release.
- **X2** This release will not modify the existing data retention policies; however, it will define the retention period for contact information related to key contacts as a minimum of three years after the last engagement or until such time as the information is deemed irrelevant by an authorized data steward.  
  Retention policies are not being modified; however, clarity around a minimum retention period for sensitive contact information is now established, thus not an immediate concern. _(C6)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will input contact information accurately, which depends on training and guidelines that will be provided separately. | Kept | C2 → escalated |
| A2 | The CRM has the necessary data fields available for contact roles and categorization, which depends on existing CRM capabilities being sufficient for this feature. | Kept | never challenged |
| A3 | User access and permissions are determined by an already established protocol, which depends on compliance with existing data protection regulations. | Kept | C3 → revised |

## Definitions

- **D1** "Key contact" means the individual in a government organization who is identified as the primary resource for communication regarding specific projects or missions.  
  Defining 'key contact' helps users understand the role's importance in project communications, adding clarity to the proposal.
- **D2** "Role" means the designated function or position of the contact within their organization, such as 'Minister', 'Deputy Minister', or 'Project Lead'. Roles must be assigned and validated by an authorized data steward prior to being inputted into the CRM.  
  Clarifying what constitutes a role is essential for ensuring accurate assignment and validating entries by authorized personnel. _(C1)_
- **D3** "Categorization feature" means a system allowing users to categorize contacts as primary, secondary, or other relevant tags for the purpose of prioritizing engagement.  
  A clear categorization feature will allow prioritization of engagement, addressing critical user needs effectively.

## Success criteria

- **K1** Achieve at least 80% accuracy in user-reported contact details within three months of release, measured by comparison against official government websites or directories that are publicly accessible and relevant to the user's assigned role.  
  The success criteria now include specified sources for measuring accuracy, providing a clear evaluation framework for the feature's effectiveness. _(C4)_

## Open questions for humans

### C2 · MAJOR · blocks the build

**What structured process will be put in place to verify the accuracy of user-inputted contact information before it is saved to the CRM?**

- Why it matters: Establishing a verification process is critical to prevent incorrect data entry that could lead to serious diplomatic errors.
- Decision owner: Head of Data Protection
- Options: Implement a review process by authorized personnel / Establish automated benchmarks for data accuracy / Develop user training programs
- Proposer's last word (R2, defend, needs human decision): The assumption that users will input accurate contact information needs a structured process for verification and correction, which requires organizational decisions on establishing such a process.
- Critic's last word (R2, escalate): The proposal does not clarify how the organization will define this process, which is a significant oversight.

## Tension report

The primary disagreement centered on ensuring data quality, particularly the adequacy of verification processes for user-inputted information. While the proposer recognized the importance of accuracy, the critic insisted on the necessity of a structured process, resulting in the need for an open question to be addressed before proceeding.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 35 | - | continue |
| 2 | 6 | 0 | 5 | 1 | 0.15 | 80 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring that all defined processes are adhered to in practice, particularly regarding data quality and user role management.
- Critic's remaining worry (80/100): The lack of a structured process for verifying user-inputted contact information could lead to serious inaccuracies.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | D2, S3 | R1 | REVISED | 0 | The proposal does not specify how role definitions (e.g., 'Minister', 'Project Lead') will be validated and who can access or edit these details, leading to risks of incorrect information reaching unauthorized personnel. |
| C2 | MAJOR | DATA_QUALITY | A1 | R1 | ESCALATED | 0 | The assumption that users will input accurate contact information is too risky unless a structured process for verification and correction is defined. |
| C3 | MAJOR | OWNERSHIP | A3, S1 | R1 | REVISED | 0 | The proposal doesn’t clarify who is responsible for managing changes in user roles and access rights as personnel shifts occur, increasing the risk of outdated records being accessible or editable. |
| C4 | MAJOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The success criteria of achieving 80% accuracy does not define how 'accuracy' will be measured and what sources will be used to determine this. |
| C5 | MAJOR | COMPLIANCE | S4 | R1 | REVISED | 0 | The proposal fails to address the compliance aspects regarding data access levels, particularly who can view sensitive information across different project teams or countries. |
| C6 | MAJOR | OPERATIONS | X2 | R1 | REVISED | 0 | The out-of-scope mention about not modifying existing data retention policies overlooks how long contact information will be stored and maintained, especially given its sensitive nature. |
