# Deliberation trace: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 2 rounds · 5 model calls (0 repairs)

## Round 1

### Proposer · confidence 75

_This release will allow project managers to view the full engagement history with a specified country, including all past missions and engagement details. The feature will help project managers make informed decisions before initiating new missions with that country._

**Core commitments**
- V1: Provide project managers with a detailed engagement history for selected countries.
- V2: Ensure the engagement history includes all relevant records such as previous missions, key contacts, and engagement dates.

**In scope**
- S1: Implement a user interface for project managers to select a country from the CRM.
- S2: Display the full engagement history for the selected country, including dates, types of engagement, and involved personnel.
- S3: Ensure that engagement history is filtered to show only interactions relevant to the requesting project manager's access level.
- S4: Include an export option for the engagement history in a PDF format for offline reference.

**Out of scope**
- X1: This release will not include real-time updates or notifications for ongoing engagements.
- X2: This release will not integrate with external data sources or CRMs beyond the current system.
- X3: User roles outside project managers will not be able to access engagement history in this release.

**Assumptions**
- A1: There is an existing database of engagement records and countries that project managers can access.
- A2: Project managers who use this feature have the necessary permissions to access engagement histories.
- A3: The structure of engagement data is consistent and complete for all member countries.

**Definitions**
- D1: 'Full engagement history' means all records of interactions with a country, including past missions, contact details, engagement dates, and engagement types.
- D2: 'Project managers' means users designated with the role of project managers in the CRM system, who have permission to view project-related data.
- D3: 'Country' means a member nation represented in the CRM.

**Success criteria**
- K1: At least 80% of project managers can successfully access and view the full engagement history for their selected countries, measured through user feedback after the release.

Biggest worry: The definition of engagement history may vary among users, impacting how it is implemented and perceived.

### Critic · confidence 40

Pre-mortem: A year after launch, a project manager accidentally accessed a sensitive engagement history for a country they should not have had visibility into, exposing confidential diplomatic interactions. This breach resulted in diplomatic tensions and damaged trust between the organization and that country, leading to a formal complaint and a government investigation into data security practices.

Questions the request leaves open:
- Which specific records are filtered based on the project manager's access level?
- What thresholds determine which past engagements a project manager can see?
- What happens when a project manager's role changes or they leave the organization?
- What safeguards prevent unauthorized access to sensitive engagement histories?
- How will the data quality of historical engagement records be ensured and maintained?
- What steps will be taken if project managers accidentally receive records that they should not have access to?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S3
- Challenge: S3 states that engagement history will be filtered based on the project manager's access level, but it does not specify the criteria or rules used to determine these access levels, leading to potential breaches of confidentiality.
- Failure scenario: A project manager inadvertently views sensitive records of past engagements which they should not be privy to, resulting in the exposure of confidential data.
- Resolution test: What are the specific criteria used to determine which engagement records a project manager can access?

**C2** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not clarify what happens to the engagement history data when a project manager changes roles or leaves the organization, raising concerns about data ownership and access continuity.
- Failure scenario: After a project manager leaves, a new manager inherits their responsibilities but cannot access the necessary engagement history, impacting mission initiation and planning.
- Resolution test: What is the policy for transferring access rights to engagement histories when a project manager leaves or changes roles?

**C3** · MAJOR · DEFINITIONS · targets S1
- Challenge: S1 mentions implementing a user interface for selecting a country, but does not define how many countries can be selected at once or the process for retrieval, potentially leading to user confusion.
- Failure scenario: A project manager believes they are selecting a specific country but accidentally retrieves data for multiple countries, leading to errors in mission planning.
- Resolution test: How many countries can a project manager select at one time, and what is the process for retrieving that data?

**C4** · MAJOR · DATA_QUALITY · targets D1
- Challenge: D1 defines 'full engagement history' but does not specify how data quality, such as duplicates or incomplete records, will be managed, risking the reliability of the engagement history presented to project managers.
- Failure scenario: A project manager starts a new mission based on outdated or duplicate engagement records, which could lead to miscommunication and project failure.
- Resolution test: What procedures are in place to ensure the engagement history data is accurate and free of duplicates?

**C5** · MINOR · FEASIBILITY · targets K1
- Challenge: K1's success criteria of 80% of project managers accessing engagement histories lacks detail on how success will be measured and whether this includes user feedback on data accuracy and relevance.
- Failure scenario: At the success measurement stage, it is found that many project managers accessed histories without confirming their relevance, leading to misleading data decisions.
- Resolution test: How will access and user satisfaction with the engagement history be measured among project managers?

**C6** · MINOR · CONFIDENTIALITY · targets X3
- Challenge: X3 specifies that user roles outside project managers will not access engagement history, but does not clarify how these roles are defined or if any exceptions exist, leading to potential exposure risks.
- Failure scenario: A user with an unclear role or temporary access gains entry to sensitive engagement histories during a transition phase, causing an unintentional data breach.
- Resolution test: What specific roles are classified as 'project managers,' and what criteria determine access for exceptions?

Biggest worry: The proposal lacks clarity on how access control will prevent unauthorized viewings of sensitive engagement histories.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 85

