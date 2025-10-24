# STIG Benchmark: HP FlexFabric Switch NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-217426`

### Rule: The HP FlexFabric Switch must limit the number of concurrent sessions to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-217426r960735_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to see if it limits the number of concurrent sessions to an organization-defined number for all administrator accounts and/or administrator account types: [HP] display local-user Device management user test: State: Active Service type: None Access limit: Enabled Max access number: 3 Current access number: 0 User group: system Bind attributes: Authorization attributes: Work directory: cfa0: User role list: network-admin If "Max access number:" line is not present, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-217427`

### Rule: The HP FlexFabric Switch must automatically audit account creation.

**Rule ID:** `SV-217427r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-217428`

### Rule: The HP FlexFabric Switch must automatically audit account modification.

**Rule ID:** `SV-217428r960780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the HP FlexFabric Switch are privileged or system-level accounts, account management is vital to the security of the HP FlexFabric Switch. Account management by a designated authority ensures access to the HP FlexFabric Switch is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-217429`

### Rule: The HP FlexFabric Switch must automatically audit account disabling actions.

**Rule ID:** `SV-217429r960783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the HP FlexFabric Switch is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-217430`

### Rule: The HP FlexFabric Switch must automatically audit account removal actions.

**Rule ID:** `SV-217430r960786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the HP FlexFabric Switch is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-217431`

### Rule: The HP FlexFabric Switch must enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the device.

**Rule ID:** `SV-217431r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Network devices use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the HP FlexFabric Switch to control access between administrators (or processes acting on behalf of administrators) and objects (e.g., device commands, files, records, processes) in the HP FlexFabric Switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the switch. [HP] display local-user Device management user admin: State: Active Service type: SSH/Telnet/Terminal User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: network-admin Password control configurations: If the HP FlexFabric Switch does not enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-217432`

### Rule: The HP FlexFabric Switch must enforce approved authorizations for controlling the flow of management information within the HP FlexFabric Switch based on information flow control policies.

**Rule ID:** `SV-217432r960801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the HP FlexFabric Switch may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the HP FlexFabric Switch or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if ACLs were configured for controlling the flow of management information within the HP FlexFabric Switch based on information flow control policies: [HP] display current-configuration acl number 3000 description ACL to block traffic with invalid address rule 0 permit icmp source 10.0.0.0 0.255.255.255 rule 1 deny ip source 172.16.0.0 0.15.255.255 rule 2 deny ip source 192.168.0.0 0.0.255.255 rule 3 deny ip source 169.254.0.0 0.0.255.255 rule 6 deny ip source 127.0.0.0 0.255.255.255 If ACLs are not configured for controlling the flow of management information within the HP FlexFabric Switch based on information flow control policies , this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-217433`

### Rule: The HP FlexFabric Switch must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-217433r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the HP FlexFabric Switch is configured to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. [HP] display password-control Global password control configurations: Maximum login attempts: 3 Action for exceeding login attempts: Lock user for 15 minutes If the limit of three consecutive invalid logon attempts by a user during a 15-minute time period is not enforced, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-217434`

### Rule: The HP FlexFabric Switch must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-217434r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the HP FlexFabric Switch ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to present a DoD-approved banner that is formatted in accordance with DTM-08-060. Establish a console or vty connection to HP FlexFabric Switch and attempt to logon to it. Once entering the username the banner should appear: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." If such a banner is not presented, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-217435`

### Rule: The HP FlexFabric Switch must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-217435r960846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to allowing the administrator access to the HP FlexFabric Switch. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement by clicking on a box indicating "OK".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to retain the Standard Mandatory DoD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access. After entering the username and password for HP FlexFabric Switch the banner and acknowledgement of the notice should be displayed: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Press Y or ENTER to continue, N to exit. If HP FlexFabric Switch does not retain the banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to logon for further access, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-217436`

### Rule: The HP FlexFabric Switch must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-217436r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the HP FlexFabric Switch are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the HP FlexFabric Switch must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric log file to determine if logging is enabled: [HP] display info-center Information Center: Enabled If the HP FlexFabric Switch does not have logging enabled, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-217438`

### Rule: The HP FlexFabric Switch must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-217438r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000092-NDM-000224

**Group ID:** `V-217439`

### Rule: The HP FlexFabric Switch must initiate session auditing upon startup.

**Rule ID:** `SV-217439r960888_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-217440`

### Rule: The HP FlexFabric Switch must produce audit log records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-217440r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-217441`

### Rule: The HP FlexFabric Switch must produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-217441r960894_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. In order to establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-217442`

### Rule: The HP FlexFabric Switch must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-217442r960897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the HP FlexFabric Switch provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-217443`

### Rule: The HP FlexFabric Switch must produce audit log records containing information to establish the source of events.

**Rule ID:** `SV-217443r960900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Associating information about where the source of the event occurred provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000099-NDM-000229

**Group ID:** `V-217444`

### Rule: The HP FlexFabric Switch must produce audit records that contain information to establish the outcome of the event.

**Rule ID:** `SV-217444r960903_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the device after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000100-NDM-000230

**Group ID:** `V-217445`

### Rule: The HP FlexFabric Switch must generate audit records containing information that establishes the identity of any individual or process associated with the event.

**Rule ID:** `SV-217445r960906_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., administrators or processes acting on behalf of administrators) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Event identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-217446`

### Rule: The HP FlexFabric Switch must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-217446r960909_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000116-NDM-000234

**Group ID:** `V-217447`

### Rule: The HP FlexFabric Switch must use internal system clocks to generate time stamps for audit records.

**Rule ID:** `SV-217447r960927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to determine what is happening within the network infrastructure or to resolve and trace an attack, the HP FlexFabric Switch must support the organization's capability to correlate the audit log data from multiple network devices to acquire a clear understanding of events. In order to correlate auditable events, time stamps are needed on all of the log records. If the internal clock is not used, the system may not be able to provide time stamps for log messages. Additionally, externally generated time stamps may not be accurate. Applications can use the capability of an operating system or purpose-built module for this purpose. (Note that the internal clock is required to be synchronized with authoritative time sources by other requirements.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to use internal system clocks to generate time stamps for audit records. [HP] display clock 06:13:14 MDT Wed 08/05/2015 Time Zone : test minus 05:00:00 Summer Time : MDT 02:00:00 March second Sunday 02:00:00 November first Sunday 01:00:00 If the switch is not configured to use internal system clocks to generate time stamps for audit records, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-217448`

