# STIG Benchmark: Splunk Enterprise 7.x for Windows Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000514-AU-002890

**Group ID:** `V-221600`

### Rule: Splunk Enterprise must be installed with FIPS mode enabled, to implement NIST FIPS 140-2 approved ciphers for all cryptographic functions.

**Rule ID:** `SV-221600r879885_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-2 precludes the use of unvalidated cryptography for the cryptographic protection of sensitive or valuable data within Federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2 standard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the Search and Reporting App. Execute a search query using the following: | rest splunk_server=local /services/server/info | fields fips_mode Verify that the report returns fips_mode = 1. If the query returns 0, this is a finding.

## Group: SRG-APP-000148-AU-002270

**Group ID:** `V-221601`

### Rule: Splunk Enterprise must use organization level authentication to uniquely identify and authenticate users.

**Rule ID:** `SV-221601r879589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be uniquely identified and authenticated to prevent potential misuse and compromise of the system. Sharing of accounts prevents accountability and non-repudiation. Organizational users must be uniquely identified and authenticated for all accesses. The use of an organizational level authentication mechanism provides centralized management of accounts, and provides many benefits not normally leveraged by local account mechanisms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the instance being checked is in a distributed environment and has the web interface disabled, this check is N/A. Select Settings >> Access Controls >> Authentication method. Verify that LDAP or SAML is selected. If LDAP or SAML is not selected, this is a finding.

## Group: SRG-APP-000148-AU-002270

**Group ID:** `V-221602`

### Rule: Splunk Enterprise must have all local user accounts removed after implementing organizational level user management system, except for one emergency account of last resort.

**Rule ID:** `SV-221602r879589_rule`
**Severity:** high

**Description:**
<VulnDiscussion>User accounts should use an organizational level authentication mechanism such as SAML, LDAP, AD, etc., to provide centralized management. The use of local accounts should be discouraged, except for an emergency account of last resort. The use of local accounts instead of organizational level accounts creates a risk where accounts are not properly disabled or deleted when users depart or their roles change.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Users. Verify that no user accounts exist with Authentication system set to Splunk except an account of last resort. They should all be set to LDAP or SAML. If any user accounts have Authentication system set to Splunk, with the exception of one emergency account of last resort, this is a finding.

## Group: SRG-APP-000391-AU-002290

**Group ID:** `V-221605`

### Rule: Splunk Enterprise must use an SSO proxy service, F5 device, or SAML implementation to accept the DoD CAC or other smart card credential for identity management, personal authentication, and multifactor authentication.

**Rule ID:** `SV-221605r879764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as a primary component of layered protection for national security systems. If the application cannot meet this requirement, the risk may be mitigated through use of an authentication server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the instance being checked is in a distributed environment and has the web interface disabled, this check is N/A. Verify that Splunk Enterprise is configured to use the DoD CAC credential to log into the application. If it is not configured to allow the use of the DoD CAC credential, this is a finding.

## Group: SRG-APP-000156-AU-002380

**Group ID:** `V-221607`

### Rule: Splunk Enterprise must use HTTPS/SSL for access to the user interface.

**Rule ID:** `SV-221607r879597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. Anti-replay is a cryptographically based mechanism; thus, it must use FIPS-approved algorithms. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Note that the anti-replay service is implicit when data contains monotonically increasing sequence numbers and data integrity is assured. Use of DoD PKI is inherently compliant with this requirement for user and device access. Use of Transport Layer Security (TLS), including application protocols, such as HTTPS and DNSSEC, that use TLS/SSL as the underlying security protocol is also complaint. Configure the information system to use the hash message authentication code (HMAC) algorithm for authentication services to Kerberos, SSH, web management tool, and any other access method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head, which may be a separate machine in a distributed environment. If the instance being reviewed is not used as a search head, this check in N/A. Select Settings >> Server Settings >> General Settings and verify that Enable SSL in Splunk Web is set. If Enable SSL is not set, this is a finding.

## Group: SRG-APP-000439-AU-004310

**Group ID:** `V-221608`

### Rule: Splunk Enterprise must use SSL to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-221608r879810_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications must leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and this check will be N/A.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a search query in Splunk using the following: index=_internal source=*metrics.log* group=tcpin_connections | dedup hostname | table _time hostname sourceIp destPort ssl Verify that the report returns ssl = true for every item listed. If the report returns ssl = false for any item, this is a finding.

## Group: SRG-APP-000172-AU-002550

**Group ID:** `V-221609`

### Rule: Splunk Enterprise must use LDAPS for the LDAP connection.

