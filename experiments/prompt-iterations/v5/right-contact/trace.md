# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 4 rounds · 11 model calls (3 repairs)

## Round 1

### Proposer · confidence 70

_This release will provide a structured way to track primary contacts for each member country using the Government CRM. It will enable regional coordinators and project managers to identify and manage the correct points of contact quickly and efficiently._

**Core commitments**
- V1: Enable users to view and update primary contact information for each country.

**In scope**
- S1: Role-based access: regional coordinators and project managers will have the ability to view and edit primary contact records.
- S2: A new field labeled 'Primary Contact' will be added to the country records in the CRM.
- S3: Users will be able to input the name, role, contact information, and email address of the primary contact.
- S4: The system will provide an alert for any changes made to primary contact information, logged with a timestamp and user ID.
- S5: A search function will be implemented to allow users to quickly find country records based on the primary contact's name or role.

**Out of scope**
- X1: Historical data on previous contacts will not be included in this release.
- X2: Bulk upload functionality for contact information will not be available in this release.
- X3: Integration with external contact management systems will not be included in this release.

**Assumptions**
- A1: All users have the necessary permissions to access and update contact records in the CRM.
- A2: Contacts and their information are available and will not have legal or privacy issues related to their storage and use.
- A3: The existing database structure can accommodate new fields without major architectural changes.
- A4: Users are familiar with the CRM and can navigate to the country records section efficiently.

**Definitions**
- D1: 'Primary Contact' means the main person designated to be contacted for any matters related to engagement with a particular country, including their name, title, contact number, and email address.

**Success criteria**
- K1: User satisfaction will be measured through a survey where at least 80% of users report an improvement in their ability to find and contact the appropriate persons in the member countries.

Biggest worry: There may be legal concerns regarding the storage and sharing of contact information for sensitive government positions.

### Critic · confidence 40

Pre-mortem: A year after launch, a serious incident occurred when a regional coordinator mistakenly sent a confidential diplomatic communication to the wrong primary contact in a country due to incorrect contact details being stored in the CRM. The correct primary contact had been changed, but the system failed to prevent the outdated information from being visible, leading to a breach of confidentiality and strained diplomatic relations with that country.

Questions the request leaves open:
- What safeguards are in place to prevent exposure of sensitive information based on incorrect primary contact records?
- What happens to the primary contact records when a user changes roles or leaves the organization?
- How will user permissions be enforced to ensure only authorized personnel can change or view sensitive contact details?
- What validation processes exist to ensure the accuracy of inputted contact information?
- Given that historical data will not be included, how will we manage continuity if contacts change frequently?
- How will we ensure that alerts regarding changes to primary contacts are effective in preventing incidents like the one described?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1, S4
- Challenge: The proposal allows regional coordinators and project managers to edit primary contact records openly, but does it account for which users should have visibility or editing capabilities based on their role, particularly in the context of sensitive diplomatic information?
- Failure scenario: A project manager with unauthorized access edits a primary contact record to the wrong person, which then leads to a sensitive email being sent to that incorrect contact, resulting in a breach of trust and confidentiality.
- Resolution test: What specific roles have access to view and edit primary contact information, and how is access controlled based on sensitivity?

**C2** · MAJOR · DEFINITIONS · targets D1
- Challenge: The definition of 'Primary Contact' is vague and does not specify boundaries on what constitutes acceptable contact information, potentially leading to inconsistencies or incomplete records.
- Failure scenario: A user inputs incomplete or inaccurate data due to unclear definitions, such as omitting the country code for a phone number, which leads to failed communications and operational delays.
- Resolution test: What exact data fields must be provided for 'Primary Contact,' and how will completeness and accuracy be validated?

**C3** · MAJOR · OWNERSHIP · targets S1
- Challenge: The current proposal does not address who is responsible for maintaining the accuracy and relevance of the primary contact records after they are created, particularly as personnel change over time.
- Failure scenario: A regional coordinator inputs a primary contact who eventually leaves, but there is no assigned individual to update or verify contact information, leading to reliance on outdated details.
- Resolution test: Outline the ownership process for maintaining primary contact records, including responsibilities for verification and updates as roles change or users leave.

