# STIG Benchmark: Samsung SDS EMM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: PP-MDM-412000

**Group ID:** `V-225640`

### Rule: The Samsung SDS EMM must implement functionality to generate an audit record of the following auditable events:
c. [selection: Commands issued to the MDM Agent].

**Rule ID:** `SV-225640r588007_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. For audit logs to be useful, administrators must have the ability to view them. SFR ID: FAU_GEN.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following procedure to verify logging of all commands issued to the MDM Agent has been configured on the SDS EMM server: On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Go to Service Overview >> Log and Event >> Audit Event. 3. Verify all audit events with Type as "Server" and Event Category as "Device Command" have been selected. If logging of all commands issued to the MDM Agent has not been configured on the SDS EMM server, this is a finding.

## Group: PP-MDM-411009

**Group ID:** `V-225641`

### Rule: The Samsung SDS EMM must be configured to communicate the following commands to the MDM Agent: read audit logs kept by the MD.

**Rule ID:** `SV-225641r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. For audit logs to be useful, administrators must have the ability to view them. SFR ID: FMT_SMF.1.1(1) #19</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following procedure to verify the command to read audits to the MDM Agent has been configured on the SDS EMM server: On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Go to Service Overview >> Log and Event >> Audit Log. 3. Verify all audit events with audit type of "Device" have been selected. If the command for reading audits to the MDM Agent has not been configured on the SDS EMM server, this is a finding.

## Group: PP-MDM-411047

**Group ID:** `V-225642`

### Rule: The Samsung SDS EMM or platform must be configured to initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-225642r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to leaving the vicinity, applications must be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead. SFR ID: FMT_SMF.1.1(2) c.8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM or platform configuration and verify the server is configured to lock after 15 minutes of inactivity. On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Click the arrow next to the Admin account ID in the header of main page and verify the "Set Session Timeout" is set to 15 minutes or less. If the MDM console session time out is not set to 15 minutes or less, this is a finding.

## Group: PP-MDM-411054

**Group ID:** `V-225643`

### Rule: The Samsung SDS EMM must be configured to transfer Samsung SDS EMM logs to another server for storage, analysis, and reporting.

Note: Samsung SDS EMM logs include logs of MDM events and logs transferred to the Samsung SDS EMM by MDM agents of managed devices.

**Rule ID:** `SV-225643r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit logs enable monitoring of security-relevant events and subsequent forensics when breaches occur. Since the Samsung SDS EMM has limited capability to store mobile device log files and perform analysis and reporting of mobile device log files, the Samsung SDS EMM must have the capability to transfer log files to an audit log management server. SFR ID: FMT_SMF.1.1(2) c.8, FAU_STG_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM configuration settings and verify the server is configured to transfer Samsung SDS EMM logs to another server for storage, analysis, and reporting. On the MDM console, do the following: 1. Go to Setting >> Server >> Configuration. 2. Click "Audit" at the top of the window and verify audit log server and other information is listed. If the MDM console is not configured to transfer audit logs to an audit log server, this is a finding. Note: Samsung SDS EMM logs include logs of MDM events and logs transferred to the Samsung SDS EMM by MDM agents of managed devices.

## Group: PP-MDM-411056

**Group ID:** `V-225644`

### Rule: The Samsung SDS EMM must be configured to display the required DoD warning banner upon administrator logon.

Note: This requirement is not applicable if the TOE platform is selected in FTA_TAB.1.1 in the Security Target (ST).

**Rule ID:** `SV-225644r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Note: The advisory notice and consent warning message is not required if the general purpose OS or network device displays an advisory notice and consent warning message when the administrator logs on to the general purpose OS or network device prior to accessing the Samsung SDS EMM or Samsung SDS EMM platform. Before granting access to the system, the Samsung SDS EMM/server platform is required to display the DoD-approved system use notification message or banner that provides privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. This ensures the legal requirements for auditing and monitoring are met. The approved DoD text must be used as specified in the KS referenced in DoDI 8500.01. The non-bracketed text below must be used without any changes as the warning banner. [A. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating “OK.”] You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. SFR ID: FMT_SMF.1.1(2) c.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Samsung SDS EMM server documentation and configuration settings to determine if the warning banner is using the appropriate designated wording. On the MDM console, do the following: 1. Log in to the Samsung SDS EMM Server Admin Console using a web browser. 2. Go to Settings >> Admin Console >> Logo Setting. 3. Verify the text in the "Logo/Notification" window that appears. Confirm the text in the Login Notification box is the required DoD banner text. Alternately, verify the banner is correct during logon to the console. If the warning banner is not set up on the Samsung SDS EMM or wording does not exactly match the requirement text, this is a finding.

