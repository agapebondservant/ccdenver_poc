# STIG Benchmark: Juniper Router NDM Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-217305`

### Rule: The Juniper router must be configured to limit the number of concurrent management sessions to an organization-defined number.

**Rule ID:** `SV-217305r1050884_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is not applicable to file transfer actions such as SCP and SFTP. Review the router configuration to determine if concurrent SSH sessions are limited as shown in the example below: system { services { ssh { max-sessions-per-connection 3; connection-limit 3; } } If the router is not configured to limit the number of concurrent sessions, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-217306`

### Rule: The Juniper router must be configured to automatically audit account creation.

**Rule ID:** `SV-217306r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it audits account creation. This requirement can be met by ensuring that configuration changes are logged as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If account creation is not audited, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-217307`

### Rule: The Juniper router must be configured to automatically audit account modification.

**Rule ID:** `SV-217307r960780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification along with an automatic notification to appropriate individuals will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it audits account modification. This requirement can be met by ensuring that configuration changes are logged as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If account modification is not audited, this is a finding.

## Group: SRG-APP-000028-NDM-000210

**Group ID:** `V-217308`

### Rule: The Juniper router must be configured to automatically audit account disabling actions.

**Rule ID:** `SV-217308r960783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account disabling actions will support account management procedures. When device management accounts are disabled, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it audits the disabling of accounts. This requirement can be met by ensuring that configuration changes are logged as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If the disabling of accounts is not audited, this is a finding. Note: Accounts can be disabled by changing the assigned class to unauthorized (no permissions).

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-217309`

### Rule: The Juniper router must be configured to automatically audit account removal actions.

**Rule ID:** `SV-217309r960786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it audits the deletion of accounts. This requirement can be met by ensuring that configuration changes are logged as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If the deletion of accounts is not audited, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-217310`

### Rule: The Juniper router must be configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies.

**Rule ID:** `SV-217310r991980_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. Step 1: Verify that an input filter has been configured for the loopback interfaces as shown in the example below. interfaces { … … … } lo0 { unit 0 { family inet { filter { input RESTRICT_MGMT_ACCESS; } address 2.2.2.2/32; } } } } Step 2: Verify that the filter restricts management traffic. The configuration example below restricts management access to specific IP addresses via SSH. filter RESTRICT_MGMT_ACCESS { term ALLOW_SSH { from { source-address { x.x.x.x/24; } protocol tcp; port ssh; } then accept; } term DENY_SSH { from { protocol tcp; port ssh; } then { log; discard; } } } Note: Management and control plane traffic destined to the router is punted to the routing engine. Hence, applying the filter to the loopback ensures that this traffic can be monitored regardless of the ingress physical interface. If the Juniper router is not configured to enforce approved authorizations for controlling the flow of management information within the device based on control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-217311`

### Rule: The Juniper router must be configured to enforce the limit of three consecutive invalid logon attempts after which time lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-217311r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it enforces the limit of three consecutive invalid logon attempts after which time it will lockout the user account from accessing the router for 15 minutes as shown in the example below. login { retry-options { tries-before-disconnect 3; lockout-period 15; } If the router is not configured to enforce the limit of three consecutive invalid logon attempts after which time it will lockout the user account from accessing the router for 15 minutes, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-217312`

### Rule: The Juniper router must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-217312r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below: System { } login { message "You are accessing a U.S. Government (USG) Information System (IS) that is provided\nfor USG-authorized use only.\n\nBy using this IS (which includes any device attached to this IS), you consent to the\nfollowing conditions:\n\n-The USG routinely intercepts and monitors communications on this IS for purposes\nincluding, but not limited to, penetration testing, COMSEC monitoring, network\noperations and defense, personnel misconduct (PM), law enforcement (LE), and\ncounterintelligence (CI) investigations.\n\n-At any time, the USG may inspect and seize data stored on this IS.\n\n-Communications using, or data stored on, this IS are not private, are subject to routine\nmonitoring, interception, and search, and may be disclosed or used for any USG-\nauthorized purpose.\n\n-This IS includes security measures (e.g., authentication and access controls) to protect\nUSG interests--not for your personal benefit or privacy.\n\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI\ninvestigative searching or monitoring of the content of privileged communications, or\nwork product, related to personal representation or services by attorneys,\npsychotherapists, or clergy, and their assistants. Such communications and work product\nare private and confidential. See User Agreement for details."; } If the router is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-217313`

