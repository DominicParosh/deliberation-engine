# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 4 rounds (policy `gated`) · $0.008.

Challenges: 8 raised · 2 settled between the agents · 6 handed to humans · 0 still open when it ended.

## Summary

This release will introduce a feature to categorize government contacts by their level of influence, allowing users to prioritize interactions accordingly. However, the implementation details regarding the ongoing maintenance and review of influence assessments remain under discussion. The organization still needs to clarify specific regulations on data handling and review criteria for influence levels.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users can view the influence level of each contact in the Government CRM.  
  Users will be able to view the influence level of each contact in the Government CRM, providing a clear understanding of their relationships.
- **V2** Users are able to sort and filter contacts based on their influence level.  
  Users are able to sort and filter contacts based on their influence level, ensuring that prioritization can easily occur.

**In scope**

- **S1** A new field called 'Influence Level' will be added to each contact record in the Government CRM.  
  A new field called 'Influence Level' will be added to each contact record to facilitate the categorization process.
- **S2** Influence Level will be categorized into three levels: 'High', 'Medium', and 'Low'.  
  The influence level will be categorized into three levels: 'High', 'Medium', and 'Low', providing a simple and understandable classification. _(C2)_
- **S3** Users will be able to filter the contacts list to show only those with 'High' influence.  
  Users will be able to filter the contacts list to show only those with 'High' influence, making it easier to focus on key contacts.
- **S4** Training materials will be developed and must include clear guidelines, practical examples, and assessments that require users to demonstrate their understanding and application of the influence categorization process.  
  Training materials will include guidelines, practical examples, and assessments to ensure users effectively understand the influence categorization process. _(C4)_
- **S5** Users can view the influence status directly on the contact detail pages.  
  Users can view the influence status directly on contact detail pages, facilitating quick access to essential classification information.
- **S6** Only designated team members, such as regional coordinators and project managers, will have the authority to assign and alter the 'Influence Level' for contacts.  
  Only designated team members will have the authority to assign and alter 'Influence Level', ensuring that only qualified individuals handle this sensitive data. _(C7)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automatic determination of influence levels; these will be manually assigned by designated team members.  
  Automatic determination of influence levels will not be included to maintain a high level of accuracy through manual assessments.
- **X2** This release will not add any predictive analytics or algorithms to determine future influence.  
  This release will not include predictive analytics or algorithms as the focus is on current influence levels only.
- **X3** The feature will not include influence tracking over time; it will focus solely on current influence levels.  
  Influence tracking over time will not be incorporated as the feature will focus solely on current levels, streamlining implementation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that designated team members will have the authority to classify influence levels, based on their knowledge of contacts. | Kept | never challenged |
| A2 | It is assumed that users will have adequate training to understand how to use the new influence categorization feature. | Kept | never challenged |
| A3 | It is assumed that there are existing procedures for updating contact information, which will include the new influence level field. | Kept | C3 → escalated |
| A4 | It is assumed that existing security and privacy regulations on sensitive data handling will be adhered to in the feature deployment. | Kept | C6 → escalated |

## Definitions

- **D1** 'Influence Level' means a classification assigned to a contact based on their ability to affect decisions or outcomes related to the organization's activities.  
  'Influence Level' is clearly defined as a classification that reflects a contact's ability to affect organizational outcomes, enhancing clarity.
- **D2** 'High', 'Medium', 'Low' influence means the following: 'High' indicates significant decision-making power or authority, 'Medium' indicates moderate influence without decision-making power, and 'Low' indicates minimal influence on decision-making.  
  The definitions of 'High', 'Medium', and 'Low' are clear and outlined, aiding users in consistent assessment. _(C2)_
- **D3** The criteria for assigning 'Influence Level' will be based on the contact's role, previous engagement history, and demonstrated ability to influence decisions related to the organization's activities.  
  Criteria for assigning influence levels are now defined, providing a consistent framework that mitigates subjectivity in evaluations. _(C8)_

## Success criteria

- **K1** At least 75% of users report that the influence categorization has improved their prioritization of contacts, measured through user feedback surveys.  
  User feedback surveys will measure the success criterion, focusing on whether the influence categorization improves prioritization.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What process is in place to ensure that influence levels are regularly reviewed and updated?**

- Why it matters: Regular updates are critical to maintain the accuracy and relevance of influence assessments as relationships evolve.
- Decision owner: Head of Operations
- Options: Define a regular review cycle / Assign specific individuals for periodic evaluations / Outline a process for user feedback on influence levels

