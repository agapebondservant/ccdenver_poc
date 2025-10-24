# STIG Benchmark: A10 Networks ADC NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-255587`

### Rule: The A10 Networks ADC must limit the number of concurrent sessions to one (1) for each administrator account and/or administrator account type.

**Rule ID:** `SV-255587r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the configuration with an output modifier to display only the phrase "multiple-auth-reject": show run | inc multiple-auth-reject If the output is blank, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255588`

### Rule: The A10 Networks ADC must enforce the limit of three consecutive invalid logon attempts.

**Rule ID:** `SV-255588r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. The A10 Networks ADC must be configured to limit the consecutive invalid logon attempts. When someone attempts to log on, but fails repeatedly, the failed logon attempts and associated "user is disabled" message will be logged. Note: The user will still be prompted up to five times, even when the account is disabled at three failed logon attempts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration. The following command shows the device configuration and filters the output on the keyword "lockout": show run | inc lockout View the output; it will contain these commands: admin lockout enable admin lockout reset-time 15 admin lockout threshold 3 If it does not, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-255589`

### Rule: The A10 Networks ADC must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-255589r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Observe someone logging onto the device. If the device does not present a DoD-approved banner, this is a finding. For the CLI, the short form of the banner is acceptable. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255590`

### Rule: The A10 Networks ADC must allow only the ISSM (or individuals or roles appointed by the ISSM) Root, Read Write, or Read Only privileges.

**Rule ID:** `SV-255590r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Administrators with Root, Read Write, or Read Only privileges can view the audit and system logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Enter the following command to view detailed information about the administrative accounts: show admin detail The output of this command will show the Access type, Privilege level, and GUI role, among other parameters. If persons other than the ISSM (or individuals or roles appointed by the ISSM) have Root, Read Write, or Read Only privileges, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-255591`

### Rule: The A10 Networks ADC must produce audit log records containing information (FQDN, unique hostname, management or loopback IP address) to establish the source of events.

**Rule ID:** `SV-255591r960900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Associating information about where the source of the event occurred provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device. When the event log or system log is written to a syslog server, the hostname is included with each record.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Observe someone logging onto the device. The prompt will appear after a successful logon. If the prompt is not a unique hostname assigned by the organization, this is a finding. Note: The device automatically includes the hostname in each Syslog message.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-255592`

### Rule: The A10 Networks ADC must have command auditing enabled.

**Rule ID:** `SV-255592r960909_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the configuration and includes an output modifier to filter on the word "audit": show run | inc audit If the output does not include "audit enable privilege", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255593`

### Rule: The A10 Networks ADC must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-255593r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Since the A10 Networks ADC can monitor connectivity to servers, it can be configured to perform a health check of the Syslog servers. When connectivity is lost or the health check fails for another reason, it can send an SNMP trap notifying authorized personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the configured Server Load Balancing instances: show run | sec slb If no Server Load Balancing instance is configured with a health check to the Syslog server, this is a finding. The following command shows the device configuration and filters the output on the string "snmp": show run | inc snmp This will include which SNMP traps the device is configured to send. If the output does not include "snmp-server enable traps slb server-down", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255594`

### Rule: The A10 Networks ADC must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-255594r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. There are two ways to meet this requirement; either by configuring the device to send the audit and event log to the syslog servers or by scheduling periodic exports of the audit and event logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement can be met by use of a syslog/audit log server if the device is configured to send logs to that server. Review the device configuration. Enter the command to view the logging policy: sho log policy If the output shows syslog hosts are configured, this not is a finding. If the output shows syslog as enabled, this is not a finding. If it is not configured to send audit and event logs to a syslog server, enter the command to view the scheduled backup of the log: show backup If the there is no backup configured, this is a finding. If the backup period is not seven days or less, this is a finding. If the last backup failed and it has been more than seven days since the last backup, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-255595`

### Rule: The A10 Networks ADC must disable management protocol access to all interfaces except the management interface.

