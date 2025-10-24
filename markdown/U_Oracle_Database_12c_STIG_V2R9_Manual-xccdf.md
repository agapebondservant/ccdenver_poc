# STIG Benchmark: Oracle Database 12c Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219824`

### Rule: Access to default accounts used to support replication must be restricted to authorized DBAs.

**Rule ID:** `SV-219824r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Replication database accounts are used for database connections between databases. Replication requires the configuration of these accounts using the same username and password on all databases participating in the replication. Replication connections use fixed user database links. This means that access to the replication account on one server provides access to the other servers participating in the replication. Granting unauthorized access to the replication account provides unauthorized and privileged access to all databases participating in the replication group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select 'The number of replication objects defined is: '|| count(*) from all_tables where table_name like 'REPCAT%'; If the count returned is 0, then Oracle Replication is not installed and this check is not a finding. Otherwise: From SQL*Plus: select count(*) from sys.dba_repcatlog; If the count returned is 0, then Oracle Replication is not in use and this check is not a finding. If any results are returned, ask the ISSO or DBA if the replication account (the default is REPADMIN, but may be customized) is restricted to ISSO-authorized personnel only. If it is not, this is a finding. If there are multiple replication accounts, confirm that all are justified and documented with the ISSO. If they are not, this is a finding. Note: Oracle Database Advanced Replication is deprecated in Oracle Database 12c. Use Oracle GoldenGate to replace all features of Advanced Replication, including multimaster replication, updatable materialized views, hierarchical materialized views, and deployment templates.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219825`

### Rule: Oracle instance names must not contain Oracle version numbers.

**Rule ID:** `SV-219825r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service names may be discovered by unauthenticated users. If the service name includes version numbers or other database product information, a malicious user may use that information to develop a targeted attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select instance_name from v$instance; select version from v$instance; If the instance name returned references the Oracle release number, this is a finding. Numbers used that include version numbers by coincidence are not a finding. The DBA should be able to relate the significance of the presence of a digit in the SID.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219826`

### Rule: Fixed user and public database links must be authorized for use.

**Rule ID:** `SV-219826r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database links define connections that may be used by the local database to access remote Oracle databases. These links provide a means for a compromise to the local database to spread to remote databases in the distributed database environment. Limiting or eliminating use of database links where they are not required to support the operational system can help isolate compromises to the local or a limited number of databases.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select owner||': '||db_link from dba_db_links; If no records are returned from the first SQL statement, this check is not a finding. Confirm the public and fixed user database links listed are documented in the System Security Plan, are authorized by the ISSO, and are used for replication or operational system requirements. If any are not, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219827`

### Rule: A minimum of two Oracle control files must be defined and configured to be stored on separate, archived disks (physical or virtual) or archived partitions on a RAID device.

**Rule ID:** `SV-219827r879887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Oracle control files are used to store information critical to Oracle database integrity. Oracle uses these files to maintain time synchronization of database files as well as at system startup to verify the validity of system data and log files. Loss of access to the control files can affect database availability, integrity and recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select name from v$controlfile; DoD guidance recommends: 2a. Each control file is to be located on separate, archived physical or virtual storage devices. OR 2b. Each control file is to be located on separate, archived directories within one or more RAID devices. 3. The Logical Paths for each control file should differ at the highest level supported by the configuration, for example: UNIX /ora03/app/oracle/{SID}/control/control01.ctl /ora04/app/oracle/{SID}/control/control02.ctl Windows D:/oracle/{SID}/control/control01.ctl E:/oracle/{SID}/control/control02.ctl If the minimum listed above is not met, this is a finding. Consult with the SA or DBA to determine that the mount points or partitions referenced in the file paths indicate separate physical disks or directories on RAID devices. Note: Distinct does not equal dedicated. May share directory space with other Oracle database instances if present.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219828`

### Rule: A minimum of two Oracle redo log groups/files must be defined and configured to be stored on separate, archived physical disks or archived directories on a RAID device.

**Rule ID:** `SV-219828r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle redo log files store the detailed information on changes made to the database. This information is critical to database recovery in case of a database failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select count(*) from V$LOG; If the value of the count returned is less than 2, this is a finding. From SQL*Plus: select count(*) from V$LOG where members > 1; If the value of the count returned is less than 2 and a RAID storage device is not being used, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219829`

### Rule: The Oracle WITH GRANT OPTION privilege must not be granted to non-DBA or non-Application administrator user accounts.

**Rule ID:** `SV-219829r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An account permission to grant privileges within the database is an administrative function. Minimizing the number and privileges of administrative accounts reduces the chances of privileged account exploitation. Application user accounts must never require WITH GRANT OPTION privileges since, by definition, they require only privileges to execute procedures or view / edit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the query: select grantee||': '||owner||'.'||table_name from dba_tab_privs where grantable = 'YES' and grantee not in (select distinct owner from dba_objects) and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA') and table_name not like 'SYS_PLSQL_%' order by grantee; If any accounts are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219830`

### Rule: The Oracle REMOTE_OS_AUTHENT parameter must be set to FALSE.

**Rule ID:** `SV-219830r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Setting this value to TRUE allows operating system authentication over an unsecured connection. Trusting remote operating systems can allow a user to impersonate another operating system user and connect to the database without having to supply a password. If REMOTE_OS_AUTHENT is set to true, the only information a remote user needs to connect to the database is the name of any user whose account is setup to be authenticated by the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = 'remote_os_authent'; If the value returned does not equal FALSE, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219831`

### Rule: The Oracle REMOTE_OS_ROLES parameter must be set to FALSE.

**Rule ID:** `SV-219831r903017_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Setting REMOTE_OS_ROLES to TRUE allows operating system groups to control Oracle roles. The default value of FALSE causes roles to be identified and managed by the database. If REMOTE_OS_ROLES is set to TRUE, a remote user could impersonate another operating system user over a network connection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = 'remote_os_roles'; If the value returned is FALSE, this is not a finding. If the value returned is TRUE, confirm that the setting is justified and documented. If not, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219832`

### Rule: The Oracle SQL92_SECURITY parameter must be set to TRUE.

**Rule ID:** `SV-219832r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The configuration option SQL92_SECURITY specifies whether table-level SELECT privileges are required to execute an update or delete that references table column values. If this option is disabled (set to FALSE), the UPDATE privilege can be used to determine values that should require SELECT privileges. The SQL92_SECURITY setting of TRUE prevents the exploitation of user credentials with only DELETE or UPDATE privileges on a table from being able to derive column values in that table by performing a series of update/delete statements using a where clause, and rolling back the change. In the following example, with SQL92_SECURITY set to FALSE, a user with only delete privilege on the scott.emp table is able to derive that there is one employee with a salary greater than 3000. With SQL92_SECURITY set to TRUE, that user is prevented from attempting to derive a value. SQL92_SECURITY = FALSE SQL> delete from scott.emp where sal > 3000; 1 row deleted SQL> rollback; Rollback complete SQL92_SECURITY = TRUE SQL> delete from scott.emp where sal > 3000; delete from scott.emp where sal > 3000 * ERROR at line 1: ORA-01031: insufficient privileges</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = 'sql92_security'; If the value returned is set to FALSE, this is a finding. If the parameter is set to TRUE or does not exist, this is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219833`

### Rule: The Oracle password file ownership and permissions should be limited and the REMOTE_LOGIN_PASSWORDFILE parameter must be set to EXCLUSIVE or NONE.

**Rule ID:** `SV-219833r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critically important to the security of your system that you protect your password file and the environment variables that identify the location of the password file. Any user with access to these could potentially compromise the security of the connection. The REMOTE_LOGIN_PASSWORDFILE setting of "NONE" disallows remote administration of the database. The REMOTE_LOGIN_PASSWORDFILE setting of "EXCLUSIVE" allows for auditing of individual DBA logons to the SYS account. If not set to "EXCLUSIVE", remote connections to the database as "internal" or "as SYSDBA" are not logged to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where upper(name) = 'REMOTE_LOGIN_PASSWORDFILE'; If the value returned does not equal 'EXCLUSIVE' or 'NONE', this is a finding. On UNIX Systems: ls -ld $ORACLE_HOME/dbs/orapw${ORACLE_SID} Substitute ${ORACLE_SID} with the name of the ORACLE_SID for the database. If permissions are granted for world access, this is a finding. On Windows Systems (From Windows Explorer): Browse to the %ORACLE_HOME\database\directory. Select and right-click on the PWD%ORACLE_SID%.ora file, select Properties, select the Security tab. Substitute %ORACLE_SID% with the name of the ORACLE_SID for the database. If permissions are granted to everyone, this is a finding. If any account other than the DBMS software installation account is listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219834`

### Rule: System privileges granted using the WITH ADMIN OPTION must not be granted to unauthorized user accounts.

**Rule ID:** `SV-219834r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The WITH ADMIN OPTION allows the grantee to grant a privilege to another database account. Best security practice restricts the privilege of assigning privileges to authorized personnel. Authorized personnel include DBAs, object owners, and, where designed and included in the application's functions, application administrators. Restricting privilege-granting functions to authorized accounts can help decrease mismanagement of privileges and wrongful assignments to unauthorized accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and non-administrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the CREATE ANY TABLE or ALTER SESSION privilege, or EXECUTE privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either SYSTEM or SYSAUX. Non-administrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is USERS. To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Non-Administrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM, SYSKM * Subject to change based on version installed Run the SQL query: From SQL*Plus: select grantee, privilege from dba_sys_privs where grantee not in (<list of non-applicable accounts>) and admin_option = 'YES' and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA'); (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) If any accounts that are not authorized to have the ADMIN OPTION are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219835`

### Rule: System Privileges must not be granted to PUBLIC.

**Rule ID:** `SV-219835r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System privileges can be granted to users and roles and to the user group PUBLIC. All privileges granted to PUBLIC are accessible to every user in the database. Many of these privileges convey considerable authority over the database and should be granted only to those persons responsible for administering the database. In general, these privileges should be granted to roles and then the appropriate roles should be granted to users. System privileges must never be granted to PUBLIC as this could allow users to compromise the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select privilege from dba_sys_privs where grantee = 'PUBLIC'; If any records are returned, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219836`

### Rule: Oracle roles granted using the WITH ADMIN OPTION must not be granted to unauthorized accounts.

**Rule ID:** `SV-219836r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The WITH ADMIN OPTION allows the grantee to grant a role to another database account. Best security practice restricts the privilege of assigning privileges to authorized personnel. Authorized personnel include DBAs, object owners, and, where designed and included in the application's functions, application administrators. Restricting privilege-granting functions to authorized accounts can help decrease mismanagement of privileges and wrongful assignments to unauthorized accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and non-administrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the CREATE ANY TABLE or ALTER SESSION privilege, or EXECUTE privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either SYSTEM or SYSAUX. Non-administrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is USERS. To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Non-Administrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM * Subject to change based on version installed Run the SQL statement: select grantee||': '||granted_role from dba_role_privs where grantee not in (<list of non-applicable accounts>) and admin_option = 'YES' and grantee not in (select distinct owner from dba_objects) and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA') order by grantee; (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) Review the System Security Plan to confirm any grantees listed are ISSO-authorized DBA accounts or application administration roles. If any grantees listed are not authorized and documented, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219837`

### Rule: Object permissions granted to PUBLIC must be restricted.

**Rule ID:** `SV-219837r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions on objects may be granted to the user group PUBLIC. Because every database user is a member of the PUBLIC group, granting object permissions to PUBLIC gives all users in the database access to that object. In a secure environment, granting object permissions to PUBLIC must be restricted to those objects that all users are allowed to access. The policy does not require object permissions assigned to PUBLIC by the installation of Oracle Database server components be revoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and non-administrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the “CREATE ANY TABLE” or “ALTER SESSION” privilege, or “EXECUTE” privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either “SYSTEM” or “SYSAUX”. Non-administrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is “USERS”. To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Non-Administrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, , GSMADMIN_INTERNAL, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM * Subject to change based on version installed Run the SQL query: select owner ||'.'|| table_name ||':'|| privilege from dba_tab_privs where grantee = 'PUBLIC' and owner not in (<list of non-applicable accounts>); (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) If there are any records returned that are not Oracle product accounts, and are not documented and authorized, this is a finding. Note: This check may return false positives where other Oracle product accounts are not included in the exclusion list.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219838`

### Rule: The Oracle Listener must be configured to require administration authentication.

**Rule ID:** `SV-219838r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Oracle listener authentication helps prevent unauthorized administration of the Oracle listener. Unauthorized administration of the listener could lead to DoS exploits; loss of connection audit data, unauthorized reconfiguration or other unauthorized access. This is a Category I finding because privileged access to the listener is not restricted to authorized users. Unauthorized access can result in stopping of the listener (DoS) and overwriting of listener audit logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a listener is not running on the local database host server, this check is not a finding. Note: This check needs to be done only once per host system and once per listener. Multiple listeners may be defined on a single host system. They must all be reviewed, but only once per database home review. For subsequent database home reviews on the same host system, this check is not a finding. Determine all Listeners running on the host. For Windows hosts, view all Windows services with TNSListener embedded in the service name - The service name format is: Oracle[ORACLE_HOME_NAME]TNSListener For UNIX hosts, the Oracle Listener process will indicate the TNSLSNR executable. At a command prompt, issue the command: ps -ef | grep tnslsnr | grep -v grep The alias for the listener follows tnslsnr in the command output. Must be logged on the host system using the account that owns the tnslsnr executable (UNIX). If the account is denied local logon, have the system SA assist in this task by adding 'su' to the listener account from the root account. On Windows platforms, log on using an account with administrator privileges to complete the check. From a system command prompt, execute the listener control utility: lsnrctl status [LISTENER NAME] Review the results for the value of Security. If "Security = OFF" is displayed, this is a finding. If "Security = ON: Local OS Authentication" is displayed, this is not a finding. If "Security = ON: Password or Local OS Authentication", this is a finding (do not set a password on Oracle versions 10.1 and higher. Instead, use Local OS Authentication). Repeat the execution of the lsnrctl utility for all active listeners.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219839`

### Rule: Application role permissions must not be assigned to the Oracle PUBLIC role.

**Rule ID:** `SV-219839r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions granted to PUBLIC are granted to all users of the database. Custom roles must be used to assign application permissions to functional groups of application users. The installation of Oracle does not assign role permissions to PUBLIC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select granted_role from dba_role_privs where grantee = 'PUBLIC'; If any roles are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219840`

### Rule: Oracle application administration roles must be disabled if not required and authorized.

**Rule ID:** `SV-219840r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application administration roles, which are assigned system or elevated application object privileges, must be protected from default activation. Application administration roles are determined by system privilege assignment (create / alter / drop user) and application user role ADMIN OPTION privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the SQL query: select grantee, granted_role from dba_role_privs where default_role='YES' and granted_role in (select grantee from dba_sys_privs where upper(privilege) like '%USER%') and grantee not in (<list of non-applicable accounts>) and grantee not in (select distinct owner from dba_tables) and grantee not in (select distinct username from dba_users where upper(account_status) like '%LOCKED%'); (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) Review the list of accounts reported for this check and ensures that they are authorized application administration roles. If any are not authorized application administration roles, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219841`

### Rule: Connections by mid-tier web and application systems to the Oracle DBMS from a DMZ or external network must be encrypted.


**Rule ID:** `SV-219841r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multi-tier systems may be configured with the database and connecting middle-tier system located on an internal network, with the database located on an internal network behind a firewall and the middle-tier system located in a DMZ. In cases where either or both systems are located in the DMZ (or on networks external to DoD), network communications between the systems must be encrypted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the System Security Plan for remote applications that access and use the database. For each remote application or application server, determine whether communications between it and the DBMS are encrypted. If any are not encrypted, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219842`

### Rule: Database job/batch queues must be reviewed regularly to detect unauthorized database job submissions.

**Rule ID:** `SV-219842r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized users may bypass security mechanisms by submitting jobs to job queues managed by the database to be run under a more privileged security context of the database or host system. These queues must be monitored regularly to detect any such unauthorized job submissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The DBMS_JOB PL/SQL package has been replaced by DBMS_SCHEDULER in Oracle versions 10.1 and higher, though it continues to be supported for backward compatibility. Run this query: select value from v$parameter where name = 'job_queue_processes'; Run this query: select value from all_scheduler_global_attribute where ATTRIBUTE_NAME = 'MAX_JOB_SLAVE_PROCESSES'; To understand the relationship between these settings, review: https://docs.oracle.com/database/121/ADMIN/appendix_a.htm#ADMIN11002 Review documented and implemented procedures for monitoring the Oracle DBMS job/batch queues for unauthorized submissions. If procedures for job queue review are not defined, documented or evidence of implementation does not exist, this is a finding. Job queue information is available from the DBA_JOBS view. The following command lists jobs submitted to the queue. DBMS_JOB does not generate a 'history' of previous job executions. Run this query: select job, next_date, next_sec, failures, broken from dba_jobs; Scheduler queue information is available from the DBA_SCHEDULER_JOBS view. The following command lists jobs submitted to the queue. Run this query: select owner, job_name, state, job_class, job_type, job_action from dba_scheduler_jobs;

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219843`

### Rule: Unauthorized database links must not be defined and active.

**Rule ID:** `SV-219843r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMS links provide a communication and data transfer path definition between two databases that may be used by malicious users to discover and obtain unauthorized access to remote systems. Database links between production and development DBMSs provide a means for developers to access production data not authorized for their access or to introduce untested or unauthorized applications to the production database. Only protected, controlled, and authorized downloads of any production data to use for development may be allowed. Only applications that have completed the configuration management process may be introduced by the application object owner account to the production system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select db_link||': '||host from dba_db_links; If no links are returned, this check is not a finding. Review documentation for definitions of authorized database links to external interfaces. The documentation should include: - Any remote access to the database - The purpose or function of the remote connection - Any access to data or procedures stored externally to the local DBMS - Any network ports or protocols used by remote connections, whether the remote connection is to a production, test, or development system - Any security accounts used by DBMS to access remote resources or objects If any unauthorized database links are defined or the definitions do not match the documentation, this is a finding. Note: findings for production-development links under this check are assigned to the production database only. If any database links are defined between the production database and any test or development databases, this is a finding. If remote interface documentation does not exist or is incomplete, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219844`

### Rule: Sensitive information from production database exports must be modified before import to a development database.

**Rule ID:** `SV-219844r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data export from production databases may include sensitive data. Application developers do not have a need to know to sensitive data. Any access they may have to production data would be considered unauthorized access and subject the sensitive data to unlawful or unauthorized disclosure. See DODD 8500.1 for a definition of Sensitive Information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database being reviewed is a production database, this check is not a finding. Review policy, procedures and restrictions for data imports of production data containing sensitive information into development databases. If data imports of production data are allowed, review procedures for protecting any sensitive data included in production exports. If sensitive data is included in the exports and no procedures are in place to remove or modify the data to render it not sensitive prior to import into a development database or policy and procedures are not in place to ensure authorization of development personnel to access sensitive information contained in production data, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219847`

### Rule: Only authorized system accounts must have the SYSTEM tablespace specified as the default tablespace.

**Rule ID:** `SV-219847r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle SYSTEM tablespace is used by the database to store all DBMS system objects. Other use of the system tablespace may compromise system availability and the effectiveness of host system access controls to the tablespace files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the query: select property_name, property_value from database_properties where property_name in ('DEFAULT_PERMANENT_TABLESPACE','DEFAULT_TEMP_TABLESPACE'); If either value is set to SYSTEM, this is a finding. Run the query: select username from dba_users where (default_tablespace = 'SYSTEM' or temporary_tablespace = 'SYSTEM') and username not in ('LBACSYS','OUTLN','SYS','SYSTEM', 'SYSKM', 'SYSDG', 'SYSBACKUP'); If any non-default account records are returned, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219848`

### Rule: Application owner accounts must have a dedicated application tablespace.

**Rule ID:** `SV-219848r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separation of tablespaces by application helps to protect the application from resource contention and unauthorized access that could result from storage space reuses or host system access controls. Application data must be stored separately from system and custom user-defined objects to facilitate administration and management of its data storage. The SYSTEM tablespace must never be used for application data storage in order to prevent resource contention and performance degradation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the SQL query: select distinct owner, tablespace_name from dba_SEGMENTS where owner not in (<list of non-applicable accounts>) order by tablespace_name; (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) Review the list of returned table owners with the tablespace used. If any of the owners listed are not default Oracle accounts and use the SYSTEM or any other tablespace not dedicated for the application’s use, this is a finding. Look for multiple applications that may share a tablespace. If no records were returned, ask the DBA if any applications use this database. If no applications use the database, this is not a finding. If there are applications that do use the database or if the application uses the SYS or other default account and SYSTEM tablespace to store its objects, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219849`

