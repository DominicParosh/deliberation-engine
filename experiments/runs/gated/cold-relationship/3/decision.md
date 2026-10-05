# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 3 rounds (policy `gated`) · $0.009.

Challenges: 8 raised · 7 settled between the agents · 1 handed to humans · 0 still open when it ended.

## Summary

This release will implement an alert system that notifies users when engagement with country contacts remains inactive for a specified duration. The system will not include suggestions for relationship-building or integration with external systems at this time. Decision-makers will still need to contend with operational concerns regarding alert management and the risk of alert fatigue as development proceeds.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Implement an alert system for detecting inactive relationships with country contacts.

**In scope**

- **S1** Define 'cold relationship' as a lack of recorded engagement activities for 90 consecutive days, with an additional requirement that alerts are sent only to users who have authorization to view information regarding that country.  
  The definition of 'cold relationship' was clarified to specifically require inactivity for 90 consecutive days, addressing confidentiality concerns regarding alert distribution. _(C1)_
- **S2** Allow users to receive alerts via email regarding cold relationships, with protocols in place ensuring that alerts regarding diplomatic contacts are sent exclusively to users with the 'diplomatic_security' role in the CRM, who have clearance to handle sensitive information.  
  Protocols for sending alerts concerning sensitive diplomatic contacts were established to ensure only authorized personnel receive them, addressing confidentiality issues. _(C4)_
- **S3** Enable users to filter and view a list of contacts with cold relationships in the CRM.
- **S4** Provide options for users to set customized thresholds for inactivity alerts, ranging from 30 to 120 days, with the stipulation that valid engagement activities must include documented interactions such as meetings, emails, or official communications logged in the CRM, which will be reviewed monthly for accuracy by the CRM administrator.  
  The threshold for engagement activities needed for alerts was specified clearly to mitigate the risk of users setting inappropriate custom values. _(C2)_
- **S5** Assign the responsibility for maintaining the alert system, monitoring engagement logs, and adjusting user preferences to the CRM administrator role, who will work with regional coordinators to filter and prioritize alerts based on urgency.  
  The responsibility for maintaining the alert system is assigned to the CRM administrator to ensure accountability and effective oversight. _(C3)_

## What it will not do

**Out of scope for this release**

- **X1** This release will not include relationship-building suggestions based on contacts' engagement history.
- **X2** This release will not integrate with external systems for engagement history tracking.

**Rejected during deliberation**

- Nothing was dropped.
- Declined **C6** (MINOR · DATA_QUALITY): What processes will be implemented to ensure engagement activities logged in the CRM are accurate and up to date? The Proposer's answer, which the Critic accepted: While reliance on user accountability is a risk, dialogue with stakeholders post-release will establish a basis for refining data accuracy measures based on user experience.

## Assumptions

| ID | Assumption | Status | Challenges |
|---|---|---|---|
| A1 | Users have sufficient privileges to set alert preferences and view engagement history; this depends on existing user role management capabilities. | Kept | never challenged |
| A2 | Engagement activities are logged in the CRM; this depends on current CRM functionality for tracking such activities. | Kept | never challenged |
| A3 | Users understand what constitutes a "cold relationship" based on the defined thresholds; this assumes adequate training and documentation is provided. | Kept | never challenged |

## Definitions

- **D1** "cold relationship" means a lack of recorded engagement activities with a country contact for 90 consecutive days.
- **D2** "engagement activities" means any logged interaction or correspondence with a country contact, such as meetings, emails, or calls.

## Success criteria

- **K1** Achieve at least a 75% user satisfaction rate with the new alert system, measured through user surveys within one month of release.

## Open questions for humans

### C5 · MINOR · does not block the build

**What strategies will be implemented to manage the potential for alert fatigue arising from numerous cold relationship notifications?**

- Why it matters: Identifying ways to effectively manage alert volume is crucial to ensure that important alerts aren't overlooked.
- Decision owner: Product Owner
- Options: Establish stricter thresholds for alerts / Offer more granular alert customization options / Incorporate monitoring tools for alert frequency
- Proposer's last word (R3, defend, acceptable risk): The risk of alert fatigue is acknowledged but managed with customization options for alerts, enabling users to filter out less relevant notifications.
- Critic's last word (R3, maintain): While there is user customization, the concern of alert fatigue remains significant and was not fully mitigated.

## Tension report

The primary disagreement centered around managing potential alert fatigue and ensuring the effectiveness of the notifications. While the Proposer believes user customization options may be sufficient, the Critic insists that the risk of irrelevant alerts overwhelms significant notifications, leaving this concern unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 6 | 6 | 0 | 0 | 1.00 | 75 | 30 | - | continue |
| 2 | 8 | 5 | 3 | 0 | 0.53 | 80 | 60 | CONTINUE | continue |
| 3 | 8 | 0 | 7 | 1 | 0.07 | 75 | 70 | CONTINUE | converged |

- Proposer's remaining worry (75/100): The potential for inaccurate logging of engagement activities leading to premature alerts still remains a concern.
- Critic's remaining worry (70/100): The risk of alert fatigue remains significant, as user customization alone may not be sufficient to prevent irrelevant alerts from overwhelming important notifications.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | BLOCKER | CONFIDENTIALITY | S1 | R1 | REVISED | 0 | The definition of 'cold relationship' does not address the risk of exposing sensitive diplomatic contacts to the wrong individuals if the alert system triggers inaccurately. |
| C2 | MAJOR | DEFINITIONS | S4 | R1 | REVISED | 0 | The thresholds for engagement inactivity alerts are vague regarding what constitutes valid engagement activities and may become untestable depending on user behavior. |
| C3 | MAJOR | OWNERSHIP | GAP | R1 | REVISED | 0 | The proposal does not clarify ownership of the alert system or the responsibility for managing engagement activity logging or oversight of alerts. |
| C4 | MAJOR | CONFIDENTIALITY | S2 | R1 | REVISED | 1 | The proposal does not define how alerts are handled with respect to sensitive contacts, risking inappropriate disclosures. |
| C5 | MINOR | OPERATIONS | GAP | R1 | ESCALATED | 2 | The proposal lacks insight into the operational workload required to manage alerts, including potential for false positives and alert fatigue. |
| C6 | MINOR | DATA_QUALITY | GAP | R1 | DEFENDED | 1 | There is a lack of clarity on the accuracy and freshness of the engagement activities tracked, which can affect the reliability of the alert system. |
| C7 | MAJOR | OPERATIONS | GAP | R2 | REVISED | 0 | The proposal lacks detailed measures to manage the volume of alerts effectively, which could overwhelm users and affect critical alert visibility. |
| C8 | MAJOR | DATA_QUALITY | GAP | R2 | REVISED | 0 | The reliance on existing logging practices and user accountability for maintaining accurate engagement records poses significant risks to the integrity of the alert system. |
