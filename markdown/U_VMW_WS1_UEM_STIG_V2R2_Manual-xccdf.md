# STIG Benchmark: VMware Workspace ONE UEM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-411047

**Group ID:** `V-221637`

### Rule: The Workspace ONE UEM server or platform must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-221637r960741_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock, but may be at the application level where the application interface window is secured instead. SFR ID: FMT_SMF.1.1(2) c.8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Workspace ONE UEM server or platform configuration and verify the server is configured to lock after 15 minutes of inactivity. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Navigate to Groups & Settings >> All Settings >> Admin >> Console Security >> Session Management. 3. Examine value present in "Idle Session Timeout" (value is number of minutes). If the MDM console [configuration setting] is not set to 15 minutes or less, this is a finding.

## Group: PP-MDM-411051

**Group ID:** `V-221638`

### Rule: The Workspace ONE UEM server must be configured with an enterprise certificate for signing policies (if function is not automatically implemented during Workspace ONE UEM server install).

**Rule ID:** `SV-221638r971322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that only authorized certificates are used for key activities such as code signing for system software updates, code signing for integrity verification, and policy signing. Otherwise, there is no assurance that a malicious actor has not inserted itself in the process of packaging the code or policy. For example, messages signed with an invalid certificate may contain links to malware, which could lead to the installation or distribution of that malware on DoD information systems, leading to compromise of DoD sensitive information and other attacks. Therefore, the Workspace ONE UEM server must have the capability to configure the enterprise certificate. SFR ID: FMT_SMF.1.1(2) c.8, FMT_POL_EXT.1.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Workspace ONE UEM server configuration settings and verify the server is configured with an enterprise certificate for signing policies. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Navigate to Groups & Settings >> All Settings >> System >> Advanced >> Policy Signing Certificate. If the "Policy Signing Certificate" choice is not present under "Advanced", this is a finding. If the "Policy Signing Certificate" choice is present, but the Workspace ONE UEM server is not configured with an enterprise certificate for signing policies, this is a finding. For Android: No additional checks are required. For iOS: 3. Navigate to Groups & Settings >> All Settings >> Devices & Users >> Apple >> Profiles. If "Sign Profiles" (Requires Server SSL Certificate)" is set to "DISABLED" or is set to "ENABLED" and no signing certificate is listed, this is a finding.

## Group: PP-MDM-411054

**Group ID:** `V-221640`

### Rule: The Workspace ONE UEM server must be configured to transfer Workspace ONE UEM server logs to another server for storage, analysis, and reporting.

Note: Workspace ONE UEM server logs include logs of MDM events and logs transferred to the Workspace ONE UEM server by MDM agents of managed devices.

**Rule ID:** `SV-221640r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the Workspace ONE UEM server has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the Workspace ONE UEM server must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) c.8, FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Workspace ONE UEM server configuration settings and verify the server is configured to transfer Workspace ONE UEM server logs to another server for storage, analysis, and reporting. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Navigate to Groups & Settings >> All Settings >> System >> Enterprise Integration >> Syslog. 3. If "Syslog Integration" is set to "DISABLED", this is a finding. 4. Examine the syslog configuration (server hostname, protocol, port, syslog facility, message tag, message content) for conformance with operational standards. If any are not set according to the standards, this is a finding. Note: Workspace ONE UEM server logs include logs of MDM events and logs transferred to the Workspace ONE UEM server by MDM agents of managed devices.

## Group: PP-MDM-411056

**Group ID:** `V-221641`

### Rule: The Workspace ONE UEM server must be configured to display the required DoD warning banner upon administrator logon.

Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-221641r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the Workspace ONE UEM server or Workspace ONE UEM server platform. Before granting access to the system, the Workspace ONE UEM server/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) c.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Workspace ONE UEM server documentation and configuration settings to determine if the Workspace ONE UEM server is using the warning banner and the wording of the banner is the required text. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Verify that the notice and consent warning message is displayed. 3. Authenticate to the Workspace ONE UEM Self-Service Portal. 4. Verify that the notice and consent warning message is displayed. If the warning banner is not set up on the Workspace ONE UEM server or wording does not exactly match the requirement text, this is a finding.

