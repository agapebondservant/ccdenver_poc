# STIG Benchmark: Juniper SRX SG NDM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-223180`

### Rule: The Juniper SRX Services Gateway must limit the number of concurrent sessions to a maximum of 10 or less for remote access using SSH.

**Rule ID:** `SV-223180r513235_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The connection-limit command limits the total number of concurrent SSH sessions. To help thwart brute force authentication attacks, the connection limit should be as restrictive as operationally practical Juniper Networks recommends the best practice of setting 10 (or less) for the connection-limit. This configuration will permit up to 10 users to log in to the device simultaneously, but an attempt to log an 11th user into the device will fail. The attempt will remain in a waiting state until a session is terminated and made available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX sets a connection-limit for the SSH protocol. Show system services ssh If the SSH connection-limit is not set to 10 or less, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-223181`

### Rule: For local accounts created on the device, the Juniper SRX Services Gateway must automatically generate log records for account creation events.

**Rule ID:** `SV-223181r513238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. An AAA server is required for account management in accordance with CCI-000370. Only a single account of last resort is permitted on the local device. However, since it is still possible for administrators to create local accounts either maliciously or to support mission needs, the SRX must be configured to log account management events. To log local account management events, ensure at least one external syslog server is configured to log facility any or facility change-log, and severity info or severity any.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-223182`

### Rule: For local accounts created on the device, the Juniper SRX Services Gateway must automatically generate log records for account modification events.

**Rule ID:** `SV-223182r513241_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to modify existing accounts to increase/decrease privileges. Notification of account modification events help to mitigate this risk. Auditing account modification events provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. An AAA server is required for account management in accordance with CCI-000370. Only a single account of last resort is permitted on the local device. However, since it is still possible for administrators to create local accounts either maliciously or to support mission needs, the SRX must be configured to log account management events. To log local account management events, ensure at least one external syslog server is configured to log facility any or facility change-log, and severity info or severity any.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-223183`

### Rule: For local accounts created on the device, the Juniper SRX Services Gateway must automatically generate log records for account disabling events.

**Rule ID:** `SV-223183r513244_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized, active accounts remain enabled and available for use when required. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. An AAA server is required for account management in accordance with CCI-000370. Only a single account of last resort is permitted on the local device. However, since it is still possible for administrators to create local accounts either maliciously or to support mission needs, the SRX must be configured to log account management events. To log local account management events, ensure at least one external syslog server is configured to log facility any or facility change-log, and severity info or severity any.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-223184`

### Rule: For local accounts created on the device, the Juniper SRX Services Gateway must automatically generate log records for account removal events.

**Rule ID:** `SV-223184r513247_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. An AAA server is required for account management in accordance with CCI-000370. Only a single account of last resort is permitted on the local device. However, since it is still possible for administrators to create local accounts either maliciously or to support mission needs, the SRX must be configured to log account management events. To log local account management events, ensure at least one external syslog server is configured to log facility any or facility change-log, and severity info or severity any.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-223185`

### Rule: The Juniper SRX Services Gateway must automatically generate a log event when accounts are enabled.

**Rule ID:** `SV-223185r513250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. Accounts can be disabled by configuring the account with the build-in login class "unauthorized". When the command is reissued with a different login class, the account is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system is not configured to generate a log record when account enabling actions occur, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-223186`

### Rule: The Juniper SRX Services Gateway must enforce the assigned privilege level for each administrator and authorizations for access to all commands by assigning a login class to all AAA-authenticated users.

**Rule ID:** `SV-223186r513253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized privileged access to the device, administrators must be assigned only the privileges needed to perform the tasked assigned to their roles. Although use of an AAA server is required for non-local access for device management, the SRX must also be configured to implement the corresponding privileges upon user login. Each externally authenticated user is assigned a template that maps to a configured login class. AAA servers are usually configured to send a Vendor Specific Attribute (VSA) to the Juniper SRX. The device uses this information to determine the login class to assign to the authenticated user. Unless a VSA is returned from the AAA server, externally-authenticated users are mapped to the “remote” user by default. Remote user is a special default account in Junos OS. If this default account, or another designated remote user account, is not configured, then only externally-authenticated users with a returned VSA of a local template account are permitted login. If the remote user is configured, all externally-authenticated users without a returned VSA default to the remote user account's configured login class. All externally-authenticated users with a returned VSA inherit the login class configured for each respective template account. Junos OS provides four built-in login classes: super-user (all permissions), operator (limited permissions), read-only (no change permissions), and unauthorized (prohibits login). Because these classes are not configurable by the system administrator, they should not be used except for the unauthorized class which may be used for the remote user to deterministically prohibit logins from externally-authenticated users without a returned VSA. Therefore, all template user accounts, and the local account of last resort, should use custom, user-defined, login classes. Externally-authenticated users maintain two account names in Junos OS: the user and login names. The user name is the local template account name and the login name is the authenticated user’s external account name. Junos OS links the names to determine permissions, based upon login class, but uses the external account name for logging. Doing so permits multiple, individually-authenticated users, to be mapped to the same template account, and therefore enforce uniform permissions for each group of administrators, while also attributing any logged changes to the appropriate individual user. Template accounts are differentiated from local accounts by the presence of an authentication stanza; only the local account of last resort should have an authentication stanza.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all accounts are assigned a user-defined (not built-in) login class with appropriate permissions configured. If the remote user is configured, it may have a user-defined, or the built-in unauthorized login class. [edit] show system login Junos OS supports groups, which are centrally located snippets of code. This allows common configuration to be applied at one or more hierarchy levels without requiring duplicated stanzas. If there are no login-classes defined at [edit system login], then check for an apply-groups statement and verify appropriate configuration at the [edit groups] level. [edit] show groups If one or more account templates are not defined with an appropriate login class, this is a finding. If more than one local account has an authentication stanza and is not documented, this is a finding. Note: Template accounts are differentiated from local accounts by the presence of an authentication stanza.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-223187`

