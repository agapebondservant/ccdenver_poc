# STIG Benchmark: Cisco ASA NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-239896`

### Rule: The Cisco ASA must be configured to limit the number of concurrent management sessions to an organization-defined number.

**Rule ID:** `SV-239896r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if concurrent management sessions are limited as show in the example below: quota management-session 2 Note: This requirement is not applicable to file transfer actions such as FTP, SCP, and SFTP. The default is 5 sessions, which would not be shown in the configuration unless the show run all command is used. If the ASA is not configured to limit the number of concurrent management sessions, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-239897`

### Rule: The Cisco ASA must be configured to automatically audit account creation.

**Rule ID:** `SV-239897r879525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if it automatically audits account creation. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If account creation is not automatically audited, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-239898`

### Rule: The Cisco ASA must be configured to automatically audit account modification.

**Rule ID:** `SV-239898r879526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if it automatically audits account modification. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If account modification is not automatically audited, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-239899`

### Rule: The Cisco ASA must be configured to automatically audit account-disabling actions.

**Rule ID:** `SV-239899r879527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if it automatically audits account disabling. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If account disabling is not automatically audited, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-239900`

### Rule: The Cisco ASA must be configured to automatically audit account removal actions.

**Rule ID:** `SV-239900r879528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if it automatically audits account removal. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If account removal is not automatically audited, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-239901`

### Rule: The Cisco ASA must be configured to enforce approved authorizations for controlling the flow of management information within the Cisco ASA based on information flow control policies.

**Rule ID:** `SV-239901r879533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that management access is restricted to specific IP address space as shown in the example below. ssh x.x.x.0 255.255.255.0 INSIDE If the Cisco ASA is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-239902`

### Rule: The Cisco ASA must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-239902r879547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement as shown in the example below. banner login You are accessing a U.S. Government (USG) Information System (IS) that is provided banner login for USG-authorized use only. banner login banner login By using this IS (which includes any device attached to this IS), you consent to the banner login following conditions: banner login banner login -The USG routinely intercepts and monitors communications on this IS for purposes banner login including, but not limited to, penetration testing, COMSEC monitoring, network banner login operations and defense, personnel misconduct (PM), law enforcement (LE), and banner login counterintelligence (CI) investigations. banner login banner login -At any time, the USG may inspect and seize data stored on this IS. banner login banner login -Communications using, or data stored on, this IS are not private, are subject to routine banner login monitoring, interception, and search, and may be disclosed or used for any USG- banner login authorized purpose. banner login banner login -This IS includes security measures (e.g., authentication and access controls) to protect banner login USG interests--not for your personal benefit or privacy. banner login banner login -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI banner login investigative searching or monitoring of the content of privileged communications, or banner login work product, related to personal representation or services by attorneys, banner login psychotherapists, or clergy, and their assistants. Such communications and work product banner login are private and banner login confidential. See User Agreement for details. If the Cisco ASA is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-239903`

### Rule: The Cisco ASA must be configured to protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-239903r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands that include the name of the user. The ASA also logs the name of the user entering the enable command. If logging of administrator activity is not configured, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-239904`

### Rule: The Cisco ASA must be configured to generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-239904r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log all login attempts as well as the name of the user entering the enable command. If the Cisco ASA is not configured to generate audit records when successful/unsuccessful attempts to logon, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-239905`

### Rule: The Cisco ASA must be configured to produce audit log records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-239905r879563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational If the ASA is not configured to generate audit records containing information to establish what type of event occurred, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-239906`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-239906r879564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. In order to establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ASA is configured to include the date and time on all log records as shown in the configuration example below. logging timestamp If time stamp is not configured, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-239907`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-239907r879565_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the network device provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log location (IP address or console) from where configuration commands are entered. If the ASA is not configured to generate audit records containing information to establish where the events occurred, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-239908`

### Rule: The Cisco ASA must be configured to produce audit log records containing information to establish the source of events.

**Rule ID:** `SV-239908r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Associating information about where the source of the event occurred provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log location (IP address or console) from where configuration commands are entered. If the ASA is not configured to generate audit records containing information to establish the source of events, this is a finding.

## Group: SRG-APP-000099-NDM-000229

**Group ID:** `V-239909`

### Rule: The Cisco ASA must be configured to produce audit records that contain information to establish the outcome of the event.

**Rule ID:** `SV-239909r879567_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the device after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational If the ASA is not configured to generate audit records containing information to establish the outcome of the event, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-239910`

### Rule: The Cisco ASA must be configured to generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-239910r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration should look similar to the example below: logging enable logging buffered informational Note: The ASA will log full-text recording of privileged commands. If the Cisco ASA is not configured to generate audit records containing the full-text recording of privileged commands, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-239911`

