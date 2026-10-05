# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **cap** after 8 rounds (policy `naive`) · $0.027.

Challenges: 23 raised · 18 settled between the agents · 2 handed to humans · 3 still open when it ended.

## Summary

The feature will enable users to view influence scores for each contact, aiding in prioritizing engagement efforts. Key elements include a defined influence scoring system based on specific criteria, monthly updates, and restricted access to sensitive data. However, several questions regarding implementation and compliance need resolution before development can commence.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable users to view an influence score for each contact so they can prioritize engagement efforts.

**In scope**

- **S1** Establish an influence scoring system that assigns a score from 1 to 10 for each contact based on three criteria: global position, mission involvement, and historical engagement frequency. Influence scores will be reviewed and updated monthly to reflect any changes in roles or engagement levels.  
  The in-scope item ensures monthly reviews and updates of influence scores to maintain accuracy, addressing concerns about outdated information due to role changes. _(C3)_
- **S2** Allow regional coordinators and project managers to filter and sort their contact list based on influence scores.
- **S3** Display influence scores alongside existing contact information in the CRM for the roles of regional coordinators and project managers only, with access to scores restricted such that users below these roles cannot view them, thereby protecting sensitive engagement data.  
  This item specifies restricted access to influence scores for appropriate roles, mitigating risks of unauthorized visibility and protecting sensitive data. _(C1, C20)_
- **S4** Provide an interface where users can view the criteria used to assess influence scores and include a warning system that alerts users about the importance of context and cautions against misinterpretation or misuse of influence data.  
  Provides users with safeguards against misinterpretation of influence scores through a warning system, emphasizing the importance of context in assessments. _(C5)_
- **S5** Establish a review schedule for the influence scoring criteria to occur semi-annually, ensuring they remain relevant and compliant. All changes will be communicated to users at each review.  
  Establishes a semi-annual review schedule for the influence scoring criteria, ensuring their compliance and relevance over time, meeting previously raised concerns about oversight. _(C7)_
- **S6** Designate a data steward responsible for monitoring and updating contact data on a quarterly basis, ensuring that all contact information and engagement activity is accurate and current prior to scoring.  
  Designates a data steward for quarterly monitoring of contact data accuracy, addressing fears of reliance on outdated information. _(C8)_
- **S7** Implement a compliance monitoring process that includes annual audits of the influence scoring system to ensure adherence to data protection regulations and the involvement of the data steward in this oversight.  
  Introduces annual compliance audits to ensure the influence scoring system adheres to data protection regulations, a critical aspect for mitigating potential legal issues. _(C23)_
- **S8** Assign the data steward as the accountable party for overseeing the influence scoring system, ensuring timely reviews and updates of influence scores according to the established schedules.  
  Assigns accountability for the influence scoring system to the data steward, ensuring clarity around responsibilities and timely updates of scores. _(C21)_
- **S9** Introduce training sessions and user guides designed to educate users on the proper interpretation of influence scores to prevent potential misuse. These sessions will emphasize the importance of context in interpreting scores and will be conducted quarterly during the user onboarding process and as part of any significant system updates.  
  Introduces training sessions to educate users on the proper interpretation of influence scores, mitigating risks of misuse and misinterpretation. _(C13)_
- **S10** Specifically define the review process of the influence scoring criteria to include a checklist of at least the following: assessment of the relevance of each criterion, alignment with current organizational goals, adherence to data protection regulations, and updates from user feedback. The data steward will be responsible for ensuring this checklist is completed during each semi-annual review.  
  Defines a comprehensive review process for influence scoring criteria to maintain consistency and appropriateness in assessments, addressing concerns about subjective evaluations. _(C15)_
- **S11** Establish an ongoing data maintenance protocol that includes designated users responsible for monitoring and updating contact data as changes occur, with a mandatory weekly check for data accuracy and an alert system within the CRM that flags any discrepancies immediately for review by the data steward.  
  Establishes an ongoing data maintenance protocol, though details on daily checks remain vague, which did not fully address operational quality between audits. _(C16)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated scoring updates; scores will be manually entered by designated users.