### Rule: The Juniper SRX Services Gateway must generate a log event when privileged commands are executed.

**Rule ID:** `SV-223187r513256_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. All commands executed on the Juniper SRX are privileged commands. Thus, this requirement is configured using the same syslog command as CCI-000172.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device generates a log event when privileged commands are executed. [edit] show system syslog If a valid syslog host server and the syslog file names are not configured to capture "any" facility and "any" event, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-223188`

### Rule: For local accounts created on the device, the Juniper SRX Services Gateway must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-223188r513259_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Juniper SRX is unable to comply with the 15-minute time period part of this control.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the number of unsuccessful logon attempts is set to 3. [edit] show system login retry-options If the number of unsuccessful logon attempts is set to 3, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-223189`

### Rule: The Juniper SRX Services Gateway must display the Standard Mandatory DoD Notice and Consent Banner before granting access.

**Rule ID:** `SV-223189r513262_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. The Standard Mandatory DoD Notice and Consent Banner must be displayed before the user has been authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Standard Mandatory DoD Notice and Consent Banner is displayed before the user has been authenticated either locally or by the AAA server by typing the following command at the [edit system login] hierarchy level. [edit] show system login message If the Standard Mandatory DoD Notice and Consent Banner is not displayed before the user has been authenticated, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-223191`

### Rule: The Juniper SRX Services Gateway must generate log records when successful attempts to configure the device and use commands occur.

**Rule ID:** `SV-223191r513265_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. While the Juniper SRX inherently has the capability to generate log records, by default only the high facility levels are captured by default to local files. Ensure at least one Syslog server and local files are configured to support requirements. However, the Syslog itself must also be configured to filter event records so it is not overwhelmed. A best practice when configuring the external Syslog server is to add similar log-prefixes to the log file names to help and researching of central Syslog server. Another best practice is to add a match condition to limit the recorded events to those containing the regular expression (REGEX).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging has been enabled and configured. [edit] show system syslog If a valid syslog host server and the syslog file names are not configured to capture "any" facility and "any" event, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-223192`

### Rule: The Juniper SRX Services Gateway must generate log records when changes are made to administrator privileges.

**Rule ID:** `SV-223192r513268_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-223193`

### Rule: The Juniper SRX Services Gateway must generate log records when administrator privileges are deleted.

**Rule ID:** `SV-223193r513271_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device logs change-log events of severity info or any to an external syslog server. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } -OR- host <syslog server address> { change-log <info | any>; source-address <device address>; } If an external syslog host is not configured to log facility change-log severity <info | any>, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-223194`

### Rule: The Juniper SRX Services Gateway must generate log records when logon events occur.

**Rule ID:** `SV-223194r513274_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device generates a log when login events occur. [edit] show system syslog host <syslog server address> { any <info | any>; source-address <device address>; } If an external syslog host is not configured to log, or configured for facility any severity <info | any>, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-223195`

### Rule: The Juniper SRX Services Gateway must generate log records when privileged commands are executed.

**Rule ID:** `SV-223195r513277_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device generates a log when login events occur. [edit] show system syslog host <syslog server address> { any any; source-address <device address>; } If an external syslog host is not configured to log, or configured for facility any severity any, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-223196`

### Rule: The Juniper SRX Services Gateway must generate log records when concurrent logons from different workstations occur.

**Rule ID:** `SV-223196r513280_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device generates a log when login events occur. [edit] show system syslog host <syslog server address> { any any; source-address <device address>; } If an external syslog host is not configured to log, or configured for facility any severity any, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-223197`

### Rule: The Juniper SRX Services Gateway must generate log records containing the full-text recording of privileged commands.

**Rule ID:** `SV-223197r513283_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if log records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. While the Juniper SRX inherently has the capability to generate log records, by default only the high facility levels are captured and only to local files. Ensure at least one Syslog server and local files are configured to support requirements. However, the Syslog itself must also be configured to filter event records so it is not overwhelmed. A best practice when configuring the external Syslog server is to add similar log-prefixes to the log file names to help and researching of central Syslog server. Another best practice is to add a match condition to limit the recorded events to those containing the regular expression (REGEX).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging has been enabled and configured. [edit] show system syslog If at least one valid syslog host server and the syslog file names are not configured to capture "any" facility and "any" event, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-223198`

### Rule: For local log files, the Juniper SRX Services Gateway must allocate log storage capacity in accordance with organization-defined log record storage requirements so that the log files do not grow to a size that causes operational issues.

**Rule ID:** `SV-223198r513286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The amount allocated for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, and how long the logs are kept on the device. Since the Syslog is the primary audit log, the local log is not essential to keep archived for lengthy periods, thus the allocated space on the device should be low.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the file size for the local system log is set. [edit] show system syslog View the archive size setting of the local log files. If all local log files are not set to an organizational-defined size, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-223199`

### Rule: The Juniper SRX Services Gateway must generate an immediate system alert message to the management console when a log processing failure is detected.

**Rule ID:** `SV-223199r513289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Without an immediate alert for critical system issues, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages at information technology speed (i.e., the time from event detection to alert occurs in seconds or less). Automated alerts can be conveyed in a variety of ways, including, for example, telephonically, via electronic mail, via text message, or via websites. Alerts must be sent immediately to the designated individuals (e.g., via Syslog configuration, SNMP trap, manned console message, or other events monitoring system). Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. While this requirement also applies to the configuration of the event monitoring system (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers), the Juniper SRX can also be configured to generate a message to the administrator console or send via email for immediate messages. Syslog and SNMP trap events with a facility of "daemon" pertaining to errors encountered by system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system Syslog has been configured to display an alert on the console for the emergency and critical levels of the daemon facility. [edit] show system syslog If the system is not configured to generate a system alert message when a component failure is detected, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-223201`

### Rule: The Juniper SRX Services Gateway must record time stamps for log records using Coordinated Universal Time (UTC).

