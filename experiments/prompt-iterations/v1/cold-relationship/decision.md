# Decision record: cold-relationship

> The CRM should alert us when our relationship with a country goes cold.

Deliberation ended **consensus** after 5 rounds (policy `gated`) · $0.009.

## Summary

This release will implement a notification system to alert users when engagement with a country has significantly decreased over a predefined period. Users will receive timely alerts and be able to track engagement history. Decisions still need to be made regarding data validation processes and user access to ensure effective and secure functionality.

## What this release will do

**Core commitments** (only the stakeholder can drop these)

- **V1** Users receive timely alerts when engagement with a country has decreased.  
  Users will receive timely alerts when engagement with a country has decreased, ensuring proactive management of relationships.
- **V2** Users can track and view engagement history for all countries in the CRM.  
  Users can track and view engagement history for all countries in the CRM, providing a comprehensive view of interactions.

**In scope**

- **S1** Develop a monitoring system to define and track 'engagement' based on frequency of interactions, with clear ownership assigned to the Regional Coordinator.  
  Developing a monitoring system to define and track 'engagement' will ensure clear ownership and consistency across interactions. _(C8)_
- **S2** Set predefined thresholds for what constitutes a decrease in engagement (e.g., no contact in the last six months), and notify only project managers and regional coordinators with limited summary information that does not disclose confidential details.  
  Setting predefined thresholds for engagement decrease and limiting notifications to certain roles ensures the handling of sensitive information appropriately. _(C1, C9)_
- **S3** Implement a notification system that alerts users (email or in-app) when engagement goes below the threshold, including details such as last contact date and type of communication.  
  Implementing a notification system will facilitate timely alerts, helping users to react quickly to reduced engagement.
- **S4** Allow users to customize notification settings (frequency, types of countries, etc.).  
  Allowing users to customize notification settings will increase user engagement and satisfaction with the system.
- **S5** Create an engagement history view in the CRM that shows last contact dates and types of interactions for each country.  
  Creating an engagement history view allows users to easily access and understand the history of interactions with each country.

## What it will not do

**Out of scope for this release**

- **X1** The release will not include any machine learning or advanced predictive analytics for engagement forecasting.  
  Machine learning or advanced predictive analytics for engagement forecasting was deemed out of scope for this release to maintain focus on basic alerting functionality.
- **X2** Historical data analysis beyond the last two years will not be included.  
  Historical data analysis beyond the last two years will not be included to streamline the current implementation.
- **X3** Integration with external communication platforms for tracking engagement (such as emails or calls) is not part of this release.  
  Integration with external communication platforms was not included to keep the project manageable and focused on internal CRM features.

**Rejected during deliberation**

- Nothing was dropped.

## Assumptions

| ID | Assumption | Why it was implicit | Challenged? |
|---|---|---|---|
| A1 | Users may have different thresholds for defining 'cold' relationships, and a nominated group will manage and interpret this across contexts. | The request assumes consensus on a cold engagement definition but does not specify how this will be managed or communicated. | C3 → revised |
| A2 | Users will actively use the alert system and value notifications regarding country engagement. | The request indicates a need for alerts, suggesting users will benefit from this feature. | Accepted (never challenged) |
| A3 | The CRM users have access to or regular interaction with the relevant data about engagement. | The request relies on the assumption that users will utilize the engagement history to manage relationships. | Accepted (never challenged) |

## Definitions

- **D1** ""goes cold"": Engagement is considered 'cold' if there has been no contact for a period of six months, but will also consider the frequency of various engagement types (e.g., meetings, reports).
- **D2** ""alert"": A notification sent via email or in-app message informing users of the decreased engagement status, including details such as last contact date, type of communication, and a recommended follow-up action.
- **D3** ""engagement history"": A record of all interactions with a country, including dates and types of communication (meetings, emails, reports, etc.) and who is responsible for updating this information.

## Success criteria

- **K1** Percentage of alerts sent: target At least 80% of users configured for notifications receive alerts within 24 hours of the engagement going cold. (Count of alerts sent and confirmed received by users in the first month after launch, using validated engagement data and regular updates based on checks conducted by data managers.)
- **K2** User satisfaction with the alert system: target At least 75% user satisfaction rating on the effectiveness of alerts in a post-deployment survey. (User feedback survey conducted 6 weeks after rollout.)

