# STIG Benchmark: EDB Postgres Advanced Server v9.6 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-213561`

### Rule: The EDB Postgres Advanced Server must limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types.

**Rule ID:** `SV-213561r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system documentation specifies limits on the number of concurrent DBMS sessions per account by type of user. If it does not, assume a limit of 10 for database administrators and 2 for all other users. Execute the following SQL as enterprisedb: SELECT rolname, rolconnlimit FROM pg_roles; If rolconnlimit is -1 or larger than the system documentation limits for any rolname, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-213562`

### Rule: The EDB Postgres Advanced Server must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-213562r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Account management functions can also include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. The DBMS must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that pg_hba.conf is not using: “trust”, “md5”, or “password” as allowable access methods. > cat <postgresql data directory>/pg_hba.conf | egrep –I ‘(trust|md5|password)’ | grep –v ‘#’ If any output is produced, verify the users are documented as being authorized to use one of these access methods. If the users are not authorized to use these access methods, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-213563`

### Rule: The EDB Postgres Advanced Server must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-213563r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the DBMS. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for DBMS server securables by type of login. Review the permissions actually in place on the server. If the actual permissions do not match the documented requirements, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213564`

### Rule: The EDB Postgres Advanced Server must protect against a user falsely repudiating having performed organization-defined actions.

**Rule ID:** `SV-213564r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables, and configuring the DBMS' audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, group account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit; If the result is not "csv" or "xml", this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-213565`

### Rule: The EDB Postgres Advanced Server must provide audit record generation capability for DoD-defined auditable events within all EDB Postgres Advanced Server/database components.

**Rule ID:** `SV-213565r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit; If the result is not "csv" or "xml", this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-213566`

### Rule: The EDB Postgres Advanced Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-213566r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the command "ls -al <postgresql data directory>/postgresql*.conf" to show file permissions. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If the files are not owned by enterprisedb(user)/enterprisedb(group) or does not have RW permission for the user only, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-213567`

### Rule: The EDB Postgres Advanced Server must generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-213567r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-213568`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-213568r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-213569`

### Rule: The EDB Postgres Advanced Server must initiate support of session auditing upon startup.

**Rule ID:** `SV-213569r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is for use when a user's activities are under investigation. Typically, this DBMS capability would be used in conjunction with comparable monitoring of a user's online session, involving other software components such as operating systems, web servers and front-end user applications. The current requirement, however, deals specifically with the DBMS. To be sure of capturing all activity during those periods when session auditing is in use, database auditing needs to be in operation for the whole time the DBMS is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000095-DB-000039

**Group ID:** `V-213570`

### Rule: The EDB Postgres Advanced Server must produce audit records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-213570r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit record content that may be necessary to satisfy the requirement of this policy includes, for example, time stamps, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly what actions were performed. This requires specific information regarding the event type an audit record is referring to. If event type information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000096-DB-000040

**Group ID:** `V-213571`

### Rule: The EDB Postgres Advanced Server must produce audit records containing time stamps to establish when the events occurred.

**Rule ID:** `SV-213571r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the date and time when events occurred. Associating the date and time with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly when specific actions were performed. This requires the date and time an audit record is referring to. If date and time information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000097-DB-000041

**Group ID:** `V-213572`

### Rule: The EDB Postgres Advanced Server must produce audit records containing sufficient information to establish where the events occurred.

**Rule ID:** `SV-213572r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as application components, modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the application provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000098-DB-000042

**Group ID:** `V-213573`

### Rule: The EDB Postgres Advanced Server must produce audit records containing sufficient information to establish the sources (origins) of the events.

**Rule ID:** `SV-213573r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events relating to an incident. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as application components, modules, session identifiers, filenames, host names, and functionality. In addition to logging where events occur within the application, the application must also produce audit records that identify the application itself as the source of the event. Associating information about the source of the event within the application provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-213574`

### Rule: The EDB Postgres Advanced Server must produce audit records containing sufficient information to establish the outcome (success or failure) of the events.

**Rule ID:** `SV-213574r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000100-DB-000201

**Group ID:** `V-213575`

### Rule: The EDB Postgres Advanced Server must produce audit records containing sufficient information to establish the identity of any user/subject or process associated with the event.

**Rule ID:** `SV-213575r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-213576`

### Rule: The EDB Postgres Advanced Server must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-213576r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. To support analysis, some types of events will need information to be logged that exceeds the basic requirements of event type, time stamps, location, source, outcome, and user identity. If additional information is not available, it could negatively impact forensic investigations into user actions or other malicious events. The organization must determine what additional information is required for complete analysis of the audited events. The additional information required is dependent on the type of information (e.g., sensitivity of the data and the environment within which it resides). At a minimum, the organization must employ either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Examples of detailed information the organization may require in audit records are full-text recording of privileged commands or the individual identities of group account users. In EnterpriseDB Postgres Plus Advanced Server, the edb_audit_tag can be used to record additional information. This tag can be set to different values by different sessions (connections), and can be set to new values any number of times. How to recognize the conditions for producing such audit data has to be determined and coded for as part of application and database design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to identify what additional information the organization has determined necessary. Check application and database design, and existing audit records to verify that all organization-defined additional, more detailed information is in the audit records for audit events identified by type, location, or subject. If any additional information is defined and is not included in the audit records, this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-213577`