### Rule: The HP FlexFabric Switch must protect audit information from unauthorized modification.

**Rule ID:** `SV-217448r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the HP FlexFabric Switch must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch protects audit information from any type of unauthorized modification with such methods as ensuring log files receive the proper file system permissions utilizing file system protections, restricting access to log data and backing up log data to ensure log data is retained, and leveraging user permissions and roles to identify the user accessing the data and the corresponding rights the user enjoys. [HP] display local-user Device management user security-user: State: Active Service type: SSH/Terminal User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: security-audit If the HP FlexFabric Switch does not protect audit information from unauthorized modification, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-217449`

### Rule: The HP FlexFabric Switch must protect audit information from unauthorized deletion.

**Rule ID:** `SV-217449r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the HP FlexFabric Switch must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch protects audit information from any type of unauthorized deletion with such methods as ensuring log files receive the proper file system permissions utilizing file system protections, restricting access to log data and backing up log data to ensure log data is retained, and leveraging user permissions and roles to identify the user accessing the data and the corresponding rights the user enjoys. [HP] display local-user Device management user security-user: State: Active Service type: SSH/Terminal User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: security-audit If the HP FlexFabric Switch does not protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-217451`

### Rule: The HP FlexFabric Switch must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-217451r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the HP FlexFabric Switch must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if unsecured protocols and services are disabled on the HP FlexFabric Switch: [HP] display ftp-server FTP is not configured. [HP] display current-configuration | include telnet Note: When Telnet server is enabled, the output for this command is telnet server enable. If all unnecessary and non-secure functions, ports, protocols, and services are not disabled, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-217452`

### Rule: The HP FlexFabric Switch must enforce a minimum 15-character password length.

**Rule ID:** `SV-217452r1113774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch or its associated authentication server enforces a minimum 15-character password length. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) If the HP FlexFabric Switch does not have password control enabled and does not enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-217453`

### Rule: If multifactor authentication is not supported and passwords must be used, the HP FlexFabric Switch must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-217453r1113778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see that the HP FlexFabric Switch enforces password complexity by requiring that at least one uppercase character be used. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (4 types, 1 characters per type) If the HP FlexFabric Switch does not have password control enabled and does not require that at least one uppercase character be used in each password, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-217454`

### Rule: If multifactor authentication is not supported and passwords must be used, the HP FlexFabric Switch must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-217454r1113781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see that the HP FlexFabric Switch enforces password complexity by requiring that at least one lowercase character be used. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (4 types, 1 characters per type) If the HP FlexFabric Switch does not have password control enabled and does not require that at least one lowercase character be used in each password, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-217455`

### Rule: If multifactor authentication is not supported and passwords must be used, the HP FlexFabric Switch must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-217455r1113782_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see that the HP FlexFabric Switch enforces password complexity by requiring that at least one numeric character be used. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (4 types, 1 characters per type) If the HP FlexFabric Switch does not have password control enabled and does not require that at least one numeric character be used in each password, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-217456`

### Rule: If multifactor authentication is not supported and passwords must be used, the HP FlexFabric Switch must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-217456r1113783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check to see that the HP FlexFabric Switch enforces password complexity by requiring that at least one special character be used. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (4 types, 1 characters per type) If the HP FlexFabric Switch does not have password control enabled and does not require that at least one special character be used in each password, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-217457`

### Rule: The HP FlexFabric Switch must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-217457r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch terminates the connection associated with a device management session at the end of the session or after 10 minutes of inactivity. If the HP FlexFabric Switch does not terminate the connection associated with a device management session at the end of the session or after 10 minutes of inactivity, this is a finding.

## Group: SRG-APP-000296-NDM-000280

**Group ID:** `V-217458`

### Rule: Network devices must provide a logoff capability for administrator-initiated communication sessions.

**Rule ID:** `SV-217458r961224_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If an administrator cannot explicitly end a device management session, the session may remain open and be exploited by an attacker; this is referred to as a zombie session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if it provides a logoff capability for administrator-initiated communication sessions. [HP] display users Idx Line Idle Time Pid Type + 177 VTY 0 00:00:00 May 29 15:45:11 1011 SSH Following are more details. VTY 0 : User name: admin@system Location: 16.117.204.17 + : Current operation user. F : Current operation user works in async mode. If the HP FlexFabric Switch does not provide a logoff capability for these sessions, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-217459`

### Rule: The HP FlexFabric Switch must automatically audit account enabling actions.

**Rule ID:** `SV-217459r961290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000328-NDM-000286

**Group ID:** `V-217460`

### Rule: If the HP FlexFabric Switch uses discretionary access control, the HP FlexFabric Switch must enforce organization-defined discretionary access control policies over defined subjects and objects.

**Rule ID:** `SV-217460r961317_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Discretionary Access Control (DAC) is based on the notion that individual network administrators are "owners" of objects and therefore have discretion over who should be authorized to access the object and in which mode (e.g., read or write). Ownership is usually acquired as a consequence of creating the object or via specified ownership assignment. DAC allows the owner to determine who will have access to objects they control. An example of DAC includes user-controlled file permissions. When discretionary access control policies are implemented, subjects are not constrained with regard to what actions they can take with information for which they have already been granted access. Thus, subjects that have been granted access to information are not prevented from passing (i.e., the subjects have the discretion to pass) the information to other subjects or objects. A subject that is constrained in its operation by Mandatory Access Control policies is still able to operate under the less rigorous constraints of this requirement. Thus, while Mandatory Access Control imposes constraints preventing a subject from passing information to another subject operating at a different sensitivity level, this requirement permits the subject to pass the information to any subject at the same sensitivity level. The policy is bounded by the information system boundary. Once the information is passed outside of the control of the information system, additional means may be required to ensure the constraints remain in effect. While the older, more traditional definitions of discretionary access control require identity-based access control, that limitation is not required for this use of discretionary access control. The discretionary access control policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch to determine if organization-defined discretionary access control policies are enforced over defined subjects and objects. [HP] display local-user local-user test authorization-attribute user-role network-operator If organization-defined discretionary access control policies are not enforced over defined subjects and objects, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-217461`

### Rule: If the HP FlexFabric Switch uses role-based access control, the HP FlexFabric Switch must enforce organization-defined role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-217461r987662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch to determine if organization-defined discretionary access control policies are enforced over defined subjects and objects. [HP] display local-user local-user test authorization-attribute user-role network-operator If organization-defined discretionary access control policies are not enforced over defined subjects and objects, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-217463`

