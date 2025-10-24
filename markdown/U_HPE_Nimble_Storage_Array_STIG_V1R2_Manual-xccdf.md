# STIG Benchmark: HPE Nimble Storage Array NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000003-NDM-000202

**Group ID:** `V-252186`

### Rule: The HPE Nimble must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-252186r879513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary network device or administrator-initiated action taken when the administrator stops work but does not log out of the network device. Rather than relying on the user to manually lock their management session prior to vacating the vicinity, network devices need to be able to identify when a management session has idled and take action to initiate the session lock. Once invoked, the session lock must remain in place until the administrator reauthenticates. No other system activity aside from reauthentication must unlock the management session. Note that CCI-001133 requires that administrative network sessions be disconnected after 10 minutes of idle time. So this requirement may only apply to local administrative sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "group --info | grep inactivity" and review the timeout value. If it is greater than 15 minutes, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-252187`

### Rule: The HPE Nimble must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-252187r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Number of authentication attempts". If the value is 2 or less, this is not a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-252188`

### Rule: The HPE Nimble must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-252188r879547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt a login to NimOS by typing "ssh username@array", where username is a valid user, and array is an array DNS name. If the correct DoD banner is not displayed before a password prompt, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-252189`

### Rule: The HPE Nimble must not have any default manufacturer passwords when deployed.

**Rule ID:** `SV-252189r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or are easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to login using SSH to a configured array using username "admin" and password "admin". If the login is successful, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-252190`

### Rule: The HPE Nimble must enforce a minimum 15-character password length.

**Rule ID:** `SV-252190r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum Length". If it is 15 or more, this is not a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-252191`

### Rule: The HPE Nimble must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-252191r879603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum Uppercase characters". If it is 1 or more, this is not a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-252192`

### Rule: The HPE Nimble must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-252192r879604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum Lowercase characters". If it is 1 or more, this is not a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-252193`

### Rule: The HPE Nimble must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-252193r879605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum Digits". If it is 1 or more, this is not a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-252194`

### Rule: The HPE Nimble must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-252194r879606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum Special characters". If it is 1 or more, this is not a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-252195`

### Rule: The HPE Nimble must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-252195r879607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "userpolicy --info" and review output for line: "Minimum number of characters change from previous password". If it is 8 or more, this is not a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-252196`

### Rule: The HPE Nimble must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity.

**Rule ID:** `SV-252196r916342_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "group --info | grep inactivity" and review the timeout value. If it is greater than 10 minutes, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-252197`

### Rule: The HPE Nimble must be configured to use an authentication server for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-252197r916111_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the command "userauth --list". If the output is "No domains configured", this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-252198`

### Rule: The HPE Nimble must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-252198r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "cert --list". Review the output to confirm that the custom-ca and custom certificates exist, and the "Use" values specified for HTTPS and APIS are both "custom". If not, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-252199`

### Rule: The HPE Nimble must forward critical alerts (at a minimum) to the system administrators and the ISSO.

**Rule ID:** `SV-252199r916114_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Alerts are essential to let the system administrators and security personnel know immediately of issues which may impact the system or users. If these alerts are also sent to the syslog, this information is used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat. Alerts are identifiers about specific actions that occur on a group of arrays. There are several ways to meet this requirement. The Nimble can be configured for forward alerts from groups to a secure Simple Mail Transfer Protocol (SMTP) server. The alert may also be sent to the syslog server and the syslog configured to send the alert to the appropriate personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "group --info | grep -i syslog" and review the output lines. The "Syslogd enabled" value should be "Yes", and the "Syslogd server" and "Syslogd port" values should contain the correct syslog server and port values. If not, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-252200`

