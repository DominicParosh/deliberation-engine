# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `naive` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 5 rounds · 17 model calls (6 repairs)

## Round 1

### Proposer · confidence 70

_This release provides project managers with access to the full engagement history of all countries tracked in the Government CRM. It ensures that project managers can make informed decisions based on past interactions before initiating new missions._

**Core commitments**
- V1: Project managers will have access to a detailed engagement history for each country.

**In scope**
- S1: The system will display the engagement history, which includes all recorded contact interactions, project affiliations, and mission details for each country in a user-friendly format.
- S2: The engagement history will be accessible only to users with the role of 'Project Manager' within the system.
- S3: The engagement history will include at least the last five years of data for each country, detailing interactions with government counterparts.
- S4: A filtering option will be added, allowing project managers to search the engagement history by date range and specific types of engagements.

**Out of scope**
- X1: The release will not include any data from countries or engagements that have been marked as confidential or diplomatic under existing data protection policies.
- X2: The system will not provide analytics or insights regarding engagement effectiveness; it will only display raw engagement history.

**Assumptions**
- A1: It is assumed that engagement data is being collected and stored accurately in the CRM system, as the display of this data relies on its existence.
- A2: It is assumed that project managers have the appropriate clearance and permissions to access the engagement history, in line with organizational data protection policies.
- A3: It is assumed that the existing database structure can support extended historical data display without performance issues, which is necessary for the UI implementation.

**Definitions**
- D1: 'Engagement history' means the record of all interactions, communications, projects, and missions involving a country, stored in the CRM and retrievable by project managers.

**Success criteria**
- K1: At least 80% of project managers can successfully access and retrieve engagement history for countries they manage, measured through user feedback and system usage analytics within three months of the release.

Biggest worry: There may be challenges ensuring compliance with data protection policies when displaying sensitive engagement history.

### Critic · confidence 30

Pre-mortem: A year after launch, project managers accessed the engagement history of a country that was marked as confidential but mistakenly included in the system. This caused a significant diplomatic incident when sensitive information reached unauthorized personnel, resulting in a breakdown of trust with that government. The organization faced backlash for failing to protect confidential data, leading to personnel changes and reputational damage.

Questions the request leaves open:
- What criteria determine whether an engagement history record is marked as confidential or diplomatic?
- Which individuals or roles have the authority to oversee the access and use of engagement history data, especially regarding confidentiality?
- What mechanisms are in place to ensure that project managers do not access or receive alerts for historical data flagged as confidential?
- How will the system handle cases where a project manager changes roles or leaves the organization regarding their access to engagement history?
- How are the last five years determined, and what happens if engagements older than that need to be referenced for certain countries?
- What checks are in place to ensure data quality and accuracy in the engagement history being pulled into the CRM?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets X1
- Challenge: The proposal does not clearly define the criteria that determine if an engagement history record is marked as confidential, which could lead to unauthorized access to sensitive data.
- Failure scenario: A project manager accesses a country's engagement history that includes confidential diplomatic records, leading to the unauthorized disclosure of sensitive information during a public briefing.
- Resolution test: What specific criteria are used to classify an engagement record as confidential or diplomatic?

**C2** · MAJOR · OWNERSHIP · targets S2
- Challenge: The proposal does not specify who oversees and manages the role permissions related to accessing engagement history, potentially leading to unauthorized access by users without adequate clearance.
- Failure scenario: A regional coordinator mistakenly requests the engagement history of a country and receives access due to unclear role permissions, resulting in a breach of data protection protocols.
- Resolution test: Who is responsible for managing access rights and permissions related to engagement history data?

**C3** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not address how the system will prevent project managers from seeing or being alerted about records flagged as confidential, risking unauthorized exposure.
- Failure scenario: A project manager receives an alert about an engagement flagged as confidential, leading to the potential mismanagement of sensitive relations with that country.
- Resolution test: What safety mechanisms will be implemented to ensure project managers do not receive alerts regarding confidential records?

