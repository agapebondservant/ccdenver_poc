# STIG Benchmark: IBM MQ Appliance v9.0 NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-255726`

### Rule: Access to the MQ Appliance network device must limit the number of concurrent sessions to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-255726r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MQ Appliance device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Review LDAP server configuration settings and verify the LDAP configuration limits the number of concurrent sessions. If MQ is not set to LDAP authentication or if LDAP is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255727`

### Rule: Access to the MQ Appliance network element must use two or more authentication servers for the purpose of granting administrative access.

**Rule ID:** `SV-255727r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All accounts used for access to the MQ Appliance network device are privileged or system-level accounts. Therefore, if account management functions are not automatically enforced, an attacker could gain privileged access to a vital element of the network security architecture. The use of Authentication, Authorization, and Accounting (AAA) affords the best methods for controlling user access, authorization levels, and activity logging. By enabling AAA on the routers in conjunction with an authentication server such as TACACS+ or RADIUS, the administrators can easily add or remove user accounts, add or remove command authorizations, and maintain a log of user activity. The use of an authentication server provides the capability to assign device administrators to tiered groups that contain their privilege level, which is used for authorization of specific commands. This control does not include emergency administration accounts that provide access to the MQ Appliance network device components in case of network failure. There must be only one such locally defined account. All other accounts must be defined. All other accounts must be created and managed on the site's authentication server (e.g., RADIUS, LDAP, or Active Directory). This requirement is applicable to account management functions provided by the MQ Appliance network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Review LDAP configuration. Verify the LDAP configuration includes a Load Balancer Group that includes two or more authentication servers. If the LDAP configuration does not include a Load Balancer Group that includes two or more authentication servers, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255728`

### Rule: The MQ Appliance network device access must automatically disable accounts after a 35-day period of account inactivity.

**Rule ID:** `SV-255728r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the MQ Appliance network device are privileged or system-level accounts, account management is vital to the security of the MQ Appliance network device. Inactive accounts could be reactivated or compromised by unauthorized users, allowing exploitation of vulnerabilities and undetected access to the MQ Appliance network device. This control does not include emergency administration accounts, which are meant for access to the MQ Appliance network device components in case of network failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Review LDAP server settings and verify accounts are configured to be disabled after 35 days of inactivity. If MQ is not set to LDAP authentication or if LDAP is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255729`

### Rule: The MQ Appliance network device must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-255729r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Review LDAP server settings and verify the LDAP configuration limits three consecutive invalid logon attempts by a user during a 15-minute time period If MQ is not set to LDAP authentication or if LDAP is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-255730`

### Rule: The MQ Appliance network device must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-255730r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the MQ Appliance network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a browser, navigate to the MQ Appliance logon page as a privileged user. Verify the logon page displays the Standard Mandatory DoD Notice and Consent Banner: For the WebGUI, the banner must read: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. Logging in signifies acceptance of this agreement." For the SSH CLI, the banner must read: "I've read & consent to terms in IS user agreem't. Logging in signifies acceptance of this agreement." If the standard banner is not displayed in both the WebGUI and CLI interfaces, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255731`

### Rule: The MQ Appliance network device must notify the administrator of changes to access and/or privilege parameters of the administrator account that occurred since the last logon.

**Rule ID:** `SV-255731r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing administrators with information regarding security-related changes to their account allows them to determine if any unauthorized activity has occurred. Changes to the account could be an indication of the account being compromised. Hence, without notification to the administrator, the compromise could go undetected if other controls were not in place to mitigate this risk. Using a syslog logging target, the MQ Appliance logs all changes to access or privilege parameters. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. It is the responsibility of the sysadmin to configure the triggers necessary to send alerts based upon information received at the syslog server. To meet the requirement, the sysadmin must trigger notification upon receiving the following audit event: 0x8240001f. Changes to access and/or privilege parameters will fall into this event category. Ask the admin to provide evidence these alerts are configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all of the following log event source and log-level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error In the WebGUI, Administration (gear icon) >> Access >> User Account, add a user. Verify the administrator receives notification of this event. If the event notifications are not configured, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-255732`

