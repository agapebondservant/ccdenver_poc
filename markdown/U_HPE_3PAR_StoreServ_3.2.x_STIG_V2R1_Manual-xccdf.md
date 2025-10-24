# STIG Benchmark: HPE 3PAR StoreServ 3.2.x Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237812`

### Rule: The storage system must be operated at the latest maintenance update available from the vendor.

**Rule ID:** `SV-237812r647845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization must install security-relevant updates (e.g., patches, maintenance updates, and version updates). Due to the potential need for isolation of the storage system from automatic update mechanisms, the organization must give careful consideration to the methodology used to carry out updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine when the last update occurred, by entering the following command: cli% showpatch -hist The output fields are InstallTime Id Package Version Examine the InstallTime of the last entry in the output. If the last update occurred more than 3 months ago, verify on the vendor's website what the latest version is. If the current installation is not at the latest release, this is a finding.

## Group: SRG-OS-000095-GPOS-00049

**Group ID:** `V-237813`

### Rule: The storage system in a hardened configuration must be configured to disable the Remote Copy feature, unless needed.

**Rule ID:** `SV-237813r647848_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Remote Copy feature is not running via the following command: cli% showrcopy Remote Copy is not configured on this system. Review the requirements by the Information Owner to determine whether the site requires the Remote Copy feature in order to meet mission objectives. If the Status is "Started" and there is no documented requirement for this usage, this is a finding. Any other response is not a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237814`

### Rule: The CIM service must be disabled, unless needed.

**Rule ID:** `SV-237814r647851_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for operating systems to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Operating systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to games, software packages, tools, and demonstration software not related to requirements or providing a wide array of functionality not required for every mission, but which cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that CIM is not running with the following command: cli% showcim Review the requirements by the Information Owner to determine whether the site requires a CIM management client in order to meet mission objectives. If the output does not report the CIM "Service" is "Disabled" and there is no documented requirement for this usage, this is a finding. If the output does not report the CIM service "State" is "Inactive" and there is no documented requirement for this usage, this is a finding.

## Group: SRG-OS-000126-GPOS-00066

**Group ID:** `V-237815`

### Rule: The storage system must terminate all network connections associated with a communications session at the end of the session, at shutdown, or after 10 minutes of inactivity.

**Rule ID:** `SV-237815r647854_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communication sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This does not mean that the operating system terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-OS-000126-GPOS-00066, SRG-OS-000163-GPOS-00072, SRG-OS-000279-GPOS-00109</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the remote session timeout is set to 10 minutes or less with the following command: cli% showsys -param If the output does not contain the information below, this is a finding. SessionTimeout : 00:10:00

## Group: SRG-OS-000423-GPOS-00187

**Group ID:** `V-237817`

### Rule: The CIM service must use DoD-approved encryption.

**Rule ID:** `SV-237817r647904_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. Facilitating the confidentiality and integrity of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via encryption. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the CIM service is running with proper encryption via the following command: cli% showcim If the CIM service is "Disabled" and the CIM service "State" is "Inactive", this requirement is not applicable. If the output does not report the CIM HTTP value is "Disabled", this is a finding. If the output does not report the CIM HPPTSPort value is "5989", this is a finding.

## Group: SRG-OS-000033-GPOS-00014

**Group ID:** `V-237818`

