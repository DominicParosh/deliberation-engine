# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 5 rounds (policy `gated`) · $0.012.

## Summary

An automatic logging feature for meetings with government officials will be implemented in the Government CRM. This feature will allow users, primarily regional coordinators and project managers, to maintain accurate engagement histories. However, unresolved issues regarding access controls and compliance with data protection regulations must be clarified by the relevant authorities before the build can commence.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable automatic logging of meetings with government officials.  
  The automatic logging feature will facilitate the tracking of meetings with government officials, as proposed by the product owner.
- **V2** Provide users the ability to view and access logged engagement history.  
  Users will have access to logged engagement history, ensuring transparency and accountability in tracking interactions with government officials.

**In scope**

- **S1** Implement functionality to record meetings initiated via the CRM system, capturing details such as date, time, participants, and a summary.  
  The functionality to record meetings via the CRM ensures that pertinent details are captured systematically, addressing the core concern of maintaining engagement history.
- **S2** Integrate with existing calendar tools (e.g., Microsoft Outlook or Google Calendar) to automatically log meetings scheduled with government officials.  
  Integrating with existing calendar tools supports seamless logging of meetings, which is essential for the automatic logging feature's effectiveness.
- **S3** Allow users to manually edit the logged meeting details post-logging for accuracy.  
  Allowing manual edits post-logging promotes accuracy in the recorded meeting details, which is critical given the sensitive nature of the information.
- **S4** Provide a report view for users to filter and search through logged meetings based on various parameters such as date range or participants.  
  Providing a report view enables users to filter and search through logged meetings, reinforcing the feature's utility in engagement tracking.
- **S5** Ensure that all logged meeting data is stored securely in compliance with data protection regulations, restricting visibility to roles with 'Engagement Manager' or 'Project Manager' permissions.  
  Securing logged meeting data in compliance with data protection regulations ensures restricted access, addressing concerns of confidentiality raised during deliberation. _(C1)_
- **S6** Designate ownership and responsibility for logged meeting data, ensuring that when a user changes roles or leaves the organization, their logged meetings can be reassigned to another relevant user.  
  Establishing ownership protocols for logged data prevents potential data management issues when users leave or change roles. _(C4)_
- **S7** Establish procedures and protocols to handle situations where automated logging fails, including manual reporting processes for missed meetings.  
  Setting up procedures for handling automated logging failures ensures that no crucial engagement information is lost, mitigating risks associated with missed logs. _(C5)_
- **S8** Define clear criteria for meetings to qualify for automatic logging, including formal meetings with government officials that are scheduled through integrated calendar tools.  
  Defining clear criteria for meetings that qualify for automatic logging clarifies expectations, enhancing the consistency of logged engagement history. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include logging engagement via informal communication channels such as emails or personal messages.
- **X2** No integration with external meeting software or platforms beyond calendar tools will be included in this release.
- **X3** User training or support documentation for this feature is not included in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users will have access to calendar tools (e.g., Microsoft Outlook or Google Calendar) that enable meeting logging functionality. | The feature requires synchronization with users' calendar tools to automatically capture meeting details. | Accepted (never challenged) |
| A2 | Users will regularly have meetings with government officials that should be logged to ensure accurate engagement history. | The necessity for automatic logging assumes that meetings with government officials are frequent. | Accepted (never challenged) |
| A3 | Users will be trained and required to utilize the logging feature in the CRM for it to be effective. | The feature's success relies on users consistently using the CRM to log meetings. | Accepted (never challenged) |
| A4 | The organization complies with relevant data protection laws governing the storage and processing of sensitive contact information. | This affects how meeting details, especially data related to government officials, are handled. | C2 → escalated |
| A5 | Logged meeting details will only include formal meetings and will not include confidential discussions outside of scheduled meetings with government officials. | This ensures the system adheres to data management protocols, preventing unauthorized visibility of sensitive information. | Accepted (never challenged) |

## Definitions

- **D1** "automatic logging of meetings": The process by which meetings scheduled through integrated calendar tools are captured in the CRM without requiring manual entry by users.  
  The definition of automatic logging clarifies that user input is not required due to automated processes, minimizing user error.
- **D2** "engagement history": A record of all formal interactions between the organization and government officials, specifically including meetings and their outcomes.  
  Refining the definition of engagement history to include only formal interactions aligns data management expectations with compliance needs.
- **D3** "clear criteria for automatic logging": Formal meetings held with government officials that are scheduled through integrated calendars and attended by authorized CRM users.  
  Clarifying the criteria for automatic logging ensures systematic adherence to compliance requirements for capturing relevant meetings.

