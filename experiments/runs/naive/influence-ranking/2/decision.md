# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 2 rounds (policy `naive`) · $0.007.

Challenges: 6 raised · 6 settled between the agents · 0 handed to humans · 0 still open when it ended.

## Summary

This release will implement a contact prioritization feature that allows users to categorize contacts based on their influence levels with specified permissions and guidelines. Automated influence determination, external integrations, and changes to existing user permissions are not included in this release. Human decision-makers must ensure that the approval processes for permissions are adequately managed to prevent unauthorized changes.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to categorize contacts based on their influence level.  
  Users will be able to categorize contacts based on their influence level, a core component of the proposal that addresses the need for prioritization.
- **V2** Provide users with a visual representation of contact influence levels for prioritization.  
  A visual representation of contact influence levels will be provided, helping users quickly assess and prioritize engagement with contacts.

**In scope**

- **S1** Create a new field in the contact record called 'Influence Level' that allows designated users (regional coordinators and project managers with approved permissions) to assign a value (e.g., Low, Medium, High) to each contact.  
  A new field for 'Influence Level' was created to allow designated users to assign values, addressing the need for a systematic way to categorize influence. _(C1)_
- **S2** Develop a simple interface for regional coordinators and project managers with approved permissions to update the Influence Level of contacts, accompanied by a review mechanism where a designated administrator checks for consistency and correctness of updates.  
  A simple interface for updating 'Influence Level' has been established, including a review mechanism, ensuring accuracy and consistency in data. _(C4)_
- **S3** Implement a filter in the contacts list that allows users to sort contacts by Influence Level.  
  Implementing a filter to sort contacts by Influence Level contributes directly to the prioritization goal by allowing for quick access to categorized contacts.
- **S4** Add tooltips or help text with standardized guidelines outlining specific criteria and examples for determining Influence Level for contacts.  
  Standardized guidelines have been established to accompany tooltips, ensuring consistent categorization among users. _(C5)_
- **S5** Include a process for auditing 'Influence Level' data retention, ensuring that sensitive categorizations are reviewed annually and retained only as long as necessary for operational needs.  
  A data retention auditing process was instituted to maintain continuity and compliance, thereby preventing unauthorized or indefinite retention of sensitive classifications. _(C3, C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release does not include automated tools or algorithms to determine a contact's Influence Level.  
  Automated tools for determining Influence Level are out of scope to prevent reliance on potentially misleading automation.
- **X2** This release will not encompass any external integrations with third-party systems for influence analytics.  
  External integrations with third-party systems are not included to keep the current system self-contained and secure.
- **X3** No changes will be made to existing user permissions in the CRM system regarding contact detail visibility.  
  No changes to existing user permissions were made to maintain the current structure and avoid complications with data access.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have the knowledge and criteria to manually assess the Influence Level of their contacts based on established protocols. | Kept | never challenged |
| A2 | All users of this CRM have the necessary permissions to edit contact details. | Kept | never challenged |
| A3 | Data integrity is maintained; users will not misuse the Influence Level categorization. | Kept | never challenged |

## Definitions

- **D1** 'Influence Level' means an assigned categorical value (Low, Medium, High) to indicate the importance of a contact in decision-making or project engagement, with specific criteria: 'Low' is for contacts with minimal impact, 'Medium' for contacts that can influence but are not central to decisions, and 'High' for contacts who are critical in decision-making processes.  
  Definitions of influence levels were clarified with specific criteria to prevent subjective interpretations and ensure consistency. _(C2)_
- **D2** 'Visual representation' means a graphical or tabular display that allows users to quickly understand the influence status of their contacts at a glance.  
  The definition of visual representation was established to clearly communicate how influence levels will be displayed for user convenience.

## Success criteria

- **K1** At least 75% of users report satisfaction with the new contact categorization feature through a follow-up survey conducted one month after release.  
  Success criteria of 75% satisfaction among users will gauge the feature's acceptance and functional success post-release.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement centered around the management of 'Influence Level' data and access permissions. The Proposer and Critic eventually reached a consensus on defining clear roles and procedures to address confidentiality risks, ensuring that only authorized users can modify sensitive categorizations.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 0 | 6 | 0 | 0.00 | 80 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): The successful implementation of defined user roles and permissions may be complex and require thorough testing.
- Critic's remaining worry (85/100): The potential for subjective assessments remains, but current revisions significantly mitigate risks.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S2, D1 | R1 | REVISED | 0 | The proposal does not specify who can see or modify the 'Influence Level' of contacts, creating a risk that unauthorized users may alter sensitive categorizations, particularly of diplomatic contacts. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definitions of 'Low', 'Medium', and 'High' influence levels are not clearly established, leading to subjective interpretations that could vary between users and introduce inconsistencies. |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not specify how 'Influence Level' data will be managed or updated when users leave or change roles, risking loss of context and continuity in the CRM. |
| C4 | MAJOR | DATA_QUALITY | S2 | R1 | REVISED | 0 | The proposal does not detail how data quality and accuracy of the 'Influence Level' assessments will be ensured, leading to potential inaccuracies. |
| C5 | MAJOR | OPERATIONS | S4 | R1 | REVISED | 0 | Tooltips or help text explaining how to determine the Influence Level of contacts are insufficient without clear guidelines, potentially leading to varying assessments of influence. |
| C6 | MAJOR | COMPLIANCE | GAP | R1 | REVISED | 0 | There is no mention of how the 'Influence Level' data will be retained or audited for compliance purposes, risking unauthorized retention of sensitive classifications. |
