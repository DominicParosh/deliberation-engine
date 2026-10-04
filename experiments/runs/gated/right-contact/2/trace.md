# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 5 rounds · 13 model calls (2 repairs)

## Round 1

### Proposer · confidence 85

_This release will improve the tracking of contact persons for each member country by creating a dedicated contact management section in the Government CRM. Users will be able to input, update, and view detailed information about the primary contact person for various government organizations across member countries._

**Core commitments**
- V1: Enable users to track and manage primary contact persons for each country.
- V2: Provide an intuitive interface for users to update and view contact information easily.

**In scope**
- S1: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries.
- S2: Implement user roles with access controls, allowing regional coordinators and project managers to view and edit contact records, while executive-level staff can only view.
- S3: Allow users to filter and search for country contacts by country name, contact name, and organization.
- S4: Set up a version history for contact records to track changes made by users, ensuring data integrity.

**Out of scope**
- X1: This release will not include any integration with external databases or API connections to pull in contact information.
- X2: Advanced user analytics or reporting features based on contact data are not included in this release.
- X3: Any functionality related to automatic alerts or notifications regarding contact updates is excluded from this release.

**Assumptions**
- A1: Users have access to the Government CRM with appropriate role-based permissions, which affects how and what they can view and edit.
- A2: Existing contact information is currently stored in the CRM or accessible in a manner that allows users to accurately populate the new 'Country Contacts' section.
- A3: Users are familiar with using CRM systems, thus enabling faster adoption of the new features.

**Definitions**
- D1: 'Primary contact person' means the individual identified as the main point of contact for each government organization in a country, responsible for all communications and engagements.
- D2: 'Intuitive interface' means a user-friendly design that allows individuals to navigate, input, and retrieve information easily without extensive training.
- D3: 'User roles' means defined access levels within the CRM, indicating who can view, edit, or manage contact information.

**Success criteria**
- K1: By the end of Q1, at least 80% of users report improved satisfaction with contact tracking capabilities through a user survey.
- K2: At least 95% of primary contact records are accurately filled within the first month of release, as verified by user input.

Biggest worry: The existing data accuracy may hinder the effectiveness of the new tracking feature.

### Critic · confidence 50

Pre-mortem: A year after launch, a major breach occurred when sensitive diplomatic records containing contact details of primary contacts were inadvertently exposed to unauthorized users. This happened because the access control settings allowed certain project managers to view confidential contact records meant only for regional coordinators, leading to significant diplomatic fallout and damaging relationships with key government partners.

Questions the request leaves open:
- What specific role permissions apply to each type of user, and how will unauthorized access be prevented?
- How will the CRM handle situations when a primary contact person changes, or leaves their position?
- What kinds of data integrity checks will be implemented to validate the accuracy of contact information provided by users?
- How will the system manage and notify users of important changes to contact records, especially in relation to diplomatic sensitivity?
- What processes are in place to ensure that shared contact records do not expose sensitive information or diplomatic relationships across different teams?
- How do we define and ensure the confidentiality of diplomatic contact details, especially when considering different levels of user access?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S2
- Challenge: S2 allows project managers to view and edit contact records, but does not clarify how sensitive records are protected against unauthorized access.
- Failure scenario: A project manager inadvertently edits or exposes sensitive diplomatic contact information, leading to leaks and negative diplomatic consequences.
- Resolution test: What specific roles or conditions restrict project managers from accessing sensitive contact records?

**C2** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not address how contact records are managed when a primary contact changes, potentially leading to outdated or incorrect information being used.
- Failure scenario: A regional coordinator continues to contact a primary person who has left, resulting in ineffective communication and missed opportunities.
- Resolution test: What is the process for updating and managing primary contact records when contacts change?

**C3** · MAJOR · DATA_QUALITY · targets S1
- Challenge: S1 does not specify how data accuracy and integrity will be ensured in the new 'Country Contacts' section, risking outdated or incorrect records being stored.
- Failure scenario: Users enter incorrect information which then propagates through other systems, leading to misinformation about key governmental contacts.
- Resolution test: What data validation mechanisms will be in place to ensure the accuracy of contact information input by users?

**C4** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal fails to define how sensitive diplomatic information will be treated differently from non-sensitive contact information.
- Failure scenario: Sensitive diplomatic contacts are erroneously accessible to all users, causing diplomatic breaches and privacy violations.
- Resolution test: What definitions clarify which contact records are classified as sensitive, and what measures will be in place to control access to these records?

