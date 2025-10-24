# STIG Benchmark: MarkLogic Server v9 Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-220339`

### Rule: MarkLogic Server must limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types.

**Rule ID:** `SV-220339r960735_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.) Limiting Concurrent Requests with User Session Limits There is an option on each App Server (HTTP, ODBC, XDBC, and WebDAV Server) configuration to limit the number of concurrent requests a user can have against that App Server. A concurrent request is defined to be a request against that App Server from the same user while another request from the same user is still active. Each App Server has a concurrent request limit configuration parameter. The default is 0, which means there is no limit to the number of concurrent requests. The value must be an integer greater than or equal to 0. Setting the concurrent request limit configuration parameter to a value other than 0 limits the number of concurrent requests any user can run against that App Server to the specified number. For example, by setting the number to 3, any requests made by a user named Raymond while 3 requests from Raymond are running will fail with an exception. When the limit is reached, the application will throw a 403 (forbidden) error with the XDMP-REQUESTLIMIT exception.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system documentation specifies limits on the number of concurrent DBMS sessions per account by type of user. If it does not, assume a limit of 10 for database administrators and 2 for all other users. Check the concurrent-sessions settings in the MarkLogic. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the App Server to be checked resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. Select the App Server in which in which to check session limits. The App Server Configuration page displays. 5. Inspect the concurrent request limit field; a value of 0 means there is no concurrent request limit (unlimited), and this is a finding. 6. If a value other than 0 but not equal to the organization-defined number is set, this is a finding. 7. Repeat for all App Servers.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-220340`

### Rule: MarkLogic Server must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-220340r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Account management functions can also include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. The DBMS must be configured to automatically utilize organization-level account management functions and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements. MarkLogic Server can be configured so that users are authenticated using an external authentication protocol, such as Lightweight Directory Access Protocol (LDAP), Kerberos, or certificate. These external agents serve as centralized points of authentication or repositories for user information from which authorization decisions can be made. MarkLogic Server can be configured with multiple external security providers. A user only needs to authenticate with one of them to gain access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all accounts are authenticated by the organization-level authentication/access mechanism and not by the MarkLogic, this is not a finding. If there are any accounts managed by MarkLogic, review the system documentation for justification and approval of these accounts. If any MarkLogic-managed accounts exist that are not documented and approved, this is a finding. Check to see if MarkLogic is configured to use External Security from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the click the Security icon in the left tree menu. 2. Click the External Security icon. 3. If no External Security Configuration Object exists, this is a finding. 4. If at least one External Security Configuration Object exists, proceed to check all existing user accounts below. 5. Click the Security icon in the left tree menu. 6. Click the Users icon. 7. Select the user to check. 8. In the User Configuration window, verify that at least one external name for the user is defined in the External Name section, if no external names are defined and justification/approval does not exists for this account, this is a finding. 9. Repeat for all users.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-220341`

### Rule: MarkLogic Server must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-220341r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the DBMS. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy. MarkLogic Server uses a role-based security model. A user’s privileges and permissions are based on the roles assigned to the user. For background information on understanding the security model in MarkLogic Server, see Security Guide.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic settings to determine whether users are restricted from accessing objects and data they are not authorized to access. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click on the Security Icon. 2. Click the Users Icon. 3. Click on a User, and then click the Describe tab. 4. Verify the User has the appropriate Roles assigned per organization/user requirements and system documentation. 5. If the User is missing a required role or possesses a Role they do not require, this is a finding. 6. Repeat for all added Users.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-220342`

### Rule: MarkLogic Server must protect against a user falsely repudiating having performed organization-defined actions.

**Rule ID:** `SV-220342r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring the DBMS's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, shared account. MarkLogic Server includes an auditing capability. Auditing can be enabled to capture security-relevant events to monitor suspicious database activity or to satisfy applicable auditing requirements. Configure the generation of audit events by including or excluding MarkLogic Server roles, users, or documents based on URI. More information on auditing can be found here: https://docs.marklogic.com/guide/security/auditing</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of audit logs to determine whether auditing includes details identifying the individual user. If it does not, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit-enabled field. A value of false means there is no auditing identifying the individual user and this is a finding. 5. If audit enabled field is true, but the settings do not meet the DoD minimum requirements for non-repudiation, this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-220343`

### Rule: MarkLogic Server must be configured to provide audit record generation capability for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-220343r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing. MarkLogic Server includes an auditing capability. Auditing can be enabled to capture security-relevant events to monitor suspicious database activity or to satisfy applicable auditing requirements. The generation of audit events can be configured by including or excluding MarkLogic Server roles, users, or documents based on URI. Some actions that can be audited are the following: - Startup and shutdown of MarkLogic Server - Adding or removing roles from a user - Usage of amps - Starting and stopping the auditing system For the complete list of auditable events and their descriptions, see Auditing Events in the Administrator's Guide: https://docs.marklogic.com/guide/admin/auditing</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS auditing to determine whether organization-defined auditable events are being audited by the system. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means there is no auditing and this is a finding. 5. If audit enabled field is true, but the selected auditable events do not meet DoD minimum requirements, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-220344`

### Rule: MarkLogic Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-220344r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log, and can make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. MarkLogic Server includes an auditing capability. Auditing can be enabled to capture security-relevant events to monitor suspicious database activity or to satisfy applicable auditing requirements. The generation of audit events can be configured by including or excluding MarkLogic Server roles, users, or documents based on URI. Some actions that can be audited are the following: - Startup and shutdown of MarkLogic Server - Adding or removing roles from a user - Usage of amps - Starting and stopping the auditing system For the complete list of auditable events and their descriptions, see Auditing Events in the Administrator's Guide: https://docs.marklogic.com/guide/admin/auditing </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic settings and documentation to determine whether designated personnel are able to select which auditable events are being audited. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Users icon on the left tree menu. 3. Inspect the Roles assigned to the Users. If a User who is designated personnel does not have the admin role, this is a finding. 4. Inspect the Roles assigned to the Users. If a User who is not designated personnel has the admin role, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-220345`

### Rule: MarkLogic Server must be able to generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-220345r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MarkLogic security and audit configurations to verify that audit records are produced when privileges/permissions/role memberships are retrieved, if they are required by the system documentation or organizational policies. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means there is no auditing and this is a finding. 5. If audit enabled field is true, but the security-access audit event is not selected, this is a finding. 6. If security-access audit event is selected, but "failed events only" is selected in the outcome setting of the audit restrictions is selected, this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-220346`

