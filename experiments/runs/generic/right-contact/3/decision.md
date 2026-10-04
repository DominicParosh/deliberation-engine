# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **consensus** after 3 rounds (policy `gated`) · $0.007.

Challenges: 7 raised · 7 settled between the agents · 0 handed to humans · 0 still open when it ended.

## Summary

This release will introduce a new contact tracking feature allowing users to identify appropriate government representatives easily, with secure access controls tailored to specific roles. Features included are a searchable database, user interface enhancements, and mechanisms for updating contact information. However, automated suggestions, integration with external databases, and AI-driven features will not be included in this release. It remains to ensure that all users understand their permissions and data security processes.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enhance user ability to identify the right contact person for government counterparts based on specific criteria.  
  Enhancing user ability to identify the right contact person was essential to address operational needs and improve interactions with government counterparts.

**In scope**

- **S1** Implement a searchable database that allows users to filter contacts by criteria such as role, ministry, and current engagement status.  
  Implementing a searchable database enables users to efficiently filter contacts, significantly benefiting project managers and regional coordinators.
- **S2** Develop a user interface for project managers and regional coordinators to view and select relevant contacts.  
  Developing a user interface tailored for the intended users enhances usability and effectiveness in identifying contacts.
- **S3** Integrate contact history in a manner that limits visibility to users based on their access rights, ensuring only 'Project Managers' and 'Regional Coordinators' can view sensitive histories associated with their projects.  
  Integrating contact history with restricted visibility based on user role ensures sensitive information is protected from unauthorized access. _(C4)_
- **S4** Ensure that there is a mechanism in place for regularly updating and verifying the accuracy of contact details in the database, including a process for timely revocation of access when personnel change roles or leave.  
  Establishing mechanisms for regularly updating contact details ensures data remains accurate, which is crucial for effective communication. _(C5, C7)_
- **S5** Establish user permissions so that only personnel in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff' can access sensitive contact details.  
  Clarifying which roles comprise 'authorized personnel' limits access to sensitive information, addressing confidentiality concerns. _(C1)_
- **S6** Provide user training and support materials to ensure users are familiar with the new contact tracking feature and can utilize it effectively.  
  Providing training and support materials enhances the likelihood of successful adoption of the new feature by users, mitigating potential underutilization risks. _(C6)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automated suggestions for contacts or any AI-driven features.
- **X2** This release will not integrate with external government databases or systems.
- **X3** This version will not provide any functionality for tracking engagement history beyond the current contact details.
- **X4** This release will not include any automatic management of access rights when personnel change roles or leave.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have appropriate access rights to sensitive contact information depending on their roles. | Kept | never challenged |
| A2 | The existing CRM infrastructure has the capacity to support a new searchable database feature. | Kept | never challenged |
| A3 | Users require accurate and up-to-date information about the contacts in their respective countries. | Kept | never challenged |

## Definitions

- **D1** "Contact tracking feature" means a system enhancement that allows users to search and filter through government contact records based on predefined criteria.  
  Defining 'contact tracking feature' clarifies system enhancements intended to streamline access to government contact records.
- **D2** "Searchable database" means a collection of contact records that users can query and filter according to specified attributes like role and engagement status.  
  Defining 'searchable database' helps specify the database's functionality for users, ensuring they understand its application.
- **D3** "Authorized personnel" means users in the roles of 'Project Manager', 'Regional Coordinator', and 'Executive Staff', who have received explicit approvals from their direct supervisors to access sensitive information within the CRM.  
  Updating the definition of 'authorized personnel' removes ambiguity around access rights, clarifying user roles required for accessing sensitive data. _(C3)_

## Success criteria

- **K1** Achieve a minimum of 80% user satisfaction based on feedback surveys within one month of release regarding the new contact tracking feature.  
  Setting a user satisfaction target ensures that feedback is captured regarding the effectiveness of the new contact tracking feature after release.

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main tension arose around the clarity of user permissions and the processes for maintaining data security. While the proposer focused on implementing a robust system, the critic raised important concerns about unauthorized access and ensuring all users understood their roles. Both perspectives ultimately contributed to refining the proposal and achieving consensus.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 60 | - | continue |
| 2 | 7 | 3 | 4 | 0 | 0.46 | 85 | 80 | CONTINUE | continue |
| 3 | 7 | 0 | 7 | 0 | 0.00 | 85 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (85/100): Ensuring all specified user roles understand their permissions and the processes in place to maintain data security.
- Critic's remaining worry (85/100): The handling of user permissions remains critical to avoid unauthorized access.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | S5 states that 'only authorized personnel can access sensitive contact details,' but it fails to specify which roles constitute 'authorized personnel.' |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not clarify what happens when personnel change roles or leave, potentially leaving gaps in ownership of contact records. |
| C3 | MAJOR | DEFINITIONS | D3 | R1 | REVISED | 1 | D3 cites 'authorized personnel' but does not define the criteria for what qualifies someone to be authorized, which could lead to ambiguity. |
| C4 | MAJOR | CONFIDENTIALITY | S3 | R1 | REVISED | 1 | S3 mentions integrating contact history but does not indicate how this historical data will be managed to prevent unauthorized access. |
| C5 | MINOR | DATA_QUALITY | GAP | R1 | REVISED | 0 | The proposal does not address how outdated or incorrect data within the contact records will be maintained or updated. |
| C6 | MINOR | OPERATIONS | GAP | R1 | REVISED | 0 | There is no mention of user training or support to ensure the system is adopted effectively, which could lead to underutilization. |
| C7 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal lacks clarity on how access to sensitive contact details will be managed during the transition when personnel leave or change roles. |