### Rule: The directories assigned to the LOG_ARCHIVE_DEST* parameters must be protected from unauthorized access.

**Rule ID:** `SV-219849r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The LOG_ARCHIVE_DEST parameter is used to specify the directory to which Oracle archive logs are written. Where the DBMS availability and recovery to a specific point in time is critical, the protection of archive log files is critical. Archive log files may also contain unencrypted sensitive data. If written to an inadequately protected or invalidated directory, the archive log files may be accessed by unauthorized persons or processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select log_mode from v$database; select value from v$parameter where name = 'log_archive_dest'; select value from v$parameter where name = 'log_archive_duplex_dest'; select name, value from v$parameter where name LIKE 'log_archive_dest_%'; select value from v$parameter where name = 'db_recovery_file_dest'; If the value returned for LOG_MODE is NOARCHIVELOG, this check is not a finding. If a value is not returned for LOG_ARCHIVE_DEST and no values are returned for any of the LOG_ARCHIVE_DEST_[1-10] parameters, and no value is returned for DB_RECOVERY_FILE_DEST, this is a finding. Note: LOG_ARCHIVE_DEST and LOG_ARCHIVE_DUPLEX_DEST are incompatible with the LOG_ARCHIVE_DEST_n parameters, and must be defined as the null string (' ') when any LOG_ARCHIVE_DEST_n parameter has a value other than a null string. On UNIX Systems: ls -ld [pathname] Substitute [pathname] with the directory paths listed from the above SQL statements for log_archive_dest and log_archive_duplex_dest. If permissions are granted for world access, this is a finding. On Windows Systems (From Windows Explorer): Browse to the directory specified. Select and right-click on the directory, select Properties, select the Security tab. If permissions are granted to everyone, this is a finding. If any account other than the Oracle process and software owner accounts, Administrators, DBAs, System group or developers authorized to write and debug applications on this database are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219850`

### Rule: The Oracle _TRACE_FILES_PUBLIC parameter if present must be set to FALSE.

**Rule ID:** `SV-219850r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The _TRACE_FILES_PUBLIC parameter is used to make trace files used for debugging database applications and events available to all database users. Use of this capability precludes the discrete assignment of privileges based on job function. Additionally, its use may provide access to external files and data to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = '_trace_files_public'; If the value returned is TRUE, this is a finding. If the parameter does not exist or is set to FALSE, this is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219851`

### Rule: Application object owner accounts must be disabled when not performing installation or maintenance actions.

**Rule ID:** `SV-219851r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Object ownership provides all database object permissions to the owned object. Access to the application object owner accounts requires special protection to prevent unauthorized access and use of the object ownership privileges. In addition to the high privileges to application objects assigned to this account, it is also an account that, by definition, is not accessed interactively except for application installation and maintenance. This reduced access to the account means that unauthorized access to the account could go undetected. To help protect the account, it must be enabled only when access is required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the SQL query: select distinct o.owner from dba_objects o, dba_users u where o.owner not in ( <list of non-applicable accounts> ) and o.object_type <> 'SYNONYM' and o.owner = username and upper(account_status) not like '%LOCKED%'; (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) To obtain a list of users assigned DBA privileges, run the query: select grantee from dba_role_privs where granted_role = 'DBA'; If any records are returned, then verify the account is an authorized application object owner account or a default account installed to support an Oracle product. Verify that any objects owned by custom DBA accounts are for the personal use of that DBA. If any objects are used to support applications or any functions other than DBA functions, this is a finding. Any unauthorized object owner accounts are not a finding under this check as they are noted as findings under check O121-C2-011000. Any other accounts listed are a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219852`

### Rule: DBMS production application and data directories must be protected from developers on shared production/development DBMS host systems.

**Rule ID:** `SV-219852r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer roles must not be assigned DBMS administrative privileges to production DBMS application and data directories. The separation of production DBA and developer roles helps protect the production system from unauthorized, malicious or unintentional interruption due to development activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the DBMS or DBMS host is not shared by production and development activities, this check is not a finding. Review OS DBA group membership. If any developer accounts, as identified in the System Security Plan, have been assigned DBA privileges, this is a finding. Note: Though shared production/non-production DBMS installations was allowed under previous database STIG guidance, doing so may place it in violation of OS, Application, Network or Enclave STIG guidance. Ensure that any shared production/non-production DBMS installation meets STIG guidance requirements at all levels or mitigate any conflicts in STIG guidance with the AO.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219853`

### Rule: Use of the DBMS installation account must be logged.

**Rule ID:** `SV-219853r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DBMS installation account may be used by any authorized user to perform DBMS installation or maintenance. Without logging, accountability for actions attributed to the account is lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documented and implemented procedures for monitoring the use of the DBMS software installation account in the System Security Plan. If use of this account is not monitored or procedures for monitoring its use do not exist or are incomplete, this is a finding. Note: On Windows systems, The Oracle DBMS software is installed using an account with administrator privileges. Ownership should be reassigned to a dedicated OS account used to operate the DBMS software. If monitoring does not include all accounts with administrator privileges on the DBMS host, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219861`

### Rule: The DBMS data files, transaction logs and audit files must be stored in dedicated directories or disk partitions separate from software or other application files.

**Rule ID:** `SV-219861r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of DBMS data, transaction and audit data files stored by the host operating system is dependent on OS controls. When different applications share the same database, resource contention and security controls are required to isolate and protect an application's data from other applications. In addition, it is an Oracle best practice to separate data, transaction logs, and audit logs into separate physical directories according to Oracle’s OFA (Optimal Flexible Architecture). And finally, DBMS software libraries and configuration files also require differing access control lists.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the disk/directory specification where database data, transaction log and audit files are stored. If DBMS data, transaction log or audit data files are stored in the same directory, this is a finding. If multiple applications are accessing the database and the database data files are stored in the same directory, this is a finding. If multiple applications are accessing the database and database data is separated into separate physical directories according to application, this check is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219862`

### Rule: The directory assigned to the AUDIT_FILE_DEST parameter must be protected from unauthorized access and must be stored in a dedicated directory or disk partition separate from software or other application files.

**Rule ID:** `SV-219862r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The AUDIT_FILE_DEST parameter specifies the directory where the database audit trail file is stored (when AUDIT_TRAIL parameter is set to ‘OS’, ‘xml’ or ‘xml, extended’ where supported by the DBMS). Unauthorized access or loss of integrity of the audit trail could result in loss of accountability or the ability to detect suspicious activity. This directory also contains the audit trail of the SYS and SYSTEM accounts that captures privileged database events when the database is not running (when AUDIT_SYS_OPERATIONS parameter is set to TRUE).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Standard Auditing is used: From SQL*Plus: select value from v$parameter where name = 'audit_trail'; select value from v$parameter where name = 'audit_file_dest'; If audit_trail is NOT set to OS, XML or XML EXTENDED, this is not applicable (NA). If audit_trail is set to OS, but the audit records are routed directly to a separate log server without writing to the local file system, this is not a finding. On UNIX Systems: ls -ld [pathname] Replace [pathname] with the directory path listed from the above SQL command for audit_file_dest. If permissions are granted for world access, this is a finding. If any groups that include members other than the Oracle process and software owner accounts, DBAs, auditors, or backup accounts are listed, this is a finding. Compare path to $ORACLE_HOME. If audit_file_dest is a subdirectory of $ORACLE_HOME, this is a finding. On Windows Systems (From Windows Explorer): Browse to the directory specified. Select and right-click on the directory, select Properties, select the Security tab. On Windows hosts, records are also written to the Windows application event log. The location of the application event log is listed under Properties for the log under the Windows console. The default location is C:\WINDOWS\system32\config\EventLogs\AppEvent.Evt. If permissions are granted to everyone, this is a finding. If any accounts other than the Administrators, DBAs, System group, auditors or backup operators are listed, this is a finding. Compare path to %ORACLE_HOME%. If audit_file_dest is a subdirectory of %ORACLE_HOME%, this is a finding. If Unified Auditing is used: AUDIT_FILE_DEST parameter is not used in Unified Auditing

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219865`

### Rule: Access to DBMS software files and directories must not be granted to unauthorized users.

**Rule ID:** `SV-219865r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DBMS software libraries contain the executables used by the DBMS to operate. Unauthorized access to the libraries can result in malicious alteration or planting of operational executables. This may in turn jeopardize data stored in the DBMS and/or operation of the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For UNIX Systems: log on using the Oracle software owner account and enter the command: umask If the value returned is 022 or more restrictive, this is not a finding. If the value returned is less restrictive than 022, this is a finding. The first number sets the mask for user/owner file permissions. The second number sets the mask for group file permissions. The third number sets file permission mask for other users. The list below shows the available settings: 0 = read/write/execute 1 = read/write 2 = read/execute 3 = read 4 = write/execute 5 = write 6 = execute 7 = no permissions Setting the umask to 022 effectively sets files for user/owner to read/write, group to read and other to read. Directories are set for user/owner to read/write/execute, group to read/execute and other to read/execute. For Windows Systems: Review the permissions that control access to the Oracle installation software directories (e.g. \Program Files\Oracle\). DBA accounts, the DBMS process account, the DBMS software installation/maintenance account, SA accounts if access by them is required for some operational level of support such as backups, and the host system itself require access. Compare the access control employed with that documented in the System Security Plan. If access controls do not match the documented requirement, this is a finding. If access controls appear excessive without justification, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219866`

### Rule: Replication accounts must not be granted DBA privileges.

**Rule ID:** `SV-219866r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Replication accounts may be used to access databases defined for the replication architecture. An exploit of a replication on one database could lead to the compromise of any database participating in the replication that uses the same account name and credentials. If the replication account is compromised and it has DBA privileges, the database is at additional risk to unauthorized or malicious action.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a review of the System Security Plan confirms the use of replication is not required, not permitted and the database is not configured for replication, this check is not a finding. If any replication accounts are assigned DBA roles or roles with DBA privileges, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219867`

### Rule: Network access to the DBMS must be restricted to authorized personnel.

**Rule ID:** `SV-219867r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting remote access to specific, trusted systems helps prevent access by unauthorized and potentially malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
IP address restriction may be defined for the database listener, by use of the Oracle Connection Manager or by an external network device. Identify the method used to enforce address restriction (interview or System Security Plan review). If enforced by the database listener, then review the SQLNET.ORA file located in the ORACLE_HOME/network/admin directory (note: this assumes that a single sqlnet.ora file, in the default location, is in use; please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files) or the directory indicated by the TNS_ADMIN environment variable or registry setting. If the following entries do not exist, then restriction by IP address is not configured and is a finding. tcp.validnode_checking=YES tcp.invited_nodes=(IP1, IP2, IP3) If enforced by an Oracle Connection Manager, then review the CMAN.ORA file for the Connection Manager (located in the TNS_ADMIN or ORACLE_HOME/network/admin directory for the connection manager). If a RULE entry allows all addresses ("/32") or does not match the address range specified in the System Security Plan, this is a finding. (rule=(src=[IP]/27)(dst=[IP])(srv=*)(act=accept)) Note: an IP address with a "/" indicates acceptance by subnet mask where the number after the "/" is the left most number of bits in the address that must match for the rule to apply. If this rule is database-specific, then determine if the SERVICE_NAMES parameter is set: From SQL*PLUS: select value from v$parameter where name = 'service_names'; If SERVICE_NAMES is set in the initialization file for the database instance, use (srv=[service name]), else, use (srv=*) if not set or rule applies to all databases on the DBMS server. If network access restriction is performed by an external device, validate ACLs are in place to prohibit unauthorized access to the DBMS. To do this, find the IP address of the database server (destination address) and source address (authorized IPs) in the System Security Plan. Confirm only authorized IPs from the System Security Plan are allowed access to the DBMS.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219868`

### Rule: Changes to configuration options must be audited.

**Rule ID:** `SV-219868r903020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When standard auditing is in use, the AUDIT_SYS_OPERATIONS parameter is used to enable auditing of actions taken by the user SYS. The SYS user account is a shared account by definition and holds all privileges in the Oracle database. It is the account accessed by users connecting to the database with SYSDBA or SYSOPER privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Unified or mixed auditing, from SQL*Plus: select count(*) from audit_unified_enabled_policies where entity_name = 'SYS'; If less than one row is returned, this is a finding. For Standard auditing, from SQL*Plus: select value from v$parameter where name = 'audit_sys_operations'; If the value returned is FALSE, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219871`

### Rule: Changes to DBMS security labels must be audited.

**Rule ID:** `SV-219871r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some DBMS systems provide the feature to assign security labels to data elements. If labeling is required, implementation options include the Oracle Label Security package, or a third-party product, or custom-developed functionality. The confidentiality and integrity of the data depends upon the security label assignment where this feature is in use. Changes to security label assignment may indicate suspicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no data has been identified as being sensitive or classified in the system documentation, this is not a finding. If security labeling is not required, this is not a finding. If Standard Auditing is used, run the SQL query: select * from dba_sa_audit_options; If no records are returned or if output from the SQL statement above does not show classification labels being audited as required in the System Security Plan, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data including changes to security label assignment, enter the following SQL*Plus command: SELECT 'Changes to security label assignment is not being audited. ' FROM dual WHERE (SELECT Count(*) FROM (select policy_name , audit_option from audit_unified_policies WHERE audit_option = 'ALL' AND audit_option_type = 'OLS ACTION' AND policy_name in (select policy_name from audit_unified_enabled_policies where user_name='ALL USERS'))) = 0 OR (SELECT value FROM v$option WHERE parameter = 'Unified Auditing') != 'TRUE'; If Oracle returns "no rows selected", this is not a finding. To confirm that Oracle audit is capturing sufficient information to establish that changes to classification labels are being audited, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If no ACTION#, or the wrong value, is returned for the auditable actions, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219872`

### Rule: Remote database or other external access must use fully-qualified names.

**Rule ID:** `SV-219872r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle GLOBAL_NAMES parameter is used to set the requirement for database link names to be the same name as the remote database whose connection they define. By using the same name for both, ambiguity is avoided and unauthorized or unintended connections to remote databases are less likely.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = 'global_names'; If the value returned is FALSE, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219873`

### Rule: The /diag subdirectory under the directory assigned to the DIAGNOSTIC_DEST parameter must be protected from unauthorized access.

**Rule ID:** `SV-219873r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion><DIAGNOSTIC_DEST>/diag indicates the directory where trace, alert, core and incident directories and files are located. The files may contain sensitive data or information that could prove useful to potential attackers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name='diagnostic_dest'; On UNIX Systems: ls -ld [pathname]/diag Substitute [pathname] with the directory path listed from the above SQL command, and append "/diag" to it, as shown. If permissions are granted for world access, this is a Finding. If any groups that include members other than the Oracle process and software owner accounts, DBAs, auditors, or backup accounts are listed, this is a Finding. On Windows Systems (From Windows Explorer): Browse to the \diag directory under the directory specified. Select and right-click on the directory, select Properties, select the Security tab. If permissions are granted to everyone, this is a Finding. If any account other than the Oracle process and software owner accounts, Administrators, DBAs, System group or developers authorized to write and debug applications on this database are listed, this is a Finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219874`

### Rule: Remote administration must be disabled for the Oracle connection manager.

**Rule ID:** `SV-219874r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote administration provides a potential opportunity for malicious users to make unauthorized changes to the Connection Manager configuration or interrupt its service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the cman.ora file in the ORACLE_HOME/network/admin directory. If the file does not exist, the database is not accessed via Oracle Connection Manager and this check is not a finding. If the entry and value for REMOTE_ADMIN is not listed or is not set to a value of NO (REMOTE_ADMIN = NO), this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-219875`

### Rule: Network client connections must be restricted to supported versions.

**Rule ID:** `SV-219875r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsupported Oracle network client installations may introduce vulnerabilities to the database. Restriction to use of supported versions helps to protect the database and helps to enforce newer, more robust security controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The SQLNET.ALLOWED_LOGON_VERSION parameter is deprecated in Oracle Database 12c. This parameter has been replaced with two new Oracle Net Services parameters: SQLNET.ALLOWED_LOGON_VERSION_SERVER SQLNET.ALLOWED_LOGON_VERSION_CLIENT View the SQLNET.ORA file in the ORACLE_HOME/network/admin directory or the directory specified in the TNS_ADMIN environment variable. (Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.) Locate the following entries: SQLNET.ALLOWED_LOGON_VERSION_SERVER = 12 SQLNET.ALLOWED_LOGON_VERSION_CLIENT = 12 If the parameters do not exist, this is a finding. If the parameters are not set to a value of 12 or 12a, this is a finding. Note: Attempting to connect with a client version lower than specified in these parameters may result in a misleading error: ORA-01017: invalid username/password: logon denied

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-220263`

