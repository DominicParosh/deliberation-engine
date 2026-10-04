# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `naive` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 3 rounds · 8 model calls (1 repairs)

## Round 1

### Proposer · confidence 75

_This release will introduce a 'Primary Contacts' feature that allows users to identify and maintain up-to-date records of the appropriate contact person for each member country. The feature will enable regional coordinators and project managers to efficiently manage and retrieve contact information tailored to their engagement needs._

**Core commitments**
- V1: Establish a user interface to define and modify primary contacts for each member country.
- V2: Provide a search and filter functionality to enable users to quickly find relevant contacts.

**In scope**
- S1: Create a 'Primary Contacts' section within the Government CRM for each country, allowing designated users to input and update contact details.
- S2: Implement user roles for regional coordinators and project managers with permission to modify contacts.
- S3: Include essential contact information fields: name, role, email, phone number, and organization.
- S4: Integrate search functionality to enable users to find contacts by name or country.
- S5: Develop a notification system to alert users when a contact's information has been updated.

**Out of scope**
- X1: This release will not include integration with external databases or third-party applications for contact information.
- X2: This release will not implement advanced analytics or reporting features related to contact interactions.
- X3: This release will not cover the historical engagement data of contacts.

**Assumptions**
- A1: Users of the Government CRM have the necessary permissions to modify primary contacts as defined in this release.
- A2: Contact information being recorded for primary contacts is sensitive and will adhere to existing data protection regulations.
- A3: This feature will rely on a stable user interface design that is consistent with existing CRM components.

**Definitions**
- D1: "Primary Contact" means the individual designated as the primary point of contact for a specific country within the Government CRM system.
- D2: "User Roles" means the permissions and access levels assigned to individuals within the Government CRM based on their job functions, specifically defined for regional coordinators and project managers.

**Success criteria**
- K1: Achieve at least an 80% user engagement rate with the new Primary Contacts feature within three months of deployment, measured by the number of user interactions with the feature.

Biggest worry: Ensuring that the sensitive data of primary contacts is adequately protected and complies with data protection regulations.

### Critic · confidence 40

Pre-mortem: A year after launch, the 'Primary Contacts' feature causes a serious incident when an email meant for a sensitive diplomatic contact is inadvertently sent to the wrong person. This happens because the system lacks adequate permissions, allowing someone with a lower role to access and modify the primary contacts. As a result, this contact information is incorrectly altered, leading to a breach of confidentiality and requiring an internal investigation.

Questions the request leaves open:
- Who can always modify primary contacts and what prevents unauthorized changes?
- What safeguards are in place to ensure only the correct person receives notifications about updates to primary contacts?
- How will the system prevent duplicates or incorrect entries for primary contacts?
- What will happen to the records of primary contacts when a regional coordinator or project manager leaves the organization?
- How will the system handle changes in roles for users to ensure appropriate permissions for modifications?
- What measures are in place to ensure compliance with data protection regulations during the updates?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S2
- Challenge: S2 allows regional coordinators and project managers to modify contacts, but it doesn't specify what safeguards are in place to prevent unauthorized changes by those with insufficient permissions.
- Failure scenario: An unauthorized user with a lower access level modifies a primary contact's details, leading to sensitive information being sent to the wrong person.
- Resolution test: What specific user roles and permissions are required to modify primary contacts, and what safeguards prevent unauthorized changes?

**C2** · MAJOR · CONFIDENTIALITY · targets S5
- Challenge: S5 includes a notification system to alert users when a primary contact is updated, but it doesn't clarify who receives these notifications and whether it can result in sensitive information being shared with the wrong personnel.
- Failure scenario: An unwanted recipient receives an alert that a sensitive contact's details were changed, raising security concerns about information leakage.
- Resolution test: Who receives notifications when primary contacts are updated, and what criteria determine this?

**C3** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The definition of 'Primary Contact' (D1) is too vague; it does not specify who officially determines or approves the designation of primary contacts or how conflicts are resolved.
- Failure scenario: Two users independently designate different individuals as the primary contact for the same country, leading to confusion and inconsistent communications.
- Resolution test: Who is responsible for determining and approving the primary contact for each country, and how is this process managed?

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not outline what happens to primary contacts when users leave or change roles, leaving the management of these records unclear.
- Failure scenario: When a project manager leaves, there is no clear authority on who assumes the responsibility for updating and maintaining the primary contacts, leading to a lapse in communication.
- Resolution test: What process is in place to transfer ownership of primary contacts when users change roles or leave the organization, and who is responsible for it?

**C5** · MAJOR · DATA_QUALITY · targets S3
- Challenge: S3 does not address how duplicates or incorrect entries are handled, risking the integrity and quality of contact information.
- Failure scenario: A user enters duplicate contact records for the same individual, resulting in communication errors and confusion among project teams.
- Resolution test: What measures do you have in place to prevent duplicate entries and ensure the accuracy of primary contact information?

