# STIG Benchmark: Cisco IOS Switch NDM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-220570`

### Rule: The Cisco switch must be configured to limit the number of concurrent management sessions to an organization-defined number.

**Rule ID:** `SV-220570r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is not applicable to file transfer actions such as FTP, SCP, and SFTP. Review the switch configuration to determine if concurrent management sessions are limited as show in the example below: ip http secure-server ip http max-connections 2 … … … For platforms that support the session-limit command: line vty 0 4 session-limit 2 transport input ssh For platforms that do not support the session-limit command, the sessions can also be limited by reducing the number of active vty lines as shown in the example below: line vty 0 1 transport input ssh line vty 2 4 transport input none If the switch is not configured to limit the number of concurrent management sessions, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-220571`

### Rule: The Cisco switch must be configured to automatically audit account creation.

**Rule ID:** `SV-220571r879525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account creation. The configuration should look similar to the example below: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If account creation is not automatically audited, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-220572`

### Rule: The Cisco switch must be configured to automatically audit account modification.

**Rule ID:** `SV-220572r879526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Because the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification, along with an automatic notification to appropriate individuals, will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account modification. The configuration should look similar to the example below: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If account modification is not automatically audited, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-220573`

### Rule: The Cisco switch must be configured to automatically audit account disabling actions.

**Rule ID:** `SV-220573r879527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account disabling. The configuration should look similar to the example below: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If account disabling is not automatically audited, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-220574`

### Rule: The Cisco switch must be configured to automatically audit account removal actions.

**Rule ID:** `SV-220574r879528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account removal. The configuration should look similar to the example below: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If account removal is not automatically audited, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-220575`

### Rule: The Cisco switch must be configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies.

**Rule ID:** `SV-220575r879533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that administrative access to the switch is allowed only from hosts residing in the management network. Step 1: Verify that the line vty has an ACL inbound applied as shown in the example below: line vty 0 1 access-class MANAGEMENT_NET in transport input ssh Step 2: Verify that the ACL permits only hosts from the management network to access the switch. iip access-list extended MANAGEMENT_NET permit ip x.x.x.0 0.0.0.255 any deny ip any any log-input If the Cisco switch is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-220576`

### Rule: The Cisco switch must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-220576r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it enforces the limit of three consecutive invalid logon attempts as shown in the example below: login block-for 900 attempts 3 within 120 Note: The configuration example above will block any logon attempt for 15 minutes after three consecutive invalid logon attempts within a two-minute period. If the Cisco switch is not configured to enforce the limit of three consecutive invalid logon attempts, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-220577`

### Rule: The Cisco switch must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-220577r879547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the device as shown in the example below: banner login ^C You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. ^C If the Cisco switch is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-220578`

### Rule: The Cisco device must be configured to audit all administrator activity.

**Rule ID:** `SV-220578r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it logs administrator activity as shown in the example below: hostname R1 ! logging userinfo ! … … … archive log config logging enable ! Note: The logging userinfo global configuration command will generate a log when a user increases his or her privilege level. If logging of administrator activity is not configured, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-220580`

### Rule: The Cisco switch must produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-220580r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network device. To establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured to include the date and time on all log records as shown in the configuration example below: service timestamps log datetime localtime If time stamps are not configured, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-220581`

### Rule: The Cisco switch must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-220581r929020_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the network device provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the deny statements in all interface ACLs to determine if the log-input parameter has been configured as shown in the example below. Note: log-input can only apply to interface bound ACLs. ip access-list extended BLOCK_INBOUND deny icmp any any log-input If the switch is not configured with the log-input parameter after any deny statements to note where packets have been dropped via an ACL, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-220582`

### Rule: The Cisco switch must be configured to generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-220582r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it generates audit records of configuration changes. The configuration example below will log all configuration changes: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If the Cisco switch is not configured to generate audit records of configuration changes, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-220583`

### Rule: The Cisco switch must be configured to protect audit information from unauthorized modification.

**Rule ID:** `SV-220583r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, forensic analysis and discovery of the true source of potentially malicious system activity would be impossible. To ensure the veracity of audit data, the network device must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend on system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding user rights to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it is configured to protect audit information. Step 1: If persistent logging is enabled as shown in the example below, go to Step 2. Otherwise, this requirement is not applicable. logging persistent url disk0:/logfile size 134217728 filesize 16384 Step 2: Verify that the switch is not configured with a privilege level other than "15" to allow access to the file system as shown in the example below: file privilege 10 Note: The default privilege level required for access to the file system is "15"; hence, the command file privilege "15" will not be shown in the configuration. If the switch is configured with a privilege level other than "15" to allow access to the file system, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-220584`

