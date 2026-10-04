# Deliberation trace: right-contact

> We need a better way to track who is the right person to contact in each country.

Policy `gated` · models: proposer gpt-4o-mini, summarizer gpt-4o-mini, critic gpt-4o-mini · ended **consensus** after 4 rounds · 15 model calls (6 repairs)

## Round 1

### Proposer · confidence 80

_This release will provide a streamlined interface for tracking key contact personnel in each member country, ensuring users can easily identify the appropriate contacts for engagement. It is designed for regional coordinators and project managers who need accessible and up-to-date information on contacts within government bodies._

**Core commitments**
- V1: Users can identify the primary contact person for each country, including their roles and affiliations.
- V2: Users can add, edit, and view contact details associated with each country.

**In scope**
- S1: The system will include a detailed contact management feature for up to 100 member countries, allowing users to view contact names, titles, ministry affiliations, and email addresses.
- S2: Regional coordinators and project managers will have access to add and edit contact information, including identifying fields for primary and secondary contacts.
- S3: The system will include validation rules for contact email formats and mandatory fields when adding or editing contact information.
- S4: The system will include a search function enabling users to query contacts by country, name, or ministry.
- S5: The system will log changes made to contact details, including who made the change and when it occurred.

**Out of scope**
- X1: This release will not include integration with external databases or CRM systems for automatically updating contact information.
- X2: This release will not implement notifications or alerts regarding changes to contact information.
- X3: This release will not focus on historical engagement tracking; it will only handle current contacts.

**Assumptions**
- A1: Users have basic training and familiarity with the CRM system; this is necessary for them to utilize the new contact management features effectively.
- A2: All contact details provided are compliant with relevant data protection regulations; the success of tracking contacts depends on having accurate and lawful contact data.
- A3: There will be a designated team responsible for data governance; this is essential for maintaining the integrity of contact information in the system.

**Definitions**
- D1: 'Contact person' means an individual representative from the government of a member country, along with their title, ministry affiliation, and contact information.
- D2: 'Key contact' means the primary person identified for engagement within a country, who is the first point of contact for communications and decisions.

**Success criteria**
- K1: At least 80% of users can identify the correct primary contact for each country within 3 clicks in the system, measured through user feedback surveys after implementation.

Biggest worry: Ensuring proper compliance with data protection regulations may pose challenges during implementation.

### Critic · confidence 30

Pre-mortem: A year after launch, a sensitive diplomatic contact record was inadvertently leaked to an unauthorized regional coordinator who had recently switched roles and gained access during a system-wide permissions error. This led to a mishandling of delicate negotiations with a foreign government, severely damaging relationships and resulting in public backlash.

Questions the request leaves open:
- Who can see contact details for sensitive or diplomatic positions, especially between different teams?
- What safeguards are in place to ensure that only authorized personnel can access or edit sensitive contact information?
- How is the system updated to reflect changes in roles for existing contacts, and what happens when a contact leaves their position?
- What are the specific criteria for determining who is a 'key contact' and how are those criteria enforced?
- How will compliance with data protection regulations (e.g., GDPR) be monitored regarding the storage and processing of contact details?
- What role does the designated governance team play in ensuring data accuracy and addressing duplicates in contact information?

New challenges:

**C1** · BLOCKER · CONFIDENTIALITY · targets S1, S2
- Challenge: The proposal does not specify who can view or edit sensitive contact information for government officials, which increases the risk of unauthorized access.
- Failure scenario: A regional coordinator unknowingly gains access to sensitive contact records of high-level diplomats and contacts, leading to inappropriate engagement attempts and diplomatic fallout.
- Resolution test: Which roles can view or edit sensitive diplomatic contact information?

**C2** · MAJOR · DEFINITIONS · targets D1, D2
- Challenge: The definitions of 'contact person' and 'key contact' lack clarity on selection criteria and context, which could lead to inconsistencies in contact entries and usage.
- Failure scenario: A user mistakenly adds an irrelevant contact to the system because they misinterpret who qualifies as a 'key contact', causing confusion and inefficiency.
- Resolution test: What specific criteria are used to classify an individual as a 'key contact' within the government CRM?