**Rule ID:** `SV-223201r513292_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. UTC is normally used in DoD; however, Greenwich Mean Time (GMT) may be used if needed for mission requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the time zone is set to UTC. [edit] show system time-zone If the time zone is not set to UTC, this is a finding.

## Group: SRG-APP-000378-NDM-000302

**Group ID:** `V-223202`

### Rule: The Juniper SRX Services Gateway must implement logon roles to ensure only authorized roles are allowed to install software and updates.

**Rule ID:** `SV-223202r513295_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing anyone to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. This requirement applies to code changes and upgrades for all network devices. For example audit admins and the account of last resort are not allowed to perform this task.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify role-based access control has been configured, view the settings for each login class defined. [edit] show system login View all login classes to see which roles are assigned the "Maintenance" or "request system software add" permissions. If login classes for user roles that are not authorized to install and update software are configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-223203`

### Rule: If the loopback interface is used, the Juniper SRX Services Gateway must protect the loopback interface with firewall filters for known attacks that may exploit this interface.

**Rule ID:** `SV-223203r513298_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loopback interface is a logical interface and has no physical port. Since the interface and addresses ranges are well-known, this port must be filtered to protect the Juniper SRX from attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the loopback interface is not used, this is not applicable. Verify the loopback interface is protected by firewall filters. [edit] show interfaces lo0 If the loopback interface is not configured with IPv6 and IPv4 firewall filters, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-223204`

### Rule: The Juniper SRX Services Gateway must have the number of rollbacks set to 5 or more.

**Rule ID:** `SV-223204r513301_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Backup of the configuration files allows recovery in case of corruption, misconfiguration, or catastrophic failure. The maximum number of rollbacks for the SRX is 50 while the default is 5 which is recommended as a best practice. Increasing this backup configuration number will result in increased disk usage and increase the number of files to manage. Organizations should not set the value to zero.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view the current setting for maximum number of rollbacks enter the following command. [edit] show system max-configuration-rollbacks If the number of back up configurations is not set to an organization-defined value which is 5 or more, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-223205`

### Rule: The Juniper SRX Services Gateway must be configured to synchronize internal information system clocks with the primary and secondary NTP servers for the network.

**Rule ID:** `SV-223205r513304_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on log events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX is configured to synchronize internal information system clocks with the primary and secondary NTP sources. [edit] show system ntp If the Juniper SRX is not configured to synchronize internal information system clocks with an NTP server, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-223206`

### Rule: The Juniper SRX Services Gateway must be configured to use an authentication server to centrally manage authentication and logon settings for remote and nonlocal access.

**Rule ID:** `SV-223206r539624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is a particularly important protection against the insider threat. Audit records for administrator accounts access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device. The Juniper SRX supports three methods of user authentication: local password authentication, Remote Authentication Dial-In User Service (RADIUS), and Terminal Access Controller Access Control System Plus (TACACS+). RADIUS and TACACS+ are remote access methods used for management of the Juniper SRX. The local password method will be configured for use only for the account of last resort. To completely set up AAA authentication, create a user template account (the default name is remote) and specify a system authentication server and an authentication order. See CCI-000213 for more details. The remote user template is not a logon account. Once the AAA server option is configured, any remote or nonlocal access attempts are redirected to the AAA server. Since individual user accounts are not defined on the SRX, the authentication server must be used to manage individual account settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX is configured to support the use of AAA services to centrally manage user authentication and logon settings. From the CLI operational mode enter: show system radius-server or show system tacplus-server If the Juniper SRX has not been configured to support the use RADIUS and/or TACACS+ servers to centrally manage authentication and logon settings for remote and nonlocal access, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-223207`

### Rule: The Juniper SRX Services Gateway must use DoD-approved PKI rather than proprietary or self-signed device certificates.

**Rule ID:** `SV-223207r513310_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs. The SRX generates a key-pair and a CSR. The CSR is sent to the approved CA, who signs it and returns it as a certificate. That certificate is then installed. The process to obtain a device PKI certificate requires the generation of a Certificate Signing Request (CSR), submission of the CSR to a CA, approval of the request by an RA, and retrieval of the issued certificate from the CA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To validate that the certificate was loaded, type the following command: show security pki local-certificate View the installed device certificates. If any of the certificates have the name or identifier of a non-approved source in the Issuer field, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223208`

### Rule: The Juniper SRX Services Gateway must be configured to prohibit the use of unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-223208r513313_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. The control plane is responsible for operating most of the system services on the SRX. The control plane is responsible not only for acting as the interface for the administrator operating the device, but also for controlling the operation of the chassis, pushing the configuration to the data plane, and operating the daemons that provide functionality to the system. The control plane operates the Junos OS, which is a FreeBSD variant. The Juniper SRX control plane services include, but are not limited to, the following: Management Daemon (MGD), Routing Protocol Daemon (RPD) (e.g., RIP, OSPF, IS-IS, BGP, PIM, IPv6 counterparts), User interfaces (SSH, J-Web, NetConf), File system interfaces (SCP), Syslogd (DNS, DHCP, NTP, ICMP, ARP/ND, SNMP), Chassisd, JSRPD (HA clustering).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Entering the following commands from the configuration level of the hierarchy. [edit] show system services If functions, ports, protocols, and services identified on the PPSM CAL are not disabled, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223209`

### Rule: For nonlocal maintenance sessions, the Juniper SRX Services Gateway must remove or explicitly deny the use of nonsecure protocols.

**Rule ID:** `SV-223209r513316_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Tools used for nonlocal management and diagnostics with the Juniper SRX include SSH but may also include compatible enterprise maintenance and diagnostics servers. Regardless of the tool used, the Juniper SRX must permit only the use of protocols with the capability to be configured securely with integrity protections. Specifically, use SSH instead of Telnet, SCP instead of FTP, and SNMPv3 rather than other versions SNMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify nonsecure protocols are not enabled for management access by viewing the enabled system services. From the operational hierarchy: > show config | match "set system services" | display set From the configuration hierarchy: [edit] show snmp show system services telnet show system services ftp show system services ssh If nonsecure protocols and protocol versions such as Telnet, FTP, SNMPv1, SNMPv2c, or SSHv1 are enabled, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-223210`

