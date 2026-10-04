# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **cap** after 8 rounds (policy `naive`) · $0.024.

Challenges: 21 raised · 14 settled between the agents · 4 handed to humans · 3 still open when it ended.

## Summary

The release will enable project managers to access a detailed engagement history for each country before starting new missions, which includes timestamps, record notes, and outcomes. However, key issues related to retention policies and data destruction timelines remain unresolved and require further clarification. Decision-makers will need to address compliance and confidentiality aspects to ensure the information is properly managed and protected.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can view a detailed engagement history for each country.  
  Project managers can now view a detailed engagement history for each country, ensuring they have necessary information for new missions.
- **V2** The engagement history includes timestamps, record notes, and outcomes.  
  The engagement history will include timestamps, record notes, and outcomes, providing comprehensive insights into previous interactions.

**In scope**

- **S1** Project managers will have access to a dedicated 'Engagement History' section in the CRM.  
  Project managers will have access to a dedicated 'Engagement History' section in the CRM, facilitating ease of use.
- **S2** Engagement history means all recorded interactions with government counterparts, including meetings, communications, and notes.  
  The definition of engagement history has been clarified to include all recorded interactions, ensuring project managers have complete information. _(C5)_
- **S3** The system will display engagement history for all countries with which there is a past record in the CRM.  
  The system will display engagement history for all countries with past records, allowing project managers to access necessary data.
- **S4** Users can filter the engagement history by date range and type of interaction.  
  Users can filter the engagement history by date range and type of interaction, enabling targeted searches for relevant information.
- **S5** Upon a project manager's transition out of their role, their access to sensitive engagement records will be revoked immediately by the system administrator responsible for managing user access, in compliance with the organization's security policy.  
  Access to sensitive records will be revoked immediately when a project manager transitions out of their role, ensuring compliance with security policies. _(C2, C19)_
- **S6** The system will maintain an audit trail of all changes made to engagement history records, documenting the user who made the change, the timestamp of the modification, and the specifics of what was changed. This audit trail will undergo quarterly reviews by designated compliance officers to ensure adherence to data governance standards.  
  An audit trail of changes to engagement history will be maintained, enhancing accountability and compliance with governance standards. _(C12, C18)_
- **S7** The system will implement a data validation process to ensure the accuracy and freshness of engagement history records, conducted by designated personnel who have a minimum of 3 years of experience in data quality management and governance, with relevant certifications in data protection and management best practices. This validation process will occur bi-annually.  
  A bi-annual data validation process will be implemented to maintain accuracy, specifying required qualifications for personnel involved. _(C13, C16)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not implement any changes to user roles or security clearances outside of current definitions.  
  The release will not implement changes to user roles or security clearances outside current definitions to maintain control.
- **X2** The release will not provide access to engagement records of countries that are not involved in any active missions.  
  This release will not provide access to records from non-active missions, focusing only on relevant historical data.
- **X3** This release will not include any real-time updates from ongoing engagements; it will only display historical data.  
  Real-time updates from ongoing engagements are out of scope, as this feature will only display historical data.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Project managers are users of the CRM with the necessary permissions to access engagement histories. | Kept | never challenged |
| A2 | Engagement records are currently stored in a structured way that allows for filtering and retrieval. | Kept | never challenged |
| A3 | There are existing records of past engagements with each country that can be extracted for display. | Kept | never challenged |
| A4 | The organization has policies in place to uphold data protection and privacy regarding sensitive contacts. | Kept | never challenged |

## Definitions

- **D1** 'Engagement history' means the chronological record of all interactions, communications, and engagements with a government contact or agency, including meeting dates, notes, and outcomes. Sensitive records within this engagement history will be flagged using classification labels clearly visible in the interface, with corresponding access requirements outlined next to each record. Unauthorized access attempts will trigger notifications to security personnel.  
  The definition of engagement history now clearly states what types of records are included and how sensitive data will be flagged. _(C1, C10)_

## Success criteria