Biggest worry: The potential for sensitive contact information to be mishandled due to unclear user permissions and ownership responsibilities.

**Ledger:** raised 3 · open 3 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S1]: The edits clarify that only regional coordinators can edit primary contact records, thus controlling access based on role and ensuring sensitivity is respected.
- **C2** REVISE (missing decision) [changed D1]: This definition now specifies which fields are necessary for 'Primary Contact,' thus setting expectations for completeness and accuracy.
- **C3** DEFEND (acceptable risk): (No usable answer: its edits broke the rules twice; the proposal stands.)

Proposal changes: edited S1, D1
- S1 now reads: Role-based access will be implemented such that only regional coordinators can edit primary contact records, while project managers can view but not edit these records. Access controls will restrict who can make changes based on predefined roles, ensuring that sensitive diplomatic information is only modified by authorized personnel.
- D1 now reads: 'Primary Contact' means the main person designated to be contacted for any matters related to engagement with a particular country, including their full name, title, direct phone number (with country code), and email address. All fields must be completed to ensure effective communication.

Biggest worry: Ensuring all users adhere to the defined access controls and maintain the accuracy of contact information.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT:  Evidence: "Role-based access will be implemented such that only regional coordinators can edit primary contact records, while project managers can view but not edit these records. Access controls will restrict who can make changes based on predefined roles, ensuring that sensitive diplomatic information is only modified by authorized personnel."
- **C2** ACCEPT:  Evidence: "'Primary Contact' means the main person designated to be contacted for any matters related to engagement with a particular country, including their full name, title, direct phone number (with country code), and email address. All fields must be completed to ensure effective communication."
- **C3** ESCALATE: The proposal does not currently address the process of maintaining the accuracy and relevance of primary contact records after they are created, particularly as personnel change.

New challenges:

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: Who is responsible for keeping primary contact records up-to-date after a contact's role changes or the user leaves the organization?
- Failure scenario: A primary contact’s role is changed, but there is no assigned person to verify and update the entry in the CRM. The outdated contact information leads to communication failures and important diplomatic messages being sent to the wrong recipient.
- Resolution test: Outline the process of ensuring primary contact records are regularly updated, including assigned responsibilities for verification and updates.

Biggest worry: Without clear ownership of contact records, there is a high risk of outdated information being used, which could lead to diplomatic incidents.

**Ledger:** raised 4 · open 1 · resolved 2 · escalated 1 · disagreement 0.44 → **continue**

## Round 3

### Proposer · confidence 85

- **C4** REVISE (missing decision) [changed S6]: This edit outlines a clear process for maintaining the accuracy of the primary contact records and assigns specific responsibilities to ensure updates are handled promptly.

Proposal changes: added S6
- S6 now reads: Responsibilities for keeping primary contact records updated will be assigned to regional coordinators, who will verify and update contact information for their respective countries within one month of any reported change in contact roles or user departures. Additionally, an annual review process will be implemented where regional coordinators will check for any changes to the primary contacts and verify their accuracy.

Biggest worry: Ensuring that regional coordinators have the resources and processes in place to maintain the accuracy of contact information regularly.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C4** ACCEPT:  Evidence: "Responsibilities for keeping primary contact records updated will be assigned to regional coordinators, who will verify and update contact information for their respective countries within one month of any reported change in contact roles or user departures."

New challenges:

**C5** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: What safeguards are in place to prevent exposure of sensitive information based on incorrect primary contact records?
- Failure scenario: A primary contact's details are outdated due to a lack of verification, leading to a regional coordinator sending sensitive information to an unauthorized individual, resulting in a data breach.
- Resolution test: What specific safeguards ensure that outdated primary contact records cannot be used to send sensitive information?

**C6** · MAJOR · DEFINITIONS · targets GAP
- Challenge: What validation processes exist to ensure the accuracy of inputted contact information?
- Failure scenario: Incorrect or incomplete contact information is entered for a primary contact, leading to miscommunication and operational failures because the CRM lacks validation checks.
- Resolution test: What validation process is implemented to ensure that entered contact information meets defined standards before being saved?

