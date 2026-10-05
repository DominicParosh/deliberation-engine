# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.004.

Challenges: 6 raised · 5 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will provide project managers with access to the full engagement history for selected countries, including relevant records like previous missions and key contacts. However, it will not include real-time updates or access for non-project manager roles. A human decision is required regarding data ownership and access continuity when a project manager changes roles or leaves the organization.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide project managers with a detailed engagement history for selected countries.
- **V2** Ensure the engagement history includes all relevant records such as previous missions, key contacts, and engagement dates.

**In scope**

- **S1** Implement a user interface that allows project managers to select one country at a time from a dropdown list, with a search functionality for easier retrieval.  
  The user interface will allow project managers to select only one country at a time, reducing the risk of user errors during data retrieval. _(C3)_
- **S2** Display the full engagement history for the selected country, including dates, types of engagement, and involved personnel.
- **S3** Ensure that engagement history is filtered to show only interactions relevant to the requesting project manager's access level, which is determined by their assigned roles and the sensitivity of the engagement data.  
  Filtering engagement history based on roles and data sensitivity addresses confidentiality concerns and prevents unauthorized access. _(C1)_
- **S4** Include an export option for the engagement history in a PDF format for offline reference.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include real-time updates or notifications for ongoing engagements.
- **X2** This release will not integrate with external data sources or CRMs beyond the current system.
- **X3** User roles outside project managers will not have access to engagement history in this release, defined explicitly as users without the 'project manager' designation in the CRM, with no exceptions.  
  Access is strictly limited to users designated as project managers, with no exceptions, enhancing data confidentiality. _(C6)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | There is an existing database of engagement records and countries that project managers can access. | Kept | never challenged |
| A2 | Project managers who use this feature have the necessary permissions to access engagement histories. | Kept | never challenged |
| A3 | The structure of engagement data is consistent and complete for all member countries. | Kept | never challenged |

## Definitions

- **D1** 'Full engagement history' means all records of interactions with a country, including past missions, contact details, engagement dates, and engagement types, and must be verified for accuracy and completeness before display.  
  The definition of 'full engagement history' was revised to include requirements for data verification, ensuring accuracy before display. _(C4)_
- **D2** 'Project managers' means users designated with the role of project managers in the CRM system, who have permission to view project-related data.
- **D3** 'Country' means a member nation represented in the CRM.

## Success criteria

- **K1** At least 80% of project managers can successfully access and view the full engagement history for their selected countries, with success measured through a two-part survey assessing both access success and perceived relevance of the data.  
  Success will be measured through a two-part survey, ensuring clarity on access and data relevance for project managers. _(C5)_

## Open questions for humans

### C2 · MAJOR · blocks the build

**What is the policy for transferring access rights to engagement histories when a project manager leaves or changes roles?**

- Why it matters: This policy will clarify how access continuity is maintained and prevent disruptions in project management processes.
- Decision owner: HR or Organizational Policy Team
- Options: Define a formal handover process / Specify restrictions based on role changes / Retain access until officially transferred
- Proposer's last word (R2, defend, needs human decision): The transfer of access rights when project managers leave or change roles involves organizational policy, which we cannot define in our proposal.
- Critic's last word (R2, escalate): This challenge cannot be settled as it relies on human decision-making related to organizational policy.

## Tension report

The main disagreement revolved around the ownership and continuity of access rights for engagement histories, particularly when project managers leave or change roles. While the proposer emphasized the need for organizational policy involvement in this matter, the critic underscored that without clear guidelines in place, there is potential for disruption affecting project continuity.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 6 | 0 | 5 | 1 | 0.18 | 85 | 80 | CONTINUE | converged |

- Proposer's remaining worry (85/100): The definition of access rights could still lead to ambiguities if organizational policies change.
- Critic's remaining worry (80/100): The challenge regarding data ownership and access continuity remains unresolved due to reliance on human decision-making.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | REVISED | 0 | S3 states that engagement history will be filtered based on the project manager's access level, but it does not specify the criteria or rules used to determine these access levels, leading to potential breaches of confidentiality. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | ESCALATED | 0 | The proposal does not clarify what happens to the engagement history data when a project manager changes roles or leaves the organization, raising concerns about data ownership and access continuity. |
| C3 | MAJOR | DEFINITIONS | S1 | R1 | REVISED | 0 | S1 mentions implementing a user interface for selecting a country, but does not define how many countries can be selected at once or the process for retrieval, potentially leading to user confusion. |
| C4 | MAJOR | DATA_QUALITY | D1 | R1 | REVISED | 0 | D1 defines 'full engagement history' but does not specify how data quality, such as duplicates or incomplete records, will be managed, risking the reliability of the engagement history presented to project managers. |
| C5 | MINOR | FEASIBILITY | K1 | R1 | REVISED | 0 | K1's success criteria of 80% of project managers accessing engagement histories lacks detail on how success will be measured and whether this includes user feedback on data accuracy and relevance. |
| C6 | MINOR | CONFIDENTIALITY | X3 | R1 | REVISED | 0 | X3 specifies that user roles outside project managers will not access engagement history, but does not clarify how these roles are defined or if any exceptions exist, leading to potential exposure risks. |
