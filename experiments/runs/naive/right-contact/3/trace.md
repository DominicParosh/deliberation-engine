# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `naive` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 7 rounds · 20 model calls (6 repairs)

## Round 1

### Proposer · confidence 80

_This release provides a new feature allowing users to designate and update a primary contact person for each country in the Government CRM. It is aimed at regional coordinators and project managers who need a reliable and transparent way to identify the appropriate contacts in each member country._

**Core commitments**
- V1: Enable users to designate a primary contact person for each country.
- V2: Allow users to view and update the primary contact details easily.

**In scope**
- S1: Provide a user interface for designated users (regional coordinators and project managers) to select and set a primary contact for each member country.
- S2: Implement functionality allowing authorized users to update, view, and save contact details such as name, title, email, and phone number for the primary contact in the system.
- S3: Integrate with existing contact records to ensure that updates to primary contact status are reflected across the CRM system.
- S4: Ensure that changes are logged for auditing purposes, tracking who made changes and when.

**Out of scope**
- X1: This release will not provide detailed historical records of changes to contact designations beyond the latest record.
- X2: This release will not implement notifications or alerts for when contact assignments change.
- X3: This release will not include additional contact-related functionalities such as ranking multiple contacts or adding multiple points of contact.

**Assumptions**
- A1: All relevant user groups (regional coordinators and project managers) have access to the CRM system, which they will utilize to track contact information.
- A2: Users understand their responsibility for maintaining up-to-date contact information to ensure effective communication with country officials.
- A3: The system has adequate security measures in place to ensure the confidentiality and proper handling of sensitive contact data.

**Definitions**
- D1: 'Primary contact' means the designated individual for each member country who is responsible for communication and coordination on behalf of the organization.
- D2: 'Designated user' means any regional coordinator or project manager authorized to update contact information within the CRM.

**Success criteria**
- K1: Achieve 90% of primary contact entries correctly updated and maintained within the CRM system as measured through user feedback and system audits within the first three months of launch.

Biggest worry: Ensuring that users actually utilize the new feature to keep contact information updated.

### Critic · confidence 40

Pre-mortem: A year after launch, the new primary contact feature inadvertently allowed unauthorized users from multiple regions to update contact details. This led to confusion and miscommunication, as key diplomatic contacts were assigned incorrectly, resulting in a breach of trust with several country officials. Sensitive government communications were mishandled, which triggered an internal review and external scrutiny concerning data security and compliance.

Questions the request leaves open:
- What criteria determine the eligibility of a user to be a 'designated user' that can update contacts?
- Who can view the primary contact information for each country, and can other project teams or regions see these records?
- What measures are in place to ensure that the primary contact information is accurate and kept up-to-date?
- What safeguards exist to prevent unauthorized access to sensitive contact records?
- How will the system handle changes when a regional coordinator or project manager leaves their role or changes responsibilities?
- How is the term 'contact' defined in terms of the necessary qualifications or roles these individuals hold?

New challenges:

**C1** · BLOCKER · OWNERSHIP · targets D2
- Challenge: The proposal does not specify who verifies the accuracy of the designated user's authority to update contact information.
- Failure scenario: An unauthorized project manager attempts to change the primary contact for a sensitive country, leading to miscommunication and potential diplomatic fallout.
- Resolution test: What is the verification process to ensure only authorized users can update contact information?

**C2** · MAJOR · CONFIDENTIALITY · targets S1
- Challenge: The proposal lacks clarity on who can view the primary contact information across different regions, potentially exposing sensitive data.
- Failure scenario: A project manager from a different region accesses and alters sensitive contact information without permission, complicating diplomatic communications and leading to distrust.
- Resolution test: Which roles can see primary contact records for different countries?

**C3** · MAJOR · DATA_QUALITY · targets S2
- Challenge: The proposal does not outline measures to ensure the accuracy and timeliness of the primary contact information updated by users.
- Failure scenario: Users make updates that are incorrect or out-of-date, leading to continued reliance on invalid contacts and further miscommunication.
- Resolution test: What measures will be implemented to ensure the accuracy of the designated contact's information?