**Rule ID:** `SV-255595r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command displays the types of management access allowed on each of the device's interfaces: show management If SSH, Telnet, HTTP, HTTPS, or SNMP is "on" for any of the interfaces other than the management interface, this is a finding. Note: Ping may be used on inward-facing interfaces.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255596`

### Rule: The A10 Networks ADC must not have any shared accounts (other than the emergency administration account).

**Rule ID:** `SV-255596r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system. This means that there must be no shared accounts. The only exception is for the emergency administration account. Note: The number of emergency administration accounts is restricted to at least one, but no more than operationally required as determined by the ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Enter the following command to view all administrative accounts: show admin detail If there are any shared accounts other than the emergency administration account, this is a finding. Obtain the list of accounts configured on the authentication server. If there are any shared accounts other than the emergency administration account, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255597`

### Rule: The A10 Networks ADC must not use the default admin account.

**Rule ID:** `SV-255597r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system. The use of a default password for any account, especially one for administrative access, can quickly lead to a compromise of the device and subsequently, the entire enclave or system. The "admin" account is intended solely for the initial setup of the device and must be disabled when the device is initially configured. The default password for this account must immediately be changed at the first logon of an authorized administrator. The ACOS device comes with one admin account, "admin", by default. The "admin" account has global Read Write privileges. The admin account, and other admin accounts with global Read Write privileges, can configure additional admin accounts. Since this account, if misused, can easily compromise the device, it must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log on to the device using the default administrator logon and password. If the logon is successful, this is a finding. Review the device configuration. The following command shows all of the configured accounts on the device: show admin If the admin account is enabled, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-255598`

### Rule: The A10 Networks ADC must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-255598r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Of the three authentication protocols for device management on the A10 Networks ADC, none are inherently replay-resistant. If LDAP or TACACS+ is selected, TLS must also be used. If RADIUS is used, the device must be a FIPS mode platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Since the device supports RADIUS, TACACS+, and LDAP, one of these must be configured. The following is a sample verification for TACACS+. The following command shows the parts of the configuration with the word "tacplus": show run | inc tacplus If the output is blank, this is a finding. The following command shows information for all configured TACACS servers: show tacacs-server If no servers are configured, this is a finding. If RADIUS is used, ask the Administrator whether or not the device is a FIPS version of the platform. This is identified by the designation "FIPS" in the stock keeping unit (SKU). The following command shows the version of ACOS used and other related information: show version If the output does not include "Platform features: fips", this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-255599`

### Rule: The A10 Networks ADC must prohibit the use of unencrypted protocols for network access to privileged accounts.

**Rule ID:** `SV-255599r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command show the types of management access allowed on each of the interfaces: show management [ipv4 | ipv6] The following command shows IPv4 management access information: show management ipv4 If either Telnet or HTTP is listed as "on" for any interface, this is a finding. The following command shows IPv6 management access information: show management ipv6 If either Telnet or HTTP is listed as "on" for any interface, this is a finding. Verify that HTTP for management is disabled. show web-service If HTTP is enabled, this is a finding. HTTPS is allowed for management and is enabled by default.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255600`

### Rule: The A10 Networks ADC must terminate management sessions after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255600r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the terminal settings: show terminal If the idle-timeout is greater than 10 minutes or is set to zero (no timeout), this is a finding. The following command shows the web management (GUI) settings: show web-service If the idle time is greater than 10 minutes or is set to zero (no timeout), this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255601`

### Rule: The A10 Networks ADC must reveal error messages only to authorized individuals (ISSO, ISSM, and SA).

**Rule ID:** `SV-255601r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state. Additionally, sensitive account information must not be revealed through error messages to unauthorized personnel or their designated representatives. In the A10 Networks ADC, the audit log is maintained in a separate file separate from the system log. Access to the audit log is role-based. The audit log messages that are displayed for an admin depend upon that administrator’s role (privilege level). Administrators with Root, Read Write, or Read Only privileges who view the audit log can view all the messages, for all system partitions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Enter the following command to view detailed information about the administrative accounts: show admin detail The output of this command will show the Access type, Privilege level, and GUI role, among other parameters. If persons other than other than the authorized individuals (ISSO, ISSM, and SA) have Root, Read Write, or Read Only privileges, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255602`

