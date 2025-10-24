# STIG Benchmark: Oracle Database 19c Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-270495`

### Rule: Oracle Database must limit the number of concurrent sessions for each system account to an organization-defined number of sessions.

**Rule ID:** `SV-270495r1115953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions using a database management system (DBMS). Unlimited concurrent connections to the DBMS could allow a successful denial-of-service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, two might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Retrieve the settings for concurrent sessions for each profile with the query: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'SESSIONS_PER_USER'; If the DBMS settings for concurrent sessions for each profile are greater than the site-specific maximum number of sessions, this is a finding.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-270496`

### Rule: Oracle Database must protect against or limit the effects of organization-defined types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-270496r1064766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A variety of technologies exist to limit, or in some cases, eliminate the effects of DoS attacks. For example, boundary protection devices can filter certain types of packets to protect devices on an organization's internal network from being directly affected by DoS attacks. Employing increased capacity and bandwidth combined with service redundancy may reduce the susceptibility to some DoS attacks. Some of the ways databases can limit their exposure to DoS attacks are through limiting the number of connections that can be opened by a single user and database clustering.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review database management system (DBMS) settings to verify the DBMS implements measures to limit the effects of the organization-defined types of DoS attacks. Check the $ORACLE_HOME/network/admin/listener.ora to verify a Rate Limit has been established. A rate limit is used to prevent DoS attacks on a database or to control a logon storm such as may be caused by an application server reboot. If a rate limit has not been set similar to the example below, this is a finding. - - - - - Example of a listener configuration with rate limiting in effect: CONNECTION_RATE_LISTENER=10 LISTENER= (ADDRESS_LIST= (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=yes)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=yes)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1526)) ) LISTENER= (ADDRESS_LIST= (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1521)(RATE_LIMIT=8)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1522)(RATE_LIMIT=12)) (ADDRESS=(PROTOCOL=tcp)(HOST=)(PORT=1526)) )

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-270497`

### Rule: Oracle Database must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-270497r1064769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance. Satisfies: SRG-APP-000295-DB-000305, SRG-APP-000296-DB-000306</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If no documentation exists or an automatic session termination time is not explicitly defined, assume a time of 15 minutes. To check the max_idle_time set, run the following query: SELECT VALUE FROM V$PARAMETER WHERE NAME = 'max_idle_time'; If the value returned does not match the documented requirement (or 15 when none is specified), this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-270498`

### Rule: Oracle Database must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-270498r1064772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for the database management system (DBMS) to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling, or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. Some DBMS systems provide the feature to assign security labels to data elements. If labeling is required, implementation options include the Oracle Label Security package, or a third-party product, or custom-developed functionality. The confidentiality and integrity of the data depends upon the security label assignment where this feature is in use. Satisfies: SRG-APP-000311-DB-000308, SRG-APP-000313-DB-000309, SRG-APP-000314-DB-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If no data has been identified as being sensitive or classified in the system documentation, this is not a finding. If security labeling is not required, this is not a finding. If security labeling requirements have been specified, but the security labeling is not implemented or does not reliably maintain labels on information in storage, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-270499`

### Rule: Oracle Database must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-270499r1064775_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make account management for applications and databases challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. Managing accounts for the same person in multiple places is inefficient and prone to problems with consistency and synchronization. A comprehensive application account management process that includes automation helps to ensure that accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to act on multiple accounts designated as inactive, suspended, or terminated, or by disabling accounts located in noncentralized account stores, such as multiple servers. Account management functions can also include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephone notification to report atypical system account usage. Oracle Database must be configured to automatically use organization-level account management functions, and these functions must immediately enforce the organization's current account policy. Automation may be comprised of differing technologies that when placed together contain an overall mechanism supporting an organization's automated account management requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. If an Oracle feature/product, an OS feature, a third-party product, or custom code is used to automate account management, this is not a finding. If there are any accounts managed by the Oracle Database, review the system documentation for justification and approval of these accounts. If any Oracle-managed accounts exist that are not documented and approved, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-270500`

### Rule: Oracle Database must enforce approved authorizations for logical access to the system in accordance with applicable policy.

**Rule ID:** `SV-270500r1064778_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authentication with a DOD-approved public key infrastructure (PKI) certificate does not necessarily imply authorization to access the database management system (DBMS). To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems, including databases, must be properly configured to implement access control policies. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications, a category that includes database management systems. If the DBMS does not follow applicable policy when approving access, it may be in conflict with networks or other applications in the information system. This may result in users either gaining or being denied access inappropriately and in conflict with applicable policy. Satisfies: SRG-APP-000033-DB-000084, SRG-APP-000340-DB-000304</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine whether users are restricted from accessing objects and data they are not authorized to access. If appropriate access controls are not implemented to restrict access to authorized users and to restrict the access of those users to objects and data they are authorized to verify, this is a finding. One option to isolate access is by using the Oracle Database Vault. To check to verify the Oracle Database Vault is installed, issue the following query: SQL> SELECT * FROM V$OPTION WHERE PARAMETER = 'Oracle Database Vault'; If Oracle Database Vault is installed, review its settings for appropriateness and completeness of the access it permits and denies to each type of user. If appropriate and complete, this is not a finding. If Oracle Database Vault is not installed, review the roles and profiles in the database and the assignment of users to these for appropriateness and completeness of the access permitted and denied each type of user. If appropriate and complete, this is not a finding. If the access permitted and denied each type of user is inappropriate or incomplete, this is a finding. Following are code examples for reviewing roles, profiles, etc. Find out what role the users have: select * from dba_role_privs where granted_role = '<role>' List all roles given to a user: select * from dba_role_privs where grantee = '<username>'; List all roles for all users: column grantee format a32 column granted_role format a32 break on grantee select grantee, granted_role from dba_role_privs; Use the following query to list all privileges given to a user: select lpad(' ', 2*level) || granted_role "User roles and privileges" from ( /* THE USERS */ select null grantee, username granted_role from dba_users where username like upper('<enter_username>') /* THE ROLES TO ROLES RELATIONS */ union select grantee, granted_role from dba_role_privs /* THE ROLES TO PRIVILEGE RELATIONS */ union select grantee, privilege from dba_sys_privs ) start with grantee is null connect by grantee = prior granted_role; List which tables a certain role gives SELECT access to using the query: select * from role_tab_privs where role='<role>' and privilege = 'SELECT'; List all tables a user can SELECT from using the query: select * from dba_tab_privs where GRANTEE ='<username>' and privilege = 'SELECT'; List all users who can SELECT on a particular table (either through being given a relevant role or through a direct grant - e.g., grant select on a table to Joe). The result of this query should also show through which role the user has this access or whether it was a direct grant. select Grantee,'Granted Through Role' as Grant_Type, role, table_name from role_tab_privs rtp, dba_role_privs drp where rtp.role = drp.granted_role and table_name = '<TABLENAME>' union select Grantee, 'Direct Grant' as Grant_type, null as role, table_name from dba_tab_privs where table_name = '<TABLENAME>';

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-270501`

### Rule: Oracle Database must protect against an individual who uses a shared account falsely denying having performed a particular action.

**Rule ID:** `SV-270501r1064781_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Nonrepudiation of actions taken is required to maintain application integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Nonrepudiation protects individuals against later claims by an author of not having authored a particular document, a sender of not having transmitted a message, a receiver of not having received a message, or a signatory of not having signed a document. Authentication via shared accounts does not provide individual accountability for actions taken on the database management system (DBMS) or data. Whenever a single database account is used to connect to the database, a secondary authentication method that provides individual accountability is required. This scenario most frequently occurs when an externally hosted application authenticates individual users to the application and the application uses a single account to retrieve or update database information on behalf of the individual users. When shared accounts are used without another means of identifying individual users, users may deny having performed a particular action. This calls for inspection of application source code, which requires collaboration with the application developers. In many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the database administrator (DBA) must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. Satisfies: SRG-APP-000080-DB-000063, SRG-APP-000815-DB-000160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If there are no shared accounts available to more than one user, this is not a finding. Review database, application, and/or OS settings to determine whether users can be identified as individuals when using shared accounts. If the individual user who is using a shared account cannot be identified, this is a finding. If Standard Auditing is used: To ensure that user activities other than SELECT, INSERT, UPDATE, and DELETE are also monitored and attributed to individuals, verify that Oracle auditing is enabled. To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If the query returns the value "NONE", this is a finding. If Unified Auditing is used: To ensure that user activities other than SELECT, INSERT, UPDATE, and DELETE are also monitored and attributed to individuals, verify that Oracle auditing is enabled. To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If the query returns something other than "TRUE", this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-270502`

### Rule: Oracle Database must provide audit record generation capability for organization-defined auditable events within the database.

**Rule ID:** `SV-270502r1064784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the database management system (DBMS) (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DOD has defined the list of events for which the DBMS will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful login attempts, privileged activities, or other system-level access, starting and ending time for user access to the system, concurrent logins from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Organizations may define additional events requiring continuous or ad hoc auditing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using vendor and system documentation, if necessary, verify the DBMS is configured to use Oracle's auditing features, or that a third-party product or custom code is deployed and configured to satisfy this requirement. If a third-party product or custom code is used, compare its current configuration with the audit requirements. If any of the requirements is not covered by the configuration, this is a finding. The remainder of this Check is applicable specifically where Oracle auditing is in use. If Standard Auditing is used: To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value "NONE", this is a finding. To confirm that Oracle audit is capturing information on the required events, review the contents of the SYS.AUD$ table or the audit file, whichever is in use. If auditable events are not listed, this is a finding. If Unified Auditing is used: To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If the query returns something other than "TRUE", this is a finding. To confirm that Oracle audit is capturing information on the required events, review the contents of the SYS.UNIFIED_AUDIT_TRAIL view. If auditable events are not listed, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-270503`

### Rule: Oracle Database must allow designated organizational personnel to select which auditable events are to be audited by the database.

**Rule ID:** `SV-270503r1064787_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent or interfere with the auditing of critical events. Suppression of auditing could permit an adversary to evade detection. Misconfigured audits can degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check database management system (DBMS) settings and documentation to determine whether designated personnel are able to select which auditable events are being audited. If designated personnel are not able to configure auditable events, this is a finding.

## Group: SRG-APP-000091-DB-000066

**Group ID:** `V-270504`

### Rule: Oracle Database must generate audit records for the DOD-selected list of auditable events, when successfully accessed, added, modified, or deleted, to the extent such information is available.

**Rule ID:** `SV-270504r1068292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit records can be generated from various components within the information system, such as network interfaces, hard disks, modems, etc. From an application perspective, certain specific application functionalities may be audited, as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records (i.e., auditable events, timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked). Organizations may define the organizational personnel accountable for determining which application components must provide auditable events. Auditing provides accountability for changes made to the database management system (DBMS) configuration or its objects and data. It provides a means to discover suspicious activity and unauthorized changes. Without auditing, a compromise may go undetected and without a means to determine accountability. The Department of Defense has established the following as the minimum set of auditable events: - When privileges/permissions are retrieved, added, modified or deleted. - When unsuccessful attempts to retrieve, add, modify, delete privileges/permissions occur. - Enforcement of access restrictions associated with changes to the configuration of the database(s). - When security objects are accessed, modified, or deleted. - When unsuccessful attempts to access, modify, or delete security objects occur. - When categories of information (e.g., classification levels/security levels) are accessed, created, modified, or deleted. - When unsuccessful attempts to access, create, modify, or delete categorized information occur. - All privileged activities or other system-level access. - When unsuccessful attempts to execute privileged activities or other system-level access occurs. - When successful or unsuccessful access to any other objects occur as specifically defined by the site. Satisfies: SRG-APP-000091-DB-000066, SRG-APP-000091-DB-000325, SRG-APP-000492-DB-000333, SRG-APP-000494-DB-000344, SRG-APP-000494-DB-000345, SRG-APP-000495-DB-000326, SRG-APP-000495-DB-000327, SRG-APP-000495-DB-000328, SRG-APP-000495-DB-000329, SRG-APP-000496-DB-000334, SRG-APP-000496-DB-000335, SRG-APP-000498-DB-000346, SRG-APP-000498-DB-000347, SRG-APP-000499-DB-000330, SRG-APP-000499-DB-000331, SRG-APP-000501-DB-000336, SRG-APP-000501-DB-000337, SRG-APP-000502-DB-000348, SRG-APP-000502-DB-000349, SRG-APP-000503-DB-000350, SRG-APP-000503-DB-000351, SRG-APP-000504-DB-000354, SRG-APP-000504-DB-000355, SRG-APP-000505-DB-000352, SRG-APP-000506-DB-000353, SRG-APP-000507-DB-000357, SRG-APP-000508-DB-000358</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Oracle Database settings to determine if auditing is being performed on the DOD-required list of auditable events supplied in the discussion. If Standard Auditing is used: To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SHOW PARAMETER AUDIT_TRAIL or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'audit_trail'; If Oracle returns the value "NONE", this is a finding. To confirm that Oracle audit is capturing information on the required events, review the contents of the SYS.AUD$ table or the audit file, whichever is in use. If auditable events are not listed, this is a finding. If Unified Auditing is used: To verify Oracle is configured to capture audit data, enter the following SQL*Plus command: SELECT * FROM V$OPTION WHERE PARAMETER = 'Unified Auditing'; If Oracle returns a value something other than "TRUE", this is a finding. Unified Audit supports named audit policies, which are defined using the CREATE AUDIT POLICY statement. A policy specifies the actions that should be audited and the objects to which it should apply. If no specific objects are included in the policy definition, it applies to all objects. A named policy is enabled using the AUDIT POLICY statement. It can be enabled for all users, for specific users only, or for all except a specified list of users. The policy can audit successful actions, unsuccessful actions, or both. Verifying existing audit policy: existing Unified Audit policies are listed in the view AUDIT_UNIFIED_POLICIES. The AUDIT_OPTION column contains one of the actions specified in a CREATE AUDIT POLICY statement. The AUDIT_OPTION_TYPE column contains "STANDARD ACTION" for a policy that applies to all objects or "OBJECT ACTION" for a policy that audits actions on a specific object. select POLICY_NAME from SYS.AUDIT_UNIFIED_POLICIES where AUDIT_OPTION='GRANT' and AUDIT_OPTION_TYPE='STANDARD ACTION'; To find policies that audit privilege grants on specific objects: select POLICY_NAME,OBJECT_SCHEMA,OBJECT_NAME from SYS.AUDIT_UNIFIED_POLICIES where AUDIT_OPTION='GRANT' and AUDIT_OPTION_TYPE='OBJECT ACTION'; The view AUDIT_UNIFIED_ENABLED_POLICIES shows which Unified Audit policies are enabled. The ENABLED_OPT and USER_NAME columns show the users for whom the policy is enabled or "ALL USERS". The SUCCESS and FAILURE columns indicate if the policy is enabled for successful or unsuccessful actions, respectively. select POLICY_NAME,ENABLED_OPTION,ENTITY_NAME,SUCCESS,FAILURE from SYS.AUDIT_UNIFIED_ENABLED_POLICIES; If auditing is not being performed for all the events listed above, this is a finding.

