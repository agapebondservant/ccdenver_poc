# STIG Benchmark: IBM MaaS360 with Watson v10.x MDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-311054

**Group ID:** `V-82153`

### Rule: The MaaS360 MDM server must be configured to transfer MaaS360 MDM server logs to another server for storage, analysis, and reporting.

Note: MaaS360 MDM server logs include logs of MDM events and logs transferred to the MaaS360 MDM server by MDM agents of managed devices.

**Rule ID:** `SV-96867r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the MaaS360 MDM server has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the MaaS360 MDM server must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) b FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the site has set up access to web services to extract server logs. If the site has not set up access to server logs so the logs can be stored on another server for analysis and reporting, this is a finding.

## Group: PP-MDM-311056

**Group ID:** `V-82159`

### Rule: The MaaS360 MDM server must be configured to display the required DoD warning banner upon administrator logon.

Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-96873r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the MaaS360 MDM server or MaaS360 MDM server platform. Before granting access to the system, the MaaS360 MDM server/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) d</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server console configuration to determine if before establishing a user session, the server displays an administrator-specified advisory notice and consent warning message regarding use of the MaaS360 server. On the MaaS360 console complete the following steps: 1. Have a System Administrator log on to the portal. 2. Verify that the approved DoD Banner is displayed before the user obtains access to the console. If the MaaS360 server does not display an administrator-specified advisory notice and consent warning message regarding use of the MaaS360 server before establishing a user session, this is a finding.

## Group: PP-MDM-311058

**Group ID:** `V-82167`

### Rule: The MaaS360 MDM server must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, auditor.

**Rule ID:** `SV-96881r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the MaaS360 MDM server supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining which apps user groups or individual users have access to in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server console and confirm that different roles (administrator, auditor, user) are created with different levels of privileges, providing separation of duties for different users/groups. On the MaaS360 console, complete the following steps: 1. Go to Setup >> Roles. 2. Verify all required roles are listed. (Note: Role titles may be different than listed in the requirement statement.) 3. Select applicable role and select "edit", and then verify the role has the appropriate rights to access based on vulnerability description of this requirement statement (check). If the MaaS360 server does not have all required roles and the roles do not have appropriate rights, this is a finding.

## Group: PP-MDM-314002

**Group ID:** `V-82169`

### Rule: The MaaS360 MDM server must be configured to leverage the MDM platform user accounts and groups for MaaS360 MDM server user identification and authentication.

**Rule ID:** `SV-96883r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MaaS360 MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MaaS360 MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server console and confirm that the MDM platform accounts are leveraged when users identify and authenticate themselves to the MaaS360 console. On the MaaS360 Console, complete the following steps: 1. Navigate to Setup >> Settings. 2. Under Administrator Setting >> Advanced, select "Login Settings". 3. Verify "Configure Federated Single Sign-On" is checked and "Authenticate against Corporate User Directory" is selected. 4. Verify the Cloud Extender is installed: Setup >> Cloud Extender and verify "Cloud Extender Online" is checked. If "Configure Federated Single Sign-On" and "Authenticate against Corporate User Directory" are not selected, this is a finding. For SaaS deployments if Cloud Extender is not installed or "Cloud Extender Online" is not checked, this is a finding.

## Group: PP-MDM-314003

**Group ID:** `V-82171`

### Rule: Authentication of MaaS360 MDM platform accounts must be configured so they are implemented via an enterprise directory service.

**Rule ID:** `SV-96885r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MaaS360 MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MaaS360 MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following steps to verify the MaaS360 portal is configured to use an Enterprise directory service for portal access: Verify the MaaS360 is configured to use the Cloud Extender that connects to the Enterprise authentication service: 1. Log in to the portal. 2. Navigate to "Users" on the menu bar. 3. Select "Directory". 4. Confirm that for every administrator listed, "User Source" has "User Directory (AD)" listed. If any listed administrator does not have "User Source" as "User Directory (AD)", this is a finding.

## Group: PP-MDM-323202

**Group ID:** `V-82175`

### Rule: The MaaS360 MDM server must be configured to enable all required audit events (if function is not automatically implemented during MDM/MAS server install): a. Failure to push a new application on a managed mobile device.

