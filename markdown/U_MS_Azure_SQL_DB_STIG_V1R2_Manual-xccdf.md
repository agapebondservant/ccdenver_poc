# STIG Benchmark: Microsoft Azure SQL Database Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-255301`

### Rule: Azure SQL Databases must integrate with Azure Active Directory for providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-255301r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in noncentralized account stores, such as multiple servers. Account management functions can also include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example, using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. SQL DB must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may comprise differing technologies, that when placed together, contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Azure SQL Database is configured to use Azure Active Directory authentication only. Only Azure Active Directory will be used to authenticate to the server. SQL authentication will be disabled, including SQL Server administrators and users. In a PowerShell or Cloud Shell interface, run the statement: az sql server ad-only-auth get --resource-group myresource --name myserver OR Get-AzSqlServerActiveDirectoryOnlyAuthentication -ServerName myserver -ResourceGroupName myresource If the returned value in the "AzureADOnlyAuthentication" column is "True", this is not a finding. If Mixed mode (both SQL Server authentication and Windows authentication) is in use and the need for mixed mode has not been documented and approved, this is a finding. From the documentation, obtain the list of accounts authorized to be managed by Azure SQL Database. Determine the accounts (SQL Logins) actually managed by Azure SQL Database. Run the statement: SELECT name FROM sys.database_principals WHERE type_desc = 'SQL_USER' AND authentication_type_desc = 'INSTANCE'; If any accounts listed by the query are not listed in the documentation, this is a finding. Risk must be accepted by the ISSO/ISSM. More information regarding this process is available at: https://docs.microsoft.com/en-us/azure/azure-sql/database/authentication-azure-ad-only-authentication

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-255302`

### Rule: Azure SQL Database must enforce approved authorizations for logical access to database information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-255302r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in noncentralized account stores, such as multiple servers. Account management functions can also include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example, using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. Azure SQL Database must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for securables in the database, by type of user. Review the permissions actually in place in the database. Execute the following query to find permissions assigned: SELECT DISTINCT [Finding] = 'Database ' + QUOTENAME(DB_NAME()) + ' ' + CASE WHEN dbp.type = 'r' THEN 'Role ' ELSE 'User ' END + QUOTENAME(dbp.name) + CASE WHEN dbp.type = 'r' THEN ' owning schema ' ELSE ' in db role ' END + QUOTENAME(ISNULL(dbp2.name,'-')) + ' has db permission ' + QUOTENAME(ISNULL(dbper.permission_name,'-')) -- + ' on object ' + QUOTENAME(ISNULL(OBJECT_NAME(dbper.major_id),'-')) + ' on object ' + QUOTENAME(ISNULL(CASE WHEN dbper.major_id = 0 THEN 'Database' ELSE OBJECT_NAME(dbper.major_id) END,'-')) + '.' COLLATE SQL_Latin1_General_CP1_CI_AS FROM sys.database_principals dbp LEFT JOIN sys.database_role_members dbrm ON dbp.principal_Id = dbrm.member_principal_Id LEFT JOIN sys.database_principals dbp2 ON dbrm.role_principal_id = dbp2.principal_id LEFT JOIN sys.database_permissions dbper ON dbper.grantee_principal_id = dbp.principal_id WHERE dbp.type IN ('u','s','g','r') /*Windows/Sql/Groups */ AND NOT (dbp.name = 'public' AND dbper.permission_name IN ('select','execute') AND DB_NAME() = 'master') /*ignore public permissions in master*/ AND NOT (dbp.name = 'public' AND dbper.permission_name IN ('select','execute') AND OBJECT_SCHEMA_NAME(major_id, DB_ID()) = 'sys') AND ( /*Filter out duplicate permissions in each database except for the base master database*/ dbp2.name IS NOT NULL /* This seems to filter out permissions granted to a role.*/ AND dbper.permission_name IS NOT NULL AND dbper.major_id IS NOT NULL OR DB_NAME() = 'master') If the actual permissions do not match the documented requirements, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-255303`

### Rule: Azure SQL Database must enforce approved authorizations for logical access to server information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-255303r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DOD-approved PKI certificate does not necessarily imply authorization to access Azure SQL Database. To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If Azure SQL Database does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for DBMS server securables, by type of login. Review the permissions actually in place on the server. Execute the following query to find permissions in place on the server: SELECT DISTINCT QUOTENAME(sp.name) + ' in server role ' + QUOTENAME(ISNULL(sp2.name,'Public')) + ' has ' + QUOTENAME(ISNULL(class_desc,'server'))+ ':' + QUOTENAME(ISNULL(object_name(major_id),'~')) + ' permission ' + QUOTENAME(ISNULL(srvper.permission_name,'-')) + '.' COLLATE SQL_Latin1_General_CP1_CI_AS Finding , object_name(major_id) ObjectName FROM sys.database_principals sp LEFT JOIN sys.database_role_members srm ON sp.principal_id = srm.member_principal_id LEFT JOIN sys.database_principals sp2 ON srm.role_principal_id = sp2.principal_id LEFT JOIN sys.database_permissions srvper ON srvper.grantee_principal_id = sp.principal_id WHERE sp.type IN ('u','s','g') --Windows/Sql/Groups AND sp.principal_id <> 1 If the actual permissions do not match the documented requirements, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-255304`

### Rule: Azure SQL Database must protect against a user falsely repudiating by ensuring only clearly unique Active Directory user accounts can connect to the database.

**Rule ID:** `SV-255304r917650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonrepudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Nonrepudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring Azure SQL Database's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to Azure SQL Database, even where the application connects to Azure SQL Database with a standard, shared account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of authorized Azure SQL Database accounts in the system documentation. Determine if any accounts are shared. A shared account is defined as a username and password that are used by multiple individuals to log in to Azure SQL Database. Azure Active Directory accounts are not shared accounts as the group itself does not have a password. If accounts are determined to be shared, determine if individuals are first individually authenticated. If individuals are not individually authenticated before using the shared account (e.g., by the operating system or possibly by an application making calls to the database), this is a finding. The key is individual accountability. If this can be traced, this is not a finding. If accounts are determined to be shared, determine if they are directly accessible to end users. If so, this is a finding. Review contents of audit logs and data tables to confirm that the identity of the individual user performing the action is captured. If shared identifiers are found and not accompanied by individual identifiers, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-255305`

### Rule: Azure SQL Database must protect against a user falsely repudiating by use of system-versioned tables (Temporal Tables).

