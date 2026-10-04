# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 4 rounds (policy `gated`) · $0.014.

## Summary

This release will create a streamlined interface for tracking key contacts in member countries, with defined protocols for compliance and governance. It will not include external CRM integration or historical data tracking. Questions remain concerning the specific responsibilities of the designated governance team and how compliance with data protection regulations will be maintained.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can identify the primary contact person for each country, including their roles and affiliations.  
  This commitment was accepted as it allows users to easily identify critical contacts for engagement.
- **V2** Users can add, edit, and view contact details associated with each country.  
  This commitment allows for contact details to be managed effectively, facilitating user engagement with government entities.

**In scope**

- **S1** The system will include a detailed contact management feature for up to 100 member countries, allowing users to view contact names, titles, ministry affiliations, and email addresses. Access to sensitive contact information for high-level government officials will be restricted to authorized regional coordinators and project managers with appropriate clearances as defined in the organization's access control policy.  
  The details about who may view and edit sensitive contacts were specifically defined to mitigate unauthorized access risks. _(C1)_
- **S2** Regional coordinators and project managers will have access to add and edit contact information, including identifying fields for primary and secondary contacts. Only users with the role of 'Regional Coordinator' or 'Project Manager' who have undergone data protection training will be allowed to edit sensitive contact information.  
  Access rights for editing sensitive contact details were clarified to ensure only authorized personnel can make changes, addressing confidentiality concerns. _(C1)_
- **S3** The system will include validation rules for contact email formats and mandatory fields when adding or editing contact information.  
  Validation rules were introduced to ensure contact information meets specific requirements, enhancing data integrity.
- **S4** The system will include a search function enabling users to query contacts by country, name, or ministry.  
  The search functionality was included to improve user experience when locating contacts by various criteria.
- **S5** The system will log changes made to contact details, including who made the change and when it occurred. Additionally, user access rights will be revoked automatically when a user changes roles or is removed from the organization as part of the user management protocol.  
  A system for revoking access was established to prevent unauthorized access when users change roles or leave, addressing continual confidentiality. _(C4)_
- **S6** The system will implement a process for identifying and managing duplicate contact entries, including regular data quality audits and user confirmation steps during data entry to minimize inaccuracies.  
  Processes for managing duplicate entries were defined to enhance data quality and trust in the system. _(C6)_
- **S7** The system will implement a continuity plan for governance responsibilities, ensuring that if key personnel change or the governance team disbands, a new governance team is appointed immediately from a designated pool of trained individuals. This plan will also include a process for transferring and reviewing contact entries, ensuring consistent data integrity.  
  A governance continuity plan was added to ensure data integrity is maintained despite personnel changes, thus addressing potential governance gaps. _(C8)_
- **S8** The system will establish a compliance review protocol whereby any new contact data is reviewed by the governance team to ensure compliance with data protection regulations before it is finalized in the system. Additionally, periodic audits will be conducted to confirm ongoing compliance with all governing policies.  
  A compliance review protocol was established to ensure that new contact data adheres to data protection laws prior to entry, addressing compliance concerns. _(C9)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external databases or CRM systems for automatically updating contact information.  
  Integration with external databases was dropped to maintain system focus and security, avoiding complexity in data management.
- **X2** This release will not implement notifications or alerts regarding changes to contact information.  
  Notifications regarding changes to contact information were out of scope to streamline immediate development needs without excess features.
- **X3** This release will not focus on historical engagement tracking; it will only handle current contacts.  
  Historical engagement tracking was deemed unnecessary for the current release to maintain focus on current contacts only.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have basic training and familiarity with the CRM system; this is necessary for them to utilize the new contact management features effectively. | Kept | never challenged |
| A2 | All contact details provided are compliant with relevant data protection regulations; the success of tracking contacts depends on having accurate and lawful contact data. | Kept | never challenged |
| A3 | There will be a designated team responsible for data governance; this is essential for maintaining the integrity of contact information in the system. | Kept | C3 → escalated; C7 → escalated |

## Definitions

