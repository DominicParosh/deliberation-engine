# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.004.

## Summary

This release will enable project managers to access the complete engagement history with a country before starting new missions, ensuring informed decision-making with proper access controls. A user-friendly interface will allow project managers to retrieve and review this information for a select number of countries. However, the process for granting and managing access permissions still requires clarification.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers will have access to the full engagement history for each country within the CRM before starting new missions.  
  Project managers will have access to the full engagement history for each country within the CRM before starting new missions, ensuring informed decision-making with proper access controls.
- **V2** The system will display user-friendly summaries of engagement history, including dates, project affiliations, and relevant notes.  
  The system will display user-friendly summaries of engagement history, including dates, project affiliations, and relevant notes to support efficient information retrieval.

**In scope**

- **S1** Project managers can view the engagement history of up to 10 selected countries at a time in the CRM, contingent upon their assigned role and appropriate security clearance as defined in organizational policy.  
  Project managers can view the engagement history of up to 10 selected countries at a time in the CRM, contingent upon their assigned role and appropriate security clearance as defined in organizational policy. _(C1)_
- **S2** Engagement history includes records of previous missions, contacts made, and notes about interactions for each country.  
  Engagement history includes records of previous missions, contacts made, and notes about interactions for each country, ensuring comprehensive insights.
- **S3** The CRM will provide a visual timeline format for engagement history, making it easy to understand the history at a glance.  
  The CRM will provide a visual timeline format for engagement history, making it easy to understand the history at a glance, enhancing user experience.
- **S4** Users can filter engagement history by date range and type of engagement (e.g., meetings, emails, reports).  
  Users can filter engagement history by date range and type of engagement (e.g., meetings, emails, reports) to customize their view, improving usability.

## What it will not do

**Out of scope for this release**

- **X1** This release will not integrate engagement data from external systems or sources.  
  This release will not integrate engagement data from external systems or sources, which is outside the current project scope.
- **X2** The feature will not provide real-time updates or notifications about ongoing engagements.  
  The feature will not provide real-time updates or notifications about ongoing engagements, keeping the focus on historical data.
- **X3** Analysis or suggestions based on engagement history will not be included in this release.  
  Analysis or suggestions based on engagement history will not be included in this release, to limit the initial scope of development.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users accessing this feature are all designated project managers within the organization. | Kept | never challenged |
| A2 | All necessary historical engagement data is already captured and stored within the CRM database. | Kept | never challenged |
| A3 | Users have the appropriate access permissions, determined and maintained through an established protocol within the organization that defines clearance levels for accessing engagement history data. | Kept | C3 → escalated |

## Definitions

- **D1** "Engagement history" means a chronological record of all interactions, projects, and communications related to a specific country within the CRM, including but not limited to: meeting notes, official correspondence, project reports, and any other documentation categorized as sensitive or confidential.  
  'Engagement history' explicitly details types of records included while highlighting their sensitivity, defining the scope of access accurately. _(C2)_
- **D2** "User-friendly interface" means a navigable and intuitively designed interface that allows users to easily access and understand the engagement history.  
  'User-friendly interface' means a navigable and intuitively designed interface for easy access to the engagement history, enhancing user experience.

## Success criteria

- **K1** At least 80% of project managers report satisfaction with the ease of access and clarity of the engagement history within the first month of release, measured through user feedback surveys.  
  At least 80% of project managers reporting satisfaction with the ease of access and clarity of the engagement history is crucial for measuring success post-release.

## Open questions for humans

### C3 · MAJOR · blocks the build

**What is the established process for granting, reviewing, and revoking access permissions for project managers?**

- Why it matters: Clarifying this process is essential to ensure that only authorized users can access sensitive diplomatic records, preventing leaks.
- Decision owner: Head of Data Protection
- Options: Establish a formal process for access management / Implement periodic reviews of current access permissions / Create a clear protocol for role changes

## Tension report

The primary disagreement arose over how access permissions would be determined and maintained, posing risks of unauthorized access to sensitive records. While the proposer aimed for a streamlined process, the critic insisted that clarity was needed to prevent future access issues, leading to an open question on the matter.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 3 | 0 | 2 | 1 | 0.29 | 75 | 80 | CONTINUE | converged |

- Proposer's remaining worry (75/100): Ensuring the user access control effectively prevents unauthorized access to sensitive engagement records.
- Critic's remaining worry (80/100): The access controls may not fully protect against future changes in personnel or role assignments.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The proposal does not restrict which project managers can access sensitive engagement history, which may include confidential information. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'engagement history' is too broad and fails to specify what types of records could be sensitive and must be protected. |
| C3 | MAJOR | OWNERSHIP | A3 | R1 | ESCALATED | 0 | The assumptions state that users have the appropriate access permissions but do not specify how these permissions are determined and maintained. |
