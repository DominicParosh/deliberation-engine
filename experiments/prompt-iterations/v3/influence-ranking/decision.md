# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 6 rounds (policy `gated`) · $0.013.

## Summary

This release will implement a system for identifying and ranking contacts based on their influence, providing tools for regional coordinators and project managers to prioritize their engagement strategies. However, several key questions remain regarding the specific criteria for influence scoring and accountability mechanisms for maintaining data accuracy. Those issues need to be resolved before the build can begin.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide a ranked list of contacts based on their influence.  
  The core commitment to provide a ranked list of contacts based on their influence reflects the foundational purpose of the new feature, ensuring prioritization in engagement.
- **V2** Allow users to filter and segment contacts for targeted engagement.  
  The commitment to allow filtering and segmenting contacts supports targeted engagement efforts, addressing user needs for effective outreach and relationship management.

**In scope**

- **S1** Develop an influence scoring system that assigns scores from 1 to 10 to each contact based on predefined criteria such as position, past project involvement, engagement frequency, and communication history.  
  Developing an influence scoring system will enable systematic analysis and prioritization of contacts, crucial for operational success. _(C1)_
- **S2** Create an interface for users to view contacts with their influence scores displayed.  
  Creating an interface to display influence scores ensures that users can easily access and utilize this information for decision-making.
- **S3** Implement sorting functionality to allow users to view contacts in order of influence scores.  
  The implementation of sorting functionality will enhance usability, allowing users to organize contacts effectively according to their scores.
- **S4** Enable a filtering system to categorize contacts by region and active projects.  
  Enabling a filtering system for categorizing contacts is essential for focused engagement by region and project, enhancing strategic outreach efforts.
- **S5** Ensure that all data handling complies with existing data protection regulations, including implementing role-based access controls and encryption for sensitive data.  
  Ensuring compliance with data protection regulations through role-based access control and encryption addresses critical confidentiality concerns. _(C2)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include a detailed analysis of influence dynamics or predictive modeling for future influence.  
  The decision to exclude detailed analysis of influence dynamics is based on the focus of this release on foundational scoring rather than predictive modeling.
- **X2** User training and documentation for the new feature will not be included in this release.  
  User training and documentation were excluded to prioritize the core feature implementation, with training to be addressed in future updates.
- **X3** Integration with external databases to gather additional data points about contacts will not be included.  
  Integration with external databases was dropped to maintain a focused approach within the existing data framework and avoid complexity in initial implementation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users have access rights to view and manage contact data within the CRM. | The feature requires users to interact with sensitive data stored in the CRM. | C3 → escalated |
| A2 | Data regarding contact roles and previous engagements is accurately maintained within the system. | The influence scoring system relies on accurate and up-to-date information about contacts. | Accepted (never challenged) |
| A3 | Existing data protection regulations are understood and adhered to by the organization during implementation. | Data processing and assessment of influence scores need to comply with regulations. | Accepted (never challenged) |

## Definitions

- **D1** "influence scoring system": A method of ranking contacts from 1 to 10 based on their perceived impact, determined by factors including but not limited to their role in government, involvement in projects, engagement frequency, and communication history.  
  The definition of the influence scoring system clarifies how contacts are assessed, which is critical for transparency and effective usage.
- **D2** "influence": The ability of a contact to affect decisions or policies within their government or agency, assessed through historical engagement data.  
  Defining 'influence' ensures a common understanding of what factors contribute to contact prioritization, vital for consistent application of the scoring system.

## Success criteria

- **K1** Percentage of users able to identify top 10 influential contacts within 5 minutes of using the feature.: target 80% (Measured by user feedback and usability testing results.)  
  Setting a target for user identification of top contacts within 5 minutes is a clear performance criterion to measure the feature's success and usability.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What specific criteria will be used to determine a contact's influence score?**

- Why it matters: This will ensure clarity in how influence is assessed and resources are allocated.
- Decision owner: Product Owner
- Options: Define clear scoring criteria / Leave to regional coordinators' discretion

### C2 · MAJOR · blocks the build

**What additional safeguards are necessary to protect influence scoring data from unauthorized access?**

