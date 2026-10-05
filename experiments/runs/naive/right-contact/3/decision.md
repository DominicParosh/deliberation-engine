# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 7 rounds (policy `naive`) · $0.021.

Challenges: 17 raised · 14 settled between the agents · 0 handed to humans · 3 still open when it ended.

## Summary

The proposal to enhance contact management by designating primary contacts for countries will be built, including an interface for updates and access controls. However, it will not include historical records of changes to contact designations. There remain unresolved questions regarding the accountability of users for maintaining accurate contact information.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to designate a primary contact person for each country.
- **V2** Allow users to view and update the primary contact details easily.

**In scope**

- **S1** Provide a user interface for designated users (regional coordinators and project managers) to select and set a primary contact for each member country.  
  Provided a user interface for designated users to select a primary contact for each member country, ensuring proper contact assignment.
- **S2** Implement functionality allowing authorized users to update, view, and save contact details such as name, title, email, and phone number for the primary contact in the system.  
  Implemented functionality for authorized users to update and save primary contact details, ensuring accuracy.
- **S3** Integrate with existing contact records to ensure that updates to primary contact status are reflected across the CRM system.
- **S4** Ensure that changes are logged for auditing purposes, tracking who made changes and when. These logs will be retained for a minimum of five years, ensuring compliance with data retention standards.  
  Ensured change logs for auditing are retained for a minimum of five years, addressing compliance needs.
- **S5** Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. When a designated user changes roles or leaves the organization, access to the primary contact information will be automatically revoked through the role management system.  
  Defined user access levels to ensure only authorized personnel can view primary contact details, enhancing data protection.
- **S6** Implement periodic reviews of primary contact details every quarter by requiring designated users to confirm the accuracy of their assigned contacts based on criteria: 1) the designation is current, 2) contact details are up-to-date (name, title, email, phone), and 3) the designated user retains authority and recognition. A reminder system will prompt users to submit confirmation or updates within 14 days of the prompt, and provide a mechanism for reporting inaccuracies.  
  Implemented a quarterly review process to verify the accuracy of primary contact information, addressing data quality concerns. _(C13)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not provide detailed historical records of changes to contact designations beyond the latest record; however, designated users will be notified of any updates made to primary contact details for accountability.  
  Historical records of changes to contact designations will not be provided, limiting visibility into past updates.
- **X2** This release will not implement notifications or alerts for when contact assignments change.
- **X3** This release will not include additional contact-related functionalities such as ranking multiple contacts or adding multiple points of contact, and will not provide alternative processes for communicating with additional individuals. Users will be expected to identify the most relevant primary contact for communication.  
  Additional functionalities for multiple contacts are out of scope, focusing only on primary contact designation.

**Rejected during deliberation**

- Nothing was dropped.
- Declined **C4** (MAJOR · CONFIDENTIALITY): What alternative solutions will be provided for situations requiring multiple contacts in a country? The Proposer's answer, which the Critic accepted: The limitation on having multiple contacts is acknowledged, but the team's existing communication policies will allow for workarounds, such as having users reference additional contacts in project metadata when necessary.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | All relevant user groups (regional coordinators and project managers) have access to the CRM system, which they will utilize to track contact information. | Kept | never challenged |
| A2 | Users understand their responsibility for maintaining up-to-date contact information to ensure effective communication with country officials. | Kept | never challenged |
| A3 | The system has adequate security measures in place to ensure the confidentiality and proper handling of sensitive contact data. | Kept | never challenged |

## Definitions

- **D1** 'Primary contact' means the designated individual for each member country who is responsible for communication and coordination on behalf of the organization, and the designated user is accountable for maintaining the accuracy of the details.  
  The definition of 'Primary contact' clarifies the accountability and responsibilities of designated individuals. _(C6, C14)_
- **D2** 'Designated user' means any regional coordinator or project manager authorized to update contact information within the CRM.
- **D3** 'Verification process' means the steps taken to confirm that a designated user, such as a regional coordinator or project manager, has the official authority to alter the primary contact information for a member country. This verification will require an approval process from a government liaison officer or a designated compliance officer who has the authority to validate the user's status and authority.  
  The verification process of user authority to update contacts is specified, ensuring accountability. _(C12)_