### Rule: The Juniper SRX Services Gateway must authenticate NTP servers before establishing a network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-223210r513319_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk, such as remote connections. The Juniper SRX can only be configured to use MD5 authentication keys. This algorithm is not FIPS 140-2 validated; thus, a CAT 1 finding is allocated in CCI-000803. However, MD5 is preferred to no authentication at all. The trusted-key statement permits authenticating NTP servers. The Juniper SRX supports multiple keys, multiple NTP servers, and different keys for each server; add the “key <key number>” parameter to the server statement to associate a key with a specific server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX is configured to synchronize internal information system clocks with the primary and secondary NTP sources. [edit] show system ntp If the NTP configuration is not configured to use authentication, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223211`

### Rule: If SNMP is enabled, the Juniper SRX Services Gateway must use and securely configure SNMPv3.

**Rule ID:** `SV-223211r513322_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent non-secure protocol communications with the organization's local SNMPv3 services, the SNMP client on the Juniper SRX must be configured for proper identification and strong cryptographically-based protocol for authentication. SNMPv3 defines a user-based security model (USM), and a view-based access control model (VACM). SNMPv3 USM provides data integrity, data origin authentication, message replay protection, and protection against disclosure of the message payload. SNMPv3 VACM provides access control to determine whether a specific type of access (read or write) to the management information is allowed. The Junos operating system allows the use of SNMPv3 to monitor or query the device for management purposes. Junos does not allow SNMPv3, of any type, to be used to make configuration changes to the device. SNMPv3 is disabled by default and must be enabled for use. SNMPv3 is the DoD-preferred method for monitoring the device securely. If SNMPv3 is not being used, it must be disabled. The following commands will configure SNMPv3. The Junos operating system allows the use of FIPS approved protocols for both authentication (SHA1) and for privacy (AES128). These protocols should be used to ensure secure management connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SNMPv3 is enabled and configured. [edit] show snmp If an SNMP stanza does not exist, this is not a finding. If SNMPv3 is not configured to meet DoD requirements, this is a finding. If versions earlier than SNMPv3 are enabled, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223212`

### Rule: The Juniper SRX Services Gateway must ensure SSH is disabled for root user logon to prevent remote access using the root account.

**Rule ID:** `SV-223212r513325_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the identity of the root account is well-known for systems based upon Linux or UNIX and this account does not have a setting to limit access attempts, there is risk of a brute force attack on the password. Root access would give superuser access to an attacker. Preventing attackers from remotely accessing management functions using root account mitigates the risk that unauthorized individuals or processes may gain superuser access to information or privileges. A separate account should be used for access and then the administrator can sudo to root when necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the CLI to view this setting for disabled for SSH. [edit] show system services ssh root-login If SSH is not disabled for the root user, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223213`

### Rule: The Juniper SRX Services Gateway must ensure access to start a UNIX-level shell is restricted to only the root account.

**Rule ID:** `SV-223213r513328_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting the privilege to create a UNIX-level shell limits access to this powerful function. System administrators, regardless of their other permissions, will need to also know the root password for this access, thus limiting the possibility of malicious or accidental circumvention of security controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each login class is configured to deny access to the UNIX shell. [edit] show system login If each configured login class is not configured to deny access to the UNIX shell, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223214`

### Rule: The Juniper SRX Services Gateway must ensure TCP forwarding is disabled for SSH to prevent unauthorized access.

**Rule ID:** `SV-223214r513331_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use this configuration option to prevent a user from creating an SSH tunnel over a CLI session to the Juniper SRX via SSH. This type of tunnel could be used to forward TCP traffic, bypassing any firewall filters or ACLs, allowing unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the CLI to view this setting for disabled for SSH. [edit] show system services ssh If TCP forwarding is not disabled for the root user, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223215`

### Rule: The Juniper SRX Services Gateway must be configured with only one local user account to be used as the account of last resort.

**Rule ID:** `SV-223215r513334_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without centralized management, credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Local accounts are configured using the local password authentication method which does not meet the multifactor authentication criteria. The account of last resort is a group authenticator which does not provide nonrepudiation, thus must be used only rare cases where the device must be accessed using the local console and an individual authenticator is not possible, including when network access is not available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only a single local account has an authentication stanza and that the name is the account of last resort. [edit] show system login user <account of last resort> { uid 2001; class <appropriate class name>; authentication { <--- This stanza permits local login encrypted-password "$sha2$22895$aVBPaRVa$o6xIqNSYg9D7yt8pI47etAjZV9uuwHrhAFT6R021HNsy"; ## SECRET-DATA } } OR user <template account> { uid 2001; class <appropriate class name>; } If accounts other than the account of last resort contain an authentication stanza, and that account is not documented, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-223216`

### Rule: The Juniper SRX Services Gateway must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-223216r513337_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. There are 2 approved methods for accessing the Juniper SRX which are, in order of preference, the SSH protocol and the console port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSH is configured to use a replay-resistant authentication mechanism. [edit] show system services ssh If SSH is not configured to use the MAC authentication protocol, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-223217`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce a minimum 15-character password length.

**Rule ID:** `SV-223217r513340_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Compliance with this requirement also prevents the system from being configured with default or no passwords.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SRX password enforces this complexity requirement. In configuration mode, enter the following command. [edit] show system login password If the minimum password length for local accounts is not set to at least a 15-character length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-223218`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce password complexity by setting the password change type to character sets.

**Rule ID:** `SV-223218r513343_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. The password change-type command specifies whether a minimum number of character-sets or a minimum number of character-set transitions are enforced. The DoD requires this setting be set to character-sets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces password complexity by setting the password change type to character sets [edit] show system login password If the password change-type is not set to character-sets, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-223219`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce password complexity by requiring at least one upper-case character be used.