### Rule: The HP FlexFabric Switch must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-217463r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the HP FlexFabric Switch, the anticipated volume of logs, the frequency of transfer from the HP FlexFabric Switch to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enter the command display logfile summary to verify audit record storage has been allocated in accordance with the organization-defined audit record storage requirements. If the switch has not been configured to allocate audit record storage in accordance with the organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-217464`

### Rule: The HP FlexFabric Switch must generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-217464r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch provides the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near-real-time. [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled 192.100.50.27, port number: 514, host facility: local7 Log buffer: Enabled Max buffer size 1024, current buffer size 512 Current messages 66, dropped messages 0, overwritten messages 0 Log file: Enabled Security log file: Enabled Information timestamp format: Log host: Date Other output destination: Date If the HP FlexFabric Switch does not provide the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near-real-time, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-217465`

### Rule: The HP FlexFabric Switch must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-217465r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The HP FlexFabric Switch must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources. [HP] display ntp status Clock status: synchronized Clock stratum: 4 System peer: 16.110.135.123 Local mode: client Reference clock ID: 16.110.135.123 Leap indicator: 00 Clock jitter: 0.004227 s Stability: 0.000 pps Clock precision: 2^-19 Root delay: 96.75598 ms Root dispersion: 149.76501 ms Reference time: d916fabd.a5c6d326 Mon, Jun 1 2015 9:37:33.647 If the HP FlexFabric Switch is not configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-217466`

### Rule: The HP FlexFabric Switch must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-217466r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if time zone is configured on the HP FlexFabric Switch: [HP] display clock 15:00:32 EST Thu 07/09/2015 Time Zone : EST minus 05:00:00 Check if info-center is configured to provide timestamp: [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled 192.100.50.27, port number: 514, host facility: local7 Log buffer: Enabled Max buffer size 1024, current buffer size 512 Current messages 66, dropped messages 0, overwritten messages 0 Log file: Enabled Security log file: Enabled Information timestamp format: Log host: Date Other output destination: Date Check logfile content to determine if the time stamp is present: <HP> cd logfile/ <HP> more logfile.log %@9377%Jan 20 23:31:03:567 2011 HP5930_SUT SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=16.123.122.155-User=admin; Command is dis info-center %@9378%Jan 20 23:31:09:342 2011 HP5930_SUT SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=16.123.122.155-User=admin; Command is qui If the HP FlexFabric Switch is not configured to enable timestamp in the log and if time zone is not configurable, this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-217467`

### Rule: The HP FlexFabric Switch must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-217467r961446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if info-center is configured to provide timestamp: [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled 192.100.50.27, port number: 514, host facility: local7 Log buffer: Enabled Max buffer size 1024, current buffer size 512 Current messages 66, dropped messages 0, overwritten messages 0 Log file: Enabled Security log file: Enabled Information timestamp format: Log host: Date Other output destination: Date Check logfile content to determine if the time stamp is present: <HP> cd logfile/ <HP> more logfile.log %@9377%Jan 20 23:31:03:567 2011 HP5930_SUT SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=16.123.122.155-User=admin; Command is dis info-center %@9378%Jan 20 23:31:09:342 2011 HP5930_SUT SHELL/6/SHELL_CMD: -Line=vty0-IPAddr=16.123.122.155-User=admin; Command is qui If the HP FlexFabric Switch is not configured to enable timestamp, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-217468`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-217468r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch implements cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications. [HP]display ssh server status SSH server: Enable SSH version : 2.0 SSH authentication-timeout : 60 second(s) SSH server key generating interval : 0 hour(s) SSH authentication retries : 3 time(s) SFTP server: Enable SFTP Server Idle-Timeout: 10 minute(s) Netconf server: Disable [HP] display current | i sftp sftp server enable If SSH and SFTP protocols are not configured for nonlocal device maintenance , this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-217469`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-217469r961557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch implements cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications. [HP] display ssh server status SSH server: Enable SSH version : 2.0 SSH authentication-timeout : 60 second(s) SSH server key generating interval : 0 hour(s) SSH authentication retries : 3 time(s) SFTP server: Enable SFTP Server Idle-Timeout: 10 minute(s) Netconf server: Disable [HP] display current | i sftp sftp server enable If SSH and SFTP protocols are not configured for nonlocal device maintenance , this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-217470`

### Rule: The HP FlexFabric Switch must protect against or limit the effects of all known types of Denial of Service (DoS) attacks on the HP FlexFabric Switch management network by employing organization-defined security safeguards.