**C6** · MAJOR · COMPLIANCE · targets A2
- Challenge: A2 asserts contact information will adhere to data protection regulations, but does not detail how compliance will be ensured during record updates.
- Failure scenario: During contact updates, insufficient safeguarding leads to unauthorized access to sensitive personal data, resulting in a data protection violation.
- Resolution test: What specific actions will be implemented to ensure compliance with data protection regulations while updating primary contacts?

Biggest worry: The proposal lacks critical safeguards and definitions regarding permissions and updates, risking data integrity and confidentiality.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S2]: The edits specify safeguards, such as role-based access controls and audit logs, ensuring that only authorized users can modify contact details.
- **C2** REVISE (missing decision) [changed S5]: This provides clarity on who receives notifications, focusing only on users with the appropriate roles, thus preventing unauthorized access to sensitive information.
- **C3** REVISE (missing decision) [changed D1]: The definition is made specific to include the approval process and escalation for conflicts, ensuring clarity around the designation of primary contacts.
- **C4** REVISE (missing decision) [changed S1]: This outlines the process for transferring contact responsibilities, addressing management continuity when users change roles.
- **C5** REVISE (missing decision) [changed S3]: This update establishes a system to ensure data integrity and manages duplicates, enhancing the overall quality of contact information.
- **C6** DEFEND (needs human decision): Ensuring compliance with existing data protection regulations during record updates requires a decision from the organization's data protection team regarding specific measures.

Proposal changes: edited S1, S2, S3, S5, D1
- S1 now reads: Create a 'Primary Contacts' section within the Government CRM for each country, detailing that when a user leaves or changes roles, their contact responsibilities will be reassigned to a designated senior user to maintain the records.
- S2 now reads: Implement user roles for regional coordinators and project managers with permission to modify contacts, including safeguards such as role-based access controls and audit logs to track changes made to primary contacts.
- S3 now reads: Include essential contact information fields: name, role, email, phone number, organization, and implement a validation system to prevent duplicate entries and flag incorrect information for review.
- S5 now reads: Develop a notification system to alert designated users, specifically regional coordinators and project managers, when a contact's information has been updated, ensuring that only those with the appropriate access receive notifications.
- D1 now reads: "Primary Contact" means the individual designated with explicit approval by the relevant regional coordinator for a specific country within the Government CRM system, and conflicts will be resolved by a defined escalation process involving senior leadership.

Biggest worry: The complexity of roles and permissions may lead to confusion among users regarding who can modify contact information.

### Critic · confidence 65 · CONTINUE

Rulings:
- **C1** ACCEPT: This adequately specifies the safeguards preventing unauthorized changes. Fact: Role-based access controls and audit logs for modifying contacts are in place. Evidence: "S2: Implement user roles for regional coordinators and project managers with permission to modify contacts, including safeguards such as role-based access controls and audit logs to track changes made to primary contacts."
- **C2** ACCEPT: This clearly defines who receives notifications, addressing the concern of unauthorized access. Fact: Notifications will be sent only to authorized users, specifically regional coordinators and project managers. Evidence: "S5: Develop a notification system to alert designated users, specifically regional coordinators and project managers, when a contact's information has been updated, ensuring that only those with the appropriate access receive notifications."
- **C3** ACCEPT: This clarifies both the determination process and conflict resolution. Fact: The approval of primary contacts is done explicitly by the relevant regional coordinator with a defined escalation process for conflicts. Evidence: "D1: 'Primary Contact' means the individual designated with explicit approval by the relevant regional coordinator for a specific country within the Government CRM system, and conflicts will be resolved by a defined escalation process involving senior leadership."
- **C4** ACCEPT: This provides a clear ownership transfer process. Fact: Contact responsibilities will transfer to a designated senior user when someone leaves or changes roles. Evidence: "S1: Create a 'Primary Contacts' section within the Government CRM for each country, detailing that when a user leaves or changes roles, their contact responsibilities will be reassigned to a designated senior user to maintain the records."
- **C5** ACCEPT: This addresses data integrity and the quality of entries. Fact: A validation system will be in place to prevent duplicate entries and flag incorrect information for review. Evidence: "S3: Include essential contact information fields: name, role, email, phone number, organization, and implement a validation system to prevent duplicate entries and flag incorrect information for review."
- **C6** ESCALATE: This depends on a human decision from the data protection team to establish specific compliance measures.

New challenges:

**C7** · MAJOR · COMPLIANCE · targets A2
- Challenge: The proposal lacks detail on specific compliance measures for data protection during record updates.
- Failure scenario: A project manager updates sensitive contact information without adequate safeguards in place, leading to unauthorized access and a breach of confidentiality.
- Resolution test: What specific safeguards will ensure compliance with data protection regulations during updates to primary contact information?