**Rule ID:** `SV-255305r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonrepudiation of actions taken is required in order to maintain data integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Nonrepudiation protects against later claims by a user of not having created, modified, or deleted a particular data item or collection of data in the database. In designing a database, the organization must define the types of data and the user actions that must be protected from repudiation. The implementation must then include building audit features into the application data tables and configuring the DBMS's audit tools to capture the necessary audit trail. Design and implementation also must ensure that applications pass individual user identification to the DBMS, even where the application connects to the DBMS with a standard, shared account. If the computer account of a remote computer is granted access to SQL Server, any service or scheduled task running as NT AUTHORITY\SYSTEM or NT AUTHORITY\NETWORK SERVICE can log into the instance and perform actions. These actions cannot be traced back to a specific user or process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the server documentation to determine if collecting and keeping historical versions of a table is required. If collecting and keeping historical versions of a table is NOT required, this is not a finding. Find all of the temporal tables in the database using the following query: SELECT SCHEMA_NAME(T.schema_id) AS schema_name, T.name AS table_name, T.temporal_type_desc, SCHEMA_NAME(H.schema_id) + '.' + H.name AS history_table FROM sys.tables T JOIN sys.tables H ON T.history_table_id = H.object_id WHERE T.temporal_type != 0 ORDER BY schema_name, table_name Using the system documentation, determine which tables are required to be temporal tables. If any tables listed in the documentation are not in the list created by running the above statement, this is a finding. Ensure a field exists documenting the login and/or user who last modified the record. If this does not exist, this is a finding. Review the system documentation to determine the history retention period. Navigate to the table in Object Explorer. Right-click on the table, and then select Script Table As >> CREATE To >> New Query Editor Window. Locate the line that contains "SYSTEM_VERSIONING". Locate the text that states "HISTORY_RETENTION_PERIOD". If this text is missing, or is set to a value less than the documented history retention period, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-255306`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to Azure SQL Database, etc.) must be owned by database/Azure SQL Database principals authorized for ownership.

**Rule ID:** `SV-255306r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify Azure SQL Database accounts authorized to own database objects. If the Azure SQL Database ownership list does not exist or needs to be updated, this is a finding. The following query can be of use in making this determination: ;with objects_cte as (SELECT o.name, o.type_desc, CASE WHEN o.principal_id is null then s.principal_id ELSE o.principal_id END as principal_id FROM sys.objects o INNER JOIN sys.schemas s ON o.schema_id = s.schema_id WHERE o.is_ms_shipped = 0 ) SELECT cte.name, cte.type_desc, dp.name as ObjectOwner FROM objects_cte cte INNER JOIN sys.database_principals dp ON cte.principal_id = dp.principal_id ORDER BY dp.name, cte.name If any of the listed owners is not authorized, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-255307`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to Azure SQL Database, etc.) must be restricted to authorized users.

**Rule ID:** `SV-255307r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the Azure SQL Database were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals will be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a listing of users and roles who are authorized to modify database structure and logic modules from the server documentation. Execute the following query to obtain a list of database principals: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) Execute the following query to obtain a list of role memberships: SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id WHERE R.name IN ('db_ddladmin','db_owner') AND M.name != 'dbo' If unauthorized access to the principal(s)/role(s) has been granted, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-255308`

### Rule: The Azure SQL Database must isolate security functions from nonsecurity functions.

**Rule ID:** `SV-255308r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database Management Systems typically separate security functionality from nonsecurity functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and nonsecurity functionality are commingled, users who have access to nonsecurity functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine elements of security functionality (lists of permissions, additional authentication information, stored procedures, application specific auditing, etc.) being housed inside Azure SQL Database. For any elements found, check Azure SQL Database to determine if these objects or code implementing security functionality are located in a separate security domain, such as a separate database, schema, or table created specifically for security functionality. Review the database structure to determine where security related functionality is stored. If security-related database objects or code are not kept separate, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-255309`

### Rule: Azure SQL Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-255309r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-255310`

### Rule: Azure SQL Database must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-255310r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database code (stored procedures, functions, triggers), application code, settings, column and field definitions, and constraints to determine whether the database is protected against invalid input. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If column/field definitions are not reflective of the data, this is a finding. If columns/fields do not contain constraints and validity checking where required, this is a finding. Where a column/field is noted in the system documentation as necessarily free-form, even though its name and context suggest that it should be strongly typed and constrained, the absence of these protections is not a finding. Where a column/field is clearly identified by name, caption or context as Notes, Comments, Description, Text, etc., the absence of these protections is not a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-255311`

### Rule: The Azure SQL Database and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-255311r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain a listing of stored procedures and functions that utilize dynamic code execution. Execute the following query: DECLARE @tblDynamicQuery TABLE (ID INT identity(1,1), ProcToExecuteDynSQL VARCHAR(500)) INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('EXEC[ (]@') INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('EXECUTE[ (]@') INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('SP_EXECUTESQL[ (]@') SELECT QUOTENAME(DB_Name()) DB_Name, QUOTENAME(SCHEMA_NAME([schema_id])) + '.' + QUOTENAME(name) Name, QUOTENAME(type_desc) ObjectType FROM sys.objects o WHERE o.is_ms_shipped = 0 and o.object_id IN ( SELECT m.object_id FROM sys.sql_modules m JOIN @tblDynamicQuery dsql ON REPLACE(REPLACE(REPLACE(m.definition,CHAR(32),'()'),')(',''),'()',CHAR(32)) like '%' + dsql.ProcToExecuteDynSQL + '%') If any procedures or functions are returned that are not documented, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-255312`

### Rule: The Azure SQL Database and associated applications, when making use of dynamic code execution, must scan input data for invalid values that may indicate a code injection attack.

**Rule ID:** `SV-255312r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: -- Allow strings as input only when necessary. -- Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. -- Limit the size of input strings to what is truly necessary. -- If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. -- If comment markers will never be valid as input, reject them. In SQL, these are -- or /* */ -- If HTML and XML tags, entities, comments, etc., will never be valid, reject them. -- If wildcards are present, reject them unless truly necessary. In SQL these are the underscore and the percentage sign, and the word ESCAPE is also a clue that wildcards are in use. -- If SQL key words, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, ESCAPE, UNION, GRANT, REVOKE, DENY, MODIFY will never be valid, reject them. Use case-insensitive comparisons when searching for these. Bear in mind that some of these words, particularly Grant (as a person's name), could also be valid input. -- If there are range limits on the values that may be entered, enforce those limits. -- Institute procedures for inspection of programs for correct use of dynamic coding, by a party other than the developer. -- Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. -- Record the inspection and testing in the system documentation. -- Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities; it may itself be the attacker. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain a listing of stored procedures and functions that utilize dynamic code execution. Execute the following query: DECLARE @tblDynamicQuery TABLE (ID INT identity(1,1), ProcToExecuteDynSQL VARCHAR(500)) INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('EXEC[ (]@') INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('EXECUTE[ (]@') INSERT INTO @tblDynamicQuery(ProcToExecuteDynSQL) values('SP_EXECUTESQL[ (]@') SELECT QUOTENAME(DB_Name()) DB_Name, QUOTENAME(SCHEMA_NAME([schema_id])) + '.' + QUOTENAME(name) Name, QUOTENAME(type_desc) ObjectType FROM sys.objects o WHERE o.is_ms_shipped = 0 and o.object_id IN ( SELECT m.object_id FROM sys.sql_modules m JOIN @tblDynamicQuery dsql ON REPLACE(REPLACE(REPLACE(m.definition,CHAR(32),'()'),')(',''),'()',CHAR(32)) like '%' + dsql.ProcToExecuteDynSQL + '%') If any procedures or functions are returned that are not documented, this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-255313`

