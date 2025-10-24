# STIG Benchmark: Riverbed SteelHead CX v8 NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255438`

### Rule: Riverbed Optimization System (RiOS) must provide automated support for account management functions.

**Rule ID:** `SV-255438r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The network device must be configured to automatically provide account management functions, and these functions must immediately enforce the organization's current account policy. All accounts used for access to the network device are privileged or system-level accounts. Therefore, if account management functions are not automatically enforced, an attacker could gain privileged access to a vital element of the network security architecture. This control does not include emergency administration accounts that provide access to the network device components in case of network failure. There must be only one such locally defined account. All other accounts must be defined. All other accounts must be created and managed on the site's authentication server (e.g., RADIUS, LDAP, or Active Directory). This requirement is applicable to account management functions provided by the network device application. If the function is provided by the underlying OS or an authentication server, it must be secured using the applicable security guide or STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS provides automated support for account management. Navigate to the device Management Console Navigate to: Configure >> Security >> User Permissions Verify user permissions are defined here. If the account management is not set, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-255439`

### Rule: Riverbed Optimization System (RiOS) must terminate local shared/group account credentials, such as the Admin account is used, when members who know the account password leave the group.

**Rule ID:** `SV-255439r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples include system accounts, account of last resort, accounts used for testing/maintenance, and shared secrets that are configured on the administrator's workstation. When users with knowledge of the account of last resort or default accounts are no longer authorized, account credentials must be changed in accordance with DoD policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify RiOS is configured to protect the confidentiality and integrity of system information at rest. Navigate to the Device Management Console Set the "Username" to "admin" Set the "Password" to "password" Click "Log In" If login occurs and administrative access is allowed, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-255440`

### Rule: Riverbed Optimization System (RiOS) must disable the local Shark and Monitor accounts so they cannot be used as shared accounts by users.

**Rule ID:** `SV-255440r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Monitor and Shark accounts which are default group accounts with shared credentials. Monitor and Shark accounts are not enabled by default, but cannot be deleted since these network tools are designed to look for that account. Monitor is a read-only account for auditor's configuration management. Shark is used to access packet captures. If the credentials for these accounts are changed, the function of the system will not be adversely impacted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to the assigned privilege level for each administrator. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Verify the privilege level values for Shark and Monitor If all privileges for the Shark and Monitor accounts are not set to Deny, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-255441`

### Rule: Riverbed Optimization System (RiOS) must automatically generate a log event for account creation events.

**Rule ID:** `SV-255441r960777_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate a log event for account creation events. Create an account Navigate to the device Management Console, then Navigate to: Reports >> Diagnostics >> System Logs Enter the account name into the filter and click Go Delete the account that was created If no event record for the user creation action exists in the event log, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-255442`

### Rule: Riverbed Optimization System (RiOS) must automatically log event for account modification.

**Rule ID:** `SV-255442r960780_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate a log event for account creation events. Create an account Modify this user account Navigate to the device Management Console, then Navigate to: Reports >> Diagnostics >> System Logs Enter the account name into the filter and click Go Delete the account that was created If no event record for the user creation action exists in the event log, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-255443`

### Rule: Riverbed Optimization System (RiOS) must automatically generate a log event for account disabling actions.

**Rule ID:** `SV-255443r960783_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate a log event for account creation events. Create an account To disable an account Navigate to the device Management Console, then Navigate to: Configure >> Security >> User >> Permissions Deselect Enable Account Click "Apply" Navigate to the device Management Console, then Navigate to: Reports >> Diagnostics >> System Logs Enter the account name into the filter and click Go Delete the account that was created If no event record for the user disabling action exists in the event log, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-255444`

### Rule: Riverbed Optimization System (RiOS) must automatically generate a log event for account removal actions.

**Rule ID:** `SV-255444r960786_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate a log event for account creation events. Create an account To disable an account Navigate to the device Management Console, then Navigate to: Configure >> Security >> User >> Permissions Select the account to be removed Click Remove Selected Account Navigate to the device Management Console, then Navigate to: Reports >> Diagnostics >> System Logs Enter the account name into the filter and click "Go" Delete the account that was created. If no event record for the user removal action exists in the event log, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255445`

