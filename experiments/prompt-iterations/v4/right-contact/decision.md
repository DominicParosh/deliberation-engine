# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.011.

## Summary

This release will enhance the CRM by implementing a Contact Management feature to effectively track primary contacts for each member country. It will allow users to add, edit, view contact details, engagement history, and designate specific individuals as primary contacts. However, open questions remain regarding the processes for managing ownership of contacts and handling duplicate information.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to identify and manage primary contacts for each country.  
  The feature enables users to manage primary contacts for each country to streamline communication.
- **V2** Ensure users can view contact details, engagement history, and project affiliations for each primary contact.  
  Users will have access to detailed information regarding each primary contact for better engagement.

**In scope**

- **S1** Users can add new contacts with details including name, title, email, phone number, and country affiliation.  
  Users can add new contacts, ensuring essential details are captured for effective contact management.
- **S2** Users can designate a contact as the primary contact for a specific country, requiring the completion of specified fields.  
  Designating a primary contact for each country enables organized communication and management of diplomatic relationships. _(C1)_
- **S3** Users can edit existing contact information.  
  The ability to edit existing contact information ensures that data remains current and reliable.
- **S4** Users can view a list of contacts with filtering options for each country.  
  This feature will support users in filtering and managing country-specific contacts for efficiency.
- **S5** Users can view engagement history associated with each contact, ensuring it is automatically linked to the designated primary contact.  
  Linking engagement history to contacts will aid in maintaining context for communications. _(C6)_
- **S6** Access to add, edit, and manage contacts will be limited to users with 'Contact Manager' role designation.  
  Access limitations ensure that only authorized personnel can edit sensitive contact data. _(C1)_
- **S7** Users will receive prompts to check for existing contacts before adding new entries to minimize duplicates.  
  User prompts to check for duplicates will help minimize data inaccuracies. _(C4, C7)_
- **S8** Administrative users can review and merge duplicate contacts identified by users or the system, following a defined process for monitoring duplicate contacts.  
  The administrative process for merging duplicates is critical for maintaining data integrity. _(C4, C7)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not implement any automated notifications for changing contacts.
- **X2** This release will not include integration with other systems or external databases.
- **X3** This release will not enforce role-based access control for contact viewing beyond the designated 'Contact Manager' role.
- **X4** This release will not provide extensive training materials for users beyond existing CRM documentation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users have the necessary permissions to manage contacts and their information in the CRM. | The request assumes that users will need access to edit and view contact information. | C2 → escalated |
| A2 | The CRM system contains current and relevant data regarding country representatives and contact details. | The request implies that users need to track contacts accurately. | Accepted (never challenged) |
| A3 | Users are familiar with navigating the CRM interface to add, edit, and view contact information. | The ability to track contacts assumes that users will know how to use the system effectively. | Accepted (never challenged) |
| A4 | There is a defined process for transferring ownership of contact information when users change roles or leave. | This proposal assumes that there is a clear method to manage contacts effectively over changes in personnel. | Accepted (never challenged) |
| A5 | Users will utilize a prescribed set of data points when designating a primary contact. | The designation of a primary contact entails standardization of data entries across users. | Accepted (never challenged) |
| A6 | Users will understand the importance of informing system administrators about changes in primary contact responsibility. | Effective tracking assumes users are proactive about contact management. | Accepted (never challenged) |

## Definitions

- **D1** "better way": A method that simplifies the tracking process for contacts, allowing users to add, edit, view, and designate contacts efficiently with measurable outcomes.  
  The definition now includes measurable indicators for better clarity.
- **D2** "right person to contact": The individual designated as the primary contact for each country, indicated in the system and associated with that country.
- **D3** "measures of better way": Measurable indicators such as user adoption rate, user satisfaction scores, and the percentage of primary contacts correctly designated compared to intended contacts.
- **D4** "primary contact designation data points": The required fields to designate a primary contact, which must include name, title, email, and phone number.  
  Specifying required data points ensures uniformity in designation processes.
- **D5** "engagement history linkage": The process where engagement history is automatically associated with the designated primary contact of a country in the system.  
  Clarification of engagement history linkage assists users in maintaining communication context.