### Rule: The Cisco switch must be configured to protect audit information from unauthorized deletion.

**Rule ID:** `SV-220584r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, forensic analysis and discovery of the true source of potentially malicious system activity would be impossible. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend on system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions using file system protections, restricting access, and backing up log data to ensure it is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding user rights to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it protects audit information from unauthorized deletion. Step 1: If persistent logging is enabled as shown in the example below, go to Step 2. Otherwise, this requirement is not applicable. logging persistent url disk0:/logfile size 134217728 filesize 16384 Step 2: Verify that the switch is not configured with a privilege level other than "15" to allow access to the file system as shown in the example below: file privilege 10 Note: The default privilege level required for access to the file system is "15"; hence, the command file privilege "15" will not be shown in the configuration. If the switch is configured with a privilege level other than "15" to allow access to the file system, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-220585`

### Rule: The Cisco switch must be configured to limit privileges to change the software resident within software libraries.

**Rule ID:** `SV-220585r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. If the network device were to enable unauthorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it limits software change privileges. Step 1: If persistent logging is enabled as shown in the example below, go to Step 2. Otherwise, this requirement is not applicable. logging persistent url disk0:/logfile size 134217728 filesize 16384 Step 2: Verify that the switch is not configured with a privilege level other than "15" to allow access to the file system as shown in the example below: file privilege 10 Note: The default privilege level required for access to the file system is "15"; hence, the command file privilege "15" will not be shown in the configuration. If the switch is configured with a privilege level other than "15" to allow access to the file system, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-220586`

### Rule: The Cisco switch must be configured to prohibit the use of all unnecessary and non-secure functions and services.

**Rule ID:** `SV-220586r892388_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch does not have any unnecessary or nonsecure ports, protocols, and services enabled. For example, the following commands should not be in the configuration: boot network ip boot server ip bootp server ip dns server ip identd ip finger ip http server ip rcmd rcp-enable ip rcmd rsh-enable service config service finger service tcp-small-servers service udp-small-servers service pad service call-home If any unnecessary or nonsecure ports, protocols, or services are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-220587`

### Rule: The Cisco switch must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-220587r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. An alternative to using a sealed envelope in a safe would be credential files, separated by technology, located in a secured location on a file server, with the files only accessible to those administrators authorized to use the accounts of last resort, and access to that location monitored by a central log server. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the Cisco switch configuration to verify that a local account for last resort has been configured with a privilege level that will enable the administrator to troubleshoot connectivity to the authentication server. username xxxxxxxxxxx privilege 10 common-criteria-policy PASSWORD_POLICY password xxxxxxxxxx Note: The configured Common Criteria policy must be used when creating or changing the local account password as shown in the example above. Step 2: Verify that local is defined after radius or tacacs+ in the authentication order as shown in the example below: aaa authentication login default group tacacs+ local If the Cisco switch is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-220589`

### Rule: The Cisco switch must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-220589r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it enforces a minimum 15-character password length as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY min-length 15 If the Cisco switch is not configured to enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-220590`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-220590r879603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it requires the use of at least one upper-case character as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY upper-case 1 If the Cisco switch is not configured to enforce password complexity by requiring that at least one upper-case character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-220591`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-220591r879604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it requires the use of at least one lower-case character as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY lower-case 1 If the Cisco switch is not configured to enforce password complexity by requiring that at least one lower-case character be used, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-220592`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-220592r879605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it requires the use of at least one numeric character as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY numeric-count 1 If the Cisco switch is not configured to enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-220593`

### Rule: The Cisco switch must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-220593r879606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it requires the use of at least one special character as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY special-case 1 If the Cisco switch is not configured to enforce password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-220594`

### Rule: The Cisco switch must be configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-220594r879607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that, when a password is changed, it requires the characters to be changed in at least eight of the positions as shown in the example below: aaa new-model ! ! aaa common-criteria policy PASSWORD_POLICY char-changes 8 If the Cisco switch is not configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password, this is a finding.

## Group: SRG-APP-000171-NDM-000258

**Group ID:** `V-220595`

