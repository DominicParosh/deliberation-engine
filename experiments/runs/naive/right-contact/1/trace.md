# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `naive` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **cap** after 8 rounds · 27 model calls (14 repairs)

## Round 1

### Proposer · confidence 75

_This release will enhance the Government CRM by adding a dedicated feature for tracking primary contact persons in each member country for various engagement topics. It will be utilized by regional coordinators and project managers to streamline contact management and improve communication efficiency with government counterparts._

**Core commitments**
- V1: Enable tracking of primary contact persons for each member country.
- V2: Provide a user-friendly interface for users to update and manage contact information.

**In scope**
- S1: Create a new section in the CRM specifically for tracking primary contact persons, including fields for name, position, email address, and phone number.
- S2: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed.
- S3: Ensure user access controls are in place, allowing only authorized users to view and edit contact information.
- S4: Include a search function that allows users to filter and find appropriate contacts by country and role.

**Out of scope**
- X1: This release will not include integration with external contact databases or systems.
- X2: This release will not cover historical engagement histories with contacts; it focuses solely on current primary contacts.
- X3: This release will not track secondary or alternative contacts or provide notifications about contact changes.

**Assumptions**
- A1: Users have the necessary permissions to access and update contact information; this enables them to manage contact details effectively.
- A2: The current data structure of the CRM can accommodate the new section for primary contacts without requiring extensive backend modifications.
- A3: There are designated staff members responsible for entering and regularly updating contact information.

**Definitions**
- D1: 'Primary contact person' means the individual identified as the main point of communication for government engagement in a specific country.
- D2: 'User access controls' means the permissions established to restrict and allow user access to different features and data within the CRM.
- D3: 'Search function' means a tool within the CRM that enables users to input criteria and retrieve relevant contacts based on defined fields.

**Success criteria**
- K1: At least 80% of users can successfully find and update contact information within three searches, measured through user feedback and CRM usage analytics.

Biggest worry: The effectiveness of user access controls might not fully prevent unauthorized modifications, potentially compromising data integrity.

### Critic · confidence 40

Pre-mortem: A year after launch, a critical incident occurred when a regional coordinator mistakenly contacted the wrong primary contact in a member country regarding a sensitive diplomatic engagement, due to outdated or incorrect contact details. This not only caused a diplomatic faux pas but also exposed the organization to reputational damage and raised serious concerns about the security and integrity of the contact management process.

Questions the request leaves open:
- What specific user roles have permission to view and edit contact information across different countries?
- How will the system prevent unauthorized access to sensitive contact information, and what safeguards are in place?
- What will be the process for regularly verifying and updating the contact information to ensure data accuracy?
- How will the system handle the situation when someone leaves a role or changes responsibilities, regarding their associated contact information?
- How will the search function prioritize contacts, or will it return multiple matching results?
- What happens if a primary contact's details are missing or incorrect when a user tries to retrieve them?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S3
- Challenge: The proposal does not clearly specify the criteria for user access controls and how they will prevent unauthorized access to sensitive contact information.
- Failure scenario: A project manager accesses and edits a primary contact's information for a sensitive diplomatic relationship without the necessary permissions, leading to a potential disclosure of confidential information.
- Resolution test: What specific roles are authorized to view and edit primary contact information?

**C2** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The term 'primary contact person' is not clearly defined in terms of authority or responsibility, leading to ambiguity in its application.
- Failure scenario: A regional coordinator assumes authority over a primary contact relationship that another team is managing, causing conflicting communications and confusion with government counterparts.
- Resolution test: What specific responsibilities define a 'primary contact person' within the CRM?

**C3** · MAJOR · DATA_QUALITY · targets S4
- Challenge: There is no clear plan for how to ensure data accuracy and regular updates, which is critical for maintaining reliable contact records.
- Failure scenario: A user retrieves outdated contact information, resulting in a failed communication with a government entity while trying to engage on a sensitive matter.
- Resolution test: What is the process established for verifying and updating contact information to ensure its accuracy?

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal lacks a clear outline of who is responsible for data integrity when contacts leave or change roles, leading to potential data management gaps.
- Failure scenario: Following the departure of a primary contact, the regional coordinator inadvertently uses old contact details, resulting in a failed diplomatic outreach.
- Resolution test: What process will the CRM implement to handle updates to contact information when individuals leave or change roles?

