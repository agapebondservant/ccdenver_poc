# STIG Benchmark: Arista MLS EOS 4.X NDM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-255947`

### Rule: The Arista network device must limit the number of concurrent sessions to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-255947r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions must be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to limit the number of concurrent management sessions with the following commands: switch#sh run | section management ssh management ssh connection limit 5 ! If the Arista network device is not configured to limit the number of SSH concurrent sessions, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-255948`

### Rule: The Arista network device must enforce approved authorizations for controlling the flow of management information within the network device based on information flow control policies.

**Rule ID:** `SV-255948r991781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured with access control lists to control the flow of management information. Step 1: Verify SSH has an inbound ACL applied as shown in the example below. sh run | sec management ssh ip access-group MGMT_NETWORK in Step 2: Verify the ACL permits only hosts from the management network to access the device. sh run | sec access-list MGMT_NETWORK ip access-list MGMT_NETWORK 10 permit ip 10.1.12.0/24 any 20 deny ip any any log If the Arista network device is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255949`

### Rule: The Arista network device must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-255949r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista device is configured to enforce the limit of three consecutive invalid logon attempts with the following command: switch#show running-config | section aaa aaa authentication policy lockout failure 3 duration 900 If the Arista device is not configured to enforce the limit of three consecutive invalid logon attempts, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-255950`

### Rule: The Arista network device must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-255950r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. Satisfies: SRG-APP-000068-NDM-000215, SRG-APP-000069-NDM-000216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured to present a DOD-approved banner that is formatted in accordance with DTM-08-060. Verify the Arista device uses the following verbiage for applications that can accommodate banners of 1300 characters by using the following command: switch#show configuration | section banner "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If the Arista device does not display such a banner, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-255951`

### Rule: The Arista network device must be configured to audit all administrator activity.

**Rule ID:** `SV-255951r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. Satisfies: SRG-APP-000026-NDM-000208, SRG-APP-000027-NDM-000209, SRG-APP-000028-NDM-000210, SRG-APP-000029-NDM-000211, SRG-APP-000080-NDM-000220, SRG-APP-000091-NDM-000223, SRG-APP-000101-NDM-000231, SRG-APP-000319-NDM-000283, SRG-APP-000343-NDM-000289, SRG-APP-000495-NDM-000318, SRG-APP-000499-NDM-000319, SRG-APP-000503-NDM-000320, SRG-APP-000504-NDM-000321, SRG-APP-000506-NDM-000323</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured to audit all administrator activity. Verify the AAA logging settings in the configuration file with the following example: switch#show running-config | section aaa aaa authentication policy on-success log aaa authentication policy on-failure log aaa accounting exec default start-stop group radius logging aaa accounting system default start-stop group radius logging aaa accounting commands all default start-stop logging group radius If the Arista network device is not configured to audit all administrator activity, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-255952`

### Rule: The Arista network device must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-255952r1043177_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device has telnet and https disabled. Step 1: Determine if telnet is disabled with the following command: switch#show management telnet Telnet status for Default VRF is disabled Telnet session limit is 20 Telnet session limit per host is 20 If telnet is enabled, this is a finding. Step 2: Determine if https is disabled with the following command: switch#show management http-server SSL Profile: none FIPS Mode: No QoS DSCP: 0 LogLevel: none CSP Frame Ancestor: None TLS Protocols: 1.0 1.1 1.2 VRF Server Status Enabled Services ------------------------------------------------------- default HTTPS: port 443 http-commands If Enabled Services in the output shows http-commands, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-255953`

### Rule: The Arista network device must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-255953r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify on the Arista network device that an account of last resort is configured using the following command: switch#sh running-config | section username username Emergency-Admin privilege 15 role network-admin secret sha512 $6$ObuWg.Eu7DwGD8k/$EgT0uI.hLrStrmxUvJijecxDXr.Zy.imi1UrDzDP38q8Erqgkfe0IhHzIhYmR3ekW74XdAFf7I6SgzAoUFd0 Step 2: Verify the Arista network device default account has been overwritten with the local account of last resort. switch#sh running-config | section username username Emergency-Admin privilege 15 role network-admin secret sha512 $6$ObuWg.Eu7DwGD8k/$EgT0uI.hLrStrmxUvJijecxDXr.Zy.imi1UrDzDP38q8Erqgkfe0IhHzIhYmR3ekW74XdAFf7I6SgzAoUFd0 If one local account on the Arista network device does not exist for use as the account of last resort in the event the authentication server is unavailable, this is a finding. If the default admin account exists on the device, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255954`

### Rule: The Arista network device must enforce a minimum 15-character password length.

**Rule ID:** `SV-255954r1015710_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista device configuration "show management security" to determine the minimum 15-character password length. switch#show run | section management security management security password minimum length 15 ! If the Arista network device does not enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-255955`

