# STIG Benchmark: MongoDB Enterprise Advanced 7.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000023-DB-000001

**Group ID:** `V-265905`

### Rule: MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.

**Rule ID:** `SV-265905r1028704_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must integrate with an organization-level authentication/access mechanism providing account management and automation for all users, groups, roles, and any other principals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: "enabled" If this parameter is not present, this is a finding. If using organization-mandated authorization: Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following to ensure LDAP auth is enabled as well: security: ldap: servers: [list of ldap servers] If this parameter is not present, this is a finding. Refer to Security LDAP configuration documentation for additional details: https://www.mongodb.com/docs/v7.0/core/security-ldap-external/#configuration

## Group: SRG-APP-000033-DB-000084

**Group ID:** `V-265906`

### Rule: MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-265906r1028504_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MongoDB must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The MongoDB administrator must ensure that additional application access control is enforced. Review the system documentation to determine the required levels of protection for MongoDB server securables by type of login. Review the permissions actually in place on the server. Run the command to view roles and privileges in a particular <database> : use <database> db.getRoles( { rolesInfo: 1, showPrivileges: true, showBuiltinRoles: true } ) If the permissions do not match the documented requirements, this is a finding.

## Group: SRG-APP-000080-DB-000063

**Group ID:** `V-265907`

### Rule: MongoDB must provide audit record generation for DOD-defined auditable events within all DBMS/database components.

**Rule ID:** `SV-265907r1028717_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MongoDB must provide audit record generation capability for DOD-defined auditable events within all DBMS/database components. Satisfies: SRG-APP-000080-DB-000063, SRG-APP-000089-DB-000064, SRG-APP-000090-DB-000065, SRG-APP-000091-DB-000066, SRG-APP-000091-DB-000325, SRG-APP-000092-DB-000208, SRG-APP-000095-DB-000039, SRG-APP-000096-DB-000040, SRG-APP-000097-DB-000041, SRG-APP-000098-DB-000042, SRG-APP-000099-DB-000043, SRG-APP-000100-DB-000201, SRG-APP-000101-DB-000044, SRG-APP-000109-DB-000049, SRG-APP-000356-DB-000315, SRG-APP-000381-DB-000361, SRG-APP-000492-DB-000332, SRG-APP-000492-DB-000333, SRG-APP-000494-DB-000344, SRG-APP-000494-DB-000345, SRG-APP-000495-DB-000326, SRG-APP-000495-DB-000327, SRG-APP-000495-DB-000328, SRG-APP-000495-DB-000329, SRG-APP-000496-DB-000334, SRG-APP-000496-DB-000335, SRG-APP-000498-DB-000346, SRG-APP-000498-DB-000347, SRG-APP-000499-DB-000330, SRG-APP-000499-DB-000331, SRG-APP-000501-DB-000336, SRG-APP-000501-DB-000337, SRG-APP-000502-DB-000348, SRG-APP-000502-DB-000349, SRG-APP-000503-DB-000350, SRG-APP-000503-DB-000351, SRG-APP-000504-DB-000354, SRG-APP-000504-DB-000355, SRG-APP-000505-DB-000352, SRG-APP-000506-DB-000353, SRG-APP-000507-DB-000356, SRG-APP-000507-DB-000357, SRG-APP-000508-DB-000358</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: /etc/mongod.conf) for a key named "auditLog:". Examples shown below: auditLog: destination: file format: BSON path: <mongodb audit log directory>/auditLog.bson filter: '{ atype: { $in: [ "createCollection", "dropCollection" ] } }' -OR- auditLog: destination: syslog If an "auditLog:" key is not present, this is a finding. If the "auditLog:" key is present, ensure the subkey of "destination:" is set to either "file" or "syslog". If not, this is a finding. If the "auditLog:" key is present and contains a subkey of "filter:", ensure the filter is valid. If the filter is invalid, this is a finding. The site auditing policy must be reviewed to determine if the "filter:" being applied meets the site auditing requirements. If not, this is a finding. Check the MongoDB configuration file (default location: /etc/mongod.conf) for the following entry: setParameter: auditAuthorizationSuccess: true If this setParameter entry does not have "auditAuthorizationSuccess: true", this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-265908`

### Rule: The audit information produced by MongoDB must be protected from unauthorized access.

**Rule ID:** `SV-265908r1028718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could potentially use to their advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, copy, etc. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Some commonly employed methods include ensuring log files enjoy the proper file system permissions using file system protections and limiting log data location. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring that audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000119-DB-000060, SRG-APP-000120-DB-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB must not permit access to its audit logs by unprivileged users. The official installation packages restrict which operating system users and groups may read or modify files. The audit log destination is not configured or created at installation time and must be manually done with appropriate ownership and permissions applied with the MongoDB user and MongoDB group. Check the MongoDB configuration file (default location: /etc/mongod.conf) for a key named "auditLog:" with "destination" set to "file". Example shown below: auditLog: destination: file format: BSON path: <MongoDB auditLog directory>/auditLog.bson If "auditLog" does not exist this is a finding. If the auditLog.destination is "file" in the MongoDB configuration file (default location /etc/mongod.conf) then the following will check ownership and permissions of the MongoDB auditLog directory: Verify User ownership, Group ownership, and permissions on the "<MongoDB auditLog directory>": $ stat <MongoDB auditLog directory> If the User owner is not "mongod", this is a finding. If the Group owner is not "mongod", this is a finding. If the directory is more permissive than "700", this is a finding. To find the auditLog directory name, view and search for the entry in the MongoDB configuration file (default location /etc/mongod.conf) for auditLog.destination. If this parameters value is "file" then use the directory portion of the auditLog.path setting as the MongoDB auditLog directory location. Example: auditLog: destination: file format: BSON path: /var/log/mongodb/audit/auditLog.bson Given the example above, to find the auditLog directory ownership and permissions run the following command: > stat /var/log/mongodb/audit The output will look similar to the following: File: '/var/log/mongodb/audit' Size: 48 Blocks: 0 IO Block: 4096 directory Device: 808h/2056d Inode: 245178 Links: 2 Access: (0700/drwx------) Uid: ( 997/ mongod) Gid: ( 996/ mongod) Context: unconfined_u:object_r:mongod_log_t:s0 Access: 2020-03-16 12:51:16.816000000 -0400 Modify: 2020-03-16 12:50:48.722000000 -0400 Change: 2020-03-16 12:50:48.722000000 -0400 Birth: -

## Group: SRG-APP-000121-DB-000202

**Group ID:** `V-265909`

### Rule: MongoDB must protect its audit features from unauthorized access.