### Rule: The EDB Postgres Advanced Server must by default shut down upon audit failure, to include the unavailability of space for more audit log records; or must be configurable to shut down upon audit failure.

**Rule ID:** `SV-213577r879571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When the need for system availability does not outweigh the need for a complete audit trail, the DBMS should shut down immediately, rolling back all in-flight transactions. Systems where audit trail completeness is paramount will most likely be at a lower MAC level than MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid a shutdown in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Postgres Enterprise Manager (PEM) is not installed and configured to shut down the database when the audit log is full, this is a finding.

## Group: SRG-APP-000109-DB-000321

**Group ID:** `V-213578`

### Rule: The EDB Postgres Advanced Server must be configurable to overwrite audit log records, oldest first (First-In-First-Out - FIFO), in the event of unavailability of space for more audit log records.

**Rule ID:** `SV-213578r879571_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the DBMS must continue generating audit records, if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the DBMS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server. Systems where availability is paramount will most likely be MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid audit data loss in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an externally managed and monitored partition or logical volume that can be grown dynamically is being used for logging, this is not a finding.   If PPAS is auditing to a directory that is not being actively checked for availability of disk space, and if logrotate is not configured to rotate logs based on the size of the audit log directory with oldest logs being replaced by newest logs, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-213579`

### Rule: The audit information produced by the EDB Postgres Advanced Server must be protected from unauthorized read access.

**Rule ID:** `SV-213579r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-213580`

### Rule: The audit information produced by the EDB Postgres Advanced Server must be protected from unauthorized modification.

**Rule ID:** `SV-213580r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-213581`

### Rule: The audit information produced by the EDB Postgres Advanced Server must be protected from unauthorized deletion.

**Rule ID:** `SV-213581r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-213582`

### Rule: The EDB Postgres Advanced Server must protect its audit features from unauthorized access.

**Rule ID:** `SV-213582r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-213583`

### Rule: The EDB Postgres Advanced Server must protect its audit configuration from unauthorized modification.

**Rule ID:** `SV-213583r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-213584`

### Rule: The EDB Postgres Advanced Server must protect its audit features from unauthorized removal.

**Rule ID:** `SV-213584r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “edb_audit” directory: > ls –ald <postgresql data directory>/edb_audit If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213585`

### Rule: Software, applications, and configuration files that are part of, or related to, the Postgres Plus Advanced Server  installation must be monitored to discover unauthorized changes.

**Rule ID:** `SV-213585r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Monitoring is required for assurance that the protections are effective. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify monitoring of changes to database software libraries, related applications, and configuration files is done. Verify the list of files and directories being monitored is complete. If monitoring does not occur or is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213586`

### Rule: EDB Postgres Advanced Server software modules, to include stored procedures, functions and triggers must be monitored to discover unauthorized changes.

**Rule ID:** `SV-213586r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Monitoring is required for assurance that the protections are effective. Unmanaged changes that occur to the logic modules within the database can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the EDB Postgres configuration for a timed job that automatically checks all system and user-defined procedures, functions and triggers for being modified by running the following EDB Postgres query: select job, what from ALL_JOBS; (Alternatively, in Postgres Enterprise Manager, navigate to the "Jobs" node of the database and examine the job from there.) If a timed job or some other method is not implemented to check for Triggers being modified, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-213587`

### Rule: The EDB Postgres Advanced Server software installation account must be restricted to authorized users.

**Rule ID:** `SV-213587r879586_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling, granting access to, and tracking use of the DBMS software installation account. If access or use of this account is not restricted to the minimum number of personnel required or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-213588`

### Rule: Database software, including EDB Postgres Advanced Server configuration files, must be stored in dedicated directories, separate from the host OS and other applications.

**Rule ID:** `SV-213588r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS software library directory and note other root directories located on the same disk directory or any subdirectories. If any non-DBMS software directories exist on the disk directory, examine or investigate their use. If any of the directories are used by other applications, including third-party applications that use the DBMS, this is a finding. Only applications that are required for the functioning and administration, not use, of the DBMS should be located in the same disk directory as the DBMS software libraries. If other applications are located in the same directory as the DBMS, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-213589`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to the EDB Postgres Advanced Server, etc.) must be owned by database/EDB Postgres Advanced Server principals authorized for ownership.

**Rule ID:** `SV-213589r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify accounts authorized to own database objects. Review accounts that own objects in the database(s) by running this SQL command: select * from sys.all_objects; If any database objects are found to be owned by users not authorized to own database objects, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-213590`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to the EDB Postgres Advanced Server, etc.) must be restricted to authorized users.

**Rule ID:** `SV-213590r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use psql to connect to the db as enterprisedb and run this command: \dp *.* If any unauthorized roles have unauthorized accesses, this is a finding. Definitions of the access privileges are defined here: http://www.postgresql.org/docs/current/static/sql-grant.html

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-213591`

### Rule: Default, demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-213591r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality, not required for every mission, that cannot be disabled. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review vendor documentation and vendor websites for vendor-provided demonstration or sample databases, database applications, objects, and files. Review the DBMS to determine if any of the demonstration and sample databases, database applications, or files are installed in the database or are included with the DBMS application. If any are present in the database or are included with the DBMS application, this is a finding. Check for the existence of EDB Postgres sample databases: postgres and edb. Execute the following SQL as enterprisedb: SELECT datname FROM pg_database WHERE datistemplate = false; If any databases are listed here that are not used by the application, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213592`