- **K1** At least 80% of project managers report they can easily access and utilize the engagement history feature based on a post-deployment survey.  
  Success criteria set to ensure at least 80% satisfaction from project managers regarding the accessibility of the new feature.

## Open questions for humans

### C9 · BLOCKER · blocks the build

**What is the defined data retention policy for engagement histories?**

- Why it matters: A defined retention policy is crucial to ensure compliance and mitigate potential legal risks associated with data mishandling.
- Decision owner: Legal and Compliance Departments
- Options: Set a specific time frame for data retention / Develop procedures for data destruction

### C14 · BLOCKER · blocks the build

**What is the defined policy for the retention and deletion of engagement history records?**

- Why it matters: Clarifying retention and deletion policies is essential for compliance with legal standards and organizational data governance.
- Decision owner: Compliance Manager
- Options: Establish a clear policy for retention periods / Specify destruction timelines for after retention period

### C17 · BLOCKER · blocks the build

**What is the timeline and process for destroying engagement history records after the retention period ends?**

- Why it matters: Having a clear timeline is crucial to ensure compliance and prevent unauthorized retention of sensitive data.
- Decision owner: Data Compliance Officer
- Options: Define a destruction process with deadlines / Align destruction timeline with legal requirements

### C20 · BLOCKER · blocks the build

**What security measures are implemented to ensure sensitive data is protected immediately after a project manager transitions out of their role?**

- Why it matters: Immediate protection of sensitive data is essential to prevent unauthorized access and potential breaches.
- Decision owner: Security Policy Lead
- Options: Define immediate access revocation procedures / Establish temporary restrictions on sensitive records

### C4 · MAJOR · blocks the build

**What is the established retention policy for engagement records, especially sensitive ones?**

- Why it matters: Determining a retention policy is essential to manage legal compliance and proper handling of sensitive data over time.
- Decision owner: Head of Compliance
- Options: Define a retention schedule based on legal requirements / Align with applicable laws and organizational policies

### C16 · MAJOR · blocks the build

**What qualifications or expertise are required for the personnel conducting data validation?**

- Why it matters: Clearly defining the expertise needed for personnel is essential to maintain the reliability of engagement history data.
- Decision owner: Head of Data Management
- Options: Set minimum experience and certifications / Define a training program for personnel

### C21 · MAJOR · blocks the build

**What processes will be employed to flag sensitive records within the engagement history?**

- Why it matters: Implementing effective flagging processes is critical to ensure sensitive data is managed properly and to mitigate the risk of accidental disclosure.
- Decision owner: Compliance and Security Teams
- Options: Create detailed flagging procedures / Develop training materials for staff on flagging sensitive data

## Tension report

The main disagreement centered around the necessity and clarity of the data retention policy, with the proposer advocating for its importance in compliance and the critic emphasizing potential legal risks. Although some aspects were resolved, challenges relating to data retention and destruction timelines remain unresolved and require further authority decisions.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 50 | - | continue |
| 2 | 6 | 0 | 5 | 1 | 0.15 | 80 | 70 | CONTINUE | continue |
| 3 | 9 | 3 | 5 | 1 | 0.45 | 80 | 45 | CONTINUE | continue |
| 4 | 13 | 4 | 7 | 2 | 0.46 | 75 | 60 | CONTINUE | continue |
| 5 | 14 | 3 | 9 | 2 | 0.39 | 80 | 40 | CONTINUE | continue |
| 6 | 16 | 4 | 9 | 3 | 0.47 | 80 | 55 | CONTINUE | continue |
| 7 | 19 | 4 | 12 | 3 | 0.40 | 80 | 70 | CONTINUE | continue |
| 8 | 21 | 3 | 14 | 4 | 0.38 | 85 | 70 | CONTINUE | cap |