### Rule: The HPE Nimble must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-252200r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to https://infosight.hpe.com using HPE Passport credentials. Click on the Main Menu icon in the upper left corner. Select Resources >> Alletra 6000, Nimble Storage >> Documentation. Determine current array OS version using User Interface (UI). Refer to Nimble "GUI Administration Guide" Version: NOS 5.2.x, section "Hardware and Software Updates", subsection "Find the Array OS Version" to determine the version of the OS that is currently in use by the array. Determine available array OS update versions using InfoSight. *Any version of Nimble OS software greater than the "current array OS version" might qualify to be an update to the "current array OS version". The option exists to bypass several releases to come up to the newest available release depending upon requirements. *Call HPE Support with any questions about choosing an appropriate release or the process to upgrade a release. - Follow above instructions to log in to HPE InfoSight. - Choose a "Software Version" from the left panel equal to or greater than the current array OS version. For example, 5.2.x would be equal to the current version and 5.3.x would be greater than the current version. - Open the Release Notes document for each version that is greater than the current array OS version. For example, "NimbleOS Release Notes Version NOS 5.2.1.700" is greater than NOS 5.2.1.600. - Review the entire release notes document. - Determine if this is a release should be used for an upgrade. - Confirm that the "From Version", for example 5.2.1.600, can be used to go to the version for which the release notes are applicable; for example 5.2.1.700. If the operating system version is no longer supported by the vendor, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-252201`

### Rule: The HPE Nimble must limit the number of concurrent sessions to an organization-defined number for each administrator account.

**Rule ID:** `SV-252201r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions. The product contains the ability to limit the number of total sessions, but not by individual user or user type.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that in Administration >> Security Policies page in the UI, "Unlimited" for the number of sessions is unchecked and a limit is specified. If a limit is not specified, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-252202`

### Rule: The HPE Nimble must be configured to synchronize internal information system clocks using an authoritative time source.

**Rule ID:** `SV-252202r879746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To Determine if the HPE Nimble Array is configured to synchronize internal information system clocks with the primary NTP server: ArrayA:/# ntpq ntpq> sysinfo associd=0 status=0615 leap_none, sync_ntp, 1 event, clock_sync, system peer: cxo-nmbldc-01.nimblestorage.com:123 system peer mode: client leap indicator: 00 stratum: 4 log2 precision: -24 root delay: 37.321 root dispersion: 265.639 reference ID: 10.157.24.95 reference time: e509b178.9f897118 Thu, Oct 7 2021 11:48:40.623 system jitter: 0.000000 clock jitter: 0.673 clock wander: 0.003 broadcast delay: -50.000 symm. auth. delay: 0.000 If the HPE Storage Array is not configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-252203`

### Rule: The HPE Nimble must configure a syslog server onto a different system or media than the system being audited.

**Rule ID:** `SV-252203r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. UDP is used to communicate between the array group and the syslog server (SSL is not supported at this time). This is an issue because DoD requires the use of TCP. One syslog message is generated for each alert and audit log message. Alert severity types include INFO, WARN, and ERROR.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Type "group --info | grep -i syslog" and review the output lines. The "Syslogd enabled" value should be "Yes", and the "Syslogd server" and "Syslogd port" values should contain the correct syslog server and port values. If not, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-252902`

### Rule: HPE Nimble must be configured to disable HPE InfoSight.

**Rule ID:** `SV-252902r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD requires that the Mission Owner uses only the cloud services offering listed in either the FedRAMP or DISA PA DoD Cloud Catalog to host Unclassified, public-releasable, DoD information. HPE InfoSight data collection is disabled by default in the HPE Nimble. Users must not enable it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Administration >> Alerts and Monitoring page of the storage array management interface. Verify the checkbox is not checked. If HPE InfoSight is enabled, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-259800`

### Rule: HPE Nimble must not be configured to use "HPE Greenlake: Data Services Cloud Console".

**Rule ID:** `SV-259800r944374_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD requires that the Mission Owner uses only the cloud services offering listed in either the FedRAMP or DISA PA DOD Cloud Catalog to host Unclassified, public-releasable, DOD information. Management by "HPE Greenlake: Data Services Cloud Console" is disabled by default for HPE Nimble and must not be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure cloud console is disabled. Type "group --info |grep -i "cloud enabled". If the response is "cloud enabled: Yes", this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-259801`

### Rule: HPE Alletra 5000/6000 must be configured to disable management by "HPE Greenlake: Data Services Cloud Console".

**Rule ID:** `SV-259801r944975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD requires that the Mission Owner uses only the cloud services offering listed in either the FedRAMP or DISA PA DOD Cloud Catalog to host Unclassified, public-releasable, DOD information.  Management by "HPE Greenlake: Data Services Cloud Console" is enabled by default for HPE Alletra and must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify cloud console is disabled. Type "group --info |grep -i "cloud enabled". If the response is "cloud enabled: Yes", this is a finding.

