# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 6 rounds (policy `naive`) · $0.020.

Challenges: 17 raised · 13 settled between the agents · 3 handed to humans · 1 still open when it ended.

## Summary

This release will implement an automatic logging feature for meetings with government officials in the Government CRM to ensure accurate tracking of engagement histories. The implementation will outline specific roles for those allowed to log meetings, detail measures for data security, and establish clear success criteria for logged records. However, questions remain regarding training responsibilities, confidentiality protocols, and ownership of data accuracy for logged meetings.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable automatic logging of meetings with government officials to preserve engagement history.  
  The core commitment to enable automatic logging of meetings was accepted to preserve engagement history as a necessary feature.

**In scope**

- **S1** Implement a feature that allows users to log meetings automatically in the Government CRM whenever a user marks that a meeting has taken place.  
  The in-scope item enabling users to log meetings automatically in the CRM was accepted to streamline meeting documentation.
- **S2** The automatic log will include fields for the meeting date, participants (both user and government officials), summary of the discussion, and follow-up actions needed. Meetings that involve sensitive topics or participants will be flagged in the system, and access to these logs will be restricted to only those users who have the appropriate security clearance, with the access control monitored by designated data managers.  
  The automatic log’s details, including sensitive flags and access controls, were emphasized to protect confidentiality and ensure proper data handling for sensitive topics. _(C2, C9, C15)_
- **S3** Users can view logged meetings in the engagement history section of the CRM for their government contacts, but only if they have the required security clearance to view those records.  
  The revision ensuring access to logged meetings is restricted based on user roles was accepted to enhance confidentiality for sensitive engagement records. _(C2)_
- **S4** The feature will only log meetings involving users with specific roles, including regional coordinators and project managers, who have been granted access to log meetings with government officials based on their security clearance.  
  The specification clarifying which roles can log meetings based on security clearance was accepted to address ownership concerns and confidentiality. _(C1)_
- **S5** The system will include a process to detect and manage duplicate meeting entries by cross-referencing meeting logs and notifying users when duplicates are suspected.  
  The process for detecting and managing duplicate meeting entries was accepted to ensure data quality and avoid clutter in engagement histories. _(C5)_
- **S6** The feature will include a designated data manager responsible for auditing logged meetings quarterly and maintaining overall accuracy. This individual will handle disputes raised by users regarding logged entries, making them the point of contact for resolving logging issues and discrepancies, thereby ensuring data integrity.  
  The clarification on the auditing and dispute resolution processes for logged meetings was accepted to ensure accuracy and accountability. _(C11, C12, C17)_

## What it will not do

**Out of scope for this release**

- **X1** The logging feature will not include automatic captures of meeting notes or detailed transcripts.
- **X2** Integration with external calendar systems for meeting scheduling and logging is not included in this release.
- **X3** Real-time updates or notifications about meeting logs will not be included, aiming for simplicity in the first release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users are trained to use the automatic logging feature effectively; therefore, training sessions will be arranged before the feature is rolled out. | Kept | C4 → escalated |
| A2 | The existing CRM system supports adding new features without major architectural changes regarding data handling. | Kept | never challenged |
| A3 | All users with the ability to log meetings have the required security clearance to access the logged information. | Kept | never challenged |

## Definitions

- **D1** "automatic logging" means the system will record meetings without requiring the user to manually input this information, triggered by user actions indicating a meeting occurred, such as the users marking that the meeting is set on their calendar and confirming attendance.  
  The definition of 'automatic logging' was revised to clarify logging triggers, ensuring accuracy in logging events and reducing errors. _(C3)_
- **D2** "engagement history" means the cumulative records of interactions and meetings with government contacts tracked within the CRM.  
  The definition of 'engagement history' was established to outline the scope of the records tracked within the CRM without contention.

## Success criteria

- **K1** At least 90% of logged meetings are correctly captured in the system, defined as entries including all required fields (date, participants, summary, follow-up actions) and no user-reported discrepancies. This will be measured by user feedback, quarterly audit checks, and by ensuring that disputes about logged entries are resolved.  
  The collection of success criteria for logged meetings includes measures of correctness, ensuring clarity and accountability in evaluating log entries. _(C6, C13, C14)_

## Open questions for humans

### C4 · MAJOR · blocks the build

**Who will be responsible for verifying the accuracy of logged meetings and overseeing training for users?**

- Why it matters: Clarifying ownership is essential for accountability regarding data integrity.
- Decision owner: Head of Data Protection
- Options: Designate a data manager / Create a training committee / No specific oversight role

### C8 · MAJOR · blocks the build

**What protocols are established to ensure confidentiality for sensitive information logged during meetings?**

- Why it matters: To safeguard against potential leaks and ensure adherence to confidentiality measures.
- Decision owner: Head of Data Protection
- Options: Implement strict access protocols / Train users on confidentiality / Regular compliance audits

### C11 · MAJOR · blocks the build

**Who will have the responsibility for maintaining the accuracy of logged meeting records, and what processes will be established for audits?**