**Rule ID:** `SV-265909r1028719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Depending upon the log format and application, system and application log tools may provide the only means to manipulate and manage application and system log data. Therefore, it is imperative that access to audit tools be controlled and protected from unauthorized access. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, OS-provided audit tools, vendor-provided audit tools, and open source audit tools needed to successfully view and manipulate audit information system activity and records. If an attacker were to gain access to audit tools, they could analyze audit logs for system weaknesses or weaknesses in the auditing itself. An attacker could also manipulate logs to hide evidence of malicious activity. Satisfies: SRG-APP-000121-DB-000202, SRG-APP-000122-DB-000203, SRG-APP-000123-DB-000204 </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure audit configurations are protected from unauthorized modification, the default installation of MongoDB restricts permission on the configuration file. Verify User ownership, Group ownership, and permissions on the "<MongoDB configuration file>": (default name and location is /etc/mongod.conf) (The name and location for the MongoDB configuration file will vary according to local circumstances.) Using the default name and location the command would be: $ stat /etc/mongod.conf If the User owner is not "mongod", this is a finding. If the Group owner is not "mongod", this is a finding. If the filename is more permissive than "600", this is a finding. Note that the audit destination cannot be modified at runtime.

## Group: SRG-APP-000133-DB-000179

**Group ID:** `V-265910`

### Rule: MongoDB must limit privileges to change software modules, to include stored procedures, functions and triggers, and links to software external to MongoDB.

**Rule ID:** `SV-265910r1028793_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review monitoring procedures and implementation evidence to verify monitoring of changes to database software libraries, related applications, and configuration files occurs. Verify the list of files, directories, and database application objects (procedures, functions, and triggers) being monitored is complete. There are many possible options to monitor the database. The most common are making use of a monitoring tool or running a script periodically. If a monitoring tool is actively being used to monitor the database and there is proof of the tool being active, this is not a finding. Where monitoring is implemented by a scheduled or on-demand running of a Bash shell script to check the current SHA-256 checksum of the MongoDB files with the original SHA-256 Checksum after installation and configuration. Run the following shell script "check_mongodb_256sha_hashes.sh" from its containing Linux directory as a system administrator. $ ./check_mongodb_256sha_hashes.sh If the output is not the following, this is a finding: "No changes detected in the monitored files." The shell script file "check_mongodb_2456sha_hashes.sh" is as follows: # filename: check_mongodb_256sha_hashes.sh #!/bin/bash # Function to compute SHA-256 hash of the specified file file_hash() { sha256sum "$1" | awk '{print $1}' } # Function to check the list of files for any changes based on their SHA-256 hashes check_files() { local changed=0 declare -A stored_hashes # Try to load last known hashes if [ -f file_hashes.txt ]; then while IFS=: read -r file hash; do stored_hashes["$file"]=$hash done < file_hashes.txt fi # Check each file's hash against stored hashes for file in "$@"; do if [ -f "$file" ]; then current_hash=$(file_hash "$file") if [[ "${stored_hashes[$file]}" != "$current_hash" ]]; then if [[ -n "${stored_hashes[$file]}" ]]; then echo "Change detected in $file" else echo "New file added or first time hashing: $file" fi changed=1 stored_hashes["$file"]=$current_hash fi else echo "Warning: $file does not exist." fi done # Save the updated hashes > file_hashes.txt for file in "${!stored_hashes[@]}"; do echo "$file:${stored_hashes[$file]}" >> file_hashes.txt done if [ "$changed" -eq 0 ]; then echo "No changes detected in the monitored files." fi } # List of files to monitor files_to_check=( "/etc/mongod.conf" "/usr/bin/mongod" "/usr/bin/mongos" "/usr/bin/mongosh" "/usr/bin/mongocryptd" "/usr/bin/mongodecrypt" "/usr/bin/mongodump" "/usr/bin/mongoexport" "/usr/bin/mongofiles" "/usr/bin/mongoimport" "/usr/bin/mongokerberos" "/usr/bin/mongoldap" "/usr/bin/mongorestore" "/usr/bin/mongostat" "/usr/bin/mongotop" ) # Invoke check_files function with the list of files check_files "${files_to_check[@]}"

## Group: SRG-APP-000133-DB-000198

**Group ID:** `V-265911`

### Rule: MongoDB software installation account must be restricted to authorized users.

**Rule ID:** `SV-265911r1028721_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can have significant effects on the overall security of the system. If the system were to allow any user to make changes to software libraries, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed access to information system components for purposes of initiating changes, including upgrades and modifications. Database administrators (DBAs) and other privileged administrative or application owner accounts are granted privileges that allow actions that can have a great impact on database security and operation. It is especially important to grant privileged access to only those persons who are qualified and authorized to use them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure log, network, security, and other audit configurations are not modifiable by unauthorized operating system users, the default installation of MongoDB restricts permission on the configuration file. Verify User ownership, Group ownership, and permissions on the "<MongoDB configuration file>": (default name and location is /etc/mongod.conf) Using the default name and location the command would be: $ stat /etc/mongod.conf If the User owner is not "mongod", this is a finding. If the Group owner is not "mongod", this is a finding. If the filename is more permissive than "600", this is a finding. Note that the audit destination cannot be modified at runtime.

## Group: SRG-APP-000133-DB-000199

**Group ID:** `V-265912`

### Rule: Database software, including DBMS configuration files, must be stored in dedicated directories, or DASD pools, separate from the host OS and other applications.

**Rule ID:** `SV-265912r1028522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When dealing with change control issues, it should be noted any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to host system directories can most likely lead to a compromise of all applications hosted by the same system. Database software not installed using dedicated directories both threatens and is threatened by other hosted applications. Access controls defined for one application may by default provide access to the other application's database objects or directories. Any method that provides any level of separation of security context assists in the protection between applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default MongoDB, runs using "mongod" user account (both user and group) and uses the following default directories: MongoDB created directories (default): /var/lib/mongo (the data directory) +-- diagnostic.data +-- _tmp +-- journal /var/log/mongodb (the mongod process log directory) +-- audit (the auditLog directory) Standard directories: /bin (the executable directory) /etc (the configuration file directory) Check if any non-MongoDB application, non-MongoDB data, or non-MongoDB directories exists under any of the MongoDB-created directories or subdirectories. If any non-MongoDB application, non-MongoDB data, or non-MongoDB directories exists under the MongoDB-created directories, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-265913`

### Rule: Database objects (including but not limited to tables, indexes, storage, stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be owned by database/DBMS principals authorized for ownership.

**Rule ID:** `SV-265913r1028525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who uses the object to perform the actions if they were the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. Conversely, if critical tables or other objects rely on unauthorized owner accounts, these objects may be lost when an account is removed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each database in MongoDB, run the following commands: use <database> db.getUsers() Example output: { _id: 'admin.user1', userId: UUID('b78e490a-4661-491f-8197-c3251934e785'), user: 'user1', db: 'admin', roles: [ { role: 'readWrite', db: 'myDatabase' }, { role: 'dbOwner', db: 'myDatabase' }, { role: 'dbOwner', db: 'anotherDatabase' } ] Here, the user named "user1" in the "admin" database has a role of "dbOwner" for the database (db:) "myDatabase" and the database (db:) "anotherDatabase". For users where the role of "dbOwner" is found, verify with the organization or site-specific documentation whether the user is authorized for the "dbOwner" role on the database resources listed. If the user account has the role of "dbOwner" but is not authorized for the role for any database listed in their output, this is a finding.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-265914`

### Rule: The role(s)/group(s) used to modify database structure (including but not limited to tables, indexes, storage, etc.) and logic modules (stored procedures, functions, triggers, links to software external to MongoDB, etc.) must be restricted to authorized users.

**Rule ID:** `SV-265914r1028528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB were to allow any user to make changes to database structure or logic, then those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Accordingly, only qualified and authorized individuals must be allowed to obtain access to information system components for purposes of initiating changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to get the roles from a MongoDB database. For each database in MongoDB: use <database> db.getRoles( { rolesInfo: 1, showPrivileges:true, showBuiltinRoles: true } ) Run the following command to the roles assigned to users: use admin db.system.users.find() Analyze the output and if any roles or users have unauthorized access, this is a finding. This will vary on an application basis.

## Group: SRG-APP-000141-DB-000091

**Group ID:** `V-265915`

### Rule: Unused database components that are integrated in MongoDB and cannot be uninstalled must be disabled.

**Rule ID:** `SV-265915r1028531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). It is detrimental for software products to provide, or install by default, functionality exceeding requirements or mission objectives. DBMSs must adhere to the principles of least functionality by providing only essential capabilities. Satisfies: SRG-APP-000141-DB-000091, SRG-APP-000141-DB-000092, SRG-APP-000142-DB-000094</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. If the following parameter is not present or not set as show below in the MongoDB configuration file (default location: /etc/mongod.conf), this is a finding. security: javascriptEnabled: false

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-265916`

### Rule: MongoDB must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-265916r1028534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals using shared accounts, for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each database in the system, run the following command: > use <database> > db.getUsers() Ensure each user identified is a member of an appropriate organization that can access the database. Alternatively, if LDAP/AD is being used for authentication/authorization, the mongoldap tool can be used to verify user account access. If a user is found not be a member of an appropriate organization that can access the database, this is a finding. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: security: authorization: "enabled" If this parameter is not present, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-265917`

### Rule: If passwords are used for authentication, MongoDB must store only hashed, salted representations of passwords.

**Rule ID:** `SV-265917r1028796_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate, and requires authorizing official (AO) approval. In such cases, database passwords stored in clear text, using reversible encryption, or using unsalted hashes would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to MongoDB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB supports several authentication mechanisms, some of which store credentials on the MongoDB server. If these mechanisms are in use, MongoDB's authSchemaVersion in the admin.system.version collection must be set to "5". 1. Validate that authenticationMechanisms is defined in config file (default location /etc/mongod.conf). The MongoDB Configuration file should contain the similar to the following entry: setParameter: authenticationMechanisms: SCRAM-SHA-256 If the config file does not contain an authenticationMechanisms entry, that is a finding. 2. Validate authSchemaVersion is set to "5". Using the shell, run the following command: > db.getSiblingDB("admin").system.version.find({ "_id" : "authSchema"}, {_id: 0}) It should return: { "currentVersion" : 5 } If currentVersion is less than 5, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-265918`