**Rule ID:** `SV-221609r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Securing the connection to the LDAP servers mitigates this risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the instance being checked is in a distributed environment and has the web interface disabled, this check is N/A. If using SAML for authentication, this check is N/A. Select Settings >> Access Controls >> Authentication method. Select LDAP Settings. Select the LDAP strategy and verify that SSL enabled is checked and the Port is set to 636. If SSL enabled is not checked, and Port is not 636, this is a finding.

## Group: SRG-APP-000125-AU-000300

**Group ID:** `V-221612`

### Rule: Splunk Enterprise must be configured to back up the log records repository at least every seven days onto a different system or system component other than the system or component being audited.

**Rule ID:** `SV-221612r879582_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of log data includes ensuring log data is not accidentally lost or deleted. Backing up log records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to ensure that in the event of a catastrophic system failure, the log records will be retained. This helps to ensure that a compromise of the information system being audited does not also result in a compromise of the log records. This requirement only applies to applications that have a native backup capability for log records. Operating system backup requirements cover applications that do not provide native backup functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a process exists to back up the Splunk log data every seven days, using the underlying OS backup tools, or another approved backup tool. If a backup plan does not exist for the Splunk log data, this is a finding.

## Group: SRG-APP-000080-AU-000010

**Group ID:** `V-221613`

### Rule: Splunk Enterprise must be configured to protect the log data stored in the indexes from alteration.

**Rule ID:** `SV-221613r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without non-repudiation, it is impossible to positively attribute an action to an individual (or process acting on behalf of an individual). The records stored by Splunk Enterprise must be protected against alteration. A hash is one way of performing this function. The server must not allow the removal of identifiers or date/time, or it must severely restrict the ability to do so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the server being reviewed does not store index data, this check is N/A. Check the following file in the installation folder: $SPLUNK_HOME/etc/system/local/indexes.conf Verify that each organization-defined index stanza in brackets [ ] has the following line added: enableDataIntegrityControl=true If this line is missing or is set to false, this is a finding.

## Group: SRG-APP-000516-AU-000340

**Group ID:** `V-221614`

### Rule: Splunk Enterprise must use TCP for data transmission.

**Rule ID:** `SV-221614r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the UDP protocol is used for communication, then data packets that do not reach the server are not detected as a data loss. The use of TCP to transport data improves delivery reliability, adds data integrity, and gives the option to encrypt the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Data Inputs, and verify there are zero inputs configured under UDP. Splunk supports UDP, but it is not permissible to use. If any exist, this is a finding. If the Web UI is disabled, open an OS command prompt and type: netstat -a -p UDP If a UDP connection is displayed for 0.0.0.0:514, the instance is listening for Syslog port 514 in UDP, and this is a finding.

## Group: SRG-APP-000086-AU-000020

**Group ID:** `V-221621`

### Rule: Splunk Enterprise must be configured to aggregate log records from organization-defined devices and hosts within its scope of coverage.

**Rule ID:** `SV-221621r879557_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the application is not configured to collate records based on the time when the events occurred, the ability to perform forensic analysis and investigations across multiple components is significantly degraded. Centralized log aggregation must also include logs from databases and servers (e.g., Windows) that do not natively send logs using the syslog protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the site documentation that lists the scope of coverage for the instance being reviewed. Select Settings >> Data Inputs. Verify that data inputs are configured to support the scope of coverage documented for the site. If Splunk enterprise is not configured to aggregate log records from organization-defined devices and hosts within its scope of coverage, this is a finding.

## Group: SRG-APP-000090-AU-000070

**Group ID:** `V-221623`

### Rule: Splunk Enterprise must allow only the Information System Security Manager (ISSM) (or individuals or roles appointed by the ISSM) to be assigned to the Power User role.

**Rule ID:** `SV-221623r879560_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without restricting which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using LDAP: Select Settings >> Access Controls >> Authentication Method >> LDAP Settings >> Map Groups. Obtain the group name mapped to the power user role. Request from the LDAP administrator the group membership of this LDAP group, and compare to the list of individuals appointed by the ISSM. If using SAML: Select Settings >> Access Controls >> Authentication Method >> SAML Settings >> Map Groups. Obtain the group name mapped to the power user role. Request from the SAML administrator the group membership of this SAML group, and compare to the list of individuals appointed by the ISSM. If users that are not defined by the ISSM as requiring elevated rights are present in the power user role membership, this is a finding.

## Group: SRG-APP-000359-AU-000120