- Why it matters: Clear accountability is crucial to build trust in the system.
- Decision owner: Head of Data Protection
- Options: Assign responsibilities to a specific role / Delegate to the logging users / No specific role designated

### C16 · MAJOR · blocks the build

**What mechanisms will be put in place to ensure that meetings with sensitive topics or participants are flagged appropriately?**

- Why it matters: Ensuring appropriate access control measures will mitigate the risk of unauthorized information access.
- Decision owner: Head of Data Protection
- Options: Automated flagging system / Manual logging review process / No specific flagging mechanism

## Tension report

The main disagreement centered around ownership and accountability for data integrity and confidentiality measures. The Proposer believed the proposed roles would suffice, while the Critic expressed concern that the lack of definitive responsibilities can lead to potential data inaccuracies. Despite comprehensive resolutions for many challenges, key questions remain unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 45 | - | continue |
| 2 | 8 | 2 | 5 | 1 | 0.40 | 85 | 60 | CONTINUE | continue |
| 3 | 11 | 4 | 5 | 2 | 0.59 | 80 | 60 | CONTINUE | continue |
| 4 | 12 | 1 | 8 | 3 | 0.33 | 85 | 75 | CONTINUE | continue |
| 5 | 17 | 6 | 8 | 3 | 0.54 | 85 | 55 | CONTINUE | continue |
| 6 | 17 | 1 | 13 | 3 | 0.23 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Potential misunderstandings regarding the defined roles may still impact data integrity if not embraced by all users.
- Critic's remaining worry (85/100): While the proposal addresses previous challenges adequately, the effectiveness of the logging feature in preventing incorrect attribution remains a concern.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | OWNERSHIP | S4 | R1 | REVISED | 0 | The proposal does not clearly define which specific roles can log meetings, potentially allowing unauthorized users to log sensitive government engagements. |
| C2 | MAJOR | CONFIDENTIALITY | S1, S3 | R1 | REVISED | 0 | There is no mention of how the system will ensure that only permitted users can view the logged meetings, raising concerns about unauthorized access to sensitive engagement records. |
| C3 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'automatic logging' lacks clarity on how the system recognizes and verifies a meeting has occurred, which could lead to incorrect logging of events. |
| C4 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 0 | There is an assumption that all users logging meetings will be appropriately trained, but it doesn't clarify the responsibilities for maintaining and overseeing the accuracy of logged data. |
| C5 | MINOR | DATA_QUALITY | S5 | R1 | REVISED | 0 | The proposal does not address how duplicate meeting entries will be managed or detected, which could lead to clutter in engagement histories. |
| C6 | MINOR | DATA_QUALITY | K1 | R1 | REVISED | 0 | The success criteria of having 90% of logged meetings correctly captured is vague; there are no specifics on how 'correctly' is defined or measured. |
| C7 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 1 | There is no definition of what constitutes a 'correct' follow-up action, potentially leading to misunderstandings about responsibilities following logged meetings. |
| C8 | MAJOR | CONFIDENTIALITY | GAP | R2 | ESCALATED | 0 | The proposal does not specify the process for handling sensitive information that may arise from logged meetings and how it will be safeguarded. |
| C9 | BLOCKER | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal does not outline how meetings with sensitive topics or participants will be securely flagged or logged to ensure appropriate access controls and confidentiality measures are applied. |
| C10 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The definition of 'correctly captured' in the success criteria is not clear; it lacks specificity regarding what constitutes correctness in the logged meeting records. |
| C11 | MAJOR | OWNERSHIP | GAP | R3 | ESCALATED | 0 | The proposal does not clarify who will be responsible for auditing and maintaining the accuracy of logged meetings, especially in cases of disputes or errors in logging. |
| C12 | MAJOR | OWNERSHIP | GAP | R4 | REVISED | 1 | The proposal does not outline what processes will be in place for audits and dispute resolution, creating potential confusion about data accuracy responsibilities. |
| C13 | MAJOR | DEFINITIONS | K1 | R5 | REVISED | 0 | The success criteria of having 90% of logged meetings correctly captured is vague and does not specify how 'correctly' is defined, risking inconsistent evaluations of the automatic logging feature's effectiveness. |
| C14 | MAJOR | DEFINITIONS | GAP | R5 | REVISED | 0 | The success criteria lack specificity on what constitutes 'correctly captured' meeting records, potentially leading to confusion on the evaluation metrics applied during auditing. |
| C15 | BLOCKER | CONFIDENTIALITY | GAP | R5 | REVISED | 0 | The proposal lacks a clear strategy for how sensitive information from logged meetings will be safeguarded and who has the authority to access this information, posing a risk of unauthorized access or data leaks. |
| C16 | MAJOR | CONFIDENTIALITY | GAP | R5 | UNRESOLVED | 1 | There is insufficient detail on how meetings involving sensitive topics or participants will be flagged, creating uncertainty about access controls and confidentiality measures. |
| C17 | MAJOR | OWNERSHIP | GAP | R5 | REVISED | 0 | There is still ambiguity regarding who will be responsible for the accuracy of logged meetings and dispute resolution processes, which is critical for trust in the logging feature's data integrity. |
