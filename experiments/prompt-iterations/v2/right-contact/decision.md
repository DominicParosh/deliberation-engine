# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.010.

## Summary

The new feature will enhance contact management by allowing users to assign and update primary contact persons for each member country and include a user-friendly search interface for efficient access to contact records. Out-of-scope items include integration with external databases and tracking historical changes. The decision about the security measures that need further clarification is still open for consideration.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to assign and update primary contact persons for each member country.  
  Users will be able to assign and update primary contact persons, which is essential for accurate communication with government representatives.
- **V2** Provide a user-friendly interface to search and filter country contacts efficiently.  
  The user-friendly interface for searching country contacts will streamline access for regional coordinators and project managers.

**In scope**

- **S1** Add a new 'Primary Contact Person' field in the contact record for each country, accessible to regional coordinators and project managers.  
  A new 'Primary Contact Person' field will be added to ensure designated contacts are recorded and accessible to authorized users. _(C1)_
- **S2** Allow users (regional coordinators and project managers) to update, delete, and view contact details for the assigned primary contact, including email notifications sent when the contact is updated.  
  Users will have the ability to update and delete contact details, including receiving notifications when contacts change, enhancing data integrity and ownership. _(C4)_
- **S3** Implement search functionality based on country and name to easily find the right contacts.  
  The search functionality will improve efficiency in finding the right contacts based on country or name, making it easier for users to communicate effectively.
- **S4** Enable data entry validations to ensure correct formatting of contact information.  
  Data entry validations will ensure all contact information is correctly formatted, enhancing overall data quality.
- **S5** Provide training materials and user guidelines for effective use of the new feature.  
  Training materials will be provided to ensure effective use of the new feature, supporting user adoption and understanding.
- **S6** Incorporate a periodic review process, occurring bi-annually, to validate the accuracy of contact data based on specific criteria including active representation and completeness.  
  A bi-annual review process will validate contact data, emphasizing the importance of data accuracy and accountability.
- **S7** Define security measures including access controls and audit logs allowing only regional coordinators and project managers to view or modify the 'Primary Contact Person' field, thereby preventing unauthorized access to sensitive contact information.  
  Specific security measures will prevent unauthorized access to sensitive contact information, addressing crucial confidentiality concerns. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** Integration with external contact databases or services.
- **X2** Tracking historical changes of contact assignments.
- **X3** Advanced analytics on contact effectiveness or engagement history.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users have the appropriate permissions to access and modify contact information, specifically regional coordinators and project managers. | The feature assumes that roles such as regional coordinators and project managers can manage contacts. | C1 → revised |
| A2 | Contact data will be maintained by users through periodic validation processes and updates, with regional coordinators and designated data managers responsible for accuracy. | The system relies on users to enter and update contact details accurately; ownership must be established to ensure data is kept current. | Accepted (never challenged) |
| A3 | Contact data privacy regulations, specifically GDPR, are being followed by obtaining user consent and maintaining data security protocols. | The system will handle sensitive data related to diplomatic contacts. | C3 → revised |

## Definitions

- **D1** "Primary Contact Person": The individual designated as the primary point of communication for each government entity, which must be a government official or designated representative officially communicated by the respective government, including their name, title, email, and phone number.  
  The definition of 'Primary Contact Person' was specified to include roles and official communication responsibilities, clarifying previous ambiguities.
- **D2** "Search Functionality": A feature that allows users to input specific criteria (such as country or name) to retrieve corresponding contact records.  
  The 'Search Functionality' definition was clarified to support user needs for quick retrieval of contact records.
- **D3** "Periodic Review Process": A scheduled process that occurs bi-annually for reviewing and confirming the accuracy of contact data based on criteria such as active representation and completeness of information.  
  The periodic review process is defined to ensure consistency in maintaining up-to-date contact records through set criteria.

## Success criteria

- **K1** User satisfaction rating: target 80% or higher (Gather feedback through a user survey conducted one month after implementation.)  
  User satisfaction rating criteria were established to measure the effectiveness of the new feature post-implementation.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement centered around access control measures for securing sensitive contact information. While the proposer expressed concern about potential gaps, the critic was more focused on the clarity of the processes for maintaining contact accuracy. This tension was somewhat resolved, but clarity on access controls remains a point of caution.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 3 | 3 | 0 | 0.46 | 80 | 70 | CONTINUE | continue |
| 3 | 8 | 3 | 5 | 0 | 0.35 | 80 | 70 | CONTINUE | continue |
| 4 | 9 | 1 | 8 | 0 | 0.11 | 80 | 70 | CONTINUE | continue |
| 5 | 9 | 0 | 9 | 0 | 0.00 | 70 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (70/100): There may still be gaps in the specifications for the access controls that could lead to potential security issues.
- Critic's remaining worry (85/100): The proposal still lacks clarity on the process for handling changes to primary contacts, which could lead to confusion and outdated contact information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S2, A1 | R1 | REVISED | 0 | The proposal does not define who has access to view and modify the 'Primary Contact Person' field, which raises confidentiality concerns regarding sensitive diplomatic contacts. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'Primary Contact Person' is too broad and does not clarify any limits or specific criteria, making it difficult to enforce consistently. |
| C3 | MAJOR | COMPLIANCE | A3 | R1 | REVISED | 0 | The assumption that contact data privacy regulations are being followed is too vague without specifying which regulations apply, risking non-compliance. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 1 | The proposal does not specify what process will be followed when a primary contact changes, leaves, or is reassigned, risking confusion and outdated contact information. |
| C5 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal lacks a clear mechanism for verifying the accuracy of the contact information which could lead to outdated or incorrect data being used. |
| C6 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal does not address what will happen if a user without permission attempts to access or modify contact information, leaving a security gap. |
| C7 | MAJOR | OWNERSHIP | GAP | R3 | REVISED | 0 | The proposal does not specify who is responsible for maintaining the accuracy of the contact information outside of the reviews, creating a gap in ownership. |
| C8 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | Terms like 'periodic review process' lack definition—how often will reviews occur, and what will be the specific criteria for maintaining contact data? |
| C9 | MAJOR | CONFIDENTIALITY | GAP | R4 | REVISED | 0 | The proposal lacks detail on what specific access controls are in place to ensure that only authorized users can view or modify sensitive contact information, raising potential confidentiality risks. |
