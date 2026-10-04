# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 5 rounds (policy `naive`) · $0.018.

Challenges: 16 raised · 10 settled between the agents · 5 handed to humans · 1 still open when it ended.

## Summary

Project managers will gain access to a detailed engagement history for each country, enhancing mission preparation. However, records marked as confidential will remain inaccessible, and no analytics on engagement effectiveness will be provided. Key organizational decisions are still needed regarding the oversight of clearance monitoring protocols.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers will have access to a detailed engagement history for each country.  
  Project managers will have access to a detailed engagement history for each country, ensuring they are better equipped for new missions.

**In scope**

- **S1** The system will display the engagement history, which includes all recorded contact interactions, project affiliations, and mission details for each country in a user-friendly format, with a monthly review to ensure data accuracy by the Data Management Team.  
  The system will display engagement history, reviewed monthly for accuracy, which supports data integrity and management oversight. _(C6)_
- **S2** The engagement history access permissions will be managed by the Data Governance Team, which will conduct quarterly audits of user access rights, logging all access attempts and authorization changes to ensure only authorized users can access sensitive records.  
  Access permissions will be managed by the Data Governance Team with quarterly audits to prevent unauthorized access, addressing accountability. _(C2)_
- **S3** The engagement history will include data from the last five years, or all available data if fewer than five years exist, with a process established for retrieving older engagement records based on project relevance determined by the Data Governance Team.  
  Engagement history will include data from the last five years or all available data, allowing for a clear understanding of historical context in missions. _(C4)_
- **S4** The system will implement security features that prevent any references to confidential records from being displayed in search results or engagement history views, ensuring no inadvertent exposure occurs.  
  The system will actively prevent the display of confidential records, which helps to protect sensitive information from inadvertent exposure. _(C13)_
- **S5** The system will implement a procedure for notifying project managers of any changes to engagement history data, including updates in contact information and project statuses, ensuring that the data is current and accurate between the monthly reviews.  
  Project managers will be notified of any changes in engagement data, ensuring that they have access to the most current information available. _(C8)_

## What it will not do

**Out of scope for this release**

- **X1** The release will not include any data from countries or engagements that have been marked as confidential or diplomatic under existing data protection policies.
- **X2** The system will not provide analytics or insights regarding engagement effectiveness; it will only display raw engagement history.
- **X3** The system will maintain retention policies for confidential engagement records and implement audit trails that log the retention of any confidential data, ensuring accountability in data management practices.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that engagement data is being collected and stored accurately in the CRM system, as the display of this data relies on its existence. | Kept | never challenged |
| A2 | It is assumed that project managers have the appropriate clearance and permissions to access the engagement history, in line with organizational data protection policies. | Kept | C5 → escalated; C7 → escalated; C9 → escalated; C12 → escalated |
| A3 | It is assumed that the existing database structure can support extended historical data display without performance issues, which is necessary for the UI implementation. | Kept | never challenged |

## Definitions

- **D1** 'Engagement history' means the record of all interactions, communications, projects, and missions involving a country, stored in the CRM and retrievable by project managers.  
  'Engagement history' is defined to include all interactions and communications related to a country, making it clear what project managers can access.
- **D2** 'Confidential record' means any engagement history record that meets the following specific criteria: (1) it contains sensitive diplomatic information as defined by the organization's data protection policies, (2) it has been explicitly marked as confidential by authorized personnel in writing with documented approval from a manager, or (3) it pertains to ongoing negotiations or engagements which have been designated as confidential by leadership with specific visibility restrictions.  
  The definition of 'Confidential record' now includes specific criteria for marking records to reduce subjectivity and the risk of unauthorized access. _(C11)_

## Success criteria

- **K1** At least 80% of project managers can successfully access and retrieve engagement history for countries they manage, with success measured by system usage analytics tracking number of access attempts and completed records retrieved within three months of the release.  
  Success criteria will track specific metrics like access attempts, ensuring a clear evaluation of project managers' ability to use engagement history effectively. _(C14)_

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What specific criteria are to be used for classifying engagement history records as confidential or diplomatic?**

