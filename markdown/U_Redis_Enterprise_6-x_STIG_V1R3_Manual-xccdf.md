# STIG Benchmark: Redis Enterprise 6.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-251183`

### Rule: Redis Enterprise DBMS must limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types.

**Rule ID:** `SV-251183r879511_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful denial-of-service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis sets this limit by default at 10k clients per shard. It reserves 32 for descriptors for internal use. The organization can set a limit based on its needs during the configuration. When the set limit is reached, Redis will deny all new incoming connections and inform senders "max number of clients reached". To check for maximum connections, run the following command: rladmin info db db:<insert_db_id> where db:1 would be: rladmin info db db:1 Search in the output for max_connections. If the max connections are greater than the organizationally defined value, this is a finding. Note: Redis Enterprise 6 does support multiple users; however, it does not support the ability to limit connections per user. If using Redis Cluster, the max number of connections remains 10k; however, each node will use two connections (incoming/outgoing).

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-251184`

### Rule: Redis Enterprise DBMS must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-251184r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to act on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Account management functions can also include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. The DBMS must be configured to automatically use organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise supports LDAP for access to the Redis Enterprise web UI. If all accounts are authenticated by the organization-level authentication/access mechanism and not by the DBMS, this is not a finding. LDAP can be checked by examining the process used during user login on the Redis web UI. If any accounts are managed by Redis Enterprise, review the system documentation for justification and approval of these accounts. Compare the documented accounts with those found on the system. If any Redis Enterprise-managed accounts exist that are not documented and approved, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-251185`

### Rule: Redis Enterprise DBMS must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-251185r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the DBMS. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine if accounts have been set with appropriate, organizationally defined role-based permissions. Compare these settings with the settings on the actual DB. To find the database id, run the command: rladmin status extra all. 1. Log in to Redis Enterprise. 2. Navigate to the access controls tab. 3. Verify that each user is assigned an appropriate role. If a user is not assigned an appropriate role, this is a finding. If the appropriate role is not assigned to a user, or the roles and permission settings are not documented, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-251186`

### Rule: Redis Enterprise DBMS must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-251186r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise discretionary access control is configured through the use of individual roles. Verify that enforcement of role-based access control (RBAC) is implemented. Review the system documentation to determine if accounts have been set with appropriate, organizationally defined Discretionary Access Control permissions. Compare these settings with the settings on the actual DB. 1. Log in to Redis Enterprise. 2. Navigate to the access controls tab. 3. Verify that each user is assigned a role. If a user is not assigned an appropriate role, this is a finding. If the appropriate access is not assigned to a user, or the access and permission settings are not documented, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-251187`

### Rule: Redis Enterprise DBMS must enforce access control lists, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-251187r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine what organizationally defined Access Control permissions should be in place. Compare these settings with the settings on the actual DB. 1. Log in to Redis Enterprise. 2. Navigate to the access controls tab >> redis acls 3. Review ACLs for appropriate rules. If ACL rules are not defined as appropriate in system documentation, this is a finding. 4. Review roles. 5. Verify that each role is assigned an appropriate ACL. If a role is not assigned an appropriate ACL, this is a finding. 6. Review users. 7. Verify that each user is assigned a role. If a user is not assigned an appropriate role, this is a finding. If any user accounts implicitly gain “Full Access” through the user/role/ACL relationship and are not authorized, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-251188`

### Rule: Redis Enterprise DBMS must prevent non-privileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-251188r879717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these. Redis Enterprise comes with a configurable role-based access control mechanism that allows users to be given specific roles. These roles provide various levels of permissions to security safeguards and countermeasures.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify this, perform the following steps: 1. Log in to the Redis Enterprise control plane. 2. Navigate to the access control tab. 3. Navigate to the users tab and review the roles for users. 4. For users without the need to modify the database, verify they are given a viewer or none for cluster management in the roles tab. 5. For users with access to databases, verify they are given the default role "Not Dangerous" or a more restrictive role that does not allow access to the dangerous command category. If a non-privileged user is granted a non-default role, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-251189`

### Rule: Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only.

**Rule ID:** `SV-251189r879719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be used only where necessary and protected from misuse. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. Redis Enterprise comes with the ability to run Redis Enterprise software modules within each database to extend the database functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that each database is not using these modules, perform the following steps: 1. Log in to the Redis Enterprise control plane. 2. Navigate to the databases tab. 3. Inspect each database for Redis modules within the database application. If the databases display "None" next to the Redis Modules field, no modules are installed. If a module is present and a necessary use case is not documented, this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-251190`

### Rule: Redis Enterprise DBMS must provide audit record generation capability for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-251190r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful login attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the organization documentation to determine the organization-defined auditable events. To validate the log of an event, check the logs tab for configuration actions within Redis Enterprise. On the Redis Enterprise UI: 1. Log in to Redis Enterprise. 2. Navigate to the logs page. 3. Review the logs as needed to verify they meet organizationally defined audit events. On the underlying server, logs may also be found in /var/opt/redislabs/log/<log_name> The eventlog.log and cnm_http log files contain all logs. To check, perform an event that should trigger an organizationally defined audit log. Review logs in the UI, and in /var/opt/redislabs/log/eventlog.log and /var/opt/redislabs/log/cnm_http.log for applicable event logs. Check DBMS auditing to determine whether organization-defined auditable events are being audited by the system. To check the current verbosity (log level), run the following command from the underlying node (as root): ccs-cli hget dmc:<node_id> log_level and ccs-cli hget dmc:<node_id> mgmt_log_level If the field does not exist it means the DMC is working with its default log_level which is "info". If the action is not captured in the logs page audit trail, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-251191`

### Rule: Redis Enterprise DBMS must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-251191r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Auditing alerts can be selected on Redis Enterprise. With the RBAC settings, by default, only the Admin group can configure these events in the database. Additional roles with admin privileges can also be configured. To view which roles have admin level privileges: 1. Log in to Redis Enterprise. 2. Navigate to the Access control tab and review the users listed therein. To view which alerts are configured: 1. Log in to Redis Enterprise. 2. Navigate to the Databases tab. 3. Select any database to view and select the configuration tab. 4. Scroll down to determine which Alerts are selected to be emailed to the appropriate audiences (if any). If designated personnel are not able to configure auditable events, this is a finding.

## Group: SRG-APP-000508-DB-000358

**Group ID:** `V-251192`

### Rule: Redis Enterprise DBMS must generate audit records for all direct access to the database(s).

**Rule ID:** `SV-251192r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this context, direct access is any query, command, or call to the DBMS that comes from any source other than the application(s) that it supports. Examples would be the command line or a database management utility program. The intent is to capture all activity from administrative and non-standard sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All local access to the server is handled by the underlying RHEL OS server that hosts the Redis Enterprise DBMS and is viewable in syslog. Additionally, RHEL can be configured to audit direct access to Redis Enterprise by modifying the rule set in /etc/audit/audit.rules to include the redis-cli and rladmin command found in /opt/redislabs/bin. To determine if the OS is auditing direct and privileged access/execution of the database and database configuration options on the server: cat to /etc/audit/audit.rules Examine the audit rules defined for rules that specify that command calls for /opt/redislabs/bin/redis-cli and /opt/redislabs/bin/rladmin are audited, if not present, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-251193`

### Rule: Redis Enterprise DBMS must use centralized management of the content captured in audit records generated by all components of Redis Enterprise DBMS.

