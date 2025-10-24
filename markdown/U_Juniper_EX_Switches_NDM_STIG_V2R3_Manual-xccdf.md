# STIG Benchmark: Juniper EX Series Switches Network Device Management Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-253878`

### Rule: The Juniper EX switch must be configured to limit the number of concurrent management sessions to 10 or an organization-defined value.

**Rule ID:** `SV-253878r1028864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions must be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions. Juniper switches apply session limits per access method (e.g., web management, SSH), which means the limit is applicable to local, remote, and root account sessions. Unconfigured management access methods are disabled. For instance, if there is no [edit system services ssh] stanza, that service is unavailable and a connection-limit should not be configured because that will enable the service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If, based on operational needs, an organization defined number other than 1 is used, document the value in the SSP. View the SSH service configuration using the "show configuration system services ssh" command. SSH example. user@host> show configuration system services ssh connection-limit 1; rate-limit 1 If the device does not limit the number of concurrent management sessions to 1 or an organization-defined number, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-253879`

### Rule: The Juniper EX switch must be configured to automatically audit account creation.

**Rule ID:** `SV-253879r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if it automatically audits account creation or is configured to use an authentication server that would perform this function. Verify the system logs the facility "any", or minimally "change-log" and "interactive-commands", and the logging level is appropriate. Generally, the "all" (debug) logging level should be avoided because the number of logged messages is significant. [edit system syslog] host <IPv4 or IPv6 syslog address> { any info; } file <file name> { change-log info; interactive-commands info; } Note: If minimally logging only configuration changes, there will be other files receiving the events from the other logging facilities (e.g., "authorizations" or "firewall"). Syslog outputs in standard format unless the "structured-data" directive is configured. Verify the "structured-data" command for all files and external syslog servers requiring that format. For example: [edit system syslog] host <IPv4 or IPv6 syslog address> { change-log info; interactive-commands info; structured-data; } file <file name> { any info; structured-data; } If account creation is not automatically audited, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-253883`

### Rule: The Juniper EX switch must be configured to assign appropriate user roles or access levels to authenticated users.

**Rule ID:** `SV-253883r960792_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful identification and authentication must not automatically give an entity full access to a network device or security domain. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset or set of resources. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Some network devices are pre-configured with security groups. Other network devices enable operators to create custom security groups with custom permissions. For example, an ISSM may require read-only access to audit the network device. Operators may create an audit security group, define permissions and access levels for members of the group, and then assign the ISSM’s user persona to the audit security group. This is still considered privileged access, but the ISSM’s security group is more restrictive than the network administrator’s security group. Network devices that rely on AAA brokers for authentication and authorization services may need to identify the available security groups or access levels available on the network devices and convey that information to the AAA operator. Once the AAA broker identifies the user persona on the centralized directory service, the user’s security group memberships can be retrieved. The AAA operator may need to create a mapping that links target security groups from the directory service to the appropriate security groups or access levels on the network device. Once these mappings are configured, authorizations can happen dynamically, based on each user’s directory service group membership.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the network device is configured to use a AAA service account, and the AAA broker is configured to assign authorization levels based on centralized user account group memberships on behalf of the network device, that will satisfy this objective. Because the responsibility for meeting this objective is transferred to the AAA broker, this requirement is not applicable for the local network device. This requirement may be verified by demonstration or configuration review. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and/or local authentication depending upon the authentication order. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives, or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. Verify the network device is configured to assign appropriate user roles or access levels to authenticated users. This requirement may be verified by demonstration or configuration review. If the network device does not enforce the assigned privilege level for each administrator and authorizations for access to all commands relative to the privilege level, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-253884`

### Rule: The Juniper EX switch must be configured to enforce approved authorizations for controlling the flow of management information within the network device based on information flow control policies.

**Rule ID:** `SV-253884r997739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if it enforces approved authorizations for controlling the flow of management information within the network device based on information flow control policies. Verify the switch permits administrative access only from the authorized management network(s). Verify filters and terms account for all authorized management traffic. Example prefix-list defining the management networks. Prefix lists are not required because IP addresses can be directly embedded into terms, but they define a set of IP addresses once that permits use across multiple terms. [edit policy-options] prefix-list ipv4-management { <IPv4 MGT subnet/mask>; } prefix-list ipv6-management { <IPv6 MGT subnet/prefix>; } Example firewall filter for SSH traffic: [edit firewall] family inet { filter permit-management-ipv4 { term 1 { from { destination-address { <OOBM IPv4 address>; } source-address { << Example embedded addresses using the 'source-address' match criterion <IPv4 MGT subnet/mask>; } --or-- source-prefix-list { << Example inherited addresses using the 'source-prefix-list' match criterion ipv4-management; } protocol tcp; destination-port 22; } then { syslog; accept; } } term 2 { then { syslog; discard; } } } } family inet6 { filter permit-management-ipv6 { term 1 { from { destination-address { <OOBM IPv6 address>; } source-address { << Example embedded addresses using the 'source-address' match criterion <IPv6 MGT subnet/prefix>; } --or-- source-prefix-list { << Example inherited addresses using the 'source-prefix-list' match criterion ipv6-management; } next-header tcp; destination-port 22; } then { syslog; accept; } } term 2 { then { syslog; discard; } } } } Note: Additional terms will be required for other services like SNMP, RADIUS, or syslog. Example firewall filter applied to the OOBM interface. Juniper devices use different OOBM interface names depending upon platform (fxp0 used in the example): [edit interfaces] fxp0 { unit 0 { family inet { filter { input permit-management-ipv4; } address <OOBM IPv4 address>/<mask>; } family inet6 { filter { input permit-management-ipv6; } address <OOBM IPv6 address>/<prefix>; } } } Note: Although the example filter is shown applied to the management interface, the filter can also be applied to the loopback interface (lo0). If applying to loopback, ensure the filter terms account for all traffic, services, and protocols that must reach the routing engine (e.g., OSPF, BGP, SNMP, etc.). If the switch does not enforce approved authorizations for controlling the flow of management information within the device based on information control policies, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-253885`

### Rule: The Juniper EX switch must be configured to enforce the limit of three consecutive invalid logon attempts for any given user, after which time it must block any login attempt for that user for 15 minutes.

