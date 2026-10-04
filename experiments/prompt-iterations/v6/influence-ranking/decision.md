# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.018.

## Summary

This release will build a feature enabling users to identify and prioritize influential contacts through influence scoring. However, the implementation details regarding governance, criteria for scoring, and user workload remain unresolved. Decisions relating to these open questions will be essential before starting the build process.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Establish a system for categorizing contacts based on a defined 'influence score'.  
  Establishing a system for categorizing contacts by 'influence score' creates a structured way to evaluate contacts based on their impact, addressing a key user need.
- **V2** Provide users with the ability to filter and sort contacts based on their influence score.  
  Providing filtering capabilities by influence score supports users in efficiently managing their outreach efforts based on the ranking of contacts.

**In scope**

- **S1** Create a rating system where each contact can be assigned an 'influence score' ranging from 1 to 10, where 10 indicates the highest level of influence. Access to view influence scores will be limited to authorized users including regional coordinators and project managers only.  
  The rating system allows authorized users to manage confidential assessments of contacts while ensuring sensitive information is not exposed to unauthorized personnel. _(C3)_
- **S2** Allow users to view the influence scores of contacts in the contact details section of the CRM.  
  Viewing influence scores in contact details supports users in understanding the context of their engagements at a glance, enhancing decision-making effectiveness.
- **S3** Enable filtering of contact lists by influence score for regional coordinators and project managers.  
  Filtering by influence score directly supports the core purpose of this feature, allowing users to prioritize their outreach effectively.
- **S4** Provide a report feature that lists contacts sorted by influence score for 10 or more entries.  
  Offering a report feature ensures that users can analyze and access contact information sorted by influence efficiently, enhancing user experience.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated updates of the influence scores based on external data or events.  
  Automated updates of influence scores from external data sources raise data governance concerns, warranting exclusion from this rollout.
- **X2** The influence scoring system will not incorporate any social media metrics.  
  Social media metrics were excluded to maintain focus on official engagement rather than fluctuating social dynamics that might not reflect actual influence.
- **X3** This release does not include training or educational materials on how to utilize influence scores.  
  Omitting training materials is due to the current scope focusing strictly on system functionality rather than user education.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The authority to assign and modify influence scores is limited to regional coordinators and project managers. Each regional coordinator and project manager is expected to dedicate no more than 2 hours per month to review, assign, and modify influence scores, ensuring that their workload remains manageable. | Kept | C1 → escalated; C5 → escalated; C8 → escalated |
| A2 | The criteria for defining an influence score will encompass the following factors: 1) engagement history, which includes frequency of meetings and other communications with the contact; 2) seniority, determined by the contact's position within the government organization; and 3) recent interactions, specifically outreach made or received in the past six months. These criteria will be documented and reviewed by the governance committee prior to initial score assignment. | Kept | C2 → escalated; C11 → escalated |
| A3 | The governance structure will include a committee comprised of selected regional coordinators and project managers responsible for determining scoring criteria, approving changes to influence scores, and conducting quarterly audits to ensure consistent application across the CRM. | Kept | C4 → escalated; C7 → escalated; C10 → escalated |
| A4 | Influence score data will be retained for a period of 3 years, after which it will be reviewed for accuracy and relevance, and either archived or deleted in compliance with data protection regulations. A governance structure composed of regional coordinators and project managers will oversee the regular updating of influence scores, including responsibilities for reviewing scores that should be validated at least quarterly. | Kept | C6 → escalated; C9 → escalated |

## Definitions

- **D1** 'Influence score' means a numerical value between 1 and 10 assigned to each contact, representing their level of influence based on criteria defined by the organization.
- **D2** 'Regional coordinators' means users in the CRM who manage relationships and engagements for specific geographic areas.
- **D3** 'Project managers' means users in the CRM responsible for overseeing and executing projects involving government contacts.

## Success criteria

- **K1** At least 80% of users report that the influence score feature helps them prioritize contacts effectively, measured through a user feedback survey after 3 months of deployment.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**Who in the organization has the final authority to assign and modify influence scores?**

- Why it matters: It ensures accountability and prevents misuse of influence scores, which could jeopardize diplomatic efforts.
- Decision owner: Head of Operations
- Options: Regional coordinators only / Project managers only / Both roles together

### C9 · BLOCKER · blocks the build

**What specific mechanisms will be established for the validation and updating of influence scores?**

- Why it matters: A clear validation process prevents outdated or corrupted data from undermining the system's objectives.
- Decision owner: Head of Data Quality
- Options: Monthly audits / Quarterly assessments / User-driven reports

### C10 · BLOCKER · blocks the build

**What governance measures will ensure effective oversight of the influence scoring process?**

- Why it matters: Proper governance structures are necessary for consistency and accountability in the influence scoring process.
- Decision owner: Program Director
- Options: Dedicated committee / Regular committee meetings / User involvement in governance

### C2 · MAJOR · blocks the build

**What are the specific, agreed-upon criteria used to calculate influence scores?**

- Why it matters: Clear criteria prevent inconsistent scoring, ensuring users have a common understanding to prioritize contacts effectively.
- Decision owner: Governance Committee Lead
- Options: Engagement history / Seniority / Recent interactions / Combination of these

