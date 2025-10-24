# STIG Benchmark: MS SQL Server 2014 Instance Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-213807`

### Rule: The number of concurrent SQL Server sessions for each system account must be limited.

**Rule ID:** `SV-213807r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks. For example, boundary protection devices can filter certain types of packets to protect devices on an organization’s internal network from being directly affected by DoS attacks. One way SQL Server can limit exposure to DoS attacks is to restrict the number of connections that can be opened by a single user. SQL Server supports this through the use of logon triggers. (Note, however, that this need not be the only, or even the principal, means for satisfying this requirement. Depending on the architecture and capabilities of the network and application, a network device or an application may be more suitable for providing this protection.) When determining the appropriate values for this limit, take the characteristics of the various kinds of user into account, and bear in mind that some applications and some users may need to have multiple sessions open. For example, while a standard account using a simple application may never need more than, say, five connections, a database administrator using SQL Server Management Studio may need significantly more, because each tab in that application counts as a distinct session. Architectural note: In SQL Server, a count of active sessions by user can be obtained from one of the dynamic management views. For example: SELECT original_login_name, count(*) FROM sys.dm_exec_sessions WHERE is_user_process = 1 GROUP BY original_login_name; However, for this to return an accurate count in a logon trigger, the user would have to have the View Server State privilege. (Without this privilege, the trigger sees information only about the current session, so would always return a count of one.) View Server State would give that user access to a wide swath of information about the server. One way to avoid this exposure is to create a summary table, and a view of that table that restricts each user to seeing his/her own count, and establish a frequently-run background job to refresh the table (using the above query or similar). The logon trigger then queries the view to obtain a count that is accurate enough for this purpose in most circumstances.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether any limits have been defined. If not, this is a finding. If one limit has been defined but is not applied to all users, including privileged administrative accounts, this is a finding. If multiple limits have been defined, to accommodate different types of user, verify that together they cover all users. If not, this is a finding. If a mechanism other than a logon trigger is used, verify its correct operation by the appropriate means. If it does not work correctly, this is a finding. Otherwise, determine if a logon trigger exists: EITHER, in SQL Server Management Studio's Object Explorer tree: Expand [SQL Server Instance] >> Security >> Server Objects >> Triggers OR run the query: SELECT * FROM master.sys.server_triggers; If no triggers are listed, this is a finding. If triggers are listed, identify the one(s) limiting the number of concurrent sessions per user. If none are found, this is a finding. If they are present but disabled, this is a finding. Examine the trigger source code for logical correctness and for compliance with the documented limit(s). If errors or variances exist, this is a finding. Verify that the system does execute the trigger(s) each time a user session is established. If it does not operate correctly for all types of user, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-213808`

### Rule: SQL Server must enforce approved authorizations for logical access to server-level system resources in accordance with applicable access control policies.

**Rule ID:** `SV-213808r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the SQL Server instance and server-level resources. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including SQL Server instances, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes SQL Server. If SQL Server is not configured to follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for DBMS server securables, by type of login. Review the permissions actually in place on the server. The server permission functions and views provided in the supplemental file Permissions.sql can help with this. If the actual permissions do not match the documented requirements, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-213809`

### Rule: SQL Server default account [sa] must have its name changed.

**Rule ID:** `SV-213809r960963_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SQL Server's [sa] account has special privileges required to administer the database. The [sa] account is a well-known SQL Server account name and is likely to be targeted by attackers, and is thus more prone to providing unauthorized access to the database. Since the SQL Server [sa] is administrative in nature, the compromise of a default account can have catastrophic consequences, including the complete loss of control over SQL Server. Since SQL Server needs for this account to exist and it should not be removed, one way to mitigate this risk is to change the [sa] account name.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SQL Server default [sa] (system administrator) account name has been changed by executing the following query: USE master; GO SELECT * FROM sys.sql_logins WHERE [name] = 'sa' OR [principal_id] = 1; GO If the login account name "SA" or "sa" appears in the query output, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-213810`

### Rule: Where SQL Server Trace is in use for auditing purposes, SQL Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be traced.

**Rule ID:** `SV-213810r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. This version of the requirement deals with Trace-based audit trails.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SQL Server Trace is not in use for audit purposes, this is not a finding. Obtain the list of approved audit maintainers from the system documentation. Review the server roles and individual logins that have the following permissions, all of which enable the ability to create and maintain audit definitions (the views and functions provided in the supplemental fine Permissions.sql can assist in this): ALTER TRACE CREATE TRACE EVENT NOTIFICATION The functions and views provided in the supplemental file Permissions.sql can assist in this review. In the following, "STIG" stands for the schema where you have deployed these views and functions. To see which logins and server roles have been granted these permissions: SELECT * FROM STIG.server_permissions P WHERE P.[Permission] IN ( 'ALTER TRACE', 'CREATE TRACE EVENT NOTIFICATION' ); To see what logins and server roles inherit these permissions from the server roles reported by the previous query, repeat the following for each one: SELECT * FROM STIG.members_of_server_role(<server role name>); To see all the permissions in effect for a server principal (server role or login): SELECT * FROM STIG.server_effective_permissions(<principal name>); If designated personnel are not able to configure auditable events, this is a finding. If unapproved personnel are able to configure auditable events, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-213811`

### Rule: Where SQL Server Audit is in use, SQL Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited at the server level.

**Rule ID:** `SV-213811r960882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. This version of the requirement deals with SQL Server Audit-based audit trails.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SQL Server Audit is not in use, this is not a finding. Obtain the list of approved audit maintainers from the system documentation. Review the server roles and individual logins that have the following permissions, all of which enable the ability to create and maintain audit definitions (the views and functions provided in the supplemental fine Permissions.sql can assist in this): ALTER ANY SERVER AUDIT CONTROL SERVER ALTER ANY DATABASE CREATE ANY DATABASE The functions and views provided in the supplemental file Permissions.sql can assist in this review. In the following, "STIG" stands for the schema where you have deployed these views and functions. To see which logins and server roles have been granted these permissions: SELECT * FROM STIG.server_permissions P WHERE P.[Permission] IN ( 'ALTER ANY SERVER AUDIT', 'CONTROL SERVER', 'ALTER ANY DATABASE', 'CREATE ANY DATABASE' ); To see what logins and server roles inherit these permissions from the server roles reported by the previous query, repeat the following for each one: SELECT * FROM STIG.members_of_server_role(<server role name>); To see all the permissions in effect for a server principal (server role or login): SELECT * FROM STIG.server_effective_permissions(<principal name>); If designated personnel are not able to configure auditable events, this is a finding. If unapproved personnel are able to configure auditable events, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-213812`

### Rule: Where SQL Server Audit is in use, SQL Server must generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-213812r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The system must monitor who/what is reading privilege/permission/role information. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that SQL Server continually performs to determine if any and every action on the database is permitted. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. This requirement applies to SQL Server Audit-based audit trails; Trace does not have this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SQL Server Trace is in use for audit purposes, and SQL Server Audit is not in use, this is not a finding. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the broad, server-level audit action group SCHEMA_OBJECT_ACCESS_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all SELECT actions on the permissions-related system views, and any locally-defined permissions tables, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'SCHEMA_OBJECT_ACCESS_GROUP'; If no row is returned, this is a finding. If the audited_result column is not "SUCCESS" or "SUCCESS AND FAILURE", this is a finding.

## Group: SRG-APP-000096-DB-000040

**Group ID:** `V-213813`

### Rule: SQL Server must produce Trace or Audit records containing sufficient information to establish when the events occurred.

