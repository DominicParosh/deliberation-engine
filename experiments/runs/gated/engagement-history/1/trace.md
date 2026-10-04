# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 2 rounds · 6 model calls (1 repairs)

## Round 1

### Proposer · confidence 70

_This release will allow project managers to view the complete engagement history with a specific country, ensuring informed decisions prior to initiating new missions. The feature is designed for project managers and regional coordinators using the Government CRM._

**Core commitments**
- V1: Enable project managers to view the complete history of engagement with selected countries.
- V2: Ensure data on engagement history is presented in a clear, accessible format.

**In scope**
- S1: Allow project managers to access engagement history records for any of the ~100 member countries.
- S2: Display engagement history that includes past projects, meeting notes, and communications related to the country.
- S3: Implement a filter option that allows project managers to search engagement history by date range or project type.
- S4: Ensure that only authorized project managers and regional coordinators can access this engagement history data.

**Out of scope**
- X1: Do not include a feature for editing engagement history records in this release.
- X2: Do not provide analytics or insights derived from engagement history data in this release.
- X3: Do not include integration with external databases or systems to fetch additional records.

**Assumptions**
- A1: Project managers have the necessary permissions to view engagement history data, which is essential for them to access this feature.
- A2: All engagement history data is maintained accurately within the CRM, relying on previous data entry processes.
- A3: Users have prior knowledge of how to navigate to the engagement history section in the CRM.

**Definitions**
- D1: "Engagement history" means a chronological record of all interactions, meetings, projects, and communications related to a specific country stored within the CRM.
- D2: "Project managers" means individuals responsible for planning and executing missions who require full context regarding a country's past engagements to make informed decisions.

**Success criteria**
- K1: Achieve an 80% satisfaction rate from project managers regarding accessibility and clarity of engagement history within the first three months of release.

Biggest worry: Data accuracy and completeness of the historical engagement records could impact decision-making.

### Critic · confidence 40

Pre-mortem: A year after launch, project managers were granted access to the full engagement history of a country, but a serious incident occurred when sensitive diplomatic communications were inadvertently disclosed to users who lacked proper clearance. This breach led to diplomatic tensions and compromised ongoing negotiations, resulting in a public relations disaster for the organization.

Questions the request leaves open:
- Who determines what is classified and sensitive in the engagement history records?
- What specific roles or positions are considered authorized project managers?
- How will data accuracy be verified to prevent potential misinformation?
- What safeguards are in place to prevent unintended access to sensitive data by unauthorized users?
- What procedures are in place if a project manager leaves or changes roles to ensure they no longer have access to sensitive engagement histories?
- Is there a limit on how far back engagement history can be viewed to manage data sensitivity?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S4
- Challenge: S4 states that only authorized project managers and regional coordinators can access engagement history data, but it does not specify how 'authorized' is determined, which is crucial for data protection.
- Failure scenario: A project manager accesses sensitive diplomatic meeting notes due to a lack of clear authorization criteria, leading to a data breach.
- Resolution test: Who defines and maintains the authorization criteria for project managers and regional coordinators to access engagement history?

**C2** · MAJOR · DEFINITIONS · targets D1
- Challenge: D1 defines 'engagement history' as a chronological record but does not clarify what types of communications or interactions are included or excluded, potentially leading to inconsistencies.
- Failure scenario: A project manager assumes verbal communications are part of the engagement history, but they are not documented, leading to decisions based on incomplete information.
- Resolution test: What specific types of interactions are included in the definition of engagement history?

**C3** · MAJOR · OWNERSHIP · targets A1
- Challenge: A1 assumes that project managers have the necessary permissions without detailing how permissions are granted or managed, creating risks of unauthorized access.
- Failure scenario: A former project manager retains access to sensitive engagement data after leaving their role, leading to potential misuse of information.
- Resolution test: What is the process for granting and revoking access permissions for project managers?

**C4** · MINOR · OPERATIONS · targets S1
- Challenge: S1 allows project managers to access engagement history for any of the ~100 member countries but does not address how to manage system load or data retrieval during high demand.
- Failure scenario: Several project managers try to access engagement history simultaneously during a peak period, causing system slowdowns or crashes, and preventing timely access to critical information.
- Resolution test: What system performance benchmarks are set to handle simultaneous requests for engagement histories?

**C5** · MINOR · DATA_QUALITY · targets A2
- Challenge: A2 relies on the assumption of accurate data maintenance within the CRM but does not outline how data quality will be monitored and verified.
- Failure scenario: Inaccurate or outdated engagement history misguides project managers, wasting resources and time on ineffective missions.
- Resolution test: What processes are in place to regularly verify and update the accuracy of engagement history data?

