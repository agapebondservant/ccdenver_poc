# STIG Benchmark: Cisco IOS XR Router NDM Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-216522`

### Rule: The Cisco router must be configured to limit the number of concurrent management sessions to an organization-defined number.

**Rule ID:** `SV-216522r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is not applicable to file transfer actions such as FTP, SCP and SFTP. Review the router configuration to determine if concurrent management sessions are limited as show in the example below: ssh server session-limit 2 If the router is not configured to limit the number of concurrent management sessions, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-216523`

### Rule: The Cisco router must be configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies.

**Rule ID:** `SV-216523r991929_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement. Step 1: Verify that the line vty has an ACL inbound applied as shown in the example below. line default access-class ingress MANAGEMENT_NET transport input ssh ! vty-pool default 0 4 Step 2: Verify that the ACL permits only hosts from the management network to access the router. ipv4 access-list MANAGEMENT_NET 10 permit ipv4 10.1.1.0 255.255.255.0 any 20 deny ipv4 any any log-input If the Cisco router is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-216524`

### Rule: The Cisco router must be configured to enforce the limit of three consecutive invalid logon attempts after which time lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-216524r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Cisco router is not compliant with this requirement. However, the risk associated with this requirement can be fully mitigated if the router is configured to utilize an authentication server to authenticate and authorize users for administrative access. Review the router configuration to verify that the device is configured to use an authentication server as primary source for authentication as shown in the following example: radius-server host 10.1.3.16 auth-port 1645 acct-port 1646 key xxxxxxxxxx … … … aaa authentication login LOGIN_AUTHENTICATION group radius local line console login authentication LOGIN_AUTHENTICATION ! line default login authentication LOGIN_AUTHENTICATION transport input ssh If the router is not configured to use an authentication server to authenticate and authorize users for administrative access, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-216525`

### Rule: The Cisco router must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-216525r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. banner login ^C You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. ^C If the Cisco router is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-216526`

### Rule: The Cisco router must be configured to generate audit records when successful/unsuccessful attempts to logon with access privileges occur.

**Rule ID:** `SV-216526r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement. The configuration example below will log all logon attempts. logging buffered informational logging 10.1.22.2 vrf default severity info If the Cisco router is not configured to generate audit records when successful/unsuccessful attempts to logon, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-216527`

### Rule: The Cisco router must produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-216527r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. In order to establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router is configured to include the date and time on all log records as shown in the configuration example below. service timestamps log datetime localtime If time stamps are not configured, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-216528`

### Rule: The Cisco router must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-216528r960897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the network device provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the deny statements in all interface ACLs to determine if the log-input parameter has been configured as shown in the example below. Note: log-input can only apply to interface bound ACLs. ipv4 access-list BLOCK_INBOUND 10 deny icmp any any log-input If the router is not configured with the log-input parameter after any deny statements to note where packets have been dropped via an ACL, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-216529`

### Rule: The Cisco router must be configured to be configured to prohibit the use of all unnecessary and nonsecure functions and services.

**Rule ID:** `SV-216529r1043177_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router does not have any unnecessary or nonsecure ports, protocols, and services enabled. For example, the following commands should not be in the configuration: service ipv4 tcp-small-servers max-servers 10 service ipv4 udp-small-servers max-servers 10 http client vrf xxxxx telnet vrf default ipv4 server max-servers 1 service call-home Note: Certain legacy devices may require 'service call-home' be enabled to support Smart Licensing as they do not support the newer smart transport configuration. Those devices do not incur a finding for having call-home enabled for Smart Licensing. If any unnecessary or nonsecure ports, protocols, or services are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-216530`

