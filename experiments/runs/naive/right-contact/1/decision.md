# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **cap** after 8 rounds (policy `naive`) · $0.030.

Challenges: 23 raised · 10 settled between the agents · 6 handed to humans · 7 still open when it ended.

## Summary

The proposal will enable tracking of primary contact persons for each member country and establish processes to ensure data accuracy through audits and designated responsibilities. However, the current release will not include integration with external systems, historical engagement records, or a defined retention policy for contact information, which will be addressed in future updates. Decisions regarding specific data protection measures and compliance processes will remain open and require human input.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable tracking of primary contact persons for each member country.
- **V2** Implement a process whereby designated staff members, specifically regional coordinators and project managers, are responsible for regularly auditing, verifying, and updating contact information to maintain data accuracy.  
  The process for regularly auditing and verifying contact information will be implemented to enhance data accuracy, addressing prior concerns about outdated records. _(C3)_
- **V3** A designated data integrity officer will oversee the ongoing accuracy of primary contact information, supported by regional coordinators and project managers who are responsible for making and tracking updates.  
  A designated data integrity officer will be responsible for maintaining the accuracy of primary contact information, which clarifies accountability for data integrity. _(C8)_

**In scope**

- **S1** Create a new section in the CRM specifically for tracking primary contact persons, including fields for name, position, email address, and phone number.
- **S2** Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to audit, verify, and protect records at least quarterly and implement corrective actions for any inaccuracies identified outside of these updates. Additionally, implement role-based authentication to ensure that only authorized users can access sensitive contact information, regularly audit user access permissions, and monitor data access logs for suspicious activities.  
  This item includes measures for regular audits of contact details, implementing user access controls, and monitoring data access logs for security, balancing user needs and data protection. _(C16)_
- **S3** Ensure user access controls are in place, allowing only the following roles to view and edit contact information for primary contacts: regional coordinators, project managers, and designated executive staff, with each role restricted to access within their designated territories and areas of responsibility.  
  User access controls are outlined to restrict viewing and editing of contact information to specific roles, enhancing confidentiality measures, though further clarifications are still needed regarding enforcement.
- **S4** Include a search function that allows users to filter and find appropriate contacts by country and role. The search function will prioritize contacts based on the most recent communication activity, sorting contacts in descending order of last communication date, ensuring that users receive the most relevant contact first. In cases where multiple contacts meet the search criteria, the system will display a message indicating the presence of multiple matches, provide buttons for users to view all matched contacts, with the primary contact clearly indicated for each project.  
  An improved search functionality enabling efficient retrieval of contacts based on most recent communication activity will enhance user experience. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external contact databases or systems.
- **X2** This release will not cover historical engagement histories with contacts; it focuses solely on current primary contacts.
- **X3** This release will not define a specific retention period for contact information; this will be determined in future releases after compliance assessment.  
  A specific retention policy for contact information is out of scope as it requires further compliance assessments in future releases.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have the necessary permissions to access and update contact information; this enables them to manage contact details effectively. | Kept | never challenged |
| A2 | The current data structure of the CRM can accommodate the new section for primary contacts without requiring extensive backend modifications. | Kept | never challenged |
| A3 | There are designated staff members responsible for entering and regularly updating contact information. | Kept | never challenged |

## Definitions

- **D1** 'Primary contact person' means the individual identified as the main point of communication for government engagement in a specific country, who has the responsibility for maintaining current contact information and engaging in government counterparts on relevant issues, with ownership of data updates resting with the regional coordinator responsible for that country.  
  The definition of 'primary contact person' has been clarified to eliminate ambiguity regarding roles and responsibilities. _(C2)_
- **D2** "User access controls" means the permissions established to restrict and allow user access to different features and data within the CRM, determined by roles such as regional coordinators, project managers, and executive staff.  
  The definition of 'user access controls' has been refined to specify role-based permissions, enhancing clarity around security measures. _(C6)_
- **D3** 'Search function' means a tool within the CRM that enables users to input criteria and retrieve relevant contacts based on defined fields.
- **D4** Data accuracy means that all contact information, including name, position, email address, and phone number, must be current and verified by a designated data integrity officer, with updates made in real-time when changes occur and verified quarterly to maintain the reliability of the records.  
  The definition of 'data accuracy' now specifies criteria for maintaining reliable contact records, aligning with overall data quality goals. _(C9)_

