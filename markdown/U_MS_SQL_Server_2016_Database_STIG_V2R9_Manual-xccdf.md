# STIG Benchmark: MS SQL Server 2016 Database Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-213900`

### Rule: SQL Server databases must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-213900r929096_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in noncentralized account stores, such as multiple servers. Account management functions can also include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. SQL Server must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together, contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if SQL Server is configured to allow the use of contained databases. In the Object Explorer in SQL Server Management Studio (SSMS), right-click on the server instance, select "Properties", and then select the "Advanced" page. If "Enabled Contained Databases" is "True", this is a finding. AND In a query interface such as the SSMS Transact-SQL editor, run the statement: EXEC sp_configure 'contained database authentication' If the returned value in the "config_value" and/or "run_value" column is "1", this is a finding. Determine whether SQL Server is configured to use only Windows authentication. In the Object Explorer in SQL Server Management Studio (SSMS), right-click on the server instance, select "Properties", and then select the "Security" page. If Windows Authentication Mode is not selected, this is a finding. AND In a query interface such as the SSMS Transact-SQL editor, run the statement: SELECT CASE SERVERPROPERTY('IsIntegratedSecurityOnly') WHEN 1 THEN 'Windows Authentication' WHEN 0 THEN 'Windows and SQL Server Authentication' END as [Authentication Mode] If the returned value in the "Authentication Mode" column is not "Windows Authentication", this is a finding. Mixed mode (both SQL Server authentication and Windows authentication) is in use. If the need for mixed mode has not been documented and approved, this is a finding. From the documentation, obtain the list of accounts authorized to be managed by SQL Server. Determine the accounts (SQL Logins) actually managed by SQL Server. Run the statement: SELECT name FROM sys.database_principals WHERE type_desc = 'SQL_USER' AND authentication_type_desc = 'DATABASE'; If any accounts listed by the query are not listed in the documentation, this is a finding. Documentation must be approved by the ISSO/ISSM.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-213901`

### Rule: SQL Server must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-213901r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DoD-approved PKI certificate does not necessarily imply authorization to access SQL Server. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If SQL Server does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for securables in the database, by type of user. If the database is tempdb, this is NA. Review the permissions actually in place in the database. If the actual permissions do not match the documented requirements, this is a finding. Use the supplemental file "Database permission assignments to users and roles.sql".

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213902`

### Rule: SQL Server must protect against a user falsely repudiating by ensuring only clearly unique Active Directory user accounts can connect to the database.

**Rule ID:** `SV-213902r944379_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring the DBMS's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, shared account. If the computer account of a remote computer is granted access to a SQL Server database, any service or scheduled task running as NT AUTHORITY\SYSTEM or NT AUTHORITY\NETWORK SERVICE can log into the instance and perform actions. These actions cannot be traced back to a specific user or process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following query: SELECT name FROM sys.database_principals WHERE type in ('U','G') AND name LIKE '%$' If no users are returned, this is not a finding. If users are returned, determine whether each user is a computer account. Launch PowerShell. Execute the following code: Note: <name> represents the username portion of the user. For example; if the user is "CONTOSO\user1$", the username is "user1". ([ADSISearcher]"(&(ObjectCategory=Computer)(Name=<name>))").FindAll() If no account information is returned, this is not a finding. If account information is returned, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213903`

### Rule: SQL Server must protect against a user falsely repudiating by use of system-versioned tables (Temporal Tables).

**Rule ID:** `SV-213903r879554_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring SQL Server's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to SQL Server, even where the application connects to SQL Server with a standard, shared account. Applications should use temporal tables to track the changes and history of sensitive data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the server documentation to determine if collecting and keeping historical versions of a table is required. If collecting and keeping historical versions of a table is NOT required, this is not a finding. Find all of the temporal tables in the database using the following query: SELECT SCHEMA_NAME(T.schema_id) AS schema_name, T.name AS table_name, T.temporal_type_desc, SCHEMA_NAME(H.schema_id) + '.' + H.name AS history_table FROM sys.tables T JOIN sys.tables H ON T.history_table_id = H.object_id WHERE T.temporal_type != 0 ORDER BY schema_name, table_name Using the system documentation, determine which tables are required to be temporal tables. If any tables listed in the documentation are not in the list created by running the above statement, this is a finding. Ensure a field exists documenting the login and/or user who last modified the record. If this does not exist, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-213904`

### Rule: SQL Server must protect against a user falsely repudiating by ensuring databases are not in a trust relationship.

