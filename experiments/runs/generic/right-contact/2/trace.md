# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 3 rounds · 10 model calls (3 repairs)

## Round 1

### Proposer · confidence 75

_This release will implement a mechanism for tracking the primary contact person for each country within the Government CRM system. It is aimed at regional coordinators and project managers who need to identify the appropriate contacts for communication and engagement._

**Core commitments**
- V1: Implement a feature that allows users to designate a primary contact for each country.
- V2: Provide a streamlined interface to update and view primary contact information.

**In scope**
- S1: Allow regional coordinators to set and edit the primary contact person for each country in the system.
- S2: Display the primary contact information prominently on each country profile within the CRM.
- S3: Enable project managers to view the list of primary contacts while browsing through country records.
- S4: Implement a search function that enables users to quickly find the primary contact for a selected country.

**Out of scope**
- X1: This release will not include integration with external databases for contact information.
- X2: This release will not support multi-language capabilities for contact information display.
- X3: This release will not include any automated alerts or notifications regarding contact changes.

**Assumptions**
- A1: It is assumed that each country will have only one designated primary contact person, which impacts the design of contact assignment.
- A2: It is assumed that all users of the CRM have the necessary permissions to edit country contact information based on established organizational policies.
- A3: It is assumed that current country records already contain basic information about contact entities, on which this feature will build.

**Definitions**
- D1: 'primary contact' means the designated individual responsible for communication on behalf of the organization within a specific country.
- D2: 'user roles' means the classification of CRM users (regional coordinators, project managers) with specific permissions related to country contact management.

**Success criteria**
- K1: At least 80% of regional coordinators report improved ability to identify primary contacts in a user satisfaction survey conducted three months after release.

Biggest worry: The assumption about having only one primary contact per country may not hold true for all countries, leading to potential gaps in contact assignment.

### Critic · confidence 40

Pre-mortem: A year after launch, the primary contact tracking feature caused a serious incident when regional coordinators attempted to reach out to a newly appointed country representative. The CRM displayed outdated contact information due to lack of oversight on updates. A sensitive diplomatic communication went to the wrong person, threatening relations and causing embarrassment to the organization.

Questions the request leaves open:
- What happens if a primary contact leaves or changes roles?
- How will permissions be managed to ensure only authorized users can edit contact information?
- What safeguards are in place to ensure the accuracy of primary contact information?
- What procedures exist for updating the primary contact information to prevent outdated records?
- What happens when a country has a more complex scenario with multiple relevant contacts?
- How are users informed about changes to primary contact information?

New challenges:

**C1** · BLOCKER · OWNERSHIP · targets S1, S2
- Challenge: The proposal does not specify how changes to the primary contact information will be managed when personnel leave or change roles.
- Failure scenario: A regional coordinator attempts to contact a primary contact who has left the organization, only to find they have no ability to change or update this information in the CRM, resulting in misguided outreach.
- Resolution test: What is the procedure for updating or reassigning the primary contact when they leave or change roles?

**C2** · MAJOR · CONFIDENTIALITY · targets S1, S4
- Challenge: The proposal lacks clarity on who can see and edit primary contact information across different user roles. This could lead to unauthorized changes.
- Failure scenario: A project manager without proper permissions gains access to sensitive country contact information and makes unauthorized changes, leading to confusion and potential data leaks.
- Resolution test: What specific permissions are required for users to edit and view primary contact information?

**C3** · MAJOR · DATA_QUALITY · targets A3
- Challenge: The assumption that current country records contain basic contact information does not address potential inaccuracies or omissions in those records.
- Failure scenario: An attempt to set a primary contact based on inaccurate existing information leads to further errors in the engagement process.
- Resolution test: How will the accuracy and completeness of existing contact records be validated before this feature is implemented?

**C4** · MINOR · OPERATIONS · targets X3
- Challenge: The proposal does not address how users will be notified of changes to primary contacts, which could lead to confusion and outdated interactions.
- Failure scenario: Regional coordinators are unaware of a change to a primary contact and continue to communicate with the outdated contact, undermining timely engagements.
- Resolution test: What mechanism will notify users of updates to primary contact information?

