# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 5 rounds · 14 model calls (3 repairs)

## Round 1

### Proposer · confidence 75

_This release delivers a new contact management feature for tracking the primary contact in each member country, designed for regional coordinators and project managers. Users will be able to assign and manage primary contact roles, ensuring accurate and searchable records of key personnel across different countries._

**Core commitments**
- V1: Provide a user interface for assigning and managing primary contacts in the Government CRM system.
- V2: Enable search functionality to easily identify and contact the primary person for engagements in each country.

**In scope**
- S1: Add a 'Primary Contact' field to the country contact records in the CRM, allowing users to designate a specific individual as the primary contact.
- S2: Create a user interface for regional coordinators and project managers to view and assign primary contacts for each member country.
- S3: Implement search functionality that allows users to find primary contacts by country name, contact name, and engagement history.
- S4: Ensure data entry validations are in place to maintain the integrity of contact information, including mandatory fields for primary contacts.

**Out of scope**
- X1: This release will not include historical engagement tracking by primary contact; it will only focus on current primary contacts.
- X2: No integration with external systems or databases will be included in this release.
- X3: This release will not address any user permissions or access control for editing contact information.

**Assumptions**
- A1: Users will have the necessary roles, such as regional coordinators and project managers, to manage and assign primary contacts. This supports the need for a primary contact management feature.
- A2: There is an existing database structure in the Government CRM that allows for the addition of new fields without major overhaul, enabling the 'Primary Contact' feature.
- A3: Users will require training or guidance materials on managing primary contacts within the CRM, which means support will be available post-release.

**Definitions**
- D1: 'Primary Contact' means the designated individual in each member country identified as the first point of contact for any engagements or communication.
- D2: 'Search Functionality' means the capacity for users to query and retrieve specific records from the CRM based on criteria such as country name or contact name.

**Success criteria**
- K1: At least 70% of regional coordinators and project managers report being satisfied with the ease of assigning or finding primary contacts, measured through a post-release survey conducted 30 days after the release.

Biggest worry: The clarity of user roles and permissions for editing contact information remains uncertain.

### Critic · confidence 30

Pre-mortem: A year after launch, the new contact management feature mistakenly classified a ministry contact as the primary diplomat for a country, which led to sensitive communications being sent to the wrong person. This resulted in a diplomatic incident when an erroneous engagement invitation reached the contact, who was not the authorized representative, causing a loss of trust and strained relations with that country's government.

Questions the request leaves open:
- Who can edit the primary contact information, and what controls are in place to prevent unauthorized changes?
- How will changes in personnel be managed, such as when a primary contact leaves or changes roles?
- What happens if multiple users attempt to assign different primary contacts for the same country?
- What constitutes a valid primary contact, specifically regarding roles or qualifications?
- How will the search functionality ensure that sensitive information is not misused or exposed to unauthorized users?
- What measures are in place to audit changes to primary contact assignments?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S3
- Challenge: S3 does not specify how the search functionality will safeguard sensitive information, risking exposure of confidential diplomatic records.
- Failure scenario: Regional coordinators accidentally access and view sensitive personnel data of a country's primary contact due to inadequate search permissions, leading to unauthorized knowledge of diplomatic relations.
- Resolution test: What specific user permissions govern access to search results for primary contacts?

**C2** · MAJOR · OWNERSHIP · targets S1, X3
- Challenge: S1 and X3 do not clarify who is responsible for maintaining the integrity of primary contact information and under what circumstances these roles can change.
- Failure scenario: When a primary contact leaves or changes roles, there is no assigned responsibility for updating or correcting the contact records, leading to outdated or incorrect information being used in official engagements.
- Resolution test: What is the defined process for updating primary contact records when personnel changes occur?

**C3** · MAJOR · CONFIDENTIALITY · targets S2, X3
- Challenge: S2 lacks clarity on access control for editing contact information, which can lead to multiple users assigning conflicting primary contacts.
- Failure scenario: Two regional coordinators assign different primary contacts for the same country without an enforced process, producing confusion and conflicting diplomatic engagement approaches.
- Resolution test: What user roles are authorized to edit primary contact information, and how is conflict resolution handled?

