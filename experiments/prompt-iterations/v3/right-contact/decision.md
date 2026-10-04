# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.015.

## Summary

This release will implement a contact tracking feature for government counterparts, enabling users to effectively identify and manage primary contacts in ~100 member countries, while ensuring data protection compliance. However, certain aspects, like security measures for sensitive data handling, have not been fully defined, requiring further decisions. Key unresolved issues regarding user permissions, contact management responsibility, and data retention policies need to be addressed before moving forward with implementation.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can efficiently access and manage contact details of the right person to contact in each member country.  
  Users will be able to access and manage contact details effectively through the new feature, aligning with the feature request for improved tracking.
- **V2** The system ensures compliance with data protection standards for sensitive contact information.  
  The system will ensure compliance with data protection standards to safeguard sensitive contact information, a crucial requirement given the nature of the data.

**In scope**

- **S1** Implement a contact management interface that allows users to add, edit, and view contacts for each of the approximately 100 member countries.  
  A contact management interface will be implemented to facilitate the addition, editing, and viewing of contacts, meeting the feature's core needs.
- **S2** Define 'right person' as the primary contact for engagement, who has decision-making authority recognized by the organization's local representatives.  
  The definition of 'right person' was clarified to include decision-making authority and local recognition, addressing inconsistencies for identifying contacts across countries. _(C1)_
- **S3** Add a status field for each contact, indicating whether they are 'active', 'inactive', or 'pending' according to their engagement.  
  A status field will be introduced for contacts, responding to the need for clear engagement tracking in diplomatic relations, despite ownership and process concerns. _(C3)_
- **S4** Include user permissions to restrict access to sensitive information based on user roles, where 'regional coordinators' have full access while 'project managers' have read access only.  
  User permissions will restrict access to sensitive information appropriately, but concerns remain about how these permissions will be enforced consistently. _(C2)_

## What it will not do

**Out of scope for this release**

- **X1** This release does not include integration with external databases for real-time data updates on contacts.  
  Integration with external databases for real-time updates was deemed out of scope as the focus remains on internal contact management and not external data sources.
- **X2** This release does not cover historical engagement data or project affiliations beyond the basic contact information.  
  Historical engagement data and project affiliations were out of scope to maintain a streamlined contact-focused approach, allowing for better initial implementation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users are familiar with the current CRM system and can be trained quickly on the new feature. | The feature is intended for existing users of the system. | Accepted (never challenged) |
| A2 | Sensitive contact data complies with existing data protection regulations applicable to government operations. | The request implies that this feature will handle sensitive information. | Accepted (never challenged) |
| A3 | There is a defined list of roles that users fit into, which determines access levels to sensitive data. | The request assumes users will have varied levels of access based on their roles. | Accepted (never challenged) |
| A4 | The organization has established a retention policy for sensitive contact information, including audit measures to ensure compliance with data protection regulations. | The request assumes that sensitive data management will follow legal guidelines. | Accepted (never challenged) |

## Definitions

- **D1** "right person": The primary contact in each country for either government relations or project engagement, defined as the person responsible for decision-making related to that country.  
  The definition of 'right person' was revised multiple times to add clarity, although ambiguities still exist regarding its application across countries.
- **D2** "active status": Contact is currently engaged and valid for communication regarding projects or government relations.  
  The definition of 'active status' serves to promote clarity in engagement tracking, which is essential for diplomatic communications.
- **D3** "sensitive information": Any data pertaining to diplomatic or confidential contacts that requires restricted access based on user roles.  
  Defining sensitive information ensures that access restrictions are appropriately applied, which is necessary for data protection.

## Success criteria

- **K1** User feedback rating: target At least 80% of users find the new feature useful and intuitive within 3 months of deployment. (Conduct a structured user survey after three months of usage. A valid response is at least 80% rating the feature as useful.)  
  The success criteria were specified to ensure reliable assessment of user feedback, fostering accountability in feature evaluation.

## Open questions for humans

### C2 · BLOCKER · does not block the build

**What are the defined user roles and the specific access levels they have regarding sensitive contact data?**

- Why it matters: Detailing access levels is critical for safeguarding sensitive information and ensuring compliance with data protection standards.
- Decision owner: Data Protection Lead
- Options: Full access for regional coordinators / Read access for project managers / User training on sensitivity handling

### C8 · BLOCKER · does not block the build

**What logging and alert mechanisms will be implemented to monitor access to sensitive contact data?**

- Why it matters: Defined monitoring mechanisms are necessary to safeguard sensitive data from unauthorized access and potential breaches.
- Decision owner: IT Security Officer
- Options: Establish logging protocols / Implement alert systems for unauthorized access / Conduct regular security audits

### C9 · BLOCKER · does not block the build

**What specific security measures will protect sensitive contact data during export or unauthorized access?**

- Why it matters: Defining these measures is crucial for preventing data leaks and ensuring compliance with privacy regulations.
- Decision owner: Data Security Officer
- Options: Develop encryption methods / Set access restrictions during export / Create security protocols for unauthorized access

### C1 · MAJOR · does not block the build