## Group: PP-MDM-411057

**Group ID:** `V-225645`

### Rule: The Samsung SDS EMM must be configured with a periodicity for reachable events of six hours or less for the following commands to the agent: 
- query connectivity status;
- query the current version of the MD firmware/software;
- query the current version of installed mobile applications;
- read audit logs kept by the MD.

**Rule ID:** `SV-225645r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Key security-related status attributes must be queried frequently so the Samsung SDS EMM can report status of devices under management to the administrator and management. The frequency of these queries must be configured to an acceptable timeframe. Six hours or less is considered acceptable for normal operations. SFR ID: FMT_SMF.1.1(2) c.3</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM agent configuration settings to determine if the agent is configured with a periodicity of reachable events set to six hours or less. This validation procedure is performed on the Samsung SDS EMM Server Admin Console. 1. Log in to the Samsung SDS EMM Server Admin Console using a web browser. 2. Go to Setting >> Server >> Configuration. 3. For Android: On row 27 verify "Inventory Collection Period for Android (hr)" is set to "6" or less. 4. For iOS: On row 28 verify "Inventory Collection Period for iOS (hr)" is set to "6" or less. If the periodicity of reachable events is not set to "6" hours or less, this is a finding.

## Group: PP-MDM-411058

**Group ID:** `V-225646`

### Rule: The Samsung SDS EMM must be configured to have at least one user in the following Administrator roles: Server primary administrator, security configuration administrator, device user group administrator, auditor.

**Rule ID:** `SV-225646r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Having several administrative roles for the Samsung SDS EMM supports separation of duties. This allows administrator-level privileges to be granted granularly, such as giving application management privileges to one group and security policy privileges to another group. This helps prevent administrators from intentionally or inadvertently altering other settings and configurations they may not understand or approve of, which can weaken overall security and increase the risk of compromise. - Server primary administrator: Responsible for server installation, initial configuration, and maintenance functions. Responsible for the setup and maintenance of security configuration administrator and auditor accounts. Responsible for the maintenance of applications in the MAS. - Security configuration administrator: Responsible for security configuration of the server, defining device user groups, setup and maintenance of device user group administrator accounts, and defining privileges of device user group administrators. - Device user group administrator: Responsible for maintenance of mobile device accounts, including setup, change of account configurations, and account deletion. Responsible for defining which apps user groups or individual users have access to in the MAS. Can only perform administrative functions assigned by the security configuration administrator. - Auditor: Responsible for reviewing and maintaining server and mobile device audit logs. SFR ID: FMT_SMR.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM configuration settings and verify the server is configured with the following Administrator roles: - Server primary administrator - Security configuration administrator - Device user group administrator - Auditor This validation procedure is performed on the MDM Administration Console. On the MDM console, do the following to verify that users in the roles (b), (c), and (d) exist: 1. Log in to the Samsung SDS EMM Server Admin Console using a web browser. 2. Go to Settings >> Admin Console >> Administrators. 3. Observe that the user with the Security configuration administrator role is in the list on this screen, that the "Type" column indicates "Super", and that a modify symbol appears under all of the columns for "App", "Cert", "Org", "Profile", "Portal", and "Audit". 4. Observe that the user with the Device user group administrator role is in the list on this screen, that the "Type" column indicates "Common", and that a modify symbol appears under all of the columns for "App", "Cert", "Org", "Profile", "Portal", and "Audit". 5. Observe that the user with the Auditor role is in the list on this screen, that the "Type" column indicates "Common", and that a modify symbol appears only under the "Audit" column. No verification is needed for the Server primary administrator since this role is always created automatically during server install. If the MDM console is not configured with the required Administrator roles, this is a finding.

## Group: PP-MDM-411065

**Group ID:** `V-225647`

### Rule: The Samsung SDS EMM must be configured to audit DoD or site-defined auditable events. Note: See VulDiscussion for a list of DoD required auditable events.