## Group: SRG-APP-000101-DB-000044

**Group ID:** `V-270505`

### Rule: Oracle Database must include organization-defined additional, more detailed information in the audit records for audit events identified by type, location, or subject.

**Rule ID:** `SV-270505r1064793_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system auditing capability is critical for accurate forensic analysis. Audit record content that may be necessary to satisfy the requirement of this control includes timestamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, file names involved, and access control or flow control rules invoked. In addition, the application must have the capability to include organization-defined additional, more detailed information in the audit records for audit events. These events may be identified by type, location, or subject. An example of detailed information the organization may require in audit records is full-text recording of privileged commands or the individual identities of shared account users. Some organizations may determine that more detailed information is required for specific database event types. If this information is not available, it could negatively impact forensic investigations into user actions or other malicious events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to identify what additional site-specific information not covered by the default audit options, the organization has determined to be necessary. If there are none, this is not a finding. If any additional information is defined, compare those auditable events that are not covered by unified auditing with the existing Fine-Grained Auditing (FGA) specifications returned by the following query: SELECT * FROM SYS.UNIFIED_AUDIT_TRAIL WHERE AUDIT_TYPE = 'FineGrainedAudit'; If any such auditable event is not covered by the existing FGA specifications, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-270506`

### Rule: Oracle Database must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-270506r1064796_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure sufficient storage capacity for the audit logs, Oracle Database must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of the database management system (DBMS) and is closely associated with the database administrator (DBA) and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on the DBMS's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the database management system (DBMS) settings to determine whether audit logging is configured to produce logs consistent with the amount of space allocated for logging. If auditing will generate excessive logs so that they may outgrow the space reserved for logging, this is a finding. If file-based auditing is in use, check that sufficient space is available to support the file(s). If not, this is a finding. If standard, table-based auditing is used, the audit logs are written to a table called AUD$; and if a Virtual Private Database is deployed, a table is created called FGA_LOG$. First, check the current location of the audit trail tables. CONN / AS SYSDBA SELECT table_name, tablespace_name FROM dba_tables WHERE table_name IN ('AUD$', 'FGA_LOG$') ORDER BY table_name; TABLE_NAME TABLESPACE_NAME ------------------------------ ------------------------------ AUD$ SYSTEM FGA_LOG$ SYSTEM If the tablespace name is SYSTEM, the table needs to be relocated to its own tablespace. Ensure that adequate space is allocated to that tablespace. If Unified Auditing is used: Audit logs are written to tables in the AUDSYS schema. The default tablespace for AUDSYS is USERS. A separate tablespace should be created to contain audit data. Ensure that adequate space is allocated to that tablespace. Investigate whether there have been any incidents where the database management system (DBMS) ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-270507`

### Rule: Oracle Database must off-load audit data to a separate log management facility; this must be continuous and in near-real-time for systems with a network connection to the storage facility, and weekly or more often for stand-alone systems.

**Rule ID:** `SV-270507r1065200_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The database management system (DBMS) may write audit records to database tables, files in the file system, other kinds of local repositories, or a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation for a description of how audit records are off-loaded. If there is no centralized audit log management system, for the audit data to be written to, this is a finding. If the DBMS has a continuous network connection to the centralized log management system, but the DBMS audit records are not written directly to the centralized log management system or transferred in near-real-time, this is a finding. If the DBMS does not have a continuous network connection to the centralized log management system, and the DBMS audit records are not transferred to the centralized log management system weekly or more often, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-270508`

### Rule: The Oracle Database, or the logging or alerting mechanism the application uses, must provide a warning when allocated audit record storage volume record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-270508r1065201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to the database management system (DBMS) on its own server will not be an issue. However, space will still be required on the DBMS server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume usage reaching 75 percent, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the information system security officer (ISSO) and the database administrator (DBA)/system administrator (SA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review OS or third-party logging application settings to determine whether a warning will be provided when 75 percent of DBMS audit log storage capacity is reached. If no warning will be provided, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-270509`

### Rule: Oracle Database must provide an immediate real-time alert to appropriate support staff of all audit log failures.

**Rule ID:** `SV-270509r1065202_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the information system security officer (ISSO) and the database administrator (DBA)/system administrator (SA). A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less). If Oracle Enterprise Manager is in use, the capability to issue such an alert is built in and configurable via the console so an alert can be sent to a designated administrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Oracle Database, OS, or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when auditing fails for any reason. If real-time alerts are not sent upon auditing failure, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-270510`

### Rule: The audit information produced by the Oracle Database must be protected from unauthorized access, modification, or deletion.

**Rule ID:** `SV-270510r1068294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions using file system protections and limiting log data location. Additionally, applications with user interfaces to audit records must not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Modification or deletion of database audit data could mask the theft of, or the unauthorized modification of, sensitive data stored in the database. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000119-DB-000060, SRG-APP-000120-DB-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review locations of audit logs, both internal to the database and database audit logs located at the operating system level. Verify there are appropriate controls and permissions to protect the audit information from unauthorized access. If appropriate controls and permissions do not exist, this is a finding. - - - - - From SQL*Plus or SQL Developer: select value from v$parameter where name = 'audit_trail'; select value from v$parameter where name = 'audit_file_dest'; If audit_trail is set to OS, XML or XML EXTENDED, this means logs are stored at the operating system level. If audit_trail is set to OS, but the audit records are routed directly to a separate log server without writing to the local file system, this is not a finding. If audit_trail is set to DB or "DB, EXTENDED" this means logs are stored in the database. If any logs are written to the database, DBA_TAB_PRIVS describes all object grants in the database. If standard auditing is in use, follow the below, check permissions on the AUD$ table. sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where table_name = 'AUD$'; If Unified Auditing is used, check permissions on the AUDSYS tables. sqlplus connect as sysdba; SQL> SELECT GRANTEE, TABLE_NAME, PRIVILEGE FROM DBA_TAB_PRIVS where owner='AUDSYS'; If appropriate controls and permissions are not implemented, this is a finding. If audit logs located at the operating system level: On Unix Systems: ls -ld [pathname] Substitute [pathname] with the directory paths listed from the above SQL statements for audit_file_dest. If permissions are granted for world access, this is a finding. If any groups that include members other than software owner accounts, DBAs, auditors, oracle processes, or any account not listed as authorized, this is a finding. On Windows Systems (from Windows Explorer): Browse to the directory specified. Select and right-click on the directory >> Properties >> Security tab. On Windows hosts, records are also written to the Windows application event log. The location of the application event log is listed under Properties for the log under the Windows console. The default location is C:\WINDOWS\system32\config\EventLogs\AppEvent.Evt. Select and right-click on the directory >> Properties >> Security tab. If permissions are granted to everyone, this is a finding. If any accounts other than the administrators, software owner accounts, DBAs, auditors, Oracle processes, or any account not listed as authorized, this is a finding. Compare path to %ORACLE_HOME%. If audit_file_dest is a subdirectory of %ORACLE_HOME%, this is a finding.

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-270511`

### Rule: The system must protect audit tools from unauthorized access, modification, or deletion.

**Rule ID:** `SV-270511r1065262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity. Satisfies: SRG-APP-000121-DB-000202, SRG-APP-000122-DB-000203, SRG-APP-000123-DB-000204</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access permissions to tools used to view or modify audit log data. These tools may include the database management system (DBMS) itself or tools external to the database. If appropriate permissions and access controls are not applied to prevent unauthorized access, modification, or deletion of these tools, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-270512`

### Rule: Oracle Database must support enforcement of logical access restrictions associated with changes to the database management system (DBMS) configuration and to the database itself.

**Rule ID:** `SV-270512r1065305_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review access restrictions associated with changes to the configuration of the DBMS or database(s). On Unix Systems: ls -ld [pathname] Replace [pathname] with the directory path where the Oracle Database software is installed (e.g., /u01/app/oracle/product/19.0.0/dbhome_1). If permissions are granted for world access, this is a finding. If any groups that include members other than the software owner account, database administrators (DBAs), or any accounts not listed as authorized, this is a finding. For Windows Systems: Review the permissions that control access to the Oracle installation software directories (e.g., \Program Files\Oracle\). If access is given to members other than the software owner account, DBAs, or any accounts not listed as authorized, this is a finding. Compare the access control employed with that documented in the system documentation. If access does not match the documented requirement, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-270513`

### Rule: Oracle Database products must be a version supported by the vendor.

**Rule ID:** `SV-270513r1064817_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and interview the database administrator. Identify all database software components. Review the version and release information. From SQL*Plus: Select version from v$instance; Access the vendor website or use other means to verify the version is still supported. Oracle Release schedule: https://support.oracle.com/knowledge/Oracle%20Database%20Products/742060_1.html If the Oracle version or any of the software components are not supported by the vendor, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-270514`

### Rule: Database software, applications, and configuration files must be monitored to discover unauthorized changes.

**Rule ID:** `SV-270514r1064820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify that monitoring of changes to database software libraries, related applications, and configuration files is done. Verify that the list of files and directories being monitored is complete. If monitoring does not occur or is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-270515`

### Rule: The OS must limit privileges to change the database management system (DBMS) software resident within software libraries (including privileged programs).

**Rule ID:** `SV-270515r1065210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review permissions that control access to the DBMS software libraries. The software library location may be determined from vendor documentation or service/process executable paths. Typically, only the DBMS software installation/maintenance account or system administrator (SA) account requires access to the software library for operational support such as backups. Any other accounts should be scrutinized and the reason for access documented. Accounts should have the least amount of privilege required to accomplish the job. Below is one example for how to review accounts with access to software libraries for a Linux-based system: cat /etc/group |grep -i dba --Example output: dba:x:102: --take above number and input in below grep command cat /etc/passwd |grep 102 If any accounts are returned that are not required and authorized to have access to the software library location do have access, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-270516`

### Rule: The Oracle Database software installation account must be restricted to authorized users.

**Rule ID:** `SV-270516r1064826_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. Database administrator (DBA) and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them. This requirement is particularly important because Oracle equates the installation account with the SYS account - the super-DBA. Once logged on to the operating system, this account can connect to the database AS SYSDBA without further authentication. It is very powerful and, by virtue of not being linked to any one person, cannot be audited to the level of the individual.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling and granting access to use of the database management system (DBMS) software installation account. If access or use of this account is not restricted to the minimum number of personnel required, or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-270517`

### Rule: Database software directories, including database management system (DBMS) configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-270517r1064829_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted, any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DBMS software library directory and note other root directories located on the same disk directory or any subdirectories. If any non-DBMS software directories exist on the disk directory, examine or investigate their use. If any of the directories are used by other applications, including third-party applications that use the DBMS, this is a finding. Only applications that are required for the functioning and administration, not use, of the DBMS should be located on the same disk directory as the DBMS software libraries. For databases located on mainframes, confirm that the database and its configuration files are isolated in their own DASD pools. If database software and database configuration files share DASD with other applications, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-270518`

### Rule: Database objects must be owned by accounts authorized for ownership.

**Rule ID:** `SV-270518r1064832_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object including the privilege to assign access to the owned objects to other subjects. Unmanaged or uncontrolled ownership of objects can lead to unauthorized object grants and alterations, and unauthorized modifications to data. If critical tables or other objects rely on unauthorized owner accounts, these objects can be lost when an account is removed. It may be the case that there are accounts that are authorized to own synonyms, but no other objects. If this is so, it should be documented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to identify accounts authorized to own database objects. Review accounts in the database management systems (DBMSs) that own objects. If any database objects are found to be owned by users not authorized to own database objects, this is a finding. - - - - - Query the object DBA_OBJECTS to show the users who own objects in the database. The query below will return all of the users who own objects. sqlplus connect as sysdba SQL>select owner, object_type, count(*) from dba_objects group by owner, object_type order by owner, object_type; If these owners are not authorized owners, select all of the objects these owners have generated and decide who they should belong to. To make a list of all of the objects, the unauthorized owner has to perform the following query. SQL>select * from dba_objects where owner =&unauthorized_owner;

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-270519`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to the DBMS, etc.) must be restricted to authorized users.

**Rule ID:** `SV-270519r1112463_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the database management system (DBMS) were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review accounts for direct assignment of administrative privileges. Connected as SYSDBA, run the query: SELECT grantee, privilege FROM dba_sys_privs WHERE grantee IN ( SELECT username FROM dba_users WHERE username NOT IN ( 'XDB', 'SYSTEM', 'SYS', 'LBACSYS', 'DVSYS', 'DVF', 'SYSMAN_RO', 'SYSMAN_BIPLATFORM', 'SYSMAN_MDS', 'SYSMAN_OPSS', 'SYSMAN_STB', 'DBSNMP', 'SYSMAN', 'APEX_040200', 'WMSYS', 'SYSDG', 'SYSBACKUP', 'SPATIAL_WFS_ADMIN_USR', 'SPATIAL_CSW_ADMIN_US', 'GSMCATUSER', 'OLAPSYS', 'SI_INFORMTN_SCHEMA', 'OUTLN', 'ORDSYS', 'ORDDATA', 'OJVMSYS', 'ORACLE_OCM', 'MDSYS', 'ORDPLUGINS', 'GSMADMIN_INTERNAL', 'MDDATA', 'FLOWS_FILES', 'DIP', 'CTXSYS', 'AUDSYS', 'APPQOSSYS', 'APEX_PUBLIC_USER', 'ANONYMOUS', 'SPATIAL_CSW_ADMIN_USR', 'SYSKM', 'SYSMAN_TYPES', 'MGMT_VIEW', 'EUS_ENGINE_USER', 'EXFSYS', 'SYSMAN_APM' ) ) AND privilege NOT IN ('UNLIMITED TABLESPACE' , 'REFERENCES', 'INDEX', 'SYSDBA', 'SYSOPER', 'CREATE SESSION' ) ORDER BY 1, 2; If any administrative privileges have been assigned directly to a database account, this is a finding. The list of special accounts that are excluded from this requirement may not be complete. It is expected that the database administrator (DBA) will edit the list to suit local circumstances, adding other special accounts as necessary, and removing any that are not supposed to be in use in the Oracle deployment that is under review.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270520`