**Rule ID:** `SV-213904r944381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. SQL Server provides the ability for high privileged accounts to impersonate users in a database using the TRUSTWORTHY feature. This will allow members of the fixed database role to impersonate any user within the database. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database being reviewed is MSDB, trustworthy is required to be enabled, and therefore this is not a finding. Execute the following query: SELECT SUSER_SNAME(d.owner_sid) AS DatabaseOwner, CASE WHEN d.is_trustworthy_on = 0 THEN 'No' WHEN d.is_trustworthy_on = 1 THEN 'Yes' END AS IsTrustworthy, CASE WHEN role.name IN ('sysadmin','securityadmin') OR permission.permission_name = 'CONTROL SERVER' THEN 'YES' ELSE 'No' END AS 'IsOwnerPrivileged' FROM sys.databases d LEFT JOIN sys.server_principals login ON d.owner_sid = login.sid LEFT JOIN sys.server_role_members rm ON login.principal_id = rm.member_principal_id LEFT JOIN sys.server_principals role ON rm.role_principal_id = role.principal_id LEFT JOIN sys.server_permissions permission ON login.principal_id = permission.grantee_principal_id WHERE d.name = DB_NAME() If trustworthy is not enabled, this is not a finding. If trustworthy is enabled and the database owner is not a privileged account, this is not a finding. If trustworthy is enabled and the database owner is a privileged account, review the system documentation to determine if the trustworthy property is required and authorized. If this is not documented, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-213905`

### Rule: SQL Server must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-213905r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of approved audit maintainers from the system documentation. Use the following query to review database roles and their membership, all of which enable the ability to create and maintain audit specifications. SELECT R.name AS role_name, RM.name AS role_member_name, RM.type_desc FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals RM ON DRM.member_principal_id = RM.principal_id WHERE R.type = 'R' AND R.name = 'db_owner' ORDER BY role_member_name If any role memberships are not documented and authorized, this is a finding. Review the database roles and individual users that have the following permissions, all of which enable the ability to create and maintain audit definitions. ALTER ANY DATABASE AUDIT CONTROL Use the following query to determine the roles and users that have the listed permissions: SELECT PERM.permission_name, DP.name AS principal_name, DP.type_desc AS principal_type, DBRM.role_member_name FROM sys.database_permissions PERM JOIN sys.database_principals DP ON PERM.grantee_principal_id = DP.principal_id LEFT OUTER JOIN ( SELECT R.principal_id AS role_principal_id, R.name AS role_name, RM.name AS role_member_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals RM ON DRM.member_principal_id = RM.principal_id WHERE R.type = 'R' ) DBRM ON DP.principal_id = DBRM.role_principal_id WHERE PERM.permission_name IN ('CONTROL','ALTER ANY DATABASE AUDIT') ORDER BY permission_name, principal_name, role_member_name If any of the roles or users returned have permissions that are not documented, or the documented audit maintainers do not have permissions, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213906`

### Rule: SQL Server must limit privileges to change software modules, to include stored procedures, functions, and triggers.

**Rule ID:** `SV-213906r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a listing of users and roles who are authorized to change stored procedures, functions, and triggers from the server documentation. In each user database, execute the following query: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id WHERE R.name IN ('db_ddladmin','db_owner') AND M.name != 'dbo' If any users or role permissions returned are not authorized to modify the specified object or type, this is a finding. If any user or role membership is not authorized, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-213907`

### Rule: SQL Server must limit privileges to change software modules, to include stored procedures, functions, and triggers, and links to software external to SQL Server.

**Rule ID:** `SV-213907r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a listing of schema ownership from the server documentation. Execute the following query to obtain a current listing of schema ownership. SELECT S.name AS schema_name, P.name AS owning_principal FROM sys.schemas S JOIN sys.database_principals P ON S.principal_id = P.principal_id ORDER BY schema_name If any schema is owned by an unauthorized database principal, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-213908`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to SQL Server, etc.) must be owned by database/DBMS principals authorized for ownership.

**Rule ID:** `SV-213908r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects in SQL Server rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify SQL Server accounts authorized to own database objects. If the SQL Server database ownership list does not exist or needs to be updated, this is a finding. The following query can be of use in making this determination: ;with objects_cte as (SELECT o.name, o.type_desc, CASE WHEN o.principal_id is null then s.principal_id ELSE o.principal_id END as principal_id FROM sys.objects o INNER JOIN sys.schemas s ON o.schema_id = s.schema_id WHERE o.is_ms_shipped = 0 ) SELECT cte.name, cte.type_desc, dp.name as ObjectOwner FROM objects_cte cte INNER JOIN sys.database_principals dp ON cte.principal_id = dp.principal_id ORDER BY dp.name, cte.name If any of the listed owners is not authorized, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-213909`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to SQL Server, etc.) must be restricted to authorized users.