### Rule: The MQ Appliance network device must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-255732r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the MQ Appliance network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. Using a syslog logging target, the MQ Appliance logs configuration changes to the device. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. Satisfies: SRG-APP-000080-NDM-000220, SRG-APP-000095-NDM-000225, SRG-APP-000097-NDM-000227, SRG-APP-000098-NDM-000228, SRG-APP-000100-NDM-000230, SRG-APP-000319-NDM-000283</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all of the following log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error If these events are not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255733`

### Rule: The MQ Appliance network device must alert the Information System Security Officer (ISSO) and System Administrator (SA) (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-255733r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Using a syslog logging target, the MQ Appliance logs audit events, including audit processing failures. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. The MQ appliance is configured to create the event in the logs that will be used to send an alert. The alerting process must be performed by a third-party alerting utility, centralized log management, or SIEM.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Configuring notification of events occurring at the external logging server is the responsibility of the administrator. Ask the system admin to provide evidence the required alert triggers for the following event codes: 0x80c0006a, 0x82400067, 0x00330034, 0x80400080 have been set up and the ISSO and SA at a minimum are alerted. If there is no evidence that alerts are sent in the event of an audit processing failure, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255734`

### Rule: The MQ Appliance network device must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-255734r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. Using a syslog logging target, the MQ Appliance logs audit events, including the continuous backup of audit records. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list of log targets includes an appropriate syslog notification target; - The log target is enabled; and - It includes all desired log event source and log level parameters, e.g., event audit debug. If any of these conditions is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255735`

### Rule: The MQ Appliance network device must uniquely identify and authenticate organizational administrators (or processes acting on behalf of organizational administrators).

**Rule ID:** `SV-255735r1000066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access to the MQ Appliance, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. If MQ is not set to LDAP authentication, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-255736`

### Rule: In the event the authentication server is unavailable, the MQ Appliance must provide one local account created for emergency administration use.

**Rule ID:** `SV-255736r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the MQ Appliance is required at all times. An account can be created on the device's local database for use in an emergency, such as when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is also referred to as the account of last resort since the emergency administration account is strictly intended to be used only as a last resort and immediate administrative access is absolutely necessary. The number of emergency administration accounts is restricted to at least one, but no more than operationally required as determined by the Information System Security Officer (ISSO). The emergency administration account logon credentials must be stored in a sealed envelope and kept in a safe. MQ provides the Fallback user account to provide access to the MQ appliance in the event the centralized authentication server is not available.v</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Verify at least one Fallback user is configured. If MQ authentication is not set to LDAP and if the Fallback user is not created, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-255737`

### Rule: The MQ Appliance network device must use multifactor authentication for network access to privileged accounts.

**Rule ID:** `SV-255737r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication requires using two or more factors to achieve authenticated access to the MQ Appliance. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the Internet).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Verify the MQ Appliance PKI-based user authentication is configured to support multifactor authentication for network access to privileged accounts. Click on the Network (gear) icon. Under Management, click on "Web Management Service". Expand the settings under "Advanced". Click the pencil icon to the right of the custom SSL Server Profile. Scroll to "Validation Credentials". Click on the pencil icon to the right. For each certificate name listed, click the pencil to the right and then click "Details" to display the certificate properties. Verify all listed client certificates are authorized to access the MQ Appliance. If certificate-based multifactor authentication is not used, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-255738`

### Rule: When connecting to the MQ Appliance network device using the WebGUI, it must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-255738r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the MQ Appliance. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Verify the MQ Appliance PKI-based user authentication is configured to support multifactor authentication to provide replay-resistant authentication. Verify an SSL Server Profile is associated with the WebGUI (CLI). Enter: co show web-mgmt [Note the name of the ssl-server] Display the parameters of the ssl-server (CLI). Enter: co crypto ssl-server <ssl-server name> show [Note the name of the valcred] Display the certificates in the ValCred (CLI). Enter: co crypto valcred <name of valcred> show Verify all listed client certificates are authorized to access the MQ Appliance. If any are not authorized, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255739`

### Rule: The MQ Appliance network device must enforce a minimum 15-character password length.

