# STIG Benchmark: MongoDB Enterprise Advanced 3.x Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-221158`

### Rule: MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-221158r960768_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: "enabled" If this parameter is not present, this is a finding.

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-221159`

### Rule: MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-221159r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to determine the required levels of protection for DBMS server securables by type of login. Review the permissions actually in place on the server. If the actual permissions do not match the documented requirements, this is a finding. MongoDB commands to view roles in a particular database: db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true } )

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-221160`

### Rule: MongoDB must provide audit record generation for DoD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-221160r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MongoDB must provide audit record generation capability for DoD-defined auditable events within all DBMS/database components. Satisfies: SRG-APP-000089-DB-000064, SRG-APP-000080-DB-000063, SRG-APP-000090-DB-000065, SRG-APP-000091-DB-000066, SRG-APP-000091-DB-000325, SRG-APP-000092-DB-000208, SRG-APP-000093-DB-000052, SRG-APP-000095-DB-000039, SRG-APP-000096-DB-000040, SRG-APP-000097-DB-000041, SRG-APP-000098-DB-000042, SRG-APP-000099-DB-000043, SRG-APP-000100-DB-000201, SRG-APP-000101-DB-000044, SRG-APP-000109-DB-000049, SRG-APP-000356-DB-000315, SRG-APP-000360-DB-000320, SRG-APP-000381-DB-000361, SRG-APP-000492-DB-000332, SRG-APP-000492-DB-000333, SRG-APP-000494-DB-000344, SRG-APP-000494-DB-000345, SRG-APP-000495-DB-000326, SRG-APP-000495-DB-000327, SRG-APP-000495-DB-000328, SRG-APP-000495-DB-000329, SRG-APP-000496-DB-000334, SRG-APP-000496-DB-000335, SRG-APP-000498-DB-000346, SRG-APP-000498-DB-000347, SRG-APP-000499-DB-000330, SRG-APP-000499-DB-000331, SRG-APP-000501-DB-000336, SRG-APP-000501-DB-000337, SRG-APP-000502-DB-000348, SRG-APP-000502-DB-000349, SRG-APP-000503-DB-000350, SRG-APP-000503-DB-000351, SRG-APP-000504-DB-000354, SRG-APP-000504-DB-000355, SRG-APP-000505-DB-000352, SRG-APP-000506-DB-000353, SRG-APP-000507-DB-000356, SRG-APP-000507-DB-000357, SRG-APP-000508-DB-000358, SRG-APP-000515-DB-000318</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: '/etc/mongod.conf)' for a key named 'auditLog:'. Example shown below: auditLog: destination: syslog If an "auditLog:" key is not present, this is a finding indicating that auditing is not turned on. If the "auditLog:" key is present and contains a subkey of "filter:" with an associated filter value string, this is a finding. The site auditing policy must be reviewed to determine if the "filter:" being applied meets the site auditing requirements. If not, then the filter being applied will need to be modified to comply. Example show below: auditLog: destination: syslog filter: '{ atype: { $in: [ "createCollection", "dropCollection" ] } }'

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-221161`

### Rule: The audit information produced by MongoDB must be protected from unauthorized read access.

**Rule ID:** `SV-221161r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions utilizing file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000119-DB-000060, SRG-APP-000120-DB-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the "<MongoDB auditLog directory>": > ls –ald <MongoDB auditLog data directory> If the User owner is not "mongod", this is a finding. If the Group owner is not "mongod", this is a finding. If the directory is more permissive than "700", this is a finding. (The path for the MongoDB auditLog directory will vary according to local circumstances. The auditLog directory will be found in the MongoDB configuration file whose default location is '/etc/mongod.conf'.) To find the auditLog directory name, view and search for the entry in the MongoDB configuration file for the auditLog.path: Example: auditLog: destination: file format: BSON path: /var/lib/mongo/auditLog.bson Given the example above, to find the auditLog directory name run the following command: > dirname /var/lib/mongo/auditLog.bson the output will be the "<MongoDB auditLog directory>" /var/lib/mongo

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-221162`

### Rule: MongoDB must protect its audit features from unauthorized access.

**Rule ID:** `SV-221162r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. It is, therefore, imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, he could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity. Satisfies: SRG-APP-000121-DB-000202, SRG-APP-000122-DB-000203, SRG-APP-000122-DB-000204</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify User ownership, Group ownership, and permissions on the “<MongoDB configuration file>": (default name and location is '/etc/mongod.conf') (The name and location for the MongoDB configuration file will vary according to local circumstances.) Using the default name and location the command would be: > ls –ald /etc/mongod.conf If the User owner is not "mongod", this is a finding. If the Group owner is not "mongod", this is a finding. If the filename is more permissive than "700", this is a finding.

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-221163`

### Rule: MongoDB software installation account must be restricted to authorized users.

**Rule ID:** `SV-221163r960960_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. DBA and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review procedures for controlling, granting access to, and tracking use of the DBMS software installation account. If access or use of this account is not restricted to the minimum number of personnel required or if unauthorized access to the account has been granted, this is a finding.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-221164`

### Rule: Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-221164r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MongoDB software library directory and note other root directories located on the same disk directory or any subdirectories. If any non-MongoDB software directories exist on the disk directory, examine or investigate their use. If any of the directories are used by other applications, including third-party applications that use the MongoDB this is a finding. Only applications that are required for the functioning and administration, not use, of the MongoDB should be located in the same disk directory as the MongoDB software libraries. If other applications are located in the same directory as the MongoDB database this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-221165`

