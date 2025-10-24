# STIG Benchmark: IBM DB2 V10.5 LUW Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-213670`

### Rule: DB2 must limit the number of concurrent sessions to an organization-defined number per user for all accounts and/or account types.

**Rule ID:** `SV-213670r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether the system documentation specifies limits on the number of concurrent DBMS sessions per account by type of user. If it does not, assume a limit of 10 for database administrators and 2 for all other users. The DB2 CONNECT_PROC configuration parameter allows the input of a two-part connect procedure name that will implicitly be executed every time an application connects to the database. Find the value of CONNECT_PROC by running the following command: $db2 get db cfg If the value of CONNECT_PROC is null (i.e., not set), this is a finding. If the value of CONNECT_PROC is set, run the following command to review the DDL for the connect procedure: DB2> SELECT text FROM SYSCAT.ROUTINES WHERE ROUTINENAME=<MY_CONNECT> If the connect procedure does not restrict the user sessions as per organization guidelines, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-213671`

### Rule: DB2 must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-213671r879522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Account management functions can also include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. The DBMS must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The default name and location for the IBM LDAP security plug-in configuration file is: On UNIX/LINUX: INSTHOME/sqllib/cfg/IBMLDAPSecurity.ini On Windows: %DB2PATH%\cfg\IBMLDAPSecurity.ini If the IBMLDAPSecurity.ini file does not exist in the default location and environment variable DB2LDAPSecurityConfig is not set, this is a finding. If the environment variable DB2LDAPSecurityConfig is set and file does not exist in DB2LDAPSecurityConfig location, this is a finding. Find the value of SRVCON_PW_PLUGIN by running $db2 get dbm cfg If SRVCON_PW_PLUGIN is not set to IBMLDAPauthserver, this is a finding. Note: In Windows, find the location of base installation directory of DB2 using one of following methods 1. Find the value of DB2PATH variable using db2set –all on DB2 CLP 2. Run db2level command 3. Go to Registry Editor in Windows Computer >> HKEY_LOCAL_MACHINE >> SOFTWARE >> IBM >> DB2 >> installedCopies >> DB2COPY1 Then find the value of the DB2 Path Name

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-213672`

### Rule: DB2 must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-213672r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access the DBMS. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following query to determine if PUBLIC has been directly granted any privileges on objects in the database: DB2> SELECT PRIVILEGE, OBJECTNAME, OBJECTSCHEMA, OBJECTTYPE FROM SYSIBMADM.PRIVILEGES WHERE AUTHID = 'PUBLIC' If any rows are returned, this is a finding. Use the following query to determine if PUBLIC has been granted membership in any database roles: DB2> SELECT ROLENAME FROM TABLE (SYSPROC.AUTH_LIST_ROLES_FOR_AUTHID ('PUBLIC', 'G') ) For each role returned by this query, determine if any privileges have been granted to it with the following query: DB2> SELECT PRIVILEGE, OBJECTNAME, OBJECTSCHEMA, OBJECTTYPE FROM SYSIBMADM.PRIVILEGES WHERE AUTHID = '<rolename>' AND AUTHIDTYPE = 'R' If any rows are returned, this is a finding. Use the following query to determine if PUBLIC has been granted any database authorities directly or indirectly through a database role: DB2> SELECT AUTHORITY, D_PUBLIC, ROLE_PUBLIC FROM TABLE(SYSPROC.AUTH_LIST_AUTHORITIES_FOR_AUTHID ('PUBLIC', 'G') ) If any of the rows have a ‘Y’ value in the D_PUBLIC column, this is a finding. If any of the rows have a ‘Y’ value in the ROLE_PUBLIC column, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213673`

### Rule: DB2 must protect against a user falsely repudiating having performed organization-defined actions.

**Rule ID:** `SV-213673r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables, and configuring the DBMS' audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, group account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon all the required application tables and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the database audit policy has the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) as well as the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If the database policy does not exist or does not cover CONTEXTSTATUS or EXECUTESTATUS then check if the appropriate policies are defined for all the required application tables. If all the required application table audit policies do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) as well as the value in the ERRORTYPE column set to 'A' (Audit), this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-213674`

### Rule: DB2 must provide audit record generation capability for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-213674r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the DBMS (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements, at the minimum AUDIT, CHECKING, CONTEXT, SECMAINT, SYSADMIN, and VALIDATE category auditing need to be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from the query above find the details of the audit policy. DB2> SELECT AUDITPOLICYNAME, AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSADMINSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSMADMINSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-213675`

### Rule: DB2 must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-213675r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the SYSADM_GROUP parameter: $db2 get dbm cfg Only users approved by the ISSM should be part of the SYSADM_GROUP. If non-ISSM authorized users are part of SYSADM_GROUP group, this is a finding. On Windows systems, if the SYSADM_GROUP database manager configuration parameter is not specified, this is a finding. Database level audit The security administrator (who holds SECADM authority within a database) can define audit policies and control the audit requirements for an individual database. The security administrator can use the following audit routines to operate upon the database audit logs: - The SYSPROC.AUDIT_ARCHIVE stored procedure archives audit logs. - The SYSPROC.AUDIT_LIST_LOGS table function allows you to locate logs of interest. - The SYSPROC.AUDIT_DELIM_EXTRACT stored procedure extracts data into delimited files for analysis. The security administrator can also grant EXECUTE privilege on these routines to another user. Run the following query to find out which users have SECADM authority in database: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.DBAUTH WHERE SECURITYADMAUTH='Y' If GRANTEETYPE is 'U' and the authorization ID is not an ISSM authorized user, this is a finding. If the GRANTEETYPE is 'G', then all members of the external group identified by GRANTEE must be ISSM authorized users, otherwise this is a finding. If the GRANTEETYPE is 'R', then all members of the database role identified by GRANTEE must be ISSM authorized users, otherwise this is a finding. The members of a role can be found using this statement: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.ROLEAUTH WHERE ROLENAME= <search role name> Run the following query to find out which users have execute privilege on SYSPROC.AUDIT_ARCHIVE, SYSPROC.AUDIT_LIST_LOGS, SYSPROC.AUDIT_DELIM_EXTRACT: DB2> SELECT * FROM SYSCAT.ROUTINEAUTH WHERE SPECIFICNAME LIKE 'AUDIT%' AND SCHEMA='SYSPROC' If non-ISSM authorized users have execute privilege on any of above three routines, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-213676`

### Rule: DB2 must generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-213676r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To monitor who/what is reading the privilege/permission/role information from catalog tables a minimum audit set of CONTEXT and EXECUTE (with data) categories on the following catalog tables are required: SYSIBM.SYSINDEXAUTH SYSIBM.SYSPLANAUTH SYSIBM.SYSPASSTHRUAUTH SYSIBM.SYSROUTINEAUTH SYSIBM.SYSSCHEMAAUTH SYSIBM.SYSSECURITYLABELACCESS SYSIBM.SYSSECURITYPOLICYEXEMPTIONS SYSIBM.SYSSEQUENCEAUTH SYSIBM.SYSSURROGATEAUTHIDS SYSIBM.SYSTABAUTH SYSIBM.SYSTBSPACEAUTH SYSIBM.SYSXSROBJECTAUTH SYSIBM.SYSCOLAUTH SYSIBM.SYSLIBRARYAUTH SYSIBM.SYSMODULEAUTH SYSIBM.SYSROLEAUTH SYSIBM.SYSVARIABLEAUTH SYSIBM.SYSWORKLOADAUTH SYSIBM.SYSDBAUTH SYSIBM.SYSUSERAUTH Run the following SQL statement to ensure that an audit policy is defined upon the above catalog tables and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with the OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the values for CONTEXTSTATUS and EXECUTESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding. If a database policy does not exist or does not cover CONTEXTSTATUS or EXECUTESTATUS then check if the appropriate policies are defined for all the required tables listed above. If audit policies for the required tables do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-213677`