**Rule ID:** `SV-255739r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM password policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy for the Fallback user minimum length is set to 15. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255740`

### Rule: The MQ Appliance network device must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-255740r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the MQ Appliance network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM Password Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) MQ Password Policy Reuse History is set to a minimum of "5". If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-255741`

### Rule: The MQ Appliance network device must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-255741r984095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM Password Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy Require Mixed Case check box is checked. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-255742`

### Rule: The MQ Appliance network device must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-255742r984098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM Password Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy Require Mixed Case check box is checked. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-255743`

### Rule: The MQ Appliance network device must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-255743r984099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM Password Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy Require Number check box is checked. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-255744`

### Rule: The MQ Appliance network device must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-255744r984100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. For LDAP authentication, the authentication server is responsible for enforcing password policy. When the LDAP server is not available, password policy is enforced by the MQ Appliance's RBM Password Policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy Require Non-alphanumeric check box is checked. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255745`

### Rule: Authorization for access to the MQ Appliance network device must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-255745r1000067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the MQ Appliance network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts meant for access to the MQ Appliance network device in case of failure. These accounts are not required to have maximum password lifetime restrictions. For LDAP authentication, the authentication server is responsible for enforcing password policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Expand Password Policy. Verify the (local) Password Policy Enable Aging check box is selected. If MQ is not set to LDAP authentication or if the local password policy is not configured to meet the requirement, this is a finding.

## Group: SRG-APP-000175-NDM-000262

**Group ID:** `V-255746`

### Rule: WebGUI access to the MQ Appliance network device, when using PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-255746r961038_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Verify the MQ Appliance is configured to support PKI-based user authentication. Verify an SSL Server Profile is associated with the WebGUI (CLI). Enter: co show web-mgmt [Note the name of the ssl-server] Display the parameters of the ssl-server (CLI). Enter: co crypto ssl-server <ssl-server name> show [Note the name of the valcred] Display the certificates in the ValCred (CLI). Enter: co crypto valcred <name of valcred> show Verify all listed client certificates are authorized to access the MQ Appliance. If any listed client certificates are not authorized to access the MQ Appliance, this is a finding.

## Group: SRG-APP-000177-NDM-000263

**Group ID:** `V-255747`

### Rule: WebGUI access to the MQ Appliance network device must map the authenticated identity to the user account for PKI-based authentication.

**Rule ID:** `SV-255747r961044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authorization for access to any MQ Appliance network device requires an approved and assigned individual account identifier. To ensure only the assigned individual is using the account, the account must be bound to a user certificate when PKI-based authentication is implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Verify the MQ Appliance is configured to support PKI-based user authentication. Verify an SSL Server Profile is associated with the WebGUI (CLI). Enter: co show web-mgmt [Note the name of the ssl-server] Display the parameters of the ssl-server (CLI). Enter: co crypto ssl-server <ssl-server name> show [Note the name of the valcred] Display the certificates in the ValCred (CLI). Enter: co crypto valcred <name of valcred> show Verify all listed client certificates are authorized to access the MQ Appliance. If any are not authorized, this is a finding. Spot-check access to the appliance: Attempt to access the appliance from a browser enabled with an authorized certificate. If authorized access does not succeed, this is a finding. Attempt to access the appliance from a browser not enabled with an authorized client certificate. If unauthorized access succeeds, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-255748`

### Rule: The MQ Appliance network device must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-255748r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. MQ Appliance network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: config crypto show crypto-mode The result should be: fips-140-2-l1 If it is not, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-255749`

### Rule: The WebGUI of the MQ Appliance network device must terminate all sessions and network connections when nonlocal device maintenance is completed.

**Rule ID:** `SV-255749r984105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> If an MQ Appliance device management session or connection remains open after management is completed, it may be hijacked by an attacker and used to compromise or damage the MQ Appliance network device. Nonlocal MQ Appliance device management and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. In the event the remote node has abnormally terminated or an upstream link from the managed device is down, the management session will be terminated, thereby freeing device resources and eliminating any possibility of an unauthorized user being orphaned to an open idle session of the managed device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co web-mgmt show If the idle-timeout value is not 600 seconds or less, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255750`