### Rule: The role(s)/group(s) used to modify database structure (including but not necessarily limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be restricted to authorized users.

**Rule ID:** `SV-221165r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to get the roles from a MongoDB database. For each database in MongoDB: use <database> db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true } ) Run the following command to the roles assigned to users: use admin db.system.users.find() Analyze the output and if any roles or users have unauthorized access, this is a finding.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-221166`

### Rule: Unused database components, DBMS software, and database objects must be removed.

**Rule ID:** `SV-221166r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of components and features installed with the MongoDB database. If unused components are installed and are not documented and authorized, this is a finding. RPM can also be used to check to see what is installed: yum list installed | grep mongodb This returns MongoDB database packages that have been installed. If any packages displayed by this command are not being used, this is a finding.

## Group: SRG-APP-000141-DB-000092

**Group ID:** `V-221167`

### Rule: Unused database components that are integrated in MongoDB and cannot be uninstalled must be disabled.

**Rule ID:** `SV-221167r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Unused, unnecessary DBMS components increase the attack vector for MongoDB by introducing additional targets for attack. By minimizing the services and applications installed on the system, the number of potential vulnerabilities is reduced. Components of the system that are unused and cannot be uninstalled must be disabled. The techniques available for disabling components will vary by DBMS product, OS, and the nature of the component and may include DBMS configuration settings, OS service settings, OS file access security, and DBMS user/role permissions. Satisfies: SRG-APP-000141-DB-000092, SRG-APP-000142-DB-000094</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: http: enabled: true JSONPEnabled: true RESTInterfaceEnabled: true If any of the <booleans> are "True" or "Enabled", this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-221168`

### Rule: MongoDB must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-221168r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view another user’s information, you must have the "viewUser" action on the other user’s database. For each database in the system, run the following command: db.getUsers() Ensure each user identified is a member of an appropriate organization that can access the database. If a user is found not be a member or an appropriate organization that can access the database, this is a finding. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: "enabled" If this parameter is not present, this is a finding.

## Group: SRG-APP-000164-DB-000401

**Group ID:** `V-221169`

### Rule: If DBMS authentication using passwords is employed, MongoDB must enforce the DoD standards for password complexity and lifetime.

**Rule ID:** `SV-221169r981946_rule`
**Severity:** high

**Description:**
<VulnDiscussion>OS/enterprise authentication and identification must be used (SQL2-00-023600). Built-in DBMS authentication may be used only when circumstances make it unavoidable and must be documented and AO-approved. The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, the DoD standards for password complexity and lifetime must be implemented. DBMS products that can inherit the rules for these from the operating system or access control program (e.g., Microsoft Active Directory) must be configured to do so. For other DBMSs, the rules must be enforced using available configuration parameters or custom code.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is using Native LDAP authentication where the LDAP server is configured to enforce password complexity and lifetime, this is not a finding. If MongoDB is using Kerberos authentication where Kerberos is configured to enforce password complexity and lifetime, this is not a finding. If MongoDB is configured for SCRAM-SHA1, MONGODB-CR, LDAP Proxy authentication, this is a finding. See: https://docs.mongodb.com/v3.4/core/authentication/#authentication-methods

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-221170`

