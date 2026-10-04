# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **converged** after 6 rounds (policy `gated`) · $0.015.

## Summary

This release will implement an alerting feature that notifies users when engagement activity with a country representative goes cold, allowing for custom thresholds of inactivity between 30 and 180 days. However, the proposal does not include processes for tracking communications outside of the CRM, nor does it address how to re-engage with cold relationships. Key organizational decisions regarding user access protocols must still be made to ensure sensitive information is protected.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Provide alerts to users when engagement with a country representative has not occurred for a predefined period.  
  Provides alerts when engagement has not occurred for a specified period, ensuring users are informed about relationship status.
- **V2** Enable users to configure what constitutes a 'cold' relationship based on the duration of inactivity.  
  Allows users to define what constitutes a cold relationship, ensuring alerts are tailored to individual situations.

**In scope**

- **S1** Implement an alert that triggers if there has been no recorded communication with a country representative for a user-defined period between 30 and 180 days, visible only to authorized users.  
  Specifies that only authorized users will see alerts to maintain confidentiality and prevent unauthorized information exposure. _(C1)_
- **S2** Create a user interface setting that allows regional coordinators and project managers to customize the inactivity threshold from 30 to 180 days.  
  Enables customization of inactivity thresholds, accommodating different engagement needs across user roles.
- **S3** Include an email notification feature that informs users of a cold relationship when triggered.  
  Includes an email notification feature to enhance communication about cold relationships.
- **S4** Record and display the last engagement date on the country contact profile, ensuring compliance with data protection regulations regarding user consent and access controls.  
  Ensures compliance with data protection regulations by implementing user consent protocols and access controls. _(C4)_
- **S5** Provide a dashboard view where users can see all relationships that are currently cold.  
  Provides a dashboard view of cold relationships, aiding in user awareness and engagement strategies.
- **S6** Ensure alerts comply with data protection regulations regarding sensitive communications.  
  Guarantees that alerts adhere to data protection regulations, safeguarding sensitive information.

## What it will not do

**Out of scope for this release**

- **X1** This release will not include any predictive analytics or recommendations to improve cold relationships.  
  Excluded predictive analytics or recommendations to focus on direct alerts regarding cold relationships.
- **X2** This release does not address how to re-engage with cold relationships.  
  Not addressing re-engagement strategies was deemed outside the immediate scope of this feature.
- **X3** The release will not involve tracking communications that happen outside of the CRM system.  
  Decided against tracking external communications, focusing only on records maintained within the CRM.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users have access to the CRM and sufficient permissions to receive alerts and configure settings. | The request implies that users will interact with the CRM and utilize its features. | Accepted (never challenged) |
| A2 | Regional coordinators and project managers will ensure the accuracy of engagement activity records. | The successful deployment of alerts depends on accurate tracking and updating of engagement activities. | C3 → escalated |
| A3 | Users are familiar with how to interpret 'cold' status and take necessary actions based on alerts. | The request assumes users will know what to do when alerted about a cold relationship. | Accepted (never challenged) |

## Definitions

- **D1** "Cold relationship": A relationship where there has been no recorded engagement activity or communication for a user-defined period between 30 and 180 days.  
  Revised to allow user-defined criteria for cold relationships, making the definition more adaptable to varying contexts.
- **D2** "Engagement activity": Any recorded communication or interaction with a country representative documented within the CRM.  
  Defined engagement activity comprehensively to encompass all recorded communications, facilitating clearer alerts.

## Success criteria

- **K1** Percentage of users receiving alerts: target 80% of users report receiving timely alerts on cold relationships (Measured through user feedback surveys within 30 days of release.)  
  Set success criteria based on user feedback for receiving timely alerts, ensuring effectiveness can be measured.

## Open questions for humans

### C2 · BLOCKER · blocks the build

**What criteria will govern the flexibility in defining a 'cold relationship' to avoid unnecessary alerts?**

- Why it matters: Flexibility in defining criteria is important to accommodate varying contexts and improve relationship management.
- Decision owner: Head of CRM Development
- Options: Allow complete user-defined criteria / Establish standard category ranges

### C1 · MAJOR · blocks the build

**Who will establish and enforce access protocols for alerts regarding cold relationships?**

- Why it matters: Clarifying access controls is critical to prevent exposure of sensitive diplomatic information.
- Decision owner: Head of Data Protection
- Options: Define strict access protocols / Allow broader access within user roles

### C3 · MAJOR · blocks the build

**What specific procedures will be implemented to ensure the accuracy of engagement activity records?**

- Why it matters: Ensuring record accuracy is crucial to prevent false alerts that could mislead or misdirect resources.
- Decision owner: Operational Manager
- Options: Implement regular audits / Require user confirmations of records

### C5 · MAJOR · blocks the build

**How will the organization monitor and ensure the systematic updating of engagement records?**

- Why it matters: Clarity on processes is needed to prevent alert inaccuracies caused by outdated information.
- Decision owner: Managing Director
- Options: Designate record quality officers / Establish an automated tracking system

### C6 · MAJOR · blocks the build

**What measures will be taken to manage alert accesses when users change roles or leave the organization?**

