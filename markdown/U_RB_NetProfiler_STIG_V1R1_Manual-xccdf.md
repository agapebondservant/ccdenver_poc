# STIG Benchmark: Riverbed NetProfiler Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-256071`

### Rule: The Riverbed NetProfiler must be configured to limit the number of concurrent sessions to one for the locally defined administrator account.

**Rule ID:** `SV-256071r882721_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DOS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click "Settings". Check under "Log-in Settings". If the "Allow only one log-in per user name/password combination" box is not checked, this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-256072`

### Rule: The Riverbed NetProfiler must be configured to automatically generate DOD-required audit records with sufficient information to support incident reporting to a central log server.

**Rule ID:** `SV-256072r882724_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Auditing can be disabled in the NetProfiler. The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. Upon gaining access to a network device, an attacker often attempts to create or change accounts to ensure continued access. Audit records and alerts with sufficient information to provide the information system security officer (ISSO) with forensic information about the incident can alert administrators to an ongoing attack attempt. The Riverbed NetProfiler audit log generates sufficient information by default to fulfill DOD requirements when the audit setting "Log all Audit Events" is selected. Sites may also fine-tune using the "Log custom set of audit events" and selecting applicable settings; however, this method may fail to capture all required audit records. Satisfies: SRG-APP-000026-NDM-000208, SRG-APP-000516-NDM-000350, SRG-APP-000027-NDM-000209, SRG-APP-000028-NDM-000210, SRG-APP-000029-NDM-000211, SRG-APP-000092-NDM-000224, SRG-APP-000095-NDM-000225, SRG-APP-000096-NDM-000226, SRG-APP-000097-NDM-000227, SRG-APP-000098-NDM-000228, SRG-APP-000099-NDM-000229, SRG-APP-000100-NDM-000230, SRG-APP-000101-NDM-000231, SRG-APP-000381-NDM-000305, SRG-APP-000080-NDM-000220, SRG-APP-000091-NDM-000223, SRG-APP-000343-NDM-000289, SRG-APP-000495-NDM-000318, SRG-APP-000499-NDM-000319, SRG-APP-000503-NDM-000320, SRG-APP-000504-NDM-000321</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enable all DOD-required audit requirements, including changes to user accounts and use of privileged functions. Go to Administration >> Audit Trail. Click "Audit Settings". Check under "Logging Settings". If "Log all Audit Events" is not selected, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-256073`

### Rule: The Riverbed NetProfiler must enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 30 minutes, at a minimum.

**Rule ID:** `SV-256073r882727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. in NetProfiler, the default "Number of log-in attempts before account is locked" is 3, and the default "Number of minutes to keep account locked" is 30.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click "Settings". Check under "Log-in Settings". If the "Number of log-in attempts before an account is locked" is not set to "3", and the "Number of minutes to keep account locked" is not set to "30", this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-256074`

### Rule: The Riverbed NetProfiler must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-256074r882730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click "Settings". Check under "Log-in Settings". Verify the following verbiage is used exactly as displayed with spacing and syntax as depicted in DTM-08-060: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the "Log-in splash screen display" is not set to display the Standard Mandatory DOD Notice and Consent Banner on the login screen exactly in the format required by DOD, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-256075`

### Rule: The Riverbed NetProfiler must be configured to retain the Standard Mandatory DOD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-256075r882733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The administrator must acknowledge the banner prior to the device allowing the administrator access to the network device. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the administrator does not acknowledge the consent banner, DOD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of CLI access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, and then entering the password is also acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click "Settings". Check under "Log-in Settings". If the "Log-in splash screen display" is not set to "Show until Acknowledged", this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-256076`

### Rule: The Riverbed NetProfiler must change the default admin credentials so they do not use the default manufacturer passwords when deployed.

**Rule ID:** `SV-256076r882736_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device. By default, NetProfiler provides a single user account and password: The user name is admin with a weak default password. This user account is assigned the built-in role of Administrator, which provides the admin user account with unrestricted access to all NetProfiler features and data. At a minimum, change the default password to something less obvious and more complex. The default password is provided solely to enable logging in to the system and changing the configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log in to the NetProfiler web user interface using the default "admin" user account and password. Work with the site representative to verify the root and mazu passwords have been changed to DOD-compliant passwords and stored securely with limited access. If the admin, root, or mazu passwords have not been changed, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-256077`

