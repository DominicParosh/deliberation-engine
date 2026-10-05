# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.011.

Challenges: 10 raised · 7 settled between the agents · 3 handed to humans · 0 still open when it ended.

## Summary

This release will introduce a feature that identifies and ranks contacts by influence within their government organizations, alongside compliance measures for data protection. It will not include historical influence scoring or notifications about changes in scores. Further clarification on compliance with privacy laws is required.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Develop a feature to identify and rank the influence of contacts based on a defined influence scoring system.
- **V2** Provide a dashboard view for regional coordinators and project managers to display the influence rankings of their contacts.

**In scope**

- **S1** Update influence scores automatically when contact information changes in the CRM using a specified influence scoring formula, which includes criteria such as position level (weighted at 50%), previous engagement frequency (weighted at 30%), and relevance to current projects (weighted at 20%). The designated data steward is responsible for maintaining and updating influence scores accordingly.
- **S2** Enable users with roles of regional coordinators and project managers to view the influence score of each contact in the CRM, while access to these influence scores for all other roles within the organization will require special clearance from a designated data protection officer.
- **S3** Implement a filter feature that allows users to sort contacts by their influence score in contact lists.
- **S4** Design a user interface for a dashboard that showcases the most influential contacts based on the scoring system for regional coordinators and project managers.
- **S5** Establish a control mechanism where only designated authorized users, such as the data protection officer, can review and approve the release of influence scores, ensuring compliance with data protection laws. All users with access will be required to undergo training on data handling and compliance.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include historical influence scoring or external data sources for influence evaluation.
- **X2** The system will not provide influence rankings for contacts outside the current CRM database.
- **X3** This release will not include notifications or alerts related to contact influence updates.

**Rejected during deliberation**

- Nothing was dropped.
- Declined **C5** (MINOR · DATA_QUALITY): How will duplicates and inaccuracies in contact data be resolved to ensure reliable influence scoring? The Proposer's answer, which the Critic accepted: The system will rely on data management processes currently in use within the CRM, which includes regular checks for duplicates and accuracy of information, minimizing the risk associated with data quality.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Assuming that the organizational policy allows us to rate the influence of contacts without infringing on any privacy or data protection laws; the success of the influence scoring system depends on this. | Kept | C3 → escalated; C8 → escalated |
| A2 | Assuming that all necessary data about contacts, such as their roles and engagement history, is already captured in the CRM; the effectiveness of the influence scoring relies on this. | Kept | C6 → escalated |
| A3 | Assuming that users will have the necessary training to utilize the new influence score feature; the implementation of the dashboard depends on user readiness. | Kept | never challenged |

## Definitions

- **D1** "Influence" means the ability of a contact to affect decision-making processes within their government organization, which will be quantified through a custom scoring system.
- **D2** "Influence scoring system" means a method for calculating and assigning a numerical score to each contact, based on predetermined criteria like their position, past interactions, and relevance to specific projects.
- **D3** "Dashboard view" means a graphical interface presented to users that displays a list of contacts ranked by their influence scores, allowing for further sorting and filtering.
- **D4** "Influence scoring criteria" means the specific metrics and thresholds that determine a contact's influence score, including (1) a position level of 1-10, where 1 is the lowest and 10 is the highest based on governmental hierarchy; (2) engagement frequency scored as the number of interactions per year, with scores from 1 (1 or fewer interactions) to 10 (more than 10 interactions); and (3) relevance to current projects scored from 1 (not relevant) to 10 (highly relevant) based on the contact's formal association with ongoing projects.

## Success criteria

- **K1** At least 80% of regional coordinators and project managers report improved ability to prioritize contacts based on influence scores within the first month of implementation.

## Open questions for humans

### C3 · MAJOR · blocks the build

**What compliance measures are in place to ensure that the influence scoring mechanism adheres to data protection laws?**

- Why it matters: Clarifying compliance is crucial to protect the organization from legal repercussions due to potential violations of privacy regulations.
- Decision owner: Head of Data Protection
- Options: Define internal compliance controls / Consult with legal and compliance teams
- Proposer's last word (R2, defend, needs human decision): Compliance will be determined by designated legal and data protection officers who will dictate adherence to local and international privacy laws regarding the use of influence data.
- Critic's last word (R2, escalate): Compliance assurance relies on inputs from legal teams which are unconfirmed.