**C4** · MAJOR · DEFINITIONS · targets S3
- Challenge: The term 'last five years' is vague as it does not clarify how historical data is chosen or what happens if older engagements need to be retrieved for context.
- Failure scenario: A project manager attempts to reference an important engagement from six years ago that is not included, leading to uninformed decisions in a new mission.
- Resolution test: What are the specific criteria used to define which engagements from the last five years are displayed to project managers?

**C5** · MAJOR · OWNERSHIP · targets A2
- Challenge: The assumption that project managers will have appropriate clearance does not clarify how clearance for sensitive data is managed or monitored after personnel changes.
- Failure scenario: A project manager who is granted access to the engagement history after a clearance change uses confidential information without proper authorization, leading to a security incident.
- Resolution test: What processes ensure that project managers' clearances are regularly reviewed and updated concerning sensitive data access?

**C6** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The proposal lacks details about how the system will ensure the accuracy and quality of the engagement data being displayed.
- Failure scenario: Project managers make decisions based on inaccurate or outdated engagement records, resulting in miscommunication and failed missions with government counterparts.
- Resolution test: What specific measures are in place to ensure the engagement data displayed to project managers is accurate and up-to-date?

Biggest worry: The proposal fails to adequately safeguard sensitive diplomatic records, risking unauthorized exposure and significant diplomatic fallout.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed D2]: By defining 'Confidential record' clearly, we can create a consistent approach to protect sensitive information and prevent unauthorized access.
- **C2** REVISE (missing decision) [changed S2]: Specifying that the Data Governance Team manages role permissions establishes clear accountability in handling sensitive data access.
- **C3** REVISE (missing decision) [changed X3]: This measure ensures project managers are not inadvertently exposed to confidential records, thus protecting sensitive information.
- **C4** REVISE (missing decision) [changed S3]: Clarifying how to handle engagements based on available data while establishing a protocol for limited historical records avoids confusion about context in missions.
- **C5** DEFEND (needs human decision): While the assumption regarding clearance checks is valid, updating the processes for monitoring clearance requires human oversight and policy decisions at the organizational level.
- **C6** REVISE (missing decision) [changed S1]: Implementing monthly reviews by the Data Management Team adds a layer of accountability to maintain the quality and accuracy of displayed engagement data.

Proposal changes: added X3, D2; edited S1, S2, S3
- X3 now reads: The system will not display or alert project managers to any engagement history records marked as confidential. Any engagement flagged as confidential will have restricted visibility and will not be included in search results.
- D2 now reads: 'Confidential record' means any engagement history record marked by authorized personnel as containing sensitive diplomatic information or classified under organizational data protection policies.
- S1 now reads: The system will display the engagement history, which includes all recorded contact interactions, project affiliations, and mission details for each country in a user-friendly format, with a monthly review to ensure data accuracy by the Data Management Team.
- S2 now reads: The engagement history will be accessible only to users with the role of 'Project Manager' within the system, and role permissions will be managed by the Data Governance Team under the oversight of the Chief Information Officer.
- S3 now reads: The engagement history will include data from the last five years, or all available data if fewer than five years exist, excluding any records flagged as confidential.

Biggest worry: Concerns about unauthorized access to sensitive data must be strictly managed.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** MAINTAIN: Lacks specific, clear cut criteria for determining what constitutes a confidential record.
- **C2** ACCEPT: This clarifies who is responsible for managing access rights, addressing the challenge. Fact: The Data Governance Team manages role permissions for accessing engagement history. Evidence: "role permissions will be managed by the Data Governance Team under the oversight of the Chief Information Officer."
- **C3** ACCEPT: The specification ensures project managers are protected from viewing confidential records, addressing the challenge. Fact: Project managers will not see alerts or records flagged as confidential. Evidence: "The system will not display or alert project managers to any engagement history records marked as confidential. Any engagement flagged as confidential will have restricted visibility and will not be included in search results."
- **C4** ACCEPT: This addresses the vagueness around historical data availability, clarifying limits on what can be displayed. Fact: Engagement history data is limited to the last five years unless less data is available. Evidence: "The engagement history will include data from the last five years, or all available data if fewer than five years exist, excluding any records flagged as confidential."
- **C5** ESCALATE: This requires organizational policy regarding clearance checks, which is outside the scope of the proposal.
- **C6** ACCEPT: This specifies a method for ensuring data quality, addressing the challenge. Fact: Monthly reviews by the Data Management Team ensure data accuracy. Evidence: "with a monthly review to ensure data accuracy by the Data Management Team."