### Rule: Azure SQL Database must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-255313r879689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for Azure SQL Database to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained. If the security labels are lost, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of Azure SQL Database, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but a third-party solution, SQL Information Protection, or an Azure SQL Database Row-Level security solution is implemented that reliably maintains labels on information in storage, this is a finding.

## Group: SRG-APP-000313-DB-000309

**Group ID:** `V-255314`

### Rule: Azure SQL Database must associate organization-defined types of security labels having organization-defined security label values with information in process.

**Rule ID:** `SV-255314r879690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for Azure SQL Database to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained. If the security labels are lost, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of Azure SQL Database, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but a third-party solution, SQL Information Protection, or an Azure SQL Database Row-Level security solution is implemented that reliably maintains labels on information in process, this is a finding.

## Group: SRG-APP-000314-DB-000310

**Group ID:** `V-255315`

### Rule: Azure SQL Database must associate organization-defined types of security labels having organization-defined security label values with information in transmission.

**Rule ID:** `SV-255315r879691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for Azure SQL Database to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies; reflect special dissemination, handling, or distribution instructions; or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained. If the security labels are lost, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of Azure SQL Database, a third-party product, or custom application code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but a third-party solution, SQL Information Protection, or an Azure SQL Database Row-Level security solution is implemented that reliably maintains labels on information in transmission, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-255316`

### Rule: Azure SQL Database must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-255316r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read, write, execute). Ownership is usually acquired implicitly when creating the object or by explicit ownership assignment. DAC allows the owner to determine who will have access to objects they control and the permissions related to that access. An example of DAC includes user-controlled table permissions. When DAC policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of DCA require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review application or system documentation to identify the required DAC. Review the security configuration of the database. If applicable, review the security configuration of the application(s) using the database. If the DAC defined in the documentation is not implemented in the security configuration, this is a finding. Validate database object ownership using the queries below: View object ownership - All objects and schemas SELECT object_id, SCHEMA_NAME(schema_id) AS SchemaName, [name] AS Securable, USER_NAME(principal_id) AS ObjectOwner, [type_desc] AS ObjectType FROM sys.objects WHERE is_ms_shipped = 0 AND principal_id IS NOT NULL ORDER BY ObjectType, Securable, ObjectOwner View object ownership - Specific object DECLARE @ObjectName nvarchar(512) SET @ObjectName = '' --Specify object name here SELECT object_id, SCHEMA_NAME(schema_id) AS SchemaName, [name] AS Securable, USER_NAME(principal_id) AS ObjectOwner, [type_desc] AS ObjectType FROM sys.objects WHERE is_ms_shipped = 0 AND principal_id IS NOT NULL AND [name] = @ObjectName ORDER BY ObjectType, Securable, ObjectOwner View object ownership - Specific schema DECLARE @SchemaName nvarchar(512) SET @SchemaName = '' --Specify schema name here SELECT object_id, SCHEMA_NAME(schema_id) AS SchemaName, [name] AS Securable, USER_NAME(principal_id) AS ObjectOwner, [type_desc] AS ObjectType FROM sys.objects WHERE is_ms_shipped = 0 AND principal_id IS NOT NULL AND SCHEMA_NAME(schema_id) = @SchemaName ORDER BY ObjectType, Securable, ObjectOwner Schemas not owned by the schema or [dbo] SELECT [name] AS [SchemaName], USER_NAME(principal_id) AS [SchemaOwner] FROM sys.schemas WHERE schema_id != principal_id --exclude schemas owned by the schema AND principal_id != 1 --exclude schema dbo Database principals delegated the right to assign additional permissions SELECT U.type_desc AS [PrincipalType], U.name AS [Grantee], DP.class_desc AS [SecurableType], CASE DP.class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_NAME(DP.major_id) WHEN 3 THEN SCHEMA_NAME(DP.major_id) ELSE CAST(DP.major_id AS nvarchar) END AS [Securable], permission_name AS [PermissionName], state_desc AS [DelegatedRight] FROM sys.database_permissions DP JOIN sys.database_principals U ON DP.grantee_principal_id = U.principal_id WHERE DP.state = 'W' ORDER BY Grantee, SecurableType, Securable If any of these rights are not documented and authorized, this is a finding.

## Group: SRG-APP-000342-DB-000302

**Group ID:** `V-255317`

### Rule: Azure SQL Database must restrict execution of stored procedures and functions that utilize [execute as] to necessary cases only.

**Rule ID:** `SV-255317r879719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, to provide required functionality, a DBMS needs to execute internal logic (stored procedures, functions, triggers, etc.) and/or external code modules with elevated privileges. However, if the privileges required for execution are at a higher level than the privileges assigned to organizational users invoking the functionality applications/programs, those users are indirectly provided with greater privileges than assigned by organizations. Privilege elevation by "Execute As" must be utilized only where necessary and protected from misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain a listing of stored procedures and functions that utilize impersonation. Execute the following query: SELECT S.name AS schema_name, O.name AS module_name, USER_NAME(CASE M.execute_as_principal_id WHEN -2 THEN COALESCE(O.principal_id, S.principal_id) ELSE M.execute_as_principal_id END) AS execute_as FROM sys.sql_modules M JOIN sys.objects O ON M.object_id = O.object_id JOIN sys.schemas S ON O.schema_id = S.schema_id WHERE execute_as_principal_id IS NOT NULL ORDER BY schema_name, module_name If any procedures or functions are returned that are not documented, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-255318`

### Rule: Azure SQL Database must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-255318r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. Azure SQL Database functionality and the nature and requirements of databases will vary, so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. Azure SQL Database must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Azure SQL Database supports only software development, experimentation and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. Obtain a listing of users and roles who are authorized to create, alter, or replace logic modules from the server documentation. Execute the following query to obtain a list of database principals: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) Execute the following query to obtain a list of role memberships: SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id WHERE R.name IN ('db_ddladmin','db_owner') AND M.name != 'dbo' If unauthorized access to the principal(s)/role(s) has been granted, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-255319`

### Rule: Azure SQL Database must enforce access restrictions associated with changes to the configuration of the Azure SQL Database server or database(s).

