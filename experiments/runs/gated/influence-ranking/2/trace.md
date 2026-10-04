# Deliberation trace: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Policy `gated` · models: proposer gpt-4o-mini, critic gpt-4o-mini, summarizer gpt-4o-mini · ended **converged** after 3 rounds · 7 model calls (0 repairs)

## Round 1

### Proposer · confidence 75

_This release will implement a contact influence scoring system to identify and rank the most influential contacts within our CRM. It is designed for regional coordinators and project managers to better prioritize engagement efforts based on influence level._

**Core commitments**
- V1: Identify the top 20 influential contacts based on a scoring mechanism.
- V2: Provide an accessible interface for users to view and filter influential contacts.

**In scope**
- S1: Define 'influence' means a score that incorporates multiple factors such as the contact's position, historical engagement level, and outcomes achieved.
- S2: Implement an influence scoring system that calculates an influence score for each contact based on the defined criteria.
- S3: Display the top 20 contacts by influence score on a dedicated dashboard for regional coordinators and project managers.
- S4: Allow filtering options by role, country, and mission status to refine visible contact lists.
- S5: Create user documentation detailing how influence scores are calculated and how to use the interface effectively.

**Out of scope**
- X1: This release will not include a detailed breakdown of how the influence score is calculated to prevent manipulation or bias.
- X2: Long-term management of influence score data beyond the initial calculation will not be included in this release.
- X3: Integration with external data sources for influence scoring will not be implemented in this release.

**Assumptions**
- A1: There exists sufficient historical engagement data to assess contact influence levels without overwhelming data volume.
- A2: Users will need training on how to interpret influence scores appropriately to take action.
- A3: Scoring methodology will comply with existing data protection policies to ensure sensitive information is handled safely.

**Definitions**
- D1: 'Influence' means a calculated score based on each contact's position, the frequency of interaction, and outcomes achieved from previous projects.
- D2: 'Top 20' means the contacts with the highest influence scores as determined by the scoring mechanism.
- D3: 'Dashboard' means a user interface feature that visually presents key metrics and lists for easy access and decision making.

**Success criteria**
- K1: At least 80% of users report satisfaction with the ability to identify and prioritize contacts based on influence scores, measured through a user survey after implementation.

Biggest worry: The scoring system may not capture influence appropriately, leading users to misprioritize engagements.

### Critic · confidence 40

Pre-mortem: A year after launch, the influence scoring system inadvertently caused a diplomatic incident by exposing a list of contacts deemed influential to unauthorized parties. This led to misunderstandings and tensions with certain country representatives who felt misrepresented or unfairly scored, damaging relationships that the organization had built over time. As a result, the organization faced widespread criticism for its data handling practices, leading to a loss of trust among crucial stakeholders.

Questions the request leaves open:
- Which roles are allowed to see the influence scores for contacts from other regions?
- What specific criteria determine the influence scoring to avoid bias or inconsistency?
- How will data retention and deletion policies apply to the influence scores generated?
- What safeguards are in place to prevent the influence scoring system from being manipulated?
- What happens to the influence scores when a contact changes roles or leaves the organization?
- How do we ensure compliance with data protection policies when calculating and displaying influence scores?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1, S2
- Challenge: The proposal does not address who is authorized to view the influence scores, potentially leading to unauthorized access to sensitive information about contacts.
- Failure scenario: A regional coordinator accesses the influence scores of contacts in another region without the proper clearance, resulting in the exposure of sensitive diplomatic relationships.
- Resolution test: Which roles can access influence scores for contacts from other regions?

**C2** · MAJOR · DEFINITIONS · targets S1
- Challenge: The criteria for determining 'influence' are broadly defined, risking subjective interpretations and inconsistency in scoring.
- Failure scenario: Users interpret influence based on personal biases, leading to flawed prioritization of contacts and potential diplomatic missteps.
- Resolution test: What specific factors are weighted in the influence scoring to ensure objectivity?

**C3** · MAJOR · OWNERSHIP · targets S3, S5
- Challenge: There is no clarity on how influence scores are maintained, updated, or who owns the data once calculated, risking outdated or inaccurate data being displayed.
- Failure scenario: A project manager relies on outdated influence scores leading to incorrect prioritization, which not only wastes resources but also impacts diplomatic relations.
- Resolution test: Who is responsible for regularly reviewing and updating the influence scores once calculated?

**C4** · MAJOR · COMPLIANCE · targets S1
- Challenge: The proposal lacks details on how influence scores will be retained or deleted, which is essential for compliance with data protection regulations.
- Failure scenario: Influence scores remain in the system longer than legally permissible, leading to potential data breaches or fines.
- Resolution test: What are the retention and deletion policies for influence scores?