New challenges:

**C7** · MAJOR · OWNERSHIP · targets A2
- Challenge: The assumption that project managers have appropriate clearance for engaging with the data lacks clarity on how clearance is monitored post-personnel changes.
- Failure scenario: A project manager who no longer has clearance accesses confidential records, inadvertently leaking sensitive information.
- Resolution test: What processes are in place to review and update project managers' access rights and clearance related to sensitive data?

**C8** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The proposal does not specify how the engagement data will be kept up to date beyond the monthly review, particularly when there are changes in projects or contacts.
- Failure scenario: A project manager retrieves outdated data from the system, leading to ineffective engagement with government counterparts due to previous contact information or project status.
- Resolution test: What specific procedures will be implemented to ensure the engagement data stays current between monthly reviews?

Biggest worry: The monitoring of project manager clearances and the processes for data accuracy between reviews are insufficiently defined.

**Ledger:** raised 8 · open 3 · resolved 4 · escalated 1 · disagreement 0.53 → **continue**

## Round 3

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed D2]: By defining specific criteria for what constitutes a confidential record, we can prevent unauthorized access to sensitive data and provide consistent guidelines for handling these records.
- **C7** DEFEND (needs human decision): This is a key organizational process that must be defined by the Data Governance Team and Chief Information Officer, as it pertains to compliance and security within existing policies.
- **C8** REVISE (missing decision) [changed S5]: By making a decision to implement a notification procedure for data updates, we address how the engagement data will be kept up to date, ensuring that project managers have access to accurate information.

Proposal changes: added S5; edited D2
- S5 now reads: The system will implement a procedure for notifying project managers of any changes to engagement history data, including updates in contact information and project statuses, ensuring that the data is current and accurate between the monthly reviews.
- D2 now reads: 'Confidential record' means any engagement history record that meets the following criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel, or (3) it pertains to ongoing negotiations or engagements that have been designated by leadership as needing restricted visibility for national security or diplomatic sensitivity.

Biggest worry: The successful implementation of the defined criteria for confidentiality and the processes for managing clearance changes will depend heavily on organizational adherence to data governance policies.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** MAINTAIN: The definition does not clearly establish the criteria that authorized personnel must follow, leaving the potential for subjective judgment.
- **C7** ESCALATE: The proposal relies on a process that requires human authority for definition; this remains unresolved.
- **C8** ACCEPT: The addition of a notification procedure addresses the concern regarding data currency adequately. Fact: There is a notification procedure implemented for updates to engagement history data. Evidence: "The system will implement a procedure for notifying project managers of any changes to engagement history data, including updates in contact information and project statuses, ensuring that the data is current and accurate between the monthly reviews."

New challenges:

**C9** · MAJOR · OWNERSHIP · targets A2
- Challenge: The proposal assumes project managers have appropriate clearance, yet does not clarify how access rights are reviewed after role changes.
- Failure scenario: After being reassigned to a different project, a previous project manager retains access to sensitive engagement histories, resulting in unauthorized data access.
- Resolution test: What processes are in place to maintain and review project managers' clearance for engagement history access post-role changes?

**C10** · MAJOR · CONFIDENTIALITY · targets S2
- Challenge: The proposal lacks clarity on how role permissions will be audited to ensure only authorized users access sensitive records.
- Failure scenario: A project manager without required clearance inadvertently accesses confidential engagement records due to inadequate permission management, leading to a breach.
- Resolution test: What audit processes are in place to monitor and manage role permissions for accessing engagement histories?

Biggest worry: A lack of clarity in clearance management and role permissions may lead to unauthorized access to sensitive data.