**Rule ID:** `SV-253885r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Introducing a lockout period significantly increases the time required for each brute-force attack and increases the likelihood that security personnel will identify (and can respond to) an ongoing attack and/or that the authorized owner will recognize and report the unauthorized activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Juniper switches maintain the number of failed login attempts per user until the session is restarted or, if lockout-period is configured, until the next successful login. If the permissible number of failed login attempts is reached, the switch prevents logging in for the duration of the lockout-period (1..43200 minutes) regardless whether the account is locally or externally authenticated and across all management access methods (e.g., local console and SSH). Review the device configuration to verify that it enforces the limit of three consecutive invalid logon attempts before introducing a 15 minute lockout period. [edit system login] retry-options { tries-before-disconnect 3; lockout-period 15; } If the device is not configured to enforce the limit of three consecutive invalid logon attempts before introducing a 15-minute block on subsequent login attempts, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-253886`

### Rule: The Juniper EX switch must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-253886r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to present a DOD-approved banner that is formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Verify the appropriate banner is configured. [edit system login] message "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions:\n\n-The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations.\n\n-At any time, the USG may inspect and seize data stored on this IS.\n\n-Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG authorized purpose.-This IS includes security measures (e.g., authentication and access controls) to protect USG interests-not for your personal benefit or privacy.\n\n-Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details.\n"; If such a banner is not presented, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-253889`

### Rule: The Juniper device must be configured to produce audit log records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-253889r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device produces audit log records containing sufficient information to establish what type of event occurred. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not produce audit log records containing sufficient information to establish what type of event occurred, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-253890`

### Rule: The Juniper EX switch must be configured to produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-253890r960894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. In order to establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to produce audit records containing information to establish when (date and time) the events occurred. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not produce audit records containing information to establish when the events occurred, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-253891`

### Rule: The Juniper EX switch must be configured to produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-253891r960897_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Associating information about where the event occurred within the network device provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to produce audit records containing information to establish where the events occurred. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not produce audit records containing information to establish where the events occurred, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-253892`

### Rule: The Juniper EX switch must be configured to produce audit log records containing information to establish the source of events.

**Rule ID:** `SV-253892r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Associating information about where the source of the event occurred provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to produce audit records containing information to establish the source (apparent cause) of the event. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not produce audit records containing information to establish the source of the event, this is a finding.

## Group: SRG-APP-000099-NDM-000229

**Group ID:** `V-253893`

### Rule: The Juniper EX switch must be configured to produce audit records that contain information to establish the outcome of the event.

**Rule ID:** `SV-253893r960903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the device after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to produce audit records that contain information to establish the outcome of the event. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not produce audit records that contain information to establish the outcome of the event, this is a finding.

## Group: SRG-APP-000100-NDM-000230

**Group ID:** `V-253894`

### Rule: The Juniper EX switch must be configured to generate audit records containing information that establishes the identity of any individual or process associated with the event.

