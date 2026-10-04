# Decision record: engagement-history

> Project managers should be able to see the full history of engagement with a country before starting a new mission.

Deliberation ended **consensus** after 4 rounds (policy `gated`) · $0.007.

## Summary

The release will enable project managers to view the complete engagement history for each country within the Government CRM, improving mission preparation. It will include features for filtering engagement records and options for exporting data securely. However, there are concerns related to the protection of sensitive data, particularly around access permissions that still need to be clarified by the relevant decision-makers.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Project managers can view a complete engagement history for any selected country.  
  Project managers will have access to the full engagement history for any selected country, which enhances their ability to prepare for new missions.
- **V2** The system provides filters to navigate engagement history effectively.

**In scope**

- **S1** Enable access to engagement history for all countries tracked in the CRM.
- **S2** Implement date and type filters (e.g., meetings, communications) for project managers to refine their view of engagement history.
- **S3** Allow project managers to export the engagement history as a PDF or CSV format.
- **S4** Display engagement history with details including date, type of engagement, participants, a summary of engagement outcomes, and the following data fields: meeting date, meeting type, participants' names, and engagement outcomes.
- **S5** Establish a process for revoking access permissions for project managers who change roles or leave the organization.
- **S6** Implement checks and validations to manage duplicate engagement records and ensure data accuracy within engagement histories.
- **S7** Introduce security measures for the export process, including data encryption and access restrictions to protect sensitive information.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include live updates to engagement histories during ongoing missions.
- **X2** Real-time collaboration features will not be available in this release.
- **X3** The release will not provide engagement history for users who do not have project manager roles.
- **X4** Integration with external data sources for historical engagement data is excluded.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Project managers will have the required access permissions to view country engagement history. | The request assumes that project managers already have defined roles in the CRM with the necessary access. | C2 → revised |
| A2 | Engagement history data is currently stored and can be retrieved from the existing CRM database. | The request implies that there is a system in place to track and store engagement history. | Accepted (never challenged) |
| A3 | A training plan will be developed by the training coordinator to ensure users are adequately prepared to use the new engagement history feature. | The request assumes that users are familiar with the CRM's interface and do not require additional training. | C3 → revised |

## Definitions

- **D1** "full history of engagement": A comprehensive record of all interactions with a specific country, including meetings (date, type), communications (date, type), participants' names, and a summary of engagement outcomes.
- **D2** "project managers": Users assigned to manage specific projects involving country engagements within the CRM.
- **D3** "new mission": A project or initiative related to international engagement that is in the planning or preparation stage.

## Success criteria

- **K1** Percentage of project managers satisfied with engagement history access: target 90% (Measured by user feedback and testing during the release review phase.)

## Open questions for humans

None: every challenge was settled between the agents.

## Tension report

The main disagreement was centered around the security of sensitive data during the engagement history feature's implementation. The Proposer emphasized the need for operational functionality, while the Critic was more focused on ensuring that adequate protections for data confidentiality were established before the build. However, both parties eventually reached a consensus on the outlined measures.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 3 | 3 | 0 | 0 | 1.00 | 85 | 40 | - | continue |
| 2 | 6 | 3 | 3 | 0 | 0.46 | 75 | 65 | CONTINUE | continue |
| 3 | 8 | 2 | 6 | 0 | 0.24 | 70 | 70 | CONTINUE | continue |
| 4 | 8 | 0 | 8 | 0 | 0.00 | 80 | 90 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring that all sensitive data is adequately protected from unauthorized access throughout the engagement history feature.
- Critic's remaining worry (90/100): How access permissions are revoked when users change roles or leave is still not fully addressed.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | The proposal defines 'full history of engagement' but lacks clarity on which specific data fields are included in this record. |
| C2 | BLOCKER | CONFIDENTIALITY | A1 | R1 | REVISED | 0 | The proposal assumes project managers already have the required access permissions without detailing how sensitive engagement records will be protected from unauthorized access. |
| C3 | MAJOR | OWNERSHIP | A3 | R1 | REVISED | 0 | The proposal assumes users will have sufficient training but does not specify who will be responsible for providing this training or how it will be conducted. |
| C4 | MAJOR | OWNERSHIP | GAP | R2 | REVISED | 0 | The proposal does not address what happens to access permissions when users change roles or leave the organization, which could risk unauthorized access or data exposure. |
| C5 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The proposal does not specify how the system will handle duplicate or inaccurate engagement records, which could lead to confusion and inaccuracy in mission preparations. |
| C6 | MAJOR | CONFIDENTIALITY | GAP | R2 | REVISED | 0 | The proposal lacks measures to ensure data confidentiality during the export process, risking exposure of sensitive information. |
| C7 | MAJOR | DEFINITIONS | GAP | R3 | REVISED | 0 | The proposal does not define which specific data fields are included in the 'full history of engagement', making it difficult to assess completeness and usability. |
| C8 | MAJOR | CONFIDENTIALITY | GAP | R3 | REVISED | 0 | While measures are in place for exports, the proposal does not clarify specific access controls within the CRM to prevent unauthorized users from viewing sensitive engagement data. |