**Group ID:** `V-221625`

### Rule: Splunk Enterprise must be configured to send an immediate alert to the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) when allocated log record storage volume reaches 75 percent of the repository maximum log record storage capacity.

**Rule ID:** `SV-221625r879732_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75 percent they are unable to plan for storage capacity expansion. Although this may be part of the operating system function, for the enterprise events management system, this is most often a function managed through the application since it is a critical function and requires the use of a large amount of external storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following checks. If any do not comply, this is a finding. (Note that these files may exist in one of the following folders or its subfolders: $SPLUNK_HOME/etc/apps/ $SPLUNK_HOME/etc/slave-apps/) 1. Examine the file in the Splunk installation folder: $SPLUNK_HOME/etc/system/local/server.conf Locate the following setting: [diskUsage] minFreeSpace = xxxx Verify that the value is set to 25 percent of the size of the storage volume. For example, 25 percent of a 100 GB drive is 25 GB, and the value set would be 25000, as the value is in megabytes. 2. Examine the file in the Splunk installation folder: $SPLUNK_HOME/etc/system/local/health.conf Locate the following setting: [alert_action:email] disabled = 0 action.to = action.cc = Verify that the email addresses of the ISSO and SA are set to receive alerts. This email address can be a group address (example alerts@domain.com) that contains the addresses of the ISSO and SA. 3. In the Splunk console, select Settings >> Health Report Manager >> feature:disk_space. Verify Red setting is 1, and Yellow setting is 2.

## Group: SRG-APP-000360-AU-000130

**Group ID:** `V-221626`

### Rule: Splunk Enterprise must notify the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) of all audit failure events, such as loss of communications with hosts and devices, or if log records are no longer being received.

**Rule ID:** `SV-221626r879733_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit function and application operation may be adversely affected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk instance is used for Tier 2 CSSP (formerly CND-SP) or JRSS analysis, this check is N/A. Interview the SA to verify that a process exists to notify the SA and ISSO of any audit failure, such as loss of communication or logs no longer being collected. Interview the ISSO to confirm receipt of this notification. If a report does not exist to notify the SA and ISSO of audit failure events, or the ISSO does not confirm receipt of the report, this is a finding.

## Group: SRG-APP-000361-AU-000140

**Group ID:** `V-221627`

### Rule: Splunk Enterprise must notify the System Administrator (SA) or Information System Security Officer (ISSO) if communication with the host and devices within its scope of coverage is lost.

**Rule ID:** `SV-221627r879734_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system were to continue processing after audit failure, actions could be taken on the system that could not be tracked and recorded for later forensic analysis. To perform this function, some type of heartbeat configuration with all of the devices and hosts must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk instance is used for Tier 2 CSSP (formerly CND-SP) or JRSS analysis, this check is N/A. Interview the SA to verify that a process exists to notify the SA and ISSO of any audit failure, such as loss of communication or logs no longer being collected. Interview the ISSO to confirm receipt of this notification. If a report does not exist to notify the SA and ISSO of audit failure events, or the ISSO does not confirm receipt of the report, this is a finding.

## Group: SRG-APP-000516-AU-000350

**Group ID:** `V-221628`

### Rule: Splunk Enterprise must be configured to notify the System Administrator (SA) and Information System Security Officer (ISSO), at a minimum, when an attack is detected on multiple devices and hosts within its scope of coverage.

**Rule ID:** `SV-221628r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Detecting when multiple systems are showing anomalies can often indicate an attack. Notifying appropriate personnel can initiate a proper response and mitigation of the attack. Splunk can aggregate events from multiple devices and create alerts when specific events occur. Detecting similar events on multiple devices simultaneously may indicate an attack. The ability to alert and report on this activity can aid in thwarting an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a process exists to notify the SA and ISSO, at a minimum, when an attack is detected on multiple devices and hosts within its scope of coverage. Interview the ISSO to confirm receipt of this notification. If a report does not exist, or the ISSO does not confirm receipt of this report, this is a finding.

## Group: SRG-APP-000166-AU-002490

**Group ID:** `V-221629`

### Rule: Splunk Enterprise must enforce password complexity for the account of last resort by requiring that at least one upper-case character be used.

**Rule ID:** `SV-221629r879603_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Uppercase is set to greater than 0. If Uppercase is set to 0, this is a finding.

## Group: SRG-APP-000167-AU-002500

**Group ID:** `V-221630`

### Rule: Splunk Enterprise must enforce password complexity for the account of last resort by requiring that at least one lower-case character be used.

**Rule ID:** `SV-221630r879604_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Lowercase is set to greater than 0. If Lowercase is set to 0, this is a finding.