### Rule: MarkLogic Server must be able to generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-220346r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. MarkLogic Server includes an auditing capability. Auditing can be enabled to capture security-relevant events to monitor suspicious database activity or to satisfy applicable auditing requirements. The generation of audit events can be configured by including or excluding MarkLogic Server roles, users, or documents based on URI. Some actions that can be audited are the following: - Startup and shutdown of MarkLogic Server - Adding or removing roles from a user - Usage of amps - Starting and stopping the auditing system For the complete list of auditable events and their descriptions, see Auditing Events in the Administrator's Guide: https://docs.marklogic.com/guide/admin/auditing</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MarkLogic is currently required to audit the retrieval of privilege/permission/role membership information, check the MarkLogic security and audit configurations to verify audit records are produced when the DBMS denies retrieval of privileges/permissions/role membership. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means there is no auditing and this is a finding. 5. If audit enabled field is true, but the security-access audit event is not selected, this is a finding. 6. If security-access audit event is selected, but "successful events only" is selected in the outcome setting of the audit restrictions is selected, this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-220347`

### Rule: MarkLogic Server must initiate session auditing upon startup.

**Rule ID:** `SV-220347r960888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is used when a user's activities are under investigation. To ensure all activity is captured during the periods when session auditing is in use, it must be in operation for the entire time the DBMS is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that MarkLogic session-level auditing and specific session audits are currently defined and session auditing is enabled; or if a third-party product is available for session auditing. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means there is no auditing, this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-220348`

### Rule: MarkLogic Server must shut down by default upon audit failure, to include the unavailability of space for more audit log records; or must be configurable to shut down upon audit failure.

**Rule ID:** `SV-220348r960915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When the need for system availability does not outweigh the need for a complete audit trail, the DBMS should shut down immediately, rolling back all in-flight transactions. Systems in which audit trail completeness is paramount will most likely be at a lower MAC level than MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. Sufficient auditing resources must be allocated to avoid a shutdown in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner has determined the need for system availability outweighs the need for a complete audit trail, this is not applicable. If the system is configured for High Availability (HA), and the application owner has determined the need for a complete audit trail outweighs the need for system availability, this is a finding. The following are the minimum configuration requirements for HA: - Failover enabled = True for the Group - Security database forests are configured with replica forests - Databases associated with the users application are configured with replica forests If HA is a requirement for Administrative functions: - App Services database forests are configured with replica forests - Modules database forests are configured with replica forests - Documents database forests are configured with replica forests - Triggers database forests are configured with replica forests Perform the check for HA from the MarkLogic Admin Interface with a user that holds administrative-level privileges: 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. On the Configuration tab, check the value of "failover enabled". True = HA can be enabled False = HA cannot be enabled 4. Click the Databases icon in the left tree menu. 5. Click the Security Database. 6. Click the Status Tab. 7. Review the Forest section: a. Count the number of forests with a state of "open". b. Count the number of forests with a state of "[sync|async|wait] replicating". c. The number of replicating forests should be greater than or equal to the number of open forests. 8. Repeat steps 4-7 for the user application databases (data/content, modules, triggers, etc.). 9. Repeat steps 4-7 for the following databases if HA is required for Administrative functions: - App Services - Modules - Documents - Triggers

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-220349`

### Rule: The audit information produced by MarkLogic Server must be protected from unauthorized read access.

**Rule ID:** `SV-220349r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to their advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions, utilizing file system protections, and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. When auditing is enabled, MarkLogic Server writes audit events to the AuditLog.txt file. Each host in a cluster maintains its own audit log files. Some actions might trigger multiple audit events, and those events might be logged over multiple hosts, as events are audited on the host in which the event occurs. For more information about the audit events, see Auditable Events. Note the following about the audit event log files: - Writes messages to AuditLog.txt file for various events. - Each event has a timestamp, event type, user, role, and other information relevant to the event (for example, document URI for document-read event). For an example of log entries, see Sample Audit Logs. - How often to rotate the audit files (similar to the log files, as described in Log Files) can be configured. - The Audit log files are stored in the same directory as the Access log files (port_AccessLog.txt) and the Error log files (ErrorLog.txt), which is in the <marklogic-data-dir>/Logs directory. These files are private to the host in which the audit event occurred. - View the current or any archived file log at any time using standard text file viewing tools. Additionally, the log files can be accessed from the Log tab on the main page of the Admin Interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review controls and permissions are sufficient to protect audit log files from unauthorized access at the operating-system level. Verify User ownership, Group ownership, and permissions on the "audit" file: > ls -al /var/opt/MarkLogic/Logs/AuditLog.txt If the User owner is not "daemon", this is a finding If the Group owner is not "daemon", this is a finding. If the directory is more permissive than 700, this is a finding.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-220350`

### Rule: The audit information produced by MarkLogic Server must be protected from unauthorized modification.

**Rule ID:** `SV-220350r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database. When auditing is enabled, MarkLogic Server writes audit events to the AuditLog.txt file. Each host in a cluster maintains its own audit log files. Some actions might trigger multiple audit events, and those events might be logged over multiple hosts, as events are audited on the host in which the event occurs. For more information about the audit events, see Auditable Events. Note the following about the audit event log files: - Writes messages to AuditLog.txt file for various events. - Each event has a timestamp, event type, user, role, and other information relevant to the event (e.g., document URI for document-read event). For an example of log entries, see Sample Audit Logs. - How often to rotate the audit files (similar to the log files, as described in Log Files) can be configured. - The Audit log files are stored in the same directory as the Access log files (port_AccessLog.txt) and the Error log files (ErrorLog.txt), which is in the <marklogic-data-dir>/Logs directory. These files are private to the host in which the audit event occurred. - View the current or any archived file log at any time using standard text file viewing tools. Additionally, the log files can be accessed from the Log tab on the main page of the Admin Interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review controls and permissions are sufficient to protect audit log files from unauthorized access at the operating-system level. Verify User ownership, Group ownership, and permissions on the "audit" file: > ls -al /var/opt/MarkLogic/Logs/AuditLog.txt If the User owner is not "daemon", this is a finding If the Group owner is not "daemon", this is a finding. If the directory is more permissive than 700, this is a finding.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-220351`

### Rule: The audit information produced by MarkLogic Server must be protected from unauthorized deletion.

