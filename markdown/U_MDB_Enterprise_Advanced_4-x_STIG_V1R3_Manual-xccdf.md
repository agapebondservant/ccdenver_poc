# STIG Benchmark: MongoDB Enterprise Advanced 4.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-252134`

### Rule: MongoDB must provide audit record generation for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-252134r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MongoDB must provide audit record generation capability for DoD-defined auditable events within all DBMS/database components. Satisfies: SRG-APP-000089-DB-000064, SRG-APP-000080-DB-000063, SRG-APP-000090-DB-000065, SRG-APP-000091-DB-000066, SRG-APP-000091-DB-000325, SRG-APP-000092-DB-000208, SRG-APP-000095-DB-000039, SRG-APP-000096-DB-000040, SRG-APP-000097-DB-000041, SRG-APP-000098-DB-000042, SRG-APP-000099-DB-000043, SRG-APP-000100-DB-000201, SRG-APP-000101-DB-000044, SRG-APP-000109-DB-000049, SRG-APP-000356-DB-000315, SRG-APP-000360-DB-000320, SRG-APP-000381-DB-000361, SRG-APP-000492-DB-000332, SRG-APP-000492-DB-000333, SRG-APP-000494-DB-000344, SRG-APP-000494-DB-000345, SRG-APP-000495-DB-000326, SRG-APP-000495-DB-000327, SRG-APP-000495-DB-000328, SRG-APP-000495-DB-000329, SRG-APP-000496-DB-000334, SRG-APP-000496-DB-000335, SRG-APP-000498-DB-000346, SRG-APP-000498-DB-000347, SRG-APP-000499-DB-000330, SRG-APP-000499-DB-000331, SRG-APP-000501-DB-000336, SRG-APP-000501-DB-000337, SRG-APP-000502-DB-000348, SRG-APP-000502-DB-000349, SRG-APP-000503-DB-000350, SRG-APP-000503-DB-000351, SRG-APP-000504-DB-000354, SRG-APP-000504-DB-000355, SRG-APP-000505-DB-000352, SRG-APP-000506-DB-000353, SRG-APP-000507-DB-000356, SRG-APP-000507-DB-000357, SRG-APP-000508-DB-000358, SRG-APP-000515-DB-000318</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: /etc/mongod.conf) for appropriate audit configuration keys. Examples shown below: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson -OR- auditLog: destination: syslog If an auditLog key is not present, this is a finding. If the MongoDB configuration file does not contain a setParameter option with auditAuthorizationSuccess: true, this is a finding. Example: setParameter: auditAuthorizationSuccess: true If the auditLog key is present and contains a filter subkey without an associated filter, this is a finding. The site auditing policy must be reviewed to determine if the filter being applied meets the site auditing requirements. If not, then the filter being applied will need to be modified to comply. Example filter shown below only audits createCollection and dropCollection: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson filter: '{ atype: { $in: [ "createCollection", "dropCollection" ] } }'

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-252135`

### Rule: The audit information produced by MongoDB must be protected from unauthorized access.

**Rule ID:** `SV-252135r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000119-DB-000060, SRG-APP-000120-DB-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB must not permit access to its audit logs by unprivileged users. The official installation packages restrict which operating system users and groups may read or modify files. The audit log destination is not configured or created at installation time and must be manually done with appropriate ownership and permissions applied with the MongoDB user and MongoDB group. Check the MongoDB configuration file (default location: /etc/mongod.conf) for a key named auditLog with destination set to file. Example shown below: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson -OR- auditLog: destination: syslog If auditLog does not exist, this is a finding. If the auditLog.destination is file in the MongoDB configuration file (default location /etc/mongod.conf), then the following will check ownership and permissions of the MongoDB auditLog directory: Verify User ownership, Group ownership, and permissions on the MongoDB auditLog directory: stat MongoDB auditLog directory If the User owner is not mongod, this is a finding. If the Group owner is not mongod, this is a finding. If the directory is more permissive than 700, this is a finding. To find the auditLog directory name, view and search for the entry in the MongoDB configuration file (default location /etc/mongod.conf) for auditLog.destination. If this parameters value is file then use the directory portion of the auditLog.path setting as the MongoDB auditLog directory location. Example: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson Given the example above, to find the auditLog directory ownership and permissions, run the following command: stat /var/log/mongodb/audit The output will look similar to the following output: File: '/var/log/mongodb/audit' Size: 48 Blocks: 0 IO Block: 4096 directory Device: 808h/2056d Inode: 245178 Links: 2 Access: (0700/drwx------) Uid: ( 997/ mongod) Gid: ( 996/ mongod) Context: unconfined_u:object_r:mongod_log_t:s0 Access: 2020-03-16 12:51:16.816000000 -0400 Modify: 2020-03-16 12:50:48.722000000 -0400 Change: 2020-03-16 12:50:48.722000000 -0400 Birth: -

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-252136`

### Rule: MongoDB must protect its audit features from unauthorized access.

**Rule ID:** `SV-252136r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, they could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity. Satisfies: SRG-APP-000121-DB-000202, SRG-APP-000122-DB-000203, SRG-APP-000123-DB-000204</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure audit configurations are protected from unauthorized modification, the default installation of MongoDB restricts permission on the configuration file. Verify User ownership, Group ownership, and permissions on the MongoDB configuration file: (default name and location is /etc/mongod.conf) (The name and location for the MongoDB configuration file will vary according to local circumstances.) Using the default name and location the command would be: stat /etc/mongod.conf If the User owner is not mongod, this is a finding. If the Group owner is not mongod, this is a finding. If the filename is more permissive than 660, this is a finding. Note that the audit destination cannot be modified at runtime.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-252137`

### Rule: Unused database components that are integrated in MongoDB and cannot be uninstalled must be disabled.

**Rule ID:** `SV-252137r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for MongoDB by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS, and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/role permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review for the following option: net: http: enabled: true JSONPEnabled: true RESTInterfaceEnabled: true If the configuration file contains any combination of http settings under the net: option, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-252138`

### Rule: Unused database components that are integrated in MongoDB and cannot be uninstalled must be disabled.

**Rule ID:** `SV-252138r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for MongoDB by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS, and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/role permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the MongoDB database configuration file (default location: /etc/mongod.conf) for any net.http options similar in construct to the following: net: http: option 1: value option 2: value Example: It may appear similar to the following (having one or more options): net: http: enabled: true port: port number JSONPEnabled: true RESTInterfaceEnabled: true If the configuration file contains any "http:" options under "net:", this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-252139`

### Rule: If passwords are used for authentication, MongoDB must transmit only encrypted representations of passwords.

**Rule ID:** `SV-252139r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database. Satisfies: SRG-APP-000172-DB-000075, SRG-APP-000175-DB-000067</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), verify the following parameters in the net.tls: (network TLS) section of the file: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/caToValidateClientCertificates.pem allowInvalidCertificates: false allowConnectionsWithoutCertificates: false If the net.tls: parameter is not present, this is a finding. If the net.tls.certificateKeyFile parameter is not present, this is a finding. If the net.tls.CAFile parameter is not present, this is a finding. If the net.tls.allowInvalidCertificates parameter is found and set to true, this is a finding. If the net.tls.allowConnectionsWithoutCertificates parameter is found and set to true, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-252140`

### Rule: MongoDB must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-252140r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB grants access to data and commands through role-based authorization and provides built-in roles that provide the different levels of access commonly needed in a database system. Additionally, user-defined roles can be created. Check a user's role to ensure correct privileges for the function: Run the following command to get a list of all the databases in the system: show dbs For each database in the system, identify the user's roles for the database: use database db.getUsers() The server will return a document with the all users in the data and their associated roles. View a roles' privileges: For each database, identify the privileges granted by a role: use database db.getRole( %rolename%, { showPrivileges: true } ) The server will return a document with the privileges and inheritedPrivileges arrays. The privileges returned document lists the privileges directly specified by the role and excludes those privileges inherited from other roles. The inheritedPrivileges returned document lists all privileges granted by this role, both directly specified and inherited. If the role does not inherit from other roles, the two fields are the same. If a user has a role with inappropriate privileges, this is a finding.

## Group: SRG-APP-000225-DB-000153

**Group ID:** `V-252141`

### Rule: MongoDB must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-252141r879640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Failure to a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Systems that fail suddenly and with no incorporated failure state planning may leave the hosting system available but with a reduced security protection capability. Preserving information system state data also facilitates system restart and return to the operational mode of the organization with less disruption of mission/business processes. Databases must fail to a known consistent state. Transactions must be successfully completed or rolled back. In general, security mechanisms should be designed so that a failure will follow the same execution path as disallowing the operation. For example, application security methods, such as isAuthorized(), isAuthenticated(), and validate(), should all return false if there is an exception during processing. If security controls can throw exceptions, they must be very clear about exactly what that condition means. Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations. Satisfies: SRG-APP-000225-DB-000153, SRG-APP-000226-DB-000147</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Journaling is enabled by default. With journaling enabled, if mongod stops unexpectedly, the program can recover everything written to the journal. MongoDB will re-apply the write operations on restart and maintain a consistent state. To validate the mongod configuration, run the following command: db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.storage.journal If it returns { enabled : false } or no output, this is a finding.

## Group: SRG-APP-000243-DB-000373

**Group ID:** `V-252142`

### Rule: MongoDB must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-252142r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse. Satisfies: SRG-APP-000243-DB-000373, SRG-APP-000243-DB-000374</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, the MongoDB official installation packages restrict user and group ownership and read/write permissions on the underlying data files and critical configuration files from other operating system users. In addition, process and memory isolation is used by default. System administrators should also consider if whole database encryption would be an effective control on an application basis. Run the following commands to verify proper permissions for the following database files or directories: stat /etc/mongod.conf If the owner and group are not both mongod, this is a finding. If the file permissions are more permissive than 600, this is a finding. stat /var/lib/mongo If the owner and group are not both mongod, this is a finding. If the file permissions are more permissive than 755, this is a finding. ls -l /var/lib/mongo If the owner and group of any file or sub-directory is not mongod, this is a finding. If the permission of any file in the main directory (/var/lib/mongo) or sub-directory of (/var/lib/mongo) is more permissive than 600, this is a finding. If the permission of any sub-directory of (/var/lib/mongo) is more permissive than 700, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-252143`

