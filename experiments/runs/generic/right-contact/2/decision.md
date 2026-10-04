# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.009.

Challenges: 8 raised · 4 settled between the agents · 4 handed to humans · 0 still open when it ended.

## Summary

This release will implement a mechanism for tracking the primary contact person for each country within the Government CRM system. It aims to enhance the communication and engagement process for regional coordinators and project managers. However, there are unresolved concerns regarding the validation of existing contact records and user permissions that must still be addressed before moving forward.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Implement a feature that allows users to designate a primary contact for each country.  
  A feature will be developed that allows users to designate a primary contact for each country, ensuring better coordination and outreach.
- **V2** Provide a streamlined interface to update and view primary contact information.  
  A streamlined interface for updating and viewing primary contact information will provide users with easier access to the necessary details.

**In scope**

- **S1** Allow regional coordinators to set and edit the primary contact person for each country in the system; if the primary contact leaves or changes roles, a designated administrator will be responsible for reassigning the primary contact to ensure up-to-date information.  
  Regional coordinators will have the capability to set and edit the primary contact, with designated administrators managing changes when contacts leave or change roles, ensuring information remains current. _(C1)_
- **S2** Display the primary contact information prominently on each country profile within the CRM.  
  Primary contact information will be displayed prominently within the country profile to allow quick access for users.
- **S3** Enable project managers to view the list of primary contacts while browsing through country records.  
  Project managers will be able to view the list of primary contacts to facilitate their engagement efforts.
- **S4** Implement a search function that enables users to quickly find the primary contact for a selected country.  
  A search function will allow users to quickly find the designated primary contact for specific countries, improving efficiency.
- **S5** Implement a notification mechanism to alert users when primary contact information has been updated, ensuring that regional coordinators and project managers are aware of any changes.  
  A notification mechanism will be implemented to alert users of any updates to primary contact information, enhancing communication among coordinators and project managers. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include integration with external databases for contact information.  
  Integration with external databases for contact information has been ruled out to maintain system integrity and focus on internal resources.
- **X2** This release will not support multi-language capabilities for contact information display.  
  Multi-language capabilities for the display of contact information have been deemed outside the scope of this release to prioritize essential functionalities.
- **X3** This release will not include any automated alerts or notifications regarding contact changes.  
  Automated alerts or notifications regarding contact changes will not be included in this release to avoid confusion with the new notification mechanism.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | It is assumed that each country will have only one designated primary contact person, which impacts the design of contact assignment. | Kept | never challenged |
| A2 | It is assumed that all users of the CRM have the necessary permissions to edit country contact information based on established organizational policies. | Kept | C6 → escalated; C8 → escalated |
| A3 | It is assumed that current country records already contain basic information about contact entities, on which this feature will build. | Kept | C3 → escalated; C7 → escalated |

## Definitions

- **D1** 'primary contact' means the designated individual responsible for communication on behalf of the organization within a specific country and designated by the regional coordinator; this individual is expected to be the point of contact for all engagements related to that country.  
  The definition of 'primary contact' has been enhanced to clarify responsibilities and reduce ambiguity in interpretations across users. _(C5)_
- **D2** 'user roles' means the classification of CRM users (regional coordinators, project managers) with specific permissions related to country contact management; regional coordinators can edit contact information, while project managers can only view it.  
  The definition of 'user roles' has been specified to prevent unauthorized access and changes, ensuring only the designated individuals can edit contact information. _(C2)_

## Success criteria

- **K1** At least 80% of regional coordinators report improved ability to identify primary contacts in a user satisfaction survey conducted three months after release.  
  A success criterion has been established to measure the effectiveness of the new contact identification feature through user satisfaction surveys.

## Open questions for humans

### C7 · BLOCKER · blocks the build

**What specific process will be followed to validate the accuracy and completeness of existing contact records?**

- Why it matters: A defined process is crucial to ensure that the primary contact system is built on reliable information.
- Decision owner: Data Quality Manager
- Options: Develop a team to review current records / Create a system for user feedback on inaccuracies / Set up periodic reviews of contact information
- Proposer's last word (R3, defend, needs human decision): The accuracy and completeness of contact records will require input from the organization to define the validation process.
- Critic's last word (R3, escalate): The proposal does not specify a definitive process for validating existing contact records, relying on undefined input from the organization.