### Rule: The A10 Networks ADC must generate alerts to the administrators and ISSO when accounts are created.

**Rule ID:** `SV-255602r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. The A10 Networks ADC records in the audit log when an account is created. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. Configuring the device to forward all audit log messages to an actively monitored syslog server or SNMP management station meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The A10 Networks ADC records in the audit log when an account is created. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. This is met by sending audit log messages to the Syslog servers or SNMP management station, which is continuously monitored. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands (no log targets are configured), this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255603`

### Rule: The A10 Networks ADC must generate alerts to the administrators and ISSO when accounts are modified.

**Rule ID:** `SV-255603r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the modification of device administrator accounts and notifies administrators and Information System Security Officers (ISSO). Such a process greatly reduces the risk that accounts will be surreptitiously modified and provides logging that can be used for forensic purposes. The A10 Networks ADC records in the audit log when an account is modified. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. Configuring the device to forward all audit log messages to an actively monitored syslog server or SNMP management station meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The A10 Networks ADC records in the audit log when an account is modified. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. This is met by sending audit log messages to the Syslog servers or SNMP management station which is continuously monitored. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host". show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands (no log targets are configured), this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255604`

### Rule: The A10 Networks ADC must generate alerts to the administrators and ISSO when accounts are disabled.

**Rule ID:** `SV-255604r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are disabled, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. The A10 Networks ADC records in the audit log when an account is disabled. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. Configuring the device to forward all audit log messages to an actively monitored syslog server or SNMP management station meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The A10 Networks ADC records in the audit log when an account is disabled. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. This is met by sending audit log messages to the Syslog servers or SNMP management station, which is continuously monitored. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands (no log targets are configured), this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255605`

### Rule: The A10 Networks ADC must generate alerts to the administrators and ISSO when accounts are removed.

**Rule ID:** `SV-255605r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, administrator accessibility is affected. Accounts are utilized for identifying individual device administrators or for identifying the device processes themselves. In order to detect and respond to events that affect administrator accessibility and device processing, devices must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that device accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. The A10 Networks ADC records in the audit log when an account is removed. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. Configuring the device to forward all audit log messages to an actively monitored syslog server or SNMP management station meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The A10 Networks ADC records in the audit log when an account is removed. This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. These messages must be forwarded to the ISSO and administrators. This is met by sending audit log messages to the Syslog servers or SNMP management station, which is continuously monitored. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands (no log targets are configured), this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-255606`

### Rule: When anyone who has access to the emergency administration account no longer requires access to it or leaves the organization, the password for the emergency administration account must be changed.

**Rule ID:** `SV-255606r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples of credentials include passwords and group membership certificates. Group accounts are not allowed except for the emergency administration account, which is an account can be created on the device's local database for use in an emergency, such as when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is also referred to as the account of last resort since the emergency administration account is strictly intended to be used only as a last resort and immediate administrative access is absolutely necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of personnel who are authorized access to the emergency administration account and determine when someone either changed roles or left the organization. Compare this against the documented last change of the emergency administration account password. If the emergency administration account was not changed, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255607`

### Rule: The A10 Networks ADC must notify System Administrators (SAs) and Information System Security Officers (ISSMs) when accounts are created, or enabled when previously disabled.

**Rule ID:** `SV-255607r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies SAs and ISSMs. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect network administrator accessibility and device processing, network devices must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The A10 Networks ADC records in the audit log when an account is created (enabled). This appears as the command that created the account and contains the keyword "admin". These messages must be forwarded to the ISSO and administrators. This is met by sending audit log messages to the Syslog servers. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands (no log targets are configured), this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255608`