**Rule ID:** `SV-217470r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the HP FlexFabric Switch is configured to protect against known DoS attacks by implementing ACLs and by enabling tcp syn-flood protection: [HP] display current-configuration tcp syn-cookie enable tcp timer syn-timeout 10 [HP] display acl all If the HP FlexFabric Switch is not configured with ACLs and tcp syn-flood features, this is a finding. Check pre-defined qos policies that are by default applied to the control plane: [HP] display qos policy control-plane pre-defined Check user-defined qos policies: [HP] display qos policy user-defined

## Group: SRG-APP-000491-NDM-000316

**Group ID:** `V-217471`

### Rule: If the HP FlexFabric Switch uses mandatory access control, the HP FlexFabric Switch must enforce organization-defined mandatory access control policies over all subjects and objects.

**Rule ID:** `SV-217471r987719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mandatory access control policies constrain what actions subjects can take with information obtained from data objects for which they have already been granted access, thus preventing the subjects from passing the information to unauthorized subjects and objects. This class of mandatory access control policies also constrains what actions subjects can take with respect to the propagation of access control privileges; that is, a subject with a privilege cannot pass that privilege to other subjects. Enforcement of mandatory access control is typically provided via an implementation that meets the reference monitor concept. The reference monitor enforces (mediates) access relationships between all subjects and objects based on privilege and need to know. The mandatory access control policies are defined uniquely for each network device, so they cannot be specified in the requirement. An example of where mandatory access control may be needed is to prevent administrators from tampering with audit objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch to determine if organization-defined mandatory access control policies are enforced over all subjects and objects. [HP] display local-user Device management user user1: State: Active Service type: SSH User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: role1 [HP] display role Role: role1 Description: VLAN policy: deny Permitted VLANs: 10 to 20 Interface policy: permit (default) VPN instance policy: permit (default) ------------------------------------------------------------------- Rule Perm Type Scope Entity ------------------------------------------------------------------- 1 permit R-- feature - 2 permit command system-view ; vlan * R:Read W:Write X:Execute If organization-defined mandatory access control policies are not enforced over all subjects and objects, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-217472`

### Rule: The HP FlexFabric Switch must generate audit records when successful/unsuccessful attempts to modify administrator privileges occur.

**Rule ID:** `SV-217472r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-217473`

### Rule: The HP FlexFabric Switch must generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-217473r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-217474`

### Rule: The HP FlexFabric Switch must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-217474r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-217475`

### Rule: The HP FlexFabric Switch must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-217475r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-217476`

### Rule: The HP FlexFabric Switch must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-217476r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-217477`

### Rule: The HP FlexFabric Switch must generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-217477r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-217478`

### Rule: The HP FlexFabric Switch must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-217478r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to use an external syslog server: [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled Source address interface: M-GigabitEthernet0/0/0 192.168.100.12, port number: 514, host facility: local7 Log buffer: Enabled Max buffer size 1024, current buffer size 512 Current messages 356, dropped messages 0, overwritten messages 0 Log file: Enabled Security log file: Enabled Information timestamp format: Log host: Date Other output destination: Date If the HP FlexFabric Switch is not configure to use an external syslog server, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-217479`

### Rule: The HP FlexFabric Switch must generate audit log events for a locally developed list of auditable events.

**Rule ID:** `SV-217479r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-217480`

### Rule: The HP FlexFabric Switch must enforce access restrictions associated with changes to the system components.

**Rule ID:** `SV-217480r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the HP FlexFabric Switch can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the HP FlexFabric Switch for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, ACLs, and policy filters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch to determine if only authorized administrators have permissions for changes, deletions and updates on HP FlexFabric Switch. [HP] display local-user Device management user user1: State: Active Service type: SSH User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: role1 [HP] display role Role: role1 Description: VLAN policy: deny Permitted VLANs: 10 to 20 Interface policy: permit (default) VPN instance policy: permit (default) ------------------------------------------------------------------- Rule Perm Type Scope Entity ------------------------------------------------------------------- 1 permit R-- feature - 2 permit command system-view ; vlan * R:Read W:Write X:Execute If unauthorized users are allowed to change the hardware or software, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-217481`

### Rule: The HP FlexFabric Switch must support organizational requirements to conduct backups of system level information contained in the information system when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-217481r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the HP FlexFabric Switch configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the HP FlexFabric Switch to support the organizational central backup process for system-level information associated with the HP FlexFabric Switch. This function may be provided by the HP FlexFabric Switch itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if it is configured to back up its configuration file on a weekly basis. If a schedule does not exist, this is a finding. [HP] display scheduler job Job name: system_backup tftp 192.168.1.13 put hp5900.cfg

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-217482`

### Rule: The HP FlexFabric Switch must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-217482r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch obtains public key certificates from an appropriate certificate policy through an approved service provider. [HP] display pki certificate domain HP local Certificate: Data: Version: 3 (0x2) Serial Number: 3e:7b:9b:bb:00:00:00:00:00:28 Signature Algorithm: sha1WithRSAEncryption Issuer: DC=local, DC=rae-domain, CN=rae-domain-WIN2008-RAE-CA Validity Not Before: Apr 23 18:19:27 2015 GMT Not After : Apr 22 18:19:27 2016 GMT Subject: unstructuredAddress=15.252.76.101, C=US, ST=MA, L=Littleton, O=HP, OU=STG, CN=12508 Subject Public Key Info: Public Key Algorithm: rsaEncryption Public-Key: (2048 bit) Modulus: 00:e1:13:04:10:94:4a:a9:f7:6b:42:bb:64:13:4a: eb:10:48:60:61:a5:e7:d6:13:95:2d:69:b0:79:ae: df:be:e3:a2:5d:7d:be:3b:97:b9:2c:99:05:37:ea: bf:a9:95:49:e7:08:50:14:68:fc:1d:16:83:f9:ea: 66:cc:8a:8f:f9:9c:28:dc:66:7a:80:0c:53:5e:cc: a2:ee:4a:c3:4f:fb:6f:81:00:6c:4f:5d:72:e7:34: dc:4c:06:18:97:7d:da:45:b5:f1:2b:7e:71:c7:62: b3:59:fe:b9:6d:62:19:43:fd:73:93:fc:f5:ed:5e: 08:db:76:e7:66:26:cb:17:fd:69:a5:f5:b9:7e:e9: 9b:b4:91:30:d1:1a:1b:89:a3:ed:07:99:59:33:1e: de:4d:96:34:67:8c:b2:20:4d:5f:ec:19:49:33:d6: 14:57:03:a5:90:9c:a7:6a:31:3f:37:c3:29:5b:0a: db:24:2c:83:7d:e9:cb:c3:70:55:24:36:f5:c5:3f: f5:4e:f5:87:05:99:2d:4a:59:6f:d9:2e:2d:90:c7: fa:43:59:86:50:ee:e0:fc:2a:f9:bc:52:8c:39:d0: 05:3f:85:5c:5e:6b:5f:95:31:7b:e7:1e:b7:b5:af: 08:0d:34:8f:a0:07:4a:5a:32:eb:e7:39:5f:0e:9a: f5:01 Exponent: 65537 (0x10001) X509v3 extensions: X509v3 Key Usage: critical Digital Signature X509v3 Subject Alternative Name: IP Address:15.252.76.101 X509v3 Subject Key Identifier: A7:B8:9F:0D:07:A9:31:91:ED:90:5C:F6:BF:6C:E0:7D:58:74:AB:08 X509v3 Authority Key Identifier: keyid:07:8D:A0:CF:CB:47:DB:E3:BE:E9:F6:18:21:F6:19:05:B8:34:26:3E X509v3 CRL Distribution Points: Full Name: URI:ldap:///CN=rae-domain-WIN2008-RAE-CA,CN=WIN2008-RAE,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=rae-domain,DC=local?certificateRevocationList?base?objectClass=cRLDistributionPoint Authority Information Access: CA Issuers - URI:ldap:///CN=rae-domain-WIN2008-RAE-CA,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=rae-domain,DC=local?cACertificate?base?objectClass=certificationAuthority 1.3.6.1.4.1.311.21.7: 0,.$+.....7.....E...\... ...0.............d... X509v3 Extended Key Usage: Code Signing 1.3.6.1.4.1.311.21.10: 0.0 ..+....... Signature Algorithm: sha1WithRSAEncryption 0b:1f:81:59:9d:4b:bf:b7:1c:a9:45:af:9e:2d:ab:0e:d4:a9: 20:3b:f7:25:36:59:72:da:c9:80:3d:66:66:ab:4f:bf:d7:b4: 55:23:96:24:2e:43:2c:20:79:41:d7:ec:23:18:55:49:d7:42: 36:d3:0f:1f:99:50:c7:84:94:0f:6f:b0:b7:e7:6a:e7:e7:e0: d5:b8:09:f7:3d:1e:9b:6e:9e:7a:d8:39:30:66:60:f5:05:fd: d9:68:0d:22:73:7e:91:69:8c:a3:99:2f:24:a3:9b:96:a7:37: 1d:a6:42:50:6d:8f:92:bf:90:8f:2b:26:a5:26:5c:59:f1:ef: 12:1f:d3:77:8e:59:58:3c:c1:1c:20:74:31:95:2b:f2:71:69: 39:fd:9b:06:4e:09:08:55:bc:ce:a7:3c:4e:1a:64:ae:0e:1b: a4:61:89:17:d1:72:31:20:2f:cc:24:97:d1:dd:1c:28:98:84: 00:bc:3c:0e:c4:14:dd:26:6f:20:7d:0d:82:f7:71:d2:00:ec: 1c:10:2e:35:a8:cc:75:0f:76:1b:7f:f2:d4:d9:df:a5:f8:c2: 75:38:4c:7c:7f:42:81:a1:36:23:a8:f3:c1:9e:f2:12:02:6f: db:3c:38:b5:0b:e4:0b:ea:f9:17:81:b2:6e:2c:34:7c:35:dc: 9f:e8:b9:0d If the HP FlexFabric Switch does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-217483`

