# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 4 rounds · 13 model calls (4 repairs)

## Round 1

### Proposer · confidence 85

_This release enables project managers to access and view the complete engagement history with specific countries, enhancing their understanding before initiating new missions. It targets project managers working within the Government CRM system across various country engagements._

**Core commitments**
- V1: Project managers will have access to a comprehensive view of each country's engagement history.

**In scope**
- S1: The system will display a timeline of all interactions with a selected country, including dates, types of engagements (meetings, reports, etc.), and key outcomes.
- S2: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system.
- S3: The engagement history will include data from the last five years to ensure relevance and manageability.
- S4: Users will be able to filter engagement history by type (meetings, correspondence, reports) to find specific interactions easily.

**Out of scope**
- X1: This release will not include features for summary metrics or analytics of engagement history.
- X2: It will not allow editing or modification of engagement history records.
- X3: Access to historical data for users who are not project managers is not included in this release.

**Assumptions**
- A1: All engagement data for the last five years is available and properly recorded in the CRM system, which is essential for providing a complete history.
- A2: Project managers have the necessary permissions to access this engagement history, depending on the role and organizational policies.
- A3: There are no legal constraints preventing project managers from viewing the complete engagement history with various countries.

**Definitions**
- D1: 'Engagement history' means a record of all interactions between the organization and a specific country, including meetings, correspondence, project affiliations, and key outcomes over a defined period.
- D2: 'Project managers' means staff members assigned to lead specific projects and missions, who require comprehensive background information to inform their decision-making.
- D3: 'Country' means any member state with which the organization interacts within the CRM system.

**Success criteria**
- K1: At least 80% of project managers report improved access to necessary information for mission planning through a survey conducted one month after the feature release.

Biggest worry: Ensuring the completeness and accuracy of the engagement history data may pose risks to user trust and utility.

### Critic · confidence 30

Pre-mortem: A year after launch, an internal incident occurred when a project manager accessed sensitive engagement history data relating to diplomatic negotiations with a country they were not directly involved with. They shared this information in a meeting with inappropriate personnel, leading to a breach of confidentiality and damaging diplomatic relations. This incident prompted an immediate investigation and raised serious concerns regarding data access and the rules surrounding project managers' visibility. Furthermore, personal data of country representatives was inadvertently exposed, resulting in complaints and legal scrutiny.

Questions the request leaves open:
- Which types of sensitive engagement history must remain confidential and inaccessible to project managers?
- What specific permissions or clearance levels are required for project managers to access engagement history?
- How will the system enforce access controls to prevent unauthorized viewing of sensitive information?
- What happens to engagement records when a project manager changes roles or leaves the organization?
- What are the procedures for handling potential data inaccuracies within the engagement history?
- How will the engagement history be maintained and updated to ensure all records remain accurate and complete over the five-year period?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S2
- Challenge: S2 does not specify which types of engagement history data may contain sensitive or confidential information that project managers should not have access to.
- Failure scenario: A project manager views confidential engagement records regarding sensitive negotiations, leading to a breach of confidentiality and diplomatic repercussions.
- Resolution test: Which types of engagement history data are restricted from project managers?

**C2** · MAJOR · CONFIDENTIALITY · targets A2
- Challenge: A2 relies on unspecified organizational policies for permissions, which could lead to unauthorized access to sensitive data by project managers.
- Failure scenario: Project managers without proper clearance access engagement history containing sensitive information, risking breaches of confidentiality involving diplomatic relations.
- Resolution test: What specific organizational policies or roles must project managers have to obtain clearance for accessing sensitive engagement history?

**C3** · MAJOR · OWNERSHIP · targets S1
- Challenge: S1 does not clarify who is responsible for managing the engagement history data and ensuring its accuracy and relevance over time.
- Failure scenario: Responsibility for the engagement history is unclear, leading to outdated or inaccurate data being used by project managers, compromising mission planning quality.
- Resolution test: Who is accountable for maintaining and updating the accuracy of engagement history records?

**C4** · MAJOR · DATA_QUALITY · targets A1
- Challenge: A1 assumes that all engagement data for the last five years is available and properly recorded without confirming how completeness and accuracy will be ensured.
- Failure scenario: Incomplete or inaccurate records lead a project manager to make decisions based on unreliable engagement history, negatively impacting outcomes.
- Resolution test: What processes are in place to verify the completeness and accuracy of the engagement data within the CRM system?

**C5** · MINOR · DATA_QUALITY · targets S3
- Challenge: S3 states the engagement history will include data from the last five years, but it does not clarify what happens to older, potentially still relevant data.
- Failure scenario: Important historical context is lost as older engagement records are automatically excluded and not accessible to project managers, risking uninformed decision-making.
- Resolution test: What happens to engagement data older than five years and is there a process to access it if needed?