### Rule: DB2 must generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-213677r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that the DBMS continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To monitor who/what is reading the privilege/permission/role information from catalog tables a minimum audit set of CONTEXT and EXECUTE (with data) categories on the following catalog tables are required: SYSIBM.SYSINDEXAUTH SYSIBM.SYSPLANAUTH SYSIBM.SYSPASSTHRUAUTH SYSIBM.SYSROUTINEAUTH SYSIBM.SYSSCHEMAAUTH SYSIBM.SYSSECURITYLABELACCESS SYSIBM.SYSSECURITYPOLICYEXEMPTIONS SYSIBM.SYSSEQUENCEAUTH SYSIBM.SYSSURROGATEAUTHIDS SYSIBM.SYSTABAUTH SYSIBM.SYSTBSPACEAUTH SYSIBM.SYSXSROBJECTAUTH SYSIBM.SYSCOLAUTH SYSIBM.SYSLIBRARYAUTH SYSIBM.SYSMODULEAUTH SYSIBM.SYSROLEAUTH SYSIBM.SYSVARIABLEAUTH SYSIBM.SYSWORKLOADAUTH SYSIBM.SYSDBAUTH SYSIBM.SYSUSERAUTH Run the following SQL statement to ensure that an audit policy is defined upon the above catalog tables and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with the OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the values for CONTEXTSTATUS and EXECUTESTATUS in the database audit policy are not 'F' (Failure) or 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding. If a database policy does not exist or does not cover CONTEXTSTATUS or EXECUTESTATUS then check if the appropriate policies are defined for all the required tables listed above. If audit policies for the required tables do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'F' (Failure) or 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-213678`

### Rule: DB2 must initiate session auditing upon startup.

**Rule ID:** `SV-213678r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is for use when a user's activities are under investigation. To be sure of capturing all activity during those periods when session auditing is in use, it needs to be in operation for the whole time the DBMS is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether there are any individuals for whom the organization requires session auditing. If there are none, this is not a finding. Type in the following command to check whether or not the user under investigation is being audited: DB2> SELECT AUDITPOLICYNAME, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('i',' ') If no rows are returned, this is a finding. If a row with the OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with the OBJECTTYPE of 'i' exists in the output, it is a user level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that all categories are part of that policy: DB2> SELECT * FROM SYSCAT.AUDITPOLICIES If there is an audit policy defined at the database level with the values for the all the audit category columns set to 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), EXECUTEWITHDATA to 'Y' this is not a finding. If the database policy does not exist or does not cover all the categories with ERRORTYPE column set to 'A' (Audit), EXECUTEWITHDATA to 'Y' then check if the appropriate policies are defined for all the required users. If the audit policy is defined on the users under investigation and does not have the values for all the audit category columns set to 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), EXECUTEWITHDATA to 'Y', this is a finding.

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-213679`

### Rule: DB2 must produce audit records containing sufficient information to establish the outcome (success or failure) of the events.

**Rule ID:** `SV-213679r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the information system after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to confirm that all audit policies are created with STATUS='B': DB2> SELECT * FROM SYSCAT.AUDITPOLICIES If any audit policy does not have the values for all the audit category columns set to 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), EXECUTEWITHDATA to 'Y' for Execute category audit policies, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-213680`

### Rule: DB2 must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-213680r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. To support analysis, some types of events will need information to be logged that exceeds the basic requirements of event type, time stamps, location, source, outcome, and user identity. If additional information is not available, it could negatively impact forensic investigations into user actions or other malicious events. The organization must determine what additional information is required for complete analysis of the audited events. The additional information required is dependent on the type of information (e.g., sensitivity of the data and the environment within which it resides). At a minimum, the organization must employ either full-text recording of privileged commands or the individual identities of group users, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Examples of detailed information the organization may require in audit records are full-text recording of privileged commands or the individual identities of group account users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check with the ISSO if any more of the organization-defined information needs to be captured as part of DBMS auditing. If there is additional information that needs to be captured and is currently not being written to audit logs, this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-213681`

### Rule: Unless it has been determined that availability is paramount, DB2 must, upon audit failure, cease all auditable activity.

**Rule ID:** `SV-213681r879571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the DBMS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. When the need for system availability does not outweigh the need for a complete audit trail, the DBMS should cease production of audit records immediately, rolling back all in-flight transactions. DB2 does this when configured to track audit errors. Systems where audit trail completeness is paramount will most likely be at a lower MAC level than MAC I; the final determination is the prerogative of the application owner, subject to Authorizing Official concurrence. In any case, sufficient auditing resources must be allocated to avoid a shutdown in all but the most extreme situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the ISSO whether the system should stay available or stop processing the auditable events. If the system needs to stay available and the Error Type is set to 'A' for the policies then this is not applicable (NA). Run the following SQL statement to find the Error type value for all audit policies: DB2> SELECT * FROM SYSCAT.AUDITPOLICIES If the system needs to stop processing the auditable events and Error Type is not set to 'A' then this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-213682`

### Rule: The audit information produced by DB2 must be protected from unauthorized read access.

**Rule ID:** `SV-213682r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run db2audit command to find the value of datapath where the audit logs are stored. $db2audit describe Only the instance owner needs write access to directory and users authorized to archive the audit logs need to have read access to audit directory. If any user other than the instance owner has write access to audit directory, this is a finding. If any user other than the users authorized to read audit log files have read access to audit directory, this is a finding.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-213683`

### Rule: The audit information produced by DB2 must be protected from unauthorized modification.

**Rule ID:** `SV-213683r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods that will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the db2audit command to find the value of the datapath where the audit logs are stored. $db2audit describe Only the instance owner needs write access to directory and users authorized to archive the audit logs need to have read access to the audit directory. If any user other than the instance owner has write access to the audit directory, this is a finding. If any user other than the users authorized to read audit log files have read access to audit directory, this is a finding.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-213684`

### Rule: The audit information produced by DB2 must be protected from unauthorized deletion.

**Rule ID:** `SV-213684r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the db2audit command to find the value of the datapath where the audit logs are stored. $db2audit describe Only the instance owner needs write access to directory and users authorized to archive the audit logs need to have read access to the audit directory. If any user other than the instance owner has write access to audit directory, this is a finding. If any user other than the users authorized to read audit log files have read access to the audit directory, this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-213685`

### Rule: DB2 must protect its audit features from unauthorized access.

**Rule ID:** `SV-213685r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the SYSADM_GROUP parameter: $db2 get dbm cfg Only authorized OS users should be part of this group. If non-authorized users are part of SYSADM_GROUP group, this is a finding. On Windows systems, if the SYSADM_GROUP database manager configuration parameter is not specified, this is a finding. Security administrator (who holds SECADM authority within a database) can define audit policies and control the audit requirements for an individual database. The security administrator can use the following audit routines to operate upon the database audit logs: - The SYSPROC.AUDIT_ARCHIVE stored procedure archives audit logs. - The SYSPROC.AUDIT_LIST_LOGS table function allows you to locate logs of interest. - The SYSPROC.AUDIT_DELIM_EXTRACT stored procedure extracts data into delimited files for analysis. The security administrator can also grant EXECUTE privilege on these routines to another user. Run the following query to find out which users have SECADM authority in database: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.DBAUTH WHERE SECURITYADMAUTH='Y' If GRANTEETYPE is 'U' and the authorization ID is not an authorized user, this is a finding. If the GRANTEETYPE is 'G', then all members of the external group identified by GRANTEE must be authorized users. Otherwise, this is a finding. If the GRANTEETYPE is 'R', then all members of the database role identified by GRANTEE must be authorized users. Otherwise, this is a finding. The members of a role can be found using this statement: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.ROLEAUTH WHERE ROLENAME= <search role name> Run the following query to find out which users have execute privilege on SYSPROC.AUDIT_ARCHIVE, SYSPROC.AUDIT_LIST_LOGS, SYSPROC.AUDIT_DELIM_EXTRACT: DB2> SELECT * FROM SYSCAT.ROUTINEAUTH WHERE SPECIFICNAME LIKE 'AUDIT%' AND SCHEMA='SYSPROC' If non-authorized users have EXECUTE privilege on any of the above three routines, this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-213686`

### Rule: DB2 must protect its audit configuration from unauthorized modification.

**Rule ID:** `SV-213686r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the SYSADM_GROUP parameter: $db2 get dbm cfg Only authorized OS users should be part of this group. If non-authorized users are part of SYSADM_GROUP group, this is a finding. On Windows systems, if the SYSADM_GROUP database manager configuration parameter is not specified, this is a finding. The security administrator (who holds SECADM authority within a database) can define audit policies and control the audit requirements for an individual database. The security administrator can use the following audit routines to operate upon the database audit logs: - The SYSPROC.AUDIT_ARCHIVE stored procedure archives audit logs. - The SYSPROC.AUDIT_LIST_LOGS table function allows you to locate logs of interest. - The SYSPROC.AUDIT_DELIM_EXTRACT stored procedure extracts data into delimited files for analysis. The security administrator can also grant EXECUTE privilege on these routines to another user. Run the following query to find out which users have SECADM authority in the database: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.DBAUTH WHERE SECURITYADMAUTH='Y' If GRANTEETYPE is 'U' and the authorization ID is not an authorized user, this is a finding. If the GRANTEETYPE is 'G', then all members of the external group identified by GRANTEE must be authorized users; otherwise, this is a finding. If the GRANTEETYPE is 'R', then all members of the database role identified by GRANTEE must be authorized users; otherwise, this is a finding. The members of a role can be found using this statement: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.ROLEAUTH WHERE ROLENAME= <search role name> Run the following query to find out which users have execute privilege on SYSPROC.AUDIT_ARCHIVE, SYSPROC.AUDIT_LIST_LOGS, SYSPROC.AUDIT_DELIM_EXTRACT: DB2> SELECT * FROM SYSCAT.ROUTINEAUTH WHERE SPECIFICNAME LIKE 'AUDIT%' AND SCHEMA='SYSPROC' If non-authorized users have EXECUTE privilege on any of the above three routines, this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-213687`

