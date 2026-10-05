# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 2 rounds (policy `naive`) · $0.005.

Challenges: 6 raised · 6 settled between the agents · 0 handed to humans · 0 still open when it ended.

## Summary

An alert system will be built to notify users when their engagement with a country representative is inactive for a specified duration. This release will allow users to customize the thresholds for when engagements are considered 'cold', but will not include any functionality for automatically re-engaging with such countries. Concerns remain about user access to sensitive information and the potential for misconfigured roles that may lead to inappropriate alerts.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Implement an alert system to notify users when engagement records are inactive for a period of time.
- **V2** Allow users to customize the duration that defines 'cold' relationships.

**In scope**

- **S1** Users will receive an email notification if no engagement has been recorded for a specified duration of 90 days.
- **S2** Regional coordinators and project managers will have the ability to set the 'inactive duration' for alerts between 30 to 120 days.
- **S3** An 'engagement record' will be defined as any update made to a country contact's record in the CRM, including emails, project updates, or meeting minutes.
- **S4** The system will have a dashboard view for users to see a list of 'cold' relationships based on their customizable thresholds.
- **S5** Users with roles of 'executive-level staff' and 'other project managers' will not receive alerts about cold relationships from teams outside their own. Only regional coordinators will receive alerts pertaining to their direct country responsibilities.  
  This item specifies role restrictions to prevent unauthorized access, addressing previous confidentiality concerns. _(C1)_
- **S6** The CRM will include a system prompt to remind users to update engagement records if no updates have been made for 30 days. Failure to update records will flag users for a review process by their supervisor every quarter.  
  Structured oversight of engagement updates is implemented to ensure accountability, minimizing reliance on self-reporting. _(C3)_
- **S7** Alerts will be governed by a threshold management mechanism in the system, which will track user engagement frequency to limit alerts to once per week for any individual user, to minimize alert fatigue.  
  A strategy to limit alert frequency will help manage user experience, reducing the risk of alert fatigue. _(C4)_
- **S8** Email alerts will only contain the country name, the date of the most recent engagement update, and a reminder to check the CRM for further details. No sensitive content from the engagement records will be included.  
  By limiting email alerts to basic information, the system ensures protection of sensitive diplomatic data, addressing confidentiality issues. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include historical data analytics or thresholds beyond 120 days.
- **X2** The system will not track communication methods outside the CRM (e.g., personal emails or calls).
- **X3** No functionality will be provided to automatically re-engage with 'cold' countries, only notifications.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will regularly update engagement records within the CRM to ensure accurate tracking of relationships. | Kept | never challenged |
| A2 | Users have access to email notifications and check their inbox for alerts regarding cold relationships. | Kept | never challenged |
| A3 | Engagement records include updates to projects or meetings with country contacts; this is necessary to define cold relationships. | Kept | never challenged |
| A4 | The users' roles allow them to set alert durations but not to modify system-level settings. | Kept | never challenged |

## Definitions

- **D1** 'Cold' means a lack of engagement record updates for a specified duration of 90 days, and at least one documented interaction must occur every 30 days to prevent a relationship from being deemed cold.  
  The definition of 'cold' relationships now incorporates both time and interaction criteria, improving clarity. _(C2)_
- **D2** 'Engagement record' means any documented interaction, update, or note added to the contact's record in the CRM.
- **D3** 'Engagement record' means any documented interaction, such as email correspondence, meeting notes, project updates, or any formal record that reflects a discussion or negotiation with a country contact added to the CRM, excluding non-official communications.  
  This expanded definition eliminates ambiguity about engagement records to prevent misclassification of cold relationships. _(C6)_

## Success criteria

- **K1** At least 75% of users report that they received timely alerts for cold relationships within the first month after implementation, measured by user feedback surveys.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main disagreement centered around the clarity of role restrictions regarding alert visibility and the definitions of engagement records and cold relationships. The Proposer expressed concern about potential user complexity introduced by these changes, while the Critic emphasized the importance of role configuration to prevent notifications being sent to unauthorized users.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 0 | 6 | 0 | 0.00 | 85 | 90 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Changes to alerts and record definitions may introduce complexity that users might find challenging to navigate.
- Critic's remaining worry (90/100): While clarity has improved, any role misconfiguration could still cause the system to alert inappropriate users.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not specify which roles are restricted from seeing alerts about each other's engagements, creating the risk of sensitive information being exposed to unauthorized users. |
| C2 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The definition of 'cold' relationship is ambiguous and only time-based. There is no mention of the types or significance of engagements needed, nor how they relate to ongoing projects or diplomatic status. |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal lacks clarity on accountability for users who fail to update engagement records, leading to reliance on users to self-report their engagement activities without oversight. |
| C4 | MAJOR | OPERATIONS | GAP | R1 | REVISED | 0 | The impact of false alerts has not been considered, particularly regarding alert fatigue among users, which could lead to missed important notifications. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not address how alerts will protect sensitive diplomatic data especially when communicated via email notifications. |
| C6 | MINOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The term 'engagement record' is broad and could lead to misinterpretation. Specific examples of what constitutes valid engagement are needed. |