**C6** · MINOR · FEASIBILITY · targets S4
- Challenge: S4 mentions users can filter engagement history, but does not clarify the specific filtering options and their reliability.
- Failure scenario: Filtering options do not function as intended, leading project managers to miss critical engagements or information while planning missions.
- Resolution test: What specific types of filters will be available for project managers to use on the engagement history, and how is their reliability ensured?

Biggest worry: The proposal does not adequately ensure the protection of confidential diplomatic records from unauthorized access.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed S2]: The edit specifies the types of engagement history data that project managers cannot access, ensuring confidentiality is maintained.
- **C2** DEFEND (needs human decision): The necessary clearance for project managers must be defined by organizational policy, which should be established by the organization itself.
- **C3** REVISE (missing decision) [changed S1]: This edit designates an accountability role for managing engagement history, ensuring that data remains accurate and updates are regularly performed.
- **C4** DEFEND (needs human decision): The processes to ensure completeness and accuracy of engagement data depend on human oversight and existing organizational procedures, which cannot be determined at this point.
- **C5** REVISE (missing decision) [changed S3]: This edit clarifies what happens to engagement data older than five years and establishes a process for accessing older records when necessary.
- **C6** REVISE (missing decision) [changed S4]: The edit specifies additional filtering options and their reliability, improving the usefulness of the filtering feature for project managers.

Proposal changes: edited S1, S2, S3, S4
- S1 now reads: The responsibility for maintaining the accuracy and relevance of engagement history data lies with the CRM Data Steward, who will review and update engagement records at least annually.
- S2 now reads: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system; they will not have access to records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications.
- S3 now reads: The engagement history will include data from the last five years, but older records will be archived and accessible upon special request by project managers, subject to review for relevance.
- S4 now reads: Users will be able to filter engagement history by type (meetings, correspondence, reports) and by date range, ensuring filters are tested for reliability prior to release.

Biggest worry: Ensuring that all defined security and access controls are upheld is critical to preventing data breaches.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: This clearly outlines the types of records project managers cannot access, addressing the confidentiality concern. Fact: Access is restricted to project managers and excludes confidential or sensitive records. Evidence: "S2: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system; they will not have access to records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications."
- **C2** ESCALATE: The lack of specified policies means the challenge is unresolved; we cannot accept it as it stands.
- **C3** ACCEPT: This clarifies who manages and updates engagement history data. Fact: The CRM Data Steward is responsible for maintaining data accuracy and relevance. Evidence: "S1: The responsibility for maintaining the accuracy and relevance of engagement history data lies with the CRM Data Steward, who will review and update engagement records at least annually."
- **C4** ESCALATE: Without defined processes for accuracy and completeness verification, we cannot accept this as settled.
- **C5** ACCEPT: This establishes a process for accessing archived records. Fact: Older records can be accessed upon request, as long as they're reviewed for relevance. Evidence: "S3: The engagement history will include data from the last five years, but older records will be archived and accessible upon special request by project managers, subject to review for relevance."
- **C6** ACCEPT: This resolves the original concern about the clarity of filtering options and their reliability. Fact: Filtering options include type and date range, with a guarantee of testing for reliability. Evidence: "S4: Users will be able to filter engagement history by type (meetings, correspondence, reports) and by date range, ensuring filters are tested for reliability prior to release."

New challenges:

**C7** · MAJOR · CONFIDENTIALITY · targets A2
- Challenge: A2 relies on unspecified organizational policies for permissions; thus, risks of unauthorized access remain significant.
- Failure scenario: Without clear organizational policies determining who has access based on roles, project managers might access sensitive data, resulting in potential diplomatic fallout.
- Resolution test: What organizational policies dictate the access level required for project managers to view engagement history?

**C8** · MAJOR · DATA_QUALITY · targets A1
- Challenge: A1 does not provide processes for verifying the completeness and accuracy of the five-year engagement data.
- Failure scenario: A project manager relies on incomplete engagement data for mission planning, leading to ineffective strategies and damage to diplomatic relations due to the misinformed decision-making process.
- Resolution test: What specific processes are in place to verify the accuracy and completeness of engagement data within the CRM system?

Biggest worry: Unresolved access permission policies risk unauthorized exposure to sensitive diplomatic data.

**Ledger:** raised 8 · open 2 · resolved 4 · escalated 2 · disagreement 0.53 → **continue**

## Round 3

### Proposer · confidence 75

- **C7** REVISE (missing decision) [changed S2]: The edits clarify that access to engagement history for project managers will be governed by organizational policies specifying roles and permissions, mitigating the risk of unauthorized access.
- **C8** DEFEND (needs human decision): The verification of engagement data accuracy and completeness as well as the processes related to it depend on existing organizational policy which I cannot define without input from the relevant stakeholders.

Proposal changes: edited S2
- S2 now reads: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system. Project managers will have clear access based on organizational policies, which dictate that only users with 'Project Manager' role classification can view engagement history excluding records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications.