**Rule ID:** `SV-213813r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes, but is not limited to: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. SQL Server is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly when actions were performed. This requires specific information regarding the date and time an audit record is referring to. If date and time information is not recorded and stored with the audit record, the record itself is of very limited use. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, the event time and date are always captured: this is not a finding. If SQL Server Trace is in use for audit purposes, verify that for all events it captures the start and (where relevant) end time. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: WITH EC AS (SELECT eventid, columnid FROM sys.fn_trace_geteventinfo(2)), E AS (SELECT DISTINCT eventid FROM EC) SELECT E.eventid, CASE WHEN EC14.columnid IS NULL THEN 'Start Time (14) missing' ELSE '14 OK' END AS field14, CASE WHEN EC15.columnid IS NULL THEN 'End Time (15) missing' ELSE '15 OK' END AS field15 FROM E E LEFT OUTER JOIN EC EC14 ON EC14.eventid = E.eventid AND EC14.columnid = 14 LEFT OUTER JOIN EC EC15 ON EC15.eventid = E.eventid AND EC15.columnid = 15 WHERE EC14.columnid IS NULL OR EC15.columnid IS NULL; If the resulting list indicates any field specifications are missing, this is a finding.

## Group: SRG-APP-000097-DB-000041

**Group ID:** `V-213814`

### Rule: SQL Server must produce Trace or Audit records containing sufficient information to establish where the events occurred.

**Rule ID:** `SV-213814r960897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes, but is not limited to: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. SQL Server is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly where actions were performed. This requires specific information regarding the event location an audit record is referring to. If event location information is not recorded and stored with the audit record, the record itself is of very limited use. An event location can be a database instance, table, column, row, etc. Without sufficient information establishing where the audit events occurred, investigation into the cause of events is severely hindered. If SQL Server Audit is enabled, SQL Server does capture the event location-specific information in all audit records. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, the server instance, database, schema, and object names are each automatically captured when applicable; this is not a finding. If SQL Server Trace is in use for audit purposes, verify that for all events it captures the server name, database name, object type, object name and object owner (each where relevant). From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: WITH EC AS (SELECT eventid, columnid FROM sys.fn_trace_geteventinfo(#)), E AS (SELECT DISTINCT eventid FROM EC) SELECT E.eventid, CASE WHEN EC26.columnid IS NULL THEN 'Server Name (26) missing' ELSE '26 OK' END AS field26, CASE WHEN EC35.columnid IS NULL THEN 'Database Name (35) missing' ELSE '35 OK' END AS field35, CASE WHEN EC28.columnid IS NULL THEN 'Object Type (28) missing' ELSE '28 OK' END AS field28, CASE WHEN EC34.columnid IS NULL THEN 'Object Name (34) missing' ELSE '34 OK' END AS field34, CASE WHEN EC37.columnid IS NULL THEN 'Object Owner (37) missing' ELSE '34 OK' END AS field37 FROM E E LEFT OUTER JOIN EC EC26 ON EC26.eventid = E.eventid AND EC26.columnid = 26 LEFT OUTER JOIN EC EC35 ON EC35.eventid = E.eventid AND EC35.columnid = 35 LEFT OUTER JOIN EC EC28 ON EC28.eventid = E.eventid AND EC28.columnid = 28 LEFT OUTER JOIN EC EC34 ON EC34.eventid = E.eventid AND EC34.columnid = 34 LEFT OUTER JOIN EC EC37 ON EC37.eventid = E.eventid AND EC37.columnid = 37 WHERE EC26.columnid IS NULL OR EC35.columnid IS NULL OR EC28.columnid IS NULL OR EC34.columnid IS NULL OR EC37.columnid IS NULL; If the resulting list indicates any field specifications are missing, this is a finding.

## Group: SRG-APP-000098-DB-000042

**Group ID:** `V-213815`

### Rule: SQL Server must produce Trace or Audit records containing sufficient information to establish the sources (origins) of the events.

**Rule ID:** `SV-213815r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes, but is not limited to: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. SQL Server is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly who performed what actions. This requires specific information regarding the source of the event an audit record is referring to. If the source of the event information is not recorded and stored with the audit record, the record itself is of very limited use. The source of the event can be a user account and sometimes a system account when timed jobs are run. Without information establishing the source of activity, the value of audit records from a forensics perspective is questionable. If Trace is enabled for auditing, SQL Server does capture the source of the event-specific information in all audit records. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, this is not a finding. If SQL Server Trace is in use for audit purposes, verify that for all events it captures the NT User Name, NT Domain Name, Host Name, Client Process ID, Application Name, Login Name, SPID, DB User Name, and Login SID (each where relevant). From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: WITH EC AS (SELECT eventid, columnid FROM sys.fn_trace_geteventinfo(#)), E AS (SELECT DISTINCT eventid FROM EC) SELECT E.eventid, CASE WHEN EC6.columnid IS NULL THEN 'NT User Name (6) missing' ELSE '6 OK' END AS field26, CASE WHEN EC7.columnid IS NULL THEN 'NT Domain Name (7) missing' ELSE '7 OK' END AS field7, CASE WHEN EC8.columnid IS NULL THEN 'Host Name (8) missing' ELSE '8 OK' END AS field8, CASE WHEN EC9.columnid IS NULL THEN 'Client Process ID (9) missing' ELSE '9 OK' END AS field9, CASE WHEN EC10.columnid IS NULL THEN 'Application Name (10) missing' ELSE '10 OK' END AS field10, CASE WHEN EC11.columnid IS NULL THEN 'Login Name (11) missing' ELSE '11 OK' END AS field11, CASE WHEN EC12.columnid IS NULL THEN 'SPID (12) missing' ELSE '12 OK' END AS field12, CASE WHEN EC40.columnid IS NULL THEN 'DB User Name (40) missing' ELSE '40 OK' END AS field40, CASE WHEN EC41.columnid IS NULL THEN 'Login SID (41) missing' ELSE '41 OK' END AS field41 FROM E E LEFT OUTER JOIN EC EC6 ON EC6.eventid = E.eventid AND EC6.columnid = 6 LEFT OUTER JOIN EC EC7 ON EC7.eventid = E.eventid AND EC7.columnid = 7 LEFT OUTER JOIN EC EC8 ON EC8.eventid = E.eventid AND EC8.columnid = 8 LEFT OUTER JOIN EC EC9 ON EC9.eventid = E.eventid AND EC9.columnid = 9 LEFT OUTER JOIN EC EC10 ON EC10.eventid = E.eventid AND EC10.columnid = 10 LEFT OUTER JOIN EC EC11 ON EC11.eventid = E.eventid AND EC11.columnid = 11 LEFT OUTER JOIN EC EC12 ON EC12.eventid = E.eventid AND EC12.columnid = 12 LEFT OUTER JOIN EC EC40 ON EC40.eventid = E.eventid AND EC40.columnid = 40 LEFT OUTER JOIN EC EC41 ON EC41.eventid = E.eventid AND EC41.columnid = 41 WHERE EC6.columnid IS NULL OR EC7.columnid IS NULL OR EC8.columnid IS NULL OR EC9.columnid IS NULL OR EC10.columnid IS NULL OR EC11.columnid IS NULL OR EC12.columnid IS NULL OR EC40.columnid IS NULL OR EC41.columnid IS NULL; If the resulting list indicates any field specifications are missing, this is a finding. If SQL Server Audit is in use, check to see that all audit records include enough information to establish the sources of the events; if not, this is a finding.

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-213816`

### Rule: SQL Server must produce Trace or Audit records containing sufficient information to establish the outcome (success or failure) of the events.

**Rule ID:** `SV-213816r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes, but is not limited to: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. SQL Server is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know the outcome of attempted actions. This requires specific information regarding the outcome of the action or event that the audit record is referring to. If outcome status information is not recorded and stored with the audit record, the record itself is of very limited use. Success and failure indicators ascertain the outcome of a particular event. As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Without knowing the outcome of audit events, it is very difficult to accurately recreate the series of events during forensic analysis. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. If Trace is enabled for auditing, SQL Server does capture the outcome status information in all audit records. If SQL Server Audit is enabled, the [Succeeded] column in the audit output indicates the success or failure of the attempted action. Be aware, however, that it may report True in some cases where one would intuitively expect False. For example, SELECT 1/0 FROM SYS.ALL_OBJECTS will appear in the audit trail as successful, if the user has permission to perform that action, even though it contains an invalid expression. Some other actions that one would consider failures (such as selecting from a table that does not exist) may not appear at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, the Succeeded column is populated for all relevant events: this is not a finding. If SQL Server Trace is in use for audit purposes, verify that for all events it captures the Success flag (successful use of permissions), State and Error number (each where relevant). From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: WITH EC AS (SELECT eventid, columnid FROM sys.fn_trace_geteventinfo(#)), E AS (SELECT DISTINCT eventid FROM EC) SELECT E.eventid, CASE WHEN EC23.columnid IS NULL THEN 'Success (successful use of permissions) (23) missing' ELSE '23 OK' END AS field23, CASE WHEN EC30.columnid IS NULL THEN 'State (30) missing' ELSE '30 OK' END AS field30, CASE WHEN EC31.columnid IS NULL THEN 'Error (31) missing' ELSE '31 OK' END AS field31 FROM E E LEFT OUTER JOIN EC EC23 ON EC23.eventid = E.eventid AND EC23.columnid = 23 LEFT OUTER JOIN EC EC30 ON EC30.eventid = E.eventid AND EC30.columnid = 30 LEFT OUTER JOIN EC EC31 ON EC31.eventid = E.eventid AND EC31.columnid = 31 WHERE EC23.columnid IS NULL OR EC30.columnid IS NULL OR EC31.columnid IS NULL; If the resulting list indicates any field specifications are missing, this is a finding.

## Group: SRG-APP-000100-DB-000201

**Group ID:** `V-213817`

### Rule: SQL Server must produce Trace or Audit records containing sufficient information to establish the identity of any user/subject associated with the event.

**Rule ID:** `SV-213817r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly who performed a given action. If user identification information is not recorded and stored with the audit record, the record itself is of very limited use. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, the Principal Name columns are populated for all relevant events: this is not a finding. If SQL Server Trace is in use for audit purposes, verify that for all events it captures the NT User Name, NT Domain Name, Host Name, Login Name, DB User Name and Login SID (each where relevant). From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: WITH EC AS (SELECT eventid, columnid FROM sys.fn_trace_geteventinfo(#)), E AS (SELECT DISTINCT eventid FROM EC) SELECT E.eventid, CASE WHEN EC6.columnid IS NULL THEN 'NT User Name (6) missing' ELSE '6 OK' END AS field26, CASE WHEN EC7.columnid IS NULL THEN 'NT Domain Name (7) missing' ELSE '7 OK' END AS field7, CASE WHEN EC8.columnid IS NULL THEN 'Host Name (8) missing' ELSE '8 OK' END AS field8, CASE WHEN EC11.columnid IS NULL THEN 'Login Name (11) missing' ELSE '11 OK' END AS field11, CASE WHEN EC40.columnid IS NULL THEN 'DB User Name (40) missing' ELSE '40 OK' END AS field40, CASE WHEN EC41.columnid IS NULL THEN 'Login SID (41) missing' ELSE '41 OK' END AS field41 FROM E E LEFT OUTER JOIN EC EC6 ON EC6.eventid = E.eventid AND EC6.columnid = 6 LEFT OUTER JOIN EC EC7 ON EC7.eventid = E.eventid AND EC7.columnid = 7 LEFT OUTER JOIN EC EC8 ON EC8.eventid = E.eventid AND EC8.columnid = 8 LEFT OUTER JOIN EC EC11 ON EC11.eventid = E.eventid AND EC11.columnid = 11 LEFT OUTER JOIN EC EC40 ON EC40.eventid = E.eventid AND EC40.columnid = 40 LEFT OUTER JOIN EC EC41 ON EC41.eventid = E.eventid AND EC41.columnid = 41 WHERE EC6.columnid IS NULL OR EC7.columnid IS NULL OR EC8.columnid IS NULL OR EC11.columnid IS NULL OR EC40.columnid IS NULL OR EC41.columnid IS NULL; If the resulting list indicates any field specifications are missing, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-213818`

### Rule: SQL Server must include organization-defined additional, more detailed information in Trace or Audit records for events identified by type, location, or subject.

**Rule ID:** `SV-213818r960909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SQL Server auditing capability is critical for accurate forensic analysis. Audit record content which may be necessary to satisfy the requirement of this control includes: time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. SQL Server does have a means available to add organizationally defined additional, more detailed information in the audit event records. These events may be identified by type, location, or subject. An example of more detailed information the organization may require in audit records could be the name of the application where the request is coming from. Some organizations may determine that more detailed information is required for specific database event types. If this information is not available, it could negatively impact forensic investigations into user actions or other malicious events. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Review system documentation to determine whether SQL Server is required to audit any events, and any fields, in addition to those in the standard audit or audit-oriented trace. If there are none specified, this is not a finding. If SQL Server Trace is in use for audit purposes, review the audit-oriented trace definition script(s) to identify any events and/or fields that are required but not in the script. If any such are identified, this is a finding. If SQL Server Audit is in use, compare the audit specification(s) with the documented requirements. If any such requirement is not satisfied by the audit specification(s) (or by supplemental, locally-deployed mechanisms), this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-213819`

### Rule: Unless it has been determined that availability is paramount, SQL Server must shut down upon the failure of an Audit, or a Trace used for auditing purposes, to include the unavailability of space for more audit/trace log records.

**Rule ID:** `SV-213819r960915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when SQL Server is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When the need for system availability does not outweigh the need for a complete audit trail, SQL Server should shut down immediately, rolling back all in-flight transactions. Systems where audit trail completeness is paramount will most likely be at a lower MAC level than MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid a shutdown in all but the most extreme situations. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If the system documentation indicates that availability takes precedence over audit trail completeness, this is not applicable (NA). If SQL Server Trace is in use for audit purposes, run the statement: SELECT * FROM sys.traces; In the results of the SELECT, identify the row representing the trace used for audit purposes. Examine the values in that row. If is_shutdown = 0, this is a finding. If SQL Server Audit is in use, review the defined server audits by running the statement: SELECT * FROM sys.server_audits; By observing the [name] and [is_state_enabled] columns, identify the row or rows in use. If the [on_failure_desc] is "SHUTDOWN SERVER INSTANCE" on this/these row(s), this is not a finding. Otherwise, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-213820`

### Rule: The audit information produced by SQL Server must be protected from unauthorized read access.

**Rule ID:** `SV-213820r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. SQL Server and third-party tools are examples of applications that are easily able to view and manipulate audit file data. Additionally, applications with user interfaces to audit records should not allow unfettered manipulation of, or access to, those records via any application. If an application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections, and limiting log data location. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the SQL Server audit file location(s) by running the following SQL script: SELECT DISTINCT LEFT(path, (LEN(path) - CHARINDEX('\',REVERSE(path)) + 1)) AS "Audit Path" FROM sys.traces UNION SELECT log_file_path AS "Audit Path" FROM sys.server_file_audits For each audit, the path column will give the location of the file. Verify that all audit files have the correct permissions by doing the following for each audit file: Navigate to audit folder location(s) using a command prompt or Windows Explorer. Right-click the file/folder, then click Properties. On the Security tab, verify that at most the following permissions are applied: Administrator(read) Users (none) Audit Administrator (Full Control) Auditors group (Read) SQL Server Service SID OR Service Account (Full Control) [Notes 1, 2] SQL Server SQL Agent Service SID OR Service Account, if SQL Server Agent is in use. (Read, Execute, Write) [Notes 1, 2] If any less restrictive permissions are present and not specifically justified and approved in the system security plan, this is a finding. If less restrictive permissions are present and specifically justified and approved in the system security plan, this is not a finding. If Trace is in use, SQL Server creates each trace file with a standard set of permissions, overriding the folder permissions. It grants full control to OWNER RIGHTS, Administrators, and <SQL Server Instance name>. Since this is not configurable, this is not a finding. ----- Note 1: It is highly advisable to use a separate account for each service. When installing SQL Server in single-server mode, the user can opt to have these provisioned for them. These automatically-generated accounts are referred to as virtual accounts. Each virtual account has an equivalent Service SID with the same name. The installer also creates an equivalent SQL Server login, also with the same name. Applying folder and file permissions to Service SIDs, rather than to domain accounts or local computer accounts, provides tighter control because these permissions are available only to the specific service when it is running, and not in any other context. (However, when using failover clustering, a domain account must be specified at installation, rather than a virtual account.) For more on this topic, see http://msdn.microsoft.com/en-us/library/ms143504(v=sql.120).aspx. Note 2: Tips for adding a service SID/virtual account to a folder's permission list: 1) In Windows Explorer, right-click on the folder and select "Properties." 2) Select the "Security" tab. 3) Click "Edit". 4) Click "Add". 5) Click "Locations". 6) Select the computer name. 7) Search for the name. 7.a) SQL Server Service 7.a.i) Type "NT SERVICE\MSSQL" and click "Check Names". (What you have just typed in is the first 16 characters of the name. At least one character must follow "NT SERVICE\"; you will be presented with a list of all matches. If you have typed in the full, correct name, step 7.a.ii is bypassed.) 7.a.ii) Select the "MSSQL$<instance name>" user and click OK. 7.b) SQL Agent Service 7.b.i) Type "NT SERVICE\SQL" and click "Check Names". 7.b.ii) Select the "SQLAgent$<instance name>" user and click OK. 8) Click OK. 9) Permission like a normal user from here.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-213821`

### Rule: The audit information produced by  SQL Server must be protected from unauthorized modification.

**Rule ID:** `SV-213821r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions, and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft or unauthorized modification of sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the SQL Server audit file location(s) by running the following SQL script: SELECT DISTINCT LEFT(path, (LEN(path) - CHARINDEX('\',REVERSE(path)) + 1)) AS "Audit Path" FROM sys.traces UNION SELECT log_file_path AS "Audit Path" FROM sys.server_file_audits For each audit, the Audit Path column will give the location of the file. Verify that all audit files have the correct permissions by doing the following for each audit file: Navigate to audit folder location(s) using a command prompt or Windows Explorer. The following instructions assume Windows Explorer is used. Right-click the file/folder, click Properties. On the Security tab, verify that at most the following permissions are applied: Administrator(read) Users (none) Audit Administrator (Full Control) Auditors group (Read) SQL Server Service SID OR Service Account (Full Control) [Notes 1, 2] SQL Server SQL Agent Service SID OR Service Account, if SQL Server Agent is in use. (Read, Execute, Write) [Notes 1, 2] If any less restrictive permissions are present and not specifically justified and approved in the system security plan, this is a finding. If less restrictive permissions are present and specifically justified and approved in the system security plan, this is not a finding. If Trace is in use, SQL Server creates each trace file with a standard set of permissions, overriding the folder permissions. It grants full control to OWNER RIGHTS, Administrators and <SQL Server Instance name>. Since this is not configurable, this is not a finding. ----- Note 1: It is highly advisable to use a separate account for each service. When installing SQL Server in single-server mode, you can opt to have these provisioned for you. These automatically-generated accounts are referred to as virtual accounts. Each virtual account has an equivalent Service SID, with the same name. The installer also creates an equivalent SQL Server login, also with the same name. Applying folder and file permissions to Service SIDs, rather than to domain accounts or local computer accounts, provides tighter control, because these permissions are available only to the specific service when it is running, and not in any other context. (However, when using failover clustering, a domain account must be specified at installation, rather than a virtual account.) For more on this topic, see http://msdn.microsoft.com/en-us/library/ms143504(v=sql.120).aspx. Note 2: Tips for adding a service SID/virtual account to a folder's permission list. 1) In Windows Explorer, right-click on the folder and select "Properties." 2) Select the "Security" tab 3) Click "Edit" 4) Click "Add" 5) Click "Locations" 6) Select the computer name 7) Search for the name 7.a) SQL Server Service 7.a.i) Type "NT SERVICE\MSSQL" and click "Check Names". (What you have just typed in is the first 16 characters of the name. At least one character must follow "NT SERVICE\"; you will be presented with a list of all matches. If you have typed in the full, correct name, step 7.a.ii is bypassed.) 7.a.ii) Select the "MSSQL$<instance name>" user and click OK 7.b) SQL Agent Service 7.b.i) Type "NT SERVICE\SQL" and click "Check Names" 7.b.ii) Select the "SQLAgent$<instance name>" user and click OK 8) Click OK 9) Permission like a normal user from here

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-213822`

### Rule: The audit information produced by SQL Server must be protected from unauthorized deletion.

**Rule ID:** `SV-213822r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft or unauthorized modification of sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the SQL Server audit file location(s) by running the following SQL script: SELECT DISTINCT LEFT(path, (LEN(path) - CHARINDEX('\',REVERSE(path)) + 1)) AS "Audit Path" FROM sys.traces UNION SELECT log_file_path AS "Audit Path" FROM sys.server_file_audits For each audit, the path column will give the location of the file. Verify that all audit files have the correct permissions by doing the following for each audit file: Navigate to audit folder location(s) using a command prompt or Windows Explorer. Right-click the file/folder, click Properties. On the Security tab, verify that at most the following permissions are applied: Administrator(read) Users (none) Audit Administrator (Full Control) Auditors group (Read) SQL Server Service SID OR Service Account (Full Control) [Notes 1, 2] SQL Server SQL Agent Service SID OR Service Account, if SQL Server Agent is in use. (Read, Execute, Write) [Notes 1, 2] If any less restrictive permissions are present and not specifically justified and approved in the system security plan, this is a finding. If less restrictive permissions are present and specifically justified and approved in the system security plan, this is not a finding. ----- Note 1: It is highly advisable to use a separate account for each service. When installing SQL Server in single-server mode, you can opt to have these provisioned for you. These automatically-generated accounts are referred to as virtual accounts. Each virtual account has an equivalent Service SID, with the same name. The installer also creates an equivalent SQL Server login, also with the same name. Applying folder and file permissions to Service SIDs, rather than to domain accounts or local computer accounts, provides tighter control, because these permissions are available only to the specific service when it is running, and not in any other context. (However, when using failover clustering, a domain account must be specified at installation, rather than a virtual account.) For more on this topic, see http://msdn.microsoft.com/en-us/library/ms143504(v=sql.120).aspx. Note 2: Tips for adding a service SID/virtual account to a folder's permission list. 1) In Windows Explorer, right-click on the folder and select "Properties." 2) Select the "Security" tab 3) Click "Edit" 4) Click "Add" 5) Click "Locations" 6) Select the computer name 7) Search for the name 7.a) SQL Server Service 7.a.i) Type "NT SERVICE\MSSQL" and click "Check Names". (What you have just typed in is the first 16 characters of the name. At least one character must follow "NT SERVICE\"; you will be presented with a list of all matches. If you have typed in the full, correct name, step 7.a.ii is bypassed.) 7.a.ii) Select the "MSSQL$<instance name>" user and click OK 7.b) SQL Agent Service 7.b.i) Type "NT SERVICE\SQL" and click "Check Names" 7.b.ii) Select the "SQLAgent$<instance name>" user and click OK 8) Click OK 9) Permission like a normal user from here

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-213823`

### Rule: Audit tools used in, or in conjunction with, SQL Server must be protected from unauthorized access.

**Rule ID:** `SV-213823r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user has in order to make access decisions regarding access to the audit tools. SQL Server is an application that does provide access to audit data. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the server documentation for a list of approved users with access to SQL Server Audits. To create, alter, or drop a server audit, principals require the "ALTER ANY SERVER AUDIT" or the "CONTROL SERVER" permission. To view an Audit log requires the "CONTROL SERVER" permission. To use Profiler, "ALTER TRACE" is required. Review the SQL Server permissions granted to principals. Look for permissions "ALTER ANY SERVER AUDIT", "ALTER ANY DATABASE AUDIT", "CONTROL SERVER", and "ALTER TRACE": SELECT login.name, perm.permission_name, perm.state_desc FROM sys.server_permissions perm -- or STIG.server_permissions JOIN sys.server_principals login ON perm.grantee_principal_id = login.principal_id WHERE permission_name in ('CONTROL SERVER', 'ALTER ANY DATABASE AUDIT', 'ALTER ANY SERVER AUDIT','ALTER TRACE') and login.name not like '##MS_%'; If unauthorized accounts have these privileges, this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-213824`

### Rule: SQL Server and/or the operating system must protect its audit configuration from unauthorized modification.

**Rule ID:** `SV-213824r960942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This focuses on external tools for log maintenance and review. Other STIG requirements govern SQL Server privileges to maintain trace or audit definitions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In Windows, review the access permissions to tools used to view or modify audit log data (to include traces used for audit purposes). If appropriate permissions and access controls to prevent unauthorized changes are not applied to these tools, this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-213825`

### Rule: SQL Server and the operating system must protect SQL Server audit features from unauthorized removal.

**Rule ID:** `SV-213825r960945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This focuses on external tools for log maintenance and review. Other STIG requirements govern SQL Server privileges to maintain trace or audit definitions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In Windows, review the access permissions to tools used to view or modify audit log data (to include traces used for audit purposes). If appropriate permissions and access controls to prevent unauthorized deletions are not applied to these tools, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213826`

### Rule: SQL Server security-relevant configuration settings must be monitored to discover unauthorized changes.

**Rule ID:** `SV-213826r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to security-relevant configuration settings of SQL Server can potentially have significant effects on the overall security of the system. If SQL Server were to allow any user to make changes to configuration settings, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement is contingent upon the configuration of SQL Server's hosted application and the security-relevant configuration settings of SQL Server. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to these security-relevant configuration settings for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to SQL Server software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify within the system documentation that SQL Server is monitored for security-relevant configuration settings to discover unauthorized changes. This can be done by a third-party tool or a SQL script that does baselining and then comparisons. If the monitoring of security-relevant configuration settings to discover unauthorized changes is not implemented on SQL Server, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213827`

### Rule: Software, applications, and configuration files that are part of, or related to, the SQL Server  installation must be monitored to discover unauthorized changes.

**Rule ID:** `SV-213827r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of applications and tools related to SQL Server can potentially have significant effects on the overall security of the system. Only qualified and authorized individuals shall be allowed to obtain access to components related to SQL Server for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the software libraries or configuration can lead to unauthorized or compromised installations. Of particular note in this context is that any software installed for auditing and/or audit file management must be protected and monitored.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that files and folders that are part of, or related to, the SQL Server 2014 installation have only the appropriate privileges. In Windows Explorer, right-click the file/folder, click Properties. On the Security tab, modify the security permissions, so that at most the following permissions are present: Trusted Installer (Full Control) SYSTEM (Full Control) Administrators (Full Control) [See Note 1] Users (Read, List Folder Contents, Read & Execute) Creator Owner (Special Permissions - Full control - Subfolders and files only) All Application Packages (Read & Execute) [Only as needed - see Note 2] If any less restrictive permissions are present (and not specifically justified and approved), this is a finding. Verify that files and folders that are part of, or related to, the SQL Server 2014 installation have auditing enabled. Right-click on the file/folder, click Properties. On the Security tab, click Advanced. On the Auditing tab, verify that the following is set up on at least one audit: Type: All Principal: Everyone Access: Modify Applies to: This Folder, subfolder, and files [where applicable] If the required audit settings are not configured, there is a risk that unauthorized changes to the software will go undetected, and this is a finding. If a third-party security and data integrity tool is not used for monitoring and alerting files and folders based on cryptographic hashes, this is a finding. If the tool does not verify files/folder locations as listed in the documentation, this is a finding. Note 1: In the interest of separation of responsibilities with least privilege, consider granting Full Control only to SQL Database Administrators (or another appropriate group of administrators) and providing the local Administrators group with Read access only. Note 2: Some files also require 'ALL APPLICATION PACKAGES (READ, EXECUTE)' permissions for certain functionality to work appropriately, and this is considered acceptable where those permissions are required. (All SQL Server files that require this access reside by default in the ..\Microsoft SQL Server\110\ directory.)

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-213828`

### Rule: SQL Server software installation account(s) must be restricted to authorized users.

**Rule ID:** `SV-213828r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. If the application were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement is contingent upon the language in which the application is programmed, as many application architectures in use today incorporate their software libraries into, and make them inseparable from, their compiled distributions, rendering them static and version dependent. However, this requirement does apply to applications with software libraries accessible and configurable, as in the case of interpreted languages. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a greater impact on SQL Server security and operation. It is especially important to grant access to privileged accounts to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check system documentation for policy and procedures to restrict use of the SQL Server software installation account. Check OS settings to determine whether users are restricted from accessing SQL Server objects and data they are not authorized to access by checking the local OS user accounts. From a Command Prompt, open lusrmgr.msc. Navigate to Users >> right-click individual user >> Properties >> Member Of. If appropriate access controls for all users are not implemented to restrict access to only authorized users and to restrict the access of those users to objects and data they are authorized, this is a finding. Review procedures for controlling and granting access to use of the SQL Server software installation account. If access or use of this account is not restricted to the minimum number of personnel required, or unauthorized access to this account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-213829`

### Rule: Database software directories, including SQL Server configuration files, must be stored in dedicated directories, separate from the host OS and other applications.

**Rule ID:** `SV-213829r960960_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit of one application can lead to an exploit of other applications sharing the same security context. For example, an exploit of a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to other applications’ database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SQL Server installations present on the server. From a Command Prompt, type regedit.exe, and press [ENTER]. Navigate to HKEY_LOCAL_MACHINE >> SOFTWARE >> Microsoft >> Microsoft SQL Server >> Instance Names. Each instance installed on the server possesses a key inside a folder under this registry entry. Analysis Services Instances are registered in the OLAP subfolder. Reporting Services Instances are registered in the RS subfolder. Standard SQL Server (database engine) Instances are registered in the SQL subfolder. Inside each one of these folders, a single key is used to reference an Instance's specific Windows Registry tree. Each key will have its own registry tree at the following registry location: HKEY_LOCAL_MACHINE >> SOFTWARE >> Microsoft >> Microsoft SQL Server >> [INSTANCE NAME]. An [INSTANCE NAME] is listed as the Data component of a key found in one of the above OLAP, RS, or SQL folders. To find the installation location of a particular instance, navigate to the following location in the Windows Registry: HKEY_LOCAL_MACHINE >> SOFTWARE >> Microsoft >> Microsoft SQL Server >> [INSTANCE NAME] >> Setup. Examine the value of the 'SqlProgramDir' key. The value of the 'SqlProgramDir' key is the SQL Server installation directory for that SQL Server Instance. Navigate to that folder location using a Command Prompt or Windows Explorer. Only applications that are required for the functioning and administration, not use, of SQL Server should be located on the same directory node as the SQL Server software libraries. If any files or subfolders that are not part of the SQL Server installation are in the folder, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-213830`

### Rule: SQL Server must have the publicly available Northwind sample database removed.

**Rule ID:** `SV-213830r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements and providing a wide array of functionality not required for every mission, but which cannot be disabled. Applications must adhere to the principles of least functionality by providing only essential capabilities. Even though the very popular "Northwind" database is no longer installed by default, it introduces a vulnerability to SQL Server and must be removed, if present. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the SQL Server and the OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SQL Server for the existence of the publicly available "Northwind" database by performing the following query: SELECT name FROM sysdatabases WHERE name LIKE 'Northwind%'; If the "Northwind" database is present, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-213831`

### Rule: SQL Server must have the publicly available pubs sample database removed.

**Rule ID:** `SV-213831r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements and providing a wide array of functionality not required for every mission, but which cannot be disabled. Applications must adhere to the principles of least functionality by providing only essential capabilities. Even though the formerly popular "pubs" database is no longer installed by default, it introduces a vulnerability to SQL Server and must be removed, if present. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the SQL Server and the OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SQL Server for the existence of the publicly available "pubs" database by performing the following query: SELECT name FROM sysdatabases WHERE name LIKE 'pubs%'; If the "pubs" database is present, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-213832`

### Rule: SQL Server must have the publicly available AdventureWorks sample database removed.

**Rule ID:** `SV-213832r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements and providing a wide array of functionality not required for every mission, but which cannot be disabled. Applications must adhere to the principles of least functionality by providing only essential capabilities. Even though the very popular "AdventureWorks" database is no longer installed by default, it introduces a vulnerability to SQL Server and must be removed, if present. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the SQL Server and the OS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SQL Server for the existence of the publicly available "AdventureWorks" database by performing the following query: SELECT name FROM sysdatabases WHERE name LIKE 'AdventureWorks%'; If the "AdventureWorks" database is present, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213833`

### Rule: SQL Server must have the SQL Server Data Tools (SSDT) software component removed if it is unused.

**Rule ID:** `SV-213833r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Data Tools (SSDT) software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of components and features installed with the database. Using an account with System Administrator privileges, from Command Prompt, open control.exe. Navigate to Programs and Features. Check for the following entries in the 'Uninstall or change a program' window. Microsoft SQL Server Data Tools - Database Projects - Web installer entry point Prerequisites for SSDT If SQL Server Data Tools is not documented as a server requirement, and these entries exist, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213834`

### Rule: SQL Server must have the SQL Server Reporting Services (SSRS) software component removed if it is unused.

**Rule ID:** `SV-213834r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Reporting Services (SSRS) software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server service "SQL Server Reporting Services (<Instance Name>)" is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Server Reporting Services (<Instance Name>)". If the "SQL Server Reporting Services (<Instance Name>)" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213835`

### Rule: SQL Server must have the SQL Server Integration Services (SSIS) software component removed if it is unused.

**Rule ID:** `SV-213835r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Integration Services (SSIS) software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server service "SQL Server Integration Services 12.0" is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Server Integration Services 12.0". If the "SQL Server Integration Services 12.0" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213836`

### Rule: SQL Server must have the SQL Server Analysis Services (SSAS) software component removed if it is unused.

**Rule ID:** `SV-213836r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Analysis Service (SSAS) software component removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server service "SQL Server Analysis Services (<Instance Name>)" is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Server Analysis Services (<Instance Name>)". If the "SQL Server Analysis Services (<Instance Name>)" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213837`

### Rule: SQL Server must have the SQL Server Distributed Replay Client software component removed if it is unused.

**Rule ID:** `SV-213837r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Distributed Replay Client software component must be removed if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server service "SQL Server Distributed Replay Client" is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Server Distributed Replay Client". If the "SQL Server Distributed Replay Client" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213838`

### Rule: SQL Server must have the SQL Server Distributed Replay Controller software component removed if it is unused.

**Rule ID:** `SV-213838r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Distributed Replay Controller software component must be removed if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server service "SQL Server Distributed Replay Controller" is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Server Distributed Replay Controller". If the "SQL Server Distributed Replay Controller" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213839`

### Rule: SQL Server must have the Full-Text Search software component removed if it is unused.

**Rule ID:** `SV-213839r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Full-Text Search software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server full-text search feature is used and satisfies organizational requirements, this is not a finding. From a command prompt or the Start menu, using an account with System Administrator Privilege, open services.msc. Look for: "SQL Full-text Daemon Launcher(<Instance name>)". If the "SQL Full-text Daemon Launcher(<Instance name>)" service exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213840`

### Rule: SQL Server must have the Master Data Services software component removed if it is unused.

**Rule ID:** `SV-213840r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Master Data Services software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Master Data Services feature is used and satisfies organizational requirements, this is not a finding. Click on the Start button. Navigate to >> Microsoft SQL Server 2014 >> Master Data Services. If the "Master Data Services" folder exists and contains any programs, this is a finding. In Windows Explorer, navigate to <drive where SQL Server is installed>:\Program Files\Microsoft SQL Server\120\Master Data Services\. If this exists and contains any files, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213841`

### Rule: SQL Server must have the SQL Server Replication software component removed if it is unused.

**Rule ID:** `SV-213841r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The SQL Server Replication software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server Replication feature is used and satisfies organizational requirements, this is not a finding. In SQL Server Management Studio, Object Explorer, expand the instance. Right-click Replication >> New >> Publication. If the Publication Wizard appears, with no error message, this is a finding. Right-click Replication >> New >> Subscription. If the Subscription Wizard appears, with no error message, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213842`

### Rule: SQL Server must have the Data Quality Client software component removed if it is unused.

**Rule ID:** `SV-213842r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Data Quality Client software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Data Quality Client feature is used and satisfies organizational requirements, this is not a finding. In Windows Server 2008 R2 or lower, click on the Start button. In the Start menu, navigate to All Programs >> Microsoft SQL Server 2014. If the "Data Quality Services" folder exists and contains the Data Quality Client program, this is a finding. In Windows Server 2012 or higher, click on the Start button. In the Start menu, navigate to Apps >> Microsoft SQL Server 2014. If the Data Quality Client program is listed, this is a finding. In Windows Explorer, navigate to <drive where SQL Server is installed>:\Program Files (x86)\Microsoft SQL Server\120\Tools\Binn\DQ\ If this folder exists and contains the file DataQualityServices.exe, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213843`

### Rule: SQL Server must have the Data Quality Services software component removed if it is unused.

**Rule ID:** `SV-213843r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Data Quality Services software component must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Data Quality Services feature is used and satisfies organizational requirements, this is not a finding. Run the query: SELECT * FROM sys.databases WHERE name in ('DQS_MAIN', 'DQS_PROJECTS', 'DQS_STAGING_DATA'); If any rows are returned, this is a finding. In Windows Server 2008 R2 or lower, click on the Start button. In the Start menu, navigate to All Programs >> Microsoft SQL Server 2014. If the "Data Quality Services" folder exists and contains the Data Quality Server Installer program, this is a finding. In Windows Server 2012 or higher, click on the Start button. In the Start menu, navigate to Apps >> Microsoft SQL Server 2014. If the Data Quality Server Installer program is listed, this is a finding. In Windows Explorer, navigate to <drive where SQL Server is installed>:\Program Files\Microsoft SQL Server\MSSQL12.<Instance name>\MSSQL\Binn\ If this contains the file DQSInstaller.exe, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213844`

### Rule: SQL Server must have the Client Tools SDK software component removed if it is unused.

**Rule ID:** `SV-213844r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Client Tools Software Development Kit must be removed from SQL Server if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Client Tools Software Development Kit is used and satisfies organizational requirements, this is not a finding. Either using the Start menu or via the command "control.exe", open the Windows Control Panel. Open Programs and Features. Double-click on Microsoft SQL Server 2014. In the dialog box that appears, select Remove. Wait for the Remove wizard to appear. Select '<< Remove shared features only >>'; click Next. If the list of shared features includes Client Tools SDK, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213845`

### Rule: SQL Server must have the Management Tools software component removed if it is unused.

**Rule ID:** `SV-213845r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Management Tools is an indispensable software component on any server running the SQL Server DBMS, if the database administrator logs on to the Windows server to do his/her work. However, it is also possible to use the management tools on a separate machine and still connect to SQL Server. If this approach is used and DBAs never need to use the Management Tools directly on the server, then the Management Tools software component must be removed from the server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server Management Tools are used and satisfy organizational requirements, this is not a finding. In Windows Server 2008 R2 or lower, click on the Start button. In the Start menu, navigate to All Programs >> Microsoft SQL Server 2014. If the SQL Server Management Studio is listed, this is a finding. In Windows Server 2012 or higher, click on the Start button. In the Start menu, navigate to Apps >> Microsoft SQL Server 2014. If the SQL Server Management Studio is listed, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213846`

### Rule: SQL Server must have the Filestream feature disabled if it is unused.

**Rule ID:** `SV-213846r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default or selected for installation by an administrator, may not be necessary to support essential organizational operations (e.g., key missions, functions). Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. The Filestream feature must be disabled if it is unused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether Filestream is required to support the database(s) in this instance of SQL Server. Either, in SQL Server Management Studio, Object Explorer, right-click on the SQL Server instance; select Properties; examine the Filestream section. If Filestream Access Level is "Disabled", this is not a finding. If Filestream Access Level is "Transact-SQL access enabled" or "Full access enabled," and Filestream is not required, this is a finding. If Filestream Access Level is "Full access enabled," but only Transact-SQL access is required, this is a finding. Or, in a query tool, run this code: EXEC sys.sp_configure N'filestream access level'; Review the number in the config_value column. If it is 0, this is not a finding. If config_value is 1 or 2, and Filestream is not required, this is a finding. If config_value is 2, but only Transact-SQL access is required, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-213847`

### Rule: Unused database components that are integrated in SQL Server and cannot be uninstalled must be disabled.

**Rule ID:** `SV-213847r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SQL Server is capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software demonstrations, or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled. Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused and unnecessary SQL Server components increase the number of available attack vectors to SQL Server by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the components and features included in SQL Server and capable of being disabled (by configuration settings, permissions and privileges, etc.). Take note of those which are enabled. Review the system documentation to verify that the enabled components or features are documented and authorized. If any enabled components or features are not authorized, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-213848`

### Rule: The SQL Server default account [sa] must be disabled.

**Rule ID:** `SV-213848r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SQL Server's [sa] account has special privileges required to administer the database. The [sa] account is a well-known SQL Server account and is likely to be targeted by attackers and thus more prone to providing unauthorized access to the database. This [sa] default account is administrative and could lead to catastrophic consequences, including the complete loss of control over SQL Server. If the [sa] default account is not disabled, an attacker might be able to gain access through the account. SQL Server by default, at installation, disables the [sa] account. Some applications that run on SQL Server require the [sa] account to be enabled in order for the application to function properly. These applications that require the [sa] account to be enabled are usually legacy systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SQL Server settings to determine if the [sa] (system administrator) account has been disabled by executing the following query: USE master; GO SELECT name, is_disabled FROM sys.sql_logins WHERE principal_id = 1; GO Verify that the "name" column contains the current name of the [sa] database server account (see note). If the "is_disabled" column is not set to 1, this is a finding. Note: If the [sa] account name has been changed per SQL4-00-010200, its new name should appear in the query results.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-213849`

### Rule: Access to xp_cmdshell must be disabled, unless specifically required and approved.

**Rule ID:** `SV-213849r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS, but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system. The xp_cmdshell extended stored procedure allows execution of host executables outside the controls of database access permissions. This access may be exploited by malicious users who have compromised the integrity of the SQL Server database process to control the host operating system to perpetrate additional malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine if xp_cmdshell is enabled, execute the following commands: EXEC SP_CONFIGURE 'show advanced options', '1'; RECONFIGURE WITH OVERRIDE; EXEC SP_CONFIGURE 'xp_cmdshell'; If the value of config_value is 0, this is not a finding. Review the system documentation to determine whether the use of xp_cmdshell is required and approved. If it is not approved, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-213850`

### Rule: SQL Server must be configured to prohibit or restrict the use of unauthorized network protocols.

**Rule ID:** `SV-213850r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Additionally, it is sometimes convenient to provide multiple services from a single component of an information system (e.g., email and web services) but doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and, through the database, to other components of the information system. For information on approved and prohibited ports, protocols, and services, see the Ports, Protocols, and Services Management (PPSM) section of DoD Cyber Exchange web site: https://public.cyber.mil/connect/ppsm/. "Functions" in this requirement refers to system and infrastructure functionality, not to functions in mathematics and programming languages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open SQL Server Configuration Manager. Navigate to SQL Server Network Configuration > Protocols for <instance name>, where <instance name> is a placeholder for the SQL Server instance name. If any listed protocol is enabled but not authorized, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-213851`

### Rule: SQL Server must be configured to prohibit or restrict the use of unauthorized network ports.

**Rule ID:** `SV-213851r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Additionally, it is sometimes convenient to provide multiple services from a single component of an information system (e.g., email and web services) but doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and, through the database, to other components of the information system. For information on approved and prohibited ports, protocols, and services, see the Ports, Protocols, and Services Management (PPSM) section of DoD Cyber Exchange web site: https://public.cyber.mil/connect/ppsm/. "Functions" in this requirement refers to system and infrastructure functionality, not to functions in mathematics and programming languages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ports used by SQL Server. If these are in conflict with PPSM guidance, and not explained and approved in the system documentation, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-213852`

### Rule: SQL Server must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-213852r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized SQL Server access, organizational users shall be identified and authenticated. Organizational users include organizational employees and individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization, which must outline specific user actions that can be performed on SQL Server without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SQL Server users to determine whether shared accounts exist. (This does not include the case where SQL Server has a guest or public account that is providing access to publicly available information.) If accounts are determined to be shared, determine if individuals are first individually authenticated. If individuals are not individually authenticated before using the shared account (e.g., by the operating system or possibly by an application making calls to the database), this is a finding. If accounts are determined to be shared, determine if they are directly accessible to end users. If so, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-213853`

### Rule: SQL Server must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-213853r961053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users shall be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. This may be accomplished by a code embedded within the userid, or via a flag or code column in a table of users, or by some other means. In any case, the user must be individually identified to, and within, SQL Server via a mapping to an individual account and not mapping to a shared account. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, and other organizations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation, SQL Server settings and authentication system settings to determine if non-organizational users are individually identified and authenticated when logging onto the system. If the documentation indicates that this is a public-facing, read-only (from the point of view of public users) database that does not require individual authentication, this is not a finding. If non-organizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-213854`

### Rule: SQL Server must be configured to separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-213854r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check SQL Server permission settings to verify that administrative functionality is kept separate from user functionality. The views and functions provided in the supplemental file Permissions.sql can help with this review. If administrator and general user functionality are not separated either physically or logically, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-213855`

### Rule: SQL Server must isolate security functions from nonsecurity functions.

**Rule ID:** `SV-213855r961131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are defined as "the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based". Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from nonsecurity functionality via separate databases or schemas. SQL Server's [master] database and [sys] schema are examples of this. Further granularity of access protection is provided by assigning logins and users to appropriate server roles and database roles Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and nonsecurity functionality is commingled, users who have access to nonsecurity functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine application-specific security objects (lists of permissions, additional authentication information, stored procedures, application specific auditing, etc.) which are being housed inside SQL server in addition to the built-in security objects. Review permissions, both direct and indirect, on the security objects, both built-in and application-specific. The functions and views provided in the supplemental file Permissions.sql can help with this. If the database(s), schema(s) and permissions on security objects are not organized to provide effective isolation of security functions from nonsecurity functions, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213856`

### Rule: SQL Server must protect against an individual using a shared account from falsely denying having performed a particular action.

**Rule ID:** `SV-213856r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain application integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. Use of shared accounts does not provide individual accountability for actions taken on the DBMS or data. Whenever a single database account is used to connect to the database, a secondary authentication method that provides individual accountability is required. This scenario most frequently occurs when an externally hosted application authenticates individual users to the application and the application uses a single account to retrieve or update database information on behalf of the individual users (as in connection pooling). When shared accounts are utilized without another means of identifying individual users, users may deny having performed a particular action. (Shared accounts should not be confused with Windows groups, which are used in role-based access control.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of authorized SQL Server accounts in the system documentation. If accounts are determined to be shared, determine if individuals are first individually authenticated. If individuals are not individually authenticated before using the shared account (e.g., by the operating system or possibly by an application making calls to the database), this is a finding. The key is individual accountability. If this can be traced, this is not a finding. If accounts are determined to be shared, determine if they are directly accessible to end users. If so, this is a finding. Review contents of audit logs, traces and data tables to confirm that the identity of the individual user performing the action is captured. If shared identifiers are found, and not accompanied by individual identifiers, this is a finding. Note: Privileged installation accounts may be required to be accessed by the DBA or other administrators for system maintenance. In these cases, each use of the account must be logged in some manner to assign accountability for any actions taken during the use of the account.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213857`

### Rule: The Service Master Key must be backed up, stored offline and off-site.

**Rule ID:** `SV-213857r961128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backup and recovery of the Service Master Key may be critical to the complete recovery of the database. Not having this key can lead to loss of data during recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for, and evidence of backup of, the SQL Server Service Master Key in the System Security Plan. If the procedures or evidence do not exist, this is a finding. If the procedures do not indicate offline and off-site storage of the Service Master Key, this is a finding. If procedures do not indicate access restrictions to the Service Master Key backup, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-213858`

### Rule: SQL Server authentication and identity management must be integrated with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-213858r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Account management functions can also include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. Account management and authentication in a Windows environment normally use an LDAP-compatible directory service, usually Windows Active Directory. This in turn, in the DoD environment, is typically integrated with the Public Key Infrastructure (PKI). Additional technologies or products may be employed that when placed together constitute an overall mechanism supporting an organization's automated account management requirements. An example is the use of Group Policy Objects to enforce rules concerning passwords. SQL Server must be configured to use Windows authentication, with SQL Server authentication disabled. If circumstances (such as the architecture of a purchased application) make it necessary to have SQL Server authentication available, its use must be kept to a minimum. The reasons for its use, and the measures taken to restrict it to only the necessary cases, must be documented, with AO approval. It is assumed throughout this STIG that this integration has been implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether SQL Server is configured to use only Windows authentication. In the Object Explorer in SQL Server Management Studio (SSMS), right-click on the server instance; select Properties. Select the Security page. If Windows Authentication Mode is selected, this is not a finding. Alternatively, in a query interface such as the SSMS Transact-SQL editor, run the statement: EXECUTE xp_instance_regread N'HKEY_LOCAL_MACHINE', N'Software\Microsoft\MSSQLServer\MSSQLServer', N'LoginMode'; If the returned value in the "Data" column is 1, this is not a finding. Mixed mode (both SQL Server authentication and Windows authentication) is in use. If the need for mixed mode has not been documented and approved, this is a finding. From the documentation, obtain the list of accounts authorized to be managed by SQL Server. Determine the accounts (SQL Logins) actually managed by SQL Server. Run the statement: SELECT name FROM sys.sql_logins WHERE type_desc = 'SQL_LOGIN' AND is_disabled = 0; If any accounts listed by the query are not listed in the documentation, this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-213859`

### Rule: Where SQL Server Audit is in use, SQL Server must generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-213859r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. This requirement applies to SQL Server Audit-based audit trails; Trace does not have this capability. Use of SQL Server Audit's SCHEMA_OBJECT_ACCESS_GROUP causes capture of all accesses, successful and otherwise, to the system views (and all other schema-scoped objects). The [Succeeded] column in the audit output indicates the success or failure of the attempted action. Be aware, however, that it may report True in some cases where one would intuitively expect False. For example, SELECT 1/0 FROM SYS.ALL_OBJECTS will appear in the audit trail as successful, if the user has permission to perform that action, even though it contains an invalid expression. Some other actions that one would consider failures (such as selecting from a table that does not exist) may not appear at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SQL Server Trace is in use for audit purposes, and SQL Server Audit is not in use, this is not a finding. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the broad, server-level audit action group SCHEMA_OBJECT_ACCESS_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all SELECT actions on the permissions-related system views, and any locally-defined permissions tables, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'SCHEMA_OBJECT_ACCESS_GROUP'; GO If no row is returned, this is a finding. If the audited_result column is not "FAILURE" or "SUCCESS AND FAILURE", this is a finding.

## Group: SRG-APP-000109-DB-000321

**Group ID:** `V-213860`

### Rule: Where availability is paramount, the SQL Server must continue processing (preferably overwriting existing records, oldest first), in the event of lack of space for more Audit/Trace log records; and must keep processing after any failure of an Audit/Trace.

**Rule ID:** `SV-213860r960915_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is critical that when SQL Server is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When availability is an overriding concern, approved actions in response to an audit failure are as follows: (i) If the failure was caused by the lack of audit record storage capacity, the DBMS must continue generating audit records, if possible (automatically restarting the audit service if necessary), preferably overwriting the oldest audit records in a first-in-first-out manner. (ii) If audit records are sent to a centralized collection server and communication with this server is lost or the server fails, the DBMS must queue audit records locally until communication is restored or until the audit records are retrieved manually. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local audit data with the collection server. Systems where availability is paramount will most likely be MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid audit data loss in all but the most extreme situations. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. However, although Trace supports FIFO rollover, SQL Server Audit does not: its CONTINUE option stops the production of new audit records when there is an audit failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the system documentation indicates that availability does not take precedence over audit trail completeness, this is not applicable (NA). If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Audit is in use, review the defined server audits by running the statement: SELECT [name], [max_rollover_files] FROM sys.server_file_audits WHERE is_state_enabled = 1; By observing the [name] and [max_rollover_files] columns, identify the row or rows in use. If the [max_rollover_files] is greater than zero, this is not a finding. Otherwise, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-213861`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to SQL Server, etc.) must be restricted to authorized users.

**Rule ID:** `SV-213861r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SQL Server were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using the system security plan, identify the group(s)/role(s) established for SQL Server DBMS and database modification, and the individuals authorized to modify the DBMS and database(s). If helpful, the views STIG.server_permissions and STIG.database_permissions, provided in the supplemental file Permissions.sql, can be used to search for the relevant roles: look for Permission values containing "Alter," "Create," "Control," etc. Obtain the list of users in those group(s)/roles. The provided functions STIG.members_of_db_role() and STIG.members_of_server_role(), can be used for this. If unauthorized access to the group(s)/role(s) has been granted, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-213862`

### Rule: SQL Server must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-213862r961050_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of SQL Server. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Operations that require the use of cryptography include the provisioning of digital signatures, the generation and validation of cryptographic hashes, and the protection of data by storing and transmitting it in encrypted form. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In Windows, open Administrative Tools >> Local Security Policy. Expand Local Policies >> Security Options. In the right-side pane, find "System cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing". If, in the Security Setting column, the value is "Disabled," this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-213863`

### Rule: Access to database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-213863r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure that those files are not shared inappropriately and are not open to backdoor access and manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions granted to users by the operating system/file system on the database files, database transaction log files, database audit log files, and database backup files. If any user/role who is not an authorized system administrator with a need to know or database administrator with a need to know, or a system account for running DBMS processes, is permitted to read/view any of these files, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-213864`

### Rule: SQL Server must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-213864r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If the documentation requires automatic session termination, but SQL Server and Windows (or third-party tools) are not configured accordingly, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-213865`

### Rule: SQL Server must prevent non-privileged users from executing privileged functionality, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-213865r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In SQL Server, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain the definition of the SQL Server database/DBMS functionality considered privileged in the context of the system in question. Review the SQL Server security configuration and/or other means used to protect privileged functionality from unauthorized use. If the configuration does not protect all of the actions defined as privileged, this is a finding. The database permission functions and views provided in the supplemental file Permissions.sql can help with this.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-213866`

### Rule: Execution of software modules (to include stored procedures, functions, and triggers) with elevated privileges must be restricted to necessary cases only.

**Rule ID:** `SV-213866r961359_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be utilized only where necessary and protected from misuse. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation, SQL Server instance and database security configuration, source code for stored procedures, functions, and triggers, source code of external modules invoked by the DBMS, and source code of the application(s) using the database. If elevation of DBMS privileges is utilized but not documented, this is a finding. If elevation of DBMS privileges is documented, but not implemented as described in the documentation, this is a finding. If the privilege-elevation logic can be invoked in ways other than intended, or in contexts other than intended, or by subjects/principals other than intended, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-213867`

### Rule: SQL Server must utilize centralized management of the content captured in audit records generated by all components of the DBMS.

**Rule ID:** `SV-213867r981952_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. SQL Server may write audit records to files in the file system, to other kinds of local repository, or directly to a centralized log management system. (If the Trace facility is used for auditing - this is no longer recommended, but may be in place for legacy reasons - a trace table is another possible destination.) Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are off-loaded and how local audit log space is managed. If the SQL Server audit records (to include traces used for audit purposes) are not written directly to or systematically transferred to a centralized log management system, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-213868`

### Rule: SQL Server must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-213868r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, SQL Server must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the ability to reuse the space formerly occupied by off-loaded records. As noted elsewhere in this document, SQL Server's Audit and/or Trace features can be used for auditing purposes. This requirement applies to both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Investigate whether there have been any incidents where the system ran out of audit log space (to include traces used for audit purposes) since the last time the space was allocated or other corrective measures were taken. If there have been, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-213869`

### Rule: SQL Server, the operating system, or the storage system must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity.

**Rule ID:** `SV-213869r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to SQL Server on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. As noted elsewhere in this document, SQL Server's Audit and/or Trace features can be used for auditing purposes. This requirement applies to both. If support personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. The monitoring and alerting may be done at the database level, the operating system level, or by specialized monitoring tools. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system configuration. If appropriate support staff are not notified immediately upon storage volume utilization reaching 75%, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-213870`

### Rule: SQL Server or software monitoring SQL Server must provide an immediate real-time alert to appropriate support staff of all audit log failures.

**Rule ID:** `SV-213870r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. As noted elsewhere in this document, SQL Server's Audit and/or Trace features can be used for auditing purposes. This requirement applies to both. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SQL Server settings, OS, or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000374-DB-000322

**Group ID:** `V-213871`

### Rule: SQL Server must produce time stamps that can be mapped to Coordinated Universal Time (UTC, formerly GMT).

**Rule ID:** `SV-213871r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis, in audit files, trace files/tables, and application data tables. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. SQL Server obtains the date and time from the Windows operating system. In a normal configuration, the OS obtains them from an official time server, using Network Time Protocol (NTP). The ultimate source is the United States Naval Observatory Master Clock. SQL Server built-in functions for retrieving current timestamps are: (high precision) sysdatetime(), sysdatetimeoffset(), sysutcdatetime(); (lower precision) CURRENT_TIMESTAMP or getdate(), getutcdate(). Provided the operating system is synchronized with an official time server, these timestamp-retrieval functions are automatically compliant with this requirement, as are SQL Server's audit and trace capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Windows operating system is configured to synchronize with an official time server, using Network Time Protocol (NTP). If it is not, and this is not documented, with justification and AO authorization, this is a finding. If the OS does not synchronize with a time server, review the procedure for maintaining accurate time on the system. If such a procedure does not exist, this is a finding. If the procedure exists, review evidence that the correct time is actually maintained. If the evidence indicates otherwise, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-213872`

### Rule: SQL Server must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-213872r981956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. The nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. SQL Server must control software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server instance supports only software development, experimentation and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. Review the SQL Server instance and database security settings with respect to non-administrative users' ability to create, alter, or replace logic modules, to include but not necessarily only stored procedures, functions, triggers, and views. The database permission functions and views provided in the supplemental file Permissions.sql can help with this. If any such permissions exist and are not documented and approved, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-213873`

### Rule: SQL Server and Windows must enforce access restrictions associated with changes to the configuration of the SQL Server instance or database(s).

**Rule ID:** `SV-213873r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, SQL Server and Windows must allow only qualified and authorized individuals to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the security configuration of the SQL Server instance and database(s). If unauthorized Windows users can start the SQL Server Configuration Manager or SQL Server Management Studio, this is a finding. If SQL Server does not enforce access restrictions associated with changes to the configuration of the SQL Server instance or database(s), this is a finding. - - - - - To assist in conducting reviews of permissions, the following views and permissions are defined in the supplemental file Permissions.sql, provided with this STIG: database_permissions database_role_members server_permissions server_role_members database_effective_permissions('<database user/role name>') database_roles_of('<database user/role name>') members_of_db_role('<database role name>') members_of_server_role('<server role name>') server_effective_permissions('<server login/role name>') server_roles_of('<server login/role name>') Permissions of concern in this respect include the following, and possibly others: - any server permission except CONNECT SQL, but including CONNECT ANY DATABASE - any database permission beginning with "CREATE" or "ALTER" - CONTROL - INSERT, UPDATE, DELETE, EXECUTE on locally-defined tables and procedures designed for supplemental configuration and security purposes.

## Group: SRG-APP-000381-DB-000361

**Group ID:** `V-213874`

### Rule: SQL Server must produce Trace or Audit records of its enforcement of access restrictions associated with changes to the configuration of the DBMS or database(s).

**Rule ID:** `SV-213874r981958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to configuration, it would be difficult to identify attempted attacks and an audit trail would not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should be among those listed; if not, this is a finding: 102 -- Audit Statement GDR Event 103 -- Audit Object GDR Event 104 -- Audit AddLogin Event 105 -- Audit Login GDR Event 106 -- Audit Login Change Property Event 107 -- Audit Login Change Password Event 108 -- Audit Add Login to Server Role Event 109 -- Audit Add DB User Event 110 -- Audit Add Member to DB Role Event 111 -- Audit Add Role Event 112 -- Audit App Role Change Password Event 113 -- Audit Statement Permission Event 115 -- Audit Backup/Restore Event 116 -- Audit DBCC Event 117 -- Audit Change Audit Event 118 -- Audit Object Derived Permission Event 128 -- Audit Database Management Event 129 -- Audit Database Object Management Event 130 -- Audit Database Principal Management Event 131 -- Audit Schema Object Management Event 132 -- Audit Server Principal Impersonation Event 133 -- Audit Database Principal Impersonation Event 134 -- Audit Server Object Take Ownership Event 135 -- Audit Database Object Take Ownership Event 152 -- Audit Change Database Owner 153 -- Audit Schema Object Take Ownership Event 162 -- User error message 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 175 -- Audit Server Alter Trace Event 176 -- Audit Server Object Management Event 177 -- Audit Server Principal Management Event If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all configuration-related actions are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name IN ( 'APPLICATION_ROLE_CHANGE_PASSWORD_GROUP', 'AUDIT_CHANGE_GROUP', 'BACKUP_RESTORE_GROUP', 'DATABASE_CHANGE_GROUP', 'DATABASE_OBJECT_ACCESS_GROUP', 'DATABASE_OBJECT_CHANGE_GROUP', 'DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP', 'DATABASE_OBJECT_PERMISSION_CHANGE_GROUP', 'DATABASE_OPERATION_GROUP', 'DATABASE_OWNERSHIP_CHANGE_GROUP', 'DATABASE_PERMISSION_CHANGE_GROUP', 'DATABASE_PRINCIPAL_CHANGE_GROUP', 'DATABASE_PRINCIPAL_IMPERSONATION_GROUP', 'DATABASE_ROLE_MEMBER_CHANGE_GROUP', 'DBCC_GROUP', 'LOGIN_CHANGE_PASSWORD_GROUP', 'SCHEMA_OBJECT_CHANGE_GROUP', 'SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OBJECT_CHANGE_GROUP', 'SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SERVER_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OPERATION_GROUP', 'SERVER_PERMISSION_CHANGE_GROUP', 'SERVER_PRINCIPAL_IMPERSONATION_GROUP', 'SERVER_ROLE_MEMBER_CHANGE_GROUP', 'SERVER_STATE_CHANGE_GROUP', 'TRACE_CHANGE_GROUP' ); GO Examine the list produced by the query. If any of the audit action groups specified in the WHERE clause are not included in the list, this is a finding. If the audited_result column is not "SUCCESS AND FAILURE" on every row, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-213875`

### Rule: SQL Server must disable communication protocols not required for operation.

**Rule ID:** `SV-213875r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having unnecessary protocols enabled exposes the system to avoidable threats. In a typical installation, only TCP/IP will be required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system security plan to determine the communication protocols used by the SQL Server instance. Open SQL Server Configuration Manager from the Windows Start menu or by entering "SQLServerManager12.msc" in a Command Prompt window or in the Run dialog box. Select SQL Server Network Configuration >> Protocols for <instance name>. Review the list of protocols. If any that are not required are shown as enabled, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-213876`

### Rule: SQL Server must implement and/or support cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-213876r961602_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of SQL Server, Windows, and additional software as relevant. If full-disk encryption is required, and Windows or the storage system is not configured for this, this is a finding. If database transparent data encryption (TDE) is called for, check whether it is enabled: In SQL Server Management Studio, Object Explorer, expand the instance and right-click on the database name; select properties. Select the Options page, State section, Encryption Enabled parameter. If the value displayed is False, this is a finding. If column encryption, done via SQL Server features, is required, review the definitions and contents of the relevant tables and columns. If any of the information defined as requiring cryptographic protection is not encrypted in a manner that provides the required level of protection, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-213877`

### Rule: The confidentiality and integrity of information managed by SQL Server must be maintained during preparation for transmission.

**Rule ID:** `SV-213877r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, SQL Server, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If SQL Server, associated applications, and infrastructure do not employ protective measures against unauthorized disclosure and modification during preparation for transmission, this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-213878`

### Rule: The confidentiality and integrity of information managed by SQL Server must be maintained during reception.

**Rule ID:** `SV-213878r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, SQL Server, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If SQL Server, associated applications, and infrastructure do not employ protective measures against unauthorized disclosure and modification during reception, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-213879`

### Rule: Security-relevant software updates to SQL Server must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-213879r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that software patches are consistently applied to SQL Server within the time frame defined for each patch. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-213880`

### Rule: Software updates to SQL Server must be tested before being applied to production systems.

**Rule ID:** `SV-213880r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>While it is important to apply SQL Server updates in a timely manner, it is also incumbent upon the database administrator and/or system administrator to ensure that their deployment will not interfere with the operation of the database and its applications. Other than in emergency situations, SQL Server updates must be applied to appropriately configured non-production systems, and the resulting version of SQL Server assessed for correct operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that SQL Server software updates are tested before being applied to production servers, and that any exceptions are approved by the ISSM. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-213881`

### Rule: SQL Server must produce Trace or Audit records when security objects are accessed.

**Rule ID:** `SV-213881r961791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via SQL Server's built-in security functionality (GRANT, REVOKE, DENY, ALTER [SERVER] ROLE ... ADD/DROP MEMBER ..., etc.). In SQL Server, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE Since the system views are read-only, and the underlying tables are kept hidden by SQL Server, the Insert, Update and Delete cases are relevant only where the database includes user-defined tables to support additional security functionality. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. Note also that Trace does not support auditing of SELECT statements, whereas Audit does.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no locally-defined security tables, functions, or procedures, this is not applicable. If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables that require tracking of Insert-Update-Delete operations. If SQL Server Trace is in use for audit purposes, review these tables for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. Check to see that all required event classes are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (at least one of these; 90 is used in the supplied script) 162 -- User error message If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the broad, server-level audit action group SCHEMA_OBJECT_ACCESS_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all SELECT, INSERT, UPDATE, and DELETE actions on locally-defined permissions tables, and EXECUTE actions on locally-defined permissions functions and procedures, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'SCHEMA_OBJECT_ACCESS_GROUP'; If no row is returned, this is a finding. If the audited_result column is not "SUCCESS" or "SUCCESS AND FAILURE", this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-213882`

### Rule: SQL Server must produce Trace or Audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-213882r961791_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via SQL Server's built-in security functionality (GRANT, REVOKE, DENY, ALTER [SERVER] ROLE ... ADD/DROP MEMBER ..., etc.). In SQL Server, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE Since the system views are read-only, and the underlying tables are kept hidden by SQL Server, the Insert, Update and Delete cases are relevant only where the database includes user-defined tables to support additional security functionality. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016. Note also that Trace does not support auditing of SELECT statements, whereas Audit does. Use of SQL Server Audit's SCHEMA_OBJECT_ACCESS_GROUP causes capture of all accesses, successful and otherwise, to all schema-scoped objects. The [Succeeded] column in the audit output indicates the success or failure of the attempted action. Be aware, however, that it may report True in some cases where one would intuitively expect False. For example, SELECT 1/0 FROM SYS.ALL_OBJECTS will appear in the audit trail as successful, if the user has permission to perform that action, even though it contains an invalid expression. Some other actions that one would consider failures (such as selecting from a table that does not exist) may not appear at all.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no locally-defined security tables, functions, or procedures, this is not applicable (NA). If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables that require tracking of Insert-Update-Delete operations. If SQL Server Trace is in use for audit purposes, review these tables for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. Check to see that all required event classes are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (at least one of these; 90 is used in the supplied script) 162 -- User error message If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the broad, server-level audit action group SCHEMA_OBJECT_ACCESS_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all SELECT, INSERT, UPDATE, and DELETE actions on locally-defined permissions tables, and EXECUTE actions on locally-defined permissions functions and procedures, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'SCHEMA_OBJECT_ACCESS_GROUP'; If no row is returned, this is a finding. If the audited_result column is not "FAILURE" or "SUCCESS AND FAILURE", this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-213883`

### Rule: SQL Server must generate Trace or Audit records when privileges/permissions are added.

**Rule ID:** `SV-213883r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In SQL Server, adding permissions is typically done via the GRANT command, or, in the negative, DENY; or with the ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . commands. Native SQL Server security functionality may be supplemented with application-specific tables and logic, in which case the following actions on these tables and procedures/triggers/functions are also relevant: INSERT UPDATE (in cases where more than one permission can be represented in a single row) EXECUTE Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables, procedures and functions (if any) that require tracking. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (required only where there are locally-defined security tables or procedures) 102 -- Audit Database Scope GDR 103 -- Audit Object GDR Event 104 -- Audit AddLogin Event 105 -- Audit Login GDR Event 108 -- Audit Add Login to Server Role Event 109 -- Audit Add DB User Event 110 -- Audit Add Member to DB Role Event 111 -- Audit Add Role Event 162 -- User error message 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 177 -- Audit Server Principal Management Event Review the locally-defined security tables (if any) for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all GRANT, ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . actions, all INSERT and UPDATE actions on any locally-defined permissions tables, and all EXECUTE actions on any system or locally-defined permissions-related procedures and functions, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name IN ( 'DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP', 'DATABASE_OBJECT_PERMISSION_CHANGE_GROUP', 'DATABASE_OWNERSHIP_CHANGE_GROUP', 'DATABASE_PERMISSION_CHANGE_GROUP', 'DATABASE_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SERVER_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_PERMISSION_CHANGE_GROUP', 'SERVER_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_ACCESS_GROUP' ); GO Examine the list produced by the query. If any locally-defined permissions tables, procedures, or functions exist, and the list does not include the audit action group SCHEMA_OBJECT_ACCESS_GROUP, this is a finding. If any of the other audit action groups specified in the WHERE clause are not included in the list, this is a finding. If the audited_result column is not "SUCCESS" or "SUCCESS AND FAILURE" on every row, this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-213884`

### Rule: SQL Server must generate Trace or Audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-213884r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. In SQL Server, adding permissions is typically done via the GRANT command, or, in the negative, DENY; or with the ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . commands. Native security functionality may be supplemented with application-specific tables and logic, in which case the following actions on these tables and procedures/triggers/functions are also relevant: INSERT UPDATE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables, procedures and functions (if any) that require tracking. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (required only where there are locally-defined security tables or procedures) 102 -- Audit Database Scope GDR 103 -- Audit Object GDR Event 104 -- Audit AddLogin Event 105 -- Audit Login GDR Event 108 -- Audit Add Login to Server Role Event 109 -- Audit Add DB User Event 110 -- Audit Add Member to DB Role Event 111 -- Audit Add Role Event 162 -- User error message 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 177 -- Audit Server Principal Management Event Review the locally-defined security tables (if any) for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all GRANT, ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . actions, all INSERT and UPDATE actions on any locally-defined permissions tables, and all EXECUTE actions on any system or locally-defined permissions-related procedures and functions, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name IN ( 'DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP', 'DATABASE_OBJECT_PERMISSION_CHANGE_GROUP', 'DATABASE_OWNERSHIP_CHANGE_GROUP', 'DATABASE_PERMISSION_CHANGE_GROUP', 'DATABASE_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SERVER_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_PERMISSION_CHANGE_GROUP', 'SERVER_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_ACCESS_GROUP' ); GO Examine the list produced by the query. If any locally-defined permissions tables, procedures, or functions exist, and the list does not include the audit action group SCHEMA_OBJECT_ACCESS_GROUP, this is a finding. If any of the other audit action groups specified in the WHERE clause are not included in the list, this is a finding. If the audited_result column is not "FAILURE" or "SUCCESS AND FAILURE" on every row, this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-213885`

### Rule: SQL Server must generate Trace or Audit records when privileges/permissions are deleted.

**Rule ID:** `SV-213885r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In SQL Server, deleting permissions is typically done via the REVOKE or DENY command; or with the ALTER SERVER ROLE . . . DROP MEMBER . . . and/or ALTER ROLE . . . DROP MEMBER . . . statements. However, native SQL Server security functionality may be supplemented with application-specific tables and logic, in which case the following actions on these tables and procedures/triggers/functions are also relevant: DELETE EXECUTE Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables (if any) that require tracking of Insert-Update-Delete operations. If SQL Server Trace is in use for audit purposes, review these tables for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. Check to see that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (required only where there are locally-defined security tables or procedures) 102 -- Audit Database Scope GDR 103 -- Audit Object GDR Event 104 -- Audit AddLogin Event 105 -- Audit Login GDR Event 108 -- Audit Add Login to Server Role Event 109 -- Audit Add DB User Event 110 -- Audit Add Member to DB Role Event 111 -- Audit Add Role Event 162 -- User error message 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 177 -- Audit Server Principal Management Event If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all GRANT, ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . actions, all INSERT and UPDATE actions on any locally-defined permissions tables, and all EXECUTE actions on any system or locally-defined permissions-related procedures and functions, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name IN ( 'DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP', 'DATABASE_OBJECT_PERMISSION_CHANGE_GROUP', 'DATABASE_OWNERSHIP_CHANGE_GROUP', 'DATABASE_PERMISSION_CHANGE_GROUP', 'DATABASE_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SERVER_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_PERMISSION_CHANGE_GROUP', 'SERVER_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_ACCESS_GROUP' ); GO Examine the list produced by the query. If any locally-defined permissions tables, procedures, or functions exist, and the list does not include the audit action group SCHEMA_OBJECT_ACCESS_GROUP, this is a finding. If any of the other audit action groups specified in the WHERE clause are not included in the list, this is a finding. If the audited_result column is not "SUCCESS" or "SUCCESS AND FAILURE" on every row, this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-213886`

### Rule: SQL Server must generate Trace or Audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-213886r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In SQL Server, deleting permissions is typically done via the REVOKE or DENY command; or with the ALTER SERVER ROLE . . . DROP MEMBER . . . and/or ALTER ROLE . . . DROP MEMBER . . . statements. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. Obtain the list of locally-defined security tables (if any) that require tracking of Insert-Update-Delete operations. If SQL Server Trace is in use for audit purposes, review these tables for the existence of triggers to raise a custom event on each Insert-Update-Delete operation. If such triggers are not present, this is a finding. Check to see that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 42 -- SP:Starting 43 -- SP:Completed 82-91 -- User-defined Event (required only where there are locally-defined security tables or procedures) 102 -- Audit Database Scope GDR 103 -- Audit Object GDR Event 104 -- Audit AddLogin Event 105 -- Audit Login GDR Event 108 -- Audit Add Login to Server Role Event 109 -- Audit Add DB User Event 110 -- Audit Add Member to DB Role Event 111 -- Audit Add Role Event 162 -- User error message 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 177 -- Audit Server Principal Management Event If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all GRANT, ALTER SERVER ROLE . . . ADD MEMBER . . ., and/or ALTER ROLE . . . ADD MEMBER . . . actions, all INSERT and UPDATE actions on any locally-defined permissions tables, and all EXECUTE actions on any system or locally-defined permissions-related procedures and functions, are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name IN ( 'DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP', 'DATABASE_OBJECT_PERMISSION_CHANGE_GROUP', 'DATABASE_OWNERSHIP_CHANGE_GROUP', 'DATABASE_PERMISSION_CHANGE_GROUP', 'DATABASE_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP', 'SERVER_OBJECT_PERMISSION_CHANGE_GROUP', 'SERVER_PERMISSION_CHANGE_GROUP', 'SERVER_ROLE_MEMBER_CHANGE_GROUP', 'SCHEMA_OBJECT_ACCESS_GROUP' ); GO Examine the list produced by the query. If any locally-defined permissions tables, procedures, or functions exist, and the list does not include the audit action group SCHEMA_OBJECT_ACCESS_GROUP, this is a finding. If any of the other audit action groups specified in the WHERE clause are not included in the list, this is a finding. If the audited_result column is not "FAILURE" or "SUCCESS AND FAILURE" on every row, this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-213887`

### Rule: SQL Server must generate Trace or Audit records when successful logons or connections occur.

**Rule ID:** `SV-213887r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to SQL Server. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 14 -- Audit Login 15 -- Audit Logout 16 -- Attention 17 -- ExistingConnection If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the server-level audit action group SUCCESSFUL_LOGIN_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all logons and connections are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'SUCCESSFUL_LOGIN_GROUP'; GO If no row is returned, this is a finding. If the "SUCCESSFUL_LOGIN_GROUP" is returned with the audited_result_column of "SUCCESS" or "SUCCESS AND FAILURE", this is not a finding. If "SUCCESSFUL_LOGIN_GROUP" is not in the active audit, determine whether "Both failed and successful logins" is enabled. In SQL Management Studio: Right-click on the instance. >> Select "Properties". >> Select "Security" on the left side. >> Check the setting for "Login auditing". If "Both failed and successful logins" is not selected, this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-213888`

### Rule: SQL Server must generate Trace or Audit records when unsuccessful logons or connection attempts occur.

**Rule ID:** `SV-213888r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to SQL Server. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event ID should be among those listed; if not, this is a finding: 20 -- Audit Login Failed If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the server-level audit action group FAILED_LOGIN_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all logons and connections are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'FAILED_LOGIN_GROUP'; GO If no row is returned, this is a finding. If the "FAILED_LOGIN_GROUP" is returned with the audited_result_column of "FAILURE" or "SUCCESS AND FAILURE", this is not a finding. If "FAILED_LOGIN_GROUP" is not in the active audit, determine whether "Both failed and successful logins" is enabled. In SQL Management Studio: Right-click on the instance. >> Select "Properties". >> Select "Security" on the left side. >> Check the setting for "Login auditing". If "Both failed and successful logins" is not selected, this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-213889`

### Rule: SQL Server must generate Trace or Audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-213889r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. This encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 46 -- Object:Created 47 -- Object:Deleted 82-91 -- User-defined Event (required only where there are locally-defined auditable actions) 115 -- Audit Backup/Restore Event 116 -- Audit DBCC Event 117 -- Audit Change Audit Event 118 -- Audit Object Derived Permission Event 128 -- Audit Database Management Event 129 -- Audit Database Object Management Event 130 -- Audit Database Principal Management Event 131 -- Audit Schema Object Management Event 164 -- Object:Altered 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 175 -- Audit Server Alter Trace Event 176 -- Audit Server Object Management Event 177 -- Audit Server Principal Management Event From the system security plan, obtain the list of any other actions considered privileged. For each, verify that event IDs (and triggers, where necessary) have been defined to capture audit information for these. If they have not, this is a finding. If SQL Server Audit is in use, verify that execution of all CREATE, ALTER, DROP, GRANT, REVOKE and DENY statements, all execution of security-related functions and procedures, and all other actions locally defined as privileged, is audited. If any such actions are not audited, this is a finding. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all configuration-related actions are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>'); GO Examine the list produced by the query. If the audited_result column is not "SUCCESS" or "SUCCESS AND FAILURE" on every row, this is a finding. If any of the audit action groups listed below is not included in the query results, this is a finding. If there are locally-defined privileged activities not encompassed by the list below and not tracked in any other way, this is a finding. APPLICATION_ROLE_CHANGE_PASSWORD_GROUP AUDIT_CHANGE_GROUP BACKUP_RESTORE_GROUP DATABASE_CHANGE_GROUP DATABASE_OBJECT_ACCESS_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP FAILED_LOGIN_GROUP LOGIN_CHANGE_PASSWORD_GROUP LOGOUT_GROUP SCHEMA_OBJECT_ACCESS_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP SERVER_OBJECT_CHANGE_GROUP SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP SERVER_OBJECT_PERMISSION_CHANGE_GROUP SERVER_OPERATION_GROUP SERVER_PERMISSION_CHANGE_GROUP SERVER_PRINCIPAL_CHANGE_GROUP SERVER_PRINCIPAL_IMPERSONATION_GROUP SERVER_ROLE_MEMBER_CHANGE_GROUP SERVER_STATE_CHANGE_GROUP SUCCESSFUL_LOGIN_GROUP TRACE_CHANGE_GROUP

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-213890`

### Rule: SQL Server must generate Trace or Audit records when unsuccessful attempts to execute privileged activities or other system-level access occur.

**Rule ID:** `SV-213890r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. This encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should all be among those listed; if not, this is a finding: 46 -- Object:Created 47 -- Object:Deleted 82-91 -- User-defined Event (required only where there are locally-defined auditable actions) 115 -- Audit Backup/Restore Event 116 -- Audit DBCC Event 117 -- Audit Change Audit Event 118 -- Audit Object Derived Permission Event 128 -- Audit Database Management Event 129 -- Audit Database Object Management Event 130 -- Audit Database Principal Management Event 131 -- Audit Schema Object Management Event 164 -- Object:Altered 170 -- Audit Server Scope GDR Event 171 -- Audit Server Object GDR Event 172 -- Audit Database Object GDR Event 173 -- Audit Server Operation Event 175 -- Audit Server Alter Trace Event 176 -- Audit Server Object Management Event 177 -- Audit Server Principal Management Event From the system security plan, obtain the list of any other actions considered privileged. For each, verify that event IDs (and triggers, where necessary) have been defined to capture audit information for these. If they have not been defined to capture audit information, this is a finding. If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses broad, server-level audit action groups for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following code to verify that all configuration-related actions are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>'); GO Examine the list produced by the query.. If the audited_result column is not "FAILURE" or "SUCCESS AND FAILURE" on every row, this is a finding. If any of the audit action groups listed below is not included in the query results, this is a finding. If there are locally-defined privileged activities not encompassed by the list below and not tracked in any other way, this is a finding. APPLICATION_ROLE_CHANGE_PASSWORD_GROUP AUDIT_CHANGE_GROUP BACKUP_RESTORE_GROUP DATABASE_CHANGE_GROUP DATABASE_OBJECT_ACCESS_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP FAILED_LOGIN_GROUP LOGIN_CHANGE_PASSWORD_GROUP LOGOUT_GROUP SCHEMA_OBJECT_ACCESS_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP SERVER_OBJECT_CHANGE_GROUP SERVER_OBJECT_OWNERSHIP_CHANGE_GROUP SERVER_OBJECT_PERMISSION_CHANGE_GROUP SERVER_OPERATION_GROUP SERVER_PERMISSION_CHANGE_GROUP SERVER_PRINCIPAL_CHANGE_GROUP SERVER_PRINCIPAL_IMPERSONATION_GROUP SERVER_ROLE_MEMBER_CHANGE_GROUP SERVER_STATE_CHANGE_GROUP SUCCESSFUL_LOGIN_GROUP TRACE_CHANGE_GROUP

## Group: SRG-APP-000505-DB-000352

**Group ID:** `V-213891`

### Rule: SQL Server must generate Trace or Audit records when logoffs or disconnections occur.

**Rule ID:** `SV-213891r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to and off from SQL Server. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should be among those listed; if not, this is a finding: 14 -- Audit Login 15 -- Audit Logout 16 -- Attention 17 -- ExistingConnection If SQL Server Audit is in use, proceed as follows. The basic SQL Server Audit configuration provided in the supplemental file Audit.sql uses the server-level audit action group LOGOUT_GROUP for this purpose. SQL Server Audit's flexibility makes other techniques possible. If an alternative technique is in use and demonstrated effective, this is not a finding. Determine the name(s) of the server audit specification(s) in use. To look at audits and audit specifications, in Management Studio's object explorer, expand <server name> >> Security >> Audits and <server name> >> Security >> Server Audit Specifications. Also, <server name> >> Databases >> <database name> >> Security >> Database Audit Specifications. Alternatively, review the contents of the system views with "audit" in their names. Run the following to verify that all logons and connections are being audited: USE [master]; GO SELECT * FROM sys.server_audit_specification_details WHERE server_specification_id = (SELECT server_specification_id FROM sys.server_audit_specifications WHERE [name] = '<server_audit_specification_name>') AND audit_action_name = 'LOGOUT_GROUP'; GO If no row is returned, this is a finding. If the audited_result column is not "SUCCESS AND FAILURE", this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-213892`

### Rule: SQL Server must generate Trace or Audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-213892r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to SQL Server. Concurrent connections by the same user from multiple workstations may be valid use of the system; or such connections may be due to improper circumvention of the requirement to use the CAC for authentication; or they may indicate unauthorized account sharing; or they may be because an account has been compromised. If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), then it is not mandatory to create additional log entries specifically for this. Use of SQL Server Audit is recommended. All features of SQL Server Audit are available in the Enterprise and Developer editions of SQL Server 2014. It is not available at the database level in other editions. For this or legacy reasons, the instance may be using SQL Server Trace for auditing, which remains an acceptable solution for the time being. Note, however, that Microsoft intends to remove most aspects of Trace at some point after SQL Server 2016.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If neither SQL Server Audit nor SQL Server Trace is in use for audit purposes, this is a finding. If SQL Server Trace is in use for audit purposes, verify that all required events are being audited. From the query prompt: SELECT * FROM sys.traces; All currently defined traces for the SQL server instance will be listed. If no traces are returned, this is a finding. Determine the trace(s) being used for the auditing requirement. In the following, replace # with a trace ID being used for the auditing requirements. From the query prompt: SELECT DISTINCT(eventid) FROM sys.fn_trace_geteventinfo(#); The following required event IDs should be among those listed; if not, this is a finding: 14 -- Audit Login 15 -- Audit Logout 16 -- Attention 17 -- ExistingConnection If SQL Server Audit is in use, verify that the SUCCESSFUL_LOGIN_GROUP and LOGOUT_GROUP are enabled, as described in other STIG requirements; if not, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-213893`

### Rule: SQL Server must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-213893r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system. This applies to all data output for audit trail purposes, whether produced by SQL Server Audit, Trace, or other means; but excluding audit-trail information built into application data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are off-loaded. If the database server has a continuous network connection to the centralized log management system, but the SQL Server audit records are not written directly to the centralized log management system or transferred in near-real-time, this is a finding. If the database server does not have a continuous network connection to the centralized log management system, and the SQL Server audit records are not transferred to the centralized log management system weekly or more often, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-213894`

### Rule: If SQL Server authentication, using passwords, is employed, SQL Server must enforce the DoD standards for password complexity.

**Rule ID:** `SV-213894r981946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows domain/enterprise authentication and identification must be used (SQL4-00-030300). Native SQL Server authentication may be used only when circumstances make it unavoidable; and must be documented and AO-approved. The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DoD standards for password complexity must be implemented. The requirements for password complexity are: a. minimum of 15 Characters, 1 of each of the following character sets: - Upper-case - Lower-case - Numeric - Special characters (e.g. ~ ! @ # $ % ^ & * ( ) _ + = - ' [ ] / ? > <)]; b. Minimum number of characters changed from previous password: 50% of the minimum password length (that is, 8). To enforce this in SQL Server, configure each DBMS-managed login to inherit the rules from Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the statement: SELECT name FROM sys.sql_logins WHERE type_desc = 'SQL_LOGIN' AND is_disabled = 0 AND is_policy_checked = 0 ; If no account names are listed, this is not a finding. For each account name listed, determine whether it is documented as requiring exemption from the standard password complexity rules, if it is not, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-213895`

### Rule: If SQL Server authentication, using passwords, is employed, SQL Server must enforce the DoD standards for password lifetime.

**Rule ID:** `SV-213895r981946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Windows domain/enterprise authentication and identification must be used (SQL4-00-030300). Native SQL Server authentication may be used only when circumstances make it unavoidable; and must be documented and AO-approved. The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DoD standards for password lifetime must be implemented. The requirements for password lifetime are: a. Password lifetime limits for interactive accounts: Minimum 24 hours, Maximum 60 days b. Password lifetime limits for non-interactive accounts: Minimum 24 hours, Maximum 365 days c. Number of password changes before an old one may be reused: Minimum of 5. To enforce this in SQL Server, configure each DBMS-managed login to inherit the rules from Windows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the statement: SELECT name FROM sys.sql_logins WHERE type_desc = 'SQL_LOGIN' AND is_disabled = 0 AND is_expiration_checked = 0; If no account names are listed, this is not a finding. For each account name listed, determine whether it is documented as requiring exemption from the standard password lifetime rules, if it is not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213896`

### Rule: Applications must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-213896r961047_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. Database applications may allow for entry of the account name and password as a visible parameter of the application execution command. This practice must be prohibited and disabled to prevent shoulder surfing. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether any applications that access the database allow for entry of the account name and password, or PIN. If any do, determine whether these applications obfuscate authentication data; if they do not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213897`

### Rule: When using command-line tools such as SQLCMD in a mixed-mode authentication environment, users must use a logon method that does not expose the password.

**Rule ID:** `SV-213897r961047_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. This requirement is applicable when mixed-mode authentication is enabled. When this is the case, password-authenticated accounts can be created in and authenticated by SQL Server. Other STIG requirements prohibit the use of mixed-mode authentication except when justified and approved. This deals with the exceptions. SQLCMD and other command-line tools are part of any SQL Server installation. These tools can accept a plain-text password, but do offer alternative techniques. Since the typical user of these tools is a database administrator, the consequences of password compromise are particularly serious. Therefore, the use of plain-text passwords must be prohibited, as a matter of practice and procedure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run this query to determine whether SQL Server authentication is enabled: EXEC master.sys.xp_loginconfig 'login mode'; If the config_value returned is "Windows NT Authentication", this is not a finding. For SQLCMD, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations; and that AO approval has been obtained; if not, this is a finding. Request evidence that all users of the tool are trained in the importance of not using the plain-text password option and in how to keep the password hidden; and that they adhere to this practice; if not, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-213898`

### Rule: The SQL Server Browser service must be disabled if its use is not necessary..

**Rule ID:** `SV-213898r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The SQL Server Browser simplifies the administration of SQL Server, particularly when multiple instances of SQL Server coexist on the same computer. It avoids the need to hard-assign port numbers to the instances and to set and maintain those port numbers in client systems. It enables administrators and authorized users to discover database management system instances, and the databases they support, over the network. This convenience also presents the possibility of unauthorized individuals gaining knowledge of the available SQL Server resources. Therefore, it is necessary to consider whether the SQL Server Browser is needed. Typically, if only a single instance is installed, using the default name (MSSQLSERVER) and port assignment (1433), the Browser is not adding any value. The more complex the installation, the more likely SQL Server Browser is to be helpful. This requirement is not intended to prohibit use of the Browser service in any circumstances; rather, it calls for administrators and management to consider whether the benefits of its use outweigh the potential negative consequences.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the need for the SQL Server Browser service is documented, with appropriate approval, this is not a finding. Open the Services tool. Either navigate, via the Windows Start Menu and/or Control Panel, to "Administrative Tools", and select "Services"; or at a command prompt, type "services.msc" and press the "Enter" key. Scroll to "SQL Server Browser". If its Startup Type is not shown as "Disabled", this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-265639`

### Rule: Microsoft SQL Server products must be a version supported by the vendor.

**Rule ID:** `SV-265639r998191_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the version and release information. Verify the SQL Server version via one of the following methods: Connect to the server by using Object Explorer in SQL Server Management Studio. After Object Explorer is connected, it will show the version information in parentheses, together with the user name that is used to connect to the specific instance of SQL Server. Or, from SQL Server Management Studio: SELECT @@VERSION; More information for finding the version is available at the following link: https://learn.microsoft.com/en-us/troubleshoot/sql/releases/find-my-sql-version SQL Server 2014 is no longer supported by the vendor. If the system is running SQL Server 2014 or earlier, this is a finding.