- **X2** Social media influence or external metrics will not be included in the scoring system for this release.
- **X3** Collaboration features or access controls beyond the basic CRM role permissions are out of scope for this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have sufficient permissions to view influence scores, depending on their role in the organization. | Kept | never challenged |
| A2 | The scoring criteria will be agreed upon by stakeholders before implementation begins. | Kept | never challenged |
| A3 | Influence scoring does not violate any data protection regulations concerning how contact information can be assessed or displayed. | Kept | never challenged |
| A4 | Contact data will be up to date and accurate to ensure correct scoring. | Kept | never challenged |
| A5 | Users will have access to training materials and guidance on interpreting influence scores to ensure understanding of the context-related factors influencing those scores. | Kept | C13 → revised |

## Definitions

- **D1** 'Influence score' means a numerical value ranging from 1 (minimal influence) to 10 (maximum influence) assigned to each contact based on their global position, mission involvement, and historical engagement frequency, where each criterion is measured against standardized benchmarks defined in the scoring guidelines.  
  Clarifies the definition of 'influence score' to enhance consistency in its application, addressing challenges around subjectivity in scoring methods. _(C10, C18)_
- **D2** 'Global position' means the official job title or role within the respective organization, defined by a standardized list of common titles evaluated for their influence potential across different countries, considering corresponding diplomatic weight.  
  Clarifies 'global position' to include considerations for international differences in roles, which was previously vague and risked misinterpretation. _(C2, C11)_
- **D3** 'Mission involvement' means the number of active projects or missions a contact is associated with within the CRM system.
- **D4** 'Historical engagement frequency' means the number of interactions recorded in the CRM between the organization and the contact over the past 12 months, standardized by type and context of engagement, ensuring categorization according to predefined engagement levels.
- **D5** 'Benchmark standards' means predefined measurable criteria, including specific weightings for 'global position', 'mission involvement', and 'historical engagement frequency', established through stakeholder agreement to ensure consistent application in the scoring process.  
  Establishes predefined measurable criteria for the influence score's components, aiming to promote consistent application and mitigate misunderstandings. _(C22)_

## Success criteria

- **K1** Achieve a minimum of 80% user satisfaction with the influence scoring feature as assessed by user feedback surveys within three months of deployment.
- **K2** At least 70% of users utilize the influence score filtering and sorting feature at least once a month after release.
- **K3** Implement a structured feedback mechanism within the CRM that allows users to submit comments and suggestions regarding the influence scoring system, with a target of incorporating relevant feedback into system updates at least twice a year.

## Open questions for humans

### C6 · MAJOR · blocks the build

**How often will the scoring criteria be reviewed to ensure they remain relevant and compliant?**

- Why it matters: Establishing a regular review frequency is crucial to ensure the scoring system aligns with any changes in regulations and organizational goals.
- Decision owner: Head of Compliance
- Options: Annually / Semi-annually / Quarterly
- Proposer's last word (R2, defend, needs human decision): The frequency of reviewing the scoring criteria to ensure relevance and compliance must be determined by the organization based on existing policies and regulations.
- Critic's last word (R2, escalate): Review frequency demands human oversight, hindering compliance assurance.

### C14 · MAJOR · blocks the build

**Who is responsible for ensuring compliance with data protection regulations during each review?**

- Why it matters: Clear oversight responsibility is needed to maintain compliance with data regulations, mitigating any legal risks.
- Decision owner: Head of Data Protection
- Options: Designate the data steward / Assign a compliance officer / Team approach with shared responsibility
- Proposer's last word (R6, defend, needs human decision): The oversight for compliance with data protection regulations during each review is a matter that is subject to existing organizational policies and should be determined by relevant stakeholders who understand legal compliance requirements.
- Critic's last word (R6, escalate): The responsibility for ensuring compliance remains undefined and reliant on unspecified organizational policies.

### C16 · MAJOR · blocks the build

**What ongoing process is in place to maintain the accuracy of contact data between the quarterly audits?**

- Why it matters: Ensuring data accuracy is vital for preventing outdated scores from compromising engagement decisions.
- Decision owner: Data Steward
- Options: Daily checks / Weekly updates / User-reported verification
- Proposer's last word (R8, revise, missing decision): This edit clarifies the mechanisms for ongoing data quality maintenance, ensuring that inaccuracies are addressed promptly between scheduled audits.
- Critic's last word (R8, maintain): While S11 mentions monitoring and updates, it lacks clear detail on how accuracy is ensured daily and what specific processes are in place.