### Rule: The DBMS, when using PKI-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-220263r879613_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and non-repudiation gained through PKI because the attacker can use the private key to digitally sign documents and can pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys. All access to the private key of the DBMS must be restricted to authorized and authenticated users. If unauthorized users have access to the DBMS’s private key, an attacker could gain access to the primary key and use it to impersonate the database on the network. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including 'SSL', such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS configuration to determine whether appropriate access controls exist to protect the DBMS’s private key. If strong access controls do not exist to enforce authorized access to the private key, this is a finding. - - - - - The database supports authentication by using digital certificates over TLS in addition to the native encryption and data integrity capabilities of these protocols. An Oracle Wallet is a container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by TLS. In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates, with the exception of Diffie-Hellman. If the $ORACLE_HOME/network/admin/sqlnet.ora contains the following entries, TLS is installed. (Note: This assumes that a single sqlnet.ora file, in the default location, is in use. Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.) WALLET_LOCATION = (SOURCE= (METHOD = FILE) (METHOD_DATA = DIRECTORY=/wallet) SSL_CIPHER_SUITES=(SSL_cipher_suiteExample) SSL_VERSION = 1.2 SSL_CLIENT_AUTHENTICATION=FALSE/TRUE

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-220264`

### Rule: The DBMS must limit the number of concurrent sessions for each system account to an organization-defined number of sessions.

**Rule ID:** `SV-220264r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions utilizing an application. Limiting the number of allowed users, and sessions per user, is helpful in limiting risks related to Denial of Service attacks. This requirement addresses concurrent session control for a single information system account and does not address concurrent sessions by a single user via multiple system accounts. Unlimited concurrent connections to the DBMS could allow a successful Denial of Service (DoS) attack by exhausting connection resources. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to take into account the work requirements of the various types of user. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Retrieve the settings for concurrent sessions for each profile with the query: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'SESSIONS_PER_USER'; If the DBMS settings for concurrent sessions for each profile are greater than the site-specific maximum number of sessions, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-220265`

### Rule: The system must employ automated mechanisms for supporting Oracle user account management.

**Rule ID:** `SV-220265r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in non-centralized account stores, such as multiple servers. Enterprise environments make application user account management challenging and complex. A user management process requiring administrators to manually address account management functions adds risk of potential oversight. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements. Databases can have large numbers of users in disparate locations and job functions. Automatic account management can help mitigate the risk of human error found in manually managing database access. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. If an Oracle feature/product, an OS feature, a third-party product, or custom code is used to automate account management, this is not a finding. Determine what is the site-defined definition of an acceptably small level of manual account-management activity. If the site has established the definition, documented it, and obtained ISSO-ISSM-AO approval, use that definition. If not, use the following rule of thumb as the definition: No more than 12 such accounts exist or are expected to exist; no more than 100 manual account-management actions (account creation, modification, locking, unlocking, removal, etc.) are expected to occur in the course of a year. If the amount of account management activity is small, as defined in the preceding paragraph, this is not a finding. Otherwise, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-220266`

### Rule: The DBMS must enforce approved authorizations for logical access to the system in accordance with applicable policy.

**Rule ID:** `SV-220266r917644_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Strong access controls are critical to securing application data. Access control policies (e.g., identity-based policies, role-based policies, attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, cryptography) must be employed by applications, when applicable, to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, domains) in the information system. Consideration should be given to the implementation of an audited, explicit override of automated mechanisms in the event of emergencies or other serious events. If the DBMS does not follow applicable policy when approving access it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and may be in conflict with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine whether users are restricted from accessing objects and data they are not authorized to access. If appropriate access controls are not implemented to restrict access to authorized users and to restrict the access of those users to objects and data they are authorized to see, this is a finding. The easiest way to isolate access is by using the Oracle Database Vault. To check to see if the Oracle Database Vault is installed, issue the following query: SQL> SELECT * FROM V$OPTION WHERE PARAMETER = 'Oracle Database Vault'; If Oracle Database Vault is installed, review its settings for appropriateness and completeness of the access it permits and denies to each type of user. If appropriate and complete, this is not a finding. If Oracle Database Vault is not installed, review the roles and profiles in the database and the assignment of users to these for appropriateness and completeness of the access permitted and denied each type of user. If appropriate and complete, this is not a finding. If the access permitted and denied each type of user is inappropriate or incomplete, this is a finding. Following are code examples for reviewing roles, profiles, etc. Find out what role the users have: select * from dba_role_privs where granted_role = '<role>' List all roles given to a user: select * from dba_role_privs where grantee = '<username>'; List all roles for all users: column grantee format a32 column granted_role format a32 break on grantee select grantee, granted_role from dba_role_privs; Use the following query to list all privileges given to a user: select lpad(' ', 2*level) || granted_role "User roles and privileges" from ( /* THE USERS */ select null grantee, username granted_role from dba_users where username like upper('<enter_username>') /* THE ROLES TO ROLES RELATIONS */ union select grantee, granted_role from dba_role_privs /* THE ROLES TO PRIVILEGE RELATIONS */ union select grantee, privilege from dba_sys_privs ) start with grantee is null connect by grantee = prior granted_role; List which tables a certain role gives SELECT access to using the query: select * from role_tab_privs where role='<role>' and privilege = 'SELECT'; List all tables a user can SELECT from using the query: select * from dba_tab_privs where GRANTEE ='<username>' and privilege = 'SELECT'; List all users who can SELECT on a particular table (either through being given a relevant role or through a direct grant - e.g., grant select on a table to Joe). The result of this query should also show through which role the user has this access or whether it was a direct grant. select Grantee,'Granted Through Role' as Grant_Type, role, table_name from role_tab_privs rtp, dba_role_privs drp where rtp.role = drp.granted_role and table_name = '<TABLENAME>' union select Grantee, 'Direct Grant' as Grant_type, null as role, table_name from dba_tab_privs where table_name = '<TABLENAME>';

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-220267`

### Rule: The DBMS must provide audit record generation capability for organization-defined auditable events within the database.

**Rule ID:** `SV-220267r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records can be generated from various components within the information system. (e.g., network interface, hard disk, modem, etc.). From an application perspective, certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (i.e., auditable events, timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked). Organizations define which application components shall provide auditable events. The DBMS must provide auditing for the list of events defined by the organization or risk negatively impacting forensic investigations into malicious behavior in the information system. Audit records can be generated from various components within the information system, such as network interfaces, hard disks, modems, etc. From an application perspective, certain specific application functionalities may be audited, as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (i.e., auditable events, timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked). Organizations may define the organizational personnel accountable for determining which application components shall provide auditable events. Auditing provides accountability for changes made to the DBMS configuration or its objects and data. It provides a means to discover suspicious activity and unauthorized changes. Without auditing, a compromise may go undetected and without a means to determine accountability. The Department of Defense has established the following as the minimum set of auditable events. Most can be audited via Oracle settings; some - marked here with an asterisk - cannot, and may require OS settings. - Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g. classification levels). - Successful and unsuccessful logon attempts, privileged activities or other system level access - Starting and ending time for user access to the system, concurrent logons from different workstations. - Successful and unsuccessful accesses to objects. - All program initiations. - *All direct access to the information system. - All account creations, modifications, disabling, and terminations. - *All kernel module loads, unloads, and restarts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value 'NONE', this is a finding. To confirm that Oracle audit is capturing information on the required events, review the contents of the SYS.AUD$ table or the audit file, whichever is in use. If auditable events are not listed, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing information on the required events, review the contents of the SYS.UNIFIED_AUDIT_TRAIL view. If auditable events are not listed, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-220268`

### Rule: The DBMS must allow designated organizational personnel to select which auditable events are to be audited by the database.

**Rule ID:** `SV-220268r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (i.e., auditable events, timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked). If the list of auditable events is not configurable, events that should be caught by auditing may be missed. This may allow malicious activity to be overlooked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and documentation to determine whether designated personnel are able to select which auditable events are being audited. If designated personnel are not able to configure auditable events, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-220269`

### Rule: The DBMS must generate audit records for the DoD-selected list of auditable events, to the extent such information is available.

**Rule ID:** `SV-220269r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records can be generated from various components within the information system, such as network interfaces, hard disks, modems, etc. From an application perspective, certain specific application functionalities may be audited, as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (i.e., auditable events, timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked). Organizations may define the organizational personnel accountable for determining which application components shall provide auditable events. Auditing provides accountability for changes made to the DBMS configuration or its objects and data. It provides a means to discover suspicious activity and unauthorized changes. Without auditing, a compromise may go undetected and without a means to determine accountability. The Department of Defense has established the following as the minimum set of auditable events. Most can be audited via Oracle settings; some - marked here with an asterisk - cannot, and may require OS settings. - Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g. classification levels). - Successful and unsuccessful logon attempts, privileged activities or other system level access - Starting and ending time for user access to the system, concurrent logons from different workstations. - Successful and unsuccessful accesses to objects. - All program initiations. - *All direct access to the information system. - All account creations, modifications, disabling, and terminations. - *All kernel module loads, unloads, and restarts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine if auditing is being performed on the events on the DoD-selected list of auditable events that lie within the scope of Oracle audit capabilities: - Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels). - Successful and unsuccessful logon attempts, privileged activities or other system-level access - Starting and ending time for user access to the system, concurrent logons from different workstations. - Successful and unsuccessful accesses to objects. - All program initiations. - All account creations, modifications, disabling, and terminations. If auditing is not being performed for any of these events, this is a finding. Notes on Oracle audit capabilities follow. Unified Audit supports named audit policies, which are defined using the CREATE AUDIT POLICY statement. A policy specifies the actions that should be audited and the objects to which it should apply. If no specific objects are included in the policy definition, it applies to all objects. A named policy is enabled using the AUDIT POLICY statement. It can be enabled for all users, for specific users only, or for all except a specified list of users. The policy can audit successful actions, unsuccessful actions, or both. Verifying existing audit policy: existing Unified Audit policies are listed in the view AUDIT_UNIFIED_POLICIES. The AUDIT_OPTION column contains one of the actions specified in a CREATE AUDIT POLICY statement. The AUDIT_OPTION_TYPE column contains 'STANDARD ACTION' for a policy that applies to all objects or 'OBJECT ACTION' for a policy that audits actions on a specific object. select POLICY_NAME from SYS.AUDIT_UNIFIED_POLICIES where AUDIT_OPTION='GRANT' and AUDIT_OPTION_TYPE='STANDARD ACTION'; To find policies that audit privilege grants on specific objects: select POLICY_NAME,OBJECT_SCHEMA,OBJECT_NAME from SYS.AUDIT_UNIFIED_POLICIES where AUDIT_OPTION='GRANT' and AUDIT_OPTION_TYPE='OBJECT ACTION'; The view AUDIT_UNIFIED_ENABLED_POLICIES shows which Unified Audit policies are enabled. The ENABLED_OPT and USER_NAME columns show the users for whom the policy is enabled or 'ALL USERS'. The SUCCESS and FAILURE columns indicate if the policy is enabled for successful or unsuccessful actions, respectively. select POLICY_NAME,ENABLED_OPT,USER_NAME,SUCCESS,FAILURE from SYS.AUDIT_UNIFIED_ENABLED_POLICIES where POLICY_NAME='POLICY1';

## Group: SRG-APP-000095-DB-000039

**Group ID:** `V-220270`

### Rule: The DBMS must produce audit records containing sufficient information to establish what type of events occurred.

**Rule ID:** `SV-220270r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes: timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly what actions were performed. This requires specific information regarding the event type an audit record is referring to. If event type information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value "NONE", this is a finding. To confirm that Oracle audit is capturing sufficient information to establish the identity of the user/subject or process, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If no ACTION#, or the wrong value, is returned for the auditable actions just performed, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing sufficient information to establish the identity of the user/subject or process, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If no ACTION_NAME, or the wrong value, is returned for the auditable actions just performed, this is a finding.

## Group: SRG-APP-000096-DB-000040

**Group ID:** `V-220271`

### Rule: The DBMS must produce audit records containing sufficient information to establish when (date and time) the events occurred.

**Rule ID:** `SV-220271r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes: timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. Database software is capable of a range of actions on data stored within the database. It's important, for accurate forensic analysis, to know exactly when specific actions were performed. This requires the date and time an audit record is referring to. If date and time information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value 'NONE', this is a finding. To confirm that Oracle audit is capturing sufficient information to establish when events occurred, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If no timestamp, or the wrong value, is returned for the auditable actions just performed, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing sufficient information to establish when events occurred, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If no timestamp, or the wrong value, is returned for the auditable actions just performed, this is a finding.

## Group: SRG-APP-000097-DB-000041

**Group ID:** `V-220272`

### Rule: The DBMS must produce audit records containing sufficient information to establish where the events occurred.

**Rule ID:** `SV-220272r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes: timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. Without sufficient information establishing where the audit events occurred, investigation into the cause of events is severely hindered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value 'NONE', this is a finding. To confirm that Oracle audit is capturing sufficient information to establish where events occurred, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If no DB ID or Object Creator (standard audit) or Object Schema (unified audit) or Object Name, or the wrong values, are returned for the auditable actions just performed, this is a finding. If no DB ID or OBJ$CREATOR or the wrong values, are returned for the auditable actions just performed, this is a finding. If correct values for USERHOST and TERMINAL are not returned when applicable, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing sufficient information to establish where events occurred, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If no DBID or OBJECT_SCHEMA or OBJECT_NAME, or the wrong values, are returned for the auditable actions just performed, this is a finding. If correct values for USERHOST and TERMINAL are not returned when applicable, this is a finding. For Unified Auditing, the following view can be useful for reviewing its output: CREATE OR REPLACE FORCE VIEW SYS.UNIFIED_AUDIT_TRAIL ( AUDIT_TYPE, SESSIONID, PROXY_SESSIONID, OS_USERNAME, USERHOST, TERMINAL, INSTANCE_ID, DBID, AUTHENTICATION_TYPE, DBUSERNAME, DBPROXY_USERNAME, EXTERNAL_USERID, GLOBAL_USERID, CLIENT_PROGRAM_NAME, DBLINK_INFO, XS_USER_NAME, XS_SESSIONID, ENTRY_ID, STATEMENT_ID, EVENT_TIMESTAMP, ACTION_NAME, RETURN_CODE, OS_PROCESS, TRANSACTION_ID, SCN, EXECUTION_ID, OBJECT_SCHEMA, OBJECT_NAME, SQL_TEXT, SQL_BINDS, APPLICATION_CONTEXTS, CLIENT_IDENTIFIER, NEW_SCHEMA, NEW_NAME, OBJECT_EDITION, SYSTEM_PRIVILEGE_USED, SYSTEM_PRIVILEGE, AUDIT_OPTION, OBJECT_PRIVILEGES, ROLE, TARGET_USER, EXCLUDED_USER, EXCLUDED_SCHEMA, EXCLUDED_OBJECT, ADDITIONAL_INFO, UNIFIED_AUDIT_POLICIES, FGA_POLICY_NAME, XS_INACTIVITY_TIMEOUT, XS_ENTITY_TYPE, XS_TARGET_PRINCIPAL_NAME, XS_PROXY_USER_NAME, XS_DATASEC_POLICY_NAME, XS_SCHEMA_NAME, XS_CALLBACK_EVENT_TYPE, XS_PACKAGE_NAME, XS_PROCEDURE_NAME, XS_ENABLED_ROLE, XS_COOKIE, XS_NS_NAME, XS_NS_ATTRIBUTE, XS_NS_ATTRIBUTE_OLD_VAL, XS_NS_ATTRIBUTE_NEW_VAL, DV_ACTION_CODE, DV_ACTION_NAME, DV_EXTENDED_ACTION_CODE, DV_GRANTEE, DV_RETURN_CODE, DV_ACTION_OBJECT_NAME, DV_RULE_SET_NAME, DV_COMMENT, DV_FACTOR_CONTEXT, DV_OBJECT_STATUS, OLS_POLICY_NAME, OLS_GRANTEE, OLS_MAX_READ_LABEL, OLS_MAX_WRITE_LABEL, OLS_MIN_WRITE_LABEL, OLS_PRIVILEGES_GRANTED, OLS_PROGRAM_UNIT_NAME, OLS_PRIVILEGES_USED, OLS_STRING_LABEL, OLS_LABEL_COMPONENT_TYPE, OLS_LABEL_COMPONENT_NAME, OLS_PARENT_GROUP_NAME, OLS_OLD_VALUE, OLS_NEW_VALUE, RMAN_SESSION_RECID, RMAN_SESSION_STAMP, RMAN_OPERATION, RMAN_OBJECT_TYPE, RMAN_DEVICE_TYPE, DP_TEXT_PARAMETERS1, DP_BOOLEAN_PARAMETERS1, DIRECT_PATH_NUM_COLUMNS_LOADED ) AS SELECT act.component, sessionid, proxy_sessionid, os_user, host_name, terminal, instance_id, dbid, authentication_type, userid, proxy_userid, external_userid, global_userid, client_program_name, dblink_info, xs_user_name, xs_sessionid, entry_id, statement_id, CAST (event_timestamp AS TIMESTAMP WITH LOCAL TIME ZONE), act.name, return_code, os_process, transaction_id, scn, execution_id, obj_owner, obj_name, sql_text, sql_binds, application_contexts, client_identifier, new_owner, new_name, object_edition, system_privilege_used, spx.name, aom.name, object_privileges, role, target_user, excluded_user, excluded_schema, excluded_object, additional_info, unified_audit_policies, fga_policy_name, xs_inactivity_timeout, xs_entity_type, xs_target_principal_name, xs_proxy_user_name, xs_datasec_policy_name, xs_schema_name, xs_callback_event_type, xs_package_name, xs_procedure_name, xs_enabled_role, xs_cookie, xs_ns_name, xs_ns_attribute, xs_ns_attribute_old_val, xs_ns_attribute_new_val, dv_action_code, dv_action_name, dv_extended_action_code, dv_grantee, dv_return_code, dv_action_object_name, dv_rule_set_name, dv_comment, dv_factor_context, dv_object_status, ols_policy_name, ols_grantee, ols_max_read_label, ols_max_write_label, ols_min_write_label, ols_privileges_granted, ols_program_unit_name, ols_privileges_used, ols_string_label, ols_label_component_type, ols_label_component_name, ols_parent_group_name, ols_old_value, ols_new_value, rman_session_recid, rman_session_stamp, rman_operation, rman_object_type, rman_device_type, dp_text_parameters1, dp_boolean_parameters1, direct_path_num_columns_loaded FROM gv$unified_audit_trail uview, all_unified_audit_actions act, system_privilege_map spx, stmt_audit_option_map aom WHERE uview.action = act.action(+) AND -uview.system_privilege = spx.privilege(+) AND uview.audit_option = aom.option#(+) AND uview.audit_type = act.TYPE;

## Group: SRG-APP-000098-DB-000042

**Group ID:** `V-220273`

### Rule: The DBMS must produce audit records containing sufficient information to establish the sources (origins) of the events.

**Rule ID:** `SV-220273r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control, includes, but is not limited to: timestamps, source and destination IP addresses, user/process identifiers, event descriptions, application specific events, success/fail indications, file names involved, access control or flow control rules invoked. Without information establishing the source of activity, the value of audit records from a forensics perspective is questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value 'NONE', this is a finding. To confirm that Oracle audit is capturing sufficient information to establish the source of events, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If correct values for User ID, User Host, and Terminal are not returned when applicable, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing sufficient information to establish the source of events, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If correct values for DBUSERNAME, USERHOST, and TERMINAL are not returned when applicable, this is a finding.

## Group: SRG-APP-000099-DB-000043

**Group ID:** `V-220274`

### Rule: The DBMS must produce audit records containing sufficient information to establish the outcome (success or failure) of the events.

**Rule ID:** `SV-220274r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes, but is not limited to: timestamps, source and destination IP addresses, user/process identifiers, event descriptions, application specific events, success/fail indications, file names involved, access control, or flow control rules invoked. Success and failure indicators ascertain the outcome of a particular event. As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response. Without knowing the outcome of audit events, it is very difficult to accurately recreate the series of events during forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value 'NONE', this is a finding. To confirm that Oracle audit is capturing sufficient information to establish outcomes, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If no return code or other outcome information is returned for the auditable action just performed, this is a finding. If error is indicated for the successful action, this is a finding. If no error is indicated for the unsuccessful action, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding To confirm that Oracle audit is capturing sufficient information to establish outcomes, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view. If no return code or other outcome information is returned for the auditable action just performed, this is a finding. If error is indicated for the successful action, this is a finding. If no error is indicated for the unsuccessful action, this is a finding.

## Group: SRG-APP-000100-DB-000201

**Group ID:** `V-220275`

### Rule: The DBMS must produce audit records containing sufficient information to establish the identity of any user/subject or process associated with the event.

**Rule ID:** `SV-220275r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes: timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. Database software is capable of a range of actions on data stored within the database. It is important, for accurate forensic analysis, to know exactly who performed a given action. If user identification information is not recorded and stored with the audit record, the record itself is of very limited use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns a value something other than "TRUE", this is a finding To confirm that Oracle audit is capturing sufficient information to establish the identity of the user/subject or process, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.AUD$ table or the audit file, whichever is in use. If no user ID, or the wrong value, is returned for the auditable actions just performed, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns the value "TRUE", this is not a finding. To confirm that Oracle audit is capturing sufficient information to establish the identity of the user/subject or process, perform a successful auditable action and an auditable action that results in an SQL error, and then view the results in the SYS.UNIFIED_AUDIT_TRAIL view, whichever is in use. If no user ID, or the wrong value, is returned for the auditable actions just performed, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-220276`

### Rule: The DBMS must include organization-defined additional, more detailed information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-220276r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes: timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. In addition, the application must have the capability to include organization-defined additional, more detailed information in the audit records for audit events. These events may be identified by type, location, or subject. An example of detailed information the organization may require in audit records is full-text recording of privileged commands or the individual identities of shared account users. Some organizations may determine that more detailed information is required for specific database event types. If this information is not available, it could negatively impact forensic investigations into user actions or other malicious events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify, using vendor and system documentation if necessary, that the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns a value something other than "TRUE", this is a finding Compare the organization-defined auditable events with the Oracle documentation to determine whether standard auditing covers all the requirements. If it does, this is not a finding. Compare those organization-defined auditable events that are not covered by the standard auditing, with the existing Fine-Grained Auditing (FGA) specifications returned by the following query: SELECT * FROM SYS.DBA_FGA_AUDIT_TRAIL; If any such auditable event is not covered by the existing FGA specifications, this is a finding. If Unified Auditing is used: To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns the value "TRUE", this is not a finding. Compare the organization-defined auditable events with the Oracle documentation to determine whether standard auditing covers all the requirements. If it does, this is not a finding. Compare those organization-defined auditable events that are not covered by unified auditing with the existing Fine-Grained Auditing (FGA) specifications returned by the following query: SELECT * FROM SYS.UNIFIED_AUDIT_TRAIL WHERE AUDIT_TYPE = 'FineGrainedAudit'; If any such auditable event is not covered by the existing FGA specifications, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-220277`

### Rule: The system must protect audit information from any type of unauthorized access.

**Rule ID:** `SV-220277r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records must not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review locations of audit logs, both internal to the database and database audit logs located at the operating system-level. Verify there are appropriate controls and permissions to protect the audit information from unauthorized access. If appropriate controls and permissions do not exist, this is a finding. - - - - - If Standard Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUD$ table. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted OWNER VARCHAR2(30) NOT NULL Owner of the object TABLE_NAME VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where table_name = 'AUD$'; If Unified Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUDSYS tables. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted OWNER VARCHAR2(30) NOT NULL Owner of the object TABLE_NAME VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where owner='AUDSYS';

## Group: SRG-APP-000119-DB-000060

**Group ID:** `V-220278`

### Rule: The system must protect audit information from unauthorized modification.

**Rule ID:** `SV-220278r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review locations of audit logs, both internal to the database and database audit logs located at the operating system-level. Verify there are appropriate controls and permissions to protect the audit information from unauthorized modification. If appropriate controls and permissions do not exist, this is a finding. - - - - - If Standard Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUD$ table. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted VARCHAR2(30) NOT NULL Owner of the object TABLE_NA VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where table_name = 'AUD$'; If Unified Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUDSYS tables. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted OWNER VARCHAR2(30) NOT NULL Owner of the object TABLE_NAME VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where owner='AUDSYS';

