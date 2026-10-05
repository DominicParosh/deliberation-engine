# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **converged** after 2 rounds (policy `gated`) · $0.007.

Challenges: 6 raised · 2 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

A contact influence scoring feature will be built to prioritize government contacts based on influence levels, helping regional coordinators and project managers improve engagement efficiency. However, the build does not include predictive analytics, historical data management, or integration with external tools. Key questions about ownership, dispute resolution, data updates, and user training must still be decided.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to assign and view an influence score for each contact.
- **V2** Provide a filtering option to display contacts based on their influence score.

**In scope**

- **S1** Create an 'influence score' field in the contact records, ranging from 1 (low influence) to 10 (high influence).
- **S2** Develop a user interface that allows regional coordinators and project managers to assign an influence score to each contact.
- **S3** Implement a sorting feature that allows users to filter and sort contacts by their influence score.
- **S4** Provide a way to visualize the distribution of influence scores across contacts in a number of reports available to users.
- **S5** Establish role-based access control so only authorized users (regional coordinators and project managers) can assign influence scores and view influence score reports. Regular audits will be conducted to ensure compliance.  
  Role-based access control will restrict score assignments and viewing, with audits ensuring confidentiality compliance. _(C2)_

## What it will not do

**Out of scope for this release**

- **X1** This release does not include predictive analytics or recommendations for influence scoring.
- **X2** This release will not handle the historical data of influence scores, only the current values will be recorded.
- **X3** This release does not include integration with external databases or influence measurement tools.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have background knowledge of their contacts and the ability to assess their influence. This assumption is necessary for assigning accurate influence scores. | Kept | never challenged |
| A2 | There are no legal or regulatory constraints preventing the use of influence scores in the government CRM. This affects the implementation of the feature. | Kept | never challenged |
| A3 | Users have defined criteria for determining influence, which will guide the scoring process. | Kept | never challenged |
| A4 | The current architecture of the CRM can accommodate new data fields and filtering features without significant redesign. | Kept | never challenged |

## Definitions

- **D1** 'influence score' means a numerical value assigned to a contact representing their perceived ability to impact decisions or actions within the context of government relations, based on criteria such as historical engagement, position within the government, and perceived effectiveness.  
  The 'influence score' definition now includes specific criteria for scoring assignments, addressing previous ambiguity. _(C1)_
- **D2** 'authorized users' means regional coordinators and project managers who have system access to assign influence scores.  
  The 'authorized users' definition clarifies the user roles involved in scoring, ensuring accountability and security.

## Success criteria

- **K1** By the end of the quarter, at least 70% of contacts have assigned influence scores by regional coordinators and project managers, measured via system usage logs.

## Open questions for humans

### C3 · MAJOR · blocks the build

**What ownership model will be established for the accuracy and consistency of influence scores?**

- Why it matters: Clear responsibility is needed to maintain score integrity as personnel change.
- Decision owner: Management Team
- Options: Designate a specific role for score oversight / Implement a rotating review committee / Establish a shared responsibility among coordinators
- Proposer's last word (R2, defend, needs human decision): The assignment of responsibility for regularly reviewing and updating influence scores involves organizational policies and roles that must be defined by the organization.
- Critic's last word (R2, escalate): The ownership model remains unresolved as it requires internal decision-making.

### C4 · MAJOR · blocks the build

**What formal process will be created for resolving disputes regarding influence score assignments?**

- Why it matters: Dispute resolution mechanisms will prevent conflicting strategies from multiple users.
- Decision owner: Policy Development Team
- Options: Create a standardized mediation protocol / Establish a scoring oversight committee / Empower a designated authority for final decisions
- Proposer's last word (R2, defend, needs human decision): Creating a formal dispute resolution process requires organizational input and is subject to existing protocols that the team should establish.
- Critic's last word (R2, escalate): The absence of a dispute process necessitates organizational involvement.

### C5 · MAJOR · blocks the build

**How frequently will influence scores be reviewed and updated to maintain current and accurate data?**

- Why it matters: Regular updates are necessary to reflect changes in relationships and influence accurately.
- Decision owner: Management Team
- Options: Bi-annual reviews / Quarterly updates / Annual assessments
- Proposer's last word (R2, defend, needs human decision): The frequency of reviewing and updating influence scores is governed by organizational policies and must be determined by management.
- Critic's last word (R2, escalate): Frequency of updates is not established and requires human authority.

### C6 · MAJOR · blocks the build

**What training will be provided to ensure users understand how to assign influence scores consistently?**

- Why it matters: Proper training is vital for effective implementation and accurate scoring across users.
- Decision owner: Training Coordination Team
- Options: Create a training workshop / Develop an online training module / Assign mentorship roles for new users
- Proposer's last word (R2, defend, needs human decision): User training protocols for assigning influence scores must be developed by the organization to ensure proper implementation and adherence to guidelines.
- Critic's last word (R2, escalate): Training protocols remain undetermined and need organizational input.

## Tension report

The primary disagreement lies in the lack of a defined ownership model for influence score accuracy and a process for dispute resolution. The Proposer is confident the system can be implemented but acknowledges user understanding as a concern. The Critic is worried about potential inconsistencies stemming from these unresolved areas, leading to a split in confidence levels.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 6 | 0 | 2 | 4 | 0.62 | 80 | 50 | CONTINUE | converged |

- Proposer's remaining worry (80/100): Ensuring all users consistently understand and apply the scoring criteria effectively.
- Critic's remaining worry (50/100): The lack of a defined ownership model and processes for disputes leaves the system vulnerable to inconsistencies and errors.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'influence score' is ambiguous and lacks a defined and measurable criterion for assignment. Without clear definitions, scores may vary significantly across users, resulting in inaccuracies and potential misuse. |
| C2 | MAJOR | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | The proposal does not outline sufficient safeguards against unauthorized access to influence scores. Given the sensitivity of the contacts involved, improper access could lead to breaches of confidentiality. |
| C3 | MAJOR | OWNERSHIP | D2 | R1 | ESCALATED | 0 | The assignment of influence scores appears to lack a clear ownership model, raising questions on who is accountable for score accuracy and consistency over time. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | ESCALATED | 0 | There is no mention of a process for handling disputes or discrepancies in influence score assignments, which could create inconsistencies in prioritization. |
| C5 | MAJOR | DATA_QUALITY | GAP | R1 | ESCALATED | 0 | The proposal does not address how influence scores will be kept up to date, potentially leading to outdated information being used. |
| C6 | MAJOR | OPERATIONS | GAP | R1 | ESCALATED | 0 | The proposal lacks a clear outline of training or guidelines for users to assign influence scores accurately, which is vital for effective implementation. |