### Rule: Unused database components, EDB Postgres Advanced Server software, and database objects must be removed.

**Rule ID:** `SV-213592r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of components and features installed with the database. If unused components are installed and are not documented and authorized, this is a finding. RPM can also be used to check to see what is installed: yum list installed | grep ppas This returns EDB database packages that have been installed. If any packages displayed by this command are not being used, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-213593`

### Rule: Unused database components which are integrated in the EDB Postgres Advanced Server and cannot be uninstalled must be disabled.

**Rule ID:** `SV-213593r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/group permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command as root: yum list installed | grep ppas If any packages are installed that are not needed, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-213594`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-213594r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command as root: yum list installed | grep ppas If any packages are installed that are not needed, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-213595`

### Rule: The EDB Postgres Advanced Server must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-213595r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW port; SHOW listen_addresses; If the port or addresses are not approved, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-213596`

### Rule: The EDB Postgres Advanced Server must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-213596r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "<postgresql data directory>/pg_hba.conf" in a viewer or editor. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any rows have "trust" specified for the "METHOD" column, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-213597`

### Rule: If passwords are used for authentication, the EDB Postgres Advanced Server must store only hashed, salted representations of passwords.

**Rule ID:** `SV-213597r879608_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW password_encryption; If the value is not "on", this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-213598`

### Rule: If passwords are used for authentication, the EDB Postgres Advanced Server must transmit only encrypted representations of passwords.

**Rule ID:** `SV-213598r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "<postgresql data directory>/pg_hba.conf" in a viewer or editor. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any rows have "password" specified for the "METHOD" column, this is a finding.

## Group: SRG-APP-000175-DB-000067

**Group ID:** `V-213599`

### Rule: The EDB Postgres Advanced Server, when utilizing PKI-based authentication, must validate certificates by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-213599r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. A certificate’s certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses. Database Management Systems that do not validate certificates by performing RFC 5280-compliant certification path validation are in danger of accepting certificates that are invalid and/or counterfeit. This could allow unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open "<postgresql data directory>/pg_hba.conf" in a viewer or editor. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any rows have TYPE of "hostssl" but do not include "clientcert=1" in the OPTIONS column at the end of the line, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-213600`

### Rule: The EDB Postgres Advanced Server must enforce authorized access to all PKI private keys stored/utilized by the EDB Postgres Advanced Server.

**Rule ID:** `SV-213600r879613_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where the DBMS-stored private keys are used to authenticate the DBMS to the system’s clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man in the middle attacks against the DBMS system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 or 140-3 validated cryptographic modules. All access to the private key(s) of the DBMS must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of the DBMS's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “server.key” file: > ls –alL <postgresql data directory>/server.key If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the file is more permissive than 600, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213601`

### Rule: Applications must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-213601r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. Database applications may allow for entry of the account name and password as a visible parameter of the application execution command. This practice must be prohibited and disabled to prevent shoulder surfing. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether any applications that access the database allow for entry of the account name and password or PIN. If any do, determine whether these applications obfuscate authentication data. If they do not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213602`

### Rule: When using command-line tools such as psql, users must use a logon method that does not expose the password.

**Rule ID:** `SV-213602r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. This requirement is applicable when mixed-mode authentication is enabled. When this is the case, password-authenticated accounts can be created in and authenticated by SQL Server. Other STIG requirements prohibit the use of mixed-mode authentication except when justified and approved. This deals with the exceptions. Psql is part of any PostgreSQL installation. Other command-line tools may also exist. These tools can accept a plain-text password, but do offer alternative techniques. Since the typical user of these tools is a database administrator, the consequences of password compromise are particularly serious. Therefore, the use of plain-text passwords must be prohibited, as a matter of practice and procedure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For psql, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations and that AO approval has been obtained. If not, this is a finding. Request evidence that all users of the tool are trained in the importance of using the "-P" option and not using the plain-text password option and in how to keep the password hidden and that they adhere to this practice. If not, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-213603`