## Group: SRG-APP-000120-DB-000061

**Group ID:** `V-220279`

### Rule: The system must protect audit information from unauthorized deletion.

**Rule ID:** `SV-220279r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files enjoy the proper file system permissions utilizing file system protections; restricting access; and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review locations of audit logs, both internal to the database and database audit logs located at the operating system-level. Verify there are appropriate controls and permissions to protect the audit information from unauthorized deletion. If appropriate controls and permissions do not exist, this is a finding. - - - - - If Standard Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUD$ table. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted OWNER VARCHAR2(30) NOT NULL Owner of the object TABLE_NAME VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where table_name = 'AUD$'; If Unified Auditing is used: DBA_TAB_PRIVS describes all object grants in the database. Check to see who has permissions on the AUDSYS tables. Related View DBA_TAB_PRIVS describes the object grants for which the current user is the object owner, grantor, or grantee. Column Datatype NULL Description GRANTEE VARCHAR2(30) NOT NULL Name of the user to whom access was granted OWNER VARCHAR2(30) NOT NULL Owner of the object TABLE_NAME VARCHAR2(30) NOT NULL Name of the object GRANTOR VARCHAR2(30) NOT NULL Name of the user who performed the grant PRIVILEGE VARCHAR2(40) NOT NULL Privilege on the object GRANTABLE VARCHAR2(3) Indicates whether the privilege was granted with the GRANT OPTION (YES) or not (NO) HIERARCHY VARCHAR2(3) Indicates whether the privilege was granted with the HIERARCHY OPTION (YES) or not (NO) COMMON VARCHAR2(3) TYPE VARCHAR2(24) sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where owner='AUDSYS';

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-220280`

### Rule: The system must protect audit tools from unauthorized access.

**Rule ID:** `SV-220280r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. These tools may include the DBMS itself or tools external to the database. If appropriate permissions and access controls to prevent unauthorized access are not applied to these tools, this is a finding.

## Group: SRG-APP-000122-DB-000203

**Group ID:** `V-220281`

### Rule: The system must protect audit tools from unauthorized modification.

**Rule ID:** `SV-220281r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. If the tools are compromised it could provide attackers with the capability to manipulate log data. It is, therefore, imperative that audit tools be controlled and protected from unauthorized modification. Audit tools include, but are not limited to, OS provided audit tools, vendor provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. These tools may include the DBMS itself or tools external to the database. If appropriate permissions and access controls are not applied to prevent unauthorized modification of these tools, this is a finding.

## Group: SRG-APP-000123-DB-000204

**Group ID:** `V-220282`

### Rule: The system must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-220282r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. These tools may include the DBMS itself or tools external to the database. If appropriate permissions and access controls are not applied to prevent unauthorized deletion of these tools, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-220283`

### Rule: Database objects must be owned by accounts authorized for ownership.

**Rule ID:** `SV-220283r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object including the privilege to assign access to the owned objects to other subjects. Unmanaged or uncontrolled ownership of objects can lead to unauthorized object grants and alterations, and unauthorized modifications to data. If critical tables or other objects rely on unauthorized owner accounts, these objects can be lost when an account is removed. It may be the case that there are accounts that are authorized to own synonyms, but no other objects. If this is so, it should be documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify accounts authorized to own database objects. Review accounts in DBMS that own objects. If any database objects are found to be owned by users not authorized to own database objects, this is a finding. - - - - - Query the object DBA_OBJECTS to show the users who own objects in the database. The query below will return all of the users who own objects. sqlplus connect as sysdba SQL>select owner, object_type, count(*) from dba_objects group by owner, object_type order by owner, object_type; If these owners are not authorized owners, select all of the objects these owners have generated and decide who they should belong to. To make a list of all of the objects, the unauthorized owner has to perform the following query. SQL>select * from dba_objects where owner =&unauthorized_owner;

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-220284`

### Rule: Default demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-220284r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Oracle is hosted on a server that does not support production systems, and is designated for the deployment of samples and demonstrations, this is not applicable (NA). Review documentation and websites from Oracle and any other relevant vendors for vendor-provided demonstration or sample databases, database applications, schemas, objects, and files. Review the Oracle DBMS to determine if any of the demonstration and sample databases, schemas, database applications, or files are installed in the database or are included with the DBMS application. If any are present in the database or are included with the DBMS application, this is a finding. The Oracle Default Sample Schema User Accounts are: BI Owns the Business Intelligence schema included in the Oracle Sample Schemas. HR Manages the Human Resources schema. Schema stores information about the employees and the facilities of the company. OE Manages the Order Entry schema. Schema stores product inventories and sales of the company's products through various channels. PM Manages the Product Media schema. Schema contains descriptions and detailed information about each product sold by the company. IX Manages the Information Exchange schema. Schema manages shipping through business-to-business (B2B) applications database. SH Manages the Sales schema. Schema stores statistics to facilitate business decisions. SCOTT A demonstration account with a simple schema. Connect to Oracle as SYSDBA; run the following SQL to check for presence of Oracle Default Sample Schema User Accounts: select distinct(username) from dba_users where username in ('BI','HR','OE','PM','IX','SH','SCOTT'); If any of the users listed above is returned it means that there are demo programs installed, so this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-220285`

### Rule: Unused database components, DBMS software, and database objects must be removed.

**Rule ID:** `SV-220285r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the DBMS and host system. Unused and unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run this query to produce a list of components and features installed with the database: SELECT comp_id, comp_name, version, status from dba_registry WHERE comp_id not in ('CATALOG','CATPROC','XDB') AND status <> 'OPTION OFF'; Review the list. If unused components are installed and are not documented and authorized, this is a finding. Starting with releases 11.1.0.7.x and above, all products are installed by default and the option to customize the product/component selection is no longer possible with the exception of those listed here: Oracle JVM, Oracle Text, Oracle Multimedia, Oracle OLAP, Oracle Spatial, Oracle Label Security, Oracle Application Express, Oracle Database Vault

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-220286`

### Rule: Unused database components that are integrated in the DBMS and cannot be uninstalled must be disabled.

**Rule ID:** `SV-220286r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run this query to check to see what integrated components are installed in the database: SELECT parameter, value from v$option where parameter in ( 'Data Mining', 'Oracle Database Extensions for .NET', 'OLAP', 'Partitioning', 'Real Application Testing' ); This will return all of the relevant database options and their status. TRUE means that the option is installed. If the option is not installed, the option will be set to FALSE. Review the options and check the system documentation to see what is required. If all listed components are authorized to be in use, this is not a finding. If any unused components or features are listed by the query as TRUE, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-220287`

### Rule: Use of external executables must be authorized.

