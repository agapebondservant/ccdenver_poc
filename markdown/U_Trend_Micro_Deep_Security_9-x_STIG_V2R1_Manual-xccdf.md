# STIG Benchmark: Trend Micro Deep Security 9.x Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-241108`

### Rule: Trend Deep Security must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-241108r879511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the number of concurrent sessions is limited to one. In the administration console go to: System Settings >> Security >> Number of concurrent sessions allowed per User Review the policy to ensure no more than 1 session is permitted. If more than 1 session is permitted this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-241109`

### Rule: Trend Deep Security must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-241109r879513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system-level and results in a system lock, but may be at the application-level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure a session lock is initiated after a 15-minute period of inactivity. Review the application System Settings, to ensure the system timeout is set to 15 minutes or less. If the timeout session is not set to 15 minutes or less this is a finding. Administration >> System Settings >> Security >> User Security >> Session Timeout: 10 Minutes

## Group: SRG-APP-000023

**Group ID:** `V-241110`

### Rule: Trend Deep Security must provide automated mechanisms for supporting account management functions.

**Rule ID:** `SV-241110r879522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enterprise environments make application account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended or terminated or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. The application must be configured to automatically provide account management functions and these functions must immediately enforce the organization's current account policy. The automated mechanisms may reside within the application itself or may be offered by the operating system or other infrastructure providing automated account management capabilities. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure automated mechanisms for supporting account management functions are automated. Interview the ISSO to determine a list of authorized users and their perspective roles supporting the application. Review the identified users within the following: Administration >> User Management >> Users >> Assign Role If the identified users do not match the roles assigned within the application this is a finding.

## Group: SRG-APP-000026

**Group ID:** `V-241111`

### Rule: Trend Deep Security must automatically audit account creation.

**Rule ID:** `SV-241111r879525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Auditing of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application owners exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure account creation is automatically audited. Verify "User Created" events is enabled by reviewing the following: Administration >> System Settings >> System Events >> Enable Event ID 650 User Created. Select: Record Select: Forward If "User Created" is not enabled this is a finding.

## Group: SRG-APP-000027

**Group ID:** `V-241112`

### Rule: Trend Deep Security must automatically audit account modification.

**Rule ID:** `SV-241112r879526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply modify an existing account. Auditing of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail documents the creation of application user accounts and, as required, notifies administrators and/or application owners exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure account creation is automatically audited. Verify "User Updated" events is enabled by reviewing the following: Administration >> System Settings >> System Events >> Enable Event ID 652 User Updated. Select: Record Select: Forward If "User Updated" is not enabled this is a finding.

## Group: SRG-APP-000028

**Group ID:** `V-241113`

### Rule: Trend Deep Security must automatically audit account disabling actions.

**Rule ID:** `SV-241113r879527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events affecting user accessibility and application processing, applications must audit account disabling actions and, as required, notify the appropriate individuals, so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/audit mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure account disabling actions are automatically audited. Verify "User Locked Out" events are enabled by reviewing the following: Administration >> System Settings >> System Events >> Enable Event ID 603 User Locked Out. Select: Record Select: Forward If "User Locked Out" is not enabled this is a finding.

## Group: SRG-APP-000029

**Group ID:** `V-241114`

### Rule: Trend Deep Security must automatically audit account removal actions.

**Rule ID:** `SV-241114r879528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events affecting user accessibility and application processing, applications must audit account removal actions and, as required, notify the appropriate individuals, so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/audit mechanisms meeting or exceeding access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure account removal actions are automatically audited. Verify "User Deleted" events are enabled by reviewing the following: Administration >> System Settings >> System Events >> Enable Event ID 651 User Deleted. Select: Record Select: Forward If "User Deleted" is not enabled this is a finding.

## Group: SRG-APP-000038

**Group ID:** `V-241115`

### Rule: Trend Deep Security must enforce approved authorizations for controlling the flow of information within the system based on organization-defined information flow control policies.

**Rule ID:** `SV-241115r879533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all system information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data. Application specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services, or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure approved authorizations for controlling the flow of information within the system based on organization-defined information flow control policies are enforced. Interview the ISSO in order to identify all users with permissions to the application. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000039

**Group ID:** `V-241116`

### Rule: Trend Deep Security must enforce approved authorizations for controlling the flow of information between interconnected systems based on organization-defined information flow control policies.

**Rule ID:** `SV-241116r879534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If information flow is not enforced based on approved authorizations, the system may become compromised. Information flow control regulates where information is allowed to travel within a system and between interconnected systems. The flow of all application information must be monitored and controlled so it does not introduce any unacceptable risk to the systems or data. Application specific examples of enforcement occurs in systems that employ rule sets or establish configuration settings that restrict information system services, or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of information between interconnected systems in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure approved authorizations for controlling the flow of information between interconnected systems based on organization-defined information flow control policies are enforced. Interview the ISSO in order to identify all users with permissions to the application. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-241117`

### Rule: Trend Deep Security must enforce the limit of three consecutive invalid logon attempts by a user during a 15 minute time period.

**Rule ID:** `SV-241117r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the limit of three consecutive invalid logon attempts by a user during a 15-minute time period is enforced. Verify the number of failed logon attempts. Go to Administration >> System Settings >> Security >> User Security >> Number of incorrect sign-in attempts allowed (before lock out): 3 If the number is greater than 3 this is a finding.

## Group: SRG-APP-000073

**Group ID:** `V-241118`

### Rule: Trend Deep Security must scan all media used for system maintenance prior to use.

**Rule ID:** `SV-241118r879550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are security-related issues arising from software brought into the information system specifically for diagnostic and repair actions (e.g., a software packet sniffer installed on a system in order to troubleshoot system traffic, or a vendor installing or running a diagnostic application in order to troubleshoot an issue with a vendor supported system). If, upon inspection of media containing maintenance diagnostic and test programs, organizations determine that the media contain malicious code, the incident is handled consistent with organizational incident handling policies and procedures. This requirement addresses security-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational information systems. Maintenance tools can include hardware, software, and firmware items. Maintenance tools are potential vehicles for transporting malicious code, either intentionally or unintentionally, into a facility and subsequently into organizational information systems. Maintenance tools can include, for example, hardware/software diagnostic test equipment and hardware/software packet sniffers. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure all media used for system maintenance is scanned prior to use. Verify Anti-Malware is enabled on each server that is applicable to the accreditation boundary. Go to Computers. Right-click a computer from the list of systems, select properties Anti-Malware >> General Verify Configuration is set to "On" or "Inherit On". If Verify Configuration is set to "Off", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-241119`

### Rule: Trend Deep Security must provide audit record generation capability for DoD-defined auditable events within all application components.

**Rule ID:** `SV-241119r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the application will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit record generation capability for DoD-defined auditable events within all application components is provided. Verify the Administration >> System Settings >> System Events, are set to “Record.” - capture successful and unsuccessful logon attempts, - privileged activities or other system level access, - starting and ending time for user access to the system - concurrent logons from different workstations - successful and unsuccessful accesses to objects - all program initiations, - all direct access to the information system, - all account creation, modification, disabling, and termination actions. If these settings are not set to “Record”, this is a finding.