### Rule: The Juniper router must be configured to protect against an individual falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-217313r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it logs configuration changes as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If configuration change activity is not logged, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-217315`

### Rule: The Juniper router must be configured to generate audit records when successful/unsuccessful attempts to logon with access privileges occur.

**Rule ID:** `SV-217315r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below will log all logon attempts. syslog { file LOG_FILE { authorization info; } } Note: The parameter "any" can be in place of "authorization" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } } } If the router is not configured to generate audit records when successful/unsuccessful attempts to logon, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-217316`

### Rule: The Juniper router must be configured to generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-217316r960909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below will log all configuration changes. syslog { file LOG_FILE { change-log info; } } Note: The parameter "any" can be in place of "change-log" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } } } If the router is not configured to generate audit records of configuration changes, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-217317`

### Rule: The Juniper router must be configured to protect audit information from unauthorized modification.

**Rule ID:** `SV-217317r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below allows only users belonging to the AUDITOR class to configure the logging parameters. system { login { class AUDITOR { permissions [configure view-configuration]; allow-configuration "(system syslog)"; } class SR_ENGINEER { permissions all; deny-configuration "(system syslog)"; } } } If the router is not configured to protect audit information from unauthorized modification, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-217318`

### Rule: The Juniper router must be configured to protect audit information from unauthorized deletion.

**Rule ID:** `SV-217318r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below depicts a class "JR_ENGINEER" which does not permit users belonging to the class to delete files or make changes to logging parameters. login { class JR_ENGINEER { permissions all; deny-commands "(file delete)"; deny-configuration "(system syslog)"; } } Note: The predefined classes "Operator" and "Read-only" do not have permissions to delete files. If the router is not configured to protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-217319`

### Rule: The Juniper router must be configured to limit privileges to change the software resident within software libraries.

**Rule ID:** `SV-217319r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. If the network device were to enable non-authorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below depicts a class JR_ENGINEER that is not permitted to add, change, or delete software installed on the router. login { class JR_ENGINEER { permissions all; deny-commands "request system software"; } Note: The following are the options under request system software: abort - Abort software upgrade add - Add extension or upgrade package delete - Remove extension or upgrade package rollback - Roll back to previous set of packages validate - Verify package compatibility with current configuration If the router is not configured to limit privileges to change the software resident within software libraries, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-217320`

### Rule: The Juniper router must be configured to prohibit the use of all unnecessary and nonsecure functions and services.

**Rule ID:** `SV-217320r1050856_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the services that have been enabled as shown in the following configuration example: services { finger; telnet; xnm-clear-text; netconf { ssh; } } Services such as finger, telnet, and clear text-based JUNOScript connections should never be enabled. Other services such as Netconf, FTP, DHCP, and SSL-based JUNOScript connections should only be enabled if operationally required. If the router is not configured to prohibit the use of all unnecessary and non-secure functions and services, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-217321`

### Rule: The Juniper router must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-217321r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that a local account for last resort has been configured as shown in the following example: system { authentication-order radius; } login { class ENGINEER { permissions all; deny-commands "(file delete)"; deny-configuration "(system syslog)"; } user Last_Resort { uid 2000; class ENGINEER; authentication { encrypted-password "$1$CYrhql/I$v2ydLnac9EPdA1F/KvROT1"; ## SECRET-DATA } } Note: If there is no response from the authentication server, JUNOS will authenticate using a local account as last resort. It is recommended to not configure password at the end of the authentication order, as JUNOS will attempt to authenticate using a local account upon a rejection from the authentication server if password is in the authentication order. The last resort account is used when the authentication server is down. If the router is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-217322`