**C5** · MINOR · OPERATIONS · targets GAP
- Challenge: There is insufficient detail on how the search function will work, specifically regarding prioritization or filtering criteria, which could affect user experience.
- Failure scenario: Users receive multiple results when searching for a primary contact, causing delays and increasing frustration due to inability to quickly identify the correct contact.
- Resolution test: How will the search function prioritize contacts or handle multiple matches in results?

**C6** · MINOR · DEFINITIONS · targets GAP
- Challenge: The definition of 'user access controls' is vague and does not specify how access levels will be determined or enforced.
- Failure scenario: An executive bypasses normal access protocols to gain insight into sensitive contacts, risking information leaks and breaching confidentiality agreements.
- Resolution test: What specific criteria or guidelines will be used to determine user access controls?

Biggest worry: The lack of clarity around access controls and data integrity could lead to unauthorized access to sensitive contact information.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S3]: The edit specifies the roles authorized to view and edit contact information, establishing clear access controls to safeguard sensitive information.
- **C2** REVISE (missing decision) [changed D1]: The revision clarifies the responsibilities of the primary contact, ensuring that users understand their authority and scope of engagement to prevent conflicting communications.
- **C3** REVISE (missing decision) [changed V2]: Setting a commitment for a dedicated process to regularly audit and verify contact information addresses the data accuracy need directly.
- **C4** REVISE (missing decision) [changed S2]: This edit details the process for managing updates when contacts change roles or leave, which clarifies ownership and responsibility for maintaining accurate data.
- **C5** REVISE (missing decision) [changed S4]: The revision specifies how the search function will prioritize contacts and handle multiple matches, improving user experience and reducing frustration.
- **C6** REVISE (missing decision) [changed D2]: By defining the criteria for user access controls in relation to specific user roles, this change enhances security and adherence to confidentiality.

Proposal changes: edited V2, S2, S3, S4, D1, D2
- V2 now reads: Implement a process whereby designated staff members are responsible for regularly auditing, verifying, and updating contact information to maintain data accuracy.
- S2 now reads: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to update records when individuals leave or change roles, ensuring data integrity.
- S3 now reads: Ensure user access controls are in place, allowing only regional coordinators and project managers to view and edit contact information for primary contacts.
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role, prioritizing results based on the most frequently contacted individuals and displaying a message when multiple contacts meet the search criteria.
- D1 now reads: "Primary contact person" means the individual identified as the main point of communication for government engagement in a specific country, with the responsibility for maintaining current contact information and engaging with government counterparts on relevant issues.
- D2 now reads: "User access controls" means the permissions established to restrict and allow user access to different features and data within the CRM, determined by roles such as regional coordinators, project managers, and executive staff.

Biggest worry: Ensuring clear responsibilities and user access protocols will be critical to maintain data integrity and confidentiality.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C1** MAINTAIN: The current text does not specify the exact roles or permissions and only states that controls will be in place.
- **C2** ACCEPT: This definition clarifies the responsibilities associated with the role, eliminating ambiguity. Fact: The primary contact person maintains current contact information and engages with government counterparts. Evidence: "D1: 'Primary contact person' means the individual identified as the main point of communication for government engagement in a specific country, with the responsibility for maintaining current contact information and engaging with government counterparts on relevant issues."
- **C3** MAINTAIN: The text describes responsibilities but does not specify who these designated staff members are.
- **C4** ACCEPT: This decision clarifies ownership and accountability for maintaining accurate data when roles change. Fact: There is a mandatory process to update records when contacts leave or change roles. Evidence: "S2: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to update records when individuals leave or change roles, ensuring data integrity."
- **C5** MAINTAIN: The text does not specify clear criteria for prioritization or how multiple matches will be handled.
- **C6** ACCEPT: This provides clarity on how access levels are determined, addressing the previous vagueness. Fact: Access controls are defined by user roles. Evidence: "D2: 'User access controls' means the permissions established to restrict and allow user access to different features and data within the CRM, determined by roles such as regional coordinators, project managers, and executive staff."

