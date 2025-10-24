# STIG Benchmark: MobileIron Core v10.x MDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-312001

**Group ID:** `V-91807`

### Rule: The MobileIron Core v10 server must be able to limit user enrollment of devices that do not have required OS type and version.

**Rule ID:** `SV-101909r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access control of mobile devices to DoD sensitive information or access to DoD networks must be controlled so that DoD data will not be compromised. The primary method of access control of mobile devices is via enrollment of authorized mobile devices on the MobileIron Core v10 server. Therefore, the MobileIron Core v10 server must have the capability to enforce a policy for this control. SFR ID: FIA_ENR_EXT.1.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following actions to verify users cannot enroll devices that do not have required OS type and version. Task 1: Verify that the appropriate OSs are allowed to register. 1. In the Admin Portal, go to Settings >> Users & Devices >> Registration. 2. Scroll to the "Platforms for Registration" section. 3. In the "Enabled Platforms" list, verify all inappropriate OSs are excluded. If inappropriate OSs are able to register, this is a finding. Task 2: Verify the OS version alert is setup. 1. Log on to the MobileIron Core Admin Portal. 2. In the Admin Portal, go to Logs >> Event Settings. 3. Select the appropriate Alert. 4. Select "Edit". 5. Verify “Disallowed {appropriate OS} version found” is selected for every managed OS and all other checkboxes are not selected. If there is no OS version alert setup or the alert is not set up correctly, this is a finding. Task 3: Verify a custom compliance action is setup. 1. Go to Policies & Configs >> Compliance Actions. 2. Select the desired compliance action. 3. Select "Actions". 4. Select "Edit". 5. Verify the following checkboxes are selected: - Enforce Compliance Actions Locally on Devices - Send a compliance notification or alert to the user - Block email access and AppConnect apps - Quarantine the device - Remove All Configurations If there is no custom compliance action setup or the custom compliance action is not set up correctly, this is a finding. Task 4: Verify each appropriate security policy is setup to trigger a compliance action when OS violations occur. 1. In Admin Portal, go to Policies & Configs >> Policies. 2. Select the security policy you want to work with. 3. Click "Edit". 4. Scroll down to the "Access Control" section of the Modifying Security Policy dialog. 5. Under appropriate OS type, verify the checkbox for when "OS version is less than" has been selected. 6. On the same line, verify in the dropdown list, the appropriate custom compliance action is selected. 7. On the same line, in the dropdown list for appropriate OS versions, verify the appropriate OS version is selected. If there is no compliance action setup for OS version in the security policy or the compliance action is not set up correctly, this is a finding. Task 5: Verify the security policy is assigned to all applicable labels. 1. Go to Policies and Configs >> Policies. 2. For the security policy being verified, put cursor over the "Labels" column. 3. Verify the "Applied Label(s)" includes all desired labels. If all desired labels are not selected in each appropriate policy, this is a finding.

## Group: PP-MDM-311047

**Group ID:** `V-91809`

### Rule: The MobileIron Core v10 server or platform must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-101911r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead. SFR ID: FMT_SMF.1.1(2) h</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server or platform configuration. Verify the server is configured to lock after "15-minutes or less" of inactivity. You will see the current value for the session timeout, in minutes. If, in the Admin Portal, Settings >> General >> Timeout is not set to "15-minutes or less", this is a finding.

## Group: PP-MDM-311054

**Group ID:** `V-91811`

### Rule: The MobileIron Core v10 server must be configured to transfer MobileIron Core v10 server logs to another server for storage, analysis, and reporting. Note: MobileIron Core v10 server logs include logs of MDM events and logs transferred to the MobileIron Core v10 server by MDM agents of managed devices.

**Rule ID:** `SV-101913r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the MobileIron Core v10 server has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the MobileIron Core v10 server must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) h, FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Splunk is configured for automated log export. Step 1: Verify that the "Splunk Forwarder" is "Enabled". 1. Log onto System Manager. 2. Go to Settings >> Services. 3. Verify that the "Enable" toggle is "ON" and "Running" is displayed. If "Enable" toggle is not "ON" or "Running" is not displayed, this is a finding. Step 2: Verify that "Splunk Indexer" is configured. 1. Log onto System Manager. 2. Go to Settings >> Data Export >> Splunk Indexer. 3. Verify that there is an entry and the Status is "Connected". If there is no entry for "Splunk Indexer" or the Status is "Not Connected", this is a finding. Step 3: Verify "Audit Log" is enabled in the Splunk "Data to Index". 1. Log onto System Manager. 2. Go to Settings >> Data Export >> Splunk Data to open the "Data to Index" window. 3. Verify "Audit Log" is included in the "Data to Index". If "Audit Log" is not included in the "Data to Index", this is a finding.