### Rule: The Juniper router must be configured to implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-217322r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that SSH is configured to use FIPS-140-2 compliant HMACs as shown in the example below. system { … … … services { ssh { protocol-version v2; macs [hmac-sha2-256 hmac-sha2-512]; } Note: An SSH configuration enables a server and client to authorize the negotiation of only those algorithms that are configured from the allowed list. If a remote party tries to negotiate using an algorithm that is not part of the allowed list, the request is rejected and the session is not established. If the router is not configured to implement replay-resistant authentication mechanisms for network access to privileged accounts, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-217323`

### Rule: The Juniper router must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-217323r1015742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … login { password { minimum-length 15; } } If the router is not configured to enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-217324`

### Rule: The Juniper router must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-217324r1015743_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … login { password { minimum-upper-cases 1; } } If the router is not configured to enforce password complexity by requiring that at least one uppercase character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-217325`

### Rule: The Juniper router must be configured to enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-217325r1015744_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … login { password { minimum-lower-cases 1; } } If the router is not configured to enforce password complexity by requiring that at least one lowercase character be used, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-217326`

### Rule: The Juniper router must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-217326r1015745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … login { password { minimum-numerics 1; } } If the router is not configured to enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-217327`

### Rule: The Juniper router must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-217327r1015746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … login { password { minimum-punctuations 1; } } If the router is not configured to enforce password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-217328`

### Rule: The Juniper router must be configured to terminate all network connections associated with device management after five minutes of inactivity.

**Rule ID:** `SV-217328r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that all login classes have the idle-timeout value to five minutes or less as shown in the following example: system { … … … } login { class ADMIN { idle-timeout 5; permissions admin-control; } } If the router is not configured to terminate all network connections associated with a device management after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-217329`

### Rule: The Juniper router must be configured to automatically audit account enabling actions.

**Rule ID:** `SV-217329r961290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it audits the enabling of accounts. This requirement can be met by ensuring that configuration changes are logged as shown in the following example: system { syslog { file LOG_FILE { change-log info; } } } Note: The parameter “any” can be in place of “change-log” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } file LOG_FILE { change-log info; } console { any error; } } } If the enabling of accounts is not audited, this is a finding. Note: Accounts can be disabled by changing the assigned class to unauthorized (no permissions). Hence, accounts can be enabled by changing the assigned class for the user to a class other than unauthorized.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-217330`

### Rule: The Juniper router must be configured to audit the execution of privileged functions.

**Rule ID:** `SV-217330r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below will log all commands entered from the command line interface as well as log all configuration changes. syslog { file LOG_FILE { interactive-commands; change-log info } } Note: The parameter "any" can be in place of configuring specific events as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host 10.1.58.2 { any info; } } If the router is not configured to log all commands entered from the command line interface as well as log all configuration changes, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-217332`

### Rule: The Juniper router must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-217332r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below specifies 12 archive log files and the maximum size of the active log file to be reached prior to archiving. syslog { file LOG_FILE { any info; archive size 1000000 files 12; } } Note: To prevent log files from growing too large, by default the Junos logging utility writes messages to a sequence of files of a defined size. The files in the sequence are referred to as archive files to distinguish them from the active file to which messages are currently being written. The default maximum size depends on the platform type. By default, the logging utility creates up to 10 archive files in this manner. When the maximum number of archive files is reached and when the size of the active file reaches the configured maximum size, the contents of the last archived file are overwritten by the current active file. If the router is not configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-217333`

### Rule: The Juniper router must be configured to generate an alert for all audit failure events.