**Rule ID:** `SV-223219r513346_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces password complexity by requiring at least one upper-case character be used. [edit] show system login password If the minimum-upper-cases is not set to at least 1, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-223220`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce password complexity by requiring at least one lower-case character be used.

**Rule ID:** `SV-223220r513349_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces password complexity by requiring at least one lower-case character be used. [edit] show system login password If the minimum-lower-cases is not set to at least 1, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-223221`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce password complexity by requiring at least one numeric character be used.

**Rule ID:** `SV-223221r513352_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces password complexity by requiring at least one numeric character be used. [edit] show system login password If the minimum numerics are not set to at least 1, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-223222`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort), the Juniper SRX Services Gateway must enforce password complexity by requiring at least one special character be used.

**Rule ID:** `SV-223222r513355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces password complexity by requiring at least one special character be used. [edit] show system login password If the minimum-punctuation is not set to at least 1, this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-223223`

### Rule: For local accounts using password authentication (i.e., the root account and the account of last resort) the Juniper SRX Services Gateway must use the SHA1 or later protocol for password authentication.

**Rule ID:** `SV-223223r513358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. The password format command is an optional command that specifies the hash algorithm used for authenticating passwords. The options are MD5, SHA1, or DES. SHA1 is recommended because it is a FIPS-approved algorithm and provides stronger security.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default local password enforces this requirement by entering the following in configuration mode. [edit] show system login password If the password format is not set to SHA-1, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-223224`

### Rule: For nonlocal maintenance sessions using SNMP, the Juniper SRX Services Gateway must use and securely configure SNMPv3 with SHA to protect the integrity of maintenance and diagnostic communications.

**Rule ID:** `SV-223224r513361_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. The Juniper SRX allows the use of SNMP to monitor or query the device in support of diagnostics information. SNMP cannot be used to make configuration changes; however, it is a valuable diagnostic tool. SNMP is disabled by default and must be enabled for use. SNMPv3 is the DoD-required version, but must be configured to be used securely.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SNMP is configured for version 3. [edit] show snmp v3 If SNMPv3 is not configured for version 3 using SHA, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-223225`

### Rule: For nonlocal maintenance sessions using SSH, the Juniper SRX Services Gateway must securely configure SSHv2 Message Authentication Code (MAC) algorithms to protect the integrity of maintenance and diagnostic communications.

**Rule ID:** `SV-223225r513364_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the integrity of nonlocal maintenance sessions, SSHv2 with MAC algorithms for integrity checking must be configured. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. The SSHv2 protocol suite includes Layer 7 protocols such as SCP and SFTP which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSHv2 and MAC algorithms for integrity checking. [edit] show system services ssh If SSHv2 and integrity options are not configured in compliance with DoD requirements, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-223226`

### Rule: For nonlocal maintenance sessions using SNMP, the Juniper SRX Services Gateway must securely configure SNMPv3 with privacy options to protect the confidentiality of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-223226r513367_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. To protect the confidentiality of nonlocal maintenance sessions, SNMPv3 with AES encryption to must be configured to provide confidentiality. The Juniper SRX allows the use of SNMPv3 to monitor or query the device in support of diagnostics information. SNMP cannot be used to make configuration changes; however, it is a valuable diagnostic tool. SNMP is disabled by default and must be enabled for use. SNMPv3 is the DoD-required version, but must be configured to be used securely.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SNMPv3 is configured with privacy options. [edit] show snmp v3 If SNMPv3, AES encryption, and other privacy options are not configured, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-223227`

### Rule: For nonlocal maintenance sessions using SSH, the Juniper SRX Services Gateway must securely configured SSHv2 with privacy options to protect the confidentiality of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-223227r513370_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To protect the confidentiality of nonlocal maintenance sessions when using SSH communications, SSHv2, AES ciphers, and key-exchange commands are configured. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. The SSHv2 protocol suite includes Layer 7 protocols such as SCP and SFTP which can be used for secure file transfers. The key-exchange commands limit the key exchanges to FIPS and DoD-approved methods.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSHv2, AES ciphers, and key-exchange commands are configured to protect confidentiality. [edit] show system services ssh If SSHv2, AES ciphers, and key-exchange commands are not configured to protect confidentiality, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-223228`

### Rule: For nonlocal maintenance sessions, the Juniper SRX Services Gateway must ensure only zones where management functionality is desired have host-inbound-traffic system-services configured.

**Rule ID:** `SV-223228r513373_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Add a firewall filter to protect the management interface. Note: The dedicated management interface (if present), and an interface placed in the functional zone management, will not participate in routing network traffic. It will only support device management traffic. The host-inbound-traffic feature of the SRX is an additional layer of security for system services. This function can be configured on either a per zone or a per interface basis within each individual security zone. By default, a security zone has all system services disabled, which means that it will not accept any inbound management or protocol requests on the control plane without explicitly enabling the service at either the interface or zone in the security zone stanzas.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only those zones where management functionality is allowed have host-inbound-traffic system-services configured and that protocols such as HTTP and HTTPS are not assigned to these zones. [edit] show security zones functional-zone management If zones configured for host-inbound-traffic system-services have protocols other than SSH configured, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-223229`

### Rule: The Juniper SRX Services Gateway must immediately terminate SSH network connections when the user logs off, the session abnormally terminates, or an upstream link from the managed device goes down.

**Rule ID:** `SV-223229r513376_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting frees device resources and mitigates the risk of an unauthorized user gaining access to an open idle session. When sessions are terminated by a normal administrator log off, the Juniper SRX makes the current contents unreadable and no user activity can take place in the session. However, abnormal terminations or loss of communications do not signal a session termination, thus a keep-alive count and interval must be configured so the device will know when communication with the client is no longer available. The keep-alive value and the interval between keep-alive messages must be set to an organization-defined value based on mission requirements and network performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
[edit] show system services ssh If the keep-alive count and keep-alive interval are not set to an organization-defined value, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-223230`

### Rule: The Juniper SRX Services Gateway must terminate the console session when the serial cable connected to the console port is unplugged.