## Group: SRG-APP-000168-AU-002510

**Group ID:** `V-221631`

### Rule: Splunk Enterprise must enforce password complexity for the account of last resort by requiring that at least one numeric character be used.

**Rule ID:** `SV-221631r879605_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Numeral is set to greater than 0. If Numeral is set to 0, this is a finding.

## Group: SRG-APP-000164-AU-002480

**Group ID:** `V-221632`

### Rule: Splunk Enterprise must enforce a minimum 15-character password length for the account of last resort.

**Rule ID:** `SV-221632r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Minimum characters is set to 15 or more. If Minimum characters is less than 15, this is a finding.

## Group: SRG-APP-000169-AU-002520

**Group ID:** `V-221633`

### Rule: Splunk Enterprise must enforce password complexity for the account of last resort by requiring that at least one special character be used.

**Rule ID:** `SV-221633r879606_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Special character is set to greater than 0. If Special character is set to 0, this is a finding.

## Group: SRG-APP-000174-AU-002570

**Group ID:** `V-221634`

### Rule: Splunk Enterprise must enforce a 60-day maximum password lifetime restriction for the account of last resort.

**Rule ID:** `SV-221634r879611_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts that are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that Expiration is Enabled and Days until password expires is set to 60. If not set this way, this is a finding.

## Group: SRG-APP-000165-AU-002580

**Group ID:** `V-221635`

### Rule: Splunk Enterprise must prohibit password reuse for a minimum of five generations for the account of last resort.

**Rule ID:** `SV-221635r879602_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management and verify that History is Enabled and Password history count is set to 5 or more. If not set to 5 or more, this is a finding.

## Group: SRG-APP-000068-AU-000035

**Group ID:** `V-221931`

### Rule: Splunk Enterprise must display the Standard Mandatory DOD Notice and Consent Banner and accept user acknowledgement before granting access to the application.

**Rule ID:** `SV-221931r918482_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DOD DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." The user must acknowledge the notice before being granted access to the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head, which may be a separate machine in a distributed environment. If the instance being reviewed is not used as a search head, this check in NA. Verify that the Standard Mandatory DOD Notice and Consent Banner appears before being granted access to Splunk Enterprise. If the Standard Mandatory DOD Notice and Consent Banner is not presented, this is a finding.

## Group: SRG-APP-000427-AU-000040

**Group ID:** `V-221932`

### Rule: Splunk Enterprise must only allow the use of DoD-approved certificate authorities for cryptographic functions.

**Rule ID:** `SV-221932r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Splunk Enterprise contains built-in certificates that are common across all Splunk installations and are for initial deployment. These should not be used in any production environment. The production certificates should be stored in another location away from the Splunk default certificates, as that folder is replaced on any upgrade of the application. An example would be to use a folder named $SPLUNK_HOME/etc/system/DoDcerts under the Splunk installation root folder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the properties of the certificates used by Splunk to ensure that the Issuer is the DoD trusted CA. Check the following files for the certificates in use by Splunk. This file is located on the machine used as the search head, which may be a separate machine in a distributed environment. $SPLUNK_HOME/etc/system/local/web.conf [settings] serverCert = <path to the DoD approved certificate in PEM format> This file is located on the machine used as an indexer, which may be a separate machine in a distributed environment. $SPLUNK_HOME/etc/system/local/inputs.conf [SSL] serverCert = <path to the DoD approved certificate in PEM format> This file is located on the machine used as a forwarder, which is always a separate machine regardless of environment. $SPLUNK_HOME/etc/system/local/outputs.conf [tcpout:group1] clientCert = <path to the DoD approved certificate in PEM format> Verify each certificate listed above with the following command: openssl x509 -text -inform PEM -in <name of cert> If the certificate issuer is not a DoD trusted CA, this is a finding.

## Group: SRG-APP-000610-AU-000050

**Group ID:** `V-221933`

### Rule: Splunk Enterprise must use TLS 1.2 and SHA-2 or higher cryptographic algorithms.

**Rule ID:** `SV-221933r879898_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. To protect the integrity of the authenticator and authentication mechanism used for the cryptographic module used by the network device, the application, operating system, or protocol must be configured to use one of the following hash functions for hashing the password or other authenticator in accordance with SP 800-131Ar1: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, and SHA3-512. Splunk Enterprise, by default, is compliant with this requirement. But since the settings can be overridden, the check and fix text in this requirement is necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the Splunk installation folder, check the following files in the $SPLUNK_HOME/etc/system/local folder: (Note that these files may exist in one of the following folders or its subfolders: $SPLUNK_HOME/etc/apps/ $SPLUNK_HOME/etc/slave-apps/) inputs.conf Check for the following lines; if they do not exist, the settings are compliant. If they exist, they must match the settings below: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 outputs.conf Check for the following lines; if they do not exist, the settings are compliant. If they exist, they must match the settings below: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 server.conf Check for the following lines; if they do not exist, the settings are compliant. If they exist, they must match the settings below: sslVersions = tls1.2 sslVersionsForClient = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES128-GCM-SHA256:AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 web.conf Check for the following lines; if they do not exist, the settings are compliant. If they exist, they must match the settings below: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 Check the following file in the $SPLUNK_HOME/etc/openldap folder: ldap.conf Check for the following lines; they must match the settings below: #TLS_PROTOCOL_MIN: 3.1 for TLSv1.0, 3.2 for TLSv1.1, 3.3 for TLSv1.2. TLS_PROTOCOL_MIN 3.3 TLS_CIPHER_SUITE ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256 If any of the above settings do not match, this is a finding.

