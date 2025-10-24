# STIG Benchmark: Palo Alto Networks NDM Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.letterkenny.FSO.mbx.stig-customer-support-mailbox@mail.mil.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-228639`

### Rule: The Palo Alto Networks security platform must enforce the limit of three consecutive invalid logon attempts.

**Rule ID:** `SV-228639r1082941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Authentication Profile. Check the authentication profile used for the local account used for the account of last resort. If the "Failed Attempts (#)" field is not set to "3", this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-228640`

### Rule: The Palo Alto Networks security platform must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-228640r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the logon screen of the Palo Alto Networks security platform. A white text box at the bottom of the screen will contain the configured text. If it is blank (there is no white text box) or the wording is not one of the approved banners, this is a finding. This is the approved verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-228642`

### Rule: The Palo Alto Networks security platform must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-228642r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. By default, the Configuration Log contains the administrator username, client (Web or CLI), and date and time for any changes to configurations and for configuration commit actions. The System Log also shows both successful and unsuccessful attempts for configuration commit actions. The System Log and Configuration Log can be configured to send log messages by severity level to specific destinations; the Panorama management console, an SNMP console, an e-mail server, or a syslog server. Since both the System Log and Configuration Log contain information concerning the use of privileges, both must be configured to send messages to a syslog server at a minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Log Settings >> System If any severity level does not have a Syslog Profile, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-228643`

### Rule: The Palo Alto Networks security platform must produce audit log records containing information (FQDN, unique hostname, management IP address) to establish the source of events.

**Rule ID:** `SV-228643r960900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Associating information about where the source of the event occurred provides a means of investigating an attack; recognizing resource utilization or capacity thresholds; or identifying an improperly configured device. The device must have a unique hostname that can be used to identify the device; fully qualified domain name (FQDN), hostname, or management IP address is used in audit logs to identify the source of a log message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management In the "General Settings" window, if the "hostname" field does not contain a unique identifier, this is a finding. Go to Device >> Setup >> Management In the "Logging and Reporting Settings" pane, if the "Send Hostname in Syslog" does not show either "FQDN", "hostname", "ipv4-address", or "ipv6-address", this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-228645`

### Rule: The Palo Alto Networks security platform must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-228645r1043177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues. The Palo Alto Networks security platform uses a hardened operating system in which unnecessary services are not present. The device has a DNS, NTP, update, and e-mail client installed. Note that these are client applications and not servers; additionally, each has a valid purpose. However, local policy may dictate that the update service, e-mail client, and statistics (reporting) service capabilities not be used. DNS can be either "Server" or "Proxy"; both are allowed unless local policy declares otherwise. NTP and SNMP are necessary functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Services In the "Services" window, view which services are configured. Note: DNS can be either "Server" or "Proxy"; both are allowed unless local policy declares otherwise. Note: The Palo Alto Networks security platform cannot be a DNS server, only a client or proxy. NTP is a necessary service. Note: The Palo Alto Networks security platform cannot be an NTP server, only a client. Go to Device >> Setup >> Management In the "Management Interface Settings" window, view the enabled services. Note: Which management services are enabled. HTTPS, SSH, ping, and SNMP, are normally allowed. If User-ID, User-ID Syslog Listener-SSL, User-ID Syslog Listener-UDP, or HTTP OCSP is present, verify with the ISSO that this has been authorized. Go to Device >> Setup >> Operations tab>> Miscellaneous Select SNMP Setup. In the "SNMP Setup" window, check if SNMP V3 is selected. If unauthorized services are configured, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-228647`

### Rule: The Palo Alto Networks security platform must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-228647r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators. Of the three authentication protocols on the Palo Alto Networks security platform, only Kerberos is inherently replay-resistant. If LDAP is selected, TLS must also be used. If RADIUS is used, the device must be operating in FIPS mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator which form of centralized authentication server is being used. Navigate to the appropriate window to view the configured server(s). For RADIUS, go to Device >> Server Profiles >> RADIUS For LDAP, go to Device >> Server Profiles >> LDAP For Kerberos, go to Device >> Server Profiles >> Kerberos If Kerberos is used, this is a not finding. If LDAP is used, view the LDAP Server Profile; if the SSL checkbox is not checked, this is a finding. If RADIUS is used, use the command line interface to determine if the device is operating in FIPS mode. Enter the CLI command "show fips-mode" or the command show fips-cc (for more recent releases). If FIPS mode is set to "off", this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-228648`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must enforce a minimum 15-character password length.