**Rule ID:** `SV-220351r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data becomes compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods depending on system architecture and design. Some commonly employed methods include: ensuring log files employ the proper file system permissions, utilizing file system protections, restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys to make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. When auditing is enabled, MarkLogic Server writes audit events to the AuditLog.txt file. Each host in a cluster maintains its own audit log files. Some actions might trigger multiple audit events, and those events might be logged over multiple hosts, as events are audited on the host in which the event occurs. For more information about the audit events, see Auditable Events. Note the following about the audit event log files: - Writes messages to AuditLog.txt file for various events. - Each event has a timestamp, event type, user, role, and other information relevant to the event (for example, document URI for document-read event). For an example of log entries, see Sample Audit Logs. - How often to rotate the audit files (similar to the log files, as described in Log Files) can be configured. - The Audit log files are stored in the same directory as the Access log files (port_AccessLog.txt) and the Error log files (ErrorLog.txt), which is in the <marklogic-data-dir>/Logs directory. These files are private to the host in which the audit event occurred. - View the current or any archived file log at any time using standard text file viewing tools. Additionally, the log files can be accessed from the Log tab on the main page of the Admin Interface. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review controls and permissions are sufficient to protect audit log files from unauthorized access at the operating-system level. Verify User ownership, Group ownership, and permissions on the "audit" file: > ls -al /var/opt/MarkLogic/Logs/AuditLog.txt If the User owner is not "daemon", this is a finding If the Group owner is not "daemon", this is a finding. If the directory is more permissive than 700, this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-220352`

### Rule: MarkLogic Server must protect its audit features from unauthorized access.

**Rule ID:** `SV-220352r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. Access to audit tools must be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity. When auditing is enabled, MarkLogic Server writes audit events to the AuditLog.txt file. Each host in a cluster maintains its own audit log files. Some actions might trigger multiple audit events, and those events might be logged over multiple hosts, as events are audited on the host in which the event occurs. For more information about the audit events, see Auditable Events. Note the following about the audit event log files: - Writes messages to AuditLog.txt file for various events. - Each event has a timestamp, event type, user, role, and other information relevant to the event (for example, document URI for document-read event). For an example of log entries, see Sample Audit Logs. - How often to rotate the audit files (similar to the log files, as described in Log Files) can be configured. - Audit log files are stored in the same directory as the Access log files (port_AccessLog.txt) and the Error log files (ErrorLog.txt), which is in the <marklogic-data-dir>/Logs directory. These files are private to the host in which the audit event occurred. - View the current or any archived file log at any time using standard text file viewing tools. Additionally, the log files can be accessed from the Log tab on the main page of the Admin Interface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. Since MarkLogic Audit logs are stored in plain text files, this includes text editors provided by the OS. Alternatively, enable Encryption-at-Rest for the logs. This would ensure only individuals/systems with a valid encryption key may access the data within logs and audit files. If appropriate permissions and access controls are not applied to prevent unauthorized modification of these tools, and Encryption-at-Rest is not enabled for logs, this is a finding. Perform the check from the MarkLogic Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon on the left tree menu. 2. Click the Keystore tab. 3. If "logs encryption" is set to "off", this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-220353`

### Rule: MarkLogic Server must protect its audit configuration from unauthorized modification.

**Rule ID:** `SV-220353r960942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. Since MarkLogic Audit logs are stored in plain text files, this includes text editors provided by the OS. Alternatively, Encryption-at-Rest can be enabled for the logs. This would ensure only individuals/systems with a valid encryption key may access the data within logs and audit files. If appropriate permissions and access controls are not applied to prevent unauthorized modification of these tools, and Encryption-at-Rest is not enabled for logs, this is a finding. Perform the check from the MarkLogic Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon on the left tree menu. 2. Click the Keystore tab. 3. If "logs encryption" is set to "off", this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-220354`

### Rule: MarkLogic Server must protect its audit features from unauthorized removal.

**Rule ID:** `SV-220354r960945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys to make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. Since MarkLogic Audit logs are stored in plain text files, this includes text editors provided by the OS. Alternatively, Encryption-at-Rest can be enabled for the logs. This would ensure only individuals/systems with a valid encryption key may access the data within logs and audit files. If appropriate permissions and access controls are not applied to prevent unauthorized modification of these tools, and Encryption-at-Rest is not enabled for logs, this is a finding. Perform the check from the MarkLogic Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon on the left tree menu. 2. Click the Keystore tab. 3. If "logs encryption" is set to "off", this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-220355`

### Rule: MarkLogic Server must limit privileges to change software modules, including stored procedures, functions, and triggers, and links to software external to the DBMS.

**Rule ID:** `SV-220355r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify monitoring of changes to MarkLogic software libraries, related applications, and configuration files is done. If a third-party file automated tool is used, this is not a finding. To check for automated monitoring, issue the following command at a command prompt with a user that has administrative privileges: Check to see if the crond service is running for scheduling recurring tasks. If it is not running, this is a finding. > sudo systemctl status crond Check to see if ml-filechange-mon.sh is in the cron schedule, and runs frequently enough to meet System Security Plan (SSP) requirements. If the script is not scheduled to run, or does not run frequently enough to meet the SSP requirements, this is a finding. > sudo crontab -l | grep ml-filechange Check ml-filechange-mon.sh to verify email addresses have been configured to receive alerts. If no email addresses have been added, this is a finding. > grep "EMAIL_LIST" /path/to/ml-filechange-mon.sh

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-220356`

### Rule: MarkLogic Server software installation account must be restricted to authorized users.

**Rule ID:** `SV-220356r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application could have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling, granting access to, and tracking use of the MarkLogic software installation account. If access or use of this account is not restricted to the minimum number of personnel required or if unauthorized access to the account has been granted, this is a finding. At a command prompt, on the system where MarkLogic is installed run the following command: > ls -al /var/opt/MarkLogic If files are owned by the user "daemon", this is not a finding. If user is not "daemon", verify that Organization policy and system documentation states that a separate user is needed and approved.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-220357`

### Rule: MarkLogic Server software, including configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-220357r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application could potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens, and is threatened by, other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Only applications required for the functioning and administration, not use of, MarkLogic should be located in the same disk directory as the MarkLogic software libraries. Review the MarkLogic software library directories /opt/MarkLogic and /var/opt/MarkLogic and note other root directories located on the same disk directory or any subdirectories. If any non-MarkLogic software directories exist on the disk directory, examine or investigate their use. If any of the directories are used by other applications, including third-party applications that use MarkLogic, this is a finding. At a command prompt on the MarkLogic system, run the following commands: > ls /opt/MarkLogic If any directories exist that are not in the list below, this is a finding. Admin bin FlexRep include Lang Messages Apps Config HealthCheck Installer mlcmd Plugins Assets Converters java lib Modules Samples At a command prompt on the MarkLogic system, run the following commands: > ls /var/opt/MarkLogic If any directories exist that are not in the list below, this is a finding. kms Lib run Stage Forests Journals Label Logs Temp If other software is installed in those directories and is not approved by Org Policy, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-220358`

### Rule: MarkLogic Server objects (including but not limited to indexes, storage, functions, triggers, links to software external to the server, etc.) must be owned by database/MarkLogic Server principals authorized for ownership.