### Rule: If passwords are used for authentication, MongoDB must store only hashed, salted representations of passwords.

**Rule ID:** `SV-221170r981949_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, database passwords stored in clear text using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to MongoDB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB supports x.509 certificate authentication for use with a secure TLS/SSL connection. The x.509 client authentication allows clients to authenticate to servers with certificates rather than with a username and password. If X.509 authentication is not used, a SCRAM-SHA-1 authentication protocol is also available. The SCRAM-SHA-1 protocol uses one-way, salted hash functions for passwords as documented here: https://docs.mongodb.com/v3.4/core/security-scram-sha-1/ To authenticate with a client certificate, you must first add a MongoDB user that corresponds to the client certificate. See Add x.509 Certificate subject as a User as documented here: https://docs.mongodb.com/v3.4/tutorial/configure-x509-client-authentication/ To authenticate, use the db.auth() method in the $external database, specifying "MONGODB-X509" for the mechanism field, and the user that corresponds to the client certificate for the user field. If the mechanism field is not set to "MONGODB-X509", this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-221171`

### Rule: If passwords are used for authentication, MongoDB must transmit only encrypted representations of passwords.

**Rule ID:** `SV-221171r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Authentication based on User ID and Password may be used only when it is not possible to employ a PKI certificate, and requires AO approval. In such cases, passwords need to be protected at all times and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database. Satisfies: SRG-APP-000172-DB-000075, SRG-APP-000175-DB-000067</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: ssl: mode: requireSSL PEMKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/mongodbca.pem If the "CAFile" parameter is not present, this is a finding. If the "allowInvalidCertificates" parameter is found, this is a finding. net: ssl: allowInvalidCertificates: true

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-221172`

### Rule: MongoDB must enforce authorized access to all PKI private keys stored/utilized by MongoDB.

**Rule ID:** `SV-221172r961041_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where MongoDB-stored private keys are used to authenticate MongoDB to the system’s clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man in the middle attacks against MongoDB system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 validated cryptographic modules. All access to the private key(s) of MongoDB must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of MongoDB's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: ssl: mode: requireSSL PEMKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/mongodbca.pem Verify ownership, group ownership, and permissions on the file given for PEMKeyFile (default 'mongodb.pem'). Run following command and review its output: ls -al /etc/mongod.conf typical output: -rw------- 1 mongod mongod 566 Apr 26 20:20 /etc/mongod.conf If the user owner is not "mongod", this is a finding. If the group owner is not "mongod", this is a finding. If the file is more permissive than "600", this is a finding. Verify ownership, group ownership, and permissions on the file given for CAFile (default 'ca.pem'). If the user owner is not "mongod", this is a finding. If the group owner is not "mongod", this is a finding. If the file is more permissive than "600", this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-221173`

### Rule: MongoDB must map the PKI-authenticated identity to an associated user account.

**Rule ID:** `SV-221173r961044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to a DBMS user account for the authenticated identity to be meaningful to MongoDB and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To authenticate with a client certificate, you must first add the value of the subject from the client certificate as a MongoDB user. Each unique x.509 client certificate corresponds to a single MongoDB user; i.e. you cannot use a single client certificate to authenticate more than one MongoDB user. Login to MongoDB and run the following command: use $external db.getUsers() If the output does not contain a Relative Distinguished Name (RDN) for an authorized user, this is a finding. If the output shows a Relative Distinguished Name (RDN) for users that are not authorized, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-221174`