### Rule: The Arista network device must use FIPS 140-2 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-255955r961050_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the Arista network device uses FIPS 140-2 approved algorithms for authentication to a cryptographic module. Step 1: Review the Arista network device configuration to verify hardware or software entropy is enabled and FIPS restrictions are used in accordance with NIST-specified validated cryptographic requirements. switch# show management security CPU Model: AMD GX-424CC SOC with Radeon(TM) R5E Graphics Security Chip: N313X Crypto Module: Arista EOS Crypto Module v2.0 Forwarding ASIC: Jericho0 Model: Jericho Blocked client protocols: None Hardware entropy generation is enabled Haveged entropy generation is disabled Jitter entropy generation is disabled ! If both hardware entropy and haveged entropy are disabled, this is a finding. Step 2: Review the Arista network device configuration to verify that FIPS restrictions are enabled for management security to use EOS Crypto Module for the RSA key pair used for SSH and the device can only use FIPS-approved algorithms. switch(config)show run | section management ssh management ssh fips restrictions ! If the FIPS restrictions line is not present, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255956`

### Rule: The Arista network device must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255956r991784_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-APP-000190-NDM-000267, SRG-APP-000186-NDM-000266</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista device is configured for 10-minute inactivity timeout for management sessions. switch#sh run | section management ! interface Management1 ip address 172.28.134.55/20 ! management console idle-timeout 10 ! management ssh idle-timeout 10 ! If the Arista network device is not configured to terminate the connection associated with a device management session at the end of the session or after 10 minutes of inactivity, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-255957`

### Rule: If the Arista network device uses role-based access control, the network device must enforce organization-defined role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-255957r987662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. Role-based access control (RBAC) simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement. Satisfies: SRG-APP-000329-NDM-000287, SRG-APP-000380-NDM-000304</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces role-based access control policy over defined subjects and objects. This requirement may be met through use of a properly configured authentication server. Note: If not using role-based access for the network device, this check is Not Applicable. Step 2: Verify the Arista network device configured AAA servers are synchronized for all role-based authentication access control structure defined by role types and user-defined control policies over defined subjects and objects. switch(config)#show running-config | section role role network-admin 10 permit command .* ! role operator 10 permit command show running-config [all|detail] sanitized 20 deny command >|>>|extension|\||session|do|delete|copy|rmdir|mkdir|python-shell|bash|platform|scp|append|redirect|tee|more|less|who|show run.* 30 deny mode config command (no |default )?(username|role|aaa|tcpdump|schedule|event.*) 40 permit command .* ! role tester 10 permit command show running-config [all|detail] sanitized 20 deny command >|>>|extension|\||session|do|delete|copy|rmdir|mkdir|python-shell|bash|platform|scp|append|redirect|tee|more|less|who|show run.* 30 deny mode config command (no |default )(username|role|aaa|tcpdump|schedule|event.*) 40 permit command .* If role-based access control policy is not enforced over defined subjects and objects, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255958`

### Rule: The Arista network device must be configured to synchronize internal system clocks using redundant authenticated time sources.

**Rule ID:** `SV-255958r1015711_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source. Satisfies: SRG-APP-000373-NDM-000298, SRG-APP-000374-NDM-000299, SRG-APP-000375-NDM-000300, SRG-APP-000395-NDM-000347</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to synchronize internal information system clocks with authenticated primary and secondary time sources. Verify the Arista network device configuration with the following example: switch# show running-config | section ntp ntp authentication-key 12 sha1 7 06131C2058470A58 ntp trusted-key 12 ntp authenticate servers ntp local-interface Management1 ntp server 192.168.16.36 prefer key 12 ntp server 192.168.16.37 key 12 If the Arista network device is not configured to synchronize internal system clocks with the primary and secondary time sources, this is a finding. If the Arista network device does not authenticate Network Time Protocol sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255959`

### Rule: The Arista network device must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-255959r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to verify SNMP messages are authenticated using a FIPS-validated HMAC. Verify the Arista network device is configured for the following SNMP example parameters: switch(config)#show run | section snmp snmp-server engineID local f5717f444ca880dbb200 snmp-server chassis-id ID CC-7050X3 snmp-server contact FedSE snmp-server location JITC snmp-server view snmpview system included snmp-server group testers v3 priv read snmpview snmp-server user jitc-sw testers v3 localized f8527f444ca990dcc200 auth sha 7b65225a6abf5111cd951e6cb7e105aef5bcd734 priv aes a1aedb1986642e766d4c8032d58e73b72bc3528b snmp-server host 192.168.10.31 version 3 priv jitc-sw snmp-server enable traps snmp authentication snmp-server enable traps snmp link-down snmp-server enable traps snmp link-up ! If the Arista network device is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255960`

### Rule: The Arista network devices must use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of remote maintenance sessions.

**Rule ID:** `SV-255960r961554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers. Satisfies: SRG-APP-000411-NDM-000330, SRG-APP-000156-NDM-000250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the Arista network device is configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions. NOTE: Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DOD systems should not be configured to use SHA-1 for integrity of remote access sessions. Verify the HMAC settings for SSH using the following command: switch#sh run | section management ssh mac hmac-sha2-256 hmac-sha2-512 If the Arista network device does not implement replay-resistant authentication mechanisms for network access to privileged accounts, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-255961`

