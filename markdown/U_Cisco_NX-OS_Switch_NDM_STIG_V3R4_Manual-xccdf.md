# STIG Benchmark: Cisco NX OS Switch NDM Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-220474`

### Rule: The Cisco switch must be configured to limit the number of concurrent management sessions to an organization-defined number.

**Rule ID:** `SV-220474r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if concurrent management sessions are limited as show in the example below: line vty session-limit 2 If the switch is not configured to limit the number of concurrent management sessions, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-220475`

### Rule: The Cisco switch must be configured to automatically audit account creation.

**Rule ID:** `SV-220475r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account creation. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If account creation is not automatically audited, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-220476`

### Rule: The Cisco switch must be configured to automatically audit account modification.

**Rule ID:** `SV-220476r960780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account modification. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If account modification is not automatically audited, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-220477`

### Rule: The Cisco switch must be configured to automatically audit account disabling actions.

**Rule ID:** `SV-220477r960783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account disabling. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If account disabling is not automatically audited, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-220478`

### Rule: The Cisco switch must be configured to automatically audit account removal actions.

**Rule ID:** `SV-220478r960786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account removal. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If account removal is not automatically audited, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-220479`

### Rule: The Cisco switch must be configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies.

**Rule ID:** `SV-220479r991956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement. Step 1: Verify that the line vty has an ACL inbound applied as shown in the example below: line vty access-class MGMT_NET in Step 2: Verify that the ACL permits only hosts from the management network to access the switch. ip access-list MGMT_NET 10 permit ip 10.1.48.0/24 any 20 deny ip any any log NX-OS v8 and later example: Step 1: Verify that an ACL has been applied to the management interface inbound as shown in the example below: interface mgmt0 ip access-group MGMT_NET in Step 2: Verify that the ACL permits only hosts from the management network to access the switch. ip access-list MGMT_NET 10 permit ip 10.1.48.0/24 any 20 deny ip any any log If the Cisco switch is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-220480`

### Rule: The Cisco switch must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must disconnect the session.

**Rule ID:** `SV-220480r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it enforces the limit of three consecutive invalid logon attempts as shown in the example below: ssh login-attempts 3 If the Cisco switch is not configured to enforce the limit of three consecutive invalid logon attempts, this is a finding. NOTE: The NX-OS switch does not lock out the account, it disconnects the session. The AAA server will lock out the user account on three failed attempts.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-220481`

### Rule: The Cisco switch must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-220481r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: banner motd # You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. # If the Cisco switch is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-220482`

### Rule: The Cisco switch must be configured to protect against an individual falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-220482r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in steps below: Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If logging of administrator activity is not configured, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-220484`

### Rule: The Cisco switch must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-220484r1026067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the network device provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the deny statements in all ACLs to determine if the log parameter has been configured as shown in the example below: ip access-list extended BLOCK_INBOUND deny icmp any any log Step 2: Verify that the Optimized Access-list Logging (OAL) has been configured. logging ip access-list cache entries nnnn Note: Once OAL has been enabled, the logged ACL hits can be viewed via the show logging ip access-list cache command. If the switch is not configured with the log parameter after any deny statements to note where packets have been dropped via an ACL, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-220485`

### Rule: The Cisco switch must be configured to generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-220485r960909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If the Cisco switch is not configured to generate audit records of configuration changes, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-220486`

### Rule: The Cisco switch must be configured to prohibit the use of all unnecessary and nonsecure functions and services.

**Rule ID:** `SV-220486r1043177_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch does not have any unnecessary or non-secure ports, protocols and services enabled. For example, the following features such as telnet should never be enabled, while other features should only be enabled if required for operations. feature telnet feature dhcp feature wccp feature nxapi feature imp If any unnecessary or non-secure ports, protocols, or services are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-220487`

### Rule: The Cisco switch must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-220487r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. An alternative to using a sealed envelope in a safe would be credential files, separated by technology, located in a secured location on a file server, with the files only accessible to those administrators authorized to use the accounts of last resort, and access to that location monitored by a central log server. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the Cisco switch configuration to verify that a local account for last resort has been configured with a privilege level that will enable the administrator to troubleshoot connectivity to the authentication server. username xxxxxxxxxxxxx password 5 $5$88SPgpAn$Q6/17o5U/5lz4dNL1iQZuj/1a0wcKdrk29ZH1HJsnF. role priv-9 Step 2: Verify that the fallback to use local account has not been disabled as shown in the example below: no aaa authentication login default fallback error local Note: The fallback is enabled by default; hence the above command should not be seen in the configuration. If the Cisco switch is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-220488`