**Rule ID:** `SV-255319r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals must be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of logins who have privileged permissions and role memberships in the data and control planes of Azure SQL Database. For Database Permissions: SELECT P.type_desc AS principal_type, P.name AS principal_name, O.type_desc, CASE class WHEN 0 THEN DB_NAME() WHEN 1 THEN OBJECT_SCHEMA_NAME(major_id) + '.' + OBJECT_NAME(major_id) WHEN 3 THEN SCHEMA_NAME(major_id) ELSE class_desc + '(' + CAST(major_id AS nvarchar) + ')' END AS securable_name, DP.state_desc, DP.permission_name FROM sys.database_permissions DP JOIN sys.database_principals P ON DP.grantee_principal_id = P.principal_id LEFT OUTER JOIN sys.all_objects O ON O.object_id = DP.major_id AND O.type IN ('TR','TA','P','X','RF','PC','IF','FN','TF','U') WHERE DP.type IN ('AL','ALTG') AND DP.class IN (0, 1, 53) For Database Role Memberships: SELECT R.name AS role_name, M.type_desc AS principal_type, M.name AS principal_name FROM sys.database_principals R JOIN sys.database_role_members DRM ON R.principal_id = DRM.role_principal_id JOIN sys.database_principals M ON DRM.member_principal_id = M.principal_id AND M.name != 'dbo' For Control Plane Role Memberships, run in PowerShell: $AzureSqlDbName = '<Azure SQL Database Name>' $AzureSqlDbResourceID = Get-AzResource -Name $AzureSqlDbName Get-AzRoleAssignment -Scope $AzureSqlDbResourceID.ResourceId -IncludeClassicAdministrators | Format-Table DisplayName,RoleDefinitionName Check the documentation to verify the logins and roles returned are authorized. If the logins and/or roles are not documented and authorized, this is a finding.

## Group: SRG-APP-000416-DB-000380

**Group ID:** `V-255320`

### Rule: Azure SQL Database must use NSA-approved cryptography to protect classified information in accordance with the data owners requirements.

**Rule ID:** `SV-255320r879944_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. NSA-approved cryptography for classified networks is hardware based. This requirement addresses the compatibility of Azure SQL Database with the encryption devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the TSQL query below to determine database encryption state: SELECT DB_NAME(database_id) AS DatabaseName, encryption_state_desc AS EncryptionState, key_algorithm+CAST(key_length AS nvarchar(128)) AS EncryptionAlgorithm, encryptor_type FROM sys.dm_database_encryption_keys Validate that for each database the [EncryptionState] is "ENCRYPTED" and the [EncryptionAlgorithm] returns one of the following values: [AES128], [AES192], or [AES256]. If any other value is returned for either the [EncryptionState] or [EncryptionAlgorithm], this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-255321`

### Rule: Azure SQL Database must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-255321r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Azure SQL Databases handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of the Azure SQL Database to ensure data at rest protections are implemented. If any of the information defined as requiring cryptographic protection from modification is not encrypted in a manner that provides the required level of protection, this is a finding. Retrieve Transparent Data Encryption status: $LogicalServerName = "myServer" $RGname = "myRG" $DBName = "myDatabase" Get-AzSqlDatabaseTransparentDataEncryption -ServerName $LogicalServerName -ResourceGroupName $RGname -DatabaseName $DBname Validate that Azure SQL Database Transparent Data Encryption (TDE) is enabled. If TDE is disabled, this is a finding.

## Group: SRG-APP-000429-DB-000387

**Group ID:** `V-255322`

### Rule: Azure SQL Database must implement cryptographic mechanisms preventing the unauthorized disclosure of organization-defined information at rest on organization-defined information system components.

**Rule ID:** `SV-255322r879800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Azure SQL Databases handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of the Azure SQL Database to ensure data at rest protections are implemented. If any of the information defined as requiring cryptographic protection from modification is not encrypted in a manner that provides the required level of protection, this is a finding. Retrieve Transparent Data Encryption status: $LogicalServerName = "myServerName" $RGname = "myResourceGroup" $DBName = "myDatabaseName" Get-AzSqlDatabaseTransparentDataEncryption -ServerName $LogicalServerName -ResourceGroupName $RGname -DatabaseName $DBname

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-255323`

### Rule: When invalid inputs are received, the Azure SQL Database must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-255323r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS code (stored procedures, functions, triggers), application code, settings, column and field definitions, and constraints to determine whether the database is protected against invalid input. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If column/field definitions are not reflective of the data, this is a finding. If columns/fields do not contain constraints and validity checking where required, this is a finding. Where a column/field is noted in the system documentation as necessarily free-form, even though its name and context suggest that it should be strongly typed and constrained, the absence of these protections is not a finding. Where a column/field is clearly identified by name, caption or context as Notes, Comments, Description, Text, etc., the absence of these protections is not a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-255324`

### Rule: The Azure SQL Database must be configured to generate audit records for DOD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-255324r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within Azure SQL Database (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the list of events for which Azure SQL Database will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Azure SQL Database to see if an auditing is enabled. Execute the following steps: 1. In the Azure Portal, open a Cloud Shell session. 2. Run this PowerShell command to determine if SQL Auditing is enabled: $ResourceGroup = "myResourceGroup" $ServerName = "myServerName" Get-AzSqlServerAudit -ResourceGroupName $ResourceGroup -ServerName $ServerName ` | Select-object -property BlobStorageTargetState,LogAnalyticsTargetState,EventHubTargetState If BlobStorageTargetState, LogAnalyticsTargetState and EventHubTargetState (all three) are Disabled, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-255325`

### Rule: Azure SQL Database must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-255325r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of approved audit maintainers from the system documentation. If any role memberships are not documented and authorized, this is a finding. Review the Azure roles and individual users, all of which enable the ability to create and maintain audits. To review the Azure roles and users, navigate to the Azure Portal and review the Azure Server controlling the Azure SQL Database. 1. Select "Access Control (IAM)". 2. Select "Role assignments" and review the roles assigned to each user. 3. Select "Roles", and then select "View" under the Details column for each role. Any roles or users with Write permissions to the auditing policy must be documented. This may include but is not limited to the Owner, Contributor, and Administrator roles. If any of the roles or users have permissions that are not documented, or the documented audit maintainers do not have permissions, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-255326`

### Rule: The Azure SQL Database must be able to generate audit records when privileges/permissions are retrieved.

**Rule ID:** `SV-255326r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that SQL Server continually performs to determine if any and every action on the database is permitted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when privileges/permissions/role memberships are retrieved. To determine if an audit is configured, follow the instructions below: Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000091-DB-000325

**Group ID:** `V-255327`

### Rule: The Azure SQL Database must be able to generate audit records when unsuccessful attempts to retrieve privileges/permissions occur.

**Rule ID:** `SV-255327r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Under some circumstances, it may be useful to monitor who/what is reading privilege/permission/role information. Therefore, it must be possible to configure auditing to do this. DBMSs typically make such information available through views or functions. This requirement addresses explicit requests for privilege/permission/role membership information. It does not refer to the implicit retrieval of privileges/permissions/role memberships that Azure SQL Database continually performs to determine if any and every action on the database is permitted. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when the system denies or fails to complete attempts to retrieve privileges/permissions/role membership. To determine if an audit is configured, follow the instructions below: Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000092-DB-000208

**Group ID:** `V-255328`

### Rule: Azure SQL Database must initiate session auditing upon startup.