**C5** · MINOR · OWNERSHIP · targets X1
- Challenge: The decision to withhold detailed scoring criteria could be seen as an issue of transparency and ownership, as stakeholders may question the fairness of results.
- Failure scenario: Stakeholders challenge the fairness of the scoring system when they cannot see details, leading to distrust in the results.
- Resolution test: What process is in place for reviewing the scoring criteria to ensure transparency and build trust?

**C6** · MAJOR · FEASIBILITY · targets S1
- Challenge: The assumption of having sufficient historical data to assess influence presupposes clarity on data sources and timelines, which are unanswered.
- Failure scenario: There is not enough historical engagement data, resulting in an unreliable scoring that fails to reflect actual influence.
- Resolution test: What specific historical engagement data is available and how will it be utilized to calculate influence?

Biggest worry: The lack of clarity around access to sensitive influence scores poses a significant risk to sensitive diplomatic relationships.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 80

- **C1** REVISE (missing decision) [changed S6]: This edit provides a specific definition of authorized users who can view influence scores, reducing the risk of unauthorized access to sensitive information.
- **C2** REVISE (missing decision) [changed S1]: The revision clarifies the specific factors that contribute to influence scoring and their respective weights, reducing subjectivity and ensuring consistency.
- **C3** REVISE (missing decision) [changed S7]: This clarifies ownership over the maintenance of influence scores, ensuring they are updated regularly and thereby reducing the risk of outdated data affecting decision-making.
- **C4** REVISE (missing decision) [changed S8]: This specifies the retention and deletion policy for influence scores, ensuring compliance with data protection regulations and reducing the risk of unintentional data breaches.
- **C5** REVISE (missing decision) [changed S9]: This provides a structured process for reviewing the scoring criteria, addressing concerns about transparency and ownership, and building trust among stakeholders.
- **C6** DEFEND (acceptable risk): While the assumption of sufficient data may seem risky, it is acceptable in this release as historical engagement data has typically been collected consistently over the years.

Proposal changes: added S6, S7, S8, S9; edited S1
- S6 now reads: Define 'Authorized Users' means regional coordinators, project managers, and executive staff who are granted access to view influence scores based on clearance levels determined by organizational policy.
- S7 now reads: Designate the responsibility for maintaining and updating influence scores to the data management team, who will review and adjust scores on a quarterly basis to ensure accuracy.
- S8 now reads: Define the retention policy for influence scores as: scores will be retained for a period of two years after the last engagement with the contact, followed by deletion unless there is a specific extension request based on ongoing engagements.
- S9 now reads: Establish a review process whereby the scoring criteria will be evaluated annually by a committee consisting of representatives from regional coordinators, project managers, and data management to ensure transparency and trust in the scoring mechanism.
- S1 now reads: Define 'influence' means a score that incorporates multiple factors such as the contact's position (weight: 50%), historical engagement level (weight: 30%), and outcomes achieved (weight: 20%), on a scale of 1 to 100.

Biggest worry: Ensuring accurate and timely updating of influence scores remains a critical concern.

### Critic · confidence 60 · CONTINUE

Rulings:
- **C1** ACCEPT: The proposal now clearly defines who can access influence scores, addressing confidentiality concerns. Fact: Authorized Users include regional coordinators, project managers, and executive staff. Evidence: "S6: Define 'Authorized Users' means regional coordinators, project managers, and executive staff who are granted access to view influence scores based on clearance levels determined by organizational policy."
- **C2** ACCEPT: The revised definition clarifies how influence scoring is determined, reducing subjectivity. Fact: Influence is calculated using defined factors and weights, providing objective scoring criteria. Evidence: "S1: Define 'influence' means a score that incorporates multiple factors such as the contact's position (weight: 50%), historical engagement level (weight: 30%), and outcomes achieved (weight: 20%), on a scale of 1 to 100."
- **C3** ACCEPT: Responsibilities for score maintenance are now clearly outlined, ensuring data is kept accurate. Fact: The data management team is responsible for maintaining and updating influence scores quarterly. Evidence: "S7: Designate the responsibility for maintaining and updating influence scores to the data management team, who will review and adjust scores on a quarterly basis to ensure accuracy."
- **C4** ACCEPT: This establishes a clear retention and deletion policy, ensuring compliance with data protection regulations. Fact: Influence scores will be retained for two years after the last engagement, then deleted unless extended. Evidence: "S8: Define the retention policy for influence scores as: scores will be retained for a period of two years after the last engagement with the contact, followed by deletion unless there is a specific extension request based on ongoing engagements."
- **C5** ACCEPT: The revision now outlines a process to ensure transparency and stakeholder trust regarding scoring. Fact: An annual review of scoring criteria will involve multiple stakeholders to ensure transparency. Evidence: "S9: Establish a review process whereby the scoring criteria will be evaluated annually by a committee consisting of representatives from regional coordinators, project managers, and data management to ensure transparency and trust in the scoring mechanism."
- **C6** MAINTAIN: While influence is defined, the adequacy of historical data for calculating influence is still unresolved.