## Group: PP-MDM-311056

**Group ID:** `V-91813`

### Rule: The MobileIron Core v10 server must be configured to display the required DoD warning banner upon administrator logon. Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-101915r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the MobileIron Core v10 server or MobileIron Core v10 server platform. Before granting access to the system, the MobileIron Core v10 server/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner must be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) d</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MDM server documentation and configuration settings to determine if the MDM server is using the warning banner and the wording of the banner is the required text. On the MDM console, do the following: 1. Connect to the MobileIron Core Server using SSH. 2. Type in a user name and press "Enter". 3. Verify the required banner is displayed before the password prompt. The required text is found in the VulDiscussion. If the required banner is not presented, this is a finding. 1. Connect to the MobileIron Core Server system manager portal using a web browser. 2. Verify the required banner is displayed on the web page. The required text is found in the VulDiscussion. If the required banner is not presented, this is a finding. 1. Connect to the MobileIron Core Server administrator portal using a web browser. 2. Verify the required banner is displayed on the web page. If the required banner is not presented, this is a finding.

## Group: PP-MDM-311057

**Group ID:** `V-91815`

### Rule: The MobileIron Core v10 server must be configured with a periodicity for reachable events of six hours or less for the following commands to the agent: - query connectivity status; - query the current version of the MD firmware/software; - query the current version of the hardware model of the device; - query the current version of installed mobile applications; - read audit logs kept by the MD.

**Rule ID:** `SV-101917r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Key security-related status attributes must be queried frequently so the MobileIron Core v10 server can report status of devices under management to the administrator and management. The periodicity of these queries must be configured to an acceptable timeframe. Six hours or less is considered acceptable for normal operations. SFR ID: FMT_SMF.1.1(2) e</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server configuration settings. Verify the server is configured with a periodicity for reachable events of "six hours or less" for the following commands to the agent: - query connectivity status; - query the current version of the MD firmware/software; - query the current version of the hardware model of the device; - query the current version of installed mobile applications; - read audit logs kept by the MD. Verify the sync interval for a device: 1. In the Admin Portal, go to Policies & Config >> Policies. 2. Select the default sync policy. 3. Verify that the Sync Interval is set to "360 minutes or less". If the "Sync interval" is not set up to "360 minutes or less", this is a finding.

## Group: PP-MDM-311058

**Group ID:** `V-91817`

### Rule: The MobileIron Core v10 server must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, auditor.

**Rule ID:** `SV-101919r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the MobileIron Core v10 server supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining which apps user groups or individual users have access to in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server configuration settings and verify the server is configured with the Administrator roles: - Server primary administrator - Security configuration administrator - Device user group administrator - Auditor On the MDM console, do the following: 1. Verify a user is in the "Server primary administrator" role. a. Logon to the MobileIron Core Server system manager portal as a user with the "server primary administrator" role using a web browser. b. Select Security >> Identity Source >> Local Users. If a user in the "server primary administrator" role is not listed, this is a finding. 2. Verify a user is in the "Security configuration administrator" role. a. Logon to the MobileIron Core Server administrator portal as a user with the "server primary administrator" role using a web browser. b. Select Admin >> Admins. c. Select user with the "Security configuration administrator" role. d. Click Actions >> Edit Roles. e. Verify that the following roles are selected: "Manage label", "View user", "Manage app", "Manage configuration", "Manage policy", "Manage settings and services", and "Manage administrators and device" spaces. If the "Security configuration administrator" user is not found or any of the required roles are not selected, this is a finding. 3. Verify a user is in the "Device user group administrator" role. a. Logon to the MobileIron Core Server administrator portal as a user with the "server primary administrator" role using a web browser. b. Select Admin >> Admins. c. Select user with the "Device user group administrator" role. d. Click Actions >> Edit Roles. e. Verify that the following roles are selected: "wipe devices", "add device", "manage ActiveSync device", and "delegate retired device" roles. If the "Device user group administrator" user is not found or any of the required roles are not selected, this is a finding. 4. Verify a user is in the "Auditor" role. a. Logon to the MobileIron Core Server administrator portal as a user with the "server primary administrator" role using a web browser. b. Select Admin >> Admins. c. Select user with the "Device user group administrator" role. d. Click Actions >> Edit Roles. e. Check that the following roles are selected: "Manage logs and events". If the user is not found or any of the required roles are not selected, this is a finding.