### Rule: Oracle Database must be configured in accordance with the security configuration settings based on DOD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-270520r1115964_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the database management system (DBMS) to implement organizationwide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DOD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. Oracle Database must be configured in compliance with guidance from all such relevant sources, with specific emphasis on the database security standards of each organization.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Oracle Database Security Assessment Tool (DBSAT) provides prioritized recommendations on how to mitigate identified security risks or gaps within Oracle Databases. With DBSAT, DISA STIG rules that are process-related, such as review system documentation to identify accounts authorized to own database objects, are now included, and marked as "Evaluate" and display details that help customers validate compliance. DBSAT automates the STIG checks whenever possible, and if the checks are process-related, DBSAT provides visibility so they can be tracked and manually validated. Download the latest version of the Oracle Database Security Assessment Tool (DBSAT). DBSAT is provided by Oracle at no additional cost: https://www.oracle.com/database/technologies/security/dbsat.html DBSAT analyzes information on the database and listener configuration to identify configuration settings that may unnecessarily introduce risk. DBSAT goes beyond simple configuration checking, examining user accounts, privilege and role grants, authorization control, separation of duties, fine-grained access control, data encryption and key management, auditing policies, and OS file permissions. DBSAT applies rules to quickly assess the current security status of a database and produce findings in all the areas above. In addition, to the Oracle database STIG checks, DBSAT helps identify areas where your database configuration, operation, or implementation introduces risks and recommends changes and controls to mitigate those risks according Oracle database security best practices. If there is evidence that the DBSAT tool is not used with the output reviewed regularly (annually), this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270521`

### Rule: Oracle instance names must not contain Oracle version numbers.

**Rule ID:** `SV-270521r1112467_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Service names may be discovered by unauthenticated users. If the service name includes version numbers or other database product information, a malicious user may use that information to develop a targeted attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using a non-CDB database: From SQL*Plus: select instance_name, version from v$instance; If using a CDB database: To check the container database (CDB): From SQL*Plus: select instance_name, version from v$instance; To check the pluggable databases (PDBs) within the CDB: select name from v$pdbs; Check Instance Name: If the instance name returned references the Oracle release number, this is a finding. Numbers used that include version numbers by coincidence are not a finding. The database administrator (DBA) should be able to relate the significance of the presence of a digit in the SID.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270522`

### Rule: Fixed user and PUBLIC Database links must be authorized for use.

**Rule ID:** `SV-270522r1115956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database links define connections that may be used by the local Oracle database to access remote Oracle databases (homogenous links) and non-Oracle Databases (heterogeneous links). These links provide a means for a compromise to the local database to spread to remote databases and for a compromise of a remote database to the local database in a distributed database environment. Limiting or eliminating the use of database links, where they are not required to support the operational system, can help isolate compromises, mitigate risk, and reduce the potential attack surface.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using a non-CDB database: Use the following query to get a list of database links. From SQL*Plus: select owner||': '||db_link from dba_db_links; If using a CDB database: Use the following query to get a list of database links. select con_id_to_con_name(con_id) con_id, owner, db_link, username, host from cdb_db_links order by 1,2,3; Check Results: If no rows are returned from the first SQL statement, this check is not a finding. If there are rows returned, verify the database links are required. If they are required and exist, this is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270523`

### Rule: The Oracle WITH GRANT OPTION privilege must not be granted to nondatabase administrator (DBA) or nonapplication administrator user accounts.

**Rule ID:** `SV-270523r1065302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An account permission to grant privileges within the database is an administrative function. Minimizing the number and privileges of administrative accounts reduces the chances of privileged account exploitation. Application user accounts must never require WITH GRANT OPTION privileges since, by definition, they require only privileges to execute procedures or view/edit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute the query: select grantee||': '||owner||'.'||table_name from dba_tab_privs where grantable = 'YES' and grantee not in (select distinct owner from dba_objects) and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA') and table_name not like 'SYS_PLSQL_%' order by grantee; If any accounts are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270524`

### Rule: The Oracle REMOTE_OS_ROLES parameter must be set to FALSE.

**Rule ID:** `SV-270524r1112471_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Setting REMOTE_OS_ROLES to TRUE allows operating system groups to control Oracle roles. The default value of FALSE causes roles to be identified and managed by the database. If REMOTE_OS_ROLES is set to TRUE, a remote user could impersonate another operating system user over a network connection. DOD requires the REMOTE_OS_ROLES to be set to FALSE.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the current status of the remote_os_roles parameter use the SQL statement: If using a non-CDB database: From SQL*Plus: COLUMN name format a20 COLUMN parameter_value format a20 SELECT name, con_id, value AS PARAMETER_VALUE FROM sys.v_$parameter WHERE vp.name = 'remote_os_roles' ORDER BY 1; If the PARAMETER_VALUE is not FALSE, that is a finding. If using a CDB database: From SQL*Plus (in the CDB database): COLUMN name format a20 COLUMN parameter_value format a20 SELECT name, inst_id, con_id, value AS PARAMETER_VALUE FROM sys.gv_$parameter WHERE vp.name = 'remote_os_roles' ORDER BY 1; In the CDB database, if the PARAMETER_VALUE is not FALSE, that is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270525`

### Rule: The Oracle SQL92_SECURITY parameter must be set to TRUE.

**Rule ID:** `SV-270525r1112473_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The configuration option SQL92_SECURITY specifies whether table-level SELECT privileges are required to execute an update or delete those references table column values. If this option is disabled (set to FALSE), the UPDATE privilege can be used to determine values that should require SELECT privileges. The SQL92_SECURITY setting of TRUE prevents the exploitation of user credentials with only DELETE or UPDATE privileges on a table from being able to derive column values in that table by performing a series of update/delete statements using a where clause, and rolling back the change. In the following example, with SQL92_SECURITY set to FALSE, a user with only delete privilege on the scott.emp table is able to derive that there is one employee with a salary greater than 3000. With SQL92_SECURITY set to TRUE, that user is prevented from attempting to derive a value. SQL92_SECURITY = FALSE SQL> delete from scott.emp where sal > 3000; 1 row deleted SQL> rollback; Rollback complete SQL92_SECURITY = TRUE SQL> delete from scott.emp where sal > 3000; delete from scott.emp where sal > 3000 * ERROR at line 1: ORA-01031: insufficient privileges</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the current status of the SQL92_SECURITY parameter use the SQL statement: If using a non-CDB database: From SQL*Plus: select value from v$parameter where name = 'sql92_security'; If using a CDB database: From SQL*Plus: column name format a20 column parameter_value format a20 SELECT name, inst_id, con_id, value AS PARAMETER_VALUE FROM sys.gv_$parameter WHERE name = 'sql92_security' ORDER BY 1; Check Result: The CDB database and all PDBs must be checked. If the value returned is set to FALSE, this is a finding. If the parameter is set to TRUE or does not exist, this is not a finding. In any instance or container, if the PARAMETER_VALUE is not TRUE, that is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270526`

### Rule: The Oracle password file ownership and permissions should be limited and the REMOTE_LOGIN_PASSWORDFILE parameter must be set to EXCLUSIVE or NONE.

**Rule ID:** `SV-270526r1115966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critically important to the security of the system to protect the password file and the environment variables that identify the location of the password file. Any user with access to these could potentially compromise the security of the connection. The REMOTE_LOGIN_PASSWORDFILE setting of "NONE" disallows remote administration of the database. The REMOTE_LOGIN_PASSWORDFILE setting of "EXCLUSIVE" allows for auditing of individual database administrator (DBA) logons to the SYS account. If not set to "EXCLUSIVE", remote connections to the database as "internal" or "as SYSDBA" are not logged to an individual account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the current status of the REMOTE_LOGIN_PASSWORDFILE parameter: If using a non-CDB database: From SQL*Plus: select value from v$parameter where upper(name) = 'REMOTE_LOGIN_PASSWORDFILE'; If the value returned does not equal 'EXCLUSIVE' or 'NONE', this is a finding. If using a CDB database: From SQL*Plus: To verify the current status of the remote_login_passwordfile parameter use the SQL statement: column name format a25 column parameter_value format a25 SELECT name, inst_id, con_id, value AS PARAMETER_VALUE FROM sys.gv_$parameter WHERE name = 'REMOTE_LOGIN_PASSWORDFILE' ORDER BY 1; In any instance or container, if the PARAMETER_VALUE is set to SHARED, or to a value other than EXCLUSIVE or NONE, that is a finding. Check the security permissions on password file within the OS. On Unix Systems: ls -ld $ORACLE_HOME/dbs/orapw${ORACLE_SID} Substitute ${ORACLE_SID} with the name of the ORACLE_SID for the database. If permissions are granted for world access, this is a finding. On Windows Systems (from Windows Explorer), browse to the %ORACLE_HOME%\database\directory. Select and right-click on the PWD%ORACLE_SID%.ora file, select Properties, then select the Security tab. Substitute %ORACLE_SID% with the name of the ORACLE_SID for the database. If permissions are granted to everyone, this is a finding. If any account other than the database management system (DBMS) software installation account is listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270527`

### Rule: System privileges granted using the WITH ADMIN OPTION must not be granted to unauthorized user accounts.

**Rule ID:** `SV-270527r1065266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The WITH ADMIN OPTION allows the grantee to grant a privilege to another database account. Best security practice restricts the privilege of assigning privileges to authorized personnel. Authorized personnel include database administrators (DBAs), object owners, and, where designed and included in the application's functions, application administrators. Restricting privilege-granting functions to authorized accounts can help decrease mismanagement of privileges and wrongful assignments to unauthorized accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and nonadministrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the CREATE ANY TABLE or ALTER SESSION privilege or EXECUTE privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either SYSTEM or SYSAUX. Nonadministrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is USERS. To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Nonadministrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM, SYSKM *Subject to change based on version installed. Run the SQL query: From SQL*Plus: select grantee, privilege from dba_sys_privs where grantee not in (<list of nonapplicable accounts>) and admin_option = 'YES' and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA'); (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) If any accounts that are not authorized to have the ADMIN OPTION are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270528`

### Rule: System Privileges must not be granted to PUBLIC.

**Rule ID:** `SV-270528r1064862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System privileges can be granted to users and roles and to the user group PUBLIC. All privileges granted to PUBLIC are accessible to every user in the database. Many of these privileges convey considerable authority over the database and should be granted only to those persons responsible for administering the database. In general, these privileges should be granted to roles and then the appropriate roles should be granted to users. System privileges must never be granted to PUBLIC as this could allow users to compromise the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: Select privilege from dba_sys_privs where grantee = 'PUBLIC'; If any records are returned, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270529`

### Rule: Oracle roles granted using the WITH ADMIN OPTION must not be granted to unauthorized accounts.

**Rule ID:** `SV-270529r1065268_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The WITH ADMIN OPTION allows the grantee to grant a role to another database account. Best security practice restricts the privilege of assigning privileges to authorized personnel. Authorized personnel include database administrators (DBAs), object owners, and application administrators (where designed and included in the application's functions). Restricting privilege-granting functions to authorized accounts can help decrease mismanagement of privileges and wrongful assignments to unauthorized accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and nonadministrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the CREATE ANY TABLE or ALTER SESSION privilege or EXECUTE privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either SYSTEM or SYSAUX. Nonadministrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is USERS. To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Non-Administrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM *Subject to change based on version installed. Run the SQL statement: select grantee||': '||granted_role from dba_role_privs where grantee not in (<list of nonapplicable accounts>) and admin_option = 'YES' and grantee not in (select distinct owner from dba_objects) and grantee not in (select grantee from dba_role_privs where granted_role = 'DBA') order by grantee; (With respect to the list of special accounts that are excluded from this requirement, it is expected that the DBA will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review.) Review the system documentation to confirm any grantees listed are information system security officer (ISSO)-authorized DBA accounts or application administration roles. If any grantees listed are not authorized and documented, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270530`

### Rule: Object permissions granted to PUBLIC must be restricted.

**Rule ID:** `SV-270530r1065320_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions on objects may be granted to the user group PUBLIC. Because every database user is a member of the PUBLIC group, granting object permissions to PUBLIC gives all users in the database access to that object. In a secure environment, granting object permissions to PUBLIC must be restricted to those objects that all users are allowed to access. The policy does not require object permissions assigned to PUBLIC by the installation of Oracle Database server components be revoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A default Oracle Database installation provides a set of predefined administrative accounts and nonadministrative accounts. These are accounts that have special privileges required to administer areas of the database, such as the "CREATE ANY TABLE" or "ALTER SESSION" privilege, or "EXECUTE" privileges on packages owned by the SYS schema. The default tablespace for administrative accounts is either "SYSTEM" or "SYSAUX". Nonadministrative user accounts only have the minimum privileges needed to perform their jobs. Their default tablespace is "USERS". To protect these accounts from unauthorized access, the installation process expires and locks most of these accounts, except where noted below. The database administrator is responsible for unlocking and resetting these accounts, as required. Non-Administrative Accounts - Expired and locked: APEX_PUBLIC_USER, DIP, FLOWS_040100*, FLOWS_FILES, MDDATA, SPATIAL_WFS_ADMIN_USR, XS$NULL Administrative Accounts - Expired and Locked: ANONYMOUS, CTXSYS, EXFSYS, LBACSYS, , GSMADMIN_INTERNAL, MDSYS, OLAPSYS, ORACLE_OCM, ORDDATA, OWBSYS, ORDPLUGINS, ORDSYS, OUTLN, SI_INFORMTN_SCHEMA, SPATIAL_CSW_ADMIN_USR, WK_TEST, WK_SYS, WKPROXY, WMSYS, XDB Administrative Accounts - Open: DBSNMP, MGMT_VIEW, SYS, SYSMAN, SYSTEM * Subject to change based on version installed. Run the SQL query: select owner ||'.'|| table_name ||':'|| privilege from dba_tab_privs where grantee = 'PUBLIC' and owner not in (<list of nonapplicable accounts>); With respect to the list of special accounts that are excluded from this requirement, it is expected that the database administrator (DBA) will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review. If there are any records returned that are not Oracle product accounts, and are not documented and authorized, this is a finding. Note: This check may return false positives where other Oracle product accounts are not included in the exclusion list.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270531`

### Rule: The Oracle Listener must be configured to require administration authentication.

**Rule ID:** `SV-270531r1065272_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Oracle listener authentication helps prevent unauthorized administration of the Oracle listener. Unauthorized administration of the listener could lead to denial-of-service (DoS) exploits, loss of connection audit data, unauthorized reconfiguration, or other unauthorized access. This is a Category I finding because privileged access to the listener is not restricted to authorized users. Unauthorized access can result in stopping of the listener (DoS) and overwriting of listener audit logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If a listener is not running on the local database host server, this check is not a finding. Note: Complete this check only once per host system and once per listener. Multiple listeners may be defined on a single host system. They must all be reviewed, but only once per database home review. For subsequent database home reviews on the same host system, this check is not a finding. Determine all listeners running on the host. For Windows hosts, view all Windows services with TNSListener embedded in the service name: - The service name format is: Oracle[ORACLE_HOME_NAME]TNSListener For Unix hosts, the Oracle Listener process will indicate the TNSLSNR executable. At a command prompt, issue the command: ps -ef | grep tnslsnr | grep -v grep The alias for the listener follows tnslsnr in the command output. Must be logged on the host system using the account that owns the tnslsnr executable (Unix). If the account is denied local logon, have the system administrator (SA) assist in this task by adding "su" to the listener account from the root account. On Windows platforms, log on using an account with administrator privileges to complete the check. From a system command prompt, execute the listener control utility: lsnrctl status [LISTENER NAME] Review the results for the value of Security. If "Security = OFF" is displayed, this is a finding. If "Security = ON: Password or Local OS Authentication", this is a finding (Instead, use Local OS Authentication). If "Security = ON: Local OS Authentication" is displayed, this is not a finding. Repeat the execution of the lsnrctl utility for all active listeners.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270532`