**Rule ID:** `SV-228648r1018774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that needs to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "Minimum Length" field is not "15", this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-228650`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-228650r1018775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that needs to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "Minimum Uppercase Letters" field is not "1", this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-228651`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-228651r1018776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that needs to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "Minimum Lowercase Letters" field is not "1", this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-228652`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-228652r1018777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that needs to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "Minimum Numeric Letters" field is not "1", this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-228653`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-228653r1018778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that needs to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "Minimum Special Letters" field is not "1", this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-228654`

### Rule: If multifactor authentication is not available and passwords must be used, the Palo Alto Networks security platform must require that when a password is changed, the characters are changed in at least 8 of the positions within the password.

**Rule ID:** `SV-228654r1043189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Minimum Password Complexity" window. If the "New Password Differs by Characters" field is not "8", this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-228655`

### Rule: The Palo Alto Networks security platform must prohibit the use of unencrypted protocols for network access to privileged accounts.

**Rule ID:** `SV-228655r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management View the "Management Interface Settings" pane. If either Telnet or HTTP is listed in the "Services" field, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-228658`

### Rule: The Palo Alto Networks security platform must terminate management sessions after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-228658r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Device management sessions are normally ended by the Administrator when he or she has completed the management activity. The session termination takes place from the web client by selecting "Logout" (located at the bottom-left of the GUI window) or using the command line commands "exit" or "quit" at Operational mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management. View the "Authentication Settings" pane. If the "Idle Timeout (min)" field is not "10" or less, ask the Administrator to produce documentation signed by the Authorizing Official that the configured value exists to support mission requirements. If this documentation is not made available, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228659`

### Rule: Administrators in the role of Security Administrator,  Cryptographic Administrator, or Audit Administrator must not also have the role of Audit Administrator.

**Rule ID:** `SV-228659r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Palo Alto Networks security platform has both pre-configured and configurable Administrator roles. Administrator roles determine the functions that the administrator is permitted to perform after logging in. Roles can be assigned directly to an administrator account, or define role profiles, which specify detailed privileges, and assign those to administrator accounts. There are three preconfigured roles designed to comply with Common Criteria requirements - Security Administrator, Audit Administrator, and Cryptographic Administrator. Of the three, only the Audit Administrator can delete audit records. The Palo Alto Networks security platform can use both pre-configured and configurable Administrator roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For the roles of Security Administrator, Cryptographic Administrator, or Audit Administators, verify the same individual does not have more than one of these roles. If the Palo Alto Networks security platform has any accounts where the same person is in the role of Security Administrator, Cryptographic Administrator, or Audit Administrator, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228660`

### Rule: The Palo Alto Networks security platform must automatically lock the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded.

**Rule ID:** `SV-228660r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account. This should not be configured in Device >> Setup >> Management >> Authentication Settings; instead, an authentication profile should be configured with lockout settings of three failed attempts and a lockout time of zero minutes. The Lockout Time is the number of minutes that a user is locked out if the number of failed attempts is reached (0-60 minutes, default 0). 0 means that the lockout is in effect until it is manually unlocked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Administrators. If there is no authentication profile configured for each account (aside from the emergency administration account), this is a finding. Note which authentication profile is used for each account. Go to Device >> Authentication Profile. Check the authentication profile used for each account (noted in the previous step). If the Lockout Time is not set to "0" (zero), this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228661`

### Rule: The Palo Alto Networks security platform must generate an immediate alert when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

**Rule ID:** `SV-228661r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion. This could lead to the loss of audit information. Note that while the network device must generate the alert, notification may be done by a management server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Log Settings >> Alarms If the Traffic Log DB, Threat Log DB, Configuration Log DB, System Log DB, Alarm DB, and HIP Match Log DB fields are not "75", this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-228662`

### Rule: The Palo Alto Networks security platform must have alarms enabled.

**Rule ID:** `SV-228662r997675_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Log Settings >> Alarms. If the "Enable Alarms" box is not checked, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228663`

### Rule: The Palo Alto Networks security platform must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-228663r1018780_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Network Time Protocol (NTP) is used to synchronize the system clock of a computer to reference time source. The Palo Alto Networks security platform can be configured to use specified NTP servers. For synchronization with the NTP server(s), NTP uses a minimum polling value of 64 seconds and a maximum polling value of 1024 seconds. These minimum and maximum polling values are not configurable on the firewall.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Services. In the "Services" window, the names or IP addresses of the Primary NTP Server and Secondary NTP Server must be present. If the "Primary NTP Server" and "Secondary NTP Server" fields are blank, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228664`

### Rule: The Palo Alto Networks security platform must synchronize internal information system clocks to the authoritative time source when the time difference is greater than one second.