### Rule: The Cisco switch must only store cryptographic representations of passwords.

**Rule ID:** `SV-220595r879608_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices must enforce cryptographic representations of passwords when storing passwords in databases, configuration files, and log files. Passwords must be protected at all times; using a strong one-way hashing encryption algorithm with a salt is the standard method for providing a means to validate a password without having to store the actual password. Performance and time required to access are factors that must be considered, and the one-way hash is the most feasible means of securing the password and providing an acceptable measure of password security. If passwords are stored in clear text, they can be plainly read and easily compromised. In many instances, verification that the user knows a password is performed using a password verifier. In its simplest form, a password verifier is a computational function that is capable of creating a hash of a password and determining if the value provided by the user matches the stored hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if passwords are encrypted as shown in the example below: service password-encryption … … … Enable secret 5 xxxxxxxxxxxxxxxxxxxxxxxxxx If the switch is not configured to encrypt passwords, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-220596`

### Rule: The Cisco switch must be configured to terminate all network connections associated with device management after five minutes of inactivity.

**Rule ID:** `SV-220596r916342_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that all network connections associated with a device management have an idle timeout value set to five minutes or less as shown in the example below: ip http secure-server ip http timeout-policy idle 300 life nnnn requests nn … … … line con 0 exec-timeout 5 0 line vty 0 1 exec-timeout 5 0 If the Cisco switch is not configured to terminate all network connections associated with a device management after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-220597`

### Rule: The Cisco switch must be configured to automatically audit account enabling actions.

**Rule ID:** `SV-220597r879696_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSOs). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it automatically audits account enabling. The configuration should look similar to the example below: archive log config logging enable Note: Configuration changes can be viewed using the show archive log config all command. If account enabling is not automatically audited, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-220599`

### Rule: The Cisco switch must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-220599r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure that network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Cisco switch is configured with a logging buffer size. The configuration should look like the example below: logging buffered xxxxxxxx informational If a logging buffer size is not configured, this is a finding. If the Cisco switch is not configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-220600`

### Rule: The Cisco switch must be configured to generate an alert for all audit failure events.

**Rule ID:** `SV-220600r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it generates an alert for all audit failure events as shown in the example below: logging trap critical Note: The parameter "critical" can replaced with a lesser severity level (i.e., error, warning, notice, informational). Informational is the default severity level; hence, if the severity level is configured to informational, the logging trap command will not be shown in the configuration. If the Cisco switch is not configured to generate an alert for all audit failure events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-220601`

### Rule: The Cisco switch must be configured to synchronize its clock with the primary and secondary time sources using redundant authoritative time sources.

**Rule ID:** `SV-220601r879746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it synchronizes its clock with redundant authoritative time sources as shown in the example below: ntp server x.x.x.x ntp server y.y.y.y If the Cisco switch is not configured to synchronize its clock with redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-220604`

### Rule: The Cisco switch must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-220604r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it authenticates SNMP messages using a FIPS-validated HMAC as shown in the example below: snmp-server group V3GROUP v3 auth read V3READ write V3WRITE snmp-server view V3READ iso included snmp-server view V3WRITE iso included snmp-server host x.x.x.x version 3 auth V3USER Authentication used by the SNMP users can be viewed via the show snmp user command as shown in the example below: R4#show snmp user User name: V3USER Engine ID: 800000090300C2042B540000 storage-type: nonvolatile active Authentication Protocol: SHA Privacy Protocol: None Group-name: V3GROUP If the Cisco switch is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-220605`

### Rule: The Cisco switch must be configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm.

**Rule ID:** `SV-220605r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the strong encryption that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information that can be used to create a network outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it encrypts SNMP messages using a FIPS 140-2 approved algorithm as shown in the example below: snmp-server group V3GROUP v3 priv read V3READ write V3WRITE snmp-server view V3READ iso included snmp-server view V3WRITE iso included snmp-server host x.x.x.x version 3 auth V3USER Encryption used by the SNMP users can be viewed via the show snmp user command as shown in the example below: R4#show snmp user User name: V3USER Engine ID: 800000090300C2042B540000 storage-type: nonvolatile active Authentication Protocol: SHA Privacy Protocol: AES256 Group-name: V3GROUP If the Cisco switch is not configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-220606`