### Rule: Application role permissions must not be assigned to the Oracle PUBLIC role.

**Rule ID:** `SV-270532r1064874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Permissions granted to PUBLIC are granted to all users of the database. Custom roles must be used to assign application permissions to functional groups of application users. The installation of Oracle does not assign role permissions to PUBLIC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select granted_role from dba_role_privs where grantee = 'PUBLIC'; If any roles are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270533`

### Rule: Oracle application administration roles must be disabled if not required and authorized.

**Rule ID:** `SV-270533r1065215_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application administration roles, which are assigned system or elevated application object privileges, must be protected from default activation. Application administration roles are determined by system privilege assignment (create/alter/drop user) and application user role ADMIN OPTION privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the SQL query: select grantee, granted_role from dba_role_privs where default_role='YES' and granted_role in (select grantee from dba_sys_privs where upper(privilege) like '%USER%') and grantee not in (<list of nonapplicable accounts>) and grantee not in (select distinct owner from dba_tables) and grantee not in (select distinct username from dba_users where upper(account_status) like '%LOCKED%'); With respect to the list of special accounts that are excluded from this requirement, it is expected that the database administrator (DBA) will maintain the list to suit local circumstances, adding special accounts as necessary and removing any that are not supposed to be in use in the Oracle deployment that is under review. Review the list of accounts reported for this check and ensures that they are authorized application administration roles. If any are not authorized application administration roles, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270534`

### Rule: The directories assigned to the LOG_ARCHIVE_DEST* parameters must be protected from unauthorized access.

**Rule ID:** `SV-270534r1065274_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The LOG_ARCHIVE_DEST parameter is used to specify the directory to which Oracle archive logs are written. Where the database management system (DBMS) availability and recovery to a specific point in time is critical, the protection of archive log files is critical. Archive log files may also contain unencrypted sensitive data. If written to an inadequately protected or invalidated directory, the archive log files may be accessed by unauthorized persons or processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select log_mode from v$database; select value from v$parameter where name = 'log_archive_dest'; select value from v$parameter where name = 'log_archive_duplex_dest'; select name, value from v$parameter where name LIKE 'log_archive_dest_%'; select value from v$parameter where name = 'db_recovery_file_dest'; If the value returned for LOG_MODE is NOARCHIVELOG, this check is not a finding. If a value is not returned for LOG_ARCHIVE_DEST and no values are returned for any of the LOG_ARCHIVE_DEST_[1-10] parameters, and no value is returned for DB_RECOVERY_FILE_DEST, this is a finding. Note: LOG_ARCHIVE_DEST and LOG_ARCHIVE_DUPLEX_DEST are incompatible with the LOG_ARCHIVE_DEST_n parameters, and must be defined as the null string (' ') when any LOG_ARCHIVE_DEST_n parameter has a value other than a null string. On Unix Systems: ls -ld [pathname] Substitute [pathname] with the directory paths listed from the above SQL statements for log_archive_dest and log_archive_duplex_dest. If permissions are granted for world access, this is a finding. On Windows systems (from Windows Explorer): Browse to the directory specified. Select and right-click on the directory >> Properties >> Security tab. If permissions are granted to everyone, this is a finding. If any account other than the Oracle process and software owner accounts, administrators, database administrators (DBAs), system group, or developers authorized to write and debug applications on this database are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270535`

### Rule: The Oracle _TRACE_FILES_PUBLIC parameter if present must be set to FALSE.

**Rule ID:** `SV-270535r1065307_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The _TRACE_FILES_PUBLIC parameter is used to make trace files used for debugging database applications and events available to all database users. Use of this capability precludes the discrete assignment of privileges based on job function. Additionally, its use may provide access to external files and data to unauthorized users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name = '_trace_files_public'; If the value returned is TRUE, this is a finding. If the parameter does not exist or is set to FALSE, this is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270536`

### Rule: Oracle Database production application and data directories must be protected from developers on shared production/development database management system (DBMS) host systems.

**Rule ID:** `SV-270536r1064886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Developer roles must not be assigned DBMS administrative privileges to production DBMS application and data directories. The separation of production database administrator (DBA) and developer roles helps protect the production system from unauthorized, malicious, or unintentional interruption due to development activities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the DBMS or DBMS host is not shared by production and development activities, this check is not a finding. Review OS DBA group membership. If any developer accounts, as identified in the system documentation, have been assigned DBA privileges, this is a finding. Note: Though shared production/nonproduction DBMS installations was allowed under previous database STIG guidance, doing so may place it in violation of OS, Application, Network, or Enclave STIG guidance. Ensure that any shared production/nonproduction DBMS installation meets STIG guidance requirements at all levels or mitigates any conflicts in STIG guidance with the authorizing official (AO).

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270537`

### Rule: Use of the Oracle Database installation account must be logged.

**Rule ID:** `SV-270537r1064889_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The database management system (DBMS) installation account may be used by any authorized user to perform DBMS installation or maintenance. Without logging, accountability for actions attributed to the account is lost.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review documented and implemented procedures for monitoring the use of the DBMS software installation account in the system documentation. If use of this account is not monitored or procedures for monitoring its use do not exist or are incomplete, this is a finding. Note: On Windows systems, the Oracle DBMS software is installed using an account with administrator privileges. Ownership should be reassigned to a dedicated OS account used to operate the DBMS software. If monitoring does not include all accounts with administrator privileges on the DBMS host, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270538`

### Rule: The Oracle Database data files, transaction logs and audit files must be stored in dedicated directories or disk partitions separate from software or other application files.

**Rule ID:** `SV-270538r1064892_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of database management system (DBMS) data, transaction and audit data files stored by the host operating system is dependent on OS controls. When different applications share the same database, resource contention and security controls are required to isolate and protect an application's data from other applications. In addition, it is an Oracle best practice to separate data, transaction logs, and audit logs into separate physical directories according to Oracle's Optimal Flexible Architecture (OFA). And finally, DBMS software libraries and configuration files also require differing access control lists.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the disk/directory specification where database data, transaction log and audit files are stored. If DBMS data, transaction log or audit data files are stored in the same directory, this is a finding. If multiple applications are accessing the database and the database data files are stored in the same directory, this is a finding. If multiple applications are accessing the database and database data is separated into separate physical directories according to application, this check is not a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270539`

### Rule: Network access to Oracle Database must be restricted to authorized personnel.

**Rule ID:** `SV-270539r1064895_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting remote access to specific, trusted systems helps prevent access by unauthorized and potentially malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
IP address restriction may be defined for the database listener, by use of the Oracle Connection Manager or by an external network device. Identify the method used to enforce address restriction (interview database administrator [DBA]) or review system documentation). If enforced by the database listener, then review the SQLNET.ORA file located in the ORACLE_HOME/network/admin directory (this assumes that a single sqlnet.ora file, in the default location, is in use; SQLNET.ORA could also be the directory indicated by the TNS_ADMIN environment variable or registry setting). If the following entries do not exist, then restriction by IP address is not configured and is a finding. tcp.validnode_checking=YES tcp.invited_nodes=(IP1, IP2, IP3) If enforced by an Oracle Connection Manager, then review the CMAN.ORA file for the Connection Manager (located in the TNS_ADMIN or ORACLE_HOME/network/admin directory for the connection manager). If a RULE entry allows all addresses ("/32") or does not match the address range specified in the system documentation, this is a finding. (rule=(src=[IP]/27)(dst=[IP])(srv=*)(act=accept)) Note: An IP address with a "/" indicates acceptance by subnet mask where the number after the "/" is the left most number of bits in the address that must match for the rule to apply.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270540`

### Rule: Changes to configuration options must be audited.

**Rule ID:** `SV-270540r1064898_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When standard auditing is in use, the AUDIT_SYS_OPERATIONS parameter is used to enable auditing of actions taken by the user SYS. The SYS user account is a shared account by definition and holds all privileges in the Oracle database. It is the account accessed by users connecting to the database with SYSDBA or SYSOPER privileges.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Unified or mixed auditing, from SQL*Plus: select count(*) from audit_unified_enabled_policies where entity_name = 'SYS'; If the count is less than one row, this is a finding. For Standard auditing, from SQL*Plus: select value from v$parameter where name = 'audit_sys_operations'; If the value returned is FALSE, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270541`

### Rule: The /diag subdirectory under the directory assigned to the DIAGNOSTIC_DEST parameter must be protected from unauthorized access.

**Rule ID:** `SV-270541r1065276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion><DIAGNOSTIC_DEST>/diag indicates the directory where trace, alert, core, and incident directories and files are located. The files may contain sensitive data or information that could prove useful to potential attackers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: select value from v$parameter where name='diagnostic_dest'; On Unix Systems: ls -ld [pathname]/diag Substitute [pathname] with the directory path listed from the above SQL command, and append "/diag" to it, as shown. If permissions are granted for world access, this is a finding. If any groups that include members other than the Oracle process and software owner accounts, DBAs, auditors, or backup accounts are listed, this is a finding. On Windows Systems (from Windows Explorer): Browse to the \diag directory under the directory specified. Select and right-click on the directory >> Properties >> Security tab. If permissions are granted to everyone, this is a finding. If any account other than the Oracle process and software owner accounts, administrators, database administrators (DBAs), system group or developers authorized to write and debug applications on this database are listed, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270542`

### Rule: Remote administration must be disabled for the Oracle connection manager.

**Rule ID:** `SV-270542r1064904_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote administration provides a potential opportunity for malicious users to make unauthorized changes to the Connection Manager configuration or interrupt its service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the cman.ora file in the ORACLE_HOME/network/admin directory. If the file does not exist, the database is not accessed via Oracle Connection Manager and this check is not a finding. If the entry and value for REMOTE_ADMIN is not listed or is not set to a value of NO (REMOTE_ADMIN = NO), this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270543`

### Rule: Network client connections must be restricted to supported versions.

**Rule ID:** `SV-270543r1064907_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unsupported Oracle network client installations may introduce vulnerabilities to the database. Restriction to use of supported versions helps to protect the database and helps to enforce newer, more robust security controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The SQLNET.ALLOWED_LOGON_VERSION parameter is deprecated in earlier Oracle Database versions. This parameter has been replaced with two new Oracle Net Services parameters: SQLNET.ALLOWED_LOGON_VERSION_SERVER SQLNET.ALLOWED_LOGON_VERSION_CLIENT View the SQLNET.ORA file in the ORACLE_HOME/network/admin directory or the directory specified in the TNS_ADMIN environment variable. Locate the following entries: SQLNET.ALLOWED_LOGON_VERSION_SERVER = 12 SQLNET.ALLOWED_LOGON_VERSION_CLIENT = 12 If the parameters do not exist, this is a finding. If the parameters are not set to a value of 12 or 12a, this is a finding. Note: Attempting to connect with a client version lower than specified in these parameters may result in a misleading error: ORA-01017: invalid username/password: logon denied

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270544`

### Rule: Database administrator (DBA) OS accounts must be granted only those host system privileges necessary for the administration of the Oracle Database.

**Rule ID:** `SV-270544r1065278_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC), is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and nonprivileged account. DBAs, if assigned excessive OS privileges, could perform actions that could endanger the information system or hide evidence of malicious activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review host system privileges assigned to the Oracle DBA group and all individual Oracle DBA accounts. Note: Do not include the Oracle software installation account in any results for this check. For Unix systems (as root): cat /etc/group | grep -i dba groups root If "root" is returned in the first list, this is a finding. If any accounts listed in the first list are also listed in the second list, this is a finding. Investigate any user account group memberships other than DBA or root groups that are returned by the following command (also as root): groups [dba user account] Replace [dba user account] with the user account name of each DBA account. If individual DBA accounts are assigned to groups that grant access or privileges for purposes other than DBA responsibilities, this is a finding. For Windows systems, click Start >> Settings >> Control Panel >> Administrative Tools >> Computer Management >> Local Users and Groups >> Groups >> ORA_DBA. Start >> Settings >> Control Panel >> Administrative Tools >> Computer Management >> Local Users and Groups >> Groups >> ORA_[SID]_DBA (if present). Note: Users assigned DBA privileges on a Windows host are granted membership in the ORA_DBA and/or ORA_[SID]_DBA groups. The ORA_DBA group grants DBA privileges to any database on the system. The ORA_[SID]_DBA groups grant DBA privileges to specific Oracle instances only. Make a note of each user listed. For each user, click Start >> Settings >> Control Panel >> Administrative Tools >> Computer Management >> Local Users and Groups >> Users >> [DBA username] >> Member of. If DBA users belong to any groups other than DBA groups and the Windows Users group, this is a finding. Examine User Rights assigned to DBA groups or group members by clicking Start >> Settings >> Control Panel >> Administrative Tools >> Local Security Policy >> Security Settings >> Local Policies >> User Rights Assignments. If any User Rights are assigned directly to the DBA group(s) or DBA user accounts, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270545`

### Rule: Oracle Database default accounts must be assigned custom passwords.

**Rule ID:** `SV-270545r1064913_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. Database management system (DBMS) default passwords provide a commonly known and exploited means for unauthorized access to database installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use this query to identify the Oracle-supplied accounts that still have their default passwords: SELECT * FROM SYS.DBA_USERS_WITH_DEFPWD; If any accounts other than XS$NULL are listed, this is a finding. XS$NULL is an internal account that represents the absence of a user in a session. Because XS$NULL is not a user, this account can only be accessed by the Oracle Database instance. XS$NULL has no privileges and no one can authenticate as XS$NULL, nor can authentication credentials ever be assigned to XS$NULL.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270546`

### Rule: Oracle Database must provide a mechanism to automatically identify accounts designated as temporary or emergency accounts.