### Rule: DB2 must protect its audit features from unauthorized removal.

**Rule ID:** `SV-213687r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the SYSADM_GROUP parameter: $db2 get dbm cfg Only authorized OS users should be part of this group. If non-authorized users are part of the SYSADM_GROUP group, this is a finding. On Windows systems, if the SYSADM_GROUP database manager configuration parameter is not specified, this is a finding. The security administrator (who holds SECADM authority within a database) can define audit policies and control the audit requirements for an individual database. The security administrator can use the following audit routines to operate upon the database audit logs: - The SYSPROC.AUDIT_ARCHIVE stored procedure archives audit logs. - The SYSPROC.AUDIT_LIST_LOGS table function allows you to locate logs of interest. - The SYSPROC.AUDIT_DELIM_EXTRACT stored procedure extracts data into delimited files for analysis. The security administrator can also grant EXECUTE privilege on these routines to another user. Run the following query to find out which users have SECADM authority in database: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.DBAUTH WHERE SECURITYADMAUTH='Y' If GRANTEETYPE is 'U' and the authorization ID is not an authorized user, this is a finding. If the GRANTEETYPE is 'G', then all members of the external group identified by GRANTEE must be authorized users, otherwise, this is a finding. If the GRANTEETYPE is 'R', then all members of the database role identified by GRANTEE must be authorized users, otherwise, this is a finding. The members of a role can be found using this statement: DB2> SELECT CHAR(GRANTOR,35) AS GRANTOR, CHAR(GRANTEE,35) AS GRANTEE, GRANTEETYPE FROM SYSCAT.ROLEAUTH WHERE ROLENAME= <search role name> Run the following query to find out which users have execute privilege on SYSPROC.AUDIT_ARCHIVE, SYSPROC.AUDIT_LIST_LOGS, SYSPROC.AUDIT_DELIM_EXTRACT: DB2> SELECT * FROM SYSCAT.ROUTINEAUTH WHERE SPECIFICNAME LIKE 'AUDIT%' AND SCHEMA='SYSPROC' If non-authorized users have EXECUTE privilege on any of above three routines, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213688`

### Rule: DB2 must limit  privileges to change software modules, to include stored procedures, functions and triggers, and links to software external to DB2.

**Rule ID:** `SV-213688r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following query to find who has privileges to alter, drop, and create objects in the schemas: DB2> SELECT * FROM SYSCAT.SCHEMAAUTH If non-authorized users have privileges to create, alter, or drop objects, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213689`

### Rule: The OS must limit privileges to change the DB2 software resident within software libraries (including privileged programs).

**Rule ID:** `SV-213689r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the db2level command to find the installation directory of DB2 server software: $db2level If any user other than the sysadmin and root users has write permission on these directories and subsequent subdirectories under this directory, this is a finding. On Linux and UNIX operating systems, the instance directory is located in the $INSTHOME/sqllib directory, where $INSTHOME is the home directory of the instance owner. On Windows operating systems, the instance directory is located under the /sqllib directory where the DB2 database product was installed. If any user other than the instance owner and the root user has write permission to instance home directory and subsequent subdirectories under it, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-213690`

### Rule: The DB2 software installation account must be restricted to authorized users.

**Rule ID:** `SV-213690r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling, granting access to, and tracking use of the DBMS software installation account. If access or use of this account is not restricted to the minimum number of personnel required or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-213691`

### Rule: Database software, including DBMS configuration files, must be stored in dedicated directories, separate from the host OS and other applications.

**Rule ID:** `SV-213691r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The base installation directory of the database server software and the instance home directory location is configurable at the time of installation. Run the db2ls command to find the installation directory of DB2 server software. The environment variable INSTHOME points to instance home directory. If there are non-DB2-related files in the instance home directory and the subsequent subdirectories under it, this is a finding. If there are non-DB2-related files in the DB2 install directory and the subsequent subdirectories under it, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-213692`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to DB2, etc.) must be owned by database/DBMS principals authorized for ownership.

**Rule ID:** `SV-213692r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Get the list of authorized owners from ISSO or DBA. Use the following catalog views/queries to find the ownership of the various database objects: Select libname,owner from syscat.libraries Select modulename,owner from syscat.modules Select tabname,owner from syscat.nicknames Select pkgname,owner from syscat.packages Select routinename,owner from syscat.routines Select seqname,owner from syscat.sequences Select constname,owner from syscat.tabconst Select tabname,owner from syscat.tables Select tbspace,owner from syscat.tablespaces Select trigname,owner from syscat.triggers If any owner is not in the ISSO/DBA provided list, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-213693`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to DB2, etc.) must be restricted to authorized users.

**Rule ID:** `SV-213693r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Get the list of qualified and authorized owners from ISSO or DBA. The following view list information about privileges held by the users, the identities of users granting privileges, and the object ownership: DB2> SELECT * FROM SYSIBMADM.PRIVILEGES If any of the privileges is held by non-qualified and non-authorized individuals, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-213694`

### Rule: Default demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-213694r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality, not required for every mission, that cannot be disabled. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the list db directory to see if the SAMPLE database exists. $db2 list db directory If the SAMPLE database exists, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-213695`

### Rule: Unused database components, DBMS software, and database objects must be removed.

**Rule ID:** `SV-213695r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On UNIX/LINUX, run the db2ls command to find all install paths of DB2 on the system: $db2ls Run the db2ls command to find installed features of database on install paths: $db2ls -q -b <db2 install path> If there are installed features which are not required by the mission objectives and are non-essential, this is a finding. On Windows, go to Registry Editor in Windows. Then select Computer >> HKEY_LOCAL_MACHINE >> SOFTWARE >> IBM >> DB2 >> COMPONENTS If there are installed features which are not required by the mission objectives and are non-essential, this is a finding. Example: db2ls -q -b /opt/ibm/db2/V10.5 Install Path : /opt/ibm/db2/V10.5 Feature Response File ID Level Fix Pack Feature Description ---------------------------------------------------------------------------------------------------- BASE_CLIENT 10.5.0.7 7 Base client support JAVA_SUPPORT 10.5.0.7 7 Java support SQL_PROCEDURES 10.5.0.7 7 SQL procedures BASE_DB2_ENGINE 10.5.0.7 7 Base server support CONNECT_SUPPORT 10.5.0.7 7 Connect support DB2_DATA_SOURCE_SUPPORT 10.5.0.7 7 DB2 data source support SPATIAL_EXTENDER_SERVER_SUPPORT 10.5.0.7 7 Spatial Extender server support JDK 10.5.0.7 7 IBM Software Development Kit (SDK) for Java(TM) LDAP_EXPLOITATION 10.5.0.7 7 DB2 LDAP support INSTANCE_SETUP_SUPPORT 10.5.0.7 7 DB2 Instance Setup wizard ACS 10.5.0.7 7 Integrated Flash Copy Support SPATIAL_EXTENDER_CLIENT_SUPPORT 10.5.0.7 7 Spatial Extender client COMMUNICATION_SUPPORT_TCPIP 10.5.0.7 7 Communication support - TCP/IP APPLICATION_DEVELOPMENT_TOOLS 10.5.0.7 7 Base application development tools DB2_UPDATE_SERVICE 10.5.0.7 7 DB2 Update Service REPL_CLIENT 10.5.0.7 7 Replication tools TEXT_SEARCH 10.5.0.7 7 DB2 Text Search INFORMIX_DATA_SOURCE_SUPPORT 10.5.0.7 7 Informix data source support ORACLE_DATA_SOURCE_SUPPORT 10.5.0.7 7 Oracle data source support FIRST_STEPS 10.5.0.7 7 First Steps GUARDIUM_INST_MNGR_CLIENT 10.5.0.7 7 Guardium Installation Manager Client

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-213696`

### Rule: Unused database components which are integrated in DB2 and cannot be uninstalled must be disabled.