### Rule: The EDB Postgres Advanced Server must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-213603r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications (including DBMSs) utilizing cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a FIPS-certified OpenSSL library is not installed and configured, this is a finding. Run this command to ensure that you are running RHEL: "cat /etc/redhat-release" Run this command to see the OpenSSL version: "openssl version" If "/etc/redhat-release" does not show a supported version of Red Hat Enterprise Linux or if the openssl version does not include "-fips" in the version, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213604`

### Rule: The EDB Postgres Advanced Server must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-213604r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. Execute the following command as root: > df If the mounted filesystem where "<postgresql data directory>" exists is not located on an encrypted disk partition, this is a finding.   (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-213605`

### Rule: The EDB Postgres Advanced Server must isolate security functions from non-security functions.

**Rule ID:** `SV-213605r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All PPAS built-in security packages are in the sys, pg_catalog, information_schema, and dbo schemas. If any application-specific packages have been added to these schemas, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-213606`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-213606r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-213607`

### Rule: Access to database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-213607r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure that those files are not shared inappropriately and are not open to backdoor access and manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the <postgressql data directory> directory: > ls –ald <postgresql data directory> If the User owner is not “enterprisedb”, this is a finding If the Group owner is not “enterprisedb”, this is a finding. If the directory is more permissive than 700, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-213608`

### Rule: The EDB Postgres Advanced Server must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-213608r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SELECT * FROM sqlprotect.list_protected_users; If the database and user that handles user input is not listed or if sqlprotect.list_protected_users does not exist (meaning SQL/Protect is not installed), and an alternative means of reviewing for vulnerable code is not in use, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-213609`

### Rule: The EDB Postgres Advanced Server and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-213609r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SELECT * FROM sqlprotect.list_protected_users; If the database and user that handles user input is not listed or if sqlprotect.list_protected_users does not exist (meaning SQL/Protect is not installed), and an alternative means of reviewing for vulnerable code is not in use, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-213610`

### Rule: The EDB Postgres Advanced Server and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack.

**Rule ID:** `SV-213610r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: -- Allow strings as input only when necessary. -- Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. -- Limit the size of input strings to what is truly necessary. -- If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. -- If comment markers will never be valid as input, reject them. In SQL, these are -- or /* */ -- If HTML and XML tags, entities, comments, etc., will never be valid, reject them. -- If wildcards are present, reject them unless truly necessary. In SQL these are the underscore and the percentage sign, and the word ESCAPE is also a clue that wildcards are in use. -- If SQL key words, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, ESCAPE, UNION, GRANT, REVOKE will never be valid, reject them. Use case-insensitive comparisons when searching for these. Bear in mind that some of these words, particularly Grant (as a person's name), could also be valid input. -- If there are range limits on the values that may be entered, enforce those limits. -- Institute procedures for inspection of programs for correct use of dynamic coding, by a party other than the developer. -- Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. -- Record the inspection and testing in the system documentation. -- Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities; it may itself be the attacker. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SELECT * FROM sqlprotect.list_protected_users; If the database and user that handles user input is not listed or if sqlprotect.list_protected_users does not exist (meaning SQL/Protect is not installed), and an alternative means of reviewing for vulnerable code is not in use, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-213611`

### Rule: The EDB Postgres Advanced Server must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-213611r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom database code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If custom database errors contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-213612`

### Rule: The EDB Postgres Advanced Server must reveal detailed error messages only to the ISSO, ISSM, SA and DBA.

**Rule ID:** `SV-213612r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, please contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA and DBA. Other individuals or roles may be specified according to organization-specific needs, with appropriate approval. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom database code to determine if detailed error messages are ever displayed to unauthorized individuals. If detailed error messages are displayed to individuals not authorized to view them, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-213613`

### Rule: The EDB Postgres Advanced Server must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-213613r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If the documentation requires automatic session termination but the DBMS is not configured via triggers, scripts, or other organization-defined manners to terminate sessions when required, this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-213614`

### Rule: The EDB Postgres Advanced Server must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-213614r879689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not applicable (NA). If security labeling requirements have been specified, execute the following SQL as enterprisedb: SELECT * from ALL_POLICIES where OBJECT_NAME = '<table name>'; If a policy is not enabled for the table requiring security labeling, this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-213615`

### Rule: The EDB Postgres Advanced Server must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-213615r879690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not applicable (NA). If security labeling requirements have been specified, execute the following SQL as enterprisedb: SELECT * from ALL_POLICIES where OBJECT_NAME = '<table name>'; If a policy is not enabled for the table requiring security labeling, this is a finding.