### Rule: If passwords are used for authentication, MongoDB must transmit only encrypted representations of passwords.

**Rule ID:** `SV-265918r1028797_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate and requires AO approval. In such cases, passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. DBMS passwords sent in clear-text format across the network are vulnerable to discovery by unauthorized users. Disclosure of passwords may easily lead to unauthorized access to the database. Satisfies: SRG-APP-000172-DB-000075, SRG-APP-000175-DB-000067</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), verify the following parameters in the "net.tls" (network TLS) section of the file: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/server.pem CAFile: /etc/ssl/ca.crt allowInvalidCertificates: false allowConnectionsWithoutCertificates: false If the "net.tls" parameter is not present, this is a finding. If the "net.tls.certificateKeyFile" parameter is not present, this is a finding. If the "net.tls.CAFile" parameter is not present, this is a finding. If the "net.tls.allowInvalidCertificates" parameter is found and set to "true", this is a finding. If the "net.tls.allowConnectionsWithoutCertificates" parameter is found and set to "true", this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-265919`

### Rule: MongoDB must enforce authorized access to all PKI private keys stored/used by MongoDB.

**Rule ID:** `SV-265919r1028543_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If the private key is stolen, an attacker can use the private key(s) to impersonate the certificate holder. In cases where MongoDB-stored private keys are used to authenticate MongoDB to the system's clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man in the middle attacks against MongoDB system and its clients. Both the holder of a digital certificate and the issuing authority must take careful measures to protect the corresponding private key. Private keys should always be generated and protected in FIPS 140-2 or 140-3 validated cryptographic modules. All access to the private key(s) of MongoDB must be restricted to authorized and authenticated users. If unauthorized users have access to one or more of MongoDB's private keys, an attacker could gain access to the key(s) and use them to impersonate the database on the network or otherwise perform unauthorized actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MongoDB database configuration file (default location: /etc/mongod.conf), review the following parameters: net: tls: mode: requireTLS certificateKeyFile: /etc/ssl/mongodb.pem CAFile: /etc/ssl/mongodbca.pem Verify ownership, group ownership, and permissions for the MongoDB config file (default: /etc/mongod.conf), the certificateKeyFile (default '/etc/ssl/mongodb.pem'), and the CAFile (default '/etc/ssl/mongodbca.pem'). For each file: Run following command and review its output: ls -al <filepath> example output: -rw------- 1 mongodb mongodb 566 Apr 26 20:20 <filepath> If the user owner is not "mongodb", this is a finding. If the group owner is not "mongodb", this is a finding. If the file is more permissive than "600", this is a finding.

## Group: SRG-APP-000177-DB-000069

**Group ID:** `V-265920`

### Rule: MongoDB must map the PKI-authenticated identity to an associated user account.

**Rule ID:** `SV-265920r1028546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. Once a PKI certificate has been validated, it must be mapped to a DBMS user account for the authenticated identity to be meaningful to MongoDB and useful for authorization decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This is not applicable if using LDAP for authentication. Each unique x.509 client certificate corresponds to a single MongoDB user; meaning a single client certificate cannot authenticate more than one MongoDB user. Login to MongoDB and run the following command: > db.runCommand( {connectionStatus: 1} ); Example output being: > db.runCommand({connectionStatus:1}).authInfo { "authenticatedUsers" : [ { "user" : "CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry", "db" : "mydb1" } ], "authenticatedUserRoles" : [ { "role" : "dbOwner", "db" : "mydb1" } ] } If the authenticated MongoDB user displayed does not have a user value equal to the x.509 cert's Subject Name, this is a finding.

## Group: SRG-APP-000178-DB-000083

**Group ID:** `V-265921`

### Rule: MongoDB must obscure feedback of authentication information during the authentication process to protect the information from possible exploitation/use by unauthorized individuals.

**Rule ID:** `SV-265921r1028798_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. Normally, with PKI authentication, the interaction with the user for authentication will be handled by a software component separate from MongoDB, such as ActivIdentity ActivClient. However, in cases where MongoDB controls the interaction, this requirement applies. To prevent the compromise of authentication information such as passwords and PINs during the authentication process, the feedback from the system must not provide any information that would allow an unauthorized user to compromise the authentication mechanism. Obfuscation of user-provided authentication secrets when typed into the system is a method used in addressing this risk. Displaying asterisks when a user types in a password or a smart card PIN is an example of obscuring feedback of authentication secrets. This calls for review of applications, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Restrict the environment to tools which meet this requirement. For the MongoDB command-line tools mongo shell "mongosh", "mongodump", "mongorestore", "mongoimport", "mongoexport", which cannot be configured not to obfuscate a plain-text password, and any other essential tool with the same limitation, verify that the system documentation explains the need for the tool, who uses it, and any relevant mitigations and that authorizing official (AO) approval has been obtained. If it is not documented, this is a finding. Request evidence that all users of these MongoDB command-line tools are trained in the use of the "-p" or "--password" option plain-text password option and how to keep the password protected from unauthorized viewing/capture and that they adhere to this practice. If evidence of training does not exist, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-265922`

### Rule: MongoDB must use NIST FIPS 140-2 or 140-3 validated cryptographic modules for cryptographic operations.

**Rule ID:** `SV-265922r1028799_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or not validated cryptographic algorithms undermines the purposes of using encryption and digital signatures to protect data. Weak algorithms can be easily broken and not validated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the DBMS. Applications (including DBMSs) using cryptography are required to use approved NIST FIPS 140-2 or 140-3 validated cryptographic modules that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. NSA Type-X (where X=1, 2, 3, 4) products are NSA-certified, hardware-based encryption modules. The standard for validating cryptographic modules will transition to the NIST FIPS 140-3 publication. FIPS 140-2 modules can remain active for up to five years after validation or until September 21, 2026, when the FIPS 140-2 validations will be moved to the historical list. Even on the historical list, CMVP supports the purchase and use of these modules for existing systems. While federal agencies decide when they move to FIPS 140-3 only modules, purchasers are reminded that for several years there may be a limited selection of FIPS 140-3 modules from which to choose. CMVP recommends purchasers consider all modules that appear on the Validated Modules Search Page: https://csrc.nist.gov/projects/cryptographic-module-validation-program/validated-modules More information on the FIPS 140-3 transition can be found here: https://csrc.nist.gov/Projects/fips-140-3-transition-effort/ Satisfies: SRG-APP-000179-DB-000114, SRG-APP-000514-DB-000381, SRG-APP-000514-DB-000382, SRG-APP-000514-DB-000383</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that FIPSMode: true is configured in the mongod.conf file (default location: /etc/mongod.conf) as shown below: net: tls: FIPSMode: true If net.tls.FIPSMode is not present or not configured as shown above in the MongoDB configuration file, this is a finding. Alternatively, run the following command from the MongoDB shell: > db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.net.tls.FIPSMode If the server is running with FIPS mode, this command will return "true". Any other output or no output is a finding. Verify that FIPS has been enabled at the OS level. Refer to the OS specific documentation on how to verify.

## Group: SRG-APP-000180-DB-000115

**Group ID:** `V-265923`

### Rule: MongoDB must uniquely identify and authenticate nonorganizational users (or processes acting on behalf of nonorganizational users).

**Rule ID:** `SV-265923r1028800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Nonorganizational users include all information system users other than organizational users, which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors, guest researchers, individuals from allied nations). Nonorganizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server. Accordingly, a risk assessment is used in determining the authentication needs of the organization. Scalability, practicality, and security are simultaneously considered in balancing the need to ensure ease of use for access to federal information and information systems with the need to protect and adequately mitigate risk to organizational operations, organizational assets, individuals, other organizations, and the nation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB grants access to data and commands through role-based authorization and provides built-in roles that provide the different levels of access commonly needed in a database system. You can additionally create user-defined roles. Check a user's role to ensure correct privileges for the function: Prerequisite: To view a user's roles, users must have the "viewUser" privilege. Connect to MongoDB. For each database in the system, identify the user's roles for the database: use <database> db.getUser("[username]") The server will return a document with the user's roles. View a role's privileges: Prerequisite: To view a user's roles, users must have the "viewUser" privilege. For each database, identify the privileges granted by a role: use <database> db.getRole( "read", { showPrivileges: true } ) The server will return a document with the "privileges" and "inheritedPrivileges" arrays. The "privileges returned document lists the privileges directly specified by the role and excludes those privileges inherited from other roles. The "inheritedPrivileges" returned document lists all privileges granted by this role, both directly specified and inherited. If the role does not inherit from other roles, the two fields are the same. If a user has a role with inappropriate privileges, this is a finding.