**C4** · MAJOR · CONFIDENTIALITY · targets X3
- Challenge: The proposal states that additional contact-related functionalities like multiple contacts will not be included, but does not specify the implications of this limitation.
- Failure scenario: A project team encounters a situation where multiple contacts are required for effective communication, but the system lacks this capability, leading to failure in outreach efforts.
- Resolution test: What alternative solutions will be provided for situations requiring multiple contacts in a country?

**C5** · MAJOR · COMPLIANCE · targets S4
- Challenge: The proposal lacks a defined retention policy or audit trail process for changes made to primary contacts, raising compliance concerns.
- Failure scenario: Changes made to primary contacts are undocumented, leading to disputes over who was responsible for communication mishaps with diplomatic entities.
- Resolution test: What is the defined retention policy for logs of changes made to primary contact details?

**C6** · MAJOR · DEFINITIONS · targets D1
- Challenge: The term 'Primary contact' is not explicitly defined in terms of the required qualifications or responsibilities of these individuals.
- Failure scenario: A project relies on an individual defined as primary contact who is neither qualified nor aware of their designation, leading to communication breakdowns.
- Resolution test: What qualifications must a person meet to be designated as a 'Primary contact' for a country?

Biggest worry: Unauthorized users may access and alter sensitive contact information, causing significant miscommunication.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed D3]: This edit specifies a clear verification process involving a designated government liaison officer to ensure that only authorized users can update contact information, addressing the concern about unauthorized changes.
- **C2** REVISE (missing decision) [changed S5]: By defining the access levels for viewing primary contact information, this edit addresses the issue of potential data exposure and ensures that sensitive contact details are protected.
- **C3** REVISE (missing decision) [changed S6]: This edit establishes a review process and feedback mechanism to ensure the accuracy and timeliness of primary contact information, effectively addressing data quality concerns.
- **C4** DEFEND (acceptable risk): The limitation on having multiple contacts is acknowledged, but the team's existing communication policies will allow for workarounds, such as having users reference additional contacts in project metadata when necessary.
- **C5** REVISE (missing decision) [changed D4]: This edit defines a retention policy for change logs that ensures compliance while addressing concerns over the documentation of alterations made to primary contacts.
- **C6** REVISE (missing decision) [changed D5]: By defining the qualifications for a primary contact, this edit clarifies the requirements necessary for effective communication and reduces the risk of miscommunications.

Proposal changes: added S5, S6, D3, D4, D5
- S5 now reads: Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts, while restricting access for users from other regions.
- S6 now reads: Implement periodic reviews of primary contact details every quarter, where designated users are prompted to confirm the accuracy of their assigned contacts. Additionally, introduce a user feedback mechanism to report inaccuracies.
- D3 now reads: 'Verification process' means the steps taken to confirm that a designated user, such as a regional coordinator or project manager, has the official authority to alter the primary contact information for a member country. This will require an approval process from a government liaison officer who can validate the user's status and authority.
- D4 now reads: 'Retention policy' means the guidelines that determine how long changes made to primary contact details will be stored, which is set to a minimum of two years from the last modification date, for audit and compliance purposes.
- D5 now reads: 'Primary contact qualifications' means the criteria that must be met for an individual to be designated as a primary contact, including relevant experience in diplomatic communications and recognition by the organization as a point of contact.

Biggest worry: The verification and access control measures might still not be robust enough to prevent unauthorized changes to sensitive contact information.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C1** ACCEPT: Acceptable confirmation process established. Fact: A government liaison officer will verify the authority of users to update primary contact information. Evidence: "This will require an approval process from a government liaison officer who can validate the user's status and authority."
- **C2** ACCEPT: Defined access levels mitigate risks of unauthorized data exposure. Fact: Only regional coordinators and project managers from the same region can view primary contact records. Evidence: "allowing only regional coordinators and project managers from the same region to view primary contacts, while restricting access for users from other regions."
- **C3** MAINTAIN: The actual measures to ensure accuracy and timeliness are still not clearly defined.
- **C4** ACCEPT: Defined retention policy ensures compliance with auditing standards. Fact: Change logs for primary contacts will be retained for at least two years. Evidence: "'Retention policy' means the guidelines that determine how long changes made to primary contact details will be stored, which is set to a minimum of two years from the last modification date, for audit and compliance purposes."
- **C5** ACCEPT: Clarified qualifications will help avoid miscommunications. Fact: Criteria for primary contact designation include relevant experience and organization recognition. Evidence: "'Primary contact qualifications' means the criteria that must be met for an individual to be designated as a primary contact, including relevant experience in diplomatic communications and recognition by the organization as a point of contact."
- **C6** MAINTAIN: Lack of functionality for multiple contacts could lead to operational challenges.