Biggest worry: The potential for serious diplomatic incidents due to outdated primary contact information and lack of safeguards against incorrect records.

**Ledger:** raised 6 · open 2 · resolved 3 · escalated 1 · disagreement 0.46 → **continue**

## Round 4

### Proposer · confidence 80

- **C5** DEFEND (needs human decision): The safeguards for preventing exposure of sensitive information depend on organizational policies regarding data protection and handling sensitive diplomatic information. The design and enforcement of these safeguards should be defined by the organization, and hence must be determined by stakeholders.
- **C6** REVISE (missing decision) [changed S4]: The proposed edits introduce a validation process for the inputted contact information to prevent errors and confirm accuracy before saving, addressing the challenge directly.

Proposal changes: edited S4
- S4 now reads: The system will provide an alert for any changes made to primary contact information, logged with a timestamp and user ID. Additionally, a validation process will be implemented to ensure that entered contact information meets defined standards, including checks against predefined formats for phone numbers and email addresses.

Biggest worry: Failure to implement proper safeguards for sensitive information may lead to data breaches.

### Critic · confidence 45 · CONTINUE

Rulings:
- **C5** ESCALATE: The proposal depends on organizational policies regarding data protection which need resolution from stakeholders.
- **C6** ESCALATE: While the proposal has introduced a validation process, the specifics of what that validation entails are still ambiguous and require clarification.

Biggest worry: Outdated primary contact records might still be visible and used, risking data breaches.

**Ledger:** raised 6 · open 0 · resolved 3 · escalated 3 · disagreement 0.46 → **converged**

## Final proposal

_This release will provide a structured way to track primary contacts for each member country using the Government CRM, ensuring authorized personnel can edit contacts while defining record maintenance responsibilities. The solution will enable efficient identification and management of the correct points of contact, with a focus on data protection and validation processes for contact information accuracy._

**Core commitments**
- V1: Enable users to view and update primary contact information for each country.

**In scope**
- S1: Role-based access will be implemented such that only regional coordinators can edit primary contact records, while project managers can view but not edit these records. Access controls will restrict who can make changes based on predefined roles, ensuring that sensitive diplomatic information is only modified by authorized personnel.
- S2: A new field labeled 'Primary Contact' will be added to the country records in the CRM.
- S3: Users will be able to input the name, role, contact information, and email address of the primary contact.
- S4: The system will provide an alert for any changes made to primary contact information, logged with a timestamp and user ID. Additionally, a validation process will be implemented to ensure that entered contact information meets defined standards, including checks against predefined formats for phone numbers and email addresses.
- S5: A search function will be implemented to allow users to quickly find country records based on the primary contact's name or role.
- S6: Responsibilities for keeping primary contact records updated will be assigned to regional coordinators, who will verify and update contact information for their respective countries within one month of any reported change in contact roles or user departures. Additionally, an annual review process will be implemented where regional coordinators will check for any changes to the primary contacts and verify their accuracy.

**Out of scope**
- X1: Historical data on previous contacts will not be included in this release.
- X2: Bulk upload functionality for contact information will not be available in this release.
- X3: Integration with external contact management systems will not be included in this release.

**Assumptions**
- A1: All users have the necessary permissions to access and update contact records in the CRM.
- A2: Contacts and their information are available and will not have legal or privacy issues related to their storage and use.
- A3: The existing database structure can accommodate new fields without major architectural changes.
- A4: Users are familiar with the CRM and can navigate to the country records section efficiently.

**Definitions**
- D1: 'Primary Contact' means the main person designated to be contacted for any matters related to engagement with a particular country, including their full name, title, direct phone number (with country code), and email address. All fields must be completed to ensure effective communication.

**Success criteria**
- K1: User satisfaction will be measured through a survey where at least 80% of users report an improvement in their ability to find and contact the appropriate persons in the member countries.

## Orchestrator warnings

- R2: after a failed repair, edits breaking these rules were dropped: C3: S1 is given two different wordings in this turn. An item has one wording: give its complete final wording, with every change, in each answer that edits it.
- R2: Proposer's REVISE of C3 had no legal edit; recorded as DEFEND.