**Rule ID:** `SV-223230r513379_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a device management session or connection remains open after management is completed, it may be hijacked by an attacker and used to compromise or damage the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify this setting by entering the following commands in configuration mode. [edit] show system ports console If the log-out-on-disconnect is not set for the console port, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-223231`

### Rule: The Juniper SRX Services Gateway must terminate a device management session after 10 minutes of inactivity, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-223231r539622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session. Quickly terminating an idle session also frees up resources. This requirement does not mean that the device terminates all sessions or network access; it only ends the inactive session. User accounts, including the account of last resort must be assigned to a login class. Configure all login classes with an idle timeout value. Pre-defined classes do not support configurations, therefore should not be used for DoD implementations. The root account cannot be assigned to a login-class which is why it is critical that this account be secured in accordance with DoD policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify idle-timeout is set for 10 minutes. [edit] show system login If a timeout value of 10 or less is not set for each class, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-223232`

### Rule: The Juniper SRX Services Gateway must terminate a device management session if the keep-alive count is exceeded.

**Rule ID:** `SV-223232r539622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the keep-alive for management protocols mitigates the risk of an open connection being hijacked by an attacker. The keep-alive messages and the interval between each message are used to force the system to disconnect a user that has lost network connectivity to the device. This differs from inactivity timeouts because the device does not wait the 10 minutes to log the user out but, instead, immediately logs the user out if the number of keep-alive messages are exceeded. The interval between messages should also be configured. These values should be set to an organization-defined value based on mission requirements and network performance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify this setting by entering the following commands in configuration mode. [edit] show system services ssh If the keep-alive count and keep-alive interval is not set to an organization-defined value, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-223233`

### Rule: The Juniper SRX Services Gateway must configure the control plane to protect against or limit the effects of common types of Denial of Service (DoS) attacks on the device itself by configuring applicable system options and internet-options.

**Rule ID:** `SV-223233r513388_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Juniper SRX uses the system commands, system internet-options, and screens to mitigate the impact of DoS attacks on device availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system options are configured to protect against DoS attacks. [edit] show system show system internet-options If the system and system-options which limit the effects of common types of DoS attacks are not configured in compliance with DoD requirements, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-223234`

### Rule: The Juniper SRX Services Gateway must limit the number of sessions per minute to an organization-defined number for SSH to protect remote access management from unauthorized access.

**Rule ID:** `SV-223234r513391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The rate-limit command limits the number of SSH session attempts allowed per minute which helps limit an attacker's ability to perform DoS attacks. The rate limit should be as restrictive as operationally practical. Juniper Networks recommends a best practice of 4 for the rate limit, however the limit should be as restrictive as operationally practical. User connections that exceed the rate-limit will be closed immediately after the connection is initiated. They will not be in a waiting state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX sets a connection-limit for the SSH protocol. Show system services ssh If the SSH connection-limit is not set to 4 or an organization-defined value, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-223235`

### Rule: The Juniper SRX Services Gateway must implement service redundancy to protect against or limit the effects of common types of Denial of Service (DoS) attacks on the device itself.

**Rule ID:** `SV-223235r513394_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Service redundancy, may reduce the susceptibility to some DoS attacks. Organizations must consider the need for service redundancy in accordance with DoD policy. If service redundancy is required then this technical control is applicable. The Juniper SRX can configure your system to monitor the health of the interfaces belonging to a redundancy group.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If service redundancy is not required by the organization's policy, this is not a finding. Verify the configuration is working properly: [edit] show chassis cluster interfaces command. If service redundancy is not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-223236`

### Rule: The Juniper SRX Services Gateway must be configured to use Junos 12.1 X46 or later to meet the minimum required version for DoD.

**Rule ID:** `SV-223236r513397_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Earlier versions of Junos may have reached the end of life cycle support by the vendor. Junos 12.1X46 is not a UC APL certified version, while 12.1X46 is UC APL Certified. The SRX with Junos 12.1X46 has been NIAP certified as a firewall and VPN. Junos 12.1X46 contains a number of enhancements, particularly related to IPv6, that are relevant to the STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the version installed is Junos 12.1 X46 or later. In operational mode, type the following: show version If the Junos version installed is not 12.1 X46 or later, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-223237`

### Rule: For nonlocal maintenance sessions, the Juniper SRX Services Gateway must explicitly deny the use of J-Web.

**Rule ID:** `SV-223237r513400_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If unsecured functions (lacking FIPS-validated cryptographic mechanisms) are used for management sessions, the contents of those sessions are susceptible to manipulation, potentially allowing alteration and hijacking. J-Web (configured using the system services web-management option) does not meet the DoD requirement for management tools. It also does not work with all Juniper SRX hardware. By default, the web interface is disabled; however, it is easily enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify web-management is not enabled. [edit] show system services web-management If a stanza exists that configures web-management service options, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229014`

### Rule: The Juniper SRX Services Gateway must automatically terminate a network administrator session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-229014r518220_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of administrator-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. These conditions will vary across environments and network device types. The Juniper SRX can be configured to limit login times or to logout users after a certain time period if desired by the organization. These setting are configured as options on the login class to which they apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the organization does not have a requirement for triggered, automated logout, this is not a finding. Obtain a list of organization-defined triggered, automated requirements that are required for the Juniper SRX. To verify configuration of special user access controls. [edit] show system login View time-based or other triggers which are configured to control automated logout. If the organization has documented requirements for triggered, automated termination and they are not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229015`

### Rule: For local accounts, the Juniper SRX Services Gateway must generate an alert message to the management console and generate a log event record that can be forwarded to the ISSO and designated system administrators when local accounts are created.