### Rule: The Cisco switch must be configured to implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-220488r1026069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify it is compliant with this requirement as shown in the example below. SSH Example ssh macs hmac-sha2-256 hmac-sha2-512 NOTE: Using "fips mode enable" to enable all FIPS protocols disables TACACS+ and RADIUS, which is required for authentication server requirements. It is recommended to enable FIPS-validated protocols manually and keep FIPS mode disabled. If the Cisco router is not configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-220489`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-220489r1026157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Password complexity is enabled by default. Review the Cisco switch configuration to verify that it is compliant with this requirement. The following command should not be found in the configuration: no password strength-check If the Cisco switch is not configured to enforce password complexity by requiring that at least one uppercase character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-220490`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-220490r1026158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Password complexity is enabled by default. Review the Cisco switch configuration to verify that it is compliant with this requirement. The following command should not be found in the configuration: no password strength-check If the Cisco switch is not configured to enforce password complexity by requiring that at least one lowercase character be used, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-220491`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-220491r1026159_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Password complexity is enabled by default. Review the Cisco switch configuration to verify that it is compliant with this requirement. The following command should not be found in the configuration: no password strength-check If the Cisco switch is not configured to enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-220492`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-220492r1026160_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Password complexity is enabled by default. Review the Cisco switch configuration to verify that it is compliant with this requirement. The following command should not be found in the configuration: no password strength-check If the Cisco switch is not configured to enforce password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-220493`

### Rule: The Cisco switch must be configured to terminate all network connections associated with device management after five minutes of inactivity.

**Rule ID:** `SV-220493r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that all network connections associated with a device management have an idle timeout value set to five minutes or less as shown in the following example: line console exec-timeout 5 line vty exec-timeout 5 If the Cisco switch is not configured to terminate all network connections associated with a device management after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-220494`

### Rule: The Cisco switch must be configured to automatically audit account enabling actions.

**Rule ID:** `SV-220494r961290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account enabling. The configuration should look similar to the example below: Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If account enabling is not automatically audited, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-220495`

### Rule: The Cisco switch must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-220495r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement. The configuration example below will log all configuration changes. Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If the Cisco switch is not configured to log all configuration changes, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-220496`

### Rule: The Cisco switch must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-220496r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Cisco switch is configured with a logfile size. The configuration should look like the example below: logging logfile LOGFILE1 6 size nnnnn If the Cisco switch is not configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-220497`

### Rule: The Cisco switch must be configured to generate an alert for all audit failure events.

**Rule ID:** `SV-220497r991965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: logging server 10.1.48.10 2 Note: The parameter 2 (critical) can replaced with a lesser severity level 3 through 6 (i.e. error, warning, notice, informational). Informational is the default severity level; hence, if the severity level is configured to informational, the parameter 7 will not be shown in the configuration. If the Cisco switch is not configured to generate an alert for all audit failure events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-220498`

### Rule: The Cisco switch must be configured to synchronize its clock with the primary and secondary time sources using redundant authoritative time sources.

**Rule ID:** `SV-220498r1026071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify it is compliant with this requirement as shown in the configuration example below: ntp server 10.1.12.10 ntp server 10.1.22.13 If the Cisco switch is not configured to synchronize its clock with redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-220499`

### Rule: The Cisco switch must be configured to record time stamps for log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-220499r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: clock timezone EST -5 0 Note: UTC is the default; hence, the command set time-zone may not be seen in the configuration. This can be verified using the show system uptime command. If the switch is not configured to record time stamps for log records that can be mapped to UTC or GMT, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-220500`

### Rule: The Cisco switch must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-220500r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: snmp-server user NETOPS auth sha 5Er23@#as178 priv aes-128 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx snmp-server host 10.1.48.10 traps version 3 priv NETOPS Authentication used by the SNMP users can be viewed via the show snmp user command as shown in the example below: SW1# show snmp user ______________________________________________________________ SNMP USERS ______________________________________________________________ User Auth Priv(enforce) Groups acl_filter ____ ____ ___________ ______ __________ NETOPS sha aes-128 network-operator If the Cisco switch is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-220501`

### Rule: The Cisco switch must be configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm.

**Rule ID:** `SV-220501r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the strong encryption that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information that can be used to create a network outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: snmp-server user NETOPS auth sha 5Er23@#as178 priv aes-128 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx snmp-server host 10.1.48.10 traps version 3 priv NETOPS Encryption used by the SNMP users can be viewed via the show snmp user command as shown in the example below: SW1# show snmp user ______________________________________________________________ SNMP USERS ______________________________________________________________ User Auth Priv(enforce) Groups acl_filter ____ ____ ___________ ______ __________ NETOPS sha aes-128 network-operator If the Cisco switch is not configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-220502`