**Rule ID:** `SV-251193r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with offloading the records to the centralized system. For more information, refer to: https://docs.redislabs.com/latest/rs/administering/logging/rsyslog-logging/ and https://redislabs.com/blog/sending-redis-cluster-alerts-to-slack-with-syslog/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are offloaded and how local audit log space is managed. Redis Enterprise leans on the RHEL host server rsyslog to unify and centralize logs as well as to send them to a centralized log management server or system. To verify that all of the logs are captured in syslog, view the redislabs.conf file in /etc/rsyslog.d. Verify that for each log produced by Redis Enterprise (found in /var/opt/redislabs/log), there is a line in redislabs.conf similar to: if $programname startswith '[Log name found in /var/opt/redislabs/log] ' then { action(type="omfile" file="/var/log/redislabs.log" template="RedisLabsEventTemplate" ) } To verify that Redis Enterprise is configured on the server to send all logs to a centralized log management system, examine the redislabs.conf file found in /etc/rsyslog.d. The file should include the line: action(type="omfwd" protocol="tcp" target="[organization defined logging server IP]" port="[organization defined logging server port]" template="RedisLabsEventTemplate" ) If redislabs.conf is not configured to capture all logs produced by Redis Enterprise or does not exist, this is a finding. If the Redis Enterprise audit records are not written directly to or systematically transfer to a centralized log management system, this is a finding.

## Group: SRG-APP-000356-DB-000315

**Group ID:** `V-251194`

### Rule: Redis Enterprise DBMS must provide centralized configuration of the content to be captured in audit records generated by all components of Redis Enterprise DBMS.

**Rule ID:** `SV-251194r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the configuration of the DBMS's auditing is spread across multiple locations in the database management software, or across multiple commands, only loosely related, it is harder to use and takes longer to reconfigure in response to events. Additional information can be found at: https://docs.redislabs.com/latest/rs/administering/logging/rsyslog-logging/ and https://redislabs.com/blog/sending-redis-cluster-alerts-to-slack-with-syslog/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise does not provide a distinct tool for audit configuration but leans on the RHEL host server rsyslog to unify and centralize the logs. Review the Redis Enterprise documentation specific to syslog configuration. By default, Redis Enterprise sends the Event_log.log file that captures all logged actions in the UI to rsyslog. To verify that all of the logs are captured in syslog, view the redislabs.conf file in /etc/rsyslog.d. The redislabs.conf file is used to centrally configure the log structure and what information is added to all log output. If redislabs.conf does not exist, this is a finding. Verify that the redislabs.conf file includes a defined template() line that specifies what should be captured in accordance with organizational standards. If no template is being used, or the template is not configured to capture log information to organizational standards (such as severity information, timestamp, machine name), this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-251195`

### Rule: Redis Enterprise DBMS must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-251195r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure sufficient storage capacity for the audit logs, the DBMS must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be offloaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the offloading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the DBMS and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are offloaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by offloaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review organization documentation to determine the organization-defined audit record storage requirements. By default, Redis Enterprise will use whatever disk space is allocated for audit logs. It is the responsibility of the organization to ensure that the RHEL OS server hosting the service has been allocated enough storage space to avoid running out of log space. Interview the system administrator and review audit log configuration and alerts to investigate whether there have been any incidents where the Redis Enterprise server ran out of audit log space since the last time the space was allocated, or other corrective measures were taken. If such incidents have occurred, this is a finding. Review the Redis Enterprise control pane as an admin user. If alerts are present indicating that storage is full or is at 95 percent full, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-251196`

### Rule: Redis Enterprise DBMS must offload audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility, and weekly or more often for stand-alone systems.

**Rule ID:** `SV-251196r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with offloading the records to the centralized system. For more information, refer to: https://docs.redislabs.com/latest/rs/administering/logging/rsyslog-logging/ and https://redislabs.com/blog/sending-redis-cluster-alerts-to-slack-with-syslog/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are offloaded. By default, all log entries shown on the log page in the Redis Enterprise UI are also written to syslog. Then, rsyslog can be configured to monitor the syslog. All alerts are logged to syslog if the alerts are configured to be enabled, in addition to other log entries. These logs can be configured to be offloaded to a centralized log management system. Verify that Redis Enterprise is configured on the server to send all logs to a centralized log management system by examining the redislabs.conf file found in /etc/rsyslog.d. The file should include the line: action(type="omfwd" protocol="tcp" target="[organization defined logging server IP]" port="[organization defined logging server port]" template="RedisLabsEventTemplate" ) If it does not, this is a finding. If the DBMS has a continuous network connection to the centralized log management system, but the DBMS audit records are not written directly to the centralized log management system or transferred in near-real-time, this is a finding. If the DBMS does not have a continuous network connection to the centralized log management system, and the DBMS audit records are not transferred to the centralized log management system weekly or more often, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-251197`

### Rule: Redis Enterprise DBMS must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-251197r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so under normal conditions, the audit space allocated to the DBMS on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that Redis Enterprise has been configured to send appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity: 1. Log in to the Redis Enterprise UI as a user with the Admin role. 2. Navigate to the Settings tab and then to Alerts. 3. Verify that the appropriate Alerts are enabled to notify support staff when storage volume reaches 75 percent. 4. Navigate to the General subtab and scroll down to verify that an email server is set up to send out alert notifications. 5. Lastly, navigate to the Access Control tab and verify that the appropriate users listed are configured to receive alert notifications. To view on a specific database: 1. Navigate to the Databases tab on the UI. 2. Select the Databases from the list and then select configuration. 3. Scroll down to view the Alert settings. Also verify that the RHEL server OS is STIG compliant to notify support staff when allocated audit record storage volume reaches 75 percent of the repository maximum audit record storage capacity. If appropriate support staff are not notified immediately upon storage volume utilization reaching 75 percent, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-251198`

### Rule: Redis Enterprise DBMS must provide an immediate real-time alert to appropriate support staff of all audit log failures.

**Rule ID:** `SV-251198r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise does not send immediate real-time alerts to support staff in the event of audit log failures; however, the host RHEL server can be configured to send such alerts using scripts or other third-party tools. It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the OS or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-251199`

### Rule: Redis Enterprise DBMS must by default shut down upon audit failure, to include the unavailability of space for more audit log records; or must be configurable to shut down upon audit failure.

**Rule ID:** `SV-251199r879571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise can be configured to generate alerts for certain other key events, but not in the instance of an audit failure. The DBMS would depend on the base Linux OS to detect and shut down in the event of an audit processing failure. It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When the need for system availability does not outweigh the need for a complete audit trail, the DBMS should shut down immediately, rolling back all in-flight transactions. Systems where audit trail completeness is paramount will most likely be at a lower MAC level than MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid a shutdown in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner has determined that the need for system availability outweighs the need for a complete audit trail, this is not applicable. Otherwise, review the procedures, manual and/or automated, for monitoring the space used by audit trail(s) and for offloading audit records to a centralized log management system. If the procedures do not exist, this is a finding. If the procedures exist, request evidence that they are followed. If the evidence indicates that the procedures are not followed, this is a finding. If the procedures exist, inquire if the system has ever run out of audit trail space in the last two years or since the last system upgrade, whichever is more recent. If it has run out of space in this period, and the procedures have not been updated to compensate, this is a finding.

## Group: SRG-APP-000109-DB-000321

**Group ID:** `V-251200`

### Rule: Redis Enterprise DBMS must be configurable to overwrite audit log records, oldest first (First-In-First-Out [FIFO]), in the event of unavailability of space for more audit log records.

**Rule ID:** `SV-251200r879571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the DBMS must continue generating audit records, if possible (automatically restarting the audit service if necessary), overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the DBMS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server. Systems where availability is paramount will most likely be MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid audit data loss in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise uses the default logrotate daemon to schedule rotation of logs stored on the operating system. The configuration of log rotation may be found at /etc/logrotate.d. By default, the log rotation should occur on a daily basis. Redis Labs recommends sending log files to a remote logging server so that they can be more effectively maintained. To check the log rotation policy, perform the following steps: 1. sudo cat /etc/logrotate.conf (The location of the log rotation configuration may vary depending on operating system distribution.) 2. Investigate the log rotation policy to verify that the appropriate policy is applied for all logs. Check to verify that log rotation is not disabled and is appropriate for the application by investigating the logrotated configuration. If log rotation is not enabled or is not configured appropriately, this is a finding.

## Group: SRG-APP-000374-DB-000322

**Group ID:** `V-251201`

### Rule: Redis Enterprise DBMS must record time stamps, in audit records and application data, that can be mapped to Coordinated Universal Time (UTC, formerly GMT).

**Rule ID:** `SV-251201r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the DBMS must include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. Some DBMS products offer a data type called TIMESTAMP that is not a representation of date and time. Rather, it is a database state counter and does not correspond to calendar and clock time. This requirement does not refer to that meaning of TIMESTAMP. Redis Enterprise application components allow the setting of a UTC timestamp associated with the logs of the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check the timestamp, perform the following steps: 1. Log in to the Redis Enterprise Control Plane. 2. Navigate to the settings tab. 3. Navigate to the general tab of the settings tab. 4. On screen find the Time zone setting. 5. Verify that the time zone is mapped to UTC. If the time zone isn't mapped to UTC, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-251202`