**Rule ID:** `SV-213909r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If SQL Server were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a listing of users and roles who are authorized to modify database structure and logic modules from the server documentation. Execute the following query: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id WHERE R.name IN ('db_ddladmin','db_owner') AND M.name != 'dbo' If any users or role permissions returned are not authorized to modify the specified object or type, this is a finding. If any user or role membership is not authorized, this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-213910`

### Rule: In the event of a system failure, hardware loss or disk failure, SQL Server must be able to restore necessary databases with least disruption to mission processes.

**Rule ID:** `SV-213910r879641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. In the event of a system failure, SQL Server must be able to bring the database back to a consistent state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system security plan (SSP) to determine whether the database is static, the recovery model to be used, the backup schedule, and the plan for testing database restoration. If the SSP does not state that the database is static, assume that it is not static. If any of the other information is absent, this is a finding. If the database is not static, and the documented recovery model is Bulk Logged, but the justification and authorization for this are not documented, this is a finding. Run the following to determine Recovery Model: USE [master] GO SELECT name, recovery_model_desc FROM sys.databases ORDER BY name If the recovery model description does not match the documented recovery model, this is a finding. Review the jobs set up to implement the backup plan. If they are absent, this is a finding. Check the history of the backups by running the following query. It checks the last 30 days of backups by database. USE [msdb] GO SELECT database_name, CASE type WHEN 'D' THEN 'Full' WHEN 'I' THEN 'Differential' WHEN 'L' THEN 'Log' ELSE type END AS backup_type, is_copy_only, backup_start_date, backup_finish_date FROM dbo.backupset WHERE backup_start_date >= dateadd(day, - 30, getdate()) ORDER BY database_name, backup_start_date DESC If the history indicates a pattern of job failures by missing or gaps in backups, this is a finding. Review evidence that database recovery is tested annually or more often, and that the most recent test was successful. If not, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213911`

### Rule: The Database Master Key encryption password must meet DOD password complexity requirements. 

**Rule ID:** `SV-213911r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Weak passwords may be easily guessed. When passwords are used to encrypt keys used for encryption of sensitive data, then the confidentiality of all data encrypted using that key is at risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the query prompt: SELECT name FROM [master].sys.databases WHERE state = 0 Repeat for each database: From the query prompt: USE [database name] SELECT COUNT(name) FROM sys.symmetric_keys s, sys.key_encryptions k WHERE s.name = '##MS_DatabaseMasterKey##' AND s.symmetric_key_id = k.key_id AND k.crypt_type in ('ESKP', 'ESP2', 'ESP3') If the value returned is zero, this is not applicable. If the value returned is greater than zero, a Database Master Key exists and is encrypted with a password. Review procedures and evidence of password requirements used to encrypt Database Master Keys. If the passwords are not required to meet DoD password standards, currently a minimum of 15 characters with at least 1 upper-case character, 1 lower-case character, 1 special character, and 1 numeric character, and at least 8 characters changed from the previous password, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213912`

### Rule: The Database Master Key must be encrypted by the Service Master Key, where a Database Master Key is required and another encryption method has not been specified. 

**Rule ID:** `SV-213912r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When not encrypted by the Service Master Key, system administrators or application administrators may access and use the Database Master Key to view sensitive data that they are not authorized to view. Where alternate encryption means are not feasible, encryption by the Service Master Key may be necessary. To help protect sensitive data from unauthorized access by DBAs, mitigations may be in order. Mitigations may include automatic alerts or other audit events when the Database Master Key is accessed outside of the application or by a DBA account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no databases require encryption, this is not a finding. From the query prompt: SELECT name FROM [master].sys.databases WHERE is_master_key_encrypted_by_server = 1 AND owner_sid <> 1 AND state = 0; (Note that this query assumes that the [sa] account is not used as the owner of application databases, in keeping with other STIG guidance. If this is not the case, modify the query accordingly.) If no databases are returned by the query, this is not a finding. For any databases returned, verify in the System Security Plan that encryption of the Database Master Key using the Service Master Key is acceptable and approved by the Information Owner, and the encrypted data does not require additional protections to deter or detect DBA access. If not approved, this is a finding. If approved and additional protections are required, then verify the additional requirements are in place in accordance with the System Security Plan. These may include additional auditing on access of the Database Master Key with alerts or other automated monitoring. If the additional requirements are not in place, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-213913`