- **D1** 'Contact person' means an individual representative from the government of a member country, along with their title, ministry affiliation, and contact information. A contact person must be an officially designated representative, holding a relevant title within their government.  
  Definitions for contact person and key contact were clarified to prevent inconsistencies in data entries. _(C2)_
- **D2** 'Key contact' means the primary person identified for engagement within a country, who is the first point of contact for communications and decisions. A key contact must be the official responsible for the area of engagement relevant to the organization's objectives, determined by title and office.  
  The definition of key contact was refined to specify criteria, ensuring clarity across user understanding and implementation. _(C2)_

## Success criteria

- **K1** At least 80% of users can identify the correct primary contact for each country within 3 clicks in the system, measured through user feedback surveys after implementation.  
  The success criterion was established to gauge user identification of key contacts, ensuring system effectiveness through feedback.

## Open questions for humans

### C3 · MAJOR · blocks the build

**What specific responsibilities does the designated governance team hold regarding data accuracy?**

- Why it matters: Defining clear responsibilities is essential to maintain data integrity and trust in the contact management system.
- Decision owner: Governance Team Lead
- Options: Define roles and responsibilities internally / Draft a policy to clarify responsibilities

### C5 · MAJOR · blocks the build

**What processes will ensure compliance with data protection regulations for newly added contact information?**

- Why it matters: Establishing clear compliance measures is necessary to mitigate legal risks and ensure adherence to data protection laws.
- Decision owner: Head of Legal Compliance
- Options: Establish specific compliance check protocols / Implement regular audits of data entry procedures

### C7 · MAJOR · blocks the build

**What individual and group responsibilities should the governance team adopt to maintain data accuracy and integrity?**

- Why it matters: Specific responsibilities for the governance team are critical to avoid data inconsistency and mismanagement.
- Decision owner: Executive Leadership
- Options: Define these during policy review meetings / Engage governance team members in defining their roles

## Tension report

The primary disagreement centered on the clarity of roles and responsibilities for the governance team, as well as ensuring compliance with data protection regulations. While several definitions and processes were clarified, questions regarding ownership of responsibilities remain unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 30 | - | continue |
| 2 | 7 | 1 | 4 | 2 | 0.40 | 75 | 65 | CONTINUE | continue |
| 3 | 9 | 2 | 4 | 3 | 0.53 | 80 | 65 | CONTINUE | continue |
| 4 | 9 | 0 | 6 | 3 | 0.32 | 75 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (75/100): Ensuring the governance continuity and compliance mechanisms are consistently upheld over time.
- Critic's remaining worry (85/100): There may still be gaps in clearly defining user roles and responsibilities around data access and governance.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S2 | R1 | REVISED | 0 | The proposal does not specify who can view or edit sensitive contact information for government officials, which increases the risk of unauthorized access. |
| C2 | MAJOR | DEFINITIONS | D1, D2 | R1 | REVISED | 0 | The definitions of 'contact person' and 'key contact' lack clarity on selection criteria and context, which could lead to inconsistencies in contact entries and usage. |
| C3 | MAJOR | OWNERSHIP | A3 | R1 | ESCALATED | 0 | The proposal relies on a designated governance team for maintaining data integrity but does not clarify who this team is or what their authority entails. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not address how contact information will be protected from unauthorized access during system updates or when users change roles. |
| C5 | MAJOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | The proposal does not specify how compliance with data protection regulations will be ensured throughout the process of collecting and managing contact information. |
| C6 | MAJOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | There are no clear processes defined for managing duplicates or inaccuracies in contact information, which could lead to a lack of trust in the system. |
| C7 | MAJOR | OWNERSHIP | A3 | R2 | ESCALATED | 0 | The proposal does not clarify what the designated governance team's specific responsibilities entail for maintaining data accuracy. |
| C8 | MAJOR | OWNERSHIP | GAP | R3 | REVISED | 0 | The proposal does not specify what happens to the contact information if the designated governance team changes or if key personnel leave, risking loss of data integrity. |
| C9 | MAJOR | COMPLIANCE | GAP | R3 | REVISED | 0 | The proposal lacks a defined mechanism for ensuring ongoing compliance with data protection regulations as new data is entered or processes change. |
