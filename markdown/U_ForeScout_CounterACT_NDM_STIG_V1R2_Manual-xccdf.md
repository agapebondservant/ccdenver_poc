# STIG Benchmark: ForeScout CounterACT NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255624`

### Rule: CounterACT must terminate all network connections associated with an Enterprise Manager Console session upon Exit, or session disconnection, or after 10 minutes of inactivity, except where prevented by documented and validated mission requirements.

**Rule ID:** `SV-255624r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
CounterACT is inherently designed to terminate upon Exit or session disconnection, thus this part of the requirement does not have to be verified. To verify the device is configured to terminate management sessions after "10" minutes of inactivity, verify the timeout value is configured. 1. On the Enterprise Manager Console. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "User Inactivity Timeout" check box is selected and the associated setting is set to "10" minutes. If applicable, verify exceptions to this requirement are documented and signed. If Counteract does not terminate the connection associated with an Enterprise Manager Console at the end of the session or after "10" minutes of inactivity, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255625`

### Rule: CounterACT must terminate all network connections associated with an SSH connection session upon Exit, session disconnection, or after 10 minutes of inactivity, except where prevented by documented and validated mission requirements.

**Rule ID:** `SV-255625r961068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
CounterACT is inherently designed to terminate upon Exit or session disconnection, thus this part of the requirement does not have to be verified. To verify the device is configured to terminate management sessions after "10" minutes of inactivity, verify the timeout value is configured. 1. On the Enterprise Manager Console. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "User Inactivity Timeout" check box is selected and the associated setting is set to "10" minutes. If applicable, verify exceptions to this requirement are documented and signed. If Counteract does not terminate the connection associated with an Enterprise Manager Console at the end of the session or after "10" minutes of inactivity, this is a finding.

## Group: SRG-APP-000231-NDM-000271

**Group ID:** `V-255626`

### Rule: CounterACT must allow only authorized administrators to view or change the device configuration, system files, and other files stored either in the device or on removable media.

**Rule ID:** `SV-255626r961128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This protection is required to prevent unauthorized alteration, corruption, or disclosure of information when not stored directly on the network device. Files on the network device or on removable media used by the device must have their permissions set to allow read or write access to those accounts that are specifically authorized to access or change them. Note that different administrative accounts or roles will have varying levels of access. File permissions must be set so that only authorized administrators can read or change their contents. Whenever files are written to removable media and the media is removed from the device, the media must be handled appropriately for the classification and sensitivity of the data stored on the device. Flash drive usage must comply with DoD external storage and flash drive policy which includes permission to use and malware verification processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
List the contents of CounterACT’s local storage, including any drives supporting removable media (such as flash drives), and check the file permissions of all files on those drives. 1. Log on to the SSH command line interface of a CounterACT Enterprise Manager (EM) or CounterACT appliance using standard admin privilege. 2. At the command prompt, type: cd / (To narrow the search to a specific LINUX directory, replace the / with the full pathname of the directory to be searched.) 3. Use the following command to review file permissions: ls- la If any files allow read or write access by accounts not specifically authorized access or access using non-privileged accounts, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255627`

### Rule: CounterACT must restrict the ability to change the auditing to be performed within the system log based on selectable event criteria to the audit administrators role or to other roles or individuals.

**Rule ID:** `SV-255627r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to effectively respond, and important forensic information may be lost. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations. In addition, auditing may be limited to a specific set of events to facilitate audit reduction, analysis, and reporting. Organizations can establish time thresholds in which audit actions are changed, for example, in near real time, within minutes, or within hours. The individuals or roles to change the auditing are dependent on the security configuration of the network device. For example, it may be configured to allow only some administrators to change the auditing, while other administrators can review audit logs but not reconfigure auditing. Because this capability is so powerful, organizations should be extremely cautious about only granting this capability to fully authorized security personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT restricts the ability to change the auditing to be performed within the system log based on selectable event criteria to the audit administrator's role or to other roles or individuals. This requirement may be verified by configuration review or demonstration. 1. Open the CounterACT Administrator Console and log on with admin or operator credentials. 2. Select Tools >> Options >> Console User Profiles. 3. Select (highlight) the user profile to be reviewed (group or user) and then select "Edit". 4. Review the "Permissions" tab and verify the following "update" radio check boxes are enabled: Action Thresholds, CounterACT Appliance Configuration, and Enterprise Manager Control. If CounterACT does not provide the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near real time, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-255628`

