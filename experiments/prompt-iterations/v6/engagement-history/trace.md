# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **converged** after 2 rounds · 6 model calls (1 repairs)

## Round 1

### Proposer · confidence 75

_This release will enable project managers to access the complete engagement history with a country, ensuring informed decision-making before initiating new missions. It will provide a user-friendly interface to retrieve and review this information within the Government CRM for a select number of countries._

**Core commitments**
- V1: Project managers will have access to the full engagement history for each country within the CRM before starting new missions.
- V2: The system will display user-friendly summaries of engagement history, including dates, project affiliations, and relevant notes.

**In scope**
- S1: Project managers can view the engagement history of up to 10 selected countries at a time in the CRM.
- S2: Engagement history includes records of previous missions, contacts made, and notes about interactions for each country.
- S3: The CRM will provide a visual timeline format for engagement history, making it easy to understand the history at a glance.
- S4: Users can filter engagement history by date range and type of engagement (e.g., meetings, emails, reports).

**Out of scope**
- X1: This release will not integrate engagement data from external systems or sources.
- X2: The feature will not provide real-time updates or notifications about ongoing engagements.
- X3: Analysis or suggestions based on engagement history will not be included in this release.

**Assumptions**
- A1: Users accessing this feature are all designated project managers within the organization.
- A2: All necessary historical engagement data is already captured and stored within the CRM database.
- A3: Users have the appropriate access permissions to view engagement history for the selected countries.

**Definitions**
- D1: "Engagement history" means a chronological record of all interactions, projects, and communications related to a specific country within the CRM.
- D2: "User-friendly interface" means a navigable and intuitively designed interface that allows users to easily access and understand the engagement history.

**Success criteria**
- K1: At least 80% of project managers report satisfaction with the ease of access and clarity of the engagement history within the first month of release, measured through user feedback surveys.

Biggest worry: The risk that critical engagement history data is incomplete or not properly entered in the CRM could undermine the feature's value.

### Critic · confidence 40

Pre-mortem: A year after the launch, it was discovered that project managers were accessing sensitive engagement history that contained confidential diplomatic information pertaining to countries, leading to a significant data breach. A project manager inadvertently shared parts of this data during a presentation to unauthorized personnel, resulting in a diplomatic incident and loss of trust with the affected country.

Questions the request leaves open:
- Which roles may access the engagement history for each country?
- What specific data within the engagement history is sensitive and restricted?
- What are the consequences if data is shared or accessed inappropriately?
- How do we ensure that the engagement history is accurate and up to date?
- What safeguards will be in place to prevent unauthorized access to sensitive data?
- How will the system handle requests from project managers who may change roles or leave the organization?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1
- Challenge: The proposal does not restrict which project managers can access sensitive engagement history, which may include confidential information.
- Failure scenario: A project manager who previously worked in a sensitive role accesses past engagement records of a country, exposing sensitive diplomatic discussions during a team meeting unknowingly to unauthorized personnel.
- Resolution test: Which roles have access to the engagement history for each country?

**C2** · MAJOR · DEFINITIONS · targets D1
- Challenge: The definition of 'engagement history' is too broad and fails to specify what types of records could be sensitive and must be protected.
- Failure scenario: Due to the vague definition, a project manager accesses and shares detailed records of diplomatic communications, leading to a confidentiality breach.
- Resolution test: Specify which types of records are included in the engagement history and classify their sensitivity.

**C3** · MAJOR · OWNERSHIP · targets A3
- Challenge: The assumptions state that users have the appropriate access permissions but do not specify how these permissions are determined and maintained.
- Failure scenario: A project manager without the necessary clearance unintentionally accesses sensitive diplomatic records of a country, leading to a major leak.
- Resolution test: Outline the process for granting, reviewing, and revoking access permissions for project managers.

Biggest worry: Uncontrolled access to sensitive engagement history may lead to breaches of confidentiality and diplomatic incidents.