### Rule: Riverbed Optimization System (RiOS) must generate alerts that can be forwarded to the administrators and ISSO when local accounts are created.

**Rule ID:** `SV-255445r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authorized insider or individual who maliciously creates a local account could gain immediate access from a remote location to privileged information on a critical security device. Sending an alert to the administrators and ISSO when this action occurs greatly reduces the risk that accounts will be surreptitiously created. RiOS can be configured to send an SNMP trap to the SNMP server. It also sends a message to the Syslog and the local log. Either of these methods results in an alert that can be forwarded to authorized accounts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS captures an SNMP trap for user creation events that can be sent to the ISSO and designated administrators by the SNMP server. Navigate to the device Management Console Navigate to Configure >> System Settings >> Email Verify that an SMTP Server is defined Verify that an SMTP Port is defined Verify that "Report Events via Email" is checked and that at least one email address is defined Verify that "Report Failures via Email" is checked and that at least one email address is defined If an email for the ISSO and the system administrator accounts are not defined, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255446`

### Rule: Riverbed Optimization System (RiOS) must generate alerts that can be forwarded to the administrators and ISSO when accounts are modified.

**Rule ID:** `SV-255446r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the modification of device administrator accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes. The network device must generate the alert. Notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS uses automated mechanisms to alert security personnel to threats identified by authoritative sources. Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that Host Servers are defined in the section "Trap Receivers" If there are no Host Servers defined in "Trap Receivers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255447`

### Rule: Riverbed Optimization System (RiOS) must generate alerts that can be forwarded to the administrators and ISSO when accounts are disabled.

**Rule ID:** `SV-255447r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When application accounts are disabled, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS uses automated mechanisms to alert security personnel to threats identified by authoritative sources. Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that Host Servers are defined in the section "Trap Receivers" If there are no Host Servers defined in "Trap Receivers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255448`

### Rule: Riverbed Optimization System (RiOS) must generate alerts that can be forwarded to the administrators and ISSO when accounts are removed.

**Rule ID:** `SV-255448r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>When application accounts are removed, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS uses automated mechanisms to alert security personnel to threats identified by authoritative sources. Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that Host Servers are defined in the section "Trap Receivers" If there are no Host Servers defined in "Trap Receivers", this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-255449`

### Rule: Riverbed Optimization System (RiOS) must enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level in accordance with applicable policy for the device.

**Rule ID:** `SV-255449r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Network devices use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the network device to control access between administrators (or processes acting on behalf of administrators) and objects (e.g., device commands, files, records, processes) in the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to the assigned privilege level for each administrator. Navigate to the device CLI Type: show rbm users Verify that the privilege level is correct for each administrator -- or -- Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Verify that the privilege level is correct for each administrator If the privilege level settings are not in accordance with applicable policy, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-255450`

### Rule: Riverbed Optimization System (RiOS) must generate a log event when privileged functions are executed.

**Rule ID:** `SV-255450r961362_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device generates a log event when commands are executed. Navigate to the device Management Console Navigate to Configure >> System Settings >> Logging Under Logging Configurations, verify Minimum Severity is set to Info If the Standard Mandatory DoD Notice and Consent Banner does not exist on this page, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255451`

### Rule: Riverbed Optimization System (RiOS) must enforce the limit of three (3) consecutive invalid logon attempts by a user during a 15-minute time period for device console access.

**Rule ID:** `SV-255451r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to limit the number of invalid logon attempts during a 15 minute period to 3. Login to the device console to access the command line interface (CLI) Type: show authentication policy Verify that "Maximum unsuccessful logins before account lockout:" is set to "3" Verify that "Wait before account unlock:" is set to "900" seconds If "Maximum unsuccessful logins before account lockout" is not set to "3" and/or "Wait before account unlock" is not set to "900" seconds, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255452`

### Rule: Riverbed Optimization System (RiOS) must enforce the limit of three (3) consecutive invalid logon attempts by a user during a 15-minute time period for web-based management access.