New challenges:

**C7** · MAJOR · OPERATIONS · targets X3
- Challenge: The workaround suggested for missing multiple contacts implies that sensitive communications may not be fully addressed, risking operational efficiency.
- Failure scenario: A regional coordinator needs to contact multiple individuals for critical updates on a diplomatic mission but finds only one primary contact assigned, leading to delays and miscommunication.
- Resolution test: What alternative process will users follow when they need to communicate with multiple points of contact for a country?

Biggest worry: Exclusion of multiple contact functionalities may lead to operational inefficiencies during critical communications.

**Ledger:** raised 7 · open 3 · resolved 4 · escalated 0 · disagreement 0.40 → **continue**

## Round 3

### Proposer · confidence 75

- **C3** REVISE (missing decision) [changed S6]: This edit establishes a clear reminder system and confirmation requirement, ensuring designated users take responsibility for the accuracy of the primary contact information.
- **C6** REVISE (missing decision) [changed D5]: This change clarifies the qualifications needed for a primary contact, ensuring that users are aware of the criteria and responsibilities associated with this designation.
- **C7** REVISE (missing decision) [changed X3]: This edit formally states that there will be no alternative processes provided for multiple contacts, clarifying the expected use of the system while emphasizing the need for effective designation of a single primary contact.

Proposal changes: edited S6, X3, D5
- S6 now reads: Implement periodic reviews of primary contact details every quarter, where designated users are prompted to confirm the accuracy of their assigned contacts. A reminder system will be built that requires designated users to submit confirmation or updates within 14 days of the prompt. Additionally, introduce a user feedback mechanism to report inaccuracies, allowing users to flag outdated or incorrect primary contacts for review.
- X3 now reads: This release will not include additional contact-related functionalities such as ranking multiple contacts or adding multiple points of contact, and will not provide alternative processes for communicating with additional individuals. Users will be expected to identify the most relevant primary contact for communication.
- D5 now reads: 'Primary contact qualifications' means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) the official authority granted by a government liaison officer to engage with counterparts.

Biggest worry: The reliance on users to correctly identify and maintain accurate primary contact information still poses a significant risk.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C3** MAINTAIN: While a reminder system is proposed, it does not clearly outline how accuracy will ultimately be ensured for contact information.
- **C6** ACCEPT: Clarifying qualifications for primary contacts addresses the concern about operational effectiveness. Fact: Clear qualifications are defined for a primary contact to ensure they are suitable for the role. Evidence: "'Primary contact qualifications' means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) the official authority granted by a government liaison officer to engage with counterparts."
- **C7** ACCEPT: The proposal explicitly states the lack of alternative processes for multiple contacts, which needs to be well understood by users. Fact: No alternative processes will be provided for situations requiring multiple contacts. Evidence: "This release will not include additional contact-related functionalities such as ranking multiple contacts or adding multiple points of contact, and will not provide alternative processes for communicating with additional individuals."

Biggest worry: The lack of clarity on how accuracy will be verified for contact details presents a significant risk.

**Ledger:** raised 7 · open 1 · resolved 6 · escalated 0 · disagreement 0.13 → **continue**

## Round 4

### Proposer · confidence 80

- **C3** REVISE (missing decision) [changed S6]: The edits clarify that not only will users confirm the accuracy of their assigned contacts quarterly, but a data validation process will also be implemented to ensure only verified entries are accepted.

Proposal changes: edited S6
- S6 now reads: Implement periodic reviews of primary contact details every quarter by requiring designated users to confirm the accuracy of their assigned contacts. A reminder system will prompt users to submit confirmation or updates within 14 days of the prompt, and provide a mechanism for reporting inaccuracies. Additionally, introduce a data validation process during updates that checks for inconsistencies or errors based on predefined rules, ensuring that only complete and validated contact entries are accepted.

Biggest worry: Ensuring that the validation process effectively reduces the risk of outdated or incorrect contact information remains a concern.

### Critic · confidence 65 · CONTINUE