**Rule ID:** `SV-270546r1112478_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary application accounts could be used in the event of a vendor support visit where a support representative requires a temporary unique account to perform diagnostic testing or conduct some other support-related activity. When these types of accounts are created, there is a risk that the temporary account may remain in place and active after the support representative has left. To address this in the event temporary application accounts are required, the application must automatically terminate temporary accounts after an organization-defined time period. Such a process and capability greatly reduces the risk that accounts will be misused, hijacked, or data compromised. Note that user authentication and account management should be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Temporary database accounts must be identified in order for the system to recognize and terminate them after a given time period. The database management system (DBMS) and any administrators must have a means to recognize any temporary accounts for special handling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization has a policy, consistently enforced, forbidding the creation of emergency or temporary accounts, this is not a finding. If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. If using the database to identify temporary accounts, and temporary accounts exist, there should be a temporary profile. If a profile for temporary accounts cannot be identified, this is a finding. To check for a temporary profile, run the scripts below: To obtain a list of profiles: SELECT PROFILE#, NAME FROM SYS.PROFNAME$; To obtain a list of users assigned a given profile (TEMPORARY_USERS, in this example): SELECT USERNAME, PROFILE FROM SYS.DBA_USERS WHERE PROFILE = 'TEMPORARY_USERS' ORDER BY USERNAME;

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270547`

### Rule: Oracle Database must provide a mechanism to automatically remove or disable temporary user accounts after 72 hours.

**Rule ID:** `SV-270547r1064919_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Temporary application accounts could ostensibly be used in the event of a vendor support visit where a support representative requires a temporary unique account to perform diagnostic testing or conduct some other support related activity. When these types of accounts are created, there is a risk that the temporary account may remain in place and active after the support representative has left. To address this, in the event temporary application accounts are required, the application must ensure accounts designated as temporary in nature must automatically terminate these accounts after a period of 72 hours. Such a process and capability greatly reduces the risk that accounts will be misused, hijacked, or data compromised. Note that user authentication and account management should be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Temporary database accounts must be automatically terminated after a 72-hour time period to mitigate the risk of the account being used beyond its original purpose or timeframe.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization has a policy, consistently enforced, forbidding the creation of emergency or temporary accounts, this is not a finding. If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. Check database management system (DBMS) settings, OS settings, and/or enterprise-level authentication/access mechanisms settings to determine if the site uses a mechanism whereby temporary are terminated after a 72-hour time period. If not, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270548`

### Rule: Oracle Database must be protected from unauthorized access by developers on shared production/development host systems.

**Rule ID:** `SV-270548r1064922_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications employ the concept of least privilege for specific duties and information systems (including specific functions, ports, protocols, and services). The concept of least privilege is also applied to information system processes, ensuring that the processes operate at privilege levels no higher than necessary to accomplish required organizational missions and/or functions. Organizations consider the creation of additional processes, roles, and information system accounts as necessary to achieve least privilege. Organizations also apply least privilege concepts to the design, development, implementation, and operations of information systems. Developers granted elevated database and/or operating system privileges on systems that support both development and production databases can affect the operation and/or security of the production database system. Operating system and database privileges assigned to developers on shared development and production systems must be restricted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify whether any hosts contain both development and production databases. If no hosts contain both production and development databases, this is Not Applicable. For any host containing both a development and a production database, determine if developers have been granted elevated privileges on the production database or on the OS. If they have, ask for documentation that shows these accounts have formal approval and risk acceptance. If this documentation does not exist, this is a finding. If developer accounts exist with the right to create and maintain tables (or other database objects) in production tablespaces, this is a finding. To check the number of instances on the host machine where applicable, check the /etc/oratab. The /etc/oratab file is updated by the Oracle Installer when the database is installed when the root.sh file is executed. Each line in the represents an ORACLE_SID:ORACLE_HOME:Y or N. The ORACLE_SID and ORACLE_HOME are self-explanatory. The Y or N signals the DBSTART program to automatically start or not start that specific instance when the machine is restarted. Check with the system owner and application development team to find what each entry represents. If a system is deemed to be a production system, review the system for development users.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270549`

### Rule: Oracle Database must verify account lockouts persist until reset by an administrator.

**Rule ID:** `SV-270549r1112480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed, to allow for the use of an application, there is a risk that attempts will be made to obtain unauthorized access. To defeat these attempts, organizations define the number of times a user account may consecutively fail a logon attempt. The organization also defines the period of time in which these consecutive failed attempts may occur. By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The account lockout duration is defined in the profile assigned to a user. To verify what profile is assigned to a user, enter the query: SQL>SELECT profile FROM dba_users WHERE username = '<username>' This will return the profile name assigned to that user. The user profile, ORA_STIG_PROFILE, has been provided to satisfy the STIG requirements pertaining to the profile parameters. Oracle recommends that this profile be customized with any site-specific requirements and assigned to all users where applicable. Note: It remains necessary to create a customized replacement for the password validation function, ORA12C_STIG_VERIFY_FUNCTION, if relying on this technique to verify password complexity. Now check the values assigned to the profile returned from the query above: column profile format a20 column limit format a20 SQL>SELECT PROFILE, RESOURCE_NAME, LIMIT FROM DBA_PROFILES WHERE PROFILE = 'ORA_STIG_PROFILE'; Check the settings for password_lock_time - this specifies how long to lock the account after the number of consecutive failed logon attempts reaches the limit. If the value is not UNLIMITED, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270550`

### Rule: Oracle Database must set the maximum number of consecutive invalid logon attempts to three.

**Rule ID:** `SV-270550r1112482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anytime an authentication method is exposed, to allow for the use of an application, there is a risk that attempts will be made to obtain unauthorized access. To defeat these attempts, organizations define the number of times a user account may consecutively fail a logon attempt. The organization also defines the period of time in which these consecutive failed attempts may occur. By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. More recent brute force attacks make attempts over long periods of time to circumvent intrusion detection systems and system account lockouts based entirely on the number of failed logons that are typically reset after a successful logon. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle. Note also that a policy that places no limit on the length of the timeframe (for counting consecutive invalid attempts) does satisfy this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The limit on the number of consecutive failed logon attempts is defined in the profile assigned to a user. Check the FAILED_LOGIN_ATTEMPTS value assigned to the profiles returned from this query: SQL>SELECT PROFILE, RESOURCE_NAME, LIMIT FROM DBA_PROFILES; Check the setting for FAILED_LOGIN_ATTEMPTS. This is the number of consecutive failed logon attempts before locking the Oracle user account. If the value is greater than three on any of the profiles, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-270551`

### Rule: Oracle Database must disable user accounts after 35 days of inactivity.

**Rule ID:** `SV-270551r1112483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive database management system (DBMS) account can potentially obtain and maintain undetected access to the database. Owners of inactive DBMS accounts will not notice if unauthorized access to their user account has been obtained. All DBMS need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. To address access requirements, some database administrators choose to integrate their databases with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the database administrator to off-load those access control functions and focus on core application features and functionality. This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local logon administrator accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are managed and authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For accounts managed by Oracle, check DBMS settings to determine if accounts are automatically disabled by the system after 35 days of inactivity. In Oracle 12c, Oracle introduced a new security parameter in the profile called INACTIVE_ACCOUNT_TIME. This parameter specifies the number of days permitted the account will be in OPEN state since the last login, after that will be LOCKED if no successful logins happens after the specified duration. Check to verify what profile each user is associated with, if any, with this query: select username, profile from dba_users order by 1,2; Then, check the profile to verify what the inactive_account_time is set to in the table dba_profiles; the inactive_account_time is a value stored in the LIMIT column, and identified by the value inactive_account_time in the RESOURCE_NAME column. SQL>select profile, resource_name, resource_type, limit from dba_profiles where upper(resource_name) = 'INACTIVE_ACCOUNT_TIME'; If the INACTIVE_ACCOUNT_TIME parameter is set to UNLIMITED (default) or it is set to more than 35 days, this is a finding. If INACTIVE_ACCOUNT_TIME is not a parameter associated with the profile, then check for a script or an automated job that is run daily that checks the audit trail or to ensure every user account has logged in within the last 35 days. If one is not present, this is a finding.

## Group: SRG-APP-000141-DB-000090

**Group ID:** `V-270552`

### Rule: Oracle Database default demonstration and sample databases, database objects, and applications must be removed.

**Rule ID:** `SV-270552r1064934_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the database management system (DBMS) and host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If Oracle is hosted on a server that does not support production systems, and is designated for the deployment of samples and demonstrations, this is Not Applicable. Review documentation and websites from Oracle and any other relevant vendors for vendor-provided demonstration or sample databases, database applications, schemas, objects, and files. Review the Oracle DBMS to determine if any of the demonstration and sample databases, schemas, database applications, or files are installed in the database or are included with the DBMS application. If any are present in the database or are included with the DBMS application, this is a finding. The Oracle Default Sample Schema User Accounts are: BI: Owns the Business Intelligence schema included in the Oracle Sample Schemas. HR: Manages the Human Resources schema. Schema stores information about the employees and the facilities of the company. OE: Manages the Order Entry schema. Schema stores product inventories and sales of the company's products through various channels. PM: Manages the Product Media schema. Schema contains descriptions and detailed information about each product sold by the company. IX: Manages the Information Exchange schema. Schema manages shipping through business-to-business (B2B) applications database. SH: Manages the Sales schema. Schema stores statistics to facilitate business decisions. SCOTT: A demonstration account with a simple schema. Connect to Oracle as SYSDBA and run the following SQL to check for presence of Oracle Default Sample Schema User Accounts: select distinct(username) from dba_users where username in ('BI','HR','OE','PM','IX','SH','SCOTT'); If any of the users listed above is returned, it means that there are demo programs installed, and this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-270553`

### Rule: Unused database components, database management system (DBMS) software, and database objects must be removed.

**Rule ID:** `SV-270553r1064937_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Demonstration and sample database objects and applications present publicly known attack points for malicious users. These demonstration and sample objects are meant to provide simple examples of coding specific functions and are not developed to prevent vulnerabilities from being introduced to the database management system (DBMS) and host system. Unused and unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run this query to produce a list of components and features installed with the database: SELECT comp_id, comp_name, version, status from dba_registry WHERE comp_id not in ('CATJAVA','CATALOG','CATPROC','SDO','DV','XDB') AND status <> 'OPTION OFF'; Review the list. If unused components are installed and are not documented and authorized, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-270554`

### Rule: Unused database components that are integrated in the database management system (DBMS) and cannot be uninstalled must be disabled.

**Rule ID:** `SV-270554r1065221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, any functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plug-ins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for the DBMS by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run this query to check to verify what integrated components are installed in the database: SELECT parameter, value from v$option where parameter in ( 'Data Mining', 'Oracle Database Extensions for .NET', 'OLAP', 'Partitioning', 'Real Application Testing' ); This will return all of the relevant database options and their status. TRUE means that the option is installed. If the option is not installed, the option will be set to FALSE. Review the options and check the system documentation to verify what is required. If all listed components are authorized to be in use, this is not a finding. If any unused components or features are listed by the query as TRUE, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-270555`

### Rule: OS accounts used to run external procedures called by Oracle Database must have limited privileges.

**Rule ID:** `SV-270555r1115550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is intended to limit exposure due to operating from within a privileged account or role. The inclusion of role is intended to address those situations where an access control policy, such as Role Based Access Control (RBAC) is being implemented and where a change of role provides the same degree of assurance in the change of access authorizations for both the user and all processes acting on behalf of the user as would be provided by a change between a privileged and nonprivileged account. To limit exposure when operating from within a privileged account or role, the application must support organizational requirements that users of information system accounts, or roles, with access to organization-defined lists of security functions or security-relevant information, use nonprivileged accounts, or roles, when accessing other (nonsecurity) system functions. Use of privileged accounts for nonadministrative purposes puts data at risk of unintended or unauthorized loss, modification, or exposure. In particular, database administrator (DBA) accounts if used for nonadministration application development or application maintenance can lead to misassignment of privileges where privileges are inherited by object owners. It may also lead to loss or compromise of application data where the elevated privileges bypass controls designed in and provided by applications. External applications called or spawned by the database management system (DBMS) process may be executed under OS accounts with unnecessary privileges. This can lead to unauthorized access to OS resources and compromise of the OS, the DBMS or any other services provided by the host platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine which OS accounts are used by Oracle to run external procedures. Validate that these OS accounts have only the privileges necessary to perform the required functionality. If any OS accounts used by the database for running external procedures have privileges beyond those required for running the external procedures, this is a finding. If use of the external procedure agent is authorized, ensure extproc is restricted to execution of authorized applications. External jobs are run using the account "nobody" by default. Review the contents of the file ORACLE_HOME/rdbms/admin/externaljob.ora for the lines run_user= and run_group=. If the user assigned to these parameters is not "nobody", this is a finding. System views providing privilege information are: DBA_SYS_PRIVS DBA_TAB_PRIVS DBA_ROLE_PRIVS

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-270556`

### Rule: Use of external executables must be authorized.