**C5** · MINOR · DEFINITIONS · targets D1
- Challenge: The definition of 'primary contact' is not detailed enough to avoid ambiguity in its application across different contexts or scenarios.
- Failure scenario: Users interpret 'primary contact' differently, leading to inconsistencies in the information entered and confusion over who the actual point of contact is.
- Resolution test: Is 'primary contact' defined as strictly the single individual responsible for communication on behalf of the organization within a specific country?

**C6** · MINOR · OWNERSHIP · targets A2
- Challenge: The assumption about user permissions lacks specificity on how these permissions are established and enforced within the organization.
- Failure scenario: Users attempt to access or edit country contact records without appropriate permissions, leading to data integrity issues.
- Resolution test: What specific organizational policies govern user permissions regarding the editing of contact information?

Biggest worry: The proposal does not prevent outdated contact information from causing serious diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S1]: The edit clarifies the responsibility for updating primary contact information when personnel changes occur. This decision ensures that accurate contact information is maintained in the CRM.
- **C2** REVISE (missing decision) [changed D2]: The edit specifies user permissions for editing and viewing contact information, addressing the potential for unauthorized changes by clearly defining user roles.
- **C3** DEFEND (needs human decision): The accuracy and completeness of existing contact records require validation that must be conducted according to the organization's policies and procedures before implementing this feature.
- **C4** REVISE (missing decision) [changed S5]: This edit adds a new scope item that establishes a notification mechanism, providing clarity on how users will be informed of changes to primary contact information.
- **C5** REVISE (missing decision) [changed D1]: The edit enhances the definition of 'primary contact' to clarify the role's responsibilities, which reduces ambiguity and ensures consistent understanding among users.
- **C6** DEFEND (needs human decision): Establishing and enforcing user permissions regarding the editing of contact information must be determined by the organization's existing policies.

Proposal changes: added S5; edited S1, D1, D2
- S5 now reads: Implement a notification mechanism to alert users when primary contact information has been updated, ensuring that regional coordinators and project managers are aware of any changes.
- S1 now reads: Allow regional coordinators to set and edit the primary contact person for each country in the system; if the primary contact leaves or changes roles, a designated administrator will be responsible for reassigning the primary contact to ensure up-to-date information.
- D1 now reads: 'primary contact' means the designated individual responsible for communication on behalf of the organization within a specific country and designated by the regional coordinator; this individual is expected to be the point of contact for all engagements related to that country.
- D2 now reads: 'user roles' means the classification of CRM users (regional coordinators, project managers) with specific permissions related to country contact management; regional coordinators can edit contact information, while project managers can only view it.

Biggest worry: Ensuring strict adherence to user permissions to prevent unauthorized access and edits.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C1** ACCEPT: This clearly defines the process for maintaining accuracy in primary contact information. Fact: A designated administrator is responsible for updating primary contact information when personnel changes occur. Evidence: "if the primary contact leaves or changes roles, a designated administrator will be responsible for reassigning the primary contact to ensure up-to-date information."
- **C2** ACCEPT: This specification clarifies the permissions for editing and viewing primary contact information. Fact: Regional coordinators can edit; project managers can only view contact information. Evidence: "regional coordinators can edit contact information, while project managers can only view it."
- **C3** ESCALATE: The reliance on human decision for validation of existing records leaves a gap in assurance for data quality.
- **C4** ACCEPT: This satisfactorily addresses user notifications regarding primary contact changes. Fact: There will be a notification mechanism to alert users of updates. Evidence: "Implement a notification mechanism to alert users when primary contact information has been updated, ensuring that regional coordinators and project managers are aware of any changes."
- **C5** ACCEPT: This definition reduces ambiguity in interpreting primary contact roles. Fact: Primary contact is clearly defined with responsibilities. Evidence: "'primary contact' means the designated individual responsible for communication on behalf of the organization within a specific country and designated by the regional coordinator."
- **C6** ESCALATE: User permissions require a clear rule from organizational policy, which remains unconfirmed.

