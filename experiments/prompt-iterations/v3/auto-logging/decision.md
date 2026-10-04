# Decision record: auto-logging

> Meetings with government officials should be logged automatically so we stop losing engagement history.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.016.

## Summary

This release will automate the logging of meetings with government officials in the Government CRM to maintain accurate engagement history. Specific user roles authorized to access this information, along with data protection policies, need further clarification and decisions by the organization. Currently, the proposal is faced with significant confidence disparity regarding access control and compliance.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Automate the logging of meetings with government officials.  
  Automating the logging of meetings with government officials is essential to improve engagement history accuracy.
- **V2** Ensure that engagement history is preserved and accessible to relevant users.  
  Preserving and making engagement history accessible to relevant users is integral for operational effectiveness.

**In scope**

- **S1** Implement a feature that integrates with existing calendar systems to capture scheduled meetings with government officials.  
  Integrating with existing calendar systems is necessary for capturing scheduled meetings automatically.
- **S2** Log meeting details including date, time, participants, agenda, and outcomes automatically in the CRM.  
  Logging meeting details automatically ensures accuracy in records and minimizes manual errors.
- **S3** Allow users to manually edit meeting logs to correct any inaccuracies immediately after automatic logging.  
  Allowing users to manually edit logs ensures that any inaccuracies are corrected promptly.
- **S4** Restrict access to logged meeting information to authorized roles, specifically regional coordinators, project managers, and executive-level staff, ensuring data protection.  
  Restricting access to logged meeting information ensures data protection, but the specifics of authorized roles need clearer definition. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** The release will not address historical meetings that have not been logged prior to this feature's implementation.  
  Addressing historical meetings is out of scope as it complicates the implementation of the new feature.
- **X2** No additional reporting features for engagement history will be included in this release.  
  No new reporting features are included to maintain focus on the core request.
- **X3** Integration with third-party video conferencing tools (e.g., Zoom, MS Teams).  
  Integration with third-party video conferencing tools is excluded to limit complexity and scope.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users of the CRM have existing calendar systems that can be integrated with the CRM to log meetings automatically. | The request assumes a mechanism for automatically capturing meetings is feasible based on existing user behavior. | Accepted (never challenged) |
| A2 | Users will consistently schedule meetings with government officials in their calendars which the CRM can access. | The feature depends on the presence of scheduled meetings to automate logging. | Accepted (never challenged) |
| A3 | The organization has policies in place that allow for automated logging of meeting information with respect to data protection and privacy regulations. | The request assumes that logging meeting information does not violate any confidentiality or data protection laws. | C3 → escalated |

## Definitions

- **D1** "automate the logging of meetings": To develop a feature that automatically records details of meetings with recognized government officials in the CRM without manual input from users, triggered by calendar integrations.  
  Defining 'government officials' helps clarify which meetings are logged, preventing potential breaches of protocol.
- **D2** "engagement history": The logged record of interactions, including meetings, email exchanges, and communications with government officials, accessible within the CRM.  
  The definition of 'engagement history' remains straightforward and consistent with existing practices.
- **D3** "users": Individuals using the CRM, specifically regional coordinators, project managers, and executive-level staff who interact with government officials.  
  Clarifying who 'users' are aligns expectations about who will benefit from the feature.
- **D4** "government officials": Individuals recognized as representatives of government bodies or agencies with whom meetings are logged.  
  Defining 'government officials' as representatives of government bodies is crucial for appropriate logging.

## Success criteria

- **K1** Percentage of meetings logged automatically: target 75% (Calculate the percentage of meetings scheduled with government officials that are automatically logged in the CRM within three months of feature deployment.)  
  Setting a target percentage for automatic logging ensures measurable success for the feature.

## Open questions for humans

### C3 · BLOCKER · blocks the build

**What are the specific data protection policies governing the automated logging of meeting information?**

- Why it matters: Understanding compliance requirements is critical to avoid legal risks associated with data protection.
- Decision owner: Compliance Officer
- Options: Outline existing policies / Develop new policies for automation

### C4 · BLOCKER · blocks the build

**What is the process for managing logged meeting records when a user changes roles or leaves the organization?**