### Rule: MongoDB and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-252143r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered. Satisfies: SRG-APP-000251-DB-000391, SRG-APP-000251-DB-000392</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. If the following parameter is not present or not set as show below in the MongoDB configuration file (default location: /etc/mongod.conf), this is a finding. security: javascriptEnabled: false

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-252144`

### Rule: MongoDB must associate organization-defined types of security labels having organization-defined security label values with information in storage and transmission.

**Rule ID:** `SV-252144r879689_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for MongoDB to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling, or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of MongoDB product, a third-party product, or custom application code. Satisfies: SRG-APP-000311-DB-000308, SRG-APP-000313-DB-000309, SRG-APP-000314-DB-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling is required, then there must be organizational or site-specific documentation on what the security labeling policy is and guidance on how and where to apply it. Review the organizational or site-specific security labeling documentation to understand how documents in specific MongoDB collection(s) must be marked. This marking process should be applied as data is entered into the database. Upon review of the security labeling documents, the following checks will be required. 1. Check if the role SLTagViewer exists. If this role does not exist this is a finding. Note: The role name SLTagViewer is a user-defined (custom) role and is organizational or site-specific. The role name of SLTagViewer is used here as an example. Run the following commands: use admin db.getRole( "SLTagViewer", { showPrivileges: true } ) If the results returned from this command is null, this is a finding. 2. Check that data is appropriately marked in the specific MongoDB collection(s) that require security labeling. This check will be specific to the security labeling policy and guidance. Log in to MongoDB with a user that has a Security Label Tag Viewer role (SLTagViewer, which is a role that has been created and has access to read/view those database/collections that require security labels) and review the data in the MongoDB collections that require security labels to ensure that the data is appropriately marked according to the security labeling documentation. For example, if documents in a MongoDB collection need to be marked as TS, S, C or U (or combination of) at the root level of the document and at each field level of the document then the security labeling policy and guidance would indicate a document might look like the following and this would be not be a finding (sl is the security label): { "_id": 1, "sl": [["TS", ["S"]], "field1" : { "sl" : [ ["S"] ], "data" : "field1 value" }, "field2" : { "sl" : [ ["TS"] ], "data" : "field2 value" }, "field3" : { "sl" : [ ["S"] ], "data" : "field3 value" } } The following document would be a finding because at the field level, field2 is missing its security label of sl: { "_id": 1, "sl": [["TS"], ["S"]], "field1" : { "sl" : [ ["S"] ], "data" : "field1 value" }, "field2" : { "data" : "field2 value" }, "field3" : { "sl" : [ ["S"] ], "data" : "field3 value" } } 3. Check that queries against that data in those collections use an appropriately constructed MongoDB $redact operation as part of the query pipeline to ensure that only the data appropriate for the query (that meets the security label requirements) is returned. Ensure that any query that targets the databases/collections that have security labeling have the appropriate MongoDB $redact operation applied. This is done through trusted middleware. This trusted middleware configuration is purpose built (custom) code and integrations and is organizational or site-specific. Information on the basics of how this is can be constructed can be found here: https://docs.mongodb.com/v4.4/reference/operator/aggregation/redact/ Any queries that target a MongoDB database/collection that has security labels and that pass through the trusted middleware and does not have an appropriately constructed $redact operator which is part of the query aggregation pipeline are a finding. The following is an example of the $redact operator for the example document: db.security_collection.aggregate( [{ $redact: { $cond: [{ $anyElementTrue: { $map: { input: "$sl", as: "setNeeded", in: { $setIsSubset: ["$$setNeeded", ["S"]] } } } }, "$$DESCEND", "$$PRUNE"] } } ] )

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-252145`

### Rule: MongoDB must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-252145r879705_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bound by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. Satisfies: SRG-APP-000328-DB-000301, SRG-APP-000340-DB-000304</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MongoDB Configuration file (default location: /etc/mongod.conf). If the file does not contain the following entry, this is a finding. security: authorization: enabled

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-252146`

### Rule: MongoDB must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-252146r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of MongoDB. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While Federal Agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/ Satisfies: SRG-APP-000179-DB-000114, SRG-APP-000416-DB-000380, SRG-APP-000514-DB-000381, SRG-APP-000514-DB-000382, SRG-APP-000514- DB-000383</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command from the MongoDB shell: db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.net.tls.FIPSMode If the MongoDB server is running with FIPS mode, this command will return true. Any other output is a finding. Verify that FIPS has been enabled at the OS level. Refer to the appropriate OS STIG documentation.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-252147`

### Rule: MongoDB must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-252147r879799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to MongoDB or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides. Satisfies: SRG-APP-000428-DB-000386, SRG-APP-000429-DB-000387</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine whether the organization has defined the information at rest that is to be protected from modification, which must include, at a minimum, PII and classified information. If no information is identified as requiring such protection, this is not a finding. If any data is PII, classified or is deemed by the organization the need to be encrypted at rest, verify the MongoDB configuration file (default location: /etc/mongod.conf) contain the following options: security: enableEncryption: true kmip: serverName: %KMIP Server HostName% port: %KMIP server port% ServerCAFile: %CA PEM file% clientCertificateFile: %client PEM file% If these above options are not part of the MongoDB configuration file, this is a finding. Items in the above are specific to the KMIP appliance and need to be set according to the KMIP appliance configuration.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-252148`

### Rule: MongoDB must limit the total number of concurrent connections to the database.

**Rule ID:** `SV-252148r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MongoDB must limit the total number of concurrent connections to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Mongo can limit the total number of connections. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: net: maxIncomingConnections: %int% If this parameter is not present, or the OS is not utilized to limit connections, this is a finding.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-252149`

### Rule: MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-252149r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: enabled If this parameter is not present, this is a finding. If using organization-mandated authorization, verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following to ensure LDAP auth is enabled as well: security: ldap: servers: [list of ldap servers] If this parameter is not present, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-252150`

### Rule: MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-252150r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The MongoDB administrator must ensure that additional application access control is enforced. Review the system documentation to determine the required levels of protection for MongoDB server securables by type of login. Review the permissions actually in place on the server. If the actual permissions do not match the documented requirements, this is a finding. Run MongoDB command to view roles and privileges in a particular database: use database db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true } )

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-252151`

### Rule: MongoDB must limit privileges to change software modules, to include stored procedures, functions and triggers, and links to software external to MongoDB.

**Rule ID:** `SV-252151r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify monitoring of changes to database software libraries, related applications, and configuration files occurs. Verify the list of files, directories, and database application objects (procedures, functions, and triggers) being monitored is complete. If monitoring does not occur or is not complete, this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-252152`

### Rule: MongoDB software installation account must be restricted to authorized users.

**Rule ID:** `SV-252152r879586_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling, granting access to, and tracking use of the DBMS software installation account. If access or use of this account is not restricted to the minimum number of personnel required or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-252153`

### Rule: Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-252153r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default MongoDB, runs using mongod user account (both user and group) and uses the following default directories: MongoDB created directories (default): /var/lib/mongo (the data directory) /var/lib/mongo/diagnostic.data /var/lib/mongo/_tmp /var/lib/mongo/journal /var/log/mongodb (the mongod process log directory) /var/log/mongodb/audit (the auditLog directory) Standard directories: /bin (the executable directory) /etc (the configuration file directory) Check if any non-MongoDB application, non-MongoDB data, or non-MongoDB directories exists under any of the MongoDB created directories or sub-directories. If any non-MongoDB application, non-MongoDB data, or non-MongoDB directories exists under the MongoDB-created directories, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-252154`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be owned by database/DBMS principals authorized for ownership.

**Rule ID:** `SV-252154r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who utilizes the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to get the roles from a MongoDB database. For each database in MongoDB: use database db.getUsers() If the output shows a role of "dbOwner", this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-252155`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be restricted to authorized users.

**Rule ID:** `SV-252155r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to get the roles from a MongoDB database. For each database in MongoDB: use database db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true } ) Run the following command to the roles assigned to users: use admin db.system.users.find() Analyze the output and if any roles or users have unauthorized access, this is a finding. This will vary on an application basis.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-252156`

### Rule: Unused database components that are integrated in MongoDB and cannot be uninstalled must be disabled.

**Rule ID:** `SV-252156r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for MongoDB by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS, and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/role permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: http: enabled: true JSONPEnabled: true RESTInterfaceEnabled: true If any of the booleans are true or enabled, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-252157`

### Rule: MongoDB must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-252157r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each database in the system, run the following command: use database db.getUsers() Ensure each user identified is a member of an appropriate organization that can access the database. Alternatively, if LDAP/AD is being used for authentication/authorization, the mongoldap tool can be used to verify user account access. If a user is found not be a member of an appropriate organization that can access the database, this is a finding. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: enabled If this parameter is not present, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-252158`

### Rule: If passwords are used for authentication, MongoDB must implement LDAP or Kerberos for authentication to enforce the DoD standards for password complexity and lifetime.

**Rule ID:** `SV-252158r879601_rule`
**Severity:** high

**Description:**
<VulnDiscussion>OS/enterprise authentication and identification must be used (SRG-APP-000023-DB-000001). Native DBMS authentication may be used only when circumstances make it unavoidable, and must be documented and AO-approved. The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DoD standards for password complexity and lifetime must be implemented. DBMS products that can inherit the rules for these from the operating system or access control program (e.g., Microsoft Active Directory) must be configured to do so. For other DBMSs, the rules must be enforced using available configuration parameters or custom code. For MongoDB, password complexity and lifetime requirements must be enforced by an external authentication source such as LDAP, Active Directory, or Kerberos.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is using Native LDAP authentication where the LDAP server is configured to enforce password complexity and lifetime, this is not a finding. If MongoDB is using Kerberos authentication where Kerberos is configured to enforce password complexity and lifetime, this is not a finding. If MongoDB is not configured for SCRAM-SHA1, MONGODB-CR, or LDAP authentication, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-252159`

### Rule: If passwords are used for authentication, MongoDB must store only hashed, salted representations of passwords.

**Rule ID:** `SV-252159r879608_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to MongoDB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB supports several authentication mechanisms, some of which store credentials on the MongoDB server. If these mechanisms are in use, MongoDBs authSchemaVersion in the admin.system.version collection must be set to 5. 1. Validate that authenticationMechansisms is defined in config file (default location /etc/mongod.conf). The MongoDB Configuration file should contain the similar to the following entry: setParameter: authenticationMechanisms: SCRAM-SHA-256 If the config file does not contain an authenticationMechanisms entry, this is a finding. 2. Validate authSchemaVersion is set to 5. Using the shell, run the following command: db.getSiblingDB("admin").system.version.find({ "_id" : "authSchema"}, {_id: 0}) It should return: { "currentVersion" : 5 } If currentVersion is less than 5, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-252160`

### Rule: MongoDB must enforce authorized access to all PKI private keys stored/utilized by MongoDB.

**Rule ID:** `SV-252160r879613_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where MongoDB-stored private keys are used to authenticate MongoDB to the system's clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man in the middle attacks against MongoDB system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 or 140-3 validated cryptographic modules. All access to the private key(s) of MongoDB must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of MongoDB's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/caToValidateClientCertificates.pem Verify ownership, group ownership, and permissions for the MongoDB config file (default: /etc/mongod.conf), the PEMKeyFile (default /etc/ssl/mongodb.pem), and the CAFile (default /etc/ssl/caToValidateClientCertificates.pem). For each file, run following command and review its output: ls -al filepath example output: -rw------- 1 mongod mongod 566 Apr 26 20:20 filepath If the user owner is not mongod, this is a finding. If the group owner is not mongod, this is a finding. If the file is more permissive than 600, this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-252161`

### Rule: MongoDB must map the PKI-authenticated identity to an associated user account.

**Rule ID:** `SV-252161r879614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to a DBMS user account for the authenticated identity to be meaningful to MongoDB and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using LDAP for authentication, this is not applicable. Each unique x.509 client certificate corresponds to a single MongoDB user; meaning it cannot use a single-client certificate to authenticate more than one MongoDB user. Log in to MongoDB and run the following command: db.runCommand( {connectionStatus: 1} ); Example output being: db.runCommand({connectionStatus:1}).authInfo { "authenticatedUsers" : [ { "user" : "CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry", "db" : "mydb1" } ], "authenticatedUserRoles" : [ { "role" : dbOwner, "db" : "mydb1" } ] } If the authenticated MongoDB user displayed does not have a user value equal to the x.509 certs Subject Name, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-252162`

### Rule: MongoDB must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-252162r879615_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Normally, with PKI authentication, the interaction with the user for authentication will be handled by a software component separate from MongoDB, such as ActivIdentity ActivClient. However, in cases where MongoDB controls the interaction, this requirement applies. To prevent the compromise of authentication information such as passwords and PINs during the authentication process, the feedback from the system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided authentication secrets when typed into the system is a method used in addressing this risk. Displaying asterisks when a user types in a password or a smart card PIN is an example of obscuring feedback of authentication secrets. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Restrict the environment to tools which meet this requirement. For the MongoDB command-line tools mongo shell, mongodump, mongorestore, mongoimport, mongoexport, which cannot be configured not to obfuscate a plain-text password, and any other essential tool with the same limitation; verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations and that AO approval has been obtained. If it is not documented, this is a finding. Request evidence that all users of MongoDB command-line tools are trained in the use of the -p option/plain-text password option and how to keep the password protected from unauthorized viewing/capture, and that they adhere to this practice. If evidence of training does not exist, this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-252163`

### Rule: MongoDB must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-252163r879617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB grants access to data and commands through role-based authorization and provides built-in roles that provide the different levels of access commonly needed in a database system. Additionally, one may create user-defined roles. Check a user's role to ensure correct privileges for the function: Prereq: To view a user's roles, you must have the viewUser privilege. Connect to MongoDB. For each database in the system, identify the user's roles for the database: use database db.getUser(%username%) The server will return a document with the user's roles. View a roles' privileges: Prereq: To view a user's roles, you must have the viewUser privilege. For each database, identify the privileges granted by a role: use database db.getRole( "read", { showPrivileges: true } ) The server will return a document with the privileges and inheritedPrivileges arrays. The privileges returned document lists the privileges directly specified by the role and excludes those privileges inherited from other roles. The inheritedPrivileges returned document lists all privileges granted by this role, both directly specified and inherited. If the role does not inherit from other roles, the two fields are the same. If a user has a role with inappropriate privileges, this is a finding.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-252164`

### Rule: MongoDB must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-252164r879639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One class of man-in-the-middle, or session hijacking, attack involves the adversary guessing at valid session identifiers based on patterns in identifiers already known. The preferred technique for thwarting guesses at Session IDs is the generation of unique session identifiers using a FIPS 140-2 or 140-3 approved random number generator. However, it is recognized that available DBMS products do not all implement the preferred technique yet may have other protections against session hijacking. Therefore, other techniques are acceptable, provided they are demonstrated to be effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: /etc/mongod.conf). The following option must be present (net.tls.mode) and set to requireTLS: net: tls: mode: requireTLS If this is not found in the MongoDB configuration file, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-252165`

### Rule: MongoDB must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-252165r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To provide integrity and confidentiality for data at rest, MongoDB must be configured to use the Encrypted Storage Engine. Run the following command to verify whether or not the Encrypted Storage Engine is enabled: db.serverStatus().encryptionAtRest.encryptionEnabled Any output other than true is a finding. Next, validate whether the Encrypted Storage Engine is running with an AEAD block cipher, which provides integrity, by running the following command: db.serverStatus().encryptionAtRest.encryptionCipherMode Any response other than AES256-GCM is a finding. Finally, validate that the system is configured to use KMIP to obtain a master encryption key, rather than storing the master key on the local filesystem. Run: db.serverStatus().encryptionAtRest.encryptionKeyId If the response is local or no response, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-252166`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-252166r879649_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-252167`

### Rule: MongoDB must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-252167r879652_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a client program assembles a query in MongoDB, it builds a BSON object, not a string. Thus, traditional SQL injection attacks are not a problem. However, MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. To check, run the following command from the MongoDB shell: db.col.find({ $where: "return true;"} ) If the response does not return an error, this is a finding. If JavaScript has been correctly disabled, the correct error would indicate that the JavaScript global engine has been disabled, e.g.: Error: error: { "ok" : 0, "errmsg" : "no globalScriptEngine in $where parsing", "code" : 2, "codeName" : "BadValue" }

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-252168`

### Rule: MongoDB must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-252168r879655_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom application code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If custom application error messages contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding. For example, when attempting to login using the MongoDB shell with incorrect client credentials, the user will receive a generic error message that the authentication failed regardless of whether the user exists or not. If a user is attempting to perform an operation using the MongoDB shell for which they do not have privileges, MongoDB will return a generic error message that the operation is not authorized. To identify the level of information being displayed in the MongoDB logfiles, run the following command: db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.security.redactClientLogData If the command does not return true, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-252169`

### Rule: MongoDB must reveal detailed error messages only to the ISSO, ISSM, SA, and DBA.

**Rule ID:** `SV-252169r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among other things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA, and DBA. Other individuals or roles may be specified according to organization-specific needs, with appropriate approval. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A mongod or mongos running with security.redactClientLogData:true redacts any message accompanying a given log event before logging. This prevents the mongod or mongos from writing potentially sensitive data stored on the database to the diagnostic log. Metadata such as error or operation codes, line numbers, and source file names are still visible in the logs. To identify the level of information being displayed in the MongoDB logfiles run the following command: db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.security.redactClientLogData If the command does not return true this is a finding. The MongoDB command getLog is an administrative command that will return the most recent 1024 logged mongod events. Ensure that application users are not authorized to execute this command. To validate this run the following command on the name of the application user to see actions its permitted to perform on the cluster resource: db.runCommand({usersInfo: %username%, showPrivileges: 1}).users[0].inheritedPrivileges.filter(privilege = privilege.resource.cluster) If getLog appears in the list of actions, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-252170`

### Rule: MongoDB must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-252170r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If the system owner, data owner, or organization requires additional assurance, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-252171`

### Rule: MongoDB must utilize centralized management of the content captured in audit records generated by all components of MongoDB.

**Rule ID:** `SV-252171r879729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. MongoDB may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Administrators can implement collection-level access control through user-defined roles. By creating a role with privileges that are scoped to a specific collection in a particular database, administrators can provision users with roles that grant privileges on a collection level. For example, a user defined role can contain the following privileges: Once enabled, the auditing system can record the following operations: schema changes (DDL), replica set and sharded cluster, authentication and authorization, and CRUD operations (requires auditAuthorizationSuccess set to true). For details on audited actions, see MongoDB documentation on the complete configuration of Audit Event Actions, Details, and Results, and Configuring Audit Filters. To ensure auditing is enabled, confirm the auditLog section in the /etc/mongod.conf configuration file exists and has been set. For example, to enable syslog centralized logging of audit events, in the MongoDB configuration file (by default: /etc/mongod.conf) verify the destination type is set as: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson -OR- auditLog: destination: syslog If this is not present, is empty, or commented, this is a finding. Review the system documentation for a description of how audit records are off-loaded and how local audit log space is managed. If the DBMS audit records are not written directly to or systematically transferred to a centralized log management system, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-252172`

### Rule: MongoDB must allocate audit record storage capacity in accordance with site audit record storage requirements.

**Rule ID:** `SV-252172r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, MongoDB must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of MongoDB and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on MongoDB's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB relies on the underlying operating system to allocate storage capacity for audit logs and as such, does not enforce arbitrary file size limits on audit logs. System administrators should confirm that the recommended centralized system logging has been enabled (e.g., syslog on Linux systems) in the /etc/mongod.conf configuration file. For example, on a Linux-based system using syslog which is mirrored to an off-server centralized location, confirm that the MongoDB configuration file (default location: /etc/mongod.conf) contains a properly configured auditLog such as follows: auditLog: destination: syslog If the auditLog entry is missing, or the destination does not reflect the intended application location, this is a finding. Investigate whether there have been any incidents where MongoDB ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been incidents where MongoDB ran out of audit log space, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-252173`

### Rule: MongoDB must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-252173r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system; so, under normal conditions, the audit space allocated to MongoDB on its own server will not be an issue. However, space will still be required on MongoDB server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that auditing is enabled in the mongodb configuration file (default location: /etc/mongod.conf) and view the auditlog.path to identify the storage volume. This is only applicable where the auditLog.destination is set to file. Verify that MongoDB Ops Manager or other organization approved monitoring software is installed. Verify that the required alert in the monitoring software to send an alert where storage volume holding the auditLog file utilization reaches 75 percent. If appropriate support staff are not notified immediately upon storage volume utilization reaching 75 percent, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-252174`

### Rule: MongoDB must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-252174r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. MongoDB must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB supports only software development, experimentation and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. MongoDB only supports views and Change Streams (similar to triggers). Stored procedures and functions that are commonly found in relational databases are not supported by MongoDB. Connect to MongoDB and authenticate as a user that has Database Administrator privileges. Check each user of the database to verify that only authorized administrative users are granted the following privileges: createCollection and changeStream Run the following command to get a list of all the databases in the system: show dbs For each database in the system, identify any non-administrative users roles for the database: use database db.getUsers() The server will return a document with the all users in the data and their associated roles. Organizational or site-specific documentation should identify which administrative and non-administrative users exist. For each role that a non-administrative user has in the database find the privileges each role has: db.getRole(rolename, { showPrivileges: true }) If any non-administrative user has a role that where the resource has the action of createCollections or changeStream this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-252175`

### Rule: MongoDB must enforce access restrictions associated with changes to the configuration of MongoDB or database(s).

**Rule ID:** `SV-252175r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that access restrictions are being enforced, create a test user and a custom role and then confirm expected operations: Once authenticated as a DBA administrator, use db.createUser() to create an additional user. The following operation adds a user myTester to the test database who has read-only access on the test database: use test db.createUser( { user: "myTester", pwd: password, roles: [ { role: "read", db: "test" } ] } ) Log out, then log back in as the "test" database user. Issue the following to attempt to write to the test database with a read-only privilege: use test db.testCollection.insert( { x: 1 } ) This operation will fail with a WriteResult error: WriteCommandError({ "ok" : 0, "errmsg" : "not authorized on test to execute command { insert: \"###\", ordered: \"###\", lsid: { id: \"###\" }, $db: \"###\" }", "code" : 13, "codeName" : "Unauthorized" }) If the operation does not fail, this is a finding.

## Group: SRG-APP-000389-DB-000372

**Group ID:** `V-252176`

### Rule: MongoDB must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.

**Rule ID:** `SV-252176r879762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication of an interactive user is the presentation of a Common Access Card (CAC) or other physical token bearing a valid, current, DoD-issued Public Key Infrastructure (PKI) certificate, coupled with a Personal Identification Number (PIN) to be entered by the user at the beginning of each session and whenever reauthentication is required. Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring reauthentication are privilege escalation and role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB Enterprise supports PKI x.509 certificate bearer authentication. The duration of a user's logical session is application-specific, but is verified on initial network session connection. Additional user authentication controls can be enabled on a client basis (including Windows OS-level CAC + PIN flow; see operating system documentation for specific configuration). By specifying both the database and the collection in the resource document for a privilege, administrator can limit the privilege actions just to a specific collection in a specific database. Each privilege action in a role can be scoped to a different collection. When a new privilege is applied to an object, such as a particular collection or a database, authorization to access that object is verified at run-time (i.e., in real time). To check that authorization is being enforced, see the documentation for Collection-Level Access Control and custom user roles (https://docs.mongodb.com/v4.4/core/collection-level-access-control/) and create a new role with the following permissions, e.g.: use admin db.createRole( { role: "myTestRole", privileges: [ { resource: { db: "products", collection: "inventory" }, actions: [ "find", "update", "insert" ] }, { resource: { db: "products", collection: "orders" }, actions: [ "find" ] } ], roles: [ ] }, { w: "majority" , wtimeout: 5000 } ) Assign that privilege to one or more users. use products db.createUser({user: "myRoleTestUser", pwd: "password1", roles: ["myTestRole"]}) Log in as "myRoleTestUser" user and attempt find(), insert() and delete() operations on a test inventory and orders collection. The following commands will succeed: use products db.inventory.insert({a: 1}) db.inventory.find() db.inventory.update({a:1}, {$set: {"updated": true}}) Example output of the above commands: use products switched to db products db.inventory.find() db.inventory.insert({a: 1}) WriteResult({ "nInserted" : 1 }) db.inventory.update({a:1}, {$set: {"updated": true}}) WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 0 }) Of the following ONLY the find() will succeed: use products switched to db products use products db.orders.find() db.orders.insert({a: 1}) db.orders.update({a:1}, {$set: {"updated": true}}) Example output: db.orders.find() db.orders.insert({a: 1}) WriteCommandError({ "ok" : 0, "errmsg" : "not authorized on products to execute command { insert: \"###\", ordered: \"###\", lsid: { id: \"###\" }, $db: \"###\" }", "code" : 13, "codeName" : "Unauthorized" }) db.orders.update({a:1}, {$set: {"updated": true}}) WriteCommandError({ "ok" : 0, "errmsg" : "not authorized on products to execute command { update: \"###\", ordered: \"###\", lsid: { id: \"###\" }, $db: \"###\" }", "code" : 13, "codeName" : "Unauthorized" }) In the last example above, if either or both insert() or update() succeed, this is a finding. Note that this check is by necessity application-specific.

## Group: SRG-APP-000400-DB-000367

**Group ID:** `V-252177`

### Rule: MongoDB must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-252177r879773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is configured to authenticate using SASL and LDAP check the saslauthd command line options in the system boot script that starts saslauthd (the location will be dependent on the specific Linux operating system and boot script layout and naming conventions). If the "-t" option is not set for the "saslauthd" process in the system boot script, this is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-252178`

### Rule: MongoDB must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-252178r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at https://cyber.mil/pki-pke/. This requirement focuses on communications protection for MongoDB session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To run MongoDB in TLS mode, obtain a valid certificate singed by a single certificate authority. Before starting the MongoDB database in TLS mode, verify that certificate used is issued by a valid DoD certificate authority (openssl x509 -in path_to_certificate_pem_file -text | grep -i issuer). If there is any issuer present in the certificate that is not a DoD approved certificate authority, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-252179`

### Rule: MongoDB must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-252179r879812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, MongoDB, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system information/specification for information indicating a strict requirement for data integrity and confidentiality when data is being prepared to be transmitted. If such information is absent therein, this is not a finding. If such information is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/caToValidateClientCertificates.pem allowInvalidCertificates: false allowConnectionsWithoutCertificates: false FIPSMode: true If net.tls.mode is not set to requireTLS, this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-252180`

### Rule: MongoDB must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-252180r879813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, MongoDB, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If such information is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/caToValidateClientCertificates.pem allowInvalidCertificates: false allowConnectionsWithoutCertificates: false FIPSMode: true If net.tls.mode is not set to requireTLS, this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-252181`

### Rule: When invalid inputs are received, MongoDB must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-252181r879818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This is application-specific, but see Schema Validation documentation here: https://docs.mongodb.com/v4.4/core/schema-validation/ As an example, as a user with the dbAdminAnyDatabase role, execute the following on the database of interest: use database db.getCollectionInfos() Where database is the name of the database on which validator rules are to be inspected. This returns an array of documents containing all collections information within the database. For all collections information received, check if the options sub-document contains a validator. If the options sub-document does not contain a validator, this is a finding. Example below shows a finding: [ { "name" : "inventory", "type" : "collection", "options" : { }, "info" : { "readOnly" : false, "uuid" : UUID("b2c86d4d-48bf-4394-9743-620e6d68b87f") }, "idIndex" : { "v" : 2, "key" : { "_id" : 1 }, "name" : "_id_", "ns" : "products.inventory" } } ]

## Group: SRG-APP-000454-DB-000389

**Group ID:** `V-252182`

### Rule: When updates are applied to MongoDB software, any software components that have been replaced or made unnecessary must be removed.

**Rule ID:** `SV-252182r879825_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of DBMS components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some DBMSs' installation tools may remove older versions of software automatically from the information system. In other cases, manual review and removal will be required. In planning installations and upgrades, organizations must include steps (automated, manual, or both) to identify and remove the outdated modules. A transition period may be necessary when both the old and the new software are required. This should be taken into account in the planning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command and observe the output. This command will determine if MongoDB has been installed with a package Manager (RedHat) and display what version is currently installed: rpm -q mongodb-enterprise-server.x86_64 mongodb-enterprise-server-4.4.8-1.el7.x86_64 The output of the command above indicates that MongoDB Enterprise Server has been installed with a package manager. The preceding output is an example showing that MongoDB Enterprise Server Version 4.4.8 is installed. The specific version will be dependent on the actual version installed. Upgrading MongoDB with the same package manager used for installation will overwrite or remove files as part of the upgrade process. If MongoDB was installed with a Package Manager (YUM/RPM for RedHat), this is not a finding. Run the following command and observe the output. rpm -q mongodb-enterprise-server.x86_64 package mongodb-enterprise-server.x86_64 is not installed The output of the command above indicates that MongoDB has not been installed via a package manager or may not have been installed at all. If MongoDB has not been installed with a Package Manager (YUM/RPM for RedHat), this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-252183`

### Rule: Security-relevant software updates to MongoDB must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-252183r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the organizational or site-specific software update policy and verify that MongoDB has been updated consistent with the time frame specified by the policy. The current major version of MongoDB can be found here: https://docs.mongodb.com/v4.4/release-notes/ This link will show the major version of MongoDB. To find the minor version within that release select the appropriate sublink. For example, to see the latest 4.4 minor releases in MongoDB, select the Release Notes for 4.4. This will show all minor releases and their notes. For example: 4.4.9, 4.4.8, 4.4.6, 4.4.5, etc. If MongoDB has not been updated to the necessary major and minor release in accordance with the policy, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-252184`

### Rule: MongoDB products must be a version supported by the vendor.

**Rule ID:** `SV-252184r944388_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation and interview the database administrator. Identify all database software components. Review the version and release information. To determine the current running MongoDB server version, run the following command from the Mongo Shell: db.version() Access the MongoDB website (https://www.mongodb.com/support-policy/lifecycles) or use other means to verify if the currently running MongoDB server version is still supported. If the DBMS or any of the software components are not supported by MongoDB, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-252185`

### Rule: MongoDB must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-252185r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring MongoDB to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. MongoDB must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Assessing the system against the STIG configurations and guidance of the current document is the check for this requirement. If the MongoDB is not configured in accordance with the security configuration settings of this document, this is a finding.

