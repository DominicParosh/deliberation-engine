# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 4 rounds (policy `gated`) · $0.012.

## Summary

The proposed release will enable project managers to view a comprehensive engagement history with specific countries, which is essential for mission planning. However, the build will not include features for summary metrics or historical data access for non-project managers. Key decisions still need to be made regarding the organizational policies that will govern access for project managers to sensitive data.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers will have access to a comprehensive view of each country's engagement history.  
  Project managers will have access to a comprehensive view of each country's engagement history, ensuring they are well informed before starting new missions.

**In scope**

- **S1** The responsibility for maintaining the accuracy and relevance of engagement history data lies with the CRM Data Steward, who will review and update engagement records at least annually.  
  The responsibility for maintaining the accuracy and relevance of engagement history data is assigned to the CRM Data Steward, who will review records at least annually to ensure their integrity. _(C3)_
- **S2** Access to engagement history will be limited to project managers who are assigned to the respective missions within the CRM system. Project managers will have clear access based on organizational policies, which dictate that only users with 'Project Manager' role classification can view engagement history excluding records classified as 'confidential' or 'sensitive', including negotiations and diplomatic communications. Engagement history data classified as sensitive includes negotiation records, internal assessments, and diplomatic correspondence.  
  Access to engagement history will be restricted to project managers assigned to missions, and will exclude confidential or sensitive records, addressing confidentiality concerns raised during deliberation. _(C10)_
- **S3** The engagement history will include data from the last five years, but older records will be archived and accessible upon special request by project managers, subject to review for relevance.  
  Engagement history will include data from the last five years, with older records archived and accessible upon request, ensuring project managers have access to potentially relevant historical data. _(C5)_
- **S4** Users will be able to filter engagement history by type (meetings, correspondence, reports) and by date range, ensuring filters are tested for reliability prior to release.  
  Users will be allowed to filter engagement history by type and date range, and reliability of these filters will be assured prior to release, enhancing user experience. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include features for summary metrics or analytics of engagement history.
- **X2** It will not allow editing or modification of engagement history records.
- **X3** Access to historical data for users who are not project managers is not included in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | All engagement data for the last five years is available and properly recorded in the CRM system, which is essential for providing a complete history. | Kept | C4 → escalated; C8 → escalated |
| A2 | Project managers have the necessary permissions to access this engagement history, depending on the role and organizational policies. | Kept | C2 → escalated; C7 → revised; C9 → escalated |
| A3 | There are no legal constraints preventing project managers from viewing the complete engagement history with various countries. | Kept | never challenged |

## Definitions

- **D1** 'Engagement history' means a record of all interactions between the organization and a specific country, including meetings, correspondence, project affiliations, and key outcomes over a defined period.  
  'Engagement history' encompasses a record of interactions, ensuring project managers have a clear understanding of previous engagements with a country.
- **D2** 'Project managers' means staff members assigned to lead specific projects and missions, who require comprehensive background information to inform their decision-making.  
  'Project managers' refers to staff leading projects; defining this scope ensures appropriate individuals have access to vital engagement history.
- **D3** 'Country' means any member state with which the organization interacts within the CRM system.  
  'Country' is defined as any member state engaged with the organization, clarifying the engagement parameters within the CRM system.

## Success criteria

- **K1** At least 80% of project managers report improved access to necessary information for mission planning through a survey conducted one month after the feature release.  
  Success will be measured by at least 80% of project managers reporting improved access to information through a follow-up survey, validating the feature's effectiveness post-release.

## Open questions for humans

### C2 · MAJOR · blocks the build

**What specific organizational policies outline the access permissions for project managers regarding engagement history?**

- Why it matters: This directly affects the security of sensitive engagement data and the ability of project managers to perform their roles appropriately.
- Decision owner: Head of Data Protection
- Options: Define clear access policies for project managers / Retain ambiguous permissions

### C4 · MAJOR · blocks the build

**What processes are in place to assure completeness and accuracy of the engagement data within the CRM system?**

- Why it matters: Incomplete data may lead to poor decision-making by project managers, jeopardizing operational integrity.
- Decision owner: CRM Data Steward
- Options: Implement standardized data verification processes / Maintain current status without additional measures

### C8 · MAJOR · blocks the build

**What specific verification processes ensure the accuracy of the five-year engagement data?**

- Why it matters: The reliability of engagement history data is crucial for informed decision-making by project managers.
- Decision owner: CRM Data Steward
- Options: Adopt existing organizational verification protocols / Create new verification measures

### C9 · MAJOR · blocks the build

**What organizational policies dictate the access level required for project managers to view sensitive engagement history?**

- Why it matters: Vague access policies increase the risk of unauthorized data exposure, affecting diplomatic relationships.
- Decision owner: Head of Data Protection
- Options: Specify access policies for role classification / Allow broad access without specific guidelines

## Tension report

The core disagreement centered around clarity in organizational policies for project managers, particularly regarding access to sensitive information. While the proposer expressed confidence in the feature's potential, the critic raised significant concerns about the lack of defined policies, leading to unresolved issues that need further clarification.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 85 | 30 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.53 | 75 | 60 | CONTINUE | continue |
| 3 | 10 | 2 | 5 | 3 | 0.53 | 75 | 60 | CONTINUE | continue |
| 4 | 10 | 0 | 6 | 4 | 0.42 | 80 | 60 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring all project managers clearly understand what engagement history data they are restricted from accessing is crucial to prevent potential breaches.
- Critic's remaining worry (60/100): Unspecified organizational policies leave room for unauthorized access to sensitive engagement history data.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | S2 does not specify which types of engagement history data may contain sensitive or confidential information that project managers should not have access to. |
| C2 | MAJOR | CONFIDENTIALITY | A2 | R1 | ESCALATED | 0 | A2 relies on unspecified organizational policies for permissions, which could lead to unauthorized access to sensitive data by project managers. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | REVISED | 0 | S1 does not clarify who is responsible for managing the engagement history data and ensuring its accuracy and relevance over time. |
| C4 | MAJOR | DATA_QUALITY | A1 | R1 | ESCALATED | 0 | A1 assumes that all engagement data for the last five years is available and properly recorded without confirming how completeness and accuracy will be ensured. |
| C5 | MINOR | DATA_QUALITY | S3 | R1 | REVISED | 0 | S3 states the engagement history will include data from the last five years, but it does not clarify what happens to older, potentially still relevant data. |
| C6 | MINOR | FEASIBILITY | S4 | R1 | REVISED | 0 | S4 mentions users can filter engagement history, but does not clarify the specific filtering options and their reliability. |
| C7 | MAJOR | CONFIDENTIALITY | A2 | R2 | REVISED | 0 | A2 relies on unspecified organizational policies for permissions; thus, risks of unauthorized access remain significant. |
| C8 | MAJOR | DATA_QUALITY | A1 | R2 | ESCALATED | 0 | A1 does not provide processes for verifying the completeness and accuracy of the five-year engagement data. |
| C9 | MAJOR | CONFIDENTIALITY | A2 | R3 | ESCALATED | 0 | The proposal does not define the organizational policies that specifically outline permissions, which poses a significant risk of unauthorized access to sensitive engagement history data. |
| C10 | MAJOR | CONFIDENTIALITY | S2 | R3 | REVISED | 0 | S2 fails to specify which types of engagement history data may contain sensitive or confidential information that project managers should not access, leaving room for potential breaches. |