- **D4** ‘Retention policy’ means the guidelines that determine how long changes made to primary contact details will be stored, set to a minimum of five years from the last modification date. Additionally, the system will implement a scheduled review of retained records every five years to ensure compliance with evolving legal and organizational standards.  
  The retention policy defines a minimum of five years for changes made to primary contact details, supporting compliance requirements. _(C17)_
- **D5** ‘Primary contact qualifications’ means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) official authority granted by a government liaison officer to engage with counterparts. Any updates must be verified and validated by the designated user.  
  Qualifications for primary contacts are defined to reduce risks of miscommunications. _(C6)_

## Success criteria

- **K1** Achieve 90% of primary contact entries correctly updated and maintained within the CRM system as measured through user feedback and system audits within the first three months of launch.

## Open questions for humans

### C13 · MAJOR · blocks the build

**What specific criteria or metrics will users use to verify the accuracy of primary contact information during quarterly reviews?**

- Why it matters: Without clear criteria, users may incorrectly validate outdated contacts, impacting communication.
- Decision owner: Project Manager
- Options: Define clear criteria / Maintain current approach without changes
- Proposer's last word (R7, revise, missing decision): This edit specifies the criteria users will follow to verify the accuracy of primary contact information, thereby ensuring a more structured review process.
- Critic's last word (R7, maintain): This defines clear criteria for contact accuracy verification. [Not counted as settled: the sentence you quote leans on 'designated users', which names no role, number or rule.]

### C14 · MAJOR · blocks the build

**Who is ultimately accountable for the accuracy of primary contact information once it is updated in the system?**

- Why it matters: Unclear accountability may lead to miscommunication if updates are not verified.
- Decision owner: Head of Country Engagement
- Options: Designated users are accountable / Accountability rests with department heads
- Proposer's last word (R7, revise, missing decision): These edits clarify that designated users are responsible for the accuracy of the primary contacts once updated, improving accountability.
- Critic's last word (R7, maintain): While there is accountability, the definition lacks specificity on enforcement measures after updates.

### C16 · MAJOR · blocks the build

**How will accountability be managed if there is no historical record of changes to primary contact designations?**

- Why it matters: Lack of historical records can complicate remediation efforts in case of errors.
- Decision owner: Data Governance Officer
- Options: Implement alternative accountability measures / Accept the limitation as is
- Proposer's last word (R7, revise, missing decision): This edit establishes a notification system for updates that supports accountability despite the lack of historical records.
- Critic's last word (R7, maintain): This establishes a mechanism for accountability but lacks detail on how accountability is reinforced without historical records.

## Tension report