## Success criteria

- **K1** At least 80% of users can successfully find and update contact information within three searches, measured through user feedback and CRM usage analytics.

## Open questions for humans

### C1 · BLOCKER · blocks the build

**What are the specific criteria for user access controls, and how will they be enforced?**

- Why it matters: This is crucial to mitigating risks of unauthorized access to sensitive information.
- Decision owner: Head of Data Protection
- Options: Define roles clearly / Establish stricter access controls / Implement role-based authentication
- Proposer's last word (R4, revise, missing decision): The revised item now specifies that user access controls not only define the roles but also establish that access will be bounded by designated territories and responsibilities, minimizing the risk of unauthorized access to sensitive information.
- Critic's last word (R4, escalate): The proposal specifies roles but still lacks detailed access control measures and rules for preventing unauthorized access, meaning it remains unaddressed.

### C16 · BLOCKER · blocks the build

**What specific measures will be implemented to safeguard sensitive contact information from unauthorized access?**

- Why it matters: Protecting sensitive information is imperative to maintaining security and diplomatic relations.
- Decision owner: Head of Data Protection
- Options: Define access roles / Establish monitoring systems / Implement training for users
- Proposer's last word (R8, revise, missing decision): The edits now specify concrete measures to protect sensitive diplomatic information, including role-based authentication and regular audits, which directly address the challenge of unauthorized access.
- Critic's last word (R8, maintain): The proposal fails to specify the roles that will be granted access, leaving ambiguity around who can actually view sensitive contact information.

### C18 · BLOCKER · blocks the build

**What are the specific criteria for user access controls, and how are they enforced?**

- Why it matters: This is essential to prevent unauthorized access to sensitive information.
- Decision owner: Head of Data Protection
- Options: Define roles clearly / Set criteria for access / Implement auditing procedures

### C23 · BLOCKER · blocks the build

**Who is responsible for ongoing data integrity checks after updates to contact information?**

- Why it matters: Clear accountability is needed to maintain contact data accuracy.
- Decision owner: Data Integrity Officer
- Options: Designated staff members / Data integrity officer / Regional coordinators

### C11 · BLOCKER · blocks the build

**The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information.**

- Why it matters: Sensitive personal information regarding diplomats is mishandled due to a lack of defined procedures for data management and compliance, leading to legal repercussions.
- Decision owner: To be assigned
- Options: What specific procedures are in place to ensure compliance with data protection laws regarding personal information?
- Proposer's last word (R6, defend, needs human decision): The proposal requires input from the organization to outline specific measures or procedures for compliance with data protection regulations regarding personal contact information.
- Critic's last word (R6, escalate): The lack of clear procedures creates a significant compliance risk that necessitates human decision-making.

### C12 · BLOCKER · blocks the build

**The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system.**

- Why it matters: Diplomats' personal contact information is exposed due to inadequate protection measures, leading to potential security breaches and diplomatic fallout.
- Decision owner: To be assigned
- Options: What specific data protection measures are in place to safeguard the sensitive personal information of diplomatic contacts?
- Proposer's last word (R7, defend, needs human decision): The organization must define specific data protection measures to safeguard sensitive contact information, as this requires compliance with existing legal frameworks and policies.
- Critic's last word (R7, escalate): This is a compliance issue that needs human input.

### C19 · BLOCKER · blocks the build

**The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system, leaving a gap in security measures.**

- Why it matters: Sensitive contact information is exposed due to lack of protective measures, potentially compromising diplomatic engagements and damaging relationships.
- Decision owner: To be assigned
- Options: What specific measures or procedures are in place for protecting sensitive diplomatic contact information?

### C20 · BLOCKER · blocks the build

**The proposal does not mention how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts, which poses legal risks.**

- Why it matters: The organization collects and stores personal data without compliance, leading to violations of data protection laws and incurring penalties.
- Decision owner: To be assigned
- Options: What measures are proposed to ensure compliance with data protection regulations for personal information?