### Rule: The audit information produced by Redis Enterprise DBMS must be protected from unauthorized read access.

**Rule ID:** `SV-251202r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions, utilizing file system protections, and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To investigate the log files used by Redis Enterprise, perform the following steps: 1. SSH into the server running Redis Enterprise. 2. Issue the command cd /var/opt/redislabs/log 3. Issue the command ls -ltr ./ Investigate the permissions on these files. These permissions should be 640 or 660 and assigned to the installation user and group or another appropriate group. If the permissions are readable by other or assigned an inappropriate owner/group, this is a finding. Redis Enterprise does not support the ability to perform transaction logging.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-251203`

### Rule: The audit information produced by Redis Enterprise DBMS must be protected from unauthorized modification.

**Rule ID:** `SV-251203r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding user rights in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To investigate the log files used by Redis Enterprise, perform the following steps: 1. SSH into the server running Redis Enterprise. 2. Issue the command cd /var/opt/redislabs/log 3. Issue the command ls -ltr ./ Investigate the permissions on these files. These permissions should be 640 or 660 and assigned to the installation user and group or another appropriate group. If the permissions are readable by other or assigned an inappropriate owner/group, this is a finding. Redis Enterprise does not support the ability to perform transaction logging.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-251204`

### Rule: The audit information produced by Redis Enterprise DBMS must be protected from unauthorized deletion.

**Rule ID:** `SV-251204r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To investigate the log files used by Redis Enterprise stored on the operating system, perform the following steps: 1. SSH into the server running Redis Enterprise. 2. Issue the command cd /var/opt/redislabs/log 3. Issue the command ls -ltr ./ Investigate the permissions on these files. These permissions should be 640 or 660 and assigned to the installation user and group or another appropriate group. If the permissions are readable by other or assigned an inappropriate owner/group, this is a finding. Redis Enterprise does not support the ability to perform transaction logging. Redis Enterprise also provides configurable role-based access control inherently within the product. This is available to users with the cluster viewer. To verify that users are provided the appropriate permissions that they are authorized to use, check each user's assigned roles. 1. Log in to Redis Enterprise. 2. Navigate to the access controls tab. 3. Navigate to the users tab. 4. Review all roles assigned to a user and verify that user is given the appropriate role for their authorization level. Roles with the Cluster Management Role of admin, cluster_member, cluster_viewer, or db_member are able to view logs in the UI. If the user is not given the appropriate role, this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-251205`

### Rule: Redis Enterprise DBMS must protect its audit features from unauthorized access.

**Rule ID:** `SV-251205r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise does not come with unique tools to view log data and logging is not configurable. Logs are stored in a standard log file on the host operating system that is accessible using standard Linux tooling. Only users in the admin role can view or modify privileged settings in the Redis Enterprise UI. Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open-source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, they could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For validating privilege on the OS, verify user ownership, group ownership, and permissions on the Redis audit directory. From Linux command line as root: > ls - ald /var/opt/redislabs/log/ (or whatever the organizationally defined location for Redis logs) If the User owner is not a defined admin, this is a finding. If the Group owner is not a defined admin group, this is a finding. If the directory is more permissive than 700, this is a finding. For validating privileges on the control plane, verify Redis Admin users listed on the control plane against documented approved admin users. If any users have unauthorized admin privileges, this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-251206`

### Rule: Redis Enterprise DBMS must protect its audit configuration from unauthorized modification.

**Rule ID:** `SV-251206r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise does not come with unique tools to view log data and logging is not configurable. Logs are stored in a standard log file on the host operating system that is accessible using standard Linux tooling. Only users in the admin role can view or modify privileged settings in the Redis Enterprise UI. Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For validating privilege on the OS, verify user ownership, group ownership, and permissions on the redis audit directory. From Linux command line as root: > ls - ald /var/opt/redislabs/log/ (or whatever the organizationally defined location for Redis logs) If the User owner is not a defined admin, this is a finding. If the Group owner is not a defined admin group, this is a finding. If the directory is more permissive than 700, this is a finding. For validating privileges on the control plane, verify Redis Admin users that are listed on the control plane against documented approved admin users. If any users have unauthorized admin privileges, this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-251207`

### Rule: Redis Enterprise DBMS must protect its audit features from unauthorized removal.

**Rule ID:** `SV-251207r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise does not come with unique tools to view log data and logging is not configurable. Logs are stored in a standard log file on the host operating system that is accessible using standard Linux tooling. Only users in the admin role can view or modify privileged settings in the Redis Enterprise UI. Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For validating privilege on the OS, verify user ownership, group ownership, and permissions on the Redis audit directory: From Linux command line as root: > ls - ald /var/opt/redislabs/log/ (or whatever the organizationally defined location for Redis logs) If the User owner is not a defined admin, this is a finding. If the Group owner is not a defined admin group, this is a finding. If the directory is more permissive than 700, this is a finding. For validating privileges on the control plane, verify Redis Admin users that are listed on the control plane against documented approved admin users. If any users have unauthorized admin privileges, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-251208`

### Rule: Redis Enterprise DBMS must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-251208r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise permits the installation of logic modules through a control plane layer to the database, which requires privilege access to the control plane. This is provisioned for support during database runtime by a user with permissions to create a database. The ability to load modules directly within the database is not supported in Redis Enterprise; however, it is supported in open-source Redis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Modules may be added to the Redis Enterprise control plane (adminUI) by navigating to the settings tab and then modules. Only admin users can view the settings tab. To verify that users without explicit privileged status are not able to install modules, do the following: 1. Log in to the Redis Enterprise control plane (adminUI) with a user with administrative privileges. 2. Navigate to the access control tab. 3. Verify that only organizationally defined users have the appropriate privileges. If a user is not assigned appropriate permissions, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-251209`

### Rule: Redis Enterprise DBMS must enforce access restrictions associated with changes to the configuration of Redis Enterprise DBMS or database(s).

**Rule ID:** `SV-251209r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise is an application database and not intended to be used by human actors. Human actor activity has been generally abstracted to a control plane that resides outside of the database level. Redis Enterprise comes with roles for both the control plane and the data plane. Viewer roles and none provide access restrictions to make configuration changes to the database. To verify that users are in the appropriate role, perform the following steps: 1. Log in to the Redis Enterprise Control Plane. 2. Navigate to the access control tab. 3. Navigate to the users tab. 4. Verify that all users are assigned an appropriate role. If the principle is using custom roles, this may require investigating the permissions provided for each custom role. If it does not enforce access restrictions associated with changes to the configuration of the DBMS or database(s), this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-251210`

### Rule: Redis Enterprise DBMS must limit privileges to change software modules; to include stored procedures, functions, and triggers, and links to software external to Redis Enterprise DBMS.

**Rule ID:** `SV-251210r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations. For Redis Enterprise this is largely handled by the RHEL OS. The OS audit logs record any changes made to the database software libraries, related applications, and configuration files. Redis Enterprise also generates audit logs by default. All log entries are shown on the Log page in the Redis Enterprise web UI as well as written in the syslog. Only users in the admin role on the Redis Enterprise web UI and users with privileged access to the server can view, add, or remove modules. In both cases, this is logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RHEL server OS must be STIG-compliant to ensure only appropriate users have access. Verify user ownership, group ownership, and permissions on the directories where the Redis logs, binaries ,and modules reside: From Linux command line as root, perform the command ls –ald on the following directory paths: /var/opt/redislabs - Default storage location for the cluster data, system logs, backups and ephemeral, persisted data /var/opt/redislabs/log - System logs for Redis Enterprise Software /var/opt/redislabs/run - Socket files for Redis Enterprise Software /etc/opt/redislabs - Default location for cluster manager configuration and certificates /opt/redislabs - Main installation directory for all Redis Enterprise Software binaries /opt/redislabs/bin - Binaries for all the utilities for command line access and managements such as "rladmin" or "redis-cli" /opt/redislabs/config - System configuration files /opt/redislabs/lib - System library files /opt/redislabs/sbin - System binaries for tweaking provisioning If the user owner is not a defined admin, this is a finding. If the group owner is not a defined admin group, this is a finding. If the directory is more permissive than 700, this is a finding. Review monitoring procedures and implementation evidence to verify monitoring of changes to database software libraries, related applications, and configuration files is done. This is performed on the RHEL OS utilizing syslog. Verify the list of files, directories, and database application objects (procedures, functions, and triggers) being monitored is complete. If monitoring does not occur or the list of monitored objects is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-251211`