### Rule: DoD-approved encryption must be implemented to protect the confidentiality and integrity of remote access sessions, information during preparation for transmission, information during reception, and information during transmission in addition to enforcing replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-237818r647863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised because unprotected communications can be intercepted and either read or altered. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Facilitating the confidentiality of transmitted information requires the operating system to take measures in preparing information for transmission. This can be accomplished via access control and encryption. This requirement applies to both internal and external networks and all types of information system components from which information can be transmitted (e.g., servers, mobile devices, notebook computers, printers, copiers, scanners, and facsimile machines). Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Operating systems using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. This allows for Security Levels 1, 2, 3, or 4 for use on a general purpose computing system. Satisfies: SRG-OS-000033-GPOS-00014, SRG-OS-000096-GPOS-00050, SRG-OS-000112-GPOS-00057, SRG-OS-000120-GPOS-00061, SRG-OS-000250-GPOS-00093, SRG-OS-000297-GPOS-00115, SRG-OS-000393-GPOS-00173, SRG-OS-000394-GPOS-00174, SRG-OS-000423-GPOS-00187, SRG-OS-000424-GPOS-00188, SRG-OS-000425-GPOS-00189, SRG-OS-000426-GPOS-00190, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that insecure ports are disabled. cli% setnet disableports yes Confirm the operation by entering "y" and pressing "Enter". If an error is reported, this is a finding. If available, a remote port scan can also verify that only secure ports are open. From a command shell on a Linux workstation in the operational environment, enter the following command: cli% nmap -sT -sU -sV --version-all -vv -p1 -65535 <ip address of storage system> If any port other than 22 (ssh), 123 (ntp), 161 and 162 (snmp), and 5783 (ssl manageability) report as open, this is a finding.

## Group: SRG-OS-000404-GPOS-00183

**Group ID:** `V-237819`

### Rule: The storage system must implement cryptographic mechanisms to prevent unauthorized modification or disclosure of all information at rest on all storage system components.

**Rule ID:** `SV-237819r647866_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Operating systems handling data requiring “data at rest” protections must employ cryptographic mechanisms to prevent unauthorized disclosure and modification of the information at rest. Selection of a cryptographic mechanism is based on the need to protect the integrity of organizational information. The strength of the mechanism is commensurate with the security category and/or classification of the information. Organizations have the flexibility to either encrypt all information on storage devices (i.e., full disk encryption) or encrypt specific data structures (e.g., files, records, or fields). Satisfies: SRG-OS-000404-GPOS-00183, SRG-OS-000405-GPOS-00184</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the requirements by the Information Owner to discover whether the system stores sensitive or classified information. If the system does not store sensitive or classified information, this is not applicable. Verify that data at rest encryption is enabled by entering the following command: cli% controlencryption status Licensed | Enabled | BackupSaved | State | SeqNum | Keystore yes | Yes | no | normal | 0 | --- If the "Enabled" flag is not set to "Yes" as shown in the output above, this is a finding.

## Group: SRG-OS-000046-GPOS-00022

**Group ID:** `V-237820`

### Rule: SNMP must be changed from default settings and must be configured on the storage system to provide alerts of critical events that impact system security.

**Rule ID:** `SV-237820r647869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Whether active or not, default SNMP passwords, users, and passphrases must be changed to maintain security. If the service is running with the default authenticators, anyone can gather data about the system and the network(s) and use the information to potentially compromise the integrity of the system or network(s). The product must be configured to alert administrators when events occur that may impact system operation or security. The alerting mechanism must support secured options and configurations that can be audited. Satisfies: SRG-OS-000046-GPOS-00022, SRG-OS-000480-GPOS-00227, SRG-OS-000344-GPOS-00135</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a SNMPv3 user account is configured. Run the following command: cli% showsnmpuser Username | AuthProtocol | PrivProtocol 3parsnmpuser | HMAC SHA 96 | CFB128 AES 128 If the output is not displayed in the above format, this is a finding. Identify the SNMP trap recipient and report SNMP configuration with the following command: cli% showsnmpmgr HostIP | Port | SNMPVersion | User <snmp trap recipient IP> | 162 | 3 | 3parsnmpuser If the SNMP trap recipient IP address is incorrect, this is a finding. If the SNMP port is not "162", this is a finding. If the SNMP version is not "3", this is a finding. If the SNMP user ID is incorrect, this is a finding. Generate a test trap: cli% checksnmp Trap sent to the following managers: < IP address of trap recipient> If the response does not indicate a trap was successfully sent, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237821`

### Rule: The SNMP service on the storage system must use only SNMPv3 or its successors.

**Rule ID:** `SV-237821r647872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMP Versions 1 and 2 are not considered secure. Without the strong authentication and privacy provided by the SNMP Version 3 User-based Security Model (USM), an attacker or other unauthorized users may gain access to detailed system management information and use the information to launch attacks against the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SNMPv3 is enabled by entering the command: cli% showsnmpmgr HostIP Port SNMPVersion User <IP address of SNMP manager> 162 3 <username> If the SNMPVersion is not 3, this is a finding.