New challenges:

**C7** · MAJOR · DATA_QUALITY · targets S4
- Challenge: The lack of clarity around who is responsible for auditing and updating contact information means there is a risk of data becoming outdated.
- Failure scenario: Without a defined role for data maintenance, outdated contacts could lead to failures in diplomatic communication, impacting international relations.
- Resolution test: Who is designated to regularly audit and verify contact information?

Biggest worry: Unclear responsibilities for data maintenance and vague access controls could lead to unauthorized access and outdated information.

**Ledger:** raised 7 · open 4 · resolved 3 · escalated 0 · disagreement 0.62 → **continue**

## Round 3

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S3]: The revision specifies the exact roles authorized to access and edit primary contact information, addressing the risk of unauthorized access.
- **C3** REVISE (missing decision) [changed V2]: The revision clarifies which designated staff members are responsible for maintaining data accuracy, thereby addressing the concern regarding data quality.
- **C5** REVISE (missing decision) [changed S4]: The revision specifies the criteria for prioritization and handling of multiple matches in the search function, which improves the user experience.
- **C7** DEFEND (needs human decision): The responsibility for regularly auditing and verifying contact information is a determination that the organization must decide, making this a question for them.

Proposal changes: edited V2, S3, S4
- V2 now reads: Implement a process whereby designated staff members, specifically regional coordinators and project managers, are responsible for regularly auditing, verifying, and updating contact information to maintain data accuracy.
- S3 now reads: Ensure user access controls are in place, allowing only the following roles to view and edit contact information for primary contacts: regional coordinators, project managers, and designated executive staff.
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role, with prioritization criteria based on the frequency of communication and the most relevant roles, displaying a message when multiple contacts meet the search criteria.

Biggest worry: Ensuring that the designated staff consistently maintain contact information for accuracy may require ongoing oversight.

### Critic · confidence 65 · CONTINUE

Rulings:
- **C1** MAINTAIN: This specifies the exact roles authorized to access and edit primary contact information. [Not counted as settled: the sentence you quote leans on 'controls are in place', which names no role, number or rule.]
- **C3** ACCEPT: This outlines who is responsible for auditing and updating contact information. Fact: Designated staff members responsible for maintaining data accuracy are regional coordinators and project managers. Evidence: "V2: Implement a process whereby designated staff members, specifically regional coordinators and project managers, are responsible for regularly auditing, verifying, and updating contact information to maintain data accuracy."
- **C5** MAINTAIN: The text does not provide enough detail to answer the resolution test.
- **C7** ESCALATE: This aspect requires a decision that is beyond the current proposal.

Biggest worry: The ongoing uncertainty regarding who will ultimately manage data accuracy may lead to outdated contacts affecting diplomatic communications.

**Ledger:** raised 7 · open 2 · resolved 4 · escalated 1 · disagreement 0.46 → **continue**

## Round 4

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S3]: The revised item now specifies that user access controls not only define the roles but also establish that access will be bounded by designated territories and responsibilities, minimizing the risk of unauthorized access to sensitive information.
- **C5** REVISE (missing decision) [changed S4]: The revision now clarifies that the search function prioritizes contacts based on communication frequency and relevance to projects, improving user experience and addressing potential frustration from multiple search results.

Proposal changes: edited S3, S4
- S3 now reads: Ensure user access controls are in place, allowing only the following roles to view and edit contact information for primary contacts: regional coordinators, project managers, and designated executive staff, with each role restricted to access within their designated territories and areas of responsibility.
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role, prioritizing contacts based on the frequency of communication and relevance to active projects, and displaying a message indicating when multiple contacts meet the search criteria, with the most frequently contacted appearing at the top.