**Rule ID:** `SV-255328r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Session auditing is for use when a user's activities are under investigation. To ensure capture of all activity during those periods when session auditing is in use, it needs to be in operation for the whole time Azure SQL Database is running.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When Audits are enabled, they start up when the audits are enabled and remain operating until the audit is disabled. Check if an audit is configured and enabled. To determine if session auditing is configured and enabled, follow the instructions below: Run this TSQL command to determine if SQL Auditing is configured and enabled: SELECT * FROM sys.database_audit_specifications where (name = 'SqlDbAuditing_ServerAuditSpec' or name = 'SqlDbAuditing_AuditSpec') and is_state_enabled = 1 All currently defined audits for the Azure SQL Database instance will be listed. If no audits are returned, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-255329`

### Rule: Azure SQL Database must include additional, more detailed, organization-defined information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-255329r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. To support analysis, some types of events will need information to be logged that exceeds the basic requirements of event type, time stamps, location, source, outcome, and user identity. If additional information is not available, it could negatively impact forensic investigations into user actions or other malicious events. The organization must determine what additional information is required for complete analysis of the audited events. The additional information required is dependent on the type of information (e.g., sensitivity of the data and the environment within which it resides). At a minimum, the organization must employ either full-text recording of privileged commands or the individual identities of users of shared accounts, or both. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Examples of detailed information the organization may require in audit records are full-text recording of privileged commands or the individual identities of shared account users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If an Azure SQL Database Audit is not in use for audit purposes, this is a finding, unless a third-party product is being used that can perform detailed auditing for Azure SQL Database. Review system documentation to determine whether Azure SQL Database is required to audit any events and fields in addition to those in the standard audit. If there are none specified, this is not a finding. If Azure SQL Database Audit is in use, compare the audit specification(s) with the documented requirements. If any such requirement is not satisfied by the audit specification(s) (or by supplemental, locally-deployed mechanisms), this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-255330`

### Rule: The audit information produced by Azure SQL Database must be protected from unauthorized read access.

**Rule ID:** `SV-255330r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records must not allow the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. SQL Server is an application that is able to view and manipulate audit file data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000121-DB-000202</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To obtain the Azure SQL Database audit file location(s), navigate to the Azure Portal, select the Azure SQL Database, then select "Auditing". Review the storage settings for the audit. Verify that the audit storage has the correct permissions by doing the following: 1. Review the Azure roles and users by navigating to the Azure Portal. 2. Review the Azure Server controlling the Azure SQL Database. 3. Select "Access Control (IAM)". 4. Select "Role assignments" and review the roles assigned to each user. 5. Select "Roles" and then select "View" under the "Details" column for each role. Any roles or users with Read permissions to the auditing policy must be documented. If not documented, this is a finding.

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-255331`

### Rule: The audit information produced by Azure SQL Database must be protected from unauthorized modification.

**Rule ID:** `SV-255331r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of, or access to, those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. SQL Server is an application that is able to view and manipulate audit file data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the Azure SQL Database audit file location(s) by navigating to the Azure Portal and selecting the Azure SQL Database, then selecting Auditing. Review the storage settings for the audit. Verify that the audit storage has the correct permissions by doing the following: 1. Navigate to the Azure Portal to review the Azure roles and users. 2. Review the Azure Server controlling the Azure SQL Database. 3. Select "Access Control (IAM)". 4. Select "Role assignments" and review the roles assigned to each user. 5. Select "Roles", and then select "View" under the Details column for each role. Any roles or users with Write permissions to the auditing policy must be documented. If not, this is a finding.

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-255332`

### Rule: The audit information produced by Azure SQL Database must be protected from unauthorized deletion.

**Rule ID:** `SV-255332r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database. Satisfies: SRG-APP-000120-DB-000061, SRG-APP-000122-DB-000203, SRG-APP-000123-DB-000204</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the Azure SQL Database audit file location(s) by navigating to the Azure Portal and selecting the Azure SQL Database, then selecting Auditing. Review the storage settings for the audit. Verify that the audit storage has the correct permissions by doing the following: 1. Navigate to the Azure Portal to review the Azure roles and users. 2. Review the Azure Server controlling the Azure SQL Database. 3. Select "Access Control (IAM)". 4. Select "Role assignments" and review the roles assigned to each user. 5. Select "Roles", and then select "View" under the Details column for each role. Any roles or users with Write permissions to the auditing policy must be documented. If not, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-255333`

### Rule: Azure SQL Database default demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-255333r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality, not required for every mission, that cannot be disabled. Azure SQL Database must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the Azure SQL Database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review vendor documentation and vendor websites to identify vendor-provided demonstration or sample databases, database applications, objects, and files. Review the Azure SQL Database to determine if any of the demonstration and sample databases, database applications, or files are installed in the database or are included with the Azure SQL Database. If any are present in the database or are included with the Azure SQL Database, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-255334`

### Rule: The Azure SQL Database must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-255334r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Azure SQL Database must only use approved firewall settings, including disabling public network access. This value is allowed by default in Azure SQL Database and must be disabled if not otherwise documented and approved. Obtain a list of all approved firewall settings from the database documentation. From the Azure Portal Dashboard, click the database, then click "Set Server Firewall". Verify that the public network access option is set to disabled. If the value is enabled and not specifically approved in the database documentation, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-255335`

### Rule: Azure SQL Database must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-255335r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database users to determine whether shared accounts exist. (This does not include the case where Azure SQL Database has a guest or public account that is providing access to publicly available information.) If accounts are determined to be shared, determine if individuals are first individually authenticated. Where an application connects to Azure SQL Database using a standard, shared account, ensure it also captures the individual user identification and passes it to Azure SQL Database. If individuals are not individually authenticated before using the shared account (e.g., by the operating system or possibly by an application making calls to the database), this is a finding. If accounts are determined to be shared, determine if they are directly accessible to end users. If so, this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-255336`

### Rule: Azure SQL Database must map the PKI-authenticated identity to an associated user account.

**Rule ID:** `SV-255336r879614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to an Azure SQL Database user account for the authenticated identity to be meaningful to Azure SQL Database and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that Azure Active Directory is configured as the authentication type, use the following PowerShell commands: $LogicalServerName = "myServer" Get-AzSqlServer -ServerName $LogicalServerName | Get-AzSqlServerActiveDirectoryOnlyAuthentication If AzureADOnlyAuthentication returns False, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-255337`

### Rule: Azure SQL Database must uniquely identify and authenticate nonorganizational users (or processes acting on behalf of nonorganizational users).

**Rule ID:** `SV-255337r879617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonorganizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Nonorganizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, assets, individuals, and other organizations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documentation, Azure SQL Database settings, and authentication system settings to determine if nonorganizational users are individually identified and authenticated when logging onto the system. If accounts are determined to be shared, determine if individuals are first individually authenticated. Where an application connects to Azure SQL Database using a standard, shared account, ensure that it also captures the individual user identification and passes it to Azure SQL Database. If the documentation indicates that this is a public-facing, read-only (from the point of view of public users) database that does not require individual authentication, this is not a finding. If nonorganizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-255338`