- Why it matters: Establishing these safeguards is crucial to maintain confidentiality and trust in the system.
- Decision owner: Head of Data Protection
- Options: Implement comprehensive access controls / Maintain current access controls

### C3 · MAJOR · blocks the build

**Who is responsible for maintaining the accuracy and updating the influence scores?**

- Why it matters: Clear accountability is needed to ensure that influence scores reflect the latest data and decisions are effective.
- Decision owner: Product Owner
- Options: Assign responsibility to regional coordinators and project managers / Create a centralized team for this task

### C4 · MAJOR · blocks the build

**What process is in place for updating influence scores when contacts or their roles change?**

- Why it matters: Defining these processes is critical for ensuring the relevance and accuracy of influence scores over time.
- Decision owner: Product Owner
- Options: Establish a clear update protocol / Leave updates to individual user discretion

### C5 · MAJOR · blocks the build

**How frequently will the influence scores be reviewed and updated?**

- Why it matters: Establishing a regular review process is vital to keep the information current and prevent misprioritization in engagement.
- Decision owner: Product Owner
- Options: Set regular review intervals / Review as needed based on user reports

### C6 · MAJOR · blocks the build

**What specific accountability measures are in place for regional coordinators and project managers regarding the maintenance of influence scores?**

- Why it matters: Without established accountability, there may be inconsistencies in maintaining accurate engagement data.
- Decision owner: Product Owner
- Options: Implement clear accountability frameworks / Leave accountability unspecified

### C7 · MAJOR · blocks the build

**What is the timeframe for updates to influence scores after they have been established?**

- Why it matters: This timeframe will determine how responsive the system is to changes in contact relevance.
- Decision owner: Product Owner
- Options: Define a specific timeframe for updates / Update as needed without set intervals

## Tension report

Tension arose over the lack of clarity regarding criteria for assigning influence scores and the specifics of accountability for maintaining those scores. Despite numerous iterations, several critical questions remain unresolved, specifically regarding roles and responsibilities, leading to a deadlock that requires further decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 5 | 5 | 0 | 0 | 1.00 | 70 | 70 | CONTINUE | continue |
| 3 | 7 | 4 | 0 | 3 | 1.00 | 60 | 30 | CONTINUE | continue |
| 4 | 8 | 3 | 0 | 5 | 1.00 | 75 | 40 | CONTINUE | continue |
| 5 | 8 | 1 | 0 | 7 | 1.00 | 75 | 30 | CONTINUE | continue |
| 6 | 8 | 0 | 1 | 7 | 0.88 | 75 | 70 | CONCLUDE | consensus |

- Proposer's remaining worry (75/100): Ensuring compliance with data protection regulations while implementing access controls.
- Critic's remaining worry (70/100): While access controls are set by policy, the actual criteria and processes for determining influence scores remain unspecified.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | S1 | R1 | ESCALATED | 2 | The proposal does not specify the criteria that will be used to assign influence scores from 1 to 10. |
| C2 | MAJOR | CONFIDENTIALITY | S5 | R1 | ESCALATED | 2 | The proposal lacks details on how sensitive data related to contacts will be protected, especially the influence scores that could expose strategic priorities. |
| C3 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 2 | The proposal does not clarify who is responsible for maintaining the accuracy of the influence scoring system and ensuring data freshness. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 2 | The proposal does not address how the system will handle situations where contacts or roles change, impacting the accuracy and relevance of influence scores. |
| C5 | MAJOR | DEFINITIONS | GAP | R2 | ESCALATED | 2 | The proposal lacks clarity on how frequently influence scores will be updated, which is crucial for maintaining data relevance. |
| C6 | MAJOR | OWNERSHIP | GAP | R3 | ESCALATED | 2 | The proposal lacks clarity on accountability mechanisms for regional coordinators and project managers in maintaining influence scores. |
| C7 | MAJOR | DEFINITIONS | GAP | R3 | ESCALATED | 2 | The proposal does not specify the timeframe for updates to influence scores after they have been established. |
| C8 | MAJOR | CONFIDENTIALITY | GAP | R4 | DEFENDED | 1 | The proposal does not clarify who will have access to view the influence scores of contacts, which raises concerns about exposure to sensitive data. |