### C21 · BLOCKER · blocks the build

**The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws, presenting significant legal risks.**

- Why it matters: Contact information is retained longer than legally allowed, which could result in fines or legal action against the organization.
- Decision owner: To be assigned
- Options: What will be the process for defining and enforcing a retention policy for contact information?

### C22 · BLOCKER · blocks the build

**The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information, risking legal repercussions.**

- Why it matters: There are violations of data protection laws due to unclear compliance processes, leading to audits and potential penalties.
- Decision owner: To be assigned
- Options: What measures will be taken to ensure compliance with data protection regulations concerning personal contact information?

### C7 · MAJOR · blocks the build

**Who is designated to regularly audit and verify contact information?**

- Why it matters: Clear assignment of auditing responsibilities is needed to maintain data integrity.
- Decision owner: Head of Data Management
- Options: Regional coordinators / Project managers / Data integrity officer
- Proposer's last word (R3, defend, needs human decision): The responsibility for regularly auditing and verifying contact information is a determination that the organization must decide, making this a question for them.
- Critic's last word (R3, escalate): This aspect requires a decision that is beyond the current proposal.

### C10 · MAJOR · blocks the build

**There is no mention of how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts.**

- Why it matters: Sensitive personal information regarding diplomats or officials gets mishandled, leading to a compliance breach and potential legal repercussions for the organization.
- Decision owner: To be assigned
- Options: What measures are in place to ensure compliance with data protection laws regarding personal contact information?
- Proposer's last word (R5, defend, needs human decision): This challenge requires input from legal and compliance teams regarding data protection regulations; current wording will remain as it directs attention to potential compliance issues that must be addressed.
- Critic's last word (R5, escalate): This challenge requires a clear input from legal and compliance teams; further actions on compliance must be taken.

### C13 · MAJOR · blocks the build

**The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws.**

- Why it matters: Contact information is retained longer than necessary, risking legal exposure for not adhering to data protection regulations, leading to potential fines or legal challenges.
- Decision owner: To be assigned
- Options: What is the defined retention period for contact information and how is it managed?
- Proposer's last word (R7, defend, needs human decision): The organization needs to establish a retention policy for contact information to ensure compliance with data protection laws, which is outside the scope of this proposal.
- Critic's last word (R7, escalate): This is a compliance issue that requires human decision.

## Tension report

The primary disagreement arose over defining specific access controls and compliance measures essential for safeguarding sensitive data. The proposer expressed concern about balancing security with user access, while the critic raised significant issues regarding compliance and risk management, leading to unresolved questions for further human decision-making.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 7 | 4 | 3 | 0 | 0.62 | 80 | 80 | CONTINUE | continue |
| 3 | 7 | 2 | 4 | 1 | 0.46 | 85 | 65 | CONTINUE | continue |
| 4 | 10 | 4 | 4 | 2 | 0.65 | 80 | 70 | CONTINUE | continue |
| 5 | 11 | 3 | 5 | 3 | 0.57 | 70 | 60 | CONTINUE | continue |
| 6 | 15 | 6 | 5 | 4 | 0.69 | 70 | 55 | CONTINUE | continue |
| 7 | 17 | 2 | 9 | 6 | 0.55 | 75 | 70 | CONTINUE | continue |
| 8 | 23 | 7 | 10 | 6 | 0.64 | 75 | 30 | CONTINUE | cap |