Rulings:
- **C3** ACCEPT: The measure of a data validation process ensures accuracy and timeliness of primary contact information. Fact: A data validation process checks for inconsistencies or errors during updates. Evidence: "Additionally, introduce a data validation process during updates that checks for inconsistencies or errors based on predefined rules, ensuring that only complete and validated contact entries are accepted."

New challenges:

**C8** · BLOCKER · OWNERSHIP · targets D2
- Challenge: The proposal still does not clarify who has the authority to verify the accuracy of the designated user's authority to update contact information.
- Failure scenario: If the lack of defined authority verification allows unqualified individuals to update primary contact details, it could lead to incorrect contact information and resulting diplomatic miscommunications.
- Resolution test: Who verifies the accuracy of a designated user's authority to update contact information?

**C9** · MAJOR · CONFIDENTIALITY · targets S1
- Challenge: The proposal lacks details on specific access levels and permissions for users from the same region to view primary contact information, which raises concerns about data exposure.
- Failure scenario: If some users from a different region gain unauthorized access to sensitive contact information, confidential diplomatic communications could be intercepted or mismanaged.
- Resolution test: What specific permissions and access levels define who can view primary contact information across different regions?

**C10** · BLOCKER · COMPLIANCE · targets S4
- Challenge: No defined retention policy is provided, raising important compliance regarding how long changes to primary contact details are kept for auditing purposes.
- Failure scenario: Without a retention policy, it is unclear how long the system retains updates, potentially leading to non-compliance during audits regarding data retention regulations.
- Resolution test: What is the exact retention period for changes made to primary contact information?

**C11** · MAJOR · DEFINITIONS · targets D1
- Challenge: The term 'Primary contact qualifications' is defined but not how changes in those qualifications are documented or managed in the CRM.
- Failure scenario: If qualifications of primary contacts change due to policy or personnel shifts without a defined process for updates, incorrect or outdated contacts may remain in the system.
- Resolution test: What is the defined process for documenting changes in primary contact qualifications?

Biggest worry: Unclear authority and verification processes could lead to unauthorized updates and severe diplomatic miscommunications.

**Ledger:** raised 11 · open 4 · resolved 7 · escalated 0 · disagreement 0.40 → **continue**

## Round 5

### Proposer · confidence 85

- **C8** REVISE (missing decision) [changed D3]: The edit specifies that either a government liaison officer or a designated compliance officer will be responsible for verifying the user's authority to update contact information. This clarifies who has the authority and ensures accountability.
- **C9** REVISE (missing decision) [changed S5]: The edit provides a clear definition of the access levels and permissions, establishing that only specific users from the same region can view primary contacts, thus addressing concerns about unauthorized access.
- **C10** REVISE (missing decision) [changed D4]: The edit now specifies a two-year retention period and includes a scheduled review to ensure compliance, addressing the concerns about audit retention.
- **C11** REVISE (missing decision) [changed D5]: The edit defines a process for documenting changes in primary contact qualifications, ensuring that any updates are formally recorded in the CRM system.

Proposal changes: edited S5, D3, D4, D5
- S5 now reads: Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. Users from other regions will have no access to this information. A role-based access control system will be implemented to ensure that only qualified users can view or edit primary contact information.
- D3 now reads: 'Verification process' means the steps taken to confirm that a designated user, such as a regional coordinator or project manager, has the official authority to alter the primary contact information for a member country. This verification will require an approval process from a government liaison officer or a designated compliance officer who has the authority to validate the user's status and authority.
- D4 now reads: Retention policy means the guidelines that determine how long changes made to primary contact details will be stored, set to a minimum of two years from the last modification date. Additionally, the system will implement a scheduled review of retained records every two years to ensure compliance with evolving legal and organizational standards.
- D5 now reads: 'Primary contact qualifications' means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) official authority granted by a government liaison officer to engage with counterparts. Any changes in qualifications will be documented through a formal process that includes notifying designated users and updating the CRM system to reflect such changes.

