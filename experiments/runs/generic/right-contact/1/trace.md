# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 3 rounds · 7 model calls (0 repairs)

## Round 1

### Proposer · confidence 70

_This release delivers a contact tracking feature for regional coordinators and project managers to identify the primary contacts in each member country, ensuring that engagement history and roles are clearly documented. The feature will enhance the existing Government CRM system by enabling users to quickly locate and verify the appropriate contacts for each country based on their project involvement._

**Core commitments**
- V1: Enable tracking of primary contacts for each member country.
- V2: Provide engagement history linked to identified contacts.

**In scope**
- S1: Implement a searchable contact list feature that allows users to filter contacts by country, role, and project affiliation.
- S2: Establish a database schema modification to include fields for 'primary contact' designation per country.
- S3: Ensure that engagement history is accessible for each contact displayed in the system.
- S4: Provide user training materials to regional coordinators and project managers on using the new contact tracking features.
- S5: Develop a user interface that highlights the primary contact whenever a country profile is viewed.

**Out of scope**
- X1: This release will not include automatic alerts or notifications for changes in contact roles.
- X2: This release will not incorporate direct integration with external databases or CRM systems.
- X3: This release will not change the underlying security protocols governing data access.

**Assumptions**
- A1: Users will have the necessary permissions to access and modify contact information based on their roles in the organization.
- A2: It is assumed that current user training on existing processes will be sufficient for using the new features.
- A3: The organization will maintain the policy of confidentiality regarding sensitive contact information.

**Definitions**
- D1: 'primary contact' means the designated individual in a member country responsible for communication regarding specific projects or engagements.
- D2: 'engagement history' means a record of interactions, communications, and transactions with the contact related to the organization's projects.
- D3: 'searchable contact list' means a feature that allows users to filter and locate contacts based on specific criteria such as country, role, or project.

**Success criteria**
- K1: Achieve a user satisfaction score of 80% or higher in post-release user feedback surveys regarding the contact tracking feature.

Biggest worry: Lack of clear definitions for user permissions and training might impede effective utilization of the new feature.

### Critic · confidence 40

Pre-mortem: A year after launch, a regional coordinator attempted to contact the designated primary contact for a country regarding an urgent project update but mistakenly reached out to the wrong person, as the primary contact information was outdated. This resulted in a significant delay in the project timeline and strained the relationship with that country’s government, causing confusion and mistrust.

Questions the request leaves open:
- Who is responsible for maintaining the accuracy and currency of the primary contact information?
- What happens to the primary contact designation when someone changes roles or leaves the organization?
- What safeguards are in place to ensure that sensitive diplomatic information is not incorrectly shared between users?
- How will the system prevent unauthorized users from accessing sensitive contact information?
- What criteria are used to determine who qualifies as a primary contact?
- How will changes to a primary contact's role or status be communicated to relevant stakeholders?

New challenges:

**C1** · BLOCKER · OWNERSHIP · targets S2
- Challenge: The proposal does not specify who is responsible for maintaining the accuracy and currency of the primary contact information, which is critical to avoid future miscommunication.
- Failure scenario: If a primary contact leaves and their information is not updated, a project manager might contact someone who is no longer in that role, leading to project delays and diplomatic issues.
- Resolution test: Who is responsible for updating and maintaining the accuracy of primary contact information?

**C2** · MAJOR · OWNERSHIP · targets GAP
- Challenge: There is no clear process outlined for how primary contact designations will be managed when an individual changes roles or leaves the organization.
- Failure scenario: A primary contact may change roles, but if their replacement is not promptly designated, users may continue to reach out to the old contact, disrupting workflows.
- Resolution test: What is the procedure for updating primary contact designations when personnel changes occur?

**C3** · MAJOR · CONFIDENTIALITY · targets D1
- Challenge: The criteria for determining who qualifies as a primary contact are not defined, risking the inclusion of individuals who should not have sensitive information accessible.
- Failure scenario: An individual who is not authorized to have access to sensitive engagement history may be designated as a primary contact, inadvertently leaking confidential information.
- Resolution test: What criteria are used to determine who qualifies as a primary contact?

**C4** · MAJOR · CONFIDENTIALITY · targets S5
- Challenge: There are no safeguards outlined to prevent unauthorized access to sensitive contact information, risking exposure of diplomatic information.
- Failure scenario: A regional coordinator might gain access to sensitive contact records that they are not authorized to view, leading to data breaches or diplomatic conflicts.
- Resolution test: What measures are in place to restrict access to sensitive contact information based on user roles?

