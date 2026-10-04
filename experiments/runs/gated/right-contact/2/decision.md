# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.012.

Challenges: 10 raised · 6 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

This release will improve the tracking and management of primary contact persons for each member country, providing defined roles and protections for sensitive information while implementing notifications for regular reviews and updates to maintain data accuracy, and process continuity when contacts change. Core functionalities include creating a 'Country Contacts' section with mandatory data fields and access controls to manage sensitive information. Key questions remain regarding ownership and diligence in updating contact records.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to track and manage primary contact persons for each country.  
  This commitment to enable tracking and management of primary contacts is essential to improve operational communication with government counterparts.
- **V2** Provide an intuitive interface for users to update and view contact information easily.

**In scope**

- **S1** Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries. Users must provide mandatory fields for name and organization to ensure data accuracy, and a notification system will remind users at least every six months to review and confirm the accuracy of contact information. If a primary contact changes, an automated workflow will assign a current user to review and update the contact record within two weeks of being notified of the change. Additionally, an automatic email notification will be sent to users when any changes are made to contact records, ensuring they are informed and up-to-date. Validation rules will check for correct formatting of email and phone number fields.
- **S2** Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view. Sensitive diplomatic contact records will only be editable by regional coordinators and designated project managers who have received additional authorization. All sensitive records will also be subject to audit logging to track any access or modifications made, and sensitive data will be encrypted at rest and in transit to prevent unauthorized access.
- **S3** Allow users to filter and search for country contacts by country name, contact name, and organization.
- **S4** Set up a version history for contact records to track changes made by users, ensuring data integrity.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any integration with external databases or API connections to pull in contact information.
- **X2** Advanced user analytics or reporting features based on contact data are not included in this release.
- **X3** Any functionality related to automatic alerts or notifications regarding contact updates is excluded from this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have access to the Government CRM with appropriate role-based permissions, which affects how and what they can view and edit. | Kept | never challenged |
| A2 | Existing contact information is currently stored in the CRM or accessible in a manner that allows users to accurately populate the new 'Country Contacts' section. | Kept | never challenged |
| A3 | Users are familiar with using CRM systems, thus enabling faster adoption of the new features. | Kept | never challenged |
| A4 | Sensitive diplomatic contact records are defined as those contacts involving classified engagements, communications with embassies, or individuals who require a higher level of access due to confidentiality. Records falling under this definition will include those flagged by the organization's policies. | Kept | C4 → escalated |

## Definitions

- **D1** 'Primary contact person' means the individual identified as the main point of contact for each government organization in a country, responsible for all communications and engagements.
- **D2** 'Intuitive interface' means a user-friendly design that allows individuals to navigate, input, and retrieve information easily without extensive training.
- **D3** 'User roles' means defined access levels within the CRM, indicating who can view, edit, or manage contact information. Authorized users who can edit contact records include regional coordinators and specific project managers based on defined criteria.

## Success criteria

- **K1** By the end of Q1, at least 80% of users report improved satisfaction with contact tracking capabilities through a user survey.
- **K2** At least 95% of primary contact records are accurately filled within the first month of release, as verified by user input.

## Open questions for humans

### C2 · MAJOR · blocks the build

**Who will be responsible for ensuring contact records are maintained and updated when primary contacts change?**

- Why it matters: Understanding ownership of record updates is crucial to prevent outdated information.
- Decision owner: Project Manager
- Options: Define a specific role for updates / Leave it to user diligence / Implement an automated tracking system
- Proposer's last word (R3, defend, acceptable risk): While the absence of an automated process for updating contact records does create some risk, we believe that manual updates will rely on users' diligence and the training they receive. Regular training sessions will be scheduled to ensure users understand the importance of keeping contact details current.
- Critic's last word (R3, maintain): The existing process of manual updates increases the risk of outdated information leading to ineffective communication.

### C4 · MAJOR · blocks the build

**What specific roles are considered 'designated project managers' for sensitive records, and how will they be determined?**

- Why it matters: Clarifying roles will help protect sensitive information effectively while ensuring proper management and oversight.
- Decision owner: Head of Data Protection
- Options: Define a list of authorized project managers / Implement a training program to certify managers / Create a review process for authorization
- Proposer's last word (R3, revise, missing decision): The revised assumption clarifies what constitutes sensitive diplomatic contact records, and the edits to S2 specify which roles are authorized to manage such records, thereby minimizing ambiguity around confidentiality.
- Critic's last word (R3, maintain): While user roles are defined, it remains unclear who qualifies as a 'designated project manager' and the process for determining this.

