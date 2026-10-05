# Decision record: right-contact

> We need a better way to track who is the right person to contact in each country.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.006.

Challenges: 8 raised · 6 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

A contact tracking feature will be built to assist regional coordinators and project managers in identifying primary contacts in member countries, accompanied by engagement history and a process for reevaluating contact roles. Automatic alerts for role changes, integration with external systems, and changes to security protocols will not be included. Decisions are still needed on how confidentiality policies are enforced and to clarify ambiguous assumptions about those policies.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable tracking of primary contacts for each member country.
- **V2** Provide engagement history linked to identified contacts.

**In scope**

- **S1** Implement a searchable contact list feature that allows users to filter contacts by country, role, and project affiliation.
- **S2** Establish a database schema modification to include fields for 'primary contact' designation per country, with a defined process for updating primary contact designations immediately upon personnel changes, handled by regional coordinators.  
  This scope item details who is responsible for maintaining currency in primary contact designations, addressing critical ownership concerns. _(C1, C2)_
- **S3** Ensure that engagement history is accessible for each contact displayed in the system.
- **S4** Provide user training materials to regional coordinators and project managers on using the new contact tracking features.
- **S5** Develop a user interface that highlights the primary contact whenever a country profile is viewed, incorporating role-based access controls to restrict views of sensitive engagement information based on user roles and responsibilities.  
  Highlighting primary contacts with role-based access controls is a necessary measure to maintain data confidentiality. _(C4)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include automatic alerts or notifications for changes in contact roles.
- **X2** This release will not incorporate direct integration with external databases or CRM systems.
- **X3** This release will not change the underlying security protocols governing data access.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users will have the necessary permissions to access and modify contact information based on their roles in the organization. | Kept | never challenged |
| A2 | It is assumed that current user training on existing processes will be sufficient for using the new features. | Kept | never challenged |
| A3 | The organization will maintain the policy of confidentiality regarding sensitive contact information. | Kept | C5 → escalated; C7 → escalated |

## Definitions

- **D1** ‘primary contact’ means the designated individual in a member country responsible for communication regarding specific projects or engagements, who must hold a role within the organization that involves oversight or direct involvement with relevant projects. The process for reevaluating a primary contact's status includes an annual review by regional coordinators or upon notification of role changes, and these changes must be documented in the system to maintain transparency.  
  Defining 'primary contact' ensures that only those with appropriate oversight roles can be designated, minimizing confidentiality risks. _(C3, C8)_
- **D2** 'engagement history' means a record of interactions, communications, and transactions with the contact related to the organization's projects, specifically including email correspondence, meeting notes, and project updates.  
  Clarifying 'engagement history' helps ensure consistency in how interactions are recorded and documented. _(C6)_
- **D3** 'searchable contact list' means a feature that allows users to filter and locate contacts based on specific criteria such as country, role, or project.

## Success criteria

- **K1** Achieve a user satisfaction score of 80% or higher in post-release user feedback surveys regarding the contact tracking feature.

## Open questions for humans

### C7 · MAJOR · blocks the build

**What specific measures are defined to enforce confidentiality policies regarding sensitive contact information?**

- Why it matters: Ensuring that measures for enforcement are in place will protect sensitive information from unauthorized access, addressing a major concern.
- Decision owner: Head of Compliance
- Options: Develop a defined enforcement strategy / Continue without specific enforcement measures
- Proposer's last word (R3, defend, needs human decision): The enforcement of confidentiality policies is an organizational matter that requires input from compliance and legal teams. The specifics of these measures are not our decision to make, so we should maintain this assumption until clarified.
- Critic's last word (R3, escalate): The specifics of confidentiality enforcement measures depend on external policies and the compliance/legal teams, leaving this unresolved.

### C5 · MINOR · does not block the build

**What specific policies are in place regarding confidentiality of sensitive contact information and how are they enforced?**

- Why it matters: Clarification of confidentiality policies will ensure consistent handling of sensitive information, reducing the risk of unintentional breaches.
- Decision owner: Head of Compliance
- Options: Define clear confidentiality policies / Maintain current ambiguity in policies
- Proposer's last word (R2, defend, needs human decision): Organizational confidentiality policies and their enforcement are not under the purview of this proposal and must be defined by the organization.
- Critic's last word (R2, escalate): This issue requires input from human decision-makers regarding organizational policies.

## Tension report

The key disagreement focused on the clarity and enforceability of confidentiality policies. The proposer believes that current provisions allow for sufficient compliance, while the critic expresses significant concern over potential exposure of sensitive information without explicit enforcement mechanisms.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 8 | 2 | 5 | 1 | 0.33 | 80 | 70 | CONTINUE | continue |
| 3 | 8 | 0 | 6 | 2 | 0.20 | 80 | 50 | CONTINUE | converged |

- Proposer's remaining worry (80/100): The implementation of appropriate enforcement measures for confidentiality policies needs clarification to ensure compliance.
- Critic's remaining worry (50/100): The proposal lacks a concrete mechanism for enforcing confidentiality, risking exposure to sensitive diplomatic information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | OWNERSHIP | S2 | R1 | REVISED | 0 | The proposal does not specify who is responsible for maintaining the accuracy and currency of the primary contact information, which is critical to avoid future miscommunication. |
| C2 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | There is no clear process outlined for how primary contact designations will be managed when an individual changes roles or leaves the organization. |
| C3 | MAJOR | CONFIDENTIALITY | D1 | R1 | REVISED | 0 | The criteria for determining who qualifies as a primary contact are not defined, risking the inclusion of individuals who should not have sensitive information accessible. |
| C4 | MAJOR | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | There are no safeguards outlined to prevent unauthorized access to sensitive contact information, risking exposure of diplomatic information. |
| C5 | MINOR | COMPLIANCE | A3 | R1 | ESCALATED | 0 | The assumption regarding the organization's policy on confidentiality is vague and could lead to inconsistencies in how contacts are managed across the system. |
| C6 | MINOR | DEFINITIONS | D2 | R1 | REVISED | 0 | The term 'engagement history' is not clearly defined in terms of what specific information it includes, which may lead to inconsistent data entry and expectations. |
| C7 | MAJOR | COMPLIANCE | A3 | R2 | ESCALATED | 0 | The lack of clarity around enforcement of confidentiality policies may lead to unintentional breaches of sensitive information. |
| C8 | MAJOR | DEFINITIONS | D1 | R2 | REVISED | 0 | While D1 defines 'primary contact', it does not clarify the process for reevaluating this status when project roles change or upon unsatisfactory performance. |