### Rule: MongoDB must use NIST FIPS 140-2-validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-221174r961050_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of utilizing encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of MongoDB. Applications, including DBMSs, utilizing cryptography are required to use approved NIST FIPS 140-2-validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The security functions validated as part of FIPS 140-2 for cryptographic modules are described in FIPS 140-2 Annex A. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. Satisfies: SRG-APP-000179-DB-000114, SRG-APP-000514-DB-000381, SRG-APP-000514-DB-000382, SRG-APP-000514-DB-000383, SRG-APP-000416-DB-000380</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is deployed in a classified environment: In the MongoDB database configuration file (default location: /etc/mongod.conf), search for and review the following parameters: net: ssl: FIPSMode: true If this parameter is not present in the configuration file, this is a finding. If "FIPSMode" is set to "false", this is a finding. Check the server log file for a message that FIPS is active: Search the log for the following text ""FIPS 140-2 mode activated"". If this text is not found, this is a finding. Verify that FIPS has been enabled at the operating system. The following will return "1" if FIPS is enabled: cat /proc/sys/crypto/fips_enabled If the above command does not return "1", this is a finding.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-221175`

### Rule: MongoDB must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-221175r961053_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-organizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the Nation. Satisfies: SRG-APP-000180-DB-000115, SRG-APP-000211-DB-000122, SRG-APP-000211-DB-000124</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB grants access to data and commands through role-based authorization and provides built-in roles that provide the different levels of access commonly needed in a database system. You can additionally create user-defined roles. Check a user's role to ensure correct privileges for the function: Prereq: To view a user's roles, you must have the "viewUser" privilege. Connect to MongoDB. For each database in the system, identify the user's roles for the database: use <database> db.getUser("[username]") The server will return a document with the user's roles. View a role's privileges: Prereq: To view a user's roles, you must have the "viewUser" privilege. For each database, identify the privileges granted by a role: use <database> db.getRole( "read", { showPrivileges: true } ) The server will return a document with the "privileges" and "inheritedPrivileges" arrays. The "privileges returned document lists the privileges directly specified by the role and excludes those privileges inherited from other roles. The "inheritedPrivileges" returned document lists all privileges granted by this role, both directly specified and inherited. If the role does not inherit from other roles, the two fields are the same. If a user has a role with inappropriate privileges, this is a finding.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-221176`

### Rule: MongoDB must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-221176r961119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One class of man-in-the-middle, or session hijacking, attack involves the adversary guessing at valid session identifiers based on patterns in identifiers already known. The preferred technique for thwarting guesses at Session IDs is the generation of unique session identifiers using a FIPS 140-2 approved random number generator. However, it is recognized that available DBMS products do not all implement the preferred technique yet may have other protections against session hijacking. Therefore, other techniques are acceptable, provided they are demonstrated to be effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: /etc/mongod.conf). The following should be set: net: ssl: mode: requireSSL If this is not found in the MongoDB configuration file, this is a finding.

## Group: SRG-APP-000225-DB-000153

**Group ID:** `V-221177`

### Rule: MongoDB must fail to a secure state if system initialization fails, shutdown fails, or aborts fail.

**Rule ID:** `SV-221177r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known state can address safety or security in accordance with the mission/business needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Failure to a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Systems that fail suddenly and with no incorporated failure state planning may leave the hosting system available but with a reduced security protection capability. Preserving information system state data also facilitates system restart and return to the operational mode of the organization with less disruption of mission/business processes. Databases must fail to a known consistent state. Transactions must be successfully completed or rolled back. In general, security mechanisms should be designed so that a failure will follow the same execution path as disallowing the operation. For example, application security methods, such as isAuthorized(), isAuthenticated(), and validate(), should all return false if there is an exception during processing. If security controls can throw exceptions, they must be very clear about exactly what that condition means. Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations. Satisfies: SRG-APP-000225-DB-000153, SRG-APP-000226-DB-000147</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Journaling is enabled by default in 64-bit systems. With journaling enabled, if mongod stops unexpectedly, the program can recover everything written to the journal. MongoDB will re-apply the write operations on restart and maintain a consistent state. By default, the greatest extent of lost writes, i.e., those not made to the journal, are those made in the last 100 milliseconds, plus the time it takes to perform the actual journal writes. Verify the mongod process startup options. If the mongod process was started with the "--nojournal" option, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-221178`