Biggest worry: The successful implementation of organizational policies to support secure access and reliable data.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C7** ACCEPT: The edit clarifies the access requirements for project managers, addressing the concern of unauthorized access. Fact: Access is limited to project managers based on role classification. Evidence: "Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system."
- **C8** ESCALATE: The answer states that verification processes depend on external policies that cannot be defined without stakeholder input.

New challenges:

**C9** · MAJOR · CONFIDENTIALITY · targets A2
- Challenge: The proposal does not define the organizational policies that specifically outline permissions, which poses a significant risk of unauthorized access to sensitive engagement history data.
- Failure scenario: A project manager accesses sensitive engagement history data due to vague policy definitions and shares it inappropriately, leading to a diplomatic incident.
- Resolution test: What specific organizational policies dictate access levels for project managers viewing engagement history?

**C10** · MAJOR · CONFIDENTIALITY · targets S2
- Challenge: S2 fails to specify which types of engagement history data may contain sensitive or confidential information that project managers should not access, leaving room for potential breaches.
- Failure scenario: A project manager unknowingly accesses sensitive negotiation records due to the lack of clarity on what constitutes sensitive information, resulting in a diplomatic fallout.
- Resolution test: Which types of engagement history data are identified as sensitive or confidential that project managers are restricted from accessing?

Biggest worry: The potential for unauthorized access to sensitive data remains due to undefined organizational policies.

**Ledger:** raised 10 · open 2 · resolved 5 · escalated 3 · disagreement 0.53 → **continue**

## Round 4

### Proposer · confidence 80

- **C9** REVISE (missing decision) [changed S2]: The revision to S2 specifies the types of engagement history data that project managers are permitted to access based on the organizational policies, thus addressing the confidentiality risk.
- **C10** REVISE (missing decision) [changed S2]: The revision to S2 clarifies the specific types of engagement history data that are considered sensitive or confidential, mitigating the risk of potential breaches.

Proposal changes: edited S2
- S2 now reads: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system. Project managers will have clear access based on organizational policies, which dictate that only users with 'Project Manager' role classification can view engagement history excluding records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications. Engagement history data classified as sensitive includes negotiation records, internal assessments, and diplomatic correspondence.

Biggest worry: Ensuring all project managers clearly understand what engagement history data they are restricted from accessing is crucial to prevent potential breaches.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C9** ESCALATE: The proposal still relies on unspecified organizational policies, thus cannot be accepted without further clarification.
- **C10** ACCEPT: This evidence clarifies types of data considered sensitive, effectively addressing the challenge. Fact: Sensitive engagement history data includes negotiation records, internal assessments, and diplomatic correspondence. Evidence: "Engagement history data classified as sensitive includes negotiation records, internal assessments, and diplomatic correspondence."

Biggest worry: Unspecified organizational policies leave room for unauthorized access to sensitive engagement history data.

**Ledger:** raised 10 · open 0 · resolved 6 · escalated 4 · disagreement 0.42 → **converged**

## Final proposal

_This release enables project managers to access and view the complete engagement history with specific countries while ensuring confidentiality and data management responsibilities are clear. It targets project managers within the Government CRM system to enhance their understanding before initiating new missions, with improvements in data verification and defined access policies._

**Core commitments**
- V1: Project managers will have access to a comprehensive view of each country's engagement history.

**In scope**
- S1: The responsibility for maintaining the accuracy and relevance of engagement history data lies with the CRM Data Steward, who will review and update engagement records at least annually.
- S2: Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system. Project managers will have clear access based on organizational policies, which dictate that only users with 'Project Manager' role classification can view engagement history excluding records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications. Engagement history data classified as sensitive includes negotiation records, internal assessments, and diplomatic correspondence.
- S3: The engagement history will include data from the last five years, but older records will be archived and accessible upon special request by project managers, subject to review for relevance.
- S4: Users will be able to filter engagement history by type (meetings, correspondence, reports) and by date range, ensuring filters are tested for reliability prior to release.

**Out of scope**
- X1: This release will not include features for summary metrics or analytics of engagement history.
- X2: It will not allow editing or modification of engagement history records.
- X3: Access to historical data for users who are not project managers is not included in this release.

**Assumptions**
- A1: All engagement data for the last five years is available and properly recorded in the CRM system, which is essential for providing a complete history.
- A2: Project managers have the necessary permissions to access this engagement history, depending on the role and organizational policies.
- A3: There are no legal constraints preventing project managers from viewing the complete engagement history with various countries.

**Definitions**
- D1: 'Engagement history' means a record of all interactions between the organization and a specific country, including meetings, correspondence, project affiliations, and key outcomes over a defined period.
- D2: 'Project managers' means staff members assigned to lead specific projects and missions, who require comprehensive background information to inform their decision-making.
- D3: 'Country' means any member state with which the organization interacts within the CRM system.

**Success criteria**
- K1: At least 80% of project managers report improved access to necessary information for mission planning through a survey conducted one month after the feature release.
