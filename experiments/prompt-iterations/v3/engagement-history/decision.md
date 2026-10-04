# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.015.

## Summary

This release will enable project managers to view the complete engagement history with each country prior to initiating a new mission, enhancing their decision-making by providing relevant historical data. However, unresolved issues remain regarding compliance with data protection laws and access control monitoring procedures. Further decisions by relevant personnel are required before moving forward with implementation.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can view the full engagement history for each country.  
  Project managers will have the capability to view the complete engagement history with each country, to support informed decision-making.

**In scope**

- **S1** Display a chronological list of all engagements with a country, including contact dates, meeting minutes, and outcomes.  
  A chronological list of all engagements with each country will be displayed, including contact dates, meeting minutes, and outcomes.
- **S2** Include filtering options for engagement history by date range and engagement type (e.g., meetings, correspondence, reports).  
  Filtering options for engagement history by date range and engagement type will facilitate better data analysis for project managers.
- **S3** Ensure that only project managers have access to this feature.  
  Only project managers will have access to this feature, ensuring that it is used appropriately within the organization.
- **S4** Implement access control using role-based permissions to protect sensitive data such as diplomatic communications, project reports, and personal identifiable information. Procedures for role changes will include immediate access revocation upon project manager turnover.  
  Access control will employ role-based permissions and will be monitored through audits to protect sensitive data, addressing confidentiality concerns raised in C1. _(C1, C9)_
- **S5** Engagement history data will be retained for a maximum of five years from the date of the interaction before it is automatically deleted.  
  Engagement history data will be retained for a maximum of five years, as decided to comply with data protection regulations.
- **S6** Access control will be monitored through regular audits of user activity logs and permissions will be revoked immediately upon project manager role changes.  
  Access control monitoring through audits, ensuring permissions are revoked when project managers change roles, addresses confidentiality risks raised in C8. _(C8)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not allow editing or modification of engagement history.
- **X2** This release does not include integration with external data sources for engagement history.
- **X3** This release will not provide detailed analytics or reporting on engagement trends.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Access permissions for project managers will only be granted through a formal role assignment process within the CRM, with notifications to manage changes in personnel.   | The request assumes that project managers will need proper access rights to view the engagement history. | C4 → escalated |
| A2 | Engagement history data exists and is reliably recorded in the CRM system. | The request assumes that historical engagement information is stored in a manner that can be retrieved. | Accepted (never challenged) |
| A3 | Data protection laws regulate access to engagement data, requiring consultation with legal allies to clarify compliance requirements. | The request assumes compliance with data protection regulations regarding sensitive information. | C3 → escalated |

## Definitions

- **D1** "full history of engagement": The complete record of all formal documented interactions with a country, including meetings, reports, and official correspondence, explicitly excluding informal communications such as personal emails or chat messages, and limited to records from the last five years.  
  The definition of 'full history of engagement' now explicitly states it includes formal documented interactions while excluding informal communications, addressing clarity concerns from C2.
- **D2** "project managers": Users in the CRM system designated to oversee and manage specific projects involving countries.  
  Defined 'project managers' as users overseeing specific projects, ensuring clarity in user roles.
- **D3** "new mission": Any officially sanctioned initiative or project that the organization undertakes with a partnering country.  
  Clarified that 'new mission' refers to any officially sanctioned initiative with partnering countries, maintaining consistency of terminology.

## Success criteria

- **K1** Percentage of project managers accessing engagement history: target 80% of project managers will successfully access the engagement history of at least one country in the first month after launch. (Monitor usage statistics in the CRM system after the release.)  
  Set a success criterion of 80% project managers accessing engagement history in the first month post-launch, to evaluate feature adoption effectiveness.

## Open questions for humans

### C3 · BLOCKER · blocks the build

**What specific data protection laws regulate access to the engagement history, and how will compliance be ensured?**

- Why it matters: Understanding legal frameworks is critical for avoiding violations and ensuring informed access.
- Decision owner: Legal Advisor
- Options: Identify applicable data protection laws / Draft a compliance framework

### C5 · BLOCKER · blocks the build

**What is the defined retention policy for engagement history data?**

- Why it matters: Establishing clear retention guidelines is vital for compliance with data protection regulations.
- Decision owner: Compliance Officer
- Options: Set a maximum retention period / Review current data retention practices

### C9 · BLOCKER · blocks the build

**What specific sensitive data needs to be protected in the engagement history, and what procedures are in place for roles and access to this data upon project manager turnover?**

