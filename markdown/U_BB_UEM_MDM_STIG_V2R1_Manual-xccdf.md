# STIG Benchmark: BlackBerry UEM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-412000

**Group ID:** `V-224371`

### Rule: The BlackBerry UEM server must [selection: invoke platform-provided functionality, implement functionality] to generate an audit record of the following auditable events: c. [selection: Commands issued to the MDM Agent].

**Rule ID:** `SV-224371r604136_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. For audit logs to be useful, administrators must have the ability to view them. SFR ID: FAU_GEN.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the audit record which can be found in the UEM console in Settings >> Infrastructure >> Audit settings >> Security event audit settings section. Verify both "Command" events are listed and "setting" is set to "All" for the "Command delivered" event. If both "Command" events are not listed and "setting" is not set to "All" for the "Command delivered" event, this is a finding.

## Group: PP-MDM-411009

**Group ID:** `V-224372`

### Rule: The BlackBerry UEM server must be configured to communicate the following commands to the MDM Agent: read audit logs kept by the MD.

**Rule ID:** `SV-224372r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. For audit logs to be useful, administrators must have the ability to view them. SFR ID: FMT_SMF.1.1(1) #19</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each Android device being managed by UEM has been configured to enable device auditing. Verify the policy pushed by UEM to each Android device include "Enable auditing". If auditing has not been enabled for each Android device being managed by UEM, this is a finding.

## Group: PP-MDM-411047

**Group ID:** `V-224374`

### Rule: The BlackBerry UEM server or platform must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-224374r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to leaving the vicinity, applications must be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead. SFR ID: FMT_SMF.1.1(2) c.8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server configuration to determine whether the system is locked after 15 minutes. Have the system administrator log into the console. Verify the session locks after 15 minutes of inactivity. If the "Session timeout" is not set correctly, this is a finding.

## Group: PP-MDM-411054

**Group ID:** `V-224375`

### Rule: The BlackBerry UEM server must be configured to transfer BlackBerry UEM server logs to another server for storage, analysis, and reporting. 

Note: BlackBerry UEM server logs include logs of MDM events and logs transferred to the BlackBerry UEM server by MDM agents of managed devices.

**Rule ID:** `SV-224375r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the BlackBerry UEM server has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the BlackBerry UEM server must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) c.8, FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Syslog audit records from the syslog audit management server and verify UEM logs are included. If UEM logs are not found on the Syslog server, this is a finding.

## Group: PP-MDM-411056

**Group ID:** `V-224376`

### Rule: The BlackBerry UEM server must be configured to display the required DoD warning banner upon administrator logon. 

Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-224376r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the BlackBerry UEM server or BlackBerry UEM server platform. Before granting access to the system, the BlackBerry UEM server/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) c.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server documentation and configuration settings to determine if the warning banner is using the appropriate designated wording. On the BlackBerry UEM, do the following: 1. Log in to the BlackBerry UEM console. 2. Select the "Settings" tab on the left pane. 3. Expand the "General" settings tab on the left pane. 4. Select "Login notices" from the menu in the left pane. 5. Verify the checkbox next to "Enable a login notice for the management console" is checked. 6. Verify the console logon notice text exactly matches the VulDiscussion text. 7. Verify the checkbox next to "Enable a login notice for the self-service console" is checked if the self-service portal is used at the site. 8. Verify the self-service console logon notice text exactly matches the VulDiscussion text. Alternately, have the administrator log in to the UEM console to view the warning banner. If the console notice wording does not exactly match the VulDiscussion text, this is a finding.

## Group: PP-MDM-411058

**Group ID:** `V-224377`

### Rule: The BlackBerry UEM server must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, or auditor.

**Rule ID:** `SV-224377r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the BlackBerry UEM server supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining which apps user groups or individual users have access to in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server configuration settings. Verify the server is configured with the "Administrator" roles: a. UEM Security Administrator; b. Auditor; c. One or more Site Custom Administrator or UEM predefined enterprise/help desk roles. Note: The exact name of the role is not important. Each role should include functions close to the role descriptions listed in the VulDiscussion. Note: The intent of the requirement is that separate people perform each administrator role; few users are assigned to the "UEM Security Administrator" role; the "auditor" role is limited to only authorized permissions; and day-to-day management of user accounts, group accounts, and profiles are performed from site-specific custom administrator roles or UEM predefined enterprise/help desk roles instead of the "UEM Security Administrator". On the BlackBerry UEM, do the following: 1. Log in to the BlackBerry UEM console. 2. Select the "Settings" tab at the top of the screen. 3. Expand the "General" settings tab on the left pane. 4. Expand the "Administrators" tab on the left pane. 5. Select the "Roles" tab on the left pane. 6. Verify at least one user is assigned to each of the following roles: a. UEM Security Administrator; b. Auditor; c. One or more Site Custom Administrator or UEM predefined enterprise/help desk roles. Verify the auditor role function is limited to only reviewing and maintaining server and mobile device audit logs as follows: 1. Log in to the BlackBerry UEM console. Select the "Settings" tab at the top of the screen. 2. Expand the "Administrators" tab on the left pane. 3. Select the "Roles" tab on the left pane. 4. Click the "Auditor" role. 5. Verify the role only has the following permissions assigned: - View audit information; - View audit settings; - Edit audit settings and purge data; and - Edit logging settings. Talk to the "UEM Security Administrator". Verify custom administrator roles/UEM predefined enterprise/help desk roles are used for day-to-day management of user accounts, group accounts, and profiles. If at least one user is not associated with the "UEM Security Administrator", "Auditor", and one or more site custom administrator roles/UEM predefined enterprise/help desk roles, this is a finding. If the "auditor" role has more permissions than authorized, this is a finding. If day-to-day management of user accounts, group accounts, and profiles is primarily performed by "UEM Security Administrators" instead of one or more site custom administrator roles/UEM predefined enterprise/help desk roles, this is a finding.