**Ledger:** raised 10 · open 3 · resolved 5 · escalated 2 · disagreement 0.52 → **continue**

## Round 4

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed D2]: The revised definition for 'Confidential record' now includes clear, specific guidelines for authorized personnel, reducing subjectivity in determining confidentiality and protecting against unauthorized access.
- **C9** DEFEND (needs human decision): The organization must define its processes for reviewing and updating access rights for project managers following any role changes, as this involves compliance with security and governance policies that are outside of our control.
- **C10** REVISE (missing decision) [changed S2]: The revision introduces a specific audit process for monitoring engagement history access permissions, providing clarity on how to ensure that only authorized users have access and preventing potential breaches.

Proposal changes: edited S2, D2
- S2 now reads: The engagement history access permissions will be managed by the Data Governance Team and will include a quarterly audit process to ensure only authorized users can access sensitive records, with documentation of any access granted.
- D2 now reads: 'Confidential record' means any engagement history record that meets the following specific criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel with clear written documentation outlining the reasons and authorizations for confidentiality, or (3) it pertains to ongoing negotiations or engagements that have been designated by leadership with clear guidelines regarding restricted visibility for national security or diplomatic sensitivity.

Biggest worry: Ensuring ongoing compliance with data protection standards and management of role permissions will require active oversight.

### Critic · confidence 35 · CONTINUE

Rulings:
- **C1** ESCALATE: The definition still does not clearly establish the specific criteria authorized personnel must follow, leaving room for potential subjectivity.
- **C9** ESCALATE: Specific processes for maintaining and reviewing clearance after role changes need to be defined as they involve compliance with governance policies.
- **C10** MAINTAIN: However, it does not clarify how permissions will specifically be monitored or enforced, which could lead to unauthorized access.

New challenges:

**C11** · BLOCKER · CONFIDENTIALITY · targets D2
- Challenge: The definition of 'Confidential record' remains subjective as it relies on interpretation by authorized personnel, leading to potential unauthorized access.
- Failure scenario: A project manager accesses sensitive data based on their interpretation of confidentiality criteria, which leads to a significant data breach and diplomatic fallout.
- Resolution test: What objective and clear criteria are established for personnel to determine if a record should be marked confidential?

**C12** · BLOCKER · OWNERSHIP · targets A2
- Challenge: The proposal assumes project managers have appropriate clearance without specifying how clearance is monitored after role changes, risking unauthorized access to sensitive information.
- Failure scenario: A project manager who is reassigned retains access to confidential engagement histories, exposing sensitive information and leading to a security incident.
- Resolution test: What specific processes are in place to ensure that project managers' clearance is revoked or reviewed following a change in roles?

**C13** · MAJOR · CONFIDENTIALITY · targets X1
- Challenge: The out-of-scope exclusion of confidential records does not ensure that project managers will not encounter flagged records inadvertently.
- Failure scenario: Despite the exclusion process, a project manager sees references to engagements flagged as confidential due to poor record-keeping, leading to confusion and potential data breaches.
- Resolution test: How will the system prevent any inadvertent access to or display of even referenced confidential records to project managers?

**C14** · MAJOR · DATA_QUALITY · targets K1
- Challenge: The success criteria rely on user feedback without defining how usage analytics will measure successful access to the engagement history, leaving ambiguity in how effectiveness is evaluated.
- Failure scenario: Without defined metrics, the organization cannot determine if project managers have effectively accessed and used the engagement history, leading to reliance on anecdotal evidence and unmeasured risks.
- Resolution test: What specific usage metrics will be tracked to evaluate the success of engagement history access for project managers?

**C15** · MAJOR · DEFINITIONS · targets S3
- Challenge: 'Last five years' is not clearly defined in terms of data retrieval criteria, posing risks when older engagements are needed for decision-making.
- Failure scenario: A project manager is unable to access critical engagement history older than five years, preventing informed decision-making on a sensitive mission, leading to operational failures.
- Resolution test: What specific process is in place to retrieve engagement histories that extend beyond the defined five-year limit?