**Rule ID:** `SV-270556r1064946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. Examples include, but are not limited to, installing advertising software, demonstrations, or browser plugins not related to requirements or providing a wide array of functionality not required for the mission. Applications must adhere to the principles of least functionality by providing only essential capabilities. Database management systems (DBMSs) may spawn additional external processes to execute procedures that are defined in the DBMS, but stored in external host files (external procedures). The spawned process used to execute the external procedure may operate within a different OS security context than the DBMS and provide unauthorized access to the host system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the database for definitions of application executable objects stored external to the database. Determine if there are methods to disable use or access, or to remove definitions for external executable objects. Verify any application executable objects listed are authorized by the information system security officer (ISSO). To check for external procedures, execute the following query, which will provide the libraries containing external procedures, the owners of those libraries, users that have been granted access to those libraries, and the privileges they have been granted. If there are owners other than the owners Oracle provides, then there might be executable objects stored either in the database or external to the database that are called by objects in the database. (connect as sysdba) set linesize 130 column library_name format a25 column name format a15 column owner format a15 column grantee format a15 column privilege format a15 select library_name,owner, '' grantee, '' privilege from dba_libraries where file_spec is not null and owner not in ('SYS', 'ORDSYS') minus ( select library_name,o.name owner, '' grantee, '' privilege from dba_libraries l, sys.user$ o, sys.user$ ge, sys.obj$ obj, sys.objauth$ oa where l.owner=o.name and obj.owner#=o.user# and obj.name=l.library_name and oa.obj#=obj.obj# and ge.user#=oa.grantee# and l.file_spec is not null ) union all select library_name,o.name owner, --obj.obj#,oa.privilege#, ge.name grantee, tpm.name privilege from dba_libraries l, sys.user$ o, sys.user$ ge, sys.obj$ obj, sys.objauth$ oa, sys.table_privilege_map tpm where l.owner=o.name and obj.owner#=o.user# and obj.name=l.library_name and oa.obj#=obj.obj# and ge.user#=oa.grantee# and tpm.privilege=oa.privilege# and l.file_spec is not null / If any owners are returned other than those Oracle provides, ensure those owners are authorized to access those libraries. If there are users that have been granted access to libraries that are not authorized, this is a finding.

## Group: SRG-APP-000141-DB-000093

**Group ID:** `V-270557`

### Rule: Access to external executables must be disabled or restricted.

**Rule ID:** `SV-270557r1065281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle external procedure capability provides use of the Oracle process account outside the operation of the database management system (DBMS) process. It can be used to submit and execute applications stored externally from the database under operating system controls. The external procedure process is the subject of frequent and successful attacks as it allows unauthenticated use of the Oracle process account on the operating system. As of Oracle version 11.1, the external procedure agent may be run directly from the database and not require use of the Oracle listener. This reduces the risk of unauthorized access to the procedure from outside of the database process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine if the use of the external procedure agent is authorized. Review the ORACLE_HOME/bin directory or search the ORACLE_BASE path for the executable extproc (Unix) or extproc.exe (Windows). If external procedure agent is not authorized for use in the system documentation and the executable file does not exist or is restricted, this is not a finding. If external procedure agent is not authorized for use in the system documentation and the executable file exists and is not restricted, this is a finding. If use of the external procedure agent is authorized, ensure extproc is restricted to execution of authorized applications. External jobs are run using the account "nobody" by default. Review the contents of the file ORACLE_HOME/rdbms/admin/externaljob.ora for the lines run_user= and run_group=. If the user assigned to these parameters is not "nobody", this is a finding. The external procedure agent (extproc executable) is available directly from the database and does not require definition in the listener.ora file for use. Review the contents of the file ORACLE_HOME/hs/admin/extproc.ora. If the file does not exist, this is a finding. If the following entry does not appear in the file, this is a finding: EXTPROC_DLLS=ONLY:[dll full file name1]:[dll full file name2]:.. [dll full file name] represents a full path and file name. This list of file names is separated by ":". Note: If "ONLY" is specified, then the list is restricted to allow execution of only the DLLs specified in the list and is not a finding. If "ANY" is specified, then there are no restrictions for execution except what is controlled by operating system permissions and is a finding. If no specification is made, any files located in the %ORACLE_HOME%\bin directory on Windows systems or $ORACLE_HOME/lib directory on Unix systems can be executed (the default) and is a finding. Ensure that EXTPROC is not accessible from the listener. Review the listener.ora file. If any entries reference "extproc", this is a finding. Determine if the external procedure agent is in use per Oracle 10.x conventions. Review the listener.ora file. If any entries reference "extproc", then the agent is in use. If external procedure agent is not authorized for use in the system documentation and references to "extproc" exist, this is a finding. Sample listener.ora entries with extproc included: LISTENER = (DESCRIPTION = (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521)) ) EXTLSNR = (DESCRIPTION = (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC)) ) SID_LIST_LISTENER = (SID_LIST = (SID_DESC = (GLOBAL_DBNAME = ORCL) (ORACLE_HOME = /home/oracle/app/oracle/product/19.0/db_1) (SID_NAME = ORCL) ) ) SID_LIST_EXTLSNR = (SID_LIST = (SID_DESC = (PROGRAM = extproc) (SID_NAME = PLSExtProc) (ORACLE_HOME = /home/oracle/app/oracle/product/19.0/db_1) (ENVS="EXTPROC_DLLS=ONLY:/home/app1/app1lib.so:/home/app2/app2lib.so, LD_LIBRARY_PATH=/private/app2/lib:/private/app1, MYPATH=/usr/fso:/usr/local/packages") ) ) Sample tnsnames.ora entries with extproc included: ORCL = (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521)) ) (CONNECT_DATA = (SERVICE_NAME = ORCL) ) ) EXTPROC_CONNECTION_DATA = (DESCRIPTION = (ADDRESS_LIST = (ADDRESS = (PROTOCOL = IPC)(KEY = extproc)) ) (CONNECT_DATA = (SERVER = DEDICATED) (SERVICE_NAME = PLSExtProc) ) ) If EXTPROC is in use, confirm that a listener is dedicated to serving the external procedure agent (as shown above). View the protocols configured for the listener. For the listener to be dedicated, the only entries will be to specify extproc. If there is not a dedicated listener in use for the external procedure agent, this is a finding. If the PROTOCOL= specified is other than IPC, this is a finding. Verify and ensure extproc is restricted executing authorized external applications only and extproc is restricted to execution of authorized applications. Review the listener.ora file. If the following entry does not exist, this is a finding: EXTPROC_DLLS=ONLY:[dll full file name1]:[dll full file name2]:... Note: [dll full file name] represents a full path and file name. This list of file names is separated by ":". Note: If "ONLY" is specified, then the list is restricted to allow execution of only the DLLs specified in the list and is not a finding. If "ANY" is specified, then there are no restrictions for execution except what is controlled by operating system permissions and is a finding. If no specification is made, any files located in the %ORACLE_HOME%\bin directory on Windows systems or $ORACLE_HOME/lib directory on Unix systems can be executed (the default) and is a finding. View the listener.ora file (usually in ORACLE_HOME/network/admin or directory specified by the TNS_ADMIN environment variable). If multiple listener processes are running, then the listener.ora file for each must be viewed. For each process, determine the directory specified in the ORACLE_HOME or TNS_ADMIN environment variable defined for the process account to locate the listener.ora file.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-270558`

### Rule: Oracle Database must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the Ports, Protocols, and Services Management Category Assurance List (PPSM CAL) and vulnerability assessments.

**Rule ID:** `SV-270558r1065283_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols/services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system. Satisfies: SRG-APP-000142-DB-000094, SRG-APP-000383-DB-000364</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the database management system (DBMS) settings for unapproved functions, ports, protocols, and services. If any are found, this is a finding. For definitive information on PPSM, refer to https://cyber.mil/ppsm/. - - - - - In the Oracle database, the communications with the database and incoming requests are performed by the Oracle Listener. The Oracle Listener listens on a specific port or ports for connections to a specific database. The Oracle Listener has configuration files located in the $ORACLE_HOME/network/admin directory. To check the ports and protocols in use, go to that directory and review the SQLNET.ora, LISTENER.ora, and the TNSNAMES.ora. If protocols or ports are in use that are not authorized, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-270559`

### Rule: Oracle Database must ensure users are authenticated with an individual authenticator prior to using a shared authenticator.

**Rule ID:** `SV-270559r1068298_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, application users (and any processes acting on behalf of users) must be individually identified and authenticated. A shared authenticator is a generic account used by multiple individuals. Use of a shared authenticator alone does not uniquely identify individual users. An example of a shared authenticator is the Unix OS "root" user account, a Windows "administrator" account, a "SA" account, or a "helpdesk" account. For example, the Unix and Windows operating systems offer a "switch user" capability allowing users to authenticate with their individual credentials and, when needed, switch to the administrator role. This method provides for unique individual authentication prior to using a shared authenticator. Some applications may not have the need to provide a group authenticator; this is considered a matter of application design. In those instances where the application design includes the use of a shared authenticator, this requirement will apply. There may also be instances when specific user actions need to be performed on the information system without unique user identification or authentication. An example of this type of access is a web server which contains publicly releasable information. These types of accesses are allowed but must be explicitly identified and documented by the organization. When shared accounts are used without another means of identifying individual users, users may deny having performed a particular action. Oracle Access Manager may be helpful in meeting this requirement. Oracle Access Manager is used when there is a need for multifactor authentication of applications front-ending Oracle Datasets that may use group accounts. Oracle Access Manager supports using PKI-based smart cards (CAC, PIV) for multifactor authentication. When a user authenticates to a smart card application, the smart card engine produces a certificate-based authentication token. Can configure a certificate-based authentication scheme in Oracle Access Manager that uses information from the smart card certificate. Certificate-based authentication works with any smart card or similar device that presents an X.509 certificate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review database management system (DBMS) settings, OS settings, and/or enterprise-level authentication/access mechanism settings to determine whether shared accounts exist. If shared accounts do not exist, this is Not Applicable. Review DBMS settings to determine if individual authentication is required before shared authentication. If shared authentication does not require prior individual authentication, this is a finding. If using Oracle Access Manager: Verify the Authentication Module is set up properly: 1. Go to the Oracle Access Manager Home Screen and click the Policy Configuration tab. Select the X509Scheme. 2. Ensure the Authentication Module option is set to X509Plugin. Verify the Authentication policy is using the x509Scheme: 1. Go to Oracle Access Manager Home Screen and click the Policy Configuration tab. 2. Select Application Domains. Select Search. 3. Select the application domain protecting the Oracle Database. 4. Select the Authentication Policies tab and click Protected Resource Policy. 5. Make sure the Authentication Scheme is set to x509Scheme.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-270560`

### Rule: Oracle Database must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-270560r1065286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthorized access, organizational users must be identified and authenticated. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Users (and any processes acting on behalf of users) are uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization which outlines specific user actions that can be performed on the information system without identification or authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review database management system (DBMS) settings, OS settings, and/or enterprise-level authentication/access mechanism settings, and site practices, to determine whether organizational users are uniquely identified and authenticated when logging on to the system. If organizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-270561`

### Rule: Oracle Database must enforce the DOD standards for password complexity.

**Rule ID:** `SV-270561r1112485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>OS/enterprise authentication and identification must be used (SRG-APP-000023-DB-000001). Native database management system (DBMS) authentication may be used only when circumstances make it unavoidable; and must be documented and authorizing official (AO)-approved. The DOD standard for authentication is DOD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate and requires AO approval. In such cases, the DOD standards for password complexity and lifetime must be implemented. DBMS products that can inherit the rules for these from the operating system or access control program (e.g., Microsoft Active Directory) must be configured to do so. For other DBMSs, the rules must be enforced using available configuration parameters or custom code. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. This requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' ORDER BY PROFILE; Note: Profiles can inherit settings from another profile so some password functions could be set to DEFAULT. If so, review the DEFAULT profile function name. If the function name is null for any profile, this is a finding. Review the password verification functions specified for the PASSWORD_VERIFY_FUNCTION settings for each profile. Determine whether the following rules are enforced by the code in those functions. a. Minimum of 15 characters, including at least one of each of the following character sets: - Uppercase - Lowercase - Numeric - Special characters (e.g., ~ ! @ # $ % ^ & * ( ) _ + = - ' [ ] / ? > <) b. Minimum number of characters changed from previous password: 50 percent of the minimum password length; that is, eight. If any of the above password requirements are not included in the function, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-270562`

### Rule: Procedures for establishing temporary passwords that meet DOD password requirements for new accounts must be defined, documented, and implemented.

**Rule ID:** `SV-270562r1064964_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. New accounts authenticated by passwords that are created without a password or with an easily guessed password are vulnerable to unauthorized access. Procedures for creating new accounts with passwords should include the required assignment of a temporary password to be modified by the user upon first use. Note that user authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP With respect to Oracle, this requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. Where accounts are authenticated using passwords, review procedures and implementation evidence for creation of temporary passwords. If the procedures or evidence do not exist or do not enforce passwords to meet DOD password requirements, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-270563`

### Rule: Oracle Database must enforce password maximum lifetime restrictions.

**Rule ID:** `SV-270563r1064967_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password maximum lifetime is the maximum period of time, (typically in days) a user's password may be in effect before the user is forced to change it. Passwords need to be changed at specific policy-based intervals as per policy. Any password, no matter how complex, can eventually be cracked. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. The PASSWORD_LIFE_TIME parameter defines the number of days a password remains valid. This can must not be set to UNLIMITED. Further, the PASSWORD_GRACE_TIME parameter, if set to UNLIMITED, can nullify the PASSWORD_LIFE_TIME. PASSWORD_GRACE_TIME must be set to 0 days (or another small integer). Note: User authentication and account management must be done via an enterprise-wide mechanism whenever possible. Examples of enterprise-level authentication/access mechanisms include, but are not limited to, Active Directory and LDAP. With respect to Oracle, this requirement applies to cases where it is necessary to have accounts directly managed by Oracle.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. Review database management system (DBMS) settings to determine if passwords must be changed periodically. Run the following script: SELECT p1.profile, CASE DECODE(p1.limit, 'DEFAULT', p3.limit, p1.limit) WHEN 'UNLIMITED' THEN 'UNLIMITED' ELSE CASE DECODE(p2.limit, 'DEFAULT', p4.limit, p2.limit) WHEN 'UNLIMITED' THEN 'UNLIMITED' ELSE TO_CHAR(DECODE(p1.limit, 'DEFAULT', p3.limit, p1.limit) + DECODE(p2.limit, 'DEFAULT', p4.limit, p2.limit)) END END effective_life_time FROM dba_profiles p1, dba_profiles p2, dba_profiles p3, dba_profiles p4 WHERE p1.profile=p2.profile AND p3.profile='DEFAULT' AND p4.profile='DEFAULT' AND p1.resource_name='PASSWORD_LIFE_TIME' AND p2.resource_name='PASSWORD_GRACE_TIME' AND p3.resource_name='PASSWORD_LIFE_TIME' -- from DEFAULT profile AND p4.resource_name='PASSWORD_GRACE_TIME' -- from DEFAULT profile order by 1; If the EFFECTIVE_LIFE_TIME is greater than 60 for any profile applied to user accounts, and the need for this has not been documented and approved, this is a finding. If PASSWORD_LIFE_TIME or PASSWORD_GRACE_TIME is set to "UNLIMITED", this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-270564`

### Rule: Oracle Database must for password-based authentication, store passwords using an approved salted key derivation function, preferably using a keyed hash.

**Rule ID:** `SV-270564r1065291_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate and requires authorizing official (AO) approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to the database management system (DBMS). Database passwords stored in clear text are vulnerable to unauthorized disclosure. Database passwords must always be encoded or encrypted when stored internally or externally to the DBMS. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names that include "SSL", such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Oracle Database stores and displays its passwords in encrypted form. Nevertheless, this should be verified by reviewing the relevant system views, along with the other items to be checked here. Review the list of DBMS database objects, database configuration files, associated scripts, and applications defined within and external to the DBMS that access the database. The list should also include files, tables, or settings used to configure the operational environment for the DBMS and for interactive DBMS user accounts. Determine whether any DBMS database objects, database configuration files, associated scripts, applications defined within or external to the DBMS that access the database, and DBMS/user environment files/settings contain database passwords. If any do, confirm that DBMS passwords stored internally or externally to the DBMS are hashed using FIPS-approved cryptographic algorithms and include a salt. If any passwords are stored in clear text, this is a finding. If any passwords are stored with reversible encryption, this is a finding. Determine if an external password store for applications, batch jobs, and scripts is in use. Verify that all passwords stored there are encrypted. If a password store is used and any password is not encrypted, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-270565`

### Rule: If passwords are used for authentication, the Oracle Database must transmit only encrypted representations of passwords.

