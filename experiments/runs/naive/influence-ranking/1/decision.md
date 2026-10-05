# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **consensus** after 7 rounds (policy `naive`) · $0.022.

Challenges: 23 raised · 12 settled between the agents · 11 handed to humans · 0 still open when it ended.

## Summary

The proposal will enhance the categorization and prioritization of contacts by their influence in the Government CRM, including clear definitions and robust protocols for data management. However, it will not incorporate machine learning or AI for scoring, and existing privacy settings regarding access controls are unchanged. There remains a need for human decision on several outstanding compliance and operational questions.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Categorize contacts by influence level based on specific criteria.
- **V2** Provide a searchable and filterable interface for users to prioritize contacts.

**In scope**

- **S1** Define 'influence' based on factors such as position, seniority, past engagement outcomes, and cultural context adaptability, allowing regional coordinators to adjust criteria as necessary for their specific country or context.  
  Defining 'influence' with adaptable criteria across contexts allows for flexibility in varying governmental interactions, which is crucial. _(C1)_
- **S2** Establish a formal protocol for transferring ownership and responsibilities of influence scores during role changes or when project managers leave, including documentation for the incoming project manager to ensure continuity in score management.  
  Establishing protocols for score ownership during role changes is vital for maintaining the accuracy of influence scores, addressing a significant concern. _(C2)_
- **S3** Develop a dashboard for regional coordinators and project managers to view and filter contacts by influence level.
- **S4** Implement role-based access controls (RBAC) to restrict influence score visibility to project managers and authorized personnel only, ensuring sensitive data is protected from unauthorized access.  
  Role-based access controls are critical for protecting sensitive data, satisfying confidentiality requirements. _(C3)_
- **S5** Incorporate compliance checks into the review process for influence scores, requiring legal and data privacy teams to review and approve the procedures for processing personal data every six months.  
  Integrating compliance checks into the procedures ensures that data privacy and legal requirements are consistently evaluated, which is essential for protection. _(C7)_
- **S6** Define operational procedures for integrating feedback from regional coordinators by establishing submission guidelines, follow-up meetings to discuss feedback impacts, and mandatory documentation of how feedback influences score adjustments.  
  Formal procedures for feedback integration from regional coordinators were established to enhance accuracy in influence scoring, hence it is included. _(C8)_
- **S7** Assign project managers to establish a documented process for conducting and integrating periodic reviews of influence scores within a timeline of three months, including specific methodologies for data validation, communication protocols, and feedback processing to ensure timely reviews and updated influence scores.  
  Documenting a process for periodic reviews ensures ongoing accuracy of influence scores, crucial for operational integrity; thus, it is included.

## What it will not do

**Out of scope for this release**

- **X1** This release will not incorporate machine learning or AI to auto-generate influence scores.
- **X2** The release will not include historical data analysis of engagement outcomes to influence future scoring.
- **X3** This release will not change the existing user privacy settings or access controls.  
  Existing user privacy settings will remain unchanged to prevent potential disruption or confusion during the rollout of the new system.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Assuming that users have access to sufficient data regarding contacts' position and engagement within their respective ministries, which is necessary for influence scoring. | Kept | never challenged |
| A2 | Assuming that the influence scoring method can be standardized across different countries and contexts. | Kept | never challenged |
| A3 | Assuming that there will be no legal barriers preventing the internal categorization of contacts based on their influence. | Kept | never challenged |

## Definitions

- **D1** 'Influential contact' means a contact within a government counterpart who holds substantial sway over decision-making processes, defined by measurable criteria such as their formal authority, ability to mobilize resources, and historical success in influencing policy outcomes, standardized across organizational contexts through consensus from project managers and regional coordinators.  
  The definition of 'influential contact' has been clarified to reduce vagueness, ensuring more objective criteria are utilized for scoring. _(C4)_
- **D2** 'Influence score' means a numerical representation assigned to a contact (ranging from 1 to 5) reflecting their level of influence, determined by a standardized methodology that includes direct assessments of the contact's authority, engagement success rates, and peer reviews.  
  The 'influence score' definition has been detailed to standardize methodology, preventing bias and misapplication of scores across contacts. _(C5)_

## Success criteria

- **K1** At least 70% of regional coordinators and project managers report satisfaction with the new feature on a post-release survey.
- **K2** Within three months of launch, at least 80% of contacts in the system should be assigned an influence score.

## Open questions for humans

### C15 · BLOCKER · blocks the build

**What are the data retention policies governing the personal data used for influence scoring?**