**C3** · MAJOR · OWNERSHIP · targets A3
- Challenge: The proposal relies on a designated governance team for maintaining data integrity but does not clarify who this team is or what their authority entails.
- Failure scenario: Contact details become outdated or inaccurate due to lack of defined responsibilities for the governance team, leading to miscommunication and lost opportunities.
- Resolution test: What team is designated for data governance, and what specific responsibilities do they hold regarding contact information accuracy?

**C4** · MAJOR · CONFIDENTIALITY · targets GAP
- Challenge: The proposal does not address how contact information will be protected from unauthorized access during system updates or when users change roles.
- Failure scenario: A former employee retains access to contact records after leaving the organization, leading to potential data breaches.
- Resolution test: What process is in place to revoke access to contact information when a user changes roles or departs from the organization?

**C5** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal does not specify how compliance with data protection regulations will be ensured throughout the process of collecting and managing contact information.
- Failure scenario: Contact details are stored without adequate consent or oversight, potentially violating data protection laws and resulting in legal action.
- Resolution test: What measures are in place to ensure compliance with relevant data protection regulations like GDPR?

**C6** · MAJOR · DATA_QUALITY · targets GAP
- Challenge: There are no clear processes defined for managing duplicates or inaccuracies in contact information, which could lead to a lack of trust in the system.
- Failure scenario: Multiple entries for the same contact confuse users, leading to incorrect engagement and lost opportunities.
- Resolution test: What procedures will be implemented to identify and resolve duplicates in the contact information?

Biggest worry: Unauthorized access to sensitive contact information could lead to significant diplomatic incidents.

**Ledger:** raised 6 · open 6 · resolved 0 · escalated 0 · disagreement 1.00 → **continue**

## Round 2

### Proposer · confidence 75

- **C1** REVISE (missing decision) [changed S1, S2]: The edits specify who is authorized to view and edit sensitive contact information, mitigating the risk of unauthorized access and ensuring compliance with data protection protocols.
- **C2** REVISE (missing decision) [changed D1, D2]: These revisions clarify the definitions of 'contact person' and 'key contact', establishing specific criteria to prevent inconsistent entries in the system.
- **C3** DEFEND (needs human decision): The specific governance team for maintaining data integrity and its responsibilities should be defined by the organization's policies, as this decision involves internal governance structure.
- **C4** REVISE (missing decision) [changed S5]: This edit introduces a process for revoking access to sensitive information, addressing the risk of unauthorized access following user role changes.
- **C5** DEFEND (needs human decision): Compliance with data protection regulations must be defined by organizational policies and procedures, which need to be confirmed by the appropriate legal or compliance team.
- **C6** REVISE (missing decision) [changed S6]: This edit details procedures for managing contact data quality, reducing the potential for confusion caused by duplicate entries.

Proposal changes: added S6; edited S1, S2, S5, D1, D2
- S6 now reads: The system will implement a process for identifying and managing duplicate contact entries, including regular data quality audits and user confirmation steps during data entry to minimize inaccuracies.
- S1 now reads: The system will include a detailed contact management feature for up to 100 member countries, allowing users to view contact names, titles, ministry affiliations, and email addresses. Access to sensitive contact information for high-level government officials will be restricted to authorized regional coordinators and project managers with appropriate clearances as defined in the organization's access control policy.
- S2 now reads: Regional coordinators and project managers will have access to add and edit contact information, including identifying fields for primary and secondary contacts. Only users with the role of 'Regional Coordinator' or 'Project Manager' who have undergone data protection training will be allowed to edit sensitive contact information.
- S5 now reads: The system will log changes made to contact details, including who made the change and when it occurred. Additionally, user access rights will be revoked automatically when a user changes roles or is removed from the organization as part of the user management protocol.
- D1 now reads: 'Contact person' means an individual representative from the government of a member country, along with their title, ministry affiliation, and contact information. A contact person must be an officially designated representative, holding a relevant title within their government.
- D2 now reads: 'Key contact' means the primary person identified for engagement within a country, who is the first point of contact for communications and decisions. A key contact must be the official responsible for the area of engagement relevant to the organization's objectives, determined by title and office.

Biggest worry: Ensuring compliance with data protection laws while implementing these features may require ongoing oversight.

### Critic · confidence 65 · CONTINUE