### Rule: CounterACT must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-255628r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is expressed in UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT records time stamps for audit records that can be mapped to UTC. This requirement may be verified by demonstration or configuration review. Verify by connecting to the appliance via SSH using standard user/operator privilege. 1. After logon, type the following command at the prompt using the IP address of the configured NTP server: fstool ntp test <ip address> 2. Verify the date references accurate time and the time zone points to UTC next to the year. If CounterACT does not record time stamps for audit records that can be mapped to UTC, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255629`

### Rule: CounterACT must enable Threat Protection notifications to alert security personnel to Cyber events detected by a CounterACT IAW CJCSM 6510.01B.

**Rule ID:** `SV-255629r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>CJCSM 6510.01B, "Cyber Incident Handling Program", in subsection e.(6)(c) sets forth requirements for Cyber events detected by an automated system. By immediately displaying an alarm message, potential security violations can be identified more quickly even when administrators are not logged into the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Threat Protection notifications are enabled and configured. 1. Select Tools >> Options >> Threat Protection. 2. At the bottom of the Threat Protection pane, select "Customer" and then select the "Notify" tab. 3. Verify the Maximum emails per day is set to "15" and infected host notification is set to 1 hour. If CounterACT does not enable Threat Protection notifications to alert security personnel to Cyber events detected by a CounterACT IAW CJCSM 6510.01B, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-255630`

### Rule: CounterACT must generate audit log events for a locally developed list of auditable events.

**Rule ID:** `SV-255630r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT generates audit log events for a locally developed list of auditable events. 1. Open the CounterACT Console. 2. Select Tools >> Options >> Plugin. 3. Select the Syslog Plugin. 4. Select CounterACT or the Enterprise Manager appliance you would like to verify. 5. Verify additional settings for audit are available by ensuring that either one of these options is selected: "Include only messages generated by the 'send message to syslog action'" or "include NAC policy logs". If CounterACT is not configured to generate audit log events for a locally developed list of auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-255631`

### Rule: CounterACT must enforce access restrictions associated with changes to the system components.

**Rule ID:** `SV-255631r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, ACLs, and policy filters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check CounterACT to determine if only authorized administrators have permissions for changes, deletions, and updates on the network device. Inspect the maintenance log to verify changes are being made only by the system administrators. 1. Log on to the CounterACT Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> User Console and Options. 3. Select (highlight) the user profile to be reviewed (group or user) and then select "Edit". 4. Verify the non-administrator account selected does not have "update" on the "Permissions" tab for "CounterACT Appliance Configuration". If unauthorized users are allowed to change the hardware or software, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255632`

### Rule: Administrative accounts for device management must be configured on the authentication server and not the network device itself (except for the account of last resort).

**Rule ID:** `SV-255632r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which leads to delays in remediating production problems and addressing compromises in a timely fashion. Administrative accounts for network device management must be configured on the authentication server and not the network device itself. This requirement does not apply to the account of last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CounterACT configuration to determine if administrative accounts for device management exist on the device other than the account of last resort and root account. 1. Log on to the CounterACT Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> User Console and Options. 3. Select (highlight) the user profile to be reviewed (group or user) and then select "Edit". 4. Verify each user profile is for an approved administrator. 5. Verify each external LDAP group account profile by verifying on the trusted external directory group membership. If any administrative accounts other than the account of last resort and root account exist on the device, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-255633`