## Group: SRG-OS-000480-GPOS-00227

**Group ID:** `V-237822`

### Rule: The SNMP service on the storage system must require the use of a FIPS 140-2 approved cryptographic hash algorithm as part of its authentication and integrity methods.

**Rule ID:** `SV-237822r647875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SNMP service must use AES or a FIPS 140-2 approved successor algorithm for protecting the privacy of communications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that SNMP encryption uses AES by entering the following command: cli% showsnmpuser Username AuthProtocol PrivProtocol 3parsnmpuser HMAC-SHA-96 CFB128-AES-128 If the PrivProtocol in the result is not AES, this is a finding.

## Group: SRG-OS-000355-GPOS-00143

**Group ID:** `V-237823`

### Rule: The storage system must, for networked systems, compare internal information system clocks at least every 24 hours with a server which is synchronized to one of the redundant United States Naval Observatory (USNO) time servers, or a time server designated for the appropriate DoD network (NIPRNet/SIPRNet), and/or the Global Positioning System (GPS).

**Rule ID:** `SV-237823r647878_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside the configured acceptable allowance (drift) may be inaccurate. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NTP is operational by entering the following command: cli% shownet < multiple lines of heading, and node network information> NTP server : <ip address of ntp server> If one of the lines of the output does not show the correct NTP server IP address, this is a finding.

## Group: SRG-OS-000123-GPOS-00064

**Group ID:** `V-237824`

### Rule: The storage system must be configured to have only 1 emergency account which can be accessed without LDAP, and which has full administrator capabilities.

**Rule ID:** `SV-237824r647881_rule`
**Severity:** high

**Description:**
<VulnDiscussion>While LDAP allows the storage system to support stronger authentication and provides additional auditing, it also places a dependency on an external entity in the operational environment. The existence of a single local account with a strong password means that administrators can continue to access the storage system in the event the LDAP system is temporarily unavailable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only essential local accounts are configured. Enter the following command: cli% showuser If the output shows users other than the four accounts below, this is a finding: 3paradm 3parsvc 3parsnmpuser 3parcimuser

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-237825`

### Rule: The storage system must only be operated in conjunction with an LDAP server in a trusted environment if an Active Directory server is not available.

**Rule ID:** `SV-237825r647884_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Where strong account and password management capabilities are required, the 3PAR system is heavily dependent on its ability to use an LDAP server. Satisfies: SRG-OS-000001-GPOS-00001, SRG-OS-000104-GPOS-00051, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is configured for LDAP. Enter the following command: cli% showauthparam If the output indicates an error, this is a finding. If the resulting output does not include group parameters "groups-dn", "group-obj", or "group-name-attr" then the host is configured to use Active Directory and this requirement is not applicable. If the host is using LDAP and the following fields of the output are not configured, this is a finding. ldap-server <ip address of LDAP server> ldap-server-hn <host name of LDAP server> Next, verify that the LDAP authentication is operational by entering the following command: cli% checkpassword <username> password: <Enter the password for username> If the username and password used in "checkpassword" are known to be valid LDAP credentials, and the following text is NOT displayed at the end of the resulting output, this is a finding. user <username> is authenticated and authorized Note: The "checkpassword" command will not display authenticated information even if LDAP is properly configured, if the username and password are not entered correctly.

## Group: SRG-OS-000125-GPOS-00065

**Group ID:** `V-237826`

### Rule: User credentials which would allow remote access to the system by the Service Processor must be removed from the storage system.

