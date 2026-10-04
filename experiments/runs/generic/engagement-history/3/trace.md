# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **consensus** after 3 rounds · 10 model calls (3 repairs)

## Round 1

### Proposer · confidence 75

_This release will provide project managers with access to the full history of engagement with a country in the Government CRM system before starting a new mission. It will ensure project managers can make informed decisions based on historical data of interactions and initiatives in each member country._

**Core commitments**
- V1: Project managers can view the complete engagement history with each country.

**In scope**
- S1: Provide project managers with a feature to access and view the engagement history of a selected country.
- S2: Display engagement history that includes contact dates, involved personnel, and summary of activities.
- S3: Limit access to engagement history to only project managers and relevant authorized regional coordinators.
- S4: Ensure that engagement history complies with data privacy and sensitivity protocols.

**Out of scope**
- X1: This release will not include features for editing or deleting engagement history.
- X2: This release will not provide additional analytics or insights into engagement history beyond what is displayed.
- X3: This release will not allow access to engagement history for users other than project managers and authorized coordinators.

**Assumptions**
- A1: It is assumed that project managers need the engagement history to make informed decisions before new missions, which is the basis for this feature request.
- A2: It is assumed that engagement histories are stored in the CRM system and are up to date.
- A3: It is assumed that there are no existing legal or organizational barriers preventing project managers from accessing historical engagement data.

**Definitions**
- D1: "engagement history" means a record of all interactions between the organization and the government counterpart, including dates of contact, participants, and summaries of discussions or activities.
- D2: "project managers" means designated personnel responsible for overseeing specific missions or projects within the organization.

**Success criteria**
- K1: Successfully providing access to engagement history to 100% of project managers as measured by system access logs within one month of the release.

Biggest worry: Dependence on the availability of accurate and complete historical engagement data.

### Critic · confidence 40

Pre-mortem: A year after launch, project managers accessed sensitive engagement histories that contained diplomatic communications. One of the project managers mistakenly shared this information in a public forum, leading to a diplomatic incident and damaging relationships with multiple countries. Sensitive engagement records that should have been restricted were not only viewed by unauthorized personnel but also exposed, undermining confidentiality protocols.

Questions the request leaves open:
- How will engagement history be monitored to ensure only authorized users have access?
- What measures are in place to handle changes in project managers or regional coordinators accessing sensitive data?
- What specific data privacy and sensitivity protocols are being followed to protect engagement history?
- How do we define 'relevant authorized regional coordinators' in terms of role and clearance for this access?
- What historical data time frame will project managers have access to regarding engagement histories?
- What processes will be in place to ensure data quality and accuracy of the engagement histories displayed?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S3
- Challenge: S3 limits access to engagement history to project managers and relevant authorized regional coordinators but does not define how unauthorized access is prevented, nor how to ensure those designated as authorized are appropriate.
- Failure scenario: A project manager mistakenly shares sensitive data that was accessed due to a flaw in access control, allowing individuals without proper clearance to view confidential engagement history.
- Resolution test: What mechanisms are in place to monitor and prevent unauthorized access to engagement histories?

**C2** · MAJOR · DATA_QUALITY · targets S2
- Challenge: S2 states the engagement history will display contact dates, involved personnel, and summaries of activities but does not confirm how the quality, accuracy, and consistency of this data will be maintained.
- Failure scenario: Inaccurate or incomplete engagement history leads project managers to make uninformed decisions, resulting in operational failures or diplomatic missteps.
- Resolution test: How will the data quality of engagement histories be ensured before allowing access to project managers?

**C3** · MAJOR · COMPLIANCE · targets S4
- Challenge: S4 mentions compliance with data privacy and sensitivity protocols, but does not specify what those protocols are or outline the necessary steps to comply with legal requirements for accessing personal data.
- Failure scenario: Sensitive data is accessed and shared in violation of legal requirements, resulting in regulatory penalties and loss of trust.
- Resolution test: What specific data privacy and sensitivity protocols will be implemented to ensure compliance?

**C4** · MAJOR · OWNERSHIP · targets GAP
- Challenge: There is no clear ownership delineation for the engagement history data among project managers and regional coordinators, raising concerns about data maintenance and access governance.
- Failure scenario: When a project manager leaves, there is confusion about who holds accountability for maintaining access and security of their engagement history, resulting in unclear data governance and oversight.
- Resolution test: Who is responsible for maintaining the engagement history data and overseeing who has access?

**C5** · MINOR · DEFINITIONS · targets GAP
- Challenge: The term 'relevant authorized regional coordinators' is vague and lacks definition, leading to uncertainty about access rights.
- Failure scenario: A regional coordinator accesses sensitive data without proper clearance due to poorly defined access parameters, leading to data breaches.
- Resolution test: What criteria define a 'relevant authorized regional coordinator' who should have access?

**C6** · MINOR · OPERATIONS · targets GAP
- Challenge: It is unclear how long engagement histories will be kept accessible to project managers and if there are any limitations or guidelines post-access.
- Failure scenario: Without clear retention policies, project managers continue accessing outdated or irrelevant engagement histories, causing confusion and inefficiencies.
- Resolution test: What will be the policy for the retention of engagement history data and how frequently will it be reviewed or updated?