### Rule: The Cisco router must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-216530r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. An alternative to using a sealed envelope in a safe would be credential files, separated by technology, located in a secured location on a file server, with the files only accessible to those administrators authorized to use the accounts of last resort, and access to that location monitored by a central log server. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the Cisco router configuration to verify that a local account for last resort has been configured. username xxxxxxxxxxxx group netadmin secret 5 xxxxxxxxxxxxxxxxxxxx Note: The following groups should not be assigned to this local account: root-system and root-lr. A custom group that provides appropriate tasks can be used. Step 2: Verify that local is defined after radius or tacas+ in the authentication order as shown in the example below. aaa authentication login default group tacacs+ local If the Cisco router is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-216531`

### Rule: The Cisco router must be configured to implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-216531r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that SSH version 2 is configured as shown in the example below. ssh server v2 Note: IOS XR supports SSHv1 and SSHv2. SSHv1 uses Rivest, Shamir, and Adelman (RSA) keys while SSHv2 uses Digital Signature Algorithm (DSA) keys. If the router is not configured to implement replay-resistant authentication mechanisms for network access to privileged accounts, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-216532`

### Rule: The Cisco router must be configured to terminate all network connections associated with device management after five minutes of inactivity.

**Rule ID:** `SV-216532r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that all network connections associated with a device management have an idle timeout value set to five minutes or less as shown in the following example: line console … … … exec-timeout 5 0 ! line default … … … exec-timeout 5 0 transport input ssh If the Cisco router is not configured to terminate all network connections associated with a device management after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-216533`

### Rule: The Cisco router must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-216533r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Cisco router is configured with a logging buffer size as well as on the hard drive. The configuration should look like the example below: logging archive device harddisk severity notifications file-size 10 archive-size 100 … … … logging buffered 8888888 If a logging buffer size and the archive size is not configured, this is a finding. If the Cisco router is not configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-216534`

### Rule: The Cisco router must be configured to generate an alert for all audit failure events.

**Rule ID:** `SV-216534r991930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. logging 10.1.12.7 vrf default severity critical Note: The parameter "critical" can be replaced with a lesser severity level (i.e., error, warning, notice, informational). If the Cisco router is not configured to generate an alert for all audit failure events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-216535`

### Rule: The Cisco router must be configured to synchronize its clock with the primary and secondary time sources using redundant authoritative time sources.

**Rule ID:** `SV-216535r1015296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the configuration example below. ntp server x.x.x.x ntp server y.y.y.y If the Cisco router is not configured to synchronize its clock with redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-216536`

### Rule: The Cisco router must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-216536r961446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. hostname R3 service timestamps log datetime localtime If the router is not configured to record time stamps that meet a granularity of one second, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-216537`

### Rule: The Cisco router must be configured to record time stamps for log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-216537r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in UTC, a modern continuation of GMT, or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. hostname R3 clock timezone EST -5 service timestamps log datetime localtime Note: UTC is the default; hence, the command set time-zone may not be seen in the configuration. This can be verified using the show system uptime command. If the router is not configured to record time stamps for audit records that can be mapped to UTC or GMT, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-216538`

### Rule: The Cisco router must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-216538r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. snmp-server host x.x.x.x traps version 3 auth V3USER snmp-server user V3USER V3GROUP v3 auth sha snmp-server view V3READ iso included snmp-server view V3WRITE iso included snmp-server group V3GROUP v3 auth read V3READ write V3WRITE If the Cisco router is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-216539`

### Rule: The Cisco router must be configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm.

**Rule ID:** `SV-216539r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the strong encryption that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information that can be used to create a network outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. snmp-server host x.x.x.x traps version 3 auth V3USER snmp-server user V3USER V3GROUP v3 auth sha encrypted 110B1607150B snmp-server view V3READ iso included snmp-server view V3WRITE iso included snmp-server group V3GROUP v3 auth read V3READ write V3WRITE If the Cisco router is not configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-216540`

### Rule: The Cisco router must be configured to authenticate NTP sources using authentication that is cryptographically based.

**Rule ID:** `SV-216540r1107163_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the configuration example below. ntp authentication-key 1 hmac-sha2-256 xxxxxx trusted-key 1 server x.x.x.x key 1 server y.y.y.y key 1 If the Cisco router is not configured to authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-216541`