## Group: SRG-APP-000090

**Group ID:** `V-241120`

### Rule: Trend Deep Security must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be audited.

**Rule ID:** `SV-241120r879560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure only the ISSM (or individuals or roles appointed by the ISSM) is allowed to select which auditable events are to be audited. Verify the user roles and assigned permissions within the Administration >> User Management >> Roles >> Properties >> Other Rights. If a user role (e.g., Auditor) has any "View Only" for Alerts, Alert Configuration, Integrity Monitoring, and Log Inspection Rules, this is a finding.

## Group: SRG-APP-000091

**Group ID:** `V-241121`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-241121r879561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure only the ISSM (or individuals or roles appointed by the ISSM) is allowed to select which auditable events are to be audited. Verify the following events within the Administration >> System Settings >> System Events, are set to “Record.” 660 Role Created 661 Role Deleted 662 Role Updated 663 Roles Imported 664 Roles Exported If these settings are not set to “Record”, this is a finding.

## Group: SRG-APP-000092

**Group ID:** `V-241122`

### Rule: Trend Deep Security must initiate session auditing upon startup.

**Rule ID:** `SV-241122r879562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure session auditing upon startup is initiated. Verify the following events within the Administration >> System Settings >> System Events, are set to “Record.” 600 User Signed In 601 User Signed Out 602 User Timed Out 603 User Locked Out 608 User Session Validation Failed 610 User Session Validated If these settings are not set to “Record”, this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-241123`

### Rule: Trend Deep Security must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-241123r879570_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the ISSO and SA (at a minimum) are alerted in the event of an audit processing failure. Verify any audit processing failure events within Administration >> System Settings >> System Events, are set to “Forward” If these settings are not set to “Forward”, this is a finding.

## Group: SRG-APP-000118

**Group ID:** `V-241124`

### Rule: Trend Deep Security must protect audit information from any type of unauthorized read access.

**Rule ID:** `SV-241124r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit information from any type of unauthorized read access is protected. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000119

**Group ID:** `V-241125`

### Rule: Trend Deep Security must protect audit information from unauthorized modification.

**Rule ID:** `SV-241125r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions, and limiting log data locations. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights that the user enjoys in order to make access decisions regarding the modification of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit information is protected from unauthorized modification. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000120

**Group ID:** `V-241126`

### Rule: Trend Deep Security must protect audit information from unauthorized deletion.

**Rule ID:** `SV-241126r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Applications providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit data. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Audit information may include data from other applications or be included with the audit application itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit information is protected from unauthorized deletion. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000121

**Group ID:** `V-241127`

### Rule: Trend Deep Security must protect audit tools from unauthorized access.

**Rule ID:** `SV-241127r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit tools are protected from unauthorized access. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000122

**Group ID:** `V-241128`

### Rule: Trend Deep Security must protect audit tools from unauthorized modification.

**Rule ID:** `SV-241128r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure audit tools are protected from unauthorized modification. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000123

**Group ID:** `V-241129`

### Rule: Trend Deep Security must protect audit tools from unauthorized deletion.

**Rule ID:** `SV-241129r879581_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Applications providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the deletion of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit tools are protected from unauthorized deletion. Interview the ISSO in order to identify all users and their permissions to the audit records. The ISSO must identify each user along with their assigned role configured for the appropriate information systems allowed. Verify the information gathered against the application's, "Computer and Group Rights" for each "Role" created along with the users assigned. If the information gathered does not match the settings within the application this is a finding.

## Group: SRG-APP-000125

**Group ID:** `V-241130`

### Rule: Trend Deep Security must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-241130r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to assure in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are backed up at least every seven days onto a different system or system component than the system or component being audited. Verify the application backup frequency by reviewing the configuration settings in Administration >> System Settings >> SIEM If the "Forward System Events to a remote computer (via Syslog)" is not enabled with the proper configuration settings, this is a finding.

## Group: SRG-APP-000126

**Group ID:** `V-241131`

### Rule: Trend Deep Security must use cryptographic mechanisms to protect the integrity of audit information.

**Rule ID:** `SV-241131r879583_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Audit records may be tampered with; if the integrity of audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. Protection of audit records and audit data is of critical importance. Cryptographic mechanisms are the industry established standard used to protect the integrity of audit data. An example of a cryptographic mechanism is the computation and application of a cryptographic-signed hash using asymmetric cryptography. This requirement applies to applications that generate or process audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure cryptographic mechanisms are used to protect the integrity of audit information. Verify PDF encryption is enabled for report generation. Go to Administration >> User Management >> Users >> Right-click an administrative user account and select "Properties". Within the "Settings" tab select "Enable PDF Encryption". If "Enable PDF Encryption" is not enabled, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-241132`

### Rule: Trend Deep Security must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-241132r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments, are prohibited or restricted. Review the firewall policy for approved ports, protocols and services associated within a defined group or a selected computer by selecting Computers, on the top menu bar. Choose the appropriate group and within the main page, select a computer for review. Double-click the selected computer and click "Firewall". Verify the following settings are enabled: Configuration: Inherit or On State: Activated Firewall Stateful Configurations: Inherited (If managed through a group policy) Assigned Firewall Rules: (are configured in accordance with local security policy) If the options identified are not set or configured in accordance with local policy, this is a finding.

## Group: SRG-APP-000148

**Group ID:** `V-241133`

### Rule: Trend Deep Security must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-241133r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses, except the following. (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure organizational users (or processes acting on behalf of organizational users) are uniquely identified and authenticated. Verify the user accounts under Administration >> User Management >> Users If the accounts configured do not uniquely specify the organizational user's affiliation, this is a finding.

## Group: SRG-APP-000164

**Group ID:** `V-241134`

### Rule: Trend Deep Security must enforce a minimum 15-character password length.

**Rule ID:** `SV-241134r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure a minimum 15-character password length is enforced. Verify the policy value for minimum password length. If the value for “User password minimum length” under the Administration >> System Settings >> Security tab is not set to 15, this is a finding.

## Group: SRG-APP-000166

**Group ID:** `V-241135`

### Rule: Trend Deep Security must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-241135r879603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure password complexity is enforced by requiring that at least one upper-case character be used. Verify the values for password complexity. If the "User password requires both upper-and lower-case characters" value for password complexity under the Administration >> System Settings >> Security tab has not been set, this is a finding.

## Group: SRG-APP-000167

**Group ID:** `V-241136`

### Rule: Trend Deep Security must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-241136r879604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure password complexity is enforced by requiring that at least one lower-case character be used. Verify the values for password complexity. If the "User password requires both upper-and lower-case characters" value for password complexity under the Administration >> System Settings >> Security tab has not been set, this is a finding.