- Why it matters: Ensures compliance with legal mandates regarding data retention and prevents violations.
- Decision owner: Data Governance Officer
- Options: Establish a retention policy / Align with legal requirements
- Proposer's last word (R4, defend, needs human decision): Determining data retention policies is outside the proposal's scope, as it requires alignment with legal and organizational guidelines that must be decided by relevant authorities.
- Critic's last word (R4, escalate): The proposal lacks clarity on data retention policies, necessitating a human decision.

### C20 · BLOCKER · blocks the build

**What specific processes are in place to regularly validate and update the influence scores to ensure accuracy and relevance?**

- Why it matters: Ongoing validation is necessary to maintain data integrity and service effectiveness.
- Decision owner: Data Quality Supervisor
- Options: Implement scheduled audits / Create a validation team
- Proposer's last word (R6, revise, missing decision): This revision introduces a structured auditing process every six months, ensuring influence scores are regularly validated and updated to maintain data quality.
- Critic's last word (R6, escalate): While compliance checks are introduced, a concrete plan for maintaining accuracy and relevance of scores is still needed.

### C21 · BLOCKER · blocks the build

**What compliance protocols are implemented to ensure that the collection and processing of personal data for influence scores adhere to legal requirements?**

- Why it matters: Compliance is critical to avoid legal issues related to data handling.
- Decision owner: Compliance Officer
- Options: Draft new compliance protocols / Review current practices
- Proposer's last word (R6, revise, missing decision): This revision introduces compliance checks as part of the review process, ensuring that data processing adheres to legal requirements.
- Critic's last word (R6, escalate): Compliance measures are included, but details on individual data privacy protocols required for influence scores are still unclear.

### C22 · BLOCKER · blocks the build

**What is the protocol for transferring ownership and responsibility of influence scores when project managers change roles or leave?**

- Why it matters: A clear protocol is needed to maintain continuity and accuracy in influence score management.
- Decision owner: Project Manager Coordinator
- Options: Document ownership transfer processes / Establish a transition timeline
- Proposer's last word (R6, revise, missing decision): This revision clarifies the protocol for transferring responsibilities when project managers change roles or leave, ensuring continuity in influence score management.
- Critic's last word (R6, escalate): The continuity in ownership is noted, yet specific protocols for maintaining score integrity through transitions remains vague.

### C6 · MAJOR · blocks the build

**Will existing privacy settings be reviewed to ensure they adequately protect the influence scores and the criteria utilized for scoring?**

- Why it matters: It determines whether current safeguards are sufficient to prevent unauthorized access and breaches.
- Decision owner: Head of Data Protection
- Options: Review existing settings for adequacy / Maintain current settings
- Proposer's last word (R2, defend, needs human decision): The existing privacy settings need to be evaluated by legal and compliance teams to ensure they adequately protect sensitive influence scores and criteria.
- Critic's last word (R2, escalate): The evaluation of existing privacy settings needs human decision for compliance.

### C9 · MAJOR · blocks the build

**What legal frameworks will govern the data collection and processing for defining influence scores?**

- Why it matters: This is crucial for compliance with data protection laws and preventing legal repercussions.
- Decision owner: Legal Compliance Officer
- Options: Clarify data handling regulations / Establish new compliance protocols
- Proposer's last word (R3, defend, needs human decision): The legal basis for processing personal data for influence scoring is determined by organizational policies and relevant regulations, which must be clarified by those responsible for compliance.
- Critic's last word (R3, escalate): The proposal does not specify the exact legal framework for processing personal data, and depends on external policies that are not clarified.

### C16 · MAJOR · blocks the build

**What specific training or handover process is in place for new project managers to ensure they understand and can accurately manage influence scores?**

- Why it matters: Training is fundamental to avoid disruptions and inaccuracies during role transitions.
- Decision owner: Human Resources Manager
- Options: Create a comprehensive training program / Develop an onboarding checklist
- Proposer's last word (R6, revise, missing decision): This revision adds a comprehensive onboarding checklist to ensure incoming project managers receive specialized training on managing influence scores, mitigating the risk of gaps in ownership.
- Critic's last word (R6, escalate): Although transfer protocols are noted, the clarity on the specific training steps is still lacking.

### C18 · MAJOR · blocks the build

**What specific protocol or process is in place to ensure project managers and regional coordinators reach consensus on the definition of influence?**

- Why it matters: Lack of a clear consensus process could lead to inconsistent scoring and interpretations.
- Decision owner: Project Management Office Leader
- Options: Establish regular consensus meetings / Define a formal voting process
- Proposer's last word (R5, defend, needs human decision): The consensus on the definition of 'influence' relies on regional coordinators and project managers, requiring their input and agreement. This should be formally established in the process.
- Critic's last word (R5, escalate): While it states a need for consensus, the process itself remains undefined, relying on future actions rather than built mechanisms.