**C8** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: There is no mention of a process for regularly reviewing and updating contact information, which can lead to outdated or incorrect data remaining in the system.
- Failure scenario: Over time, outdated contact information remains uncorrected, leading to failed communications and loss of trust with diplomatic contacts.
- Resolution test: What process will be implemented to regularly review and update primary contact information to maintain accuracy?

Biggest worry: Overall compliance with data protection regulations is still reliant on human decisions, which increases risk.

**Ledger:** raised 8 · open 2 · resolved 5 · escalated 1 · disagreement 0.35 → **continue**

## Round 3

### Proposer · confidence 75

- **C7** REVISE (missing decision) [changed S2]: The edits specify two-factor authentication for updates as a safeguard to ensure compliance with data protection regulations when sensitive information is modified.
- **C8** REVISE (missing decision) [changed S1]: The edits introduce a quarterly review process for primary contact information, which will help maintain accuracy and prevent outdated data from remaining in the system.

Proposal changes: edited S1, S2
- S1 now reads: Create a 'Primary Contacts' section within the Government CRM for each country, detailing that when a user leaves or changes roles, their contact responsibilities will be reassigned to a designated senior user to maintain the records, and implement a quarterly review process to update and verify contact information.
- S2 now reads: Implement user roles for regional coordinators and project managers with permission to modify contacts, including safeguards such as two-factor authentication for updates, role-based access controls, and audit logs to track changes made to primary contacts, ensuring compliance with data protection regulations.

Biggest worry: Ensuring user adherence to the new safeguards and processes once implemented.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C7** ACCEPT: The safeguards now specified adequately address the compliance concerns surrounding record updates. Fact: two-factor authentication and role-based access controls are safeguards for compliance. Evidence: "safeguards such as two-factor authentication for updates, role-based access controls, and audit logs to track changes made to primary contacts, ensuring compliance with data protection regulations."
- **C8** ACCEPT: The quarterly review process satisfies the need for regular updates to contact information. Fact: a quarterly review process is established for maintaining contact accuracy. Evidence: "implement a quarterly review process to update and verify contact information."

Biggest worry: There may still be issues with user role clarity and management of contact updates.

**Ledger:** raised 8 · open 0 · resolved 7 · escalated 1 · disagreement 0.12 → **consensus**

## Final proposal

_This release will establish a 'Primary Contacts' feature to define and maintain records of appropriate contact persons for each member country with added safeguards for data protection, including two-factor authentication and a quarterly review process for data accuracy. It will enhance user functionality with search capabilities while ensuring sensitive information is managed properly through appropriate roles and notifications._

**Core commitments**
- V1: Establish a user interface to define and modify primary contacts for each member country.
- V2: Provide a search and filter functionality to enable users to quickly find relevant contacts.

**In scope**
- S1: Create a 'Primary Contacts' section within the Government CRM for each country, detailing that when a user leaves or changes roles, their contact responsibilities will be reassigned to a designated senior user to maintain the records, and implement a quarterly review process to update and verify contact information.
- S2: Implement user roles for regional coordinators and project managers with permission to modify contacts, including safeguards such as two-factor authentication for updates, role-based access controls, and audit logs to track changes made to primary contacts, ensuring compliance with data protection regulations.
- S3: Include essential contact information fields: name, role, email, phone number, organization, and implement a validation system to prevent duplicate entries and flag incorrect information for review.
- S4: Integrate search functionality to enable users to find contacts by name or country.
- S5: Develop a notification system to alert designated users, specifically regional coordinators and project managers, when a contact's information has been updated, ensuring that only those with the appropriate access receive notifications.

**Out of scope**
- X1: This release will not include integration with external databases or third-party applications for contact information.
- X2: This release will not implement advanced analytics or reporting features related to contact interactions.
- X3: This release will not cover the historical engagement data of contacts.

**Assumptions**
- A1: Users of the Government CRM have the necessary permissions to modify primary contacts as defined in this release.
- A2: Contact information being recorded for primary contacts is sensitive and will adhere to existing data protection regulations.
- A3: This feature will rely on a stable user interface design that is consistent with existing CRM components.

**Definitions**
- D1: "Primary Contact" means the individual designated with explicit approval by the relevant regional coordinator for a specific country within the Government CRM system, and conflicts will be resolved by a defined escalation process involving senior leadership.
- D2: "User Roles" means the permissions and access levels assigned to individuals within the Government CRM based on their job functions, specifically defined for regional coordinators and project managers.

**Success criteria**
- K1: Achieve at least an 80% user engagement rate with the new Primary Contacts feature within three months of deployment, measured by the number of user interactions with the feature.