### Rule: MongoDB must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-221178r961128_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in non-mobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the MongoDB Encrypted Storage Engines is being used, ensure that the "security.enableEncryption" option is set to "true" in the MongoDB configuration file (default location: /etc/mongod.conf) or that MongoDB was started with the "--enableEncryption" command line option. Check the MongoDB configuration file (default location: /etc/mongod.conf). If the following parameter is not present, this is a finding. security: enableEncryption: "true" If any mongod process is started with "--enableEncryption false", this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-221179`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-221179r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000243-DB-000373

**Group ID:** `V-221180`

### Rule: MongoDB must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-221180r961149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse. Satisfies: SRG-APP-000243-DB-000373, SRG-APP-000243-DB-000374</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the permissions for the following database files or directories: MongoDB default configuration file: "/etc/mongod.conf" MongoDB default data directory: "/var/lib/mongo" If the owner and group are not both "mongod", this is a finding. If the file permissions are more permissive than "755", this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-221181`

### Rule: MongoDB must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-221181r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a client program assembles a query in MongoDB, it builds a BSON object, not a string. Thus traditional SQL injection attacks are not a problem. However, MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. If the "security.javascriptEnabled" option is set to "true" in the config file, this is a finding. Starting with MongoDB 3.2, database-level document validation can be configured for specific collections. Configured validation rules for the selected database can be viewed via the db.getSisterDB("database_name").getCollectionInfos() command in mongo shell. If validation is desired, but no rules are set, the valdiationAction is not "error" or the "bypassDocumentValidation" option is used for write commands on the application side, this is a finding.

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-221182`

### Rule: MongoDB and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-221182r961158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be utilized otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, pre-compiled stored procedures and functions (and triggers). This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered. Satisfies: SRG-APP-000251-DB-000391, SRG-APP-000251-DB-000392</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. If the following parameter is not present or not set as show below in the MongoDB configuration file (default location: /etc/mongod.conf), this is a finding. security: javascriptEnabled: "false"

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-221183`

### Rule: MongoDB must provide non-privileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-221183r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom database code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If custom database errors contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding. When attempting to login with incorrect credentials, the user will receive an error message that the operation was unauthorized. If a user is attempting to perform an operation for which they do not have privileges, the database will return an error message that the operation is not authorized.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-221184`

### Rule: MongoDB must reveal detailed error messages only to the ISSO, ISSM, SA, and DBA.

**Rule ID:** `SV-221184r961170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages need to be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among others things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA, and DBA. Other individuals or roles may be specified according to organization-specific needs, with appropriate approval. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A mongod or mongos running with "security.redactClientLogData" redacts any message accompanying a given log event before logging. This prevents the mongod or mongos from writing potentially sensitive data stored on the database to the diagnostic log. Metadata such as error or operation codes, line numbers, and source file names are still visible in the logs. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: redactClientLogData: "true" If this parameter is not present, this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-221185`

### Rule: MongoDB must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-221185r961269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for MongoDB to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling, or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or FOUO. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of MongoDB product, a third-party product, or custom application code. Satisfies: SRG-APP-000311-DB-000308, SRG-APP-000313-DB-000309, SRG-APP-000313-DB-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB supports role-based access control at the collection level. If enabled, the database process should be started with "security.authorization:enabled" in the config file or with "--auth" in the command line. For documents that have been labeled (e.g., {"tag" : "classified"}), read-only views can be created and secured via access privileges such that a user can only view those documents that have a specific tag or tags (e.g., user x can only view records that are labeled with the tag of classified). Existing views can be listed using the db.getCollectionInfos() command for the selected database in mongo shell. If a view is not present for the collection requiring security labeling, this is a finding. MongoDB supports field-level redaction that allows the application to indicate to the database whether or not certain fields should be returned based on values in the field labels. If desired and aggregation queries in the application code are not using the $redact stage with appropriate logic, this is a finding.

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-221186`

### Rule: MongoDB must enforce discretionary access control policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-221186r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. Satisfies: SRG-APP-000328-DB-000301, SRG-APP-000340-DB-000304</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system documentation to obtain the definition of the database/DBMS functionality considered privileged in the context of the system in question. If any functionality considered privileged has access privileges granted to non-privileged users, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-221188`