Biggest worry: Unauthorized access to sensitive engagement histories could lead to major diplomatic issues and legal violations.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S3]: The revision clarifies how access is limited and monitored, establishing specific mechanisms to prevent unauthorized access.
- **C2** REVISE (missing decision) [changed S2]: This edit introduces a commitment to maintain the quality and accuracy of the data displayed, minimizing the risk of misinformation.
- **C3** REVISE (missing decision) [changed S4]: This revision specifies the compliance measures and frameworks required, ensuring that legal requirements are followed.
- **C4** REVISE (missing decision) [changed S3]: The edit introduces a responsible role for data governance that clarifies ownership and accountability for data management.
- **C5** REVISE (missing decision) [changed D3]: This definition formalizes the criteria for who qualifies as a 'relevant authorized regional coordinator', reducing ambiguities.
- **C6** REVISE (missing decision) [changed S4]: This ensures clarity on how long engagement histories will be accessible and emphasizes the importance of maintaining current and relevant information.

Proposal changes: added D3; edited S2, S3, S4
- D3 now reads: "relevant authorized regional coordinators" means regional coordinators designated by the Data Steward based on their involvement in or necessity for accessing a specific country’s engagement history.
- S2 now reads: Display engagement history that includes contact dates, involved personnel, and summary of activities, ensuring data quality is maintained through regular audits, validation protocols, and user input verification before information is accessed by project managers.
- S3 now reads: Limit access to engagement history to only project managers and relevant authorized regional coordinators, with designated roles managed by a Data Steward who will oversee data governance, including the maintenance of access rights and accountability for the engagement history.
- S4 now reads: Ensure that engagement history complies with data privacy and sensitivity protocols, with a retention policy stating engagement histories will be accessible for a period of three years from the last engagement, subject to yearly reviews for relevance and compliance.

Biggest worry: There may still be underlying data governance complexities that need further clarification.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C1** MAINTAIN: While access is limited, the proposal does not detail mechanisms to prevent unauthorized access or monitor those granted access.
- **C2** MAINTAIN: While a commitment to data quality has been introduced, specific mechanisms for ensuring accuracy and consistency before access are still not defined.
- **C3** MAINTAIN: The compliance protocols are still not specified, raising concerns about adherence to legal data handling requirements.
- **C4** MAINTAIN: The proposal does not specify how the Data Steward will manage governance and accountability, leaving ownership unclear.
- **C5** ACCEPT: The definition clarifies access rights and removes ambiguity. Fact: Defined criteria for relevant authorized regional coordinators. Evidence: "regional coordinators designated by the Data Steward based on their involvement in or necessity for accessing a specific country’s engagement history."
- **C6** ACCEPT: The updated retention policy provides clarity on the accessibility of engagement history. Fact: Engagement histories have a defined retention period of three years, reviewed yearly for relevance. Evidence: "Ensure that engagement history complies with data privacy and sensitivity protocols, with a retention policy stating engagement histories will be accessible for a period of three years from the last engagement, subject to yearly reviews for relevance and compliance."

New challenges:

**C7** · BLOCKER · CONFIDENTIALITY · targets GAP
- Challenge: There is no indication of the specific protocols or mechanisms in place to prevent unauthorized access to sensitive engagement histories.
- Failure scenario: A project manager can access sensitive negotiation history that should be restricted and inadvertently shares it, causing a diplomatic breach.
- Resolution test: What specific mechanisms ensure that unauthorized access is prevented and monitored?

**C8** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal lacks clear definitions of the existing data privacy and sensitivity protocols which are critical to ensuring compliance with legal requirements.
- Failure scenario: Sensitive engagement history is accessed without understanding the necessary legal protocols, resulting in breaches of compliance and potential legal penalties.
- Resolution test: What are the specific data privacy and sensitivity protocols that will be adhered to for engaging with historical data?

Biggest worry: Unauthorized access control mechanisms may be inadequate, risking exposure of sensitive data.

**Ledger:** raised 8 · open 6 · resolved 2 · escalated 0 · disagreement 0.88 → **continue**

## Round 3

### Proposer · confidence 65

- **C1** REVISE (missing decision) [changed S3]: This revision clarifies how access to engagement history is monitored and provides mechanisms for preventing unauthorized access, addressing both the security of sensitive information and compliance with data governance.
- **C2** REVISE (missing decision) [changed S2]: This edit introduces a specific role for ensuring data quality, detailing a validation process for the engagement history before it is shown to project managers, helping to prevent misinformation.
- **C3** REVISE (missing decision) [changed S4]: This revision specifies adherence to GDPR and organizational data protection policies, clarifying compliance measures to be taken when handling sensitive engagement histories.
- **C4** REVISE (missing decision) [changed S3]: Revising S3 specifies the role of the Data Steward in managing access rights and clarifies responsibilities related to maintaining governance and accountability, addressing ownership concerns.
- **C7** REVISE (missing decision) [changed S3]: The wording now includes specific access control measures that will be implemented by the Data Steward, enhancing security against unauthorized access.
- **C8** REVISE (missing decision) [changed S4]: This edit specifies adherence to GDPR and various national laws, along with a compliance check process that helps to clarify the necessary protocols for accessing sensitive engagement history.