Biggest worry: The successful implementation of strict user access controls is critical to preventing unauthorized access to sensitive data.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** ESCALATE: The proposal specifies roles but still lacks detailed access control measures and rules for preventing unauthorized access, meaning it remains unaddressed.
- **C5** MAINTAIN: This adequately addresses my test; the criteria for prioritization are now clear. [Not counted as settled: the sentence you quote leans on 'appropriate', which names no role, number or rule.]

New challenges:

**C8** · BLOCKER · OWNERSHIP · targets GAP
- Challenge: The proposal does not specify who is responsible for maintaining the data integrity of contact information or how ongoing management will occur after updates are made by regional coordinators and project managers.
- Failure scenario: After changing roles, a project manager updates a primary contact's information, but nobody monitors or verifies these changes, leading to outdated or incorrect contact records, which creates issues during sensitive communications.
- Resolution test: Who is designated to oversee the ongoing accuracy of primary contact information?

**C9** · MAJOR · DEFINITIONS · targets GAP
- Challenge: The definition of 'data accuracy' is not provided, leading to ambiguity around what conditions must be met for contact information to be considered accurate and current.
- Failure scenario: Users believe they can rely on out-of-date contact information because 'data accuracy' was not well-defined, ultimately leading to errors in diplomatic engagements.
- Resolution test: What specific criteria define 'data accuracy' for primary contact information?

**C10** · MAJOR · COMPLIANCE · targets GAP
- Challenge: There is no mention of how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts.
- Failure scenario: Sensitive personal information regarding diplomats or officials gets mishandled, leading to a compliance breach and potential legal repercussions for the organization.
- Resolution test: What measures are in place to ensure compliance with data protection laws regarding personal contact information?

Biggest worry: Lack of clarity on roles and responsibilities for data accuracy and management may lead to significant operational failures.

**Ledger:** raised 10 · open 4 · resolved 4 · escalated 2 · disagreement 0.65 → **continue**

## Round 5

### Proposer · confidence 70

- **C5** REVISE (missing decision) [changed S4]: The edits now specify how multiple contacts will be prioritized based on recent communication activity, addressing the concern about user experience and clarity in search results.
- **C8** REVISE (missing decision) [changed V3]: This revision clearly identifies who is responsible for maintaining the ongoing accuracy of primary contact information, addressing concerns about data management after updates.
- **C9** REVISE (missing decision) [changed D4]: This edit provides a specific definition for data accuracy, outlining the conditions that must be met to ensure contact records are reliable.
- **C10** DEFEND (needs human decision): This challenge requires input from legal and compliance teams regarding data protection regulations; current wording will remain as it directs attention to potential compliance issues that must be addressed.

Proposal changes: added V3, D4; edited S4
- V3 now reads: A designated data integrity officer will oversee the ongoing accuracy of primary contact information, supported by regional coordinators and project managers who are responsible for making and tracking updates.
- D4 now reads: 'Data accuracy' means that all contact information, including name, position, email address, and phone number, must be current, verified through regular audits by designated staff members at least quarterly, and updated in real-time when changes occur.
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role, prioritizing contacts based on the frequency of communication and relevance to active projects. In cases where multiple contacts meet the search criteria, the system will display a message indicating the presence of multiple matches, sort contacts in descending order of recent communication activity, and provide buttons for users to view all matched contacts.

Biggest worry: Ensuring compliance with data protection laws remains unresolved and critical to the project's success.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C5** MAINTAIN: This does not adequately settle how prioritization is handled.
- **C8** ACCEPT: This provides clarity on data integrity management and addresses my earlier concerns. Fact: A designated data integrity officer oversees data accuracy, with support from regional coordinators and project managers for updates. Evidence: "A designated data integrity officer will oversee the ongoing accuracy of primary contact information, supported by regional coordinators and project managers who are responsible for making and tracking updates."
- **C9** MAINTAIN: This is not defined clearly enough; 'designated staff members' does not name a specific title or role.
- **C10** ESCALATE: This challenge requires a clear input from legal and compliance teams; further actions on compliance must be taken.