**C4** · MINOR · DEFINITIONS · targets D1
- Challenge: D1 is vague about the qualifications necessary for someone to be designated as a 'Primary Contact', potentially leading to confusion or inconsistency.
- Failure scenario: Users randomly assign contacts as primary without a clear understanding of the necessary qualifications, which may lead to assigning the wrong individuals and complicating diplomatic relations.
- Resolution test: What specific criteria must an individual meet to be designated as a 'Primary Contact' in the CRM?

**C5** · MINOR · OPERATIONS · targets A1
- Challenge: A1 assumes users will have the necessary roles, but doesn't specify the required credentials or approval process, which could create operational delays.
- Failure scenario: A project manager without the required approval tries to assign a primary contact, leading to a delay in responding to important diplomatic inquiries.
- Resolution test: What specific roles and approvals are required for users to manage primary contacts?

**C6** · MAJOR · OWNERSHIP · targets X3
- Challenge: X3 explicitly states there's no plan to address user permissions for editing and managing contact information, which is critical for data integrity.
- Failure scenario: Unsanctioned edits to primary contact information by unauthorized personnel lead to miscommunication and diplomatic faux pas, damaging the organization's reputation.
- Resolution test: What permissions and approval mechanisms must be established to regulate changes to primary contact information?

Biggest worry: The absence of defined ownership for primary contact information management could lead to unauthorized changes and diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S3]: The edit clarifies that the search functionality will be controlled by user permissions to prevent unauthorized access to sensitive contact data.
- **C2** REVISE (missing decision) [changed S1]: This revision establishes a clear process for maintaining the integrity of primary contact information, including who is responsible for updates.
- **C3** REVISE (missing decision) [changed S2]: This revision addresses the need for clear roles and protocols regarding editing primary contact information to prevent conflicting assignments.
- **C4** REVISE (missing decision) [changed D1]: This edit specifies the qualifications required to be designated as a 'Primary Contact,' reducing ambiguity and ensuring that users assign appropriate individuals.
- **C5** REVISE (missing decision) [changed A1]: This change clarifies the approval process that users must go through to manage primary contacts, addressing potential operational delays.
- **C6** CONCEDE (should not build) [changed X3]: Training designed to cover the absence of system-level controls in this release will be communicated, and the decision to postpone this functionality will allow us to focus on critical features now.

Proposal changes: edited S1, S2, S3, X3, A1, D1
- S1 now reads: Add a 'Primary Contact' field to the country contact records in the CRM, allowing users to designate a specific individual as the primary contact, with a specified process for assigning and updating primary contacts, which includes the responsibility of regional coordinators.
- S2 now reads: Create a user interface for regional coordinators and project managers to view and assign primary contacts for each member country, with clearly defined roles for who is authorized to edit contact information and a conflict resolution protocol to manage simultaneous edits.
- S3 now reads: Implement search functionality that allows users to find primary contacts by country name, contact name, and engagement history, with safeguards in place to ensure that only authorized users can access sensitive information related to primary contacts, as determined by their user role.
- X3 now reads: This release will not address user permissions or access control for editing contact information, but a plan for such controls will be developed in subsequent releases.
- A1 now reads: Users will have the necessary roles, such as regional coordinators and project managers, to manage and assign primary contacts, with the approval process defined as requiring confirmation from an oversight committee to assign a primary contact.
- D1 now reads: The term 'Primary Contact' means the designated individual in each member country identified as the first point of contact for any engagements or communication, and must meet the qualification criteria of having direct involvement in diplomatic or project-related matters within that country.

Biggest worry: Inadequate clarity on user permissions may still lead to challenges in data integrity.

### Critic · confidence 75 · CONTINUE