## Group: PP-MDM-411057

**Group ID:** `V-221642`

### Rule: The Workspace ONE UEM server must be configured with a periodicity for reachable events of six hours or less for the following commands to the agent: 
- query connectivity status;
- query the current version of the MD firmware/software;
- query the current version of installed mobile applications;
- read audit logs kept by the MD.


**Rule ID:** `SV-221642r961731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Key security-related status attributes must be queried frequently so the Workspace ONE UEM server can report status of devices under management to the administrator and management. The periodicity of these queries must be configured to an acceptable timeframe. Six hours or less is considered acceptable for normal operations. SFR ID: FMT_SMF.1.1(2) c.3</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Workspace ONE UEM server for a periodicity for reachable events of six hours or less for the following commands to the agent: - query connectivity status; - query the current version of the MD firmware/software; - query the current version of installed mobile applications. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Navigate to Groups & Settings >> All Settings. 3. Under the "Devices & Users" heading: For Android, choose Android >> Intelligent Hub Settings. a. Under the General heading, if "Heartbeat Interval" is set to more than six hours, this is a finding. This setting handles querying of connectivity status and current version of MD firmware/software. b. Under the Application List heading, if the "Application List Interval" is set to more than 360 minutes, this is a finding. This setting handles querying for current version of installed mobile applications. For iOS, Apple >> MDM Sample Schedule. a. If "Device Information Sample" is set to more than six hours, this is a finding. This setting handles querying of connectivity status and current version of MD firmware/software. b. If "Application List Sample" and "Managed App List Sample" are set to more than 6 hours, this is a finding. This setting handles querying for current version of installed mobile applications.

## Group: PP-MDM-411058

**Group ID:** `V-221643`

### Rule: The Workspace ONE UEM server must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, or auditor.

**Rule ID:** `SV-221643r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the Workspace ONE UEM server supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configuration, which they may not understand or approve of, that can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining to which apps user groups or individual users have access in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Workspace ONE UEM server configuration settings and verify the server is configured with the Administrator roles: - Server primary administrator - Security configuration administrator - Device user group administrator - Auditor On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console. 2. Navigate to Accounts >> Administrators >> Roles. 3. From the Roles page, examine the currently defined roles under the "General Info" heading. Each role can be selected for examination by clicking on the name link. Each role will have a set of attributes for which that role has been granted: "Read", "Edit", or no access. If the MDM console administrative role is not present or the role attributes are not set to organizational standards, this is a finding.

## Group: PP-MDM-414002

**Group ID:** `V-221644`

### Rule: The Workspace ONE UEM server must be configured to leverage the MDM platform user and administrator accounts and groups for Workspace ONE UEM server user identification and authentication.