### Rule: The Riverbed NetProfiler must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-256077r882739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, it must be documented and approved. NOTE: Configuration of the network firewall is out of scope for this STIG. However, the network firewall must be configured to ONLY allow the following ports to the Riverbed NetProfiler. - TCP/22 – (SSH) Used for secure shell access to SteelCentral software components and for the appliance to obtain information from servers via scripts. - TCP/443 – Used to secure web-based management interfaces. - TCP/8443 – Used for exchange of encryption certificates between SteelCentral products. - TCP/41017 – Used for encrypted communication between NetProfiler and Flow Gateway, NetShark, and AppResponse appliances. - TCP/5432 – (ODBC) Enable this port if plans are to enable other applications' access to the NetProfiler internal database via ODBC. - TCP/42999 – Enable traffic on this port if the intent is to use the NetProfiler user identification feature with a Microsoft Active Directory domain controller. - UDP/123 – (NTP) Used for synchronization of time between a Flow Gateway and NetProfiler. - UDP/161 – (SNMP) Used by the NetProfiler or Flow Gateway to obtain interface information from switches, routers, firewalls, SteelHeads, and any sFlow or Netflow sources. Also, management systems use this port to read the SteelCentral product Management Information Base (MIB). - Vulnerability scanner ports – Use of the NetProfiler vulnerability scan feature requires allowing traffic on the port the SteelCentral product uses to access the vulnerability scanner server. Obtain the vulnerability scanner server addresses and port numbers from the administrator of those systems. The default ports are: - Nessus: 1241 - nCircle: 443 - Rapid7: 3780 - Qualys: Requires external https access to qualysapi.qualys.com (Note: This is separate from qualysguard.qualys.com.) - Foundstone: 3800</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Work with the site representative to identify unnecessary and/or nonsecure functions, ports, protocols, and/or services that are enabled. If unnecessary and/or nonsecure functions, ports, protocols, and/or services are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-256078`

### Rule: The Riverbed NetProfiler must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-256078r882742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort because it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the Configuration >> Account Management >> User Accounts page. If accounts exist other than the "admin" account, this is a finding.

## Group: SRG-APP-000153-NDM-000249

**Group ID:** `V-256079`

### Rule: The Riverbed NetProfiler must be configured to authenticate each administrator prior to authorizing privileges based on roles.

**Rule ID:** `SV-256079r882745_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The lack of role-based access control could result in the immediate compromise of and unauthorized access to sensitive information. Additionally, without mapping the PKI certificate to a unique user account, the ability to determine the identities of individuals or assert nonrepudiation is lost. Individual accountability mandates that each administrator is uniquely identified. For public key infrastructure (PKI)-based authentication, the device must be configured to map validated certificates to unique user accounts. This requirement applies to accounts or roles created and managed on or by the network device. Satisfies: SRG-APP-000153-NDM-000249, SRG-APP-000119-NDM-000236, SRG-APP-000120-NDM-000237, SRG-APP-000121-NDM-000238, SRG-APP-000122-NDM-000239, SRG-APP-000123-NDM-000240, SRG-APP-000329-NDM-000287, SRG-APP-000177-NDM-000263, SRG-APP-000033-NDM-000212</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the site's System Security Plan (SSP) to determine which personnel are assigned to each NetProfiler role. Go to Administration >> Account Management >> User Accounts. Go to the Roles-Attributes Mapping section of the RADIUS, TACACS+, or SAML tab of the Configuration >> Account Management >> Remote Authentication page. If account roles are not configured, or if the roles assigned do not match the site's SSP, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-256080`

### Rule: The Riverbed NetProfiler must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-256080r882748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-APP-000164-NDM-000252, SRG-APP-000170-NDM-000329</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click the "Settings" button. Check under "Password Requirements". If "Minimum number of characters" is set not to "15", this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-256081`