- Why it matters: Failing to manage access effectively can lead to misuse and loss of valuable engagement history.
- Decision owner: HR Policy Maker
- Options: Establish clear management protocol / Leave as is and manage ad hoc

### C5 · BLOCKER · blocks the build

**What are the specific data protection policies regarding the automated logging of meeting information?**

- Why it matters: Ensuring that there are clear policies in place mitigates risks of data breaches.
- Decision owner: Compliance Officer
- Options: Develop policies / Rely on existing regulations

### C6 · BLOCKER · blocks the build

**What is the established protocol for managing logged meeting records when users change roles or leave the organization?**

- Why it matters: Lack of defined protocols risks unauthorized access to sensitive data.
- Decision owner: HR Policy Maker
- Options: Develop management protocols / Leave access unregulated

### C7 · BLOCKER · blocks the build

**What are the specific roles that have access to logged meeting information and what criteria determine that access?**

- Why it matters: Clarifying access roles prevents potential confidentiality breaches.
- Decision owner: Head of Data Protection
- Options: Define access roles tightly / Keep roles broad based on existing functions

### C1 · MAJOR · blocks the build

**What specific user roles can access logged meeting information, and what criteria determine their access level?**

- Why it matters: Clarity on access roles is crucial for ensuring sensitive data security and preventing unauthorized access.
- Decision owner: Head of Data Protection
- Options: Define specific roles for access / Leave access broad based on job functions

### C2 · MAJOR · blocks the build

**What is the definition of 'government official' used for logging meetings?**

- Why it matters: A clear definition is necessary to avoid improper logging of meetings that could breach protocols.
- Decision owner: Governance Team
- Options: Define as representatives of government agencies / Expand to include other officials

## Tension report

The primary disagreement centers on the clarity and specifics around access controls for logged meeting information. The proposer seeks to automate meeting logging while ensuring access remains secure, whereas the critic expresses significant concern over unresolved definitions and potential unauthorized access risks.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 70 | 30 | - | continue |
| 2 | 4 | 4 | 0 | 0 | 1.00 | 80 | 70 | CONTINUE | continue |
| 3 | 6 | 3 | 0 | 3 | 1.00 | 70 | 40 | CONTINUE | continue |
| 4 | 7 | 3 | 0 | 4 | 1.00 | 60 | 20 | CONTINUE | continue |
| 5 | 7 | 1 | 0 | 6 | 1.00 | 60 | 55 | CONTINUE | continue |
| 6 | 7 | 0 | 0 | 7 | 1.00 | 70 | 30 | CONTINUE | converged |

- Proposer's remaining worry (70/100): Access controls need to be clearly defined by the organization to prevent potential security risks.
- Critic's remaining worry (30/100): Access to sensitive meeting logs is still unclearly defined, potentially leading to unauthorized access.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S4 | R1 | ESCALATED | 2 | S4 restricts access to logged meeting information based on user roles, but does not specify which roles can access what information or how those roles are determined, risking unauthorized access to sensitive data. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | ESCALATED | 2 | D1 defines 'automate the logging of meetings' but does not specify which government officials are included or how they are determined, leading to ambiguity in implementation. |
| C3 | BLOCKER | COMPLIANCE | A3 | R1 | ESCALATED | 2 | A3 states there are policies allowing automated logging but does not provide clarity on what those policies entail or how compliance with data protection regulations will be ensured. |
| C4 | BLOCKER | OWNERSHIP | GAP | R2 | ESCALATED | 2 | There is no information provided on how the system will manage logged meeting records when personnel change roles or leave the organization, which risks losing important engagement history or compromising access permissions. |
| C5 | BLOCKER | COMPLIANCE | GAP | R3 | ESCALATED | 2 | The proposal lacks detailed information on specific data protection policies related to the automated logging of meeting information, which is crucial for ensuring compliance. |
| C6 | BLOCKER | OWNERSHIP | GAP | R3 | ESCALATED | 2 | There is no outlined process for managing logged meeting records when personnel change roles or leave, which could lead to unauthorized access or loss of valuable engagement history. |
| C7 | BLOCKER | CONFIDENTIALITY | GAP | R4 | ESCALATED | 2 | The proposal does not specify which roles have access to logged meeting information nor how those roles are determined, raising potential issues of unauthorized access to sensitive data. |