## Group: SRG-APP-000211-DB-000122

**Group ID:** `V-265924`

### Rule: MongoDB must separate user functionality (including user interface services) from database management functionality.

**Rule ID:** `SV-265924r1028722_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system management functionality includes functions necessary to administer databases, network components, workstations, or servers and typically requires privileged user access. The separation of user functionality from information system management functionality is either physical or logical and is accomplished by using different computers, different central processing units, different instances of the operating system, different network addresses, combinations of these methods, or other methods, as appropriate. An example of this type of separation is observed in web administrative interfaces that use separate authentication methods for users of any other information system resources. This may include isolating the administrative interface on a different domain and with additional access controls. If administrative functionality or information regarding DBMS management is presented on an interface available for users, information on DBMS settings may be inadvertently made available to the user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB grants access to data and commands through role-based authorization and provides built-in roles that provide the different levels of access commonly needed in a database system. Additionally, user-defined roles can be created. Check a user's role to ensure correct privileges for the function: Run the following command to get a list of all the databases in the system: > show dbs For each database in the system, identify the user's roles for the database: > use <database> > db.getUsers() The server will return a document with the all users in the data and their associated roles. View a role's privileges: For each database, identify the privileges granted by a role: > use <database> > db.getRole( "<role name>", { showPrivileges: true } ) The server will return a document with the "privileges" and "inheritedPrivileges" arrays. The "privileges returned document lists the privileges directly specified by the role and excludes those privileges inherited from other roles. The "inheritedPrivileges" returned document lists all privileges granted by this role, both directly specified and inherited. If the role does not inherit from other roles, the two fields are the same. If a user has a role with inappropriate privileges, this is a finding.

## Group: SRG-APP-000224-DB-000384

**Group ID:** `V-265925`

### Rule: MongoDB must maintain the authenticity of communications sessions by guarding against man-in-the-middle attacks that guess at Session ID values.

**Rule ID:** `SV-265925r1028561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One class of man-in-the-middle, or session hijacking, attack involves the adversary guessing at valid session identifiers based on patterns in identifiers already known. The preferred technique for thwarting guesses at Session IDs is the generation of unique session identifiers using a FIPS 140-2 or 140-3 approved random number generator. However, it is recognized that available DBMS products do not all implement the preferred technique yet may have other protections against session hijacking. Therefore, other techniques are acceptable, provided they are demonstrated to be effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the MongoDB configuration file (default location: /etc/mongod.conf). The following option must be present ( "net.tls.mode") and set to "requireTLS": net: tls: mode: requireTLS If this is not found in the MongoDB configuration file, this is a finding.

## Group: SRG-APP-000231-DB-000154

**Group ID:** `V-265926`

### Rule: MongoDB must protect the confidentiality and integrity of all information at rest.

**Rule ID:** `SV-265926r1028802_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This control is intended to address the confidentiality and integrity of information at rest in nonmobile devices and covers user information and system information. Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive, tape drive) within an organizational information system. Applications and application users generate information throughout the course of their application use. User data generated, as well as application-specific configuration data, needs to be protected. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate. If the confidentiality and integrity of application data is not protected, the data will be open to compromise and unauthorized modification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To provide integrity and confidentiality for data at rest, MongoDB must be configured to use the Encrypted Storage Engine. Run the following command to verify whether or not the Encrypted Storage Engine is enabled: > db.serverStatus().encryptionAtRest.encryptionEnabled Any output other than "true" is a finding. Validate whether the Encrypted Storage Engine is running with an AEAD block cipher, which provides integrity, by running the following command: > db.serverStatus().encryptionAtRest.encryptionCipherMode Any response other than "AES256-GCM" is a finding. Validate that the system is configured to use KMIP to obtain a master encryption key, rather than storing the master key on the local filesystem. Run: > db.serverStatus().encryptionAtRest.encryptionKeyId If the response is "local" or no response, this is a finding.

## Group: SRG-APP-000243-DB-000128

**Group ID:** `V-265927`

### Rule: Database contents must be protected from unauthorized and unintended information transfer by enforcement of a data-transfer policy.

**Rule ID:** `SV-265927r1028567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications, including DBMSs, must prevent unauthorized and unintended information transfer via shared system resources. Data used for the development and testing of applications often involves copying data from production. It is important that specific procedures exist for this process, to include the conditions under which such transfer may take place, where the copies may reside, and the rules for ensuring sensitive data are not exposed. Copies of sensitive data must not be misplaced or left in a temporary location without the proper controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the procedures for the refreshing of development/test data from production. Review any scripts or code that exists for the movement of production data to development/test systems, or to any other location or for any other purpose. Verify that copies of production data are not left in unprotected locations. If the code that exists for data movement does not comply with the organization-defined data transfer policy and/or fails to remove any copies of production data from unprotected locations, this is a finding.

## Group: SRG-APP-000243-DB-000373

**Group ID:** `V-265928`

### Rule: MongoDB must prevent unauthorized and unintended information transfer via shared system resources.

**Rule ID:** `SV-265928r1028570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The purpose of this control is to prevent information, including encrypted representations of information, produced by the actions of a prior user/role (or the actions of a process acting on behalf of a prior user/role) from being available to any current user/role (or current process) that obtains access to a shared system resource (e.g., registers, main memory, secondary storage) after the resource has been released back to the information system. Control of information in shared resources is also referred to as object reuse. Satisfies: SRG-APP-000243-DB-000373, SRG-APP-000243-DB-000374</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, the MongoDB official installation packages restrict user and group ownership and read/write permissions on the underlying data files and critical configuration files from other operating system users. In addition, process and memory isolation is used by default. System administrators should also consider if whole database encryption would be an effective control on an application basis. Run the following commands to verify proper permissions for the following database files or directories: $ stat /etc/mongod.conf If the owner and group are not both "mongod", this is a finding. If the file permissions are more permissive than "600", this is a finding. $ stat /var/lib/mongo If the owner and group are not both "mongod", this is a finding. If the file permissions are more permissive than "755", this is a finding. $ ls -l /var/lib/mongo If the owner and group of any file or sub-directory is not "mongod", this is a finding. If the permission of any file in the main directory (/var/lib/mongo) or sub-directory of (/var/lib/mongo) is more permissive than "600", this is a finding. If the permission of any sub-directory of (/var/lib/mongo) is more permissive than "700", this is a finding.

## Group: SRG-APP-000251-DB-000160

**Group ID:** `V-265929`

### Rule: MongoDB must check the validity of all data inputs except those specifically identified by the organization.

**Rule ID:** `SV-265929r1028804_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Invalid user input occurs when a user inserts data or characters into an application's data entry fields and the application is unprepared to process that data. This results in unanticipated application behavior, potentially leading to an application or information system compromise. Invalid user input is one of the primary methods employed when attempting to compromise an application. With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. Even when no such hijacking takes place, invalid input that gets recorded in the database, whether accidental or malicious, reduces the reliability and usability of the system. Available protections include data types, referential constraints, uniqueness constraints, range checking, and application-specific logic. Application-specific logic can be implemented within the database in stored procedures and triggers, where appropriate. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
As a client program assembles a query in MongoDB, it builds a BSON object, not a string. Thus traditional SQL injection attacks are not a problem. However, MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. To check, run the following command from the MongoDB shell: > db.col.find({ $where: "return true;"} ) If the response does not return an error, this is a finding. If javascript has been correctly disabled, the correct error would indicate that the javascript global engine has been disabled. For example: MongoServerError: no globalScriptEngine in $where parsing}

## Group: SRG-APP-000251-DB-000391

**Group ID:** `V-265930`