**C5** · MINOR · OPERATIONS · targets GAP
- Challenge: The proposal does not specify how users will be notified of changes to contact records, which is essential for maintaining operational effectiveness across teams.
- Failure scenario: Users in the field are unaware of changes to primary contacts and attempt to reach out to individuals who are no longer the point of contact, hindering operations.
- Resolution test: What formal process is established to notify users of updates or changes to contact records?

**C6** · MINOR · DEFINITIONS · targets GAP
- Challenge: The definitions provided in the proposal do not clarify who is considered authorized to manage contact records, leading to potential overreach or misuse of access.
- Failure scenario: A user, misunderstanding the definition of 'user roles,' edits contact records without proper authority, resulting in inaccurate data being propagated.
- Resolution test: Which roles are explicitly defined as authorized to manage contact records?

Biggest worry: The proposal could lead to unauthorized access and management of sensitive diplomatic contact information.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S2]: This revision clearly defines the access levels for project managers and restricts their ability to edit sensitive contact records, thus protecting sensitive information from unauthorized access.
- **C2** DEFEND (acceptable risk): Updating contact records will require users to manually update information to ensure records are current, recognizing that this is a process that involves user diligence over automation.
- **C3** REVISE (missing decision) [changed S1]: This revision adds specific data validation requirements for the contact information being entered, enhancing the accuracy and integrity of the records stored.
- **C4** REVISE (missing decision) [changed A4, S2]: The new assumption defines what 'sensitive diplomatic contact records' entails, and the edits to S2 clarify how access is controlled based on the sensitivity of contact information.
- **C5** DEFEND (needs human decision): The process for notification of changes to contact records must be defined by organizational policies or determined by existing operational practices, which should be clarified beyond this scope.
- **C6** REVISE (missing decision) [changed D3]: This edit explicitly states which roles are authorized to manage contact records, mitigating the risk of unauthorized access or data manipulation.

Proposal changes: added A4; edited S1, S2, D3
- A4 now reads: Sensitive diplomatic contact records are those marked as classified by the organization's policies, including records involving sensitive communications or engagements.
- S1 now reads: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries, with mandatory fields for name and organization to ensure data accuracy and validation rules in place to check for correct formatting of email and phone number fields.
- S2 now reads: Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view. Sensitive diplomatic contact records will only be editable by authorized personnel defined by the user roles.
- D3 now reads: 'User roles' means defined access levels within the CRM, indicating who can view, edit, or manage contact information. Authorized users who can edit contact records include regional coordinators and specific project managers based on defined criteria.

Biggest worry: Ensuring data quality and the protection of sensitive information is crucial for this feature's success.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** ACCEPT: This clearly defines access levels for different user roles, protecting against unauthorized access. Fact: User roles with access controls are implemented to restrict access based on sensitivity of contact records. Evidence: "Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view."
- **C2** MAINTAIN: The absence of an automated process may lead to outdated contact information, which is a risk in effectiveness.
- **C3** ACCEPT: This ensures that the input data has a basic level of accuracy. Fact: Mandatory fields are enforced, and validation rules for data formatting are established. Evidence: "...with mandatory fields for name and organization to ensure data accuracy and validation rules in place to check for correct formatting of email and phone number fields."
- **C4** MAINTAIN: This does not clearly define what roles these 'authorized personnel' are, leaving ambiguity.
- **C5** ESCALATE: This relies on outside rules or decisions that are not specified.
- **C6** ACCEPT: This explicitly states who is authorized to manage contact records. Fact: Only defined user roles can edit the contact records. Evidence: "Authorized users who can edit contact records include regional coordinators and specific project managers based on defined criteria."

New challenges:

**C7** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The manual updating of contact records could lead to inaccuracies over time, especially if users neglect their duty to update them.
- Failure scenario: A regional coordinator relies on incorrect contact details for a key government contact, leading to failed communications and missed opportunities.
- Resolution test: What is the proposed strategy to ensure contact records are regularly reviewed and updated?

Biggest worry: The reliance on manual updating processes may lead to outdated information and operational inefficiencies.

**Ledger:** raised 7 · open 3 · resolved 3 · escalated 1 · disagreement 0.54 → **continue**

## Round 3

### Proposer · confidence 80

- **C2** DEFEND (acceptable risk): While the absence of an automated process for updating contact records does create some risk, we believe that manual updates will rely on users' diligence and the training they receive. Regular training sessions will be scheduled to ensure users understand the importance of keeping contact details current.
- **C4** REVISE (missing decision) [changed A4, S2]: The revised assumption clarifies what constitutes sensitive diplomatic contact records, and the edits to S2 specify which roles are authorized to manage such records, thereby minimizing ambiguity around confidentiality.
- **C7** REVISE (missing decision) [changed S1]: The proposed strategy includes a notification system to remind users to review and confirm the accuracy of contact information, adding a layer of accountability to reduce potential inaccuracies that arise from manual updates.