**Rule ID:** `SV-237826r647903_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failure to remove the default user accounts associated with remote access from the Service Processor increases the risk of unauthorized access to the 3PAR OS via the product's remote support interface. The Service Processor's authentication methods have not been evaluated and using such mechanisms to permit remote, full control of the system by organizational or non-organizational users represents an increased risk to unauthorized access. The Service Processor can also send system data offsite providing access to system information to non-DoD organizations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Service Processor credentials are not present. cli% showuser If any of the users, "3parbrowse", "3paredit", or "3parservice" exist, this is a finding

## Group: SRG-OS-000001-GPOS-00001

**Group ID:** `V-237827`

### Rule: The storage system must only be operated in conjunction with an Active Directory server in a trusted environment if an LDAP server is not available.

**Rule ID:** `SV-237827r647890_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Where strong account and password management capabilities are required, the 3PAR system is heavily dependent on its ability to use an AD server. Satisfies: SRG-OS-000001-GPOS-00001, SRG-OS-000104-GPOS-00051, SRG-OS-000480-GPOS-00227</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the system is configured for Active Directory (AD). Enter the following command: cli% showauthparam If the result returns an error, this is a finding. If the resulting output does include the parameters "groups-dn", "group-obj", or "group-name-attr" then the host is setup for LDAP, this requirement is not applicable. If the host is setup for Active Directory and these fields in the output are not configured, this is a finding. ldap-server <ip address of AD server> ldap-server-hn <host name of AD server> Next, verify that the AD authentication is operational by entering the following command: cli% checkpassword <username>: password: <Enter the password for username> If the username and password used in checkpassword are known to be valid AD credentials, and the following text is NOT displayed at the end of the resulting output, this is a finding. user <username> is authenticated and authorized Note: The "checkpassword" command will not display authenticated information even if AD is properly configured, if the username and password are not entered correctly.

## Group: SRG-OS-000078-GPOS-00046

**Group ID:** `V-237828`

### Rule: The storage system must require passwords contain a minimum of 15 characters, after an administrator has set the minimum password length to that value.

**Rule ID:** `SV-237828r647893_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the minimum password length is set to a value of "15". Check the current password configuration: cli% setpassword -minlen 15 If an error is reported, this is a finding. Note: You must have super-admin privileges to perform this action.

## Group: SRG-OS-000023-GPOS-00006

**Group ID:** `V-237829`

### Rule: The Standard Mandatory DoD Notice and Consent Banner must be displayed until users acknowledge the usage conditions and take explicit actions to log on for further access.

**Rule ID:** `SV-237829r647896_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. The banner must be acknowledged by the user prior to allowing the user access to the operating system. This provides assurance that the user has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the user, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the application usage policy, a click-through banner at system logon is required. The system must prevent further activity until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for operating systems that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-OS-000023-GPOS-00006, SRG-OS-000024-GPOS-00007, SRG-OS-000228-GPOS-00088</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the SSH login banner is properly configured. Enter the following command: cli% showsshbanner I've read & consent to terms in IS user agreem't If the output is not: "I've read & consent to terms in IS user agreem't" this is a finding. Alternatively: To inspect the banner, login via SSH from a remote host. If the output shown above is not displayed during SSH authentication, this is a finding.

## Group: SRG-OS-000341-GPOS-00132

**Group ID:** `V-237830`

### Rule: The storage system must allocate audit record storage capacity to store at least one weeks worth of audit records, when audit records are not immediately sent to a central audit record storage facility.

**Rule ID:** `SV-237830r647899_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To verify operating systems have a sufficient storage capacity in which to write the audit logs, operating systems need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial installation of the operating system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the logging capacity is set to the maximum value of "4", with the following command: cli% showsys -param If the resulting list of configured parameters and values, does not contain "EventLogSize : 4M", this is a finding.

## Group: SRG-OS-000359-GPOS-00146

**Group ID:** `V-237831`

### Rule: The storage system must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-237831r647902_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the operating system include date and time. Time is commonly expressed in UTC, a modern continuation of GMT, or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the "Timezone" field is configured by entering the following command: cli% showdate Node Date 0 2016-05-18 23:46:29 UTC (Etc/UTC) 1 2016-05-18 23:46:37 UTC (Etc/UTC) If the output does not match the required time zone, this is a finding.