**Rule ID:** `SV-221644r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire Workspace ONE UEM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the Workspace ONE UEM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration steps necessary to leverage MDM platform user and administrator accounts and groups for Workspace ONE UEM server user identification and authentication: On the Workspace ONE UEM console, complete the following procedure to ensure the Workspace ONE UEM (MDM) Server is configured to leverage an enterprise authentication mechanism, and that Workspace ONE UEM users and administrators can only use directory accounts to enroll into the Workspace ONE UEM (MDM) Server: 1. For Workspace ONE UEM server Platform configuration, refer to "https://docs.vmware.com/en/VMware-Workspace-ONE-UEM/1907/Directory_Service_Integration/GUID-AWT-DIRECTORYSERVICESOVERVIEW.html". 2. Log in to the Workspace ONE UEM Administration console. 3. Choose "Groups and Settings". 4. Choose "All Settings". 5. Under the "System" heading, choose "Enterprise Integration". 6. Choose "Directory Services". 7. Under the "Server" tab, verify directory service connection information. 8. Under the "User" tab, verify User Group connection information. 9. Under the "Group" tab, verify Group connection information. 10. Choose "X" to close screen. 11. Choose "Groups and Settings". 12. Choose "All Settings". 13. Under "Devices and Users", choose "General". 14. Choose "Enrollment". 15. On the "Authentication Modes" setting, verify only the box titled "Directory" is selected. If on the Workspace ONE UEM server console "Directory" is not selected as the authentication mode, this is a finding. If the MDM platform user authentication is not implemented via an enterprise directory service, this is a finding. To verify administrators can only use directory services accounts: 16. Choose Accounts >> Administrators >> List View. 17. Review user types under the Admin Type heading. If any users have an Admin Type of "Basic", this is a finding. To verify users can only use directory services accounts: 18. Choose Accounts >> Users >> List View. If only a small number of user accounts are listed, it is recommended to use the following steps: a. Under the "General Info" tab, click each username link to view the user's summary data. b. Under "Type" in the "User Info" column, if "Basic" is listed, this is a finding. c. Choose "List View" again to be presented with the list of user accounts and repeat steps a and b until the full set of user accounts has been examined. If a large number of user accounts are listed, it is recommended to use the following steps instead: a. Choose the "Export" drop-down and select the format to be used for the export list. b. An "Export List" pop-up window will appear with instructions on where to locate and examine the exported list of user accounts. c. Examine the exported list. If any user accounts are denoted as "Basic" in the "Security Type" column, this is a finding. Exception: One local "Emergency" account may remain.

## Group: PP-MDM-414003

**Group ID:** `V-221645`

### Rule: Authentication of MDM platform accounts must be configured so they are implemented via an enterprise directory service.

**Rule ID:** `SV-221645r960768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire Workspace ONE UEM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the Workspace ONE UEM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM platform to verify user and administrator authentication is implemented via an enterprise directory service. On the Workspace ONE UEM console complete the following procedure to ensure that the Workspace ONE UEM (MDM) Server is configured to leverage an enterprise authentication mechanism, and that Workspace ONE UEM users and administrators can only use directory accounts to enroll into the Workspace ONE UEM (MDM) Server: 1. For Workspace ONE UEM server Platform configuration, refer to "https://docs.vmware.com/en/VMware-Workspace-ONE-UEM/1907/Directory_Service_Integration/GUID-AWT-DIRECTORYSERVICESOVERVIEW.html". 2. Log in to the Workspace ONE UEM Administration console. 3. Choose "Groups and Settings". 4. Choose "All Settings". 5. Under "System" heading, choose "Enterprise Integration". 6. Choose "Directory Services". 7. Under "Server" tab, verify directory service connection information. 8. Under "User" tab, verify User Group connection information. 9. Under "Group" tab, verify Group connection information. 10. Choose "X" to close screen. 11. Choose "Groups and Settings". 12. Choose "All Settings". 13. Under "Devices and Users", choose "General". 14. Choose "Enrollment". 15. On "Authentication Modes" setting, verify only the box titled "Directory" is selected. If on the Workspace ONE UEM server console "Directory" is not selected as the authentication mode, this is a finding. If the MDM platform user authentication is not implemented via an enterprise directory service, this is a finding. To verify administrators can only use directory services accounts: 16. Choose Accounts >> Administrators >> List View. 17. Review user types under the Admin Type heading. If any users have an Admin Type of "Basic", this is a finding. Exception: One local "Emergency" account may remain that uses WS1 authentication services. To verify users can only use directory services accounts: 18. Choose Accounts >> Users >> List View. If only a small number of user accounts are listed, it is recommended to use the following steps: a. Under the "General Info" tab, click on each username link to view the user's summary data. b. Under "Type" in the "User Info" column, if "Basic" is listed, this is a finding. c. Choose "List View" again to be presented with the list of user accounts and repeat steps a and b until the full set of user accounts has been examined. If a large number of user accounts are listed, it is recommended to use the following steps instead: a. Choose the "Export" drop-down and select the format to be used for the export list. b. An "Export List" pop-up window will appear with instructions on where to locate and examine the exported list of user accounts. c. Examine the exported list. If any user accounts are denoted as Basic in the Security Type column, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-221646`