- Why it matters: This clarity is crucial to prevent unauthorized access to sensitive data by project managers.
- Decision owner: Head of Data Protection
- Options: Establish objective criteria / Maintain current definitions with monitoring / No changes needed
- Proposer's last word (R4, revise, missing decision): The revised definition for 'Confidential record' now includes clear, specific guidelines for authorized personnel, reducing subjectivity in determining confidentiality and protecting against unauthorized access.
- Critic's last word (R4, escalate): The definition still does not clearly establish the specific criteria authorized personnel must follow, leaving room for potential subjectivity.

### C12 · BLOCKER · blocks the build

**What specific processes ensure that project managers' clearance is revoked or reviewed following a change in roles?**

- Why it matters: To ensure accountability and protect sensitive information from exposure after personnel changes.
- Decision owner: Data Governance Team
- Options: Define a clear clearance process / Maintain existing processes / No changes needed
- Proposer's last word (R5, defend, needs human decision): The access clearance for project managers is dependent on organizational policies and human decisions, particularly regarding monitoring and revoking access after role changes, which must be clarified within the organization.
- Critic's last word (R5, escalate): The assumption about project manager clearance lacks a defined process for monitoring access rights after role changes.

### C5 · MAJOR · blocks the build

**What processes ensure that project managers' clearances are regularly reviewed and updated concerning sensitive data access?**

- Why it matters: To prevent unauthorized access after personnel changes, clear processes need to be defined.
- Decision owner: Chief Information Officer
- Options: Implement regular access review processes / Define a new policy for clearance monitoring / No changes needed
- Proposer's last word (R2, defend, needs human decision): While the assumption regarding clearance checks is valid, updating the processes for monitoring clearance requires human oversight and policy decisions at the organizational level.
- Critic's last word (R2, escalate): This requires organizational policy regarding clearance checks, which is outside the scope of the proposal.

### C7 · MAJOR · blocks the build

**What processes are in place to maintain and review project managers' clearance for engagement history access post-role changes?**

- Why it matters: It's vital to ensure that access rights are updated to prevent sensitive data exposure.
- Decision owner: Chief Information Officer
- Options: Develop a clear monitoring process / Rely on current clearance processes / No changes needed
- Proposer's last word (R3, defend, needs human decision): This is a key organizational process that must be defined by the Data Governance Team and Chief Information Officer, as it pertains to compliance and security within existing policies.
- Critic's last word (R3, escalate): The proposal relies on a process that requires human authority for definition; this remains unresolved.

### C9 · MAJOR · blocks the build

**What processes are in place to maintain and review project managers' clearance for engagement history access after role changes?**

- Why it matters: Defining this is essential to uphold data protection protocols and prevent unauthorized access.
- Decision owner: Data Governance Team
- Options: Create a procedure for reviewing access rights / Maintain current monitoring processes / No changes needed
- Proposer's last word (R4, defend, needs human decision): The organization must define its processes for reviewing and updating access rights for project managers following any role changes, as this involves compliance with security and governance policies that are outside of our control.
- Critic's last word (R4, escalate): Specific processes for maintaining and reviewing clearance after role changes need to be defined as they involve compliance with governance policies.

### C10 · MAJOR · blocks the build

**What audit processes are in place to monitor and manage role permissions for accessing engagement histories?**

- Why it matters: Lack of defined audit processes could lead to unauthorized data access, which presents significant risks.
- Decision owner: Head of Data Governance
- Options: Implement regular audit practices / Continue current auditing methods / No changes needed
- Proposer's last word (R5, revise, missing decision): The revision clarifies that the Data Governance Team is responsible for quarterly audits of user access rights, detailing the logging process for access attempts to prevent unauthorized access.
- Critic's last word (R5, maintain): While quarterly audits are mentioned, the evidence does not specify how active monitoring and enforcement of role permissions will be managed.

## Tension report

The primary disagreement centered on how to effectively monitor and enforce confidentiality measures for sensitive data access. The Proposer expressed confidence in the overall structure, yet highlighted concerns regarding incomplete clarity in enforcement, while the Critic raised critical worries about potential unauthorized access due to vagueness in role clearance review processes.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 30 | - | continue |
| 2 | 8 | 3 | 4 | 1 | 0.53 | 85 | 70 | CONTINUE | continue |
| 3 | 10 | 3 | 5 | 2 | 0.52 | 75 | 60 | CONTINUE | continue |
| 4 | 16 | 7 | 5 | 4 | 0.71 | 75 | 35 | CONTINUE | continue |
| 5 | 16 | 1 | 10 | 5 | 0.40 | 82 | 70 | CONCLUDE | consensus |