Proposal changes: edited S1, S2, A4
- S1 now reads: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries. Users must provide mandatory fields for name and organization to ensure data accuracy, and a notification system will remind users at least every six months to review and confirm the accuracy of contact information. Validation rules will check for correct formatting of email and phone number fields.
- S2 now reads: Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view. Sensitive diplomatic contact records will only be editable by regional coordinators and designated project managers who have received additional authorization.
- A4 now reads: Sensitive diplomatic contact records are defined as those contacts involving classified engagements, communications with embassies, or individuals who require a higher level of access due to confidentiality. Records falling under this definition will include those flagged by the organization's policies.

Biggest worry: Ensuring user diligence in updating contact records may still lead to outdated information.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C2** MAINTAIN: The existing process of manual updates increases the risk of outdated information leading to ineffective communication.
- **C2** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C4** MAINTAIN: While user roles are defined, it remains unclear who qualifies as a 'designated project manager' and the process for determining this.
- **C4** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C7** MAINTAIN: While a notification system is specified, its reliance on user action still leaves the likelihood of inaccuracies in the records.

New challenges:

**C8** · MAJOR · OPERATIONS · targets GAP
- Challenge: The proposal does not specify how users will be notified about changes to contact records.
- Failure scenario: A regional coordinator believes they are contacting the right government representative, but the contact information has changed and they have not been informed, leading to miscommunication.
- Resolution test: What procedures will be in place to ensure users are notified when contact records are updated?

**C9** · BLOCKER · CONFIDENTIALITY · targets S2
- Challenge: S2 does not clarify how sensitive records are protected against unauthorized access, which could lead to a security breach.
- Failure scenario: A project manager attempts to access a sensitive diplomatic contact record due to vague access control policies, potentially exposing classified information.
- Resolution test: What specific measures are in place to protect sensitive records from unauthorized access?

Biggest worry: The risk of confidential contact records being accessed by unauthorized users remains high.

**Ledger:** raised 9 · open 3 · resolved 3 · escalated 3 · disagreement 0.67 → **continue**

## Round 4

### Proposer · confidence 85

- **C7** DEFEND (acceptable risk): While the concern over manual updates is valid, the notification system will still enforce accountability. Regular reviews will encourage users to maintain the accuracy of the records, thus balancing the risk of inaccuracies.
- **C8** REVISE (missing decision) [changed S1]: The added clause ensures that all users are automatically notified by email of any changes made to contact records, helping to minimize miscommunication caused by outdated information.
- **C9** REVISE (missing decision) [changed S2]: The edits clarify that sensitive records will be audited, encrypted, and restricted to authorized users, addressing confidentiality concerns and ensuring compliance with security protocols.

Proposal changes: edited S1, S2
- S1 now reads: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries. Users must provide mandatory fields for name and organization to ensure data accuracy, and a notification system will remind users at least every six months to review and confirm the accuracy of contact information. Additionally, an automatic email notification will be sent to users when any changes are made to contact records, ensuring they are informed and up-to-date. Validation rules will check for correct formatting of email and phone number fields.
- S2 now reads: Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view. Sensitive diplomatic contact records will only be editable by regional coordinators and designated project managers who have received additional authorization. All sensitive records will also be subject to audit logging to track any access or modifications made, and sensitive data will be encrypted at rest and in transit to prevent unauthorized access.

Biggest worry: The reliance on users to update information may still lead to some inaccuracies despite notifications.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C7** MAINTAIN: While the notification system seeks to mitigate inaccuracies, it still places the onus on users to take action, leaving room for potential lapses in updates.
- **C7** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.
- **C8** ACCEPT: This addresses the challenge directly and provides a clear procedure for notifying users. Fact: Users will be automatically notified by email of changes to contact records. Evidence: "an automatic email notification will be sent to users when any changes are made to contact records"
- **C9** ACCEPT: This outlines specific measures in place to protect sensitive records from unauthorized access. Fact: Sensitive records are protected through limited editing rights, audit logging, and encryption. Evidence: "Sensitive diplomatic contact records will only be editable by regional coordinators and designated project managers who have received additional authorization. All sensitive records will also be subject to audit logging to track any access or modifications made, and sensitive data will be encrypted at rest and in transit to prevent unauthorized access."

New challenges:

**C10** · BLOCKER · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify how contact records will be managed when a primary contact changes, leaving process gaps regarding ownership and continuity of information.
- Failure scenario: A key government representative resigns or changes their role, yet the organization fails to update the contact records promptly, leading to confusion and communication breakdown with the new representative.
- Resolution test: What is the process for updating contact records to reflect changes in primary contacts?