Biggest worry: Ensuring that new definitions and processes are implemented correctly and consistently across all users.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C8** ACCEPT: This clearly defines who is responsible for verifying user authority. Fact: User authority verification is confirmed by government liaison officer or compliance officer. Evidence: "This verification will require an approval process from a government liaison officer or a designated compliance officer who has the authority to validate the user's status and authority."
- **C9** ACCEPT: The proposal now specifies access levels that ensure confidentiality. Fact: Access to primary contacts is limited to regional coordinators and project managers from the same region only. Evidence: "Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. Users from other regions will have no access to this information."
- **C10** ACCEPT: A clear retention period for changes is now defined. Fact: Changes to primary contacts are retained for a minimum of two years. Evidence: "Retention policy means the guidelines that determine how long changes made to primary contact details will be stored, set to a minimum of two years from the last modification date."
- **C11** MAINTAIN: The proposal does not contain a clear and testable fact for documenting changes in qualifications.

Biggest worry: The potential for unauthorized updates still exists if user roles and responsibilities are not rigorously enforced.

**Ledger:** raised 11 · open 1 · resolved 10 · escalated 0 · disagreement 0.08 → **continue**

## Round 6

### Proposer · confidence 70

- **C11** REVISE (missing decision) [changed D5]: The edit specifies how changes in primary contact qualifications will be documented in the CRM, ensuring that a formal process is established for managing these updates.

Proposal changes: edited D5
- D5 now reads: 'Primary contact qualifications' means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) official authority granted by a government liaison officer to engage with counterparts. Any changes in qualifications will be documented through a formal process that requires notification to designated users following approval by a government liaison officer or designated compliance officer, and these changes will be recorded in the CRM system to ensure accurate and updated qualifications are maintained.

Biggest worry: The success of the release relies heavily on user compliance with the established processes for maintaining accurate contact data.

### Critic · confidence 75 · CONTINUE

Rulings:
- **C11** ACCEPT: This definition provides a clear and testable fact on how changes in qualifications are documented. Fact: Changes in primary contact qualifications are documented through a formal process requiring notification to designated users after approval from a government liaison officer or compliance officer. Evidence: "Any changes in qualifications will be documented through a formal process that requires notification to designated users following approval by a government liaison officer or designated compliance officer, and these changes will be recorded in the CRM system to ensure accurate and updated qualifications are maintained."

New challenges:

**C12** · MAJOR · CONFIDENTIALITY · targets S5
- Challenge: The proposal states that only regional coordinators and project managers from the same region can view primary contacts, but it does not define how access is managed when users change roles or leave.
- Failure scenario: If a regional coordinator transitions to a different role within the organization, their access to primary contact information may not be properly revoked, potentially allowing unauthorized access to sensitive data.
- Resolution test: What process is in place to revoke access to primary contact information when a designated user changes roles or leaves the organization?

**C13** · MAJOR · DATA_QUALITY · targets S6
- Challenge: The periodic review process for primary contact details does not define the criteria or metrics for determining if a contact is accurate or outdated.
- Failure scenario: During the quarterly review, if unclear criteria for accuracy exist, users may incorrectly validate outdated contacts, leading to ongoing miscommunication with country representatives.
- Resolution test: What specific criteria or metrics will users use to verify the accuracy of primary contact information during quarterly reviews?

**C14** · MAJOR · OWNERSHIP · targets D1, D5
- Challenge: The ownership and responsibility for maintaining the accuracy of the primary contacts is unclear. The proposal does not specify if designated users are held accountable for the accuracy of their assigned contacts after they are updated in the CRM.
- Failure scenario: If users are not held accountable for maintaining accurate contact information, updates may be made without proper verification, leading to potential diplomatic errors and lack of trust with country representatives.
- Resolution test: Who is ultimately accountable for the accuracy of primary contact information once it is updated in the system?

**C15** · MAJOR · COMPLIANCE · targets S4
- Challenge: The proposed logging mechanism for tracking changes to primary contacts does not specify how long the logs will be retained, potentially causing compliance risks.
- Failure scenario: If change logs are not retained for an appropriate period, the organization may fail to meet compliance obligations regarding data retention and auditing.
- Resolution test: What is the retention period for logs tracking changes to primary contact information?

**C16** · MAJOR · OWNERSHIP · targets X1
- Challenge: By not providing historical records of changes, there's a lack of clarity on how accountability is tracked over time, especially concerning the designated users who made changes.
- Failure scenario: If errors arise, there will be no historical record to identify who made the incorrect changes to primary contacts, complicating accountability and remediation efforts.
- Resolution test: How will accountability be managed if there is no historical record of changes to primary contact designations?