**Rule ID:** `SV-255452r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to limit the number of invalid logon attempts during a 15 minute period to 3. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Login Attempts Before Lockout:" is set to "3" Verify that "Timeout for User Login After Lockout (seconds)" is set to "900" If "Login Attempts Before Lockout" is not set to "3" and/or "Timeout for User Login After Lockout (seconds)" is not set to "900", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255453`

### Rule: Riverbed Optimization System (RiOS) must automatically lock the account until the locked account is released by an administrator when three unsuccessful login attempts in 15 minutes are exceeded.

**Rule ID:** `SV-255453r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to limit the number of unsuccessful login attempts during a 15-minute period to 3. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Login Attempts Before Lockout:" is set to "3" Verify that "Timeout for User Login After Lockout (seconds)" is set to "900" If "Login Attempts Before Lockout" is not set to "3" and/or "Timeout for User Login After Lockout (seconds)" is not set to "900", this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-255454`

### Rule: Riverbed Optimization System (RiOS) must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-255454r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device. Navigate to the device Management Console Navigate to Configure >> System Settings >> Announcements Verify that the Standard Mandatory DoD Notice and Consent Banner is contained in the Logon Message If the Standard Mandatory DoD Notice and Consent Banner does not exist on this page, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-255455`

### Rule: Riverbed Optimization System (RiOS) must limit the number of concurrent sessions to one (1) for each administrator account and/or administrator account type.

**Rule ID:** `SV-255455r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. Recommended best practice for authentication and authorization is to leverage an AAA server (e.g., TACACS or RADIUS). Password of Last Resort is not affected by this requirement. Note that this is a hidden CLI command. Access to the device management console is not affected by this command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to limit the number of concurrent sessions to one (1) for each administrator account and/or administrator account type. This requirement does not apply to the Admin account. Navigate to the device CLI Type: enable Type: show username <user-other-than-admin> detailed Verify that "Maximum Logins" is set to "1" If "Maximum Logins" is not set to "1", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255456`

### Rule: Riverbed Optimization System (RiOS) must automatically terminate a network administrator session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-255456r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of administrator-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever an administrator (or process acting on behalf of a user) accesses a network device. Such administrator sessions can be terminated (and thus terminate network administrator access) without terminating network sessions. Session termination terminates all processes associated with an administrator's logical session except those processes that are specifically created by the administrator (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. These conditions will vary across environments and network device types.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to terminate a network administrator's session after a trigger event such as inactivity timeout. Navigate to the device CLI Type: enable Type: show web Verify that "Inactivity Timeout:" is set to the organizations defined condition If no triggers are required by the organization, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-255457`

### Rule: Riverbed Optimization System (RiOS) must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-255457r960909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate audit records containing the full-text recording of privileged commands Navigate to the device Management Console Navigate to Configure >> System Settings >> Logging Verify that "Minimum Severity" is set to "info" If the "Minimum Severity" is not set to "info", this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-255458`

### Rule: Riverbed Optimization System (RiOS) must generate an email alert of all log failure events requiring alerts.

**Rule ID:** `SV-255458r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate an immediate real-time alert for all audit failure events requiring real-time alerts. Navigate to the device Management Console Navigate to Configure >> System Settings >> Email Verify that an SMTP Server is defined Verify that an SMTP Port is defined Verify that "Report Events via Email" is checked and that at least one email address is defined Verify that "Report Failures via Email" is checked and that at least one email address is defined If no email accounts are defined, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255459`

### Rule: Riverbed Optimization System (RiOS) must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-255459r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS uses automated mechanisms to alert security personnel to threats identified by authoritative sources. Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that Host Servers are defined in the section "Trap Receivers" If there are no Host Servers defined in "Trap Receivers", this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-255460`

### Rule: Riverbed Optimization System (RiOS) must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-255460r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured select UTC. Navigate to the device Management Console Navigate to Configure >> System Settings >> Date and Time Verify that "UTC" is selected If no NTP Servers are visible after the command "show ntp all" or on "Requested Servers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255461`

### Rule: Riverbed Optimization System (RiOS) must protect audit information from any type of unauthorized read access.