**Rule ID:** `SV-220358r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify accounts authorized to own database objects. Review accounts that own objects in the database(s). Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Users icon on the left tree menu. 3. Inspect the Users. If there is a User who is not authorized to own database objects, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-220359`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to indexes, storage, etc.) and logic modules (functions, triggers, links to software external to the MarkLogic Server, etc.) must be restricted to authorized users.

**Rule ID:** `SV-220359r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify the group(s)/role(s) established for MarkLogic modification and the list of users in those group(s)/roles. Identify the individuals authorized to modify the DBMS. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Users icon on the left tree menu. 3. Inspect the Users. If there is a User who is not authorized to own database objects, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-220360`

### Rule: Unused database components, DBMS software, and database objects must be removed.

**Rule ID:** `SV-220360r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of components and features installed with MarkLogic, and check for unused components or features. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Databases icon. 2. Inspect the list of databases. If there is an unused database, this is a finding. 3. Click the Forests icon. 4. Inspect the list of forests. If there is an unused forest, this is a finding. 5. Click the Groups >> [GroupName] >> App Servers 6. Inspect the list of app servers. If there is an unused database, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-220361`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-220361r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify whether external executables are being used. If so, check with the ISSO to determine if the use of the external executables (MLSQL/odbc client and Converters) is authorized. If it is not, this is a finding. To check for Converters, issue the following command at a command prompt with a user that has administrative privileges. > sudo yum info MarkLogicConverters If the command returns information on the version of MarkLogic converters installed, and use of this package has not been authorized, this is a finding. To check for MLSQL/odbc client, issue the following command at a command prompt with a user that has administrative privileges. > sudo yum info mlsqlodbc If the command returns information on the version of MLSQL odbc client install, and use of this package has not been authorized, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-220362`

### Rule: MarkLogic Server must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-220362r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS settings and local documentation for functions, ports, protocols, and services that are approved. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the App Server to check resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. Inspect the list of App Servers and associated Protocols and Ports. 5. If any App Server has an associated protocol or port that is not approved, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-220363`

### Rule: MarkLogic Server must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-220363r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings to determine whether organizational users are uniquely identified and authenticated when logging on/connecting to the system. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the App Server to be checked resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. Select each of the App Servers. 5. Inspect the selected authentication method. If "application-level" is selected and a user other than "nobody" (or equivalent) is set as the default user, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-220364`

### Rule: If MarkLogic Server authentication using passwords is employed, MarkLogic Server must enforce the DOD standards for password complexity and lifetime.

**Rule ID:** `SV-220364r1018604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS/enterprise authentication and identification must be used (SRG-APP-000023-DB-000001). Native DBMS authentication may be used only when circumstances make it unavoidable, and must be documented and Authorizing Official (AO)-approved. The DOD standard for authentication is DOD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DOD standards for password complexity and lifetime must be implemented. DBMS products that can inherit the rules for these from the operating system or access control program (e.g., Microsoft Active Directory) must be configured to do so. For other DBMSs, the rules must be enforced using available configuration parameters or custom code. Types of Authentication Control the authentication scheme for HTTP, WebDAV, ODBC, and XDBC App Servers. - Basic authentication is the typical authentication scheme for web applications. A user is prompted for a username and password when accessing an application page. In basic mode, the password is obfuscated but not encrypted. - Digest authentication works the same way as basic, but offers encryption of passwords sent over the network. A user is prompted for a username and password when accessing an application page. - The digest-basic authentication scheme uses the more secure digest scheme whenever possible, but reverts to basic authentication when needed. Some older browsers, for example, do not support digest authentication. The digest-basic scheme is also useful if basic authentication was previously used, but must be migrated to digest. The first time a user accesses the server after changing from basic to digest-basic authentication scheme, the server computes the digest password by extracting the relevant information from the credentials supplied in basic mode. - Certificate-based authentication requires internal and external users and HTTPS clients to authenticate to MarkLogic Server via a client certificate, either in addition to, or rather than a password. - Application-level authentication bypasses all authentication and automatically logs all users in as a specified default user. Specify the default user in the Admin Interface, and any users accessing the server automatically inherit the security attributes (roles, privileges, default permissions) of the default user. Application-level authentication is available on HTTP, ODBC, and WebDAV servers. - In Kerberos Ticket, the user is authenticated by Kerberos and a Kerberos session ticket is used to authenticate the user to access MarkLogic Server. - When SAML authentication is used, a client requests a resource from MarkLogic Server with no security context. MarkLogic redirects the authentication request to an Identity Provider, the Identity Provider prompts the user to login, if necessary, and sends the authentication request back to MarkLogic Server (the Service Provider) for validation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic settings to see if password authentication is being used, and whether password complexity and lifetime rules are being enforced. Check for MarkLogic Password Plugin from the MarkLogic Query Console with a user that holds administrative-level privileges. 1. Select "XQuery" in the Query Type drop down and copy the following code into the window: xquery version "1.0-ml"; import module namespace plugin = "http://marklogic.com/extension/plugin" at "/MarkLogic/plugin/plugin.xqy"; plugin:plugins("http://marklogic.com/xdmp/security/password-check") 2. Run the script. If the script returns "your query returned an empty sequence", then no password plugin is present. 3. If the script returns a file name or file names (e.g., password-check-minimum-length.xqy), then review the file/s in the <MarkLogic Home>/Plugins directory to verify compliance with DOD minimum password requirements. 4. Log in to the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 5. Click the Groups icon. 6. Click the group in which the App Server to be checked resides (e.g., Default). 7. Click the App Servers icon on the left tree menu. 8. Select each of the App Servers. 9. Inspect the selected authentication method, if "basic", "digestbasic", or "digest" is selected and there is not a custom password plugin, or if the password plugin does not meet DOD minimum requirements, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-220365`

### Rule: If passwords are used for authentication, the MarkLogic Server must transmit only encrypted representations of passwords.

**Rule ID:** `SV-220365r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords must be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database. MarkLogic Types of Authentication: Basic* Digest Digest-Basic* Certificate Application Level Kerberos Ticket SAML * Indicates that the authentication method allows the username and password to be transmitted in clear text. For more information on the types of authentication MarkLogic offers, follow this link: https://docs.marklogic.com/9.0/guide/security/authentication#id_14250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic configuration settings for encrypting passwords in transit across the network. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the App Server to be checked resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. Select each of the App Servers. 5. Inspect the selected authentication method, if "basic" or "digest-basic" is selected, this is a finding. If Application Level is selected and the application server is not configured for SSL, this is a finding

## Group: SRG-APP-000175-DB-000067

**Group ID:** `V-220366`

### Rule: MarkLogic Server, when utilizing PKI-based authentication, must validate certificates by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-220366r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. A certificate’s certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information resource/or CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses. Database Management Systems that do not validate certificates by performing RFC 5280-compliant certification path validation are in danger of accepting certificates that are invalid and/or counterfeit. This could allow unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS configuration to verify that certificates being accepted by the DBMS are validated by performing RFC 5280-compliant certification path validation, specifically periodic revocation list processing, with custom application code that performs these functions. To check for existing CRLs, use the MarkLogic QConsole and execute the following XQuery command against the Security Database: cts:uri-match("http://marklogic.com/xdmp/pki/crls/*") If there are CRLs, then it will return which CRLs are loaded, if not then it will return an empty sequence. If any required CRLs are missing, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-220367`