**Rule ID:** `SV-217333r991991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { syslog { host x.x.x.x { any critical; } } Note: The parameter "critical" can be replaced with a lesser severity level (i.e., error, warning, notice, info). If the router is not configured to generate an alert for all audit failure events, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-217334`

### Rule: The Juniper router must be configured to synchronize its clock with the primary and secondary time sources using redundant authoritative time sources.

**Rule ID:** `SV-217334r1015747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the configuration example below. system { … … … } ntp { server x.x.x.x prefer; server x.x.x.x; } If the router is not configured to synchronize its clock with redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-217335`

### Rule: The Juniper router must be configured to record time stamps for log records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-217335r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { time-zone UTC; Note: UTC is the default; hence, the command set time-zone may not be seen in the configuration. This can be verified using the show system uptime command. If the router is not configured record time stamps for log records that can be mapped to UTC or GMT, this is a finding.

## Group: SRG-APP-000378-NDM-000302

**Group ID:** `V-217336`

### Rule: The Juniper router must be configured to prohibit installation of software without explicit privileged status.

**Rule ID:** `SV-217336r1015748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing anyone to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. This requirement applies to code changes and upgrades for all network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration example below depicts a class JR_ENGINEER that is not permitted to add or change software installed on the router. login { class JR_ENGINEER { permissions all; deny-commands "request system software"; } Note: The following are the options under request system software: abort -Abort software upgrade add -Add extension or upgrade package delete -Remove extension or upgrade package rollback -Roll back to previous set of packages validate -Verify package compatibility with current configuration If the router is not configured to prohibit installation of software without explicit privileged status, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-217337`

### Rule: The Juniper router must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-217337r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. snmp { v3 { usm { local-engine { user R5_NMS { authentication-sha { authentication-key "$8$vOiLX-Vb2oaUwsJDiHmPz3690BcSevM"; ## SECRET-DATA } } } } target-address NMS_HOST { address x.x.x.x; address-mask 255.255.255.0; tag-list NMS; target-parameters TP1; } target-parameters TP1 { parameters { message-processing-model v3; security-model usm; security-level authentication; security-name R5_NMS; } } notify SEND_TRAPS { type trap; tag NMS; } snmp-community index1 { security-name R5_NMS; tag NMS; } } } If the router is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-217338`

### Rule: The Juniper router must be configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm.

**Rule ID:** `SV-217338r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the strong encryption that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information that can be used to create a network outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. snmp { v3 { usm { local-engine { user R5_NMS { authentication-sha { authentication-key "$8$vOiLX-Vb2oaUwsJDiHmPz3690BcSevM"; ## SECRET-DATA } privacy-aes128 { privacy-key "$8$3Q4T9CuOBESyK1IrvW87NwYgoDiPfz3nCs24Z"; ## SECRET-DATA } } } } target-address NMS_HOST { address 10.1.58.2; address-mask 255.255.255.0; tag-list NMS; target-parameters TP1; } target-parameters TP1 { parameters { message-processing-model v3; security-model usm; security-level privacy; security-name R5_NMS; } } notify SEND_TRAPS { type trap; tag NMS; } snmp-community index1 { security-name R5_NMS; tag NMS; } } } Note: SNMPv3 security level privacy also authenticates the messages using the configured HMAC. If the router is not configured to encrypt SNMP messages using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-217339`

### Rule: The Juniper router must be configured to authenticate NTP sources using authentication that is cryptographically based.

**Rule ID:** `SV-217339r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the configuration example below. system { … … … } ntp { authentication-key 1 type md5 value "$8$LMK7NbHkPTQnVwF/"; ## SECRET-DATA authentication-key 2 type md5 value "$8$I3KceWbwgJUH"; ## SECRET-DATA server x.x.x.x key 1 prefer; ## SECRET-DATA server x.x.x.x key 2; ## SECRET-DATA trusted-key [1 2]; } If the router is not configured to authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-217340`

### Rule: The Juniper router must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of remote maintenance sessions.