### Rule: Redis Enterprise DBMS software installation account must be restricted to authorized users.

**Rule ID:** `SV-251211r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To install the software, the user must have root level access to each node it will be installed on. Review the procedure used to install Redis Enterprise. In this procedure, users are capable of selecting their own user to own the software. Typically, this is run under a Redis Labs system user. To check this requirement, investigate the user used and verify that only the appropriate people are able to access this account on the host operating system. If more than the appropriate people can access this account, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-251212`

### Rule: Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-251212r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default directories that Redis Enterprise Software uses for data and metadata are: 1. /var/opt/redislabs - Default storage location for the cluster data, system logs, backups and ephemeral, persisted data 2. /var/opt/redislabs/log - System logs for Redis Enterprise Software 3. /var/opt/redislabs/run - Socket files for Redis Enterprise Software 4. /etc/opt/redislabs - Default location for cluster manager configuration and certificates 5. /tmp - Temporary files 6. /opt/redislabs - Main installation directory for all Redis Enterprise Software binaries 7. /opt/redislabs/bin - Binaries for all the utilities for command line access and managements such as "rladmin" or "redis-cli" 8. /opt/redislabs/config - System configuration files 9. /opt/redislabs/lib - System library files 10. /opt/redislabs/sbin - System binaries for tweaking provisioning To check this finding, examine the documentation for third-party applications and verify that no other applications are installed in these directories. It is recommended that Redis Enterprise be installed on a single tenant operating system. If another application is using these directories on the host operating system, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-251213`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to Redis Enterprise DBMS, etc.) must be restricted to authorized users.

**Rule ID:** `SV-251213r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations. Redis Enterprise provides configurable role-based access control inherently within the product. To ensure that users are provided the appropriate permissions that they are authorized to use, check each user's assigned roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check each user's assigned role: 1. Log in to Redis Enterprise. 2. Navigate to the access controls tab. 3. Navigate to the users tab. 4. Review all roles assigned to a user and verify that user is given the appropriate role for their authorization level. If the user is not given the appropriate role, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-251214`

### Rule: Redis Enterprise DBMS must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-251214r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the DBMS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across the DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this STIG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. The DBMS must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The organization that is implementing Redis Enterprise must review the documentation and configuration to determine if it is configured in accordance with DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs. If Redis Enterprise is not configured in accordance with security configuration settings, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-251215`

### Rule: Redis Enterprise DBMS must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-251215r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check this control, investigate the application documentation and understand what services and ports are in use within the application. Inspect the ports running on the server using the following command: sudo ss -tulw If any ports or services that are not approved are present in the output of this command, this is a finding. Redis Enterprise makes use of the following ports: 1. TCP 1968, Internal, Proxy traffic 2. TCP 3333, 3334, 3335, 3336, 3337, 3338, 3339, 36379, 36380, Internal, Cluster traffic 3. TCP 8001, Internal, External, Sentinel Traffic 4. TCP 8002, 8004, Internal, System health monitoring 5. TCP 8443 Internal, External, User Interface 6. TCP 8444, 9080, Internal, Proxy Traffic 7. TCP 9081. Internal, Active-Active 8. TCP 8070, 8071, Internal & External, Metrics Exporter 9. TCP 9443 (Recommended), 8080 (Recommended to be removed), REST API traffic 10. TCP 10000-19999, Internal, External, Active-Active Database traffic 11. TCP 20000-29999, Internal 12. UDP 53, 5353, Internal, External DNS/mDNS traffic

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-251216`

### Rule: Redis Enterprise products must be a version supported by the vendor.

**Rule ID:** `SV-251216r944390_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and interview the database administrator. Identify all database software components. Review the version and release information. 1. Log in to the adminUI console as an authorized user. 2. Navigate to the cluster tab and select configuration. 3. Check the version number next to Redis Labs Enterprise Cluster. Access the below Redis website or use other means to verify the version is still supported: https://docs.redislabs.com/latest/rs/administering/product-lifecycle If the DBMS or any of the software components are not supported by the vendor, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-251217`

### Rule: Unused database components, DBMS software, and database objects must be removed.

**Rule ID:** `SV-251217r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Modules are not needed for Redis Enterprise to function properly but can make some tasks easier. The following come by default on Redis Enterprise 6: RedisBloom RediSearch RedisGraph RedisJSON RedisTimeSeries More information can be found at: https://docs.redislabs.com/latest/modules/?s=modules</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise comes with a suite of capabilities sorted into modules. These modules can be removed if deemed unnecessary. Modules are not needed for Redis Enterprise to function properly but can make some tasks easier. Check the installed modules in the UI at the following location: 1. Log in to the Redis Enterprise UI as an Admin user. 2. Navigate to the Settings tab. 3. View the Redis Modules tab. If unused components or features are installed and are not documented and authorized, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-251218`

### Rule: Unused database components that are integrated in Redis Enterprise DBMS and cannot be uninstalled must be disabled.

**Rule ID:** `SV-251218r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS, and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/role permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise comes with a suite of capabilities sorted into modules. These modules can be removed if deemed unnecessary. Check the installed modules in the UI at the following location: 1. Log in to the Redis Enterprise UI as an Admin user. 2. Navigate to the Settings tab. 3. View the Redis Modules tab. If unused components or features are present on the system, can be disabled, and are not disabled, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-251219`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-251219r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise has this feature available if any object used is approved by the ISSO. By default, external executables are not included in Redis Enterprise, and only admin users on the Redis Enterprise web UI or admins who have direct access to the server can add them. To determine what modules or executables are applied: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the settings and then Redis modules tabs. Verify that no unapproved external executables exist. If external executables do exist and are not approved by the ISSO, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-251220`

### Rule: Redis Enterprise DBMS must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-251220r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check this control, investigate the application documentation and understand what services and ports are in use within the application. Inspect the ports running on the server using the following command: sudo ss -tulw If any ports or services that are not approved are present in the output of this command, this is a finding. Redis Enterprise makes use of the following ports: 1. TCP 1968, Internal, Proxy traffic 2. TCP 3333, 3334, 3335, 3336, 3337, 3338, 3339, 36379, 36380, Internal, Cluster traffic 3. TCP 8001, Internal, External, Sentinel Traffic 4. TCP 8002, 8004, Internal, System health monitoring 5. TCP 8443, Internal, External, User Interface 6. TCP 8444, 9080, Internal, Proxy Traffic 7. TCP 9081, Internal, Active-Active 8. TCP 8070, 8071, Internal & External, Metrics Exporter 9. TCP 9443 (Recommended), 8080 (Recommended to be removed), REST API traffic 10. TCP 10000-19999, Internal, External, Active-Active Database traffic 11. TCP 20000-29999, Internal 12. UDP 53, 5353, Internal, External DNS/mDNS traffic

## Group: SRG-APP-000389-DB-000372

**Group ID:** `V-251221`

### Rule: Redis Enterprise DBMS must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.

**Rule ID:** `SV-251221r879762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication of an interactive user is the presentation of a Common Access Card (CAC) or other physical token bearing a valid, current, DoD-issued Public Key Infrastructure (PKI) certificate, coupled with a Personal Identification Number (PIN) to be entered by the user at the beginning of each session and whenever reauthentication is required. Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring reauthentication are privilege escalation and role changes. For more information refer to: https://docs.redislabs.com/latest/rs/administering/access-control/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and the configuration of Redis Enterprise and related applications and tools. If the information owner has identified additional cases where reauthentication is needed, but there are circumstances where the system does not ask the user to reauthenticate when those cases occur, this is a finding. Redis Enterprise requires users to reauthenticate after the configured time-out period has been met, but does not require reauthentication when permissions are updated; permissions are automatically updated and applied on both the database and the Redis Enterprise web UI. Only admin users can modify privileges and roles.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-251222`

### Rule: Redis Enterprise DBMS must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-251222r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise allows the user to configure unique users per role. Review roles and ensure roles use unique organizational principles per user to the database. Redis does come with a default user for backwards compatibility. This user may be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To audit this configuration: 1. Log in to Redis Enterprise Administrative Control Plane. 2. Go to databases tab. 3. Select the desired database and then the configuration subtab. 4. Verify that Default database access is enabled. If it is enabled, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-251223`

### Rule: If passwords are used for authentication, Redis Enterprise DBMS must store only hashed, salted representations of passwords.