## Group: PP-MDM-314001

**Group ID:** `V-91819`

### Rule: The MobileIron Core v10 server must be configured to implement FIPS 140-2 mode for all server encryption (if not automatically configured during server install).

**Rule ID:** `SV-101921r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved cryptographic algorithms cannot be relied on to provide confidentiality or integrity, and DoD data could be compromised as a result. The most common vulnerabilities with cryptographic modules are those associated with poor implementation. FIPS 140-2 validation provides assurance that the relevant cryptography has been implemented correctly. FIPS 140-2 validation is also a strict requirement for use of cryptography in the federal government for protecting unclassified data. SFR ID: FCS</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MDM console, do the following: 1. SSH to MobileIron Core Server from any SSH client. 2. Enter the administrator credentials you set when you installed MobileIron Core. 3. Enter "show fips". 4. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Server Core does not report that fips mode is "enabled", this is a finding.

## Group: PP-MDM-314003

**Group ID:** `V-91821`

### Rule: Authentication of MDM platform accounts must be configured so they are implemented via an enterprise directory service.

**Rule ID:** `SV-101923r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MobileIron Core v10 server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MobileIron Core v10 server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MDM console, do the following: 1. Logon to the MobileIron Core Server administrator portal as a user with the "security configuration administrator" role using a web browser. 2. Select "Services" on the web page. 3. Select "LDAP" on the web page. 4. Click the "edit" icon on an existing LDAP configuration to be tested. 5. Select "Test" on the LDAP server configuration dialog. 6. Enter a valid LDAP user ID. 7. Select "Submit". 8. Verify the LDAP query is successful and shows user attributes in a dialog box. If the MDM server does not leverage the MDM platform user accounts and groups for the MDM server user identification and authentication, this is a finding.

## Group: PP-MDM-331004

**Group ID:** `V-91823`

### Rule: The MDM server platform must be protected by a DoD-approved firewall.

**Rule ID:** `SV-101925r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the MDM server runs on a standalone platform. Network firewalls or other architectures may be preferred where the MDM server runs in a cloud or virtualized solution. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server platform configuration to determine whether a DoD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on the MDM server platform, this is a finding.

## Group: PP-MDM-331005

**Group ID:** `V-91825`

### Rule: The firewall protecting the MDM server platform must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support MDM server and platform functions.

**Rule ID:** `SV-101927r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the MDM server provides a protection mechanism to ensure unwanted service requests do not reach the MDM server and outbound traffic is limited to only MDM server functionality. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and IP address ranges necessary to support MDM server and platform functionality. A list can usually be found in the STIG Supplemental document or MDM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-331006

**Group ID:** `V-91827`

### Rule: The firewall protecting the MDM server platform must be configured so that only DoD-approved ports, protocols, and services are enabled. (See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services.)

**Rule ID:** `SV-101929r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the MDM server or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the MDM host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

