# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.012.

## Summary

This release will introduce a new contact management feature for tracking primary contacts in each member country, primarily for regional coordinators and project managers. The implementation excludes historical engagement tracking and user permissions for editing contact information. Remaining unresolved questions about the supervisor approval process for assigning primary contacts need to be addressed.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide a user interface for assigning and managing primary contacts in the Government CRM system.  
  A user interface for managing primary contacts will enhance usability and facilitate contact assignments.
- **V2** Enable search functionality to easily identify and contact the primary person for engagements in each country.  
  The new search functionality allows for efficient identification of primary contacts, addressing user needs.

**In scope**

- **S1** Add a 'Primary Contact' field to the country contact records in the CRM, allowing users to designate a specific individual as the primary contact, with a specified process for assigning and updating primary contacts, which includes the responsibility of regional coordinators.  
  The addition of a 'Primary Contact' field will allow for explicit designation, ensuring clearer communication. _(C2)_
- **S2** Create a user interface for regional coordinators and project managers to view and assign primary contacts for each member country, with clearly defined roles for who is authorized to edit contact information and a conflict resolution protocol to manage simultaneous edits.  
  Creating a user interface for assigning contacts ensures clarity on roles and protocols in contact assignment. _(C3)_
- **S3** Implement search functionality that allows users to find primary contacts by country name, contact name, and engagement history, with safeguards in place to ensure that only authorized users can access sensitive information related to primary contacts, as determined by their user role.  
  The search functionality now includes controls that safeguard sensitive information, mitigating confidentiality risks. _(C1)_
- **S4** Ensure data entry validations are in place to maintain the integrity of contact information, including mandatory fields for primary contacts.  
  Data entry validations will maintain contact information integrity through mandatory fields.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include historical engagement tracking by primary contact; it will only focus on current primary contacts.  
  Historical engagement tracking has been excluded as it does not align with the immediate focus of managing current contacts.
- **X2** No integration with external systems or databases will be included in this release.  
  Integration with external systems is out of scope for this release to prioritize core features.
- **X3** This release will not address user permissions or access control for editing contact information, but a plan for such controls will be developed in subsequent releases.  
  No user permissions for editing contact information will be resolved in future releases rather than being included in this one. _(C6)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have the necessary roles, including 'Regional Coordinator' and 'Project Manager', to manage and assign primary contacts. Approval from their immediate supervisor is required to designate a primary contact only if the supervisor is currently managing an active project in that country and has confirmed that the individual being proposed has direct involvement and qualifications related to diplomatic or project-related matters within that country. | Kept | C5 → escalated; C7 → escalated |
| A2 | There is an existing database structure in the Government CRM that allows for the addition of new fields without major overhaul, enabling the 'Primary Contact' feature. | Kept | never challenged |
| A3 | Users will require training or guidance materials on managing primary contacts within the CRM, which means support will be available post-release. | Kept | never challenged |

## Definitions

- **D1** The term 'Primary Contact' means the designated individual in each member country identified as the first point of contact for any engagements or communication, and must meet the qualification criteria of having direct involvement in diplomatic or project-related matters within that country.  
  The definition of 'Primary Contact' now specifies necessary qualifications to ensure appropriate assignments. _(C4)_
- **D2** 'Search Functionality' means the capacity for users to query and retrieve specific records from the CRM based on criteria such as country name or contact name.  
  The definition of 'Search Functionality' provides clarity on record retrieval capabilities.

## Success criteria

- **K1** At least 70% of regional coordinators and project managers report being satisfied with the ease of assigning or finding primary contacts, measured through a post-release survey conducted 30 days after the release.  
  Satisfaction measurement through post-release surveys is a targeted outcome for evaluating the feature.

## Open questions for humans

### C7 · BLOCKER · blocks the build

**What specific qualifications should supervisors assess when approving primary contact assignments?**

- Why it matters: Clear qualifications will reduce the risk of improper contacts being assigned, enhancing diplomatic relations.
- Decision owner: Head of Data Protection
- Options: Specify qualifications / Add contextual criteria for approval

### C5 · MINOR · blocks the build

**What specific criteria must users meet for supervisor approval of primary contacts?**

- Why it matters: Clarifying this will prevent delays in the assignment of primary contacts due to ambiguity.
- Decision owner: Head of Data Protection
- Options: Define specific qualifications for supervisors / Implement a training program for supervisors

## Tension report

The primary disagreement revolved around the clarity required for the supervisor approval process associated with assigning primary contacts. While the proposer revised assumptions to add some clarity, the critic maintained that it still lacks specificity, leading to unresolved questions that require human decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 6 | 1 | 5 | 0 | 0.09 | 80 | 75 | CONTINUE | continue |
| 3 | 7 | 1 | 5 | 1 | 0.29 | 85 | 80 | CONTINUE | continue |
| 4 | 7 | 1 | 5 | 1 | 0.29 | 85 | 75 | CONTINUE | continue |
| 5 | 7 | 0 | 5 | 2 | 0.29 | 75 | 50 | CONTINUE | converged |

- Proposer's remaining worry (75/100): The clarity provided in supervisor approval conditions may still lead to inconsistencies in contact assignment if not properly followed.
- Critic's remaining worry (50/100): The approval process for assigning primary contacts remains vague and could lead to mismanagement.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | S3 does not specify how the search functionality will safeguard sensitive information, risking exposure of confidential diplomatic records. |
| C2 | MAJOR | OWNERSHIP | S1, X3 | R1 | REVISED | 0 | S1 and X3 do not clarify who is responsible for maintaining the integrity of primary contact information and under what circumstances these roles can change. |
| C3 | MAJOR | CONFIDENTIALITY | S2, X3 | R1 | REVISED | 0 | S2 lacks clarity on access control for editing contact information, which can lead to multiple users assigning conflicting primary contacts. |
| C4 | MINOR | DEFINITIONS | D1 | R1 | REVISED | 0 | D1 is vague about the qualifications necessary for someone to be designated as a 'Primary Contact', potentially leading to confusion or inconsistency. |
| C5 | MINOR | OPERATIONS | A1 | R1 | ESCALATED | 2 | A1 assumes users will have the necessary roles, but doesn't specify the required credentials or approval process, which could create operational delays. |
| C6 | MAJOR | OWNERSHIP | X3 | R1 | CONCEDED | 0 | X3 explicitly states there's no plan to address user permissions for editing and managing contact information, which is critical for data integrity. |
| C7 | BLOCKER | OWNERSHIP | A1 | R3 | ESCALATED | 2 | A1 requires users to gain approval from their supervisor but does not specify the conditions for approval or who can provide it. This uncertainty can lead to improper management of primary contacts. |