**Rule ID:** `SV-251223r879608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis stores and displays its user passwords in encrypted form, it also and transmits passwords as one-way hashed representations utilizing SHA256. Nevertheless, any User ID and Password stores should be verified by interviewing the DBA. Interview the DBA or ISSO and review any associated scripts, and applications defined within or external to the DBMS that access the database. The list must also include files, tables, or settings used to configure the operational environment for the DBMS and for interactive DBMS user accounts. Determine if any files contain database passwords. If any do, confirm that DBMS passwords stored internally or externally to the DBMS are encoded or encrypted. If any passwords are stored in clear text, this is a finding. Ask the DBA/System Administrator (SA)/Application Support staff if they have created an external password store for applications, batch jobs, and scripts to use on the database server. Verify that all passwords stored there are encrypted. If a password store is used and any password is not encrypted, this is a finding.

## Group: SRG-APP-000400-DB-000367

**Group ID:** `V-251224`

### Rule: Redis Enterprise DBMS must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-251224r879773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out of date, the validity of the authentication information may be questionable. For more information on configuring time out periods on Redis Enterprise refer to: https://docs.redislabs.com/latest/rs/administering/access-control/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system administrator to determine what, if any, the organizational policy is for cached authentication. By default, Redis Enterprise terminates authenticators after a user logs or times out. To view the current time out period for authentication, log in to the RHEL server that the Redis Enterprise database is hosted on as an admin user. 1. Type: rladmin 2. Once rladmin is started, type: info cluster Check documentation to verify that organizationally defined limits, if any, have been set. Compare documentation to actual settings found on the DB. If the settings do not match the documentation, this is a finding.

## Group: SRG-APP-000175-DB-000067

**Group ID:** `V-251225`

### Rule: Redis Enterprise DBMS, when utilizing PKI-based authentication, must validate certificates by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-251225r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses. Database Management Systems that do not validate certificates by performing RFC 5280-compliant certification path validation are in danger of accepting certificates that are invalid and/or counterfeit. This could allow unauthorized access to the database. For more information refer to: https://docs.redislabs.com/latest/rs/administering/designing-production/security/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At this time, Redis Enterprise does not support OSCP and is partially compliant with RFC 5280. Verify that the host operating system is encrypted. If the host operating system is not encrypted or STIG-compliant, this is a finding. To test, have the user log in to the database. If certificates are not being validated by performing RFC 5280-compliant certification path validation (i.e., "pop up" certificate validation), this is a finding. If the host operating system is encrypted, run the following commands and verify that only DoD-approved PKI certificates are present and used for Redis Enterprise: # cd /etc/opt/redislabs # cat proxy_cert.pem If no DoD-approved certificates are found, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-251226`

### Rule: Redis Enterprise DBMS must enforce authorized access to all PKI private keys stored/used by Redis Enterprise DBMS.

**Rule ID:** `SV-251226r879613_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where the DBMS-stored private keys are used to authenticate the DBMS to the system's clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man-in-the-middle attacks against the DBMS system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 or 140-3 validated cryptographic modules. All access to the private key(s) of the DBMS must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of the DBMS's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
All keys must be stored by the host RHEL OS that Redis Enterprise resides on. On the server, look for proxy_cert.pem found in /etc/opt/redislabs. If proxy_cert.pem has file permissions that would allow unauthorized users to access it, this is a finding. Keys can also be manipulated on the Redis Enterprise UI. RBAC prevents unauthorized users from doing this; to check: Review organization documentation to determine which users should have administrative privileges. From there: 1. Log in to Redis Enterprise UI as a user in the administrator role. 2. Navigate to the Access Control tab. 3. Compare the documented users to the users found in the user settings on the web UI. If any users have administrative privileges and are not documented, this is a finding. If access to the DBMS's private key(s) is not restricted to authenticated and authorized users, this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-251227`

### Rule: Redis Enterprise DBMS must map the PKI-authenticated identity to an associated user account.

**Rule ID:** `SV-251227r879614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to a DBMS user account for the authenticated identity to be meaningful to the DBMS and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Redis Enterprise configuration to verify user accounts are being mapped directly to unique identifying information within the validated PKI certificate. To test, have the user log in to the database and verify that the unique certificate to the authenticating user is used or prompted. If user accounts are not being mapped to authenticated identities, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-251228`

### Rule: Redis Enterprise DBMS must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-251228r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Normally, with PKI authentication, the interaction with the user for authentication will be handled by a software component separate from the DBMS, such as ActivID ActivClient. However, in cases where the DBMS controls the interaction, this requirement applies. To prevent the compromise of authentication information such as passwords and PINs during the authentication process, the feedback from the system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided authentication secrets when typed into the system is a method used in addressing this risk. Displaying asterisks when a user types in a password or a smart card PIN is an example of obscuring feedback of authentication secrets. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all interaction with the user for purposes of authentication is handled by a software component separate from the DBMS, this is not a finding. The Redis Enterprise web UI does inherently obscure passwords. For Redis CLI, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations and that AO approval has been obtained. If not, this is a finding. Request evidence that all users of the tool are trained in the importance of using the "--askpass" option (and not using the plain-text password option), how to keep the password hidden, and that they adhere to this practice. If not, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-251229`

### Rule: Redis Enterprise DBMS must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-251229r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/ For more detailed information on Redis, refer to: https://docs.redislabs.com/latest/rs/administering/designing-production/security/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Redis Enterprise configuration to verify it is using NIST FIPS validated cryptographic modules for cryptographic operations. Redis Enterprise uses TLS 1.2 and has a cyber suite of options that is configurable through the rladmin, REST API, and on the Redis Enterprise web UI. Verify the host operating system is encrypted. If the host operating system is not encrypted, this is a finding. If the host operating system is encrypted, run the following commands and verify that only DoD-approved PKI certificates are present: # cd /etc/opt/redislabs # ls Verify the following file is present: proxy_cert.pem If no certificates are present, this is a finding. Verify TLS is configured to be used. To check this: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the Databases tab and select the database and then configuration. 3. Review the configuration and verify that TLS is enabled for all communications. If TLS is not configured to be used, this is a finding. To check the current TLS version, run the following commands on one of the servers that is hosting Redis Enterprise as a privileged user: # ccs-cli # hgetall min_control_tls_version If TLS is not FIPS compliant, this is a finding. To validate the openssl version, run the following command on one of the servers that is hosting Redis Enterprise as a privileged user: # openssl version If NIST FIPS validated modules are not being used for all cryptographic operations, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-251230`

### Rule: Redis Enterprise DBMS must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-251230r879617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise databases can be configured and set to deny by default posture. Access is granted when the database is configured and can be granted by admins at a later time. Verify in the database configuration that the default user is disabled. This would force non-organizational users to authenticate with a username and password similar to any organizationally defined user. In web UI: 1. Log in to Redis Enterprise as an admin user. 2. Select the Database tab. 3. Select the Configuration subtab. 4. Confirm "Default database access" reads "nopass" and is "Inactive". If default database access is active and there is no password set, this is a finding.

## Group: SRG-APP-000416-DB-000380

**Group ID:** `V-251231`

### Rule: Redis Enterprise DBMS must use NSA-approved cryptography to protect classified information in accordance with the data owners requirements.