- Proposer's remaining worry (85/100): The clarity and implementation of the retention policy remain unresolved and could pose compliance risks.
- Critic's remaining worry (70/100): Lack of a defined retention policy and timeline for data destruction poses a significant legal risk.
- ⚠ Proposer reported 85/100 confidence while blocker(s) C9, C14, C17, C20 remain unsettled.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | D1 | R1 | REVISED | 0 | The definition of 'engagement history' does not clarify which specific records are classified as sensitive, potentially leading to unauthorized access to diplomatic communications. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal doesn't specify what happens to engagement history records when project managers leave the organization or change roles, risking data integrity and access issues. |
| C3 | MAJOR | CONFIDENTIALITY | X1 | R1 | REVISED | 0 | The proposal does not define how project managers' clearance will be managed, risking access to sensitive information by unauthorized users. |
| C4 | MAJOR | COMPLIANCE | GAP | R1 | ESCALATED | 0 | No retention policy for engagement records is indicated, raising concerns about legal compliance and proper handling of sensitive data over time. |
| C5 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The proposal does not specify what constitutes 'all recorded interactions,' leaving it open to interpretation and data inconsistency. |
| C6 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | There is no mention of how sensitive data within engagement history will be flagged or restricted, heightening risk of accidental disclosure. |
| C7 | MAJOR | OWNERSHIP | GAP | R3 | REVISED | 0 | The proposal does not define how access to records will be managed when project managers leave the organization or change roles, which could allow unauthorized users access to sensitive information. |
| C8 | MAJOR | OWNERSHIP | X1 | R3 | REVISED | 0 | The proposal does not specify how the security clearance of users will be maintained over time, risking access to sensitive information by unauthorized individuals after role changes. |
| C9 | BLOCKER | COMPLIANCE | GAP | R3 | ESCALATED | 0 | The absence of a data retention policy for engagement records creates a legal risk and fails to ensure proper handling of sensitive data over time. |
| C10 | MAJOR | CONFIDENTIALITY | GAP | R4 | REVISED | 2 | The proposal does not specifically outline how sensitive engagement records will be flagged or managed, which could lead to unauthorized access to confidential communications. |
| C11 | MAJOR | DEFINITIONS | GAP | R4 | REVISED | 0 | The definition of 'engagement history' lacks clarity on how interactions are categorized and what specific criteria are used for 'all recorded interactions'. |
| C12 | MAJOR | COMPLIANCE | GAP | R4 | REVISED | 0 | There is no detailed process for audit trails or accountability for changes in the engagement history records, risking non-compliance with data governance standards. |
| C13 | MAJOR | DATA_QUALITY | GAP | R4 | REVISED | 2 | The proposal does not address how data accuracy and quality will be maintained in the engagement history records, risking the reliability of information presented to users. |
| C14 | BLOCKER | COMPLIANCE | GAP | R5 | ESCALATED | 0 | The absence of a data retention policy for engagement records is a serious issue that poses legal risks. |
| C15 | BLOCKER | CONFIDENTIALITY | GAP | R6 | REVISED | 0 | The proposal does not specify the methods for flagging sensitive engagement records, which could lead to unauthorized access to confidential communications. |
| C16 | MAJOR | DATA_QUALITY | GAP | R6 | UNRESOLVED | 2 | The proposal lacks clarity on the roles and expertise of the designated personnel responsible for data validation, risking the reliability of engagement history data. |
| C17 | BLOCKER | COMPLIANCE | GAP | R7 | ESCALATED | 0 | The proposal still lacks a retention policy for engagement records, creating potential legal risks. |
| C18 | MAJOR | DATA_QUALITY | GAP | R7 | REVISED | 0 | The audit process for engagement history records is ambiguous, risking non-compliance with data governance standards. |
| C19 | MAJOR | OWNERSHIP | GAP | R7 | REVISED | 0 | The proposal does not clarify the process to follow when project managers leave or change their roles concerning access to engagement history. |
| C20 | BLOCKER | COMPLIANCE | GAP | R8 | UNRESOLVED | 0 | The proposal lacks a clearly defined timeline for data destruction following the defined data retention policy, risking compliance breaches. |
| C21 | MAJOR | CONFIDENTIALITY | GAP | R8 | UNRESOLVED | 0 | The proposal does not specify what measures will be taken to protect sensitive data in the engagement history after a project manager leaves their role, leading to potential unauthorized access. |