### Rule: MongoDB and associated applications must reserve the use of dynamic code execution for situations that require it.

**Rule ID:** `SV-265930r1028805_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>With respect to database management systems, one class of threat is known as SQL Injection, or more generally, code injection. It takes advantage of the dynamic execution capabilities of various programming languages, including dialects of SQL. In such cases, the attacker deduces the manner in which SQL statements are being processed, either from inside knowledge or by observing system behavior in response to invalid inputs. When the attacker identifies scenarios where SQL queries are being assembled by application code (which may be within the database or separate from it) and executed dynamically, the attacker is then able to craft input strings that subvert the intent of the query. Potentially, the attacker can gain unauthorized access to data, including security settings, and severely corrupt or destroy the database. The principal protection against code injection is not to use dynamic execution except where it provides necessary functionality that cannot be used otherwise. Use strongly typed data items rather than general-purpose strings as input parameters to task-specific, precompiled stored procedures and functions (and triggers). This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. Satisfies: SRG-APP-000251-DB-000391, SRG-APP-000251-DB-000392</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB operations permit arbitrary JavaScript expressions to be run directly on the server. If the following parameter is not present or not set as show below in the MongoDB configuration file (default location: /etc/mongod.conf), this is a finding. security: javascriptEnabled: false

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-265931`

### Rule: MongoDB must provide nonprivileged users with error messages that provide information necessary for corrective actions without revealing information that could be exploited by adversaries.

**Rule ID:** `SV-265931r1028807_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any DBMS or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages need to be carefully considered by the organization and development team. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, usernames, and other system information not required for troubleshooting but very useful to someone targeting the system. Carefully consider the structure/content of error messages. The extent to which information systems are able to identify and handle error conditions is guided by organizational policy and operational requirements. Information that could be exploited by adversaries includes, for example, logon attempts with passwords entered by mistake as the username, mission/business information that can be derived from (if not stated explicitly by) information recorded, and personal information, such as account numbers, social security numbers, and credit card numbers. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check custom application code to verify that error messages do not contain information beyond what is needed for troubleshooting the issue. If custom application error messages contain PII data, sensitive business data, or information useful for identifying the host system or database structure, this is a finding. For example, when attempting to log in using the MongoDB shell with incorrect client credentials, the user will receive a generic error message that the authentication failed regardless of whether the user exists. If a user is attempting to perform an operation using the MongoDB shell for which they do not have privileges, MongoDB will return a generic error message that the operation is not authorized. To prevent too much information being displayed in the MongoDB logfiles, run the following command: > db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.security.redactClientLogData If the command does not return true, this is a finding.

## Group: SRG-APP-000267-DB-000163

**Group ID:** `V-265932`

### Rule: MongoDB must reveal detailed error messages only to the information system security officer (ISSO), information system security manager (ISSM), system administrator (SA), and database administrator (DBA).

**Rule ID:** `SV-265932r1028808_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If MongoDB provides too much information in error logs and administrative messages to the screen, this could lead to compromise. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements. Some default DBMS error messages can contain information that could aid an attacker in, among other things, identifying the database type, host address, or state of the database. Custom errors may contain sensitive customer information. It is important that detailed error messages be visible only to those who are authorized to view them; that general users receive only generalized acknowledgment that errors have occurred; and that these generalized messages appear only when relevant to the user's task. For example, a message along the lines of, "An error has occurred. Unable to save your changes. If this problem persists, contact your help desk" would be relevant. A message such as "Warning: your transaction generated a large number of page splits" would likely not be relevant. Administrative users authorized to review detailed error messages typically are the ISSO, ISSM, SA, and DBA. Other individuals or roles may be specified according to organization-specific needs, with appropriate approval. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A mongod or mongos running with "security.redactClientLogData:true" redacts any message accompanying a given log event before logging. This prevents the mongod or mongos from writing potentially sensitive data stored on the database to the diagnostic log. Metadata such as error or operation codes, line numbers, and source file names are still visible in the logs. To prevent too much information being displayed in the MongoDB logfiles, run the following command: > db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.security.redactClientLogData If the command does not return true, this is a finding. The MongoDB command "getLog" will return data from the log file, which requires the "getLog" action type on the cluster resource. Ensure that application users are not authorized to execute this command. To validate this run the following command on the name of the application user to view actions its permitted to perform on the cluster resource: > db.runCommand({usersInfo: "<USER NAME>", showPrivileges: 1}).users[0].inheritedPrivileges.filter(privilege => privilege.resource.cluster) If "getLog" appears in the list of actions, this is a finding.

## Group: SRG-APP-000295-DB-000305

**Group ID:** `V-265933`

### Rule: The DBMS must automatically terminate a user session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-265933r1028585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination ends all processes associated with a user's logical session except those batch processes/jobs that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific cases where the system owner, data owner, or organization requires additional assurance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation to obtain the organization's definition of circumstances requiring automatic session termination. If the documentation explicitly states that such termination is not required or is prohibited, this is not a finding. If the system owner, data owner, or organization requires additional assurance, this is a finding.

## Group: SRG-APP-000311-DB-000308

**Group ID:** `V-265934`

### Rule: MongoDB must associate organization-defined types of security labels having organization-defined security label values with information in storage.

**Rule ID:** `SV-265934r1028811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the association of security labels to information, there is no basis for MongoDB to make security-related access-control decisions. Security labels are abstractions representing the basic properties or characteristics of an entity (e.g., subjects and objects) with respect to safeguarding information. These labels are typically associated with internal data structures (e.g., tables, rows) within the database and are used to enable the implementation of access control and flow control policies, reflect special dissemination, handling, or distribution instructions, or support other aspects of the information security policy. One example includes marking data as classified or CUI. These security labels may be assigned manually or during data processing, but, either way, it is imperative these assignments are maintained while the data is in storage. If the security labels are lost when the data is stored, there is the risk of a data compromise. The mechanism used to support security labeling may be a feature of MongoDB product, a third-party product, or custom application code. Satisfies: SRG-APP-000311-DB-000308, SRG-APP-000313-DB-000309, SRG-APP-000314-DB-000310</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If security labeling is not required, this is not a finding. If security labeling is required then there must be an organizational or site specific documentation on what the security labeling policy is and guidance on how and where to apply it. Review the organization- or site-specific security labeling documentation to understand how documents in specific MongoDB collection(s) must be marked. This marking process should be applied as data is entered into the database. Upon review of the security labeling documents, the following checks will be required. 1. Check if the role "SLTagViewer" exists. If this role does not exist, this is a finding. Note: The role name "SLTagViewer" is a user-defined (custom) role and is organizational or site specific. The role name of "SLTagViewer" is used here as an example. Run the following commands: > use admin > db.getRole( "SLTagViewer", { showPrivileges: true } ) If the results returned from this command is "null", this is a finding. 2. Check that data is appropriately marked in the specific MongoDB collection(s) that require security labeling. This check will be specific to the security labeling policy and guidance. Log in to MongoDB with a user that has a Security Label Tag Viewer role ("SLTagViewer", which is a role that has been created and has access to read/view those database/collections that require security labels). Review the data in the MongoDB collections requiring security labels to ensure that the data is appropriately marked according to the security labeling documentation. For example, if documents in a MongoDB collection need to be marked as "TS", "S", "C" or "U" (or combination of) at the root level of the document and at each field level of the document, then the security labeling policy and guidance would indicate a document might look like the following and this would not be a finding ("sl" is the security label): { "_id": 1, "sl": [["TS"], ["S"]], "field1" : { "sl" : [ ["S"] ], "data" : "field1 value" }, "field2" : { "sl" : [ ["TS"] ], "data" : "field2 value" }, "field3" : { "sl" : [ ["S"] ], "data" : "field3 value" } } The following document would be a finding because at the field level, field2 is missing its security label of "sl": { "_id": 1, "sl": [["TS"], ["S"]], "field1" : { "sl" : [ ["S"] ], "data" : "field1 value" }, "field2" : { "data" : "field2 value" }, "field3" : { "sl" : [ ["S"] ], "data" : "field3 value" } } 3. Check that queries against that data in those collections use an appropriately constructed MongoDB $redact operation as part of the query pipeline to ensure that only the data appropriate for the query (that meets the security label requirements) is returned. Ensure that any query that targets the databases/collections that have security labeling have the appropriate MongoDB $redact operation applied. This is done through trusted middleware. This trusted middleware configuration is purpose built (custom) code and integrations and is organizational or site specific. Information on the basics of this can be found here: https://www.mongodb.com/docs/v7.0/reference/operator/aggregation/redact/ Any queries that target a MongoDB database/collection that has security labels and pass through the trusted middleware and does not have an appropriately constructed $redact operator that is part of the query aggregation pipeline is a finding. The following is an example of the $redact operator for the example document: > db.security_collection.aggregate( [{ $redact: { $cond: [{ $anyElementTrue: { $map: { input: "$sl", as: "setNeeded", in: { $setIsSubset: ["$$setNeeded", ["S"]] } } } }, "$$DESCEND", "$$PRUNE"] } } ] )

## Group: SRG-APP-000328-DB-000301

**Group ID:** `V-265935`

### Rule: MongoDB must enforce discretionary access control (DAC) policies, as defined by the data owner, over defined subjects and objects.

**Rule ID:** `SV-265935r1031272_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAC is based on the notion that individual users are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled table permissions. When DAC policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control (MAC) policies is still able to operate under the less rigorous constraints of this requirement. Thus, while MAC imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MongoDB Configuration file (default location: /etc/mongod.conf). If the file does not contain the following entry, this is a finding: security: authorization: enabled