### Rule: The Cisco ASA must be configured to prohibit the use of all unnecessary and/or non-secure functions, ports, protocols, and/or services.

**Rule ID:** `SV-239911r879588_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA does not have any unnecessary or non-secure ports, protocols, and services enabled. For example, the following features such as telnet should never be enabled, while other features should only be enabled if required for operations. In the example below, http and telnet service are enabled. http server enable … … … telnet 10.1.22.2 255.255.255.255 INSIDE Note: The command http server enables https and is required for ASDM. If any unnecessary or non-secure ports, protocols, or services are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-239912`

### Rule: The Cisco ASA must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-239912r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the Cisco ASA configuration to verify that a local account for last resort has been configured with a privilege level that will enable the administrator to troubleshoot connectivity to the authentication server. username LAST_RESORT password $sha512$5000$tb2eaIcI/Q5Q==$ScFJI1ChS4gIjXw== pbkdf2 privilege 15 Step 2: Verify the fallback to use local account has been configured as shown in the example below. user-identity default-domain LOCAL aaa authentication serial console RADIUS_GROUP LOCAL aaa authentication ssh console RADIUS_GROUP LOCAL If the Cisco ASA is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-239913`

### Rule: The Cisco ASA must be configured to implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-239913r879597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that FIPS mode is enabled as shown in the example. fips enable Step 2: Verify only SSH is configured to only use FIPS-compliant ciphers and that Diffie-Hellman Group 14 is used for the key exchange as shown in the example below. ssh version 2 ssh cipher encryption fips ssh key-exchange group dh-group14-sha1 Note: The ASA only supports SSHv2. If the ASA is not configured to implement replay-resistant authentication mechanisms for network access, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-239914`

### Rule: The Cisco ASA must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-239914r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it is compliant with this requirement as shown in the example below. password-policy minimum-length 15 If the ASA is not configured to enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-239915`

### Rule: The Cisco ASA must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-239915r879603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it is compliant with this requirement as shown in the example below. password-policy minimum-uppercase 1 If the Cisco ASA is not configured to enforce password complexity by requiring that at least one uppercase character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-239916`

### Rule: The Cisco ASA must be configured to enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-239916r879604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it is compliant with this requirement as shown in the example below. password-policy minimum-lowercase 1 If the Cisco ASA is not configured to enforce password complexity by requiring that at least one lowercase character be used, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-239917`

### Rule: The Cisco ASA must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-239917r879605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it is compliant with this requirement as shown in the example below. password-policy minimum-numeric 1 If the Cisco ASA is not configured to enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-239918`

### Rule: The Cisco ASA must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-239918r879606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it is compliant with this requirement as shown in the example below. password-policy minimum-special 1 If the Cisco ASA is not configured to enforce password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-239919`

### Rule: The Cisco ASA must be configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-239919r879607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify it is compliant with this requirement as shown in the example below. password-policy minimum-changes 8 If the Cisco router is not configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-239920`

### Rule: The Cisco ASA must be configured to terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after five minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-239920r916342_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify all network connections associated with a device management have an idle timeout value set to five minutes or less as shown in the following example: http server idle-timeout 5 … … … ssh timeout 5 … … … console timeout 5 If the Cisco ASA is not configured to terminate all network connections associated with a device management after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-239921`

### Rule: The Cisco ASA must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-239921r879720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement. The configuration example below will log all configuration changes. logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If the Cisco ASA is not configured to log all configuration changes, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-239922`

### Rule: The Cisco ASA must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-239922r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Cisco ASA is configured with a logfile size. The configuration should look like the example below. logging flash-bufferwrap logging flash-minimum-free nnnnnnn logging flash-maximum-allocation nnnnnnn If the Cisco ASA is not configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-239923`

### Rule: The Cisco ASA must be configured to generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-239923r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement as shown in the example below. logging trap critical logging host NDM_INTERFACE 10.1.48.10 Note: The parameter critical can replaced with a lesser severity (i.e., error, warning, notice, informational). A logging list can be used as an alternative to the severity level. If the Cisco ASA is not configured to generate an alert for all audit failure events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-239924`

### Rule: The Cisco ASA must be configured to synchronize its clock with the primary and secondary time sources using redundant authoritative time sources.