### Rule: CounterACT must support organizational requirements to conduct backups of system-level information contained in the information system when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-255633r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who use this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check CounterACT to determine if the network device is configured to conduct backups of system-level information contained in the information system when changes occur or weekly, whichever is sooner. 1. Open CounterACT Console and select Tools >> Options. 2. Select the "+" next to "Advanced" menu (toward the bottom). 3. Select the “Backup” submenu. 4. On the “System Backup” tab, verify the "Enable System Backup" radio button is selected. 5. Verify the Backup schedule is selected to at least "weekly". If CounterACT does not support the organizational requirements to conduct backups of system-level data according to the defined frequency, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-255634`

### Rule: CounterACT must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-255634r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CounterACT backup configuration to determine if the network device backs up the information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner. 1. Open the CounterACT Console and select Tools >> Options. 2. Select the "+" next to "Advanced" menu (toward the bottom). 3. Select the “Backup” submenu. 4. On the “System Backup” tab, verify the "Enable System Backup" radio button is selected. 5. Verify the Backup schedule is selected to at least "weekly". If the network device does not back up the information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255635`

### Rule: CounterACT must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255635r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this certification authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT obtains public key certificates from an appropriate certificate policy through an approved service provider. To review the Web server certificate presented for captive portal/authentication: 1. Open a command line SSH to CounterACT appliance or Enterprise Manager. 2. Run the following command: >fstool cert test 3. Verify all Web server certificate(s) are printed and reviewable. 4. Verify the signing authority is from an approved certificate authority. If the network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255636`

### Rule: CounterACT must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255636r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this certification authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT obtains public key certificates from an appropriate certificate policy through an approved service provider. 1. Open a command line SSH to CounterACT appliance or Enterprise Manager. 2. Run the following command: >fstool dot1x cert print <pathname/filename> for the local server certificate (/usr/local/forescout/etc/dot1x/certs.production/server.pem) 3. Verify the signing authority is from an approved certificate authority. If the network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255637`

### Rule: For the local account, CounterACT must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-255637r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Nonlocal account are configured on the authentication server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT is configured either to enforce the limit of three consecutive invalid logon attempts by a user during a "15" minute time period or to use an authentication server that would perform this function. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "Lock account after" radio button is selected. 4. Verify that "3" password failures for "15" minutes is configured. If the limit of three consecutive invalid logon attempts by a user during a "15" minute time period is not enforced, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-255638`

### Rule: CounterACT must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-255638r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to CounterACT ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Enable "Display this Notice and Consent Message after login" and complete the provided text input area to have the Standard Mandatory DoD and Consent Banner appear before granting access to the device. This banner must include the following text: By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details". If this is not present, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-255639`

### Rule: CounterACT must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-255639r960846_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The administrator must acknowledge the banner prior to CounterACT allowing the administrator access to CounterACT. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of CLI access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, and then entering the password is also acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify CounterACT retains the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and takes explicit actions to log on for further access. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the options for the logon banner "require confirmation" is selected. If CounterACT does not retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255640`

### Rule: If any logs are stored locally which are not sent to the centralized audit server, CounterACT must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-255640r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes ensuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to ensure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement can be met by using of a syslog/audit log server if the device is configured to send logs to that server. Backup requirements would be levied on the target server but are not a part of this check.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If all audit logs for the Enterprise Manager and appliances are sent to an audit log, this is not a finding. Determine if CounterACT backs up local logs on the Enterprise Manager or appliances at least every seven days onto a different system or system component than the system or component being audited. This requirement may be verified by configuration review. 1. Open the CounterACT Console and select Tools >> Options. 2. Select the "+" next to "Advanced" menu (toward the bottom). 3. Select the “Backup” submenu. 4. On the "System Backup" tab, verify the "Enable System Backup" radio button is selected. 5. Verify the Backup schedule is selected to at least "weekly". 6. On the "Backup Server" tab, verify an external backup server is configured with SFTP or SCP (and appropriate port/protocol requirements). If the network device does not back up audit records at least every seven days onto a different system or system component than the system or component being audited, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-255641`