**What specific criteria will be used to define and identify the 'right person' for each country?**

- Why it matters: Clear criteria will help ensure consistent application across different countries and minimize miscommunication.
- Decision owner: Product Team
- Options: Establish specific decision-making authority criteria / Include local representative endorsement / Create a comprehensive guideline for selection

### C3 · MAJOR · does not block the build

**Who will be responsible for updating the status of each contact, and what is the process in place for this?**

- Why it matters: Defining ownership and processes for status updates will prevent outdated or incorrect information, enhancing operational effectiveness.
- Decision owner: Operations Manager
- Options: Assign dedicated personnel for updates / Create a rotating responsibility system / Develop a status update protocol

### C4 · MAJOR · does not block the build

**Who will oversee the contact management process, including updates when roles change?**

- Why it matters: Clear oversight will ensure the contact list remains accurate as personnel changes occur, maintaining diplomatic effectiveness.
- Decision owner: Senior Management
- Options: Designate a specific role for oversight / Implement a shared responsibility approach / Utilize automated systems for updates

### C5 · MAJOR · does not block the build

**What is the established retention policy for sensitive contact information, and how will it be audited for compliance?**

- Why it matters: A defined retention policy is essential to meet legal requirements and protect sensitive information from unnecessary exposure.
- Decision owner: Legal Compliance Officer
- Options: Define specific retention timelines / Create audit measures for compliance / Establish a regular review process

### C6 · MAJOR · does not block the build

**What methods will be used to gather user feedback on the feature, and what constitutes a successful rating?**

- Why it matters: Clear methods for feedback collection will ensure the feature meets user needs effectively, impacting future iterations of the CRM.
- Decision owner: User Experience Manager
- Options: Structured surveys post-deployment / Focus groups with users / Continuous feedback mechanism

### C7 · MAJOR · does not block the build

**Who is responsible for ensuring the accuracy and currency of the contact information as roles change?**

- Why it matters: Defining accountability for updates is essential to maintain correct contact information and avoid operational complications.
- Decision owner: Human Resources Leader
- Options: Designate a role for updates / Incorporate checks into ongoing processes / Use technology solutions to manage changes

## Tension report

The real disagreement centered around the definitions and ownership related to sensitive data handling and contact management processes. The proposer sought to clarify definitions and establish a pathway for implementation, while the critic insisted on more specific, actionable details to ensure compliance and reduce risk. These areas remained unresolved, necessitating additional decisions from relevant stakeholders.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 6 | 0 | 0 | 1.00 | 75 | 50 | CONTINUE | continue |
| 3 | 8 | 4 | 0 | 4 | 1.00 | 60 | 40 | CONTINUE | continue |
| 4 | 9 | 3 | 0 | 6 | 1.00 | 40 | 25 | CONTINUE | continue |
| 5 | 9 | 1 | 0 | 8 | 1.00 | 70 | 20 | CONTINUE | continue |
| 6 | 9 | 0 | 0 | 9 | 1.00 | 60 | 40 | CONTINUE | converged |

- Proposer's remaining worry (60/100): The lack of specific security measures for sensitive data handling may lead to compliance issues.
- Critic's remaining worry (40/100): Without clear security measures, sensitive contact data remains at high risk of exposure.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | DEFINITIONS | S2 | R1 | ESCALATED | 2 | The definition of 'right person' lacks clarity on the criteria for selection and how it will be consistently applied across different countries. |
| C2 | BLOCKER | CONFIDENTIALITY | S4 | R1 | ESCALATED | 2 | The proposal does not specify how user permissions will be structured to ensure sensitive data protection, risking unauthorized access to critical contact information. |
| C3 | MAJOR | OWNERSHIP | S3 | R1 | ESCALATED | 2 | The management of the status field for each contact has no defined ownership or process, which could lead to outdated or incorrect engagement statuses posted, complicating diplomatic relations. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 0 | The proposal does not define who will oversee the overall contact management process, including changes to primary contacts when roles change or individuals leave their position. |
| C5 | MAJOR | COMPLIANCE | GAP | R2 | ESCALATED | 2 | The proposal lacks clarity on how long sensitive contact information will be retained and what audit measures are in place for this data. |
| C6 | MAJOR | DEFINITIONS | GAP | R2 | ESCALATED | 2 | The success criteria do not define how user feedback will be collected or what constitutes a valid response to ensure the feature's perceived usefulness and intuitiveness. |
| C7 | MAJOR | OWNERSHIP | GAP | R3 | ESCALATED | 2 | The proposal does not specify who is responsible for ensuring the accuracy and currency of the contact information as user roles change or contacts leave their positions. |
| C8 | BLOCKER | CONFIDENTIALITY | GAP | R3 | ESCALATED | 2 | The proposal does not specify any logging or alert mechanisms to curb unauthorized access or changes to sensitive contact data. |
| C9 | BLOCKER | CONFIDENTIALITY | GAP | R4 | ESCALATED | 2 | The proposal does not address how sensitive contact data will be protected during data export or when accessed by unauthorized users. |