New challenges:

**C11** · BLOCKER · COMPLIANCE · targets GAP
- Challenge: The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information.
- Failure scenario: Sensitive personal information regarding diplomats is mishandled due to a lack of defined procedures for data management and compliance, leading to legal repercussions.
- Resolution test: What specific procedures are in place to ensure compliance with data protection laws regarding personal information?

Biggest worry: Compliance with data protection laws remains unaddressed, creating risks of mishandling sensitive information.

**Ledger:** raised 11 · open 3 · resolved 5 · escalated 3 · disagreement 0.57 → **continue**

## Round 6

### Proposer · confidence 70

- **C5** REVISE (missing decision) [changed S4]: The revised wording in S4 now outlines specific criteria on how the search function will handle prioritization and multiple contact matches, ensuring a clearer user experience.
- **C9** REVISE (missing decision) [changed D4]: The revision provides a more specific definition of data accuracy by naming 'designated data integrity officers' as the responsible party, eliminating ambiguity.
- **C11** DEFEND (needs human decision): The proposal requires input from the organization to outline specific measures or procedures for compliance with data protection regulations regarding personal contact information.

Proposal changes: edited S4, D4
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role, prioritizing contacts based on communication frequency and relevance to active projects. In cases where multiple contacts meet the search criteria, the system will display a message indicating the presence of multiple matches, sort contacts in descending order of recent communication activity, and when three or more matches exist, provide buttons for users to view all matched contacts with clear indications of the primary contact for each project.
- D4 now reads: Data accuracy means that all contact information, including name, position, email address, and phone number, must be current, verified quarterly by designated data integrity officers responsible for these records, and updated in real-time when changes occur.

Biggest worry: The definition of compliance measures may still lead to issues unless properly addressed by the organization.

### Critic · confidence 55 · CONTINUE

Rulings:
- **C5** MAINTAIN: The revised wording does not specify what constitutes 'communication frequency' and does not provide clarity on how the sorting mechanism works.
- **C9** MAINTAIN: While the definition includes some specifics, it relies on 'designated data integrity officers', which still lacks naming a precise role responsible for ensuring data integrity.
- **C11** ESCALATE: The lack of clear procedures creates a significant compliance risk that necessitates human decision-making.

New challenges:

**C12** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system.
- Failure scenario: Diplomats' personal contact information is exposed due to inadequate protection measures, leading to potential security breaches and diplomatic fallout.
- Resolution test: What specific data protection measures are in place to safeguard the sensitive personal information of diplomatic contacts?

**C13** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws.
- Failure scenario: Contact information is retained longer than necessary, risking legal exposure for not adhering to data protection regulations, leading to potential fines or legal challenges.
- Resolution test: What is the defined retention period for contact information and how is it managed?

**C14** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify who officially owns the contact data once it is updated by various users, which raises accountability issues.
- Failure scenario: Disputes arise over responsibility and ownership of contact data updates, leading to confusion in data management and maintenance duties.
- Resolution test: Who officially owns the responsibility for maintaining the contact information once updated by regional coordinators and project managers?

**C15** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: There is no process defined for identifying and fixing inaccuracies in the contact database outside regular updates, risking reliance on outdated information.
- Failure scenario: Users come across outdated or incorrect contact information because there is no systematic way to identify and correct inaccuracies, causing operational and diplomatic issues.
- Resolution test: What processes are in place to audit the contact information outside of scheduled updates to ensure ongoing accuracy?

Biggest worry: The proposal lacks critical procedures for ensuring data protection and compliance, which could lead to severe legal consequences.

**Ledger:** raised 15 · open 6 · resolved 5 · escalated 4 · disagreement 0.69 → **continue**

## Round 7

### Proposer · confidence 75