### Rule: Azure SQL Database must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-255338r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding Azure SQL Database management is presented on an interface available for users, information on Azure SQL Database settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To validate Azure role-based access controls (RBAC) for a specific resource, use the PowerShell script below: $LogicalServerName = "myServer" $ResourceScope = Get-AzResource -name $LogicalServerName | Where-Object {$_.ResourceType -eq "Microsoft.Sql/servers"} | Select-Object -ExpandProperty ResourceID Get-AzRoleAssignment | Where-Object {$_.Scope -eq $ResourceScope} If a user not assigned information system management responsibilities has membership in any of the following roles, this is a finding: ##SQL DB Contributor ##SQL Security Manager ##SQL Server Contributor ##User Access Administrator ##Owner ##Contributor ##Reader

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-255339`

### Rule: Azure SQL Database must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-255339r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in nonmobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the PowerShell command below to determine database encryption status: $LogicalServerName = "myServerName" $RGname = "myRG" $DBName = "myDatabaseName" Get-AzSqlDatabaseTransparentDataEncryption -ServerName $LogicalServerName -ResourceGroupName $RGname -DatabaseName $Dbname If the application owner and Authorizing Official have determined that encryption of data at rest is required and the "EncryptionState" column returns "UNENCRYPTED" or "DECRYPTION_IN_PROGRESS", this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-255340`

### Rule: Azure SQL Database must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-255340r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If the system owner, data owner, or organization requires additional assurance, this is a finding.

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-255341`

### Rule: Azure SQL Database must prevent nonprivileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-255341r879717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation must include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from Nonprivileged users. A privileged function in Azure SQL Database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an Azure SQL Database environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; Any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of Azure SQL Database and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of Azure SQL Database security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database securables and built-in role membership to ensure only authorized users have privileged access and the ability to create server-level objects and grant permissions to themselves or others. Review the system documentation to determine the required levels of protection for Azure SQL Database securables. Review the permissions in place in the control and data planes in Azure SQL Database. If the actual permissions do not match the documented requirements, this is a finding. Ensure only the documented and approved logins have privileged functions in Azure SQL Database. If the current configuration does not match the documented baseline, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-255342`

### Rule: Azure SQL Database must utilize centralized management of the content captured in audit records generated by all components of the DBMS.

**Rule ID:** `SV-255342r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Azure SQL Database may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with offloading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are offloaded and how local audit log space is managed. From the Azure Portal Azure SQL Database page, select Auditing. Review the audit storage methods in use. If Azure SQL Database audit records are not written directly to or systematically transferred to a centralized log management system, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-255343`

### Rule: Azure SQL Database must be able to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-255343r917652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure sufficient storage capacity for the audit logs, the Azure SQL Database must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be offloaded to a centralized log management system, it remains necessary to provide space to serve as a buffer against outages and capacity limits of the offloading mechanism. The task of allocating audit record storage capacity is usually performed during initial setup of Azure SQL Database and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as the maximum storage account size for blob data is 5PB, the total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are offloaded to the central log management system; and any limitations that exist on the Azure storage accounts ability to reuse the space formerly occupied by offloaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Refer to the online documentation for the Azure SQL Database Audit configuration or the online documentation for the PowerShell cmdlet Get-AzSQLServerAudit using the links provided below. https://docs.microsoft.com/en-us/azure/azure-sql/database/auditing-overview#manage-auditing https://docs.microsoft.com/en-us/powershell/module/az.sql/get-azsqlserveraudit?view=azps-6.4.0 Use the following PowerShell script to check for the proper configuration settings: $FormatEnumerationLimit=-1 Get-AzSqlServerAudit -ResourceGroupName "Resource Group Name" -ServerName "Azure SQL Server Name" | Format-List -Property ServerName, *TargetState If the BlobStorageTargetState, EventHubTargetState, or LogAnalyticsTargetState is disabled, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-255344`

### Rule: Azure SQL Database must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-255344r917654_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing for Azure SQL Database tracks database events and writes them to an audit log in the Azure storage account, Log Analytics workspace, or Event Hubs. Under normal conditions, the audit space allocated by an Azure Storage account can grow quite large. Since a requirement exists to halt processing upon audit failure, a service outage would result.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Azure SQL Database must provide notice upon audit storage reaching capacity. Verify if an Azure Rule exists with the following command example: $storageAcct = Get-AzStorageAccount -ResourceGroupName "Name of RG for Audit Storage" -Name "Audit Storage Account Name" $metric = Get-AzMetricAlertRuleV2 | Where-Object TargetResourceId -eq $storageAcct.Id $metric.Criteria If no alert exists, this is a finding. If the criteria does not match 75 percent or less than the maximum capacity of 5 TiB, this is a finding.

## Group: SRG-APP-000381-DB-000361

**Group ID:** `V-255345`

### Rule: Azure SQL Database must produce audit records of its enforcement of access restrictions associated with changes to the configuration of Azure SQL Database(s).

**Rule ID:** `SV-255345r879754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to configuration, it would be difficult to identify attempted attacks and an audit trail would not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when denied actions occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-255346`

### Rule: Azure SQL Database must only use approved firewall settings deemed by the organization to be secure, including denying public network access.

**Rule ID:** `SV-255346r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure firewall settings, such as allowing public access, exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Azure SQL Database must only use approved firewall settings, including denying public network access. This value is allowed by default in Azure SQL Database and should be disabled if not otherwise documented and approved. Obtain a list of approved firewall settings from the database documentation. Verify that the public network access option is set to disabled. If the value is enabled and not in use and specifically approved in the database documentation, this is a finding. 1. From the Azure Portal Dashboard, click "Set Server Firewall". 2. Review the Allow Azure services and resources to access this server option.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-255347`

### Rule: Azure SQL Database must only use approved firewall settings deemed by the organization to be secure, including denying azure services access to the server.

**Rule ID:** `SV-255347r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure firewall settings, such as allowing azure services to access the server, exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Azure SQL Database must only use approved firewall settings, including denying access to azure services and resources to the server. This option is denied by default in Azure SQL Database and should be left disabled if not otherwise documented and approved. Obtain a list of approved firewall settings from the database documentation. Verify that the "Allow Azure services and resources to access this server" option is disabled. 1. From the Azure Portal, navigate to the Azure SQL Database Dashboard. 2. Select "Set Server Firewall" on the top menu. 3. Under "Exceptions", review the "Allow Azure services and resources to access this server" option and verify that the value is not checked. If the "Allow Azure services and resources to access this server" option is enabled, it must be necessary and specifically approved in the database documentation, otherwise this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-255348`

