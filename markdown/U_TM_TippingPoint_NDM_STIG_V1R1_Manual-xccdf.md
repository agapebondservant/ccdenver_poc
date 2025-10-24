# STIG Benchmark: Trend Micro TippingPoint NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-242231`

### Rule: The TippingPoint SMS must limit the maximum number of concurrent active sessions to one for the account of last resort.

**Rule ID:** `SV-242231r710700_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions is defined by DoD as one based on operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log in to the SMS client. 2. Select >> "Edit" >> "Preferences". Select "Security" under "Session Preferences". 3. Verify the setting for the "limit number of total and user sessions" option is checked. 4. Verify the active sessions allowed for a user option has a numeric value of 1. If the TippingPoint SMS does limit the maximum number of concurrent active sessions to one for the account of last resort, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-242232`

### Rule: The TippingPoint SMS must limit total number of user sessions for privileged uses to a maximum of 10.

**Rule ID:** `SV-242232r710703_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of currently allowed administrator sessions is a best practice that lowers the risk of DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log in to the SMS client. 2. Select >> "Edit" >> "Preferences". Select "Security" under "Session Preferences". 3. Verify the setting for the "limit number of total and user sessions" option is checked. 4. Verify the active sessions allowed on SMS option has a numeric value of 10 or less. If the TippingPoint SMS does not limit total number of user sessions for privileged uses to a maximum of 10, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-242233`

### Rule: The TippingPoint SMS must disable auto reconnect after disconnect.

**Rule ID:** `SV-242233r710706_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Requiring authentication for auto reconnecting expired administrator sessions is a best practice that lowers the risk of DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log in to the SMS client. 2. Select >> "Edit" >> "Preferences". Select "Security" Under "Client Preferences". 3. Verify the option for "Auto reconnect client to server after a disconnect occurs" is unchecked. If the TippingPoint SMS does not disable auto reconnect after disconnect, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-242234`

### Rule: The TippingPoint SMS must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-242234r710709_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the SMS client requires locking of account after three invalid login attempts. Navigate to Edit >> Preferences. If the checkbox for "Lock user after failed login attempts" is not checked, or if the threshold is not set to 3, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-242235`

### Rule: The TippingPoint SMS, TPS, and SMS client must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-242235r710712_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. Configure banner messages to display security notices on the SMS client toolbar or when a user attempts to log in to the following interfaces: SMS client, SMS web management console, CLI, or remote SSH client. When configured, the notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access, as required by CCI-000050. Satisfies: SRG-APP-000068-NDM-000215, SRG-APP-000069-NDM-000216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to present a DoD-approved banner that is formatted in accordance with DTM-08-060. Verify the SMS client has a login banner configured by viewing the SMS client toolbar, client login, web login, console/CLI, or remote/SSH login. Verify the TPS login banner is enabled: 1. Click Devices, All Devices, and the TPS Device hostname. 2. Click Device Configuration. 3. Click Login Banner. If the TippingPoint SMS, TPS, and SMS client does not display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-242236`

### Rule: The TippingPoint SMS must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-242236r710715_rule`
**Severity:** high

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS and TPS have disabled all unnecessary and insecure protocols. 1. For SMS, click Admin and Management. 2. Ensure only Ping is enabled and the SMS is in FIPS Mode. If any other services are enabled or if the SMS is not in FIPS mode, this is a finding. 3. For TPS, click Devices, All Devices, and the subject device hostname. 4. Click Device Configuration and select Services. Ensure only TLS 1.2 is enabled. 5. Under FIPS Settings ensure the FIPS Mode is selected. If any other services are enabled or if the TPS is not in FIPS mode, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-242237`

### Rule: The TippingPoint SMS must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-242237r710718_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort because it is intended to be used as a last resort, and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS has only a single local account. Select Admin >> Authentication and Authorization >> Users. If more than one user is enabled under user accounts, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-242238`

### Rule: The TippingPoint SMS must enforce a minimum 15-character password length.

**Rule ID:** `SV-242238r710721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS password complexity requirements are met. 1. Under Security, click Edit and Preferences. 2. If the security level is set to anything except "3 - High", this is a finding. This setting ensures a 15-character minimum, uppercase, lowercase, numbers, and symbols are used.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-242239`

### Rule: The TippingPoint SMS must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-242239r710724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS password complexity requirements are met. 1. Under Security, click Edit and Preferences. 2. If the security level is set to anything except "3 - High", this is a finding. This setting ensures a 15-character minimum, uppercase, lowercase, numbers, and symbols are used.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-242240`