- **C5** REVISE (missing decision) [changed S4]: The edits now specify how contacts will be prioritized based on recent communication activity, addressing the concern about user experience and clarity in search results.
- **C9** REVISE (missing decision) [changed D4]: This revision clarifies the role responsible for maintaining data accuracy and provides specific criteria that define what constitutes accurate contact information.
- **C12** DEFEND (needs human decision): The organization must define specific data protection measures to safeguard sensitive contact information, as this requires compliance with existing legal frameworks and policies.
- **C13** DEFEND (needs human decision): The organization needs to establish a retention policy for contact information to ensure compliance with data protection laws, which is outside the scope of this proposal.
- **C14** REVISE (missing decision) [changed D1]: The revision specifies the ownership of updated contact data, which is crucial for accountability in data management.
- **C15** REVISE (missing decision) [changed S2]: This edit outlines a systematic process for identifying and correcting inaccuracies in contact data, addressing ongoing data quality concerns.

Proposal changes: edited S2, S4, D1, D4
- S2 now reads: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to audit and verify records at least quarterly and implement corrective actions for any inaccuracies identified outside of these updates.
- S4 now reads: Include a search function that allows users to filter and find appropriate contacts by country and role. The search function will prioritize contacts based on the most recent communication activity, sorting contacts in descending order of last communication date, ensuring that users receive the most relevant contact first. In cases where multiple contacts meet the search criteria, the system will display a message indicating the presence of multiple matches, provide buttons for users to view all matched contacts, with the primary contact clearly indicated for each project.
- D1 now reads: 'Primary contact person' means the individual identified as the main point of communication for government engagement in a specific country, who has the responsibility for maintaining current contact information and engaging in government counterparts on relevant issues, with ownership of data updates resting with the regional coordinator responsible for that country.
- D4 now reads: Data accuracy means that all contact information, including name, position, email address, and phone number, must be current and verified by a designated data integrity officer, with updates made in real-time when changes occur and verified quarterly to maintain the reliability of the records.

Biggest worry: There are still open challenges regarding data protection and compliance that require resolution.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C5** ACCEPT: This adequately addresses the resolution test. Fact: Contacts are prioritized by the most recent communication activity. Evidence: "The search function will prioritize contacts based on the most recent communication activity, sorting contacts in descending order of last communication date."
- **C9** ACCEPT: The revision clarifies the criteria for data accuracy sufficiently. Fact: Data accuracy requires current contact info verified by a designated data integrity officer. Evidence: "Data accuracy means that all contact information, including name, position, email address, and phone number, must be current and verified by a designated data integrity officer, with updates made in real-time when changes occur and verified quarterly to maintain the reliability of the records."
- **C12** ESCALATE: This is a compliance issue that needs human input.
- **C13** ESCALATE: This is a compliance issue that requires human decision.
- **C14** ACCEPT: This adequately addresses the resolution test. Fact: Regional coordinators own the responsibility for maintaining data updates. Evidence: "The individual identified as the main point of communication for government engagement in a specific country, who has the responsibility for maintaining current contact information and engaging in government counterparts on relevant issues, with ownership of data updates resting with the regional coordinator responsible for that country."
- **C15** ACCEPT: This sufficiently answers the resolution test. Fact: A mandatory process for auditing and verifying records exists at least quarterly. Evidence: "Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to audit and verify records at least quarterly and implement corrective actions for any inaccuracies identified outside of these updates."

New challenges:

**C16** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: The proposal fails to address specific measures or procedures that will be used to protect sensitive diplomatic contact information from unauthorized access.
- Failure scenario: Sensitive diplomatic contact information is accessed by unauthorized individuals due to inadequately defined protection measures, leading to a security breach and damaging diplomatic relations.
- Resolution test: What specific measures will be implemented to safeguard the sensitive personal information of diplomatic contacts?