Rulings:
- **C1** ACCEPT: This clearly defines the roles with access to sensitive information, resolving the confidentiality concern. Fact: Access to sensitive contact information is restricted to authorized regional coordinators and project managers. Evidence: "Access to sensitive contact information for high-level government officials will be restricted to authorized regional coordinators and project managers."
- **C2** ACCEPT: This provides clarity on the selection criteria for key contacts, resolving the definition issue. Fact: A key contact is defined by their official title and office related to the organization's objectives. Evidence: "A key contact must be the official responsible for the area of engagement relevant to the organization's objectives, determined by title and office."
- **C3** ESCALATE: The lack of clarity on the governance team and their responsibilities remains unresolved.
- **C4** ACCEPT: This addresses the concern of unauthorized access following role changes. Fact: User access rights are revoked when a user changes roles or is removed from the organization. Evidence: "Additionally, user access rights will be revoked automatically when a user changes roles or is removed from the organization."
- **C5** ESCALATE: Compliance with data protection regulations remains uncertain as it relies on external validation.
- **C6** ACCEPT: This addresses the data quality concerns adequately. Fact: There are processes for auditing and confirming data accuracy and managing duplicates. Evidence: "The system will implement a process for identifying and managing duplicate contact entries, including regular data quality audits and user confirmation steps during data entry to minimize inaccuracies."

New challenges:

**C7** · MAJOR · OWNERSHIP · targets A3
- Challenge: The proposal does not clarify what the designated governance team's specific responsibilities entail for maintaining data accuracy.
- Failure scenario: Without defined responsibilities, the governance team's role becomes ineffective, leading to inaccurate or outdated contact details and potential diplomatic incidents.
- Resolution test: What specific responsibilities does the designated governance team hold regarding contact information accuracy?

Biggest worry: Compliance and ownership of data integrity remain unclear, posing risks to the system's reliability and security.

**Ledger:** raised 7 · open 1 · resolved 4 · escalated 2 · disagreement 0.40 → **continue**

## Round 3

### Proposer · confidence 80

- **C7** DEFEND (needs human decision): The responsibilities of the designated governance team regarding data accuracy should be determined by the organization itself, as its scope and authority might vary based on specific internal guidelines.

Proposal changes: none

Biggest worry: Ensuring compliance with data protection regulations while maintaining up-to-date contact information.

### Critic · confidence 65 · CONTINUE

Rulings:
- **C7** ESCALATE: The proposal does not define the specific responsibilities, leaving it ambiguous and dependent on organizational structure.

New challenges:

**C8** · MAJOR · OWNERSHIP · targets GAP
- Challenge: The proposal does not specify what happens to the contact information if the designated governance team changes or if key personnel leave, risking loss of data integrity.
- Failure scenario: If the designated governance team disbands or key personnel leave without a clear handover, the system may operate without proper maintenance, leading to outdated or incorrect contact information.
- Resolution test: What process ensures continuity of governance responsibilities and data accuracy if key personnel change?

**C9** · MAJOR · COMPLIANCE · targets GAP
- Challenge: The proposal lacks a defined mechanism for ensuring ongoing compliance with data protection regulations as new data is entered or processes change.
- Failure scenario: New contact data is added without proper checks against data protection laws, leading to the organization handling non-compliant data and facing legal repercussions.
- Resolution test: What processes will be put in place to review compliance with data protection regulations for newly added contact information?

Biggest worry: Without clear governance responsibilities, the integrity and compliance of sensitive contact information may be compromised.

**Ledger:** raised 9 · open 2 · resolved 4 · escalated 3 · disagreement 0.53 → **continue**

## Round 4

### Proposer · confidence 75

- **C8** REVISE (missing decision) [changed S7]: The new governance continuity plan outlines how the organization will handle key personnel changes and ensures ongoing accountability for data integrity.
- **C9** REVISE (missing decision) [changed S8]: The compliance review protocol ensures that all new data entered will meet legal requirements, mitigating the risk of data breaches and compliance issues.

Proposal changes: added S7, S8
- S7 now reads: The system will implement a continuity plan for governance responsibilities, ensuring that if key personnel change or the governance team disbands, a new governance team is appointed immediately from a designated pool of trained individuals. This plan will also include a process for transferring and reviewing contact entries, ensuring consistent data integrity.
- S8 now reads: The system will establish a compliance review protocol whereby any new contact data is reviewed by the governance team to ensure compliance with data protection regulations before it is finalized in the system. Additionally, periodic audits will be conducted to confirm ongoing compliance with all governing policies.