### Rule: The WebGUI of the MQ Appliance network device must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255750r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co web-mgmt show If the idle-timeout value is not 600 seconds or less, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255751`

### Rule: The SSH CLI of the MQ Appliance network device must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255751r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co rbm show If the idle-timeout value is not 600 seconds or less, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-255752`

### Rule: The MQ Appliance network device must generate unique session identifiers using a FIPS 140-2 approved random number generator.

**Rule ID:** `SV-255752r961119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sequentially generated session IDs can be easily guessed by an attacker. Employing the concept of randomness in the generation of unique session identifiers helps to protect against brute-force attacks to determine future session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement is applicable to devices that use a web interface for MQ Appliance device management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: config crypto show crypto-mode If the result is not fips-140-2-l1, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255753`

### Rule: The MQ Appliance network device must activate a system alert message, send an alarm, and/or automatically shut down when a component failure is detected.

**Rule ID:** `SV-255753r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address device failure issues. If components key to maintaining the device's security fail to function, the device could continue operating in an insecure state. If appropriate actions are not taken when an MQ Appliance network device failure occurs, a denial of service condition may occur, which could result in mission failure since the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of MQ Appliance network device security components, the MQ Appliance network device must activate a system alert message, send an alarm, or shut down. With failure notification enabled, an error report can be sent to a designated recipient or uploaded to a specific location after the appliance returns to service from an unscheduled outage. This error report can contain diagnostic details. Intrusion detection will provide a warning and restart in Fail-Safe mode. (See https://ibm.biz/Bd4NJ5)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: failure-notification show failure-notification Examine the configured parameters to verify the current configuration, including the notification address. If the MQ Appliance is not configured to send an alert when a component failure is detected, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255754`

### Rule: The MQ Appliance network device must generate account activity alerts that are forwarded to the administrators and Information System Security Officer (ISSO). Activity includes, creation, removal, modification and re-enablement after being previously disabled.

**Rule ID:** `SV-255754r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. Using a syslog logging target, the MQ Appliance logs audit events, including when accounts are created. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. It is the responsibility of the sysadmin to configure the triggers necessary to send alerts based upon information received at the syslog server. To meet the current requirement, the sysadmin must configure trigger notifications upon receiving the following audit events in the syslog server: 0x8240001f and 0x810001f0. Changes to access and/or privilege parameters will fall into this event category. Satisfies: SRG-APP-000291-NDM-000275, SRG-APP-000292-NDM-000276, SRG-APP-000293-NDM-000277, SRG-APP-000294-NDM-000278, SRG-APP-000319-NDM-000283, SRG-APP-000320-NDM-000284</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Ask the system admin to provide evidence that alerts are sent based on the following audit events: 0x8240001f and 0x810001f0. Account administration events will fall into this event category and be written to the audit logs. If alerts are not sent when accounts on the MQ appliance are created, modified, deleted, or re-enabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255755`

### Rule: The MQ Appliance network device must automatically terminate a network administrator session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-255755r1000068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of administrator-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever an administrator (or process acting on behalf of a user) accesses an MQ Appliance network device. Such administrator sessions can be terminated (and thus terminate network administrator access) without terminating network sessions. Session termination terminates all processes associated with an administrator's logical session, except processes specifically created by the administrator (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. These conditions will vary across environments and MQ Appliance network device types.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co web-mgmt show If the idle-timeout value is not 600 seconds or less, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-255756`

### Rule: The MQ Appliance network device must terminate shared/group account credentials when members leave the group.

**Rule ID:** `SV-255756r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the MQ Appliance network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. The only local account on the MQ Appliance should be the emergency admin account of last resort referred to as the "Fallback user". This account is automatically inactive and not accessible as long as LDAP access is enabled. If network access to the LDAP server is lost, the MQ appliance will automatically enable the Fallback user account to allow for emergency administrative access. If a former admin knows the Fallback user password, still has network access, and can force the MQ appliance to not communicate with the LDAP server, they could access the MQ appliance using the Fallback user credentials. The Fallback user account password must be changed whenever MQ administrators leave the group/team or if their roles change and they no longer require access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ appliance WebGUI as an admin user. Click Administration (gear icon) >> Access. Select User Account and User Group options. Review user names that are displayed. Local user accounts should not be shared. The only exception is the local "Fallback" user account of last resort, which is used for emergency access. Verify that no user accounts other than the designated Fallback user emergency account exist or are shared. Verify the local Fallback user password is changed whenever MQ administrators leave the team and no longer have a need to access the MQ device. If any user accounts other than the Fallback user exist or are shared, or if the local Fallback user password is not changed when MQ admins leave the team/group, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255757`