### Rule: The HP FlexFabric Switch must have a local account that will only be used as an account of last resort with full access to the network device.

**Rule ID:** `SV-217483r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In the event the network device loses connectivity to the management network authentication service, only a local account can gain access to the switch to perform configuration and maintenance. Without this capability, the network device is inaccessible to administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured with a local user that has full access by entering the following command: display local-user user-name <name of user account>. The user role list should contain the following: network-admin, network-operator If the switch does not have a local user with full access, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-217484`

### Rule: The HP FlexFabric switch must be configured to utilize an authentication server for the purpose of authenticating privilege users, managing accounts, and to centrally verify authentication settings and Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-217484r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system. Protecting access authorization information ensures that authorization information cannot be altered, spoofed, or otherwise compromised during transmission. The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if it is authenticating user logon via an authentication server. Local authentication must only be used as a last resort. Example configuration would look similar to the following: authentication login hwtacacs-scheme <name of scheme> local or authentication login radius-scheme <name of scheme> local If the HP FlexFabric Switch does not have an authentication server configured as the primary authentication method, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-217485`

### Rule: The HP FlexFabric switch must be configured to send log data to a syslog server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-217485r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of accounts and notifies administrators and Information System Security Officers (ISSOs). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch generates alerts that can be forwarded to the administrators and ISSO when accounts are created. [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled Source address interface: GigabitEthernet0/1 192.168.16.102, port number: 514, host facility: local7 If the HP FlexFabric Switch is configured to use an authentication server which would perform this function, this is not a finding. If alerts are not generated when accounts are created and forwarded to the administrators and ISSO, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-217486`

### Rule: The HP FlexFabric switch must be configured to send SNMP traps and notifications to the SNMP manager for the purpose of sending alarms and notifying appropriate personnel as required by specific events.

**Rule ID:** `SV-217486r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If appropriate actions are not taken when a network device failure occurs, a denial of service condition may occur which could result in mission failure since the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of network device security components, the HP FlexFabric Switch must activate a system alert message, send an alarm, or shut down. By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged on to the device. This can be facilitated by the switch sending SNMP traps to the SNMP manager that can then have the necessary action taken by automatic or operator intervention.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to send system alert messages, alarms to a SNMP agent and/or automatically shuts down when a component failure is detected. [HP] display current-configuration snmp-agent snmp-agent local-engineid 800063A280D07E28ECBDB800000001 snmp-agent sys-info version v3 snmp-agent group v3 group1 privacy snmp-agent target-host trap address udp-domain 192.168.16.103 params securityname snmp1 v3 privacy snmp-agent usm-user v3 user1 group1 cipher authentication-mode sha $c$3$3C41avdWWmRMT64buQYb6FLdhVIUpAVHhIGyxIMhX6o3Qe3+GjY= privacy-mode aes128 $c$3$YpvVDasCitD9iCUvGc01ycckCq0rY+c6sThoqny+TjMTlQ== If the HP FlexFabric Switch is not configured to send system alert messages and alarms to a SNMP agent and/or does not automatically shuts down when a component failure is detected, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230161`

### Rule: The HP FlexFabric Switch must automatically disable accounts after a 35-day period of account inactivity.