**C6** · MINOR · CONFIDENTIALITY · targets D1
- Challenge: D1 does not clarify whether there are any thresholds for what types of engagement histories can be accessed, particularly concerning more sensitive diplomatic records.
- Failure scenario: A project manager inadvertently accesses and uses confidential diplomatic records inappropriately, harming ongoing relations.
- Resolution test: Are there any thresholds or distinctions in access for different types of engagement histories based on their sensitivity?

Biggest worry: The proposal lacks clarity on authorization and data sensitivity, posing a high risk of unintentional breaches.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S4]: The edit specifies that authorization criteria will follow the organization's access control policies, clarifying who can access sensitive data.
- **C2** REVISE (missing decision) [changed D1]: The edit clarifies what constitutes engagement history by explicitly stating which types of communications are included, reducing the risk of misinterpretation.
- **C3** DEFEND (needs human decision): The specifics of how access permissions are granted and maintained depend on organizational procedures and practices, which must be determined by the relevant authorities.
- **C4** DEFEND (needs human decision): System performance benchmarks depend on organizational IT policies and infrastructure capabilities, which must be defined by the relevant technical teams.
- **C5** DEFEND (needs human decision): The process for monitoring and verifying data quality must be established by the organization and is not solely determined by this feature release.
- **C6** REVISE (missing decision) [changed D1]: The revision introduces sensitivity thresholds for access to different types of engagement histories, addressing concerns about the misuse of confidential information.

Proposal changes: edited S4, D1
- S4 now reads: Ensure that only authorized project managers and regional coordinators, as defined by the organization’s access control policies, can access this engagement history data.
- D1 now reads: "Engagement history" means a chronological record of all documented interactions, meetings, projects, and communications related to a specific country stored within the CRM. This includes written communications such as emails and official reports, as well as notes from meetings. Access to engagement histories will vary based on their sensitivity, and more sensitive diplomatic records will have stricter access thresholds.

Biggest worry: Ensuring the integrity and accuracy of sensitive data access in compliance with data protection standards.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: Fact: Access to engagement history is governed by the organization's access control policies. Evidence: "Ensure that only authorized project managers and regional coordinators, as defined by the organization’s access control policies, can access this engagement history data."
- **C2** ACCEPT: Fact: Engagement history includes documented interactions, meetings, projects, and written communications. Evidence: "'Engagement history' means a chronological record of all documented interactions, meetings, projects, and communications... This includes written communications such as emails and official reports, as well as notes from meetings."
- **C3** ESCALATE: How access permissions are granted and revoked depends on organizational procedures, which must be clarified.
- **C4** ESCALATE: Performance benchmarks are determined by organizational IT policy, requiring further clarification.
- **C5** ESCALATE: Data monitoring processes are contingent on organizational policies, which need to be defined.
- **C6** ACCEPT: Fact: Access to engagement histories is subject to sensitivity thresholds. Evidence: "Access to engagement histories will vary based on their sensitivity, and more sensitive diplomatic records will have stricter access thresholds."

Biggest worry: Unclear processes for granting and revoking user permissions leave the system vulnerable to unauthorized access.

**Ledger:** raised 6 · open 0 · resolved 3 · escalated 3 · disagreement 0.40 → **converged**

## Final proposal

_This release will allow project managers to view the complete engagement history with a specific country while ensuring confidentiality through defined access controls, ultimately aiding informed decisions prior to initiating new missions._

**Core commitments**
- V1: Enable project managers to view the complete history of engagement with selected countries.
- V2: Ensure data on engagement history is presented in a clear, accessible format.

**In scope**
- S1: Allow project managers to access engagement history records for any of the ~100 member countries.
- S2: Display engagement history that includes past projects, meeting notes, and communications related to the country.
- S3: Implement a filter option that allows project managers to search engagement history by date range or project type.
- S4: Ensure that only authorized project managers and regional coordinators, as defined by the organization’s access control policies, can access this engagement history data.

**Out of scope**
- X1: Do not include a feature for editing engagement history records in this release.
- X2: Do not provide analytics or insights derived from engagement history data in this release.
- X3: Do not include integration with external databases or systems to fetch additional records.

**Assumptions**
- A1: Project managers have the necessary permissions to view engagement history data, which is essential for them to access this feature.
- A2: All engagement history data is maintained accurately within the CRM, relying on previous data entry processes.
- A3: Users have prior knowledge of how to navigate to the engagement history section in the CRM.

**Definitions**
- D1: "Engagement history" means a chronological record of all documented interactions, meetings, projects, and communications related to a specific country stored within the CRM. This includes written communications such as emails and official reports, as well as notes from meetings. Access to engagement histories will vary based on their sensitivity, and more sensitive diplomatic records will have stricter access thresholds.
- D2: "Project managers" means individuals responsible for planning and executing missions who require full context regarding a country's past engagements to make informed decisions.

**Success criteria**
- K1: Achieve an 80% satisfaction rate from project managers regarding accessibility and clarity of engagement history within the first three months of release.
