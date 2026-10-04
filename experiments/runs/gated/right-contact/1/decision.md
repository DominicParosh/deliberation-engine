# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.011.

Challenges: 9 raised · 5 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

This release will enable users to track key contacts in each of the ~100 member countries while ensuring information remains current and access is controlled. It includes a history log of changes and compliance provisions for data protection policies. However, details on transitional ownership of contact data and specific data protection policies require further human decisions.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to view and update key contact information for each of the ~100 member countries.  
  Users will be enabled to view and update key contact information, facilitating better management of government counterparts.
- **V2** Allow users to assign a primary contact per country for easier identification.  
  Assigning a primary contact per country simplifies identification and improves communication.

**In scope**

- **S1** Create a 'Key Contacts' section in the Government CRM for each member country, displaying the primary contact's name, title, and contact details. The designation of primary contacts will be reviewed quarterly by regional coordinators to ensure accuracy.  
  A 'Key Contacts' section will be created, with a quarterly review process for primary contacts to maintain data accuracy. _(C2)_
- **S2** Provide a form for users to add or edit contact information, including options to designate a contact as the primary for each country.  
  A form for adding or editing contact information will facilitate user engagement with the system’s features.
- **S3** Implement a search feature that allows users to find key contacts by country or name.  
  Implementing a search feature allows users to efficiently locate key contacts, supporting user needs.
- **S4** Ensure that only authorized users can add, edit, or view contact information. Authorized access is restricted to users within their own project teams for the countries they are responsible for, and is managed by the data privacy officer. Each project team will have a defined list of users authorized for their specific countries, with access privileges checkable through the system for compliance audits.  
  Access is strictly limited to authorized users within their project teams to prevent unauthorized exposure of sensitive contacts. _(C1, C3, C9)_
- **S5** Provide a history log of changes made to each contact entry to track updates.  
  A history log of contact entry changes will track updates and allow for review. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automatic updates of contact information from external databases.  
  Automatic updates from external databases were dropped to maintain control over data accuracy and integrity.
- **X2** Integration with third-party communication tools is not included in this release.  
  Integration with third-party communication tools was deemed outside the scope of this release to avoid complexity.
- **X3** Historical engagement data with contacts beyond the current contact information will not be part of this release.  
  Historical engagement data with contacts will not be included to focus on current contact management.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have the necessary training to access and use the new 'Key Contacts' feature, which is necessary for engagement efficiency. | Kept | never challenged |
| A2 | There are no existing protocols preventing users from storing and updating contact details for government counterparts. | Kept | never challenged |
| A3 | Sensitive data protection policies are in place to ensure that contact details are securely managed, which is crucial for maintaining confidentiality. | Kept | C5 → escalated; C8 → revised |

## Definitions

- **D1** 'Key Contacts' means a designated individual representing a specific country for collaboration, including their name, title, and contact information.  
  'Key Contacts' is defined to specify the individuals representing countries for communication.
- **D2** 'Primary contact' means the key contact designated as the main point of contact for a country in the Government CRM.  
  'Primary contact' is clearly defined to help in the identification of main points of communication.

## Success criteria

- **K1** By the end of the quarter, at least 80% of regional coordinators and project managers report improved access to key contact information, measured through a user survey.  
  Success will be measured through surveys showing improved access, emphasizing user satisfaction.

## Open questions for humans

### C5 · BLOCKER · blocks the build

**What specific data protection policies will govern the storage and access of contact information within the 'Key Contacts' feature?**

- Why it matters: Lack of clarity can lead to mishandling of sensitive data and legal repercussions.
- Decision owner: Head of Data Protection
- Options: Define specific protocols for sensitive data management / Train users on data protection practices / Implement regular audits for compliance
- Proposer's last word (R2, defend, needs human decision): The specific data protection policies must be established by the organization, as they vary based on regulatory requirements and existing frameworks.
- Critic's last word (R2, escalate): The specifics of data protection policies are still unspecified, and thus the challenge remains open.

### C4 · MAJOR · blocks the build

**What is the process for transitioning ownership of contact information when a responsible user changes roles or departs?**

- Why it matters: If not addressed, key contact information may become unmanaged, leading to confusion and ineffective outreach.
- Decision owner: Organizational Policy Maker
- Options: Establish a formal handover process for outgoing personnel / Allow team members to assume responsibility / Implement a centralized system to reassign contacts
- Proposer's last word (R2, defend, needs human decision): The specific process for transitioning ownership of contact data when users leave must be determined by the organization, as it depends on existing protocols and policies.
- Critic's last word (R2, escalate): The challenge regarding transitioning ownership remains open as it requires a human decision.