### Rule: MarkLogic Server must enforce authorized access to all PKI private keys stored/utilized by the DBMS.

**Rule ID:** `SV-220367r961041_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where the DBMS-stored private keys are used to authenticate the DBMS to the system’s clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man-in-the-middle attacks against the DBMS system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 or 140-3 validated cryptographic modules. All access to the private key(s) of the DBMS must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of the DBMS's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic configuration to determine whether SSL FIPS has been enabled. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon on the left tree menu. 2. Select the local cluster. Click the Configure tab and verify "ssl fips enabled" is set to true. If not, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-220368`

### Rule: MarkLogic Server must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations and protect classified information in accordance with the requirements of the data owner.

**Rule ID:** `SV-220368r961050_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of using encryption and digital signatures to protect data. Weak algorithms can be easily broken, and cryptographic modules that are not validated may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications, including DBMSs, using cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/ Satisfies: SRG-APP-000179-DB-000114, SRG-APP-000416-DB-000380</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic configuration to determine whether SSL FIPS has been enabled. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon. 2. In the Summary tab, if the value for "ssl fips enabled" is "false", this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-220369`

### Rule: MarkLogic Server must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-220369r961053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic settings to determine if non-organizational users are uniquely identified and authenticated. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Users icon on the left tree menu. 3. Inspect the Users; if there is a non-organizational user who is not uniquely identified, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-220370`

### Rule: MarkLogic Server must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-220370r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers, and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate MarkLogic User accounts to verify only Administrators have Administrative roles assigned and each Administrator has an individual account. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Users icon on the left tree menu. 3. Inspect the Users. If administrator and general user accounts are not separated, this is a finding.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-220371`

### Rule: MarkLogic Server must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-220371r961119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One class of man-in-the-middle, or session hijacking, attacks involves the adversary guessing at valid session identifiers based on patterns in known identifiers. The preferred technique for thwarting guesses at Session IDs is the generation of unique session identifiers using a FIPS 140-2 or 140-3 approved random number generator. However, it is recognized that available DBMS products do not all implement the preferred technique yet may have other protections against session hijacking. Therefore, other techniques are acceptable, provided they are demonstrated to be effective. MarkLogic Server uses OpenSSL to implement the Secure Sockets Layer (SSL v3) and Transport Layer Security (TLS v1) protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic settings to determine whether protections against man-in-the-middle attacks that guess at session identifier values are enabled. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the App Server to check resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. If any of the application servers has a "no" under the SSL column, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-220372`

### Rule: MarkLogic Server must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-220372r961128_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification. Encryption at rest protects data on media, that is, data at rest as opposed to data moving across a communications channel (data in motion). Increasing security risks and compliance requirements sometimes mandate the use of encryption at rest to prevent unauthorized access to data on disk. Encryption at rest can be configured to encrypt data, log files, and configuration files separately. Encryption is only applied to newly created files once encryption at rest is enabled, and does not apply to existing files without further action by the user. For existing data, a merge or re-index will trigger encryption of data, a configuration change will trigger encryption of configuration files, and log rotation will initiate log encryption. More information can be found here: https://docs.marklogic.com/guide/security/encryption</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. If full-disk encryption is being used, this is not a finding. Review system documentation to determine whether the system handles classified information. If the system does not handle classified information, the severity of this check should be downgraded to Category II. Review MarkLogic settings to determine whether controls exist to protect the confidentiality and integrity of data at rest in the database. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Databases icon. 2. Click the database to be checked. 3. If the "data encryption" drop-down is set to ON, this is not a finding, and no further checks need to be performed. 4. If the "data encryption" drop-down is set to OFF, continue the check. 5. If the "data encryption" drop-down is set to default-cluster, continue the check with the steps below: a. Click the Clusters icon. b. Click [Cluster Name]. c. Click the Keystore Tab. d. If the Cluster Default Encryption configuration is OFF, this is a finding. Findings Matrix ------------------------------------------------------- Database Cfg. | Cluster Cfg | Finding -------------------------------------------------------- ON | *Any* | No *Any* | Force | No Default-cluster | Default-on | No Default-cluster | Default-off | Yes Off | Default-on | Yes Off | Default-off | Yes

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-220373`

### Rule: Access to MarkLogic Server files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-220373r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure those files are not shared inappropriately and are not open to backdoor access and manipulation. Encryption at rest protects data on media, that is, data at rest as opposed to data moving across a communications channel, otherwise known as data in motion. Increasing security risks and compliance requirements sometimes mandate the use of encryption at rest to prevent unauthorized access to data on disk. Encryption at rest can be configured to encrypt data, log files, and configuration files separately. Encryption is only applied to newly created files once encryption at rest is enabled, and does not apply to existing files without further action by the user. For existing data, a merge or re-index will trigger encryption of data, a configuration change will trigger encryption of configuration files, and log rotation will initiate log encryption. For more information: See: https://docs.marklogic.com/guide/security/encryption</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. If full-disk encryption is being used, this is not a finding. Review system documentation to determine whether the system handles classified information. If the system does not handle classified information, the severity of this check should be downgraded to Category II. Review MarkLogic settings to determine whether controls exist to protect the confidentiality and integrity of data at rest in the database. From a command line at the OS level, verify User ownership, Group ownership, and permissions on the files: > ls -al /var/opt/MarkLogic/ If the User owner is not "daemon", and encryption at rest is not enabled, this is a finding. If the Group owner is not "daemon", and encryption at rest is not enabled, this is a finding. If the directory is more permissive than 750, and encryption at rest is not enabled, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Databases icon. 2. Click the database to be checked. 3. If the "data encryption" drop-down is set to ON, this is not a finding, and no further checks need to be performed. 4. If the "data encryption" drop-down is set to OFF, continue the check. 5. If the "data encryption" drop-down is set to default-cluster, continue the check with the steps below: a. Click the Clusters icon. b. Click [Cluster Name]. c. Click the Configure Tab. d. If the Cluster Default Encryption configuration is OFF, this is a finding. Findings Matrix ------------------------------------------------------- Database Cfg. | Cluster Cfg | Finding -------------------------------------------------------- ON | *Any* | No *Any* | Force | No Default-cluster | Default-on | No Default-cluster | Default-off | Yes Off | Default-on | Yes Off | Default-off | Yes

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-220374`