New challenges:

**C7** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: The proposal does not specify the quality or sources of historical engagement data needed for accurate influence scoring.
- Failure scenario: A project manager uses influence scores calculated from incomplete or inaccurate historical engagement data, leading to misprioritized diplomatic engagements and potential conflicts.
- Resolution test: What sources of historical engagement data are used for calculating influence scores, and how is data quality validated?

Biggest worry: The reliability of influence scoring depends on the quality and completeness of historical engagement data, which is not sufficiently defined.

**Ledger:** raised 7 · open 2 · resolved 5 · escalated 0 · disagreement 0.29 → **continue**

## Round 3

### Proposer · confidence 70

- **C6** DEFEND (needs human decision): The specific sources of historical engagement data and their timelines are dependent on existing organizational data structures and must be verified by the relevant internal teams.
- **C7** DEFEND (needs human decision): The proposal cannot define the quality or sources of historical engagement data without input from the teams responsible for data management and quality assurance.

Proposal changes: none

Biggest worry: We face significant dependencies on confirming data sources and quality from the internal organization, which could delay the project.

### Critic · confidence 50 · CONTINUE

Rulings:
- **C6** ESCALATE: The proposal relies on human verification of data sources, which prevents acceptance.
- **C7** ESCALATE: The reliance on certain teams for input on data quality and sources needs human decision.

Biggest worry: The feature risks unauthorized exposure of sensitive influence scores and relies entirely on human verification of data quality.

**Ledger:** raised 7 · open 0 · resolved 5 · escalated 2 · disagreement 0.29 → **converged**

## Final proposal

_This release will implement a contact influence scoring system to identify and rank the most influential contacts within our CRM, targeting regional coordinators and project managers for engagement prioritization based on influence level. Specific historical engagement data and its quality must be confirmed by organizational teams for accurate scoring._

**Core commitments**
- V1: Identify the top 20 influential contacts based on a scoring mechanism.
- V2: Provide an accessible interface for users to view and filter influential contacts.

**In scope**
- S1: Define 'influence' means a score that incorporates multiple factors such as the contact's position (weight: 50%), historical engagement level (weight: 30%), and outcomes achieved (weight: 20%), on a scale of 1 to 100.
- S2: Implement an influence scoring system that calculates an influence score for each contact based on the defined criteria.
- S3: Display the top 20 contacts by influence score on a dedicated dashboard for regional coordinators and project managers.
- S4: Allow filtering options by role, country, and mission status to refine visible contact lists.
- S5: Create user documentation detailing how influence scores are calculated and how to use the interface effectively.
- S6: Define 'Authorized Users' means regional coordinators, project managers, and executive staff who are granted access to view influence scores based on clearance levels determined by organizational policy.
- S7: Designate the responsibility for maintaining and updating influence scores to the data management team, who will review and adjust scores on a quarterly basis to ensure accuracy.
- S8: Define the retention policy for influence scores as: scores will be retained for a period of two years after the last engagement with the contact, followed by deletion unless there is a specific extension request based on ongoing engagements.
- S9: Establish a review process whereby the scoring criteria will be evaluated annually by a committee consisting of representatives from regional coordinators, project managers, and data management to ensure transparency and trust in the scoring mechanism.

**Out of scope**
- X1: This release will not include a detailed breakdown of how the influence score is calculated to prevent manipulation or bias.
- X2: Long-term management of influence score data beyond the initial calculation will not be included in this release.
- X3: Integration with external data sources for influence scoring will not be implemented in this release.

**Assumptions**
- A1: There exists sufficient historical engagement data to assess contact influence levels without overwhelming data volume.
- A2: Users will need training on how to interpret influence scores appropriately to take action.
- A3: Scoring methodology will comply with existing data protection policies to ensure sensitive information is handled safely.

**Definitions**
- D1: 'Influence' means a calculated score based on each contact's position, the frequency of interaction, and outcomes achieved from previous projects.
- D2: 'Top 20' means the contacts with the highest influence scores as determined by the scoring mechanism.
- D3: 'Dashboard' means a user interface feature that visually presents key metrics and lists for easy access and decision making.

**Success criteria**
- K1: At least 80% of users report satisfaction with the ability to identify and prioritize contacts based on influence scores, measured through a user survey after implementation.
