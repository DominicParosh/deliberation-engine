# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **consensus** after 4 rounds (policy `naive`) · $0.009.

Challenges: 7 raised · 6 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will introduce an automatic logging feature for meetings with government officials, ensuring that engagement history is consistently recorded. Users will receive notifications when meetings are logged. Organizations must still determine the best practices for verifying the accuracy of logged meeting details, as this remains an open question.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automatically log meetings with government officials in the CRM system.  
  This feature will automatically log meetings without requiring user intervention, ensuring accurate engagement history recording.
- **V2** Provide notifications to the relevant users when meetings are logged.  
  Notifications will be sent to relevant users to enhance transparency regarding logged meetings and their details.

**In scope**

- **S1** Enable the automatic logging of meetings with government officials that are scheduled through the CRM's calendar feature.  
  This scope item allows for meetings scheduled through the CRM's calendar to be logged automatically, streamlining the process effectively.
- **S2** Notify users via email when a meeting is logged into the CRM, including details such as date, time, participants, and key discussion points.  
  Email notifications are essential for ensuring users are aware of newly logged meetings and can access the relevant details.
- **S3** Allow users to manually edit the automatically logged meeting entries if needed.  
  Allowing users to manually edit entries ensures accuracy and accountability in the logged information.
- **S4** Provide access to these logged meetings for regional coordinators and project managers.  
  Providing access to logged meetings for regional coordinators and project managers enhances security around sensitive information.
- **S5** Establish role-based access controls where access to logged meetings is restricted to users with the roles of regional coordinators and project managers; other roles cannot view or edit these logs.  
  This scope item establishes necessary role-based access, ensuring that only authorized personnel can view and edit logged meetings. _(C1)_
- **S6** Retain logged meetings within the individual user's profile, but set access restrictions so if a user changes roles, their access to these logs is limited to their new role; if they leave the organization, access is removed completely.  
  It ensures that access to logged meetings is managed according to user roles, preserving confidentiality when personnel change. _(C3)_
- **S7** Implement a verification process for automatically logged meetings requiring users to review meeting details and confirm their accuracy within 24 hours of logging; if no confirmation is received, automatically flag the entry for review by a regional coordinator or project manager.  
  This introduces a crucial verification step that requires user involvement to guarantee the accuracy of logged meetings. _(C4, C7)_

## What it will not do

**Out of scope for this release**

- **X1** Manual logging of meetings; this feature will focus solely on automation.  
  Manual logging is out of scope because the focus is on automating the logging process to prevent loss of engagement history.
- **X2** Integration with external calendar systems other than the CRM's internal calendar.  
  Integration with external systems is excluded as it would complicate the implementation of the automated logging feature.
- **X3** Tracking of informal or non-scheduled conversations with government officials.  
  Informal conversations are out of scope, as the focus is on systematically logging scheduled meetings for clarity and accuracy.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have access to the CRM and use its calendar feature to schedule meetings, as the logging relies on this functionality. | Kept | never challenged |
| A2 | The CRM has the capability to send email notifications to users based on meeting entries. | Kept | never challenged |
| A3 | Users trust the automatic logging feature and will accurately represent their meetings in any necessary follow-up actions. | Kept | never challenged |

## Definitions

- **D1** "Automatically log meetings" means the system will create an entry in the CRM without user intervention when a meeting concludes, capturing relevant information from the calendar.  
  This definition clarifies that automatic logging occurs without user intervention, ensuring a systematic record is maintained.
- **D2** "Engagement history" means the record of interactions, including date, time, participants, and any discussed topics related to meetings with government officials.  
  Defining engagement history ensures clarity about what constitutes recorded interactions with government officials.
- **D3** "Logged meeting entries" means the automatically created records will include the date, time, participants, and key discussion points; confidential information must be marked and encrypted to restrict access.  
  This outlines the specific content included in logged meetings to prevent confusion regarding data management. _(C2)_
- **D4** "Eligible meetings for automatic logging" means any meeting with government officials that is scheduled using the CRM calendar feature; ad-hoc meetings without prior scheduling are not included.  
  This definition clarifies eligibility for meetings to be logged automatically, excluding ad-hoc meetings for consistency. _(C5)_
- **D5** "Safeguards against inaccurate logging" means the system will implement confirmation of attendance through pre-meeting notifications where participants must acknowledge their attendance.  
  This establishes necessary safeguards for participant verification to prevent inaccuracies in logged meetings. _(C6)_

## Success criteria

- **K1** At least 80% of scheduled meetings with government officials are logged automatically within 10 minutes of the meeting's conclusion, measured by monitoring system logs.  
  This success criterion sets a measurable goal for the automatic logging efficiency, aligning with operational expectations.
- **K2** User satisfaction regarding meeting logging increases by at least 20% in a survey conducted three months after the feature release.  
  User satisfaction measurement is essential to ensure that the new feature meets user needs and expectations after implementation.

## Open questions for humans

### C4 · MINOR · does not block the build

**What specific measures will be implemented to verify the accuracy of logged meeting details after the automated logging process?**

- Why it matters: Accurate logged details are critical for maintaining effective relationships with government officials and ensuring reliable follow-up actions.
- Decision owner: Head of Operations
- Options: Implement mandatory user confirmations for log accuracy / Establish a random review process for logged meetings / Create user guidelines for log accuracy
- Proposer's last word (R2, defend, needs human decision): Ensuring the accuracy of logged meeting details may require user involvement or validation processes that are best determined by organizational policy, thus can't be mandated here.
- Critic's last word (R2, escalate): Without defined measures for verifying accuracy, potential inaccuracies might lead to poor decision-making.

## Tension report

The primary disagreement centered around the verification of logged meeting details, with the critic emphasizing the potential risks of inaccuracies if user compliance is lacking. Although the proposer acknowledged the importance of this issue, they believed that the outlined verification process would be sufficient to address concerns.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 7 | 1 | 5 | 1 | 0.25 | 85 | 70 | CONTINUE | continue |
| 3 | 7 | 0 | 6 | 1 | 0.08 | 85 | 80 | CONTINUE | continue |
| 4 | 7 | 0 | 6 | 1 | 0.08 | 80 | 95 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring users comply with the verification process for logged meetings.
- Critic's remaining worry (95/100): The proposal relies heavily on user confirmation and role-based access, which could still be bypassed or mismanaged.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | How are permission levels structured to ensure only authorized users can view and edit logged meetings? |
| C2 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | What data from the meetings is included in the automatically logged entries and how is sensitive information handled? |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | What happens if a user's role changes or they leave the organization; who retains access to their logged meetings? |
| C4 | MINOR | DATA_QUALITY | GAP | R1 | ESCALATED | 0 | What measures are in place to verify the accuracy of logged meeting details? |
| C5 | MINOR | DEFINITIONS | GAP | R1 | REVISED | 0 | How will a logged meeting be defined in terms of its necessity for automatic logging (e.g., must it be scheduled via the CRM, or can ad-hoc meetings be logged)? |
| C6 | MINOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | What are the safeguards against the system inaccurately logging meetings or including users not present during the meetings? |
| C7 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | What specific measures will be established to ensure the accuracy of logged meeting details since relying on organizational policy can lead to inconsistencies? |