**Rule ID:** `SV-213696r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/group permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system security plan. Determine what DB2 features are recognized as requiring specific access controls. Determine which roles are authorized to use and which may not use the designated features. Review the permissions granted in the database. If any role is permitted to use any feature not designated as authorized, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-213697`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-213697r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following SQL Query to find external routines: DB2> SELECT ROUTINENAME FROM SYSCAT.ROUTINES WHERE ORIGIN='E' Use the following command to find out which user has privileges to run the external routines found with last query. DB2> SELECT GRANTEE FROM SYSCAT.ROUTINEAUTH If non-essential routines exist outside the database, this is a finding. If non-authorized users have privileges on external routines, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-213698`

### Rule: DB2 must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-213698r917662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Find out the communication protocol used by running the following command: $db2set DB2COMM If DB2 is not set to SSL, this is a finding. Run the following command to find the service names/port numbers used by the database manager: $db2 get dbm cfg Find the port numbers used by the TCP/IP and SSL services used by database manager (SVCNAME, SSL_SVCENAME) or match the service name in services file to find port numbers. Default Location for services file Windows Service File: %SystemRoot%\system32\drivers\etc\services UNIX Services File: /etc/services If ports used by the database manager are nonapproved or deemed unsafe, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-213699`

### Rule: If passwords are used for authentication, DB2 must transmit only encrypted representations of passwords.

**Rule ID:** `SV-213699r917664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the authentication parameter: $db2 get dbm cfg If the AUTHENTICATION parameter is not set to SERVER_ENCRYPT, this is a finding. Run the following command to find the value of the registry variable DB2AUTH: $db2set -all If the value of DB2AUTH is not set to JCC_ENFORCE_SECMEC, or DB2AUTH is not set (i.e. a row is not returned for DB2AUTH from the above command), this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213700`

### Rule: Applications using the database must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-213700r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. Database applications may allow for entry of the account name and password as a visible parameter of the application execution command. This practice must be prohibited and disabled to prevent shoulder surfing. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether any applications that access the database allow for entry of the account name and password, or PIN. If any do, determine whether these applications obfuscate authentication data; if they do not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-213701`

### Rule: When using command-line tools such as db2, users must use a Connect method that does not expose the password.

**Rule ID:** `SV-213701r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords and PINs, during the authentication process, the feedback from the information system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password or PIN, is an example of obscuring feedback of authentication information. "db2" and other command-line tools are part of any DB2 for LUW installation. These tools can accept a plain-text password, but do offer alternative techniques. Since the typical user of these tools is a database administrator, the consequences of password compromise are particularly serious. Therefore, the use of plain-text passwords must be prohibited, as a matter of practice and procedure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For the "db2" command, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations; and that AO approval has been obtained; if not, this is a finding. Request evidence that all users of the tool are trained in the importance of not using the plain-text password option and in how to keep the password hidden; and that they adhere to this practice. If not, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-213702`

### Rule: DB2 must use NIST FIPS 140-2 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-213702r917666_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The security functions validated as part of FIPS 140-2 for cryptographic modules are described in FIPS 140-2 Annex A. The cryptographic functionality in IBM DB2 for LUW includes features that are fully FIPS 140-2 validated, and others that are not. To be sure of using only FIPS 140-2 validated modules, specify SSL (TLS) for communication and IBM Database Native Encryption for data at rest. The decision whether to employ cryptography is the responsibility of the information owner/steward, who exercises discretion within the framework of applicable rules, policies, and law.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If it has been determined that encryption is not required, this is not a finding. Review the cryptographic configuration. If SSL/TLS is not specified for encryption of communications, this is a finding. See below for more detailed instructions. If IBM Database Native Encryption is not specified for encryption of data at rest, this is a finding. See below for more detailed instructions. To Verify SSL is in use: Check the DB2 registry variable DB2COMM to include SSL. $db2set -all If DB2COMM does not include SSL, this is a finding. Find the value of SSL_VERSIONS by running: $db2 get dbm cfg If SSL_VERSIONS is not set to TLSV12, this is a finding. Find the value of SSL_CIPHERSPECS by running: $db2 get dbm cfg If SSL_CIPHERSPECS is not set to a symmetric algorithm key length that is greater than or equal to 112, this is a finding. Find the value of SSL_SVC_LABEL by running: $db2 get dbm cfg If the parameter SSL_SVC_LABEL is not set to a certificate with RSA key length that is greater than or equal to 2048, this is a finding. If the certificate does not have a digital signature with minimum SHA2, this is a finding. The above settings ensure that all connections over SSL in any CLP or Java application strictly adhere to NIST SP 800-131A. To Verify DB2 native encryption is being used, run the following SQL Query: DB2> SELECT SUBSTR(object_name,1,8) AS NAME, SUBSTR(object_type,1,8) TYPE, SUBSTR(algorithm,1,8) ALGORITHM FROM TABLE(sysproc.admin_get_encryption_info()) If value of Algorithm is NULL for the database, this is a finding. If the database is not encrypted with native encryption or any third-party tool, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-213703`

### Rule: DB2 must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-213703r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the privileged groups and get the value of SYSADM_GROUP, SYSCTRL_GROUP, SYSMAINT_GROUP, SYSMON_GROUP: $db2 get dbm cfg If general users are part of any of above groups, this is a finding. On Windows systems, if the SYSADM_GROUP database manager configuration parameter is not specified, this is a finding. Note: On UNIX to find the members of a group from the following two files or system admin utilities provided by LINUX/UNIX vendors. /etc/passwd /etc/group e.g. if value of SYSADM_GROUP is DB2IADM1 From operating system files find out who is member of DB2IADM1 ON WINDOWS You can use lusrmgr.msc or any other OS utility to manage user group memberships.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-213704`

### Rule: DB2 must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-213704r879639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One class of man-in-the-middle, or session hijacking, attack involves the adversary guessing at valid session identifiers based on patterns in identifiers already known. The preferred technique for thwarting guesses at Session IDs is the generation of unique session identifiers using a FIPS 140-2 approved random number generator. However, it is recognized that available DBMS products do not all implement the preferred technique yet may have other protections against session hijacking. Therefore, other techniques are acceptable, provided they are demonstrated to be effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure DB2 is using the SSL communication protocol: Run the following command to find the value of the network service: $db2 get dbm cfg TCP/IP Service name (SVCENAME) SSL service name (SSL_SVCENAME) If the port numbers are not specified, look for the port numbers in services file and find the port numbers defined for the TCP/IP service name and SSL service name (SVCENAME, SSL_SVCENAME) above. Default Location for services file: Windows Service File: %SystemRoot%\system32\drivers\etc\services UNIX Services File: /etc/services If the network protocols and ports found in previous step are not in as per PPSM guidance, this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-213705`

### Rule: In the event of a system failure, DB2 must preserve any information necessary to determine cause of failure and any information necessary to return to operations with least disruption to mission processes.

**Rule ID:** `SV-213705r879641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving information system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes. Since it is usually not possible to test this capability in a production environment, systems should either be validated in a testing environment or prior to installation. This requirement is normally a function of the design of the IDPS component. Compliance can be verified by acceptance/validation processes or vendor attestation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system backup and recovery plan for db2 database to determine whether the database is in archive logging or circular logging, the recovery methods to be used, the backup schedule, backup media integration and the plan for testing database restoration. If any information is absent, this is a finding. Run the following command to get the details on the logging method: $db2 get db cfg If roll forward recovery is required and both logarchmeth1 and logarchmeth2 are set to value OFF then DB2 is not in archive logging, this is a finding. Run the following command to verify backup history: $db2 list history backup all for <dbname> Review the output of the above to see frequency and mode of backups, If the database is not being backed up per the organization’s system backup plan, this is a finding. Review evidence that database recovery is tested annually or more often per the backup and recovery document, and that the most recent test was successful. If not, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213706`

### Rule: DB2 must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-213706r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. To protect the confidentiality and integrity of information at rest, the database must be encrypted. DB2 native encryption can encrypt the data at rest; or third-party tools, like IBM Guardium, can provide encryption for data at rest. To find if a database is encrypted with DB2 native encryption, run the following SQL Query: DB2> SELECT SUBSTR(OBJECT_NAME,1,8) AS NAME, SUBSTR(ALGORITHM,1,8) ALGORITHM FROM TABLE(SYSPROC.ADMIN_GET_ENCRYPTION_INFO()) WHERE OBJECT_TYPE='DATABASE' If the value of Algorithm is NULL for the database, this is a finding. If the database is not encrypted with native encryption or any third-party tool, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-213707`

### Rule: DB2 must isolate security functions from non-security functions.