### Rule: The Cisco switch must be configured to authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-220606r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If NTP is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it authenticates NTP sources using cryptographically based authentication as shown in the configuration example below: ntp authentication-key 1 md5 121B0A151012 7 ntp authenticate ntp trusted-key 1 ntp server x.x.x.x key 1 ntp server y.y.y.y key 1 If the Cisco switch is not configured to authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-220607`

### Rule: The Cisco switch must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of remote maintenance sessions.

**Rule ID:** `SV-220607r879784_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied on to provide confidentiality or integrity, and DoD data may be compromised. Non-local maintenance and diagnostic activities are conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it uses FIPS-validated HMAC to protect the integrity of remote maintenance sessions as shown in the example below: NOTE: Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and Government standards. Unless required for legacy use, DoD systems should not be configured to use SHA-1 for integrity of remote access sessions. SSH Example ip ssh version 2 ip ssh server algorithm mac hmac-sha2-512 hmac-sha2-256 If the Cisco switch is not configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-220608`

### Rule: The Cisco switch must be configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-220608r879785_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it implements cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm as shown in the example below: ip ssh version 2 ip ssh server algorithm encryption aes256-ctr aes192-ctr aes128-ctr If the switch is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-220609`

### Rule: The Cisco switch must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-220609r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (e.g., firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it protects against known types of DoS attacks by employing organization-defined security safeguards. Step 1: Verify traffic types have been classified based on importance levels. The following is an example configuration: class-map match-all CoPP_CRITICAL match access-group name CoPP_CRITICAL class-map match-any CoPP_IMPORTANT match access-group name CoPP_IMPORTANT match protocol arp class-map match-all CoPP_NORMAL match access-group name CoPP_NORMAL class-map match-any CoPP_UNDESIRABLE match access-group name CoPP_UNDESIRABLE class-map match-all CoPP_DEFAULT match access-group name CoPP_DEFAULT Step 2: Review the access control lists (ACLs) referenced by the class-maps to determine if the traffic is being classified appropriately. The following is an example configuration: ip access-list extended CoPP_CRITICAL remark our control plane adjacencies are critical permit ospf host [OSPF neighbor A] any permit ospf host [OSPF neighbor B] any permit pim host [PIM neighbor A] any permit pim host [PIM neighbor B] any permit pim host [RP addr] any permit igmp any 224.0.0.0 15.255.255.255 permit tcp host [BGP neighbor] eq bgp host [local BGP addr] permit tcp host [BGP neighbor] host [local BGP addr] eq bgp deny ip any any ip access-list extended CoPP_IMPORTANT permit tcp host [TACACS server] eq tacacs any permit tcp [management subnet] 0.0.0.255 any eq 22 permit udp host [SNMP manager] any eq snmp permit udp host [NTP server] eq ntp any deny ip any any ip access-list extended CoPP_NORMAL remark we will want to rate limit ICMP traffic permit icmp any any echo permit icmp any any echo-reply permit icmp any any time-exceeded permit icmp any any unreachable deny ip any any ip access-list extended CoPP_UNDESIRABLE remark other management plane traffic that should not be received permit udp any any eq ntp permit udp any any eq snmp permit tcp any any eq 22 permit tcp any any eq 23 remark other control plane traffic not configured on switch permit eigrp any any permit udp any any eq rip deny ip any any ip access-list extended CoPP_DEFAULT permit ip any any Note: Explicitly defining undesirable traffic with ACL entries enables the network operator to collect statistics. Excessive Address Resolution Protocol (ARP) packets can potentially monopolize Route Processor resources, starving other important processes. Currently, ARP is the only Layer 2 protocol that can be specifically classified using the match protocol command. Step 3: Review the policy-map to determine if the traffic is being policed appropriately for each classification. The following is an example configuration: policy-map CONTROL_PLANE_POLICY class CoPP_CRITICAL police 512000 8000 conform-action transmit exceed-action transmit class CoPP_IMPORTANT police 256000 4000 conform-action transmit exceed-action drop class CoPP_NORMAL police 128000 2000 conform-action transmit exceed-action drop class CoPP_UNDESIRABLE police 8000 1000 conform-action drop exceed-action drop class CoPP_DEFAULT police 64000 1000 conform-action transmit exceed-action drop Step 4: Verify that the Control Plane Policing (CoPP) policy is enabled. The following is an example configuration: control-plane service-policy input CONTROL_PLANE_POLICY Note: Control Plane Protection (CPPr) can be used to filter as well as police control plane traffic destined to the RP. CPPr is very similar to CoPP and has the ability to filter and police traffic using finer granularity by dividing the aggregate control plane into three separate categories: 1) host, 2) transit, and 3) CEF-exception. Hence, a separate policy-map could be configured for each traffic category. If the Cisco switch is not configured to protect against known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-220611`