## Group: SRG-APP-000141-AU-000090

**Group ID:** `V-221934`

### Rule: When Splunk Enterprise is distributed over multiple servers, each server must be configured to disable non-essential capabilities.

**Rule ID:** `SV-221934r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications are capable of providing a wide variety of functions and services. Some of the functions and services may not be necessary to support the configuration. This becomes more of an issue in distributed environments, where the application functions are spread out over multiple servers. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk Installation is not distributed among multiple servers, this check is N/A. If the machine being reviewed is not designated as a search head, check the following file in the Splunk installation folders: $SPLUNK_HOME/etc/system/local/web.conf Check for the following lines: [settings] startwebserver = 0 If the startwebserver = 0 line is missing, or is = 1, this is a finding. If the machine being reviewed is not designated as an indexer, check the following file in the Splunk installation folders: $SPLUNK_HOME/etc/system/local/indexes.conf If this file exists, this is a finding. This file should only exist on an instance designated as an indexer.

## Group: SRG-APP-000118-AU-000100

**Group ID:** `V-221935`

### Rule: Splunk Enterprise installation directories must be secured.

**Rule ID:** `SV-221935r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, competent forensic analysis and discovery of the true source of potentially malicious system activity would be difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods, which will depend on system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-AU-000100, SRG-APP-000119-AU-000110, SRG-APP-000120-AU-000120, SRG-APP-000121-AU-000130, SRG-APP-000122-AU-000140, SRG-APP-000123-AU-000150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be done as a server administrator. From an Explorer window, right-click on the Splunk target installation folder and select Properties. Select the Security tab and then the Advanced button. Verify that Administrators and SYSTEM are the only accounts listed and are set to Full Control. If accounts other than Administrators and SYSTEM are listed, this is a finding.

## Group: SRG-APP-000516-AU-000340

**Group ID:** `V-221936`

### Rule: Splunk Enterprise forwarders must be configured with Indexer Acknowledgement enabled.

**Rule ID:** `SV-221936r879887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent the loss of data during transmission, a handshake acknowledgement between the sender and the recipient may need configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the server being reviewed is not a forwarder, this check is N/A. In the Splunk installation folder, check the following file in the $SPLUNK_HOME/etc/system/local folder: outputs.conf Locate the section similar to: [tcpout:group1] useACK=true Note that group1 may be named differently depending on how tcpout was configured. If the useACK=true statement is missing or set to false, this is a finding.

## Group: SRG-APP-000389-AU-000180

**Group ID:** `V-221937`

### Rule: Splunk Enterprise idle session timeout must be set to not exceed 15 minutes.


**Rule ID:** `SV-221937r879762_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without reauthentication, users may access resources or perform tasks for which they do not have authorization. When applications provide the capability to change security roles or escalate the functional capability of the application, it is critical the user reauthenticate. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of individuals and/or devices in other situations, including (but not limited to) the following circumstances: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) When the execution of privileged functions occurs; (v) After a fixed period of time; or (vi) Periodically. Within the DoD, the minimum circumstances requiring reauthentication are privilege escalation and role changes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Server Settings >> General Settings and verify that Session timeout is set to 15 minutes or less. If Splunk is not configured to 15 minutes or less, this is a finding.

## Group: SRG-APP-000295-AU-000190

**Group ID:** `V-221938`