**Rule ID:** `SV-213707r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine application-specific security objects (lists of permissions, additional authentication information, stored procedures, application specific auditing, etc.) which are being housed inside DB2 database in addition to the built-in security objects. Review permissions, both direct and indirect, on the security objects, both built-in and application-specific. The following functions and views provided can help with this: DB2> SELECT LIBNAME, OWNER, LIBSCHEMA FROM SYSCAT.LIBRARIES DB2> SELECT MODULENAME, OWNER, MODULESCHEMA FROM SYSCAT.MODULES DB2> SELECT PKGNAME, OWNER, PKGSCHEMA FROM SYSCAT.PACKAGES DB2> SELECT ROUTINENAME, OWNER, ROUTINESCHEMA FROM SYSCAT.ROUTINES DB2> SELECT TRIGNAME, OWNER, TRIGSCHEMA FROM SYSCAT.TRIGGERS DB2> SELECT * FROM SYSIBMADM.PRIVILEGES If the database(s), schema(s) and permissions on security objects are not organized to provide effective isolation of security functions from nonsecurity functions, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-213708`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-213708r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are proper procedures in place for the transfer of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test and verify copies of production data are not left in unprotected locations. If there is no documented procedure for data movement from production to development/test, this is a finding. If data movement code that copies from production to development/test does exist and leaves any copies of production data in unprotected locations, this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-213709`

### Rule: Access to database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-213709r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure that those files are not shared inappropriately and are not open to backdoor access and manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions granted to users by the operating system/file system on the instance files, database files, database transaction log files, database audit log files, and database backup files. If any user/role who is not an authorized system administrator with a need to know or database administrator with a need to know, or a system account for running DBMS processes, is permitted to read/view any of these files, this is a finding. Note: When the instance and database directories are created by the DB2 database manager, the permissions are accurate and should not be changed. Use the Following queries/commands to find the locations of instance directory, database directory, transaction logs directory, archive logs directory, audit logs directory and backup files location. 1. Instance Directory On Linux and UNIX operating systems, the instance directory is located in the $INSTHOME/sqllib directory, where $INSTHOME is the home directory of the instance owner. For Windows run following command to show the parent directory of the instance directory: $db2set db2instprof e.g., for db2 instance "DB2" C:\>db2set db2instprof C:\ProgramData\IBM\DB2\DB2COPY1\DB2 The instance path in this case will be C:\ProgramData\IBM\DB2\DB2COPY1\DB2 2. Database Directory For LINUX/UNIX Run Command: $db2 list db directory Go to instance home directory then under this path, there is one or more db2 node directories. The naming convention is NODExxxx, where xxxx is numeric Identifying the DB2 node number. Under the node directory, there are 3 types of subdirectories a) Same as database name. b) Database directories. The naming convention is SQLxxxxx, where xxxxx is numeric. c) SQLDBDIR, the system database directory. For Windows: Under this local database directory, the next level is based on the instance name. For example db2 instance "DB2", the path will be C:\DB2 Under this path, there is one or more db2 node directories. The naming convention is NODExxxx, where xxxx is numeric Identifying the DB2 node number. Under the node directory, there are 3 types of subdirectories a) Same as database name. b) Database directories. The naming convention is SQLxxxxx, where xxxxx is numeric. c) SQLDBDIR, the system database directory. 3. Audit Log Directory Run following command: $db2audit describe Find value of Audit Data Path and Audit Archive Path 4. Transaction Log Directory and Archive Logs Directory Run the command: $db2 get db cfg Find value of following parameters and determine the directory locations. Changed path to log files (NEWLOGPATH) Path to log files Overflow log path (OVERFLOWLOGPATH) Mirror log path (MIRRORLOGPATH) Failover log archive path (FAILARCHPATH) First log archive method (LOGARCHMETH1) Second log archive method (LOGARCHMETH2) 5. Storage Files Run following SQL queries to find the value of tablespace containers and storage paths: DB2> SELECT varchar(container_name,70) as container_name, varchar(tbsp_name,20) as tbsp_name FROM TABLE(MON_GET_CONTAINER('',-2)) SELECT VARCHAR(STORAGE_GROUP_NAME, 30) AS STOGROUP, VARCHAR(DB_STORAGE_PATH, 40) AS STORAGE_PATH FROM TABLE(ADMIN_GET_STORAGE_PATHS('',-1)) 6. Backup File Location Run the following command and review the result for Location of Backups $db2 list history backup all for <database name>

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-213710`

### Rule: DB2 must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-213710r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS code (stored procedures, functions, and triggers), application code, settings, column and field definitions, and constraints to determine whether the database is protected against invalid input. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If column/field definitions do not exist in the database, this is a finding. If columns/fields do not contain constraints and validity checking where required, this is a finding. Where a column/field is noted in the system documentation as necessarily free-form, even though its name and context suggest that it should be strongly typed and constrained, the absence of these protections is not a finding. Where a column/field is clearly identified by name, caption or context as Notes, Comments, Description, Text, etc., the absence of these protections is not a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-213711`

### Rule: DB2 and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-213711r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS source code (stored procedures, functions, triggers) and application source code, to identify cases of dynamic code execution. If dynamic code execution is employed in circumstances where the objective could practically be satisfied by static execution with strongly typed parameters, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-213712`

### Rule: DB2 and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack.

**Rule ID:** `SV-213712r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: -- Allow strings as input only when necessary. -- Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. -- Limit the size of input strings to what is truly necessary. -- If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. -- If comment markers will never be valid as input, reject them. In SQL, these are -- or /* */ -- If HTML and XML tags, entities, comments, etc., will never be valid, reject them. -- If wildcards are present, reject them unless truly necessary. In SQL these are the underscore and the percentage sign, and the word ESCAPE is also a clue that wildcards are in use. -- If SQL key words, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, ESCAPE, UNION, GRANT, REVOKE, DENY, MODIFY will never be valid, reject them. Use case-insensitive comparisons when searching for these. Bear in mind that some of these words, particularly Grant (as a person's name), could also be valid input. -- If there are range limits on the values that may be entered, enforce those limits. -- Institute procedures for inspection of programs for correct use of dynamic coding, by a party other than the developer. -- Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. -- Record the inspection and testing in the system documentation. -- Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities; it may itself be the attacker. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS source code (stored procedures, functions, triggers) and application source code, to identify cases of dynamic code execution. If dynamic code execution is employed in circumstances where the objective could practically be satisfied by static execution with strongly typed parameters, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-213713`

### Rule: DB2 must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-213713r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DB2 settings and custom database code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If database errors contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-213714`

### Rule: DB2 must reveal detailed error messages only to the ISSO, ISSM, SA and DBA.

**Rule ID:** `SV-213714r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBMS provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA and DBA. Other individuals or roles may be specified according to organization-specific needs, with DBA approval. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DB2 settings and custom database code to determine if detailed error messages are ever displayed to unauthorized individuals. If detailed error messages are displayed to individuals not authorized to view them, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-213715`

### Rule: DB2 must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-213715r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following query to check the existing thresholds defined in database: DB2> SELECT thresholdname, thresholdpredicate, maxvalue, execution FROM syscat.thresholds If there are no thresholds defined in the required categories this is a finding. Review the defined thresholds, if the thresholds are not defined per the organization policies, this is a finding. Note: Select the following link for the knowledgebase on syscat.thresholds: http://www.ibm.com/support/knowledgecenter/SSEPGG_10.5.0/com.ibm.db2.luw.sql.ref.doc/doc/r0050565.html?cp=SSEPGG_10.5.0%2F2-12-8-111

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-213716`

### Rule: When supporting applications that require security labeling of data, DB2 must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-213716r879689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. Query the system catalog to find out the existing security labels: DB2> SELECT * FROM SYSCAT.SECURITYLABELS If the required labels are not created in database this is a finding. Query the following catalog views find details of existing security labels: DB2> SELECT * FROM SYSCAT.SECURITYLABELACCESS DB2> SELECT * FROM SYSCAT.SECURITYLABELCOMPONENTELEMENTS DB2> SELECT * FROM SYSCAT.SECURITYLABELCOMPONENTS If the security labels are not defined as per organization security policies, this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-213717`

### Rule: When supporting applications that require security labeling of data, DB2 must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-213717r879690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the DBMS to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of the DBMS product, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. Query the system catalog to find out the existing security labels: DB2> SELECT * FROM SYSCAT.SECURITYLABELS If the required labels are not created in database this is a finding. Query the following catalog views find details of existing security labels: DB2> SELECT * FROM SYSCAT.SECURITYLABELACCESS DB2> SELECT * FROM SYSCAT.SECURITYLABELCOMPONENTELEMENTS DB2> SELECT * FROM SYSCAT.SECURITYLABELCOMPONENTS If the security labels are not defined as per organization security policies, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-213718`