- **C1** REVISE (missing decision) [changed S3]: The revised S3 item specifies that filtering is based on assigned roles and data sensitivity, addressing confidentiality concerns and preventing unauthorized access.
- **C2** DEFEND (needs human decision): The transfer of access rights when project managers leave or change roles involves organizational policy, which we cannot define in our proposal.
- **C3** REVISE (missing decision) [changed S1]: The revision clarifies that only one country can be selected, addressing potential confusion during data retrieval and ensuring accurate access to information.
- **C4** REVISE (missing decision) [changed D1]: The update to D1 includes a requirement for verifying the accuracy and completeness of engagement data, thus mitigating the risk of presenting duplicate or incomplete records.
- **C5** REVISE (missing decision) [changed K1]: The revised K1 now specifies that success will be measured through a survey evaluating both access and data relevance, providing a clearer picture of the release's effectiveness.
- **C6** REVISE (missing decision) [changed X3]: The revision specifies that 'project managers' is a clearly defined role without exceptions, enhancing data confidentiality by outlining precise access restrictions.

Proposal changes: edited S1, S3, X3, D1, K1
- S1 now reads: Implement a user interface that allows project managers to select one country at a time from a dropdown list, with a search functionality for easier retrieval.
- S3 now reads: Ensure that engagement history is filtered to show only interactions relevant to the requesting project manager's access level, which is determined by their assigned roles and the sensitivity of the engagement data.
- X3 now reads: User roles outside project managers will not have access to engagement history in this release, defined explicitly as users without the 'project manager' designation in the CRM, with no exceptions.
- D1 now reads: 'Full engagement history' means all records of interactions with a country, including past missions, contact details, engagement dates, and engagement types, and must be verified for accuracy and completeness before display.
- K1 now reads: At least 80% of project managers can successfully access and view the full engagement history for their selected countries, with success measured through a two-part survey assessing both access success and perceived relevance of the data.

Biggest worry: The definition of access rights could still lead to ambiguities if organizational policies change.

### Critic · confidence 80 · CONTINUE

Rulings:
- **C1** ACCEPT: This revision specifies the basis for filtering engagement history, which addresses the confidentiality concern. Fact: Filtering is based on assigned roles and data sensitivity. Evidence: "S3: Ensure that engagement history is filtered to show only interactions relevant to the requesting project manager's access level, which is determined by their assigned roles and the sensitivity of the engagement data."
- **C2** ESCALATE: This challenge cannot be settled as it relies on human decision-making related to organizational policy.
- **C3** ACCEPT: This revision clarifies the selection process for countries, addressing potential user confusion. Fact: Only one country can be selected for retrieval. Evidence: "S1: Implement a user interface that allows project managers to select one country at a time from a dropdown list, with a search functionality for easier retrieval."
- **C4** ACCEPT: The update addresses the concern regarding data quality, ensuring only accurate records are presented. Fact: Engagement history data must be verified for accuracy and completeness before display. Evidence: "D1: 'Full engagement history' means all records of interactions with a country, including past missions, contact details, engagement dates, and engagement types, and must be verified for accuracy and completeness before display."
- **C5** ACCEPT: This revision provides clarity on how success will be assessed, addressing the challenge. Fact: Success will be measured via a two-part survey. Evidence: "K1: At least 80% of project managers can successfully access and view the full engagement history for their selected countries, with success measured through a two-part survey assessing both access success and perceived relevance of the data."
- **C6** ACCEPT: This revision clarifies the access restrictions, enhancing the confidentiality of engagement history. Fact: Access to engagement history is limited to users designated as project managers, with no exceptions allowed. Evidence: "X3: User roles outside project managers will not have access to engagement history in this release, defined explicitly as users without the 'project manager' designation in the CRM, with no exceptions."

Biggest worry: The challenge regarding data ownership and access continuity remains unresolved due to reliance on human decision-making.

**Ledger:** raised 6 · open 0 · resolved 5 · escalated 1 · disagreement 0.18 → **converged**

## Final proposal

_This release will allow project managers to view the full engagement history with a specified country, ensuring accurate data presentation while maintaining confidentiality and defining access roles. It includes a user-friendly interface for selecting countries, filtering access based on data sensitivity, and provides a clear method for measuring user satisfaction._

**Core commitments**
- V1: Provide project managers with a detailed engagement history for selected countries.
- V2: Ensure the engagement history includes all relevant records such as previous missions, key contacts, and engagement dates.

**In scope**
- S1: Implement a user interface that allows project managers to select one country at a time from a dropdown list, with a search functionality for easier retrieval.
- S2: Display the full engagement history for the selected country, including dates, types of engagement, and involved personnel.
- S3: Ensure that engagement history is filtered to show only interactions relevant to the requesting project manager's access level, which is determined by their assigned roles and the sensitivity of the engagement data.
- S4: Include an export option for the engagement history in a PDF format for offline reference.

**Out of scope**
- X1: This release will not include real-time updates or notifications for ongoing engagements.
- X2: This release will not integrate with external data sources or CRMs beyond the current system.
- X3: User roles outside project managers will not have access to engagement history in this release, defined explicitly as users without the 'project manager' designation in the CRM, with no exceptions.

**Assumptions**
- A1: There is an existing database of engagement records and countries that project managers can access.
- A2: Project managers who use this feature have the necessary permissions to access engagement histories.
- A3: The structure of engagement data is consistent and complete for all member countries.

**Definitions**
- D1: 'Full engagement history' means all records of interactions with a country, including past missions, contact details, engagement dates, and engagement types, and must be verified for accuracy and completeness before display.
- D2: 'Project managers' means users designated with the role of project managers in the CRM system, who have permission to view project-related data.
- D3: 'Country' means a member nation represented in the CRM.

**Success criteria**
- K1: At least 80% of project managers can successfully access and view the full engagement history for their selected countries, with success measured through a two-part survey assessing both access success and perceived relevance of the data.
