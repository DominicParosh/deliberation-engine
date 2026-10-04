# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 2 rounds · 7 model calls (3 repairs)

## Round 1

### Proposer · confidence 85

_This release will allow project managers to view the complete engagement history with a specific country before initiating a new mission. It will provide essential data regarding past interactions, projects, and contacts related to that country._

**Core commitments**
- V1: Project managers will have access to a comprehensive engagement history of each country.
- V2: The system will display past project affiliations and associated contacts for each country.

**In scope**
- S1: Engagement history means all recorded interactions with a country, including meetings, communications, project details, and mission specifics.
- S2: The feature will be accessible to users with the role of project manager within the Government CRM.
- S3: The history will include data from the last five years of engagement with the country.
- S4: The data displayed will include the names of relevant contacts, general notes from engagements, and project outcomes.
- S5: Project managers will be able to filter the engagement history by date, type of engagement (meeting, email, etc.), and involved contacts.
- S6: The proposal includes a user interface that allows project managers to easily navigate and read the engagement history.

**Out of scope**
- X1: This release will not include the ability to edit or delete engagement history records.
- X2: The feature will not integrate with external systems or databases that provide historical data outside of the current CRM records.
- X3: The display of engagement history will not include sensitive data points that require higher security clearance.

**Assumptions**
- A1: Project managers have the required permissions to view engagement data as per existing organizational policies.
- A2: All relevant engagement history data is currently being recorded and maintained within the Government CRM.
- A3: User interface elements for the engagement history feature can be developed within the timeframe of this release.
- A4: The technical infrastructure can support the filtering and display requirements outlined in this proposal.

**Definitions**
- D1: "Engagement history" means all documented interactions and engagements with a specific country, including meetings, communications, and project details within the CRM.
- D2: "Project manager" means a user role that consists of personnel responsible for overseeing projects and missions within the Government CRM.
- D3: "Filter" means the capability to sort and display specific engagement records based on user-selected criteria.

**Success criteria**
- K1: By the end of the quarter, 80% of project managers will successfully access and review a country's full engagement history within the system, as measured by user feedback surveys.

Biggest worry: There may be limitations on the quality and completeness of historical engagement data currently stored in the CRM.

### Critic · confidence 40

Pre-mortem: A year after the launch of the engagement history feature, a serious incident occurred when a project manager mistakenly accessed sensitive diplomatic notes during a country's engagement history review. Sensitive data that should have been restricted due to clearance levels was visible, leading to a breach of confidentiality and embarrassment for the organization, as it caused diplomatic tensions and endangered ongoing relations with that country.

Questions the request leaves open:
- Which roles can see sensitive data in the engagement history?
- What specific sensitive data points are being excluded from the engagement history display?
- How are permissions enforced to prevent unauthorized access to engagement records?
- What happens if a project manager changes roles or leaves before accessing the engagement history?
- What criteria are used to define 'relevant contacts' in the engagement history?
- What audits are in place to track access to engagement history records?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S4
- Challenge: The proposal does not specify which sensitive data points have been excluded from the engagement history display.
- Failure scenario: A project manager views engagement history for a country, which includes sensitive diplomatic notes rather than just general engagement records, leading to unauthorized information disclosure to individuals without clearance.
- Resolution test: What specific sensitive data points will not be included in the engagement history?

**C2** · MAJOR · OWNERSHIP · targets S2
- Challenge: The proposal does not clarify how permissions are enforced to ensure that only authorized project managers can access sensitive parts of the engagement history.
- Failure scenario: A newly appointed project manager inadvertently accesses records from engagements requiring higher security clearance due to inadequate permission settings, leading to a potential leak of confidential information.
- Resolution test: Which roles are explicitly authorized to access engagement history?

**C3** · MAJOR · COMPLIANCE · targets A1
- Challenge: Assumption A1 about project managers having required permissions is unsubstantiated, posing a risk if current policies do not align with the proposal.
- Failure scenario: Permissions granted to project managers are inconsistent with existing organizational policies, allowing unauthorized access to sensitive engagement details, leading to compliance failure.
- Resolution test: Do existing organizational policies grant project managers permission to access engagement history?

**C4** · MINOR · DEFINITIONS · targets D1
- Challenge: The definition of 'engagement history' is broad and may lead to inconsistencies in what data is included in the engagement history.
- Failure scenario: An ambiguity in what constitutes 'engagement history' leads to the inclusion of irrelevant data or important records being omitted, impacting the usability of the feature for project managers.
- Resolution test: What types of engagement data are defined as part of 'engagement history'?

**C5** · MINOR · DEFINITIONS · targets D3
- Challenge: The term 'filter' is not clearly defined, potentially causing confusion on how users can filter their results in the engagement history.
- Failure scenario: Project managers misunderstand filtering capabilities and fail to retrieve the information they need about past engagements due to an unclear definition of what filtering entails.
- Resolution test: What filtering criteria can users apply when accessing engagement history?

**C6** · MINOR · CONFIDENTIALITY · targets X1
- Challenge: The proposal does not explain how engagement records will be safeguarded against user actions like editing or deleting sensitive information in the future.
- Failure scenario: In the event that editing capabilities are mistakenly included in future iterations, project managers could unintentionally alter or erase critical engagement history, compromising data integrity.
- Resolution test: Are there technical safeguards to prevent modifications to engagement history records?