### Rule: The Cisco switch must be configured to authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-220502r1107166_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the configuration example below: ntp distribute ntp server 10.1.12.10 key 1 ntp server 10.1.22.13 key 1 ntp authenticate ntp authentication-key 1 hmac-sha2-256 xxxxxx ntp trusted-key 1 ntp commit If the Cisco switch is not configured to authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-220503`

### Rule: The Cisco switch must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of remote maintenance sessions.

**Rule ID:** `SV-220503r1026073_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not verified; therefore, they cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify it is compliant with this requirement as shown in the example below. SSH Example ssh macs hmac-sha2-256 hmac-sha2-512 NOTE: Using "fips mode enable" to enable all FIPS protocols disables TACACS+ and RADIUS, which is required for authentication server requirements. It is recommended to enable FIPS-validated protocols manually and keep FIPS mode disabled. If the Cisco router is not configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-220504`

### Rule: The Cisco switch must be configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-220504r1026075_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco router configuration to verify it is compliant with this requirement. SSH Example ssh ciphers aes128-ctr aes256-ctr NOTE: Using "fips mode enable" to enable all FIPS protocols disables TACACS+ and RADIUS, which is required for authentication server requirements. It is recommended to enable FIPS-validated protocols manually and keep FIPS mode disabled. If the router is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-220506`

### Rule: The Cisco switch must be configured to generate log records when administrator privileges are modified.

**Rule ID:** `SV-220506r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If the Cisco switch is not configured to generate log records when administrator privileges are modified, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-220507`

### Rule: The Cisco switch must be configured to generate log records when administrator privileges are deleted.

**Rule ID:** `SV-220507r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If the Cisco switch is not configured to generate log records when administrator privileges are deleted, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-220508`

### Rule: The Cisco switch must be configured to generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-220508r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the examples below: logging logfile LOG_FILE 6 logging level authpri 6 If the Cisco switch is not configured to generate audit records when successful/unsuccessful logon attempts occur, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-220509`

### Rule: The Cisco switch must be configured to generate log records for privileged activities.

**Rule ID:** `SV-220509r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that account records will be sent to an AAA server as shown in the example below: aaa accounting default group RADIUS_SERVERS Step 2: Verify that the referenced group name has defined AAA servers that are online. aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.12 Note: Cisco NX-OS devices report configuration activity to TACACS+ or RADIUS servers in the form of accounting records. Each accounting record contains accounting attribute-value (AV) pairs and is stored on the AAA server. If the Cisco switch is not configured to generate log records for privileged activities, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-220510`

### Rule: The Cisco switch must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-220510r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured to generate log records showing starting and ending time for administrator access as shown in the example below: logging level authpri 6 If the switch is not configured to generate log records showing starting and ending time for administrator access, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-220512`

### Rule: The Cisco switch must be configured to off-load log records onto a different system than the system being audited.

**Rule ID:** `SV-220512r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement as shown in the example below: logging server 10.1.48.10 6 If the Cisco switch is not configured to off-load log records onto a different system than the system being audited, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-220513`

### Rule: The Cisco switch must be configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-220513r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of user accounts and authentication increases the administrative access to the switch. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that the device is configured to use at least two authentication servers as primary source for authentication. Step 1: Verify that an AAA server group is configured for login authentication for both in-band and console access methods. aaa authentication login default group RADIUS_SERVERS aaa authentication login console group RADIUS_SERVERS Step 2: Verify that at least two AAA servers have been defined for the server group as shown in the example below: radius-server host 10.1.48.10 key 7 "xxxxxx" radius-server host 10.1.48.11 key 7 "xxxxxx" authentication accounting aaa group server radius RADIUS_SERVERS server 10.1.48.10 server 10.1.48.11 If the Cisco switch is not configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-220514`

### Rule: The Cisco switch must be configured to support organizational requirements to conduct backups of the configuration when changes occur.

**Rule ID:** `SV-220514r1069522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is compliant with this requirement. The example configuration below will send the configuration to a SCP server when a configuration change occurs. event manager applet BACKUP_CONFIG event syslog pattern "SYSLOG_CONFIG_I" action 1 cli command "copy startup-config scp://user@10.1.48.10/nx-config.bak" action 2 syslog priority informational msg "Configuration backup was executed" If the Cisco switch is not configured to conduct backups of the configuration when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-220515`