**Rule ID:** `SV-228664r1018781_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. The Palo Alto Networks security platform can be configured to use specified Network Time Protocol (NTP) servers. NTP is used to synchronize the system clock of a computer to reference time source. Sources outside of the configured acceptable allowance (drift) may be inaccurate. When properly configured, NTP will synchronize all participating computers to within a few milliseconds of the reference time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Services. In the "Services" window, the names or IP addresses of the Primary NTP Server and Secondary NTP Server must be present. If the "Primary NTP Server" and "Secondary NTP Server" fields are blank, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-228665`

### Rule: The Palo Alto Networks security platform must be configured to synchronize internal information system clocks with the primary and secondary time sources located in different geographic regions using redundant authoritative time sources.

**Rule ID:** `SV-228665r1018782_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region from the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Services. If there is only one NTP Server configured, this is a finding. Ask the firewall administrator where the Primary NTP Server and Secondary NTP Server are located; if they are not in different geographic regions, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-228666`

### Rule: The Palo Alto Networks security platform must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-228666r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time and must be expressed in Coordinated Universal Time (UTC), also known as Zulu time, a modern continuation of Greenwich Mean Time (GMT).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management In the "General Settings" window, if the time zone is not set to "GMT" or "UTC", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228667`

### Rule: The Palo Alto Networks security platform must accept and verify Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-228667r997687_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12 and as a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Certificate Management >> Certificates. If no DOD Certification Authority (CA) certificates and subordinate certificates are imported, this is a finding. Go to Device >> Setup >> Management. In the Authentication Settings pane, if the Certificate Profile field is blank, this is a finding. View the Certificate Profile, if it does not list the DOD CA certificates and subordinate certificates, this is a finding. If the Use OCSP checkbox is not selected, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-228669`

### Rule: The Palo Alto Networks security platform must only allow the use of secure protocols that implement cryptographic mechanisms to protect the integrity of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-228669r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. Note that HTTP OCSP is permitted to support OCSP where used. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management In the "Management Interface Settings" window, view the enabled services. Note: Which management services are enabled. If Telnet or HTTP is selected, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-228670`

### Rule: The Palo Alto Networks security platform must not use SNMP Versions 1 or 2.

**Rule ID:** `SV-228670r961557_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SNMP Versions 1 and 2 are not considered secure. Without the strong authentication and privacy that is provided by the SNMP Version 3 User-based Security Model (USM), an unauthorized user can gain access to network management information used to launch an attack against the network. SNMP Versions 1 and 2 cannot authenticate the source of a message nor can they provide encryption. Without authentication, it is possible for nonauthorized users to exercise SNMP network management functions. It is also possible for nonauthorized users to eavesdrop on management information as it passes from managed systems to the management system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Operations; in the Miscellaneous pane, select SNMP Setup. In the SNMP Setup window, check if SNMP V3 is selected. If V3 is not selected, this is a finding. Go to Device >> Server Profiles >> SNMP Trap. View the list of configured SNMP servers; if the Version is not "v3", this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-228671`

### Rule: The Palo Alto Networks security platform must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-228671r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. The Palo Alto Networks security platform has multiple log types; at a minimum, the Traffic, Threat, System, and Configuration logs must be sent to a Syslog server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view a syslog server profile, Go to Device >> Server Profiles >> Syslog If there are no Syslog Server Profiles present, this is a finding. Select each Syslog Server Profile. If no server is configured, this is a finding. View the log-forwarding profile to determine which logs are forwarded to the syslog server. Go to Objects >> Log forwarding If no Log Forwarding Profile is present, this is a finding. The "Log Forwarding Profile" window has five columns. If there are no Syslog Server Profiles present in the Syslog column for the Traffic Log Type, this is a finding. If there are no Syslog Server Profiles present for each of the severity levels of the Threat Log Type, this is a finding. Go to Device >> Log Settings >> System Logs The list of Severity levels is displayed. If any of the Severity levels does not have a configured Syslog Profile, this is a finding. Go to Device >> Log Settings >> Config Logs If the "Syslog" field is blank, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228672`

### Rule: The Palo Alto Networks security platform must use automated mechanisms to alert security personnel to threats identified by authoritative sources (e.g., CTOs) and IAW CJCSM 6510.01B.