### Rule: Azure SQL Database must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-255348r879812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, Azure SQL Database, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Document transmission protection mechanisms based on organizationally defined requirements, if this documentation does not exist this is a finding. Validate that transmission protection mechanisms match documentation of organizationally defined requirements, if discrepancies exist this is a finding. Run the following PowerShell script to check the TLS version: $ResourceGroupName = '<Resource Group Name>' Get-AzSqlServer -ResourceGroupName $ResourceGroupName | Format-Table ServerName,MinimalTlsVersion Ensure that the minimum TLS version property is set to the latest available TLS version, if a less secure TLS version is set this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-255349`

### Rule: Azure SQL Database must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-255349r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, Azure SQL Database, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Document reception protection mechanisms based on organizationally defined requirements, if this documentation does not exist this is a finding. Validate that reception protection mechanisms match documentation of organizationally defined requirements, if discrepancies exist this is a finding. Run the following PowerShell script to check the TLS version: $ResourceGroupName = '<Resource Group Name>' Get-AzSqlServer -ResourceGroupName $ResourceGroupName | Format-Table ServerName,MinimalTlsVersion Verify that the minimum TLS version property is set to the latest available TLS version. If a less secure TLS version is set, this is a finding.

## Group: SRG-APP-000492-DB-000332

**Group ID:** `V-255350`

### Rule: Azure SQL DB must be able to generate audit records when security objects are accessed.

**Rule ID:** `SV-255350r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when security objects are accessed. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000492-DB-000333

**Group ID:** `V-255351`

### Rule: Azure SQL DB must generate audit records when unsuccessful attempts to access security objects occur.

**Rule ID:** `SV-255351r879863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the security configuration must be tracked. This requirement applies to situations where security data is retrieved or modified via data manipulation operations, as opposed to via specialized security functionality. In a SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to access security objects occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000494-DB-000344

**Group ID:** `V-255352`

### Rule: Azure SQL DB must generate audit records when categorized information (e.g., classification levels/security levels) is accessed.

**Rule ID:** `SV-255352r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when categorized information is accessed. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000494-DB-000345

**Group ID:** `V-255353`

### Rule: Azure SQL DB must generate audit records when unsuccessful attempts to access categories of information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-255353r879865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to access categories of information occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000495-DB-000326

**Group ID:** `V-255354`

### Rule: Azure SQL DB must generate audit records when privileges/permissions are added.

**Rule ID:** `SV-255354r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an Azure SQL Database environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when privileges/permissions are added. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000495-DB-000327

**Group ID:** `V-255355`

### Rule: Azure SQL DB must generate audit records when unsuccessful attempts to add privileges/permissions occur.

**Rule ID:** `SV-255355r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. In an Azure SQL Database environment, adding permissions is typically done via the GRANT command, or, in the negative, the DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to add privileges/permissions occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000495-DB-000328

**Group ID:** `V-255356`

### Rule: Azure SQL DB must generate audit records when privileges/permissions are modified.

**Rule ID:** `SV-255356r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, modifying permissions is typically done via the GRANT, REVOKE, and DENY commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when privileges/permissions are modified. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000495-DB-000329

**Group ID:** `V-255357`

### Rule: Azure SQL DB must generate audit records when unsuccessful attempts to modify privileges/permissions occur.

**Rule ID:** `SV-255357r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. In an SQL environment, modifying permissions is typically done via the GRANT, REVOKE, and DENY commands. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to modify privileges/permissions occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000496-DB-000334

**Group ID:** `V-255358`

### Rule: Azure SQL Database must generate audit records when security objects are modified.

**Rule ID:** `SV-255358r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when security objects are modified. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000496-DB-000335

**Group ID:** `V-255359`

### Rule: Azure SQL DB must generate audit records when unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-255359r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the database objects (tables, views, procedures, functions) that record and control permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized changes to the security subsystem could go undetected. The database could be severely compromised or rendered inoperative. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to modify security objects occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000498-DB-000346

**Group ID:** `V-255360`

### Rule: Azure SQL Database must generate audit records when categorized information (e.g., classification levels/security levels) is modified.

**Rule ID:** `SV-255360r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when categorized information is modified. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000498-DB-000347

**Group ID:** `V-255361`

### Rule: Azure SQL Database must generate audit records when unsuccessful attempts to modify categorized information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-255361r879869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categories of information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to modify categorized information occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000499-DB-000330

**Group ID:** `V-255362`

### Rule: Azure SQL Database must generate audit records when privileges/permissions are deleted.

**Rule ID:** `SV-255362r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized elevation or restriction of privileges could go undetected. Elevated privileges give users access to information and functionality that they should not have; restricted privileges wrongly deny access to authorized users. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when privileges/permissions are deleted. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000499-DB-000331

**Group ID:** `V-255363`

### Rule: Azure SQL Database must generate audit records when unsuccessful attempts to delete privileges/permissions occur.

**Rule ID:** `SV-255363r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failed attempts to change the permissions, privileges, and roles granted to users and roles must be tracked. Without an audit trail, unauthorized attempts to elevate or restrict privileges could go undetected. In an SQL environment, deleting permissions is typically done via the REVOKE or DENY command. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to delete privileges/permissions occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000501-DB-000336

**Group ID:** `V-255364`

### Rule: Azure SQL Database must generate audit records when security objects are deleted.

**Rule ID:** `SV-255364r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an event occurs, it must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when security objects are deleted. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000501-DB-000337

**Group ID:** `V-255365`

### Rule: Azure SQL Database must generate audit records when unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-255365r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The removal of security objects from the database/DBMS would seriously degrade a system's information assurance posture. If such an action is attempted, it must be logged. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to delete security objects occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_CHANGE_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000502-DB-000348

**Group ID:** `V-255366`

### Rule: Azure SQL Database must generate audit records when categories of information (e.g., classification levels/security levels) are deleted.

**Rule ID:** `SV-255366r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when categorized information is deleted. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000502-DB-000349

**Group ID:** `V-255367`

### Rule: Azure SQL Database must generate audit records when unsuccessful attempts to delete categories of information (e.g., classification levels/security levels) occur.

**Rule ID:** `SV-255367r879873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes in categorized information must be tracked. Without an audit trail, unauthorized access to protected data could go undetected. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones. For detailed information on categorizing information, refer to FIPS Publication 199, Standards for Security Categorization of Federal Information and Information Systems, and FIPS Publication 200, Minimum Security Requirements for Federal Information and Information Systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful attempts to delete categorized information occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000503-DB-000350

**Group ID:** `V-255368`

### Rule: Azure SQL Database must generate audit records when successful logons or connections occur.

**Rule ID:** `SV-255368r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who/what (a user or other principal) logs on to Azure SQL Database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when successful logons or connections occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000503-DB-000351

**Group ID:** `V-255369`

### Rule: Azure SQL Database must generate audit records when unsuccessful logons or connection attempts occur.

**Rule ID:** `SV-255369r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track failed attempts to log on to Azure SQL Database. While positive identification may not be possible in a case of failed authentication, as much information as possible about the incident must be captured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful logons or connection attempts occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: FAILED_DATABASE_AUTHENTICATION_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000504-DB-000354

