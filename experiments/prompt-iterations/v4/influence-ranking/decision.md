# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.008.

## Summary

This release will build a contact prioritization feature for government relations support teams, enabling users to identify and manage influential contacts effectively. It will include a rating system, dashboard view, and auditing mechanisms, while excluding automated influence evaluations or third-party integrations. Concerns remain regarding user resistance to the influence ratings and the definition of 'influence' in practice.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can identify and prioritize influential contacts in the CRM.  
  Users will be able to identify and prioritize influential contacts in the CRM as the core function of the feature.
- **V2** Provide a visual representation of contact influence levels for easy reference.  
  A visual representation of contact influence levels will be provided for easy reference, enhancing usability.

**In scope**

- **S1** Implement a rating system that allows users to assign influence scores (1-5) to contacts.  
  The implementation of a manual rating system allows users to assign influence scores, meeting the defined needs without automation.
- **S2** Display a dashboard view with a list of contacts sorted by their influence score.  
  The dashboard view displaying sorted contacts by influence scores ensures effective prioritization can be visualized easily.
- **S3** Include filters to view contacts based on influence levels (e.g., high, medium, low).  
  Filters to categorize contacts based on influence levels will make navigation more efficient for users.
- **S4** Allow users to edit influence scores and provide a history of changes to this data for audit purposes, with project managers responsible for the integrity of influence scores.  
  The responsibility of project managers for score integrity ensures accountability in the rating process. _(C2)_
- **S5** Ensure only users with appropriate roles (e.g., regional coordinators, project managers, executive roles) can assign and modify influence scores.  
  Defining user roles for assigning and modifying scores ensures confidentiality and control over sensitive data. _(C3)_
- **S6** Implement tooltip information or guidelines on what criteria to consider when assigning influence scores.  
  Tooltip information for scoring criteria will support consistency in ratings among users, addressing clarity issues. _(C1)_
- **S7** Establish a protocol that resets influence scores when a user changes roles or leaves the organization, ensuring the project manager or designated authority reviews the scores.  
  A protocol for resetting scores upon role changes helps maintain data integrity and relevance within the system. _(C4)_
- **S8** Include an audit mechanism that periodically reviews and verifies influence scores across contacts.  
  An audit mechanism to review influence scores periodically ensures data quality and mitigates bias or inaccuracies in scoring. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated algorithms to evaluate contact influence; all scoring will be manual.
- **X2** The feature will not integrate with external social media platforms or third-party databases to determine influence.
- **X3** Real-time alerts or notifications related to changes in contact influence will not be included in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users understand the concept of 'influence' in the context of government relations and will be able to apply it consistently while rating contacts.  | The request implies users will accurately rate the influence of contacts without further training. | Accepted (never challenged) |
| A2 | Users are able to accurately assess and provide feedback on the influence of their contacts based on experience. | The request assumes users have sufficient background knowledge to assess influence correctly. | Accepted (never challenged) |
| A3 | There are no conflicting organizational policies on how to rate contacts or store influence data in the CRM. | There is the assumption that such rating won't violate internal regulations. | Accepted (never challenged) |
| A4 | The CRM has the ability to support data storage for influence ratings without significant performance impact. | Storing additional data points about contacts is necessary to fulfill the feature's requirements. | Accepted (never challenged) |

## Definitions

- **D1** "influence score": A numerical rating between 1 (low influence) and 5 (high influence) that users assign to a contact to reflect their importance and potential impact on engagements, based on defined criteria.  
  The definition of 'influence score' clarifies scoring expectations for users and aligns with the feature's goals.
- **D2** "dashboard view": A visual interface that displays a list of contacts along with their assigned influence scores and allows users to sort and filter based on these scores.  
  Clarifying the 'dashboard view' ensures users understand its purpose and functionality within the CRM context.
- **D3** "roles": Defined user permissions within the CRM that determine who can view, assign, and modify influence scores.  
  Defining 'roles' is essential for establishing who has access and control over influence scores, impacting overall security.
- **D4** "influence assessment criteria": A list of factors that should be considered when assigning influence scores, such as previous engagement outcomes, the contact's position within the government, and feedback from other team members.  
  The 'influence assessment criteria' is now outlined to guide users in their scoring, promoting consistency and accuracy.

## Success criteria

- **K1** Number of contacts rated: target At least 75% of contacts have an influence score assigned within 3 months of rollout. (Monitor the CRM usage statistics to evaluate the percentage of contacts with assigned influence scores.)  
  Setting a target for 75% of contacts rated ensures we measure adoption of the influence feature.
- **K2** User feedback on usability: target At least 80% of users find the influence rating feature useful and easy to use within 3 months of rollout. (Conduct a user satisfaction survey after the first quarter of usage.)  
  Measuring user feedback on usability provides insights to improve the feature's effectiveness post-launch.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The primary disagreement revolved around defining 'influence' and its scoring criteria, with the Proposer concerned about user consistency and the Critic focused on clarity to avoid misprioritization. Through iterations, both positions led to the final definitions and structured guidelines, though uncertainties about user reception persist.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 45 | - | continue |
| 2 | 5 | 2 | 3 | 0 | 0.40 | 85 | 70 | CONTINUE | continue |
| 3 | 5 | 0 | 5 | 0 | 0.00 | 80 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): There may be resistance from users in applying influence ratings consistently across different contexts.
- Critic's remaining worry (80/100): The influence scoring could lead to misprioritization without clear definitions of 'influence' and 'criteria'.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | DEFINITIONS | S1, D1 | R1 | REVISED | 0 | The definition of 'influence' is not clear enough to ensure consistent scoring across users. What specific criteria should users utilize to assign ratings? |
| C2 | MAJOR | OWNERSHIP | S4 | R1 | REVISED | 0 | Who is responsible for maintaining the integrity of influence scores over time? |
| C3 | MAJOR | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | The proposal does not clarify viewing permissions for influence scores. Who beyond the assigned roles can access this information? |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R2 | DEFENDED | 0 | The proposal does not specify what happens to influence scores when a user changes roles or leaves the organization. |
| C5 | MAJOR | DATA_QUALITY | GAP | R2 | DEFENDED | 0 | No audits or measures are defined for verifying the influence scores assigned to contacts, risking inaccuracies. |