### Rule: The Certificate used for encryption must be backed up and stored in a secure location that is not on the SQL Server.

**Rule ID:** `SV-213913r952219_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backup and recovery of the Certificate used for encryption is critical to the complete recovery of the database. Not having this key can lead to loss of data during recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and authorizing official have determined that encryption of data at rest is not required, this is not a finding. Review procedures for and evidence of backup of the Certificate used for encryption in the System Security Plan. If the procedures or evidence does not exist, this is a finding. If the procedures do not indicate that a backup of the Certificate used for encryption is stored in a secure location that is not on the SQL Server, this is a finding. If procedures do not indicate access restrictions to the Certificate backup, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-213914`

### Rule: SQL Server must isolate security functions from non-security functions.

**Rule ID:** `SV-213914r879643_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and non-security functionality are commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine elements of security functionality (lists of permissions, additional authentication information, stored procedures, application specific auditing, etc.) that are being housed inside SQL server. For any elements found, check SQL Server to determine if these objects or code implementing security functionality are located in a separate security domain, such as a separate database, schema, or table created specifically for security functionality. If the database is a SQL Server default database (master, msdb, model, tempdb), this is NA. Run the following query to list all the user-defined databases: SELECT Name FROM sys.databases WHERE database_id > 4 ORDER BY 1; Review the database structure to determine where security related functionality is stored. If security-related database objects or code are not kept separate, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-213915`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-213915r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-213916`

### Rule: SQL Server must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-213916r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS code (stored procedures, functions, triggers), application code, settings, column and field definitions, and constraints to determine whether the database is protected against invalid input. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If column/field definitions are not reflective of the data, this is a finding. If columns/fields do not contain constraints and validity checking where required, this is a finding. Where a column/field is noted in the system documentation as necessarily free-form, even though its name and context suggest that it should be strongly typed and constrained, the absence of these protections is not a finding. Where a column/field is clearly identified by name, caption or context as Notes, Comments, Description, Text, etc., the absence of these protections is not a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-213917`

### Rule: SQL Server must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-213917r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review application behavior and custom database code (stored procedures, triggers), to determine whether error messages contain information beyond what is needed for explaining the issue to general users. If database error messages contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-213918`

### Rule: SQL Server must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-213918r879689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for SQL Server to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of SQL Server, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but neither a third-party solution nor a SQL Server Row-Level security solution is implemented that reliably maintains labels on information in storage, this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-213919`

### Rule: SQL Server must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-213919r879690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for SQL Server to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of SQL Server, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but neither a third-party solution nor a SQL Server Row-Level security solution is implemented that reliably maintains labels on information in process, this is a finding.

## Group: SRG-APP-000314-DB-000310

**Group ID:** `V-213920`

### Rule: SQL Server must associate organization-defined types of security labels having organization-defined security label values with information in transmission.

**Rule ID:** `SV-213920r879691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for SQL Server to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of SQL Server, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but neither a third-party solution nor a SQL Server Row-Level security solution is implemented that reliably maintains labels on information in transmission, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-213921`

### Rule: SQL Server must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-213921r879705_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to determine requirements for object ownership and authorization delegation. Use the following query to discover database object ownership: Schemas not owned by the schema or dbo: SELECT name AS schema_name, USER_NAME(principal_id) AS schema_owner FROM sys.schemas WHERE schema_id != principal_id AND principal_id != 1 Objects owned by an individual principal: SELECT object_id, name AS securable, USER_NAME(principal_id) AS object_owner, type_desc FROM sys.objects WHERE is_ms_shipped = 0 AND principal_id IS NOT NULL ORDER BY type_desc, securable, object_owner Use the following query to discover database users who have been delegated the right to assign additional permissions: SELECT U.type_desc, U.name AS grantee, DP.class_desc AS securable_type, CASE DP.class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_NAME(DP.major_id) WHEN 3 THEN SCHEMA_NAME(DP.major_id) ELSE CAST(DP.major_id AS nvarchar) END AS securable, permission_name, state_desc FROM sys.database_permissions DP JOIN sys.database_principals U ON DP.grantee_principal_id = U.principal_id WHERE DP.state = 'W' ORDER BY grantee, securable_type, securable If any of these rights are not documented and authorized, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-213922`

### Rule: Execution of stored procedures and functions that utilize execute as must be restricted to necessary cases only.