**Rule ID:** `SV-230161r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Since the accounts in the HP FlexFabric Switch are privileged or system-level accounts, account management is vital to the security of the HP FlexFabric Switch. Inactive accounts could be reactivated or compromised by unauthorized users, allowing exploitation of vulnerabilities and undetected access to the HP FlexFabric Switch. This control does not include emergency administration accounts, which are meant for access to the HP FlexFabric Switch components in case of network failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if it automatically disables accounts after 35 days. [HP] display password-control Global password control configurations: User account idle time: 35 days If accounts are not automatically disabled after 35 days of inactivity, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230162`

### Rule: Upon successful logon, the HP FlexFabric Switch must notify the administrator of the date and time of the last logon.

**Rule ID:** `SV-230162r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful logon allows them to determine if any unauthorized activity has occurred. This incorporates all methods of logon, including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to notify the administrator of the date and time of their last logon. Once the logon credentials have been entered the system should display the previous logon information for the user: Log on as: admin admin@15.252.78.64's password: Your logon failures since the last successful logon: Wed May 27 10:06:04 2015 Wed May 27 10:06:09 2015 Last successfully logon time: Wed May 27 10:45:51 2015 If the administrator is not notified of the date and time of the last logon upon successful logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230163`

### Rule: Upon successful logon, the HP FlexFabric Switch must notify the administrator of the number of unsuccessful logon attempts since the last successful logon.

**Rule ID:** `SV-230163r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the number of unsuccessful attempts made to logon to their account allows them to determine if any unauthorized activity has occurred. Without this information, the administrator may not be aware that unauthorized activity has occurred. This incorporates all methods of logon, including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch is configured to notify the administrator of the date and time of their last logon. Once the logon credentials have been entered the system should display the previous logon information for the user: Log on as: admin admin@15.252.78.64's password: Your logon failures since the last successful logon: Wed May 27 10:06:04 2015 Wed May 27 10:06:09 2015 Last successfully logon time: Wed May 27 10:45:51 2015 If the administrator is not notified of the date and time of the last logon upon successful logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230164`

### Rule: The HP FlexFabric Switch must provide audit record generation capability for DoD-defined auditable events within the HP FlexFabric Switch.

**Rule ID:** `SV-230164r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch provides audit record generation capability for DoD-defined auditable events within the HP FlexFabric Switch. The list of events for which the device will provide an audit record generation capability is outlined in the vulnerability discussion. [HP] display security-logfile summary summary Display summary information of the security log file Security log file: Disabled Security log file size quota: 10 MB Security log file directory: cfa0:/seclog Alarm threshold: 80% Current usage: 0% Writing frequency: 24 hour 0 min 0 sec If the HP FlexFabric Switch does not provide audit record generation capability for DoD-defined auditable events within the HP FlexFabric Switch, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230165`

### Rule: The HP FlexFabric Switch must protect audit information from any type of unauthorized read access.

**Rule ID:** `SV-230165r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could use to his or her advantage. To ensure the veracity of audit data, the information system and/or the HP FlexFabric Switch must protect audit information from any and all unauthorized read access. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, network devices with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the device interface. If the device provides access to the audit data, the device becomes accountable for ensuring audit information is protected from unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch protects audit information from any type of unauthorized read access with such methods as least privilege permissions, restrictions on the location and number of log file repositories and not allowing for the unfettered manipulation of or access to audit records via switch interface. [HP] display local-user Device management user security-user: State: Active Service type: SSH/Terminal User group: system Bind attributes: Authorization attributes: Work directory: flash: User role list: security-audit If the HP FlexFabric Switch does not protect audit information from any type of unauthorized read access, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230166`

### Rule: The HP FlexFabric Switch must disable identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-230166r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to network devices. Attackers that are able to exploit an inactive identifier can potentially obtain and maintain undetected access to the device. Owners of inactive accounts will not notice if unauthorized access to their account has been obtained. Network devices need to track periods of inactivity and disable application identifiers after 35 days of inactivity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if it automatically disables accounts after 35 days. [HP] display password-control Global password control configurations: User account idle time: 35 days If accounts are not automatically disabled after 35 days of inactivity, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230167`

### Rule: The HP FlexFabric Switch must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-230167r1113775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the HP FlexFabric Switch allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch prohibits password reuse for a minimum of five generations. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (1 types, 1 characters per type) Password history: Enabled (max history records: 4) If the HP FlexFabric Switch does not have password control enabled and does not prohibit password reuse for a minimum of five generations, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230168`

### Rule: The HP FlexFabric Switch must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-230168r1113784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. Restricting this setting limits the user's ability to change their password. Passwords need to be changed at specific policy-based intervals; however, if the HP FlexFabric Switch allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch enforces 24 hours/1 day as the minimum password lifetime. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) Password length: Enabled (15 characters) Password composition: Enabled (1 types, 1 characters per type) Password history: Enabled (max history records: 4) Early notice on password expiration: 7 days Maximum login attempts: 3 Action for exceeding login attempts: Lock user for 1 minutes Minimum interval between two updates: 24 hours If the HP FlexFabric Switch does not have password control enabled and does not enforce 24 hours/1 day as the minimum password lifetime, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230169`

### Rule: The HP FlexFabric Switch must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-230169r1113785_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the HP FlexFabric Switch does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the HP FlexFabric Switch in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch enforces a 60-day maximum password lifetime. [HP] display password-control Global password control configurations: Password control: Enabled Password aging: Enabled (60 days) If the HP FlexFabric Switch does not have password control enabled and does not enforce a 60-day maximum password lifetime, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230170`