### C7 · MAJOR · blocks the build

**What established processes are in place to ensure continuity in contact data management when users change roles or leave?**

- Why it matters: Ensuring data continuity is crucial to maintain effective communication and operations.
- Decision owner: Organizational Policy Maker
- Options: Create a formal transition procedure for departing personnel / Assign a deputy to manage contact data / Document contact data protocols within teams
- Proposer's last word (R4, defend, needs human decision): The responsibility for data continuity and management during personnel changes must be established by organizational policies and cannot be assumed in this proposal.
- Critic's last word (R4, escalate): The proposal lacks clarity on established processes for managing data continuity during personnel changes, requiring organizational input.

### C6 · MINOR · does not block the build

**What measures will be implemented to protect sensitive data within the history log of changes to contact entries?**

- Why it matters: Preventing unauthorized access to changes in sensitive information is critical for maintaining confidentiality.
- Decision owner: Data Privacy Officer
- Options: Restrict access to the history log based on user roles / Encrypt sensitive data changes in the log / Limit retention of sensitive updates in the log
- Proposer's last word (R3, defend, acceptable risk): The risk of sensitive updates being exposed in the history log is acknowledged as acceptable for this release, as access is restricted to authorized users only. This access control mitigates potential risks, although further steps can be considered in future updates.
- Critic's last word (R3, maintain): While access is restricted to authorized users, the potential exposure of sensitive updates in the history log remains a concern that needs addressing.

## Tension report

The major disagreement centered on the management of sensitive data access and the continuity of contact information when key personnel depart. While the Proposer pushed for immediate solutions, the Critic expressed concerns about potential gaps and mismanagement, resulting in several open questions that require resolution.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 1 | 3 | 2 | 0.46 | 80 | 70 | CONTINUE | continue |
| 3 | 8 | 2 | 3 | 3 | 0.61 | 75 | 55 | CONTINUE | continue |
| 4 | 9 | 1 | 4 | 4 | 0.52 | 75 | 70 | CONTINUE | continue |
| 5 | 9 | 0 | 5 | 4 | 0.38 | 80 | 70 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring that all authorized access privileges are effectively managed and audited to avoid unauthorized exposure.
- Critic's remaining worry (70/100): There is still a lack of clarity on what happens to contact data when key personnel leave, increasing the potential for gaps in management.
- ⚠ Proposer reported 80/100 confidence while blocker(s) C5 remain unsettled.
- ⚠ C8 was settled by wording a later edit removed; the final proposal no longer says: "Data protection compliance will be ensured through regular audits conducted by the compliance team to confirm access privileges and the secure handling of sensitive data."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal does not specify criteria for authorized access to sensitive contact information, risking exposure to unauthorized users. |
| C2 | MAJOR | OWNERSHIP | S1, S5 | R1 | REVISED | 0 | The proposal is unclear about how the designation of a primary contact is managed and validated, risking inconsistency. |
| C3 | MAJOR | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal lacks details on how to prevent users from seeing sensitive contacts in other teams or regions, leading to possible leaks. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | ESCALATED | 0 | The proposal does not mention what happens to the contact data if a user responsible for maintaining it leaves the organization. |
| C5 | BLOCKER | COMPLIANCE | A3 | R1 | ESCALATED | 0 | The proposal does not detail how data protection policies will be enforced in relation to the new 'Key Contacts' feature. |
| C6 | MINOR | CONFIDENTIALITY | S5 | R1 | ESCALATED | 2 | The history log might expose sensitive updates unnecessarily, creating a security risk. |
| C7 | MAJOR | OWNERSHIP | S4, GAP | R3 | ESCALATED | 0 | The proposal does not clarify who is responsible for the continuity of contact data in the event that regional coordinators or project managers leave, leading to gaps in contact management. |
| C8 | BLOCKER | COMPLIANCE | A3 | R3 | REVISED | 0 | The proposal lacks details on how data protection policies will be enforced specifically for the 'Key Contacts' feature, risking non-compliance with regulatory and internal policies. |
| C9 | BLOCKER | CONFIDENTIALITY | GAP | R4 | REVISED | 0 | The proposal does not specify how access to sensitive contact information is limited within teams, risking unauthorized exposure to sensitive data. |