**Rule ID:** `SV-229015r518223_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authorized insider or individual who maliciously creates a local account could gain immediate access from a remote location to privileged information on a critical security device. Sending an alert to the administrators and ISSO when this action occurs greatly reduces the risk that accounts will be surreptitiously created. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Although, based on policy, administrator accounts must be created on the AAA server, thus this requirement addresses the creation of unauthorized accounts on the Juniper SRX itself. This does not negate the need to address this requirement on the AAA server and the event monitoring server (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system is not configured to display account creation actions on the management console and generate an event log message to the Syslog server and a local file, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229016`

### Rule: The Juniper SRX Services Gateway must generate an alert message to the management console and generate a log event record that can be forwarded to the ISSO and designated system administrators when the local accounts (i.e., the account of last resort or root account) are modified.

**Rule ID:** `SV-229016r518226_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authorized insider or individual who maliciously modifies a local account could gain immediate access from a remote location to privileged information on a critical security device. Sending an alert to the administrators and ISSO when this action occurs greatly reduces the risk that accounts will be surreptitiously modified. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Although, based on policy, administrator accounts must be modified on the AAA server, thus this requirement addresses the modification of unauthorized accounts on the Juniper SRX itself. This does not negate the need to address this requirement on the AAA server and the event monitoring server (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system does not display account modification actions on the management console and generate an event log message to the Syslog server and a local file, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229017`

### Rule: The Juniper SRX Services Gateway must generate an alert message to the management console and generate a log event record that can be forwarded to the ISSO and designated system administrators when accounts are disabled.

**Rule ID:** `SV-229017r518229_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authorized insider or individual who maliciously disables a local account could gain immediate access from a remote location to privileged information on a critical security device. Sending an alert to the administrators and ISSO when this action occurs greatly reduces the risk that accounts will be surreptitiously disabled. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Although, based on policy, administrator accounts must be disabled on the AAA server, this requirement addresses the disabling of unauthorized accounts on the Juniper SRX itself. This does not negate the need to address this requirement on the AAA server and the event monitoring server (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system does not display account disabling actions on the management console and generate an event log message to the Syslog server and a local file, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229018`

### Rule: The Juniper SRX Services Gateway must generate alerts to the management console and generate a log record that can be forwarded to the ISSO and designated system administrators when the local accounts (i.e., the account of last resort or root account) are deleted.

**Rule ID:** `SV-229018r518232_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An authorized insider or individual who maliciously delete a local account could gain immediate access from a remote location to privileged information on a critical security device. Sending an alert to the administrators and ISSO when this action occurs greatly reduces the risk that accounts will be surreptitiously deleted. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Although, based on policy, administrator accounts must be deleted on the AAA server, this requirement addresses the deletion of unauthorized accounts on the Juniper SRX itself. This does not negate the need to address this requirement on the AAA server and the event monitoring server (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers). Accounts can be disabled by configuring the account with the built-in login class "unauthorized". When the command is reissued with a different login class, the account is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system is not configured to display account deletion actions on the management console and generate an event log message to the Syslog server and a local file, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229019`

### Rule: The Juniper SRX Services Gateway must generate an immediate alert message to the management console for account enabling actions.

**Rule ID:** `SV-229019r518235_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. Alerts must be sent immediately to the designated individuals (e.g., via Syslog configuration, SNMP trap, manned console message, or other events monitoring system). Accounts can be disabled by configuring the account with the built-in login class "unauthorized". When the command is reissued with a different login class, the account is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the device is configured to display change-log events of severity info. [edit] show system syslog If the system is not configured to display account enabling actions on the management console, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229021`

### Rule: The Juniper SRX Services Gateway must allow only the ISSM (or administrators/roles appointed by the ISSM) to select which auditable events are to be generated and forwarded to the syslog and/or local logs.

**Rule ID:** `SV-229021r518241_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. The primary audit log permissions are set on the Syslog server, not the Juniper SRX. However, it is a best practice to also keep local logs for troubleshooting and backup. These logs are subject to access control requirements. This configuration is a two-step process. Part of the configuration must be performed on the AAA server. After a user successfully logs on, the AAA sever passes the template or role of the user to the Juniper SRX. Each AAA template or role is mapped to a login class on the Juniper SRX. On the Juniper SRX, the class name, audit-admin, is recommended as a best practice because it follows the naming convention used in NIAP testing and is self-documenting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only the ISSM (or administrators or roles appointed by the ISSM) have permission to configure and control audit events. [edit] show system login class show system login View permissions for the audit-admin class (audit-admin is an example class name; local policy may dictate another name). View class assignment for all users and template users configured on the Juniper SRX. If user templates or users are other than the ISSM (or administrators or roles appointed by the ISSM) have permission to select which auditable events are to be audited, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229022`

### Rule: For local logging, the Juniper SRX Services Gateway must generate a message to the system management console when a log processing failure occurs.

**Rule ID:** `SV-229022r518244_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Without this alert, the security personnel may be unaware of an impending failure of the log capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages at information technology speed (i.e., the time from event detection to alert occurs in seconds or less). Automated alerts can be conveyed in a variety of ways, including, for example, telephonically, via electronic mail, via text message, or via websites. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. While this requirement also applies to the event monitoring system (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers), the Juniper SRX must also be configured to generate a message to the administrator console. Syslog and SNMP trap events with a facility of "daemon" pertain to errors encountered by system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system Syslog has been configured to display an alert on the console for the emergency and alert levels of the daemon facility. [edit] show system syslog If the system is not configured to generate a message to the system management console when a log processing failure occurs, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229023`

### Rule: In the event that communications with the events server is lost, the Juniper SRX Services Gateway must continue to queue log records locally.

**Rule ID:** `SV-229023r518247_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network device is at risk of failing to process logs as required, it take action to mitigate the failure. Log processing failures include: software/hardware errors; failures in the log capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to log failure depend upon the nature of the failure mode. Since availability is an overriding concern given the role of the Juniper SRX in the enterprise, the system must not be configured to shut down in the event of a log processing failure. The system will be configured to log events to local files, which will provide a log backup. If communication with the Syslog server is lost or the server fails, the network device must continue to queue log records locally. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local log data with the collection server. A best practice is to add log-prefixes to the log file names to help in researching the events and filters to prevent log overload. Another best practice is to add a match condition to limit the recorded events to those containing the regular expression (REGEX). Thus, the Juniper SRX will inherently and continuously capture events to local files to guard against the loss of connectivity to the primary and secondary events server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging has been enabled and configured to capture to local log files in case connection with the primary and secondary log servers is lost. [edit] show system syslog If local log files are not configured to capture events, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229024`