## Group: PP-MDM-411065

**Group ID:** `V-224378`

### Rule: The BlackBerry UEM server must be configured to audit DoD or site-defined auditable events. Note: See VulDiscussion for a list of DoD required auditable events.

**Rule ID:** `SV-224378r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the application will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. DoD Required auditable events (from the MDM Protection Profile): - Change in enrollment status - Failure to apply policies to a mobile device - Start up and shut down of the MDM System - All administrative actions - Commands issued to the MDM Agent, none] - Specifically defined auditable events listed in Table 2 of the MDM Protection Profile SFR ID: FAU_GEN.1.1(1), FMT_SMF.1.1(2)c.8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of audit events: 1. In the UEM console go to Settings >> Infrastructure >> Audit settings 2. Verify all required events are listed and "setting" is set to "All" for all events where this selection is available. Note: Events are organized by category. All events for each required event category should be selected (see the list below). If all required events are not listed and "setting" is not set to "All" for all events where this selection is available, this is a finding. Required events: all "Enrollment" events, all "Policy" events, all "Server" events, all "System" related events, and all "Application" events

## Group: PP-MDM-414002

**Group ID:** `V-224379`

### Rule: The BlackBerry UEM server must be configured to leverage the MDM platform user accounts and groups for BlackBerry UEM server user identification and CAC authentication.

**Rule ID:** `SV-224379r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire BlackBerry UEM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the BlackBerry UEM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server configuration settings. Verify the server is configured to leverage the MDM Platform user accounts and groups for BlackBerry UEM server user identification and authentication. On the BlackBerry UEM, do the following: 1. Navigate to the BlackBerry UEM console. 2. Verify the BlackBerry UEM does not prompt for additional authentication before opening the UEM console. If the BlackBerry UEM server prompts for additional authentication before opening the UEM console, this is a finding.

## Group: PP-MDM-414003

**Group ID:** `V-224380`

### Rule: Authentication of MDM platform accounts must be configured so they are implemented via an enterprise directory service.