**Rule ID:** `SV-225647r744409_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the application will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. DoD Required auditable events (from the MDM Protection Profile): - Change in enrollment status - Failure to apply policies to a mobile device - Startup and shutdown of the MDM System - All administrative actions - Commands issued to the MDM Agent, none] - Specifically defined auditable events listed in Table 2 of the MDM Protection Profile SFR ID: FAU_GEN.1.1(1), FMT_SMF.1.1(2)c.8</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the event log to verify the following events are logged: - Change in enrollment status - Failure to apply policies to a mobile device - Startup and shutdown of the MDM System - All administrative actions On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Go to Service Overview >> Log and Event >> Audit Event. 3. Search on "Enrollment" and verify each "Console" and "Device" audit event are selected to audit Change in enrollment status. 4. Search on "Policy" and verify "Agent Policy Apply Success on a Device" (Event ID CPLC0029) and "Failed to apply Agent policy on Device" (Event ID CPLC0030) are selected to audit Failure to apply policies to a mobile device. 5. Search on "Start" and verify "Start up EMM Server" (Event ID CACS0001) is selected. Search on "shut down" and verify "Shut Down EMM Server" (Event ID CACS0002) is selected to audit startup and shutdown of the MDM System. 6. Verify all audit events with the event category of Admin Login, Administrators, Alerts, Dashboard, Device, Devices, Group, Logs, Profiles, and User Management are selected to audit all Administrative actions. If the following required audit events have not been selected, this is a finding. - Change in enrollment status - Failure to apply policies to a mobile device - Startup and shutdown of the MDM System - All administrative actions

## Group: PP-MDM-413002

**Group ID:** `V-225648`

### Rule: The [selection: Samsung SDS EMM, MDM platform] must have the capability to display the DoD warning banner prior to establishing a user session.

**Rule ID:** `SV-225648r588007_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." SFR ID: FTA_TAB.1.1, FMT_SMF.1.1(2) c.2</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Samsung SDS EMM server documentation and configuration settings to determine if the warning banner is using the appropriate designated wording. On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Go to Setting >> Server >> Configuration and click "EULA" at the top of the window. 3. Check the required DoD text in the EULA "Content" box. If the warning banner is not set up on the MDM server or wording does not exactly match the VulDiscussion text, this is a finding.

## Group: PP-MDM-414003

**Group ID:** `V-225649`

### Rule: The Samsung SDS EMM server must be configured to use one-time password in addition to username and password for administrator logon to the server.

**Rule ID:** `SV-225649r744410_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Two-factor authentication ensures strong authentication and access controls are in place for privileged accounts. But One-Time Passwords (OTP) do not meet DoD requirements that system administrators access privileged accounts via CAC authentication through a directory service (Active Directory). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the EMM server has not been configured to use one-time password (OTP) for administrator logon to the server. On the MDM console, do the following: 1. Log into the SDS EMM console. 2. Go to Setting >> Server >> Configuration >> Two-Factor Authentication. 3. Verify Two-Factor Authentication is set to "No". If the EMM server has not been configured to disable one-time-password (OTP) for administrator logon to the server, this is a finding.

## Group: PP-MDM-992000

**Group ID:** `V-225650`

### Rule: The Samsung SDS EMM server must be maintained at a supported version.

**Rule ID:** `SV-225650r588007_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Versions of Samsung SDS EMM are maintained by Samsung SDS for specific periods of time. Unsupported versions will not receive security updates for new vulnerabilities which leaves them subject to exploitation. SFR ID: FPT_TUD_EXT.1</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the installed version of the Samsung SDS EMM server is a supported version. A list of supported versions of EMM can be found at http://support.samsungsds.com. (Note: An account is needed to access this web page. The site EMM system administrator should be able to access the site and print the list for the reviewer/auditor.) For viewing the installed version of EMM, on the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Check the version by version number and deploy date at the bottom left on the screen. 3. Verify the version is on the list of supported versions on the Samsung SDS website. If the installed version of Samsung SDS EMM server is not a supported version, this is a finding.

## Group: PP-MDM-431004

**Group ID:** `V-225651`

### Rule: The Samsung SDS EMM platform must be protected by a DoD-approved firewall.