**Rule ID:** `SV-239924r891333_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement as shown in the configuration example below. ntp server 10.1.22.2 ntp server 10.1.48.8 prefer Note: For ASAs running on Firepower Chassis hardware, the NTP settings are visible in the FXOS web UI only (not in the ASA CLI or ASDM web UI). If the Cisco ASA is not configured to synchronize its clock with redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-239925`

### Rule: The Cisco ASA must be configured to record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-239925r879748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is configured to include the time on all log records as shown in the configuration example below. logging timestamp If time stamp is not configured, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-239927`

### Rule: The Cisco ASA must be configured to authenticate Simple Network Management Protocol (SNMP) messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-239927r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement as shown in the example below. snmp-server group NETOPS v3 priv snmp-server user FWADMIN NETOPS v3 engineID xxxxxxxxxxxx encrypted auth sha xxxxxxxxxxxxxxxx snmp-server host NDM_INTERFACE 10.1.48.10 version 3 FWADMIN If the Cisco ASA is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-239928`

### Rule: The Cisco ASA must be configured to encrypt Simple Network Management Protocol (SNMP) messages using a FIPS 140-2 approved algorithm.

**Rule ID:** `SV-239928r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement as shown in the example below. snmp-server group NETOPS v3 priv snmp-server user FWADMIN NETOPS v3 engineID xxxxxxxxxxxx encrypted auth sha xxxxxxxxxxxx priv aes xxxxxxxxxxxx snmp-server host NDM_INTERFACE 10.1.48.10 version 3 FWADMIN If the Cisco ASA is not configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-239929`

### Rule: The Cisco ASA must be configured to authenticate Network Time Protocol sources using authentication that is cryptographically based.

**Rule ID:** `SV-239929r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement as shown in the configuration example below. ntp authentication-key 1 md5 ***** ntp authenticate ntp trusted-key 1 ntp server 10.1.12.2 key 1 prefer ntp server 10.1.48.10 key 1 Note: For ASAs running on Firepower Chassis hardware, the NTP settings are visible in the FXOS web UI only (not in the ASA CLI or ASDM web UI). If the Cisco ASA is not configured to authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-239930`

### Rule: The Cisco ASA must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of non-local maintenance and diagnostic communications.

**Rule ID:** `SV-239930r879784_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Non-local maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
SSH Example Step 1: Verify that FIPS mode is enabled as shown in the example below. fips enable Step 2: Verify that SSH is configured to only use FIPS-compliant ciphers and that Diffie-Hellman Group 14 is used for the key exchange as shown in the example below. ssh version 2 ssh cipher encryption fips ssh key-exchange group dh-group14-sha1 Note: The ASA only supports SSHv2. SNMP Example snmp-server group NETOPS v3 auth snmp-server user FWADMIN NETOPS v3 engineID xxxxxxxxxxxx encrypted auth sha xxxxxxxxxxxxxxxx snmp-server host NDM_INTERFACE 10.1.48.10 version 3 FWADMIN If the ASA is not configured to implement cryptographic mechanisms to protect the integrity of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-239931`

### Rule: The Cisco ASA must be configured to implement cryptographic mechanisms using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-239931r879785_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify FIPS mode is enabled as shown in the example below. fips enable Step 2: Verify that only SSH is configured to only use FIPS-compliant ciphers and that Diffie-Hellman Group 14 is used for the key exchange as shown in the example below. ssh version 2 ssh cipher encryption fips ssh key-exchange group dh-group14-sha1 Note: The ASA only supports SSHv2. If the ASA is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-239932`

### Rule: The Cisco ASA must be configured to protect against known types of denial-of-service (DoS) attacks by enabling the Threat Detection feature.

**Rule ID:** `SV-239932r929026_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: When operating the ASA in multi-context mode with a separate IDPS, threat detection cannot be enabled, and this check is Not Applicable. Review the ASA configuration and verify the Threat Detection feature is enabled as shown in the example below. threat-detection basic-threat If the Cisco ASA does not have the Threat Detection feature enabled, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-239933`

### Rule: The Cisco ASA must be configured to generate audit records when successful/unsuccessful attempts to modify administrator privileges occur.

**Rule ID:** `SV-239933r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If the Cisco ASA is not configured to generate log records when administrator privileges are modified, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-239934`

### Rule: The Cisco ASA must be configured to generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-239934r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If the Cisco ASA is not configured to generate log records when administrator privileges are deleted, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-239935`