The primary tension revolved around user accountability for maintaining accurate contact information after updates. While the proposer aimed to clarify responsibilities, the critic raised concerns about the effectiveness of proposed measures. The resolution did not fully address the critic's concerns, leaving some accountability issues unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 7 | 3 | 4 | 0 | 0.40 | 80 | 50 | CONTINUE | continue |
| 3 | 7 | 1 | 6 | 0 | 0.13 | 75 | 80 | CONTINUE | continue |
| 4 | 11 | 4 | 7 | 0 | 0.40 | 80 | 65 | CONTINUE | continue |
| 5 | 11 | 1 | 10 | 0 | 0.08 | 85 | 80 | CONTINUE | continue |
| 6 | 17 | 6 | 11 | 0 | 0.34 | 70 | 75 | CONTINUE | continue |
| 7 | 17 | 3 | 14 | 0 | 0.16 | 85 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring all users uphold accountability for contact information updates may still prove challenging.
- Critic's remaining worry (80/100): The effectiveness of primary contact updates hinges on user accountability and the adequacy of review processes.
- ⚠ C2 was settled by wording a later edit removed; the final proposal no longer says: "allowing only regional coordinators and project managers from the same region to view primary contacts, while restricting access for users from other regions."
- ⚠ C3 was settled by wording a later edit removed; the final proposal no longer says: "Additionally, introduce a data validation process during updates that checks for inconsistencies or errors based on predefined rules, ensuring that only complete and validated contact entries are accepted."
- ⚠ C5 was settled by wording a later edit removed; the final proposal no longer says: "'Primary contact qualifications' means the criteria that must be met for an individual to be designated as a primary contact, including relevant experience in diplomatic communications and recognition by the organization as a point of contact."
- ⚠ C9 was settled by wording a later edit removed; the final proposal no longer says: "Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. Users from other regions will have no access to this information."
- ⚠ C11 was settled by wording a later edit removed; the final proposal no longer says: "Any changes in qualifications will be documented through a formal process that requires notification to designated users following approval by a government liaison officer or designated compliance officer, and these changes will be recorded in the CRM system to ensure accurate and updated qualifications are maintained."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | OWNERSHIP | D2 | R1 | REVISED | 0 | The proposal does not specify who verifies the accuracy of the designated user's authority to update contact information. |
| C2 | MAJOR | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The proposal lacks clarity on who can view the primary contact information across different regions, potentially exposing sensitive data. |
| C3 | MAJOR | DATA_QUALITY | S2 | R1 | REVISED | 2 | The proposal does not outline measures to ensure the accuracy and timeliness of the primary contact information updated by users. |
| C4 | MAJOR | CONFIDENTIALITY | X3 | R1 | DEFENDED | 0 | The proposal states that additional contact-related functionalities like multiple contacts will not be included, but does not specify the implications of this limitation. |
| C5 | MAJOR | COMPLIANCE | S4 | R1 | REVISED | 0 | The proposal lacks a defined retention policy or audit trail process for changes made to primary contacts, raising compliance concerns. |
| C6 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 1 | The term 'Primary contact' is not explicitly defined in terms of the required qualifications or responsibilities of these individuals. |
| C7 | MAJOR | OPERATIONS | X3 | R2 | REVISED | 0 | The workaround suggested for missing multiple contacts implies that sensitive communications may not be fully addressed, risking operational efficiency. |
| C8 | BLOCKER | OWNERSHIP | D2 | R4 | REVISED | 0 | The proposal still does not clarify who has the authority to verify the accuracy of the designated user's authority to update contact information. |
| C9 | MAJOR | CONFIDENTIALITY | S1 | R4 | REVISED | 0 | The proposal lacks details on specific access levels and permissions for users from the same region to view primary contact information, which raises concerns about data exposure. |
| C10 | BLOCKER | COMPLIANCE | S4 | R4 | REVISED | 0 | No defined retention policy is provided, raising important compliance regarding how long changes to primary contact details are kept for auditing purposes. |
| C11 | MAJOR | DEFINITIONS | D1 | R4 | REVISED | 1 | The term 'Primary contact qualifications' is defined but not how changes in those qualifications are documented or managed in the CRM. |
| C12 | MAJOR | CONFIDENTIALITY | S5 | R6 | REVISED | 0 | The proposal states that only regional coordinators and project managers from the same region can view primary contacts, but it does not define how access is managed when users change roles or leave. |
| C13 | MAJOR | DATA_QUALITY | S6 | R6 | UNRESOLVED | 1 | The periodic review process for primary contact details does not define the criteria or metrics for determining if a contact is accurate or outdated. |
| C14 | MAJOR | OWNERSHIP | D1, D5 | R6 | UNRESOLVED | 1 | The ownership and responsibility for maintaining the accuracy of the primary contacts is unclear. The proposal does not specify if designated users are held accountable for the accuracy of their assigned contacts after they are updated in the CRM. |
| C15 | MAJOR | COMPLIANCE | S4 | R6 | REVISED | 0 | The proposed logging mechanism for tracking changes to primary contacts does not specify how long the logs will be retained, potentially causing compliance risks. |
| C16 | MAJOR | OWNERSHIP | X1 | R6 | UNRESOLVED | 1 | By not providing historical records of changes, there's a lack of clarity on how accountability is tracked over time, especially concerning the designated users who made changes. |
| C17 | BLOCKER | COMPLIANCE | D4 | R6 | REVISED | 0 | The proposal lacks a comprehensive retention policy for primary contact information that aligns with legal and regulatory compliance. |