**C17** · BLOCKER · COMPLIANCE · targets D4
- Challenge: The proposal lacks a comprehensive retention policy for primary contact information that aligns with legal and regulatory compliance.
- Failure scenario: Without a clear retention policy, the organization risks storing sensitive data longer than permitted, potentially incurring legal penalties.
- Resolution test: What legal and regulatory timeframe will be established for the retention of primary contact records?

Biggest worry: Multiple major challenges regarding data ownership, confidentiality, and compliance remain unresolved.

**Ledger:** raised 17 · open 6 · resolved 11 · escalated 0 · disagreement 0.34 → **continue**

## Round 7

### Proposer · confidence 85

- **C12** REVISE (missing decision) [changed S5]: The edit establishes a clear process for managing access to primary contact information, ensuring that users who no longer have authorization will no longer have access.
- **C13** REVISE (missing decision) [changed S6]: This edit specifies the criteria users will follow to verify the accuracy of primary contact information, thereby ensuring a more structured review process.
- **C14** REVISE (missing decision) [changed D1, D5]: These edits clarify that designated users are responsible for the accuracy of the primary contacts once updated, improving accountability.
- **C15** REVISE (missing decision) [changed S4]: Clarifying the retention period for logs addresses compliance concerns and sets a clear expectation for how long records are maintained.
- **C16** REVISE (missing decision) [changed X1]: This edit establishes a notification system for updates that supports accountability despite the lack of historical records.
- **C17** REVISE (missing decision) [changed D4]: Extending the retention period aligns the policy with compliance needs, mitigating legal risks.

Proposal changes: edited S4, S5, S6, X1, D1, D4, D5
- S4 now reads: Ensure that changes are logged for auditing purposes, tracking who made changes and when. These logs will be retained for a minimum of five years, ensuring compliance with data retention standards.
- S5 now reads: Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. When a designated user changes roles or leaves the organization, access to the primary contact information will be automatically revoked through the role management system.
- S6 now reads: Implement periodic reviews of primary contact details every quarter by requiring designated users to confirm the accuracy of their assigned contacts based on criteria: 1) the designation is current, 2) contact details are up-to-date (name, title, email, phone), and 3) the designated user retains authority and recognition. A reminder system will prompt users to submit confirmation or updates within 14 days of the prompt, and provide a mechanism for reporting inaccuracies.
- X1 now reads: This release will not provide detailed historical records of changes to contact designations beyond the latest record; however, designated users will be notified of any updates made to primary contact details for accountability.
- D1 now reads: 'Primary contact' means the designated individual for each member country who is responsible for communication and coordination on behalf of the organization, and the designated user is accountable for maintaining the accuracy of the details.
- D4 now reads: ‘Retention policy’ means the guidelines that determine how long changes made to primary contact details will be stored, set to a minimum of five years from the last modification date. Additionally, the system will implement a scheduled review of retained records every five years to ensure compliance with evolving legal and organizational standards.
- D5 now reads: ‘Primary contact qualifications’ means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) official authority granted by a government liaison officer to engage with counterparts. Any updates must be verified and validated by the designated user.

Biggest worry: Ensuring all users uphold accountability for contact information updates may still prove challenging.

### Critic · confidence 80 · CONCLUDE

Rulings:
- **C12** ACCEPT: This clarifies how access is managed when users change roles or leave. Fact: Access to primary contact information is revoked automatically via the role management system. Evidence: "access to the primary contact information will be automatically revoked through the role management system."
- **C13** MAINTAIN: This defines clear criteria for contact accuracy verification. [Not counted as settled: the sentence you quote leans on 'designated users', which names no role, number or rule.]
- **C13** OPEN_AT_CLOSE: Still open when deliberation ended (consensus).
- **C14** MAINTAIN: While there is accountability, the definition lacks specificity on enforcement measures after updates.
- **C14** OPEN_AT_CLOSE: Still open when deliberation ended (consensus).
- **C15** ACCEPT: This specifies the retention period for logs, addressing compliance. Fact: Change logs will be retained for at least five years. Evidence: "These logs will be retained for a minimum of five years, ensuring compliance with data retention standards."
- **C16** MAINTAIN: This establishes a mechanism for accountability but lacks detail on how accountability is reinforced without historical records.
- **C16** OPEN_AT_CLOSE: Still open when deliberation ended (consensus).
- **C17** ACCEPT: The retention policy now supports compliance needs. Fact: Primary contact records will be retained for at least five years. Evidence: "set to a minimum of five years from the last modification date."