**Rule ID:** `SV-217340r961554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the Internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { … … … } services { ssh { protocol-version v2; macs hmac-sha2-256; } } If the router is not configured to use FIPS-validated HMAC to protect the integrity of remote maintenance sessions, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-217341`

### Rule: The Juniper router must be configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-217341r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. system { … … … } services { ssh { protocol-version v2; ciphers aes128-cbc; } } If the router is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-217342`

### Rule: The Juniper router must be configured to protect against known types of Denial of Service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-217342r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. Step 1: Verify that the loopback interfaces has been configured with an input filter. The example below defined a control plane policing (CoPP) filter named CoPP_Policy. interfaces { … … … lo0 { unit 0 { family inet { filter { input CoPP_Policy; } address 5.5.5.5/32; } } } } Step 2: Verify that the filter will protect against DoS attacks. firewall { … … … } filter CoPP_Policy { term CRITICAL { from { protocol [ ospf pim tcp ]; source-port bgp; destination-port bgp; } then policer CRITICAL; } term IMPORTANT { from { source-address { 10.1.1.0/24; } protocol tcp; destination-port [ ssh snmp ntp ]; } then { policer IMPORTANT; discard; } } term NORMAL { from { protocol icmp; icmp-type [ echo-reply echo-request ]; icmp-code [ ttl-eq-zero-during-transit port-unreachable ]; } then policer NORMAL; } term UNDESIRABLE { from { protocol udp; destination-port 1434; } then policer UNDESIRABLE; } term ALL-OTHER { from { address { 0.0.0.0/0; } } then policer ALL-OTHER; } } } Step 3: verify that policers configured will restrict bandwidth based on traffic types as shown in the example below. firewall { … … … } policer CRITICAL { filter-specific; if-exceeding { bandwidth-limit 4m; burst-size-limit 1500; } then discard; } policer IMPORTANT { filter-specific; if-exceeding { bandwidth-limit 512k; burst-size-limit 16k; } then discard; } policer NORMAL { filter-specific; if-exceeding { bandwidth-limit 64k; burst-size-limit 2k; } then discard; } policer UNDESIRABLE { filter-specific; if-exceeding { bandwidth-limit 32k; burst-size-limit 1500; } then discard; } policer ALL-OTHER { filter-specific; if-exceeding { bandwidth-limit 32k; burst-size-limit 1500; } then discard; } If the router is not configured to protect against known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-217343`

### Rule: The Juniper router must be configured to generate log records when administrator privileges are modified.

**Rule ID:** `SV-217343r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the examples below. syslog { file LOG_FILE { change-log info; } } Note: The parameter "any" can be in place of "authorization info" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to generate log records when administrator privileges are modified, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-217344`

### Rule: The Juniper router must be configured to generate log records when administrator privileges are deleted.

**Rule ID:** `SV-217344r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. syslog { file LOG_FILE { change-log info; } } Note: The parameter "any" can be in place of "change-log" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to generate log records when administrator privileges are deleted, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-217345`

### Rule: The Juniper router must be configured to generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-217345r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the examples below. syslog { file LOG_FILE { authorization info; } } Note: The parameter "any" can be in place of "authorization" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to generate audit records when successful/unsuccessful logon attempts occur, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-217346`

### Rule: The Juniper router must be configured to generate log records for privileged activities.

**Rule ID:** `SV-217346r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example configurations below. syslog { file LOG_FILE { change-log info; interactive-commands info; } } Note: The parameter "any" can be in place of "change-log" and “interactive-commands” as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to generate log records for privileged activities, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-217347`

### Rule: The Juniper router must be configured to generate log records when concurrent logons from different workstations occur.

**Rule ID:** `SV-217347r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the examples below. syslog { file LOG_FILE { authorization info; } } Note: The parameter "any" can be in place of "authorization" as this will log everything. Also, a syslog server can be configured in addition to or in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to generate log records when concurrent logons from different workstations occur, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-217348`