## Group: SRG-APP-000314-DB-000310

**Group ID:** `V-213616`

### Rule: The EDB Postgres Advanced Server must associate organization-defined types of security labels having organization-defined security label values with information in transmission.

**Rule ID:** `SV-213616r879691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not applicable (NA). If security labeling requirements have been specified, execute the following SQL as enterprisedb: SELECT * from ALL_POLICIES where OBJECT_NAME = '<table name>'; If a policy is not enabled for the table requiring security labeling, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-213617`

### Rule: The EDB Postgres Advanced Server must prevent non-privileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-213617r879717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain the definition of the database/DBMS functionality considered privileged in the context of the system in question. If any functionality considered privileged has access privileges granted to non-privileged users, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-213618`

### Rule: Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only.

**Rule ID:** `SV-213618r879719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be utilized only where necessary and protected from misuse. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and source code of the application(s) using the database. If elevation of DBMS privileges is used but not documented, this is a finding. If elevation of DBMS privileges is documented but not implemented as described in the documentation, this is a finding. If the privilege-elevation logic can be invoked in ways other than intended, in contexts other than intended, or by subjects/principals other than intended, this is a finding. Execute the following SQL to find any SECURITY DEFINER functions (meaning they are executed as owner rather than invoker): select proname from pg_proc where prosecdef = true; If any of these functions should not be SECURITY DEFINER, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-213619`

### Rule: Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only.

**Rule ID:** `SV-213619r879719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be utilized only where necessary and protected from misuse. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and source code of the application(s) using the database. If elevation of DBMS privileges is used but not documented, this is a finding. If elevation of DBMS privileges is documented but not implemented as described in the documentation, this is a finding. If the privilege-elevation logic can be invoked in ways other than intended, in contexts other than intended, or by subjects/principals other than intended, this is a finding. Execute the following SQL to find any users with BYPASS RLS permissions: select rolname from pg_roles where rolbypassrls = true; If any of these users are not superusers that should bypass RLS, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-213620`

### Rule: The EDB Postgres Advanced Server must utilize centralized management of the content captured in audit records generated by all components of the EDB Postgres Advanced Server.

**Rule ID:** `SV-213620r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a centralized log collecting tool such as Postgres Enterprise Manager (PEM) is not installed and configured to automatically collect audit logs, this is a finding. Review the system documentation for a description of how audit records are off-loaded and how local audit log space is managed.

## Group: SRG-APP-000356-DB-000315

**Group ID:** `V-213621`

### Rule: The EDB Postgres Advanced Server must provide centralized configuration of the content to be captured in audit records generated by all components of the EDB Postgres Advanced Server.

**Rule ID:** `SV-213621r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the configuration of the DBMS's auditing is spread across multiple locations in the database management software, or across multiple commands, only loosely related, it is harder to use and takes longer to reconfigure in response to events. The DBMS must provide a unified tool for audit configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a unified tool for audit configuration such as PEM (Postgres Enterprise Manager) is not installed and configured to automatically collect audit logs, this is a finding. Review the system documentation for a description of how audit records are off-loaded and how local audit log space is managed.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-213622`

### Rule: The EDB Postgres Advanced Server must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-213622r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, the DBMS must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the DBMS and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Investigate whether there have been any incidents where the DBMS ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-213623`

### Rule: The EDB Postgres Advanced Server must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity.

**Rule ID:** `SV-213623r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so under normal conditions, the audit space allocated to the DBMS on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Postgres Enterprise Manager (PEM) or another similar monitoring capability is not installed and configured to probe storage volume utilization of "<postgresql data directory>" and notify appropriate support staff upon storage volume utilization reaching 75 percent, this is a finding. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.)

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-213624`

### Rule: The EDB Postgres Advanced Server must provide an immediate real-time alert to appropriate support staff of all audit log failures.

**Rule ID:** `SV-213624r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Postgres Enterprise Manager (PEM) alert settings, OS, or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-213625`

### Rule: The EDB Postgres Advanced Server must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-213625r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. The DBMS must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization. In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If EDB Postgres supports only software development, experimentation, and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. Review the EDB Postgres security settings with respect to non-administrative users' ability to create, alter, or replace logic modules, to include but not necessarily only stored procedures, functions, triggers, and views. These psql commands can help with showing existing permissions of databases and schemas: \l \dn+ If any such permissions exist and are not documented and approved, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-213626`

### Rule: The EDB Postgres Advanced Server must enforce access restrictions associated with changes to the configuration of the EDB Postgres Advanced Server or database(s).