**Rule ID:** `SV-225651r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Unneeded services and processes provide additional threat vectors and avenues of attack to the information system. The Samsung SDS EMM is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality. All others must be expressly disabled or removed. A DoD-approved firewall implements the required network restrictions. A host-based firewall is appropriate where the Samsung SDS EMM runs on a standalone platform. Network firewalls or other architectures may be preferred where the Samsung SDS EMM runs in a cloud or virtualized solution. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142, PP-MDM-431004</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM platform configuration to determine whether a DoD-approved firewall is installed or if the platform operating system provides a firewall service that can restrict both inbound and outbound traffic by TCP/UDP port and IP address. If there is not a host-based firewall present on the Samsung SDS EMM platform, this is a finding.

## Group: PP-MDM-431005

**Group ID:** `V-225652`

### Rule: The firewall protecting the Samsung SDS EMM platform must be configured to restrict all network traffic to and from all addresses with the exception of ports, protocols, and IP address ranges required to support Samsung SDS EMM and platform functions.

**Rule ID:** `SV-225652r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Most information systems are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations. Since Samsung SDS EMM is a critical component of the mobility architecture and must be configured to enable only those ports, protocols, and services (PPS) necessary to support functionality, all others must be expressly disabled or removed. A firewall installed on the Samsung SDS EMM provides a protection mechanism to ensure unwanted service requests do not reach the Samsung SDS EMM and outbound traffic is limited to only Samsung SDS EMM functionality. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142, PP-MDM-43100</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and IP address ranges necessary to support Samsung SDS EMM and platform functionality. A list can usually be found in the STIG Supplemental document or MDM product documentation. Compare the list against the configuration of the firewall and identify discrepancies. If the host-based firewall is not configured to support only ports, protocols, and IP address ranges necessary for operation, this is a finding.

## Group: PP-MDM-431006

**Group ID:** `V-225653`

### Rule: The firewall protecting the Samsung SDS EMM platform must be configured so that only DoD-approved ports, protocols, and services are enabled. See the DoD Ports, Protocols, Services Management [PPSM] Category Assurance Levels [CAL] list for DoD-approved ports, protocols, and services.

**Rule ID:** `SV-225653r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All ports, protocols, and services used on DoD networks must be approved and registered via the DoD PPSM process. This is to ensure that a risk assessment has been completed before a new port, protocol, or service is configured on a DoD network and has been approved by proper DoD authorities. Otherwise, the new port, protocol, or service could cause a vulnerability to the DoD network, which could be exploited by an adversary. SFR ID: FMT_SMF.1.1(2) b / CM-7 b Satisfies: SRG-APP-000142, PP-MDM-431006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the MDM administrator for a list of ports, protocols, and services that have been configured on the host-based firewall of the Samsung SDS EMM or generate the list by inspecting the firewall. Verify all allowed ports, protocols, and services are included on the DoD PPSM CAL list. If any allowed ports, protocols, and services on the MDM host-based firewall are not included on the DoD PPSM CAL list, this is a finding.

## Group: PP-MDM-431010

**Group ID:** `V-225654`

### Rule: The Samsung SDS EMM must limit the number of concurrent sessions to one session for all accounts and/or account types.

**Rule ID:** `SV-225654r835013_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by using information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. SFR ID: FMT_SMF.1.1(2) b / AC-10 Satisfies: SRG-APP-000001, PP-MDM-431010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM configuration settings and verify the server is configured to limit the number of concurrent sessions to one session for all accounts and/or account types. On the MDM console, do the following: 1. Log in to the Admin Console using a web browser. 2. Go to Setting >> Server >> Configuration and verify Multiple login is set to "Disallow." If the MDM console Multiple login is not set to "Disallow", this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-225655`

### Rule: The Samsung SDS EMM must automatically disable accounts after a 35 day period of account inactivity (local accounts).

**Rule ID:** `SV-225655r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers that are able to exploit an inactive account can potentially obtain and maintain undetected access to an application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Applications need to track periods of user inactivity and disable accounts after 35 days of inactivity. Such a process greatly reduces the risk that accounts will be hijacked, leading to a data compromise. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality. This policy does not apply to either emergency accounts or infrequently used accounts. Infrequently used accounts are local login administrator accounts used by system administrators when network or normal logon/access is not available. Emergency accounts are administrator accounts created in response to crisis situations. SFR ID: FMT_SMF.1(2)b. / AC-2(3) Satisfies: SRG-APP-000025, PP-MDM-991000</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Samsung SDS EMM server documentation and configuration settings to determine if the admin account is automatically disabled after 35 days. On the MDM console, verify that the MDM console Inactivity Limit on Admin Accounts (days) is set to "35". If sub-administrators or read-only administrators do not sign in for 35 days, their accounts are locked. If the MDM console Inactivity Limit on Admin Accounts (days) is not set to "35", this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-225656`

### Rule: The Samsung SDS EMM must enforce the limit of three consecutive invalid logon attempts by a user.

**Rule ID:** `SV-225656r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. SFR ID: FMT_SMF.1(2)b. / IA-7-a Satisfies: SRG-APP-000065, PP-MDM-991000</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM configuration settings and verify the server is configured to enforce the limit of three consecutive invalid logon attempts by admin. On the MDM console, verify that the MDM console "Maximum Failed Login Attempts" is set to "3". If the administrator incorrectly enters the login password three times, the account is locked. If the MDM console Maximum Failed Login Attempts is not set to "3", this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-225657`

### Rule: The Samsung SDS EMM must use multifactor authentication for local access to privileged accounts.

**Rule ID:** `SV-225657r588007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, privileged users must use multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication is defined as using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network. Applications integrating with the DoD Active Directory and using the DoD CAC are examples of compliant multifactor authentication solutions. SFR ID: FMT_SMF.1(2)b. / IA-2(3) Satisfies: SRG-APP-000151, PP-MDM-991000</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Samsung SDS EMM configuration settings and verify the server is configured to use multifactor authentication for local access to privileged accounts. On the MDM console, do the following: 1. In the Admin Console login page, enter the Admin ID and password and click the "Sign in" button. 2. Enter the OTP (one-time password) in the pop-up by sending SMS or email that is registered in admin account information. 3. Login is successful. If the OTP pop-up does not display, this is a finding.