**Rule ID:** `SV-255461r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult, if not impossible, to achieve. In addition, access to audit records provides information an attacker could use to his or her advantage. To ensure the veracity of audit data, the information system and/or the network device must protect audit information from any and all unauthorized read access. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, network devices with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the device interface. If the device provides access to the audit data, the device becomes accountable for ensuring audit information is protected from unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to protect audit information from any type of unauthorized read access. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the view icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-255462`

### Rule: Riverbed Optimization System (RiOS) must protect audit information from unauthorized modification.

**Rule ID:** `SV-255462r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to protect audit information from unauthorized modification. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the "View" icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-255463`

### Rule: Riverbed Optimization System (RiOS) must protect audit information from unauthorized deletion.

**Rule ID:** `SV-255463r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to protect audit information from unauthorized deletion. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the "View" icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-255464`

### Rule: Riverbed Optimization System (RiOS) must protect audit tools from unauthorized access.

**Rule ID:** `SV-255464r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to protect audit tools from unauthorized access. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the "View" icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000123-NDM-000240

**Group ID:** `V-255465`

### Rule: Riverbed Optimization System (RiOS) must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-255465r960945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operations on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to protect audit tools from unauthorized deletion. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the "View" icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255466`

### Rule: Riverbed Optimization System (RiOS) must provide audit record generation capability for DoD-defined auditable events within the network device.

**Rule ID:** `SV-255466r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to off-load audit records (logs) onto a different system than the system being audited. Navigate to the device Management Console Navigate to Configure >> System Settings >> Logging Verify that "Remote Log Servers" contains IP addresses for all available log servers View "Per-Process Logging" section to see if a process or severity has been configured. Note: This only affects the system log, not the user type facilities. If a filter has been added in 'Per-Process Logging" which prevents the capture of DoD-defined auditable events, this is a finding. If "Remote Log Servers" is empty and no remote log servers are configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255467`

### Rule: Riverbed Optimization System (RiOS) must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be logged.

**Rule ID:** `SV-255467r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS restricts permission to select auditable event to authorized administrators. Navigate to the device Management Console Navigate to: Configure >> Security >> User Permissions Verify the "Deny" attribute is selected for "Basic Diagnostics", "TCP Dumps", "Reports" permissions If the "Deny" attribute is not set for users who are not authorized access to configure auditable events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255468`

### Rule: Riverbed Optimization System (RiOS) must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-255468r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions. Navigate to the device CLI Type: enable Type: show ntp all Verify that at least two NTP Servers are configured -- or -- Navigate to the device Management Console Navigate to Configure >> System Settings >> Date and Time Verify that at least two servers are configured in the section "Requested Servers" If no NTP Servers are visible after the command 'show ntp all' or on "Requested Servers", this is a finding.

## Group: SRG-APP-000381-NDM-000305

**Group ID:** `V-255469`

### Rule: Riverbed Optimization System (RiOS) must generate a log event for the enforcement actions used to restrict access associated with changes to the device.

**Rule ID:** `SV-255469r984111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the device configuration, it will be difficult to identify attempted attacks, and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact. For RiOS, all configuration changes authorized or unauthorized are logged in the system logs. Log entries include the user that initiated the configuration change for accountability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to audit the enforcement actions used to restrict access associated with changes to the device. Navigate to the device Management Console Navigate to Configure >> System Settings >> Logging Verify that "Minimum Severity" is set to "info" If the minimum severity is not set to "info", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255470`

### Rule: Riverbed Optimization System (RiOS) must enable the password authentication control policy to ensure password complexity controls and other password policy requirements are enforced.

**Rule ID:** `SV-255470r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify authentication policy is enabled. Navigate to the device Management Console Navigate to: Configure >> Security >> Password Policy Verify the "Enable Account Control" is selected If "Enable Account Control" is not set, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255471`

### Rule: Riverbed Optimization System (RiOS) must employ automated mechanisms to centrally manage authentication settings.

**Rule ID:** `SV-255471r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to employ automated mechanisms to centrally manage authentication settings. Navigate to the device Management Console Navigate to Configure >> Security >> TACACS+ Verify that "TACACS+ Servers" has at least one server defined -- or -- Navigate to Configure >> Security >> RADIUS Verify that "RADIUS Servers" has at least one server defined If no servers exist in "TACACS+ Servers" or "RADIUS Servers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255472`