## Group: SRG-APP-000168

**Group ID:** `V-241137`

### Rule: Trend Deep Security must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-241137r879605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure password complexity is enforced by requiring that at least one numeric character be used. Verify the values for password complexity. If the "User password requires both letters and numbers" value for password complexity under the Administration >> System Settings >> Security tab has not been set, this is a finding.

## Group: SRG-APP-000169

**Group ID:** `V-241138`

### Rule: Trend Deep Security must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-241138r879606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure password complexity is enforced by requiring that at least one special character be used. Verify the values for password complexity. If the "User password requires non-alphanumeric characters" value for password complexity under the Administration >> System Settings >> Security tab has not been set, this is a finding.

## Group: SRG-APP-000174

**Group ID:** `V-241139`

### Rule: Trend Deep Security must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-241139r879611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure a 60 day maximum password lifetime restriction is enforced. Verify the policy value for minimum password length. If the value for “User password expires” under the Administration >> System Settings >> Security tab is not set to 60 Days, this is a finding.

## Group: SRG-APP-000180

**Group ID:** `V-241140`

### Rule: Trend Deep Security must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-241140r879617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication and identification enables non-organizational users to gain access to the application or possibly other information systems and provides an opportunity for intruders to compromise resources within the application or information system. Non-organizational users include all information system users other than organizational users which include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors and guest researchers). Non-organizational users must be uniquely identified and authenticated for all accesses other than those accesses explicitly identified and documented by the organization when related to the use of anonymous access, such as accessing a web server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure non-organizational users (or processes acting on behalf of non-organizational users) are uniquely identified and authenticated. Verify the user accounts under Administration >> User Management >> Users If the accounts configured do not uniquely specify the organizational user's affiliation, this is a finding.

## Group: SRG-APP-000190

**Group ID:** `V-241141`

### Rule: Trend Deep Security must terminate all network connections associated with a communications session at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity, except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-241141r879622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system level network connection. This does not mean that the application terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure all network connections associated with a communications session are terminated at the end of the session, or as follows: for in-band management sessions (privileged sessions), the session must be terminated after 10 minutes of inactivity; and for user sessions (non-privileged session), the session must be terminated after 15 minutes of inactivity, except to fulfill documented and validated mission requirements. If the value for user session termination under the Administration >> System Settings >> Security >> Session timeout, is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000233

**Group ID:** `V-241142`

### Rule: Trend Deep Security must isolate security functions from non-security functions.

**Rule ID:** `SV-241142r879643_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An isolation boundary provides access control and protects the integrity of the hardware, software, and firmware that perform security functions. Security functions are the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Developers and implementers can increase the assurance in security functions by employing well-defined security policy models; structured, disciplined, and rigorous hardware and software development techniques; and sound system/security engineering principles. Implementation may include isolation of memory space and libraries. Applications restrict access to security functions through the use of access control mechanisms and by implementing least privilege capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure security functions are isolated from non-security functions. In order to restrict access to security functions through the use of access control mechanisms, least privilege capabilities must be enforced within the Deep Security, “User management” settings. If role-based access controls are not enforced within the Administration >> User management >> Roles, this is a finding.

## Group: SRG-APP-000246

**Group ID:** `V-241143`

### Rule: Trend Deep Security must restrict the ability of individuals to use information systems to launch organization-defined Denial of Service (DoS) attacks against other information systems.

**Rule ID:** `SV-241143r879650_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition where a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Individuals of concern can include hostile insiders or external adversaries that have successfully breached the information system and are using the system as a platform to launch cyber attacks on third parties. Applications and application developers must take the steps needed to ensure users cannot use an authorized application to launch DoS attacks against other systems and networks. For example, applications may include mechanisms that throttle network traffic so users are not able to generate unlimited network traffic via the application. Limiting system resources that are allocated to any user to a bare minimum may also reduce the ability of users to launch some DoS attacks. The methods employed to counter this risk will be dependent upon the application layer methods that can be used to exploit it.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the ability of individuals to use information systems to launch organization-defined Denial of Service (DoS) attacks against other information systems is restricted. Deep Security policies for Firewall Rules can be disruptive causing a denial of service to the environment if not properly configured. It is imperative that access to the firewall rule policies be restricted to authorized personnel by enforcing least privileged within the Deep Security, “User management” settings. If role-based access controls are not enforced within the Administration >> User management >> Roles >> [Policy Name] >> Properties >> Policy Rights, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-241144`

### Rule: Trend Deep Security must manage excess capacity, bandwidth, or other redundancy to limit the effects of information flooding types of Denial of Service (DoS) attacks.

**Rule ID:** `SV-241144r879651_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. In the case of application DoS attacks, care must be taken when designing the application to ensure the application makes the best use of system resources. SQL queries have the potential to consume large amounts of CPU cycles if they are not tuned for optimal performance. Web services containing complex calculations requiring large amounts of time to complete can bog down if too many requests for the service are encountered within a short period of time. The methods employed to meet this requirement will vary depending upon the technology the application utilizes. However, a variety of technologies exist to limit or, in some cases, eliminate the effects of application related DoS attacks. Employing increased capacity and bandwidth combined with specialized application layer protection devices and service redundancy may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure excess capacity, bandwidth, or other redundancy is managed to limit the effects of information flooding types of Denial of Service (DoS) attacks. Review the “CPU Usage Level” under Administration >> System Settings >> Advanced >> CPU Usage During Recommendation Scans. Depending on resource capabilities for monitored agent scans, it may be necessary to limit the “CPU Usage Level” from High to Low. If the setting is not configured in accordance with the SA best practice recommendation this is a finding.

## Group: SRG-APP-000272

**Group ID:** `V-241145`

### Rule: Trend Deep Security must automatically update malicious code protection mechanisms.

**Rule ID:** `SV-241145r879659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious software detection applications need to be constantly updated in order to identify new threats as they are discovered. All malicious software detection software must come with an update mechanism that automatically updates the application and any associated signature definitions. The organization (including any contractor to the organization) is required to promptly install security-relevant malicious code protection software updates. Examples of relevant updates include anti-virus signatures, detection heuristic rule sets, and/or file reputation data employed to identify and/or block malicious software from executing. Malicious code includes viruses, worms, Trojan horses, and Spyware. This requirement applies to applications providing malicious code protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure malicious code protection mechanisms are automatically updated. Analyze the system using the Administration >> System Settings >> Updates page. Verify that the “Automatically download updates to imported software” option is checked. If this option is not enabled, this is a finding.

## Group: SRG-APP-000275

**Group ID:** `V-241146`

### Rule: Trend Deep Security must notify ISSO and ISSM of failed security verification tests.

**Rule ID:** `SV-241146r879661_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If personnel are not notified of failed security verification tests, they will not be able to take corrective action and the unsecure condition(s) will remain. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This requirement applies to applications performing security functions and the applications performing security function verification/testing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the ISSO and ISSM are notified of failed security verification tests. From Administration >> User Management >> Users Select the account associated with the ISSM or ISSO and double-click. Under the Contact Information tab, verify the Contact Information is associated with account is complete and accurate. If the account information is missing or incorrect, this is a finding. Next, verify the "Receive Alert Email" check box is selected. If the "Receive Alert Email" checkbox is not selected, this is finding.

