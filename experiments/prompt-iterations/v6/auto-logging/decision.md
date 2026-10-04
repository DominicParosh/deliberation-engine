# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.007.

## Summary

The feature will implement automated logging of meeting details to maintain engagement history, ensuring that only relevant meetings are logged through clear guidelines and access measures. It will not include integration with calendar apps or provide analytics on engagement history. A decision is needed on the criteria for logging meetings to ensure accuracy and relevance.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automate the logging of meeting details, including date, time, participants, and notes.  
  Automating the logging of meeting details addresses the need for a reliable record of engagements with government officials.
- **V2** Ensure that all logged meetings are easily accessible and searchable by authorized users.  
  Enabling easy access and search functionality for logged meetings enhances the usability of the engagement history.

**In scope**

- **S1** Automatically log meeting details such as the date, time, attendees (both internal and external), and a summary of the discussion, triggered only by meetings that involve direct engagement with government officials, subject to predefined criteria established by an oversight committee, with an auditing mechanism implemented to track access and changes to logged meetings.  
  The item specifies that only meetings with direct engagement involving government officials will be logged, addressing concerns over irrelevant logs. _(C4, C7)_
- **S2** Implement a feature for regional coordinators and project managers to edit or add notes to logged meetings.  
  Allowing editing or adding notes by regional coordinators and project managers supports the accuracy of logged meetings.
- **S3** Provide a search function to filter logged meetings by date, participant, or keywords in the notes.  
  Providing a search function for logged meetings improves the efficiency of retrieving engagement history.
- **S4** Set access permissions so that only regional coordinators and project managers can view and edit meeting logs, with automated alerts sent to administrators for any unauthorized access attempts.  
  Setting access permissions with alerts for unauthorized access maintains the confidentiality and security of sensitive information. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external calendar applications for automatic meeting logging.  
  Integration with external calendar applications was deemed unnecessary for the initial implementation of automated logging.
- **X2** This release will not provide analytics or reporting features on engagement history.  
  Analytics on engagement history was excluded to focus on the core feature of automated logging.
- **X3** This release will not cover meetings that lack proper authorization or have confidentiality concerns unless identified and approved by a designated oversight committee responsible for authorization.  
  Meetings lacking proper authorization or confidentiality concerns will not be logged unless identified by an oversight committee, ensuring appropriate handling of sensitive data. _(C2)_

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | The system will have access to a complete list of meetings scheduled with government officials, which depends on the proper entry of data by users. | Kept | never challenged |
| A2 | All users logging meetings will have the necessary training and understanding of how to report sensitive information securely. | Kept | never challenged |
| A3 | Relevant stakeholders will prioritize and approve the automatic logging feature, assuming they recognize the importance of maintaining engagement history. | Kept | never challenged |

## Definitions

- **D1** 'automatically log' means to record meeting details in the database without manual entry, triggered by a meeting initiation.  
  'Automatically log' requires triggering by the initiation of meetings, clarifying how data will be recorded.
- **D2** 'engagement history' means a chronological record of interactions with government officials, including but not limited to meetings, calls, and correspondence, with documented ownership and transfer protocols for all logged interactions.  
  Defining 'engagement history' ensures that all logged interactions are accounted for effectively, especially during role changes. _(C3)_
- **D3** 'confidential meetings' means meetings that involve sensitive topics such as diplomatic discussions, classified information, or discussions under non-disclosure agreements, which require prior approval from the oversight committee to be logged.  
  Specifying 'confidential meetings' prevents the logging of sensitive discussions without oversight approval. _(C5)_

## Success criteria

- **K1** By the end of the quarter, the automated logging feature should log at least 90% of scheduled meetings with government officials, as determined by comparing meeting entries to calendar data.  
  The success criterion of logging 90% of scheduled meetings emphasizes the goal for effective automatic logging.

## Open questions for humans

### C4 · MAJOR · blocks the build

**What specific guidelines will be implemented to ensure only relevant meetings are logged automatically?**

- Why it matters: Clarifying this will prevent irrelevant meetings from cluttering engagement history.
- Decision owner: Oversight Committee Lead
- Options: Develop comprehensive criteria for logging / Trust project managers' discretion / Exclude ambiguous meetings from logging

### C7 · MAJOR · blocks the build

**What particular criteria should the oversight committee establish to define relevant meetings for automatic logging?**

- Why it matters: Ensuring clarity on these criteria is essential to avoid unnecessary logging of unrelated meetings.
- Decision owner: Oversight Committee Lead
- Options: Set specific definitions of relevant engagements / Implement user feedback on logged meetings / Review logged data regularly for relevance

## Tension report

The significant disagreement centered around the criteria for logging meetings, with the Proposer concerned about the success of the automated logging mechanism relying on clear definitions, while the Critic emphasized the risks of undefined committee criteria potentially leading to irrelevant meetings being captured. While some concerns were resolved, the issue of clarity and specifics remains contentious.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 80 | 40 | - | continue |
| 2 | 7 | 2 | 5 | 0 | 0.25 | 75 | 75 | CONTINUE | continue |
| 3 | 7 | 0 | 5 | 2 | 0.25 | 75 | 40 | CONTINUE | converged |

- Proposer's remaining worry (75/100): The success of this automated logging mechanism will heavily depend on the clear definition of 'direct engagement' and the criteria set by the oversight committee.
- Critic's remaining worry (40/100): The reliance on undefined criteria by an oversight committee leaves room for logging irrelevant meetings.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | S4 commits to setting access permissions for regional coordinators and project managers, but fails to specify how unauthorized access will be prevented or monitored. |
| C2 | MAJOR | OWNERSHIP | X3 | R1 | REVISED | 0 | X3 states that meetings lacking proper authorization or confidentiality concerns are out of scope, yet does not define how these criteria will be identified or who decides this. |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | There is no clarity on the ownership and maintenance responsibilities of logged meeting data after personnel changes. |
| C4 | MAJOR | OPERATIONS | GAP | R1 | ESCALATED | 1 | The proposal does not address management of false positives in logging, risking irrelevant meetings being recorded, which could confuse users. |
| C5 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not specify the criteria for determining whether a meeting is confidential and should not be logged. |
| C6 | BLOCKER | COMPLIANCE | GAP | R1 | REVISED | 0 | There is no mention of an auditing mechanism to ensure compliance with data protection regulations regarding logged meeting data. |
| C7 | MAJOR | OPERATIONS | GAP | R2 | ESCALATED | 0 | The proposal does not specify clear guidelines to ensure that only relevant meetings are logged automatically, risking irrelevant meetings being recorded. |