**Rule ID:** `SV-270565r1064973_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate, and requires authorizing official (AO) approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Database management system (DBMS) passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including "SSL", such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. Review configuration settings for encrypting passwords in transit across the network. If passwords are not encrypted, this is a finding. The database supports PKI-based authentication by using digital certificates over TLS in addition to the native encryption and data integrity capabilities of these protocols. Oracle provides a complete PKI that is based on RSA Security, Inc., Public-Key Cryptography Standards, and which interoperates with Oracle servers and clients. The database uses a wallet that is a container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by TLS. In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates. Verify that the $ORACLE_HOME/network/admin/sqlnet.ora contains entries similar to the following to ensure TLS is installed: WALLET_LOCATION = (SOURCE= (METHOD = FILE) (METHOD_DATA = DIRECTORY=/wallet) SSL_CIPHER_SUITES=(SSL_cipher_suiteExample) SSL_VERSION = 3.0 SSL_CLIENT_AUTHENTICATION=TRUE If the sqlnet.ora file does not contain such entries, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-270566`

### Rule: Oracle Database, when using public key infrastructure (PKI)-based authentication, must enforce authorized access to the corresponding private key.

**Rule ID:** `SV-270566r1064976_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The cornerstone of the PKI is the private key used to encrypt or digitally sign information. If the private key is stolen, this will lead to the compromise of the authentication and nonrepudiation gained through PKI because the attacker can use the private key to digitally sign documents and can pretend to be the authorized user. Both the holders of a digital certificate and the issuing authority must protect the computers, storage devices, or whatever they use to keep the private keys. All access to the private key of Oracle Database must be restricted to authorized and authenticated users. If unauthorized users have access to the database management system's (DBMS's) private key, an attacker could gain access to the primary key and use it to impersonate the database on the network. Transport Layer Security (TLS) is the successor protocol to Secure Sockets Layer (SSL). Although the Oracle configuration parameters have names including 'SSL', such as SSL_VERSION and SSL_CIPHER_SUITES, they refer to TLS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS configuration to determine whether appropriate access controls exist to protect the DBMS's private key. If strong access controls do not exist to enforce authorized access to the private key, this is a finding. The database supports authentication by using digital certificates over TLS in addition to the native encryption and data integrity capabilities of these protocols. An Oracle Wallet is a container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by TLS. In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates, with the exception of Diffie-Hellman. Verify the $ORACLE_HOME/network/admin/sqlnet.ora contains entries similar to the following to ensure TLS is installed: WALLET_LOCATION = (SOURCE= (METHOD = FILE) (METHOD_DATA = DIRECTORY=/wallet) SSL_CIPHER_SUITES=(SSL_cipher_suiteExample) SSL_VERSION = 3.0 SSL_CLIENT_AUTHENTICATION=TRUE If the sqlnet.ora file does not contain such entries, this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-270567`

### Rule: Oracle Database must map the authenticated identity to the user account using public key infrastructure (PKI)-based authentication.

**Rule ID:** `SV-270567r1064979_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to a database management system (DBMS) user account for the authenticated identity to be meaningful to the DBMS and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS configuration to verify DBMS user accounts are being mapped directly to unique identifying information within the validated PKI certificate. If user accounts are not being mapped to authenticated identities, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-270568`

### Rule: When using command-line tools such as Oracle SQL*Plus, which can accept a plain-text password, users must use an alternative logon method that does not expose the password.

**Rule ID:** `SV-270568r1065293_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Normally, with PKI authentication, the interaction with the user for authentication will be handled by a software component separate from the database management system (DBMS), such as ActivIdentity ActivClient. However, in cases where the DBMS controls the interaction, this requirement applies. To prevent the compromise of authentication information such as passwords and PINs during the authentication process, the feedback from the system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided authentication secrets when typed into the system is a method used in addressing this risk. Displaying asterisks when a user types in a password or a smart card PIN is an example of obscuring feedback of authentication secrets. This requires reviewing applications, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For Oracle SQL*Plus, which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations; and that authorizing official (AO) approval has been obtained. If not, this is a finding. Request evidence that all users of the tool are trained in the importance of not using the plain-text password option and in how to keep the password hidden; and that they adhere to this practice. If not, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-270569`

### Rule: Oracle Database must use NIST-validated FIPS 140-2/140-3 compliant cryptography for authentication mechanisms.

**Rule ID:** `SV-270569r1065205_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of using encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the database management system (DBMS). Applications (including DBMSs) using cryptography are required to use approved NIST FIPS 140-2/140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While federal agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules. More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following settings to verify FIPS 140-2 or FIPS 140-3 authentication/encryption is configured. If encryption is required but not configured, check with the database administrator (DBA) and system administrator to verify if other mechanisms or third-party cryptography products are deployed for authentication. To verify if Oracle is configured for FIPS 140 Secure Sockets Layer (SSL)/Transport Layer Security (TLS) authentication and/or encryption: Open the fips.ora file in a browser or editor. (The default location for fips.ora is $ORACLE_HOME/ldap/admin/ but alternate locations are possible. An alternate location, if it is in use, is specified in the FIPS_HOME environment variable.) If the line "SSLFIPS_140=TRUE" is not found in fips.ora, or the file does not exist, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-270570`

### Rule: Oracle Database must uniquely identify and authenticate nonorganizational users (or processes acting on behalf of nonorganizational users).

**Rule ID:** `SV-270570r1065294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonorganizational users include all information system users other than organizational users which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Nonorganizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review database management system (DBMS) settings to determine whether nonorganizational users are uniquely identified and authenticated when logging onto the system. If nonorganizational users are not uniquely identified and authenticated, this is a finding.

## Group: SRG-APP-000514-DB-000383

**Group ID:** `V-270571`

### Rule: Oracle Database must implement NIST FIPS 140-2/140-3 validated cryptographic modules to protect unclassified information requiring confidentiality and cryptographic protection, in accordance with the data owner's requirements.

**Rule ID:** `SV-270571r1065207_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. For detailed information, refer to NIST FIPS Publication 140-3, Security Requirements For Cryptographic Modules. Note that the product's cryptographic modules must be validated and certified by NIST as FIPS-compliant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If encryption is not required for the database, this is not a finding. If the database management system (DBMS) has not implemented federally required cryptographic protections for the level of classification of the data it contains, this is a finding. Check the following settings to verify FIPS 140-2/140-3 encryption is configured. If encryption is not configured, check with the database administrator (DBA) and system administrator (SA) to verify if other mechanisms or third-party products are deployed to encrypt data during the transmission or storage of data. For Transparent Data Encryption and DBMS_CRYPTO: To verify if Oracle is configured for FIPS 140 Transparent Data Encryption and/or DBMS_CRYPTO, enter the following SQL*Plus command: SHOW PARAMETER DBFIPS_140 or the following SQL query: SELECT * FROM SYS.V$PARAMETER WHERE NAME = 'DBFIPS_140'; If Oracle returns the value "FALSE", or returns no rows, this is a finding. To verify if Oracle is configured for FIPS 140 Secure Sockets Layer (SSL)/Transport Layer Security (TLS) authentication and/or encryption: Open the fips.ora file in a browser or editor. (The default location for fips.ora is $ORACLE_HOME/ldap/admin/ but alternate locations are possible. An alternate location, if it is in use, is specified in the FIPS_HOME environment variable.) If the line "SSLFIPS_140=TRUE" is not found in fips.ora, or the file does not exist, this is a finding. For (Native) Network Data Encryption: If the line, SQLNET.FIPS_140=TRUE is not found in $ORACLE_HOME/network/admin/sqlnet.ora, this is a finding. (Note: This assumes that a single sqlnet.ora file, in the default location, is in use).

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-270572`

### Rule: Oracle Database must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-270572r1064994_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers, and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding database management system (DBMS) management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and vendor documentation to verify administrative functionality is separate from user functionality. If administrator and general user functionality is not separated either physically or logically, this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-270573`

### Rule: Oracle Database must preserve any organization-defined system state information in the event of a system failure.

**Rule ID:** `SV-270573r1064997_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a known state can address safety or security in accordance with the mission/business needs of the organization. Failure in a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving information system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the database is used solely for transient data (such as one dedicated to Extract-Transform-Load [ETL]), and a clear plan exists for the recovery of the database by means other than archiving, this is not a finding. If it has been determined that up-to-the second recovery is not necessary and this fact is recorded in the system documentation, with appropriate approval, this is not a finding. Check database management system (DBMS) settings to determine whether system state information is being preserved in the event of a system failure. The necessary state information is defined as "information necessary to determine cause of failure and to return to operations with least disruption to mission/business processes". Oracle creates what is known as archive logs. Archive logs contain information required to replay a transaction should something happen. The redo logs are also used to copy transactions or pieces of transactions. Issue the following commands to check the status of archive log mode: $ sqlplus connect as sysdba --Check current archivelog mode in database SQL> archive log list Database log mode Archive Mode Automatic archival Enabled Archive destination /home/oracle/app/oracle/arc2/ORCL Oldest online log sequence 433 Next log sequence to archive 435 Current log sequence 435 If archive log mode is not enabled, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-270574`

### Rule: Oracle Database must take needed steps to protect data at rest and ensure confidentiality and integrity of application data.

**Rule ID:** `SV-270574r1065000_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in nonmobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User-generated data and application-specific configuration data both need to be protected. Configurations and/or rule sets for firewalls, gateways, intrusion detection/prevention systems, and filtering routers and authenticator content are examples of system information likely requiring protection. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the application owner and authorizing official (AO) have determined that encryption of data at rest is not required, this is not a finding. Review database management system (DBMS) settings to determine whether controls exist to protect the confidentiality and integrity of data at rest in the database. If controls do not exist or are not enabled, this is a finding. To ensure that the appropriate controls are in place, discuss the precautions taken with the site database administrators (DBAs) and system administrators (SAs) and try to modify data at rest. Oracle recommends using Transparent Data Encryption, which is part of Oracle Advanced Security Option, to protect data. To check to verify the data is encrypted, for example, upon an auditor's request Oracle provides views that document the encryption status of the database. For TDE column encryption, use the view "dba_encrypted_columns", which lists the owner, table name, column name, encryption algorithm, and salt for all encrypted columns. For TDE tablespace encryption, the following SQL statement lists all encrypted tablespaces with their encryption algorithm and corresponding, encrypted, data files. Issue the following commands to check to verify the data at rest is encrypted. $ sqlplus connect as sysdba SQL> SELECT t.name "TSName", e.encryptionalg "Algorithm", d.file_name "File Name" FROM v$tablespace t, v$encrypted_tablespaces e, dba_data_files d WHERE t.ts# = e.ts# and t.name = d.tablespace_name; The next SQL statement lists the table owner, tables within encrypted tablespaces, and the encryption algorithm: SQL> SELECT a.owner "Owner", a.table_name "Table Name", e.encryptionalg "Algorithm" FROM dba_tables a, v$encrypted_tablespaces e WHERE a.tablespace_name in (select t.name from v$tablespace t, v$encrypted_tablespaces e where t.ts# = e.ts#);

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-270575`

### Rule: Oracle Database must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-270575r1065003_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management systems (DBMSs) handling data requiring data at rest protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to the DBMS or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. Review the configuration of the DBMS, operating system/file system, and additional software as relevant. If any of the information defined as requiring cryptographic protection from modification is not encrypted in a manner that provides the required level of protection, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-270576`

### Rule: Oracle Database must isolate security functions from nonsecurity functions by means of separate security domains.

**Rule ID:** `SV-270576r1065006_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Database management systems (DBMSs) typically separate security functionality from nonsecurity functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and nonsecurity functionality are commingled, users who have access to nonsecurity functionality may be able to access security functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings to determine whether objects or code implementing security functionality are located in a separate security domain, such as a separate database or schema created specifically for security functionality. If security-related database objects or code are not kept separate, this is a finding. The Oracle elements of security functionality, such as the roles, permissions, and profiles, along with password complexity requirements, are stored in separate schemas in the database. Review any site-specific applications security modules built into the database and determine what schema they are located in and take appropriate action. The Oracle objects will be in the Oracle Data Dictionary.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-270577`

### Rule: Oracle Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-270577r1065009_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including database management systems (DBMSs), must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding. If sensitive data is included in the exports and no procedures are in place to remove or modify the data to render it not sensitive prior to import into a development database or policy and procedures are not in place to ensure authorization of development personnel to access sensitive information contained in production data, this is a finding.

## Group: SRG-APP-000243-DB-000374

**Group ID:** `V-270578`

### Rule: Access to Oracle Database files must be limited to relevant processes and to authorized, administrative users.

**Rule ID:** `SV-270578r1115960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including database management systems (DBMSs), must prevent unauthorized and unintended information transfer via shared system resources. Permitting only DBMS processes and authorized, administrative users to have access to the files where the database resides helps ensure that those files are not shared inappropriately and are not open to backdoor access and manipulation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the permissions granted to users by the operating system/file system on the database files, database log files, and database backup files. On Unix Systems: ls -ld [pathname] Substitute [pathname] with the directory path where the database files, logs, and database backup files are located. (examples: /*/app/oracle/oradata/db_name, /*/app/oracle/oradata/db_name/audit, and /*/app/oracle/fast_recovery_area/db_name) If permissions are granted for world access, this is a finding. If any user/role who is not an authorized system administrator with a need to know or database administrator with a need to know, or a system account for running DBMS processes, is permitted to read/view any of these files, this is a finding. On Windows Systems (from Windows Explorer): Browse to the directory specified (example: %ORACLE_BASE%\oradata and %ORACLE_BASE%\fast_recovery_area). Select and right-click on the directory >> Properties >> Security tab. On Windows hosts, records are also written to the Windows application event log. The location of the application event log is listed under Properties for the log under the Windows console. The default location is C:\WINDOWS\system32\config\EventLogs\AppEvent.Evt. Select and right-click on the directory >> Properties >> Security tab. If permissions are granted to everyone, this is a finding. If any user/role who is not an authorized system administrator with a need to know or database administrator with a need to know, or a system account for running DBMS processes permitted to read/view any of these files, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-270579`

### Rule: Oracle Database must employ cryptographic mechanisms preventing the unauthorized disclosure of information during transmission unless the transmitted data is otherwise protected by alternative physical measures.