**Rule ID:** `SV-251231r879944_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. NSA-approved cryptography for classified networks is hardware based. This requirement addresses the compatibility of a DBMS with the encryption devices. Redis Enterprise does not encrypt data at rest. Redis Enterprise encryption of data at rest is handled by the underlying Linux OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the organization requires encryption. If Redis is deployed in an unclassified environment, this is not applicable. Determine if FIPS mode is enabled with the following command: # sudo fipscheck usage: fipscheck [-s <hmac-suffix>] <paths-to-files> fips mode is on If FIPS mode is "on", determine if the kernel command line is configured to use FIPS mode with the following command: # sudo grep fips /boot/grub2/grub.cfg /vmlinuz-3.8.0-0.40.el7.x86_64 root=/dev/mapper/rhel-root ro rd.md=0 rd.dm=0 rd.lvm.lv=rhel/swap crashkernel=auto rd.luks=0 vconsole.keymap=us rd.lvm.lv=rhel/root rhgb fips=1 quiet If the kernel command line is configured to use FIPS mode, determine if the system is in FIPS mode with the following command: # sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "on", the kernel command line does not have a FIPS entry, or the system has a value of "0" for "fips_enabled" in "/proc/sys/crypto", this is a finding.

## Group: SRG-APP-000514-DB-000381

**Group ID:** `V-251232`

### Rule: Redis Enterprise DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to provision digital signatures.

**Rule ID:** `SV-251232r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DBMS relies on the underlying operating system's cryptographic modules to provision digital signatures. Verify the operating system implements DoD-approved encryption to protect the confidentiality of remote access sessions. Determine if FIPS mode is enabled with the following command: # sudo fipscheck usage: fipscheck [-s <hmac-suffix>] <paths-to-files> fips mode is on If FIPS mode is "on", determine if the kernel command line is configured to use FIPS mode with the following command: # sudo grep fips /boot/grub2/grub.cfg /vmlinuz-3.8.0-0.40.el7.x86_64 root=/dev/mapper/rhel-root ro rd.md=0 rd.dm=0 rd.lvm.lv=rhel/swap crashkernel=auto rd.luks=0 vconsole.keymap=us rd.lvm.lv=rhel/root rhgb fips=1 quiet If the kernel command line is configured to use FIPS mode, determine if the system is in FIPS mode with the following command: # sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "on", the kernel command line does not have a FIPS entry, or the system has a value of "0" for "fips_enabled" in "/proc/sys/crypto", this is a finding.

## Group: SRG-APP-000514-DB-000382

**Group ID:** `V-251233`

### Rule: Redis Enterprise DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to generate and validate cryptographic hashes.

**Rule ID:** `SV-251233r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DBMS relies on the underlying operating system's file integrity tools use of cryptographic hashes for verifying file contents and directories have not been altered. These hashes must be FIPS-compliant cryptographic hashes. Determine if FIPS mode is enabled with the following command: # sudo fipscheck usage: fipscheck [-s <hmac-suffix>] <paths-to-files> fips mode is on If FIPS mode is "on", determine if the kernel command line is configured to use FIPS mode with the following command: # sudo grep fips /boot/grub2/grub.cfg /vmlinuz-3.8.0-0.40.el7.x86_64 root=/dev/mapper/rhel-root ro rd.md=0 rd.dm=0 rd.lvm.lv=rhel/swap crashkernel=auto rd.luks=0 vconsole.keymap=us rd.lvm.lv=rhel/root rhgb fips=1 quiet If the kernel command line is configured to use FIPS mode, determine if the system is in FIPS mode with the following command: # sudo cat /proc/sys/crypto/fips_enabled 1 If FIPS mode is not "on", the kernel command line does not have a FIPS entry, or the system has a value of "0" for "fips_enabled" in "/proc/sys/crypto", this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-251234`

### Rule: Redis Enterprise DBMS must implement NIST FIPS 140-2 or 140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the data owners requirements.

**Rule ID:** `SV-251234r879885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-2 or Publication 140-3, Security Requirements for Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant. The DBMS relies on the underlying Linux operating system to meet this check.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system implements FIPS compliant cryptographic modules. As the system administrator, run the following to determine if FIPS is enabled: # cat /proc/sys/crypto/fips_enabled If fips_enabled is not 1, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-251235`

### Rule: Redis Enterprise DBMS must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-251235r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers and typically requires privileged user access.  The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise provides separate user functionality by default. An administrative control plane helps facilitate configuration and a database layer helps facilitate application integrations with the database. This functionality is provided by default; however, the same user may be used for both the database layer and the administrative control plane. First, obtain the list of authorized admin users and general users. To check user functionality, perform the following steps: 1. Log in to the administrative control plane. 2. Navigate to the access controls tab. 3. Navigate to the roles tab. 4. Review all roles and verify that any role that provides access to the data path is configured with the cluster management role of "None". If a role provides access to both data and management paths, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-251236`

### Rule: Access to the Redis Enterprise control plane must be restricted.

**Rule ID:** `SV-251236r879631_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user. The Redis administrative control plane helps facilitate configuration and application integrations with the database. Exposing the control plane application to any network interface that is available to non-administrative personnel leaves the server vulnerable to attempts to access the management application. To mitigate this risk, the management application must only be run on network interfaces tied to a dedicated management network or firewall rule to limit access to dedicated trusted machines. Redis does not provide a configuration setting that can be used to restrict access to the administrative control plane, so firewall controls must be applied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation (SSP) and identify the documented management networks as well as the documented client networks. A management network can be defined through physical means or logical means to achieve network separation. Check the network interface to verify the administrative console is on a separate management network interface. If the control plane is set up to only be accessed via a defined management network, this is not a finding. If a management network does not exist or network separation is not established, verify the control plane can only be accessed via trusted approved machines. Review system documentation and obtain a list of approved machines for administrator use. Check the firewall rules on the server. An example command is: firewall-cmd --list-all Check for rules showing that only the trusted and approved machines have access to the ports for the control plane (default is 8443) and REST API interface (default 9443). Below is an example of the output: rich rules: rule family="ipv4" source address="<trusted ip>" forward-port port="8443" protocol="tcp" to-port="80" rule family="ipv4" source address="<trusted ip>" forward-port port="9443" protocol="tcp" to-port="80" If access is not limited using a management network, network separation such as vlans, or a firewall rule, this a finding.

## Group: SRG-APP-000223-DB-000168

**Group ID:** `V-251237`

### Rule: Redis Enterprise DBMS must recognize only system-generated session identifiers.

**Rule ID:** `SV-251237r879638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement focuses on communications protection for the DBMS session rather than for the network packet. The intent of this control is to establish grounds for confidence at each end of a communications session in the ongoing identity of the other party and in the validity of the information being transmitted. Redis Enterprise Software (RS) uses self-signed certificates out-of-the-box to make sure that sessions are secure by default. When using the default self-signed certificates, an untrusted connection notification is shown in the web UI. Depending on the browser used, the user can allow the connection for each session or add an exception to make the site trusted in future sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, each cluster node has a different set of self-signed certificates. These certificates can be replaced with a DoD-acceptable certificate, preferably a certificate issued by an intermediate certificate authority (CA). For security reasons, Redis Enterprise only supports the TLS protocol. Therefore, verify that the Redis client or secured tunnel solution is TLS v1.2 or above. Run the following commands and verify that certificates are present: # cd /etc/opt/redislabs # ls Verify the proxy_cert.pem file is present. If no certificates are present, this is a finding.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-251238`

### Rule: Redis Enterprise DBMS must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-251238r879639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session IDs are tokens generated by web applications to uniquely identify an application user's session. Applications will make application decisions and execute business logic based on the session ID. Unique session identifiers or IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session IDs help to reduce predictability of said identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attackers are unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. When a user logs out, or when any other session termination event occurs, the application must terminate the user session to minimize the potential for an attacker to hijack that particular user session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise Software (RS) can use industry-standard encryption to protect data in transit between a Redis client and RS. For this purpose, RS uses transport layer security (TLS) protocol. Run the following commands and verify certificates are present: # cd /etc/opt/redislabs # ls Verify the proxy_cert.pem file is present. If no certificates are found, this is a finding. Verify that TLS is configured to be used. To check this: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the Databases tab and select the database and then configuration. 3. Review the configuration and verify that TLS is enabled for all communications. If TLS is not configured to be used, this is a finding. To check the current TLS version, run the following commands on one of the servers that is hosting Redis Enterprise as a privileged user: # ccs-cli # hgetall min_control_tls_version If TLS is not FIPS compliant, this is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-251239`

### Rule: Redis Enterprise DBMS must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-251239r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise Software (RS) can use industry-standard encryption to protect data in transit between a Redis client and RS. For this purpose, RS uses transport layer security (TLS) protocol. Run the following commands and verify certificates are present: # cd /etc/opt/redislabs # ls Verify that all present certificates are issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs). If non DoD-approved PKI certificates are found, this is a finding. Verify TLS is configured to be used. To check this: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the Databases tab and select the database and then configuration. 3. Review the configuration and verify that TLS is enabled for all communications. If TLS is not configured to be used, this is a finding. To check the current TLS version, run the following commands on one of the servers that is hosting Redis Enterprise as a privileged user: # ccs-cli # hgetall min_control_tls_version If TLS is not FIPS compliant, this is a finding.

## Group: SRG-APP-000225-DB-000153

**Group ID:** `V-251240`