**Rule ID:** `SV-213626r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the security configuration of the EDB Postgres database(s). If unauthorized users can start the SQL Server Configuration Manager or SQL Server Management Studio, this is a finding. If EDB Postgres does not enforce access restrictions associated with changes to the configuration of the database(s), this is a finding. - - - - - To assist in conducting reviews of permissions, the following psql commands describe permissions of databases, schemas, and users: \l \dn+ \du Permissions of concern in this respect include the following, and possibly others: - any user with SUPERUSER privileges - any database or schema with "C" (create) or "w" (update) privileges that are not necessary

## Group: SRG-APP-000381-DB-000361

**Group ID:** `V-213627`

### Rule: The EDB Postgres Advanced Server must produce audit records of its enforcement of access restrictions associated with changes to the configuration of the EDB Postgres Advanced Server or database(s).

**Rule ID:** `SV-213627r879754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to configuration, it would be difficult to identify attempted attacks and an audit trail would not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-213628`

### Rule: The EDB Postgres Advanced Server must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-213628r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats. A database cluster listens on a single port (usually 5444 for Postgres Plus Advanced Server). The Postgres Enterprise Manager (PEM) agents do not listen on ports, they only act as clients to the PEM server. The PEM server has two components (a repository which is a Postgres database) and a PHP application. The PHP application listens on a port configured in Apache, generally 8080 or 8443. The ports to check are: 1) The primary Postgres cluster port, 2) The PEM PHP port, and 3) The PEM Repository DB port. Generally 2 and 3 should be installed on an isolated management machine without access from anyone other than administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network functions, ports, protocols, and services supported by the DBMS. If any protocol is prohibited by the PPSM guidance and is enabled, this is a finding. Open "<postgresql data directory>/pg_hba.conf" in a viewer. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any rows have a TYPE that is "host" or "hostnossl", this is a finding. Execute the following SQL as enterprisedb: SHOW port; If the displayed port is not allowed, this is a finding.

## Group: SRG-APP-000389-DB-000372

**Group ID:** `V-213629`

### Rule: The EDB Postgres Advanced Server must require users to re-authenticate when organization-defined circumstances or situations require re-authentication.

**Rule ID:** `SV-213629r879762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication of an interactive user is the presentation of a Common Access Card (CAC) or other physical token bearing a valid, current, DoD-issued Public Key Infrastructure (PKI) certificate, coupled with a Personal Identification Number (PIN) to be entered by the user at the beginning of each session and whenever re-authentication is required. Without re-authentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user re-authenticate. In addition to the re-authentication requirements associated with session locks, organizations may require re-authentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring re-authentication are privilege escalation and role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If organization-defined circumstances or situations require re-authentication, and these situations are not configured to terminate existing logins to require re-authentication, this is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-213630`

### Rule: The EDB Postgres Advanced Server must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-213630r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. This requirement focuses on communications protection for the DBMS session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the root.crt certificate was issued by a valid DoD entity. > openssl x509 -in <postgresql data directory>/root.crt –text | grep –i “issuer”. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any issuers are listed that are not valid DoD certificate authorities, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-213631`

### Rule: The EDB Postgres Advanced Server must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-213631r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of the DBMS, operating system/file system, and additional software as relevant. If any of the information defined as requiring cryptographic protection from modification is not encrypted in a manner that provides the required level of protection, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-213632`

### Rule: The EDB Postgres Advanced Server must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-213632r879800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of the DBMS, operating system/file system, and additional software as relevant. If any of the information defined as requiring cryptographic protection from modification is not encrypted in a manner that provides the required level of protection, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-213633`

### Rule: The EDB Postgres Advanced Server must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-213633r879812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms. EDB Postgres Advanced Server provides native support for using SSL connections to encrypt client/server communications. To enable the use of SSL, the postgres “ssl” configuration parameter must be set to “on”, and the database instance needs to be configured to use a valid server certificate and private key installed on the server. With SSL enabled, connections made to the database server will default to being encrypted. However, it is possible for clients to override the default and attempt to establish an unencrypted connection. To prevent connections made from non-local hosts from being unencrypted, the postgres host-based authentication settings should be configured to only allow hostssl (i.e., encrypted) connections. The hostssl connections can be further configured to require that the client present a valid (trusted) SSL certificate for a connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. Open "<postgresql data directory>/pg_hba.conf" in a viewer or editor. (The default path for the postgresql data directory is /var/lib/ppas/9.5/data, but this will vary according to local circumstances.) If any rows do not have TYPE of "hostssl" as well as a METHOD of "cert", this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-213634`