### Rule: The Riverbed NetProfiler must configure the local account password to "require mixed case".

**Rule ID:** `SV-256081r882751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account. Satisfies: SRG-APP-000166-NDM-000254, SRG-APP-000167-NDM-000255</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click the "Settings" button. Check under "Password Requirements". If the "Require mixed case" rule is not checked, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-256082`

### Rule: The Riverbed NetProfiler must require that at least one special character be used.

**Rule ID:** `SV-256082r882754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> User Accounts. Click the "Settings" button. Check under "Password Requirements". If the "Require nonalphanumeric characters" rule is not checked, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-256083`

### Rule: The Riverbed NetProfiler must be configured to terminate all sessions and network connections when nonlocal device maintenance is completed.

**Rule ID:** `SV-256083r882757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a device management session or connection remains open after management is completed, it may be hijacked by an attacker and used to compromise or damage the network device. Nonlocal device management and diagnostic activities are conducted by individuals communicating through an external network (e.g., the internet) or an internal network. Logging out of NetProfiler ends the session with NetProfiler. It does not close sessions with the SAML identity provider involved with the initial authentication process or those for any other Riverbed product involved in cross-product drill downs. Therefore, it is recommended to close all browser tabs and close the browser when finished accessing NetProfiler authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask if the system administrators are trained to log out and close browsers upon finishing with management sessions. Verify the inactivity timeout is set. Go to Configuration >> Appliance Security >> Password Security. Under "Inactivity Timeout", verify the "Enable Maximum Inactivity Timeout" box is checked and the timer is set for 10 minutes. If the inactivity timeout is not enabled, and/or the timer is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-256084`

### Rule: The Riverbed NetProfiler must be configured to terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-256084r882760_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Configuration >> Appliance Security >> Password Security. Under "Inactivity Timeout", verify the "Enable Maximum Inactivity Timeout" box is checked and the timer is set for 10 minutes. If the inactivity timeout is not enabled, and/or the timer is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-256085`

### Rule: The Riverbed NetProfiler must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-256085r882763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> General Settings. Under "Time Configuration", verify that at least the IP address for both Server 1 and Server 2 has been configured. If redundant time servers have not been configured, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-256086`

### Rule: The Riverbed NetProfiler must be configured to record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-256086r882766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in UTC, a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> General Settings. Under "Time Configuration", verify the Time Zone is set to "UTC". If the Time Zone is not "UTC", this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-256087`

### Rule: The Riverbed NetProfiler must be configured to record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-256087r882769_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> General Settings. Under "Time Configuration", verify that redundant NTP servers have been configured. If NTP is not configured, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-256088`

### Rule: The Riverbed NetProfiler must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-256088r882772_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to apply the requirement only to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Appliance Security >> Security Compliance. Under "Operational Modes", verify "Strict Security Mode" is enabled. If it is not enabled, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-256089`

### Rule: The Riverbed NetProfiler must be configured to authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-256089r882775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If NTP is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> General Settings. Under "Time Configuration", verify the "Encryption" for the NTP servers is set to "SHA-1" and the Key and Index columns have a value that corresponds to each NTP server. If SHA-1 is not configured for the NTP servers, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-256090`

### Rule: The Riverbed NetProfiler must be configured to implement cryptographic mechanisms using a FIPS 140-2/140-3 validated algorithm to protect the confidentiality and integrity of all cryptographic functions.

**Rule ID:** `SV-256090r882778_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and allowing hijacking of maintenance sessions. Network devices using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms. Currently, HMAC is the only FIPS-validated algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2/140-3 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. All protocols (e.g., SNMPv3, SSHv2, NTP, HTTPS, HMAC, password authentication, remote communications, password encryption, random number/session ID generation, and other protocols and cryptograph applications/functions that require server/client authentication) are to be FIPS 140-2/140-3 validated. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers. Satisfies: SRG-APP-000412-NDM-000331, SRG-APP-000156-NDM-000250, SRG-APP-000171-NDM-000258, SRG-APP-000172-NDM-000259, SRG-APP-000179-NDM-000265, SRG-APP-000224-NDM-000270, SRG-APP-000411-NDM-000330</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Appliance Security >> Security Compliance. Check under "Operational Modes". If "FIPS 140-2 Compatible Cryptography" is not enabled, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-256091`

