# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 3 rounds (policy `naive`) · $0.007.

Challenges: 8 raised · 7 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

A new 'Primary Contacts' feature will be implemented to define and maintain primary contacts for member countries, incorporating safeguards for data protection such as two-factor authentication and a quarterly review process. User functionality will be enhanced with a search capability to locate relevant contacts quickly. However, adherence to the safeguards and processes once implemented requires further consideration from the data protection team, as a specific compliance question remains open.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Establish a user interface to define and modify primary contacts for each member country.
- **V2** Provide a search and filter functionality to enable users to quickly find relevant contacts.

**In scope**

- **S1** Create a 'Primary Contacts' section within the Government CRM for each country, detailing that when a user leaves or changes roles, their contact responsibilities will be reassigned to a designated senior user to maintain the records, and implement a quarterly review process to update and verify contact information.
- **S2** Implement user roles for regional coordinators and project managers with permission to modify contacts, including safeguards such as two-factor authentication for updates, role-based access controls, and audit logs to track changes made to primary contacts, ensuring compliance with data protection regulations.
- **S3** Include essential contact information fields: name, role, email, phone number, organization, and implement a validation system to prevent duplicate entries and flag incorrect information for review.
- **S4** Integrate search functionality to enable users to find contacts by name or country.
- **S5** Develop a notification system to alert designated users, specifically regional coordinators and project managers, when a contact's information has been updated, ensuring that only those with the appropriate access receive notifications.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external databases or third-party applications for contact information.
- **X2** This release will not implement advanced analytics or reporting features related to contact interactions.
- **X3** This release will not cover the historical engagement data of contacts.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users of the Government CRM have the necessary permissions to modify primary contacts as defined in this release. | Kept | never challenged |
| A2 | Contact information being recorded for primary contacts is sensitive and will adhere to existing data protection regulations. | Kept | C6 → escalated; C7 → revised |
| A3 | This feature will rely on a stable user interface design that is consistent with existing CRM components. | Kept | never challenged |

## Definitions

- **D1** "Primary Contact" means the individual designated with explicit approval by the relevant regional coordinator for a specific country within the Government CRM system, and conflicts will be resolved by a defined escalation process involving senior leadership.
- **D2** "User Roles" means the permissions and access levels assigned to individuals within the Government CRM based on their job functions, specifically defined for regional coordinators and project managers.

## Success criteria

- **K1** Achieve at least an 80% user engagement rate with the new Primary Contacts feature within three months of deployment, measured by the number of user interactions with the feature.

## Open questions for humans

### C6 · MAJOR · blocks the build

**What specific actions will be implemented to ensure compliance with data protection regulations while updating primary contacts?**

- Why it matters: Understanding the compliance measures is crucial to prevent data protection violations during record updates.
- Decision owner: Data Protection Officer
- Options: Specify additional safeguards for data protection during updates / Establish regular audits of compliance measures
- Proposer's last word (R2, defend, needs human decision): Ensuring compliance with existing data protection regulations during record updates requires a decision from the organization's data protection team regarding specific measures.
- Critic's last word (R2, escalate): This depends on a human decision from the data protection team to establish specific compliance measures.

## Tension report

The primary tension centered around ensuring compliance with data protection regulations during contact updates. While the Proposer emphasized functionality and user engagement, the Critic raised concerns about the adequacy of the proposed safeguards, resulting in a need for further clarity on compliance measures.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 8 | 2 | 5 | 1 | 0.35 | 85 | 65 | CONTINUE | continue |
| 3 | 8 | 0 | 7 | 1 | 0.12 | 75 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (75/100): Ensuring user adherence to the new safeguards and processes once implemented.
- Critic's remaining worry (85/100): There may still be issues with user role clarity and management of contact updates.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | S2 allows regional coordinators and project managers to modify contacts, but it doesn't specify what safeguards are in place to prevent unauthorized changes by those with insufficient permissions. |
| C2 | MAJOR | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | S5 includes a notification system to alert users when a primary contact is updated, but it doesn't clarify who receives these notifications and whether it can result in sensitive information being shared with the wrong personnel. |
| C3 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The definition of 'Primary Contact' (D1) is too vague; it does not specify who officially determines or approves the designation of primary contacts or how conflicts are resolved. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not outline what happens to primary contacts when users leave or change roles, leaving the management of these records unclear. |
| C5 | MAJOR | DATA_QUALITY | S3 | R1 | REVISED | 0 | S3 does not address how duplicates or incorrect entries are handled, risking the integrity and quality of contact information. |
| C6 | MAJOR | COMPLIANCE | A2 | R1 | ESCALATED | 0 | A2 asserts contact information will adhere to data protection regulations, but does not detail how compliance will be ensured during record updates. |
| C7 | MAJOR | COMPLIANCE | A2 | R2 | REVISED | 0 | The proposal lacks detail on specific compliance measures for data protection during record updates. |
| C8 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | There is no mention of a process for regularly reviewing and updating contact information, which can lead to outdated or incorrect data remaining in the system. |