### Rule: The HP FlexFabric Switch, when utilizing PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-230170r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If PKI-based authentication is being used, determine if the HP FlexFabric Switch validates certificates by constructing a certification path to an accepted trust anchor. [HP] display pki certificate domain HP local Certificate: Data: Version: 3 (0x2) Serial Number: 3e:7b:9b:bb:00:00:00:00:00:28 Signature Algorithm: sha1WithRSAEncryption Issuer: DC=local, DC=rae-domain, CN=rae-domain-WIN2008-RAE-CA Validity Not Before: Apr 23 18:19:27 2015 GMT Not After : Apr 22 18:19:27 2016 GMT Subject: unstructuredAddress=15.252.76.101, C=US, ST=MA, L=Littleton, O=HP, OU=STG, CN=12508 Subject Public Key Info: Public Key Algorithm: rsaEncryption Public-Key: (2048 bit) Modulus: 00:e1:13:04:10:94:4a:a9:f7:6b:42:bb:64:13:4a: eb:10:48:60:61:a5:e7:d6:13:95:2d:69:b0:79:ae: df:be:e3:a2:5d:7d:be:3b:97:b9:2c:99:05:37:ea: bf:a9:95:49:e7:08:50:14:68:fc:1d:16:83:f9:ea: 66:cc:8a:8f:f9:9c:28:dc:66:7a:80:0c:53:5e:cc: a2:ee:4a:c3:4f:fb:6f:81:00:6c:4f:5d:72:e7:34: dc:4c:06:18:97:7d:da:45:b5:f1:2b:7e:71:c7:62: b3:59:fe:b9:6d:62:19:43:fd:73:93:fc:f5:ed:5e: 08:db:76:e7:66:26:cb:17:fd:69:a5:f5:b9:7e:e9: 9b:b4:91:30:d1:1a:1b:89:a3:ed:07:99:59:33:1e: de:4d:96:34:67:8c:b2:20:4d:5f:ec:19:49:33:d6: 14:57:03:a5:90:9c:a7:6a:31:3f:37:c3:29:5b:0a: db:24:2c:83:7d:e9:cb:c3:70:55:24:36:f5:c5:3f: f5:4e:f5:87:05:99:2d:4a:59:6f:d9:2e:2d:90:c7: fa:43:59:86:50:ee:e0:fc:2a:f9:bc:52:8c:39:d0: 05:3f:85:5c:5e:6b:5f:95:31:7b:e7:1e:b7:b5:af: 08:0d:34:8f:a0:07:4a:5a:32:eb:e7:39:5f:0e:9a: f5:01 Exponent: 65537 (0x10001) X509v3 extensions: X509v3 Key Usage: critical Digital Signature X509v3 Subject Alternative Name: IP Address:15.252.76.101 X509v3 Subject Key Identifier: A7:B8:9F:0D:07:A9:31:91:ED:90:5C:F6:BF:6C:E0:7D:58:74:AB:08 X509v3 Authority Key Identifier: keyid:07:8D:A0:CF:CB:47:DB:E3:BE:E9:F6:18:21:F6:19:05:B8:34:26:3E X509v3 CRL Distribution Points: Full Name: URI:ldap:///CN=rae-domain-WIN2008-RAE-CA,CN=WIN2008-RAE,CN=CDP,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=rae-domain,DC=local?certificateRevocationList?base?objectClass=cRLDistributionPoint Authority Information Access: CA Issuers - URI:ldap:///CN=rae-domain-WIN2008-RAE-CA,CN=AIA,CN=Public%20Key%20Services,CN=Services,CN=Configuration,DC=rae-domain,DC=local?cACertificate?base?objectClass=certificationAuthority 1.3.6.1.4.1.311.21.7: 0,.$+.....7.....E...\... ...0.............d... X509v3 Extended Key Usage: Code Signing 1.3.6.1.4.1.311.21.10: 0.0 ..+....... Signature Algorithm: sha1WithRSAEncryption 0b:1f:81:59:9d:4b:bf:b7:1c:a9:45:af:9e:2d:ab:0e:d4:a9: 20:3b:f7:25:36:59:72:da:c9:80:3d:66:66:ab:4f:bf:d7:b4: 55:23:96:24:2e:43:2c:20:79:41:d7:ec:23:18:55:49:d7:42: 36:d3:0f:1f:99:50:c7:84:94:0f:6f:b0:b7:e7:6a:e7:e7:e0: d5:b8:09:f7:3d:1e:9b:6e:9e:7a:d8:39:30:66:60:f5:05:fd: d9:68:0d:22:73:7e:91:69:8c:a3:99:2f:24:a3:9b:96:a7:37: 1d:a6:42:50:6d:8f:92:bf:90:8f:2b:26:a5:26:5c:59:f1:ef: 12:1f:d3:77:8e:59:58:3c:c1:1c:20:74:31:95:2b:f2:71:69: 39:fd:9b:06:4e:09:08:55:bc:ce:a7:3c:4e:1a:64:ae:0e:1b: a4:61:89:17:d1:72:31:20:2f:cc:24:97:d1:dd:1c:28:98:84: 00:bc:3c:0e:c4:14:dd:26:6f:20:7d:0d:82:f7:71:d2:00:ec: 1c:10:2e:35:a8:cc:75:0f:76:1b:7f:f2:d4:d9:df:a5:f8:c2: 75:38:4c:7c:7f:42:81:a1:36:23:a8:f3:c1:9e:f2:12:02:6f: db:3c:38:b5:0b:e4:0b:ea:f9:17:81:b2:6e:2c:34:7c:35:dc: 9f:e8:b9:0d If PKI-based authentication is being used and HP FlexFabric Switch does not validate certificates by constructing a certification path to an accepted trust anchor, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230171`

### Rule: The HP FlexFabric Switch must map the authenticated identity to the user account for PKI-based authentication.

**Rule ID:** `SV-230171r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any network device requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch maps the authenticated identity to the user account for PKI-based authentication. [HP] display ssh user-information Total ssh users: 3 Username Authentication-type User-public-key-name Service-type pkiuser password-publickey hp all If the HP FlexFabric Switch does not map the authenticated identity to the user account for PKI-based authentication, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230172`

### Rule: The HP FlexFabric Switch must generate an immediate alert for account enabling actions.

**Rule ID:** `SV-230172r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230173`

### Rule: The HP FlexFabric Switch must automatically lock the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded.

**Rule ID:** `SV-230173r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch automatically locks the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded. [HP] display local-user Device management user admin: State: Active Service type: SSH/Terminal User group: system Bind attributes: Authorization attributes: Work directory: cfa0: User role list: network-admin, network-operator Password control configurations: Maximum login attempts: 3 Action for exceeding login attempts: Lock user for 15 minutes If an account is not automatically locked out until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230174`