Proposal changes: edited S2, S3, S4
- S2 now reads: Display engagement history that includes contact dates, involved personnel, and summary of activities. Data quality will be maintained through a tiered auditing process, where a designated data quality officer will validate information before access is granted to project managers, ensuring accuracy and consistency.
- S3 now reads: Limit access to engagement history to only project managers and authorized regional coordinators. The Data Steward will implement access control measures that include authentication protocols, logging of access attempts, and a notification system for unauthorized access attempts.
- S4 now reads: Ensure that engagement history complies with data privacy and sensitivity protocols, including adherence to GDPR, national confidentiality laws, and organizational policies. All access will require justification and will be documented, maintaining a compliance check process.

Biggest worry: Ensuring effective implementation of security and compliance measures in a timely manner.

### Critic · confidence 80 · CONCLUDE

Rulings:
- **C1** ACCEPT: The mechanisms for access control are now specified and adequately address the concerns of unauthorized access. Fact: The Data Steward will manage access control with specific measures in place. Evidence: "The Data Steward will implement access control measures that include authentication protocols, logging of access attempts, and a notification system for unauthorized access attempts."
- **C2** ACCEPT: The proposal now specifies a role for ensuring data quality before project managers access engagement histories. Fact: A designated data quality officer will ensure data quality prior to access. Evidence: "Data quality will be maintained through a tiered auditing process, where a designated data quality officer will validate information before access is granted to project managers."
- **C3** ACCEPT: The revisions clarify the necessary compliance measures required for handling sensitive data. Fact: Engagement history will comply with GDPR and national confidentiality laws. Evidence: "Ensure that engagement history complies with data privacy and sensitivity protocols, including adherence to GDPR, national confidentiality laws, and organizational policies."
- **C4** ACCEPT: Ownership and accountability for data management are now adequately clarified. Fact: The Data Steward is responsible for managing access rights and data governance. Evidence: "The Data Steward will implement access control measures..."
- **C7** ACCEPT: The proposal now includes clear mechanisms for monitoring and preventing unauthorized access. Fact: Mechanisms are in place to monitor access, including logging of attempts and notification of unauthorized access. Evidence: "The Data Steward will implement access control measures that include authentication protocols, logging of access attempts, and a notification system for unauthorized access attempts."
- **C8** ACCEPT: The compliance measures now specify adherence to relevant laws, addressing the concerns raised. Fact: Engagement history will comply with GDPR and national confidentiality laws, providing a framework for legal compliance. Evidence: "Ensure that engagement history complies with data privacy and sensitivity protocols, including adherence to GDPR, national confidentiality laws, and organizational policies."

Biggest worry: Despite clarifying mechanisms for access and monitoring, there remains a concern about the potential for mishandling of sensitive data.

**Ledger:** raised 8 · open 0 · resolved 8 · escalated 0 · disagreement 0.00 → **consensus**

## Final proposal

_This release will provide project managers access to the full engagement history with a country and clarify controls around access, data quality, and compliance, ensuring informed decision-making prior to starting new missions. Enhanced security measures and accountability structures will be established to protect sensitive information and ensure compliance with legal requirements._

**Core commitments**
- V1: Project managers can view the complete engagement history with each country.

**In scope**
- S1: Provide project managers with a feature to access and view the engagement history of a selected country.
- S2: Display engagement history that includes contact dates, involved personnel, and summary of activities. Data quality will be maintained through a tiered auditing process, where a designated data quality officer will validate information before access is granted to project managers, ensuring accuracy and consistency.
- S3: Limit access to engagement history to only project managers and authorized regional coordinators. The Data Steward will implement access control measures that include authentication protocols, logging of access attempts, and a notification system for unauthorized access attempts.
- S4: Ensure that engagement history complies with data privacy and sensitivity protocols, including adherence to GDPR, national confidentiality laws, and organizational policies. All access will require justification and will be documented, maintaining a compliance check process.

**Out of scope**
- X1: This release will not include features for editing or deleting engagement history.
- X2: This release will not provide additional analytics or insights into engagement history beyond what is displayed.
- X3: This release will not allow access to engagement history for users other than project managers and authorized coordinators.

**Assumptions**
- A1: It is assumed that project managers need the engagement history to make informed decisions before new missions, which is the basis for this feature request.
- A2: It is assumed that engagement histories are stored in the CRM system and are up to date.
- A3: It is assumed that there are no existing legal or organizational barriers preventing project managers from accessing historical engagement data.

**Definitions**
- D1: "engagement history" means a record of all interactions between the organization and the government counterpart, including dates of contact, participants, and summaries of discussions or activities.
- D2: "project managers" means designated personnel responsible for overseeing specific missions or projects within the organization.
- D3: "relevant authorized regional coordinators" means regional coordinators designated by the Data Steward based on their involvement in or necessity for accessing a specific country’s engagement history.

**Success criteria**
- K1: Successfully providing access to engagement history to 100% of project managers as measured by system access logs within one month of the release.