- Proposer's remaining worry (82/100): Incomplete clarity on the enforcement of confidentiality measures could expose sensitive information.
- Critic's remaining worry (70/100): The monitoring of user access rights might still lead to unauthorized access if processes for tracking changes in role assignments are not clearly defined.
- ⚠ Proposer reported 82/100 confidence while blocker(s) C1, C12 remain unsettled.
- ⚠ C2 was settled by wording a later edit removed; the final proposal no longer says: "role permissions will be managed by the Data Governance Team under the oversight of the Chief Information Officer."
- ⚠ C3 was settled by wording a later edit removed; the final proposal no longer says: "The system will not display or alert project managers to any engagement history records marked as confidential. Any engagement flagged as confidential will have restricted visibility and will not be included in search results."
- ⚠ C4 was settled by wording a later edit removed; the final proposal no longer says: "The engagement history will include data from the last five years, or all available data if fewer than five years exist, excluding any records flagged as confidential."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | X1 | R1 | ESCALATED | 2 | The proposal does not clearly define the criteria that determine if an engagement history record is marked as confidential, which could lead to unauthorized access to sensitive data. |
| C2 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | The proposal does not specify who oversees and manages the role permissions related to accessing engagement history, potentially leading to unauthorized access by users without adequate clearance. |
| C3 | MAJOR | CONFIDENTIALITY | GAP | R1 | REVISED | 0 | The proposal does not address how the system will prevent project managers from seeing or being alerted about records flagged as confidential, risking unauthorized exposure. |
| C4 | MAJOR | DEFINITIONS | S3 | R1 | REVISED | 0 | The term 'last five years' is vague as it does not clarify how historical data is chosen or what happens if older engagements need to be retrieved for context. |
| C5 | MAJOR | OWNERSHIP | A2 | R1 | ESCALATED | 0 | The assumption that project managers will have appropriate clearance does not clarify how clearance for sensitive data is managed or monitored after personnel changes. |
| C6 | MAJOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | The proposal lacks details about how the system will ensure the accuracy and quality of the engagement data being displayed. |
| C7 | MAJOR | OWNERSHIP | A2 | R2 | ESCALATED | 0 | The assumption that project managers have appropriate clearance for engaging with the data lacks clarity on how clearance is monitored post-personnel changes. |
| C8 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal does not specify how the engagement data will be kept up to date beyond the monthly review, particularly when there are changes in projects or contacts. |
| C9 | MAJOR | OWNERSHIP | A2 | R3 | ESCALATED | 0 | The proposal assumes project managers have appropriate clearance, yet does not clarify how access rights are reviewed after role changes. |
| C10 | MAJOR | CONFIDENTIALITY | S2 | R3 | UNRESOLVED | 2 | The proposal lacks clarity on how role permissions will be audited to ensure only authorized users access sensitive records. |
| C11 | BLOCKER | CONFIDENTIALITY | D2 | R4 | REVISED | 0 | The definition of 'Confidential record' remains subjective as it relies on interpretation by authorized personnel, leading to potential unauthorized access. |
| C12 | BLOCKER | OWNERSHIP | A2 | R4 | ESCALATED | 0 | The proposal assumes project managers have appropriate clearance without specifying how clearance is monitored after role changes, risking unauthorized access to sensitive information. |
| C13 | MAJOR | CONFIDENTIALITY | X1 | R4 | REVISED | 0 | The out-of-scope exclusion of confidential records does not ensure that project managers will not encounter flagged records inadvertently. |
| C14 | MAJOR | DATA_QUALITY | K1 | R4 | REVISED | 0 | The success criteria rely on user feedback without defining how usage analytics will measure successful access to the engagement history, leaving ambiguity in how effectiveness is evaluated. |
| C15 | MAJOR | DEFINITIONS | S3 | R4 | REVISED | 0 | 'Last five years' is not clearly defined in terms of data retrieval criteria, posing risks when older engagements are needed for decision-making. |
| C16 | MAJOR | COMPLIANCE | X3 | R4 | REVISED | 0 | The out-of-scope statement does not address whether there are any retention policies or audit trails for sensitive engagement records that might be exempt from visibility rules. |