## Group: SRG-APP-000340-DB-000304

**Group ID:** `V-265936`

### Rule: MongoDB must prevent nonprivileged users from executing privileged functions, to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-265936r1028813_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. System documentation should include a definition of the functionality considered privileged. Depending on circumstances, privileged functions can include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals that do not possess appropriate authorizations. Circumventing intrusion detection and prevention mechanisms or malicious code protection mechanisms are examples of privileged functions that require protection from nonprivileged users. A privileged function in the DBMS/database context is any operation that modifies the structure of the database, its built-in logic, or its security settings. This would include all Data Definition Language (DDL) statements and all security-related statements. In a MongoDB environment, it encompasses, but is not necessarily limited to: createCollection() dropCollection() grantRolesToUsers() revokeRolesFromUsers() There may also be Data Manipulation Language (DML) statements that, subject to context, should be regarded as privileged. Possible examples include: deleteOne(), deleteMany() updateOne(), updateMany() any find(), insertXXX(), updateXXX(), deleteXXX() to an application-defined security table executed by other than a security principal. Depending on the capabilities of the DBMS and the design of the database and associated applications, the prevention of unauthorized use of privileged functions may be achieved by means of DBMS security features, database triggers, other mechanisms, or a combination of these.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
A organizational or site-specific document should exist and be reviewed to determine what built-in MongoDB roles and associated privileges may be considered authorized and what users are administrative users. For each database, run the following commands in MongoDB as an administrative user to determine what users and roles they are assigned: > use <database> > db.getUsers() For any nonadministrative user in a database, check if any roles are not compliant with the site-specific documentation for users. If any nonadministrative user in a database has a noncompliant role, this is a finding.

## Group: SRG-APP-000357-DB-000316

**Group ID:** `V-265938`

### Rule: MongoDB must allocate audit record storage capacity in accordance with site audit record storage requirements.

**Rule ID:** `SV-265938r1028600_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure sufficient storage capacity for the audit logs, MongoDB must be able to allocate audit record storage capacity. Although another requirement (SRG-APP-000515-DB-000318) mandates that audit data be off-loaded to a centralized log management system, it remains necessary to provide space on the database server to serve as a buffer against outages and capacity limits of the off-loading mechanism. The task of allocating audit record storage capacity is usually performed during initial installation of MongoDB and is closely associated with the DBA and system administrator roles. The DBA or system administrator will usually coordinate the allocation of physical drive space with the application owner/installer and the application will prompt the installer to provide the capacity information, the physical location of the disk, or both. In determining the capacity requirements, consider such factors as: total number of users; expected number of concurrent users during busy periods; number and type of events being monitored; types and amounts of data being captured; the frequency/speed with which audit records are off-loaded to the central log management system; and any limitations that exist on MongoDB's ability to reuse the space formerly occupied by off-loaded records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Investigate whether there have been any incidents where the MongoDB server ran out of audit log space since the last time the space was allocated or other corrective measures were taken. If these conditions exist, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-265939`

### Rule: MongoDB must provide a warning to appropriate support staff when allocated audit record storage volume reaches 75 percent of maximum audit record storage capacity.

**Rule ID:** `SV-265939r1028603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations are required to use a central log management system, so, under normal conditions, the audit space allocated to MongoDB on its own server will not be an issue. However, space will still be required on MongoDB server for audit records in transit, and, under abnormal conditions, this could fill up. Since a requirement exists to halt processing upon audit failure, a service outage would result. If support personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. The appropriate support staff include, at a minimum, the information system security officer (ISSO) and the database administrator (DBA)/system administrator (SA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that auditing is enabled in the mongodb configuration file (default location: /etc/mongod.conf) and view the "auditlog.path" to identify the storage volume. Verify that OS or other organization approved third-party monitoring software is installed. Verify that the required alert in the monitoring software to send an alert where storage volume holding the auditLog file utilization reaches 75 percent. If appropriate support staff are not notified immediately upon storage volume utilization reaching 75 percent, this is a finding.

## Group: SRG-APP-000360-DB-000320

**Group ID:** `V-265940`

### Rule: MongoDB must provide an immediate real-time alert to appropriate support staff of all audit log failures.

**Rule ID:** `SV-265940r1028815_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. The appropriate support staff include, at a minimum, the information system security officer (ISSO) and the database administrator (DBA)/system administrator (SA). A failure of database auditing will result in either the database continuing to function without auditing or in a complete halt to database operations. When audit processing fails, appropriate personnel must be alerted immediately to avoid further downtime or unaudited transactions. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB database halts if it cannot write audit events to the audit log due to insufficient storage on the volume where the audit log is being written. Check the operating system or third-party logging software settings to determine whether a real-time alert will be sent to the appropriate personnel when the volume hosting the MongoDB audit log is nearing capacity. If real-time alerts are not set up to monitor the remaining storage capacity of the volume hosting the MongoDB audit logs, this is a finding.

## Group: SRG-APP-000378-DB-000365

**Group ID:** `V-265941`

### Rule: MongoDB must prohibit user installation of logic modules (stored procedures, functions, triggers, views, etc.) without explicit privileged status.

**Rule ID:** `SV-265941r1028609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software without explicit privileges creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceed the rights of a regular user. DBMS functionality and the nature and requirements of databases will vary; so while users are not permitted to install unapproved software, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The requirements for production servers will be more restrictive than those used for development and research. MongoDB must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization. In the case of a database management system, this requirement covers stored procedures, functions, triggers, views, etc.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB supports only software development, experimentation and/or developer-level testing (that is, excluding production systems, integration testing, stress testing, and user acceptance testing), this is not a finding. MongoDB can control nonadministrative users' ability to create, alter, or replace logic modules by defining specific roles and permissions. While MongoDB does not directly support stored procedures, functions, triggers, and views in the way relational databases do, similar functionalities can be implemented using various features. A organizational- or site-specific document should exist and be reviewed to determine what built-in MongoDB roles and associated privileges may be considered authorized and what users are administrative users. For each database, run the following commands in MongoDB as an administrative user to determine what users and roles they are assigned: > use <database> > db.getUsers() For any nonadministrative user in a database, check if any roles are not compliant with the site-specific documentation for users. If any user in any database is found to have a role that is not allowed, this is a finding. MongoDB allows users to store JavaScript functions on the server. Javascript should be disabled for all users. Review the Mongodb configuration file (default location: /etc/mongod.conf) and ensure the following is set to disable JavaScript: security: javascriptEnabled: false If this is not set in the MongoDB configuration file, this is a finding.

## Group: SRG-APP-000380-DB-000360

**Group ID:** `V-265942`

### Rule: MongoDB must enforce access restrictions associated with changes to the configuration of MongoDB or database(s).

**Rule ID:** `SV-265942r1028817_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to system components for the purposes of initiating changes, including upgrades and modifications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that authentication and Role-Based Access Controls (RBAC) is configured correctly and restrictions are being enforced, create a test user and a custom role, and then confirm expected operations: Once authenticated as a DBA administrator, use db.createUser() to create an additional user. The following operation adds a user "myTester" to the test database who has read-only access on the test database: > use test > db.createUser( { user: "myTester", pwd: <password>, roles: [ { role: "read", db: "test" } ] } ) Log out and then back in as the "test" database user. Issue the following to attempt to write to the test database with a read-only privilege: > use test > db.testCollection.insertOne( { x: 1 } ) This operation will fail with an error similar to the following: "MongoServerError":"not authorized on test to execute command"{ "insert":"testCollection", "documents":[ { "x":1, "_id":"ObjectId(""6500b96d1114d3a3ba7dda39"")" } ], "ordered":true, "lsid":{ "id":"UUID(""6cb3b9af-1ddc-446c-b0e0-bc9bf22807fa"")" }, "$db":"test" } If the operation does not fail, this is a finding.