### Rule: Splunk Enterprise idle session timeout must be set to not exceed 15 minutes.


**Rule ID:** `SV-221938r879673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination after a period of inactivity addresses the potential for a malicious actor to exploit the unattended session. Closing any unattended sessions reduces the attack surface to the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Server Settings >> General Settings and verify that Session timeout is set to 15 minutes or less. If Splunk is not configured to 15 minutes or less, this is a finding.

## Group: SRG-APP-000291-AU-000200

**Group ID:** `V-221939`

### Rule: Splunk Enterprise must notify the System Administrator (SA) and Information System Security Officer (ISSO) when account events are received (creation, deletion, modification, disabling).


**Rule ID:** `SV-221939r879669_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Once an attacker establishes access to an application, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Sending notification of account creation events to the SA and ISSO is one method for mitigating this risk. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to offload those access control functions and focus on core application features and functionality. Satisfies: SRG-APP-000291-AU-000200, SRG-APP-000292-AU-000420, SRG-APP-000293-AU-000430, SRG-APP-000294-AU-000440</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk instance is used for Tier 2 CSSP (formerly CND-SP) or JRSS analysis, this check is N/A. Interview the SA to verify that a process exists to notify the SA and ISSO when account events are received for all devices and hosts within its scope of coverage. Interview the ISSO to confirm receipt of this notification. If Splunk Enterprise is not configured to notify the SA and ISSO when account events are received for all devices and hosts within its scope of coverage, this is a finding.

## Group: SRG-APP-000291-AU-000200

**Group ID:** `V-221940`

### Rule: Splunk Enterprise must notify analysts of applicable events for Tier 2 CSSP and JRSS only.

**Rule ID:** `SV-221940r879669_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Sending notifications or populating dashboards are ways to monitor and alert on applicable events and allow analysts to mitigate issues. Tier 2 CSSP and JRSS analysts perform higher-level analysis at larger network coverage and have specific guidelines to handle alerts and reports. This requirement allows these analysts to not be burdened by all of the lower-level alerts that can be considered "white noise" by isolating their alerting and reporting requirements from other requirements in this STIG. Satisfies: SRG-APP-000291-AU-000200, SRG-APP-000292-AU-000420, SRG-APP-000293-AU-000430, SRG-APP-000294-AU-000440</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check applies to Tier 2 CSSP or JRSS instances only. Verify that notifications and dashboards are configured in accordance with designated SSPs, SOPs, and/or TTPs. The absence of notifications and dashboards is a finding.

## Group: SRG-APP-000065-AU-000240

**Group ID:** `V-221941`

### Rule: Splunk Enterprise must enforce the limit of 3 consecutive invalid logon attempts by a user during a 15 minute time period.

**Rule ID:** `SV-221941r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account gets created, for example, an emergency account of last resort for recovery.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select Settings >> Access Controls >> Password Policy Management. Verify that Lockout is Enabled, Failed login attempts is set to 3, and Lockout threshold in minutes is set to 15. If these settings are not set as described, this is a finding.

## Group: SRG-APP-000503-AU-000280

**Group ID:** `V-221942`

### Rule: Splunk Enterprise must be configured with a successful/unsuccessful logon attempts report.

**Rule ID:** `SV-221942r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SIEM or Central Log Server is the mitigation method for most of the other STIGs applied to an organization. Robust alerting and reporting is a key feature in any incident response plan. The ability to report on logon attempts is the first step is creating a chain of events for a forensic analysis and incident response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk instance is used for Tier 2 CSSP (formerly CND-SP) or JRSS analysis, this check is N/A. Interview the System Administrator (SA) to demonstrate that a logon attempts report exists. If a report does not exist, this is a finding.

## Group: SRG-APP-000095-AU-000050

**Group ID:** `V-246917`

### Rule: The System Administrator (SA) and Information System Security Officer (ISSO) must configure the retention of the log records based on the defined security plan.

**Rule ID:** `SV-246917r879563_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to respond effectively and important forensic information may be lost. The organization must define and document log retention requirements for each device and host and then configure Splunk Enterprise to comply with the required retention period. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the site documentation for the retention time for log data. Examine the following file in the Splunk installation folder: (Note that these files may exist in one of the following folders or its subfolders: $SPLUNK_HOME/etc/apps/ $SPLUNK_HOME/etc/slave-apps/) $SPLUNK_HOME/etc/system/local/indexes.conf For each index defined in the scope, the frozenTimePeriodInSecs setting must match the site documentation. If the settings do not match, this is a finding.