- Why it matters: Failing to manage access correctly can lead to sensitive information leaks.
- Decision owner: HR Manager
- Options: Implement automatic access revocation / Conduct regular access reviews

### C7 · MAJOR · blocks the build

**What specific mechanisms will be established to ensure accurate tracking of engagement activity within the CRM?**

- Why it matters: Accurate tracking is vital to avoid discrepancies that lead to incorrect alerts.
- Decision owner: Data Governance Lead
- Options: Develop a tracking framework / Integrate user training modules

### C8 · MAJOR · blocks the build

**What explicit processes will be put in place for the systematic monitoring of engagement activities?**

- Why it matters: Systematic processes are crucial to prevent record inaccuracies and ensure reliable operations.
- Decision owner: Quality Assurance Manager
- Options: Establish a monitoring committee / Train staff on best practices

### C9 · MAJOR · blocks the build

**What procedures will safeguard access to cold relationship alerts for users who transfer roles or leave?**

- Why it matters: Addressing changes in user roles is essential for maintaining data confidentiality.
- Decision owner: Security Officer
- Options: Create a role change protocol / Update access lists in real time

### C10 · MAJOR · blocks the build

**What protocols will be specified to manage alert access relative to role changes or departures within the organization?**

- Why it matters: Clear protocols will help ensure former users do not retain access to sensitive alerts.
- Decision owner: IT Compliance Manager
- Options: Establish a revocation timeline / Define alert access policies

### C4 · MINOR · blocks the build

**What specific user consent protocols will be enforced to safeguard sensitive data related to engagement activities?**

- Why it matters: Compliance with data protection is essential to avoid legal violations and maintain user trust.
- Decision owner: Compliance Officer
- Options: Custom consent forms / Standard user agreement

## Tension report

The central disagreement revolves around the clarity and management of access protocols for alerts about cold relationships. The Proposer maintains that organizational input is necessary for defining access protocols and ensuring data security, while the Critic views the lack of detail as a significant risk, particularly regarding unauthorized access to sensitive information.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 4 | 4 | 0 | 0 | 1.00 | 80 | 60 | - | continue |
| 2 | 7 | 7 | 0 | 0 | 1.00 | 70 | 65 | CONTINUE | continue |
| 3 | 9 | 5 | 0 | 4 | 1.00 | 70 | 50 | CONTINUE | continue |
| 4 | 10 | 3 | 0 | 7 | 1.00 | 40 | 15 | CONTINUE | continue |
| 5 | 10 | 1 | 0 | 9 | 1.00 | 60 | 30 | CONTINUE | continue |
| 6 | 10 | 0 | 0 | 10 | 1.00 | 60 | 50 | CONTINUE | converged |

- Proposer's remaining worry (60/100): The organization must define specific access protocols to ensure the secure management of sensitive information in cold relationship alerts.
- Critic's remaining worry (50/100): Undefined protocols for access management may lead to unauthorized exposure of sensitive information.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S1 | R1 | ESCALATED | 2 | The proposal does not specify who can see the alert notifications for cold relationships, potentially exposing sensitive information to unauthorized users. |
| C2 | BLOCKER | DEFINITIONS | D1 | R1 | ESCALATED | 2 | The definition of 'cold relationship' is too rigid and lacks clarity, as it only specifies 90 days without engagement, which might not apply to every scenario. |
| C3 | MAJOR | OWNERSHIP | A2 | R1 | ESCALATED | 2 | The proposal does not clarify who maintains the engagement activity records or ensures their accuracy, risking outdated or incorrect data being used to trigger alerts. |
| C4 | MINOR | COMPLIANCE | S4 | R1 | ESCALATED | 2 | The proposal mentions compliance with data protection regulations but does not specify how user consent or data privacy will be managed in the context of storing and displaying engagement records. |
| C5 | MAJOR | OWNERSHIP | GAP | R2 | ESCALATED | 2 | The proposal lacks a clear process for how engagement activity records will be maintained and updated to ensure their accuracy over time. |
| C6 | MAJOR | CONFIDENTIALITY | GAP | R2 | ESCALATED | 2 | The proposal does not define how alerts will be managed when users change roles or leave the organization, which could potentially expose sensitive information to unauthorized users. |
| C7 | MAJOR | DATA_QUALITY | GAP | R2 | ESCALATED | 2 | The proposal does not specify how engagement activity will be accurately tracked within the CRM, leading to potential discrepancies between actual and recorded communication. |
| C8 | MAJOR | OWNERSHIP | GAP | R3 | ESCALATED | 2 | The proposal lacks an explicit process for systematic monitoring and enforcement of maintaining engagement records, risking future inconsistencies and inaccuracies. |
| C9 | MAJOR | CONFIDENTIALITY | GAP | R3 | ESCALATED | 2 | There is no defined policy for managing access to alerts for users who were previously involved but have changed roles or left the organization, risking sensitive information exposure. |
| C10 | MAJOR | CONFIDENTIALITY | GAP | R4 | ESCALATED | 2 | The proposal does not clarify how access to cold relationship alerts will be managed to prevent unauthorized exposure, especially when users change roles or leave the organization. |