### Rule: Redis Enterprise DBMS must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-251240r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Databases must fail to a known consistent state. Transactions must be successfully completed or rolled back. All data is stored and managed exclusively in either RAM or RAM + Flash Memory (Redis on Flash) and therefore, is at risk of being lost upon a process or server failure. As Redis Enterprise Software is not just a caching solution, but also a full-fledged database, persistence to disk is critical. Therefore, Redis Enterprise Software supports persisting data to disk on a per-database basis. Append Only File (AOF) is a continuous writing of data to disk Snapshot. It is not a replacement for backups but should be done in addition to backups. AOF writes the latest "write" commands into a file either every second or during every write. It resembles a traditional RDBMS's redo log. This file can later be replayed to recover from a crash. To ensure data availability, Redis Enterprise Software must be implemented in, at a minimum, a three-node cluster. A three-node cluster can withstand one node failure without data loss. If more than one node is lost in a three-node cluster and persistence is not enabled, then data loss is to be expected. The Append Only File is a persistence mode that provides much better durability. For instance, using the default data fsync policy, Redis can lose just one second of writes in a dramatic event like a server power outage, or a single write if something goes wrong with the Redis process itself, but the operating system is still running correctly. AOF and RDB persistence can be enabled at the same time without problems. If the AOF is enabled on startup Redis will load the AOF, that is the file with the better durability guarantees. Check http://redis.io/topics/persistence for more information. Redis Labs additionally recommends using the wait command. Review the wait command at: https://redis.io/commands/wait and determine if this meets organizational needs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the console UI, click the databases tab. 2. For each listed database, click it and select configuration. 3. Verify that "Persistence" is set to: "Append Only File (AOF) - fsync every write". If the setting is not configured or not documented to be set differently, this is a finding. 4. For each listed database, click it and select configuration. 5. Verify "Replication" is set enabled. If the setting is not configured or not documented to be set differently, this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-251241`

### Rule: In the event of a system failure, Redis Enterprise DBMS must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes.

**Rule ID:** `SV-251241r879641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving information system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes. Since it is usually not possible to test this capability in a production environment, systems should either be validated in a testing environment or prior to installation. This requirement is usually a function of the design of the IDPS component. Compliance can be verified by acceptance/validation processes or vendor attestation. Additional information can be found at: https://docs.redislabs.com/latest/rs/administering/troubleshooting/cluster-recovery/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the Redis Enterprise web UI, select settings and then alerts. Verify the alerts documented by the ISSO/ISSM are checked. If required alerts are not checked, this is a finding. In the Redis Enterprise web UI, select databases, then select the individual databases. For each database, select configuration. Verify that "Persistence", "Periodic backup", and "Alerts" are all configured as organizationally defined and documented by the ISSO or ISSM. Verify that organizationally defined path for the centralized log server is also applied and configured external to the database. If any of these items are not configured as documented, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-251242`

### Rule: Redis Enterprise DBMS must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-251242r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification. Redis Enterprise does not inherently encrypt data at rest and is designed to have the OS handle encryption for data at rest.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. Verify the operating system implements encryption to protect the confidentiality and integrity of information at rest. If a disk or filesystem requires encryption, ask the system owner, DBA, and SA to demonstrate the use of filesystem and/or disk-level encryption. If this is required and is not found, this is a finding. To check if full disk encryption is enabled, log in to RHEL as an admin user and run the following commands: # lsblk Identify the partition that Redis Enterprise is located on. # blkid /dev/[name of partition] If the output shows TYPE="crypto_LUKS" then the partition is encrypted. If encryption must be used and is not employed, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-251243`

### Rule: Redis Enterprise DBMS must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-251243r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring data at rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides. Redis Enterprise does not inherently encrypt data at rest; however, this can be handled at the OS level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Verify the operating system implements encryption to protect the confidentiality and integrity of information at rest. If a disk or filesystem requires encryption, ask the system owner, DBA, and SA to demonstrate the use of filesystem and/or disk-level encryption. If this is required and is not found, this is a finding. To check if full disk encryption is enabled, log in to RHEL as an Admin user and run the following commands: # lsblk Identify the partition that Redis Enterprise is located on. # blkid /dev/[name of partition] If the output shows TYPE="crypto_LUKS" then the partition is encrypted. If encryption must be used and is not employed, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-251244`

### Rule: Redis Enterprise DBMS must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-251244r879800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides. Redis Enterprise does not inherently encrypt data at rest; however, this can be handled at the OS level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from disclosure, which must include, at a minimum, PII and classified information. If the documentation indicates no information requires such protections, this is not a finding. Verify the operating system implements encryption to protect the confidentiality and integrity of information at rest. If a disk or filesystem requires encryption, ask the system owner, DBA, and SA to demonstrate the use of filesystem and/or disk-level encryption. If this is required and is not found, this is a finding. To check if full disk encryption is enabled, log in to RHEL as an Admin user and run the following commands: # lsblk Identify the partition that Redis Enterprise is located on. # blkid /dev/[name of partition] If the output shows TYPE="crypto_LUKS" then the partition is encrypted. If encryption must be used and is not employed, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-251245`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-251245r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000243-DB-000373

**Group ID:** `V-251246`

### Rule: Redis Enterprise DBMS must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-251246r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse. For more information, refer to: https://redis.io/topics/acl more information on creating clearly defined categories and adding/editing users to categories and ACLs. and https://docs.redislabs.com/latest/rs/administering/access-control/user-roles/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all returned users with security permissions are documented as requiring the permissions. In the web UI, select access control >> Redis acls. Verify that the documented users have the correct ACL(s) assigned to them by clicking the "Used By" link for each listed ACL. Verify that all documented ACLs match each of the listed ACLs. If "Redis ACL name" and "Used By" do not match the documentation, this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-251247`

### Rule: Access to database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-251247r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions granted to users by the operating system/file system on the database files, database log files, and database backup files. If any user/role who is not an authorized system administrator with a need to know or database administrator with a need to know, or a system account for running DBMS processes, is permitted to read/view any of these files, this is a finding. Review the directory contents and files and verify that the appropriate file permissions are set. Verify that the file owner and group is set to Redis Labs or a group defined per site requirements. To check permissions of log files (Note: This may vary depending on the installation path.): # /var/opt/redislabs/log To check persisted files from memory if they are being used run the following command (Note: This may vary depending on the installation path.) # ls -ltr /var/opt/redislabs/persist/redis/ To check the default file permissions to verify that all authenticated users can only read and modify their own files: # cat/etc/login.defs|grep UMASK Verify the value is set to 077 or an appropriate organizationally defined setting. Investigate the permissions on these files. If the permissions allow access by other, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-251248`

### Rule: Redis Enterprise DBMS must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-251248r879812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms. For more detailed information, refer to: https://docs.redislabs.com/latest/rs/administering/designing-production/security/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis has optional support for TLS on all communication channels, including client connections, replication links, and the Redis Cluster bus protocol. By default, each cluster node has a different set of self-signed certificates. These certificates can be replaced with a DoD-acceptable certificate, preferably a certificate issued by an intermediate certificate authority (CA). For security reasons, Redis Enterprise only supports only the TLS protocol. Therefore, verify that the Redis client or secured tunnel solution is TLS v1.2 or above. First, verify that the host operating system is encrypted. If the host operating system is not encrypted, this is a finding. If the host operating system is encrypted, run the following commands and verify that only DoD-approved PKI certificates are present: # cd /etc/opt/redislabs # ls Verify the proxy_cert.pem file is present. If no certificates are found, this is a finding. Verify that TLS is configured to be used. To check this: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the Databases tab and select the database and then configuration. 3. Review the configuration and verify that TLS is enabled for all communications. If TLS is not configured to be used, this is a finding. To check the current TLS version, run the following commands on one of the servers that is hosting Redis Enterprise as a privileged user: # ccs-cli # hgetall min_control_tls_version If TLS is not FIPS compliant, this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-251249`

