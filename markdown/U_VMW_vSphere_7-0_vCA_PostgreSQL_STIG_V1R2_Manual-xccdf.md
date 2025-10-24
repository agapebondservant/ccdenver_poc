# STIG Benchmark: VMware vSphere 7.0 vCenter Appliance PostgreSQL Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-DB-000031

**Group ID:** `V-256591`

### Rule: VMware Postgres must limit the number of connections.

**Rule ID:** `SV-256591r887559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management includes the ability to control the number of users and user sessions utilizing a database management system (DBMS). Unlimited concurrent connections to the DBMS could allow a successful denial-of-service (DoS) attack by exhausting connection resources, and a system can also fail or be degraded by an overload of legitimate users. Limiting the number of concurrent sessions per user is helpful in reducing these risks. VMware Postgres as deployed on the vCenter Service Appliance (VCSA) comes preconfigured with a "max_connections" limit that is appropriate for all tested, supported scenarios. The out-of-the-box configuration is dynamic, based on a lower limit plus allowances for the resources assigned to VCSA and the deployment size. However, this number will always be between 100 and 1000 (inclusive).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW max_connections;" If the returned number is not greater than or equal to 100 and less than or equal to 1000, this is a finding.

## Group: SRG-APP-000089-DB-000064

**Group ID:** `V-256592`

### Rule: VMware Postgres log files must contain required fields.

**Rule ID:** `SV-256592r887562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. As an embedded database that is only accessible via "localhost", VMware Postgres on the vCenter Server Appliance (VCSA) does not implement robust auditing. However, it can and must be configured to log reasonable levels of information relating to user actions to enable proper troubleshooting. Satisfies: SRG-APP-000089-DB-000064, SRG-APP-000095-DB-000039, SRG-APP-000096-DB-000040, SRG-APP-000097-DB-000041, SRG-APP-000098-DB-000042, SRG-APP-000099-DB-000043, SRG-APP-000100-DB-000201, SRG-APP-000101-DB-000044, SRG-APP-000375-DB-000323</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW log_line_prefix;" Expected result: %m %c %x %d %u %r %p %l If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000090-DB-000065

**Group ID:** `V-256593`

### Rule: VMware Postgres configuration files must not be accessible by unauthorized users.

**Rule ID:** `SV-256593r887565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VMware Postgres has a few configuration files that directly control the security posture of the database management system (DBMS). Protecting these files from unauthorized access and modification is fundamental to ensuring the security of VMware Postgres. Satisfies: SRG-APP-000090-DB-000065, SRG-APP-000121-DB-000202, SRG-APP-000122-DB-000203, SRG-APP-000123-DB-000204, SRG-APP-000380-DB-000360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /storage/db/vpostgres/*conf* -xdev -type f -a '(' -not -perm 600 -o -not -user vpostgres -o -not -group vpgmongrp ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000109-DB-000321

**Group ID:** `V-256594`

### Rule: VMware Postgres must be configured to overwrite older logs when necessary.

**Rule ID:** `SV-256594r887568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without proper configuration, log files for VMware Postgres can grow without bound, filling the partition and potentially affecting the availability of the vCenter Server Appliance (VCSA). One part of this configuration is to ensure the logging subsystem overwrites, rather than appends to, any previous logs that would share the same name. This is avoided in other configuration steps, but this best practice should be followed for good measure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW log_truncate_on_rotation;" Expected result: on If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000118-DB-000059

**Group ID:** `V-256595`

### Rule: The VMware Postgres database must protect log files from unauthorized access and modification.