**Rule ID:** `SV-228672r997690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CJCSM 6510.01B, "Cyber Incident Handling Program", in subsection e.(6)(c) sets forth three requirements for Cyber events detected by an automated system: If the cyber event is detected by an automated system, an alert will be sent to the POC designated for receiving such automated alerts. CC/S/A/FAs that maintain automated detection systems and sensors must ensure that a POC for receiving the alerts has been defined and that the IS configured to send alerts to that POC. The POC must then ensure that the cyber event is reviewed as part of the preliminary analysis phase and reported to the appropriate individuals if it meets the criteria for a reportable cyber event or incident. By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged on to the network device. An example of a mechanism to facilitate this would be through the utilization of SNMP traps. The Palo Alto Networks security platform can be configured to send messages to an SNMP server and to an email server as well as a Syslog server. SNMP traps can be generated for each of the five logging event types on the firewall: traffic, threat, system, hip, config. For this requirement, only the threat logs must be sent. Note that only traffic that matches an action in a rule will be logged and forwarded. In the case of traps, the messages are initiated by the firewall and sent unsolicited to the management stations. The use of email as a notification method may result in a very larger number of messages being sent and possibly overwhelming the email server as well as the POC. The use of SNMP is preferred over email in general, but organizations may want to use email in addition to SNMP for high-priority messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: The actual method is determined by the organization. Review the system/network documentation to determine who the Points of Contact are and which methods are being used. If the selected method is SNMP, verify that the device is configured. Go to Device >> Server Profiles. If no SNMP servers are configured, this is a finding. Go to Objects >> Log Forwarding. If no Log Forwarding Profile is listed, this is a finding. If the "Log Type" column does not include "Threat", this is a finding. If any Severity is not listed, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228673`

### Rule: The Palo Alto Networks security platform must employ centrally managed authentication server(s).

**Rule ID:** `SV-228673r1082978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion. Only the emergency administration account, also known as the account of last resort, can be locally configured on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the administrator which form of centralized authentication server is being used. This requirement is not applicable to the local account of last resort. Navigate to the appropriate window to view the configured server(s). For RADIUS, go to Device >> Server Profiles >> RADIUS. For LDAP, go to Device >> Server Profiles >> LDAP. For Kerberos, go to Device >> Server Profiles >> Kerberos. If there are no servers configured in the window that match the specified form of centralized authentication, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-228674`

### Rule: The Palo Alto Networks security platform must use DoD-approved PKI rather than proprietary or self-signed device certificates.

**Rule ID:** `SV-228674r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoD Instruction 8520.02, Public Key Infrastructure (PKI) and Public Key (PK) Enabling mandates that certificates must be issued by the DoD PKI or by a DoD-approved PKI for authentication, digital signature, or encryption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Certificate Management >> Certificates Installed Certificates are listed in the "Device Certificates" tab. If any of the have the name or identifier of a non-approved source in the "Issuer" field, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228675`

### Rule: The Palo Alto Networks security platform must not use Password Profiles.

**Rule ID:** `SV-228675r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password profiles override settings made in the Minimum Password Complexity window. If Password Profiles are used they can bypass password complexity requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Password Profiles If there are configured Password Profiles, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-228676`

### Rule: The Palo Alto Networks security platform must not use the default admin account password.

**Rule ID:** `SV-228676r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system. The use of a default password for any account, especially one for administrative access, can quickly lead to a compromise of the device and subsequently, the entire enclave or system. The "admin" account is intended solely for the initial setup of the device and must be disabled when the device is initially configured. The default password for this account must immediately be changed at the first login of an authorized administrator.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open a web browser at an authorized workstation and enter the management IP address of the Palo Alto Networks security platform. Use HTTP Secure (HTTPS) instead of HTTP since HTTP is disabled by default. The logon window will appear. Enter "admin" into both the "Name" and "Password" fields. If anything except the logon screen with the message "Invalid username or password" appears, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-228677`

### Rule: The Palo Alto Networks security platform must generate an audit log record when the Data Plane CPU utilization is 100%.

**Rule ID:** `SV-228677r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis. If the Data Plane CPU utilization is 100%, this may indicate an attack or simply an over-utilized device. In either case, action must be taken to identify the source of the issue and take corrective action.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management In the "Logging and Reporting Settings" pane. If the "Enable Log on High DP Load" check box is not selected, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-228678`

### Rule: The Palo Alto Networks security platform must authenticate Network Time Protocol sources.

**Rule ID:** `SV-228678r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affected scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Services In the "Services" window, the Primary NTP Server Authentication Type and Secondary NTP Server Authentication Type must be either Symmetric Key or Autokey. If the "Primary NTP Server Authentication Type" and "Secondary NTP Server Authentication Type" fields are "none", this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-268323`

### Rule: The Palo Alto device must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-268323r1084266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit must be added to the envelope as a record. Administrators must secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Device >> Administrators. Review the user list. If there is an authentication profile/user account configured (and enabled) for any account other than the emergency administration account, this is a finding.

