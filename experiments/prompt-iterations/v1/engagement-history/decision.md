# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 2 rounds (policy `gated`) · $0.004.

## Summary

This release will enable project managers to access the full engagement history for each country, enhancing decision-making before initiating new missions. Changes include the development of a user-friendly interface to present engagement records, filters to sort history, and access controls to safeguard sensitive data. However, humans still need to ensure that the access control mechanism effectively protects sensitive information while providing necessary access to project managers.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Enable project managers to access the full engagement history for each country.  
  Core commitment to allow project managers access to complete engagement history ensures informed mission planning. _(C1, C2)_
- **V2** Enhance decision-making by providing historical context for mission planning.  
  Enhancing decision-making by providing historical context is vital for successful mission planning. _(C2)_

**In scope**

- **S1** Develop a user interface in the Government CRM for project managers to select a country.  
  In-scope to develop a user interface for project managers aligns with the need for easy access to information.
- **S2** Retrieve and display engagement history for the selected country, including all past missions and communications. This will include details on record owners who are responsible for maintaining the engagement logs.  
  Inclusion of ownership structure for maintaining engagement records ensures accuracy and currency of information. _(C3)_
- **S3** Ensure that the displayed information includes a timeline of engagements, project details, and relevant communication notes.  
  Displaying a timeline of engagements provides clarity and context for project managers.
- **S4** Enable filters to sort engagement history by date, type of engagement (e.g., meeting, email), and project affiliation.  
  Filters for sorting engagement history are included to enhance the usability of the feature.
- **S5** Implement user access controls to ensure that only authorized personnel, defined as those with appropriate clearance levels (e.g., diplomatic, security), can view sensitive engagement information.  
  Access controls ensure that sensitive information is protected and only accessible to authorized personnel, addressing confidentiality issues. _(C1)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include edits or deletions of engagement records.  
  Edits or deletions of engagement records were deemed unnecessary for this release’s goals.
- **X2** This release does not involve changes to the existing data structure or database schema.  
  Changes to the existing data structure were outside the scope to keep the implementation straightforward.
- **X3** This release will not include integration with external data sources for additional insights.  
  Integration with external data sources was not included to focus on existing data capabilities.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Project managers will have access to the Government CRM system and the required permissions to view engagement histories. | The request implies that project managers are users of the system. | Accepted (never challenged) |
| A2 | The existing data infrastructure can support querying historical engagement records without extensive redesign. | The feature relies on the availability of prior engagement data. | Accepted (never challenged) |
| A3 | The organization intends to maintain confidentiality over sensitive engagement data while allowing project managers access to pertinent historical information. | Access controls are necessary to manage sensitive data according to regulations. | Accepted (never challenged) |

## Definitions

- **D1** "full history of engagement": All records of interactions between the organization and the country's representatives, including meetings, correspondence, and project updates, displayed in chronological order. This includes informal communications when directly relevant to mission planning.
- **D2** "engagement history": A complete list comprising all past missions, communications, and outcomes associated with a specific country, including relevant informal interactions.
- **D3** "project managers": Designated personnel responsible for overseeing and managing missions and projects within the government CRM system.

## Success criteria

- **K1** Percentage of project managers engaging with the feature: target 80% (Measured by tracking the unique number of project managers who access the engagement history feature at least once and the frequency of their access within the first month of deployment.)

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main tension arose around the implementation of the access control mechanism and how to effectively protect sensitive data while allowing necessary access for project managers. Both the proposer and critic expressed concerns over the final details ensuring data confidentiality, highlighting the need for clarity and robustness in the implementation.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 0 | 0 | 1.00 | 75 | 40 | - | continue |
| 2 | 4 | 0 | 4 | 0 | 0.00 | 80 | 85 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring the updated access control mechanism effectively protects sensitive data while allowing necessary access for project managers.
- Critic's remaining worry (85/100): There could still be ambiguity in the user access controls affecting sensitive data protection.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S5 | R1 | REVISED | 0 | The access control implementation needs explicit details on how sensitive information will be protected and who qualifies as 'authorized personnel.' |
| C2 | MAJOR | DEFINITIONS | D1, D2 | R1 | REVISED | 0 | The definitions of 'full history of engagement' and 'engagement history' lack clarity on the criteria for what records are included or excluded. |
| C3 | MAJOR | OWNERSHIP | S2 | R1 | REVISED | 0 | There should be clarity on who maintains the engagement history records, especially regarding the accuracy and updates of these records over time. |
| C4 | MINOR | DEFINITIONS | K1 | R1 | REVISED | 0 | The success criteria defined in K1 regarding user engagement does not specify how 'engagement' is measured in a quantifiable way. |