### Rule: MongoDB must utilize centralized management of the content captured in audit records generated by all components of MongoDB.

**Rule ID:** `SV-221188r981952_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. MongoDB may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB can be configured to write audit events to the syslog in Linux, but this is not available in Windows. Audit events can also be written to a file in either JSON on BSON format. Through the use of third-party tools or via syslog directly, audit records can be pushed to a centralized log management system. If a centralized tool for log management is not installed and configured to collect audit logs or syslogs, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-221189`

### Rule: MongoDB must allocate audit record storage capacity in accordance with site audit record storage requirements.

**Rule ID:** `SV-221189r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, MongoDB must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of MongoDB and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on MongoDB's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Investigate whether there have been any incidents where MongoDB ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If there have been incidents where MongoDB ran out of audit log space, this is a finding. A MongoDB audit log that is configured to be stored in a file is identified in the MongoDB configuration file (default: /etc/mongod.conf) under the "auditLog:" key and subkey "destination:" where "destination" is "file". If this is the case then the "AuditLog:" subkey "path:" determines where (device/directory) that file will be located. View the mongodb configuration file (default location: /etc/mongod.conf) and identify how the "auditlog.destination" is configured. When the "auditlog.destination" is "file", this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-221190`

### Rule: MongoDB must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75% of maximum audit record storage capacity.

**Rule ID:** `SV-221190r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to MongoDB on its own server will not be an issue. However, space will still be required on MongoDB server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the ISSO and the DBA/SA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A MongoDB audit log that is configured to be stored in a file is identified in the MongoDB configuration file (default: /etc/mongod.conf) under the "auditLog:" key and subkey "destination:" where "destination" is "file". If this is the case then the "AuditLog:" subkey "path:" determines where (device/directory) that file will be located. View the mongodb configuration file (default location: /etc/mongod.conf) and identify how the "auditlog.destination" is configured. When the "auditlog.destination" is "file", this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-221191`

### Rule: MongoDB must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-221191r981956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. MongoDB must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization). In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB supports only software development, experimentation, and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. Review the MongoDB security settings with respect to non-administrative users' ability to create, alter, or replace functions or views. These MongoDB commands can help with showing existing roles and permissions of users of the databases. db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true }) If any such permissions exist and are not documented and approved, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-221192`

### Rule: MongoDB must enforce access restrictions associated with changes to the configuration of MongoDB or database(s).

**Rule ID:** `SV-221192r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the security configuration of the MongoDB database(s). If unauthorized users can start the mongod or mongos processes or edit the MongoDB configuration file (default location: /etc/mongod.conf), this is a finding. If MongoDB does not enforce access restrictions associated with changes to the configuration of the database(s), this is a finding. To assist in conducting reviews of permissions, the following MongoDB commands describe permissions of databases and users: Permissions of concern in this respect include the following, and possibly others: - any user with a role of userAdminAnyDatabase role or userAdmin role - any database or with a user have a role or privilege with "C" (create) or "w" (update) privileges that are not necessary MongoDB commands to view roles in a particular database: db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true })

## Group: SRG-APP-000389-DB-000372

**Group ID:** `V-221193`

### Rule: MongoDB must require users to reauthenticate when organization-defined circumstances or situations require reauthentication.

**Rule ID:** `SV-221193r987687_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DoD standard for authentication of an interactive user is the presentation of a Common Access Card (CAC) or other physical token bearing a valid, current, DoD-issued Public Key Infrastructure (PKI) certificate, coupled with a Personal Identification Number (PIN) to be entered by the user at the beginning of each session and whenever reauthentication is required. Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring reauthentication are privilege escalation and role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If organization-defined circumstances or situations require reauthentication, and these situations are not configured to terminate existing logins to require reauthentication, this is a finding.

## Group: SRG-APP-000400-DB-000367

**Group ID:** `V-221194`

### Rule: MongoDB must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-221194r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If cached authentication information is out-of-date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is configured to authenticate using SASL and LDAP/Active Directory check the saslauthd command line options in the system boot script that starts saslauthd (the location will be dependent on the specific Linux operating system and boot script layout and naming conventions). If the "-t" option is not set for the "saslauthd" process in the system boot script, this is a finding. If any mongos process is running (a MongoDB shared cluster) the "userCacheInvalidationIntervalSecs" option can be used to specify the cache timeout. The default is "30" seconds and the minimum is "1" second.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-221195`