### Rule: The EDB Postgres Advanced Server must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-213634r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, the DBMS, associated applications, and infrastructure must leverage protection mechanisms. EDB Postgres Advanced Server provides native support for using SSL connections to encrypt client/server communications. To enable the use of SSL, the postgres “ssl” configuration parameter must be set to “on” and the database instance needs to be configured to use a valid server certificate and private key installed on the server. With SSL enabled, connections made to the database server will default to being encrypted. However, it is possible for clients to override the default and attempt to establish an unencrypted connection. To prevent connections made from non-local hosts from being unencrypted, the postgres host-based authentication settings should be configured to only allow hostssl (i.e., encrypted) connections. The hostssl connections can be further configured to require that the client present a valid (trusted) SSL certificate for a connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. First, check if SSL is enabled for the database instance by executing the following command from a command prompt: psql -d <database name> -U <database superuser name> -c "SHOW ssl” Where, <database name> is any database in the EDB postgres instance and <database superuser name> is a database superuser. By default, a database named "edb" and a superuser named "enterprisedb" are installed with EDB Postgres Advanced Server (EPAS). If the result is not "on", this is a finding. Next, open the pg_hba.conf file in a viewer or editor and review the authentication settings that are configured in that file. Note the default location for the pg_hba.conf file is in the postgresql data directory. The location of the pg_hba.conf file for a running EDB postgres instance can be found using the following command run from a command prompt: psql -d <database name> -U <database superuser name> -c "SHOW hba_file" Where, <database name> is any database in the EDB postgres instance and <database superuser name> is a database superuser. By default, a database named "edb" and a superuser named "enterprisedb" are installed with EDB Postgres Advanced Server (EPAS). If any uncommented lines are not of TYPE "hostssl" and do not include the "clientcert=1" authentication option and are not documented in the system security plan or equivalent document as being approved, this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-213635`

### Rule: When invalid inputs are received, the EDB Postgres Advanced Server must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-213635r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SELECT * FROM sqlprotect.list_protected_users; If the database and user that handles user input is not listed or if sqlprotect.list_protected_users does not exist (meaning SQL/Protect is not installed), and an alternative means of reviewing for vulnerable code is not in use, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-213636`

### Rule: Security-relevant software updates to the EDB Postgres Advanced Server must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-213636r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Timeframes for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that software patches are obtained from EnterpriseDB and are consistently applied to the DBMS within the timeframe defined for each patch. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding. If an administrator is not registered on the EDB Support Portal with an email address for monitoring technical alerts, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-213637`

### Rule: The EDB Postgres Advanced Server must generate audit records when security objects are accessed.

**Rule ID:** `SV-213637r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-213638`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-213638r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000494-DB-000344

**Group ID:** `V-213639`

### Rule: The DBMS must generate audit records when categories of information (e.g., classification levels/security levels) are accessed.

**Rule ID:** `SV-213639r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000494-DB-000345

**Group ID:** `V-213640`

### Rule: Audit records must be generated  when unsuccessful attempts to access categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213640r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-213641`

### Rule: The EDB Postgres Advanced Server must generate audit records when privileges/permissions are added.

**Rule ID:** `SV-213641r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the REVOKE command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-213642`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-213642r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, adding permissions is typically done via the GRANT command, or, in the negative, the REVOKE command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-213643`

### Rule: The EDB Postgres Advanced Server must generate audit records when security objects are modified.

**Rule ID:** `SV-213643r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-213644`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-213644r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000498-DB-000346

**Group ID:** `V-213645`

### Rule: Audit records must be generated when categorized information (e.g., classification levels/security levels) is created.

**Rule ID:** `SV-213645r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000498-DB-000346

**Group ID:** `V-213646`

### Rule: Audit records must be generated when categorized information (e.g., classification levels/security levels) is modified.

**Rule ID:** `SV-213646r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000498-DB-000347

**Group ID:** `V-213647`

### Rule: Audit records must be generated when unsuccessful attempts to create categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213647r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000498-DB-000347

**Group ID:** `V-213648`

### Rule: Audit records must be generated when unsuccessful attempts to modify categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213648r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-213649`

### Rule: The EDB Postgres Advanced Server must generate audit records when privileges/permissions are deleted.

**Rule ID:** `SV-213649r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, deleting permissions is typically done via the REVOKE command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-213650`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-213650r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, deleting permissions is typically done via the REVOKE command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-213651`

### Rule: The EDB Postgres Advanced Server must generate audit records when security objects are deleted.

**Rule ID:** `SV-213651r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-213652`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-213652r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-213653`

### Rule: Audit records must be generated when categorized information (e.g., classification levels/security levels) is deleted.

**Rule ID:** `SV-213653r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000502-DB-000349

**Group ID:** `V-213654`

### Rule: Audit records must be generated when unsuccessful attempts to delete categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213654r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categorized information, such as classification or sensitivity level. If it is not, this is not applicable (NA). Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-213655`

### Rule: The EDB Postgres Advanced Server must generate audit records when successful logons or connections occur.

**Rule ID:** `SV-213655r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_connect; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-213656`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful logons or connection attempts occur.

**Rule ID:** `SV-213656r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to the DBMS. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_connect; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-213657`