### C7 · MAJOR · blocks the build

**What additional mechanisms can be introduced to ensure contact records are reviewed and updated regularly?**

- Why it matters: Maintaining accurate contact information is vital for effective communication, and regular review processes can mitigate risks.
- Decision owner: Project Manager
- Options: Automated reminders for users / Mandatory quarterly reviews / User-led review sessions
- Proposer's last word (R4, defend, acceptable risk): While the concern over manual updates is valid, the notification system will still enforce accountability. Regular reviews will encourage users to maintain the accuracy of the records, thus balancing the risk of inaccuracies.
- Critic's last word (R4, maintain): While the notification system seeks to mitigate inaccuracies, it still places the onus on users to take action, leaving room for potential lapses in updates.

### C5 · MINOR · does not block the build

**What formal processes should be established to notify users when contact records are updated?**

- Why it matters: Clear notification processes are essential to maintain effective communication and operations across teams.
- Decision owner: Operations Manager
- Options: Define standard communication protocols / Use email alerts for updates / Regular team meetings to discuss updates
- Proposer's last word (R2, defend, needs human decision): The process for notification of changes to contact records must be defined by organizational policies or determined by existing operational practices, which should be clarified beyond this scope.
- Critic's last word (R2, escalate): This relies on outside rules or decisions that are not specified.

## Tension report

The primary disagreement centered around the management of sensitive contact records and user responsibilities for maintaining data accuracy. While the Proposer leaned towards user diligence for updates, the Critic expressed concerns about potential risks without a structured process, leading to ongoing debates over ownership and updates.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 85 | 50 | - | continue |
| 2 | 7 | 3 | 3 | 1 | 0.54 | 85 | 70 | CONTINUE | continue |
| 3 | 9 | 3 | 3 | 3 | 0.67 | 80 | 50 | CONTINUE | continue |
| 4 | 10 | 1 | 5 | 4 | 0.48 | 85 | 70 | CONTINUE | continue |
| 5 | 10 | 0 | 6 | 4 | 0.33 | 85 | 70 | CONTINUE | converged |

- Proposer's remaining worry (85/100): Ensuring timely updates of contact information remains a challenge without user diligence.
- Critic's remaining worry (70/100): There are still unresolved challenges regarding the protection of sensitive data and differences in treatment between sensitive and non-sensitive records.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | S2 allows project managers to view and edit contact records, but does not clarify how sensitive records are protected against unauthorized access. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | ESCALATED | 2 | The proposal does not address how contact records are managed when a primary contact changes, potentially leading to outdated or incorrect information being used. |
| C3 | MAJOR | DATA_QUALITY | S1 | R1 | REVISED | 0 | S1 does not specify how data accuracy and integrity will be ensured in the new 'Country Contacts' section, risking outdated or incorrect records being stored. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R1 | ESCALATED | 2 | The proposal fails to define how sensitive diplomatic information will be treated differently from non-sensitive contact information. |
| C5 | MINOR | OPERATIONS | GAP | R1 | ESCALATED | 0 | The proposal does not specify how users will be notified of changes to contact records, which is essential for maintaining operational effectiveness across teams. |
| C6 | MINOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The definitions provided in the proposal do not clarify who is considered authorized to manage contact records, leading to potential overreach or misuse of access. |
| C7 | MAJOR | DATA_QUALITY | GAP | R2 | ESCALATED | 2 | The manual updating of contact records could lead to inaccuracies over time, especially if users neglect their duty to update them. |
| C8 | MAJOR | OPERATIONS | GAP | R3 | REVISED | 0 | The proposal does not specify how users will be notified about changes to contact records. |
| C9 | BLOCKER | CONFIDENTIALITY | S2 | R3 | REVISED | 0 | S2 does not clarify how sensitive records are protected against unauthorized access, which could lead to a security breach. |
| C10 | BLOCKER | OWNERSHIP | GAP | R4 | REVISED | 0 | The proposal does not clarify how contact records will be managed when a primary contact changes, leaving process gaps regarding ownership and continuity of information. |