## Group: SRG-APP-000276

**Group ID:** `V-241147`

### Rule: Trend Deep Security must update malicious code protection mechanisms whenever new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-241147r879662_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code includes viruses, worms, Trojan horses, and spyware. The code provides the ability for a malicious user to read from and write to files and folders on a computer's hard drive. Malicious code may also be able to run and attach programs, which may allow the unauthorized distribution of malicious mobile code. Once this code is installed on endpoints within the network, unauthorized users may be able to breach firewalls and gain access to sensitive data. This requirement applies to applications providing malicious code protection. Malicious code protection mechanisms include, but are not limited, to, anti-virus and malware detection software. Malicious code protection mechanisms (including signature definitions and rule sets) must be updated when new releases are available.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure malicious code protection mechanisms are updated whenever new releases are available in accordance with organizational configuration management policy and procedures. Analyze the system using the Administration >> System Settings >> Updates page. Verify that the “Automatically download updates to imported software” option is enabled. If this option is not enabled, this is a finding.

## Group: SRG-APP-000277

**Group ID:** `V-241148`

### Rule: Trend Deep Security must configure malicious code protection mechanisms to perform periodic scans of the information system every seven (7) days.

**Rule ID:** `SV-241148r879663_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited, to anti-virus and malware detection software. In order to minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Malicious code includes viruses, worms, Trojan horses, and Spyware. It is not enough to simply have the software installed; this software must periodically scan the system to search for malware on an organization-defined frequency. This requirement applies to applications providing malicious code protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure malicious code protection mechanisms perform periodic scans of the information system every seven (7) days. Analyze one of the custom policies under the “Policies” tab, by right clicking and selecting “Details.” Verify the following settings are enabled: 1. Under the Overview >> General tab, "Anti-Malware" is set to “On” 2. Under the Anti-Malware >> General tab, “Real-Time Scan” is set to “Default” 3. Under the Anti-Malware >> General tab, a custom “Malware Scan Configuration” is enabled with a Schedule configured to no more than 7 days. If "Anti-Malware" is set anything other than “On” this is a finding. If “Malware Scan Configuration” is set to “No Configuration,” this is a finding.

## Group: SRG-APP-000278

**Group ID:** `V-241149`

### Rule: Trend Deep Security must be configured to perform real-time malicious code protection scans of files from external sources at endpoints as the files are downloaded, opened, or executed in accordance with organizational security policy.

**Rule ID:** `SV-241149r879664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited, to, anti-virus and malware detection software. In order to minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Malicious code includes viruses, worms, Trojan horses, and Spyware. It is not enough to simply have the software installed; this software must periodically scan the system to search for malware on an organization-defined frequency. This requirement applies to applications providing malicious code protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure real-time malicious code protection scans are performed on files from external sources at endpoints as the files are downloaded, opened, or executed in accordance with organizational security policy. Verify the Anti-Malware, Real-Time Scan is enabled by reviewing the following settings under the “Policies” tab. Under “Policies” right click and select “Details” and choose “Anti-Malware. Review the following settings: Anti-Malware State is set to “On” and the “Real-Time Scan” is set to “Default.” If the two settings are not configured accordingly, this is a finding.

## Group: SRG-APP-000279

**Group ID:** `V-241150`

### Rule: Trend Deep Security must be configured to block and quarantine malicious code upon detection, then send an immediate alert to appropriate individuals.

**Rule ID:** `SV-241150r879665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include, but are not limited, to anti-virus and malware detection software. In order to minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Applications providing this capability must be able to perform actions in response to detected malware. Responses include blocking, quarantining, deleting, and alerting. Other technology- or organization-specific responses may also be employed to satisfy this requirement. Malicious code includes viruses, worms, Trojan horses, and Spyware. This requirement applies to applications providing malicious code protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure malicious code is blocked and quarantined upon detection, then send an immediate alert to appropriate individuals. Verify the “Custom remediation actions” for “Recognized Malware” under the Policy settings for Anti-Malware. - Under “Policies” tab right click any of the selected policies and click “Details.” - Choose “Anti-Malware” and deselect “Default Real-Time Scan Configuration.” Be sure to re-enable this option once the review is complete. - Click “Edit” and select “Actions.” - Under the “Recognized Malware” verify the following settings: - For Virus: Clean - For Trojans: Quarantine - For Packer: Quarantine - For Spyware: Quarantine - For Other Threats: Clean - Under “Possible Malware” verify “Quarantine” is selected. If any of the settings are not configured accordingly, this is a finding.

## Group: SRG-APP-000291

**Group ID:** `V-241151`

### Rule: Trend Deep Security must notify System Administrators and Information System Security Officers when accounts are created.

**Rule ID:** `SV-241151r879669_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO) exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure System Administrators and Information System Security Officers are notified when accounts are created. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Created” Event ID 650. If the options for “Record” and “Forward” are not enabled for "User Created", this is a finding.

## Group: SRG-APP-000292

**Group ID:** `V-241152`

### Rule: Trend Deep Security must notify System Administrators and Information System Security Officers when accounts are modified.

**Rule ID:** `SV-241152r879670_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply modify an existing account. Notification of account modification is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSOs) exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure System Administrators and Information System Security Officers are notified when accounts are modified. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Updated” Event ID 652. If the options for “Record” and “Forward” are not enabled for "User Updated", this is a finding.

## Group: SRG-APP-000293

**Group ID:** `V-241153`

### Rule: Trend Deep Security must notify System Administrators and Information System Security Officers for account disabling actions.

**Rule ID:** `SV-241153r879671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are disabled, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account disabling actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure System Administrators and Information System Security Officers are notified when accounts are disabled. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Locked Out” Event ID 603. If the options for “Record” and “Forward” are not enabled for "User Locked Out", this is a finding.

## Group: SRG-APP-000294

**Group ID:** `V-241154`

### Rule: Trend Deep Security must notify System Administrators and Information System Security Officers for account removal actions.

**Rule ID:** `SV-241154r879672_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When application accounts are removed, user accessibility is affected. Accounts are utilized for identifying individual application users or for identifying the application processes themselves. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account removal actions and, as required, notify the appropriate individuals so they can investigate the event. Such a capability greatly reduces the risk that application accessibility will be negatively affected for extended periods of time and also provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure System Administrators and Information System Security Officers are notified when accounts are removed. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Deleted” Event ID 651. If the options for “Record” and “Forward” are not enabled for "User Deleted", this is a finding.

## Group: SRG-APP-000319

**Group ID:** `V-241155`

### Rule: Trend Deep Security must automatically audit account enabling actions.

**Rule ID:** `SV-241155r879696_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and Information System Security Officers (ISSO) exists. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure account enabling actions are automatically audited. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Created” Event ID 650. If the options for “Record” and “Forward” are not enabled for "User Created", this is a finding.