### Rule: DB2 must prevent non-privileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-213718r879717_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing non-privileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Non-privileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from non-privileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain the definition of the DB2 functionality considered privileged in the context of the system in question. Run the following command to find the privileged groups to get the value of SYSADM_GROUP, SYSCTRL_GROUP, SYSMAINT_GROUP, SYSMON_GROUP: $db2 get dbm cfg If non-privileged users are members of any of these groups, this is a finding. Run the following SQL command to find the database authorities: DB2> SELECT * FROM SYSCAT.DBAUTH If non-privileged users have any database authority, this is a finding. Query the following system catalog views to find out the authorities on all database objects: SYSCAT.COLAUTH: Lists the column privileges SYSCAT.DBAUTH: Lists the database privileges SYSCAT.INDEXAUTH: Lists the index privileges SYSCAT.MODULEAUTH: Lists the module privileges SYSCAT.PACKAGEAUTH: Lists the package privileges SYSCAT.PASSTHRUAUTH: Lists the server privilege SYSCAT.ROLEAUTH: Lists the role privileges SYSCAT.ROUTINEAUTH: Lists the routine (functions, methods, and stored procedures) privileges SYSCAT.SCHEMAAUTH: Lists the schema privileges SYSCAT.SEQUENCEAUTH: Lists the sequence privileges SYSCAT.SURROGATEAUTHIDS: Lists the authorization IDs for which another authorization ID can act as a surrogate. SYSCAT.TABAUTH: Lists the table and view privileges SYSCAT.TBSPACEAUTH: Lists the table space privileges SYSCAT.VARIABLEAUTH: Lists the variable privileges SYSCAT.WORKLOADAUTH: Lists the workload privileges SYSCAT.XSROBJECTAUTH: Lists the XSR object privileges If non-privileged users have any authority, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-213719`

### Rule: DB2 must utilize centralized management of the content captured in audit records generated by all components of DB2.

**Rule ID:** `SV-213719r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the location of the audit data and archive data directories: $db2audit describe If this filesystem location is not compatible with the centralized audit management system, this is a finding. If DB2 is not used in conjunction with a centralized audit management system, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-213720`

### Rule: DB2 must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-213720r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, the DBMS must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the DBMS and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the location of the audit data directory: $db2audit describe Note the location of audit data directory. Check the operating system log records find out if there has been any out of space event for that location. If there has been any out of space event for audit data directory, this is a finding. Take samples of peak database activity and measure the space utilized in the audit data directory location during that time. If the audit data directory is not sized to handle the workload between audit archiving intervals this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-213721`

### Rule: DB2 must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity.

**Rule ID:** `SV-213721r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to the DBMS on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following command to find the directory for the Audit Data Path: $db2audit describe If there is no monitoring of the Audit Data Path location at the Operating System level using OS utilities or system management utilities to send an alert at 75% space utilization, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-213722`

### Rule: DB2 must provide an immediate real-time alert to appropriate support staff of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-213722r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the audit policies are created with ERRORTYPE=Audit and if there is a failure in writing the audit event log for the policy, audit failure is logged in the diagnostic.log file and user action is not completed. Run the following statement to find the error type for each policy: DB2> SELECT AUDITPOLICYNAME, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If ERRORTYPE value is not set to 'A', this is a finding. Run the following command to monitor the database diagnostic log file for audit failure errors: $db2diag -g msg:="Write to audit log failed" If the diagnostic log file is not being monitored for audit failure errors, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-213723`

### Rule: DB2 must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-213723r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. The DBMS must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The user needs CREATEINAUTH privileges for the schema to create objects in an existing schema. Run the following Query to find which user has privilege to create objects in schemas: DB2> SELECT GRANTEE, SCHEMANAME, CREATEINAUTH, ALTERINAUTH FROM SYSCAT.SCHEMAAUTH If a non-authorized user has privilege, this is a finding. Run the following query to which user has privilege to create new schema and other objects: DB2> SELECT GRANTEE, CREATETABAUTH, EXTERNALROUTINEAUTH, DBADMAUTH, IMPLSCHEMAAUTH FROM SYSCAT.DBAUTH If a non-authorized user has privilege, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-213724`

### Rule: DB2 and the operating system must enforce access restrictions associated with changes to the configuration of DB2 or database(s).

**Rule ID:** `SV-213724r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The base installation directory of the database server software and instance home directory location is configurable at the time of installation. Run the db2level command to find the installation directory of DB2 server software: $db2level If any user other than the sysadmin and root users has write permission on these directories and subsequent subdirectories under this directory, this is a finding. On Linux and UNIX operating systems, the instance directory is located in the $INSTHOME/sqllib directory, where $INSTHOME is the home directory of the instance owner. On Windows operating systems, the instance directory is located under the /sqllib directory where the DB2 database product was installed. If any user other than the instance owner and the root user has write permission to instance home directory and subsequent subdirectories under it, this is a finding.

## Group: SRG-APP-000381-DB-000361

**Group ID:** `V-213725`

### Rule: DB2 must produce audit records of its enforcement of access restrictions associated with changes to the configuration of DB2 or database(s).

**Rule ID:** `SV-213725r879754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to configuration, it would be difficult to identify attempted attacks and an audit trail would not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To audit changes in configuration, the SYSADMIN category needs to be audited at both the instance level and the database level. Run the following command to ensure that the SYSADMIN category is being audited at the instance level: $db2audit describe If Log system administrator events is not set to “Both”, this is a finding. Run the following SQL statement to ensure that an audit policy exists at the database level: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE = ' ' If no rows are returned, this is a finding. For the audit policy returned in the statement above, run the following SQL statement to confirm that the SYSADMIN category is part of that policy and the ERROR TYPE='A': DB2> SELECT AUDITPOLICYNAME, SYSADMINSTATUS, CONTEXTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for SYSADMINSTATUS and CONTEXTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-213726`

### Rule: DB2 must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-213726r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of the network service: $db2 get dbm cfg TCP/IP Service name (SVCENAME) SSL service name (SSL_SVCENAME) If the port numbers are not specified, look for the port numbers in services file and find the port numbers defined for the TCP/IP service name and SSL service name (SVCENAME, SSL_SVCENAME) above. Default Location for services file: Windows Service File: %SystemRoot%\system32\drivers\etc\services UNIX Services File: /etc/services If the network protocols and ports found in previous step are not in as per PPSM guidance, this is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-213728`

### Rule: DB2 must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-213728r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. This requirement focuses on communications protection for the DBMS session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find certificate details: $gsk8capicmd_64 -cert -details -db "<mydbserver.kdb>" -pw "<PASSWORD>" -label "<myselfsigned>" The output is displayed in a form similar to the following: -- label : myselfsigned key size : 1024 version : X509 V3 serial : 96c2db8fa769a09d -- issue:CN=myhost.mycompany.com,O=myOrganization,OU=myOrganizationUnit, L=myLocation,ST=ON,C=CA -- subject:CN=myhost.mycompany.com,O=myOrganization,OU=myOrganizationUnit, L=myLocation,ST=ON,C=CA not before : Tuesday, 24 February 2009 17:11:50 PM not after : Thursday, 25 February 2010 17:11:50 PM If the certificate is not issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs), this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-213729`

### Rule: DB2 must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-213729r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether to employ cryptography is the responsibility of the information owner/steward, who exercises discretion within the framework of applicable rules, policies, and law.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from disclosure; which must include, at a minimum, PII and classified information. If the documentation indicates no information requires such protections, this is not a finding. DB2 native encryption can encrypt the data at rest; or third-party tools, like IBM Guardium, can provide encryption for data at rest. To find if a database is encrypted with DB2 native encryption, run the following SQL Query: DB2> SELECT * FROM TABLE(SYSPROC.ADMIN_GET_ENCRYPTION_INFO()) If the value of Algorithm is NULL for the database, this is a finding. If the database is not encrypted with native encryption or any third-party tool, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-213730`

### Rule: DB2 must implement and/or support cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-213730r879800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether to employ cryptography is the responsibility of the information owner/steward, who exercises discretion within the framework of applicable rules, policies, and law.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from disclosure; which must include, at a minimum, PII and classified information. If the documentation indicates no information requires such protections, this is not a finding. DB2 native encryption can encrypt the data at rest; or third-party tools, like IBM Guardium, can provide encryption for data at rest. To find if a database is encrypted with DB2 native encryption, run the following SQL Query: DB2> SELECT * FROM TABLE(SYSPROC.ADMIN_GET_ENCRYPTION_INFO()) If the value of Algorithm is NULL for the database, this is a finding. If the database is not encrypted with native encryption or any third-party tool, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-213731`

