# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 4 rounds (policy `gated`) · $0.012.

## Summary

This release will automate the logging of meetings with government officials for regional coordinators and project managers within the Government CRM, ensuring secure access and compliance with data protection laws. Meeting details will be captured and stored for at least five years, with specific measures in place for data handling when users change roles or leave. However, questions remain about the specifics of compliance measures and access control which need resolution before proceeding.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide an automated logging feature for meetings between users and government officials.  
  The commitment to provide an automated logging feature was agreed upon as essential for improving engagement history.
- **V2** Ensure secure storage and access to engagement history that is in compliance with applicable data protection laws.  
  The assurance of secure storage and compliance with data protection laws was established to protect sensitive information.

**In scope**

- **S1** Enable automatic logging of meetings for designated roles: regional coordinators and project managers.  
  The scope includes automatic logging for designated roles to streamline user engagement with government officials.
- **S2** Log meetings when a user schedules them in the CRM calendar with the associated government official's contact.  
  In-scope logging will occur when a user schedules meetings in the CRM calendar to ensure comprehensive tracking.
- **S3** Capture details of each meeting including date, time, participants, agenda, and key outcomes as part of engagement history.  
  Essential details for meetings were defined to ensure complete engagement history and prevent issues with missing data. _(C3)_
- **S4** Provide a user interface for users with the role of regional coordinators and project managers to view logged meetings in their engagement history, while ensuring that each user can only access their own logs and those of their direct team members.  
  The user interface will be restricted to regional coordinators and project managers, ensuring confidentiality of engagement histories. _(C1)_
- **S5** Ensure that the logging feature retains data for a minimum of five years, complying with government record retention policies and applicable data protection laws, specifically GDPR and national data protection regulations.  
  Retention for five years complies with data protection laws, addressing concerns about longevity and governance of sensitive data. _(C5)_
- **S6** When a user leaves the organization, their logged meetings will be archived and access will be removed immediately. If a user changes roles, access to their logged meetings will be revoked, and the meetings will be reassigned to the new direct manager.  
  Guidelines for managing logged meetings when users transition roles or leave were clarified, preventing unauthorized access post-transition. _(C2, C7)_
- **S7** Compliance measures for the logged meeting data will include encryption during storage and transmission, access controls limited to authorized users based on their role, specifically the roles of regional coordinators and project managers, and routine audits of access logs to ensure adherence to data protection standards.  
  Specific compliance measures were established to ensure that sensitive data is handled correctly, with roles defined to restrict access appropriately. _(C8)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include notifications or alerts for users when meetings are logged.
- **X2** Integration with external calendar applications (e.g., Google Calendar, Outlook) is not included in this release.
- **X3** The release will not provide support for logging meetings retroactively.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have the necessary permissions to log meetings; this affects who can utilize the feature. | Kept | never challenged |
| A2 | The CRM can access the contact details of government officials to associate them with logged meetings. | Kept | never challenged |
| A3 | Compliance measures for sensitive data storage and handling are in place according to existing organizational data protection policies. | Kept | C6 → escalated |
| A4 | The users are familiar with using the CRM calendar functionality to schedule meetings. | Kept | never challenged |

## Definitions

- **D1** "automatic logging" means the system will record meeting information without requiring manual input from users at the time of scheduling.  
  The definition of 'automatic logging' clarifies that it involves system-generated records, removing ambiguity from the proposal.
- **D2** "engagement history" means the compiled record of interactions (meetings, communications) with government officials, stored within the CRM.  
  Defining 'engagement history' ensures that users understand what is being tracked within the CRM.

## Success criteria

- **K1** At least 90% of scheduled meetings with government officials are logged correctly within the system, as determined by reviewing entries for completeness and accuracy, measured through user feedback within the first three months post-release.  
  Success criteria regarding the correctness of logged meetings were clarified to ensure users can rely on accurate tracking of engagements. _(C4)_

## Open questions for humans

### C2 · MAJOR · blocks the build

**What specific measures will be taken to manage logged meetings when users transition roles or leave?**

- Why it matters: Clarifying these measures is critical to prevent unauthorized access to sensitive data after personnel changes.
- Decision owner: Head of Data Protection
- Options: Establish role-based access updates upon transition / Archive data upon user departure and revoke access / Retain data with changed access rights

### C8 · MAJOR · blocks the build

**Which user roles will be classified as 'authorized users' for accessing logged meetings?**

- Why it matters: Defining authorized roles is vital for maintaining security and preventing unauthorized access to sensitive information.
- Decision owner: Head of Data Protection
- Options: Include only defined roles like coordinators and project managers / Allow broader access to additional roles / Identify roles based on project requirements

### C6 · MINOR · blocks the build

**What specific compliance measures are ensured to protect sensitive meeting data during automatic logging?**

- Why it matters: Detailing compliance measures is essential to safeguard against potential data breaches and legal risks.
- Decision owner: Head of Data Protection
- Options: Implement role-based encryption / Regular audits of access logs / Training for users on data handling

## Tension report

The main disagreement revolved around the clarity of compliance measures and access control for sensitive data. While the proposer aimed for robust solutions to address these areas, the critic remained concerned about potential points of failure regarding unauthorized access and data protection, leading to several unresolved issues requiring further decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.50 | 80 | 70 | CONTINUE | continue |
| 3 | 8 | 1 | 5 | 2 | 0.36 | 75 | 75 | CONTINUE | continue |
| 4 | 8 | 0 | 5 | 3 | 0.36 | 85 | 75 | CONTINUE | converged |

- Proposer's remaining worry (85/100): There may still be aspects of data access and handling that require further clarification.
- Critic's remaining worry (75/100): The failure to clearly define authorized users may lead to improper access control and potential data leaks.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S4 | R1 | REVISED | 0 | The proposal does not clarify who can see the logged engagement history across different user roles. This lack of clarity risks unauthorized access to sensitive meeting information. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | ESCALATED | 0 | The proposal lacks details about maintaining the logged data when a user changes roles or leaves, which could lead to confusion and improper access to sensitive information post-transition. |
| C3 | MAJOR | DEFINITIONS | S3 | R1 | REVISED | 0 | The term 'automatic logging' is undefined and unbounded, risking potential issues with how meetings are captured and what essential details might be missed. |
| C4 | MINOR | DATA_QUALITY | K1 | R1 | REVISED | 0 | The success criteria based on '90% of scheduled meetings logged correctly' lacks clarity on how 'correctly' is measured and what constitutes a failure. |
| C5 | MINOR | COMPLIANCE | S5 | R1 | REVISED | 0 | The minimum retention period of five years does not specify compliance with specific data protection laws or policies governing sensitive data. |
| C6 | MINOR | FEASIBILITY | A3 | R1 | ESCALATED | 0 | The assumptions state that compliance measures for sensitive data are in place, but there are no specifics provided regarding for what conditions these measures apply. |
| C7 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal still lacks details on how logged meetings will be maintained when users change roles or leave, which can lead to unauthorized access. |
| C8 | MAJOR | COMPLIANCE | GAP | R2 | ESCALATED | 2 | There is still no clarity on what specific compliance measures are in place to ensure data protection for logged meetings, which creates risk. |