**Rule ID:** `SV-96889r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to generate these audit records makes it more difficult to identify or investigate attempted or successful compromises, potentially causing incidents to last longer than necessary. SFR ID: FMT_SMF.1.1(3) c, FAU_GEN.1.1(2)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server console and confirm the server is configured to alert for audit event failures on managed mobile devices. On the MaaS360 Console, complete the following steps: 1. Navigate to Security >> Policies and have the System Administrator identify which mobile operating system (iOS, etc.) the MDM policy alerts apply to. 2. Open the identified policy and go to device settings >> application compliance. 3. Verify that "Configure required applications" is set to "yes" and that all new applications are listed. 4. Repeat for other MOS as required (for example, Android). If the "Configure required applications" is not set to "yes" or all new applications are not on the list, this is a finding.

## Group: PP-MDM-323202

**Group ID:** `V-82181`

### Rule: The MaaS360 server must be configured to enable all required audit events (if function is not automatically implemented during MDM/MAS server install): b. Failure to update an existing application on a managed mobile device.

**Rule ID:** `SV-96895r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Failure to generate these audit records makes it more difficult to identify or investigate attempted or successful compromises, potentially causing incidents to last longer than necessary. SFR ID: FMT_SMF.1.1(3) c, FAU_GEN.1.1(2)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server console and confirm the server is configured to alert for audit event failures on managed mobile devices. On the MaaS360 Console, complete the following steps: 1. Navigate to Devices >> Groups. 2. Have the System Administrator identify one or more groups that alert for failure to update an existing application on a managed mobile device. 3. Select "edit" for one of the identified groups and verify that the two conditions exist: - Condition 1: "Software Installed", "Application Name", "Contains", "<Name of Application>" - Condition 2: "Software Installed", "Full Version", "Contains","<latest version of Application>" 4. Navigate to Security >> Compliance Rules. 5. Have the System Administrator identify one or more Rule Set Names that alert for failure to update an existing application on a managed mobile device. 6. Open “Rule Set Name” and select “Enforcement Rules”. 7. Verify that “Application Compliance” is enabled and "Alert" is selected for “Enforcement Action”. 8. Go to Group Based Rules and verify that the rule selected in Step 5 has been assigned to the group identified in Step 3. If two conditions in the device group are not set correctly, or application compliance is not enabled and set correctly in the rule set name, or the rule is not assigned to the group, this is a finding.

## Group: PP-MDM-331004

**Group ID:** `V-82187`

### Rule: The MaaS360 server platform must be protected by a DoD-approved firewall.

**Rule ID:** `SV-96901r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the MDM server runs on a standalone platform. Network firewalls or other architectures may be preferred where the MDM server runs in a cloud or virtualized solution. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the implementation of the MaaS360 server with the site System Administrator. Verify a host-based firewall (for example, HBSS) is installed on the Windows server. If the MaaS360 server is not protected by a DoD-approved firewall, this is a finding.

## Group: PP-MDM-331005

**Group ID:** `V-82189`

### Rule: The firewall protecting the MaaS360 server platform must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support MaaS360 server and platform functions.

**Rule ID:** `SV-96903r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since MDM server is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the MDM server provides a protection mechanism to ensure unwanted service requests do not reach the MDM server and outbound traffic is limited to only MDM server functionality. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MaaS360 administrator for a list of ports, protocols, and IP address ranges necessary to support MaaS360 server and platform functionality. A list can usually be found in the STIG Supplemental document or MDM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only those ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-331006

**Group ID:** `V-82191`

### Rule: The firewall protecting the MaaS360 server platform must be configured so that only DoD-approved ports, protocols, and services are enabled. (See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services.)

**Rule ID:** `SV-96905r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. SFR ID: FMT_SMF.1.1(2) b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MaaS360 administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the MaaS360 server or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the MaaS360 host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

## Group: PP-MDM-301011

**Group ID:** `V-82193`

### Rule: The MaaS360 MDM Agent must be configured to implement the management setting: periodicity of reachability events equals six hours or less.

**Rule ID:** `SV-96907r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Key security-related status attributes must be queried frequently so the MaaS360 MDM Agent can report status of devices under management to the Administrator and management. The periodicity of these queries must be configured to an acceptable timeframe. Six hours or less is considered acceptable for normal operations. SFR ID: FAU_ALT_EXT.2.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the periodicity for agent checking to the server has been set to six hours or less. For Apple iOS devices, confirm with IBM that the periodicity for agent checking to the server has been set to 6 hours or less. For Samsung Android devices: 1. In the portal, navigate to "Security". 2. Select "Policy". 3. Select the policy for Samsung Android devices. 4. Open the policy. 5. Select "Device Settings" and then "Device Management". 6. Verify "Data Heartbeat Frequency" is set to 360 minutes or less. If the periodicity for agent checking to the server has not been set to 6 hours or less, this is a finding.

## Group: PP-MDM-302001

**Group ID:** `V-82195`

### Rule: The MaaS360 MDM Agent must provide an alert via the trusted channel to the MDM server for the following event: change in enrollment state.

**Rule ID:** `SV-96909r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Alerts providing notification of a change in enrollment state facilitate verification of the correct operation of security functions. When an MDM server receives such an alert from a MaaS360 MDM Agent, it indicates that the security policy may no longer be enforced on the mobile device. This enables the MDM administrator to take an appropriate remedial action. SFR ID: FAU_ALT_EXT.2.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MaaS360 server configuration to verify the MaaS360 Agent alerts the MDM via the trusted channel to the MaaS360 server for the following event: change in enrollment status. On the MaaS360 Console, complete the following steps: 1. Navigate to Security >> Compliance Rules. 2. Have the system administrator identify the applicable "Change in enrollment status" rule set name. 3. Select rule set name in list. 4. Under “Enforcement Rules”, verify the "Enrollment" box is checked, all boxes are checked for "Trigger Action on Managed Status", and "Enforcement Action" is set to "alert". If there are no "Change in enrollment status" rule set names set up or rules that have been set up are not configured correctly, this is a finding.