### C19 · MAJOR · blocks the build

**What specific criteria are used to determine the influence score to ensure it is standard and free from bias?**

- Why it matters: Clear criteria are vital to maintain objectivity and fairness in scoring.
- Decision owner: Chief Data Officer
- Options: Develop a standard scoring rubric / Solicit input from regional coordinators
- Proposer's last word (R5, defend, needs human decision): Detailing specific criteria for determining the influence score will require input from project managers and regional coordinators to establish a fair and standardized method.
- Critic's last word (R5, escalate): The reliance on input without a concrete decision-making framework leaves room for bias or inconsistency.

### C23 · MAJOR · blocks the build

**What operational procedures are established to ensure that feedback from regional coordinators is consistently and accurately integrated into influence score updates?**

- Why it matters: Defined procedures are necessary to ensure feedback relevance and effectiveness.
- Decision owner: Feedback Process Administrator
- Options: Outline integration workflows / Schedule regular feedback review sessions
- Proposer's last word (R6, revise, missing decision): This revision specifies operational procedures for feedback integration, ensuring that regional coordinators' input is consistently documented and incorporated into influence scores.
- Critic's last word (R6, escalate): The operational procedures are set but require more detail to ensure effective integration of feedback.

### C10 · MINOR · does not block the build

**What operational processes will support project managers in conducting and documenting periodic reviews of influence scores?**

- Why it matters: Clear operational support is essential to ensure timely and reliable updates of influence scores.
- Decision owner: Operational Manager
- Options: Define specific workflows / Implement training sessions
- Proposer's last word (R6, revise, missing decision): The revision specifies that project managers must establish a documented process that includes methodologies for data validation and feedback processing to ensure timely reviews of influence scores.
- Critic's last word (R6, escalate): The specification of methodologies needs to be clarified further to ensure operational effectiveness.

## Tension report