**C17** · BLOCKER · COMPLIANCE · targets GAP
- Challenge: Without a defined retention policy for contact information, the proposal risks non-compliance with data protection regulations.
- Failure scenario: Contact information is kept longer than necessary, violating legal requirements and resulting in potential fines or challenges.
- Resolution test: What is the proposed retention period for contact information and how will it be enforced?

Biggest worry: The lack of specific data protection measures for sensitive diplomatic contacts could lead to unauthorized access.

**Ledger:** raised 17 · open 2 · resolved 9 · escalated 6 · disagreement 0.55 → **continue**

## Round 8

### Proposer · confidence 75

- **C16** REVISE (missing decision) [changed S2]: The edits now specify concrete measures to protect sensitive diplomatic information, including role-based authentication and regular audits, which directly address the challenge of unauthorized access.
- **C17** CONCEDE (should not build) [changed X3]: This edit removes the retention policy from the current scope, acknowledging it as a future requirement while focusing on the immediate needs of the release.

Proposal changes: edited S2, X3
- S2 now reads: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to audit, verify, and protect records at least quarterly and implement corrective actions for any inaccuracies identified outside of these updates. Additionally, implement role-based authentication to ensure that only authorized users can access sensitive contact information, regularly audit user access permissions, and monitor data access logs for suspicious activities.
- X3 now reads: This release will not define a specific retention period for contact information; this will be determined in future releases after compliance assessment.

Biggest worry: The challenge of implementing sufficient security measures while balancing user access requirements remains significant.

### Critic · confidence 30 · CONTINUE

Rulings:
- **C16** MAINTAIN: The proposal fails to specify the roles that will be granted access, leaving ambiguity around who can actually view sensitive contact information.
- **C16** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C17** ACCEPT: While this addresses the risk, it indicates that the proposal is not compliant at this stage, which is a significant concern. Fact: The retention period for contact information will be determined in future releases after a compliance assessment. Evidence: "This release will not define a specific retention period for contact information; this will be determined in future releases after compliance assessment."
- **C18** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C19** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C20** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C21** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C22** OPEN_AT_CLOSE: Still open when deliberation ended (cap).
- **C23** OPEN_AT_CLOSE: Still open when deliberation ended (cap).

New challenges:

**C18** · BLOCKER · CONFIDENTIALITY · targets S3
- Challenge: The proposal does not clearly specify the criteria for user access controls and how they will prevent unauthorized access to sensitive contact information, which remains a major risk.
- Failure scenario: Unauthorized access occurs because criteria for access controls are not defined; a non-authorized user views sensitive contact details, leading to security breaches and risk to diplomatic relations.
- Resolution test: What are the specific criteria for user access controls, and how are they enforced?

**C19** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system, leaving a gap in security measures.
- Failure scenario: Sensitive contact information is exposed due to lack of protective measures, potentially compromising diplomatic engagements and damaging relationships.
- Resolution test: What specific measures or procedures are in place for protecting sensitive diplomatic contact information?

**C20** · BLOCKER · COMPLIANCE · targets GAP
- Challenge: The proposal does not mention how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts, which poses legal risks.
- Failure scenario: The organization collects and stores personal data without compliance, leading to violations of data protection laws and incurring penalties.
- Resolution test: What measures are proposed to ensure compliance with data protection regulations for personal information?

**C21** · BLOCKER · COMPLIANCE · targets GAP
- Challenge: The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws, presenting significant legal risks.
- Failure scenario: Contact information is retained longer than legally allowed, which could result in fines or legal action against the organization.
- Resolution test: What will be the process for defining and enforcing a retention policy for contact information?

**C22** · BLOCKER · COMPLIANCE · targets GAP
- Challenge: The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information, risking legal repercussions.
- Failure scenario: There are violations of data protection laws due to unclear compliance processes, leading to audits and potential penalties.
- Resolution test: What measures will be taken to ensure compliance with data protection regulations concerning personal contact information?