### Rule: CounterACT must limit privileges to change the software resident within software libraries.

**Rule ID:** `SV-255641r960960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. If CounterACT were to enable unauthorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask if there are users defined in CounterACT that are not authorized to change the software libraries. Verify that Administrator privileges have been restricted for these users. This is verified by reviewing the administrator account profiles and auditing the assigned privilege for updated CounterACT software. 1. Log on to the CounterACT Console and select Tools >> Options >> Console User Profiles. 2. Select the non-privileged user profiles and then select "Edit". 3. Verify the users do not have the "Plugin Management" and "Software Upgrade" options selected. If CounterACT is not configured to limit privileges to change the software resident within software libraries for unauthorized users, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-255642`

### Rule: CounterACT must disable all unnecessary and/or nonsecure plugins.

**Rule ID:** `SV-255642r960966_rule`
**Severity:** high

**Description:**
<VulnDiscussion>CounterACT is capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. If the 802.1x plugin is installed and there are no wireless APs or controllers directly managed by CounterACT, the wireless plugin should be disabled. The wireless plugin enabled with no configuration will also produce a finding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the plugin tool and remove all unneeded or unsecure services. 1. Connect to the CounterACT Console and select Tools >> Options >> Plugins. 2. Review the list of plugins. If an unnecessary or nonsecure service is "Enabled", select the plugin and then select "Configure". If no configuration is present, this is a finding. If any unnecessary or nonsecure functions are enabled, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-255643`

### Rule: In the event the authentication server is unavailable, one local account must be created for use as the account of last resort.

**Rule ID:** `SV-255643r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on CounterACT's local database for use in an emergency, such as when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since the emergency administration account is strictly intended to be used only as a last resort when immediate administrative access is absolutely necessary. The number of local accounts is restricted to one. The username and password for the emergency account is contained within a sealed envelope kept in a safe. All other users/groups should leverage the external directory. Remove any other accounts using Single-Local. The default admin account may be used to fulfill this requirement (requires DoD compliant password or cryptographically generated shared secret).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only one local account exists and it has full administrator privileges. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options. If more than one local user account exists, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255644`

### Rule: CounterACT must enforce a minimum 15-character password length.

**Rule ID:** `SV-255644r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces a minimum 15-character password length. This requirement may be verified by demonstration or configuration review. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "minimum length" is configured for "15". If CounterACT does not enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255645`

### Rule: CounterACT must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-255645r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT prohibits password reuse for a minimum of five generations. This requirement may be verified by demonstration or configuration review. 1. Verify if the user profiles are using external authentication server or local. If using local, proceed to Step 2. If using external, verify the settings using the Authentication Server configuration guide. 2. Log on to the CounterACT Administrator UI. 3. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 4. Verify the "Last" radio button is selected and the option with "5" passwords cannot be reused is configured. If CounterACT does not prohibit password reuse for a minimum of five generations, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-255646`

### Rule: CounterACT must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-255646r984099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify CounterACT enforces password complexity by requiring that at least one numeric character be used. This requirement may be verified by demonstration, configuration review, or validated test results. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the complexity requirements are met. If CounterACT does not require that at least one numeric character be used in each password, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-255647`

### Rule: CounterACT must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-255647r984100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify CounterACT enforces password complexity by requiring that at least one special character be used. This requirement may be verified by demonstration, configuration review, or validated test results. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the complexity requirement for use of at least one special character is met. If CounterACT does not require that at least one special character be used in each password, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255648`

### Rule: CounterACT must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-255648r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include root account or the account of last resort which are meant for access to the network device in case of failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT enforces a 60-day maximum password lifetime. This requirement may be verified by demonstration or configuration review. This requirement does not include root account or the account of last resort. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "password expires after" radio button is selected and configured to 60 days. If CounterACT does not enforce a 60-day maximum password lifetime, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255649`