## Group: SRG-APP-000320

**Group ID:** `V-241156`

### Rule: Trend Deep Security must notify SA and ISSO of account enabling actions.

**Rule ID:** `SV-241156r879697_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of application user accounts and notifies administrators and ISSOs exists. Such a process greatly reduces the risk that accounts will be surreptitiously enabled and provides logging that can be used for forensic purposes. In order to detect and respond to events that affect user accessibility and application processing, applications must audit account enabling actions and, as required, notify the appropriate individuals so they can investigate the event. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the SA and ISSO are notified of account enabling actions. 1. Analyze the system using the Administration >> System Settings >> Alerts. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “User Created” Event ID 650. If the options for “Record” and “Forward” are not enabled for "User Created", this is a finding.

## Group: SRG-APP-000343

**Group ID:** `V-241157`

### Rule: Trend Deep Security must audit the execution of privileged functions.

**Rule ID:** `SV-241157r879720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse, and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure the execution of privileged functions are audited. Interview the ISSO for a list of functions identified as privileged within the application “System Events.” Privileged functions within the system events will include but are not limited to: Computer Created, Computer Deleted, User Added, etc.). Verify the list against the Administration >> System Settings >> System Events tab. If the events are not to Record and Forward, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-241158`

### Rule: Trend Deep Security must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-241158r879731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are off-loaded onto a different system or media than the system being audited. Verify that audit records are off-loaded by configuring the Manager to instruct all managed computers to use Syslog: 1. Go to the Administration> > System Settings >> SIEM tab. 2. In the System Event Notification (from the Manager) area, verify the “Forward System Events to a remote computer (via Syslog) option” is Enabled. 3. Verify the IP address to the selected host name is entered. 4. Verify UDP port 514 or agency selected port is provided. 5. Verify the appropriate Syslog facility and Common Event Settings If any of these settings are missing from the SIEM configuration, this is a finding.

## Group: SRG-APP-000359

**Group ID:** `V-241159`

### Rule: Trend Deep Security must provide an immediate warning to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity.

**Rule ID:** `SV-241159r879732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75%, they are unable to plan for storage capacity expansion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure an immediate warning is provided to the SA and ISSO (at a minimum) when allocated audit record storage volume reaches 75% of repository maximum audit record storage capacity. 1. Analyze the system using the Administration > System Settings >> Alerts tab. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrator and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events tab for “Manager Available Disk Space Too Low” Event ID 170. If the options for “Record” and “Forward” are not enabled for “Manager Available Disk Space Too Low”, this is a finding

## Group: SRG-APP-000360

**Group ID:** `V-241160`

### Rule: Trend Deep Security must provide an immediate real-time alert to the SA and ISSO, at a minimum, of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-241160r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure an immediate real-time alert is provided to the SA and ISSO, at a minimum, of all audit failure events requiring real-time alerts. Analyze the system using the Administration >> System Settings >> Alerts tab. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding.

## Group: SRG-APP-000377

**Group ID:** `V-241161`

### Rule: Trend Deep Security must alert the ISSO, ISSM, and other designated personnel (deemed appropriate by the local organization) when the unauthorized installation of software is detected.

**Rule ID:** `SV-241161r879750_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized software not only increases risk by increasing the number of potential vulnerabilities, it also can contain malicious code. Sending an alert (in real time) when unauthorized software is detected allows designated personnel to take action on the installation of unauthorized software. This requirement applies to configuration management applications or similar types of applications designed to manage system processes and configurations (e.g., HBSS and software wrappers).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the ISSO, ISSM, and other designated personnel (deemed appropriate by the local organization) are alerted when the unauthorized installation of software is detected. 1. Analyze the system using the Administration >> System Settings >> Alerts tab. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrators and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events for “Software Added” Event ID 151. If the options for “Record” and “Forward” are not enabled for “Software Added”, this is a finding.

## Group: SRG-APP-000378

**Group ID:** `V-241162`

### Rule: Trend Deep Security must prohibit user installation of software without explicit privileged status.

**Rule ID:** `SV-241162r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing regular users to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. Explicit privileges (escalated or administrative privileges) provide the regular user with explicit capabilities and control that exceeds the rights of a regular user. Application functionality will vary, and while users are not permitted to install unapproved applications, there may be instances where the organization allows the user to install approved software packages such as from an approved software repository. The application must enforce software installation by users based upon what types of software installations are permitted (e.g., updates and security patches to existing software) and what types of installations are prohibited (e.g., software whose pedigree with regard to being potentially malicious is unknown or suspect) by the organization. This requirement applies, for example, to applications that provide the ability to extend application functionality (e.g., plug-ins, add-ons) and software management applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure user installation of software without explicit privileged status is prohibited. Analyze the system using Administration >> User Management >> Roles. Review each role created that is not “Full Access”. Right-Click >> Properties on the desired role, and select “Other Rights.” The “Updates” setting should be set to “View Only” or “Hide.” If any other option is selected other than “View Only” or “Hide”, this is a finding.

## Group: SRG-APP-000379

**Group ID:** `V-241163`

### Rule: Trend Deep Security must implement organization-defined automated security responses if baseline configurations are changed in an unauthorized manner.

**Rule ID:** `SV-241163r879752_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to the baseline configuration could make the system vulnerable to various attacks or allow unauthorized access to the system. Changes to information system configurations can have unintended side effects, some of which may be relevant to security. Detecting such changes and providing an automated response can help avoid unintended, negative consequences that could ultimately affect the security state of the application. Examples of security responses include, but are not limited to the following: halting application processing; halting selected application functions; or issuing alerts/notifications to organizational personnel when there is an unauthorized modification of a configuration item.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure organization-defined automated security responses are implemented if baseline configurations are changed in an unauthorized manner. Deep Security, Policies, are policy templates that specify the security rules to be configured and enforced automatically for one or more computers. These compact, manageable rule sets make it simple to provide comprehensive security without the need to manage thousands of rules. Default Policies provide the necessary rules for a wide range of common computer configurations. 1. Analyze the system using the Administration >> System Settings >> Alerts tab. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution for system administrator and ISSOs, this is a finding. 2. Analyze the system using the Administration >> System Settings >> System Events tab to ensure the following events are enabled: 350 Policy Created Record Forward 351 Policy Deleted Record Forward 352 Policy Updated Record Forward 353 Policies Exported Record Forward 354 Policies Imported Record Forward If the options for “Record” and “Forward” are not enabled on these events, this is a finding

## Group: SRG-APP-000380

**Group ID:** `V-241164`

### Rule: Trend Deep Security must enforce access restrictions associated with changes to application configuration.

**Rule ID:** `SV-241164r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to application configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to application components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure access restrictions associated with changes to application configuration are enforced. Inspect the settings used for enforcing least privilege through access restrictions under Administration >> User Management >> Roles. Select a role under the “Roles” menu and click "Properties". 1. Select the “Computer Rights” tab and verify the settings configured under the “Computer and Group Rights” area. If non-authorized users have access to anything other than “View”, this is a finding. 2. Select the “Policy Rights” tab and verify the settings configured under the “Policy Rights” area. If non-authorized users have access to anything other than “View,” this is a finding. 3. Select the “User Rights” tab and verify the settings configured under the “User Rights” area. If non-authorized users have access to anything other than “Change own password and contact information only”, this is a finding. 4. Select the Other Rights, tab and verify the settings configured under the “Other Rights” area. If non-authorized users have access to anything other than "View-Only" or "Hide", this is a finding.