### Rule: DB2 must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-213731r917668_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, the DBMS, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DB2 database system supports the use of Transport Layer Security (TLS) to enable a client to authenticate a server and to provide private communication between the client and server by use of encryption. Run the following command to find out what versions of TLS are supported by the server: $db2 get dbm cfg If the value of the ssl_versions parameter is not set to "TLSV1" or "TLSV12", this is a finding. Check the value of the DB2COMM parameter using the following command: $db2set -all If the value of DB2COMM is not set to "SSL", this is a finding. Note: When this topic mentions SSL, the same information applies to TLS unless otherwise noted.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-213732`

### Rule: DB2 must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-213732r917670_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>: Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, the DBMS, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DB2 database system supports the use of Transport Layer Security (TLS) to enable a client to authenticate a server and to provide private communication between the client and server by use of encryption. Run the following command to find out what versions of TLS are supported by the server: $db2 get dbm cfg If the value of the ssl_versions parameter is not set to "TLSV1" or "TLSV12" this is a finding. Check the value of the DB2COMM parameter using the following command: $db2set -all If the value of DB2COMM is not set to "SSL", this is a finding. Note: When this topic mentions SSL, the same information applies to TLS unless otherwise noted.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-213733`

### Rule: When invalid inputs are received, DB2 must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-213733r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for the review of applications, which will require collaboration with the application developers. It is recognized that in many cases the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue is addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to determine how input errors are to be handled in general and if any special handling is defined for specific circumstances. Review the source code for database program objects (stored procedures, functions, triggers) and application source code to identify how the system responds to invalid input. If it does not implement the documented behavior, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-213734`

### Rule: Security-relevant software updates to DB2 must be installed within the time period directed by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-213734r879827_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g. IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain evidence that software patches are consistently applied to DB2 within the time frame defined for each patch. If such evidence cannot be obtained, or the evidence that is obtained indicates a pattern of noncompliance, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-213735`

### Rule: DB2 must generate audit records when security objects are accessed.

**Rule ID:** `SV-213735r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure the database generates audit records when security objects are accessed the following audit categories must be implemented at the database level: AUDIT CHECKING CONTEXT SECMAINT SYSADMIN VALIDATE Run the following SQL statement to determine if an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID returned from above query, run the following command to find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSADMINSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSMADMINSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-213736`

### Rule: DB2 must generate audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-213736r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure the database generates audit records when unsuccessful attempts are made to access security objects the following audit categories must be implemented at the database level: AUDIT CHECKING CONTEXT SECMAINT SYSADMIN VALIDATE Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSADMINSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for AUDITSTATUS, CHECKINGSTATUS, CONTEXTSTATUS, SECMAINTSTATUS, SYSMADMINSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000494-DB-000344

**Group ID:** `V-213737`

### Rule: DB2 must generate audit records when categorized information (e.g., classification levels/security levels) are accessed.

**Rule ID:** `SV-213737r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categories of information, such as classification or sensitivity level. If it is not, this is not applicable (NA). To verify the database generates audit records when categorized information (e.g., classification levels/security levels) is accessed the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from the above query to find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for SECMAINTSTATUS and CONTEXTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000494-DB-000345

**Group ID:** `V-213738`

### Rule: DB2 must generate audit records when unsuccessful attempts to access categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213738r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categories of information, such as classification or sensitivity level. If it is not, this is not applicable (NA). To verify the database generates audit records when categorized information (e.g., classification levels/security levels) is unsuccessfully accessed the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID returned from query above to find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values is not 'B' (Both) CONTEXTSTATUS, SECMAINTSTATUS, columns and the value in ERRORTYPE column set to 'A' (AUDIT) , this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-213739`

### Rule: DB2 must generate audit records when privileges/permissions are added.

**Rule ID:** `SV-213739r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, adding permissions is typically done via the GRANT command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the database generates audit records when privileges/permissions are added is accessed the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from query above to find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-213740`

### Rule: DB2 must generate audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-213740r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, adding permissions is typically done via the GRANT command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the database generates audit records when unsuccessful attempts are made to add privileges/permissions the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from the query above find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000495-DB-000328

**Group ID:** `V-213741`

### Rule: DB2 must generate audit records when privileges/permissions are modified.

**Rule ID:** `SV-213741r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, modifying permissions is typically done via the GRANT and REVOKE.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the database generates audit records when the database privileges/permissions are modified the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from the query above to find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000495-DB-000329

**Group ID:** `V-213742`

### Rule: DB2 must generate audit records when unsuccessful attempts to modify privileges/permissions occur.

**Rule ID:** `SV-213742r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, modifying permissions is typically done via the GRANT and REVOKE. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the database generates audit records when an unsuccessful attempt is made to modify the database privileges/permissions and that the SECMAINT, CONTEXT category auditing must be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Run the following SQL statement using the AUDITPOLICYID from the query above to find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-213743`

### Rule: DB2 must generate audit records when security objects are modified.

**Rule ID:** `SV-213743r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no locally defined security objects this is not applicable (NA). If there are locally defined security objects get a list of those objects from ISSO/DBA. If there are only tables in the list then a minimum audit set of OBJMAINT and SECMAINT categories on the locally defined security tables or database is required. If there are objects like packages and procedures in the list of locally defined security objects then a minimum audit set of OBJMAINT and SECMAINT categories on the database is required. Run the following SQL statement to ensure that an audit policy is defined in the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the OBJMAINT and SECMAINT categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, SECMAINTSTATUS, OBJMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the database audit policy has the values for the SECMAINTSTATUS and OBJMAINTSTATUS columns set to 'S' (Success) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If there are objects in addition to tables in the list of locally defined security objects and if the database policy does not exist or does not cover SECMAINTSTATUS or OBJMAINTSTATUS, this is a finding. If there are only tables in the list and if the database policy does not exist or does not cover SECMAINTSTATUS or OBJMAINTSTATUS then check if the appropriate policies are defined for all the required locally defined security tables. If all the required locally defined security tables' audit policies do not have the values for the SECMAINTSTATUS and OBJMAINTSTATUS columns set to 'S' (Success) or 'B' (Both) or if the value in the ERRORTYPE column is not set to 'A' (Audit), this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-213744`

### Rule: DB2 must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-213744r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no locally defined security objects this is not applicable (NA). If there are locally defined security objects get a list of those objects from ISSO/DBA. If there are only tables in the list then a minimum audit set of OBJMAINT and SECMAINT categories on the locally defined security tables or database is required. If there are objects like packages and procedures in the list of locally defined security objects then a minimum audit set of OBJMAINT and SECMAINT categories on the database is required. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the OBJMAINT and SECMAINT categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, SECMAINTSTATUS, OBJMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the database audit policy has the values for the SECMAINTSTATUS and OBJMAINTSTATUS columns set to 'F' (Failure) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If there are objects in additions to tables in the list of locally defined security objects and if the database policy does not exist or does not cover SECMAINTSTATUS or OBJMAINTSTATUS, this is a finding. If there are only tables in the list and if the database policy does not exist or does not cover SECMAINTSTATUS or OBJMAINTSTATUS then check if the appropriate policies are defined for all the required locally defined security tables. If any of the required locally defined security tables' audit policies do not have the values for the SECMAINTSTATUS and OBJMAINTSTATUS columns set to 'F' (Failure) or 'B' (Both) or the value in the ERRORTYPE column set to 'A' (Audit), then this is a finding.

## Group: SRG-APP-000498-DB-000346

**Group ID:** `V-213745`

### Rule: DB2 must generate audit records when categorized information (e.g., classification levels/security levels) is modified.

**Rule ID:** `SV-213745r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categories of information, such as classification or sensitivity level. If it is not, this is not applicable (NA). To meet these requirements at the SECMAINT, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000498-DB-000347

**Group ID:** `V-213746`

### Rule: DB2 must generate audit records when unsuccessful attempts to modify categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213746r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether it is required to track categories of information, such as classification or sensitivity level. If it is not, this is not applicable (NA). To meet these requirements at the SECMAINT, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-213747`

### Rule: DB2 must generate audit records when privileges/permissions are deleted.

**Rule ID:** `SV-213747r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of individuals' and groups' privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, deleting permissions is typically done via the REVOKE command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the SECMAINT, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-213748`

### Rule: DB2 must generate audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-213748r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict individuals' and groups' privileges could go undetected. In an SQL environment, deleting permissions is typically done via the REVOKE command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the SECMAINT, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-213749`

### Rule: DB2 must generate audit records when security objects are deleted.

**Rule ID:** `SV-213749r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the SECMAINT, OBJMAINT, and CONTEXT categories, auditing need to be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, OBJMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS, OBJMAINTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-213750`

### Rule: DB2 must generate audit records when unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-213750r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the SECMAINT, OBJMAINT, and CONTEXT categories, auditing need to be implemented at the database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, SECMAINTSTATUS, OBJMAINTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS, OBJMAINTSTATUS and SECMAINTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-213751`