### Rule: The Workspace ONE UEM server must be maintained at a supported version.

**Rule ID:** `SV-221646r986316_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The MDM/EMM vendor maintains specific product versions for a specific period of time. MDM/EMM server versions no longer supported by the vendor will not receive security updates for new vulnerabilities which leaves them subject to exploitation. SFR ID: FPT_TUD_EXT.1.1, FPT_TUD_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the installed version of Workspace ONE UEM server is currently supported. On the Workspace ONE UEM server console, do the following to determine the version number of the server: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Click "About" on the bottom of the left hand menu. The version and build of the installed software will be displayed. List of current supported versions: https://www.vmware.com/content/dam/digitalmarketing/vmware/en/pdf/support/product-lifecycle-matrix.pdf, scroll to Workspace ONE UEM Console. If the displayed Workspace ONE server version is not currently supported, this is a finding.

## Group: PP-MDM-431004

**Group ID:** `V-221647`

### Rule: The Workspace ONE UEM server must be protected by a DoD-approved firewall.

**Rule ID:** `SV-221647r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the MDM server runs on a standalone platform. Network firewalls or other architectures may be preferred where the MDM server runs in a cloud or virtualized solution. Satisfies: SRG-APP-000142 SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server platform configuration to determine whether a DoD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on the MDM server platform, or if it is not configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, this is a finding.

## Group: PP-MDM-431005

**Group ID:** `V-221648`

### Rule: The firewall protecting the Workspace ONE UEM server must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support MDM server and platform functions.

**Rule ID:** `SV-221648r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the MDM server provides a protection mechanism to ensure unwanted service requests do not reach the MDM server and outbound traffic is limited to only MDM server functionality. Satisfies: SRG-APP-000142 SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and IP address ranges necessary to support MDM server and platform functionality. A list can usually be found in the STIG Supplemental document or MDM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-431006

**Group ID:** `V-221649`

### Rule: The firewall protecting the Workspace ONE UEM server must be configured so that only DoD-approved ports, protocols, and services are enabled. (See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services).

**Rule ID:** `SV-221649r960966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. Satisfies: SRG-APP-000142 SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the MDM server or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the MDM host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

## Group: PP-MDM-431007

**Group ID:** `V-221650`

### Rule: All Workspace ONE UEM server local accounts created during application installation and configuration must be disabled or removed.