## Group: SRG-APP-000383-DB-000364

**Group ID:** `V-265943`

### Rule: The DBMS must disable network functions, ports, protocols, and services deemed by the organization to be nonsecure, in accord with the Ports, Protocols, and Services Management (PPSM) guidance.

**Rule ID:** `SV-265943r1028615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of nonsecure network functions, ports, protocols, and services exposes the system to avoidable threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network functions, ports, protocols, and services supported by the DBMS. If any protocol is prohibited by the PPSM guidance and is enabled, this is a finding.

## Group: SRG-APP-000416-DB-000380

**Group ID:** `V-265945`

### Rule: MongoDB must use NSA-approved cryptography to protect classified information in accordance with the data owner's requirements.

**Rule ID:** `SV-265945r1028621_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. It is the responsibility of the data owner to assess the cryptography requirements in light of applicable federal laws, Executive Orders, directives, policies, regulations, and standards. NSA-approved cryptography for classified networks is hardware based. This requirement addresses the compatibility of a DBMS with the encryption devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If MongoDB is deployed in an unclassified environment, this is not a finding. Run the following command as an administrative user: > db.getSiblingDB("admin").runCommand({getCmdLineOpts: 1}).parsed.net.tls.FIPSMode If the output is not "true", this is a finding.

## Group: SRG-APP-000427-DB-000385

**Group ID:** `V-265946`

### Rule: MongoDB must only accept end entity certificates issued by DOD PKI or DOD-approved PKI Certification Authorities (CAs) for the establishment of all encrypted sessions.

**Rule ID:** `SV-265946r1028723_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only DOD-approved external PKIs have been evaluated to ensure that they have security controls and identity vetting procedures in place which are sufficient for DOD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DOD-approved PKIs is published at https://public.cyber.mil/pki-pke/. This requirement focuses on communications protection for MongoDB session rather than for the network packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To run MongoDB in TLS mode, obtain a valid certificate singed by a single CA. Before starting the MongoDB database in TLS mode, verify the certificate used is issued by a valid DOD CA (openssl x509 -in <path_to_certificate_pem_file> -text | grep -i "issuer"). The certificates (pem files) used by MongoDB will be in the MongoDB configuration file net.tls section as shown below (default location: /etc/mongod.conf). Each of these must be inspected, when present, to make sure they comply with a DOD Issuer for the certificate. net: tls: CAFile: <PEM file> certificateKeyFile: <PEM file> clusterFile: <PEM file> clusterCAFile: <PEM file> CRLFile: <PEM file> When using MongoDBs native encryption at rest, the following must also be inspected in the security.kmip section of the MongoDB configuration file: security: kmip: clientCertificateFile: <PEM file> serverCAFile: <PEM file> net.tls.CAFile The .pem file that contains the root certificate chain from the CA. Specify the file name of the .pem file using relative or absolute paths. net.tls.certificateKeyFile The .pem file that contains both the TLS certificate and key. net.tls.clusterFile The .pem file that contains the x.509 certificate-key file for membership authentication for the cluster or replica set. If there is any issuer present in the certificates being used that is not a DOD approved certificate authority, this is a finding. net.tls.clusterCAFile The .pem file that contains the root certificate chain from the CA used to validate the certificate presented by a client establishing a connection. Specify the file name of the .pem file using relative or absolute paths. net.tls.clusterCAFile requires that net.tls.CAFile is set. net.tls.CRLFile The .pem file that contains the Certificate Revocation List. Specify the file name of the .pem file using relative or absolute paths. security.kmip.clientCertificateFile Path to the .pem file used to authenticate MongoDB to the KMIP server. The specified .pem file must contain both the TLS/SSL certificate and key. security.kmip.serverCAFile Path to CA File. Used for validating secure client connection to KMIP server.

## Group: SRG-APP-000428-DB-000386

**Group ID:** `V-265947`

### Rule: MongoDB must implement cryptographic mechanisms to prevent unauthorized modification of organization-defined information at rest (to include, at a minimum, PII and classified information) on organization-defined information system components.

**Rule ID:** `SV-265947r1028627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DBMSs handling data requiring "data at rest" protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. These cryptographic mechanisms may be native to MongoDB or implemented via additional software or operating system/file system settings, as appropriate to the situation. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). The decision whether and what to encrypt rests with the data owner and is also influenced by the physical measures taken to secure the equipment and media on which the information resides. Satisfies: SRG-APP-000428-DB-000386, SRG-APP-000429-DB-000387</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation or specification for the organization-defined information. If any data is PII, classified, or is deemed by the organization the need to be encrypted at rest, verify the method of encryption is documented. If no documented mechanism is being used encrypt data at rest such as hardware encryption, volume encryption, filesystem encryption or the use of third-party products to enable encryption at rest, this is a finding. If the documented method to encrypt MongoDB data at rest is the native MongoDB encryption at rest, verify the MongoDB configuration file (default location: /etc/mongod.conf) contains the following options: security: kmip: keyIdentifier: <string> rotateMasterKey: <boolean> serverName: <string> port: <string> clientCertificateFile: <string> clientCertificatePassword: <string> clientCertificateSelector: <string> serverCAFile: <string> connectRetries: <int> connectTimeoutMS: <int> activateKeys: <boolean> keyStatePollingSeconds: <int> If these above options are not configured in the MongoDB security.kmip section in the MongoDB configuration file, this is a finding.

## Group: SRG-APP-000441-DB-000378

**Group ID:** `V-265948`

### Rule: MongoDB must maintain the confidentiality and integrity of information during preparation for transmission.

**Rule ID:** `SV-265948r1028630_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during preparation for transmission, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, MongoDB, associated applications, and infrastructure must leverage transmission protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If such a requirement is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: tls: mode: requireTLS certificateKeyFile: <PEM File> CAFile: <PEM File> allowInvalidCertificates: false allowConnectionsWithoutCertificates: false FIPSMode: true If net.tls.mode is not set to "requireTLS", this is a finding.

## Group: SRG-APP-000442-DB-000379

**Group ID:** `V-265949`

### Rule: MongoDB must maintain the confidentiality and integrity of information during reception.

**Rule ID:** `SV-265949r1028633_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information can be either unintentionally or maliciously disclosed or modified during reception, including, for example, during aggregation, at protocol transformation points, and during packing/unpacking. These unauthorized disclosures or modifications compromise the confidentiality or integrity of the information. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When receiving data, MongoDB, associated applications, and infrastructure must leverage protection mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the data owner does not have a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process, this is not a finding. If such a requirement is present, inspect the MongoDB configuration file (default location: /etc/mongod.conf) for the following entries: net: tls: mode: requireTLS certificateKeyFile: <PEM File> CAFile: <PEM File> allowInvalidCertificates: false allowConnectionsWithoutCertificates: false FIPSMode: true If net.tls.mode is not set to "requireTLS", this is a finding.

## Group: SRG-APP-000447-DB-000393

**Group ID:** `V-265950`