**Rule ID:** `SV-256595r887571_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could use to their advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from all unauthorized access. This includes read, write, copy, etc. Satisfies: SRG-APP-000118-DB-000059, SRG-APP-000119-DB-000060, SRG-APP-000120-DB-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # find /var/log/vmware/vpostgres/* -xdev -type f -a '(' -not -perm 600 -o -not -user vpostgres -o -not -group vpgmongrp ')' -exec ls -ld {} \; If any files are returned, this is a finding.

## Group: SRG-APP-000133-DB-000200

**Group ID:** `V-256596`

### Rule: All vCenter database (VCDB) tables must be owned by the "vc" user account.

**Rule ID:** `SV-256596r918971_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Within the database, object ownership implies full privileges to the owned object, including the privilege to assign access to the owned objects to other subjects. Database functions and procedures can be coded using definer's rights. This allows anyone who uses the object to perform the actions if they are the owner. If not properly managed, this can lead to privileged actions being taken by unauthorized individuals. VCDB is configured out of the box to be owned by the "vc" Postgres user. This configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -d VCDB -U postgres -t -A -c "\dt;" | grep -v 'table|vc' If any tables are returned, this is a finding. Note: Upgrades may introduce new tables that are owned by the "postgres" user and can be updated to be owned by the "vc" user.

## Group: SRG-APP-000133-DB-000362

**Group ID:** `V-256597`

### Rule: VMware Postgres must limit modify privileges to authorized accounts.

**Rule ID:** `SV-256597r887577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If VMware Postgres were to allow any user to make changes to database structure or logic, those changes might be implemented without undergoing the appropriate testing and approvals that are part of a robust change management process. Only qualified and authorized individuals must be allowed to obtain access to information system components to initiate changes, including upgrades and modifications. Unmanaged changes that occur to the database software libraries or configuration can lead to unauthorized or compromised installations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "\du;"|grep "Create" Expected result: postgres | Superuser, Create role, Create DB, Replication, Bypass RLS | {} vc | Create DB | {} vlcmuser | Create DB | {} If accounts other than "postgres","vc", and "vlcmuser" have any "Create" privileges, this is a finding.

## Group: SRG-APP-000142-DB-000094

**Group ID:** `V-256598`

### Rule: VMware Postgres must be configured to use the correct port.

**Rule ID:** `SV-256598r887580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports, protocols, and services on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. Database Management Systems using ports, protocols, and services deemed unsafe are open to attack through those ports, protocols, and services. This can allow unauthorized access to the database and through the database to other components of the information system. Satisfies: SRG-APP-000142-DB-000094, SRG-APP-000383-DB-000364</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW port;" Expected result: 5432 If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000148-DB-000103

**Group ID:** `V-256599`

### Rule: VMware Postgres must require authentication on all connections.