**Rule ID:** `SV-221650r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). Satisfies: SRG-APP-000148 SFR ID: FMT_SMF.1.1(2) b / IA-5(1)(a)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration for Workspace ONE UEM server administrative accounts for any local accounts: 1. Log in to the Workspace ONE UEM Administration console. 2. Choose Accounts >> Administrators >> List View. 3. Review user types under the Admin Type heading. If any users have an Admin Type of "Basic", this is a finding. Exception: One local "Emergency" account may remain.

## Group: PP-MDM-401005

**Group ID:** `V-221651`

### Rule: The MDM Agent must be configured to enable the following function: [selection: read audit logs of the MD].

This requirement is inherently met if the function is automatically implemented during MDM Agent install/device enrollment.


**Rule ID:** `SV-221651r960918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs and alerts enable monitoring of security-relevant events and subsequent forensics when breaches occur. They help identify when the security posture of the device is not as expected. This enables the MDM administrator to take an appropriate remedial action. SFR ID: FMT_SMF_EXT.4.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM Agent documentation and configuration settings to determine if the following function is enabled: read audit logs of the MD. This validation procedure is performed on the MDM Administration Console. On the MDM console, do the following: 1. Authenticate to the Workspace ONE UEM console as the administrator. 2. Navigate to Groups & Settings >> All Settings >> Devices & Users >> General >> Privacy and enable Request Device Log in the privacy settings. If "Request Device Log" is present, then no device log is being requested from the MD and this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251259`

### Rule: The Workspace ONE UEM local accounts password must be configured with length of 15 characters.

**Rule ID:** `SV-251259r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. SFRID: FMT_SMF.1(2)b. / IA-5 (1) (a)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is configured to enforce a local account password length of at least 15 characters for the emergency local account. 1. Log in to the WS1UEM console. 2. Go to Settings >> Admin >> Console Security >> Passwords. 3. Verify "Minimum Password Length" is set to 15. If the minimum password length is not set to 15, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251260`

### Rule: The Workspace ONE UEM local accounts must be configured with at least one lowercase character, one uppercase character, one number, and one special character.

**Rule ID:** `SV-251260r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is configured to enforce a local account password with at least one lower case letter, one uppercase character, one number, and one special character for the emergency local account. 1. Log in to the WS1UEM console. 2. Go to Settings >> Admin >> Console Security >> Passwords. 3. Verify "Password complexity level" to "Mixed case, alphabetic, numeric and special characters". If password complexity is not set as listed above, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251261`

### Rule: The Workspace ONE UEM local accounts must be configured with password maximum lifetime of 60 days.

**Rule ID:** `SV-251261r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (d)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is configured to have a local account password lifetime of 60 days for the emergency local account. 1. Log in to the WS1UEM console. 2. Go to Settings >> Admin >> Console Security >> Passwords. 3. Verify "Password Expiration Period (days)" is set to 60. If WS1 UEM is not configured to have a local account password lifetime of 60 days, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251262`

### Rule: The Workspace ONE UEM local accounts must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-251262r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (e)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is configured to prohibit password reuse for a minimum of five generations for local account passwords for the emergency local account. 1. Log in to the WS1UEM console. 2. Go to Settings >> Admin >> Console Security >> Passwords. 3. Verify "Enforced password history" to "5 passwords remembered". If WS1 UEM is not configured to prohibit password reuse for a minimum of five generations for local account passwords, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251263`

### Rule: The Workspace ONE UEM must enforce the limit of three consecutive invalid logon attempts by a user.

**Rule ID:** `SV-251263r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. SFR ID: FMT_SMF.1(2)b. / IA-7-a</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is configured to enforce a limit of three invalid logon attempts for a local account. 1. Log in to the WS1UEM console. 2. Go to Settings >> Admin >> Console Security >> Passwords. 3. Verify "Maximum invalid login attempts" is set to 3. If WS1 UEM is not configured to enforce a limit of three invalid logon attempts for a local account, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-251264`

### Rule: The Workspace ONE UEM must use multifactor authentication for local access to privileged accounts.

**Rule ID:** `SV-251264r971326_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication is defined as using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network. Applications integrating with the DoD Active Directory and utilize the DoD Common Access Card (CAC) are examples of compliant multifactor authentication solutions. SFR ID: FMT_SMF.1(2)b. / IA-2(3)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify WS1 UEM is using multifactor authentication for the local emergency account. Use one of the following two methods to confirm compliance: Method 1 Have the emergency account admin user log into the emergency account and verify the server requires 2FA before console access is granted. Method 2 1. Log in to the WS1UEM console. 2. Go to Accounts >> Administrators >> List View. 3. Select the Emergency account user and double-click on the account. 4. In the Add/Edit Admin screen, verify "Two-Factor Authentication" has been selected with either Email of SMS. Verify Notification has been selected and the token expiration time is 10 minutes or less. If WS1 UEM is not using multifactor authentication for the local emergency account, this is a finding.