New challenges:

**C7** · BLOCKER · DATA_QUALITY · targets A3
- Challenge: The proposal does not detail how to ensure the accuracy and completeness of contact records before the feature is implemented, which is critical for preventing misinformation.
- Failure scenario: If outdated or inaccurate contact records are not validated before implementation, regional coordinators may rely on incorrect information, leading to diplomatic miscommunications.
- Resolution test: What specific process will be followed to validate the accuracy and completeness of existing contact records?

**C8** · BLOCKER · OWNERSHIP · targets A2
- Challenge: User permissions for editing contact information remain unclear and require definitive organization-wide rules.
- Failure scenario: Without clear rules on user permissions, unauthorized users might alter or access sensitive information, risking data integrity and confidentiality.
- Resolution test: What specific organizational policies dictate user permissions for editing primary contact information?

Biggest worry: The lack of confirmed processes for data quality and user permissions poses significant risks for the feature's success.

**Ledger:** raised 8 · open 2 · resolved 4 · escalated 2 · disagreement 0.56 → **continue**

## Round 3

### Proposer · confidence 75

- **C7** DEFEND (needs human decision): The accuracy and completeness of contact records will require input from the organization to define the validation process.
- **C8** DEFEND (needs human decision): The definition of user permissions for editing contact information must be established by organizational policies and cannot be decided in this proposal.

Proposal changes: none

Biggest worry: Ensuring the accuracy of contact records before the feature goes live is critical to avoid miscommunications.

### Critic · confidence 20 · CONTINUE

Rulings:
- **C7** ESCALATE: The proposal does not specify a definitive process for validating existing contact records, relying on undefined input from the organization.
- **C8** ESCALATE: The proposal does not provide established user permissions for editing contact information, depending on policies outside this proposal.

Biggest worry: The lack of clarity and established processes for validating contact information and user permissions jeopardizes the feature's integrity.

**Ledger:** raised 8 · open 0 · resolved 4 · escalated 4 · disagreement 0.56 → **converged**

## Final proposal

_This release will implement a mechanism for tracking the primary contact person for each country within the Government CRM system, ensuring accurate and timely updates. It is aimed at regional coordinators and project managers who need to identify appropriate contacts for communication and engagement effectively._

**Core commitments**
- V1: Implement a feature that allows users to designate a primary contact for each country.
- V2: Provide a streamlined interface to update and view primary contact information.

**In scope**
- S1: Allow regional coordinators to set and edit the primary contact person for each country in the system; if the primary contact leaves or changes roles, a designated administrator will be responsible for reassigning the primary contact to ensure up-to-date information.
- S2: Display the primary contact information prominently on each country profile within the CRM.
- S3: Enable project managers to view the list of primary contacts while browsing through country records.
- S4: Implement a search function that enables users to quickly find the primary contact for a selected country.
- S5: Implement a notification mechanism to alert users when primary contact information has been updated, ensuring that regional coordinators and project managers are aware of any changes.

**Out of scope**
- X1: This release will not include integration with external databases for contact information.
- X2: This release will not support multi-language capabilities for contact information display.
- X3: This release will not include any automated alerts or notifications regarding contact changes.

**Assumptions**
- A1: It is assumed that each country will have only one designated primary contact person, which impacts the design of contact assignment.
- A2: It is assumed that all users of the CRM have the necessary permissions to edit country contact information based on established organizational policies.
- A3: It is assumed that current country records already contain basic information about contact entities, on which this feature will build.

**Definitions**
- D1: 'primary contact' means the designated individual responsible for communication on behalf of the organization within a specific country and designated by the regional coordinator; this individual is expected to be the point of contact for all engagements related to that country.
- D2: 'user roles' means the classification of CRM users (regional coordinators, project managers) with specific permissions related to country contact management; regional coordinators can edit contact information, while project managers can only view it.

**Success criteria**
- K1: At least 80% of regional coordinators report improved ability to identify primary contacts in a user satisfaction survey conducted three months after release.