Biggest worry: The proposal lacks clear definitions and safeguards for sensitive data access, risking unauthorized disclosures.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S4]: The edit specifies which sensitive data points will be excluded from the engagement history display, thereby addressing the concerns about confidentiality.
- **C2** REVISE (missing decision) [changed S2]: The edit clarifies that access is enforced as per permission settings, ensuring that only authorized project managers can access the relevant engagement history.
- **C3** DEFEND (needs human decision): The existing organizational policies regarding access permissions need to be reviewed by compliance personnel to confirm that project managers have the necessary access.
- **C4** REVISE (missing decision) [changed D1]: The edit refines the definition of 'engagement history,' reducing ambiguity about what data is included, thereby enhancing the clarity for development and usability.
- **C5** REVISE (missing decision) [changed D3]: The edit provides a detailed definition of 'filter' that clarifies the filtering capabilities available to project managers, minimizing user confusion.
- **C6** DEFEND (acceptable risk): While future iterations may introduce issues related to editing or deleting records, current scope explicitly prohibits these actions, which serves as a technical safeguard against potential modifications.

Proposal changes: edited S2, S4, D1, D3
- S2 now reads: The feature will be accessible only to users with the role of project manager and will have enforced permission settings to ensure they can access engagement history relevant to their clearance level.
- S4 now reads: The data displayed will include the names of relevant contacts, general notes from engagements, and project outcomes; it will explicitly exclude sensitive diplomatic notes, internal assessments, and security-related information.
- D1 now reads: "Engagement history" means all documented interactions and engagements with a specific country, including meetings, communications, project details, and outcomes, but excluding sensitive diplomatic notes and internal assessments.
- D3 now reads: "Filter" means the capability to sort and display specific engagement records based on user-selected criteria, which includes date, type of engagement (meeting, email, report), and involved contacts.

Biggest worry: There's still uncertainty regarding existing organizational policies on access permissions.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** ACCEPT: This directly addresses the concern and specifies what sensitive information is excluded. Fact: Sensitive diplomatic notes, internal assessments, and security-related information are excluded from the engagement history. Evidence: "The data displayed will include the names of relevant contacts, general notes from engagements, and project outcomes; it will explicitly exclude sensitive diplomatic notes, internal assessments, and security-related information."
- **C2** ACCEPT: The commitment clarifies that access is restricted appropriately. Fact: Access is restricted to project managers with appropriate permissions according to their clearance level. Evidence: "The feature will be accessible only to users with the role of project manager and will have enforced permission settings to ensure they can access engagement history relevant to their clearance level."
- **C3** ESCALATE: Compliance confirmation requires a review of existing policies by relevant personnel, which is not within the proposal's current scope.
- **C4** ACCEPT: Clarifying what constitutes engagement history resolves the ambiguity. Fact: Engagement history includes specific documented interactions and excludes certain sensitive data. Evidence: ""Engagement history" means all documented interactions and engagements with a specific country, including meetings, communications, project details, and outcomes, but excluding sensitive diplomatic notes and internal assessments."
- **C5** ACCEPT: Clarification of filtering capabilities minimizes potential user confusion. Fact: Filtering criteria for engagement history include date and type of engagement. Evidence: ""Filter" means the capability to sort and display specific engagement records based on user-selected criteria, which includes date, type of engagement (meeting, email, report), and involved contacts."
- **C6** ACCEPT: The current scope safeguards against alterations to existing records. Fact: Editing or deleting engagement records is prohibited in this release. Evidence: "This release will not include the ability to edit or delete engagement history records."

Biggest worry: The adequacy of existing organizational policies regarding access permissions remains unconfirmed, leaving room for potential compliance risks.

**Ledger:** raised 6 · open 0 · resolved 5 · escalated 1 · disagreement 0.20 → **converged**

## Final proposal

_This release will allow project managers to view comprehensive engagement history with each country, ensuring they have access to essential data for new mission planning while excluding sensitive information. New definitions and clarifications will mitigate risks related to privacy and data access permissions._

**Core commitments**
- V1: Project managers will have access to a comprehensive engagement history of each country.
- V2: The system will display past project affiliations and associated contacts for each country.

**In scope**
- S1: Engagement history means all recorded interactions with a country, including meetings, communications, project details, and mission specifics.
- S2: The feature will be accessible only to users with the role of project manager and will have enforced permission settings to ensure they can access engagement history relevant to their clearance level.
- S3: The history will include data from the last five years of engagement with the country.
- S4: The data displayed will include the names of relevant contacts, general notes from engagements, and project outcomes; it will explicitly exclude sensitive diplomatic notes, internal assessments, and security-related information.
- S5: Project managers will be able to filter the engagement history by date, type of engagement (meeting, email, etc.), and involved contacts.
- S6: The proposal includes a user interface that allows project managers to easily navigate and read the engagement history.

**Out of scope**
- X1: This release will not include the ability to edit or delete engagement history records.
- X2: The feature will not integrate with external systems or databases that provide historical data outside of the current CRM records.
- X3: The display of engagement history will not include sensitive data points that require higher security clearance.

**Assumptions**
- A1: Project managers have the required permissions to view engagement data as per existing organizational policies.
- A2: All relevant engagement history data is currently being recorded and maintained within the Government CRM.
- A3: User interface elements for the engagement history feature can be developed within the timeframe of this release.
- A4: The technical infrastructure can support the filtering and display requirements outlined in this proposal.

**Definitions**
- D1: "Engagement history" means all documented interactions and engagements with a specific country, including meetings, communications, project details, and outcomes, but excluding sensitive diplomatic notes and internal assessments.
- D2: "Project manager" means a user role that consists of personnel responsible for overseeing projects and missions within the Government CRM.
- D3: "Filter" means the capability to sort and display specific engagement records based on user-selected criteria, which includes date, type of engagement (meeting, email, report), and involved contacts.

**Success criteria**
- K1: By the end of the quarter, 80% of project managers will successfully access and review a country's full engagement history within the system, as measured by user feedback surveys.

## Orchestrator warnings

- R2: dropped new challenge(s) that repeated an open question: #1 (C3).