### C17 · MAJOR · blocks the build

**What measures will be taken to ensure that the manual entry and review processes for influence scores do not create operational delays?**

- Why it matters: Operational delays could hinder timely updates, impacting the effectiveness of the influence scoring system.
- Decision owner: Project Manager
- Options: Clear timelines / Increased staffing / Automated systems
- Proposer's last word (R8, revise, missing decision): These edits provide concrete deadlines for both entry and review processes, which are designed to mitigate risks of delays in updating influence scores.
- Critic's last word (R8, maintain): The measures described still do not provide sufficient detail on how to avoid bottlenecks in score updates during manual processes.

### C19 · MAJOR · blocks the build

**What is the specific timeline for manual entry and peer review of influence scores?**

- Why it matters: Defining timelines is essential to ensure timely updates and prevent reliance on outdated data.
- Decision owner: Project Manager
- Options: Set weekly deadlines / Implement bi-weekly reviews / Flexible deadlines based on volume
- Proposer's last word (R8, revise, missing decision): This revision clarifies timelines for the peer review process and ensures timely updates to influence scores, thereby reducing the risk of acting on outdated information.
- Critic's last word (R8, maintain): While a timeline is now included, it does not fully address how user actions will be coordinated to avoid stale data.

## Tension report

The primary contention arose around the clarity and responsibility for ensuring compliance with data protection regulations during scoring criteria reviews, with concerns about accountability remaining unresolved. Disagreements also persisted over mechanisms for maintaining data quality and operational efficiency amidst manual processes, leading to open questions before any implementation begins.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 9 | 3 | 5 | 1 | 0.45 | 85 | 70 | CONTINUE | continue |
| 3 | 11 | 3 | 7 | 1 | 0.33 | 80 | 70 | CONTINUE | continue |
| 4 | 13 | 2 | 10 | 1 | 0.21 | 85 | 60 | CONTINUE | continue |
| 5 | 18 | 5 | 12 | 1 | 0.32 | 80 | 65 | CONTINUE | continue |
| 6 | 19 | 3 | 14 | 2 | 0.25 | 75 | 70 | CONTINUE | continue |
| 7 | 23 | 7 | 14 | 2 | 0.38 | 85 | 75 | CONTINUE | continue |
| 8 | 23 | 3 | 18 | 2 | 0.21 | 80 | 65 | CONTINUE | cap |