**Rule ID:** `SV-224380r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire BlackBerry UEM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the BlackBerry UEM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server configuration settings. Verify the server is configured to leverage the MDM Platform user accounts and groups for BlackBerry UEM server user identification and authentication. On the BlackBerry UEM, do the following: 1. Navigate to the BlackBerry UEM console. 2. Verify the BlackBerry UEM does not prompt for additional authentication before opening the UEM console. If the BlackBerry UEM server prompts for additional authentication before opening the UEM console, this is a finding.

## Group: PP-MDM-992000

**Group ID:** `V-224381`

### Rule: The BlackBerry UEM server must be maintained at a supported version.

**Rule ID:** `SV-224381r604136_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Versions of BlackBerry UEM are maintained by BlackBerry for specific periods of time. Unsupported versions will not receive security updates for new vulnerabilities which leaves them subject to exploitation. A list of supported UEM versions is maintained by BlackBerry here: https://www.blackberry.com/us/en/support/software-support-life-cycle. SFR ID: FPT_TUD_EXT.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the UEM console version, via the help page. Correlate the version with the latest supported version of UEM. If the installed version of UEM is not a supported version, this is a finding.

## Group: PP-MDM-431005

**Group ID:** `V-224382`

### Rule: The BlackBerry UEM server platform must be protected by a DoD-approved firewall.

**Rule ID:** `SV-224382r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The BlackBerry UEM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the BlackBerry UEM server runs on a standalone platform. Network firewalls or other architectures may be preferred where the BlackBerry UEM server runs in a cloud or virtualized solution. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server platform configuration to determine whether a DoD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on the BlackBerry UEM server platform, this is a finding.

## Group: PP-MDM-431005

**Group ID:** `V-224383`

### Rule: The firewall protecting the BlackBerry UEM server platform must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support BlackBerry UEM server and platform functions.

**Rule ID:** `SV-224383r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since BlackBerry UEM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the BlackBerry UEM server provides a protection mechanism to ensure unwanted service requests do not reach the BlackBerry UEM server and outbound traffic is limited to only BlackBerry UEM server functionality. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the BlackBerry UEM administrator for a list of ports, protocols, and IP address ranges necessary to support BlackBerry UEM server and platform functionality. A list can usually be found in the STIG Supplemental document or BlackBerry UEM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-431006

**Group ID:** `V-224384`

### Rule: The firewall protecting the BlackBerry UEM server platform must be configured so that only DoD-approved ports, protocols, and services are enabled. (See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services).

**Rule ID:** `SV-224384r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the BlackBerry UEM administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the BlackBerry UEM server or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the BlackBerry UEM host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

## Group: PP-MDM-431007

**Group ID:** `V-224385`

### Rule: All BlackBerry UEM server local accounts created during application installation and configuration must be disabled or removed.

**Rule ID:** `SV-224385r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire BlackBerry UEM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the BlackBerry UEM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FMT_SMF.1.1(2) b / IA-5(1)(a) Satisfies: SRG-APP-000148</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BlackBerry UEM server configuration settings. Verify the server is configured to leverage the MDM Platform user accounts and groups for BlackBerry UEM 12.11 server user identification and authentication. On the BlackBerry UEM, do the following: 1. Navigate to the BlackBerry UEM console. 2. Verify the BlackBerry UEM does not prompt for additional authentication before opening the UEM console. If the BlackBerry UEM server prompts for additional authentication before opening the UEM console, this is a finding.

## Group: PP-MDM-431009

**Group ID:** `V-224386`

### Rule: The BlackBerry UEM server must connect to [assignment: [SQL Server]] with an authenticated and secure (encrypted) connection to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-224386r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: PP-MDM-431009 / SRG-APP-000439, SRG-APP-000440 SFR ID: FMT_SMF.1.1(2) b / SC-8, SC-8 (1), SC-8 (2)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Talk to the site UEM Administrator to confirm the SQL server has been configured to connect to UEM using the TLS connection or confirm during a review of the SQL server. If the SQL server has not been configured to connect to UEM using the TLS connection, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-224387`

### Rule: The BlackBerry UEM server Blackberry Web Services must not be authorized access from external sources unnecessarily.

**Rule ID:** `SV-224387r604136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting access to the subset of Administrator UI functions to internal administrators, the risk of an attacker developing a custom application to administer UEM potentially changing pre-configuration items in UEM is reduced SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify BlackBerry UEM server Blackberry Web Services has not been configured to allow access from external sources unnecessarily. 1. Log in to the UEM Server console. 2. On the left bar, access Settings >> General Settings >> Blackberry Web Services access. 3. Verify the status has not changed from disabled unless the ISSM has approved access. If BlackBerry UEM server Blackberry Web Services has not disabled access from external sources unnecessarily without ISSM approval, this is a finding.