### Rule: The Arista network device must be configured to implement cryptographic mechanisms using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-255961r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Validate that a FIPS validated SSH encryption algorithm is selected. NOTE: AES-CBC algorithms have been considered compromised and are no longer recommended for cryptographic algorithms. AES-CTR and AES-GCM are both superior algorithms and are recommended. sh run | section management ssh cipher aes256-ctr aes512-ctr aes128-ctr If the Arista network device is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-255962`

### Rule: The Arista network device must be configured to capture all DOD auditable events.

**Rule ID:** `SV-255962r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis. Satisfies: SRG-APP-000095-NDM-000225, SRG-APP-000096-NDM-000226, SRG-APP-000097-NDM-000227, SRG-APP-000098-NDM-000228, SRG-APP-000099-NDM-000229, SRG-APP-000100-NDM-000230, SRG-APP-000516-NDM-000334, SRG-APP-000357-NDM-000293, SRG-APP-000360-NDM-000295, SRG-APP-000505-NDM-000322</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured to audit all DOD auditable events. Verify the logging settings in the configuration file with the following example: switch#sh running-config | section logging logging buffered informational logging trap informational NOTE: Acceptable settings include debugging, informational, and notifications to adjust syslog server traffic impact. Setting to higher severity levels can cause necessary lower-level events to be missed. If the Arista network device is not configured to audit all DOD auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255963`

### Rule: The network device must be configured to use an authentication server to authenticate users prior to granting administrative access.

**Rule ID:** `SV-255963r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured to use an authentication server as primary source for authentication. Verify the Arista network device configuration for RADIUS server IP, aaa group server, and defined encryption key using the following example command: switch#show running-config |section radius radius-server host 192.168.10.101 key 7 106D1A182224E12AZ ! aaa group server radius RADIUS_1 server 192.168.10.101 ! switch#show running-config | section aaa aaa authentication login default group radius local aaa authentication login console group radius local aaa authentication dot1x default group radius aaa authentication policy on-success log aaa authentication policy on-failure log aaa authorization console aaa authorization commands all default local aaa accounting exec default start-stop group radius logging aaa accounting system default start-stop group radius logging aaa accounting commands all default start-stop logging group radius If the Arista network device is not configured to use an authentication server to authenticate users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-255964`

### Rule: The network device must be configured to conduct backups of system level information contained in the information system when changes occur.

**Rule ID:** `SV-255964r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device is configured with an “event-handler” to complete an incremental backup of the running configuration, which can be maintained in the switch flash memory stored in /mnt/flash/startup-config_directory (filetime): switch#show run | section event-handler event-handler CFG_BACKUP trigger on-startup-config action bash buf () { filetime=$(date +%Y%m%d); cp /mnt/flash/startup-config /mnt/flash/startup-config_${filetime}; }; buf ! If the Arista network device is not configured to conduct backups of system-level data when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255965`

### Rule: The Arista network device must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255965r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the Arista network device obtains public key certificates from an appropriate certificate policy through an approved service provider. Note: This check is Not Applicable if not using any PKI certificates. Verify the DOD PKI certificates are copied to /certificate directory on the switch as outlined in the Arista Military Deployment Guide and configured as in the section "Configuring RSA SecureID with OTP Management". switch# #dir certificate: Directory of certificate:/ -rw- 2025 Apr 30 17:34 ARISTA_ROOT_CA.crt -rw- 2110 Apr 30 17:34 ARISTA_SIGNING_CA.crt -rw- 2015 Apr 30 17:35 Arista-CCS-720XP-48Y6.pem -rw- 2020 Apr 30 17:35 DOD_JITC_Root_CA_3__0x01__DOD_JITC_Root_CA_3.cer -rw- 2125 Apr 30 17:35 CA-60.cer ! Verify the provider of the certificate is a DOD-approved certificate authority. If the Arista network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-255966`

### Rule: The Arista network Arista device must be configured to send log data to a central log server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-255966r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat. Satisfies: SRG-APP-000516-NDM-000350, SRG-APP-000119-NDM-000236, SRG-APP-000120-NDM-000237, SRG-APP-000515-NDM-000325</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista network device has been configured Syslog server for auditing data by using the following command: switch#show running-config | section logging logging host 192.168.16.30 514 ! If logging host is not configured to send log data to a central log server, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-255967`

### Rule: The Arista network device must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-255967r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista device is running a certified version of EOS from the Arista.com website on the Support/Software Download section. switch#show version Arista DCS-7280SRA-48C6-F Hardware version: 21.00 Serial number: SSJ18250372 Hardware MAC address: 7483.ef6d.86f7 System MAC address: 7483.ef6d.86f7 Software image version: 4.26.4M Architecture: i686 Internal build version: 4.26.4M-25280047.4264M Internal build ID: 79589245-f1f3-49b7-8bee-cbfacac004e6 Image format version: 1.0 Uptime: 2 weeks, 0 days, 9 hours and 53 minutes Total memory: 8098984 kB Free memory: 6155528 kB If the Arista network device is not running an operating system release that is currently supported by Arista Networks, this is a finding.

