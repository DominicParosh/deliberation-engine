# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 2 rounds (policy `gated`) · $0.004.

## Summary

This release will establish a method for identifying and tracking primary contacts within each country based on their role, enhancing users' ability to manage government relationships. The new features will not address historical engagement data or change user permissions for viewing contact information. Stakeholders must ensure that data ownership and validation processes are properly defined before implementation.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can identify the primary contact for each country based on their role in the organization.  
  Users will be able to identify the primary contact for each country based on their organizational role, improving clarity in communication.
- **V2** Users can access and modify details of the primary contacts including their responsibilities and affiliation.  
  Users will have the ability to access and modify details of primary contacts, ensuring current information is maintained and responsibilities are clear.

**In scope**

- **S1** Create a new contact type labeled 'Primary Contact' for each country.  
  A new contact type labeled 'Primary Contact' will be created to distinguish primary contacts from others.
- **S2** Develop a user interface that displays primary contacts for each country alongside the existing contacts.  
  A user interface will be developed to display primary contacts alongside existing contacts, enhancing user navigation and efficiency.
- **S3** Allow users to assign roles to contacts, indicating their responsibilities with validated permissions (e.g., Project Lead, Ministry Contact).  
  The proposal will allow roles to be assigned to contacts, with validated permissions, ensuring that sensitive information is only accessible to authorized users. _(C4)_
- **S4** Implement a search filter that allows users to find primary contacts by country and role.  
  A search filter will enable users to efficiently find primary contacts by country and role, supporting effective management of communications.
- **S5** Enable users to edit and update details of primary contacts, including contact information and assigned role.  
  Users will be able to edit and update primary contact details, which is vital for maintaining accurate records within the CRM.

## What it will not do

**Out of scope for this release**

- **X1** This release will not provide historical engagement data linked to primary contacts.  
  Historical engagement data will not be included in this release to maintain focus on establishing primary contacts.
- **X2** This release does not include additional permissions for viewing contact information beyond current user roles.  
  The decision not to include additional permissions was made to keep the implementation straightforward and within current user roles.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users have necessary permissions to access and modify contact information. | The request assumes that users are currently allowed to manage contact details. | Accepted (never challenged) |
| A2 | There is a defined ownership process for contact data updates, clarifying who is responsible for data integrity and how discrepancies will be resolved. | The request assumes that roles and responsibilities for managing primary contacts are well understood and documented. | C2 → revised |
| A3 | There are mechanisms in place to ensure every ministry or project has at least one designated primary contact before the implementation. | To ensure the effectiveness of primary contacts, it must be validated that no ministries are left without designated contacts. | C3 → revised |
| A4 | Users are trained and comfortable with navigating the updated interface. | The change in tracking will require users to adapt to a new way of accessing contacts. | Accepted (never challenged) |

## Definitions

- **D1** "better way": An improved method of tracking which includes the ability to categorize contacts efficiently, access their information quickly, and prioritize contacts based on their roles compared to the previous method.
- **D2** "right person to contact": The individual designated as the primary point of contact for each specific role or project within a country.
- **D3** "track": The ability to view, modify, and search for contact information within the CRM system.

## Success criteria

- **K1** Percentage of users able to successfully locate the primary contact for their designated countries with accurate information.: target 85% of users should be able to locate the correct primary contact within 2 minutes. (User testing before release and feedback gathering post-release, with an additional check on data accuracy and freshness.)

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main disagreement revolved around ensuring clear ownership and validation processes for contact information. The Proposer was moderately confident but raised concerns about the potential impact of these elements on the proposal's success, while the Critic expressed a higher confidence level, focusing on the need for ongoing data validation.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 5 | 0 | 5 | 0 | 0.00 | 70 | 90 | CONCLUDE | consensus |

- Proposer's remaining worry (70/100): The success of the proposal heavily relies on clear ownership and validation processes for contact information.
- Critic's remaining worry (90/100): Ensuring ongoing data validation as roles and responsibilities change.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'better way' is vague and does not specify what improvements are being made compared to the existing tracking method. |
| C2 | MAJOR | OWNERSHIP | A2 | R1 | REVISED | 0 | Assuming a clear distinction between primary contacts and other types of contacts requires defined ownership of data updates and responsibilities. |
| C3 | MAJOR | CONFIDENTIALITY | A3 | R1 | REVISED | 0 | The assumption that every ministry or project will have a designated primary contact is risky; without ensuring proper data validation, confidential records may inadvertently expose sensitive information. |
| C4 | MAJOR | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | The proposal does not address how roles assigned to contacts will be controlled or verified, which could lead to unauthorized access to sensitive information. |
| C5 | MAJOR | DATA_QUALITY | K1 | R1 | REVISED | 0 | The success criterion regarding the ability to locate primary contacts within 2 minutes does not account for data freshness or accuracy, which are critical for identifying the right contacts. |