### Rule: Riverbed Optimization System (RiOS) must employ automated mechanisms to centrally apply authentication settings.

**Rule ID:** `SV-255472r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to employ automated mechanisms to centrally apply authentication settings. Navigate to the device Management Console Navigate to Configure >> Security >> TACACS+ Verify that "TACACS+ Servers" has at least one server defined -- or -- Navigate to Configure >> Security >> RADIUS Verify that "RADIUS Servers" has at least one server defined If no servers exist in "TACACS+ Servers" or "RADIUS Servers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255473`

### Rule: Riverbed Optimization System (RiOS) must employ automated mechanisms to centrally verify authentication settings.

**Rule ID:** `SV-255473r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to employ automated mechanisms to centrally verify authentication settings. Navigate to the device Management Console Navigate to Configure >> Security >> TACACS+ Verify that "TACACS+ Servers" has at least one server defined -- or -- Navigate to Configure >> Security >> RADIUS Verify that "RADIUS Servers" has at least one server defined If no servers exist in "TACACS+ Servers" or "RADIUS Servers", this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-255474`

### Rule: Riverbed Optimization System (RiOS) must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-255474r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments. Navigate to the device Management Console Navigate to Configure >> Security >> Management ACL Verify that this page contains all unnecessary and/or nonsecure functional, ports, protocols, and/or services as defined in the PPSM CAL and vulnerability assessments. Verify that "Enable Management ACL" is checked. If no PPSM CAL or vulnerability assessment information is presented on this page or "Enable Management ACL" is not checked, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-255475`

### Rule: Riverbed Optimization System (RiOS) must back up the system configuration files when configuration changes are made to the device.

**Rule ID:** `SV-255475r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is backed up when system configuration changes are made to the device by interviewing the site representative and checking any existing backup log. Evidence may also be provided by the date of the last back up. Navigate to the device Management Console Navigate to Configure >> Configurations Verify that the table for "Configuration" and "Date" contains backup configurations If there are no entries under "Configuration" and "Date", this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-255476`

### Rule: Riverbed Optimization System (RiOS) must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-255476r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to implement replay resistant authentication mechanisms for network access to privileged accounts. Navigate to the device CLI Type: enable Type: show config full Type: Spacebar to tab through the configuration Verify that the following commands are contained in the configuration "no web http enable" "web https enable" "no web ssl protocol sslv3" "no web ssl protocol tlsv1" "web ssl protocol tlsv1.1" "web ssl protocol tlsv1.2" If all of the above configurations are not defined as listed, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255477`

### Rule: Riverbed Optimization System (RiOS) must authenticate network management endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255477r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to authenticate network management endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based (network management portion of the requirement). Navigate to the device CLI Type: enable Type: show configuration full Verify that 'no telnet-server enable' is in the configuration Verify that 'ssh server enable' is set in the configuration Verify that 'web enable' is in the configuration Verify that 'no web http enable' is in the configuration Verify that 'web https enable' is in the configuration If any one of the above settings is missing from the configuration, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255478`

### Rule: Riverbed Optimization System (RiOS) must authenticate SNMP server before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255478r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to authenticate SNMP server before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based (SNMP portion of the requirement). Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that at least one "Host" is defined under "Trap Receivers" Verify that the "Host" defined under "Trap Receivers" is set for "Version" v3 Verify that "Enable SNMP Traps" is set If no "Host" exists under "Trap Receivers or the "Host" is not "Version" v3 and/or "Enable SNMP Traps" is not set, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255479`

### Rule: Riverbed Optimization System (RiOS) must authenticate  NTP server before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255479r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to authenticate NTP server before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based (NTP portion of the requirement). Navigate to the device CLI Type: enable Type: show ntp all Verify that at least two NTP Servers are configured Type: show ntp authentication Verify the "Trusted Keys" are defined for use with NTP -- or -- Navigate to the device Management Console Navigate to Configure >> System Settings >> Date and Time Verify that at least two servers are configured in the section "Requested Servers" If no NTP Servers are visible after the command 'show ntp all' or on "Requested Servers", this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255480`