### Rule: The Cisco switch must be configured to generate log records when administrator privileges are deleted.

**Rule ID:** `SV-220611r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it generates log records when administrator privileges are deleted as shown in the example below: archive log config logging enable If the Cisco switch is not configured to generate log records when administrator privileges are deleted, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-220612`

### Rule: The Cisco switch must be configured to generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-220612r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it generates audit records when successful/unsuccessful logon attempts occur as shown in the examples below: login on-failure log login on-success log If the Cisco switch is not configured to generate audit records when successful/unsuccessful logon attempts occur, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-220613`

### Rule: The Cisco switch must be configured to generate log records for privileged activities.

**Rule ID:** `SV-220613r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it generates log records for privileged activities as shown in the example configurations below: archive log config logging enable If the Cisco switch is not configured to generate log records for privileged activities, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-220617`

### Rule: The Cisco switch must be configured to use at least two authentication servers to authenticate users prior to granting administrative access.

**Rule ID:** `SV-220617r939989_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of user accounts and authentication increases the administrative access to the switch. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that the device is configured to use at least two authentication servers as the primary source for authentication as shown in the example below: aaa new-model ! aaa authentication CONSOLE local aaa authentication login LOGIN_AUTHENTICATION group radius local … … … ip http authentication aaa login-authentication LOGIN_AUTHENTICATION ip http secure-server … … … radius-server host x.x.x.x auth-port 1812 acct-port 1813 key xxxxxxx radius-server host x.x.x.x auth-port 1812 acct-port 1813 key xxxxxxx … … … line con 0 exec-timeout 5 0 login authentication CONSOLE line vty 0 1 exec-timeout 5 0 login authentication LOGIN_AUTHENTICATION If the Cisco switch is not configured to use at least two authentication servers to authenticate users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-220618`

### Rule: The Cisco switch must be configured to support organizational requirements to conduct backups of the configuration when changes occur.

**Rule ID:** `SV-220618r916221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including access control lists (ACLs) that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who use this critical network component. The network device must support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify that it backs up the configuration when changes occur. The example configuration below will send the configuration to a TFTP server when a configuration change occurs: event manager applet BACKUP_CONFIG event syslog pattern "%SYS-5-CONFIG_I" action 1 info type switchname action 2 cli command "enable" action 3 cli command "copy run tftp" pattern "remote host" action 4 cli command "x.x.x.x" pattern "filename" action 5 cli command "$_info_switchname-config" action 6 syslog priority informational msg "Configuration backup was executed" If the Cisco switch is not configured to conduct backups of the configuration when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-220619`

### Rule: The Cisco switch must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-220619r949114_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Each organization obtains user certificates from an approved, shared service provider as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority (CA) at medium assurance or higher, this CA will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is not applicable if the router or switch does not have any public key certificates. Review the switch configuration to determine if a CA trust point has been configured. The CA trust point will contain the URL of the CA in which the switch has enrolled. Verify this is a DoD or DoD-approved CA. This will ensure the switch has enrolled and received a certificate from a trusted CA. The CA trust point configuration would look similar to the example below: crypto pki trustpoint CA_X enrollment url http://trustpoint1.example.com Note: A remote endpoint's certificate will always be validated by the switch by verifying the signature of the CA on the certificate using the CA's public key, which is contained in the switch's certificate that it received at enrollment. If the Cisco switch is not configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-220620`

### Rule: The Cisco switch must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-220620r916114_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network Information Assurance (IA) team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, is important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured to send logs to at least two central log servers. The configuration should be similar to the example below: logging x.x.x.x logging x.x.x.x If the switch is not configured to send log data to the syslog servers, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-220621`

### Rule: The Cisco switch must be running an IOS release that is currently supported by Cisco Systems.

**Rule ID:** `SV-220621r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities. Running a supported release enables operations to maintain a stable and reliable network provided by improved quality of service and security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is in compliance with this requirement by having the switch administrator enter the following command: show version Verify that the release is still supported by Cisco. All releases supported by Cisco can be found at: www.cisco.com/c/en/us/support/ios-nx-os-software If the switch is not running a supported release, this is a finding.