### Rule: MongoDB must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-221195r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DoD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. This requirement focuses on communications protection for MongoDB session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To run MongoDB in SSL mode, you have to obtain a valid certificate singed by a single certificate authority. Before starting the MongoDB database in SSL mode, verify that certificate used is issued by a valid DoD certificate authority (openssl x509 -in <path_to_certificate_pem_file> -text | grep -i "issuer"). If there is any issuer present in the certificate that is not a DoD approved certificate authority, this is a finding.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-221196`

### Rule: MongoDB must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-221196r961599_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to MongoDB or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides. Satisfies: SRG-APP-000428-DB-000386, SRG-APP-000429-DB-000387</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation and/or specification for the organization-defined information. If any data is PII, classified or is deemed by the organization to be encrypted at rest, this is a finding. Verify the mongod command line contain the following options: --enableEncryption --kmipServerName <KMIP Server HostName> --kmipPort <KMIP server port> --kmipServerCAFile ca.pem --kmipClientCertificateFile client.pem If these above options are not part of the mongod command line, this is a finding. Items in the <> above and starting with kmip* are specific to the KMIP appliance and need to be set according to the KMIP appliance configuration.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-221197`

### Rule: MongoDB must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-221197r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, MongoDB, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the system information/specification for information indicating a strict requirement for data integrity and confidentiality when data is being prepared to be transmitted. If such information is absent therein, this is not a finding. If such information is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: ssl: mode: requireSSL PEMKeyFile: /etc/ssl/mongodb.pem If net.ssl.mode is not set to "requireSSL", this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-221198`

### Rule: MongoDB must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-221198r961641_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, MongoDB, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If such strict requirement for ensure data integrity and confidentially is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: ssl: mode: requireSSL PEMKeyFile: /etc/ssl/mongodb.pem If net.ssl.mode is not set to "requireSSL", this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-221199`

### Rule: When invalid inputs are received, MongoDB must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-221199r961656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a user with the "dbAdminAnyDatabase" role, execute the following on the database of interest: use myDB db.getCollectionInfos() Where "myDB" is the name of the database on which validator rules are to be inspected. This returns an array of documents containing all collections information within myDB. For each collection's information received. If the "options" sub-document within each does not contain a "validator" sub-document, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-221200`

### Rule: MongoDB must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-221200r961047_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DoD standard for authentication is DoD-approved PKI certificates. Normally, with PKI authentication, the interaction with the user for authentication will be handled by a software component separate from MongoDB, such as ActivIdentity ActivClient. However, in cases where MongoDB controls the interaction, this requirement applies. To prevent the compromise of authentication information such as passwords and PINs during the authentication process, the feedback from the system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided authentication secrets when typed into the system is a method used in addressing this risk. Displaying asterisks when a user types in a password or a smart card PIN is an example of obscuring feedback of authentication secrets. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed, and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For the MongoDB command-line tools "mongo shell", "mongodump", "mongorestore", "mongoimport", "mongoexport", which cannot be configured not to accept a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations and that AO approval has been obtained. If it is not documented, this is a finding. Request evidence that all users of these MongoDB command-line tools are trained in the use of the "-p" option plain-text password option and how to keep the password protected from unauthorized viewing/capture and that they adhere to this practice. If evidence of training does not exist, this is a finding.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-221201`

### Rule: MongoDB must be configured in accordance with the security configuration settings based on DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-221201r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring MongoDB to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. MongoDB must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MongoDB documentation and configuration to determine it is configured in accordance with DoD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs. If the MongoDB is not configured in accordance with security configuration settings, this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-265875`

### Rule: MongoDB products must be a version supported by the vendor.

**Rule ID:** `SV-265875r999531_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To determine the current running MongoDB server version, run the following command from the Mongo Shell: db.version() MongoDB 3.x is no longer supported by the vendor. If the system is running MongoDB 3.x, this is a finding.