### Rule: MarkLogic Server must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-220374r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages must be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic settings and custom database code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group that is to be checked. 3. Check settings for "file log level" and "system log level". If "file log level" is set to "debug", "finer", or "finest", this is a finding. If "system log level" is set to "debug", "finer", or "finest", this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-220375`

### Rule: MarkLogic Server must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-220375r961272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, and it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MarkLogic supports role-based access control for all entities/documents maintained within the database. User roles and applied document permissions determine access. For example, if a document has read permission for role1 and read permission for role2, a user who possesses either role1 or role2 can read that document. Permissions in this example are evaluated using OR semantics. Adding a Compartment to a role ensures access controls are evaluated using AND semantics when determining user access to a given resource. This security level is applied to the entire document/resource. 1. Verify applicable roles are configured with the necessary access Compartments for the specified role. 2. Verify all documents inserted into the MarkLogic database have the applicable permission (Compartment) applied. If applicable roles do not have Compartments defined, this is a finding. If documents inserted into the database do not have the applicable document permissions (Compartments) applied, this is a finding. Additionally, MarkLogic can enforce Element Level Security and Element Redaction ensuring users can only access specific elements of information they are permitted to access. Data a user is not permitted to see may be redacted or excluded all together. Element Level Security also ensures document searches do not return results where the search value is within an Element the user does not have access to. This security level is applied to specified elements within a given document. When/where applicable: 1. Navigate to the MarkLogic Admin page >> Security >> Protected Paths. 2. Verify the applicable elements requiring additional protections are defined using an XQuery path expression (applicable for both XML and JSON document types). 3. Verify the applicable role(s) are added against the specified path expression. If specific document elements require additional protections and no Protected Paths or Protect Path roles are defined, this is a finding.

## Group: SRG-APP-000314-DB-000310

**Group ID:** `V-220376`

### Rule: MarkLogic Server must associate organization-defined types of security labels having organization-defined security label values with information in transmission.

**Rule ID:** `SV-220376r961275_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, and it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MarkLogic supports role-based access control for all entities/documents maintained within the database. User roles and applied document permissions determine access. For example, if a document has read permission for role1 and read permission for role2, a user who possesses either role1 or role2 can read that document. Permissions in this example are evaluated using "OR" semantics. Adding a Compartment to a role ensures access controls are evaluated using "AND" semantics when determining user access to a given resource. This security level is applied to the entire document/resource. 1. Verify applicable roles are configured with the necessary access Compartments for the specified role. 2. Verify all documents inserted into the MarkLogic database have the applicable permission (Compartment) applied. If applicable roles do not have Compartments defined, this is a finding. If documents inserted into the database do not have the applicable document permissions (Compartments) applied, this is a finding. Additionally, MarkLogic can enforce Element-Level Security and Element Redaction ensuring users can only access specific elements of information they are permitted to access. Data a user is not permitted to see may be redacted or excluded all together. Element-Level Security also ensures document searches do not return results where the search value is within an Element to which the user does not have access. This security level is applied to specified elements within a given document. When/where applicable: 1. Navigate to the MarkLogic Admin page >> Security >> Protected Paths. 2. Verify the applicable elements requiring additional protections are defined using an XQuery path expression (applicable for both XML and JSON document types). 3. Verify the applicable role(s) are added against the specified path expression. If specific document elements require additional protections and no Protected Paths or Protect Path roles are defined, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-220377`

### Rule: MarkLogic Server must prevent non-privileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-220377r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MarkLogic system documentation to obtain the definition of the database/DBMS functionality considered privileged in the context of the system in question. Review MarkLogic users and assigned roles 1. Navigate to the MarkLogic Admin page >> Security >> Roles. 2. Validate user-created roles have appropriate permissions/roles applied. 3. Navigate to the MarkLogic Admin page >> Security >> Users. 4. Verify user-created Users are only granted roles meeting their specific requirements and do not allow for unnecessary elevated privileges. If Users are assigned roles providing unnecessary elevated or privileged permissions, this is a finding. If Roles are defined with unnecessary elevated permissions, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-220378`

### Rule: Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only.

**Rule ID:** `SV-220378r961359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be utilized only where necessary and protected from misuse. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, MarkLogic does not allow any user to perform any actions within or against the system unless that user is assigned specific roles granting access/execution privileges. All read, update, or execute privileges are defined by specifying applicable system roles/permissions. 1. Verify MarkLogic user-defined modules are created and stored with applicable document permissions. 2. Verify users interacting with the system are assigned to roles with the least amount of privileges required for a given user. 3. Navigate to the MarkLogic Admin page >> Security >> Users. 4. Validate all system users are assigned to roles with the least amount of privileges necessary while allowing them to interact with system resources and perform applicable actions based upon their use case. If a user is assigned roles exceeding their required access/privilege level, this is a finding. If custom modules are stored with unnecessary elevated document permissions, this is finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-220380`

### Rule: MarkLogic Server must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-220380r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure sufficient storage capacity for the audit logs, the DBMS must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the DBMS and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Investigate whether there have been any incidents where the MarkLogic server ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-220381`

### Rule: MarkLogic Server must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-220381r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to the DBMS on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system configuration to determine if appropriate support staff are not notified immediately upon storage volume utilization reaching 75 percent. If the Organization is not using Ops Director, or a third-party tool for storage volume utilization/alerting, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-220382`

### Rule: MarkLogic Server must provide an immediate real-time alert to appropriate support staff of all audit failures.

**Rule ID:** `SV-220382r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. A failure of database auditing will result in either the database continuing to function without auditing or a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review OS scripts, or third-party monitoring software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000381-DB-000361

**Group ID:** `V-220383`

### Rule: MarkLogic Server must produce audit records of its enforcement of access restrictions associated with changes to the configuration of the DBMS or database(s).

**Rule ID:** `SV-220383r1018605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to configuration, it would be difficult to identify attempted attacks and an audit trail would not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MarkLogic security and audit configurations to verify that audit records are produced when other errors prevent attempts to change the configuration of the MarkLogic Server or database(s). Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means auditing is not enabled, this is a finding. 5. If the following audit events are not enabled, this is a finding: - Audit Configuration Change - Configuration Change - User Configuration Change 6. If the Audit Restrictions - Outcome is not Both, this is a finding. 7. If any Audit Restriction Inclusions/Exclusions are not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-220384`

### Rule: MarkLogic Server must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accordance with Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-220384r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network functions, ports, protocols, and services supported by MarkLogic for any that are prohibited by the PPSM guidance. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the App Servers icon on the left tree menu. 4. Inspect the Summary screen for the Type/Port/ and SSL configuration. 5. If any of the App Servers uses a protocol or port prohibited by the PPSM guidance, this is a finding.

## Group: SRG-APP-000400-DB-000367

**Group ID:** `V-220385`

### Rule: MarkLogic Server must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-220385r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic settings to determine whether the organization-defined limit for cached authentication is implemented. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the External Security icon. 3. Select each of the External Security providers. 4. For each of the providers inspect the cache timeout field, a value that does not match the organization-defined time limit is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-220386`