## Group: SRG-APP-000381

**Group ID:** `V-241165`

### Rule: Trend Deep Security must audit the enforcement actions used to restrict access associated with changes to the application.

**Rule ID:** `SV-241165r879754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the application configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the enforcement actions used to restrict access associated with changes to the application are audited. System Events include changes to the configuration of an Agent/Appliance, the Deep Security Manager, or Users. They also include errors that may occur during normal operation of the Trend Deep Security system. To ensure the necessary events are captured, verify the Administration >> System Settings >> System Events, against the local policy established by the ISSO. If the settings configured do not match local policy, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-241166`

### Rule: Trend Deep Security must only allow the use of DoD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-241166r879798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure only the use of DoD PKI established certificate authorities are allowed for verification of the establishment of protected sessions. Verify the certificate CA and by reviewing the issued to and validity date by clicking the certificate icon in the web browser and selecting View Certificates, Certificate Information, etc. (browser dependent). If the certificate is not issued by a DoD CA, this is a finding.

## Group: SRG-APP-000431

**Group ID:** `V-241167`

### Rule: Trend Deep Security must maintain a separate execution domain for each executing process.

**Rule ID:** `SV-241167r879802_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications can maintain separate execution domains for each executing process by assigning each process a separate address space. Each process has a distinct address space so that communication between processes is performed in a manner controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces. An example is a web browser with process isolation that provides tabs that are separate processes using separate address spaces to prevent one tab crashing the entire browser.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure a separate execution domain for each executing process is maintained. Review the network topology supporting Deep Security for separation of zones and host OS. If the architecture does separate the Deep Security Manager (DSM) from the Database, this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-241168`

### Rule: Trend Deep Security must protect against or limit the effects of all types of Denial of Service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-241168r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the effects of all types of Denial of Service (DoS) attacks are protected against or limited by employing organization-defined security safeguards. Policies are templates that specify the settings and security rules to be configured and enforced automatically for one or more computers. These compact, manageable rule sets make it simple to provide comprehensive security without the need to manage thousands of rules. Default Policies provide the necessary rules for a wide range of common computer configurations. Select “Computers” from the top menu and double click on any computer from the “Computers” area. Click the “Firewall” menu and review the configuration setting under the “General” tab. If Firewall >> Configuration is set to "Off", this is a finding. Click the “Intrusion Prevention” menu and review the configuration setting under the “General” tab. If Intrusion Prevention >> Configuration is set to “Off”, this is a finding.

## Group: SRG-APP-000450

**Group ID:** `V-241169`

### Rule: Trend Deep Security must implement organization-defined security safeguards to protect its memory from unauthorized code execution.

**Rule ID:** `SV-241169r879821_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some adversaries launch attacks with the intent of executing code in non-executable regions of memory or in memory locations that are prohibited. Security safeguards employed to protect memory include, for example, data execution prevention and address space layout randomization. Data execution prevention safeguards can either be hardware-enforced or software-enforced with hardware providing the greater strength of mechanism. Examples of attacks are buffer overflow attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure organization-defined security safeguards are implemented to protect its memory from unauthorized code execution. Policies are templates that specify the settings and security rules to be configured and enforced automatically for one or more computers. These compact, manageable rule sets make it simple to provide comprehensive security without the need to manage thousands of rules. Default Policies provide the necessary rules for a wide range of common computer configurations. Select “Computers” from the top menu and double click on any computer from the “Computers” window. Click the “Firewall” option and review the Configuration setting under the “General” tab. If this is set to “Off”, this is a finding. Click the “Intrusion Prevention” option and review the Configuration setting under the “General” tab. If this is set to “Off”, this is a finding

## Group: SRG-APP-000456

**Group ID:** `V-241170`

### Rule: Trend Deep Security must install security-relevant software updates within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).

**Rule ID:** `SV-241170r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period utilized must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure security-relevant software updates are installed within the time period directed by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs). Review the Scheduled Tasks under Administration >> Scheduled Tasks to see if “Daily Check for Security Updates” is present. If “Daily Check for Security Updates” is not present, this is a finding.

## Group: SRG-APP-000463

**Group ID:** `V-241171`

### Rule: Trend Deep Security detection application must detect network services that have not been authorized or approved by the organization-defined authorization or approval processes.

**Rule ID:** `SV-241171r879834_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore, may be unreliable or serve as malicious rogues for valid services. This requirement can be addressed by a host-based IDS capability or by remote scanning functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure network services that have not been authorized or approved by the organization-defined authorization or approval processes are detected. Review the Intrusion Detection policy for approved ports, protocols and services associated within a defined group or a selected computer by: - Selecting “Computers”, on the top menu bar. - Choose the appropriate group and within the main page and select a computer for review. - Double click the selected computer and click “Intrusion Detection” - Verify the following settings are enabled: - Configuration: is set to On - Intrusion Prevention Behavior is set to Prevent or Detect; review local security policy for appropriate setting. - Assigned Intrusion Prevention Rules: review local security policy for appropriate setting If the Assigned Intrusion Prevention Rules do not match the local defined policy, this is a finding.

## Group: SRG-APP-000464

**Group ID:** `V-241172`

### Rule: Trend Deep Security must, when unauthorized network services are detected, log the event and alert the ISSO, ISSM, and other individuals designated by the local organization.

**Rule ID:** `SV-241172r879835_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore, may be unreliable or serve as malicious rogues for valid services. The detection of such unauthorized services must be logged and appropriate personnel must be notified. This requirement can be addressed by a host-based IDS capability or by remote scanning functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the event is logged, and the ISSO, ISSM, and other individuals designated by the local organization are alerted when unauthorized network services are detected. Policies are templates that specify the settings and security rules to be configured and enforced automatically for one or more computers. These compact, manageable rule sets make it simple to provide comprehensive security without the need to manage thousands of rules. Default Policies provide the necessary rules for a wide range of common computer configurations. Select “Computers” from the top menu and double click on any computer from the list. Under Firewall >> General Tab >> Firewall area, verify "Configuration" is set to "On". If "Configuration" is set to “Off”, this is a finding. Under Intrusion Detection >> General Tab >> Intrusion Detection area, verify "Configuration" is set to "On". If "Configuration" is set to “Off”, this is a finding.