### Rule: When invalid inputs are received, MongoDB must behave in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-265950r1028819_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability is unplanned behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs, where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This calls for inspection of application source code, which will require collaboration with the application developers. It is recognized that in many cases, the database administrator (DBA) is organizationally separate from the application developers, and may have limited, if any, access to source code. Nevertheless, protections of this type are so important to the secure operation of databases that they must not be ignored. At a minimum, the DBA must attempt to obtain assurances from the development organization that this issue has been addressed and must document what has been discovered. MongoDB schema validation allows database administrators to create rules at the collection level for fields, specifying allowed data types and value ranges. This is distinct from application-level checks and input validation. It is particularly important in MongoDB due to its flexible schema model, which allows documents in a collection to have different fields and data types by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
When an application requires specific fields to be validated at the collection level, MongoDB's schema validation ensures that there are no unintended schema changes or improper data types for those fields. Refer to the application's guidelines and documentation. If there is no requirement for collection-level schema validation for specific fields, this is not a finding. If the application's guidelines and documentation require collection-level schema validation for a specific collection on specific fields, follow these steps: 1. As a user with the "dbAdminAnyDatabase" role, run the following commands for each database that contains collections used by the application: use <database> db.getCollectionInfos() This returns an array of documents containing information about all collections within "<database>". 2. For each specific collection (identified by the "name:" field in the output) used by the application that requires a schema validation, check the "options" sub-document for that collection. 3. If the "options" sub-document for that specific collection does not contain a "validator" sub-document, this is a finding. Below shows an example output of a collection named "testCollectionWithValidator" (indicated by "name" field) with a "validator" in the "options" sub-document: [ { name: 'testCollectionWithValidator', type: 'collection', options: { validator: { '$jsonSchema': { bsonType: 'object', required: [ 'username', 'password' ], properties: { username: { bsonType: 'string', minLength: 3, description: 'must be a string and is required with a minimum length of 3 characters' }, password: { bsonType: 'string', minLength: 8, description: 'must be a string and is required with a minimum length of 8 characters' } } } }, validationLevel: 'strict', validationAction: 'error' }, info: { readOnly: false, uuid: UUID('cf0629c2-7355-4bf8-a44b-54b9f31e4845') }, idIndex: { v: 2, key: { _id: 1 }, name: '_id_' } } ] If the "options" sub-document contains a "validator", verify it against the application guidelines and documentation. Ensure the validator checks for the presence of all fields specified in the application guidelines and documentation needing a collection level validation and confirm that the correct data types and/or ranges are being validated. If any fields specified in the application guidelines or documentation are missing from the validator, or if present and the fields do not have the correct data types and/or ranges, this is a finding.

## Group: SRG-APP-000454-DB-000389

**Group ID:** `V-265951`

### Rule: When updates are applied to MongoDB software, any software components that have been replaced or made unnecessary must be removed.

**Rule ID:** `SV-265951r1028639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Previous versions of DBMS components that are not removed from the information system after updates have been installed may be exploited by adversaries. Some DBMSs' installation tools may remove older versions of software automatically from the information system. In other cases, manual review and removal will be required. In planning installations and upgrades, organizations must include steps (automated, manual, or both) to identify and remove the outdated modules. A transition period may be necessary when both the old and the new software are required. This should be taken into account in the planning.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command and observe the output. This command will determine if MongoDB has been installed with a package Manager (RedHat) and display what version is currently installed: > rpm -q mongodb-enterprise-server.x86_64 mongodb-enterprise-server-7.0.8-1.el8.x86_64 The output of the command above indicates that MongoDB Enterprise Server has been installed with a package manager. In the preceding output is an example showing that MongoDB Enterprise Server Version 7.0.8 is installed. The specific version will be dependent on the actual version installed. Upgrading MongoDB with the same package manager used for installation will overwrite or remove files as part of the upgrade process. If MongoDB was installed with a Package Manager (YUM/RPM for RedHat) then this is not a finding. Run the following command and observe the output. > rpm -q mongodb-enterprise-server.x86_64 package mongodb-enterprise-server.x86_64 is not installed The output of the command above indicates that MongoDB has not been installed via a package manager or may not have been installed at all. If MongoDB has not been installed with a Package Manger (YUM/RPM for RedHat), this is a finding.

## Group: SRG-APP-000456-DB-000400

**Group ID:** `V-265952`

### Rule: MongoDB products must be a supported version.

**Rule ID:** `SV-265952r1028821_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unsupported commercial and database systems should not be used because fixes to newly identified bugs will not be implemented by the vendor. The lack of support can result in potential vulnerabilities. Systems at unsupported servicing levels or releases will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. When maintenance updates and patches are no longer available, the database software is no longer considered supported and should be upgraded or decommissioned.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the current version of MongoDB running on the system. Run the following command from the OS command line and review the "db version" listed in the output: $ mongod --version | grep "db version" Compare the version from the output to the supported version matrix here: https://www.mongodb.com/support-policy/lifecycles If the version output in the above command has reached its "End of Life Date" shown in the matrix, this is a finding.

## Group: SRG-APP-000515-DB-000318

**Group ID:** `V-265953`

### Rule: MongoDB must off-load audit data to a separate log management facility; this must be continuous and in near real time for systems with a network connection to the storage facility and weekly or more often for standalone systems.

**Rule ID:** `SV-265953r1028645_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The DBMS may write audit records to database tables, to files in the file system, to other kinds of local repository, or directly to a centralized log management system. Whatever the method used, it must be compatible with off-loading the records to the centralized system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MongoDB relies on the underlying operating system to allocate storage capacity for audit logs and as such, does not enforce arbitrary file size limits on audit logs. System administrators should confirm that the recommended centralized system logging has been enabled (e.g., syslog on Linux systems) in the /etc/mongod.conf configuration file. For example, on a Linux-based system using syslog which is mirrored to an off-server centralized location, confirm that the MongdoDB configuration file (default location: /etc/mongod.conf) contains a properly configured auditLog such as follows: auditLog: destination: syslog If the auditLog entry is missing, or the destination does not reflect the intended application location, this is a finding. Investigate whether there have been any incidents where MongoDB ran out of audit log space since the last time the space was allocated or other corrective measures were taken.

## Group: SRG-APP-000516-DB-000363

**Group ID:** `V-265954`

### Rule: MongoDB must be configured in accordance with the security configuration settings based on DOD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, DTMs, and IAVMs.

**Rule ID:** `SV-265954r1028648_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring MongoDB to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DOD that reflects the most restrictive security posture consistent with operational requirements. In addition to this SRG, sources of guidance on security and information assurance exist. These include NSA configuration guides, CTOs, DTMs, and IAVMs. MongoDB must be configured in compliance with guidance from all such relevant sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MongoDB documentation and configuration to determine if the DBMS is configured in accordance with DOD security configuration and implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs and IAVMs. If MongoDB is not configured in accordance with security configuration settings, this is a finding.

## Group: SRG-APP-000456-DB-000390

**Group ID:** `V-265972`

### Rule: Security-relevant software updates to MongoDB must be installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-265972r1028826_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications, including database management systems, are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the organizational or site-specific software update policy and verify that MongoDB has been updated consistent with the time frame specified by that policy. The current patch release versions of MongoDB 7.0.x can be found here: https://www.mongodb.com/docs/manual/release-notes/7.0/ This link will show the patch release versions with the date of release for all of MongoDB 7.0.x. If MongoDB has not been updated to the necessary major and minor release in accordance with the policy this is a finding.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-265973`

### Rule: MongoDB must limit the total number of concurrent connections to the database.

**Rule ID:** `SV-265973r1028715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a DBMS. Unlimited concurrent connections to the DBMS could allow a successful denial-of-service (DoS) attack by exhausting connection resources; and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. This requirement addresses concurrent session control for a single account. It does not address concurrent sessions by a single user via multiple system accounts; and it does not deal with the total number of sessions across all accounts. The capability to limit the number of concurrent sessions per user must be configured in or added to the DBMS (for example, by use of a logon trigger), when this is technically feasible. Note that it is not sufficient to limit sessions via a web server or application server alone, because legitimate users and adversaries can potentially connect to the DBMS by other means. The organization will need to define the maximum number of concurrent sessions by account type, by account, or a combination thereof. In deciding on the appropriate number, it is important to consider the work requirements of the various types of users. For example, 2 might be an acceptable limit for general users accessing the database via an application; but 10 might be too few for a database administrator using a database management GUI tool, where each query tab and navigation pane may count as a separate session. (Sessions may also be referred to as connections or logons, which for the purposes of this requirement are synonyms.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Mongo can limit the total number of connections. Verify that the MongoDB configuration file (default location: /etc/mongod.conf) contains the following: net: maxIncomingConnections: %int% If this parameter is not present, or the OS is not utilized to limit connections, this is a finding.