### Rule: CounterACT must automatically lock the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded.

**Rule ID:** `SV-255649r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine CounterACT automatically locks the account until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded. This requirement may be verified by demonstration or configuration review. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "Lock account After" radio button is selected. 4. Verify "3" is selected for the password failures setting. 5. Verify that "15" and "minutes" are selected. If an account is not automatically locked out until the locked account is released by an administrator when three unsuccessful logon attempts in 15 minutes are exceeded, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255650`

### Rule: CounterACT must compare internal information systems clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-255650r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the network device configuration to determine if the device compares internal information system clocks at least every 24 hours with an authoritative time server. 1. Open an SSH session and authenticate to the CounterACT command line. 2. Verify the configured NTP servers with the command "fstool ntp". 3. Run the "date" command to look at the current system time compared to the known good, Network Time Protocol (NTP) server time. If the device does not compare internal information system clocks at least every 24 hours, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-255651`

### Rule: CounterACT must be configured to synchronize internal information system clocks with the organizations primary and secondary NTP servers.

**Rule ID:** `SV-255651r987682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. CounterACT appliances must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT is configured to synchronize internal clocks with the organization's primary and secondary NTP servers. 1. Open an SSH session and authenticate to the CounterACT command line. 2. Verify a primary and secondary NTP server has been configured with the command "fstool ntp". If CounterACT is not configured to synchronize internal information system clocks with the organization's primary and secondary NTP servers, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255652`

### Rule: CounterACT must authenticate any endpoint used for network management before establishing a local, remote, and/or network connection using cryptographically based bidirectional authentication.

**Rule ID:** `SV-255652r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication. Use of non-secure versions of management protocols with well-known exploits puts the system at immediate risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CounterACT configuration to determine if the network device authenticates network management endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based. 1. Select Tools >> Options >> Switch. 2. Select a network device and review the "CLI" tab. 3. If the radio button for "Use CLI" is selected, verify that the "SSH" drop-down option is also selected. Repeat this process for each switch. If anything other than SSH is selected, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-255653`

### Rule: CounterACT must authenticate SNMPv3 endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255653r961506_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). For network device management, this has been determined to be network management device addresses, SNMP authentication, and NTP authentication. Use of non-secure versions of management protocols with well-known exploits puts the system at immediate risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CounterACT configuration to determine if the network device authenticates SNMP endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based. 1. Select Tools >> Options >> Switch. 2. Select a network device and review the "SNMP" tab. 3. Verify that the "SNMPv3" option is selected and the "HMAC-SHA" authentication protocol is selected. 4. Verify that the "use privacy" radio button is selected and "AES-128" is also selected from the drop-down box. If CounterACT does not authenticate the endpoint devices before establishing a connection using bidirectional authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000408-NDM-000314

**Group ID:** `V-255654`

### Rule: CounterACT appliances performing maintenance functions must restrict use of these functions to authorized personal only.

**Rule ID:** `SV-255654r961545_rule`
**Severity:** high