## Success criteria

- **K1** percentage of meetings logged automatically: target 80% of all scheduled meetings with government officials should be logged automatically within the first quarter after implementation. (Monitor the logging functionality's performance via system metrics for the first three months post-release.)  
  The success criterion targets logging 80% of scheduled meetings, ensuring the feature's performance can be effectively measured after implementation.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What access controls will be implemented to ensure logged meeting details are only visible to authorized users?**

- Why it matters: This is crucial to protect sensitive diplomatic information and maintain confidentiality for logged meetings.
- Decision owner: Head of Data Protection
- Options: Define specific roles with access / Engage legal team for guidance

### C9 · BLOCKER · blocks the build

**What enforcement protocols will be established to ensure only authorized roles can access logged meeting data?**

- Why it matters: Defining access protocols is vital to prevent unauthorized access to sensitive information.
- Decision owner: Head of Data Protection
- Options: Develop an access control framework / Consult with IT security

### C2 · MAJOR · blocks the build

**Which specific data protection laws will govern the logging of meetings with government officials?**

- Why it matters: Identifying applicable laws is necessary to ensure compliance and avoid legal repercussions.
- Decision owner: Legal Compliance Team
- Options: GDPR / Local data protection laws

### C3 · MAJOR · blocks the build

**Is 'engagement history' strictly limited to formal meetings, or does it include other forms of communication?**

- Why it matters: Clarifying this definition affects data management practices and compliance efforts.
- Decision owner: Data Governance Team
- Options: Limit to formal meetings only / Include informal communications

### C8 · MAJOR · blocks the build

**How will compliance with data protection regulations be enforced during the logging process?**

- Why it matters: Ensuring compliance is critical to safeguarding sensitive data and preventing potential legal issues.
- Decision owner: Compliance Officer
- Options: Regular audits / Review by legal team

## Tension report

The primary point of contention was around access controls and data protection compliance, with the critic expressing significant concerns about unauthorized access to sensitive information and the necessity for clarity in legal regulations. The proposer remained focused on justifying the logging feature's potential while acknowledging the need for these controls, but unresolved issues could delay implementation.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 75 | 50 | - | continue |
| 2 | 6 | 3 | 0 | 3 | 1.00 | 75 | 40 | CONTINUE | continue |
| 3 | 8 | 2 | 3 | 3 | 0.63 | 85 | 60 | CONTINUE | continue |
| 4 | 9 | 1 | 4 | 4 | 0.55 | 70 | 40 | CONTINUE | continue |
| 5 | 9 | 0 | 4 | 5 | 0.55 | 75 | 60 | CONTINUE | converged |

- Proposer's remaining worry (75/100): Clarity on access controls for logged meetings may delay implementation if not defined in advance.
- Critic's remaining worry (60/100): The access control procedures for logged meetings are not adequately defined, risking unauthorized access to sensitive information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, D1 | R1 | ESCALATED | 0 | The proposal does not clarify how the system will handle the visibility of logged meetings, particularly regarding sensitive information about government officials. |
| C2 | MAJOR | COMPLIANCE | A4 | R1 | ESCALATED | 0 | The assumptions regarding compliance with data protection laws leave open the specific regulations applicable and how they will be enforced in the logging process. |
| C3 | MAJOR | DEFINITIONS | D2 | R1 | ESCALATED | 0 | The definition of 'engagement history' is ambiguous and may encompass various types of interactions beyond meetings, which could affect data management and compliance efforts. |
| C4 | BLOCKER | OWNERSHIP | GAP | R2 | DEFENDED | 0 | The proposal does not address who is responsible for maintaining the logged meeting data, particularly after users change roles or leave the organization. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R2 | DEFENDED | 0 | It is unclear how the system will handle situations where automated logging fails or does not accurately capture a meeting, which may allow sensitive information to be unlogged or misrepresented. |
| C6 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal lacks clarity on the criteria for determining if a meeting qualifies for automatic logging, which could lead to inconsistency in captured engagement history. |
| C7 | BLOCKER | CONFIDENTIALITY | GAP | R3 | DEFENDED | 0 | The proposal still does not clarify how logged meeting information will be managed and who can access sensitive details about government officials. |
| C8 | MAJOR | COMPLIANCE | GAP | R3 | ESCALATED | 0 | There is still no explicit mention of which data protection regulations will be adhered to in the logging process. |
| C9 | BLOCKER | CONFIDENTIALITY | GAP | R4 | ESCALATED | 0 | There is insufficient clarity on how enforcement of access controls will be implemented for logged meetings, potentially exposing sensitive data to unauthorized users. |