### Rule: The Cisco ASA must be configured to generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-239935r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log all login attempts. If the Cisco ASA is not configured to generate audit records when successful/unsuccessful attempts to logon, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-239936`

### Rule: The Cisco ASA must be configured to generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-239936r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log all EXEC-mode commands. If the Cisco ASA is not configured to generate log records for privileged activities, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-239937`

### Rule: The Cisco ASA must be configured to generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-239937r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging timestamp logging buffered informational Note: The ASA will log all login attempts as well as log the administrator’s name and time executing the enable command. The ASA will also log the time when the administrator logs out. If the Cisco ASA is not configured to generate log records showing starting and ending time for administrator access to the system, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-239938`

### Rule: The Cisco ASA must be configured to generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-239938r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The configuration should look similar to the example below. logging enable logging buffered informational Note: The ASA will log all login attempts including the IP address of the workstation. If the Cisco ASA is not configured to generate log records when concurrent logons from different workstations occur, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-239939`

### Rule: The Cisco ASA must be configured to offload audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-239939r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement as shown in the example below. logging trap notifications logging host NDM_INTERFACE 10.1.48.10 6/1514 Note: A logging list can be used as an alternative to the severity level. If the Cisco ASA is not configured to offload log records onto a different system than the system being audited, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-239940`

### Rule: The Cisco ASA must be configured to use at least two authentication servers to authenticate users prior to granting administrative access.

**Rule ID:** `SV-239940r916111_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and non-local access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify the device is configured to use at least two authentication servers as primary source for authentication. Step 1: Verify that an AAA group is configured for login authentication for both in-band and console access methods. aaa authentication serial console RADIUS_GROUP LOCAL aaa authentication ssh console RADIUS_GROUP LOCAL Step 2: Verify that an AAA group and server has been defined for the group referenced in the above example. aaa-server RADIUS_GROUP protocol radius aaa-server RADIUS_GROUP (NDM_INTERFACE) host 10.1.48.10 key ***** aaa-server RADIUS_GROUP (NDM_INTERFACE) host 10.1.48.11 key ***** If the Cisco ASA is not configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-239941`

### Rule: The Cisco ASA must be configured to conduct backups of system-level information contained in the information system when changes occur.

**Rule ID:** `SV-239941r916221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify it is compliant with this requirement. The example configuration below will send the configuration to an SCP server when a configuration change occurs. event manager applet BACKUP_CONFIG event syslog pattern "SYSLOG_CONFIG_I" action 1 cli command "copy startup-config scp://userx:xxxxxxx@10.1.48.10//opt/config_backup" action 2 syslog priority informational msg "Configuration backup was executed" Note: Tools such as Cisco Security Manager, Cisco Prime Infrastructure, Firemon, or Tripwire can be used to back up the configuration. If the Cisco ASA is not configured to conduct backups of the configuration when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-239942`

### Rule: The Cisco ASA must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-239942r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If PKI certificates are not implemented on the ASA, this requirement is not applicable. Step 1: Review the ASA configuration to determine if a CA trust point has been configured as shown in the example below. Step 2: Verify the CA is a DoD or DoD-approved service provider by entering the following command. show crypto ca certificates The output will list the following information for each certificate: Associated Trustpoints: (will map to a configured trustpoint from Step 1) Common Name (CN) of the issuer Organization Unit (OU) of the issuer Organization (O) of the issuer Validity Date If the ASA is not configured to obtain its public key certificates from a DoD or DoD-approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-239943`

### Rule: The Cisco ASA must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to organization-defined personnel and/or the firewall administrator.

**Rule ID:** `SV-239943r916114_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat. The ISSM or ISSO may designate the firewall/system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the information system security manager (ISSM) and information system security officer (ISSO).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is configured to send logs to at least two syslog servers. The configuration should look similar to the example below. logging trap notifications logging host NDM_INTERFACE 10.1.48.10 6/1514 logging host NDM_INTERFACE 10.1.48.11 6/1514 Note: A logging list can be used as an alternative to the severity level. If the ASA is not configured to send log data to at least two syslog servers, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-239944`

### Rule: The Cisco ASA must be running an operating system release that is currently supported by Cisco Systems.

**Rule ID:** `SV-239944r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is in compliance with this requirement by having the ASA administrator enter the following command. show version Verify the release is still supported by Cisco. All releases supported by Cisco can be found at the following URL: https://www.cisco.com/c/en/us/products/security/asa-firepower-services/eos-eol-notice-listing.html If the ASA is not running a supported release, this is a finding.