### C2 · MAJOR · blocks the build

**What specific criteria will define 'High', 'Medium', and 'Low' influence, and who will be responsible for establishing them?**

- Why it matters: Clearly defined criteria are essential for consistent and objective influence level assignments, reducing bias.
- Decision owner: Head of Data Governance
- Options: Create a committee to define criteria / Use existing data relationships as a guide / Develop criteria based on user-feedback

### C3 · MAJOR · blocks the build

**Who is explicitly responsible for maintaining and updating the influence levels in contacts?**

- Why it matters: Clarifying ownership prevents data inaccuracies that could arise following personnel changes.
- Decision owner: Executive Management
- Options: Assign a specific role to manage updates / Establish a collaborative process for updating influenced levels / Define a fallback process for absent team members

### C6 · MAJOR · blocks the build

**Which specific security and privacy regulations will govern the handling of influence level data?**

- Why it matters: Clarity on applicable regulations is essential for ensuring compliance and protecting sensitive information throughout the categorization process.
- Decision owner: Head of Data Protection
- Options: Consult legal for detailed compliance requirements / Review existing GDPR and data protection guidelines / Align with current organizational policies

### C4 · MINOR · does not block the build

**What measures will be put in place to ensure that users are adequately trained to understand and apply influence classifications?**

- Why it matters: Effective training is crucial to ensure accurate use of the influence categorization feature and improve engagement efforts with contacts.
- Decision owner: Training Coordinator
- Options: Implement a comprehensive training program / Use assessments with real scenarios / Follow-up training sessions to reinforce knowledge

### C5 · MINOR · does not block the build

**What is the procedure if a designated team member responsible for assigning influence levels is unavailable?**

- Why it matters: A fallback process is essential to maintain workflow and responsiveness to urgent needs despite personnel absences.
- Decision owner: Head of Project Management
- Options: Create a backup designation process / Implement a temporary authority delegation / Develop alternative access for influence assignment

## Tension report

The primary tension revolved around the necessity for a clear and consistent process for maintaining and updating influence assessments, as well as the definitions guiding influence categorization. While both parties acknowledged the importance of these processes, the proposer favored a flexible approach, while the critic insisted on specific guidelines, leaving several key questions open for further resolution.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 6 | 1 | 0 | 5 | 1.00 | 70 | 20 | CONTINUE | continue |
| 3 | 8 | 2 | 0 | 6 | 1.00 | 80 | 35 | CONTINUE | continue |
| 4 | 8 | 0 | 2 | 6 | 0.69 | 80 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): There may still be ambiguity in how influence levels are maintained and updated over time.
- Critic's remaining worry (85/100): Inaccurate influence assessments could still arise from subjective evaluations despite clearer criteria.
- ⚠ Proposer reported 80/100 confidence while blocker(s) C1 remain unsettled.
- ⚠ Critic reported 85/100 confidence while blocker(s) C1 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | ESCALATED | 0 | The influence categorization could lead to decisions being made on outdated or incorrect influence assessments, especially as relationships change over time. |
| C2 | MAJOR | DEFINITIONS | S2 | R1 | ESCALATED | 0 | The terms 'High', 'Medium', and 'Low' for influence are vague without established criteria, potentially leading to inconsistent or subjective assignments. |
| C3 | MAJOR | OWNERSHIP | A3 | R1 | ESCALATED | 0 | The assumption that there are existing procedures for updating contact information must include explicit ownership for maintaining the accuracy of the influence level. |
| C4 | MINOR | OPERATIONS | S4 | R1 | ESCALATED | 2 | The effectiveness of training materials is uncertain; how will it ensure all users understand the influence categorization process? |
| C5 | MINOR | FEASIBILITY | X1 | R1 | ESCALATED | 0 | If the influence levels are to be manually assigned, what is the fallback process if designated team members are unavailable? |
| C6 | MAJOR | COMPLIANCE | A4 | R1 | ESCALATED | 0 | The assumption about adhering to existing security and privacy regulations does not specify which regulations apply to the data being handled, particularly in terms of influence categorization. |
| C7 | MAJOR | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal lacks clear guidelines on who can assign and alter the 'Influence Level' for contacts, raising risks of unauthorized or inconsistent changes to sensitive contact information. |
| C8 | BLOCKER | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not define the criteria or process by which influence levels are assigned, leading to potential inconsistencies and subjective judgments. |