Rulings:
- **C1** ACCEPT: This statement clearly outlines that access is controlled by user roles, which directly addresses the concern. Fact: Only authorized users can access sensitive contact information based on their role. Evidence: "with safeguards in place to ensure that only authorized users can access sensitive information related to primary contacts, as determined by their user role."
- **C2** ACCEPT: This clarifies who maintains the integrity of primary contact information. Fact: Regional coordinators are responsible for assigning and updating primary contacts. Evidence: "with a specified process for assigning and updating primary contacts, which includes the responsibility of regional coordinators."
- **C3** ACCEPT: This adequately addresses access controls and conflict resolution for editing records. Fact: Defined roles will manage who can edit contact information, along with a conflict resolution protocol. Evidence: "with clearly defined roles for who is authorized to edit contact information and a conflict resolution protocol to manage simultaneous edits."
- **C4** ACCEPT: This provides specific criteria for persons designated as primary contacts. Fact: A primary contact must have direct involvement in diplomatic or project-related matters. Evidence: "must meet the qualification criteria of having direct involvement in diplomatic or project-related matters within that country."
- **C5** MAINTAIN: The proposal does not provide a clear decision on the roles and permissions required for managing primary contacts.
- **C6** ACCEPT: This acknowledges the absence of user permissions and access controls but plans to address it later. Fact: This feature will not be included in the current release; it will be in future releases. Evidence: "a plan for such controls will be developed in subsequent releases."

Biggest worry: There are still significant gaps in access control and user permissions that may affect data integrity.

**Ledger:** raised 6 · open 1 · resolved 5 · escalated 0 · disagreement 0.09 → **continue**

## Round 3

### Proposer · confidence 85

- **C5** REVISE (missing decision) [changed A1]: This edit specifies the user roles of 'Regional Coordinator' and 'Project Manager' and defines the approval process required to manage primary contacts, which addresses the operational delays raised in the challenge.

Proposal changes: edited A1
- A1 now reads: Users will have the necessary roles, including 'Regional Coordinator' and 'Project Manager', to manage and assign primary contacts. Users must gain approval from their immediate supervisor and confirm their responsibilities in the assignment of a primary contact.

Biggest worry: The main concern remains ensuring that the approval process is consistently followed to prevent operational delays.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C5** MAINTAIN: The absence of a clear delineation of the approval process leaves operational delays unaddressed. This requires definition.
- **C5** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.

New challenges:

**C7** · BLOCKER · OWNERSHIP · targets A1
- Challenge: A1 requires users to gain approval from their supervisor but does not specify the conditions for approval or who can provide it. This uncertainty can lead to improper management of primary contacts.
- Failure scenario: A regional coordinator may seek to assign a primary contact without receiving proper approval, leading to incorrect assignments and diplomatic misunderstandings.
- Resolution test: What specific criteria must the supervisor meet to approve a primary contact assignment?

Biggest worry: The lack of specificity around approval processes for assigning primary contacts leaves room for critical errors.

**Ledger:** raised 7 · open 1 · resolved 5 · escalated 1 · disagreement 0.29 → **continue**

## Round 4

### Proposer · confidence 85

- **C7** REVISE (missing decision) [changed A1]: This edit clarifies the conditions under which a supervisor can approve an assignment, reducing the risk of improper contact management.

Proposal changes: edited A1
- A1 now reads: Users will have the necessary roles, including 'Regional Coordinator' and 'Project Manager', to manage and assign primary contacts. Approval from their immediate supervisor is required, which must be based on a demonstrated need for the primary contact assignment backed by current engagement with the country or project, ensuring the supervisor has adequate knowledge of the individual's qualifications.

Biggest worry: Inadequate clarity around the approval process could still introduce mismanagement risks if supervisors are not properly trained.

### Critic · confidence 75 · CONTINUE

Rulings:
- **C7** MAINTAIN: While there are conditions for supervisor approval, it lacks specific criteria regarding the qualifications or context needed for making an informed decision.