**C16** · MAJOR · COMPLIANCE · targets X3
- Challenge: The out-of-scope statement does not address whether there are any retention policies or audit trails for sensitive engagement records that might be exempt from visibility rules.
- Failure scenario: Engagements marked as confidential might remain in the system indefinitely without the necessary audit trails for accountability, risking continuity problems in management oversight.
- Resolution test: What retention and audit trail policies are in place for any data that is retained in the CRM?

Biggest worry: Multiple critical definitions and processes remain ambiguous, risking unauthorized access to sensitive data.

**Ledger:** raised 16 · open 7 · resolved 5 · escalated 4 · disagreement 0.71 → **continue**

## Round 5

### Proposer · confidence 82

- **C10** REVISE (missing decision) [changed S2]: The revision clarifies that the Data Governance Team is responsible for quarterly audits of user access rights, detailing the logging process for access attempts to prevent unauthorized access.
- **C11** REVISE (missing decision) [changed D2]: The revision specifies that confidentiality marking requires documented approval from a manager, providing clearer and more objective criteria for determining what constitutes a confidential record.
- **C12** DEFEND (needs human decision): The access clearance for project managers is dependent on organizational policies and human decisions, particularly regarding monitoring and revoking access after role changes, which must be clarified within the organization.
- **C13** REVISE (missing decision) [changed S4]: This revision specifies that the system will actively prevent any references to confidential records from appearing, enhancing data security by eliminating the potential for confusion or accidental access.
- **C14** REVISE (missing decision) [changed K1]: The revision clarifies that success will be measured by tracking specific usage metrics, including the number of access attempts and successful record retrievals.
- **C15** REVISE (missing decision) [changed S3]: The revision establishes a clear process for retrieving engagement histories beyond the five-year limit based on its relevance, thus allowing for better decision-making.
- **C16** REVISE (missing decision) [changed X3]: This revision addresses retention policies explicitly, ensuring there is a clear mechanism for accountability regarding sensitive engagement records.

Proposal changes: edited S2, S3, S4, X3, D2, K1
- S2 now reads: The engagement history access permissions will be managed by the Data Governance Team, which will conduct quarterly audits of user access rights, logging all access attempts and authorization changes to ensure only authorized users can access sensitive records.
- S3 now reads: The engagement history will include data from the last five years, or all available data if fewer than five years exist, with a process established for retrieving older engagement records based on project relevance determined by the Data Governance Team.
- S4 now reads: The system will implement security features that prevent any references to confidential records from being displayed in search results or engagement history views, ensuring no inadvertent exposure occurs.
- X3 now reads: The system will maintain retention policies for confidential engagement records and implement audit trails that log the retention of any confidential data, ensuring accountability in data management practices.
- D2 now reads: 'Confidential record' means any engagement history record that meets the following specific criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel in writing with documented approval from a manager, or (3) it pertains to ongoing negotiations or engagements which have been designated as confidential by leadership with specific visibility restrictions.
- K1 now reads: At least 80% of project managers can successfully access and retrieve engagement history for countries they manage, with success measured by system usage analytics tracking number of access attempts and completed records retrieved within three months of the release.

Biggest worry: Incomplete clarity on the enforcement of confidentiality measures could expose sensitive information.

### Critic · confidence 70 · CONCLUDE