### Rule: MarkLogic Server must only accept end-entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-220386r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at https://public.cyber.mil/pki-pke/interoperability/. This requirement focuses on communications protection for the DBMS session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic settings to determine whether the server will accept non-DoD approved PKI end-entity certificates, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Security icon. 2. Click the Certificate Authorities icon. 3. If there are any PKI end-entity certificates that are not DoD approved, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-220387`

### Rule: MarkLogic Server must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-220387r1018556_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DBMSs handling data requiring data-at-rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review system settings to determine if any of the information defined as requiring cryptographic protection from modification, is not encrypted in a manner that provides the required level of protection. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Databases icon. 2. Click the database that is to be checked. 3. If the "data encryption" drop-down is set to ON, this is not a finding, and no further checks need to be performed. 4. If the "data encryption" drop-down is set to OFF, continue the check. 5. If the "data encryption" drop-down is set to default-cluster, continue the check with the steps below: a. Click on the Clusters icon. b. Click [Cluster Name]. c. Click the Keystore Tab. d. If the Cluster Default Encryption configuration is OFF, this is a finding. Findings Matrix ------------------------------------------------------- Database Cfg. | Cluster Cfg | Finding -------------------------------------------------------- ON | *Any* | No *Any* | Force | No Default-cluster | Default-on | No Default-cluster | Default-off | Yes Off | Default-on | Yes Off | Default-off | Yes

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-220388`

### Rule: MarkLogic Server must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-220388r1018557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>DBMSs handling data requiring data-at-rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information-at-rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review system settings to determine if any of the information defined as requiring cryptographic protection from modification, is not encrypted in a manner that provides the required level of protection. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Databases icon. 2. Click the database to be checked. 3. If the data encryption drop-down is set to ON, this is not a finding, and no further checks need to be performed. 4. If the data encryption drop-down is set to OFF, continue the check. 5. If the data encryption drop-down is set to default-cluster, continue the check with the steps below: a. Click the Clusters icon. b. Click [Cluster Name]. c. Click the Configure Tab. d. If the Cluster Default Encryption configuration is OFF, this is a finding. Findings Matrix ------------------------------------------------------- Database Cfg. | Cluster Cfg | Finding -------------------------------------------------------- ON | *Any* | No *Any* | Force | No Default-cluster | Default-on | No Default-cluster | Default-off | Yes Off | Default-on | Yes Off | Default-off | Yes

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-220389`

### Rule: Security-relevant software updates to MarkLogic Server must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-220389r1001008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and also to applications themselves not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs). MarkLogic releases full software package updates that include all relevant security updates as well as enhancements and bug fixes. Larger updates are usually released quarterly, with smaller updates provided as needed between quarterly releases. Security updates are not packaged separately.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that package updates are consistently applied to MarkLogic within the time frame defined for each patch. The most recent releases of MarkLogic Server can be found at https://help.marklogic.com. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. Check the MarkLogic version identified in the upper left side of the Admin Interface and compare it to the versions found on the MarkLogic website. Obtain evidence that package updates are consistently applied to MarkLogic within the time frame defined for each patch. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-220390`

### Rule: MarkLogic Server must be able to generate audit records when security objects are accessed.

**Rule ID:** `SV-220390r961791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic configuration to determine if audit records will be produced when security objects are accessed, to include reads, creations, modifications and deletions of data, and execution of logic. Perform the fix from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Verify audit enabled field is set to true. If the setting is not true, this is a finding. 5. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-220391`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-220391r961791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic configuration to determine if audit records will be produced when security objects are accessed, to include reads, creations, modifications and deletions of data, and execution of logic. Perform the fix from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Verify audit enabled field is set to true. If the setting is not true, this is a finding. 5. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding.

## Group: SRG-APP-000494-DB-000344

**Group ID:** `V-220392`

### Rule: MarkLogic Server must generate audit records when categories of information (e.g., classification levels/security levels) are accessed.

**Rule ID:** `SV-220392r961797_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS/database security and audit configurations to verify that audit records are produced when categories of information are accessed, to include reads, creations, modifications, and deletions. If they are not produced, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means there is no auditing identifying the individual user, this is a finding. 5. If audit enabled field is true but the document-read event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not both, this is a finding. 7. If the role that has been configured for the category of information is not included under the audit restriction roles, this is a finding.

## Group: SRG-APP-000494-DB-000345

**Group ID:** `V-220393`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to access categories of information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-220393r961797_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic security and audit configurations to verify that audit records are produced when the system denies attempts or when other errors prevent attempts to access categories of information, including reads, creations, modifications, and deletions. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means there is no auditing identifying the individual user, this is a finding. 5. If audit enabled field is true, but the document-read event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If the role that has been configured for the category of information is not included under the audit restriction roles, this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-220394`

### Rule: MarkLogic Server must generate audit records when privileges/permissions are added.

**Rule ID:** `SV-220394r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic security and audit configurations to verify that audit records are produced when privileges/permissions/role memberships are added. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means there is no auditing identifying the individual user and this is a finding. 5. If audit enabled field is true, but the user-role-addition event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-220395`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-220395r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic security and audit configurations to verify audit records are produced when the DBMS denies the addition of privileges/permissions/role membership or when other errors prevent the addition of privileges/permissions/role membership. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means auditing is not enabled, this is a finding. 5. If audit enabled field is true but the user-role-addition event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding.

## Group: SRG-APP-000495-DB-000328

**Group ID:** `V-220396`

### Rule: MarkLogic Server must generate audit records when privileges/permissions are modified.

**Rule ID:** `SV-220396r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when privileges/permissions/role memberships are modified. If they are not produced, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true but the permission-change, user-role-addition and user-role-removal events are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000495-DB-000329

**Group ID:** `V-220397`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to modify privileges/permissions occur.

**Rule ID:** `SV-220397r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when attempts to modify privileges/permissions/role memberships are denied. If they are not produced, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means auditing is not enabled, this is a finding. 5. If audit enabled field is true but the permission-change, user-role-addition, and user-role-removal events are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-220398`

### Rule: MarkLogic Server must generate audit records when security objects are modified.

**Rule ID:** `SV-220398r961803_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when security objects are modified. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the security-access event are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-220399`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-220399r961803_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when the system denies attempts or other errors prevent attempts to modify security objects. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true but the security-access event are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000498-DB-000346

**Group ID:** `V-220400`

### Rule: MarkLogic Server must generate audit records when categories of information (e.g., classification levels/security levels) are modified.

**Rule ID:** `SV-220400r961809_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when categories of information are modified. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field, a value of false means auditing is not enabled, this is a finding. 5. If audit enabled field is true but the document-update event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not both, this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000498-DB-000347