## Open questions for humans

### C4 · MAJOR · blocks the build

**What specific process will be implemented to validate and maintain the engagement data regularly? **

- Why it matters: Accurate and up-to-date engagement data is crucial for alert effectiveness and to avoid misallocation of resources.
- Decision owner: Head of Data Management
- Options: Establish routine data checks and updates / Delegate responsibility to specific roles for validation / Integrate automatic data validation systems

### C6 · MAJOR · blocks the build

**How will the implementation of the data validation process be monitored to ensure consistent upkeep of engagement data?**

- Why it matters: Monitoring the validation process is key to maintaining data accuracy, which directly impacts the reliability of alerts.
- Decision owner: Head of Data Management
- Options: Implement regular audits of data / Assign a team for continual oversight / Set up automated data validation alerts

## Tension report

The primary disagreement centered on ensuring data quality, particularly around engagement data validation processes. While the proposer expressed confidence in the provided solutions, the critic maintained concerns over the lack of specificity in how these processes would be implemented, leaving significant questions unresolved.

| Round | Raised | Open | Resolved | Escalated | Disagreement | Proposer conf. | Critic conf. | Critic signal | Outcome |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 5 | 5 | 0 | 0 | 1.00 | 70 | 40 | - | continue |
| 2 | 6 | 2 | 4 | 0 | 0.40 | 80 | 65 | CONTINUE | continue |
| 3 | 8 | 3 | 4 | 1 | 0.57 | 75 | 60 | CONTINUE | continue |
| 4 | 9 | 1 | 6 | 2 | 0.38 | 75 | 70 | CONTINUE | continue |
| 5 | 9 | 0 | 7 | 2 | 0.25 | 80 | 80 | CONCLUDE | consensus |

- Proposer's remaining worry (80/100): Ensuring that only authorized users receive alerts without compromising sensitive information.
- Critic's remaining worry (80/100): Ensuring the accuracy and completeness of engagement data remains unaddressed, which impacts overall alert effectiveness.

## Appendix: issue ledger

| ID | Severity | Lens | Targets | Raised | Outcome | Strikes | Challenge |
|---|---|---|---|---|---|---|---|
| C1 | MAJOR | CONFIDENTIALITY | S2 | R1 | REVISED | 0 | S2 states that a decrease in engagement is defined as no contact in the last six months, but it doesn’t specify who is notified of this engagement drop. |
| C2 | MAJOR | DEFINITIONS | D1 | R1 | REVISED | 0 | D1 defines 'goes cold' without considering variations in engagement types or communication among countries, which could lead to confusion in applying this threshold. |
| C3 | MINOR | OWNERSHIP | A1 | R1 | REVISED | 0 | A1 assumes a standard definition of cold relationships without identifying WHO interprets and manages variations in that definition across different users and contexts. |
| C4 | MAJOR | DATA_QUALITY | K1 | R1 | ESCALATED | 2 | K1's success criteria do not account for the accuracy or completeness of engagement data used to trigger alerts, which is critical for effectiveness. |
| C5 | MINOR | OWNERSHIP | D3 | R1 | REVISED | 0 | D3 does not clarify who is responsible for maintaining the engagement history or how it will be updated to ensure ongoing accuracy. |
| C6 | MAJOR | DATA_QUALITY | K1 | R2 | ESCALATED | 2 | K1 does not specify how the engagement data will be validated and kept up-to-date regularly, which is critical for alert effectiveness. |
| C7 | MAJOR | DEFINITIONS | K1 | R3 | REVISED | 0 | The term 'alerts' in K1 lacks specificity regarding the content and clarity of the information communicated to users. |
| C8 | MAJOR | OWNERSHIP | S1 | R3 | REVISED | 0 | S1 does not specify who is responsible for tracking and defining 'engagement' metrics, which raises questions about ongoing ownership and accountability. |
| C9 | MAJOR | CONFIDENTIALITY | GAP | R4 | REVISED | 0 | The proposal lacks clarity on how sensitive diplomatic information will be handled to ensure that alerts do not inadvertently expose confidential engagement information to unauthorized users. |