Biggest worry: The lack of specific criteria for supervisor approval could lead to improper management of primary contacts.

**Ledger:** raised 7 · open 1 · resolved 5 · escalated 1 · disagreement 0.29 → **continue**

## Round 5

### Proposer · confidence 75

- **C7** REVISE (missing decision) [changed A1]: This edit specifies the conditions under which a supervisor can approve an assignment, reducing the risk of improper contact management.

Proposal changes: edited A1
- A1 now reads: Users will have the necessary roles, including 'Regional Coordinator' and 'Project Manager', to manage and assign primary contacts. Approval from their immediate supervisor is required to designate a primary contact only if the supervisor is currently managing an active project in that country and has confirmed that the individual being proposed has direct involvement and qualifications related to diplomatic or project-related matters within that country.

Biggest worry: The clarity provided in supervisor approval conditions may still lead to inconsistencies in contact assignment if not properly followed.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C7** MAINTAIN: While the conditions for approval have been clarified, it still lacks specificity regarding the qualifications that the supervisor must assess, creating risk of improper assignments.
- **C7** AUTO_ESCALATE: Maintained 2 times without agreement; handed to human decision-makers.

Biggest worry: The approval process for assigning primary contacts remains vague and could lead to mismanagement.

**Ledger:** raised 7 · open 0 · resolved 5 · escalated 2 · disagreement 0.29 → **converged**

## Final proposal

_This release delivers a new contact management feature for tracking the primary contact in each member country, designed for regional coordinators and project managers, with a specified process for updating and safeguarding sensitive contact data. Users will be able to assign and manage primary contact roles while ensuring the integrity and security of records through defined user roles and responsibilities._

**Core commitments**
- V1: Provide a user interface for assigning and managing primary contacts in the Government CRM system.
- V2: Enable search functionality to easily identify and contact the primary person for engagements in each country.

**In scope**
- S1: Add a 'Primary Contact' field to the country contact records in the CRM, allowing users to designate a specific individual as the primary contact, with a specified process for assigning and updating primary contacts, which includes the responsibility of regional coordinators.
- S2: Create a user interface for regional coordinators and project managers to view and assign primary contacts for each member country, with clearly defined roles for who is authorized to edit contact information and a conflict resolution protocol to manage simultaneous edits.
- S3: Implement search functionality that allows users to find primary contacts by country name, contact name, and engagement history, with safeguards in place to ensure that only authorized users can access sensitive information related to primary contacts, as determined by their user role.
- S4: Ensure data entry validations are in place to maintain the integrity of contact information, including mandatory fields for primary contacts.

**Out of scope**
- X1: This release will not include historical engagement tracking by primary contact; it will only focus on current primary contacts.
- X2: No integration with external systems or databases will be included in this release.
- X3: This release will not address user permissions or access control for editing contact information, but a plan for such controls will be developed in subsequent releases.

**Assumptions**
- A1: Users will have the necessary roles, including 'Regional Coordinator' and 'Project Manager', to manage and assign primary contacts. Approval from their immediate supervisor is required to designate a primary contact only if the supervisor is currently managing an active project in that country and has confirmed that the individual being proposed has direct involvement and qualifications related to diplomatic or project-related matters within that country.
- A2: There is an existing database structure in the Government CRM that allows for the addition of new fields without major overhaul, enabling the 'Primary Contact' feature.
- A3: Users will require training or guidance materials on managing primary contacts within the CRM, which means support will be available post-release.

**Definitions**
- D1: The term 'Primary Contact' means the designated individual in each member country identified as the first point of contact for any engagements or communication, and must meet the qualification criteria of having direct involvement in diplomatic or project-related matters within that country.
- D2: 'Search Functionality' means the capacity for users to query and retrieve specific records from the CRM based on criteria such as country name or contact name.

**Success criteria**
- K1: At least 70% of regional coordinators and project managers report being satisfied with the ease of assigning or finding primary contacts, measured through a post-release survey conducted 30 days after the release.