### C8 · MAJOR · blocks the build

**What specific measures are in place to ensure compliance with data protection laws regarding influence scoring?**

- Why it matters: Identifying specific compliance measures is essential to minimize legal risks related to data protection.
- Decision owner: Legal and Compliance Officer
- Options: Designate clear access roles for influence scores / Develop data sharing protocols
- Proposer's last word (R3, defend, needs human decision): While we can establish some internal controls, the specifics of compliance with data protection laws must be determined by our legal and compliance teams to ensure we do not violate privacy regulations.
- Critic's last word (R3, escalate): The specifics of compliance still depend on legal and compliance teams for verification.

### C6 · MINOR · does not block the build

**What guarantees are there that the required data to derive influence scores is complete and current?**

- Why it matters: Ensuring data completeness is necessary for accurate influence scoring, which directly impacts decision-making.
- Decision owner: Data Steward
- Options: Implement regular data audits / Establish manual data entry protocols for missing data
- Proposer's last word (R3, defend, acceptable risk): The assumption stands that project managers will verify that all necessary data is present before engaging with influence scores, and any missing critical data will be flagged for manual entry by users.
- Critic's last word (R3, maintain): Despite the defense, the proposal still lacks concrete measures to ensure data completeness, maintaining significant risk.

## Tension report

The main disagreement arose regarding compliance with data protection laws. While the Proposer was confident in the proposed features, the Critic emphasized the need for tangible compliance measures and training to prevent misuse and ambiguity in influence assessment.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 8 | 4 | 3 | 1 | 0.69 | 75 | 40 | CONTINUE | continue |
| 3 | 9 | 1 | 5 | 3 | 0.42 | 75 | 65 | CONTINUE | continue |
| 4 | 10 | 1 | 6 | 3 | 0.36 | 85 | 70 | CONTINUE | continue |
| 5 | 10 | 0 | 7 | 3 | 0.23 | 85 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring the ongoing accuracy and integrity of the influence scoring system as contact information evolves.
- Critic's remaining worry (80/100): The feature's effectiveness and usage may still strain relationships if ambiguity in influence scoring training persists.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | S1 | R1 | REVISED | 1 | The criteria for determining influence scores are not defined. What exactly constitutes a 'high' influence score, and how are its components weighted? |
| C2 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There is no mention of confidentiality safeguards to limit access to influence scores. Who can access these sensitive rankings and data, and what controls are in place? |
| C3 | MAJOR | COMPLIANCE | A1 | R1 | ESCALATED | 0 | The assumption about compliance with privacy laws is vague. How do we ensure that the influence scoring mechanism adheres to data protection laws? |
| C4 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | It is unclear how influence scores will be maintained and updated, especially when contacts change roles or leave. What is the ownership structure of this data? |
| C5 | MINOR | DATA_QUALITY | S3 | R1 | DEFENDED | 0 | There is no indication of how duplicates, inaccuracies, or outdated data will be managed in the influence scoring system. How will data integrity be maintained? |
| C6 | MINOR | FEASIBILITY | A2 | R1 | ESCALATED | 2 | The assumption that all necessary data is captured is unstated. What if critical data for the scoring system is missing? How is this mitigated? |
| C7 | BLOCKER | DEFINITIONS | S1 | R2 | REVISED | 0 | The exact definitions of influence scoring and criteria for high scores remain vague and undefined. |
| C8 | MAJOR | COMPLIANCE | A1 | R2 | ESCALATED | 0 | The proposal does not provide measures to ensure compliance with data protection laws regarding influence scoring. |
| C9 | BLOCKER | COMPLIANCE | GAP | R3 | REVISED | 0 | The proposal does not include any internal controls or measures to ensure compliance with data protection laws when sharing or utilizing influence scores. |
| C10 | BLOCKER | DEFINITIONS | GAP | R4 | REVISED | 0 | The influence scoring criteria are vague, especially on how influence is quantified and what constitutes a 'high' score. |