### Rule: The Cisco router must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of remote maintenance sessions.

**Rule ID:** `SV-216541r961554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code use d for authentication to cryptographic modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that SSH version 2 is configured as shown in the example below. ssh server v2 Note: IOS XR supports SSHv1 and SSHv2. SSHv1 uses Rivest, Shamir, and Adelman (RSA) keys while SSHv2 uses Digital Signature Algorithm (DSA) keys which is FIPS 186-4. If the Cisco router is not configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-216542`

### Rule: The Cisco router must be configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-216542r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that SSH version 2 is configured as shown in the example below. ssh server v2 Note: IOS XR supports SSHv1 and SSHv2. The AES encryption algorithm is supported on the SSHv2 server and client, but not on the SSHv1 server and client. Any requests for an AES cipher sent by an SSHv2 client to an SSHv1 server are ignored, with the server using 3DES instead. The cipher preference for the SSH server follows the order AES128, AES192, AES256, and, finally, 3DES. The server rejects any requests by the client for an unsupported cipher, and the SSH session does not proceed. If the router is configured to implement SSH version 1, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-216543`

### Rule: The Cisco router must be configured to off-load log records onto a different system than the system being audited.

**Rule ID:** `SV-216543r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement as shown in the example below. logging 10.1.12.7 vrf default severity info If the Cisco router is not configured to off-load log records onto a different system than the system being audited, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-216544`

### Rule: The Cisco router must be configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-216544r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of user accounts and authentication increases the administrative access to the router. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that the device is configured to use at least two authentication servers as primary source for authentication as shown in the following example: radius-server host 10.1.3.16 auth-port 1645 acct-port 1646 key xxxxxxxxxx radius-server host 10.1.3.17 auth-port 1645 acct-port 1646 key xxxxxxxxxx… … … aaa authentication login LOGIN_AUTHENTICATION group radius local line console login authentication LOGIN_AUTHENTICATION ! line default login authentication LOGIN_AUTHENTICATION transport input ssh If the Cisco router is not configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-216545`

### Rule: The Cisco router must be configured to back up the configuration when changes occur.

**Rule ID:** `SV-216545r1069525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify that it is compliant with this requirement. The example configuration below will send the configuration to an SCP server when a configuration change occurs. configuration commit auto-save filename scp://user1@server1://test-folder/test_123 If the Cisco router is not configured to conduct backups of the configuration when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-216546`

### Rule: The Cisco router must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-216546r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority (CA) at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if a CA trust point has been configured. The CA trust point will contain the URL of the CA in which the router has enrolled with. Verify this is a DoD or DoD-approved CA. This will ensure the router has enrolled and received a certificate from a trusted CA. The CA trust point configuration would look similar to the example below. crypto pki trustpoint CA_X enrollment url http://trustpoint1.example.com Note: A remote end-point's certificate will always be validated by the router by verifying the signature of the CA on the certificate using the CA's public key, which is contained in the router's certificate it received at enrollment. Note: This requirement is not applicable if the router does not have any public key certificates. If the Cisco router is not configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-216547`

### Rule: The Cisco router must be configured to send log data to at least two syslog servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-216547r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router is configured to send logs to at least two syslog servers. The configuration should look similar to the example below: logging 10.1.3.22 vrf default severity info logging 10.1.3.23 vrf default severity info If the router is not configured to send log data to the syslog server, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-216549`

### Rule: The Cisco router must be running an IOS release that is currently supported by Cisco Systems.

**Rule ID:** `SV-216549r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities. Running a supported release also enables operations to maintain a stable and reliable network provided by improved quality of service and security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router is in compliance with this requirement by having the router administrator enter the following command: show version Verify that the release is still supported by Cisco. All releases supported by Cisco can be found on the following URL: www.cisco.com/c/en/us/support/ios-nx-os-software If the router is not running a supported release, this is a finding.