### Rule: The MQ Appliance network device must notify the administrator, upon successful logon (access), of the location of last logon (terminal or IP address) in addition to the result, date and time of the last logon (access).

**Rule ID:** `SV-255757r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Administrators need to be aware of activity that occurs regarding their account. Providing them with information deemed important by the organization may aid in the discovery of unauthorized access or thwart a potential attacker. Organizations should consider the risks to the specific information system being accessed and the threats presented by the device to the environment when configuring this option. An excessive or unnecessary amount of information presented to the administrator at logon is not recommended. MQ provides logon information including date, time and source IP information in event logs. A third party log monitoring solution that monitors the logs for unsuccessful logons and corresponding date, time and location information must be utilized to provide the notification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Request third-party log monitoring alarming information that provides the notification alerts regarding logons, dates, times, and source IP addresses. If it is not set to LDAP and third-party alarming notifications are not used, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255758`

### Rule: The MQ Appliance network device must generate an immediate alert when allocated audit record storage volume reaches 75 percent of repository maximum audit record storage capacity.

**Rule ID:** `SV-255758r1000069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. This could lead to the loss of audit information. Note that while the MQ Appliance network device must generate the alert, notification may be done by a management server. At the syslog server, set up event notification triggers for the following event codes: 0x80c0006a, 0x82400067, 0x00330034, 0x80400080. Note: The above notifications will occur if there is an interruption in logging information being sent to its intended external logging target. Configuring notification of storage capacity events occurring at the external logging server (e.g., 75 percent capacity) is the responsibility of that server's server administrator. Satisfies: SRG-APP-000359-NDM-000294, SRG-APP-000360-NDM-000295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Ask the system admin to provide evidence the following alert triggers have been set up: 0x80c0006a, 0x82400067, 0x00330034, 0x80400080. Verify alerts are immediately sent when syslog storage capacity reaches 75% of maximum audit record storage capacity. If any is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255759`

### Rule: The MQ Appliance network device must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-255759r1000070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. On the Manage Appliance tab, select Network >> Interface/NTP Service. Verify: - NTP server destinations are configured; - The NTP servers are located in different geographic regions; and - Status (at the top of the page) is "up". If any is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255760`

### Rule: The MQ Appliance network device must synchronize internal information system clocks to the authoritative time source when the time difference is greater than the organization-defined time period.

**Rule ID:** `SV-255760r1000071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in CCI-001891 because a comparison must be done in order to determine the time difference. The organization-defined time period will depend on multiple factors, most notably the granularity of time stamps in audit logs. For example, if time stamps only show to the nearest second, there is no need to have accuracy of a tenth of a second in clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. On the Manage Appliance tab, select Network >> Interface/NTP Service. Verify: - NTP server destinations are configured; - The NTP servers are located in different geographic regions; and - Status (at the top of the page) is "up". If any is not true, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255761`

### Rule: The MQ Appliance network device must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-255761r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The MQ Appliance network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. On the Manage Appliance tab, select Network >> Interface/NTP Service. Verify: - NTP server destinations are configured; * The NTP servers are located in different geographic regions; and * Status (at the top of the page) is "up". If any is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255762`

### Rule: WebGUI access to the MQ Appliance network device must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-255762r1000072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Verify MQ Appliance PKI-based user authentication is configured. Verify an SSL Server Profile is associated with the WebGUI (CLI). Enter: co show web-mgmt [Note the name of the ssl-server] Display the parameters of the ssl-server (CLI). Enter: co crypto ssl-server <ssl-server name> show [Note the name of the valcred] Display the certificates in the ValCred (CLI). Enter: co crypto valcred <name of valcred> show Verify all listed client certificates are authorized to access the MQ Appliance. If any are not authorized, this is a finding. Spot-check access to the appliance: Attempt to access the appliance from a browser enabled with an authorized certificate. If authorized access does not succeed, this is a finding. Attempt to access the appliance from a browser not enabled with an authorized client certificate. If unauthorized access succeeds, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255763`