### Rule: The Riverbed NetProfiler must be configured to protect against known types of denial-of-service (DOS) attacks by restricting web and SSH access to the appliance.

**Rule ID:** `SV-256091r882781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DOS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DOS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DOS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DOS attacks. The security safeguards cannot be defined at the DOD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DOS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to configuration >> Appliance Security >> Password Security. Under Access >> Remote Access, verify the "Restrict Web access to" radio button and the "Restrict SSH access to" radio button are selected, and the boxes contain the authorized range of IP addresses. If this is not set, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-256092`

### Rule: The Riverbed NetProfiler must be configured to use redundant Syslog servers that are configured on a different system than the NetProfiler appliance.

**Rule ID:** `SV-256092r882784_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> General Settings. Under "Syslog", verify the entries for Server 1 Host and Server 2 Host are configured. Verify "Audit Trail" and "Events" are selected for each Syslog server. If this is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-256093`

### Rule: The Riverbed NetProfiler must be configured to use an authentication server to authenticate users prior to granting administrative access.

**Rule ID:** `SV-256093r882787_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Administration >> Account Management >> Remote Authentication. Verify that RADIUS, TACACS+, or SAML 2.0 are enabled and configured. If this is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-256094`

### Rule: The Riverbed NetProfiler must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-256094r882790_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this certification authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Configuration >> Appliance Security >> Encryption Key Management. Under the "Local Credentials" tab, look for the "Apache SSL certificate". Under the "Action" column, click the drop-down menu and select "View Certificate". Verify the Privacy Enhanced Mail (PEM) format for the certificate and key match the certification authority-provided certificate and the certificate is signed by a DOD-approved certificate authority. If this is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-256095`

### Rule: The Riverbed NetProfiler must be configured to run an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-256095r882793_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to System >> Update. Verify the current version is higher than 10.0.0 and currently supported by the vendor by checking the vendor's website (support.riverbed.com). If this is not true, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-256096`

### Rule: The Riverbed NetProfiler must be configured to conduct backups of system-level information and system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-256096r882796_rule`
**Severity:** low

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including access control lists (ACLs) that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who use this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups. The backup feature securely copies traffic and configuration information to a specified backup system. NetProfiler cannot be configured to automatically run backups, but backups can be configured and run manually via the Backup page. Manually back up the system periodically in accordance with the site System Security Plan (SSP). NetExpress packet logs and index files are not backed up. Additionally, capture jobs are not restored if the backup and restore operations are performed from a physical NetExpress to a virtual edition or vice versa. The NetProfiler uses the SSH public key to connect to a backup server for running backups. Satisfies: SRG-APP-000516-NDM-000340, SRG-APP-000516-NDM-000341</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SSP to determine the site's network device backup policy. Check the NetProfiler backup log to verify regular backups are being performed. Go to System >> Backup. View if there is a recent backup. If the site does not conduct backups of system-level information contained in the information system when changes occur, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-256097`

### Rule: The network device must terminate shared/group account credentials when members leave the group.

**Rule ID:** `SV-256097r882799_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples of credentials include passwords and group membership certificates. The “mazu” account is the local Linux OS account created and used by the NetProfiler and Flow Gateway application for ownership of application, configuration, and data files stored on the appliance. Operations such as changing appliance settings and running reports on a cluster, as well as using backup/restore functionality rely on the existence of the “mazu” user. The account is required for proper operation of the solution. However, the ability to login to this account can be disabled on the Security Compliance page, as well as firewall rules can be used to restrict the remote access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the site's System Security Plan (SSP) to verify the password for the account of last resort and/or the root account are changed when a system administrator with knowledge of the password leaves or no longer has a need to know/access. If the credentials for the account of last resort are not changed when administrators who know the credential leave the organization, this is a finding.

