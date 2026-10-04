# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 3 rounds · 8 model calls (1 repairs)

## Round 1

### Proposer · confidence 70

_This release delivers a new contact tracking feature for government representatives in the CRM system, aimed at project managers and regional coordinators. It enables users to easily identify the appropriate contact person for each member country based on their roles._

**Core commitments**
- V1: Enhance user ability to identify the right contact person for government counterparts based on specific criteria.

**In scope**
- S1: Implement a searchable database that allows users to filter contacts by criteria such as role, ministry, and current engagement status.
- S2: Develop a user interface for project managers and regional coordinators to view and select relevant contacts.
- S3: Integrate contact history to reflect the most active and relevant contacts for current projects and missions.
- S4: Ensure users can view the contact details for the selected representatives, including name, role, and current engagement.
- S5: Establish user permissions so that only authorized personnel can access sensitive contact details.

**Out of scope**
- X1: This release will not include automated suggestions for contacts or any AI-driven features.
- X2: This release will not integrate with external government databases or systems.
- X3: This version will not provide any functionality for tracking engagement history beyond the current contact details.

**Assumptions**
- A1: Users will have appropriate access rights to sensitive contact information depending on their roles.
- A2: The existing CRM infrastructure has the capacity to support a new searchable database feature.
- A3: Users require accurate and up-to-date information about the contacts in their respective countries.

**Definitions**
- D1: "Contact tracking feature" means a system enhancement that allows users to search and filter through government contact records based on predefined criteria.
- D2: "Searchable database" means a collection of contact records that users can query and filter according to specified attributes like role and engagement status.
- D3: "Authorized personnel" means users who have received the necessary approvals to access sensitive information within the CRM.

**Success criteria**
- K1: Achieve a minimum of 80% user satisfaction based on feedback surveys within one month of release regarding the new contact tracking feature.

Biggest worry: The assumptions about user access rights and CRM capacity may not hold true.

### Critic · confidence 60

Pre-mortem: A year after launch, an unauthorized regional coordinator accessed sensitive diplomatic contact details for a sensitive government project, causing diplomatic tensions when the wrong information was shared publicly. This breach occurred because the user permissions set up allowed greater access to contact information than initially intended, resulting in a significant backlash against the organization.

Questions the request leaves open:
- Which specific roles have the necessary access rights to sensitive contact information?
- What criteria determine the authorizations for different user roles to access sensitive information?
- How is the searchability of the database limited to prevent unauthorized access to sensitive contact details?
- What precautions are in place to ensure that only relevant contact history is displayed to users?
- How will changes in personnel roles affect access to contact details, particularly for those leaving or changing roles?
- What procedures are in place to update and maintain the accuracy of contact details within the searchable database?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S5
- Challenge: S5 states that 'only authorized personnel can access sensitive contact details,' but it fails to specify which roles constitute 'authorized personnel.'
- Failure scenario: A project manager accidentally shares sensitive information with a user who lacks the necessary clearance, leading to leaks and potential diplomatic incidents.
- Resolution test: Which specific roles have the necessary access rights to sensitive contact information?

**C2** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify what happens when personnel change roles or leave, potentially leaving gaps in ownership of contact records.
- Failure scenario: When a regional coordinator leaves, their access to contact details remains active, and no one updates the records, leading to confusion and unauthorized access.
- Resolution test: What processes are in place to manage access to sensitive contact details when personnel change roles or leave?

**C3** · MAJOR · DEFINITIONS · targets D3
- Challenge: D3 cites 'authorized personnel' but does not define the criteria for what qualifies someone to be authorized, which could lead to ambiguity.
- Failure scenario: A project manager assumes they are authorized to access sensitive information based on unclear definitions, resulting in unauthorized access and diplomatic issues.
- Resolution test: What criteria determine the authorizations for different user roles to access sensitive information?

**C4** · MAJOR · CONFIDENTIALITY · targets S3
- Challenge: S3 mentions integrating contact history but does not indicate how this historical data will be managed to prevent unauthorized access.
- Failure scenario: A project manager inadvertently views sensitive contact histories of other projects, leading to the sharing of confidential information inappropriately.
- Resolution test: How is the searchability of the database limited to prevent unauthorized access to sensitive contact details?