### Rule: WebGUI access to the MQ Appliance network device must electronically verify Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-255763r1000073_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Verify MQ Appliance PKI-based user authentication is configured. Verify an SSL Server Profile is associated with the WebGUI (CLI). Enter: co show web-mgmt [Note the name of the ssl-server] Display the parameters of the ssl-server (CLI). Enter: co crypto ssl-server <ssl-server name> show [Note the name of the valcred] Display the certificates in the ValCred (CLI). Enter: co crypto valcred <name of valcred> show Verify all listed client certificates are authorized to access the MQ Appliance. Spot-check access to the appliance: Attempt to access the appliance from a browser enabled with an authorized certificate. Attempt to access the appliance from a browser not enabled with an authorized client certificate. If unauthorized access succeeds, this is a finding.

## Group: SRG-APP-000400-NDM-000313

**Group ID:** `V-255764`

### Rule: The MQ Appliance network device must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-255764r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some authentication implementations can be configured to use cached authenticators. If cached authentication information is out of date, the validity of the authentication information may be questionable. The organization-defined time period should be established for each device depending on the nature of the device; for example, a device with just a few administrators in a facility with spotty network connectivity may merit a longer caching time period than a device with many administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP and the cache setting is defined and specifies the organization-defined time period. If the Authentication Method is not set to LDAP and the cache setting does not specify the organization-defined time period, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255765`

### Rule: Applications used for nonlocal maintenance sessions using the MQ Appliance WebGUI must implement cryptographic mechanisms to protect the confidentiality and integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-255765r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions. Satisfies: SRG-APP-000411-NDM-000330, SRG-APP-000412-NDM-000331</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Display the SSL Server Profile associated with the WebGUI (CLI). Enter: co show web-mgmt Verify the following: An ssl-server is associated with the WebGUI. [Note the name of the ssl-server.] List parameters of the SSL Server (CLI). Enter: co crypto ssl-server <ssl-server name> show Verify the following: protocols TLSv1d2 If TLS protocol is not configured for use with the ssl-server, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-255766`

### Rule: The MQ Appliance network device must generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-255766r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Using a syslog logging target, the MQ Appliance logs all logons to the device-, including the source, time and date, and identity of the user. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. Audit records can be generated from various components within the MQ Appliance network device (e.g., module or policy filter). It is the responsibility of the sysadmin to configure the triggers necessary to send alerts based upon information received at the syslog server. The sysadmin can trigger notifications upon receiving the following audit event: 0x81000033. This is the logon event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Log onto the MQ appliance from two different workstations simultaneously. Request a copy of the audit logs and verify both events were recorded in the logs. If log events were not created, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255767`

### Rule: The MQ Appliance network device must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-255767r1000074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Using a syslog logging target, the MQ Appliance logs all audit events, including account creations, modifications, disabling, and termination events. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. Audit records can be generated from various components within the MQ Appliance network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters, e.g., event audit info. In the WebGUI, Manage Appliance/User access. Create, disable or modify an account. Verify the administrator receives notification of this event. If any is not true, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-255768`

### Rule: The MQ Appliance network device must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-255768r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Using a syslog logging target, the MQ Appliance logs all audit records to the syslog. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Ask the system admin to provide logs from syslog server and verify the MQ appliance is logging to the syslog server. If the logs are not off-loaded, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255769`

### Rule: The MQ Appliance network device must use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and in association with CJCSM 6510.01B.