### Rule: The Cisco switch must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-220515r991969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority (CA) at medium assurance or higher, this CA will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If PKI certificates are not implemented on the switch, this requirement is not applicable. Step 1: Review the switch configuration to determine if a CA trust point has been configured as shown in the example below: crypto ca trustpoint CA_X enrollment terminal Step 2: Verify the CA is a DOD or DOD-approved service provider by entering the following command: show crypto ca certificates The output will list the following information for each certificate: Trustpoint (will map to a configured trustpoint from step 1) Common Name (CN) of the issuer Organization (O) of the issuer Organization Unit (OU) of the issuer Note: Cisco NX-OS software supports only the manual cut-and-paste method for certificate enrollment. If the switch is not configured to obtain its public key certificates from a DOD or DOD-approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-220516`

### Rule: The Cisco switch must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-220516r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured to send logs to at least two syslog servers. The configuration should look similar to the example below: logging server 10.1.48.10 6 logging server 10.1.48.11 6 If the switch is not configured to send log data to the syslog servers, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-220517`

### Rule: The Cisco switch must be running an IOS release that is currently supported by Cisco Systems.

**Rule ID:** `SV-220517r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities. Running a supported release also enables operations to maintain a stable and reliable network provided by improved quality of service and security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is in compliance with this requirement by having the switch administrator enter the following command: show version Verify that the release is still supported by Cisco. All releases supported by Cisco can be found on the following URL: www.cisco.com/c/en/us/support/ios-nx-os-software If the switch is not running a supported release, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-260464`

### Rule: The Cisco switch must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-260464r1082186_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DOD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (e.g., firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify it is compliant with this requirement. Step 1: Verify traffic types have been classified based on importance levels. The following is an example configuration: class-map type control-plane match-all CoPP_CRITICAL match access-group name CoPP_CRITICAL class-map type control-plane match-any CoPP_IMPORTANT match access-group name CoPP_IMPORTANT match protocol arp class-map type control-plane match-all CoPP_NORMAL match access-group name CoPP_NORMAL class-map type control-plane match-any CoPP_UNDESIRABLE match access-group name CoPP_UNDESIRABLE class-map type control-plane match-all CoPP_DEFAULT match access-group name CoPP_DEFAULT Step 2: Review the ACLs referenced by the class maps to determine if the traffic is being classified appropriately. The following is an example configuration: ip access-list extended CoPP_CRITICAL remark our control plane adjacencies are critical permit ospf host [OSPF neighbor A] any permit ospf host [OSPF neighbor B] any permit pim host [PIM neighbor A] any permit pim host [PIM neighbor B] any permit pim host [RP addr] any permit igmp any 224.0.0.0 15.255.255.255 permit tcp host [BGP neighbor] eq bgp host [local BGP addr] permit tcp host [BGP neighbor] host [local BGP addr] eq bgp deny ip any any ip access-list extended CoPP_IMPORTANT permit tcp host [TACACS server] eq tacacs any permit tcp [management subnet] 0.0.0.255 any eq 22 permit udp host [SNMP manager] any eq snmp permit udp host [NTP server] eq ntp any deny ip any any ip access-list extended CoPP_NORMAL remark we will want to rate limit ICMP traffic permit icmp any any echo permit icmp any any echo-reply permit icmp any any time-exceeded permit icmp any any unreachable deny ip any any ip access-list extended CoPP_UNDESIRABLE remark other management plane traffic that should not be received permit udp any any eq ntp permit udp any any eq snmp permit tcp any any eq 22 permit tcp any any eq 23 remark other control plane traffic not configured on switch permit eigrp any any permit udp any any eq rip deny ip any any ip access-list extended CoPP_DEFAULT permit ip any any Note: Explicitly defining undesirable traffic with ACL entries enables the network operator to collect statistics. Excessive ARP packets can potentially monopolize Route Processor resources, starving other important processes. Currently, ARP is the only Layer 2 protocol that can be specifically classified using the match protocol command. Step 3: Review the policy-map type control-plane to determine if the traffic is being policed appropriately for each classification. The following is an example configuration: policy-map type control-plane CONTROL_PLANE_POLICY class CoPP_CRITICAL police 512000 8000 conform-action transmit exceed-action transmit class CoPP_IMPORTANT police 256000 4000 conform-action transmit exceed-action drop class CoPP_NORMAL police 128000 2000 conform-action transmit exceed-action drop class CoPP_UNDESIRABLE police 8000 1000 conform-action drop exceed-action drop class CoPP_DEFAULT police 64000 1000 conform-action transmit exceed-action drop Step 4: Verify the CoPP policy is enabled. The following is an example configuration: control-plane service-policy input CONTROL_PLANE_POLICY If the Cisco switch is not configured to protect against known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