**Group ID:** `V-220401`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to modify categories of information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-220401r961809_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when the system denies attempts, other errors prevent attempts to modify categories of information. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true but the document-update event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-220402`

### Rule: MarkLogic Server must generate audit records when privileges/permissions are deleted.

**Rule ID:** `SV-220402r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when privileges/permissions/role memberships are removed, revoked, or denied to any user or role. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true but the user-role-removal event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-220403`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-220403r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when the system denies attempts to remove, revoke, or deny privileges/permissions/role membership, or when other errors prevent attempts to remove, revoke, or deny privileges/permissions/role membership to any user or role. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the user-role-removal event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-220404`

### Rule: MarkLogic Server DBMS must generate audit records when security objects are deleted.

**Rule ID:** `SV-220404r961818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when security objects are dropped. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the user-role-removal and security-access events are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-220405`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-220405r961818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when the system denies attempts, or when other errors prevent attempts to drop security objects. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the user-role-removal and security-access events are not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-220406`

### Rule: MarkLogic Server must generate audit records when categories of information (e.g., classification levels/security levels) are deleted.

**Rule ID:** `SV-220406r961821_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when categories of information are deleted. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the document-update event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000502-DB-000349

**Group ID:** `V-220407`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to delete categories of information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-220407r961821_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configurations to verify that audit records are produced when the system denies attempts, or when other errors prevent attempts to delete categories of information. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the document-update event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not both, this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-220408`

### Rule: MarkLogic Server must generate audit records when successful logons or connections occur.

**Rule ID:** `SV-220408r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MarkLogic audit settings to verify whether an audit record is generated each time a user (or other principal) logs on or connects to the DBMS, this is a finding. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to check resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the authentication-failure event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-220409`

### Rule: MarkLogic Server must generate audit records when unsuccessful logons or connection attempts occur.

**Rule ID:** `SV-220409r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to the DBMS. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit settings to verify an audit record is generated each time a user (or other principal) attempts but fails to log on or connect to the DBMS (including attempts where the user ID is invalid/unknown). Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enable and this is a finding. 5. If audit enabled field is true but the authentication-failure event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-220410`

### Rule: MarkLogic Server must generate audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-220410r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configuration to verify audit records are generated when privileged actions occur. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true but the security-access event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions, and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-220411`

### Rule: MarkLogic Server must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur.

**Rule ID:** `SV-220411r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MarkLogic security and audit configurations to verify that audit records are produced when the DBMS prevents attempted privileged actions. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the security-access event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-220412`

### Rule: MarkLogic Server must generate audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-220412r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to the DBMS. Concurrent connections by the same user from multiple workstations may be valid uses of the system, such connections may be due to improper circumvention of the requirement to use the CAC for authentication, may indicate unauthorized account sharing, or may be because an account has been compromised. (If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), then it is not mandatory to create additional log entries specifically for this.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic audit configuration to verify whether audit records are generated each time a user (or other principal) who is already connected to the DBMS logs on or connects to the DBMS from a different workstation. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If audit enabled field is true, but the security-access event is not selected, this is a finding. 6. Under the Audit Restrictions - Outcome section, verify the security-access event for auditing is set to "both". If the setting is not "both", this is a finding. 7. If any roles, URIs, or users are identified in audit restrictions and not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-220413`

### Rule: MarkLogic must be able to generate audit records when successful accesses to objects occur.

**Rule ID:** `SV-220413r961836_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review audit settings to verify objects identified by the application owner, for which access must be audited, are being audited. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Groups icon. 2. Click the group in which the configuration to be checked resides (e.g., Default). 3. Click the Auditing icon on the left tree menu. 4. Inspect the audit enabled field. A value of false means auditing is not enabled and this is a finding. 5. If any audit events identified in the System Security Plan are not enabled, this is a finding. 6. If the Audit Restrictions - Outcome is not Both, this is a finding. 7. If any Audit Restriction Inclusions/Exclusions are not documented in the System Security Plan, this is a finding.

## Group: SRG-APP-000514-DB-000381

**Group ID:** `V-220414`

### Rule: MarkLogic Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to provision digital signatures.

**Rule ID:** `SV-220414r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic configuration to verify use of NIST FIPS validated cryptographic modules to provision digital signatures. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon. 2. Click the local cluster. 3. If SSL FIPS enabled button is false, this is a finding.

## Group: SRG-APP-000514-DB-000382

**Group ID:** `V-220415`

### Rule: MarkLogic Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to generate and validate cryptographic hashes.

**Rule ID:** `SV-220415r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check MarkLogic configuration to verify use of a NIST FIPS validated cryptographic modules to generate and verify cryptographic hashes. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level-privileges. 1. Click the Clusters icon. 2. Click the local cluster. 3. If SSL FIPS enabled button is false, this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-220416`

### Rule: MarkLogic Server must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the requirements of the data owner.

**Rule ID:** `SV-220416r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database contains, or is intended to contain, unclassified information requiring confidentiality and cryptographic protection, check MarkLogic configuration to verify use of NIST FIPS validated cryptographic modules to provide this protection. Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. 1. Click the Clusters icon. 2. Click the local cluster. 3. If SSL FIPS enabled button is false, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-220417`

### Rule: MarkLogic Server must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-220417r961860_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine how audit records are offloaded. If the MarkLogic Server instance is not monitored by a third-party audit management tool, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-220418`

### Rule: MarkLogic Server must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-220418r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the DBMS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. The DBMS must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the applicable DoD security configuration and implementation guidance for the deployment environment. Asses the MarkLogic Server documentation and configuration in accordance with the applicable guidance. If MarkLogic is not configured in accordance with security configuration settings, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-265874`

### Rule: MarkLogic Server must be a version supported by the vendor.

**Rule ID:** `SV-265874r999528_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and interview the database administrator. Identify all database software components. Review the current version and release information; execute the following from the query console: xdmp:version(); --OR-- Perform the check from the MarkLogic Server Admin Interface with a user that holds administrative-level privileges. Version is displayed in the upper left corner of the console. Access the MarkLogic website to validate that the version is currently supported: https://developer.marklogic.com/products/support-matrix/ If the DBMS or any of the software components are not supported by the vendor, this is a finding.