**Group ID:** `V-255370`

### Rule: Azure SQL Database must generate audit records for all privileged activities or other system-level access.

**Rule ID:** `SV-255370r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples in SQL include: TRUNCATE TABLE; DELETE, or DELETE affecting more than n rows, for some n, or DELETE without a WHERE clause; UPDATE or UPDATE affecting more than n rows, for some n, or UPDATE without a WHERE clause; any SELECT, INSERT, UPDATE, or DELETE to an application-defined security table executed by other than a security principal. Depending on the capabilities of Azure SQL Database and the design of the database and associated applications, audit logging may be achieved by means of Azure SQL Database auditing features, database triggers, other mechanisms, or a combination of these. Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced for all privileged activities or other system-level access. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_CHANGE_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP USER_CHANGE_PASSWORD_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000504-DB-000355

**Group ID:** `V-255371`

### Rule: Azure SQL Database must generate audit records for all unsuccessful attempts to execute privileged activities or other system-level access.

**Rule ID:** `SV-255371r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking privileged activity, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. System documentation should include a definition of the functionality considered privileged. A privileged function in this context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In an SQL environment, it encompasses, but is not necessarily limited to: CREATE ALTER DROP GRANT REVOKE DENY Note that it is particularly important to audit, and tightly control, any action that weakens the implementation of this requirement itself, since the objective is to have a complete audit trail of all administrative activity. To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced for all unsuccessful attempts to execute privileged activities or other system-level access. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_CHANGE_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP USER_CHANGE_PASSWORD_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000505-DB-000352

**Group ID:** `V-255372`

### Rule: Azure SQL Database must generate audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-255372r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to know how long a user's (or other principal's) connection to the Azure Database lasts. This can be achieved by recording disconnections, in addition to logons/connections, in the audit logs. Disconnection may be initiated by the user or forced by the system (as in a timeout) or result from a system or network failure. To the greatest extent possible, all disconnections must be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced showing starting and ending time for user access to the database(s). To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT distinct audit_action_name FROM sys.database_audit_specification_details ORDER BY audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: APPLICATION_ROLE_CHANGE_PASSWORD_GROUP BACKUP_RESTORE_GROUP DATABASE_CHANGE_GROUP DATABASE_OBJECT_CHANGE_GROUP DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP DATABASE_OBJECT_PERMISSION_CHANGE_GROUP DATABASE_OPERATION_GROUP DATABASE_OWNERSHIP_CHANGE_GROUP DATABASE_PERMISSION_CHANGE_GROUP DATABASE_PRINCIPAL_CHANGE_GROUP DATABASE_PRINCIPAL_IMPERSONATION_GROUP DATABASE_ROLE_MEMBER_CHANGE_GROUP DBCC_GROUP SCHEMA_OBJECT_CHANGE_GROUP SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP USER_CHANGE_PASSWORD_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000506-DB-000353

**Group ID:** `V-255373`

### Rule: Azure SQL Database must generate audit records when concurrent logons/connections by the same user from different workstations occur.

**Rule ID:** `SV-255373r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For completeness of forensic analysis, it is necessary to track who logs on to Azure SQL Database. Concurrent connections by the same user from multiple workstations may be valid use of the system; or such connections may be due to improper circumvention of the requirement to use the CAC for authentication; or they may indicate unauthorized account sharing; or they may be because an account has been compromised. If the fact of multiple, concurrent logons by a given user can be reliably reconstructed from the log entries for other events (logons/connections; voluntary and involuntary disconnections), it is not mandatory to create additional log entries specifically for this.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when concurrent logons/connections by the same user from different workstations occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000507-DB-000356

**Group ID:** `V-255374`

### Rule: Azure SQL Database must be able to generate audit records when successful accesses to objects occur.

**Rule ID:** `SV-255374r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when successful accesses to objects occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000507-DB-000357

**Group ID:** `V-255375`

### Rule: Azure SQL Database must generate audit records when unsuccessful accesses to objects occur.

**Rule ID:** `SV-255375r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without tracking all or selected types of access to all or selected objects (tables, views, procedures, functions, etc.), it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. In an SQL environment, types of access include, but are not necessarily limited to: SELECT INSERT UPDATE DELETE EXECUTE To aid in diagnosis, it is necessary to keep track of failed attempts in addition to the successful ones.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced when unsuccessful accesses to objects occur. To determine if an audit is configured, execute the following script. Run this TSQL command to determine if SQL Auditing AuditActionGroups are configured: SELECT DISTINCT sd.audit_action_name FROM sys.database_audit_specification_details sd JOIN sys.database_audit_specifications s ON s.database_specification_id = sd.database_specification_id WHERE (name = 'SqlDbAuditing_ServerAuditSpec' /*Server Audit*/ OR name = 'SqlDbAuditing_AuditSpec') /*Database Audit*/ AND s.is_state_enabled = 1 ORDER BY sd.audit_action_name If no values exist for AuditActionGroup, this is a finding. Verify the following AuditActionGroup(s) are configured: SCHEMA_OBJECT_ACCESS_GROUP If any listed AuditActionGroups do not exist in the configuration, this is a finding.

## Group: SRG-APP-000508-DB-000358

**Group ID:** `V-255376`

### Rule: Azure SQL Database must generate audit records for all direct access to the database(s).

**Rule ID:** `SV-255376r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this context, direct access is any query, command, or call to Azure SQL Database that comes from any source other than the application(s) that it supports. Examples would be the command line or a database management utility program. The intent is to capture all activity from administrative and nonstandard sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Azure SQL Database configuration to verify that audit records are produced for all direct access to the database(s). To determine if an audit PredicateExpression (filter) exists, execute the following PowerShell script. 1. In the Azure Portal, open a Cloud Shell session. 2. Run this PowerShell command to determine the PredicateExpression: $ResourceGroup = "myResourceGroup" $ServerName = "myServerName" $FormatEnumerationLimit=-1 Get-AzSqlServerAudit -ResourceGroupName $ResourceGroup -ServerName $ServerName If a PredicateExpression is returned, review the associated filters to determine whether administrative activities are being excluded. If any audits are configured to exclude administrative activities, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-255377`

### Rule: Azure SQL Database must offload audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for stand-alone systems.

**Rule ID:** `SV-255377r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Azure SQL Database may write audit records blob storage, log analytics, or event hub. Multiple methods should be used to ensure audit files are retained, or immutable storage should be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are stored. 1. Review the Auditing link in the Azure Portal for the SQL Database. Ensure audit logs are written to more than one storage system. If not, navigate to the Storage Container where the audits are stored via the Portal. 2. Select "Containers". 3. Select the ellipsis on the container for the audit storage. 4. Select "Access Policy". Verify that an Immutable Blob Storage policy has been added to the audit container. If Azure audit logs are written to only one storage system or immutable storage is not enabled, this is a finding.