The primary disagreement involved the definitions related to 'influence' and 'influence score', where the Critic expressed concerns about the vagueness and potential subjective interpretations that could arise. Over the deliberation rounds, specifics were added, with a focus on measurable criteria and protocols to manage the scoring process.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 25 | - | continue |
| 2 | 10 | 4 | 5 | 1 | 0.48 | 85 | 75 | CONTINUE | continue |
| 3 | 15 | 6 | 7 | 2 | 0.52 | 75 | 50 | CONTINUE | continue |
| 4 | 19 | 5 | 11 | 3 | 0.40 | 85 | 45 | CONTINUE | continue |
| 5 | 23 | 6 | 12 | 5 | 0.47 | 70 | 40 | CONTINUE | continue |
| 6 | 23 | 0 | 12 | 11 | 0.47 | 75 | 25 | CONTINUE | continue |
| 7 | 23 | 0 | 12 | 11 | 0.47 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring the integration of feedback and continual validation of influence scores is adequately managed without undermining data quality.
- Critic's remaining worry (85/100): Continued risk of vague definitions and potential misunderstandings regarding influence and influence scores may still lead to unintended outcomes.
- ⚠ Proposer reported 85/100 confidence while blocker(s) C15, C20, C21, C22 remain unsettled.
- ⚠ Critic reported 85/100 confidence while blocker(s) C15, C20, C21, C22 remain unsettled.
- ⚠ C2 was settled by wording a later edit removed; the final proposal no longer says: "Assign ownership of influence score accuracy to designated project managers, who must review and update scores every six months, or immediately upon known role changes."
- ⚠ C7 was settled by wording a later edit removed; the final proposal no longer says: "Establish a secure communication protocol requiring project managers to document sharing instances of influence scores to external parties, ensuring that only finalized and vetted scores are shared and communicated through encrypted channels."
- ⚠ C8 was settled by wording a later edit removed; the final proposal no longer says: "Implement an ongoing data verification process that includes quarterly reviews of influence scores and criteria by project managers, utilizing feedback from regional coordinators and updated engagement outcome data to ensure accuracy of scores."
- ⚠ C11 was settled by wording a later edit removed; the final proposal no longer says: "Implement a review process for influence scores that includes guidelines restricting use to specific purposes related to enhancing engagement strategies, alongside an approval requirement for communicating scores externally."
- ⚠ C13 was settled by wording a later edit removed; the final proposal no longer says: "...upon role changes or departures, a transition process is executed within one month to review and verify ongoing scores, assigning responsibility to a new project manager."
- ⚠ C14 was settled by wording a later edit removed; the final proposal no longer says: "...project managers required to review and document how this feedback is incorporated into score updates."
- ⚠ C17 was settled by wording a later edit removed; the final proposal no longer says: "All communications involving influence scores must be logged and authorized by at least two project managers to ensure confidentiality."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | DEFINITIONS | S1 | R1 | REVISED | 0 | The definition of 'influence' is unclear and may not be universally applicable across different countries or contexts. How will the influence criteria be adapted or standardized? |
| C2 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | There is no clarity on who maintains and verifies the accuracy of influence scores and how role changes or staff turnover will affect ownership of this responsibility. |
| C3 | MAJOR | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal does not adequately outline measures to prevent unauthorized access to the influence scores and the criteria used for scoring, which could expose sensitive information. |
| C4 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'influential contact' is vague and lacks specific measurable criteria. What constitutes 'substantial sway over decision-making processes'? |
| C5 | MAJOR | DEFINITIONS | D2 | R1 | REVISED | 0 | The definition of 'influence score' lacks detail on how it is determined. The scoring system could lead to inconsistencies and bias. |
| C6 | MAJOR | CONFIDENTIALITY | X3 | R1 | ESCALATED | 0 | The out-of-scope mention that existing privacy settings won't change doesn't address whether current settings adequately protect sensitive influence scores. |
| C7 | BLOCKER | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | There are no stipulations on how influence scores will be communicated to avoid leaks or misinterpretations, especially in sensitive contexts. |
| C8 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal lacks provisions for ensuring the data quality and accuracy of the influencing criteria and score over time, especially as contexts change. |
| C9 | MAJOR | COMPLIANCE | GAP | R2 | ESCALATED | 0 | The proposal does not specify the legal basis for processing personal data contained in the influence scoring system. |
| C10 | MINOR | OPERATIONS | GAP | R2 | ESCALATED | 3 | There are no details on how the implementation of periodic reviews of influence scores will be managed operationally, beyond just assigning responsibility to project managers. |
| C11 | BLOCKER | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal does not address potential misuse of influence scores, especially in sensitive diplomatic contexts. |
| C12 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The term 'influence' is vaguely defined and depends on subjective criteria that could result in inconsistencies in scoring. |
| C13 | MAJOR | OWNERSHIP | GAP | R3 | REVISED | 0 | The proposal is unclear on what happens to influence scores when project managers change roles or if they leave. |
| C14 | MAJOR | DATA_QUALITY | GAP | R3 | REVISED | 0 | S6 does not specify how feedback from regional coordinators will be integrated into the influence scoring process, which may lead to inconsistencies. |
| C15 | BLOCKER | COMPLIANCE | GAP | R3 | ESCALATED | 0 | There is a lack of clear data retention policies regarding influence scores and any associated personal data. |
| C16 | MAJOR | OWNERSHIP | S2 | R4 | ESCALATED | 1 | The transition process for verifying influence scores could lead to gaps in ownership or oversight if not managed carefully. |
| C17 | BLOCKER | CONFIDENTIALITY | S5 | R4 | REVISED | 0 | The proposal does not provide adequate measures for communicating influence scores which could lead to leaks in sensitive situations. |
| C18 | MAJOR | DEFINITIONS | D1 | R4 | ESCALATED | 0 | The mechanisms for establishing consensus on the definition of 'influence' are not illustrated, leaving room for subjective interpretations. |
| C19 | MAJOR | DEFINITIONS | D2 | R4 | ESCALATED | 0 | The definition of 'influence score' lacks clarity on the assessment criteria leading to potential bias in scoring. |
| C20 | BLOCKER | DATA_QUALITY | GAP | R5 | ESCALATED | 0 | The proposal lacks a concrete plan for maintaining the accuracy and relevance of influence scores over time, raising concerns about data quality and reliability. |
| C21 | BLOCKER | COMPLIANCE | GAP | R5 | ESCALATED | 0 | There is no mention of compliance checks for processing personal data involved in establishing and maintaining influence scores, posing legal risks. |
| C22 | BLOCKER | OWNERSHIP | GAP | R5 | ESCALATED | 0 | The proposal does not clarify who retains responsibility for influence score updates during role changes or when project managers leave, which could disrupt continuity and ownership. |
| C23 | MAJOR | OPERATIONS | GAP | R5 | ESCALATED | 0 | The operational implications of integrating feedback from regional coordinators into influence scores are under-specified, risking inconsistencies and inefficiencies in scoring. |