**Description:**
<VulnDiscussion>There are security-related issues arising from software brought into the network device specifically for diagnostic and repair actions (e.g., a software packet sniffer installed on a device to troubleshoot system traffic or a vendor installing or running a diagnostic application to troubleshoot an issue with a vendor-supported device). If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. This requirement addresses security-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational network devices. Maintenance tools can include hardware, software, and firmware items. Maintenance tools are potential vehicles for transporting malicious code, either intentionally or unintentionally, into a facility and subsequently into organizational information systems. Maintenance tools can include, for example, hardware/software diagnostic test equipment and hardware/software packet sniffers. This requirement does not cover hardware/software components that may support information system maintenance yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device restricts the use of maintenance functions to authorized personnel only. View the list of users defined on the device. Select Tools >> Options >> Console User Profiles. If other personnel can use maintenance functions on the network device, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-255655`

### Rule: CounterACT must sent audit logs to a centralized audit server (i.e., syslog server).

**Rule ID:** `SV-255655r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the CounterACT configuration to determine if the device off-loads audit records onto a different system or media than the system being audited. 1. From the console, select Tools >> Options >> Plugins >> Syslog. 2. Verify the Syslog Plugin is running (on all CounterACT appliances). 3. Open the Plugin, selecting the appliance configuration for review. 4. Verify the "Send To" tab has an available log server properly configured. 5. Verify the Events Filtering includes ALL events, except the "Include only messages generated by the 'Send Message to Syslog' Action". This item should remain unchecked. If the device does not off-load audit records onto a different system or media, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255656`

### Rule: CounterACT must employ automated mechanisms to centrally apply authentication settings.

**Rule ID:** `SV-255656r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which leads to delays in remediating production problems and addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network device configuration to determine if it employs automated mechanisms to centrally apply authentication settings. 1. Connect to the User Directory Console user interface. 2. Select Tools >> Options >> User Directory. 3. Verify the Active Directory configuration exists and tests pass by selecting the chosen directory and selecting "Test". If authentication settings are not applied centrally using automated mechanisms, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-255657`

### Rule: CounterACT must limit the number of concurrent sessions to an organization-defined number for each administrator account type.

**Rule ID:** `SV-255657r960735_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Network device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT requires a limit of one session per user. This requirement may be verified by demonstration or configuration review. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "allow only one login session per user" radio button is selected and configured to either Log out existing session or Deny new logon attempts. If CounterACT does not enforce one session per user, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255658`

### Rule: The network device must be configured to use a centralized authentication server to authenticate privileged users for remote and nonlocal access for device management.

**Rule ID:** `SV-255658r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of authentication servers or other centralized management servers for providing centralized authentication services is required for network device management. Maintaining local administrator accounts for daily usage on each network device without centralized management is not scalable or feasible. Without centralized management, it is likely that credentials for some network devices will be forgotten, leading to delays in administration, which itself leads to delays in remediating production problems and in addressing compromises in a timely fashion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the CounterACT configuration to determine if an authentication server is required to access the device. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Directory. 3. Verify the selected authentication server is enabled for GUI authentication. If an authentication server is not configured for use by CounterACT, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-255659`

### Rule: If multifactor authentication is not supported and passwords must be used, CounterACT must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-255659r984095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT requires at least one upper-case character to be used in passwords. This requirement may be verified by demonstration or configuration review. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "password must contain at least # upper case alphabetic characters" radio button is selected and configured to at least 1. If CounterACT does not enforce at least one upper-case character, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-255660`

### Rule: If multifactor authentication is not supported and passwords must be used, CounterACT must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-255660r984098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some devices may not have the need to provide a group authenticator; this is considered a matter of device design. In those instances where the device design includes the use of a group authenticator, this requirement will apply. This requirement applies to accounts created and managed on or by the network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if CounterACT requires at least one lower-case character to be used in passwords. This requirement may be verified by demonstration or configuration review. 1. Log on to the CounterACT Administrator UI. 2. From the menu, select Tools >> Options >> User Console and Options >> Password and Login. 3. Verify the "password must contain at least # lower case alphabetic characters" radio button is selected and configured to at least 1. If CounterACT does not enforce at least one lower-case character, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-255661`

### Rule: The network device must terminate shared/group account credentials when members leave the group.

**Rule ID:** `SV-255661r984107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples of credentials include passwords and group membership certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation to verify that a procedure exists to change the account of last resort and root account password when users with knowledge of the password leave the group. If a procedure does not exist to change the account of last resort and root account password when users with knowledge of the password leave the group, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-265636`

### Rule: The version of ForeScout CounterAct must be a supported version.

**Rule ID:** `SV-265636r997800_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified period from the availability of the update. The specific period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
ForeScout CounterAct versions supported by this STIG (Version 8 and earlier) are no longer supported by the vendor. If the system is running any CounterAct version, this is a finding.