- Why it matters: Clarifying sensitive data protection is crucial for safeguarding confidential information.
- Decision owner: Head of Data Protection
- Options: Specify types of sensitive data / Outline access procedures for role changes

### C1 · MAJOR · blocks the build

**What specific measures will be taken to ensure sensitive data within the engagement history is protected?**

- Why it matters: Defining protection measures for sensitive data is crucial to avoid legal repercussions.
- Decision owner: Head of Data Protection
- Options: Define specific sensitive data types / Clarify monitoring and enforcement procedures

### C2 · MAJOR · blocks the build

**What is the exact scope of records included in the 'full history of engagement' and are there exclusions?**

- Why it matters: Clarifying this prevents misinterpretation and ensures compliance with data protection protocols.
- Decision owner: Product Owner
- Options: Confirm that only formal records are included / Detail exclusions more explicitly

### C4 · MAJOR · blocks the build

**How are permissions managed for project managers and what processes exist for updating access rights when personnel change?**

- Why it matters: Addressing this ensures that sensitive information is accessed only by the appropriate personnel.
- Decision owner: CRM Administrator
- Options: Implement a role-based access system / Establish a notification process for role changes

### C6 · MAJOR · blocks the build

**What specific measures are in place to monitor and enforce access control for engagement history?**

- Why it matters: Detailed procedures for monitoring access control are essential to prevent unauthorized access.
- Decision owner: Security Officer
- Options: Define a regular audit schedule / Implement user access reviews

## Tension report

The primary disagreements centered around the definitions of sensitive data and the clarity of access control measures. Despite multiple revisions, the Proposer and Critic could not fully reconcile their differences after several rounds, leading to multiple escalated issues that require further organizational input.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 0 | 0 | 1.00 | 70 | 50 | - | continue |
| 2 | 6 | 6 | 0 | 0 | 1.00 | 75 | 50 | CONTINUE | continue |
| 3 | 8 | 2 | 0 | 6 | 1.00 | 70 | 50 | CONTINUE | continue |
| 4 | 9 | 1 | 2 | 6 | 0.74 | 80 | 70 | CONTINUE | continue |
| 5 | 9 | 1 | 2 | 6 | 0.74 | 70 | 60 | CONTINUE | continue |
| 6 | 9 | 0 | 2 | 7 | 0.74 | 50 | 70 | CONTINUE | converged |

- Proposer's remaining worry (50/100): There is still uncertainty regarding compliance with data protection laws, which could impact successful implementation.
- Critic's remaining worry (70/100): Access control monitoring and enforcement procedures remain unspecified, posing risk of unauthorized data exposure.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S4 | R1 | ESCALATED | 2 | The proposal mentions access control to protect sensitive data, but it does not specify how this will be implemented or what sensitive data is included. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | ESCALATED | 2 | The definition of 'full history of engagement' is unbounded as it does not specify the limitation on records, leading to uncertainty on what is included or excluded. |
| C3 | BLOCKER | COMPLIANCE | A3 | R1 | ESCALATED | 2 | The assumption that data protection laws permit access to engagement data is unfounded and lacks clarity on legal compliance regarding sensitive information. |
| C4 | MAJOR | OWNERSHIP | A1 | R1 | ESCALATED | 2 | The assumption that project managers have the necessary permissions to access engagement history is vague and does not outline how permissions are granted or what happens on role changes. |
| C5 | BLOCKER | COMPLIANCE | GAP | R2 | ESCALATED | 0 | The proposal does not address what the retention policy is for engagement history data, which is critical for compliance with data protection laws. |
| C6 | MAJOR | CONFIDENTIALITY | GAP | R2 | ESCALATED | 0 | It remains unspecified how access control will be monitored and enforced beyond the initial role-based permissions, which raises risks of unauthorized access following personnel changes or user errors. |
| C7 | BLOCKER | COMPLIANCE | GAP | R3 | REVISED | 0 | The proposal does not specify a retention policy for engagement history data. |
| C8 | BLOCKER | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | The proposal does not address how access control will be enforced and monitored beyond role-based permissions, raising risks of unauthorized access. |
| C9 | BLOCKER | CONFIDENTIALITY | GAP | R4 | ESCALATED | 2 | The proposal does not define what specific sensitive data from engagement history needs to be protected, nor does it clarify the procedures when project managers leave the organization or change roles, raising risks of unauthorized access. |
