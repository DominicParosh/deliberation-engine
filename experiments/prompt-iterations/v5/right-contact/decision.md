# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 4 rounds (policy `gated`) · $0.008.

## Summary

This release will provide a structured way to track primary contacts for each member country using the Government CRM, focusing on data protection and validation processes for accuracy. Users will be able to view and update primary contact information while defining responsibilities for record maintenance. However, unresolved questions about ownership and safeguards for sensitive information remain to be decided by stakeholders.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to view and update primary contact information for each country.  
  Enable users to view and update primary contact information for each country, resolving challenges around visibility and editing capabilities based on roles.

**In scope**

- **S1** Role-based access will be implemented such that only regional coordinators can edit primary contact records, while project managers can view but not edit these records. Access controls will restrict who can make changes based on predefined roles, ensuring that sensitive diplomatic information is only modified by authorized personnel.  
  Role-based access ensures only regional coordinators can edit primary contact records while project managers can view. This addresses concerns about sensitive diplomatic information being modified by unauthorized personnel. _(C1)_
- **S2** A new field labeled 'Primary Contact' will be added to the country records in the CRM.  
  Adding a 'Primary Contact' field allows for structured data entry concerning vital contact details, making data easier to manage and access.
- **S3** Users will be able to input the name, role, contact information, and email address of the primary contact.  
  Users will input comprehensive details for the primary contact, ensuring that contact information is complete and usable for effective communication.
- **S4** The system will provide an alert for any changes made to primary contact information, logged with a timestamp and user ID. Additionally, a validation process will be implemented to ensure that entered contact information meets defined standards, including checks against predefined formats for phone numbers and email addresses.  
  An alert system for changes and a validation process will help maintain accuracy in contact details and prevent errors in the records. _(C2)_
- **S5** A search function will be implemented to allow users to quickly find country records based on the primary contact's name or role.  
  The search function will facilitate quick access to country records based on primary contact attributes, enhancing usability and efficiency.
- **S6** Responsibilities for keeping primary contact records updated will be assigned to regional coordinators, who will verify and update contact information for their respective countries within one month of any reported change in contact roles or user departures. Additionally, an annual review process will be implemented where regional coordinators will check for any changes to the primary contacts and verify their accuracy.  
  Responsibilities for updating contact records are assigned to regional coordinators, ensuring that records remain accurate and relevant over time. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** Historical data on previous contacts will not be included in this release.
- **X2** Bulk upload functionality for contact information will not be available in this release.
- **X3** Integration with external contact management systems will not be included in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | All users have the necessary permissions to access and update contact records in the CRM. | Kept | never challenged |
| A2 | Contacts and their information are available and will not have legal or privacy issues related to their storage and use. | Kept | never challenged |
| A3 | The existing database structure can accommodate new fields without major architectural changes. | Kept | never challenged |
| A4 | Users are familiar with the CRM and can navigate to the country records section efficiently. | Kept | never challenged |

## Definitions

- **D1** 'Primary Contact' means the main person designated to be contacted for any matters related to engagement with a particular country, including their full name, title, direct phone number (with country code), and email address. All fields must be completed to ensure effective communication.  
  The definition of 'Primary Contact' is now explicit, detailing required fields to ensure completeness and minimize input errors. _(C2)_

## Success criteria

- **K1** User satisfaction will be measured through a survey where at least 80% of users report an improvement in their ability to find and contact the appropriate persons in the member countries.  
  User satisfaction will be measured to ensure the effectiveness of the implemented changes, reflecting the goals of improved communication and contact identification.

## Open questions for humans

### C5 · MAJOR · blocks the build

**What specific safeguards will be implemented to prevent exposure of sensitive information from outdated primary contact records?**

- Why it matters: To ensure that sensitive diplomatic information remains protected and that unauthorized individuals do not receive critical communications.
- Decision owner: Head of Data Protection
- Options: Implement a two-step verification process / Train coordinators on data handling / Review access permissions regularly

### C3 · MAJOR · does not block the build

**Who is ultimately responsible for maintaining the accuracy and relevance of primary contact records as personnel change?**

- Why it matters: Clarification is needed to ensure accountability and efficient record management.
- Decision owner: Head of Regional Coordination
- Options: Assign a dedicated role for ongoing updates / Implement a periodic review process / Combine both options

### C6 · MAJOR · does not block the build

**What validation processes will exist to ensure the accuracy of inputted contact information before it is saved in the system?**

- Why it matters: To prevent inaccuracies and ensure effective communication facilitated through reliable contact information.
- Decision owner: Data Quality Manager
- Options: Specify validation rules for each contact field / Develop a training module for users / Create an audit process for validation

## Tension report

The primary disagreement was centered around the adequacy of safeguards for sensitive information and the ownership for maintaining primary contact records. While the proposer is somewhat confident about the current design, the critic raised significant concerns about potential data breaches due to outdated information, emphasizing the need for further decision-making to address these risks.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 4 | 1 | 2 | 1 | 0.44 | 80 | 60 | CONTINUE | continue |
| 3 | 6 | 2 | 3 | 1 | 0.46 | 85 | 50 | CONTINUE | continue |
| 4 | 6 | 0 | 3 | 3 | 0.46 | 80 | 45 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Failure to implement proper safeguards for sensitive information may lead to data breaches.
- Critic's remaining worry (45/100): Outdated primary contact records might still be visible and used, risking data breaches.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S4 | R1 | REVISED | 0 | The proposal allows regional coordinators and project managers to edit primary contact records openly, but does it account for which users should have visibility or editing capabilities based on their role, particularly in the context of sensitive diplomatic information? |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'Primary Contact' is vague and does not specify boundaries on what constitutes acceptable contact information, potentially leading to inconsistencies or incomplete records. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | ESCALATED | 0 | The current proposal does not address who is responsible for maintaining the accuracy and relevance of the primary contact records after they are created, particularly as personnel change over time. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | Who is responsible for keeping primary contact records up-to-date after a contact's role changes or the user leaves the organization? |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R3 | ESCALATED | 0 | What safeguards are in place to prevent exposure of sensitive information based on incorrect primary contact records? |
| C6 | MAJOR | DEFINITIONS | GAP | R3 | ESCALATED | 0 | What validation processes exist to ensure the accuracy of inputted contact information? |
