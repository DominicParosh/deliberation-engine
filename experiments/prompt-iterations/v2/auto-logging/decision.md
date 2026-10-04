# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.012.

## Summary

This release will implement an automatic logging system for meetings with government officials, designed to capture and store relevant meeting details to enhance engagement history accuracy. It will not include logging meetings unrelated to government officials or complex machine learning features for summarizing meeting notes. A decision remains on defining access levels for logged meeting data, which is crucial for maintaining data confidentiality.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automatically log meeting details for engagements with government officials.  
  Automatically logging meeting details caters to the need for accurate engagement history by ensuring relevant meetings are recorded without user input.
- **V2** Provide a user interface for regional coordinators and project managers to view logged meeting histories.  
  Providing a user interface for users to view logged histories supports efficient access to engagement data after meetings have been logged automatically.

**In scope**

- **S1** Integrate the CRM with existing calendar systems (e.g., Microsoft Outlook) to capture meeting data while ensuring sensitive information is protected.  
  The integration with existing calendar systems was revised to ensure that confidentiality measures are detailed, protecting sensitive information during logging. _(C1, C7)_
- **S2** Log the following details for each meeting: date, time, attendees, agenda, and meeting notes only if the meeting is classified as an official engagement.  
  Logging specific details for official meetings ensures that only relevant information is captured, maintaining data relevance and integrity.
- **S3** Allow users to manually add or edit meeting details after automatic logging.  
  Allowing users to manually add or edit meeting details provides flexibility while ensuring automatic logs capture essential information.
- **S4** Enable notifications to users when a meeting is logged.  
  Enabling notifications for logged meetings ensures users remain informed about their engagement history in real-time.
- **S5** Provide reporting functionality that allows users to filter logged meetings by date and government official.  
  Reporting functionality allows users to filter meetings, supporting better management and oversight of engagement practices.
- **S6** Specify access levels for regional coordinators and project managers to logged meeting data, ensuring that sensitive information is kept secure according to user roles.  
  Defining access levels for logged data ensures that sensitive information is not improperly accessed, crucial for protecting diplomatic communications. _(C5)_
- **S7** Implement a protocol for managing and transitioning responsibility for logged meeting histories when project managers change roles or leave the organization to maintain data integrity and continuity.  
  Establishing protocols for managing meeting histories during personnel changes maintains continuity and prevents loss of important engagement context.

## What it will not do

**Out of scope for this release**

- **X1** This release will not log meetings that are not associated with government officials.  
  Out of scope items detail the boundaries for what is not included in this release, helping to focus on key project goals.
- **X2** No integration with non-calendar platforms or third-party applications beyond the supported calendar systems.  
  Integration with non-calendar platforms is excluded to limit project complexity and resources.
- **X3** Complex machine learning features for automatically summarizing meeting notes are out of scope for this release.  
  Complex machine learning features were dropped to prioritize essential functionalities and reduce risks during implementation.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users will have access to calendar systems that can be integrated with the CRM for automatic logging. | (implicit because: The request assumes that meeting dates and attendees can be fetched from a connected calendar.) | Accepted (never challenged) |
| A2 | Users understand the importance of maintaining accurate engagement history records. | (implicit because: The request implies that users currently struggle with tracking engagement history.) | Accepted (never challenged) |
| A3 | The system’s database can handle additional entries without performance issues due to the automatic logging. | (implicit because: Assumes that the logging of additional meeting records will not overwhelm the existing system.) | Accepted (never challenged) |
| A4 | Organizations have established guidelines on what constitutes an 'official engagement'. | (implicit because: The request implies there are criteria in place to differentiate official engagements from informal meetings.) | Accepted (never challenged) |

## Definitions

- **D1** "automatically log": The system will capture and save meeting details without user intervention, triggered by a calendar event that qualifies as an official engagement with a government official.  
  The definition of 'automatically log' ensures clarity on the system's operations and logging triggers for official meetings.
- **D2** "engagement history": A record of all meetings, including details such as date, time, attendees, agenda, and notes, with clear ownership by the respective project manager.  
  Defining 'engagement history' explicitly clarifies data ownership and management responsibilities for logged meetings over time.
- **D3** "government official": For the purposes of logging meetings, a government official is defined as a current employee or representative of a government or international organization, including designated titles such as Minister, Secretary, Attaché, or equivalent roles involved in official engagements.  
  Clarifying the criteria for a 'government official' prevents unauthorized meetings from being logged, addressing confidentiality risks.
- **D4** "official engagement": An official engagement is defined as any scheduled meeting with a government official where the agenda is formally aligned with governmental or organizational objectives.  
  Defining 'official engagement' helps ensure that the system logs only meetings that are relevant and directly aligned with organizational goals.

## Success criteria

- **K1** Number of logged meetings: target At least 80% of scheduled meetings are logged automatically within one week of implementation. (Monitor and report on the percentage of scheduled meetings logged in the system versus the total number in the connected calendar.)  
  The success criterion is focused on the quantifiable aspect of logged meetings, ensuring effectiveness of the system after implementation.

## Open questions for humans

### C5 · MAJOR · blocks the build

**What specific access levels will regional coordinators and project managers have to logged meeting data from other teams?**

- Why it matters: Establishing clear access levels is essential to avoid unauthorized disclosure of sensitive information.
- Decision owner: Head of Data Protection
- Options: Define specific access levels for logged meeting data / Implement an access matrix / Maintain current access practices

## Tension report

The primary disagreement pertained to the clarity of access levels for logged meeting data after escalation. The product owner emphasized the need for security in handling sensitive information, while the architect sought a more defined framework to prevent unauthorized access. This issue remains unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 6 | 3 | 3 | 0 | 0.50 | 70 | 60 | CONTINUE | continue |
| 3 | 8 | 5 | 3 | 0 | 0.62 | 80 | 60 | CONTINUE | continue |
| 4 | 9 | 1 | 7 | 1 | 0.22 | 75 | 70 | CONTINUE | continue |
| 5 | 9 | 0 | 8 | 1 | 0.11 | 80 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): The clarity of ownership and responsibility for logged meeting data management is paramount to prevent data loss.
- Critic's remaining worry (80/100): Without clarified access levels for logged meeting data, there remains a risk of unauthorized access to sensitive information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The integration with calendar systems does not specify what data is captured or how issues of confidentiality and diplomatic sensitivity are managed. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The term 'automatically log' is insufficiently defined; it does not specify how it will determine which meetings to log based on the context of the engagement. |
| C3 | MAJOR | OWNERSHIP | D2 | R1 | REVISED | 0 | The ownership of the logged meeting data is not addressed; specifically, who is responsible for maintaining and managing this information over time. |
| C4 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 1 | The proposal does not specify who qualifies as a government official for logging purposes, raising the risk of inadvertent logging of non-official meetings. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R2 | ESCALATED | 2 | There is no definition of what access levels regional coordinators and project managers have to logged meeting data from other teams, which can lead to unauthorized disclosure of sensitive information. |
| C6 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 1 | No clear protocols are established for handling logged meeting histories when project managers change roles or leave the organization, risking data mismanagement. |
| C7 | MAJOR | CONFIDENTIALITY | S1 | R3 | REVISED | 0 | The proposal does not explain how sensitive diplomatic or confidential information will be managed during the logging process, potentially exposing sensitive data. |
| C8 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The term 'official engagement' is not defined, leaving ambiguity about what qualifies as an official meeting worthy of logging. |
| C9 | MAJOR | OWNERSHIP | GAP | R4 | REVISED | 0 | There is still no clear explanation of who will be responsible for maintaining the logged meeting data over time, especially after project managers change roles. |