### Rule: Redis Enterprise DBMS must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-251249r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, the DBMS, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If Redis Enterprise DBMS, associated applications, and infrastructure do not employ protective measures against unauthorized disclosure and modification during reception, this is a finding. Redis Enterprise Software (RS) can use industry-standard encryption to protect data in transit between a Redis client and RS. For this purpose, RS uses transport layer security (TLS) protocol. Run the following commands and verify certificates are present: # cd /etc/opt/redislabs # ls Verify the proxy_cert.pem file is present. If no certificates are found, this is a finding. Verify that TLS is configured to be used. To check this: 1. Log in to the Redis Enterprise web UI as an admin user. 2. Navigate to the Databases tab and select the database and then configuration. 3. Review the configuration and verify that TLS is enabled for all communications. If TLS is not configured to be used, this is a finding. To check the current TLS version, run the following commands on one of the servers that is hosting Redis Enterprise as a privileged user: # ccs-cli # hgetall min_control_tls_version If TLS is not FIPS compliant, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-251250`

### Rule: Redis Enterprise DBMS and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-251250r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of LUA and SQL. In such cases, the attacker deduces the manner in which code is processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where code is executed dynamically, the attacker is then able to craft input strings that subvert it. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be used otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). Because Redis does not rely on a query language, there is no known method of SQL injection that would apply to Redis. Redis is a key value store and relies on commands that do not have a unified query language. Redis does have an embedded LUA interpreter and the user will need to disable these. When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: - Allow strings as input only when necessary. - Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. - Limit the size of input strings to what is truly necessary. - If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. - If comment markers will never be valid as input, reject them. - If HTML and XML tags, entities, comments, etc., will never be valid, reject them. - If wildcards are present, reject them unless truly necessary. - If there are range limits on the values that may be entered, enforce those limits. - Institute procedures for inspection of programs for correct use of dynamic coding by a party other than the developer. - Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. - Record the inspection and testing in the system documentation. - Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities, but it may also itself be the attacker. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis does not rely on a query language and there is no known method of SQL injection that would apply to Redis. Redis is a key value store and relies on commands that do not have a unified query language. Redis has an embedded LUA interpreter that is recommended to disable. Interview the system administrator and ask if the practice of disabling LUA scripting is a documented practice or has been completed. To check if LUA scripting is disabled on the desired database: 1. Connect to one of the nodes/servers in the redis enterprise cluster as an admin (sudo su -). 2. Type: rladmin status to get the DB ID of the database on which LUA scripting is to be disabled 3. Run the following command, substituting in the bdb_id from the previous step: ccs-cli hget bdb:<bdb_id> If the response is NIL or doesn't return EVAL, EVALSHA, this is a finding. If no documentation exists or if the database otherwise accepts LUA scripts, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-251251`

### Rule: Redis Enterprise DBMS and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack.

**Rule ID:** `SV-251251r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of LUA and SQL. In such cases, the attacker deduces the manner in which code is processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where code is executed dynamically, the attacker is then able to craft input strings that subvert it. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be used otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). Because Redis does not rely on a query language there is no known method of SQL injection that would apply to Redis. Redis is a key value store and relies on commands that do not have a unified query language. Redis does have an embedded LUA interpreter and the user will need to disable these. When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: - Allow strings as input only when necessary. - Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. - Limit the size of input strings to what is truly necessary. - If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. - If comment markers will never be valid as input, reject them. - If HTML and XML tags, entities, comments, etc., will never be valid, reject them. - If wildcards are present, reject them unless truly necessary. - If there are range limits on the values that may be entered, enforce those limits. - Institute procedures for inspection of programs for correct use of dynamic coding, by a party other than the developer. - Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. - Record the inspection and testing in the system documentation. - Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities; it may itself be the attacker. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis does not rely on a query language and there is no known method of SQL injection that would apply to Redis. Redis is a key value store and relies on commands that do not have a unified query language. Redis has an embedded LUA interpreter that is recommended to disable. Interview the system administrator and ask if the practice of disabling LUA scripting is a documented practice or has been completed. To check if LUA scripting is disabled on the desired database: 1. Connect to one of the nodes/servers in the redis enterprise cluster as an admin (sudo su -). 2. Type: rladmin status to get the DB ID of the database on which LUA scripting is to be disabled. 3. Run the following command, substituting in the bdb_id from the previous step: ccs-cli hget bdb:<bdb_id> If the response is NIL or doesn't return EVAL, EVALSHA, this is a finding If no documentation exists or if the database otherwise accepts LUA scripts, this is a finding.

## Group: SRG-APP-000454-DB-000389

**Group ID:** `V-251252`

### Rule: When updates are applied to Redis Enterprise DBMS software, any software components that have been replaced or made unnecessary must be removed.

**Rule ID:** `SV-251252r879825_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Previous versions of DBMS components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some DBMSs' installation tools may remove older versions of software automatically from the information system. In other cases, manual review and removal will be required. In planning installations and upgrades, organizations must include steps (automated, manual, or both) to identify and remove the outdated modules. A transition period may be necessary when both the old and the new software are required. This should be considered in the planning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When the Redis software is upgraded to a new version, the old version install file remains on the server. The users must remove this manually. To verify if the old install files have been deleted, check the locations below: /opt/redislabs - Main Installation directory for all Redis Enterprise Software binaries /opt/redislabs/config - System configuration files /opt/redislabs/lib - System library files /var/opt/redislabs - Default storage location for the cluster data, system logs, backups and ephemeral, persisted data /tmp - Temporary files The GREP command can be used to search for old Redis files in the above locations. If software components that have been replaced or made unnecessary are not removed, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-251253`

### Rule: Security-relevant software updates to Redis Enterprise DBMS must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-251253r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). For more information, refer to: https://docs.redislabs.com/latest/rs/installing-upgrading/upgrading/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine the current version of the software, perform the steps below: 1. Log in to the Redis Enterprise UI as an Admin user. 2. Navigate to the Cluster tab in the red banner. 3. Click on the Configuration option. 4. Find the Version number of the Cluster, Latest Redis version supported, and Latest Memcached version supported. 5. Compare to current Redis Enterprise version available. If the organization is not following their own defined time periods to apply updates, this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-251426`

### Rule: Redis Enterprise DBMS must generate audit records for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-251426r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Redis Enterprise does not generate all the DoD-required audit records. This could lead to incomplete information as follows: - Without an audit trail, unauthorized access to protected data and attempts to elevate or restrict privileges could go undetected. - It would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. - Without the creation of certain audit logs, it would be difficult to identify attempted attacks, and an audit trail would not be available for some forensic investigation for after-the-fact actions. For a complete list of unsupported audit requirements, email "disa.letterkenny.re.mbx.stig-customer-support-mailbox@mail.mil". Once the identity of the requester has been verified and the specifics of missing audit requirements obtained, risk can be assessed and a determination made as to whether it is acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is a permanent finding and cannot be fixed. Redis Enterprise does not currently support session or transactional auditing on the database. Redis Enterprise does not generate all the DoD-required audit records; therefore this is a finding. The site must seek AO or ISSO approval for use of Redis Enterprise 6.x with the understanding that not all of the DoD audit requirements are being met.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-251428`

### Rule: If DBMS authentication using passwords is employed, Redis Enterprise DBMS must enforce the DoD standards for password complexity and lifetime.

**Rule ID:** `SV-251428r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS/enterprise authentication and identification must be used (SRG-APP-000023-DB-000001). Native DBMS authentication may be used only when circumstances make it unavoidable and must be documented and AO-approved. The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DoD standards for password complexity and lifetime must be implemented. DBMS products that can inherit the rules for these from the operating system or access control program (e.g., Microsoft Active Directory) must be configured to do so. For other DBMSs, the rules must be enforced using available configuration parameters or custom code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Redis Enterprise Software supports Lightweight Directory Access Protocol (LDAP) admin console users. LDAP must be enabled to enforce password complexity. If LDAP is not in use, a password complexity profile can be configured in Redis Enterprise; however, it currently does not meet the DoD standard. Review the LDAP settings relating to password complexity. To check the LDAP settings: 1. Log in to the server housing the Redis Enterprise as an admin user. 2. CAT /etc/opt/redislabs/saslauthd.conf or the installation choice used during initial configuration. 3. Verify the following is configured: ldap_servers Ldap_tls_cacert_file ldap_filter ldap_bind_dn ldap_password If LDAP cannot be configured, this check can be downgraded if the password complexity profile has been configured: - At least eight characters - At least one uppercase character - At least one lowercase character - At least one number (not first or last character) - At least one special character (not first or last character) In addition, the password: - Cannot contain the user ID or reverse of the user ID - Cannot have more than three repeating characters To verify this, either attempt a password change or view the password complexity settings in the REST API. If LDAP or the password complexity profile is not in use, this is a finding.

