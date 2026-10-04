# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.007.

Challenges: 6 raised · 5 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will allow project managers to view a comprehensive engagement history with each country, ensuring they have essential data for new mission planning while excluding sensitive information. The features outlined include restricted access based on role and various filtering capabilities. However, uncertainty remains regarding existing organizational policies on project manager access permissions, which needs to be resolved before development begins.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers will have access to a comprehensive engagement history of each country.  
  Project managers will have access to a comprehensive engagement history of each country, addressing the need for better data access for planning new missions.
- **V2** The system will display past project affiliations and associated contacts for each country.  
  The system will display past project affiliations and associated contacts for each country, providing context and continuity for project managers.

**In scope**

- **S1** Engagement history means all recorded interactions with a country, including meetings, communications, project details, and mission specifics.  
  Engagement history is defined to include all recorded interactions with a country, ensuring project managers have complete insights into past engagements.
- **S2** The feature will be accessible only to users with the role of project manager and will have enforced permission settings to ensure they can access engagement history relevant to their clearance level.  
  The feature restricts access to authorized project managers only, ensuring sensitive information is protected according to permission settings. _(C2)_
- **S3** The history will include data from the last five years of engagement with the country.  
  Limiting the history to data from the last five years ensures relevance and manageability of the information provided to project managers.
- **S4** The data displayed will include the names of relevant contacts, general notes from engagements, and project outcomes; it will explicitly exclude sensitive diplomatic notes, internal assessments, and security-related information.  
  The data will explicitly exclude sensitive diplomatic notes, internal assessments, and security-related information to maintain confidentiality and protect sensitive content. _(C1)_
- **S5** Project managers will be able to filter the engagement history by date, type of engagement (meeting, email, etc.), and involved contacts.  
  Filtering capabilities allow project managers to efficiently navigate through historical data, focusing on specific types of interactions and timeframes.
- **S6** The proposal includes a user interface that allows project managers to easily navigate and read the engagement history.  
  A user-friendly interface is included to enhance usability, making it easier for project managers to access the engagement history.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include the ability to edit or delete engagement history records.  
  Editing or deleting records is not included to prevent potential data integrity issues in future iterations, ensuring current safeguarded restrictions remain effective. _(C6)_
- **X2** The feature will not integrate with external systems or databases that provide historical data outside of the current CRM records.  
  The decision not to integrate with external systems is made to maintain focus on the current CRM records and streamline project management functions.
- **X3** The display of engagement history will not include sensitive data points that require higher security clearance.  
  Exclusion of sensitive data points is vital for compliance and user security, addressing significant confidentiality concerns raised during discussions.

**Rejected during deliberation**

- Nothing was dropped.
- Declined **C6** (MINOR · CONFIDENTIALITY): Are there technical safeguards to prevent modifications to engagement history records? The Proposer's answer, which the Critic accepted: While future iterations may introduce issues related to editing or deleting records, current scope explicitly prohibits these actions, which serves as a technical safeguard against potential modifications.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Project managers have the required permissions to view engagement data as per existing organizational policies. | Kept | C3 → escalated |
| A2 | All relevant engagement history data is currently being recorded and maintained within the Government CRM. | Kept | never challenged |
| A3 | User interface elements for the engagement history feature can be developed within the timeframe of this release. | Kept | never challenged |
| A4 | The technical infrastructure can support the filtering and display requirements outlined in this proposal. | Kept | never challenged |

## Definitions

- **D1** "Engagement history" means all documented interactions and engagements with a specific country, including meetings, communications, project details, and outcomes, but excluding sensitive diplomatic notes and internal assessments.  
  The refined definition of 'engagement history' clarifies what interactions are included and ensures consistency and usability for project managers. _(C4)_
- **D2** "Project manager" means a user role that consists of personnel responsible for overseeing projects and missions within the Government CRM.  
  Defining 'project manager' helps outline user roles clearly within the system and aligns with operational structure.
- **D3** "Filter" means the capability to sort and display specific engagement records based on user-selected criteria, which includes date, type of engagement (meeting, email, report), and involved contacts.  
  Clarifying the definition of 'filter' minimizes potential confusion and establishes clear expectations for project managers on how to access historical data. _(C5)_

## Success criteria

- **K1** By the end of the quarter, 80% of project managers will successfully access and review a country's full engagement history within the system, as measured by user feedback surveys.  
  The success criterion ensures that the implementation of the feature meets user needs and gauges its acceptance and functionality by measuring access and reviews from project managers.

## Open questions for humans

### C3 · MAJOR · blocks the build

**Do existing organizational policies grant project managers permission to access engagement history?**

- Why it matters: Clarifying this question will ensure compliance with organizational standards and prevent unauthorized access to sensitive data.
- Decision owner: Compliance Personnel
- Options: Confirm existing permissions / Revise permissions accordingly / Retain current policy until review is complete
- Proposer's last word (R2, defend, needs human decision): The existing organizational policies regarding access permissions need to be reviewed by compliance personnel to confirm that project managers have the necessary access.
- Critic's last word (R2, escalate): Compliance confirmation requires a review of existing policies by relevant personnel, which is not within the proposal's current scope.

## Tension report

The primary disagreement centered around the assumption of existing organizational policies on project manager permissions, which remains unconfirmed. While the proposer felt confident about proceeding with access for project managers, the critic emphasized the need for compliance verification, leading to the issue being escalated rather than resolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 85 | 40 | - | continue |
| 2 | 6 | 0 | 5 | 1 | 0.20 | 85 | 70 | CONTINUE | converged |

- Proposer's remaining worry (85/100): There's still uncertainty regarding existing organizational policies on access permissions.
- Critic's remaining worry (70/100): The adequacy of existing organizational policies regarding access permissions remains unconfirmed, leaving room for potential compliance risks.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal does not specify which sensitive data points have been excluded from the engagement history display. |
| C2 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | The proposal does not clarify how permissions are enforced to ensure that only authorized project managers can access sensitive parts of the engagement history. |
| C3 | MAJOR | COMPLIANCE | A1 | R1 | ESCALATED | 0 | Assumption A1 about project managers having required permissions is unsubstantiated, posing a risk if current policies do not align with the proposal. |
| C4 | MINOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'engagement history' is broad and may lead to inconsistencies in what data is included in the engagement history. |
| C5 | MINOR | DEFINITIONS | D3 | R1 | REVISED | 0 | The term 'filter' is not clearly defined, potentially causing confusion on how users can filter their results in the engagement history. |
| C6 | MINOR | CONFIDENTIALITY | X1 | R1 | DEFENDED | 0 | The proposal does not explain how engagement records will be safeguarded against user actions like editing or deleting sensitive information in the future. |