**C5** · MINOR · COMPLIANCE · targets A3
- Challenge: The assumption regarding the organization's policy on confidentiality is vague and could lead to inconsistencies in how contacts are managed across the system.
- Failure scenario: If there are lapses in following the confidentiality policy, users may inadvertently share sensitive information without proper clearance, resulting in diplomatic repercussions.
- Resolution test: What specific policies are in place regarding confidentiality of sensitive contact information and how are they enforced?

**C6** · MINOR · DEFINITIONS · targets D2
- Challenge: The term 'engagement history' is not clearly defined in terms of what specific information it includes, which may lead to inconsistent data entry and expectations.
- Failure scenario: If different users interpret engagement history differently, some may record important interactions while others may leave out critical information, leading to incomplete records.
- Resolution test: What specific interactions and communications are included in the definition of 'engagement history'?

Biggest worry: Inadequate clarity on data ownership and procedures for managing primary contacts poses a serious risk of miscommunication and data breaches.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S2]: The edit specifies that regional coordinators and project managers are responsible for verifying and maintaining the accuracy of primary contact information, which directly addresses the challenge.
- **C2** REVISE (missing decision) [changed S2]: The revision clarifies the procedure for updating primary contact designations, ensuring that changes are documented promptly, mitigating the risk of outdated contact information.
- **C3** REVISE (missing decision) [changed D1]: The revised definition establishes criteria that restrict primary contact designation to individuals with relevant roles, helping to ensure that only authorized personnel have access to sensitive information.
- **C4** REVISE (missing decision) [changed S5]: This edit adds necessary safeguards by specifying that role-based access controls will be in place, which addresses the risk of unauthorized access to sensitive contact information.
- **C5** DEFEND (needs human decision): Organizational confidentiality policies and their enforcement are not under the purview of this proposal and must be defined by the organization.
- **C6** REVISE (missing decision) [changed D2]: This edit clarifies what constitutes engagement history, helping ensure consistency in data entry and expectations among users.

Proposal changes: edited S2, S5, D1, D2
- S2 now reads: Establish a database schema modification to include fields for 'primary contact' designation per country, with a defined process for updating primary contact designations immediately upon personnel changes, handled by regional coordinators.
- S5 now reads: Develop a user interface that highlights the primary contact whenever a country profile is viewed, incorporating role-based access controls to restrict views of sensitive engagement information based on user roles and responsibilities.
- D1 now reads: ‘primary contact’ means the designated individual in a member country responsible for communication regarding specific projects or engagements, who must hold a role within the organization that involves oversight or direct involvement with relevant projects.
- D2 now reads: 'engagement history' means a record of interactions, communications, and transactions with the contact related to the organization's projects, specifically including email correspondence, meeting notes, and project updates.

Biggest worry: Ensuring adherence to the established processes for maintaining contact information may be challenging within the organizational workflow.

### Critic · confidence 70 · CONTINUE

Rulings:
- **C1** ACCEPT: This clearly states who is responsible for maintaining the accuracy of primary contact information. Fact: Regional coordinators and project managers are responsible for updating primary contact information. Evidence: "...a defined process for updating primary contact designations immediately upon personnel changes, handled by regional coordinators."
- **C2** ACCEPT: The revision adequately specifies the procedure for managing primary contact designations after personnel changes. Fact: Changes to primary contact designations will be documented promptly by regional coordinators. Evidence: "...a defined process for updating primary contact designations immediately upon personnel changes, handled by regional coordinators."
- **C3** ACCEPT: The definition adequately restricts primary contact designation to authorized personnel. Fact: Only individuals with relevant roles can be designated as primary contacts. Evidence: "...who must hold a role within the organization that involves oversight or direct involvement with relevant projects."
- **C4** ACCEPT: The proposal now specifies safeguards to prevent unauthorized access to sensitive contact information. Fact: Role-based access controls will be implemented to protect sensitive information. Evidence: "...incorporating role-based access controls to restrict views of sensitive engagement information based on user roles and responsibilities."
- **C5** ESCALATE: This issue requires input from human decision-makers regarding organizational policies.
- **C6** ACCEPT: The definition is now clear and helps ensure consistent data entry. Fact: Engagement history includes specific types of records, such as email correspondence and meeting notes. Evidence: "...a record of interactions, communications, and transactions with the contact related to the organization's projects, specifically including email correspondence, meeting notes, and project updates."

New challenges:

**C7** · MAJOR · COMPLIANCE · targets A3
- Challenge: The lack of clarity around enforcement of confidentiality policies may lead to unintentional breaches of sensitive information.
- Failure scenario: If users continue to access sensitive contact information without awareness of clear enforcement mechanisms, the organization may face diplomatic fallout and loss of trust.
- Resolution test: What specific measures are in place to enforce confidentiality policies regarding sensitive contact information?