### Rule: Riverbed Optimization System (RiOS) must enforce a minimum 15-character password length.

**Rule ID:** `SV-255480r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce a minimum 15-character password length. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Password Length:" is set to "15" If "Minimum Password Length:" is not set to "15", this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-255481`

### Rule: Riverbed Optimization System (RiOS) must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-255481r984095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce password complexity that requires at least one upper-case character. Navigate to the device Management Console Navigate to Configure >> Security>Password Policy Verify that "Minimum Uppercase Characters:" is set to "1" If "Minimum Uppercase Characters:" is not set to "1", this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-255482`

### Rule: Riverbed Optimization System (RiOS) must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-255482r984098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce password complexity that requires at least one lower-case character. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Lowercase Characters:" is set to "1" If "Minimum Lowercase Characters:" is not set to "1", this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-255483`

### Rule: Riverbed Optimization System (RiOS) must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-255483r984099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce password complexity that requires at least one numeric character. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Numerical Characters:" is set to "1" If "Minimum Numerical Characters:" is not set to "1", this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-255484`

### Rule: Riverbed Optimization System (RiOS) must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-255484r984100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce password complexity that requires at least one special character. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Special Characters:" is set to "1" If "Minimum Special Characters:" is not set to "1", this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-255485`

### Rule: Riverbed Optimization System (RiOS) must require that when a password is changed, the characters are changed in at least 15 of the positions within the password.

**Rule ID:** `SV-255485r984101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to require that when a password is changed, the characters are changed in at least 15 of the positions within the password. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Character Difference Between Passwords:" is set to "15" If "Minimum Character Difference Between Passwords:" is not set to "15", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255486`

### Rule: Riverbed Optimization System (RiOS) must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-255486r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the network device in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to enforce a 60-day maximum password lifetime restriction. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Days Before Password Expires:" is set to "60" If "Days Before Password Expires:" is not set to "60", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255487`

### Rule: Riverbed Optimization System (RiOS) must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-255487r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to prohibit password reuse for a minimum of five generations. Navigate to the device Management Console Navigate to Configure >> Security >> Password Policy Verify that "Minimum Interval for Password Reuse:" is set to "5" If "Minimum Interval for Password Reuse:" is not set to "5", this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-255488`

### Rule: Riverbed Optimization System (RiOS) must use mechanisms meeting the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-255488r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. Note that adding the FIPS 140-2 licenses incurs a cost from the vendor for support for FIPS mode/module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is licensed to use FIPS 140-2 cryptographic modules. Navigate to the device CLI Type: enable Type: config t Type: show licenses Verify installation of a FIPS License Type: show web ssl cipher Verify that the web ssl cipher string is: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If a FIPS license is not present and the web ssl cipher string is not set properly, this is a finding.

## Group: SRG-APP-000408-NDM-000314

**Group ID:** `V-255489`

### Rule: Riverbed Optimization System (RiOS) performing maintenance functions must restrict use of these functions to authorized personnel only.

**Rule ID:** `SV-255489r961545_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are security-related issues arising from software brought into the network device specifically for diagnostic and repair actions (e.g., a software packet sniffer installed on a device in order to troubleshoot system traffic, or a vendor installing or running a diagnostic application in order to troubleshoot an issue with a vendor-supported device). If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. This requirement addresses security-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational network devices. Maintenance tools can include hardware, software, and firmware items. Maintenance tools are potential vehicles for transporting malicious code, either intentionally or unintentionally, into a facility and subsequently into organizational information systems. Maintenance tools can include, for example, hardware/software diagnostic test equipment and hardware/software packet sniffers. This requirement does not cover hardware/software components that may support information system maintenance yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured so that performing maintenance functions is restricted to authorized personnel only. Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Verify that only authorized personnel have the permissions to perform maintenance functions If user permissions for authorized personnel are not set to authorize maintenance functions, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255490`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-255490r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications. Navigate to the device CLI Type: enable Type: show configuration full Verify that "no telnet-server enable" is in the configuration Verify that "ssh server enable" is set in the configuration Verify that "web enable" is in the configuration Verify that "no web http enable" is in the configuration Verify that "web https enable" is in the configuration If any one of the above settings is missing from the configuration, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-255491`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-255491r961557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications. Navigate to the device CLI Type: enable Type: show configuration full Verify that "no telnet-server enable" is in the configuration Verify that "ssh server enable" is set in the configuration Verify that "web enable" is in the configuration Verify that "no web http enable" is in the configuration Verify that "web https enable" is in the configuration If any one of the above settings is missing from the configuration, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255492`