Biggest worry: Ensuring the governance continuity and compliance mechanisms are consistently upheld over time.

### Critic · confidence 85 · CONCLUDE

Rulings:
- **C8** ACCEPT: This effectively addresses the continuity of governance responsibilities and data integrity. Fact: A new governance team will be appointed from a designated pool when key personnel change or the original team disbands. Evidence: "The system will implement a continuity plan for governance responsibilities, ensuring that if key personnel change or the governance team disbands, a new governance team is appointed immediately from a designated pool of trained individuals. This plan will also include a process for transferring and reviewing contact entries, ensuring consistent data integrity."
- **C9** ACCEPT: The protocol stipulates that new contact data must be reviewed for compliance prior to being finalized, which addresses the challenge. Fact: New contact data will be reviewed by the governance team for compliance with data protection regulations before finalization. Evidence: "The system will establish a compliance review protocol whereby any new contact data is reviewed by the governance team to ensure compliance with data protection regulations before it is finalized in the system."

Biggest worry: There may still be gaps in clearly defining user roles and responsibilities around data access and governance.

**Ledger:** raised 9 · open 0 · resolved 6 · escalated 3 · disagreement 0.32 → **consensus**

## Final proposal

_This release will provide a streamlined interface for tracking key contact personnel in each member country, with protocols for authorization, entry criteria, governance, compliance, and data quality management, including a plan for continuity of governance and ensuring compliance with data protection regulations. It is designed for regional coordinators and project managers who need accessible and up-to-date information on contacts within government bodies._

**Core commitments**
- V1: Users can identify the primary contact person for each country, including their roles and affiliations.
- V2: Users can add, edit, and view contact details associated with each country.

**In scope**
- S1: The system will include a detailed contact management feature for up to 100 member countries, allowing users to view contact names, titles, ministry affiliations, and email addresses. Access to sensitive contact information for high-level government officials will be restricted to authorized regional coordinators and project managers with appropriate clearances as defined in the organization's access control policy.
- S2: Regional coordinators and project managers will have access to add and edit contact information, including identifying fields for primary and secondary contacts. Only users with the role of 'Regional Coordinator' or 'Project Manager' who have undergone data protection training will be allowed to edit sensitive contact information.
- S3: The system will include validation rules for contact email formats and mandatory fields when adding or editing contact information.
- S4: The system will include a search function enabling users to query contacts by country, name, or ministry.
- S5: The system will log changes made to contact details, including who made the change and when it occurred. Additionally, user access rights will be revoked automatically when a user changes roles or is removed from the organization as part of the user management protocol.
- S6: The system will implement a process for identifying and managing duplicate contact entries, including regular data quality audits and user confirmation steps during data entry to minimize inaccuracies.
- S7: The system will implement a continuity plan for governance responsibilities, ensuring that if key personnel change or the governance team disbands, a new governance team is appointed immediately from a designated pool of trained individuals. This plan will also include a process for transferring and reviewing contact entries, ensuring consistent data integrity.
- S8: The system will establish a compliance review protocol whereby any new contact data is reviewed by the governance team to ensure compliance with data protection regulations before it is finalized in the system. Additionally, periodic audits will be conducted to confirm ongoing compliance with all governing policies.

**Out of scope**
- X1: This release will not include integration with external databases or CRM systems for automatically updating contact information.
- X2: This release will not implement notifications or alerts regarding changes to contact information.
- X3: This release will not focus on historical engagement tracking; it will only handle current contacts.

**Assumptions**
- A1: Users have basic training and familiarity with the CRM system; this is necessary for them to utilize the new contact management features effectively.
- A2: All contact details provided are compliant with relevant data protection regulations; the success of tracking contacts depends on having accurate and lawful contact data.
- A3: There will be a designated team responsible for data governance; this is essential for maintaining the integrity of contact information in the system.

**Definitions**
- D1: 'Contact person' means an individual representative from the government of a member country, along with their title, ministry affiliation, and contact information. A contact person must be an officially designated representative, holding a relevant title within their government.
- D2: 'Key contact' means the primary person identified for engagement within a country, who is the first point of contact for communications and decisions. A key contact must be the official responsible for the area of engagement relevant to the organization's objectives, determined by title and office.

**Success criteria**
- K1: At least 80% of users can identify the correct primary contact for each country within 3 clicks in the system, measured through user feedback surveys after implementation.