## Group: PP-MDM-414002

**Group ID:** `V-245525`

### Rule: The Samsung SDS EMM must be configured to leverage the MDM platform administrator accounts and groups for Samsung SDS EMM user identification and CAC authentication.

**Rule ID:** `SV-245525r744387_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SDS EMM is leveraging the MDM platform administrator accounts and groups for user (system administrator) identification and CAC authentication. Use one of the following methods: Method 1: - Attempt to log on to the SDS EMM console using a CAC. - Verify CAC log on was successful. Method 2: - Log in to the SDS EMM console. - Go to Settings >> Server >> Configuration. - Click "CAC Sign-In". - Verify CAC Sign-In has been set up. If SDS EMM is not leveraging the MDM platform administrator accounts and groups for user (system administrator) identification and CAC authentication, this is a finding.

## Group: PP-MDM-414003

**Group ID:** `V-245526`

### Rule: Authentication of MDM platform accounts must be configured so they are implemented via an enterprise directory service.

**Rule ID:** `SV-245526r744388_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). SFR ID: FIA</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SDS EMM is leveraging the MDM platform administrator accounts and groups for user (system administrator) identification and CAC authentication. Use one of the following methods: Method 1: - Attempt to log on to the SDS EMM console using a CAC. - Verify CAC log on was successful. Method 2: - Log in to the SDS EMM console. - Go to Settings >> Server >> Configuration. - Click "CAC Sign-In". - Verify CAC Sign-In has been set up. If SDS EMM is not leveraging the MDM platform administrator accounts and groups for user (system administrator) identification and CAC authentication, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-245527`

### Rule: The Samsung SDS EMM local accounts password must be configured with length of 15 characters.

**Rule ID:** `SV-245527r744391_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (a)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Samsung SDS EMM local accounts have been configured with a password with length of 15 characters or more. 1. Log into the SDS EMM console. 2. Go to Setting >> Server >> Configuration >> Minimum Password Length. 3. Verify the Minimum Password Length is set to 15 or more. If the Minimum Password Length is not set to 15 or more, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-245528`

### Rule: The Samsung SDS EMM local accounts must be configured with password maximum lifetime of 60 Days.

**Rule ID:** `SV-245528r836815_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (d)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Samsung SDS EMM local accounts have been configured to prohibit password reuse for a minimum of five generations. 1. Log in to the SDS EMM console. 2. Go to Setting >> Server >> Configuration >> Manage Password History (Times). 3. Verify the Manage Password History (Times) is set to 5. If the Manage Password History (Times) is not set to 5, this is a finding.

## Group: PP-MDM-991000

**Group ID:** `V-245529`

### Rule: The Samsung SDS EMM local accounts must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-245529r836816_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. SFR ID: FMT_SMF.1(2)b. / IA-5 (1) (e)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Samsung SDS EMM local accounts have been configured to prohibit password reuse for a minimum of five generations. 1. Log in to the SDS EMM console. 2. Go to Setting >> Server >> Configuration >> Manage Password History (Times). 3. Verify the Manage Password History (Times) is set to 5. If the Manage Password History (Times) is not set to 5, this is a finding.