- Proposer's remaining worry (80/100): While I've attempted to address the open challenges, the success of the updates relies on clear implementation and adherence to timelines by the team.
- Critic's remaining worry (65/100): Unresolved operational bottlenecks and clarity on daily accuracy checks may lead to reliance on outdated influence scores.
- ⚠ C1 was settled by wording a later edit removed; the final proposal no longer says: "S3: Display influence scores alongside existing contact information in the CRM for the roles of regional coordinators and project managers only, ensuring that sensitive engagement data is not visible to lower-level staff."
- ⚠ C2 was settled by wording a later edit removed; the final proposal no longer says: "D2: 'Global position' means the official job title or role of a contact within their respective organization, which may include considerations for variations in political and organizational structures across different countries, defined by a list of equivalencies that aligns roles with their influence potential."
- ⚠ C9 was settled by wording a later edit removed; the final proposal no longer says: "Additionally, the data steward will conduct quarterly audits of the manually entered scores to cross-verify with engagement data to minimize discrepancies."
- ⚠ C18 was settled by wording a later edit removed; the final proposal no longer says: "'Benchmark standards' means predefined measurable criteria established through stakeholder agreement to quantify the global position, mission involvement, and historical engagement frequency, ensuring consistent application of influence scores across various contexts and user interpretations."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not clarify who can see the influence scores and the criteria used, leading to risks of unauthorized access to sensitive insights about contacts. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'global position' is vague; it fails to consider international differences in roles and the potential for misinterpretation. |
| C3 | MAJOR | OWNERSHIP | S1 | R1 | REVISED | 0 | The proposal does not address how influence scores will be updated in the event contacts change roles or their engagement level fluctuates, leaving the risk of outdated information. |
| C4 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The proposal does not define how users will provide feedback about the scoring system, leading to lack of iterative improvements and user dissatisfaction. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There are no safeguards described to prevent users from misinterpreting or misusing the influence scores, which could lead to significant diplomatic missteps. |
| C6 | MAJOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | The proposal does not stipulate how often the scoring criteria will be reviewed to ensure they remain relevant and compliant with any regulations. |
| C7 | BLOCKER | COMPLIANCE | GAP | R2 | REVISED | 0 | The proposal lacks a clear schedule for reviewing the scoring criteria, which is essential for compliance and relevance over time. |
| C8 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | There is no assurance that incoming data on contacts (e.g., roles, engagement frequency) will be kept updated and accurate, which is critical for correct scoring. |
| C9 | MAJOR | FEASIBILITY | GAP | R2 | REVISED | 1 | The manual entry of influence scores could lead to inconsistencies and inaccuracies, challenging the feasibility of reliable scoring within the system's planned operational parameters. |
| C10 | MAJOR | DEFINITIONS | D1 | R3 | REVISED | 0 | The definition of 'influence score' relies on potentially subjective criteria that may not be consistently measurable or interpretable across different contexts. |
| C11 | MAJOR | DEFINITIONS | D2, D4 | R3 | REVISED | 0 | The definitions of 'global position' and 'historical engagement frequency' may vary significantly across different countries and contexts, risking misrepresentation of influence. |
| C12 | MAJOR | OWNERSHIP | GAP | R4 | REVISED | 0 | The proposal still does not clarify how users will provide feedback regarding the scoring system, potentially leading to lack of iterative improvements and user satisfaction issues. |
| C13 | MAJOR | CONFIDENTIALITY | GAP | R4 | REVISED | 0 | While a warning system alerts users about context importance, there are no specified safeguards preventing misinterpretation or misuse of influence scores, which could result in damaging diplomatic decisions. |
| C14 | MAJOR | COMPLIANCE | GAP | R5 | ESCALATED | 0 | While the proposal includes a semi-annual review, it does not specify how compliance with data protection regulations will be monitored or who is responsible for this oversight. |
| C15 | MAJOR | DEFINITIONS | GAP | R5 | REVISED | 0 | The proposal does not define what constitutes a sufficient review process for the influence scoring criteria, leaving it open to subjective interpretation. |
| C16 | MAJOR | DATA_QUALITY | GAP | R5 | UNRESOLVED | 3 | The proposal mentions quarterly audits, but it lacks a mechanism for ensuring that contact data remains accurate between audits, raising concerns about data quality and reliability in scoring. |
| C17 | MAJOR | FEASIBILITY | GAP | R5 | UNRESOLVED | 3 | The manual entry of influence scores with peer review may introduce operational bottlenecks that affect the timely update of scores, impacting user experience and system effectiveness. |
| C18 | MAJOR | DEFINITIONS | D1 | R5 | REVISED | 0 | The definition of 'influence score' relies on subjective measures; without defined benchmarks, scores may not be applied consistently, impacting scoring reliability. |
| C19 | MAJOR | OPERATIONS | GAP | R6 | UNRESOLVED | 2 | The proposal does not define the specific timelines and procedures for peer review of influence scores, leaving operational gaps that could lead to bottlenecks. |
| C20 | MAJOR | CONFIDENTIALITY | GAP | R7 | REVISED | 0 | The proposal does not clarify how influence scores will prevent unauthorized access, especially regarding exposure to lower-level staff or contacts outside designated roles. |
| C21 | MAJOR | OWNERSHIP | GAP | R7 | REVISED | 0 | The proposal lacks specifics on who owns the influence scoring process and the accountability of those designated for its maintenance and updates. |
| C22 | MAJOR | DEFINITIONS | GAP | R7 | REVISED | 0 | The criteria used to define 'influence score' and how each element is weighted are not fully outlined, risking inconsistent application across different contexts. |
| C23 | MAJOR | COMPLIANCE | GAP | R7 | REVISED | 0 | There is no explicit mention of how the scoring system will adhere to data protection regulations, which is essential given the sensitivity of the data involved. |
