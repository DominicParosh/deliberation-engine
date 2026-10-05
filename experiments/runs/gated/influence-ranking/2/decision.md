# Decision record: influence-ranking

> We should know which of our contacts are most influential so we can prioritize them.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.006.

Challenges: 7 raised · 5 settled between the agents · 2 handed to humans · 0 still open when it ended.

## Summary

This release will implement a contact influence scoring system that identifies and ranks the top 20 influential contacts within the CRM to aid regional coordinators and project managers in engagement prioritization. However, the proposal will not include a detailed breakdown of how influence scores are calculated or integration with external data sources at this time. Users must confirm specific historical engagement data to ensure accurate scoring, which remains a point of uncertainty.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Identify the top 20 influential contacts based on a scoring mechanism.
- **V2** Provide an accessible interface for users to view and filter influential contacts.

**In scope**

- **S1** Define 'influence' means a score that incorporates multiple factors such as the contact's position (weight: 50%), historical engagement level (weight: 30%), and outcomes achieved (weight: 20%), on a scale of 1 to 100.  
  The definition of 'influence' has been clarified to ensure objectivity and consistency in scoring across users. _(C2)_
- **S2** Implement an influence scoring system that calculates an influence score for each contact based on the defined criteria.  
  The influence scoring system will calculate scores based on defined criteria, ensuring proper prioritization of contacts. _(C2)_
- **S3** Display the top 20 contacts by influence score on a dedicated dashboard for regional coordinators and project managers.  
  The display of the top 20 contacts by influence score in a dashboard allows for easy access by key users.
- **S4** Allow filtering options by role, country, and mission status to refine visible contact lists.
- **S5** Create user documentation detailing how influence scores are calculated and how to use the interface effectively.  
  User documentation will be crucial for instructing users on how to interpret and utilize influence scores correctly.
- **S6** Define 'Authorized Users' means regional coordinators, project managers, and executive staff who are granted access to view influence scores based on clearance levels determined by organizational policy.  
  Defining 'Authorized Users' clarifies who can access influence scores, mitigating confidentiality risks. _(C1)_
- **S7** Designate the responsibility for maintaining and updating influence scores to the data management team, who will review and adjust scores on a quarterly basis to ensure accuracy.  
  The data management team is responsible for maintaining influence scores, ensuring they are updated regularly. _(C3)_
- **S8** Define the retention policy for influence scores as: scores will be retained for a period of two years after the last engagement with the contact, followed by deletion unless there is a specific extension request based on ongoing engagements.  
  The retention policy for influence scores has been established to comply with data protection regulations. _(C4)_
- **S9** Establish a review process whereby the scoring criteria will be evaluated annually by a committee consisting of representatives from regional coordinators, project managers, and data management to ensure transparency and trust in the scoring mechanism.  
  An annual review process for scoring criteria has been set to improve transparency and trust in the system. _(C5)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include a detailed breakdown of how the influence score is calculated to prevent manipulation or bias.  
  Excluding a detailed breakdown of how influence scores are calculated was decided to prevent potential manipulation.
- **X2** Long-term management of influence score data beyond the initial calculation will not be included in this release.
- **X3** Integration with external data sources for influence scoring will not be implemented in this release.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | There exists sufficient historical engagement data to assess contact influence levels without overwhelming data volume. | Kept | never challenged |
| A2 | Users will need training on how to interpret influence scores appropriately to take action. | Kept | never challenged |
| A3 | Scoring methodology will comply with existing data protection policies to ensure sensitive information is handled safely. | Kept | never challenged |

## Definitions

- **D1** 'Influence' means a calculated score based on each contact's position, the frequency of interaction, and outcomes achieved from previous projects.
- **D2** 'Top 20' means the contacts with the highest influence scores as determined by the scoring mechanism.
- **D3** 'Dashboard' means a user interface feature that visually presents key metrics and lists for easy access and decision making.

## Success criteria

- **K1** At least 80% of users report satisfaction with the ability to identify and prioritize contacts based on influence scores, measured through a user survey after implementation.

## Open questions for humans

### C6 · MAJOR · blocks the build

**What specific historical engagement data is available, and how will it be used to calculate influence scores?**

- Why it matters: Clarity on available data sources is critical to ensure the accuracy and reliability of influence scoring.
- Decision owner: Data Management Team
- Options: Confirm available historical data sources / Proceed with assumptions on historical data usage
- Proposer's last word (R3, defend, needs human decision): The specific sources of historical engagement data and their timelines are dependent on existing organizational data structures and must be verified by the relevant internal teams.
- Critic's last word (R3, escalate): The proposal relies on human verification of data sources, which prevents acceptance.

### C7 · MAJOR · blocks the build

**What sources of historical engagement data are used for calculating influence scores, and how is data quality validated?**

- Why it matters: Establishing the sources and quality of data is essential to ensure influence scores reflect actual contact influence accurately.
- Decision owner: Data Quality Assurance Team
- Options: Define data sources and establish quality assurance processes / Accept scoring with current unknown data sources
- Proposer's last word (R3, defend, needs human decision): The proposal cannot define the quality or sources of historical engagement data without input from the teams responsible for data management and quality assurance.
- Critic's last word (R3, escalate): The reliance on certain teams for input on data quality and sources needs human decision.

## Tension report

The primary disagreement revolved around the potential risks to data quality and unauthorized access to sensitive information. While the proposer argued for proceeding with the current assumption of available data, the critic maintained concerns about verification processes, leading to unresolved issues that could delay the project.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 7 | 2 | 5 | 0 | 0.29 | 80 | 60 | CONTINUE | continue |
| 3 | 7 | 0 | 5 | 2 | 0.29 | 70 | 50 | CONTINUE | converged |

- Proposer's remaining worry (70/100): We face significant dependencies on confirming data sources and quality from the internal organization, which could delay the project.
- Critic's remaining worry (50/100): The feature risks unauthorized exposure of sensitive influence scores and relies entirely on human verification of data quality.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1, S2 | R1 | REVISED | 0 | The proposal does not address who is authorized to view the influence scores, potentially leading to unauthorized access to sensitive information about contacts. |
| C2 | MAJOR | DEFINITIONS | S1 | R1 | REVISED | 0 | The criteria for determining 'influence' are broadly defined, risking subjective interpretations and inconsistency in scoring. |
| C3 | MAJOR | OWNERSHIP | S3, S5 | R1 | REVISED | 0 | There is no clarity on how influence scores are maintained, updated, or who owns the data once calculated, risking outdated or inaccurate data being displayed. |
| C4 | MAJOR | COMPLIANCE | S1 | R1 | REVISED | 0 | The proposal lacks details on how influence scores will be retained or deleted, which is essential for compliance with data protection regulations. |
| C5 | MINOR | OWNERSHIP | X1 | R1 | REVISED | 0 | The decision to withhold detailed scoring criteria could be seen as an issue of transparency and ownership, as stakeholders may question the fairness of results. |
| C6 | MAJOR | FEASIBILITY | S1 | R1 | ESCALATED | 1 | The assumption of having sufficient historical data to assess influence presupposes clarity on data sources and timelines, which are unanswered. |
| C7 | MAJOR | DATA_QUALITY | GAP | R2 | ESCALATED | 0 | The proposal does not specify the quality or sources of historical engagement data needed for accurate influence scoring. |