**C5** · MINOR · DATA_QUALITY · targets GAP
- Challenge: The proposal does not address how outdated or incorrect data within the contact records will be maintained or updated.
- Failure scenario: Users rely on outdated contact details and end up contacting individuals who are no longer in the right role, leading to ineffective communication and project delays.
- Resolution test: What procedures are in place to update and maintain the accuracy of contact details within the searchable database?

**C6** · MINOR · OPERATIONS · targets GAP
- Challenge: There is no mention of user training or support to ensure the system is adopted effectively, which could lead to underutilization.
- Failure scenario: Users find the new feature complex and abandon it, leading to ongoing reliance on outdated methods for contact tracking.
- Resolution test: What training or support will be available to ensure effective adoption of the new contact tracking feature?

Biggest worry: The proposal may create significant risks due to ambiguous definitions and unclear user access controls.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S5]: This edit specifies the roles that are authorized personnel, ensuring clarity about who has access to sensitive information.
- **C2** REVISE (missing decision) [changed X4]: This revision acknowledges that access management will not be automated in this release, and it raises an awareness of responsibility that must be managed outside of the system.
- **C3** REVISE (missing decision) [changed D3]: This edit clarifies the criteria for being classified as authorized personnel, reducing ambiguity regarding access rights.
- **C4** REVISE (missing decision) [changed S3]: This revision specifies that visibility of contact histories will be restricted based on user access, addressing confidentiality concerns.
- **C5** REVISE (missing decision) [changed S4]: This addition establishes a commitment to data quality and sets expectations for maintaining the accuracy of contact records.
- **C6** REVISE (missing decision) [changed S6]: This edit commits to offering training and support to facilitate effective adoption of the new feature.

Proposal changes: added S6, X4; edited S3, S4, S5, D3
- S6 now reads: Provide user training and support materials to ensure users are familiar with the new contact tracking feature and can utilize it effectively.
- X4 now reads: This release will not include any automatic management of access rights when personnel change roles or leave.
- S3 now reads: Integrate contact history in a manner that limits visibility to users based on their access rights, ensuring only authorized personnel can view sensitive histories.
- S4 now reads: Ensure that there is a mechanism in place for regularly updating and verifying the accuracy of contact details in the database.
- S5 now reads: Establish user permissions so that only personnel in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff' can access sensitive contact details.
- D3 now reads: "Authorized personnel" means users who have received the necessary approvals from their direct supervisors to access sensitive information within the CRM.

Biggest worry: The success of user adoption may depend significantly on the effectiveness of training and support provided.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C1** ACCEPT: The proposal clearly specifies which roles have access, thus addressing the concern about unauthorized access. Fact: Roles with access rights to sensitive contact details are 'Project Manager', 'Regional Coordinator', and 'Executive Staff'. Evidence: "S5: Establish user permissions so that only personnel in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff' can access sensitive contact details."
- **C2** ACCEPT: The acknowledgement that access won't be managed automatically raises awareness of the manual process required, which is crucial for ownership. Fact: There will be no automated management of access rights when personnel change roles or leave. Evidence: "X4: This release will not include any automatic management of access rights when personnel change roles or leave."
- **C3** MAINTAIN: The definition does not provide specific roles, so it does not clearly indicate who has authorization.
- **C4** MAINTAIN: The evidence does not specifically outline the exact roles that have rights to view sensitive histories.
- **C5** ACCEPT: The commitment to regularly update and verify the data addresses concerns regarding outdated information. Fact: A mechanism for regularly updating and verifying contact details will be implemented. Evidence: "S4: Ensure that there is a mechanism in place for regularly updating and verifying the accuracy of contact details in the database."
- **C6** ACCEPT: The proposal includes training and support, mitigating the risk of underutilization. Fact: Training and support will be available to help users utilize the new feature effectively. Evidence: "S6: Provide user training and support materials to ensure users are familiar with the new contact tracking feature and can utilize it effectively."

New challenges:

**C7** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal lacks clarity on how access to sensitive contact details will be managed during the transition when personnel leave or change roles.
- Failure scenario: When a regional coordinator leaves, their access remains active and may not get revoked in a timely manner, possibly allowing unauthorized access.
- Resolution test: What processes are in place to manage access rights dynamically when personnel change roles or leave?

Biggest worry: There is ambiguity regarding who qualifies as 'authorized personnel', which could lead to unauthorized access to sensitive information.

**Ledger:** raised 7 · open 3 · resolved 4 · escalated 0 · disagreement 0.46 → **continue**