### Rule: The EDB Postgres Advanced Server must generate audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-213657r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-213658`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur.

**Rule ID:** `SV-213658r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000505-DB-000352

**Group ID:** `V-213659`

### Rule: The EDB Postgres Advanced Server must generate audit records showing starting and ending time for user access to the database(s).

**Rule ID:** `SV-213659r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to know how long a user's (or other principal's) connection to the DBMS lasts. This can be achieved by recording disconnections, in addition to logons/connections, in the audit logs. Disconnection may be initiated by the user or forced by the system (as in a timeout) or result from a system or network failure. To the greatest extent possible, all disconnections must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_connect; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-213660`

### Rule: The EDB Postgres Advanced Server must generate audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-213660r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to the DBMS. Concurrent connections by the same user from multiple workstations may be valid use of the system; or such connections may be due to improper circumvention of the requirement to use the CAC for authentication; or they may indicate unauthorized account sharing; or they may be because an account has been compromised. (If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), then it is not mandatory to create additional log entries specifically for this.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_connect; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-213661`

### Rule: The EDB Postgres Advanced Server must be able to generate audit records when successful accesses to objects occur.

**Rule ID:** `SV-213661r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000507-DB-000357

**Group ID:** `V-213662`

### Rule: The EDB Postgres Advanced Server must generate audit records when unsuccessful accesses to objects occur.

**Rule ID:** `SV-213662r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; If the result is not "all" or if the current setting for this requirement has not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000508-DB-000358

**Group ID:** `V-213663`

### Rule: The EDB Postgres Advanced Server must generate audit records for all direct access to the database(s).

**Rule ID:** `SV-213663r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this context, direct access is any query, command, or call to the DBMS that comes from any source other than the application(s) that it supports. Examples would be the command line or a database management utility program. The intent is to capture all activity from administrative and non-standard sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following SQL as enterprisedb: SHOW edb_audit_statement; SHOW edb_audit_connect; SHOW edb_audit_disconnect; If the result is not "all" for any or if the current settings for this requirement have not been noted and approved by the organization in the system documentation, this is a finding.

## Group: SRG-APP-000514-DB-000381

**Group ID:** `V-213664`

### Rule: The EDB Postgres Advanced Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to provision digital signatures.

**Rule ID:** `SV-213664r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-3, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a FIPS-certified OpenSSL library is not installed, this is a finding. Run the command "cat /proc/sys/crypto/fips_enabled". If the output is not "1", this is a finding.

## Group: SRG-APP-000514-DB-000382

**Group ID:** `V-213665`

### Rule: The EDB Postgres Advanced Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to generate and validate cryptographic hashes.

**Rule ID:** `SV-213665r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-3, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a FIPS-certified OpenSSL library is not installed, this is a finding. Run the command "cat /proc/sys/crypto/fips_enabled". If the output is not "1", this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-213666`

### Rule: The EDB Postgres Advanced Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the requirements of the data owner.

**Rule ID:** `SV-213666r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-3, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a FIPS-certified OpenSSL library is not installed, this is a finding. Run the command "cat /proc/sys/crypto/fips_enabled". If the output is not "1", this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-213667`

### Rule: The EDB Postgres Advanced Server must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-213667r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Postgres Enterprise Manager (PEM) or another log collection tool is not installed and configured to automatically collect audit logs, this is a finding. Review the system documentation for a description of how audit records are off-loaded and how local audit log space is managed.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-213668`

### Rule: The EDB Postgres Advanced Server must be configured on a platform that has a NIST certified FIPS 140-2 ior 140-3 nstallation of OpenSSL.

**Rule ID:** `SV-213668r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>PostgreSQL uses OpenSSL for the underlying encryption layer. It must be installed on an operating system that contains a certified FIPS 140-2 or 140-3 distribution of OpenSSL. For other operating systems, users must obtain or build their own FIPS 140 OpenSSL libraries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the deployment incorporates a custom build of the operating system and PostgreSQL guaranteeing the use of FIPS 140-2 or 140-3 compliant OpenSSL, this is not a finding. If PostgreSQL is not installed on an OS found in the CMVP (https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules), this is a finding. If FIPS encryption is not enabled, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-259741`

### Rule: EDB Postgres Advanced Server products must be a version supported by the vendor.

**Rule ID:** `SV-259741r944425_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If new packages are available for PostgreSQL, they can be reviewed in the package manager appropriate for the server operating system: To list the version of installed PostgreSQL using psql: $ sudo su - postgres $ psql --version To list the current version of software for RPM: $ rpm -qa | grep postgres To list the current version of software for APT: $ apt-cache policy postgres All versions of PostgreSQL will be listed here: http://www.postgresql.org/support/versioning/ All security-relevant software updates for PostgreSQL will be listed here: http://www.postgresql.org/support/security/ If PostgreSQL is not at the latest version, this is a finding.