**Rule ID:** `SV-220287r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. DBMSs may spawn additional external processes to execute procedures that are defined in the DBMS, but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the database for definitions of application executable objects stored external to the database. Determine if there are methods to disable use or access, or to remove definitions for external executable objects. Verify any application executable objects listed are authorized by the ISSO. To check for external procedures, execute the following query, which will provide the libraries containing external procedures, the owners of those libraries, users that have been granted access to those libraries, and the privileges they have been granted. If there are owners other than the owners Oracle provides, then there might be executable objects stored either in the database or external to the database that are called by objects in the database. (connect as sysdba) set linesize 130 column library_name format a25 column name format a15 column owner format a15 column grantee format a15 column privilege format a15 select library_name,owner, '' grantee, '' privilege from dba_libraries where file_spec is not null and owner not in ('SYS', 'ORDSYS') minus ( select library_name,o.name owner, '' grantee, '' privilege from dba_libraries l, sys.user$ o, sys.user$ ge, sys.obj$ obj, sys.objauth$ oa where l.owner=o.name and obj.owner#=o.user# and obj.name=l.library_name and oa.obj#=obj.obj# and ge.user#=oa.grantee# and l.file_spec is not null ) union all select library_name,o.name owner, --obj.obj#,oa.privilege#, ge.name grantee, tpm.name privilege from dba_libraries l, sys.user$ o, sys.user$ ge, sys.obj$ obj, sys.objauth$ oa, sys.table_privilege_map tpm where l.owner=o.name and obj.owner#=o.user# and obj.name=l.library_name and oa.obj#=obj.obj# and ge.user#=oa.grantee# and tpm.privilege=oa.privilege# and l.file_spec is not null / If any owners are returned other than those Oracle provides, ensure those owners are authorized to access those libraries. If there are users that have been granted access to libraries that are not authorized, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-220288`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-220288r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle external procedure capability provides use of the Oracle process account outside the operation of the DBMS process. You can use it to submit and execute applications stored externally from the database under operating system controls. The external procedure process is the subject of frequent and successful attacks as it allows unauthenticated use of the Oracle process account on the operating system. As of Oracle version 11.1, the external procedure agent may be run directly from the database and not require use of the Oracle listener. This reduces the risk of unauthorized access to the procedure from outside of the database process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the System Security Plan to determine if the use of the external procedure agent is authorized. Review the ORACLE_HOME/bin directory or search the ORACLE_BASE path for the executable extproc (UNIX) or extproc.exe (Windows). If external procedure agent is not authorized for use in the System Security Plan and the executable file does not exist or is restricted, this is not a finding. If external procedure agent is not authorized for use in the System Security Plan and the executable file exists and is not restricted, this is a finding. If use of the external procedure agent is authorized, ensure extproc is restricted to execution of authorized applications. External jobs are run using the account nobody by default. Review the contents of the file ORACLE_HOME/rdbms/admin/externaljob.ora for the lines run_user= and run_group=. If the user assigned to these parameters is not "nobody", this is a finding. For versions 11.1 and later, the external procedure agent (extproc executable) is available directly from the database and does not require definition in the listener.ora file for use. Review the contents of the file ORACLE_HOME/hs/admin/extproc.ora. If the file does not exist, this is a finding. If the following entry does not appear in the file, this is a finding: EXTPROC_DLLS=ONLY:[dll full file name1]:[dll full file name2]:.. [dll full file name] represents a full path and file name. This list of file names is separated by ":". Note: If "ONLY" is specified, then the list is restricted to allow execution of only the DLLs specified in the list and is not a finding. If "ANY" is specified, then there are no restrictions for execution except what is controlled by operating system permissions and is a finding. If no specification is made, any files located in the %ORACLE_HOME%\bin directory on Windows systems or $ORACLE_HOME/lib directory on UNIX systems can be executed (the default) and is a finding. Ensure that EXTPROC is not accessible from the listener. Review the listener.ora file. If any entries reference "extproc", this is a finding. Determine if the external procedure agent is in use per Oracle 10.x conventions. Review the listener.ora file. If any entries reference "extproc", then the agent is in use. If external procedure agent is not authorized for use in the System Security Plan and references to "extproc" exist, this is a finding. Sample listener.ora entries with extproc included: LISTENER = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521)) ) EXTLSNR = (DESCRIPTION = (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC)) ) SID_LIST_LISTENER = (SID_LIST = (SID_DESC = (GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /home/oracle/app/oracle/product/11.1.0/db_1) (SID_NAME = ORCL) ) ) SID_LIST_EXTLSNR = (SID_LIST = (SID_DESC = (PROGRAM = extproc) (SID_NAME = PLSExtProc) (ORACLE_HOME = /home/oracle/app/oracle/product/11.1.0/db_1) (ENVS="EXTPROC_DLLS=ONLY:/home/app1/app1lib.so:/home/app2/app2lib.so, LD_LIBRARY_PATH=/private/app2/lib:/private/app1, MYPATH=/usr/fso:/usr/local/packages") ) ) Sample tnsnames.ora entries with extproc included: ORCL = (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521)) ) (CONNECT_DATA = (SERVICE_NAME = ORCL) ) ) EXTPROC_CONNECTION_DATA = (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = IPC)(KEY = extproc)) ) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = PLSExtProc) ) ) If EXTPROC is in use, confirm that a listener is dedicated to serving the external procedure agent (as shown above). View the protocols configured for the listener. For the listener to be dedicated, the only entries will be to specify extproc. If there is not a dedicated listener in use for the external procedure agent, this is a finding. If the PROTOCOL= specified is other than IPC, this is a finding. Verify and ensure extproc is restricted executing authorized external applications only and extproc is restricted to execution of authorized applications. Review the listener.ora file. If the following entry does not exist, this is a finding: EXTPROC_DLLS=ONLY:[dll full file name1]:[dll full file name2]:... Note: [dll full file name] represents a full path and file name. This list of file names is separated by ":". Note: If "ONLY" is specified, then the list is restricted to allow execution of only the DLLs specified in the list and is not a finding. If "ANY" is specified, then there are no restrictions for execution except what is controlled by operating system permissions and is a finding. If no specification is made, any files located in the %ORACLE_HOME%\bin directory on Windows systems or $ORACLE_HOME/lib directory on UNIX systems can be executed (the default) and is a finding. View the listener.ora file (usually in ORACLE_HOME/network/admin or directory specified by the TNS_ADMIN environment variable). If multiple listener processes are running, then the listener.ora file for each must be viewed. For each process, determine the directory specified in the ORACLE_HOME or TNS_ADMIN environment variable defined for the process account to locate the listener.ora file.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-220289`

### Rule: The DBMS must support the organizational requirements to specifically prohibit or restrict the use of unauthorized functions, ports, protocols, and/or services.

**Rule ID:** `SV-220289r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Additionally, it is sometimes convenient to provide multiple services from a single component of an information system (e.g., email and web services), but doing so increases risk by constraining the ability to restrict the use of functions, ports, protocols, and/or services. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS settings for functions, ports, protocols, and services that are not approved. If any are found, this is a finding. (For definitive information on Ports, Protocols, and Services Management [PPSM], refer to https://cyber.mil/ppsm/) - - - - - In the Oracle database, the communications with the database and incoming requests are performed by the Oracle Listener. The Oracle Listener listens on a specific port or ports for connections to a specific database. The Oracle Listener has configuration files located in the $ORACLE_HOME/network/admin directory. To check the ports and protocols in use, go to that directory and review the SQLNET.ora, LISTENER.ora, and the TNSNAMES.ora. If protocols or ports are in use that are not authorized, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-220290`

### Rule: The DBMS must support organizational requirements to enforce password encryption for storage.

**Rule ID:** `SV-220290r879608_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Applications must enforce password encryption when storing passwords. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read and easily compromised. Database passwords stored in clear text are vulnerable to unauthorized disclosure. Database passwords must always be encoded or encrypted when stored internally or externally to the DBMS. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names that include "SSL", such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
(Oracle stores and displays its passwords in encrypted form. Nevertheless, this should be verified by reviewing the relevant system views, along with the other items to be checked here.) Ask the DBA to review the list of DBMS database objects, database configuration files, associated scripts, and applications defined within and external to the DBMS that access the database. The list should also include files, tables, or settings used to configure the operational environment for the DBMS and for interactive DBMS user accounts. Ask the DBA and/or ISSO to determine if any DBMS database objects, database configuration files, associated scripts, and applications defined within or external to the DBMS that access the database, and DBMS/user environment files/settings/tables, contain database passwords. If any do, confirm that DBMS passwords stored internally or externally to the DBMS are encoded or encrypted. If any passwords are stored in clear text, this is a finding. Ask the DBA/SA/Application Support staff if they have created an external password store for applications, batch jobs, and scripts to use. Verify that all passwords stored there are encrypted. If a password store is used and any password is not encrypted, this is a finding. - - - - - The following are notes on implementing a Secure External Password Store using Oracle Wallet. Password credentials can be stored for connecting to databases using a client-side Oracle wallet. An Oracle wallet is a secure software container that stores authentication and signing credentials. This wallet usage can simplify large-scale deployments that rely on password credentials for connecting to databases. When this feature is configured, application code, batch jobs, and scripts no longer need embedded user names and passwords. This reduces risk because the passwords are no longer exposed, and password management policies are more easily enforced without changing application code whenever user names or passwords change. The external password store of the wallet is separate from the area where public key infrastructure (PKI) credentials are stored. Consequently, Oracle Wallet Manager cannot be used to manage credentials in the external password store of the wallet. Instead, use the command-line utility mkstore to manage these credentials. How Does the External Password Store Work? Typically, users (and applications, batch jobs, and scripts) connect to databases by using a standard CONNECT statement that specifies a database connection string. This string can include a user name and password, and an Oracle Net service name identifying the database on an Oracle Database network. If the password is omitted, the connection prompts the user for the password. For example, the service name could be the URL that identifies that database, or a TNS alias entered in the tnsnames.ora file in the database. Another possibility is a host:port:sid string. The following examples are standard CONNECT statements that could be used for a client that is not configured to use the external password store: CONNECT salesapp@sales_db.us.example.com Enter password: password CONNECT salesapp@orasales Enter password: password CONNECT salesapp@ourhost37:1527:DB17 Enter password: password In these examples, salesapp is the user name, with the unique connection string for the database shown as specified in three different ways; use its URL sales_db.us.example.com, or its TNS alias, orasales, from the tnsnames.ora file, or its host:port:sid string. However, when clients are configured to use the secure external password store, applications can connect to a database with the following CONNECT statement syntax, without specifying database logon credentials: CONNECT /@db_connect_string CONNECT /@db_connect_string AS SYSDBA CONNECT /@db_connect_string AS SYSOPER In this specification, db_connect_string is a valid connection string to access the intended database, such as the service name, URL, or alias as shown in the earlier examples. Each user account must have its own unique connection string; cannot create one connection string for multiple users. In this case, the database credentials, user name and password, are securely stored in an Oracle wallet created for this purpose. The autologon feature of this wallet is turned on, so the system does not need a password to open the wallet. From the wallet, it gets the credentials to access the database for the user they represent.

## Group: SRG-APP-000175-DB-000067

**Group ID:** `V-220291`

### Rule: The DBMS, when utilizing PKI-based authentication, must validate certificates by constructing a certification path with status information to an accepted trust anchor.

**Rule ID:** `SV-220291r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be for example a Certification Authority (CA). A certification path starts with the Subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Database Management Systems that do not validate certificates to a trust anchor are in danger of accepting certificates that are invalid and/or counterfeit. This could allow unauthorized access to the database. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including 'SSL', such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. Review DBMS configuration to verify the certificates being accepted by the DBMS have a valid certification path with status information to an accepted trust anchor. If certification paths are not being validated back to a trust anchor, this is a finding. - - - - - The database supports PKI-based authentication by using digital certificates over TLS in addition to the native encryption and data integrity capabilities of these protocols. Oracle provides a complete PKI that is based on RSA Security, Inc., Public-Key Cryptography Standards, and which interoperates with Oracle servers and clients. The database uses a wallet that is a container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by TLS. In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates. If the $ORACLE_HOME/network/admin/sqlnet.ora contains the following entries, TLS is installed. WALLET_LOCATION = (SOURCE= (METHOD = FILE) (METHOD_DATA = DIRECTORY=/wallet) SSL_CIPHER_SUITES=(SSL_cipher_suiteExample) SSL_VERSION = 1.2 SSL_CLIENT_AUTHENTICATION=TRUE (Note: This assumes that a single sqlnet.ora file, in the default location, is in use. Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.)

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-220293`

### Rule: Processes (services, applications, etc.) that connect to the DBMS independently of individual users, must use valid, current DoD approved PKI certificates for authentication to the DBMS.

**Rule ID:** `SV-220293r879614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Just as individual users must be authenticated, and just as they must use PKI-based authentication, so must any processes that connect to the DBMS. The DoD standard for authentication of a process or device communicating with another process or device is the presentation of a valid, current, DoD-issued Public Key Infrastructure (PKI) certificate that has previously been verified as Trusted by an administrator of the other process or device. This applies both to processes that run on the same server as the DBMS and to processes running on other computers. The Oracle-supplied accounts, SYS, SYSBACKUP, SYSDG, and SYSKM, are exceptions. These cannot currently use certificate-based authentication. For this reason among others, use of these accounts should be restricted to where it is truly needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to confirm that accounts used by processes to connect to the DBMS are authenticated using valid, current DoD approved PKI certificates. If any such account (other than SYS, SYSBACKUP, SYSDG, and SYSKM) is not certificate-based, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-220294`

### Rule: The DBMS must use NIST-validated FIPS 140-2 or 140-3 compliant cryptography for authentication mechanisms.

**Rule ID:** `SV-220294r903013_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications (including DBMSs) utilizing cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following settings to verify FIPS 140 authentication/encryption is configured. If encryption is required but not configured, check with the DBA and system administrator to verify if other mechanisms or third-party cryptography products are deployed for authentication. To verify if Oracle is configured for FIPS 140 SSL/TLS authentication and/or Encryption: Verify the DBMS version: select * from V$VERSION; If the version displayed for Oracle Database is lower than 12.1.0.2, this is a finding. If the operating system is Windows and the DBMS version is 12.1.0.2, use the opatch command to display the patches applied to the DBMS. If the patches listed do not include "WINDOWS DB BUNDLE PATCH 12.1.0.2.7", this is a finding. Open the fips.ora file in a browser or editor. (The default location for fips.ora is $ORACLE_HOME/ldap/admin/ but alternate locations are possible. An alternate location, if it is in use, is specified in the FIPS_HOME environment variable.) If the line "SSLFIPS_140=TRUE" is not found in fips.ora, or the file does not exist, this is a finding.

## Group: SRG-APP-000220-DB-000149

**Group ID:** `V-220295`

### Rule: The DBMS must terminate user sessions upon user logoff or any other organization or policy-defined session termination events, such as idle time limit exceeded.

**Rule ID:** `SV-220295r879637_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement focuses on communications protection at the application session, versus network packet, level. Session IDs are tokens generated by web applications to uniquely identify an application user's session. Applications will make application decisions and execute business logic based on the session ID. Unique session identifiers or IDs are the opposite of sequentially generated session IDs, which can be easily guessed by an attacker. Unique session IDs help to reduce predictability of said identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attackers are unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. When a user logs out, or when any other session termination event occurs, the application must terminate the user session to minimize the potential for an attacker to hijack that particular user session. Database sessions must be terminated when no longer in use in order to prevent session hijacking.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings and vendor documentation to verify user sessions are terminated upon user logout. If they are not, this is a finding. Review system documentation and organization policy to identify other events that should result in session terminations. If other session termination events are defined, review DBMS settings to verify occurrences of these events would cause session termination. If occurrences of defined session-terminating events do not cause session terminations, this is a finding. When a user logs off of an Oracle session gracefully or has the session terminated for an idle timeout or any other reason, the session is terminated, and the resources are returned to the system. Check with the DBA to see what mechanism is used to disconnect the session and what events the site uses to determine if a connection needs to be terminated. To test for timeout, open a connection and leave it idle for a period greater than the defined idle timeout setting enforced by the system. Then try to use the connection. If the connection is no longer active, then the mechanism deployed to terminate the connection is active and working.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-220296`

### Rule: The DBMS must preserve any organization-defined system state information in the event of a system failure.

**Rule ID:** `SV-220296r879641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a known state can address safety or security in accordance with the mission/business needs of the organization. Failure in a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving information system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database is used solely for transient data (such as one dedicated to Extract-Transform-Load (ETL)), and a clear plan exists for the recovery of the database by means other than archiving, this is not a finding. If it has been determined that up-to-the second recovery is not necessary and this fact is recorded in the system documentation, with appropriate approval, this is not a finding. Check DBMS settings to determine whether system state information is being preserved in the event of a system failure. The necessary state information is defined as "information necessary to determine cause of failure and to return to operations with least disruption to mission/business processes". Oracle creates what is known as archive logs. Archive logs contain information required to replay a transaction should something happen. The redo logs are also used to copy transactions or pieces of transactions. Issue the following commands to check the status of archive log mode: $ sqlplus connect as sysdba --Check current archivelog mode in database SQL> archive log list Database log mode Archive Mode Automatic archival Enabled Archive destination /home/oracle/app/oracle/arc2/ORCL Oldest online log sequence 433 Next log sequence to archive 435 Current log sequence 435 If archive log mode is not enabled, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-220297`

### Rule: The DBMS must take needed steps to protect data at rest and ensure confidentiality and integrity of application data.

**Rule ID:** `SV-220297r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User-generated data and application-specific configuration data both need to be protected. Configurations and/or rule sets for firewalls, gateways, intrusion detection/prevention systems, and filtering routers and authenticator content are examples of system information likely requiring protection. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and Authorizing Official have determined that encryption of data at rest is NOT required, this is not a finding. Review DBMS settings to determine whether controls exist to protect the confidentiality and integrity of data at rest in the database. If controls do not exist or are not enabled, this is a finding. To ensure that the appropriate controls are in place, discuss the precautions taken with the site Database Administrators and System Administrators and try to modify data at rest. Oracle recommends using Transparent Data Encryption to protect data. To check to see if the data is encrypted, for example, upon an auditor's request Oracle provides views that document the encryption status of the database. For TDE column encryption, use the view "dba_encrypted_columns", which lists the owner, table name, column name, encryption algorithm, and salt for all encrypted columns. For TDE tablespace encryption, the following SQL statement lists all encrypted tablespaces with their encryption algorithm and corresponding, encrypted, data files. Issue the following commands to check to see if the data at rest is encrypted. $ sqlplus connect as sysdba SQL> SELECT t.name "TSName", e.encryptionalg "Algorithm", d.file_name "File Name" FROM v$tablespace t, v$encrypted_tablespaces e, dba_data_files d WHERE t.ts# = e.ts# and t.name = d.tablespace_name; The next SQL statement lists the table owner, tables within encrypted tablespaces, and the encryption algorithm: SQL> SELECT a.owner "Owner", a.table_name "Table Name", e.encryptionalg "Algorithm" FROM dba_tables a, v$encrypted_tablespaces e WHERE a.tablespace_name in (select t.name from v$tablespace t, v$encrypted_tablespaces e where t.ts# = e.ts#);

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-220298`

### Rule: The DBMS must isolate security functions from nonsecurity functions by means of separate security domains.

**Rule ID:** `SV-220298r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security functions are defined as "the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based". Developers and implementers can increase the assurance in security functions by employing well-defined security policy models, structured, disciplined, and rigorous hardware and software development techniques, and sound system/security engineering principles. Database Management Systems typically separate security functionality from non-security functionality via separate databases or schemas. Database objects or code implementing security functionality must not be commingled with objects or code implementing application logic. When security and non-security functionality is commingled, users who have access to non-security functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine whether objects or code implementing security functionality are located in a separate security domain, such as a separate database or schema created specifically for security functionality. If security-related database objects or code are not kept separate, this is a finding. The Oracle elements of security functionality, such as the roles, permissions, and profiles, along with password complexity requirements, are stored in separate schemas in the database. Review any site-specific applications security modules built into the database and determine what schema they are located in and take appropriate action. The Oracle objects will be in the Oracle Data Dictionary.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-220299`

### Rule: The DBMS must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-220299r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, so copies of sensitive data are not misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are proper procedures in place for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test, and verify copies of production data are not left in unprotected locations. If there is no documented procedure for data movement from production to development/test, this is a finding. If the code that exists for data movement does not remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-220300`

### Rule: The DBMS must check the validity of data inputs.

**Rule ID:** `SV-220300r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. All applications need to validate the data users attempt to input to the application for processing. Rules for checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, acceptable values) are in place to verify inputs match specified definitions for format and content. Inputs passed to interpreters are prescreened to prevent the content from being unintentionally interpreted as commands. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS code, settings, field definitions, constraints, and triggers to determine whether or not data being input into the database is validated. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If field definitions do not exist in the database, this is a finding. If fields do not contain enabled constraints where required, this is a finding. - - - - - Oracle provides built-in processes to keep data and its integrity intact by using constraints. Integrity Constraint States Can specify that a constraint is enabled (ENABLE) or disabled (DISABLE). If a constraint is enabled, data is checked as it is entered or updated in the database, and data that does not conform to the constraint is prevented from being entered. If a constraint is disabled, then data that does not conform can be allowed to enter the database. Additionally, can specify that existing data in the table must conform to the constraint (VALIDATE). Conversely, if specified NOVALIDATE, are not ensured that existing data conforms. An integrity constraint defined on a table can be in one of the following states: ENABLE, VALIDATE ENABLE, NOVALIDATE DISABLE, VALIDATE DISABLE, NOVALIDATE For details about the meaning of these states and an understanding of their consequences, see the Oracle Database SQL Language Reference. Some of these consequences are discussed here. Disabling Constraints To enforce the rules defined by integrity constraints, the constraints should always be enabled. However, consider temporarily disabling the integrity constraints of a table for the following performance reasons: - When loading large amounts of data into a table - When performing batch operations that make massive changes to a table (for example, changing every employee's number by adding 1000 to the existing number) - When importing or exporting one table at a time In all three cases, temporarily disabling integrity constraints can improve the performance of the operation, especially in data warehouse configurations. It is possible to enter data that violates a constraint while that constraint is disabled. Thus, always enable the constraint after completing any of the operations listed in the preceding bullet list. Enabling Constraints While a constraint is enabled, no row violating the constraint can be inserted into the table. However, while the constraint is disabled, such a row can be inserted. This row is known as an exception to the constraint. If the constraint is in the ENABLE, NOVALIDATE state, violations resulting from data entered while the constraint was disabled remain. The rows that violate the constraint must be either updated or deleted in order for the constraint to be put in the validated state. Can identify exceptions to a specific integrity constraint while attempting to enable the constraint. See "Reporting Constraint Exceptions". All rows violating constraints are noted in an EXCEPTIONS table, which can be examined. ENABLE, NOVALIDATE Constraint State When a constraint is in the ENABLE, NOVALIDATE state, all subsequent statements are checked for conformity to the constraint. However, any existing data in the table is not checked. A table with ENABLE, NOVALIDATE constraints can contain invalid data, but it is not possible to add new invalid data to it. Constraints in the ENABLE, NOVALIDATE state is most useful in data warehouse configurations that are uploading valid OLTP data. Enabling a constraint does not require validation. Enabling a constraint novalidate is much faster than enabling and validating a constraint. Also, validating a constraint that is already enabled does not require any DML locks during validation (unlike validating a previously disabled constraint). Enforcement guarantees that no violations are introduced during the validation. Hence, enabling without validating reduces the downtime typically associated with enabling a constraint. Efficient Use of Integrity Constraints: A Procedure Using integrity constraint states in the following order can ensure the best benefits: Disable state. Perform the operation (load, export, import). ENABLE, NOVALIDATE state. Enable state. Some benefits of using constraints in this order are: No locks are held. All constraints can go to enable state concurrently. Constraint enabling is done in parallel. Concurrent activity on table is permitted. Setting Integrity Constraints Upon Definition When an integrity constraint is defined in a CREATE TABLE or ALTER TABLE statement, it can be enabled, disabled, or validated or not validated as determined by the specification of the ENABLE/DISABLE clause. If the ENABLE/DISABLE clause is not specified in a constraint definition, the database automatically enables and validates the constraint. Disabling Constraints Upon Definition The following CREATE TABLE and ALTER TABLE statements both define and disable integrity constraints: CREATE TABLE emp ( empno NUMBER(5) PRIMARY KEY DISABLE, . . . ; ALTER TABLE emp ADD PRIMARY KEY (empno) DISABLE; An ALTER TABLE statement that defines and disables an integrity constraint never fails because of rows in the table that violate the integrity constraint. The definition of the constraint is allowed because its rule is not enforced. Enabling Constraints Upon Definition The following CREATE TABLE and ALTER TABLE statements both define and enable integrity constraints: CREATE TABLE emp ( empno NUMBER(5) CONSTRAINT emp.pk PRIMARY KEY, . . . ; ALTER TABLE emp ADD CONSTRAINT emp.pk PRIMARY KEY (empno); An ALTER TABLE statement that defines and attempts to enable an integrity constraint can fail because rows of the table violate the integrity constraint. If this case, the statement is rolled back, and the constraint definition is not stored and not enabled. When enabling a UNIQUE or PRIMARY KEY constraint, an associated index is created.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-220301`

### Rule: The DBMS must only generate error messages that provide information necessary for corrective actions without revealing organization-defined sensitive or potentially harmful information in error logs and administrative messages that could be exploited.

**Rule ID:** `SV-220301r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The structure and content of error messages needs to be carefully considered by the organization and development team. The extent to which the application is able to identify and handle error conditions is guided by organizational policy and operational requirements. Sensitive information includes account numbers, social security numbers, and credit card numbers. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and custom database and application code to verify error messages do not contain information beyond what is needed for troubleshooting the issue. If database errors contain PII data, sensitive business data, or information useful for identifying the host system, this is a finding. Notes on Oracle's approach to this issue: Out of the box, Oracle covers this. For example, if a user does not have access to a table, the error is just that the table or view does not exist. The Oracle database is not going to display a Social Security Number in an error code unless an application is programmed to do so. Oracle applications will not expose the actual transactional data to a screen. The only way Oracle will capture this information is to enable specific logging levels. Custom code would require a review to ensure compliance.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-220302`

### Rule: The DBMS must restrict error messages so only authorized personnel may view them.

**Rule ID:** `SV-220302r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that error messages are displayed only to those who are authorized to view them. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and custom database code to determine if error messages are ever displayed to unauthorized individuals: i) Review all end-user-facing applications that use the database, to determine whether they display any DBMS-generated error messages to general users. If they do, this is a finding. ii) Review whether the database is accessible to users who are not authorized system administrators or database administrators, via the following types of software: iia) Oracle SQL*Plus iib) Reporting and analysis tools iic) Database management and/or development tools, such as, but not limited to, Toad. iid) Application development tools, such as, but not limited to, Oracle JDeveloper, Microsoft Visual Studio, PowerBuilder, or Eclipse. If the answer to the preceding question (iia through iid) is Yes, inquire whether, for each role or individual with respect to each tool, this access is required to enable the user(s) to perform authorized job duties. If No, this is a finding. If Yes, continue: For each tool in use, determine whether it is capable of suppressing DBMS-generated error messages, and if it is, whether it is configured to do so. Determine whether the role or individual, with respect to each tool, needs to see detailed DBMS-generated error messages. If No, and if the tool is not configured to suppress such messages, this is a finding. If Yes, determine whether the role/user's need to see such messages is documented in the System Security Plan. If so, this is not a finding. If not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-220303`

### Rule: Applications must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-220303r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent the compromise of authentication information, such as passwords, during the authentication process, the feedback from the information system shall not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided information when typed into the system is a method used in addressing this risk. For example, displaying asterisks when a user types in a password, is an example of obscuring feedback of authentication information. Database applications may allow for entry of the account name and password as a visible parameter of the application execution command. This practice should be prohibited and disabled to prevent shoulder surfing. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the DBA to determine if any applications that access the database allow for entry of the account name and password on the command line. If any do, determine whether these applications obfuscate authentication data. If they do not, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-220304`

### Rule: When using command-line tools such as Oracle SQL*Plus, which can accept a plain-text password, users must use an alternative logon method that does not expose the password.

**Rule ID:** `SV-220304r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SRG states: "To prevent the compromise of authentication information, such as passwords, during the authentication process, the feedback from the information system shall not provide any information that would allow an unauthorized user to compromise the authentication mechanism." "Obfuscation of user-provided information when typed into the system is a method used in addressing this risk." "For example, displaying asterisks when a user types in a password, is an example of obscuring feedback of authentication information." "Database applications may allow for entry of the account name and password as a visible parameter of the application execution command. This practice should be prohibited and disabled to prevent shoulder surfing." SQL*Plus is an essential part of any Oracle installation. SQL*Plus cannot be configured not to accept a plain-text password. Since the typical SQL*Plus user is a database administrator, the consequences of password compromise are particularly serious. Therefore, the use of plain-text passwords must be prohibited, as a matter of practice and procedure. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including 'SSL', such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Oracle SQL*Plus, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations; and that AO approval has been obtained. If not, this is a finding. Request evidence that all users of the tool are trained in the importance of not using the plain-text password option and in how to keep the password hidden; and that they adhere to this practice. If not, this is a finding.

## Group: SRG-APP-000109-DB-000049

**Group ID:** `V-220305`

### Rule: The DBMS must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-220305r879571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, the DBMS must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the DBMS and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS settings to determine whether audit logging is configured to produce logs consistent with the amount of space allocated for logging. If auditing will generate excessive logs so that they may outgrow the space reserved for logging, this is a finding. If file-based auditing is in use, check that sufficient space is available to support the file(s). If not, this is a finding. If standard, table-based auditing is used, the audit logs are written to a table called AUD$; and if a Virtual Private Database is deployed, a table is created called FGA_LOG$. First, check the current location of the audit trail tables. CONN / AS SYSDBA SELECT table_name, tablespace_name FROM dba_tables WHERE table_name IN ('AUD$', 'FGA_LOG$') ORDER BY table_name; TABLE_NAME TABLESPACE_NAME ------------------------------ ------------------------------ AUD$ SYSTEM FGA_LOG$ SYSTEM If the tablespace name is SYSTEM, the table needs to be relocated to its own tablespace. Ensure that adequate space is allocated to that tablespace. If Unified Auditing is used: Audit logs are written to tables in the AUDSYS schema. The default tablespace for AUDSYS is USERS. A separate tablespace should be created to contain audit data. Ensure that adequate space is allocated to that tablespace. Investigate whether there have been any incidents where the DBMS ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-220306`

### Rule: Database software, applications, and configuration files must be monitored to discover unauthorized changes.

**Rule ID:** `SV-220306r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify that monitoring of changes to database software libraries, related applications, and configuration files is done. Verify that the list of files and directories being monitored is complete. If monitoring does not occur or is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-220307`

### Rule: Logic modules within the database (to include packages, procedures, functions and triggers) must be monitored to discover unauthorized changes.

**Rule ID:** `SV-220307r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. This includes the logic modules implemented within the database, such as packages, procedures, functions and triggers. If the DBMS were to allow any user to make changes to these, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database logic modules can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify that monitoring of changes to database logic modules is done. Verify the list of objects (packages, procedures, functions, and triggers) being monitored is complete. If monitoring does not occur or is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-220308`

### Rule: The DBMS software installation account must be restricted to authorized users.

**Rule ID:** `SV-220308r879586_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. If the application were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement is contingent upon the language in which the application is programmed, as many application architectures in use today incorporate their software libraries into, and make them inseparable from, their compiled distributions, rendering them static and version-dependent. However, this requirement does apply to applications with software libraries accessible and configurable, as in the case of interpreted languages. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a greater impact on database security and operation. It is especially important to grant access to privileged accounts to only those persons who are qualified and authorized to use them. This requirement is particularly important because Oracle equates the installation account with the SYS account - the super-DBA. Once logged on to the operating system, this account can connect to the database AS SYSDBA without further authentication. It is very powerful and, by virtue of not being linked to any one person, cannot be audited to the level of the individual.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling and granting access to use of the DBMS software installation account. If access or use of this account is not restricted to the minimum number of personnel required, or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-220309`

### Rule: Database software directories, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-220309r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS software library directory and note other root directories located on the same disk directory or any subdirectories. If any non-DBMS software directories exist on the disk directory, examine or investigate their use. If any of the directories are used by other applications, including third-party applications that use the DBMS, this is a finding. Only applications that are required for the functioning and administration, not use, of the DBMS should be located on the same disk directory as the DBMS software libraries. For databases located on mainframes, confirm that the database and its configuration files are isolated in their own DASD pools. If database software and database configuration files share DASD with other applications, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-220310`

### Rule: The DBMS must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-220310r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, organizational users shall be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings, OS settings, and/or enterprise-level authentication/access mechanism settings, and site practices, to determine whether organizational users are uniquely identified and authenticated when logging on to the system. If organizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-220311`

### Rule: The DBMS must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-220311r879617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users shall be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings to determine whether non-organizational users are uniquely identified and authenticated when logging onto the system. If non-organizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-220312`

### Rule: The DBMS must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-220312r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers, and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and vendor documentation to verify administrative functionality is separate from user functionality. If administrator and general user functionality is not separated either physically or logically, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-220313`

### Rule: The DBMS must protect against an individual who uses a shared account falsely denying having performed a particular action.

**Rule ID:** `SV-220313r879554_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to maintain application integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects individuals against later claims by an author of not having authored a particular document, a sender of not having transmitted a message, a receiver of not having received a message, or a signatory of not having signed a document. Authentication via shared accounts does not provide individual accountability for actions taken on the DBMS or data. Whenever a single database account is used to connect to the database, a secondary authentication method that provides individual accountability is required. This scenario most frequently occurs when an externally hosted application authenticates individual users to the application and the application uses a single account to retrieve or update database information on behalf of the individual users. When shared accounts are utilized without another means of identifying individual users, users may deny having performed a particular action. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no shared accounts available to more than one user, this is not a finding. If a shared account is used by an application to interact with the database, review the System Security Plan, the tables in the database, and the application source code/documentation to determine whether the application captures the individual user's identity and stores that identity along with all data inserted and updated (also with all records of reads and/or deletions, if these are required to be logged). If there are gaps in the application's ability to do this, and the gaps and the risk are not defined in the system documentation and accepted by the AO, this is a finding. If users are sharing a group account to log on to Oracle tools or third-party products that access the database, this is a finding. If Standard Auditing is used: To ensure that user activities other than SELECT, INSERT, UPDATE, and DELETE are also monitored and attributed to individuals, verify that Oracle auditing is enabled. To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value "NONE", this is a finding. If Unified Auditing is used: To ensure that user activities other than SELECT, INSERT, UPDATE, and DELETE are also monitored and attributed to individuals, verify that Oracle auditing is enabled. To see if Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237696`

### Rule: DBA OS accounts must be granted only those host system privileges necessary for the administration of the DBMS.

**Rule ID:** `SV-237696r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC), is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account. DBAs, if assigned excessive OS privileges, could perform actions that could endanger the information system or hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review host system privileges assigned to the Oracle DBA group and all individual Oracle DBA accounts. Note: do not include the Oracle software installation account in any results for this check. For UNIX systems (as root): cat /etc/group | grep -i dba groups root If "root" is returned in the first list, this is a finding. If any accounts listed in the first list are also listed in the second list, this is a finding. Investigate any user account group memberships other than DBA or root groups that are returned by the following command (also as root): groups [dba user account] Replace [dba user account] with the user account name of each DBA account. If individual DBA accounts are assigned to groups that grant access or privileges for purposes other than DBA responsibilities, this is a finding. For Windows Systems (click or select): Start / Settings / Control Panel / Administrative Tools / Computer Management / Local Users and Groups / Groups / ORA_DBA Start / Settings / Control Panel / Administrative Tools / Computer Management / Local Users and Groups / Groups / ORA_[SID]_DBA (if present) Note: Users assigned DBA privileges on a Windows host are granted membership in the ORA_DBA and/or ORA_[SID]_DBA groups. The ORA_DBA group grants DBA privileges to any database on the system. The ORA_[SID]_DBA groups grant DBA privileges to specific Oracle instances only. Make a note of each user listed. For each user (click or select): Start / Settings / Control Panel / Administrative Tools / Computer Management / Local Users and Groups / Users / [DBA user name] / Member of If DBA users belong to any groups other than DBA groups and the Windows Users group, this is a finding. Examine User Rights assigned to DBA groups or group members: Start / Settings / Control Panel / Administrative Tools / Local Security Policy / Security Settings / Local Policies / User Rights Assignments If any User Rights are assigned directly to the DBA group(s) or DBA user accounts, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-237697`

### Rule: Oracle software must be evaluated and patched against newly found vulnerabilities.

**Rule ID:** `SV-237697r879827_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security faults with software applications and operating systems are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling, must also be addressed expeditiously. Anytime new software code is introduced to a system there is the potential for unintended consequences. There have been documented instances where the application of a patch has caused problems with system integrity or availability. Due to information system integrity and availability concerns, organizations must give careful consideration to the methodology used to carry out automatic updates. Unsupported software versions are not patched by vendors to address newly discovered security versions. An unpatched version is vulnerable to attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When the Quarterly CPU is released, check the CPU Notice and note the specific patch number for the system. Then, issue the following command: SELECT patch_id, version, action, status, description from dba_registry_sqlpatch; This will generate the patch levels for the home and any specific patches that have been applied to it. If the currently installed patch levels are lower than the latest, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237698`

### Rule: DBMS default accounts must be assigned custom passwords.

**Rule ID:** `SV-237698r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. DBMS default passwords provide a commonly known and exploited means for unauthorized access to database installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use this query to identify the Oracle-supplied accounts that still have their default passwords: SELECT * FROM SYS.DBA_USERS_WITH_DEFPWD; If any accounts other than XS$NULL are listed, this is a finding. (XS$NULL is an internal account that represents the absence of a user in a session. Because XS$NULL is not a user, this account can only be accessed by the Oracle Database instance. XS$NULL has no privileges and no one can authenticate as XS$NULL, nor can authentication credentials ever be assigned to XS$NULL.)

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-237699`

### Rule: The DBMS must employ cryptographic mechanisms preventing the unauthorized disclosure of information during transmission unless the transmitted data is otherwise protected by alternative physical measures.

**Rule ID:** `SV-237699r879812_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPSEC tunnel. Alternative physical protection measures include Protected Distribution Systems (PDS). PDS are used to transmit unencrypted classified NSI through an area of lesser classification or control. Inasmuch as the classified NSI is unencrypted, the PDS must provide adequate electrical, electromagnetic, and physical safeguards to deter exploitation. Refer to NSTSSI No. 7003 for additional details on a PDS. Information in transmission is particularly vulnerable to attack. If the DBMS does not employ cryptographic mechanisms preventing unauthorized disclosure of information during transit, the information may be compromised. SHA-1 is in the process of being removed from service within the DoD and it's use is to be limited during the transition to SHA-2. Use of SHA-1 for digital signature generation is prohibited. Allowable uses during the transition include CHECKSUM usage and verification of legacy certificate signatures. SHA-1 is considered a temporary solution during legacy application transitionary periods and should not be engineered into new applications. SHA-2 is the path forward for DoD. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine whether cryptographic mechanisms are used to prevent the unauthorized disclosure of information during transmission. Determine whether physical measures are being used instead of cryptographic mechanisms. If neither cryptographic nor physical measures are being utilized, this is a finding. To check that network encryption is enabled and using site-specified encryption procedures, look in SQLNET.ORA located at $ORACLE_HOME/network/admin/sqlnet.ora. (Note: This assumes that a single sqlnet.ora file, in the default location, is in use. Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.) If encryption is set, entries like the following will be present: SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT= (SHA384) SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER= (SHA384) SQLNET.ENCRYPTION_TYPES_CLIENT= (AES256) SQLNET.ENCRYPTION_TYPES_SERVER= (AES256) SQLNET.CRYPTO_CHECKSUM_CLIENT = requested SQLNET.CRYPTO_CHECKSUM_SERVER = required (The values assigned to the parameters may be different, the combination of parameters may be different, and not all of the example parameters will necessarily exist in the file.)

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-237700`

### Rule: The DBMS must support the disabling of network protocols deemed by the organization to be nonsecure.

**Rule ID:** `SV-237700r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is related to remote access, but more specifically to the networking protocols allowing systems to communicate. Remote access is any access to an organizational information system by a user (or an information system) communicating through an external, non-organization controlled network (e.g., the internet). Examples of remote access methods include dial-up, broadband, and wireless. Some networking protocols allowing remote access may not meet security requirements to protect data and components. Bluetooth and peer-to-peer networking are examples of less than secure networking protocols. The DoD Ports, Protocols, and Services Management (PPSM) program provides implementation guidance on the use of IP protocols and application and data services traversing the DoD Networks in a manner supporting net-centric operations. Applications implementing or utilizing remote access network protocols need to ensure the application is developed and implemented in accordance with the PPSM requirements. In situations where it has been determined that specific operational requirements outweigh the risks of enabling an insecure network protocol, the organization may pursue a risk acceptance. Using protocols deemed nonsecure would compromise the ability of the DBMS to operate in a secure fashion. The database must be able to disable network protocols deemed nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PPSM Technical Assurance List to acquire an up-to-date list of network protocols deemed nonsecure. (For definitive information on Ports, Protocols, and Services Management (PPSM), refer to https://cyber.mil/ppsm/) Review DBMS settings to determine if the database is utilizing any network protocols deemed nonsecure. If the DBMS is not using any network protocols deemed nonsecure, this is not a finding. If the database is utilizing protocols specified as nonsecure in the PPSM, verify the protocols are explicitly identified in the System Security Plan (SSP) and that they are in support of specific operational requirements. If they are not identified in the SSP or are not supporting specific operational requirements, this is a finding. If nonsecure network protocols are not being used but are not disabled in the DBMS's configuration, this is a finding. After determining the site-specific operational requirements and the protocols explicitly defined in the SSP, check the $TNS_ADMIN setting for the location of the Oracle listener.ora file. The listener.ora file is a configuration file for Oracle Net Listener that identifies the following: A unique name for the listener, typically LISTENER A protocol address that it is accepting connection requests on, and A service it is listening for. If the listener.ora file shows a PROTOCOL= statement and the PROTOCOL is deemed nonsecure, that is a finding. LISTENER= (DESCRIPTION= (ADDRESS_LIST= (ADDRESS=(PROTOCOL=tcp)(HOST=sale-server)(PORT=1521)) (ADDRESS=(PROTOCOL=ipc)(KEY=extproc)))) SID_LIST_LISTENER= (SID_LIST= (SID_DESC= (GLOBAL_DBNAME=sales.us.example.com) (ORACLE_HOME=/oracle12c) (SID_NAME=sales)) (SID_DESC= (SID_NAME=plsextproc) (ORACLE_HOME=/oracle12c) (PROGRAM=extproc))) Protocol Parameters The Oracle Listener and the Oracle Connection Manager are identified by protocol addresses. The information below contains the "Protocol-Specific Parameters" used by the Oracle protocol support. Protocol-Specific Parameters Protocol: IPC Parameter: PROTOCOL Notes: Specify ipc as the value. Protocol: IPC Parameter: KEY Notes: Specify a unique name for the service. Oracle recommends using the service name or SID of the service. Example: (PROTOCOL=ipc)(KEY=sales) Protocol: Named Pipes Parameter: PROTOCOL Notes: Specify nmp as the value. Protocol: Named Pipes Parameter: SERVER Notes: Specify the name of the Oracle server. Protocol: Named Pipes Parameter: PIPE Notes: Specify the pipe name used to connect to the database server. This is the same PIPE keyword specified on the server with Named Pipes. This name can be any name. Example: (Protocol=nmp) (SERVER=USDOD) (PIPE=dbpipe01) Protocol: SDP Parameter: PROTOCOL Notes: Specify sdp as the value. Protocol: SDP Parameter: HOST Notes: Specify the host name or IP address of the computer. Protocol: SDP Parameter: PORT Notes: Specify the listening port number. Example: (PROTOCOL=sdp)(HOST=sales-server)(PORT=1521) (PROTOCOL=sdp)(HOST=192.168.2.204)(PORT=1521) Protocol: TCP/IP Parameter: PROTOCOL Notes: Specify TCP as the value. Protocol: TCP/IP Parameter: HOST Notes: Specify the host name or IP address of the computer. Protocol: TCP/IP Parameter: PORT Notes: Specify the listening port number. Example: (PROTOCOL=tcp)(HOST=sales-server)(PORT=1521) (PROTOCOL=tcp)(HOST=192.168.2.204)(PORT=1521) Protocol: TCP/IP with TLS Parameter: PROTOCOL Notes: Specify tcps as the value. Protocol: TCP/IP with TLS Parameter: HOST Notes: Specify the host name or IP address of the computer. Protocol: TCP/IP with TLS Parameter: PORT Notes: Specify the listening port number. Example:(PROTOCOL=tcps)(HOST=sales-server) (PORT=2484) (PROTOCOL=tcps)(HOST=192.168.2.204)(PORT=2484)

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237701`

### Rule: The DBMS must provide a mechanism to automatically identify accounts designated as temporary or emergency accounts.

**Rule ID:** `SV-237701r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary application accounts could be used in the event of a vendor support visit where a support representative requires a temporary unique account in order to perform diagnostic testing or conduct some other support-related activity. When these types of accounts are created, there is a risk that the temporary account may remain in place and active after the support representative has left. To address this, in the event temporary application accounts are required, the application must ensure accounts designated as temporary in nature shall automatically terminate these accounts after an organization-defined time period. Such a process and capability greatly reduces the risk that accounts will be misused, hijacked, or data compromised. Note that user authentication and account management should be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Temporary database accounts must be identified in order for the system to recognize and terminate them after a given time period. The DBMS and any administrators must have a means to recognize any temporary accounts for special handling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
: If the organization has a policy, consistently enforced, forbidding the creation of emergency or temporary accounts, this is not a finding. If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. If using the database to identify temporary accounts, and temporary accounts exist, there should be a temporary profile. If a profile for temporary accounts cannot be identified, this is a finding. To check for a temporary profile, run the scripts below: To obtain a list of profiles: SELECT PROFILE#, NAME FROM SYS.PROFNAME$; To obtain a list of users assigned a given profile (TEMPORARY_USERS, in this example): SELECT USERNAME, PROFILE FROM SYS.DBA_USERS WHERE PROFILE = 'TEMPORARY_USERS' ORDER BY USERNAME;

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237702`

### Rule: The DBMS must provide a mechanism to automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-237702r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary application accounts could ostensibly be used in the event of a vendor support visit where a support representative requires a temporary unique account in order to perform diagnostic testing or conduct some other support related activity. When these types of accounts are created, there is a risk that the temporary account may remain in place and active after the support representative has left. To address this, in the event temporary application accounts are required, the application must ensure accounts designated as temporary in nature shall automatically terminate these accounts after a period of 72 hours. Such a process and capability greatly reduces the risk that accounts will be misused, hijacked, or data compromised. Note that user authentication and account management should be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Temporary database accounts must be automatically terminated after a 72 hour time period in order to mitigate the risk of the account being used beyond its original purpose or timeframe.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization has a policy, consistently enforced, forbidding the creation of emergency or temporary accounts, this is not a finding. If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. Check DBMS settings, OS settings, and/or enterprise-level authentication/access mechanisms settings to determine if the site utilizes a mechanism whereby temporary are terminated after a 72 hour time period. If not, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-237703`

### Rule: The DBMS must enforce Discretionary Access Control (DAC) policy allowing users to specify and control sharing by named individuals, groups of individuals, or by both, limiting propagation of access rights and including or excluding access to the granularity of a single user.

**Rule ID:** `SV-237703r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access control policies (e.g., identity-based policies, role-based policies, attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, cryptography) are employed by organizations to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, domains). DAC is a type of access control methodology serving as a means of restricting access to objects and data based on the identity of subjects and/or groups to which they belong. It is discretionary in the sense that application users with the appropriate permissions to access an application resource or data have the discretion to pass that permission on to another user either directly or indirectly. Data protection requirements may result in a DAC policy being specified as part of the application design. Discretionary access controls would be employed at the application level to restrict and control access to application objects and data thereby providing increased information security for the organization. When DAC controls are employed, those controls must limit sharing to named application users, groups of users, or both. The application DAC controls must also limit the propagation of access rights and have the ability to exclude access to data down to the granularity of a single user. Databases using DAC must have the ability for the owner of an object or information to assign or revoke rights to view or modify the object or information. If the owner of an object or information does not have rights to exclude access to an object or information at a user level, users may gain access to objects and information they are not authorized to view/modify.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine if users are able to assign and revoke rights to the objects and information that they own. If users cannot assign or revoke rights to the objects and information that they own to groups, roles, or individual users, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237705`

### Rule: A single database connection configuration file must not be used to configure all database clients.

**Rule ID:** `SV-237705r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Many sites distribute a single client database connection configuration file to all site database users that contains network access information for all databases on the site. Such a file provides information to access databases not required by all users that may assist in unauthorized access attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for providing database connection information to users/user workstations. If procedures do not indicate or implement restrictions to connections required by the particular user, this is a finding. Note: This check is specific for the DBMS host system and not directed at client systems (client systems are included in the Application STIG/Checklist); however, detection of unauthorized client connections to the DBMS host system obtained through log files should be performed regularly and documented where authorized.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-237706`

### Rule: The DBMS must be protected from unauthorized access by developers.

**Rule ID:** `SV-237706r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Developers granted elevated database and/or operating system privileges on production databases can affect the operation and/or security of the database system. Operating system and database privileges assigned to developers on production systems must not be allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the production system to ensure no developer accounts have rights to modify the production database structure or alter production data. If developer accounts with these rights exist, ask for documentation that shows these accounts have formal approval and risk acceptance. If this documentation does not exist, this is a finding. If developer accounts exist with the right to create and maintain tables (or other database objects) in production tablespaces, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237707`

### Rule: The DBMS must be protected from unauthorized access by developers on shared production/development host systems.

**Rule ID:** `SV-237707r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Developers granted elevated database and/or operating system privileges on systems that support both development and production databases can affect the operation and/or security of the production database system. Operating system and database privileges assigned to developers on shared development and production systems must be restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify whether any hosts contain both development and production databases. If no hosts contain both production and development databases, this is NA. For any host containing both a development and a production database, determine if developers have been granted elevated privileges on the production database or on the OS. If they have, ask for documentation that shows these accounts have formal approval and risk acceptance. If this documentation does not exist, this is a finding. If developer accounts exist with the right to create and maintain tables (or other database objects) in production tablespaces, this is a finding. (Where applicable, to check the number of instances on the host machine, check the /etc/oratab. The /etc/oratab file is updated by the Oracle Installer when the database is installed when the root.sh file is executed. Each line in the represents an ORACLE_SID:ORACLE_HOME:Y or N. The ORACLE_SID and ORACLE_HOME are self-explanatory. The Y or N signals the DBSTART program to automatically start or not start that specific instance when the machine is restarted. Check with the system owner and application development team to see what each entry represents. If a system is deemed to be a production system, review the system for development users.)

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-237708`

### Rule: The DBMS must restrict access to system tables and other configuration information or metadata to DBAs or other authorized users.

**Rule ID:** `SV-237708r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Administrative data includes DBMS metadata and other configuration and management data. Unauthorized access to this data could result in unauthorized changes to database objects, access controls, or DBMS configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review user privileges to system tables and configuration data stored in the Oracle database. If non-DBA users are assigned privileges to access system tables and tables containing configuration data, this is a finding. To obtain a list of users and roles that have been granted access to any dictionary table, run the query: SELECT unique grantee from dba_tab_privs where table_name in (select table_name from dictionary) order by grantee; To obtain a list of dictionary tables and assigned privileges granted to a specific user or role, run the query: SELECT grantee, table_name, privilege from dba_tab_privs where table_name in (select table_name from dictionary) and grantee = '<applicable account>';

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-237709`

### Rule: Administrative privileges must be assigned to database accounts via database roles.

**Rule ID:** `SV-237709r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Privileges granted outside the context of the application user job function are more likely to go unmanaged or without oversight for authorization. Maintenance of privileges using roles defined for discrete job functions offers improved oversight of application user privilege assignments and helps to protect against unauthorized privilege assignment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review accounts for direct assignment of administrative privileges. Connected as SYSDBA, run the query: SELECT grantee, privilege FROM dba_sys_privs WHERE grantee IN ( SELECT username FROM dba_users WHERE username NOT IN ( 'XDB', 'SYSTEM', 'SYS', 'LBACSYS', 'DVSYS', 'DVF', 'SYSMAN_RO', 'SYSMAN_BIPLATFORM', 'SYSMAN_MDS', 'SYSMAN_OPSS', 'SYSMAN_STB', 'DBSNMP', 'SYSMAN', 'APEX_040200', 'WMSYS', 'SYSDG', 'SYSBACKUP', 'SPATIAL_WFS_ADMIN_USR', 'SPATIAL_CSW_ADMIN_US', 'GSMCATUSER', 'OLAPSYS', 'SI_INFORMTN_SCHEMA', 'OUTLN', 'ORDSYS', 'ORDDATA', 'OJVMSYS', 'ORACLE_OCM', 'MDSYS', 'ORDPLUGINS', 'GSMADMIN_INTERNAL', 'MDDATA', 'FLOWS_FILES', 'DIP', 'CTXSYS', 'AUDSYS', 'APPQOSSYS', 'APEX_PUBLIC_USER', 'ANONYMOUS', 'SPATIAL_CSW_ADMIN_USR', 'SYSKM', 'SYSMAN_TYPES', 'MGMT_VIEW', 'EUS_ENGINE_USER', 'EXFSYS', 'SYSMAN_APM' ) ) AND privilege NOT IN ('UNLIMITED TABLESPACE' , 'REFERENCES', 'INDEX', 'SYSDBA', 'SYSOPER' ) ORDER BY 1, 2; If any administrative privileges have been assigned directly to a database account, this is a finding. (The list of special accounts that are excluded from this requirement may not be complete. It is expected that the DBA will edit the list to suit local circumstances, adding other special accounts as necessary, and removing any that are not supposed to be in use in the Oracle deployment that is under review.)

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-237710`

### Rule: Administrators must utilize a separate, distinct administrative account when performing administrative activities, accessing database security functions, or accessing security-relevant information.

**Rule ID:** `SV-237710r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC), is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account. To limit exposure when operating from within a privileged account or role, the application must support organizational requirements that users of information system accounts, or roles, with access to organization-defined lists of security functions or security-relevant information, use non-privileged accounts, or roles, when accessing other (non-security) system functions. When privileged activities are not separated from non-privileged activities, the database can be subject to unauthorized changes to settings and data that a standard user would not normally have access to, outside of an authorized maintenance session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review permissions for objects owned by DBA or other administrative accounts. If any objects owned by administrative accounts can be accessed by non-DBA/non-administrative users, either directly or indirectly, this is a finding. Verify DBAs have separate administrative accounts. If DBAs do not have a separate account for database administration purposes, this is a finding. To list all objects owned by an administrative account that have had access granted to another account, run the query: SELECT grantee, table_name, grantor, privilege, type from dba_tab_privs where owner= '<applicable account>';

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-237712`

### Rule: OS accounts utilized to run external procedures called by the DBMS must have limited privileges.

**Rule ID:** `SV-237712r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC) is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account. To limit exposure when operating from within a privileged account or role, the application must support organizational requirements that users of information system accounts, or roles, with access to organization-defined lists of security functions or security-relevant information, use non-privileged accounts, or roles, when accessing other (non-security) system functions. Use of privileged accounts for non-administrative purposes puts data at risk of unintended or unauthorized loss, modification, or exposure. In particular, DBA accounts if used for non-administration application development or application maintenance can lead to miss-assignment of privileges where privileges are inherited by object owners. It may also lead to loss or compromise of application data where the elevated privileges bypass controls designed in and provided by applications. External applications called or spawned by the DBMS process may be executed under OS accounts with unnecessary privileges. This can lead to unauthorized access to OS resources and compromise of the OS, the DBMS or any other services provided by the host platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine which OS accounts are used by the DBMS to run external procedures. Validate that these OS accounts have only the privileges necessary to perform the required functionality. If any OS accounts, utilized by the database for running external procedures, have privileges beyond those required for running the external procedures, this is a finding. If use of the external procedure agent is authorized, ensure extproc is restricted to execution of authorized applications. External jobs are run using the account nobody by default. Review the contents of the file ORACLE_HOME/rdbms/admin/externaljob.ora for the lines run_user= and run_group=. If the user assigned to these parameters is not "nobody", this is a finding. System views providing privilege information are: DBA_SYS_PRIVS DBA_TAB_PRIVS DBA_ROLE_PRIVS

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237713`

### Rule: The DBMS must verify account lockouts persist until reset by an administrator.

**Rule ID:** `SV-237713r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed, to allow for the utilization of an application, there is a risk that attempts will be made to obtain unauthorized access. To defeat these attempts, organizations define the number of times a user account may consecutively fail a logon attempt. The organization also defines the period of time in which these consecutive failed attempts may occur. By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The account lockout duration is defined in the profile assigned to a user. To see what profile is assigned to a user, enter the query: SQL>SELECT profile FROM dba_users WHERE username = '<username>' This will return the profile name assigned to that user. The user profile, ORA_STIG_PROFILE, has been provided (starting with Oracle 12.1.0.2) to satisfy the STIG requirements pertaining to the profile parameters. Oracle recommends that this profile be customized with any site-specific requirements and assigned to all users where applicable. Note: It remains necessary to create a customized replacement for the password validation function, ORA12C_STRONG_VERIFY_FUNCTION, if relying on this technique to verify password complexity. Now check the values assigned to the profile returned from the query above: column profile format a20 column limit format a20 SQL>SELECT PROFILE, RESOURCE_NAME, LIMIT FROM DBA_PROFILES WHERE PROFILE = 'ORA_STIG_PROFILE'; Check the settings for password_lock_time - this specifies how long to lock the account after the number of consecutive failed logon attempts reaches the limit. If the value is not UNLIMITED, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237714`

### Rule: The DBMS must set the maximum number of consecutive invalid logon attempts to three.

**Rule ID:** `SV-237714r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed, to allow for the utilization of an application, there is a risk that attempts will be made to obtain unauthorized access. To defeat these attempts, organizations define the number of times a user account may consecutively fail a logon attempt. The organization also defines the period of time in which these consecutive failed attempts may occur. By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. More recent brute force attacks make attempts over long periods of time to circumvent intrusion detection systems and system account lockouts based entirely on the number of failed logons that are typically reset after a successful logon. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Note also that a policy that places no limit on the length of the timeframe (for counting consecutive invalid attempts) does satisfy this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The limit on the number of consecutive failed logon attempts is defined in the profile assigned to a user. Check the FAILED_LOGIN_ATTEMPTS value assigned to the profiles returned from this query: SQL>SELECT PROFILE, RESOURCE_NAME, LIMIT FROM DBA_PROFILES; Check the setting for FAILED_LOGIN_ATTEMPTS - this is the number of consecutive failed logon attempts before locking the Oracle user account. If the value is greater than three on any of the profiles, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-237715`

### Rule: Databases utilizing Discretionary Access Control (DAC) must enforce a policy that limits propagation of access rights.

**Rule ID:** `SV-237715r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the premise that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. DAC models have the potential for the access controls to propagate without limit, resulting in unauthorized access to said objects. When applications provide a discretionary access control mechanism, the application must be able to limit the propagation of those access rights. The DBMS must ensure the recipient of permissions possesses only the access intended. The database must enforce the ability to limit rights propagation if that is the intent of the grantor. If the propagation of access rights is not limited, users with rights to objects they do not own can continue to grant rights to those objects to other users without limit. This is default behavior for Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBMS has the ability to grant permissions without the grantee receiving the right to grant those same permissions to another user. Review organization policies regarding access propagation. If an access propagation policy limiting the propagation of rights does not exist, this is a finding. Review DBMS configuration to verify access propagation policies are enforced by the DBMS as configured. If the DBMS does not enforce the access propagation policy, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-237716`

### Rule: A DBMS utilizing Discretionary Access Control (DAC) must enforce a policy that includes or excludes access to the granularity of a single user.

**Rule ID:** `SV-237716r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAC is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. Including or excluding access to the granularity of a single user means providing the capability to either allow or deny access to objects (e.g., files, folders) on a per single user basis. Databases using DAC must have the ability for the owner of an object or information to assign or revoke rights to view or modify the object or information. If the owner of an object or information does not have rights to exclude access to an object or information at a user level, users may gain access to objects and information they are not authorized to view/modify.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and documentation to determine if users are able to assign and revoke rights to the objects and information they own. If users cannot assign or revoke rights to the objects and information they own to the granularity of a single user, this is a finding. (This is default Oracle behavior.)

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-237717`

### Rule: The DBMS itself, or the logging or alerting mechanism the application utilizes, must provide a warning when allocated audit record storage volume reaches an organization-defined percentage of maximum audit record storage capacity.

**Rule ID:** `SV-237717r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Audit processing failures include: software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. If audit log capacity were to be exceeded, then events subsequently occurring would not be recorded. Organizations shall define a maximum allowable percentage of storage capacity serving as an alarming threshold (e.g., application has exceeded 80% of log storage capacity allocated) at which time the application or the logging mechanism the application utilizes will provide a warning to the appropriate personnel. A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. This can be an alert provided by the database, a log repository, or the OS when a designated log directory is nearing capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS, OS, or third-party logging application settings to determine whether a warning will be provided when a specific percentage of log storage capacity is reached. If no warning will be provided, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-237718`

### Rule: The system must provide a real-time alert when organization-defined audit failure events occur.

**Rule ID:** `SV-237718r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Audit processing failures include: software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. If audit log capacity were to be exceeded, then events subsequently occurring would not be recorded. Organizations shall define a maximum allowable percentage of storage capacity serving as an alarming threshold (e.g., application has exceeded 80% of log storage capacity allocated) at which time the application or the logging mechanism the application utilizes will provide a warning to the appropriate personnel. A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. This can be an alert provided by the database, a log repository, or the OS when a designated log directory is nearing capacity. If Oracle Enterprise Manager is in use, the capability to issue such an alert is built in and configurable via the console so an alert can be sent to a designated administrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Oracle Corp., OS, or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-237719`

### Rule: The DBMS must support enforcement of logical access restrictions associated with changes to the DBMS configuration and to the database itself.

**Rule ID:** `SV-237719r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with access restrictions pertaining to change control, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals must be allowed to obtain access to application components for the purposes of initiating changes, including upgrades and modifications. Modifications to the DBMS settings, the database files, database configuration files, or the underlying database application files themselves could have catastrophic consequences to the database. Modification to DBMS settings could include turning off access controls to the database, the halting of archiving, the halting of auditing, and any number of other malicious actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings and vendor documentation to ensure the database supports and does not interfere with enforcement of logical access restrictions associated with changes to the DBMS configuration and to the database itself. If the DBMS software in any way restricts the implementation of logical access controls implemented to protect its integrity or availability, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237720`

### Rule: Database backup procedures must be defined, documented, and implemented.

**Rule ID:** `SV-237720r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. User-level information is data generated by information system and/or application users. In order to assure availability of this data in the event of a system failure, DoD organizations are required to ensure user-generated data is backed up at a defined frequency. This includes data stored on file systems, within databases or within any other storage media. Applications performing backups must be capable of backing up user-level information per the DoD-defined frequency. Database backups provide the required means to restore databases after compromise or loss. Backups help reduce the vulnerability to unauthorized access or hardware loss.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the database backup procedures and implementation evidence. Evidence of implementation includes records of backup events and physical review of backup media. Evidence should match the backup plan as recorded in the system documentation. If backup procedures do not exist or are not implemented in accordance with the procedures, this is a finding. - - - - - The Oracle recommended process for backup and recovery is Oracle RMAN. If Oracle RMAN is deployed, execute the following commands to ensure that the evidence of the implementation of the backup policy includes validating that the files are restorable: Validating Database Files with BACKUP VALIDATE --Use the BACKUP VALIDATE command to do the following: --Check datafiles for physical and logical block corruption --Confirm that all database files exist and are in the correct locations --When BACKUP VALIDATE is run, RMAN reads the files to be backed up in their entirety, as it would during a real backup. RMAN does not, however, actually produce any backup sets or image copies. --Cannot use the BACKUPSET, MAXCORRUPT, or PROXY parameters with BACKUP VALIDATE. --To validate files with the BACKUP VALIDATE command: 1. Start RMAN and connect to a target database and recovery catalog (if used). 2. Run the BACKUP VALIDATE command. For example, can validate that all database files and archived logs can be backed up by running a command as shown in the following example. This command checks for physical corruptions only. BACKUP VALIDATE DATABASE ARCHIVELOG ALL; To check for logical corruptions in addition to physical corruptions, run the following variation of the preceding command: BACKUP VALIDATE CHECK LOGICAL DATABASE ARCHIVELOG ALL; In the preceding examples, the RMAN client displays the same output that it would if it were really backing up the files. If RMAN cannot back up one or more of the files, then it issues an error message. Validating Backups Before Restoring Them Run RESTORE ... VALIDATE to test whether RMAN can restore a specific file or set of files from a backup. RMAN chooses which backups to use. The database must be mounted or open for this command. Do not have to take datafiles off-line when validating the restore of datafiles, because validation of backups of the datafiles only reads the backups and does not affect the production datafiles. When validating files on disk or tape, RMAN reads all blocks in the backup piece or image copy. RMAN also validates off-site backups. The validation is identical to a real restore operation except that RMAN does not write output files. To validate backups with the RESTORE command: 1. Run the RESTORE command with the VALIDATE option. This following example illustrates validating the restore of the database and all archived redo logs: RESTORE DATABASE VALIDATE; RESTORE ARCHIVELOG ALL VALIDATE; If an RMAN error stack is not generated, then skip the subsequent steps. The lack of error messages means that RMAN had confirmed that it can use these backups successfully during a real restore and recovery. 2. If error messages are seen in the output and one is the RMAN-06026 message, then investigate the cause of the problem. If possible, correct the problem that is preventing RMAN from validating the backups and retry the validation. The following error means that RMAN cannot restore one or more of the specified files from available backups: RMAN-06026: some targets not found - aborting restore The following sample output shows that RMAN encountered a problem reading the specified backup: RMAN-03009: failure of restore command on c1 channel at 12-DEC-14 23:22:30 ORA-19505: failed to identify file "oracle/dbs/1fafv9gl_1_1" ORA-27037: unable to obtain file status SVR4 Error: 2: No such file or directory Additional information: 3

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237721`

### Rule: Database recovery procedures must be developed, documented, implemented, and periodically tested.

**Rule ID:** `SV-237721r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. User-level information is data generated by information system and/or application users. In order to assure availability of this data in the event of a system failure, DoD organizations are required to ensure user-generated data is backed up at a defined frequency. This includes data stored on file systems, within databases or within any other storage media. Applications performing backups must be capable of backing up user-level information per the DoD-defined frequency. Problems with backup procedures or backup media may not be discovered until after a recovery is needed. Testing and verification of procedures provides the opportunity to discover oversights, conflicts, or other issues in the backup procedures or use of media designed to be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the testing and verification procedures documented in the system documentation. Review evidence of implementation of testing and verification procedures by reviewing logs from backup and recovery implementation. Logs may be in electronic form or hardcopy and may include email or other notification. If testing and verification of backup and recovery procedures is not documented in the system documentation, this is a finding. If evidence of testing and verification of backup and recovery procedures does not exist, this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-237722`

### Rule: DBMS backup and restoration files must be protected from unauthorized access.

**Rule ID:** `SV-237722r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. User-level information is data generated by information system and/or application users. In order to assure availability of this data in the event of a system failure, DoD organizations are required to ensure user-generated data is backed up at a defined frequency. This includes data stored on file systems, within databases or within any other storage media. Applications performing backups must be capable of backing up user-level information per the DoD-defined frequency. Lost or compromised DBMS backup and restoration files may lead to not only the loss of data, but also the unauthorized access to sensitive data. Backup files need the same protections against unauthorized access when stored on backup media as when online and actively in use by the database system. In addition, the backup media needs to be protected against physical loss. Most DBMS's maintain online copies of critical control files to provide transparent or easy recovery from hard disk loss or other interruptions to database operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review file protections assigned to online backup and restoration files. Review access protections and procedures for off-line backup and restoration files. If backup or restoration files are subject to unauthorized access, this is a finding. It may be necessary to review backup and restoration procedures to determine ownership and access during all phases of backup and recovery.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-237723`

### Rule: The DBMS must use multifactor authentication for access to user accounts.

**Rule ID:** `SV-237723r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Multifactor authentication is defined as using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). The DBMS must be configured to automatically utilize organization-level account management functions, and these functions must immediately enforce the organization's current account policy. The lack of multifactor authentication makes it much easier for an attacker to gain unauthorized access to a system. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names that include "SSL", such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS. Use authentication to prove the identities of users who are attempting to log on to the database. Oracle Database enables strong authentication with Oracle authentication adapters that support various third-party authentication services, including TLS with digital certificates, as well as Smart Cards (CAC, PIV).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the organization-level authentication/access mechanism and not by the DBMS, this is not a finding. Review DBMS settings, OS settings, and/or enterprise-level authentication/access mechanism settings to determine whether user accounts are required to use multifactor authentication. If user accounts are not required to use multifactor authentication, this is a finding. If the $ORACLE_HOME/network/admin/sqlnet.ora contains entries similar to the following, TLS is enabled. (Note: This assumes that a single sqlnet.ora file, in the default location, is in use. Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.) SQLNET.AUTHENTICATION_SERVICES= (BEQ, TCPS) SSL_VERSION = 1.2 SSL_CLIENT_AUTHENTICATION = TRUE WALLET_LOCATION = (SOURCE = (METHOD = FILE) (METHOD_DATA = (DIRECTORY = /u01/app/oracle/product/12.1.0/dbhome_1/owm/wallets) ) ) SSL_CIPHER_SUITES= (SSL_RSA_WITH_AES_256_CBC_SHA384) ADR_BASE = /u01/app/oracle

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-237724`

### Rule: The DBMS must ensure users are authenticated with an individual authenticator prior to using a shared authenticator.

**Rule ID:** `SV-237724r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, application users (and any processes acting on behalf of users) must be individually identified and authenticated. A shared authenticator is a generic account used by multiple individuals. Use of a shared authenticator alone does not uniquely identify individual users. An example of a shared authenticator is the UNIX OS 'root' user account, a Windows 'administrator' account, an 'SA' account, or a 'helpdesk' account. For example, the UNIX and Windows operating systems offer a 'switch user' capability allowing users to authenticate with their individual credentials and, when needed, 'switch' to the administrator role. This method provides for unique individual authentication prior to using a shared authenticator. Some applications may not have the need to provide a group authenticator; this is considered a matter of application design. In those instances where the application design includes the use of a shared authenticator, this requirement will apply. There may also be instances when specific user actions need to be performed on the information system without unique user identification or authentication. An example of this type of access is a web server which contains publicly releasable information. These types of accesses are allowed but must be explicitly identified and documented by the organization. When shared accounts are utilized without another means of identifying individual users, users may deny having performed a particular action.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings, OS settings, and/or enterprise-level authentication/access mechanism settings to determine whether shared accounts exist. If group accounts do not exist, this is NA. Review DBMS settings to determine if individual authentication is required before shared authentication. If shared authentication does not require prior individual authentication, this is a finding. (Oracle Access Manager may be helpful in meeting this requirement. Notes on Oracle Access Manager follow.) Oracle Access Manager is used when there is a need for multifactor authentication of applications front-ending Oracle Datasets that may use group accounts. Oracle Access Manager supports using PKI-based smart cards (CAC, PIV) for multifactor authentication. When a user authenticates to a smart card application, the smart card engine produces a certificate-based authentication token. Can configure a certificate-based authentication scheme in Oracle Access Manager that uses information from the smart card certificate. Certificate-based authentication works with any smart card or similar device that presents an X.509 certificate. Check: First, check that the Authentication Module is set up properly: 1) Go to Oracle Access Manager Home Screen and click the Policy Configuration tab. Select the X509Scheme. 2) Make sure the Authentication Module option is set to X509Plugin. Second, check that the Authentication policy is using the x509Scheme: 1) Go to Oracle Access Manager Home Screen and click the Policy Configuration tab. 2) Select Application Domains. Select Search. 3) Select the application domain protecting the Oracle Database. 4) Select the Authentication Polices tab and Click Protected Resource Policy. 5) Make sure the Authentication Scheme is set to x509Scheme.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237725`

### Rule: The DBMS must disable user accounts after 35 days of inactivity.

**Rule ID:** `SV-237725r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive DBMS account can potentially obtain and maintain undetected access to the database. Owners of inactive DBMS accounts will not notice if unauthorized access to their user account has been obtained. All DBMS need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. To address access requirements, some database administrators choose to integrate their databases with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the database administrator to off-load those access control functions and focus on core application features and functionality. This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local logon administrator accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For accounts managed by Oracle, check DBMS settings to determine if accounts are automatically disabled by the system after 35 days of inactivity. In Oracle 12c, Oracle introduced a new security parameter in the profile called INACTIVE_ACCOUNT_TIME. The INACTIVE_ACCOUNT_TIME parameter specifies the number of days permitted the account will be in OPEN state since the last login, after that will be LOCKED if no successful logins happens after the specified duration. Check to see what profile each user is associated with, if any, with this query: select username, profile from dba_users order by 1,2; Then check the profile to see what the inactive_account_time is set to in the table dba_profiles; the inactive_account_time is a value stored in the LIMIT column, and identified by the value inactive_account_time in the RESOURCE_NAME column. SQL>select profile, resource_name, resource_type, limit from dba_profiles where upper(resource_name) = 'INACTIVE_ACCOUNT_TIME'; If the INACTIVE_ACCOUNT_TIME parameter is set to UNLIMITED (default) or it is set to more than 35 days, this is a finding. If INACTIVE_ACCOUNT_TIME is not a parameter associated with the profile then check for a script or an automated job that is run daily that checks the audit trail or other means to make sure every user account has logged in within the last 35 days. If one is not present, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237726`

### Rule: The DBMS must support organizational requirements to enforce minimum password length.

**Rule ID:** `SV-237726r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. Weak passwords are a primary target for attack to gain unauthorized access to databases and other systems. Where username/password is used for identification and authentication to the database, requiring the use of strong passwords can help prevent simple and more sophisticated methods for guessing at passwords. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the DoD-defined minimum length (15 unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237727`

### Rule: The DBMS must support organizational requirements to prohibit password reuse for the organization-defined number of generations.

**Rule ID:** `SV-237727r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. Password reuse restrictions protect against bypass of password expiration requirements and help protect accounts from password guessing attempts. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password reuse rule, if any, that is in effect: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME IN ('PASSWORD_REUSE_MAX', 'PASSWORD_REUSE_TIME') [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE, RESOURCE_NAME; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the value of the PASSWORD_REUSE_MAX effective for each profile. If, for any profile, the PASSWORD_REUSE_MAX value does not enforce the DoD-defined minimum number of password changes before a password may be repeated (five or greater), this is a finding. PASSWORD_REUSE_MAX is effective if and only if PASSWORD_REUSE_TIME is specified, so if both are UNLIMITED, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237728`

### Rule: The DBMS must support organizational requirements to enforce password complexity by the number of upper-case characters used.

**Rule ID:** `SV-237728r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Use of a complex password helps to increase the time and resources required to compromise the password. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the organization-defined minimum number of upper-case characters (1 unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237729`

### Rule: The DBMS must support organizational requirements to enforce password complexity by the number of lower-case characters used.

**Rule ID:** `SV-237729r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Use of a complex password helps to increase the time and resources required to compromise the password. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the organization-defined minimum number of lower-case characters (1 unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237730`

### Rule: The DBMS must support organizational requirements to enforce password complexity by the number of numeric characters used.

**Rule ID:** `SV-237730r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Use of a complex password helps to increase the time and resources required to compromise the password. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the organization-defined minimum number of numeric characters (1 unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237731`

### Rule: The DBMS must support organizational requirements to enforce password complexity by the number of special characters used.

**Rule ID:** `SV-237731r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity or strength is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Use of a complex password helps to increase the time and resources required to compromise the password. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the organization-defined minimum number of special characters (1 unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237732`

### Rule: The DBMS must support organizational requirements to enforce the number of characters that get changed when passwords are changed.

**Rule ID:** `SV-237732r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse extensive portions of their password when they change their password, the end result is a password that has not had enough elements changed to meet the policy requirements. Changing passwords frequently can thwart password-guessing attempts or re-establish protection of a compromised DBMS account. Minor changes to passwords may not accomplish this since password guessing may be able to continue to build on previous guesses, or the new password may be easily guessed using the old password. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function, if any, that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' [AND PROFILE NOT IN (<list of non-applicable profiles>)] ORDER BY PROFILE; Bearing in mind that a profile can inherit from another profile, and the root profile is called DEFAULT, determine the name of the password verification function effective for each profile. If, for any profile, the function name is null, this is a finding. For each password verification function, examine its source code. If it does not enforce the organization-defined minimum number of characters by which the password must differ from the previous password (eight of the characters unless otherwise specified), this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237733`

### Rule: Procedures for establishing temporary passwords that meet DoD password requirements for new accounts must be defined, documented, and implemented.

**Rule ID:** `SV-237733r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. New accounts authenticated by passwords that are created without a password or with an easily guessed password are vulnerable to unauthorized access. Procedures for creating new accounts with passwords should include the required assignment of a temporary password to be modified by the user upon first use. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP With respect to Oracle, this requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. Where accounts are authenticated using passwords, review procedures and implementation evidence for creation of temporary passwords. If the procedures or evidence do not exist or do not enforce passwords to meet DoD password requirements, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237734`

### Rule: DBMS passwords must not be stored in compiled, encoded, or encrypted batch jobs or compiled, encoded, or encrypted application source code.

**Rule ID:** `SV-237734r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. The storage of passwords in application source or batch job code that is compiled, encoded, or encrypted prevents compliance with password expiration and other management requirements, as well as provides another means for potential discovery. This requirement applies equally to those accounts managed by Oracle and those managed and authenticated by the OS or an enterprise-wide mechanism. This requirement should not be construed as prohibiting or discouraging the encryption of source code, which remains an advisable precaution. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including 'SSL', such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review application source code required to be encoded or encrypted for database accounts used by applications or batch jobs to access the database. Review source batch job code prior to compiling, encoding, or encrypting for database accounts used by applications or the batch jobs themselves to access the database. Determine if the compiled, encoded, or encrypted application source code or batch jobs contain passwords used for authentication to the database. If any of the identified compiled, encoded, or encrypted application source code or batch job code do contain passwords used for authentication to the database, this is a finding. - - - - - The check would depend on the information provided by the DBA. In a default Oracle installation, all passwords are stored in an encrypted manner. Ask the DBA if they have created an External Password Store for applications, batch jobs, and scripts to use. Secure External Password Store Can store password credentials for connecting to databases by using a client-side Oracle wallet. An Oracle wallet is a secure software container that stores authentication and signing credentials. This wallet usage can simplify large-scale deployments that rely on password credentials for connecting to databases. When this feature is configured, application code, batch jobs, and scripts no longer need embedded user names and passwords. This reduces risk because the passwords are no longer exposed, and password management policies are more easily enforced without changing application code whenever user names or passwords change. The external password store of the wallet is separate from the area where public key infrastructure (PKI) credentials are stored. Consequently, cannot use Oracle Wallet Manager to manage credentials in the external password store of the wallet. Instead, use the command-line utility mkstore to manage these credentials. How Does the External Password Store Work? Typically, users (and as applications, batch jobs, and scripts) connect to databases by using a standard CONNECT statement that specifies a database connection string. This string can include a user name and password, and an Oracle Net service name identifying the database on an Oracle Database network. If the password is omitted, the connection prompts the user for the password. For example, the service name could be the URL that identifies that database, or a TNS alias entered in the tnsnames.ora file in the database. Another possibility is a host:port:sid string. The following examples are standard CONNECT statements that could be used for a client that is not configured to use the external password store: CONNECT salesapp@sales_db.us.example.com Enter password: password CONNECT salesapp@orasales Enter password: password CONNECT salesapp@ourhost37:1527:DB17 Enter password: password In these examples, salesapp is the user name, with the unique connection string for the database shown as specified in three different ways. Could use its URL sales_db.us.example.com, or its TNS alias, orasales, from the tnsnames.ora file, or its host:port:sid string. However, when clients are configured to use the secure external password store, applications can connect to a database with the following CONNECT statement syntax, without specifying database logon credentials: CONNECT /@db_connect_string CONNECT /@db_connect_string AS SYSDBA CONNECT /@db_connect_string AS SYSOPER In this specification, db_connect_string is a valid connection string to access the intended database, such as the service name, URL, or alias as shown in the earlier examples. Each user account must have its own unique connection string; cannot create one connection string for multiple users. In this case, the database credentials, user name and password, are securely stored in an Oracle wallet created for this purpose. The autologon feature of this wallet is turned on, so the system does not need a password to open the wallet. From the wallet, it gets the credentials to access the database for the user they represent.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-237735`

### Rule: The DBMS must enforce password maximum lifetime restrictions.

**Rule ID:** `SV-237735r944384_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. The PASSWORD_LIFE_TIME parameter defines the number of days a password remains valid. This can must not be set to UNLIMITED. Further, the PASSWORD_GRACE_TIME parameter, if set to UNLIMITED, can nullify the PASSWORD_LIFE_TIME. PASSWORD_GRACE_TIME must be set to 0 days (or another small integer). Note: User authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. With respect to Oracle, this requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. Review DBMS settings to determine if passwords must be changed periodically. Run the following script: SELECT p1.profile, CASE DECODE(p1.limit, 'DEFAULT', p3.limit, p1.limit) WHEN 'UNLIMITED' THEN 'UNLIMITED' ELSE CASE DECODE(p2.limit, 'DEFAULT', p4.limit, p2.limit) WHEN 'UNLIMITED' THEN 'UNLIMITED' ELSE TO_CHAR(DECODE(p1.limit, 'DEFAULT', p3.limit, p1.limit) + DECODE(p2.limit, 'DEFAULT', p4.limit, p2.limit)) END END effective_life_time FROM dba_profiles p1, dba_profiles p2, dba_profiles p3, dba_profiles p4 WHERE p1.profile=p2.profile AND p3.profile='DEFAULT' AND p4.profile='DEFAULT' AND p1.resource_name='PASSWORD_LIFE_TIME' AND p2.resource_name='PASSWORD_GRACE_TIME' AND p3.resource_name='PASSWORD_LIFE_TIME' -- from DEFAULT profile AND p4.resource_name='PASSWORD_GRACE_TIME' -- from DEFAULT profile order by 1; If the EFFECTIVE_LIFE_TIME is greater than 60 for any profile applied to user accounts, and the need for this has not been documented and approved by the ISSO, this is a finding. If PASSWORD_LIFE_TIME or PASSWORD_GRACE_TIME is set to "UNLIMITED", this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-237738`

### Rule: The DBMS must terminate the network connection associated with a communications session at the end of the session or 15 minutes of inactivity.

**Rule ID:** `SV-237738r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. The act of managing systems and applications includes the ability to access sensitive application information, such as system configuration details, diagnostic information, user information, and potentially sensitive application data. When applications provide a remote management capability inherent to the application, the application needs to ensure all sessions and network connections are terminated when non-local maintenance is completed. When network connections are left open after the database session has closed, the network session is open to session hijacking. The Oracle Listener inherently meets most of this SRG requirement. When a user logs off, or times out, or encounters an unrecoverable network fault, the Oracle Listener terminates all sessions and network connections. The remaining aspect of the requirement, the timeout because of inactivity, is configurable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings, OS settings, and vendor documentation to verify network connections are terminated when a database communications session is ended or after 15 minutes of inactivity. If the network connection is not terminated, this is a finding. The defined duration for these timeouts 15 minutes, except to fulfill documented and validated mission requirements.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-237739`

### Rule: The DBMS must implement required cryptographic protections using cryptographic modules complying with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

**Rule ID:** `SV-237739r903015_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of cryptography to provide confidentiality and non-repudiation is not effective unless strong methods are employed. Many earlier encryption methods and modules have been broken and/or overtaken by increasing computing power. The NIST FIPS 140-2 or 140-3 cryptographic standards provide proven methods and strengths to employ cryptography effectively. Detailed information on the NIST Cryptographic Module Validation Program (CMVP) is available at: http://csrc.nist.gov/groups/STM/cmvp/index.html Note: this does not require that all databases be encrypted. It specifies that if encryption is required, then the implementation of the encryption must satisfy the prevailing standards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If encryption is not required for the database, this is not a finding. If the DBMS has not implemented federally required cryptographic protections for the level of classification of the data it contains, this is a finding. Check the following settings to verify FIPS 140-2 or 140-3 encryption is configured. If encryption is not configured, check with the DBA and SYSTEM Administrator to verify if other mechanisms or third-party products are deployed to encrypt data during the transmission or storage of data. For Transparent Data Encryption and DBMS_CRYPTO: To verify if Oracle is configured for FIPS 140 Transparent Data Encryption and/or DBMS_CRYPTO, enter the following SQL*Plus command: SHOW PARAMETER DBFIPS_140 or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'DBFIPS_140'; If Oracle returns the value 'FALSE', or returns no rows, this is a finding. To verify if Oracle is configured for FIPS 140 SSL/TLS authentication and/or Encryption: Verify the DBMS version: select * from V$VERSION; If the version displayed for Oracle Database is lower than 12.1.0.2, this is a finding. If the operating system is Windows and the DBMS version is 12.1.0.2, use the opatch command to display the patches applied to the DBMS. If the patches listed do not include "WINDOWS DB BUNDLE PATCH 12.1.0.2.7", this is a finding. Open the fips.ora file in a browser or editor. (The default location for fips.ora is $ORACLE_HOME/ldap/admin/ but alternate locations are possible. An alternate location, if it is in use, is specified in the FIPS_HOME environment variable.) If the line "SSLFIPS_140=TRUE" is not found in fips.ora, or the file does not exist, this is a finding. For (Native) Network Data Encryption: If the line, SQLNET.FIPS_140=TRUE is not found in $ORACLE_HOME/network/admin/sqlnet.ora, this is a finding. (Note: This assumes that a single sqlnet.ora file, in the default location, is in use. Please see the supplemental file "Non-default sqlnet.ora configurations.pdf" for how to find multiple and/or differently located sqlnet.ora files.) Note: For the Solaris platform, when DBFIPS_140 is FALSE, TDE (but not DBMS_CRYPTO) can still operate in a FIPS 140-compliant manner if FIPS 140 operation is enabled for the Solaris Cryptographic Framework.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237740`

### Rule: Database data files containing sensitive information must be encrypted.

**Rule ID:** `SV-237740r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. Data files that are not encrypted are vulnerable to theft. When data files are not encrypted they can be copied and opened on a separate system. The data can be compromised without the information owner's knowledge that the theft has even taken place.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database does not handle sensitive information, this is not a finding. Review the system documentation to determine whether the database handles classified information. If the database handles classified information, upgrade the severity Category Code to I. Review the system documentation to discover sensitive or classified data identified by the Information Owner that requires encryption. If no sensitive or classified data is identified as requiring encryption by the Information Owner, this is not a finding. Have the DBA use select statements in the database to review sensitive data stored in tables as identified in the system documentation. To see if Oracle is configured for FIPS 140 Transparent Data Encryption and/or DBMS_CRYPTO, enter the following SQL*Plus command: SHOW PARAMETER DBFIPS_140 or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'DBFIPS_140'; If Oracle returns the value 'FALSE', or returns no rows, this is a finding. To see if there are encrypted tablespaces, enter the following SQL*Plus command: SELECT * FROM V$ENCRYPTED_TABLESPACES; If no rows are returned, then there are no encrypted tablespaces. To see if there are encrypted columns within existing tables, enter the following SQL*Plus command: SELECT * FROM DBA_ENCRYPTED_COLUMNS; If no rows are returned, then there are no encrypted columns within existing tables. If all sensitive data identified is encrypted within the database objects, encryption of the DBMS data files is optional and not a finding. If all sensitive data is not encrypted within database objects, review encryption applied to the DBMS host data files. If no encryption is applied, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-237741`

### Rule: The DBMS must automatically terminate emergency accounts after an organization-defined time period for each type of account.

**Rule ID:** `SV-237741r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency application accounts are typically created due to an unforeseen operational event or could ostensibly be used in the event of a vendor support visit where a support representative requires a temporary unique account in order to perform diagnostic testing or conduct some other support-related activity. When these types of accounts are created, there is a risk that the temporary account may remain in place and active after the support representative has left. In the event emergency application accounts are required, the application must ensure accounts that are designated as temporary in nature shall automatically terminate these accounts after an organization-defined time period. Such a process and capability greatly reduces the risk that accounts will be misused, hijacked, or application data compromised. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. If it is possible for any temporary emergency accounts to be created and managed by Oracle, then the DBMS or application must provide or utilize a mechanism to automatically terminate such accounts after an organization-defined time period. Emergency database accounts must be automatically terminated after an organization-defined time period in order to mitigate the risk of the account being misused.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization has a policy, consistently enforced, forbidding the creation of emergency or temporary accounts, this is not a finding. Check DBMS settings, OS settings, and/or enterprise-level authentication/access mechanisms settings to determine if emergency accounts are being automatically terminated by the system after an organization-defined time period. Check also for custom code (scheduled jobs, procedures, triggers, etc.) for achieving this. If emergency accounts are not being terminated after an organization-defined time period, this is a finding.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-237742`

### Rule: The DBMS must protect against or limit the effects of organization-defined types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-237742r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A variety of technologies exist to limit, or in some cases, eliminate the effects of DoS attacks. For example, boundary protection devices can filter certain types of packets to protect devices on an organization's internal network from being directly affected by DoS attacks. Employing increased capacity and bandwidth combined with service redundancy may reduce the susceptibility to some DoS attacks. Some of the ways databases can limit their exposure to DoS attacks are through limiting the number of connections that can be opened by a single user and database clustering.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS settings to verify the DBMS implements measures to limit the effects of the organization-defined types of Denial of Service (DoS) attacks. If measures have not been implemented, this is a finding. Check the $ORACLE_HOME/network/admin/listener.ora to see if a Rate Limit has been established. A rate limit is used to prevent denial of service (DOS) attacks on a database or to control a logon storm such as may be caused by an application server reboot. - - - - - Example of a listener configuration with rate limiting in effect: CONNECTION_RATE_LISTENER=10 LISTENER= (ADDRESS_LIST= (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=yes)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=yes)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1526)) ) LISTENER= (ADDRESS_LIST= (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=8)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=12)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1526)) )

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-237743`

### Rule: The system must verify there have not been unauthorized changes to the DBMS software and information.

**Rule ID:** `SV-237743r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to employ integrity verification applications on information systems to look for evidence of information tampering, errors, and omissions. The organization is also required to employ good software engineering practices with regard to commercial off-the-shelf integrity mechanisms (e.g., parity checks, cyclical redundancy checks, and cryptographic hashes), and to use tools to automatically monitor the integrity of the information system and the applications it hosts. The DBMS opens data files and reads configuration files at system startup, system shutdown, and during abort recovery efforts. If the DBMS does not verify the trustworthiness of these files, it is vulnerable to malicious alterations of its configuration or unauthorized replacement of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBMS system initialization/parameter files and software is included in the configuration of any third-party software or custom scripting at the OS level to perform integrity verification. If neither a third-party application nor the OS is performing integrity verification of DBMS system files, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-237745`

### Rule: Use of the DBMS software installation account must be restricted.

**Rule ID:** `SV-237745r879586_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC), is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and non-privileged account. To limit exposure when operating from within a privileged account or role, the application must support organizational requirements that users of information system accounts, or roles, with access to organization-defined lists of security functions or security-relevant information, use non-privileged accounts, or roles, when accessing other (non-security) system functions. Use of privileged accounts for non-administrative purposes puts data at risk of unintended or unauthorized loss, modification, or exposure. In particular, DBA accounts if used for non-administration application development or application maintenance can lead to miss-assignment of privileges where privileges are inherited by object owners. It may also lead to loss or compromise of application data where the elevated privileges bypass controls designed in and provided by applications. The DBMS software installation account may require privileges not required for database administration or other functions. Use of accounts configured with excess privileges may result in the loss or compromise of data or system settings due to elevated privileges that bypass controls designed to protect them. This requirement is particularly important because Oracle equates the installation account with the SYS account - the super-DBA. Once logged on to the operating system, this account can connect to the database AS SYSDBA without further authentication. It is very powerful and, by virtue of not being linked to any one person, cannot be audited to the level of the individual.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify the installation account. Verify whether the account is used for anything involving interactive activity beyond DBMS software installation, upgrade, and maintenance actions. If the account is used for anything involving interactive activity beyond DBMS software installation, upgrade, and maintenance actions, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-237746`

### Rule: The OS must limit privileges to change the DBMS software resident within software libraries (including privileged programs).

**Rule ID:** `SV-237746r917648_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. If the application were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. This requirement is contingent upon the language in which the application is programmed, as many application architectures in use today incorporate their software libraries into, and make them inseparable from, their compiled distributions, rendering them static and version-dependent. However, this requirement does apply to applications with software libraries accessible and configurable as in the case of interpreted languages. Accordingly, only qualified and authorized individuals shall be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. The DBMS software libraries contain the executables used by the DBMS to operate. Unauthorized access to the libraries can result in malicious alteration. This may in turn jeopardize data stored in the DBMS and/or operation of the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review permissions that control access to the DBMS software libraries. The software library location may be determined from vendor documentation or service/process executable paths. Typically, only the DBMS software installation/maintenance account or SA account requires access to the software library for operational support such as backups. Any other accounts should be scrutinized and the reason for access documented. Accounts should have the least amount of privilege required to accompTypically, only the DBMS software installation/maintenance account or SA account requires access to the software library for operational support such as backups. Any other accounts should be scrutinized and the reason for access documented. Accounts should have the least amount of privilege required to accomplish the job. Below is one example for how to review accounts with access to software libraries for a Linux-based system: cat /etc/group |grep -i dba --Example output: dba:x:102: --take above number and input in below grep command cat /etc/passwd |grep 102 If any accounts are returned that are not required and authorized to have access to the software library location do have access, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-237747`

### Rule: Oracle Database must off-load audit data to a separate log management facility; this must be continuous and in near-real-time for systems with a network connection to the storage facility, and weekly or more often for stand-alone systems.

**Rule ID:** `SV-237747r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, files in the file system, other kinds of local repositories, or a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are off-loaded. If the DBMS has a continuous network connection to the centralized log management system, but the DBMS audit records are not written directly to the centralized log management system or transferred in near-real-time, this is a finding. If the DBMS does not have a continuous network connection to the centralized log management system, and the DBMS audit records are not transferred to the centralized log management system weekly or more often, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-251802`

### Rule: Oracle database products must be a version supported by the vendor.

**Rule ID:** `SV-251802r944386_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and interview the database administrator. Identify all database software components. Review the version and release information. From SQL*Plus: Select version from v$instance; Access the vendor website or use other means to verify the version is still supported. Oracle Release schedule: https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html If the Oracle version or any of the software components are not supported by the vendor, this is a finding.