### Rule: The HP FlexFabric Switch must notify the administrator, upon successful logon (access), of the location of last logon (terminal or IP address) in addition to the date and time of the last logon (access).

**Rule ID:** `SV-230174r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their account. Providing them with information deemed important by the organization may aid in the discovery of unauthorized access or thwart a potential attacker. Organizations should consider the risks to the specific information system being accessed and the threats presented by the device to the environment when configuring this option. An excessive or unnecessary amount of information presented to the administrator at logon is not recommended.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch notifies the administrator upon successful logon of the location of last logon (terminal or IP address) in addition to the date and time of the last logon. [HP] display password-control Global password control configurations: Password control: Enabled If the administrator is not notified of the location of last logon (terminal or IP address) upon successful logon, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230175`

### Rule: The HP FlexFabric Switch must generate an immediate alert when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

**Rule ID:** `SV-230175r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. This could lead to the loss of audit information. Note that while the HP FlexFabric Switch must generate the alert, notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch provides the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near-real-time. [HP] display info-center Information Center: Enabled Console: Enabled Monitor: Enabled Log host: Enabled 192.100.50.27, port number: 514, host facility: local7 Log buffer: Enabled Max buffer size 1024, current buffer size 512 Current messages 66, dropped messages 0, overwritten messages 0 Log file: Enabled Security log file: Enabled Information timestamp format: Log host: Date Other output destination: Date If the HP FlexFabric Switch does not provide the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near-real-time, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230176`

### Rule: The HP FlexFabric Switch must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-230176r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch configuration to determine if compares internal information system clocks at least every 24 hours with an authoritative time server. [HP] display ntp status Clock status: synchronized Clock stratum: 4 System peer: 16.110.135.123 Local mode: client Reference clock ID: 16.110.135.123 Leap indicator: 00 Clock jitter: 0.004227 s Stability: 0.000 pps Clock precision: 2^-19 Root delay: 96.75598 ms Root dispersion: 149.76501 ms Reference time: d916fabd.a5c6d326 Mon, Jun 1 2015 9:37:33.647 If this comparison does not occur at least every 24 hours, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230177`

### Rule: The HP FlexFabric Switch must synchronize internal information system clocks to the authoritative time source when the time difference is greater than the organization-defined time period.

**Rule ID:** `SV-230177r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in CCI-001891 because a comparison must be done in order to determine the time difference. The organization-defined time period will depend on multiple factors, most notably the granularity of time stamps in audit logs. For example, if time stamps only show to the nearest second, there is no need to have accuracy of a tenth of a second in clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the HP FlexFabric Switch configuration to determine if it synchronizes internal information system clocks to the authoritative time source when the time difference is greater than the organization-defined time period. [HP] display ntp status Clock status: synchronized Clock stratum: 4 System peer: 16.110.135.123 Local mode: client Reference clock ID: 16.110.135.123 Leap indicator: 00 Clock jitter: 0.004227 s Stability: 0.000 pps Clock precision: 2^-19 Root delay: 96.75598 ms Root dispersion: 149.76501 ms Reference time: d916fabd.a5c6d326 Mon, Jun 1 2015 9:37:33.647 If this synchronization is not occurring when the time difference is greater than the organization-defined time period, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230178`

### Rule: The HP FlexFabric Switch must allow the use of a temporary password for system logons with an immediate change to a permanent password.

**Rule ID:** `SV-230178r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without providing this capability, an account may be created without a password. Non-repudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial logon. Temporary passwords are typically used to allow access to applications when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts that allow the users to log on yet force them to change the password once they have successfully authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch allows the use of a temporary password for system logons with an immediate change to a permanent password. This requirement may be verified by demonstration, configuration review, or validated test results. This requirement may be met through use of a properly configured authentication server if the device is configured to use the authentication server. [HP] display password-control Global password control configurations: Password control: Enabled If the use of a temporary password for system logons with an immediate change to a permanent password is not allowed, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230179`

### Rule: The HP FlexFabric Switch must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-230179r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the HP FlexFabric Switch (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230180`

### Rule: The HP FlexFabric Switch must notify the administrator of the number of successful logon attempts occurring during an organization-defined time period.

**Rule ID:** `SV-230180r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their network device management account. Providing administrators with information regarding the date and time of their last successful logon allows the administrator to determine if any unauthorized activity has occurred. This incorporates all methods of logon including, but not limited to, SSH, HTTP, HTTPS, and physical connectivity. The organization-defined time period is dependent on the frequency with which administrators typically log on to the HP FlexFabric Switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the HP FlexFabric Switch notifies the administrator of the number of successful logon attempts occurring during an organization-defined time period. Once the logon credentials have been entered, the system should display the previous logon information for the user: Log on as: admin admin@15.252.78.64's password: Your logon failures since the last successful logon: Wed May 27 10:06:04 2015 Wed May 27 10:06:09 2015 Last successfully logon time: Wed May 27 10:45:51 2015 If the administrator is not notified of the number of successful logon attempts occurring during an organization-defined time period, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-230181`

### Rule: The HP FlexFabric Switch must employ automated mechanisms to assist in the tracking of security incidents.

**Rule ID:** `SV-230181r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Despite the investment in perimeter defense technologies, enclaves are still faced with detecting, analyzing, and remediating network breaches and exploits that have made it past the HP FlexFabric Switch. An automated incident response infrastructure allows network operations to immediately react to incidents by identifying, analyzing, and mitigating any network device compromise. Incident response teams can perform root cause analysis, determine how the exploit proliferated, and identify all affected nodes, as well as contain and eliminate the threat. The HP FlexFabric Switch assists in the tracking of security incidents by logging detected security events. The audit log and network device application logs capture different types of events. The audit log tracks audit events occurring on the components of the HP FlexFabric Switch. The application log tracks the results of the HP FlexFabric Switch content filtering function. These logs must be aggregated into a centralized server and can be used as part of the organization's security incident tracking and analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the info-center feature is enabled on the HP FlexFabric Switch: [HP] display info-center Information Center: Enabled If logging is not enabled, this is a finding.