### C8 · BLOCKER · blocks the build

**What specific organizational policies dictate user permissions for editing primary contact information?**

- Why it matters: This will help establish clear rules to manage access and ensure data integrity.
- Decision owner: Director of IT Governance
- Options: Draft new detailed permission guidelines / Clarify current permissions with stakeholders / Define permissions based on user roles and responsibilities
- Proposer's last word (R3, defend, needs human decision): The definition of user permissions for editing contact information must be established by organizational policies and cannot be decided in this proposal.
- Critic's last word (R3, escalate): The proposal does not provide established user permissions for editing contact information, depending on policies outside this proposal.

### C3 · MAJOR · blocks the build

**How will the accuracy and completeness of existing contact records be validated before this feature is implemented?**

- Why it matters: Ensuring accurate contact records is essential for preventing misinformation in diplomatic communications.
- Decision owner: Head of Data Management
- Options: Conduct a thorough audit of existing records / Implement a user-driven update process / Set baseline requirements for existing records
- Proposer's last word (R2, defend, needs human decision): The accuracy and completeness of existing contact records require validation that must be conducted according to the organization's policies and procedures before implementing this feature.
- Critic's last word (R2, escalate): The reliance on human decision for validation of existing records leaves a gap in assurance for data quality.

### C6 · MINOR · does not block the build

**What specific organizational policies govern user permissions regarding the editing of contact information?**

- Why it matters: Clear policies are necessary to prevent unauthorized access and maintain data integrity.
- Decision owner: Head of Data Protection
- Options: Establish a new policy for user permissions / Reinforce existing policies with updates / Limit user access based on role-specific guidelines
- Proposer's last word (R2, defend, needs human decision): Establishing and enforcing user permissions regarding the editing of contact information must be determined by the organization's existing policies.
- Critic's last word (R2, escalate): User permissions require a clear rule from organizational policy, which remains unconfirmed.

## Tension report

The primary tension arose around the validation of existing contact records and the establishment of clear user permissions for editing contact information. The Proposer expressed a need for accurate records to mitigate miscommunication, while the Critic highlighted the lack of established processes, which remains unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 8 | 2 | 4 | 2 | 0.56 | 80 | 50 | CONTINUE | continue |
| 3 | 8 | 0 | 4 | 4 | 0.56 | 75 | 20 | CONTINUE | converged |

- Proposer's remaining worry (75/100): Ensuring the accuracy of contact records before the feature goes live is critical to avoid miscommunications.
- Critic's remaining worry (20/100): The lack of clarity and established processes for validating contact information and user permissions jeopardizes the feature's integrity.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | OWNERSHIP | S1, S2 | R1 | REVISED | 0 | The proposal does not specify how changes to the primary contact information will be managed when personnel leave or change roles. |
| C2 | MAJOR | CONFIDENTIALITY | S1, S4 | R1 | REVISED | 0 | The proposal lacks clarity on who can see and edit primary contact information across different user roles. This could lead to unauthorized changes. |
| C3 | MAJOR | DATA_QUALITY | A3 | R1 | ESCALATED | 0 | The assumption that current country records contain basic contact information does not address potential inaccuracies or omissions in those records. |
| C4 | MINOR | OPERATIONS | X3 | R1 | REVISED | 0 | The proposal does not address how users will be notified of changes to primary contacts, which could lead to confusion and outdated interactions. |
| C5 | MINOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The definition of 'primary contact' is not detailed enough to avoid ambiguity in its application across different contexts or scenarios. |
| C6 | MINOR | OWNERSHIP | A2 | R1 | ESCALATED | 0 | The assumption about user permissions lacks specificity on how these permissions are established and enforced within the organization. |
| C7 | BLOCKER | DATA_QUALITY | A3 | R2 | ESCALATED | 0 | The proposal does not detail how to ensure the accuracy and completeness of contact records before the feature is implemented, which is critical for preventing misinformation. |
| C8 | BLOCKER | OWNERSHIP | A2 | R2 | ESCALATED | 0 | User permissions for editing contact information remain unclear and require definitive organization-wide rules. |