**Rule ID:** `SV-255769r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged into the MQ Appliance network device. An example of a mechanism to facilitate this would be through the use of SNMP traps. Using a syslog logging target, the MQ Appliance logs all audit and system events. Logging may be set to the following logging levels in descending order of criticality: debug, info, notice, warn, error, alert, emerg. The default is notice. It is the responsibility of the sysadmin to configure the triggers necessary to send alerts based upon information received at the syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. Enter: co show logging target All configured logging targets will be displayed. Verify: - This list includes a remote syslog notification target; and - It includes all desired log event source and log level parameters: event audit info event auth notice event mgmt notice event cli notice event user notice event system error Ask the system admin to provide evidence the required alert triggers have been set up. If any is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255770`

### Rule: Administrative accounts for device management must be configured on the authentication server and not the MQ Appliance network device itself (except for the emergency administration account).

**Rule ID:** `SV-255770r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network MQ Appliance device management. Maintaining local administrator accounts for daily usage on each MQ Appliance network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some MQ Appliance network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. Administrative accounts for network MQ Appliance device management must be configured on the authentication server and not the MQ Appliance network device itself. The only exception is for the emergency administration account (also known as the account of last resort), which is configured locally on each device. Note that more than one emergency administration account may be permitted if approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. Verify only one Fallback user is specified. If administrative accounts other than the Fallback user are on the local MQ appliance, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255771`

### Rule: Access to the MQ Appliance network device must employ automated mechanisms to centrally apply authentication settings.

**Rule ID:** `SV-255771r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network MQ Appliance device management. Maintaining local administrator accounts for daily usage on each MQ Appliance network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some MQ Appliance network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. Satisfies: SRG-APP-000516-NDM-000337, SRG-APP-000516-NDM-000338, SRG-APP-000325-NDM-000285</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to Administration (gear icon) >> Access >> RBM Settings. Verify the Authentication Method is set to LDAP. If MQ is not set to LDAP authentication, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-255772`

### Rule: The MQ Appliance network device must support organizational requirements to conduct backups of system level information contained in the information system when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-255772r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the MQ Appliance network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the MQ Appliance network device to support the organizational central backup process for system-level information associated with the MQ Appliance network device. This function may be provided by the MQ Appliance network device itself; however, the preferred best practice is a centralized backup rather than each MQ Appliance network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system admin and determine how the MQ system is backed up. The MQ Appliance provides three features for providing system backup: - High Availability (HA) configuration of paired appliances https://ibm.biz/Bd43aV - Disaster Recovery (DR) configuration using a paired off-site appliance https://ibm.biz/Bd43au - Manual backup and restore https://ibm.biz/Bd43ah If manual backup and restore is used verify backups are performed when changes to the system occur or at least weekly. If none of the above methods are employed or if no backups exist, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255773`

### Rule: The MQ Appliance network device must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255773r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. To verify certs, enter: co crypto show certificate [lists all defined cert aliases] Verify the following: All certificate aliases point to standard DoD cert files and none are self-generated. If the certificates were not generated by a DoD approved CA, or if they are self-signed certificates, this is a finding.

## Group: SRG-APP-000408-NDM-000314

**Group ID:** `V-255774`

### Rule: SSH CLI access to the MQ Appliance management interface must be restricted to approved management workstations.

**Rule ID:** `SV-255774r961545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The approved method for authenticating to systems is via two-factor authentication. Two-factor authentication is defined as using something you have (e.g., CAC or token) and something you know (e.g., PIN). The SSH CLI in MQ does not have the native ability to use multifactor authentication. This increases the risk of user account compromise. Restricting access to the MQ SSH management interface helps to mitigate this risk. Access must be restricted to only those management workstations or networks that require access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance WebGUI as a privileged user. Go to the Network icon. Select Management >> SSH Service. Click "edit" next to the Access control list field. View the SSH ACL and obtain the list of authorized addresses. Ask the administrator for the list of approved addresses. If an authorized management network is in place, the SSH ACL can include a range of addresses within the authorized management network. If a firewall is used to isolate SSH traffic, request the IP addresses of the MQ appliance and the relevant firewall ruleset. If SSH traffic is not restricted to the list of approved addresses, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-265886`

### Rule: The version of MQ Appliance messaging server running on the system must be a supported version.

**Rule ID:** `SV-265886r1001152_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MQ Appliance messaging server 9.x is no longer supported by the vendor. If the system is running MQ Appliance 9.x, this is a finding.