### C4 · MAJOR · blocks the build

**What processes are established for routinely validating and updating influence scores for accuracy?**

- Why it matters: Regular validation ensures that users are relying on current and relevant influence scores, reducing the risk of outdated information affecting decisions.
- Decision owner: Head of Data Quality
- Options: Quarterly reviews / Feedback from users / Automated adjustments based on interaction data

### C7 · MAJOR · blocks the build

**What measures will be implemented to maintain the accuracy of influence scores post-assignment?**

- Why it matters: Ensuring ongoing accuracy is crucial for maintaining the integrity of the database and preventing misallocation of resources.
- Decision owner: Governance Committee Lead
- Options: Quarterly reviews / Random audits / Updates triggered by user feedback

### C11 · MAJOR · blocks the build

**What explicit criteria will be used for assigning initial influence scores to contacts?**

- Why it matters: Defining clear criteria ensures consistency across the organization and reduces subjective assessments of influence.
- Decision owner: Governance Committee Lead
- Options: Statistical analysis of engagement / User role and title / External validation

### C6 · MINOR · blocks the build

**What is the defined retention policy for influence score data in compliance with data protection regulations?**

- Why it matters: A clear retention policy safeguards against legal risks related to data management and enhances compliance measures.
- Decision owner: Data Protection Officer
- Options: 1 year / 3 years / 5 years

### C8 · MAJOR · does not block the build

**What is the anticipated user workload for maintaining influence score systems?**

- Why it matters: Clear expectations help manage user responsibilities effectively and prevent potential burnout.
- Decision owner: Project Manager
- Options: Assumed workload based on role / Feedback forms post-implementation / Trial period assessments

### C5 · MINOR · does not block the build

**What are the expected time commitments and workload implications for users managing influence scores?**

- Why it matters: Understanding user workload is essential to prevent fatigue and ensure effective maintenance of influence scoring.
- Decision owner: HR Manager
- Options: 1 hour per month / 2 hours per month / 3 hours per month

## Tension report

The primary disagreement centered around the clarity and definition of criteria for influence scoring, which the critic felt lacked sufficient detail to ensure consistent application among users. The proposer aimed to clarify these points through revisions, but several critical issues regarding governance, accountability, and user workload remain unresolved, leading to escalations and a need for human decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 8 | 2 | 1 | 5 | 0.87 | 85 | 50 | CONTINUE | continue |
| 3 | 10 | 4 | 1 | 5 | 0.90 | 85 | 50 | CONTINUE | continue |
| 4 | 11 | 3 | 1 | 7 | 0.91 | 75 | 70 | CONTINUE | continue |
| 5 | 11 | 1 | 1 | 9 | 0.91 | 70 | 30 | CONTINUE | continue |
| 6 | 11 | 0 | 1 | 10 | 0.91 | 75 | 50 | CONTINUE | converged |

- Proposer's remaining worry (75/100): The successful implementation of this feature hinges on user adherence to the defined criteria, which may vary in interpretation.
- Critic's remaining worry (50/100): The criteria for influence scores remain ambiguous and untested, risking inconsistent scoring and potential diplomatic breaches.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | OWNERSHIP | A1, D3 | R1 | ESCALATED | 0 | The proposal does not clarify who specifically has the authority to assign and modify influence scores, creating risks for misuse. |
| C2 | MAJOR | DEFINITIONS | D1, A2 | R1 | ESCALATED | 0 | The criteria for what constitutes an influence score and how it is calculated are not defined, leading to inconsistent scoring across different users. |
| C3 | MAJOR | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The scoring system could lead to potential confidentiality breaches, as the influence scores might reveal sensitive assessments of contacts that should be protected. |
| C4 | MAJOR | DATA_QUALITY | A3, S4 | R1 | ESCALATED | 0 | The proposal lacks clarity on how influence scores will be validated and maintained for accuracy, raising concerns about data quality. |
| C5 | MINOR | OPERATIONS | A1 | R1 | ESCALATED | 0 | The proposal does not consider the impact on users' workload in maintaining and assigning influence scores, potentially leading to user fatigue. |
| C6 | MINOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | The proposal does not address how long influence data will be retained or the legal basis for processing this personal data, raising compliance issues. |
| C7 | MAJOR | DATA_QUALITY | A3 | R2 | ESCALATED | 2 | The proposal lacks clarity on how influence scores will be validated and maintained after the initial assignment, raising concerns about data quality. |
| C8 | MAJOR | OPERATIONS | A1 | R2 | ESCALATED | 2 | There is no clarity on the expected workload and time commitment for users to maintain the influence scoring system, which could lead to fatigue and inefficiency. |
| C9 | BLOCKER | DATA_QUALITY | GAP | R3 | ESCALATED | 1 | The proposal does not provide a clear mechanism for validating or updating influence scores post-assignment, which could lead to outdated or incorrect scores being used. |
| C10 | BLOCKER | OPERATIONS | GAP | R3 | ESCALATED | 1 | There is no defined governance structure to manage the influence scoring process over time, which is essential for consistent application and accountability. |
| C11 | MAJOR | DEFINITIONS | GAP | R4 | ESCALATED | 2 | The proposal does not adequately define what criteria are used to assign the initial influence scores, creating ambiguity. |