### Rule: The A10 Networks ADC must automatically lock the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded.

**Rule ID:** `SV-255608r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log on to an administrator account three times. On each attempt, deliberately enter an incorrect password. Attempt to log on a fourth time with a correct password. If the attempt succeeds, this is a finding. This can also be verified using the following command to view the lockout status of all administrative accounts: show admin detail If the Lock Status is not Locked, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-255609`

### Rule: The A10 Networks ADC must send Emergency messages to the Console, Syslog, and Monitor.

**Rule ID:** `SV-255609r961401_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the logging policy: show log policy If the level of logging for the Console, Syslog, and Monitor is not at least Emergency, this is a finding. Since each severity level includes the levels below it, other levels are permitted. However, the debugging level may generate too many messages when used and must be used carefully.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255610`

### Rule: The A10 Networks ADC must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-255610r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows clock information: show clock detail If the output does not show NTP as the time source, this is a finding. If a dot appears in front of the time, the device has been configured to use NTP, but NTP is not synchronized. This is also a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255611`

### Rule: The A10 Networks ADC must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-255611r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in CCI-001891 because a comparison must be done in order to determine the time difference. The organization-defined time period will depend on multiple factors, most notably the granularity of time stamps in audit logs. For example, if time stamps only show to the nearest second, there is no need to have accuracy of a tenth of a second in clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows clock information: show clock detail If the output does not show NTP as the time source, this is a finding. If a dot appears in front of the time, the device has been configured to use NTP, but NTP is not synchronized. This is also a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255612`

### Rule: The A10 Networks ADC must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-255612r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the configuration with an output modifier to display only NTP-related configuration: show run | include ntp Alternately, enter the command to display the configured NTP servers and whether or not NTP is enabled: show ntp servers If the output shows fewer than two configured NTP servers, this is a finding. Ask the device administrator where the Primary NTP Server and Secondary NTP Server are located. If they are not in different geographic regions, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-255613`

### Rule: The A10 Networks ADC must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-255613r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows clock information: show clock detail If the output does not show GMT as the time zone, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255614`

### Rule: The A10 Networks ADC must authenticate Network Time Protocol sources.

**Rule ID:** `SV-255614r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affected scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command includes an output modifier to display only NTP-related configuration: show run | include ntp The output should contain either the "ntp auth-key" command or the "ntp trusted-key" command. If it does not, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255615`

### Rule: Operators of the A10 Networks ADC must not use the Telnet client built into the device.

**Rule ID:** `SV-255615r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions. Telnet is an unsecure protocol; use SSH instead. Note: This requirement does not refer to the device accepting incoming Telnet connections (server), but instead being used as an originator of Telnet requests (client). This is the exec level command "telnet".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if any operators have used Telnet. Evidence of the use of Telnet will be in the audit log. The following command shows any instances of the word "telnet" in the audit log: show audit | inc telnet If the log shows the use of the Telnet command, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-255616`

### Rule: The A10 Networks ADC must not use SNMP Versions 1 or 2.

**Rule ID:** `SV-255616r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SNMP Versions 1 and 2 are not considered secure. Without the strong authentication and privacy that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information used to launch an attack against the network. SNMP Versions 1 and 2 cannot authenticate the source of a message nor can they provide encryption. Without authentication, it is possible for unauthorized users to exercise SNMP network management functions. It is also possible for unauthorized users to eavesdrop on management information as it passes from managed systems to the management system. The A10 Networks ADC platforms support SNMPv3. The SNMP service is disabled by default and all traps are disabled by default. SNMP and SNMP trap are disabled on all data interfaces. Use the enable-management command to enable SNMP on the management interface. The OID for A10 Networks A10 Thunder Series and AX Series objects is 1.3.6.1.4.1.22610. Note: A10 Networks devices do not support SNMP “write” commands; this reduces the risk of the device configuration being modified by SNMP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the running configuration and filters the output on the string "snmp-server": show run | inc snmp-server If the output shows servers using SNMPv1 or SNMPv2, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-255617`