### Rule: DB2 must generate audit records when categorized information (e.g., classification levels/security levels) is deleted.

**Rule ID:** `SV-213751r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Get a list of tables from ISSO/DBA where the categorized information is stored. If there are no tables with categorized information, this is not applicable (NA). Run the following SQL statement to ensure that an audit policy is defined upon all the required tables and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the database audit policy has the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If the database policy does not exist or does not cover CONTEXTSTATUS and EXECUTESTATUS then check if the appropriate policies are defined for all the required tables. If any required application table audit policies do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) or the value in the ERRORTYPE column set to 'A' (Audit), then this is a finding.

## Group: SRG-APP-000502-DB-000349

**Group ID:** `V-213752`

### Rule: DB2 must generate audit records when unsuccessful attempts to delete categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-213752r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Get a list of tables from ISSO/DBA where the categorized information is stored. If there are no tables with categorized information, this is not applicable (NA). Run the following SQL statement to ensure that an audit policy is defined upon all the required tables and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the database audit policy has the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'F' (Failure) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If the database policy does not exist or does not cover CONTEXTSTATUS and EXECUTESTATUS then check if the appropriate policies are defined for all the required tables. If any required application table audit policies do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'F' (Failure) or 'B' (Both) or the value in the ERRORTYPE column set to 'A' (Audit), then this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-213753`

### Rule: DB2 must generate audit records when successful logons or connections occur.

**Rule ID:** `SV-213753r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to the DBMS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the VALIDATE, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-213754`

### Rule: DB2 must generate audit records when unsuccessful logons or connection attempts occur.

**Rule ID:** `SV-213754r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to the DBMS. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To meet these requirements at the VALIDATE, CONTEXT category auditing needs to be implemented at database level. Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-213755`

### Rule: DB2 must generate audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-213755r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, audit logging may be achieved by means of DBMS auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of the audit policy: DB2> SELECT AUDITPOLICYNAME, SECMAINTSTATUS, SYSADMINSTATUS, OBJMAINTSTATUS, AUDITSTATUS, CONTEXTSTATUS, ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for SECMAINTSTATUS, OBJMAINTSTATUS, SYSADMINSTATUS, AUDITSTATUS and CONTEXTSTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-213756`

### Rule: DB2 must generate audit records when unsuccessful attempts to execute privileged activities or other system-level access occur.

**Rule ID:** `SV-213756r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, SECMAINTSTATUS, SYSADMINSTATUS, OBJMAINTSTATUS, AUDITSTATUS, CONTEXTSTATUS, ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for SECMAINTSTATUS, OBJMAINTSTATUS, SYSADMINSTATUS, AUDITSTATUS and CONTEXTSTATUS are not 'B' (Both) or 'F' (Failure), or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000505-DB-000352

**Group ID:** `V-213757`

### Rule: DB2 must generate audit records showing starting and ending time for user access to the database(s).

**Rule ID:** `SV-213757r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to know how long a user's (or other principal's) connection to the DBMS lasts. This can be achieved by recording disconnections, in addition to logons/connections, in the audit logs. Disconnection may be initiated by the user or forced by the system (as in a timeout) or result from a system or network failure. To the greatest extent possible, all disconnections must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy. DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the value for CONTEXTSTATUS is not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-213758`

### Rule: DB2 must generate audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-213758r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to the DBMS. Concurrent connections by the same user from multiple workstations may be valid use of the system; or such connections may be due to improper circumvention of the requirement to use the CAC for authentication; or they may indicate unauthorized account sharing; or they may be because an account has been compromised. (If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), then it is not mandatory to create additional log entries specifically for this.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-213759`

### Rule: DB2 must generate audit records when successful accesses to objects occur.

**Rule ID:** `SV-213759r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the all required application tables, routines and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the database audit policy has the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If the database policy does not exist or does not cover CONTEXTSTATUS or EXECUTESTATUS then check if the appropriate policies are defined for all the required application tables. If any required application table audit policies do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) or the value in the ERRORTYPE column set to 'A' (Audit), then this is a finding. Note: If the routines (stored procedures) execution need to be audited then execute policy has to be defined at database level. In DB2 EXECUTE policy can be created at the Database level or table level. EXECUTE audit policy covers the routine also if defined at database level. Currently there is no provision to define auditing of individual/specified routines.

## Group: SRG-APP-000507-DB-000357

**Group ID:** `V-213760`

### Rule: DB2 must generate audit records when unsuccessful accesses to objects occur.

**Rule ID:** `SV-213760r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the all required application tables, routines and/or the database: DB2> SELECT AUDITPOLICYNAME, OBJECTSCHEMA, OBJECTNAME, OBJECTTYPE FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN ('T',' ') If no rows are returned, this is a finding. If a row with OBJECTTYPE of ' ' (Database; value is a blank) exists in the output, it is a database level policy. If a row with OBJECTTYPE of 'T' exists in the output, it is a table level policy. For each audit policy returned in the statement above, run the following SQL statement to confirm that the CONTEXT and EXECUTE categories are part of that policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, EXECUTESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES If the database audit policy has the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) and the value in the ERRORTYPE column set to 'A' (Audit), this is not a finding. If the database policy does not exist or does not cover CONTEXTSTATUS or EXECUTESTATUS then check if the appropriate policies are defined for all the required application tables. If any required application table audit policies do not have the values for the CONTEXTSTATUS and EXECUTESTATUS columns set to 'S' (Success) or 'B' (Both) or the value in the ERRORTYPE column set to 'A' (Audit), then this is a finding. Note: If the routines (stored procedures) execution need to be audited then execute policy has to be defined at database level. . In DB2 EXECUTE policy can be created at the Database level or table level. EXECUTE audit policy covers the routine also if defined at database level. Currently there is no provision to define auditing of individual/specified routines.

## Group: SRG-APP-000508-DB-000358

**Group ID:** `V-213761`

### Rule: DB2 must generate audit records for all direct access to the database(s).

**Rule ID:** `SV-213761r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this context, direct access is any query, command, or call to the DBMS that comes from any source other than the application(s) that it supports. Examples would be the command line or a database management utility program. The intent is to capture all activity from administrative and non-standard sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following SQL statement to ensure that an audit policy is defined upon the database: DB2> SELECT AUDITPOLICYNAME, AUDITPOLICYID FROM SYSCAT.AUDITUSE WHERE OBJECTTYPE IN (' ') If no rows are returned, this is a finding. Using the AUDITPOLICYID from above query find the details of audit policy: DB2> SELECT AUDITPOLICYNAME, CONTEXTSTATUS, VALIDATESTATUS, ERRORTYPE AS ERRORTYPE FROM SYSCAT.AUDITPOLICIES WHERE AUDITPOLICYID = <audit policy ID> If the values for CONTEXTSTATUS and VALIDATESTATUS are not 'B' (Both) or ERRORTYPE is not 'A' (Audit), this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-213762`

### Rule: DB2 must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-213762r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to find the value of “Audit Data Path” and “Audit Archive Path” $db2audit describe DB2 can asynchronously extract the audit records in comma delimited format from “Audit Archive Path”. If a separate log management facility approved by the organization exists and is configured to absorb the comma delimited audit log files, this is not a finding. If a separate log management facility is not configured to absorb the extracted log data, this is a finding.

## Group: SRG-APP-000416-DB-000380

**Group ID:** `V-253507`

### Rule: DB2 must use NSA-approved cryptography to protect classified information in accordance with the data owners requirements.

**Rule ID:** `SV-253507r917672_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. NSA-approved cryptography for classified networks is hardware based. This requirement addresses the compatibility of a DBMS with the encryption devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database is in the unclassified environment, this is not applicable (NA). Verify the instance configuration parameters so that the instance is strictly compliant with NIST SP 800-131A. Check the DB2 registry variable DB2COMM is set to SSL: $db2set -all If DB2COMM is not set to SSL, this is a finding. Find the value of SSL_VERSIONS by running: $db2 get dbm cfg If SSL_VERSIONS is not set to TLSV12, this is a finding. Find the value of SSL_CIPHERSPECS by running: $db2 get dbm cfg If SSL_CIPHERSPECS is not set to a symmetric algorithm key length that is greater than or equal to 112, this is a finding. Find the value of SSL_SVC_LABEL by running: $db2 get dbm cfg If the parameter SSL_SVC_LABEL is not set to a certificate with RSA key length that is greater than or equal to 2048, this is a finding. If the certificate does not have a digital signature with minimum SHA2, this is a finding. The above settings ensure that all connections over SSL in any CLP or Java application strictly adhere to NIST SP 800-131A.