Biggest worry: The effectiveness of primary contact updates hinges on user accountability and the adequacy of review processes.

**Ledger:** raised 17 · open 3 · resolved 14 · escalated 0 · disagreement 0.16 → **consensus**

## Final proposal

_The proposal details features for designating primary contacts for countries, including user access controls and periodic reviews for accuracy, while also addressing retention policies for both contact details and change logs. Specific processes for managing access and accountability have now been established, improving the overall governance of contact information management._

**Core commitments**
- V1: Enable users to designate a primary contact person for each country.
- V2: Allow users to view and update the primary contact details easily.

**In scope**
- S1: Provide a user interface for designated users (regional coordinators and project managers) to select and set a primary contact for each member country.
- S2: Implement functionality allowing authorized users to update, view, and save contact details such as name, title, email, and phone number for the primary contact in the system.
- S3: Integrate with existing contact records to ensure that updates to primary contact status are reflected across the CRM system.
- S4: Ensure that changes are logged for auditing purposes, tracking who made changes and when. These logs will be retained for a minimum of five years, ensuring compliance with data retention standards.
- S5: Define user access levels for primary contact information, allowing only regional coordinators and project managers from the same region to view primary contacts. When a designated user changes roles or leaves the organization, access to the primary contact information will be automatically revoked through the role management system.
- S6: Implement periodic reviews of primary contact details every quarter by requiring designated users to confirm the accuracy of their assigned contacts based on criteria: 1) the designation is current, 2) contact details are up-to-date (name, title, email, phone), and 3) the designated user retains authority and recognition. A reminder system will prompt users to submit confirmation or updates within 14 days of the prompt, and provide a mechanism for reporting inaccuracies.

**Out of scope**
- X1: This release will not provide detailed historical records of changes to contact designations beyond the latest record; however, designated users will be notified of any updates made to primary contact details for accountability.
- X2: This release will not implement notifications or alerts for when contact assignments change.
- X3: This release will not include additional contact-related functionalities such as ranking multiple contacts or adding multiple points of contact, and will not provide alternative processes for communicating with additional individuals. Users will be expected to identify the most relevant primary contact for communication.

**Assumptions**
- A1: All relevant user groups (regional coordinators and project managers) have access to the CRM system, which they will utilize to track contact information.
- A2: Users understand their responsibility for maintaining up-to-date contact information to ensure effective communication with country officials.
- A3: The system has adequate security measures in place to ensure the confidentiality and proper handling of sensitive contact data.

**Definitions**
- D1: 'Primary contact' means the designated individual for each member country who is responsible for communication and coordination on behalf of the organization, and the designated user is accountable for maintaining the accuracy of the details.
- D2: 'Designated user' means any regional coordinator or project manager authorized to update contact information within the CRM.
- D3: 'Verification process' means the steps taken to confirm that a designated user, such as a regional coordinator or project manager, has the official authority to alter the primary contact information for a member country. This verification will require an approval process from a government liaison officer or a designated compliance officer who has the authority to validate the user's status and authority.
- D4: ‘Retention policy’ means the guidelines that determine how long changes made to primary contact details will be stored, set to a minimum of five years from the last modification date. Additionally, the system will implement a scheduled review of retained records every five years to ensure compliance with evolving legal and organizational standards.
- D5: ‘Primary contact qualifications’ means that an individual designated as a primary contact must have the following qualifications: 1) prior experience in diplomatic communications, 2) recognition by the organization as a point of contact, and 3) official authority granted by a government liaison officer to engage with counterparts. Any updates must be verified and validated by the designated user.

**Success criteria**
- K1: Achieve 90% of primary contact entries correctly updated and maintained within the CRM system as measured through user feedback and system audits within the first three months of launch.

## Orchestrator warnings

- R7: Critic's ACCEPT of C13 was refused (the sentence you quote leans on 'designated users', which names no role, number or rule); recorded as MAINTAIN.