Biggest worry: The reliance on user diligence to maintain the accuracy of sensitive contact records leaves room for critical inaccuracies.

**Ledger:** raised 10 · open 1 · resolved 5 · escalated 4 · disagreement 0.48 → **continue**

## Round 5

### Proposer · confidence 85

- **C10** REVISE (missing decision) [changed S1]: The revision clarifies the process for managing contact records when a primary contact changes by introducing an automated workflow to ensure timely updates.

Proposal changes: edited S1
- S1 now reads: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries. Users must provide mandatory fields for name and organization to ensure data accuracy, and a notification system will remind users at least every six months to review and confirm the accuracy of contact information. If a primary contact changes, an automated workflow will assign a current user to review and update the contact record within two weeks of being notified of the change. Additionally, an automatic email notification will be sent to users when any changes are made to contact records, ensuring they are informed and up-to-date. Validation rules will check for correct formatting of email and phone number fields.

Biggest worry: Ensuring timely updates of contact information remains a challenge without user diligence.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C10** ACCEPT: This establishes a clear process for updating contacts when changes occur. Fact: An automated workflow will update records within two weeks. Evidence: "If a primary contact changes, an automated workflow will assign a current user to review and update the contact record within two weeks of being notified of the change."

Biggest worry: There are still unresolved challenges regarding the protection of sensitive data and differences in treatment between sensitive and non-sensitive records.

**Ledger:** raised 10 · open 0 · resolved 6 · escalated 4 · disagreement 0.33 → **converged**

## Final proposal

_This release will improve the tracking and management of primary contact persons for each member country, providing defined roles and protections for sensitive information while implementing notifications for regular reviews and updates to maintain data accuracy, and process continuity when contacts change._

**Core commitments**
- V1: Enable users to track and manage primary contact persons for each country.
- V2: Provide an intuitive interface for users to update and view contact information easily.

**In scope**
- S1: Create a 'Country Contacts' section within the CRM that allows users to record the name, title, email, phone number, and organization of the primary contact person for each of the ~100 member countries. Users must provide mandatory fields for name and organization to ensure data accuracy, and a notification system will remind users at least every six months to review and confirm the accuracy of contact information. If a primary contact changes, an automated workflow will assign a current user to review and update the contact record within two weeks of being notified of the change. Additionally, an automatic email notification will be sent to users when any changes are made to contact records, ensuring they are informed and up-to-date. Validation rules will check for correct formatting of email and phone number fields.
- S2: Implement user roles with access controls, allowing regional coordinators to view and edit all contact records, while project managers can view but only edit non-sensitive contact records, and executive-level staff can only view. Sensitive diplomatic contact records will only be editable by regional coordinators and designated project managers who have received additional authorization. All sensitive records will also be subject to audit logging to track any access or modifications made, and sensitive data will be encrypted at rest and in transit to prevent unauthorized access.
- S3: Allow users to filter and search for country contacts by country name, contact name, and organization.
- S4: Set up a version history for contact records to track changes made by users, ensuring data integrity.

**Out of scope**
- X1: This release will not include any integration with external databases or API connections to pull in contact information.
- X2: Advanced user analytics or reporting features based on contact data are not included in this release.
- X3: Any functionality related to automatic alerts or notifications regarding contact updates is excluded from this release.

**Assumptions**
- A1: Users have access to the Government CRM with appropriate role-based permissions, which affects how and what they can view and edit.
- A2: Existing contact information is currently stored in the CRM or accessible in a manner that allows users to accurately populate the new 'Country Contacts' section.
- A3: Users are familiar with using CRM systems, thus enabling faster adoption of the new features.
- A4: Sensitive diplomatic contact records are defined as those contacts involving classified engagements, communications with embassies, or individuals who require a higher level of access due to confidentiality. Records falling under this definition will include those flagged by the organization's policies.

**Definitions**
- D1: 'Primary contact person' means the individual identified as the main point of contact for each government organization in a country, responsible for all communications and engagements.
- D2: 'Intuitive interface' means a user-friendly design that allows individuals to navigate, input, and retrieve information easily without extensive training.
- D3: 'User roles' means defined access levels within the CRM, indicating who can view, edit, or manage contact information. Authorized users who can edit contact records include regional coordinators and specific project managers based on defined criteria.

**Success criteria**
- K1: By the end of Q1, at least 80% of users report improved satisfaction with contact tracking capabilities through a user survey.
- K2: At least 95% of primary contact records are accurately filled within the first month of release, as verified by user input.