**C8** · MAJOR · DEFINITIONS · targets D1
- Challenge: While D1 defines 'primary contact', it does not clarify the process for reevaluating this status when project roles change or upon unsatisfactory performance.
- Failure scenario: If an ineffective primary contact remains designated without a process for reevaluation, important communications may be compromised, leading to project delays.
- Resolution test: What is the process for reviewing and potentially changing an individual's status as a primary contact?

Biggest worry: Without defined measures for enforcing confidentiality policies, there is a significant risk of data breaches.

**Ledger:** raised 8 · open 2 · resolved 5 · escalated 1 · disagreement 0.33 → **continue**

## Round 3

### Proposer · confidence 80

- **C7** DEFEND (needs human decision): The enforcement of confidentiality policies is an organizational matter that requires input from compliance and legal teams. The specifics of these measures are not our decision to make, so we should maintain this assumption until clarified.
- **C8** REVISE (missing decision) [changed D1]: The edit clarifies the reevaluation process for primary contacts when project roles or performance issues arise, ensuring better communication flow and accountability.

Proposal changes: edited D1
- D1 now reads: ‘primary contact’ means the designated individual in a member country responsible for communication regarding specific projects or engagements, who must hold a role within the organization that involves oversight or direct involvement with relevant projects. The process for reevaluating a primary contact's status includes an annual review by regional coordinators or upon notification of role changes, and these changes must be documented in the system to maintain transparency.

Biggest worry: The implementation of appropriate enforcement measures for confidentiality policies needs clarification to ensure compliance.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C7** ESCALATE: The specifics of confidentiality enforcement measures depend on external policies and the compliance/legal teams, leaving this unresolved.
- **C8** ACCEPT: This definition clarifies how primary contacts will be reevaluated, sufficiently addressing the concern. Fact: annual review by regional coordinators upon notification of role changes. Evidence: "The process for reevaluating a primary contact's status includes an annual review by regional coordinators or upon notification of role changes, and these changes must be documented in the system to maintain transparency."

Biggest worry: The proposal lacks a concrete mechanism for enforcing confidentiality, risking exposure to sensitive diplomatic information.

**Ledger:** raised 8 · open 0 · resolved 6 · escalated 2 · disagreement 0.20 → **converged**

## Final proposal

_This release delivers a contact tracking feature for regional coordinators and project managers to identify the primary contacts in each member country, ensuring that engagement history and roles are clearly documented, while incorporating a process for reevaluating primary contacts as needed. The feature will enhance the existing Government CRM system by enabling users to quickly locate and verify the appropriate contacts for each country based on their project involvement, with safeguards for maintaining data accuracy and confidentiality._

**Core commitments**
- V1: Enable tracking of primary contacts for each member country.
- V2: Provide engagement history linked to identified contacts.

**In scope**
- S1: Implement a searchable contact list feature that allows users to filter contacts by country, role, and project affiliation.
- S2: Establish a database schema modification to include fields for 'primary contact' designation per country, with a defined process for updating primary contact designations immediately upon personnel changes, handled by regional coordinators.
- S3: Ensure that engagement history is accessible for each contact displayed in the system.
- S4: Provide user training materials to regional coordinators and project managers on using the new contact tracking features.
- S5: Develop a user interface that highlights the primary contact whenever a country profile is viewed, incorporating role-based access controls to restrict views of sensitive engagement information based on user roles and responsibilities.

**Out of scope**
- X1: This release will not include automatic alerts or notifications for changes in contact roles.
- X2: This release will not incorporate direct integration with external databases or CRM systems.
- X3: This release will not change the underlying security protocols governing data access.

**Assumptions**
- A1: Users will have the necessary permissions to access and modify contact information based on their roles in the organization.
- A2: It is assumed that current user training on existing processes will be sufficient for using the new features.
- A3: The organization will maintain the policy of confidentiality regarding sensitive contact information.

**Definitions**
- D1: ‘primary contact’ means the designated individual in a member country responsible for communication regarding specific projects or engagements, who must hold a role within the organization that involves oversight or direct involvement with relevant projects. The process for reevaluating a primary contact's status includes an annual review by regional coordinators or upon notification of role changes, and these changes must be documented in the system to maintain transparency.
- D2: 'engagement history' means a record of interactions, communications, and transactions with the contact related to the organization's projects, specifically including email correspondence, meeting notes, and project updates.
- D3: 'searchable contact list' means a feature that allows users to filter and locate contacts based on specific criteria such as country, role, or project.

**Success criteria**
- K1: Achieve a user satisfaction score of 80% or higher in post-release user feedback surveys regarding the contact tracking feature.