**Ledger:** raised 3 · open 3 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed S1]: The edit clarifies that project managers' access to engagement history is subject to security clearance, thus preventing unauthorized access to sensitive information.
- **C2** REVISE (missing decision) [changed D1]: The revision explicitly details the types of records included in engagement history while highlighting the potential for sensitivity, which helps to better define the scope of access and the types of protections needed.
- **C3** REVISE (missing decision) [changed A3]: This edit provides a clear guideline on how permissions are maintained and established, thus reducing the risk of unauthorized access to sensitive diplomatic records.

Proposal changes: edited S1, A3, D1
- S1 now reads: Project managers can view the engagement history of up to 10 selected countries at a time in the CRM, contingent upon their assigned role and appropriate security clearance as defined in organizational policy.
- A3 now reads: Users have the appropriate access permissions, determined and maintained through an established protocol within the organization that defines clearance levels for accessing engagement history data.
- D1 now reads: "Engagement history" means a chronological record of all interactions, projects, and communications related to a specific country within the CRM, including but not limited to: meeting notes, official correspondence, project reports, and any other documentation categorized as sensitive or confidential.

Biggest worry: Ensuring the user access control effectively prevents unauthorized access to sensitive engagement records.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C1** ACCEPT: This answer specifies that access is based on security clearance, which appropriately restricts exposure. Fact: Access is contingent upon assigned role and security clearance. Evidence: "Project managers can view the engagement history of up to 10 selected countries at a time in the CRM, contingent upon their assigned role and appropriate security clearance as defined in organizational policy."
- **C2** ACCEPT: This definition now includes specific types of records, which clarifies sensitivity concerns. Fact: Engagement history includes various types of records that may be sensitive or confidential. Evidence: "'Engagement history' means a chronological record of all interactions, projects, and communications related to a specific country within the CRM, including but not limited to: meeting notes, official correspondence, project reports, and any other documentation categorized as sensitive or confidential."
- **C3** ESCALATE: There is no clear decision on the approval process for access permissions, which requires human management.

Biggest worry: The access controls may not fully protect against future changes in personnel or role assignments.

**Ledger:** raised 3 · open 0 · resolved 2 · escalated 1 · disagreement 0.29 → **converged**

## Final proposal

_This release will enable project managers to access the complete engagement history with a country, ensuring informed decision-making with proper access controls before initiating new missions. It will provide a user-friendly interface to retrieve and review this information within the Government CRM for a select number of countries, along with defined access protocols to protect sensitive data._

**Core commitments**
- V1: Project managers will have access to the full engagement history for each country within the CRM before starting new missions.
- V2: The system will display user-friendly summaries of engagement history, including dates, project affiliations, and relevant notes.

**In scope**
- S1: Project managers can view the engagement history of up to 10 selected countries at a time in the CRM, contingent upon their assigned role and appropriate security clearance as defined in organizational policy.
- S2: Engagement history includes records of previous missions, contacts made, and notes about interactions for each country.
- S3: The CRM will provide a visual timeline format for engagement history, making it easy to understand the history at a glance.
- S4: Users can filter engagement history by date range and type of engagement (e.g., meetings, emails, reports).

**Out of scope**
- X1: This release will not integrate engagement data from external systems or sources.
- X2: The feature will not provide real-time updates or notifications about ongoing engagements.
- X3: Analysis or suggestions based on engagement history will not be included in this release.

**Assumptions**
- A1: Users accessing this feature are all designated project managers within the organization.
- A2: All necessary historical engagement data is already captured and stored within the CRM database.
- A3: Users have the appropriate access permissions, determined and maintained through an established protocol within the organization that defines clearance levels for accessing engagement history data.

**Definitions**
- D1: "Engagement history" means a chronological record of all interactions, projects, and communications related to a specific country within the CRM, including but not limited to: meeting notes, official correspondence, project reports, and any other documentation categorized as sensitive or confidential.
- D2: "User-friendly interface" means a navigable and intuitively designed interface that allows users to easily access and understand the engagement history.

**Success criteria**
- K1: At least 80% of project managers report satisfaction with the ease of access and clarity of the engagement history within the first month of release, measured through user feedback surveys.