- Proposer's remaining worry (75/100): The challenge of implementing sufficient security measures while balancing user access requirements remains significant.
- Critic's remaining worry (30/100): The proposal still lacks sufficient measures to ensure compliance and protect sensitive information, leading to significant security and legal risks.
- ⚠ C4 was settled by wording a later edit removed; the final proposal no longer says: "S2: Implement functionality allowing regional coordinators and project managers to edit and update contact details as needed, with a mandatory process to update records when individuals leave or change roles, ensuring data integrity."

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S3 | R1 | ESCALATED | 2 | The proposal does not clearly specify the criteria for user access controls and how they will prevent unauthorized access to sensitive contact information. |
| C2 | MAJOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The term 'primary contact person' is not clearly defined in terms of authority or responsibility, leading to ambiguity in its application. |
| C3 | MAJOR | DATA_QUALITY | S4 | R1 | REVISED | 1 | There is no clear plan for how to ensure data accuracy and regular updates, which is critical for maintaining reliable contact records. |
| C4 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal lacks a clear outline of who is responsible for data integrity when contacts leave or change roles, leading to potential data management gaps. |
| C5 | MINOR | OPERATIONS | GAP | R1 | REVISED | 5 | There is insufficient detail on how the search function will work, specifically regarding prioritization or filtering criteria, which could affect user experience. |
| C6 | MINOR | DEFINITIONS | GAP | R1 | REVISED | 0 | The definition of 'user access controls' is vague and does not specify how access levels will be determined or enforced. |
| C7 | MAJOR | DATA_QUALITY | S4 | R2 | ESCALATED | 0 | The lack of clarity around who is responsible for auditing and updating contact information means there is a risk of data becoming outdated. |
| C8 | BLOCKER | OWNERSHIP | GAP | R4 | REVISED | 0 | The proposal does not specify who is responsible for maintaining the data integrity of contact information or how ongoing management will occur after updates are made by regional coordinators and project managers. |
| C9 | MAJOR | DEFINITIONS | GAP | R4 | REVISED | 2 | The definition of 'data accuracy' is not provided, leading to ambiguity around what conditions must be met for contact information to be considered accurate and current. |
| C10 | MAJOR | COMPLIANCE | GAP | R4 | ESCALATED | 0 | There is no mention of how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts. |
| C11 | BLOCKER | COMPLIANCE | GAP | R5 | ESCALATED | 0 | The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information. |
| C12 | BLOCKER | CONFIDENTIALITY | GAP | R6 | ESCALATED | 0 | The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system. |
| C13 | MAJOR | COMPLIANCE | GAP | R6 | ESCALATED | 0 | The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws. |
| C14 | MAJOR | OWNERSHIP | GAP | R6 | REVISED | 0 | The proposal does not clarify who officially owns the contact data once it is updated by various users, which raises accountability issues. |
| C15 | MAJOR | DATA_QUALITY | GAP | R6 | REVISED | 0 | There is no process defined for identifying and fixing inaccuracies in the contact database outside regular updates, risking reliance on outdated information. |
| C16 | BLOCKER | CONFIDENTIALITY | GAP | R7 | UNRESOLVED | 1 | The proposal fails to address specific measures or procedures that will be used to protect sensitive diplomatic contact information from unauthorized access. |
| C17 | BLOCKER | COMPLIANCE | GAP | R7 | CONCEDED | 0 | Without a defined retention policy for contact information, the proposal risks non-compliance with data protection regulations. |
| C18 | BLOCKER | CONFIDENTIALITY | S3 | R8 | UNRESOLVED | 0 | The proposal does not clearly specify the criteria for user access controls and how they will prevent unauthorized access to sensitive contact information, which remains a major risk. |
| C19 | BLOCKER | CONFIDENTIALITY | GAP | R8 | UNRESOLVED | 0 | The proposal does not specify how sensitive contact information, particularly diplomatic contacts, will be protected from unauthorized access or breaches in the system, leaving a gap in security measures. |
| C20 | BLOCKER | COMPLIANCE | GAP | R8 | UNRESOLVED | 0 | The proposal does not mention how personal data will be managed in compliance with data protection regulations, especially given the sensitivity of diplomatic contacts, which poses legal risks. |
| C21 | BLOCKER | COMPLIANCE | GAP | R8 | UNRESOLVED | 0 | The proposal does not outline a retention policy for contact information, which is crucial for compliance with data protection laws, presenting significant legal risks. |
| C22 | BLOCKER | COMPLIANCE | GAP | R8 | UNRESOLVED | 0 | The proposal does not outline specific measures or procedures in place for ensuring compliance with data protection regulations regarding personal contact information, risking legal repercussions. |
| C23 | BLOCKER | OWNERSHIP | GAP | R8 | UNRESOLVED | 0 | The proposal does not specify who is responsible for maintaining the data integrity of contact information or how ongoing management will occur after updates are made, leading to potential data management gaps. |