**Rule ID:** `SV-270579r1065015_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that applications take measures to employ some form of cryptographic mechanism to protect the information during transmission. This is usually achieved using Transport Layer Security (TLS), secure sockets layer (SSL) virtual private network (VPN), or IPsec tunnel. Alternative physical protection measures include Protected Distribution Systems (PDS). PDS are used to transmit unencrypted classified NSI through an area of lesser classification or control. Inasmuch as the classified NSI is unencrypted, the PDS must provide adequate electrical, electromagnetic, and physical safeguards to deter exploitation. Refer to NSTSSI No. 7003 for additional details on a PDS. Information in transmission is particularly vulnerable to attack. If the database management system (DBMS) does not employ cryptographic mechanisms preventing unauthorized disclosure of information during transit, the information may be compromised. SHA-1 is in the process of being removed from service within the DOD and its use is to be limited during the transition to SHA-2. Use of SHA-1 for digital signature generation is prohibited. Allowable uses during the transition include CHECKSUM usage and verification of legacy certificate signatures. SHA-1 is considered a temporary solution during legacy application transitionary periods and should not be engineered into new applications. SHA-2 is the path forward for DOD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check database management system (DBMS) settings to determine whether cryptographic mechanisms are used to prevent the unauthorized disclosure of information during transmission. Determine whether physical measures are being used instead of cryptographic mechanisms. If neither cryptographic nor physical measures are being used, this is a finding. To check that network encryption is enabled and using site-specified encryption procedures, look in SQLNET.ORA located at $ORACLE_HOME/network/admin/sqlnet.ora. If encryption is set, entries like the following will be present: SQLNET.CRYPTO_CHECKSUM_TYPES_CLIENT= (SHA384) SQLNET.CRYPTO_CHECKSUM_TYPES_SERVER= (SHA384) SQLNET.ENCRYPTION_TYPES_CLIENT= (AES256) SQLNET.ENCRYPTION_TYPES_SERVER= (AES256) SQLNET.CRYPTO_CHECKSUM_CLIENT = requested SQLNET.CRYPTO_CHECKSUM_SERVER = required The values assigned to the parameters may be different, the combination of parameters may be different, and not all of the example parameters will necessarily exist in the file.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-270580`

### Rule: Oracle Database must check the validity of data inputs.

**Rule ID:** `SV-270580r1068300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. All applications need to validate the data users attempt to input to the application for processing. Rules for checking the valid syntax and semantics of information system inputs (e.g., character set, length, numerical range, acceptable values) are in place to verify inputs match specified definitions for format and content. Inputs passed to interpreters are prescreened to prevent the content from being unintentionally interpreted as commands. This requires for inspection of application source code, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. Oracle provides built-in processes to keep data and its integrity intact by using constraints. Integrity Constraint States can specify that a constraint is enabled (ENABLE) or disabled (DISABLE). If a constraint is enabled, data is checked as it is entered or updated in the database, and data that does not conform to the constraint is prevented from being entered. If a constraint is disabled, then data that does not conform can be allowed to enter the database. Additionally, can specify that existing data in the table must conform to the constraint (VALIDATE). Conversely, if specified NOVALIDATE, are not ensured that existing data conforms. An integrity constraint defined on a table can be in one of the following states: ENABLE, VALIDATE ENABLE, NOVALIDATE DISABLE, VALIDATE DISABLE, NOVALIDATE</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review database management system (DBMS) code, settings, field definitions, constraints, and triggers to determine whether or not data being input into the database is validated. If code exists that allows invalid data to be acted upon or input into the database, this is a finding. If field definitions do not exist in the database, this is a finding. If fields do not contain enabled constraints where required, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-270581`

### Rule: The database management system (DBMS) and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-270581r1065225_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be used otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, precompiled stored procedures and functions (and triggers). This requires inspection of application source code, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS source code (stored procedures, functions, triggers) and application source code, to identify cases of dynamic code execution. If dynamic code execution is employed in circumstances where the objective could practically be satisfied by static execution with strongly typed parameters, this is a finding.

## Group: SRG-APP-000251-DB-000392

**Group ID:** `V-270582`

### Rule: The database management system (DBMS) and associated applications, when making use of dynamic code execution, must take steps against invalid values that may be used in a SQL injection attack, therefore resulting in steps to prevent a SQL injection attack.

**Rule ID:** `SV-270582r1065226_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be used otherwise. Use strongly typed data items rather than general purpose strings as input parameters to task-specific, precompiled stored procedures and functions (and triggers). When dynamic execution is necessary, ways to mitigate the risk include the following, which should be implemented both in the on-screen application and at the database level, in the stored procedures: - Allow strings as input only when necessary. - Rely on data typing to validate numbers, dates, etc. Do not accept invalid values. If substituting other values for them, think carefully about whether this could be subverted. - Limit the size of input strings to what is truly necessary. - If single quotes/apostrophes, double quotes, semicolons, equals signs, angle brackets, or square brackets will never be valid as input, reject them. - If comment markers will never be valid as input, reject them. In SQL, these are -- or /* */ - If HTML and XML tags, entities, comments, etc., will never be valid, reject them. - If wildcards are present, reject them unless truly necessary. In SQL these are the underscore and the percentage sign, and the word ESCAPE is also a clue that wildcards are in use. - If SQL key words, such as SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP, ESCAPE, UNION, GRANT, REVOKE, DENY, MODIFY will never be valid, reject them. Use case-insensitive comparisons when searching for these. Bear in mind that some of these words, particularly Grant (as a person's name), could also be valid input. - If there are range limits on the values that may be entered, enforce those limits. - Institute procedures for inspection of programs for correct use of dynamic coding, by a party other than the developer. - Conduct rigorous testing of program modules that use dynamic coding, searching for ways to subvert the intended use. - Record the inspection and testing in the system documentation. - Bear in mind that all this applies not only to screen input, but also to the values in an incoming message to a web service or to a stored procedure called by a software component that has not itself been hardened in these ways. Not only can the caller be subject to such vulnerabilities; it may itself be the attacker. This requires for inspection of application source code, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review DBMS source code (stored procedures, functions, triggers) and application source code to identify cases of dynamic code execution. If dynamic code execution is employed without protective measures against code injection, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-270583`

### Rule: Oracle Database must only generate error messages that provide information necessary for corrective actions without revealing organization-defined sensitive or potentially harmful information in error logs and administrative messages that could be exploited.

**Rule ID:** `SV-270583r1065027_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any database management system (DBMS) or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, usernames, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This requires for inspection of application source code, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the database administrator (DBA) must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. Out of the box, Oracle Database covers this. For example, if a user does not have access to a table, the error is just that the table or view does not exist. The Oracle Database is not going to display a Social Security Number in an error code unless an application is programmed to do so. Oracle applications will not expose the actual transactional data to a screen. The only way Oracle will capture this information is to enable specific logging levels. Custom code would require a review to ensure compliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and custom database and application code to verify error messages do not contain information beyond what is needed for troubleshooting the issue. If database errors contain PII data, sensitive business data, or information useful for identifying the host system, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-270584`

### Rule: Oracle Database must restrict error messages so only authorized personnel may view them.

**Rule ID:** `SV-270584r1065296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any database management system (DBMS) or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, usernames, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This requires for inspection of application source code, which will involve collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check DBMS settings and custom database code to determine if error messages are ever displayed to unauthorized individuals: i) Review all end-user-facing applications that use the database, to determine whether they display any DBMS-generated error messages to general users. If they do, this is a finding. ii) Review whether the database is accessible to users who are not authorized system administrators or database administrators, via the following types of software: iia) Oracle SQL*Plus. iib) Reporting and analysis tools. iic) Database management and/or development tools, such as, but not limited to, Toad. iid) Application development tools, such as, but not limited to, Oracle JDeveloper, Microsoft Visual Studio, PowerBuilder, or Eclipse. If the answer to the preceding question (iia through iid) is Yes, inquire whether, for each role or individual with respect to each tool, this access is required to enable the user(s) to perform authorized job duties. If No, this is a finding. If Yes, continue: For each tool in use, determine whether it is capable of suppressing DBMS-generated error messages, and if it is, whether it is configured to do so. Determine whether the role or individual, with respect to each tool, needs to verify detailed DBMS-generated error messages. If No, and if the tool is not configured to suppress such messages, this is a finding. If Yes, determine whether the role/user's need to verify such messages is documented in the system documentation. If so, this is not a finding. If not, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-270585`

### Rule: Oracle Database software must be evaluated and patched against newly found vulnerabilities.

**Rule ID:** `SV-270585r1065298_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When the Quarterly CPU is released, check the CPU Notice and note the specific patch number for the system. Then, issue the following command: SELECT patch_id, source_version, action, status, description from dba_registry_sqlpatch; This will generate the patch levels for the home and any specific patches that have been applied to it. If the currently installed patch levels are lower than the latest, this is a finding.

## Group: SRG-APP-000845-DB-000220

**Group ID:** `V-270587`

### Rule: Oracle Database must, for password-based authentication, verify that when users create or update passwords, the passwords are not found on the list of commonly used, expected, or compromised passwords in IA-5 (1) (a).

**Rule ID:** `SV-270587r1112489_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password-based authentication applies to passwords regardless of whether they are used in single-factor or multifactor authentication (MFA). Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the database management system (DBMS) is configured to verify when users create or update passwords, that the passwords are not found on the list of commonly used, expected, or compromised passwords in IA-5 (1) (a). If all user accounts are authenticated by the OS or an enterprise-level authentication/access mechanism, and not by Oracle, this is not a finding. For each profile that can be applied to accounts where authentication is under Oracle's control, determine the password verification function that is in use: SELECT * FROM SYS.DBA_PROFILES WHERE RESOURCE_NAME = 'PASSWORD_VERIFY_FUNCTION' ORDER BY PROFILE; Note: Profiles can inherit settings from another profile so some password functions could be set to DEFAULT. If so, review the DEFAULT profile function name. If the function name is null for any profile, this is a finding. Review the password verification functions specified for the PASSWORD_VERIFY_FUNCTION settings for each profile. Determine whether it is configured for when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords. If the verify_function is not configured to verify when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5 (1) (a), this is a finding.

## Group: SRG-APP-000855-DB-000240

**Group ID:** `V-270588`

### Rule: Oracle Database must, for password-based authentication, require immediate selection of a new password upon account recovery.

**Rule ID:** `SV-270588r1065042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password-based authentication applies to passwords regardless of whether they are used in single-factor or multifactor authentication (MFA). Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the database management system (DBMS) is configured to require immediate selection of a new password upon account recovery. All scripts, functions, triggers, and stored procedures that are used to create a user or reset a user's password should include a line similar to the following: alter user <username> password expire; If they do not, this is a finding. If the DBMS is not configured to require immediate selection of a new password upon account recovery, this is a finding.

## Group: SRG-APP-000910-DB-000300

**Group ID:** `V-270589`

### Rule: Oracle Database must include only approved trust anchors in trust stores or certificate stores managed by the organization.

**Rule ID:** `SV-270589r1065045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Public key infrastructure (PKI) certificates are certificates with visibility external to organizational systems and certificates related to the internal operations of systems, such as application-specific time services. In cryptographic systems with a hierarchical structure, a trust anchor is an authoritative source (i.e., a certificate authority) for which trust is assumed and not derived. A root certificate for a PKI system is an example of a trust anchor. A trust store or certificate store maintains a list of trusted root certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all accounts are authenticated by the OS or an enterprise-level authentication/access mechanism and not by Oracle, this is not a finding. Verify the database management system (DBMS) is configured to include only approved trust anchors in trust stores or certificate stores managed by the organization. If trust stores or certification paths are not being validated back to a trust anchor, this is a finding. The database supports PKI-based authentication by using digital certificates over Transport Layer Security (TLS) in addition to the native encryption and data integrity capabilities of these protocols. Oracle provides a complete PKI that is based on RSA Security, Inc., Public-Key Cryptography Standards, and which interoperates with Oracle servers and clients. The database uses a wallet that is a container that is used to store authentication and signing credentials, including private keys, certificates, and trusted certificates needed by TLS. In an Oracle environment, every entity that communicates over TLS must have a wallet containing an X.509 version 3 certificate, private key, and list of trusted certificates. If the $ORACLE_HOME/network/admin/sqlnet.ora contains the following entries, TLS is installed. WALLET_LOCATION = (SOURCE= (METHOD = FILE) (METHOD_DATA = DIRECTORY=/wallet) SSL_CIPHER_SUITES=(SSL_cipher_suiteExample) SSL_VERSION = 3.0 SSL_CLIENT_AUTHENTICATION=TRUE

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-275999`

### Rule: A minimum of three Oracle Control Files must be created and each stored on a separate physical and logical device.

**Rule ID:** `SV-275999r1115962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Oracle control files store information critical to Oracle database integrity. Oracle uses these files to maintain time synchronization of database files and verify the validity of system data and log files at system startup. Loss of access to the control files can affect database availability, integrity, and recovery. Oracle Pluggable Databases (PDBs) do not contain their own control files; instead, all PDBs within a Container Database (CDB) share control files managed by the CDB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the SQL statement below to obtain information on each currently existing Control File: SELECT name FROM sys.v$controlfile ORDER BY 1; Oracle Best Practice: Oracle recommends a minimum of three Oracle Control Files and each stored on a separate physical and logical device (RAID 1 + 0). DOD guidance recommends: Each control file must be located on a separate physical and logical (virtual) storage device. Consult with the storage administrator, system administrator, or database administrator to determine whether the mount points or partitions referenced in the file paths indicate separate physical disks or directories on RAID devices. Note: Distinct does not equal dedicated. May share directory space with other Oracle database instances if present. If the minimum of three control files is not met, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-276000`

### Rule: A minimum of three Oracle redo log groups/files must be defined and configured to be stored on separate, archived physical disks or archived directories on a RAID device. In addition, each Oracle redo log group must have a minimum of two Oracle redo log members (files).

**Rule ID:** `SV-276000r1112495_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Oracle Database Redo Log files store detailed transactional information on changes made to the database using SQL Data Manipulation Language (DML), Data Definition Language (DDL), and Data Control Language (DCL), which is required for undo, backup, restoration, and recovery. A minimum of three Oracle redo log groups/files must be defined and configured to be stored on separate, archived physical disks or archived directories on a RAID (mirrored) device. In addition, each Oracle redo log group must have a minimum to two Oracle redo log members (files). Each side of the Redo Log Mirror (group 1, member 1) is identical to its mirror image (group 1, member 2), making it possible to continue operations if one file or even one complete mirror is lost due to corruption or accidental deletion. Writing each mirror to a physically and logically separate storage device is an important part of minimizing single points of failure. Oracle redo logs, which are crucial for database recovery, are managed at the CDB level, not at the PDB level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From SQL*Plus: -- Check to see how many Oracle redo log groups there are: select group#, bytes, members, status, archived from v$log; -- Check to see how many Oracle redo log members there are: select * from v$logfile; This is a finding if there are less than three Oracle redo log groups a RAID storage device, or equivalent storage system, is not being used. If one or more groups (group#) has only a single member this is a finding. If one or more groups (group#) have more than a single member but one or more of those members are located on the same physical or logical device this is a finding. select count(*) from V$LOG; If the value of the count returned is less than 3, this is a finding. From SQL*Plus: select count(*) from V$LOG where members > 1; If the value of the count returned is less than 3 and a RAID storage device is not being used, this is a finding.