### Rule: The TippingPoint SMS must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-242240r710727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS password complexity requirements are met. 1. Under Security, click Edit and Preferences. 2. If the security level is set to anything except "3 - High", this is a finding. This setting ensures a 15-character minimum, uppercase, lowercase, numbers, and symbols are used.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-242241`

### Rule: The TippingPoint SMS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-242241r710730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS password complexity requirements are met. 1. Under Security, click Edit and Preferences. 2. If the security level is set to anything except "3 - High", this is a finding. This setting ensures a 15-character minimum, uppercase, lowercase, numbers, and symbols are used.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-242242`

### Rule: The TippingPoint SMS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-242242r710733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS password complexity requirements are met. 1. Under Security, click Edit and Preferences. 2. If the security level is set to anything except "3 - High", this is a finding. This setting ensures a 15-character minimum, uppercase, lowercase, numbers, and symbols are used.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-242243`

### Rule: The TippingPoint TPS must have FIPS Mode enforced.

**Rule ID:** `SV-242243r754439_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, verify the TPS FIPS Mode is enabled. 1. For TPS, click Devices, All Devices, and the subject device hostname. 2. Click FIPS Settings and ensure the FIPS Mode is selected. If the TPS is not in FIPS mode, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-242244`

### Rule: The TippingPoint SMS must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-242244r754440_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the SMS inactivity timeouts are configured. 1. Under Security, click Edit and Preferences. 2. Under Client Preferences, if "Timeout client session after inactivity" is not checked or the Time is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-242245`

### Rule: The Trend Micro SMS must generate an alert for all audit failure events requiring real-time alerts.

**Rule ID:** `SV-242245r710742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure a SNMPv3 trap destination is configured. 1. Navigate to Admin >> Server Properties >> SNMP. 2. View the NMS configuration. If an NMS Trap Destination is not configured, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-242246`

### Rule: The TippingPoint SMS must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-242246r710745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure two NTP sources are configured. 1. Select Admin, Server Properties, and Network. 2. If Enable NTP is not checked or at least two NTP servers are not configured under Date/Time, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-242247`

### Rule: The TippingPoint SMS must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-242247r710748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the GMT/UTC time zone is configured. 1. Select Admin, Server Properties, and Network. 2. If a time zone other than UTC is selected, this is a finding.

## Group: SRG-APP-000380-NDM-000304

**Group ID:** `V-242248`

### Rule: The TippingPoint SMS must enforce access restrictions associated with changes to device configuration.

**Rule ID:** `SV-242248r710751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to device configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the device can potentially have significant effects on the overall security of the device. Accordingly, only qualified and authorized individuals should be allowed to obtain access to device components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the Trend Micro TippingPoint system, ensure the SMS client is using CAC authentication and LDAPS authorization. 1. Log in to the SMS client. 2. Navigate to Authentication and Authorization >> Authentication. If "Use CAC authentication" is not selected, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-242249`

### Rule: The TippingPoint SMS must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-242249r710754_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure a SNMPv3 trap destination and SNMPv3 Requests are configured. 1. Select Admin and Server Properties. 2. Select SNMP. If an NMS Trap Destination is not configured, or if SNMPv3 requests are not configured, or if the SNMPv3 protocol does not use as least AES-128 for privacy and SHA1 for authentication, then this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-242250`

### Rule: The TippingPoint SMS must authenticate Network Time Protocol sources using authentication that is cryptographically based.

**Rule ID:** `SV-242250r710757_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure NTP authentication is enabled. 1. Log in to the serial console or ESXi virtual console. 2. Run the command ntp-auth. If NTP auth is not enabled for client and server, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-242251`

### Rule: The TippingPoint TPS must have FIPS mode enforced.

**Rule ID:** `SV-242251r754441_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Satisfies: SRG-APP-000411-NDM-000330, SRG-APP-000412-NDM-000331</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client: 1. Click Admin and Management. 2. Ensure the SMS is in FIPS Mode. If the SMS is not in FIPS mode, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-242252`

### Rule: The TippingPoint SMS must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-242252r710763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, verify the SMS and TPS have DoS protections enabled. 1. Navigate to Devices and select the SMS hostname. 2. Select Device Configuration >> Select Host IP filters. If no filters exist or the default action is set to "allow", this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-242253`