### Rule: The Juniper SRX Services Gateway must be configured to use an authentication server to centrally apply authentication and logon settings for remote and nonlocal access for device management.

**Rule ID:** `SV-229024r518250_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized application (e.g., TACACS+, RADIUS) of authentication settings increases the security of remote and nonlocal access methods. This control is a particularly important protection against the insider threat. Audit records for administrator accounts access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device. This requirement references identification and authentication and does not prevent the configuration of privileges using the remote template account (CCI-000213).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX is configured to support the use of AAA services to centrally apply user authentication and logon settings. From the CLI operational mode enter: show system radius-server or show system tacplus-server If the Juniper SRX has not been configured to support the use of RADIUS and/or TACACS+ servers to centrally apply authentication and logon settings for remote and nonlocal access, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229025`

### Rule: The Juniper SRX Services Gateway must be configured to use a centralized authentication server to authenticate privileged users for remote and nonlocal access for device management.

**Rule ID:** `SV-229025r518253_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is a particularly important protection against the insider threat. Audit records for administrator accounts access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device. The Juniper SRX supports three methods of user authentication: local password authentication, Remote Authentication Dial-In User Service (RADIUS), and Terminal Access Controller Access Control System Plus (TACACS+). RADIUS and TACACS+ are remote access methods used for management of the Juniper SRX. The local password method will be configured for use only for the account of last resort; however, it will not be used for remote and nonlocal access or this will result in a CAT 1 finding (CCI-000765). This requirement references identification and authentication and does not prevent the configuration of privileges using the remote template account (CCI-000213).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Juniper SRX is configured to forward logon requests to a RADIUS or TACACS+. From the CLI operational mode enter: show system radius-server or show system tacplus-server If the Juniper SRX is not configured to use at least one RADIUS or TACACS+ server, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229026`

### Rule: The Juniper SRX Services Gateway must specify the order in which authentication servers are used.

**Rule ID:** `SV-229026r518256_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Specifying an authentication order implements an authentication, authorization, and accounting methods list to be used, thus allowing the implementation of redundant or backup AAA servers. These commands also ensure that a default method or order will not be used by the device (e.g., local passwords). The Juniper SRX must specify the order in which authentication is attempted by including the authentication-order statement in the authentication server configuration. Remote logon using password results in a CAT 1 finding (CCI-000765) for failure to use two-factor authentication. Thus, if the account of last resort uses only password authentication, this configuration prevents remote access. DoD policy is that redundant AAA servers are required to mitigate the risk of a failure of the primary AAA device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a RADIUS or TACACS+ server order has been configured. From operational mode enter the command: show system authentication-order If the authentication-order for either or both RADIUS or TACACS+ server order has not been configured, this is a finding. If the authentication-order includes the password method, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229027`

### Rule: The Juniper SRX Services Gateway must detect the addition of components and issue a priority 1 alert to the ISSM and SA, at a minimum.

**Rule ID:** `SV-229027r518259_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The network device must automatically detect the installation of unauthorized software or hardware onto the device itself. Monitoring may be accomplished on an ongoing basis or by periodic monitoring. Automated mechanisms can be implemented within the network device and/or in another separate information system or device. If the addition of unauthorized components or devices is not automatically detected, then such components or devices could be used for malicious purposes, such as transferring sensitive data to removable media for compromise. Alerts must be sent immediately to the designated individuals (e.g., via Syslog configuration, SNMP trap, manned console message, or other events monitoring system).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SNMP is configured to capture chassis and device traps. If Syslog or a console method is used, verify that method instead. [edit] show snmp v3 If an immediate alert is not sent via SNMPv3 or another method, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229028`

### Rule: The Juniper SRX Services Gateway must generate an alarm or send an alert message to the management console when a component failure is detected.

**Rule ID:** `SV-229028r518262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Component (e.g., chassis, file storage, file corruption) failure may cause the system to become unavailable, which could result in mission failure since the network would be operating without a critical security traffic inspection or access function. Alerts provide organizations with urgent messages. Real-time alerts provide these messages at information technology speed (i.e., the time from event detection to alert occurs in seconds or less). Automated alerts can be conveyed in a variety of ways, including, for example, telephonically, via electronic mail, via text message, or via websites. While this requirement also applies to the event monitoring system (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers), the Juniper SRX must also be configured to generate a message to the administrator console. Syslog and SNMP trap events with a facility of "daemon" pertain to errors encountered by system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the system Syslog has been configured to display an alert on the console for the emergency and critical levels of the daemon facility. [edit] show system syslog If the system is not configured to generate a system alert message when a component failure is detected, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-229029`

### Rule: The Juniper SRX Services Gateway must reveal log messages or management console alerts only to the ISSO, ISSM, and SA roles).

**Rule ID:** `SV-229029r518265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state. Additionally, sensitive account information must not be revealed through error messages to unauthorized personnel or their designated representatives. Although, based on policy, administrator accounts must be created on the AAA server, thus this requirement addresses the creation of unauthorized accounts on the Juniper SRX itself. This does not negate the need to address this requirement on the AAA server and the event monitoring server (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain a list of authorized user names that are authorized to view the audit log and console notification messages. Verify classes are created that separate administrator roles based on authorization. View user classes and class members by typing the following commands. [edit] show system login View class assignment for all users and template users configured on the Juniper SRX. Users with login classes audit-admin, security-admin, and system-admin have permission to view error message in logs and/or notifications. If classes or users that are not authorized to have access to the logs (e.g., crypto-admin) have permissions to view or access error message in logs and/or notifications, this is a finding.