### Rule: The A10 Networks ADC must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-255617r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands, this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255618`

### Rule: The A10 Networks ADC must use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and IAW CJCSM 6510.01B.

**Rule ID:** `SV-255618r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged into the network device. An example of a mechanism to facilitate this would be through the use of SNMP traps or a Syslog server where messages are sent to an SNMP console or Syslog server that is monitored by the CNDSP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a log destination is configured for a CNDSP or other mechanism that is monitored by security personnel. Obtain the IP address of a Syslog server monitored by the CNDSP. Review the device configuration. The following command shows the portion of the device configuration that includes the word "host": show run | inc host If the output does not display the "logging host" and "logging auditlog host" commands, or does not include the IP address of the Syslog server used by the CNDSP, this is a finding. The following command shows the logging policy: show log policy If Syslog logging is disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255619`

### Rule: The A10 Networks ADC must employ centrally managed authentication server(s).

**Rule ID:** `SV-255619r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. You can configure the device to use remote servers for Authentication, Authorization, and Accounting (AAA) for administrative sessions. The device supports RADIUS, TACACS+, and LDAP servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. Since the device supports RADIUS, TACACS+, and LDAP, one of these must be configured. The following is a sample verification for TACACS+. The following command shows the parts of the configuration with the word "tacplus": show run | inc tacplus If the output is blank, this is a finding. The following command shows information for all configured TACACS servers: show tacacs-server If no servers are configured, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255620`

### Rule: The A10 Networks ADC must use DoD-approved PKI rather than proprietary or self-signed device certificates.

**Rule ID:** `SV-255620r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. This can be checked using the GUI: Log on to the device and navigate to Config >> System >> Settings >> Web Certificate. In the certificate pane, view the issuer information. If each certificate is not issued by an approved service provider, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-255621`

### Rule: The A10 Networks ADC must restrict management connections to the management network.

**Rule ID:** `SV-255621r960801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote administration is inherently dangerous because anyone with a sniffer and access to the right LAN segment could acquire the device account and password information. With this intercepted information they could gain access to the infrastructure and cause denial of service attacks, intercept sensitive information, or perform other destructive actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the device administrator what the subnet assigned to the management network is and which access-list is used to restrict management traffic. Review the device configuration. The following command displays a configured access-list: show access-list [ipv4 | ipv6] [acl-id] If no access list for the management network is configured, this is a finding. If the access list for the management network does not restrict traffic solely to the management network, this is a finding. The following command displays information about the management interface: show interface management If the access list is not applied to the management interface, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255622`

### Rule: The A10 Networks ADC must only allow the use of secure protocols that implement cryptographic mechanisms to protect the integrity of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-255622r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration. The following command shows the types of management access allowed on each of the interfaces: show management [ipv4 | ipv6] The following command shows IPv4 management access information: show management ipv4 If either Telnet or HTTP is listed as "on" for any interface, this is a finding. The following command shows IPv6 management access information: show management ipv6 If either Telnet or HTTP is listed as "on" for any interface, this is a finding. Verify that HTTP for management is disabled. show web-service If HTTP is enabled, this is a finding. HTTPS is allowed for management and is enabled by default.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255623`

### Rule: The A10 Networks ADC must not use the default enable password.

**Rule ID:** `SV-255623r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system. The use of a default password for any account, especially one for administrative access, can quickly lead to a compromise of the device and subsequently, the entire enclave or system. The "admin" account is intended solely for the initial setup of the device and must be disabled when the device is initially configured. The default password for this account must immediately be changed at the first logon of an authorized administrator. The default enable password on the A10 is blank password, which can immediately be guessed and lead to a compromise. This password must be immediately set.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
After successfully logging on to the device, attempt to enter enable mode using the default (blank) password. If that is successful, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-264426`

### Rule: The A10 Networks NDM must be using a version supported by the vendor.

**Rule ID:** `SV-264426r992075_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