### Rule: Riverbed Optimization System (RiOS) must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255492r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to terminate a device management session at the end of the session, or after 10 minutes of inactivity. Navigate to the device CLI Type: enable Type: show web Verify that "Inactivity Timeout:" is set to "10" minutes -- or -- Navigate to the device Management Console Navigate to Configure >> Security >> Web Settings Verify that "Web Inactivity Timeout (minutes):" is set to "10" If "Inactivity Timeout" or "Web Inactivity Timeout (minutes)" is not set to "10", this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255493`

### Rule: Riverbed Optimization System (RiOS) must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255493r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider. Navigate to the device Management Console Navigate to Configure >> Optimization >> Certificate Authorities Verify that DoD Root Certificates are listed on this page If no DoD Root CA Certificates are listed on this page, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-255494`

### Rule: Riverbed Optimization System (RiOS) must generate unique session identifiers using a FIPS 140-2 approved random number generator.

**Rule ID:** `SV-255494r961119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sequentially generated session IDs can be easily guessed by an attacker. Employing the concept of randomness in the generation of unique session identifiers helps to protect against brute-force attacks to determine future session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement is applicable to devices that use a web interface for device management. Recommended best practice is that the FIPS license be installed and utilized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to generate unique session identifiers using a FIPS 140-2 approved random number generator. Navigate to the device CLI Type: enable Type: conf t Type: show fips status Verify that "FIPS Mode: Enabled" is displayed on the console If "FIPS Mode: Enabled" is not displayed on the console, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-255495`

### Rule: Riverbed Optimization System (RiOS) must protect against or limit the effects of all known types of Denial of Service (DoS) attacks on the network device management network by employing organization-defined security safeguards.

**Rule ID:** `SV-255495r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RIOS is configured to protect against or limit the effects of all know types of Denial of Service (DoS) attacks on the device management network. Navigate to the device Management Console Navigate to Configure >> Security >> Management ACL Verify that there is a rule to limit management access from authorized devices and that the interface is set to other than an in-path interface Verify that "Enable Management ACL" is checked If Management ACLs are not defined to limit access to identified or known devices and/or a management interface is not defined that is different from the in-path interface and/or "Enable Management ACL" is not checked, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255496`

### Rule: Riverbed Optimization System (RiOS) must generate an alert that can be sent to security personnel when threats identified by authoritative sources (e.g., CTOs) and IAW with CJCSM 6510.01B occur.

**Rule ID:** `SV-255496r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged into the network device. An example of a mechanism to facilitate this would be through the utilization of SNMP traps.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS uses automated mechanisms to alert security personnel to threats identified by authoritative sources. Navigate to the device Management Console Navigate to Configure >> System Settings >> SNMP Basic Verify that Host Servers are defined in the section "Trap Receivers" If there are no Host Servers defined in "Trap Receivers", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255497`

### Rule: The application must reveal error messages only to authorized individuals (ISSO, ISSM, and SA).

**Rule ID:** `SV-255497r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state. Additionally, sensitive account information must not be revealed through error messages to unauthorized personnel or their designated representatives.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to reveal error messages only to authorized individuals (ISSO, ISSM, and SA). Navigate to the device Management Console Navigate to Configure >> Security >> User Permissions Select the view icon next to each user name Verify that the Control "Basic Diagnostics" is set according to the authorization level of the user If the control "Basic Diagnostics" is not set according to the authorization level of the user, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-264433`

### Rule: The Riverbed NDM must be using a version supported by the vendor.

**Rule ID:** `SV-264433r992096_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