## Group: SRG-APP-000469

**Group ID:** `V-241173`

### Rule: Trend Deep Security must continuously monitor inbound communications traffic for unusual or unauthorized activities or conditions.

**Rule ID:** `SV-241173r879840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Evidence of malicious code is used to identify potentially compromised information systems or information system components. Unusual/unauthorized activities or conditions related to information system inbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. This requirement applies to applications that provide monitoring capability for unusual/unauthorized activities including, but are not limited to, host-based intrusion detection, anti-virus, and malware applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure inbound communications traffic is continuously monitored for unusual or unauthorized activities or conditions. Verify the state of the Intrusion Prevent policies: - Select “Computers” on the top menu bar - Choose the appropriate group and within the main page and select a computer for review. - Double click the selected computer and click “Intrusion Prevention” - Verify the following settings are enabled: - Configuration: is set to Inherit or On - “State:” is listing “Activated” - Policies are defined under the Assigned Intrusion Prevention Rules. If any of these settings are not configured, this is a finding

## Group: SRG-APP-000471

**Group ID:** `V-241174`

### Rule: Trend Deep Security must alert the ISSO, ISSM, and other individuals designated by the local organization when the following Indicators of Compromise (IOCs) or potential compromise are detected: real-time intrusion detection; threats identified by authoritative sources (e.g., CTOs); and Category I, II, IV, and VII incidents in accordance with CJCSM 6510.01B.

**Rule ID:** `SV-241174r879842_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a security event occurs, the application that has detected the event must immediately notify the appropriate support personnel so they can respond appropriately. Alerts may be generated from a variety of sources, including, audit records or inputs from malicious code protection mechanisms, intrusion detection, or prevention mechanisms. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. Individuals designated by the local organization to receive alerts may include, for example, system administrators, mission/business owners, or system owners. IOCs are forensic artifacts from intrusions that are identified on organizational information systems (at the host or network level). IOCs provide organizations with valuable information on objects or information systems that have been compromised. These indicators reflect the occurrence of a compromise or a potential compromise. This requirement applies to applications that provide monitoring capability for unusual/unauthorized activities including, but are not limited to, host-based intrusion detection, anti-virus, and malware applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure ISSO, ISSM, and other individuals designated by the local organization are alerted when the following Indicators of Compromise (IOCs) or potential compromise are detected: real time intrusion detection; threats identified by authoritative sources (e.g., CTOs); and Category I, II, IV, and VII incidents in accordance with CJCSM 6510.01B. 1. Analyze the system using the Administration >> System Settings >> Alerts tab. Review the email address listed in the “Alert Event Forwarding (From The Manager).” If this email address is not present or does not belong to a distribution group for system administrators and ISSOs, this is a finding. 2. Select Computers from the top menu and double click on any computer from the “Computers” window. Click the “Intrusion Prevention” option and review the Configuration setting under the “General” tab. If “Intrusion Prevention” is set to “Off”, this is a finding 3. Select a rule from the “Assigned Intrusion Prevention Rules” and double click to bring up the properties. Click “Options” and verify that the “Alert” tab is set to “On”. If “Alert” is set to “Off”, this is a finding.

## Group: SRG-APP-000495

**Group ID:** `V-241175`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to modify privileges occur.

**Rule ID:** `SV-241175r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful attempts to modify privileges occur. Review the system using the Administration >> System Settings >> System Events tab for successful/unsuccessful attempts to delete privileges. If the options for “Record” and “Forward” are not enabled for successful/unsuccessful attempts to delete privileges, this is a finding

## Group: SRG-APP-000496

**Group ID:** `V-241176`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to modify security objects occur.

**Rule ID:** `SV-241176r879867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful attempts to modify security objects occur. Review the system using the Administration >> System Settings >> System Events tab for successful/unsuccessful attempts to modify security objects. If the options for “Record” and “Forward” are not enabled for successful/unsuccessful attempts to modify security objects, this is a finding

## Group: SRG-APP-000497

**Group ID:** `V-241177`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to modify security levels occur.

**Rule ID:** `SV-241177r879868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful attempts to modify security levels occur. Review the system using the Administration >> System Settings >> System Events tab for successful/unsuccessful attempts to modify security levels. If the “Record” and “Forward” options for successful/unsuccessful attempts to modify security levels are not enabled, this is a finding.

## Group: SRG-APP-000499

**Group ID:** `V-241178`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to delete privileges occur.

**Rule ID:** `SV-241178r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful attempts to delete privileges occur. Review the system using the Administration >> System Settings >> System Events tab for successful/unsuccessful attempts to delete privileges. If the “Record” and “Forward” options for successful/unsuccessful attempts to delete privileges are not enabled, this is a finding.

## Group: SRG-APP-000501

**Group ID:** `V-241179`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful attempts to delete security objects occur.

**Rule ID:** `SV-241179r879872_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful attempts to delete security objects occur. Review the system using the Administration >> System Settings >> System Events tab for successful/unsuccessful attempts to delete security objects. If the “Record” and “Forward" options for are not enabled for successful/unsuccessful attempts to delete security objects, this is a finding.

## Group: SRG-APP-000503

**Group ID:** `V-241180`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-241180r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated when successful/unsuccessful logon attempts occur. Review the system using the Administration >> System Settings >> System Events for successful/unsuccessful attempts for "User Signed In" (Event ID 600). If the options for “Record” and “Forward” are not enabled, this is a finding.

## Group: SRG-APP-000504

**Group ID:** `V-241181`

### Rule: Trend Deep Security must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-241181r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure audit records are generated for privileged activities or other system-level access. Interview the ISSO for a list of functions identified as privileged within the application “System Events.” Privileged functions within the system events will include but are not limited to: Computer Created, Computer Deleted, User Added, etc. Verify the list against the Administration >> System Settings >> System Events tab. If the events are not set to “Record” and “Forward”, this is a finding.

## Group: SRG-APP-000507

**Group ID:** `V-241182`

### Rule: Trend Deep Security must generate audit records when successful/unsuccessful accesses to objects occur.

**Rule ID:** `SV-241182r879878_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure audit records are generated when successful/unsuccessful accesses to objects occur. Interview the ISSO for a list of functions identified as objects that should be audited within the application “System Events.” Verify the list against the Administration >> System Settings >> System Events tab. If the events are not set to “Record” and “Forward”, this is a finding.

## Group: SRG-APP-000508

**Group ID:** `V-241183`

### Rule: Trend Deep Security must generate audit records for all direct access to the information system.