- **D6** "duplicate contact management": The processes including user prompts for duplicates during entry and an administrative review process to merge duplicate contacts.  
  Defining duplicate contact management processes enhances data reliability.
- **D7** "ownership transfer process": The defined method by which responsibility for primary contacts and associated engagement history is passed on when users change roles or leave.  
  Establishing a clear ownership transfer process aims to maintain context when roles change.

## Success criteria

- **K1** Number of primary contacts recorded in the system.: target At least 80% of member countries have a designated primary contact after one month of implementation. (Count of primary contacts logged in the database at the end of the month.)  
  Success criteria focuses on establishing primary contacts across member countries for accountability.

## Open questions for humans

### C2 · MAJOR · blocks the build

**What is the defined process for transferring contact management when users change roles or leave?**

- Why it matters: Without a clear process, there is a risk of loss of responsibility for contact data, leading to potential diplomatic communication issues.
- Decision owner: Head of Data Management
- Options: Develop a standardized process for contact ownership transfer. / Assign a dedicated review team for ownership transitions. / Continue with existing informal practices.

### C4 · MAJOR · blocks the build

**What specific processes will be in place for identifying and managing duplicate or stale contacts in the CRM?**

- Why it matters: Failure to address duplicates could lead to miscommunication and operational inefficiencies.
- Decision owner: Data Quality Manager
- Options: Implement systemic checks for duplicates during contact entry. / Establish periodic review of contacts for duplicates. / Rely on user vigilance and reporting for duplicate management.

### C7 · MAJOR · blocks the build

**What is the specific protocol for monitoring duplicate or stale contact information in the CRM?**

- Why it matters: A well-defined monitoring protocol is essential to maintain data accuracy and prevent confusion.
- Decision owner: Operational Head
- Options: Deploy enhanced monitoring tools for data entry. / Create a user feedback loop for reporting inconsistencies. / Do not implement new protocols and continue current practices.

## Tension report

The primary disagreement centered on the need for a detailed process in managing duplicate and stale contacts, with the Critic emphasizing the necessity of specific guidelines. While the Proposer expressed confidence in the proposed features’ ability to enforce basic duplicate management steps, the Critic remained concerned about the lack of comprehensive detail, leading to unresolved questions that need addressing before development. This tension highlights the critical balance between feature implementation and ensuring data integrity.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 80 | 30 | - | continue |
| 2 | 6 | 3 | 2 | 1 | 0.62 | 80 | 60 | CONTINUE | continue |
| 3 | 8 | 2 | 4 | 2 | 0.47 | 85 | 60 | CONTINUE | continue |
| 4 | 8 | 1 | 5 | 2 | 0.35 | 85 | 80 | CONTINUE | continue |
| 5 | 8 | 0 | 5 | 3 | 0.35 | 75 | 60 | CONTINUE | converged |

- Proposer's remaining worry (75/100): Ensuring users consistently follow through on prompting for duplicates and that the administrative process for merging is effectively carried out.
- Critic's remaining worry (60/100): The proposal still lacks a detailed and specific process for managing duplicate or stale contact information in the CRM.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | The proposal does not clarify who can see and modify the primary contacts for each country. |
| C2 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | The proposal fails to address what happens to contact information when users leave or change roles, risking loss of data ownership and responsibility. |
| C3 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'better way' is vague and unbounded, making it difficult to measure the success of the feature. |
| C4 | MAJOR | DATA_QUALITY | GAP | R2 | ESCALATED | 0 | The proposal does not address how the system will handle duplicates or stale contact information, risking inaccuracies and confusion during operational use. |
| C5 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal does not specify what specific data points are required to designate a primary contact, which could lead to inconsistencies in data entry. |
| C6 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | There is no mention of how the engagement history will be linked to primary contacts, which is crucial for maintaining context in diplomatic communications. |
| C7 | MAJOR | DATA_QUALITY | GAP | R3 | ESCALATED | 1 | The proposal does not define the specific process for monitoring and managing duplicate or stale contact information in the CRM. |
| C8 | MAJOR | OWNERSHIP | GAP | R3 | REVISED | 0 | There is no defined process for data ownership transfer for primary contacts when users leave or change roles, risking a loss of context and management responsibility. |