**Rule ID:** `SV-256599r887583_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. VMware Postgres client authentication configuration is configured in "pg_hba.conf". In this file are a number of lines that specify who can connect to the service, from where, and using what authentication methods. In Postgres there is a concept of a trusted connection where a specific network mask can connect without any authentication to any account. This connection is termed "trust" in "pg_hba.conf", and it must not be present. Out of the box, VMware Postgres requires standard password authentication for all connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # grep -v "^#" /storage/db/vpostgres/pg_hba.conf|grep -z --color=always "trust" If any lines are returned, this is a finding.

## Group: SRG-APP-000171-DB-000074

**Group ID:** `V-256600`

### Rule: The vPostgres database must use "md5" for authentication.

**Rule ID:** `SV-256600r887586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate, and requires authorizing official approval. In such cases, database passwords stored in clear text, using reversible encryption or unsalted hashes, would be vulnerable to unauthorized disclosure. Database passwords must always be in the form of one-way, salted hashes when stored internally or externally to the database management system (DBMS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW password_encryption;" Expected result: md5 If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000172-DB-000075

**Group ID:** `V-256601`

### Rule: VMware Postgres must be configured to use Transport Layer Security (TLS).

**Rule ID:** `SV-256601r887589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved public key infrastructure (PKI) certificates. Authentication based on user ID and password may be used only when it is not possible to employ a PKI certificate. In such cases, passwords, must be protected at all times, and encryption is the standard method for protecting passwords during transmission. VMware Postgres is configured out of the box to require TLS connections with remote clients. As an embedded database and available only on "localhost" for standalone vCenter Server Appliances (VCSAs), TLS connections are used only in high-availability deployments for connections between a primary and a standby. This configuration must be verified and maintained. Satisfies: SRG-APP-000172-DB-000075, SRG-APP-000442-DB-000379</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW ssl;" Expected result: on If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000176-DB-000068

**Group ID:** `V-256602`

### Rule: VMware Postgres must enforce authorized access to all public key infrastructure (PKI) private keys.

**Rule ID:** `SV-256602r887592_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The DOD standard for authentication is DOD-approved PKI certificates. PKI certificate-based authentication is performed by requiring the certificate holder to cryptographically prove possession of the corresponding private key. If a private key is stolen, an attacker can use it to impersonate the certificate holder. In cases where the database management system (DBMS)-stored private keys are used to authenticate the DBMS to the system's clients, loss of the corresponding private keys would allow an attacker to successfully perform undetected man-in-the-middle attacks against the DBMS system and its clients. All access to the private key(s) of the DBMS must be restricted to authorized and authenticated users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # stat -c "%a:%U:%G" /storage/db/vpostgres_ssl/server.key Expected result: 600:vpostgres:vpgmongrp If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000179-DB-000114

**Group ID:** `V-256603`

### Rule: VMware Postgres must use FIPS 140-2 approved Transport Layer Security (TLS) ciphers.

**Rule ID:** `SV-256603r887595_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or unvalidated cryptographic algorithms undermines the purposes of using encryption and digital signatures to protect data. Weak algorithms can be broken, and unvalidated cryptographic modules may not implement algorithms correctly. Unapproved cryptographic modules or algorithms should not be relied on for authentication, confidentiality, or integrity. Weak cryptography could allow an attacker to gain access to and modify data stored in the database as well as the administration settings of the database management system (DBMS). VMware Postgres does not currently implement FIPS-validated cryptographic modules. This is planned but, in the interim, Postgres can be configured with strong ciphers from the FIPS-140 approved suite. Additionally, as an embedded database available only on "localhost" for a standalone vCenter Server Appliance, TLS connections are used only in high-availability deployments for connections between a primary and a standby. Satisfies: SRG-APP-000179-DB-000114, SRG-APP-000514-DB-000381, SRG-APP-000514-DB-000382, SRG-APP-000514-DB-000383</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW ssl_ciphers;" Expected result: !aNULL:kECDH+AES:ECDH+AES:RSA+AES:@STRENGTH If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000226-DB-000147

**Group ID:** `V-256604`

### Rule: VMware Postgres must write log entries to disk prior to returning operation success or failure.

**Rule ID:** `SV-256604r887598_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. Preserving system state information helps to facilitate system restart and return to the operational mode of the organization with less disruption of mission/business processes. Aggregating log writes saves on performance but leaves a window for log data loss. The logging system inside VMware Postgres is capable of writing logs to disk fully and completely before the associated operation is returned to the client. This ensures database activity is always captured, even in the event of a system crash during or immediately after a given operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SELECT name,setting FROM pg_settings WHERE name IN ('fsync','full_page_writes','synchronous_commit');" Expected result: fsync | on full_page_writes | on synchronous_commit | on If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000233-DB-000124

**Group ID:** `V-256605`

### Rule: VMware Postgres must not allow schema access to unauthorized accounts.

**Rule ID:** `SV-256605r887601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Database management systems typically separate security functionality from nonsecurity functionality via separate databases or schemas. Database objects or code implementing security functionality should not be commingled with objects or code implementing application logic. When security and nonsecurity functionality are commingled, users who have access to nonsecurity functionality may be able to access security functionality. VMware Postgres contains a number of system configuration schemas for which access must be strictly limited. By default, the "pg_catalog" and "information_schema" objects are configured to only be accessible in a read-only manner publicly and otherwise only accessible by the Postgres user. This configuration must be verified and maintained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -c "\dp .*.;" |grep -E "information_schema|pg_catalog"|awk -F '|' '{print $4}'|awk -F '/' '{print $1}'|grep -v "=r" | grep -v "^[[:space:]]*$" | grep -v "postgres" If any lines are returned, this is a finding.

## Group: SRG-APP-000266-DB-000162

**Group ID:** `V-256606`

### Rule: VMware Postgres must provide nonprivileged users with minimal error information.

**Rule ID:** `SV-256606r887604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any database management system (DBMS) or associated application providing too much information in error messages on the screen or printout risks compromising the data and security of the system. The structure and content of error messages must contain the minimal amount of information. Databases can inadvertently provide a wealth of information to an attacker through improperly handled error messages. In addition to sensitive business or personal information, database errors can provide host names, IP addresses, user names, and other system information not required for troubleshooting but very useful to someone targeting the system. Satisfies: SRG-APP-000266-DB-000162, SRG-APP-000267-DB-000163</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW client_min_messages;" Expected result: notice If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000356-DB-000314

**Group ID:** `V-256607`

### Rule: VMware Postgres must have log collection enabled.

**Rule ID:** `SV-256607r887607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. VMware Postgres is capable of outputting directly to syslog but for performance reasons, the vCenter Server Appliance (VCSA) is configured to ship logs centrally via "rsyslog" file monitoring. To facilitate that configuration, log files must be generated to disk. Satisfies: SRG-APP-000356-DB-000314, SRG-APP-000356-DB-000315, SRG-APP-000092-DB-000208, SRG-APP-000381-DB-000361, SRG-APP-000495-DB-000326, SRG-APP-000495-DB-000327, SRG-APP-000495-DB-000328, SRG-APP-000495-DB-000329, SRG-APP-000496-DB-000334, SRG-APP-000496-DB-000335, SRG-APP-000499-DB-000330, SRG-APP-000499-DB-000331, SRG-APP-000501-DB-000336, SRG-APP-000501-DB-000337, SRG-APP-000504-DB-000354, SRG-APP-000504-DB-000355, SRG-APP-000507-DB-000356, SRG-APP-000507-DB-000357, SRG-APP-000508-DB-000358</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW logging_collector;" Expected result: on If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-256608`

### Rule: VMware Postgres must be configured to log to "stderr".

**Rule ID:** `SV-256608r887610_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. For VMware Postgres logs to be successfully sent to a remote log management system, log events must be sent to "stderr". Those events will be captured and logged to disk where they will be picked up by "rsyslog" for shipping.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW log_destination;" Expected result: stderr If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000359-DB-000319

**Group ID:** `V-256609`

### Rule: "Rsyslog" must be configured to monitor VMware Postgres logs.

**Rule ID:** `SV-256609r887613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For performance reasons, "rsyslog" file monitoring is preferred over configuring VMware Postgres to send events to a "syslog" facility. Without ensuring that logs are created, that "rsyslog" configs are created, and that those configs are loaded, the log file monitoring and shipping will not be effective. Satisfies: SRG-APP-000359-DB-000319, SRG-APP-000360-DB-000320, SRG-APP-000515-DB-000318</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # rpm -V VMware-Postgres-cis-visl-scripts|grep -E "vmware-services-vmware-vpostgres.conf|vmware-services-vmware-postgres-archiver.conf" | grep "^..5......" If the command returns any output, this is a finding.

## Group: SRG-APP-000374-DB-000322

**Group ID:** `V-256610`

### Rule: VMware Postgres must use Coordinated Universal Time (UTC) for log timestamps.

**Rule ID:** `SV-256610r887616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by VMware Postgres must include date and time expressed in UTC, a modern continuation of Greenwich Mean Time (GMT).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
At the command prompt, run the following command: # /opt/vmware/vpostgres/current/bin/psql -U postgres -A -t -c "SHOW log_timezone;" Expected result: Etc/UTC If the output does not match the expected result, this is a finding.