### Rule: The TippingPoint SMS must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-242253r710766_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the remote system is configured to generate all audit records. 1. Navigate to Admin >> Server properties >> Syslog. 2. Verify the configuration enables TCP. 3. Verify Device Audit, Device System, SMS Audit, and SMS System log types are enabled and configured. If syslog is not configured to use TCP or does not include the four log types, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-242254`

### Rule: The TippingPoint SMS must be configured to use an authentication server for the purpose of authenticating users prior to granting administrative access and to enforce access restrictions.

**Rule ID:** `SV-242254r754442_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device. Satisfies: SRG-APP-000516-NDM-000336, SRG-APP-000516-NDM-000335, SRG-APP-000033-NDM-000212, SRG-APP-000038-NDM-000213, SRG-APP-000153-NDM-000249, SRG-APP-000329-NDM-000287 SRG-APP-000156-NDM-000250, SRG-APP-000340-NDM-000288, SRG-APP-000380-NDM-000304, SRG-APP-000408-NDM-000314</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Configure the Trend Micro TippingPoint system to ensure the SMS client is using CAC authentication and LDAPS authorization. 1. Log in to the SMS client. 2. Click on Authentication and Authorization. 3. Click authentication. 4. Ensure "Use CAC authentication" is currently selected. If the TippingPoint SMS is not configured to use an authentication server for the purpose of authenticating users prior to granting administrative access, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-242255`

### Rule: The TippingPoint SMS must be configured to conduct backups of system level information contained in the information system when changes occur.

**Rule ID:** `SV-242255r710772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure backups are enabled and scheduled. 1. Select Admin >> Database >> Backup. 2. If no scheduled backup is configured, or if the backup is not configured at least weekly, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-242256`

### Rule: The TippingPoint SMS must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-242256r710775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure backups are enabled and scheduled. 1. Select Admin >> Database >> Backup. 2. If no scheduled backup is configured, or if the backup is not configured at least weekly then this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-242257`

### Rule: The TippingPoint SMS must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-242257r710778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the certificate is signed by an authorized DoD Certificate Authority. Select Admin >> Certificate Management >> Certificates. If there is no certificate, or the certificate is signed by a CA that is not authorized in the DoD, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-242258`

### Rule: The TippingPoint SMS must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-242258r710781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the operating system version under devices and version in the SMS Software under Admin and General is still under security support by Trend Micro on the https://tmc.tippingpoint.com/TMC/ support website. If the operating system version is not under support, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-242259`

### Rule: The TippingPoint SMS must automatically generate audit records for account changes and actions with containing information needed for analysis of the event that occurred on the SMS and TPS.

**Rule ID:** `SV-242259r754443_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Auditing account changes provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. Associating event types, date/time of the event, identity of any individual or process associated with the event, source/destination of the event, location of the event, and the outcome of the event provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured network device. Satisfies: SRG-APP-000026-NDM-000208, SRG-APP-000027-NDM-000209, SRG-APP-000028-NDM-000210, SRG-APP-000029-NDM-000211, SRG-APP-000319-NDM-000283, SRG-APP-000091-NDM-000223, SRG-APP-000095-NDM-000225, SRG-APP-000096-NDM-000226, SRG-APP-000097-NDM-000227, SRG-APP-000099-NDM-000229, SRG-APP-000100-NDM-000230, SRG-APP-000100-NDM-000231, SRG-APP-000100-NDM-000289, SRG-APP-000100-NDM-000305, SRG-APP-000100-NDM-000318, SRG-APP-000100-NDM-000319, SRG-APP-000100-NDM-000321, SRG-APP-000100-NDM-000325, SRG-APP-000100-NDM-000334, SRG-APP-000100-NDM-000250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the SMS client, ensure the remote system is configured to generate all audit records. 1. Navigate to Admin >> Server properties >> Syslog. 2. Verify the configuration enables TCP. 3. Verify Device Audit, Device System, SMS Audit, and SMS System log types are enabled and configured. If syslog is not configured to use TCP or does not include the four log types, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-242260`

### Rule: The password for the local account of last resort and the device password (if configured) must be changed when members who had access to the password leave the role and are no longer authorized access.

**Rule ID:** `SV-242260r710787_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the local representative show password change logs or documentation to show this is a local process. If the password for the local account of last resort is not changed when members who had access to the password leave the role and are no longer authorized access, this is a finding.