**Rule ID:** `SV-241183r879879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure audit records are generated for all direct access to the information system. Interview the ISSO for a list of direct access objects that should be audited within the application “System Events.” Verify the list against the Administration >> System Settings >> System Events tab. If the events are not set to “Record” and “Forward”, this is a finding.

## Group: SRG-APP-000509

**Group ID:** `V-241184`

### Rule: Trend Deep Security must generate audit records for all account creations, modifications, disabling, and termination events.

**Rule ID:** `SV-241184r879880_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure audit records are generated for all account creations, modifications, disabling, and termination events. Verify all creations, modifications, disabling, and termination events identified within the Trend Deep Security System Events are set to “Record” and “Forward”. If the events are not set to “Record” and “Forward”, this is a finding.

## Group: SRG-APP-000510

**Group ID:** `V-241185`

### Rule: Trend Deep Security must generate audit records for all kernel module load, unload, and restart events and, also for all program initiations.

**Rule ID:** `SV-241185r879881_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure audit records are generated for all kernel module load, unload, and restart events and, also for all program initiations. Verify that audit records are off-loaded by configuring the Manager to instruct all managed computers to use Syslog: 1. Go to the Administration >> System Settings >> SIEM tab. 2. In the System Event Notification (from the Manager) area, verify the “Forward System Events to a remote computer (via Syslog)" box is checked. 3. Verify the IP address to the selected host name is entered. 4. Verify UDP port 514 or agency selected port is provided. 5. Verify the appropriate Syslog facility and Common Event Settings If any of these settings are missing from the SIEM configuration, this is a finding.

## Group: SRG-APP-000515

**Group ID:** `V-241186`

### Rule: Trend Deep Security must, at a minimum, off-load interconnected systems in real time and off-load standalone systems weekly.

**Rule ID:** `SV-241186r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure, at a minimum, off-load interconnected systems in real time and off-load standalone systems weekly. Verify that audit records are off-loaded by configuring the Manager to instruct all managed computers to use Syslog: 1. Go to the Administration >> System Settings >> SIEM tab. 2. In the System Event Notification (from the Manager) area, verify the “Forward System Events to a remote computer (via Syslog)" box is checked. 3. Verify the IP address to the selected host name is entered. 4. Verify UDP port 514 or agency selected port is provided. 5. Verify the appropriate Syslog facility and Common Event Settings If any of these settings are missing from the SIEM configuration, this is a finding.

## Group: SRG-APP-000474

**Group ID:** `V-241187`

### Rule: Trend Deep Security must notify the system administrator when anomalies in the operation of the security functions are discovered.

**Rule ID:** `SV-241187r879845_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If anomalies are not acted upon, security functions may fail to secure the system. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. Notifications provided by information systems include messages to local computer consoles, and/or hardware indications, such as lights. This requirement applies to applications performing security functions and the applications performing security function verification/testing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure the system administrator is notified when anomalies in the operation of the security functions are discovered. Verify Intrusion Prevention is enabled for all connected host systems by navigating to Policy >> Policy Editor. Navigate to Intrusion Prevention >> General, verify that the intrusion prevention module is "On" and configured with assigned rules. If "Intrusion Prevention" is not set to "On", this is a finding.

## Group: SRG-APP-000480

**Group ID:** `V-241188`

### Rule: Trend Deep Security must implement security safeguards when integrity violations are discovered.

**Rule ID:** `SV-241188r879851_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized changes to software, firmware, and information can occur due to errors or malicious activity (e.g., tampering). Information includes metadata, such as security attributes associated with information. State-of-the-practice integrity-checking mechanisms (e.g., parity checks, cyclical redundancy checks, cryptographic hashes) and associated tools can automatically monitor the integrity of information systems and hosted applications. Organizations may define different integrity checking and anomaly responses by type of information (e.g., firmware, software, user data); by specific information (e.g., boot firmware, boot firmware for a specific types of machines); or a combination of both. Automatic implementation of specific safeguards within organizational information systems includes, for example, reversing the changes, halting the information system, restarting the information system, notification to the appropriate personnel or roles, or triggering audit alerts when unauthorized modifications to critical security files occur. This capability must take into account operational requirements for availability for selecting an appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server configuration to ensure security safeguards are implemented when integrity violations are discovered. Verify Integrity Monitoring is enabled for all connected host systems by navigating to Policy >> Policy Editor. Navigate to Integrity Monitoring >> General, verify that the Integrity Monitoring module is "On" and configured with assigned rules. If "Integrity Monitoring" is not set to "On", this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-241189`

### Rule: Trend Deep Security must synchronize with Active Directory on a daily (or AO-defined) basis.

**Rule ID:** `SV-241189r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure synchronization occurs with Active Directory on a daily (or AO-defined) basis. Under Administration >> Scheduled Tasks, review the scheduled tasks listed for "Daily Sync Users". If a task for syncing user's accounts with AD does not exist, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-241190`

### Rule: Trend Deep Security must reside on a Web Server configured for multifactor authentication.

**Rule ID:** `SV-241190r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Web Server hosting Trend Deep Security to ensure multifactor authentication has been configured. 1. Open Internet Information Services (IIS) Manager. 2. In the console tree, expand the server name. 3. In the server Home page, double-click Authentication to open the Authentication page. 4. In the Authentication page, right-click AD Client Certificate Authentication, and ensure "Enable" is selected. 5. Close the Authentication page. 6. In the server Home page, double-click SSL Settings to open the SSL Settings page. 7. Ensure the "Require SSL" Checkbox is checked, and "Require" radio button is selected. 8. Close the SSL Settings page. 9. Close IIS Manager. If "Enable" is not selected in the Authentication page, this is a finding. If "Require SSL" is not selected in the SSL Settings page, this is a finding. If "Ignore" or "Accept" radio buttons are selected in the SSL settings page, this is a finding.

## Group: SRG-APP-000153

**Group ID:** `V-241191`

### Rule: Trend Deep Security must ensure users are authenticated with an individual authenticator prior to using a group authenticator.

**Rule ID:** `SV-241191r879594_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure individual accountability and prevent unauthorized access, application users must be individually identified and authenticated. Individual accountability mandates that each user is uniquely identified. A group authenticator is a shared account or some other form of authentication that allows multiple unique individuals to access the application using a single account. If an application allows or provides for group authenticators, it must first individually authenticate users prior to implementing group authenticator functionality. Some applications may not have the need to provide a group authenticator; this is considered a matter of application design. In those instances where the application design includes the use of a group authenticator, this requirement will apply. There may also be instances when specific user actions need to be performed on the information system without unique user identification or authentication. An example of this type of access is a web server which contains publicly releasable information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Trend Deep Security server to ensure users are authenticated with an individual authenticator prior to using a group authenticator. Review the settings to ensure identify management is being performed through the organizations Active Directory. Navigate to Administration >> User Management >> Users and click "Synchronize with Directory". Select "Re-Synchronize (Using previous settings)", and click "Next". If the synchronization fails, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-259713`

### Rule: The version of Trend Deep Security running on the system must be a supported version.

**Rule ID:** `SV-259713r942481_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Trend Deep Security 9.x is no longer supported by the vendor. If the system is running Trend Deep Security 9.x, this is a finding.