**Rule ID:** `SV-213922r879719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation must be utilized only where necessary and protected from misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain a listing of stored procedures and functions that utilize impersonation. Execute the following query: SELECT S.name AS schema_name, O.name AS module_name, USER_NAME( CASE M.execute_as_principal_id WHEN -2 THEN COALESCE(O.principal_id, S.principal_id) ELSE M.execute_as_principal_id END ) AS execute_as FROM sys.sql_modules M JOIN sys.objects O ON M.object_id = O.object_id JOIN sys.schemas S ON O.schema_id = S.schema_id WHERE execute_as_principal_id IS NOT NULL and o.name not in ( 'fn_sysdac_get_username', 'fn_sysutility_ucp_get_instance_is_mi', 'sp_send_dbmail', 'sp_SendMailMessage', 'sp_syscollector_create_collection_set', 'sp_syscollector_delete_collection_set', 'sp_syscollector_disable_collector', 'sp_syscollector_enable_collector', 'sp_syscollector_get_collection_set_execution_status', 'sp_syscollector_run_collection_set', 'sp_syscollector_start_collection_set', 'sp_syscollector_update_collection_set', 'sp_syscollector_upload_collection_set', 'sp_syscollector_verify_collector_state', 'sp_syspolicy_add_policy', 'sp_syspolicy_add_policy_category_subscription', 'sp_syspolicy_delete_policy', 'sp_syspolicy_delete_policy_category_subscription', 'sp_syspolicy_update_policy', 'sp_sysutility_mi_add_ucp_registration', 'sp_sysutility_mi_disable_collection', 'sp_sysutility_mi_enroll', 'sp_sysutility_mi_initialize_collection', 'sp_sysutility_mi_remove', 'sp_sysutility_mi_remove_ucp_registration', 'sp_sysutility_mi_upload', 'sp_sysutility_mi_validate_enrollment_preconditions', 'sp_sysutility_ucp_add_mi', 'sp_sysutility_ucp_add_policy', 'sp_sysutility_ucp_calculate_aggregated_dac_health', 'sp_sysutility_ucp_calculate_aggregated_mi_health', 'sp_sysutility_ucp_calculate_computer_health', 'sp_sysutility_ucp_calculate_dac_file_space_health', 'sp_sysutility_ucp_calculate_dac_health', 'sp_sysutility_ucp_calculate_filegroups_with_policy_violations', 'sp_sysutility_ucp_calculate_health', 'sp_sysutility_ucp_calculate_mi_file_space_health', 'sp_sysutility_ucp_calculate_mi_health', 'sp_sysutility_ucp_configure_policies', 'sp_sysutility_ucp_create', 'sp_sysutility_ucp_delete_policy', 'sp_sysutility_ucp_delete_policy_history', 'sp_sysutility_ucp_get_policy_violations', 'sp_sysutility_ucp_initialize', 'sp_sysutility_ucp_initialize_mdw', 'sp_sysutility_ucp_remove_mi', 'sp_sysutility_ucp_update_policy', 'sp_sysutility_ucp_update_utility_configuration', 'sp_sysutility_ucp_validate_prerequisites', 'sp_validate_user', 'syscollector_collection_set_is_running_update_trigger', 'sysmail_help_status_sp' ) ORDER BY schema_name, module_name If any procedures or functions are returned that are not documented, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-213923`

### Rule: SQL Server must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-213923r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. SQL Server must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the SQL Server instance supports only software development, experimentation, and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. Obtain a listing of users and roles who are authorized to create, alter, or replace logic modules from the server documentation. In each user database, execute the following query: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id WHERE R.name IN ('db_ddladmin','db_owner') AND M.name != 'dbo' If any users or role permissions returned are not authorized to modify the specified object or type, this is a finding. If any user or role membership is not authorized, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-213924`

### Rule: SQL Server must enforce access restrictions associated with changes to the configuration of the database(s).

**Rule ID:** `SV-213924r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the following query to obtain a listing of user databases whose owner is a member of a fixed server role: SELECT D.name AS database_name, SUSER_SNAME(D.owner_sid) AS owner_name, FRM.is_fixed_role_member FROM sys.databases D OUTER APPLY ( SELECT MAX(fixed_role_member) AS is_fixed_role_member FROM ( SELECT IS_SRVROLEMEMBER(R.name, SUSER_SNAME(D.owner_sid)) AS fixed_role_member FROM sys.server_principals R WHERE is_fixed_role = 1 ) A ) FRM WHERE D.database_id > 4 AND (FRM.is_fixed_role_member = 1 OR FRM.is_fixed_role_member IS NULL) ORDER BY database_name If no databases are returned, this is not a finding. For each database/login returned, review the Server Role memberships 1. In SQL Server Management Studio, Expand “Logins” 2. Double-click the name of the Login 3. Click the “Server Roles” tab If any server roles are selected, but not documented and authorized, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-213926`

