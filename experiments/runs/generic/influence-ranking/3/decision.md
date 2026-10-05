# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.009.

Challenges: 7 raised · 2 settled between the agents · 5 handed to humans · 0 still open when it ended.

## Summary

This release will implement a feature that allows users to categorize and identify influential contacts using a manual influence scoring system, while putting in place strict permissions and training protocols. However, it will not include an automated influence scoring system, nor will it alter existing contact record fields outside of the new scoring feature. There remain critical questions regarding the definition of 'influence' and the responsibilities for maintaining influence scores that need resolution before build can begin.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users will be able to assign an influence score to each contact within the Government CRM.
- **V2** Users will see a prioritized list of contacts based on their influence scores.
- **V3** There will be a standard set of criteria established by the organization to define 'influence' for consistent scoring across all users.  
  Establishing a set of criteria to define 'influence' ensures consistent application among users of influence scoring. _(C1)_

**In scope**

- **S1** Regional coordinators, project managers, and executive-level staff will be able to assign influence scores to contacts on a scale of 1-5, where 1 means low influence and 5 means high influence.  
  Users, specifically regional coordinators and executive-level staff, will score contacts on a scale of 1-5, allowing for prioritized engagement.
- **S2** The contact list will display the assigned influence scores alongside contact names to help users quickly identify influential contacts.
- **S3** Users will have the ability to filter the contact list based on influence scores to prioritize engagements.
- **S4** The feature will include permissions: only regional coordinators and executive-level staff will be authorized to assign influence scores; project managers will be permitted to view but not assign these scores.  
  Clear permissions will be implemented so that only certain users can assign scores, reducing the risk of unauthorized access to sensitive information. _(C2)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include a manual influence scoring system; the feature will instead be developed as a foundational capability without an automated influence assessment.  
  The decision to exclude a manual influence scoring system aims to prevent subjective bias and ensure foundational capabilities are prioritized. _(C6)_
- **X2** This release will not change existing contact record fields outside the influence scoring.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users are familiar with the concept of influence scoring and understand how to use a scoring system; this knowledge is required for effective use of the feature. | Kept | never challenged |
| A2 | Contact information is accurate and up-to-date in the system, allowing for meaningful influence assessments. | Kept | C5 → escalated |
| A3 | There is a clear understanding of what constitutes 'influence' among users; this understanding is needed to create consistent scoring. | Kept | C4 → escalated |

## Definitions

- **D1** "influence score" means a numerical value assigned to a contact that represents their level of influence, rated on a scale of 1 (low influence) to 5 (high influence).  
  'Influence score' is defined as a rating from 1 to 5 that reflects a contact's level of influence, which must be consistently applied. _(C1)_
- **D2** "prioritized list" means an ordered list of contacts displayed in the Government CRM that reflects their influence scores, with the highest scores appearing first.

## Success criteria

- **K1** At least 75% of users assign influence scores to their contacts within the first month of release, measured by system usage analytics.
- **K2** Users report a satisfaction rating of 80% or higher in a post-release survey regarding the usefulness of the influence feature for contact prioritization.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What specific criteria will be established by the organization to define 'influence' for consistent scoring?**

- Why it matters: This definition is crucial to avoid biased or inconsistent scores that could mislead engagement priorities.
- Decision owner: Head of Operations
- Options: Define criteria collaboratively within the organization / Allow users to define criteria individually / Establish a task force to create a standard definition
- Proposer's last word (R2, defend, needs human decision): To ensure accuracy in influence scoring, a clear organizational framework or guidelines defining 'influence' must be developed by the organization, which is outside the current scope of this release.
- Critic's last word (R2, escalate): The criteria defining 'influence' need to be established by the organization, which is outside the current proposal's scope.

### C3 · MAJOR · blocks the build

**Who will be responsible for regularly reviewing and updating influence scores based on changes in contact relationships?**

- Why it matters: Clear ownership is needed to ensure that influence scores reflect current realities and remain actionable.
- Decision owner: Regional Coordinators
- Options: Assign responsibility to regional coordinators / Create a rotating responsibility among team members / Leave it to individual user discretion
- Proposer's last word (R2, defend, needs human decision): Responsibility for reviewing and updating influence scores based on evolving relationships needs to be defined by the organization and should not be specified in this proposal.
- Critic's last word (R2, escalate): Responsibility for maintaining updated influence scores must be defined and is outside this proposal.