**C23** · BLOCKER · OWNERSHIP · targets GAP
- Challenge: The proposal does not specify who is responsible for maintaining the data integrity of contact information or how ongoing management will occur after updates are made, leading to potential data management gaps.
- Failure scenario: After an update is made, no one monitors the integrity of the data, leading to widespread inaccuracies and potential diplomatic miscommunications.
- Resolution test: Who is responsible for ongoing data integrity checks after updates to contact information?

Biggest worry: The proposal still lacks sufficient measures to ensure compliance and protect sensitive information, leading to significant security and legal risks.

**Ledger:** raised 23 · open 7 · resolved 10 · escalated 6 · disagreement 0.64 → **cap**

## Final proposal

_The proposal now includes specific measures to protect sensitive information from unauthorized access and states that a retention policy will be developed in future releases, ensuring compliance planning._

**Core commitments**
- V1: Enable tracking of primary contact persons for each member country.
- V2: Implement a process whereby designated staff members, specifically regional coordinators and project managers, are responsible for regularly auditing, verifying, and updating contact information to maintain data accuracy.
- V3: A designated data integrity officer will oversee the ongoing accuracy of primary contact information, supported by regional coordinators and project managers who are responsible for making and tracking updates.

**In scope**
- S1: Create a new section in the CRM specifically for tracking primary contact persons, including fields for name, position, email address, and phone number.
- S2: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to audit, verify, and protect records at least quarterly and implement corrective actions for any inaccuracies identified outside of these updates. Additionally, implement role-based authentication to ensure that only authorized users can access sensitive contact information, regularly audit user access permissions, and monitor data access logs for suspicious activities.
- S3: Ensure user access controls are in place, allowing only the following roles to view and edit contact information for primary contacts: regional coordinators, project managers, and designated executive staff, with each role restricted to access within their designated territories and areas of responsibility.
- S4: Include a search function that allows users to filter and find appropriate contacts by country and role. The search function will prioritize contacts based on the most recent communication activity, sorting contacts in descending order of last communication date, ensuring that users receive the most relevant contact first. In cases where multiple contacts meet the search criteria, the system will display a message indicating the presence of multiple matches, provide buttons for users to view all matched contacts, with the primary contact clearly indicated for each project.

**Out of scope**
- X1: This release will not include integration with external contact databases or systems.
- X2: This release will not cover historical engagement histories with contacts; it focuses solely on current primary contacts.
- X3: This release will not define a specific retention period for contact information; this will be determined in future releases after compliance assessment.

**Assumptions**
- A1: Users have the necessary permissions to access and update contact information; this enables them to manage contact details effectively.
- A2: The current data structure of the CRM can accommodate the new section for primary contacts without requiring extensive backend modifications.
- A3: There are designated staff members responsible for entering and regularly updating contact information.

**Definitions**
- D1: 'Primary contact person' means the individual identified as the main point of communication for government engagement in a specific country, who has the responsibility for maintaining current contact information and engaging in government counterparts on relevant issues, with ownership of data updates resting with the regional coordinator responsible for that country.
- D2: "User access controls" means the permissions established to restrict and allow user access to different features and data within the CRM, determined by roles such as regional coordinators, project managers, and executive staff.
- D3: 'Search function' means a tool within the CRM that enables users to input criteria and retrieve relevant contacts based on defined fields.
- D4: Data accuracy means that all contact information, including name, position, email address, and phone number, must be current and verified by a designated data integrity officer, with updates made in real-time when changes occur and verified quarterly to maintain the reliability of the records.

**Success criteria**
- K1: At least 80% of users can successfully find and update contact information within three searches, measured through user feedback and CRM usage analytics.

## Orchestrator warnings

- R2: dropped new challenge(s) that repeated an open question: #1 (C1), #3 (C5).
- R3: Critic's ACCEPT of C1 was refused (the sentence you quote leans on 'controls are in place', which names no role, number or rule); recorded as MAINTAIN.
- R4: Critic's ACCEPT of C5 was refused (the sentence you quote leans on 'appropriate', which names no role, number or rule); recorded as MAINTAIN.
- Summarizer output needed coercion after a failed repair; see events.jsonl.