Rulings:
- **C10** MAINTAIN: While quarterly audits are mentioned, the evidence does not specify how active monitoring and enforcement of role permissions will be managed.
- **C10** OPEN_AT_CLOSE: Still open when deliberation ended (consensus).
- **C11** ACCEPT: The revised definition provides clearer criteria that decreases subjectivity for marking records as confidential. Fact: Confidential records require documented approval to be marked, providing a clearer standard than previously stated. Evidence: "'Confidential record' means any engagement history record that meets the following specific criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel in writing with documented approval from a manager,..."
- **C12** ESCALATE: The assumption about project manager clearance lacks a defined process for monitoring access rights after role changes.
- **C13** ACCEPT: The system has a mechanism to prevent inadvertent exposure, addressing the concern sufficiently. Fact: The system will actively prevent unauthorized exposure of confidential records from appearing in views or searches. Evidence: "The system will implement security features that prevent any references to confidential records from being displayed in search results or engagement history views, ensuring no inadvertent exposure occurs."
- **C14** ACCEPT: Defined success criteria clarify usage metrics that will be tracked to evaluate access. Fact: Success is defined with a threshold of 80% access success to engagement histories based on usage analytics. Evidence: "At least 80% of project managers can successfully access and retrieve engagement history for countries they manage, with success measured by system usage analytics tracking number of access attempts and completed records retrieved within three months of the release."
- **C15** ACCEPT: The criteria for accessing older data is now established to allow for informed decision-making. Fact: Engagement history data from the last five years can be retrieved, with a process for accessing older data based on relevance to projects. Evidence: "The engagement history will include data from the last five years, or all available data if fewer than five years exist, with a process established for retrieving older engagement records based on project relevance determined by the Data Governance Team."
- **C16** ACCEPT: Defined retention and audit trail policies enhance compliance with accountability measures. Fact: The system will log retention of confidential engagement records to ensure accountability. Evidence: "The system will maintain retention policies for confidential engagement records and implement audit trails that log the retention of any confidential data, ensuring accountability in data management practices."

Biggest worry: The monitoring of user access rights might still lead to unauthorized access if processes for tracking changes in role assignments are not clearly defined.

**Ledger:** raised 16 · open 1 · resolved 10 · escalated 5 · disagreement 0.40 → **consensus**

## Final proposal

_This release provides project managers with access to the detailed engagement history of all countries tracked in the Government CRM, with updated identities and processes defined to enhance confidentiality and data management practices. Core functionalities include controlled access to engagement history, detailed user role management, and a clear process for maintaining data integrity over time while ensuring compliance with data protection policies._

**Core commitments**
- V1: Project managers will have access to a detailed engagement history for each country.

**In scope**
- S1: The system will display the engagement history, which includes all recorded contact interactions, project affiliations, and mission details for each country in a user-friendly format, with a monthly review to ensure data accuracy by the Data Management Team.
- S2: The engagement history access permissions will be managed by the Data Governance Team, which will conduct quarterly audits of user access rights, logging all access attempts and authorization changes to ensure only authorized users can access sensitive records.
- S3: The engagement history will include data from the last five years, or all available data if fewer than five years exist, with a process established for retrieving older engagement records based on project relevance determined by the Data Governance Team.
- S4: The system will implement security features that prevent any references to confidential records from being displayed in search results or engagement history views, ensuring no inadvertent exposure occurs.
- S5: The system will implement a procedure for notifying project managers of any changes to engagement history data, including updates in contact information and project statuses, ensuring that the data is current and accurate between the monthly reviews.

**Out of scope**
- X1: The release will not include any data from countries or engagements that have been marked as confidential or diplomatic under existing data protection policies.
- X2: The system will not provide analytics or insights regarding engagement effectiveness; it will only display raw engagement history.
- X3: The system will maintain retention policies for confidential engagement records and implement audit trails that log the retention of any confidential data, ensuring accountability in data management practices.

**Assumptions**
- A1: It is assumed that engagement data is being collected and stored accurately in the CRM system, as the display of this data relies on its existence.
- A2: It is assumed that project managers have the appropriate clearance and permissions to access the engagement history, in line with organizational data protection policies.
- A3: It is assumed that the existing database structure can support extended historical data display without performance issues, which is necessary for the UI implementation.

**Definitions**
- D1: 'Engagement history' means the record of all interactions, communications, projects, and missions involving a country, stored in the CRM and retrievable by project managers.
- D2: 'Confidential record' means any engagement history record that meets the following specific criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel in writing with documented approval from a manager, or (3) it pertains to ongoing negotiations or engagements which have been designated as confidential by leadership with specific visibility restrictions.

**Success criteria**
- K1: At least 80% of project managers can successfully access and retrieve engagement history for countries they manage, with success measured by system usage analytics tracking number of access attempts and completed records retrieved within three months of the release.