### C4 · MAJOR · blocks the build

**What specific training or resources will enhance users' understanding of what constitutes 'influence'?**

- Why it matters: Consistent training is essential to ensure all users apply the scoring uniformly, enabling effective prioritization of engagements.
- Decision owner: Training Coordinator
- Options: Develop a standardized training module / Rely on individual managers to train their teams / Utilize existing materials without changes
- Proposer's last word (R2, revise, missing decision): This edit formalizes that the organization will establish clear criteria for influence, ensuring consistent scoring practices among users.
- Critic's last word (R2, escalate): The specific training or resources needed to ensure users have a uniform understanding of influence must be determined by the organization.

### C5 · MAJOR · blocks the build

**What mechanisms will be implemented to ensure contact information remains accurate and current within the CRM?**

- Why it matters: Up-to-date contact information is vital for accurate influence scoring and effective engagement.
- Decision owner: Data Management Team
- Options: Regular audits of contact information / User responsibility for updates / Implement automatic data validation processes
- Proposer's last word (R2, defend, acceptable risk): While ensuring data accuracy is critical, current processes will rely on user diligence and periodic reviews, as no immediate mechanisms are established within this proposal to enforce data accuracy.
- Critic's last word (R2, escalate): The mechanisms to ensure accurate data must be clarified and established by the organization.

### C7 · MAJOR · blocks the build

**What specific training protocols and resources will be established to ensure consistent application of the influence scoring system?**

- Why it matters: Without clear protocols, there may be inconsistencies in how influence scoring is applied, leading to ineffective prioritization.
- Decision owner: Training Coordinator
- Options: Develop a formalized training program / Rely on informal training methods / Encourage self-guided learning without materials
- Proposer's last word (R3, defend, needs human decision): The proposal includes training protocols and resources, which requires organizational decisions on specific training content and methods to ensure consistent user application; thus, it remains as written.
- Critic's last word (R3, escalate): The answer indicates that the training protocols are dependent on organizational decisions, which means it cannot be accepted as it stands.

## Tension report

The primary contention arose over the definition of 'influence,' impacting the consistency of scoring across users; the Proposer argued for a need for clarity and organizational input, whereas the Critic emphasized the necessity of a defined responsibility for maintaining the accuracy of scores. The disagreement over these issues led to several open questions that remain unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 7 | 1 | 2 | 4 | 0.69 | 75 | 60 | CONTINUE | continue |
| 3 | 7 | 0 | 2 | 5 | 0.69 | 75 | 30 | CONTINUE | converged |

- Proposer's remaining worry (75/100): Ensuring every user applies the influence scoring consistently despite individual interpretations of influence.
- Critic's remaining worry (30/100): The influence scoring system's reliance on subjective assessments and training leaves significant room for inconsistency and inaccuracy.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | D1 | R1 | ESCALATED | 0 | The term 'influence' is not adequately defined or standardized, leading to inconsistent application among users, which could result in significant errors in engagement prioritization. |
| C2 | MAJOR | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal does not clearly define the permissions associated with viewing, editing, or assigning influence scores, raising potential risks around data exposure and confidentiality. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | ESCALATED | 0 | There is no clarity on who is responsible for verifying and updating influence scores as relationships change over time, which could lead to outdated or inaccurate scores being used for prioritization. |
| C4 | MAJOR | DATA_QUALITY | A3 | R1 | ESCALATED | 0 | The assumption that users understand what constitutes 'influence' lacks clarity in practice, which could lead to subjective and unreliable scoring outcomes. |
| C5 | MAJOR | DATA_QUALITY | A2 | R1 | ESCALATED | 0 | The assumption that contact information is accurate may not be true, causing potentially misleading influence assignments based on outdated or incorrect data. |
| C6 | BLOCKER | FEASIBILITY | X1 | R1 | CONCEDED | 0 | The lack of an automated scoring system means influence scores are entirely subjective and may not be scalable to all users across the 100 member countries. |
| C7 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 0 | The proposal does not specify how users will be trained to consistently apply the influence scoring system, potentially leading to arbitrary and inconsistent scoring. |