**Rule ID:** `SV-253894r960906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., administrators or processes acting on behalf of administrators) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Event identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit records containing information that establishes the identity of any individual or process associated with the event. This requirement may be verified by demonstration or validated test results. Junos standard event log messages are configurable for time format, inclusion of logging facility and severity levels, and format. Setting "structured-data" automatically includes "explicit-priority" and "time-format year millisecond". Verify logging is enabled. [edit system] syslog { host <syslog IPv4 or IPv6 address> { any info; structured-data; <<< Includes 'explicit-priority' and 'time-format' } host <syslog IPv4 or IPv6 address> { any info; explicit-priority; <<< Includes logging facility and severity in standard format } file <file name> { any info; <<< Uses only standard format } time-format year; <<< Applied only to standard format } Note: In the example, events sent to the first external syslog server include the year and time is expressed in milliseconds. The second syslog server and the file both include the year, but time is expressed in seconds. If the network device does not generate audit records containing information that establishes the identity of any individual or process associated with the event, this is a finding.

## Group: SRG-APP-000119-NDM-000236

**Group ID:** `V-253896`

### Rule: The Juniper EX switch must be configured to protect audit information from unauthorized modification.

**Rule ID:** `SV-253896r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit network device activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys to make access decisions regarding the modification of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device protects audit information from any type of unauthorized modification with such methods as ensuring log files receive the proper file system permissions, limiting log data locations, and leveraging user permissions and roles to identify the user accessing the data and the corresponding rights that the user enjoys. This requirement may be verified by demonstration, configuration, or validated test results. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Audit logs are configured in the [edit system] hierarchy and require the "system" permission to view and the "system-control" permission to configure (or permissions set "all"). However, using the allow or deny statements permits adding, or removing, specific commands or configuration hierarchy levels. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If the network device does not protect audit information from unauthorized modification, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-253897`

### Rule: The Juniper EX switch must be configured to protect audit information from unauthorized deletion.

**Rule ID:** `SV-253897r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device protects audit information from any type of unauthorized deletion with such methods as ensuring log files receive the proper file system permissions utilizing file system protections, restricting access to log data and backing up log data to ensure log data is retained, and leveraging user permissions and roles to identify the user accessing the data and the corresponding rights the user enjoys. This requirement may be verified by demonstration, configuration, or validated test results. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Audit logs are configured in the [edit system] hierarchy and require the "system" permission to view and the "system-control" permission to configure (or permissions set "all"). However, using the allow or deny statements permits adding, or removing, specific commands or configuration hierarchy levels. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If the network device does not protect audit information from unauthorized deletion, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-253898`

### Rule: The Juniper EX switch must be configured to protect audit tools from unauthorized access.

**Rule ID:** `SV-253898r960939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Junos provides the operational mode commands "show" (to display the contents of a log file) or "clear" (to delete all of the contents of a log file); there is no text editor or other "audit tool" provided in the CLI. Operational and configuration mode commands require assignment of the required permission bit to execute. For example, audit logs are configured in the [edit system] hierarchy and require the "system" permission to view and the "system-control" permission to configure (or permissions set "all"). However, using the allow or deny statements permits adding, or removing, specific commands or configuration hierarchy levels. Adding the "deny-commands "^clear log"" directive to a login class prevents any user assigned to that class from clearing any log file. Verify the permissions assigned to each login class is appropriate. In addition to limiting permissions, Junos supports limiting commands and hierarchy levels that would otherwise be permitted. For example, to remove the ability to modify auditing from a login class with the "system-control" or "all" permissions assigned, use the "deny-configuration-regexps [ "system syslog" ]" directive. To prevent administrative users assigned to that same login class from viewing and/or deleting the audit file contents, add the "deny-commands "^(show|clear) log"" directive. Example login-class definitions: [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If the network device does not protect its audit tools from unauthorized access, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-253899`

### Rule: The Juniper EX switch must be configured to limit privileges to change the software resident within software libraries.

**Rule ID:** `SV-253899r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. If the network device were to enable nonauthorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device limits privileges to change the software resident within software libraries. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Installation of firmware requires the maintenance permission bit. However, even with that bit set, software installation can be limited by the "deny-commands" statement (e.g., deny-commands "^request system software"). The command takes a regular expression (REGEX) enclosed in double quotes ("). Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If it does not limit privileges to change the software resident within software libraries, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-253900`

### Rule: The Juniper EX switch must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-253900r1043177_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device prohibits the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services. Verify unnecessary or nonsecure functions are not configured or are explicitly disabled. For example, FTP and Telnet are nonsecure. Verify these services are not enabled as in the example below: [edit system services] ftp; telnet; If any unnecessary or nonsecure functions are permitted, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-253901`

### Rule: The Juniper EX switch must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-253901r1082953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account is created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit must be added to the envelope as a record. Administrators must secure the credentials and disable access to the root account (if possible) when not needed for system administration functions. Junos does not have default passwords, and the root account cannot be renamed or disabled. The root account password must be saved in the same manner as the account of last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the Juniper EX configuration to determine if an account of last resort is configured. 2. Verify the username and password for the root account, and the account of last resort is contained within sealed envelopes and kept in a safe. Junos categorizes user accounts as "local" or "template", with the difference being the presence of an authentication stanza. Accounts with an authentication stanza are local because the administrator can log in without the need for an external AAA service. Accounts without an authentication stanza are templates that require external authentication. Verify only authorized account(s) have an authentication stanza. user@host> show configuration system login ... user <name> { ... <<< No authentication stanza for externally authenticated accounts } user <account of last resort username> { ... authentication { encrypted-password <password hash>; } } The authentication order must be configured to prefer external AAA, and "password" authentication can be omitted if required. If "password" is present, Junos will attempt password authentication upon external AAA authentication failure. This feature is useful if the account of last resort is required while external AAA remains reachable but is misconfigured and prevents successful logon. If "password" is not present, Junos will not fail over to local authentication unless there is a loss of connectivity with the external AAA service (e.g., timeout). Verify the authentication order prefers external AAA (first in the order). user@host> show configuration system authentication-order authentication-order [ <external AAA> password ] --or-- authentication-order <external AAA>; Verify that direct root logon is disabled. user@host> show configuration system services ssh <<< missing root-login directive inherits the default 'deny' protocol-version v2; ...<snip>... --or-- root-login deny; ...<snip>... If one local account does not exist for use as the account of last resort, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-253903`

### Rule: The Juniper EX switch must be configured to implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-253903r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device implements replay-resistant authentication mechanisms for network access to privileged accounts. This requirement may be verified by demonstration, configuration review, or validated test results. This requirement may be met through use of a properly configured authentication server if the device is configured to use the authentication server. Verify SSH version 2 is configured for network (remote) access to privileged accounts. [edit system services ssh] protocol-version v2; If the network device does not implement replay-resistant authentication mechanisms for network access to privileged accounts, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-253904`

### Rule: The Juniper EX switch must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-253904r1018762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device or its associated authentication server enforces a minimum 15-character password length. This requirement may be verified by demonstration or configuration review. [edit system login password] : minimum-length 15; : If the network device or its associated authentication server does not enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-253905`

### Rule: The Juniper EX switch must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-253905r1028866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement may be verified by demonstration, configuration review, or validated test results. [edit system login password] : minimum-upper-cases 1; : If the network device and associated authentication server does not require that at least one uppercase character be used in each password, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-253906`

### Rule: The Juniper EX switch must be configured to enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-253906r1028873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that the network device and associated authentication server enforces password complexity by requiring that at least one lowercase character be used. This requirement may be verified by demonstration, configuration review, or validated test results. [edit system login password] : minimum-lower-cases 1; : If the network device and associated authentication server does not require that at least one lowercase character be used in each password, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-253907`

### Rule: The Juniper EX switch must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-253907r1018765_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that the network device and associated authentication server enforces password complexity by requiring that at least one numeric character be used. This requirement may be verified by demonstration, configuration review, or validated test results. [edit system login password] : minimum-numerics 1; : If the network device and associated authentication server does not require that at least one numeric character be used in each password, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-253908`

### Rule: The Juniper EX switch must be configured to enforce password complexity by requiring that at least one punctuation (special) character be used.

**Rule ID:** `SV-253908r1018766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that the network device and associated authentication server enforces password complexity by requiring that at least one punctuation (special) character be used. This requirement may be verified by demonstration, configuration review, or validated test results. [edit system login password] : minimum-punctuations 1; : If the network device and associated authentication server does not require that at least one special character be used in each password, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-253909`

### Rule: The Juniper EX switch must be configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-253909r1082956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account. Note: For older Juniper EX versions, only four characters may be changed instead of the DOD-required eight characters. If so, four characters should be selected. This remains a finding when set to four characters, but is mitigated to a CAT 3.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For older Juniper EX versions, only four characters may be changed instead of the DOD-required eight characters. If so, four characters should be selected. This remains a finding when set to four characters, but is mitigated to a CAT 3. Where passwords are used, confirm the characters are changed in at least eight of the positions within the password. This requirement may be verified by demonstration, configuration review, or validated test results. [edit system login password] : minimum-character-changes 8; : If the network device and associated authentication server does not require that when a password is changed, the characters are changed in at least eight of the positions within the password, this is a finding.

## Group: SRG-APP-000171-NDM-000258

**Group ID:** `V-253910`

### Rule: The Juniper EX switch must be configured to only store cryptographic representations of passwords.

**Rule ID:** `SV-253910r1018768_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices must enforce cryptographic representations of passwords when storing passwords in databases, configuration files, and log files. Passwords must be protected at all times; using a strong one-way hashing encryption algorithm with a salt is the standard method for providing a means to validate a password without having to store the actual password. Performance and time required to access are factors that must be considered, and the one-way hash is the most feasible means of securing the password and providing an acceptable measure of password security. If passwords are stored in clear text, they can be plainly read and easily compromised. In many instances, verifying the user knows a password is performed using a password verifier. In its simplest form, a password verifier is a computational function that is capable of creating a hash of a password and determining if the value provided by the user matches the stored hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device’s files using a text editor or a database tool that allows viewing data stored in database tables. Determine if password strings are readable/discernable. Determine if the network device, and any associated authentication servers, enforce only storing cryptographic representations of passwords. Verify that databases, configuration files, and log files have encrypted representations of all passwords, and that no password strings are readable/discernable. Potential locations include the local file system where configurations and events are stored, or in a network device related database table. Also identify if the network device uses the MD5 hashing algorithm to create password hashes. By default, Junos uses SHA-512 as the password hashing algorithm to save only hashed representations of passwords. Verify the hashing algorithm at [edit system login password] format. [edit system login password] : format sha512; If the network device, or any associated authentication servers, stores unencrypted (clear text) representations of passwords, this is a finding. If the network device uses MD5 hashing algorithm to create password hashes, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-253911`

### Rule: The Juniper EX switch must be configured to use FIPS 140-2/140-3 validated algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-253911r1082959_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not validated and therefore, cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-validated and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the password format, and that SSH uses FIPS validated algorithms and random number generator (RNG) as shown in the following example configuration. user@host> show configuration system login { password { : format <sha-256|sha-512>; } } services { ssh { : ciphers [ aes256-ctr aes256-cbc]; macs [ hmac-sha2-512 hmac-sha2-256 ]; key-exchange [ ecdh-sha2-nistp521 ecdh-sha2-nistp384 ecdh-sha2-nistp256 ]; : } } rng { hmac-drbg; } If the network device is not configured to use FIPS 140-2/140-3 validated authentication algorithms, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-253913`

### Rule: The Juniper EX switch must be configured to end all network connections associated with a device management session at the end of the session, or the session must be terminated after five minutes of inactivity except to fulfill mission requirements.

**Rule ID:** `SV-253913r1082962_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device terminates the connection associated with a device management session at the end of the session or after five minutes of inactivity. This requirement may be verified by demonstration or configuration review. Junos permits the administrator to log out at the end of the session, which terminates the session and the network connection. Junos forcibly terminates the session and network connection upon exceeding the inactivity timeout threshold. Inactivity timeouts are assigned to login classes and apply to every administrative access method; there is no provision to set inactivity timeout differently for local (console) and network (remote) device management sessions. Verify the idle-timeout for the root user, and each login class, has an appropriate idle-timeout value. user@host> show configuration system login ... idle-timeout 5; class <name> { idle-timeout 5; ... } Note: Inactivity timeout (idle-timeout) must be assigned to every login class. If the network device does not terminate the connection associated with a device management session at the end of the session or after five minutes of inactivity, this is a finding.

## Group: SRG-APP-000231-NDM-000271

**Group ID:** `V-253914`

### Rule: The Juniper device must be configured to only allow authorized administrators to view or change the device configuration, system files, and other files stored either in the device or on removable media (such as a flash drive).

**Rule ID:** `SV-253914r961128_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement is intended to address the confidentiality and integrity of system information at rest (e.g., network device rule sets) when it is located on a storage device within the network device or as a component of the network device. This protection is required to prevent unauthorized alteration, corruption, or disclosure of information when not stored directly on the network device. Files on the network device or on removable media used by the device must have their permissions set to allow read or write access to those accounts that are specifically authorized to access or change them. Note that different administrative accounts or roles will have varying levels of access. File permissions must be set so that only authorized administrators can read or change their contents. Whenever files are written to removable media and the media removed from the device, the media must be handled appropriately for the classification and sensitivity of the data stored on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Junos operating system maintains file permissions for all files on the device and cannot be configured otherwise. Because Juniper digitally signs and used cryptographic hashes, modified system files (specifically binary files) will invalidate the signature/hash and will not be executed. The Junos OS enforces the permissions assigned to each user to restrict access to system, configuration, and audit files via login classes. Every account must be assigned a login class by an authorized administrator. Verify each account is assigned a login class with appropriate permissions based on organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Verify "no-world-readable" for archived log files. [edit system syslog] archive size <file size> files <number of files> no-world-readable; If any files allow read or write access by accounts not specifically authorized access or by nonprivileged accounts, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-253916`

### Rule: The Juniper EX switch must be configured to enforce organization-defined role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-253916r987662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces role-based access control policy over defined subjects and objects. This requirement may be verified by demonstration, configuration review, or validated test results. This requirement may be met through use of a properly configured authentication server if the device is configured to use the authentication server. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If role-based access control policy is not enforced over defined subjects and objects, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-253918`

### Rule: The Juniper EX switch must be configured to allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-253918r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device allocates audit record storage capacity in accordance with organization-defined audit record storage requirements. This requirement may be verified by configuration review or vendor-provided information. This requirement may be met through use of a properly configured syslog server if the device is configured to use the syslog server. Junos does not permit configuring audit logging storage space. However, the majority of disk space is reserved for local audit log storage and file are rotated using a first-in-first-out (FIFO) function. Verify external syslog servers are configured. [edit system syslog] host <address 1> { any info; } host <address 2> { any info; } If audit record store capacity is not allocated in accordance with organization-defined audit record storage requirements, or the device is not configured to use external syslog server(s), this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-253919`

### Rule: The Juniper EX switch must be configured to generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-253919r961401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates an immediate alert of all audit failure events requiring real-time alerts. Juniper network devices support monitoring the audit log storage partition (/var), monitoring the SNMP health status, or both. On devices supporting disk partition monitoring, verify the audit log partition (/var) free space is configured appropriately for the environment. For example, to generate "high disk usage" alerts at 80 percent capacity (20 percent free), and "full disk usage" at 90 percent capacity (10 percent free): [edit chassis] disk-partition /var { level full { free-space 10 percent; } level high { free-space 20 percent; } } Note: The configurable parameter is a percentage of free space remaining, not percentage used. "High" usage percent of remaining free space must be equal to, or greater than, the "full" usage percent of remaining free space. For network devices supporting SNMP health monitoring, verify the rising and falling threshold values for monitored objects (e.g., CPU, memory, and disk storage usage). In the example below, any monitored object exceeding 75 percent usage will generate an alert. Another alert is generated when the usage falls below 74 percent. As configured in the example, Junos samples every 300 seconds. The falling threshold value must be less than the rising threshold value. Verify the thresholds are appropriate for the target environment. [edit snmp] health-monitor { interval 300; rising-threshold 75; falling-threshold 74; } Note: Monitored objects generate an event the first time they cross a threshold, not at every sample interval. This requirement may be verified by configuration review or validated test results. If an immediate alert of all audit failure events requiring real-time alerts is not generated, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-253920`

### Rule: The Juniper EX switch must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-253920r1018769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: A time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to synchronize internal information system clocks with the primary and secondary time sources. Verify the Network Time Protocol (NTP) configuration. [edit system ntp] authentication-key 1 type sha256 value "PSK"; ## SECRET-DATA authentication-key 2 type sha1 value "PSK"; ## SECRET-DATA server <address 1> key 1 prefer; ## SECRET-DATA server <address 2> key 2; ## SECRET-DATA trusted-key [ 1 2 ]; source-address <lo0 or OOBM address>; If the network device is not configured to synchronize internal information system clocks with the primary and secondary time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-253921`

### Rule: The Juniper EX switch must be configured to record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-253921r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in UTC, a modern continuation of GMT, or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device records time stamps for audit records that can be mapped to UTC or GMT. This requirement may be verified by demonstration or configuration review. Verify the time zone is UTC. [edit system] time-zone UTC; If the network device does not record time stamps for audit records that can be mapped to UTC or GMT, this is a finding.

## Group: SRG-APP-000378-NDM-000302

**Group ID:** `V-253922`

### Rule: The Juniper EX switch must be configured to prohibit installation of software without explicit privileged status.

**Rule ID:** `SV-253922r1018770_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing anyone to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. This requirement applies to code changes and upgrades for all network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device prohibits installation of software without explicit privileged status. This requirement may be verified by demonstration or configuration review. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Installation of firmware requires the maintenance permission bit. However, even with that bit set, software installation can be limited by the "deny-commands" statement (e.g., deny-commands "^request system software"). The command takes a regular expression (REGEX) enclosed in double quotes ("). Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If installation of software is not prohibited without explicit privileged status, this is a finding.

## Group: SRG-APP-000380-NDM-000304

**Group ID:** `V-253923`

### Rule: The Juniper EX switch must be configured to enforce access restrictions associated with changes to device configuration.

**Rule ID:** `SV-253923r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to device configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the device can potentially have significant effects on the overall security of the device. Accordingly, only qualified and authorized individuals should be allowed to obtain access to device components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces access restrictions associated with changes to device configuration. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Configuration changes require permissions sets appropriate for each stanza. For example, the "system" bit permits one to view [edit system] and the "system-control" bit permits editing (add, delete, modify). Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If the network device does not enforce such access restrictions, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-253925`

### Rule: The Juniper EX switch must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-253925r961506_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to verify SNMP messages are authenticated using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC). By default, SNMP is disabled. If used, verify SNMPv3 is configured (minimally) for authentication-sha. Although HMAC-MD5-96 is supported as required by RFC, Junos also supports HMAC-SHA, HMAC-SHA224/256/384/512. Configure the strongest HMAC supported by both the Juniper device and the Network Management System (NMS). [edit snmp v3] usm { local-engine { user <SNMPv3 user> { authentication-sha { authentication-key "$8$aes256-gcm$hmac-sha2-256$100$2CM/LosUGF4$A...<snip>...rflBKxq/w+jaAVF55Bsc6PA"; ## SECRET-DATA } } } } If the network device is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-253926`

### Rule: The Juniper EX switch must use an an NTP service that is hosted by a trusted source or a DOD-compliant enterprise or local NTP server.

**Rule ID:** `SV-253926r961506_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If a trusted time source is not used, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate which may hide attacks or result in inaccurate forensic analysis. The recommended solution is that the application or endpoint is configured to point to an enterprise or site-owned time server that is DOD-compliant (instead of directly to an NTP source as implied by the current wording of the requirement). Most products are unable to meet the requirement, but DISA can mitigate the risk by using a trusted time source. So the requirement should state that NTPS is used with USNO NTP as an alternative mitigation for this to be marked as Not a Finding. More information can be found at: https://www.cnmoc.usff.navy.mil/Our-Commands/United-States-Naval-Observatory/Precise-Time-Department/Network-Time-Protocol-NTP/DoD-Customer-Servers/ DOD users should not use tick, tock, or ntp2. There are also instructions for obtaining authenticated NTP at the site listed above.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Juniper EX configuration to determine if it obtains time information from a trusted source. [edit system ntp] authentication-key 1 type sha256 value "PSK"; ## SECRET-DATA authentication-key 2 type sha1 value "PSK"; ## SECRET-DATA server <address 1> key 1 prefer; ## SECRET-DATA server <address 2> key 2; ## SECRET-DATA trusted-key [ 1 2 ]; If the network device does not support FIPS-validated algorithms, verify the network device configuration to determine NTP endpoints are authenticated before establishing the local, remote, or network connection using cryptographically based algorithms. [edit system ntp] authentication-key 3 type md5 value "PSK"; ## SECRET-DATA server <address 3> key 3; ## SECRET-DATA trusted-key [ 1 2 3 ]; If the Juniper EX switch is not configured to use an NTP service that is hosted by a trusted source or a DOD-compliant enterprise or local NTP server, this is a finding.

## Group: SRG-APP-000400-NDM-000313

**Group ID:** `V-253927`

### Rule: The Juniper EX switch must be configured to prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-253927r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some authentication implementations can be configured to use cached authenticators. If cached authentication information is out-of-date, the validity of the authentication information may be questionable. The organization-defined time period should be established for each device depending on the nature of the device; for example, a device with just a few administrators in a facility with spotty network connectivity may merit a longer caching time period than a device with many administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if the network device or its associated authentication server prohibits the use of cached authenticators after an organization-defined time period. Verify idle-timeouts, SSH keepalive messages, and SSH rekey are configured to meet the requirements of the target network. [edit system] login { idle-timeout 10; } system { services { ssh { protocol-version v2; client-alive-count-max (0..255); client-alive-interval (0..65535 seconds); rekey { data-limit (51200..4294967295 bytes); time-limit (1..1440 minutes); } } } } For externally authenticated accounts, verify the external authentication server enforces appropriate authenticator timeouts. If cached authenticators are used after an organization-defined time period, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-253928`

### Rule: The Juniper EX switches must be configured to use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-253928r961554_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers. Use only AES Counter (CTR) cipher block chaining modes in compliance with CVE-2008-5161, plugin 70658 based on vendor guidance in KB20853. This prevents certain plaintext attacks in OpenSSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the network device uses FIPS-validated HMAC to protect the integrity of nonlocal maintenance and diagnostic communications. If using SNMPv3, verify (minimally) that authentication-sha is configured. Juniper devices also support authentication-sha224/256/384/512. Verify the strongest mutually supported HMAC between the network device and the Network Management Server (NMS) is configured. [edit system snmp] v3 { usm { local-engine { user <SNMPv3 user> { authentication-sha { authentication-key "PSK"; ## SECRET-DATA } } } } } Verify SSHv2 is configured for protocol V2 only, ciphers [ aes256-ctr aes192-ctr aes128-ctr ], key-exchange [ ecdh-sha2-nistp521 ecdh-sha2-nistp384 ecdh-sha2-nistp256 ], and macs [ hmac-sha2-512 hmac-sha2-256]. [edit system services ssh] : protocol-version v2; ciphers [ aes256-ctr aes192-ctr aes128-ctr ]; macs [ hmac-sha2-512 hmac-sha2-256 ]; key-exchange [ ecdh-sha2-nistp521 ecdh-sha2-nistp384 ecdh-sha2-nistp256 ]; If the network device does not use FIPS-validated HMAC to protect the integrity of nonlocal maintenance and diagnostic communications, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-253929`

### Rule: The Juniper EX switch must be configured to implement cryptographic mechanisms using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-253929r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions. Use only CTR cipher block chaining modes in compliance with CVE-2008-5161, plugin 70658 based on vendor guidance in KB20853. This prevents certain plaintext attacks in OpenSSH.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if cryptographic mechanisms are implemented using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions. If using SNMPv3, verify (minimally) that authentication-sha is configured. Juniper devices also support authentication-sha224/256/384/512. Verify the strongest mutually supported HMAC between the network device and the Network Management Server (NMS) is configured. [edit system snmp] v3 { usm { local-engine { user <SNMPv3 user> { authentication-sha { authentication-key "PSK"; ## SECRET-DATA } } } } } Verify SSHv2 is configured for protocol V2 only, ciphers [ aes256-ctr aes192-ctr aes128-ctr ], key-exchange [ ecdh-sha2-nistp521 ecdh-sha2-nistp384 ecdh-sha2-nistp256 ], and macs [ hmac-sha2-512 hmac-sha2-256 ]. [edit system services ssh] : protocol-version v2; ciphers [ aes256-ctr aes192-ctr aes128-ctr ]; macs [ hmac-sha2-512 hmac-sha2-256 ]; key-exchange [ ecdh-sha2-nistp521 ecdh-sha2-nistp384 ecdh-sha2-nistp256 ]; If the network device is not configured to implement cryptographic mechanisms to protect the confidentiality of remote maintenance sessions using a FIPS 140-2 approved algorithm, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-253930`

### Rule: The Juniper EX switch must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-253930r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD-level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device protects against or limits the effects of all known types of DoS attacks by employing organization-defined security safeguards. Verify session and (if supported) rate limits for management connections. SSH example: [edit system services ssh] connection-limit <1..250>; rate-limit <1..250>; Note: The SSH connection- and rate-limit directives affect secure file transfer protocols like SCP and SFTP. NETCONF over SSH example: [edit system services netconf] ssh { connection-limit <1..250>; rate-limit <1..250>; } Note: Rate limiting is the permissible number of connections per one minute interval. Verify policers (rate limiters) are appropriately applied to limit traffic; for example, to limit SSH connection attempts: [edit firewall] family inet { filter <filter name> { term 1 { from { destination-address { <device OOBM or loopback address>; } source-prefix-list { <management address list name>; } protocol tcp; destination-port 22; tcp-initial; } then { policer policer-32k; syslog; accept; } } term 2 { from { destination-address { <device OOBM or loopback address>; } source-prefix-list { <management address list name>; } protocol tcp; destination-port 22; } then { syslog; accept; } } term default { then { syslog; discard; } } } } family inet6 { filter <filter name-1> { term 1 { from { destination-address { <device OOBM or loopback address>; } source-prefix-list { <management address list name-1>; } next-header tcp; destination-port 22; tcp-initial; } then { policer policer-32k; syslog; accept; } } term 2 { from { destination-address { <device OOBM or loopback address>; } source-prefix-list { <management address list name-1>; } next-header tcp; destination-port 22; } then { syslog; accept; } } term default { then { syslog; discard; } } } } Note: Additional terms will be required for other services like SNMP. policer policer-32k { if-exceeding { bandwidth-limit 32k; burst-size-limit 1500; } then discard; } [edit interfaces] <OOBM interface> { unit 0 { family inet { filter { input <filter name>; } address <IPv4 address>/<mask>; } family inet6 { filter { input <filter name-1>; } address <IPv6 address>/<prefix>; } } } Note: Although the example filter is shown applied to the management interface, the filter can be also be applied to the loopback interface. If applying to loopback, ensure the filter terms account for all traffic, services, and protocols that must reach the routing engine (e.g., OSPF, BGP, SNMP, etc.). If the network device does not protect against or limit the effects of all known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-253933`

### Rule: The Juniper EX switch must be configured to generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-253933r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit records when successful/unsuccessful logon attempts occur. Junos logs all logon attempts via the "authorization" syslog facility (or facility "any"). Verify logging level "any info" or "authorization info" is configured. [edit system syslog] file <file name> { authorization info; } host <external syslog address> { any info; } time-format year millisecond; Syslog outputs in standard format unless the "structured-data" directive is configured. Verify the "structured-data" command for all files and external syslog servers requiring that format. For example: [edit system syslog] host <syslog address> { authorization info; structured-data; } file <file name> { any info; structured-data; } If it does not generate audit records when successful/unsuccessful logon attempts occur, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-253934`

### Rule: The Juniper EX switch must be configured to generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-253934r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit records for privileged activities or other system-level access. Junos logs all completed commands via the "interactive-commands" syslog facility and all configuration changes via "change-log". Successful and unsuccessful login attempts are logged using the "authorization" facility. Verify syslog is configured to capture these facilities using the logging level "info" or above. The lowest logging level, "any", is debug and will generate significant numbers of messages. The "any" logging facility (not to be confused with the severity level "any") includes authorization, change-log, and interactive-commands. Example configuration to generate audit records for privileged activities or other system-level access. [edit system syslog] file <file name> { authorization info; change-log info; interactive-commands info; } host <syslog address> { any info; explicit-priority; } time-format year millisecond; Note: The time-format command supports including the year and/or the time in milliseconds (both shown for clarity). The default format does not include the year and time is recorded in seconds. Syslog outputs in standard format unless the "structured-data" directive is configured. Verify the "structured-data" command for all files and external syslog servers requiring that format. For example: [edit system syslog] host <syslog address> { authorization info; change-log info; interactive-commands info; structured-data; } file <file name> { any info; structured-data; } If the network device does not generate audit records for privileged activities or other system-level access, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-253935`

### Rule: The Juniper EX switch must be configured to generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-253935r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit records showing starting and ending time for administrator access to the system. Junos logs all logon attempts via the "authorization" syslog facility. Verify logging level "any info" or "authorization info" is configured. Time stamps are created for every log entry, both successful and failed logon attempts, and logout. [edit system syslog] file <file name> { any info; } host <external syslog address> { any info; } time-format year millisecond; Syslog outputs in standard format unless the "structured-data" directive is configured. Verify the "structured-data" command for all files and external syslog servers requiring that format. For example: [edit system syslog] host <syslog address> { change-log info; interactive-commands info; structured-data; } file <file name> { any info; structured-data; } If the network device does not generate audit records showing starting and ending time for administrator access to the system, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-253936`

### Rule: The Juniper EX switch must be configured to generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-253936r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit records when concurrent logons from different workstations occur. Junos logs all logon attempts via the "authorization" syslog facility. Verify logging level "any info" or "authorization info" is configured. Time stamps are created for every log entry, both successful and failed logon attempts, and logout. [edit system syslog] file <file name> { any info; } host <external syslog address> { any info; } time-format year millisecond; Syslog outputs in standard format unless the "structured-data" directive is configured. Verify the "structured-data" command for all files and external syslog servers requiring that format. For example: [edit system syslog] host <syslog address> { change-log info; interactive-commands info; structured-data; } file <file name> { any info; structured-data; } If the network device does not generate audit records when concurrent logons from different workstations occur, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-253937`

### Rule: The Juniper EX switch must be configured to offload audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-253937r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Archiving is not required unless space is limited in the audit server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Mark as not a finding if the site has a solution in place to prevent the device from running out of audit storage. Verify the device is configured to send system events to external syslog. If the organization has a centralized repository (or repositories) for secure transfer of audit log files, verify each log file is configured to transfer files to the appropriate repository. Each log file must be configured separately. [edit system syslog] file <file name> { any info; archive size <65536..1073741824 bytes> files <1..1000> transfer-interval <5..2880 minutes> start-time "<yyyy-mm-dd.hh:mm>" archive-sites { "URL" password "hashed PSK" } ## SECRET-DATA } Note: The URL format is: <scp|sftp>://<username>@<address>/<path>. The trailing slash is omitted because Junos automatically adds that when it appends the filename. host <external syslog address> { any info; } Note: If using secure file transfer to offload log files, the Juniper device will immediately attempt to connect with the configured protocol, address, and credentials. If successful, Junos will prompt to accept an untrusted public key. If the administrator accepts that key, Junos adds it to [edit security ssh-known-hosts]. Alternately, configure the trusted public key at [edit security ssh-known-hosts] before configuring automatic file offload. If the device does not offload audit records onto a different system or media, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-253939`

### Rule: The Juniper EX switch must be configured to generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-253939r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device generates audit log events for a locally developed list of auditable events. Verify audit logging is enabled. [edit system syslog] file <file name> { any info; } host <external syslog address> { any info; } time-format year; Note: Without the "structured-data" directive (as shown), syslog outputs in standard format. Add the "structured-data" command to all files and external syslog servers requiring that format. For example: [edit system syslog] file <file name> { any info; structured-data; } If the logging facility and level is too broad, Junos supports REGEX or string match conditions to filter events. If used, verify the match conditions capture the required events. [edit system syslog] file <file name> { any info; match <REGEX>; -or- match-strings [ "string 1" "string 2" ]; } Note: When using match conditions, it may be necessary to use the "any" (debug) severity level, but this should not generate overwhelming numbers of messages because the filter will ignore all unmatched events. If the network device is not configured to generate audit log events for a locally developed list of auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-253940`

### Rule: The Juniper EX switch must be configured to enforce access restrictions associated with changes to the system components.

**Rule ID:** `SV-253940r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, firewall filters, and policy filters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the network device to determine if only authorized administrators have permissions for changes, deletions and updates on the network device. Inspect the maintenance log to verify changes are being made only by the system administrators. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and local authentication. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. If unauthorized users are allowed to change the hardware or software, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-253941`

### Rule: The Juniper EX switch must be configured to use an authentication server for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-253941r1001014_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to verify the device is configured to use an authentication server as the primary source for authentication. Verify the RADIUS and/or TACACS+ server addresses. [edit system] radius-server { <RADIUS-1 address> secret "hashed PSK"; ## SECRET-DATA <RADIUS-2 address> secret "hashed PSK"; ## SECRET-DATA } tacplus-server { <TACPLUS-1 address> secret "hashed PSK"; ## SECRET-DATA <TACPLUS-2 address> secret "hashed PSK"; ## SECRET-DATA } Verify the authentication order places the external authentication server first. [edit system] authentication-order [ radius tacplus password ]; Note: Only the global authentication order is required; all administrative access methods will honor the global setting unless configured separately. If the network device is not configured to use an authentication server to authenticate users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-253942`

### Rule: The Juniper EX switch must be configured to conduct backups of system level information contained in the information system when changes occur.

**Rule ID:** `SV-253942r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including firewall filters that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if the device is configured to conduct backups of system-level information contained in the information system when changes occur. Verify the preferred centralized backup system is configured to retrieve the configuration file. There is no provision for backing up system binaries because Juniper provides the signed installation packages rather than individual files. Therefore, verify the centralized backup solution has the appropriate installation packages for the deployed platforms. When the configuration file is pulled from the centralized server, an example retrieval method is authenticated connections over NETCONF or manual retrieval using SSH. Junos supports authenticating external services via RADIUS or TACACS+, or via a local account. [edit system services netconf] ssh; rfc-compliant; Note: The rfc command is recommended for compatibility in large enterprises, but can be omitted if there are overriding operational considerations. If the network device will be saving system files to a centralized repository, verify the configuration file is automatically saved at each commit. [edit system archival] configuration { transfer-on-commit; archive-sites { "sftp://user@host/configuration_files" password "$9$w52...<snip>...mfzn/"; ## SECRET-DATA } } Note: The URL uses <scp|sftp>://<username>@<repository address>/<path without trailing slash (/)> format because Junos appends the slash with the system-generated filename. Junos supports file transfer either on commit, or at configured intervals. If the network device is not configured to conduct backups of system-level data when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-253943`

### Rule: The Juniper EX switch must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-253943r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device obtains public key certificates from an appropriate certificate policy through an approved service provider. Verify the certificate is signed by an approved CA via the "show security pki local-certificate" or "show security pki local-certificate detail" commands. If the network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-253944`

### Rule: The Juniper EX switch must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-253944r1028872_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. Information stored in one location is vulnerable to accidental or incidental deletion or alteration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify that the network device is configured to send log data to a redundant central log servers. 2. Verify the external syslog server is configured. The lowest severity level, "any", is debug and will generate a significant number of messages. [edit system syslog] host <external syslog address> { any info; structured-format; << Only if structured formatting is required, otherwise events are recorded in standard format. } time-format year; If the network device is not configured to send log data to redundant log servers, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-253945`

### Rule: The Juniper EX switch must be configured with an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-253945r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the network device is in compliance with this requirement. The currently running version is displayed at login and can be displayed at any time by running the "show version" (or "show version local" depending upon platform) command. If the network device is not running an operating system release that is currently supported by the vendor, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-253946`

### Rule: The Juniper EX switch must change credentials for account of last resort when administrators who know the credential leave the organization.

**Rule ID:** `SV-253946r1018771_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples of credentials include passwords and group membership certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the site's SSP to verify the password for the account of last resort and the root account are changed when a system administrator with knowledge of the password leaves or no longer has a need to know/access. If the credentials for account of last resort are not changed when administrators who know the credential leave the organization, this is a finding.

## Group: SRG-APP-000340-NDM-000288

**Group ID:** `V-253947`

### Rule: The Juniper EX switch must prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures.

**Rule ID:** `SV-253947r961353_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals that do not possess appropriate authorizations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the network device is configured to use a AAA service account, and the AAA broker is configured to assign authorization levels based on centralized user account group memberships on behalf of the network device, that will satisfy this objective. Because the responsibility for meeting this objective is transferred to the AAA broker, this requirement is not applicable for the local network device. This requirement may be verified by demonstration or configuration review. Juniper switches use role-based access controls (RBAC) to assign privilege levels. Account definitions in Junos are either "local" or "template", discriminated by the presence of an authentication stanza. Local accounts have an authentication stanza and support both external and/or local authentication depending upon the authentication order. Template accounts do not have an authentication stanza and only support external authentication. Every account (local and template) must be assigned a login class by an authorized administrator. Verify each account is assigned a login class with appropriate permissions based upon organizational requirements. Login classes support optional allow- and deny- directives as shown in the examples. Organizational requirements may require different allow- and deny- directives, or no directives at all. [edit system login] class <name> { idle-timeout 10; permissions all; deny-commands "^clear (log|security log)|^(clear|show) security alarms alarm-type idp|^request (security|system set-encryption-key|system firmware upgrade re|system decrypt)|^rollback"; deny-configuration-regexps [ "security alarms potential-violation idp" "security (ike|ipsec) (policy|proposal)" "security ipsec ^vpn$ .* manual (authentication|encryption|protocol|spi)" "security log" "system fips self-test after-key-generation" "system (archival|syslog|root-authentication|authentication-order|master-password)" "system services ssh (protocol-version|root-login)" "system login password" "system login user [a-zA-Z0-9_-]+ (authentication|class)" "system login class [a-zA-Z0-9_-]+ (permissions|deny-|allow-)" ]; } class <name-1> { idle-timeout 10; permissions [ configure maintenance security system-control trace view-configuration ]; allow-commands "^clear (log|security log)|^show cli authorization"; deny-commands "^clear (security alarms|system login lockout)|^file (copy|delete|list|rename|show)|^request (security|system set-encryption-key|system firmware upgrade re)|^rollback|^set date|^show security (alarms|dynamic-policies|match-policies|policies)|^start shell|^request system (decrypt|halt|reboot|software|zeroize)"; deny-configuration-regexps [ "system (login|internet-options|scripts|services|time-zone|^[a-r]+)" "security services event-options" ]; security-role audit-administrator; } Example local and template accounts: user <account of last resort> { uid 2000; class <name>; authentication { encrypted-password "$6$HEQnJP/W$/QD...<snip>...5r./"; ## SECRET-DATA } } user <account name> { uid 2015; class <name-1>; } Note: Accounts without an authentication stanza are template accounts, must be externally authenticated, and cannot log in locally. Verify the network device is configured to assign appropriate user roles or access levels to authenticated users. This requirement may be verified by demonstration or configuration review. If the Juniper EX switch does not prevent nonprivileged users from executing privileged functions to include disabling, circumventing, or altering implemented security safeguards/countermeasures, this is a finding.