### Rule: SQL Server must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-213926r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to SQL Server or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of SQL Server, Windows, and additional software as relevant. If full-disk encryption is required, and Windows or the storage system is not configured for this, this is a finding. If database transparent data encryption (TDE) is called for, check whether it is enabled: SELECT DB_NAME(database_id) AS [Database Name], CASE encryption_state WHEN 0 THEN 'No database encryption key present, no encryption' WHEN 1 THEN 'Unencrypted' WHEN 2 THEN 'Encryption in progress' WHEN 3 THEN 'Encrypted' WHEN 4 THEN 'Key change in progress' WHEN 5 THEN 'Decryption in progress' WHEN 6 THEN 'Protection change in progress' END AS [Encryption State] FROM sys.dm_database_encryption_keys For each user database for which encryption is called for and it is marked Unencrypted, this is a finding. If table/column encryption and/or a separation between those who own the data (and can view it) and those who manage the data (but should have no access) is required for PII or similar types of data, use Always Encrypted. The details for configuring Always Encrypted are located here: https://msdn.microsoft.com/en-us/library/mt163865.aspx. Review the definitions and contents of the relevant tables/columns for the Always Encryption settings, if any of the information defined as requiring cryptographic protection is not encrypted this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-213927`

### Rule: SQL Server must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-213927r879800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SQL Server’s handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to SQL Server or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from disclosure, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. If full-disk encryption is required, and Windows or the storage system is not configured for this, this is a finding. If database transparent data encryption (TDE) is called for, check whether it is enabled: SELECT DB_NAME(database_id) AS [Database Name], CASE encryption_state WHEN 0 THEN 'No database encryption key present, no encryption' WHEN 1 THEN 'Unencrypted' WHEN 2 THEN 'Encryption in progress' WHEN 3 THEN 'Encrypted' WHEN 4 THEN 'Key change in progress' WHEN 5 THEN 'Decryption in progress' WHEN 6 THEN 'Protection change in progress' END AS [Encryption State] FROM sys.dm_database_encryption_keys For each user database for which encryption is called for and it is marked Unencrypted, this is a finding. If table/column encryption and/or a separation between those who own the data (and can view it) and those who manage the data (but should have no access) is required for PII or similar types of data, use Always Encrypted.  The details for configuring Always Encrypted are located here: https://msdn.microsoft.com/en-us/library/mt163865.aspx. Review the definitions and contents of the relevant tables/columns for the Always Encryption settings, if any of the information defined as requiring cryptographic protection is not encrypted this is a finding.

## Group: SRG-APP-000416-DB-000380

**Group ID:** `V-251040`

### Rule: SQL Server must use NSA-approved cryptography to protect classified information in accordance with the data owners requirements.

**Rule ID:** `SV-251040r879944_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. NSA-approved cryptography for classified networks is hardware based. This requirement addresses the compatibility of a DBMS with the encryption devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Detailed information on the NIST Cryptographic Module Validation Program (CMVP) is available at the following website: http://csrc.nist.gov/groups/STM/cmvp/index.html. Review system documentation to determine whether cryptography for classified or sensitive information is required by the information owner. If the system documentation does not specify the type of information hosted on SQL Server as classified, sensitive, and/or unclassified, this is a finding. If neither classified nor sensitive information exists within SQL Server databases or configuration, this is not a finding. Verify that Windows is configured to require the use of FIPS-compliant algorithms. Click "Start", enter "Local Security Policy", and then press "Enter". Expand "Local Policies", select "Security Options", and then locate "System Cryptography: Use FIPS compliant algorithms for encryption, hashing, and signing". If the Security Setting for this option is "Disabled", this is a finding. Note: The list of acceptable algorithms is "AES 256" and "Triple DES". If cryptography is being used by SQL Server, verify that the cryptography is NIST FIPS 140-2 or 140-3 certified by running the following SQL query: SELECT DISTINCT name, algorithm_desc FROM sys.symmetric_keys WHERE key_algorithm NOT IN ('D3','A3') ORDER BY name If any items listed show an uncertified NIST FIPS 140-2 algorithm type, this is a finding.