### Rule: The Juniper router must be configured to off-load log records onto a different system than the system being audited.

**Rule ID:** `SV-217348r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement as shown in the example below. system { syslog { host x.x.x.x { any info; } } If the router is not configured to off-load log records onto a different system than the system being audited, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-217349`

### Rule: The Juniper router must be configured to generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-217349r1050859_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The example below illustrates how selected events can be logged. syslog { file LOG_FILE { authorization info; any info; change-log info; } } Note: A syslog server can be configured in lieu of logging to a file as shown in the example below. system { syslog { host x.x.x.x { authorization info; any info; change-log info; } } If the router is not configured to generate log records for a locally developed list of auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-217350`

### Rule: The Juniper router must be configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-217350r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of user accounts and authentication increases the administrative access to the router. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that the device is configured to use at least two authentication servers as primary source for authentication as shown in the following example: system { authentication-order radius; } radius-server { x.x.x.x secret "$8$xYW-dsq.5zF/wYnC"; ## SECRET-DATA } radius-server { x.x.x.x secret "$8$xYW-dsq.5zF/wYnC"; ## SECRET-DATA } If the router is not configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-217351`

### Rule: The Juniper router must be configured to support organizational requirements to conduct backups of the configuration when changes occur.

**Rule ID:** `SV-217351r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The example configuration below will send the router configuration to an SCP server upon the commit command. system { … … … archival { configuration { transfer-on-commit; archive-sites { "scp://scpuser@1.2.3.4:/configs" password "$9$CMJKpu1LX-bwgBIYo"; ## SECRET-DATA } } } } If the router is not configured to conduct backups of the configuration when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-217352`

### Rule: The Juniper router must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-217352r991995_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority (CA) at medium assurance or higher, this CA will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that it is compliant with this requirement. The configuration below is an example of a CA profile defining name of the CA, the location of CRL for revocation check and to refresh the CRL every 24 hours, and the email address to send a certificate request. security { pki { ca-profile DODXX_CA { ca-identity xxxxx.mil; revocation-check { crl { url http://server1.xxxxx.mil/CertEnroll/example.crl; refresh-interval 24; } } administrator { email-address "certadmin@xxxxx.mil"; } } } } If the router is not configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-220141`

### Rule: The Juniper router must be configured to send log data to at least two syslog servers for the purpose of forwarding alerts to the administrators and the Information System Security Officers (ISSO).

**Rule ID:** `SV-220141r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router is configured to send logs to at least two syslog servers. The configuration should look similar to the example below: system { syslog { host x.x.x.x { any info; } host x.x.x.x { any info; } } If the router is not configured to send log data to the syslog servers, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-220142`

### Rule: The Juniper router must be configured with a master password that is used to generate encrypted keys for shared secrets.

**Rule ID:** `SV-220142r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, shared secrets in a Junos configuration only use an obfuscation algorithm ($9$ format), which is not very strong and can easily be decrypted. Strong encryption for configured secrets can be enabled by configuring a master password to be used as input to the password based key derivation function (PBKDF2) to generate an encryption key. The key is used as input to the Advanced Encryption Standard in Galois/Counter Mode (AES256-GCM).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a master password has been configured as by entering the following command: show configuration system master-password The output will appear as follows: password-configured; Note: The master password is hidden from the configuration. If a master password has not been configured, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-220143`

### Rule: The Juniper router must be running a Junos release that is currently supported by Juniper Networks.

**Rule ID:** `SV-220143r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities. Running a supported release also enables operations to maintain a stable and reliable network provided by improved quality of service and security features.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the router is in compliance with this requirement by having the router administrator enter the following command: show version End of support dates for all Junos releases can be found at the URL listed below. https://support.juniper.net/support/eol/software/junos/ If the Juniper router is not running a supported Junos release, this is a finding.