## Round 3

### Proposer · confidence 85

- **C3** REVISE (missing decision) [changed D3]: This revision clarifies the specific roles that qualify as authorized personnel, removing ambiguity regarding access rights.
- **C4** REVISE (missing decision) [changed S3]: This edit specifies the roles that can view sensitive contact histories, addressing confidentiality concerns and ensuring appropriate access.
- **C7** REVISE (missing decision) [changed S4]: This addition establishes a clear process for managing access rights during personnel changes, reducing the risk of unauthorized access.

Proposal changes: edited S3, S4, D3
- S3 now reads: Integrate contact history in a manner that limits visibility to users based on their access rights, ensuring only 'Project Managers' and 'Regional Coordinators' can view sensitive histories associated with their projects.
- S4 now reads: Ensure that there is a mechanism in place for regularly updating and verifying the accuracy of contact details in the database, including a process for timely revocation of access when personnel change roles or leave.
- D3 now reads: "Authorized personnel" means users in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff', who have received explicit approvals from their direct supervisors to access sensitive information within the CRM.

Biggest worry: Ensuring all specified user roles understand their permissions and the processes in place to maintain data security.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C3** ACCEPT: The definition now specifies that users must receive explicit approvals for access, clearly defining authorization criteria. Fact: Users require explicit supervisory approvals for sensitive information access. Evidence: "'Authorized personnel' means users in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff', who have received explicit approvals from their direct supervisors to access sensitive information within the CRM."
- **C4** ACCEPT: The specification of roles clarifies visibility limits for sensitive histories, addressing prior concerns. Fact: Only specific roles can view sensitive histories. Evidence: "'only 'Project Managers' and 'Regional Coordinators' can view sensitive histories associated with their projects.'"
- **C7** ACCEPT: The commitment to a timely revocation process clarifies ownership during personnel changes. Fact: A process exists for revoking access rights promptly. Evidence: "'a process for timely revocation of access when personnel change roles or leave.'"

Biggest worry: The handling of user permissions remains critical to avoid unauthorized access.

**Ledger:** raised 7 · open 0 · resolved 7 · escalated 0 · disagreement 0.00 → **consensus**

## Final proposal

_This release delivers a new contact tracking feature for government representatives in the CRM system, aimed at project managers and regional coordinators. It enables users to easily identify the appropriate contact person for each member country based on their roles, with defined access controls, user support, and improved clarity on user permissions to maintain data accuracy and facilitate effective use of the system._

**Core commitments**
- V1: Enhance user ability to identify the right contact person for government counterparts based on specific criteria.

**In scope**
- S1: Implement a searchable database that allows users to filter contacts by criteria such as role, ministry, and current engagement status.
- S2: Develop a user interface for project managers and regional coordinators to view and select relevant contacts.
- S3: Integrate contact history in a manner that limits visibility to users based on their access rights, ensuring only 'Project Managers' and 'Regional Coordinators' can view sensitive histories associated with their projects.
- S4: Ensure that there is a mechanism in place for regularly updating and verifying the accuracy of contact details in the database, including a process for timely revocation of access when personnel change roles or leave.
- S5: Establish user permissions so that only personnel in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff' can access sensitive contact details.
- S6: Provide user training and support materials to ensure users are familiar with the new contact tracking feature and can utilize it effectively.

**Out of scope**
- X1: This release will not include automated suggestions for contacts or any AI-driven features.
- X2: This release will not integrate with external government databases or systems.
- X3: This version will not provide any functionality for tracking engagement history beyond the current contact details.
- X4: This release will not include any automatic management of access rights when personnel change roles or leave.

**Assumptions**
- A1: Users will have appropriate access rights to sensitive contact information depending on their roles.
- A2: The existing CRM infrastructure has the capacity to support a new searchable database feature.
- A3: Users require accurate and up-to-date information about the contacts in their respective countries.

**Definitions**
- D1: "Contact tracking feature" means a system enhancement that allows users to search and filter through government contact records based on predefined criteria.
- D2: "Searchable database" means a collection of contact records that users can query and filter according to specified attributes like role and engagement status.
- D3: "Authorized personnel" means users in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff', who have received explicit approvals from their direct supervisors to access sensitive information within the CRM.

**Success criteria**
- K1: Achieve a minimum of 80% user satisfaction based on feedback surveys within one month of release regarding the new contact tracking feature.
