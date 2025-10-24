# STIG Benchmark: DBN-6300 NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255529`

### Rule: The DBN-6300 must provide automated support for account management functions.

**Rule ID:** `SV-255529r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If account management functions are not automatically enforced, an attacker could gain privileged access to a vital element of the network security architecture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the LDAP authentication server is configured correctly. Navigate to Settings >> Initial Configuration >> Authentication. Verify that the LDAP server entry is correct and that the button for "LDAP Based Authentication" is enabled. Verify that the "Native takes precedence" button is set to "Disabled". If the LDAP server entry is not present and enabled, and the "Native takes precedence" button is not set to "Disabled", this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-255530`

### Rule: The DBN-6300 must automatically audit account creation.

**Rule ID:** `SV-255530r960777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. This control does not apply to the account of last resort or root account. DoD prohibits local user accounts on the device, except for an account of last resort and (where applicable) a root account. With the DB-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account creation. Confirm the presence of a syslog message on the syslog server containing the information for successful account creation. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a successful account creation has just occurred is not there, this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-255531`

### Rule: The DBN-6300 must automatically audit account modification.

**Rule ID:** `SV-255531r960780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often attempt to create a persistent method of reestablishing access. One way to accomplish this is to modify an account. This control does not apply to the account of last resort or root account. DoD prohibits local user accounts on the device, except for an account of last resort and (where applicable) a root account. Account management functions include assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account modification. Confirm the presence of a syslog message on the syslog server containing the information for successful account modification. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a successful account modification has just occurred is not there, this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-255532`

### Rule: The DBN-6300 must automatically audit account removal actions.

**Rule ID:** `SV-255532r960786_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account removal. Confirm the presence of a syslog message on the syslog server containing the information for successful account removal. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a successful account removal has just occurred is not there, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-255533`

### Rule: The DBN-6300 must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-255533r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed logon attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. It is possible to set a time-to-retry variable, as well as number of retries during that lockout timeout variable, within the DBN-6300.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system will lock out the user if three failed logon attempts occur within 15 minutes, attempt to log on as a user three times in succession and deliberately fail (by entering the wrong password). After the third attempt, the user will be locked out from retrying until the oldest attempt (by time) ages out past the 15-minute mark and then will be allowed to try again. If the user is not locked out after three failed logon attempts within 15 minutes, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-255534`

### Rule: The DBN-6300 must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-255534r960864_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required in order to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any account function. Confirm the presence of a syslog message on the syslog server containing the information for whatever that account function represented. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information for the account action that took place is not present, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255535`

### Rule: The DBN-6300 must provide audit record generation capability for DoD-defined auditable events within the DBN-6300.

**Rule ID:** `SV-255535r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. With the DB-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any account function. Confirm the presence of a syslog message on the syslog server containing the information for whatever that account function represented. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information for the account action that took place is not present, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255536`

### Rule: The DBN-6300 must allow only the ISSM (or individuals or roles appointed by the ISSM) to select which auditable events are to be generated and forwarded to the audit log.

**Rule ID:** `SV-255536r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories can be checked in accordance with the role assigned. For an administrator, the admin role should allow all categories to be checked for Audit Log, Syslog, and Audit Console. Log off, log on again, and attempt to repeat the process logged on as a "lesser" user that does not have privileges to configure audit. Attempt to modify the audit log categories. This should fail. Following this verification, if it is possible for a non-privileged user with no audit log modification privileges to modify log functions, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-255537`

### Rule: The DBN-6300 must generate log records when successful attempts to access privileges occur.

**Rule ID:** `SV-255537r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter). It is not possible to perform unsuccessful commands in the UI web management interface since it is a GUI interface. Unauthorized menu items/commands are not visible.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories can be checked in accordance with the role assigned. For an administrator, the admin role should allow all categories to be checked for Audit Log, Syslog, and Audit Console. Log off, log on again, and attempt to repeat the process logged on as a "lesser" user that does not have privileges to configure audit. Attempt to modify the audit log categories. This should fail. Following this verification, if it is possible for a non-privileged user with no audit log modification privileges to modify log functions, this is a finding.

## Group: SRG-APP-000092-NDM-000224

**Group ID:** `V-255538`

### Rule: The DBN-6300 must initiate session auditing upon startup.

**Rule ID:** `SV-255538r960888_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If auditing is enabled late in the startup process, the actions of some start-up processes may not be audited. Some audit systems also maintain state information only available if auditing is enabled before a given process is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories can be checked in accordance with the role assigned. For an administrator, the admin role should allow all categories to be checked for Audit Log, Syslog, and Audit Console. Log off and log on to the system again. Examine the message at the syslog server. If there is no message, or no information in the message containing data showing the logon, this is a finding.

## Group: SRG-APP-000095-NDM-000225

**Group ID:** `V-255539`

### Rule: The DBN-6300 must produce audit log records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-255539r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Associating event types with detected events in the application and audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network device. Without this capability, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. If the DBN-6300 is not connected to the syslog server, this is a finding.

## Group: SRG-APP-000096-NDM-000226

**Group ID:** `V-255540`

### Rule: The DBN-6300 must produce audit records containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-255540r960894_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is essential for security personnel to know what is being done, what was attempted, where it was done, when it was done, and by whom it was done in order to compile an accurate risk assessment. Logging the date and time of each detected event provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network device. In order to establish and correlate the series of events leading up to an outage or attack, it is imperative the date and time are recorded in all log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing date and time information for when the event occurred. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain date and time information, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-255541`

### Rule: The DBN-6300 must produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-255541r960897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as device hardware components, device software modules, session identifiers, filenames, host names, and functionality. Location of events includes hardware components, device software module, session identifiers, filenames, host names, and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing information to establish where the event occurred. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain information to establish where the event occurred, this is a finding.

## Group: SRG-APP-000098-NDM-000228

**Group ID:** `V-255542`

### Rule: The DBN-6300 must produce audit log records containing information to establish the source of events.

**Rule ID:** `SV-255542r960900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know the source of the event. The source may be a component, module, or process within the device or an external session, administrator, or device. Location of events includes hardware components, device software module, processes within the device or external session, administrator ID, or device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing information to establish the source of events. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain information to establish the source of events, this is a finding.

## Group: SRG-APP-000099-NDM-000229

**Group ID:** `V-255543`

### Rule: The DBN-6300 must produce audit records that contain information to establish the outcome of the event.

**Rule ID:** `SV-255543r960903_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the system. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the device after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing information to establish the outcome of the event. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain information to establish the outcome of the event, this is a finding.

## Group: SRG-APP-000100-NDM-000230

**Group ID:** `V-255544`

### Rule: The DBN-6300 must generate audit records containing information that establishes the identity of any individual or process associated with the event.

**Rule ID:** `SV-255544r960906_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., administrators or processes acting on behalf of administrators) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Event identifiers (if authenticated or otherwise known) include but are not limited to user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing information to establish the identity of any individual or process associated with the event. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain information to establish the identity of any individual or process associated with the event, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-255545`

### Rule: The DBN-6300 must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-255545r960909_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment in which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an auditable action. Confirm the presence of a syslog message on the syslog server containing the full-text recording of privileged commands. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message for the event does not contain the full-text recording of privileged commands, this is a finding.

## Group: SRG-APP-000116-NDM-000234

**Group ID:** `V-255546`

### Rule: The DBN-6300 must use internal system clocks to generate time stamps for audit records.

**Rule ID:** `SV-255546r960927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to determine what is happening within the network infrastructure or to resolve and trace an attack, the network device must support the organization's capability to correlate the audit log data from multiple network devices to acquire a clear understanding of events. In order to correlate auditable events, time stamps are needed on all of the log records. If the internal clock is not used, the system may not be able to provide time stamps for log messages. Additionally, externally generated time stamps may not be accurate. Applications can use the capability of an operating system or purpose-built module for this purpose. (Note that the internal clock is required to be synchronized with authoritative time sources by other requirements.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the configuration of the NTP server. Navigate to Settings >> Initial Configuration >> Time. View the "Time" settings window. If an NTP server address is not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255547`

### Rule: The DBN-6300 must back up audit records at least every seven days onto a different system or system component than the system or component being audited.

**Rule ID:** `SV-255547r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to ensure that, in the event of a catastrophic system failure, the audit records will be retained. Backup of audit records helps to ensure that a compromise of the information system being audited does not also result in a compromise of the audit records. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process a logon. Confirm the presence of a syslog message on the syslog server containing the date and time of this last logon. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a logon had just occurred is not there, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-255548`

### Rule: The DBN-6300 must uniquely identify and authenticate organizational administrators (or processes acting on behalf of organizational administrators).

**Rule ID:** `SV-255548r960969_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational administrators must be uniquely identified and authenticated for all network management accesses to prevent potential misuse and compromise of the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there is one local account configured on the DBN-6300. Navigate to Settings >> User Management. Verify that there is one account on the system and that this account has unrestricted privileges. If no local account is configured in this way, or more than one account is configured locally, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-255549`

### Rule: The DBN-6300 must use multifactor authentication for network access (remote and nonlocal) to privileged accounts.

**Rule ID:** `SV-255549r960972_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., LAN, WAN, or the Internet). DoD has mandated the use of the Common Access Card (CAC) token/credential to support identity management and personal authentication for systems covered under HSPD 12. DoD recommended architecture for network devices is for system administrators to authenticate using an authentication server using the DoD CAC credential with DoD-approved PKI. This requirement also applies to the account of last resort and the root account only if non-local access via the network is enabled for these accounts (not recommended). This control does not apply to the account of last resort or root account. DoD prohibits local user accounts on the device, except for an account of last resort and (where applicable) a root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Multifactor authentication is managed through the LDAP server. Verify that LDAP (remote authentication) is enabled. Navigate to Settings >> Initial Configuration >> Authentication. Verify that LDAP server information is correctly entered and enabled. Verify that "Native takes precedence" is disabled. If LDAP server is not connected, or if "Native takes precedence" is not disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255550`

### Rule: The DBN-6300 must use multifactor authentication for local access to privileged accounts.

**Rule ID:** `SV-255550r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Multifactor authentication is defined as using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). To ensure accountability and prevent unauthenticated access, privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Local access is defined as access to an organizational information system by a user (or process acting on behalf of a user) communicating through a direct connection without the use of a network. Applications integrating with the DoD Active Directory and utilizing the DoD CAC are examples of compliant multifactor authentication solutions. This control does not apply to the account of last resort or root account. DoD prohibits local user accounts on the device, except for an account of last resort and (where applicable) a root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Multifactor authentication is managed through the LDAP server. Verify that LDAP (remote authentication) is enabled. Navigate to Settings >> Initial Configuration >> Authentication. Verify that LDAP server information is correctly entered and enabled. Verify that "Native takes precedence" is disabled. If LDAP server is not connected, or if "Native takes precedence" is not disabled, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-255551`

### Rule: The DBN-6300 must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-255551r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSL is configured to use SSL for the web management tool. Navigate to Settings >> Initial Configuration >> Security. If the check box for "Enforce secure communications (SSL) for user interface access" is not checked, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-255552`

### Rule: The DBN-6300 must enforce a minimum 15-character password length.

**Rule ID:** `SV-255552r984092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. Since the device cannot be configured for password complexity, not having a strong password can result in the success of a brute force attack, which would give immediate access to a privileged system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the minimum password length is set to "15". Navigate to Settings >> Initial Configuration >> Authentication. If the "Minimum User Password Length" is not set to "15", this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255553`

### Rule: The DBN-6300 must prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-255553r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the network device allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system prohibits password reuse attempt to change the users password deliberately reusing the last passwords used. The user should fail to update their password for the last five passwords that their account has used. If the user is able to reuse their password before using five different password, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-255554`

### Rule: If multifactor authentication is not supported and passwords must be used, the DBN-6300 must enforce password complexity by requiring that at least one upper-case character be used.

**Rule ID:** `SV-255554r984095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires password complexity attempt to change your password to a non-conforming password. If the user is able to change their password without meeting the requirement, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-255555`

### Rule: If multifactor authentication is not supported and passwords must be used, the DBN-6300 must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-255555r984098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires password complexity attempt to change your password to a non-conforming password. If the user is able to change their password without meeting the requirement, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-255556`

### Rule: If multifactor authentication is not supported and passwords must be used, the DBN-6300 must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-255556r984099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires password complexity attempt to change your password to a non-conforming password. If the user is able to change their password without meeting the requirement, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-255557`

### Rule: If multifactor authentication is not supported and passwords must be used, the DBN-6300 must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-255557r984100_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires password complexity attempt to change your password to a non-conforming password. If the user is able to change their password without meeting the requirement, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255558`

### Rule: The DBN-6300 must enforce 24 hours/1 day as the minimum password lifetime.

**Rule ID:** `SV-255558r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enforcing a minimum password lifetime helps prevent repeated password changes to defeat the password reuse or history enforcement requirement. Restricting this setting limits the user's ability to change their password. Passwords need to be changed at specific policy-based intervals; however, if the network device allows the user to immediately and continually change their password, then the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires a minimum password lifetime attempt to change your password two times quickly. If the user is able to change their password the second time, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255559`

### Rule: The DBN-6300 must enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-255559r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. One method of minimizing this risk is to use complex passwords and periodically change them. If the network device does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the passwords could be compromised. This requirement does not include emergency administration accounts which are meant for access to the network device in case of failure. These accounts are not required to have maximum password lifetime restrictions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To see if the system requires a maximum password lifetime attempt to login with a user who has had their password set longer then password lifetime setting. If a user is able to log in successfully, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-255560`

### Rule: The DBN-6300 must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-255560r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify administrator accounts are configured with a 10-minute timeout setting. Navigate to Settings >> Users. Click on the wrench for an existing user. View each user defined on the device since there is no setting for a global value. If a timeout value of "600" is not set for each administrator account configured on the device, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255561`

### Rule: The DBN-6300 must reveal error messages only to authorized individuals (ISSO, ISSM, and SA).

**Rule ID:** `SV-255561r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state. Additionally, sensitive account information must not be revealed through error messages to unauthorized personnel or their designated representatives. The DBN-6300 will reveal error messages only to authorized individuals (ISSO, ISSM, and SA). Only privileged users have visibility into any error messages. The audit log requires authorized users to log on to obtain visibility. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any account function. Confirm the presence of a syslog message on the syslog server containing the information for whatever that account function represented. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information for the account action that took place is not present, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255562`

### Rule: The DBN-6300 must activate a system alert message, send an alarm, and/or automatically shut down when a component failure is detected.

**Rule ID:** `SV-255562r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Predictable failure prevention requires organizational planning to address device failure issues. If components key to maintaining the device's security fail to function, the device could continue operating in a nonsecure state. If appropriate actions are not taken when a network device failure occurs, a denial-of-service condition may occur that could result in mission failure because the network would be operating without a critical security monitoring and prevention function. Upon detecting a failure of network device security components, the network device must activate a system alert message, send an alarm, or shut down. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and that the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any account function. Confirm the presence of a syslog message on the syslog server containing the information for whatever that account function represented. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information for the account action that took place is not present, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255563`

### Rule: The DBN-6300 must automatically terminate a network administrator session after organization-defined conditions or trigger events requiring session disconnect.

**Rule ID:** `SV-255563r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of administrator-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever an administrator (or process acting on behalf of a user) accesses a network device. Such administrator sessions can be terminated (and thus terminate network administrator access) without terminating network sessions. Session termination terminates all processes associated with an administrator's logical session except those processes that are specifically created by the administrator (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. These conditions will vary across environments and network device types.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify administrator accounts are configured with a 10 minute timeout setting. Navigate to Settings >> Users. Click on the wrench for an existing user. View each user defined on the device since there is no setting for a global value. If a timeout value of "600" is not set for each administrator account configured on the device, this is a finding.

## Group: SRG-APP-000319-NDM-000283

**Group ID:** `V-255564`

### Rule: The DBN-6300 must automatically audit account enabling actions.

**Rule ID:** `SV-255564r961290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply enable a new or disabled account. Notification of account enabling is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of application user accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, enable an account. Confirm the presence of a syslog message on the syslog server containing the date and time of this last logon. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that an account has been enabled is not there, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255565`

### Rule: The DBN-6300 must be compliant with at least one IETF Internet standard authentication protocol.

**Rule ID:** `SV-255565r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting access authorization information (i.e., access control decisions) ensures that authorization information cannot be altered, spoofed, or otherwise compromised during transmission. In distributed information systems, authorization processes and access control decisions may occur in separate parts of the systems. In such instances, authorization information is transmitted securely so timely access control decisions can be enforced at the appropriate locations. To support the access control decisions, it may be necessary to transmit, as part of the access authorization information, supporting security attributes. This is because, in distributed information systems, there are various access control decisions that need to be made, and different entities (e.g., services) make these decisions in a serial fashion, each requiring some security attributes to make the decisions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the LDAP authentication server is configured correctly. Navigate to Settings >> Initial Configuration >> Authentication. Verify that the LDAP server entry is correct and the button for "LDAP Based Authentication" is enabled. Verify that the "Native takes precedence" button is set to "Disabled". If the LDAP server entry is not present and enabled, and the "Native takes precedence" button is not set to "Disabled", this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-255566`

### Rule: The DBN-6300 must audit the execution of privileged functions.

**Rule ID:** `SV-255566r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process a privileged function. Confirm the presence of a syslog message on the syslog server containing the privileged function. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that the privileged function that just occurred is not there, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255567`

### Rule: The DBN-6300 must provide the capability for organization-identified individuals or roles to change the auditing to be performed based on all selectable event criteria within near real time.

**Rule ID:** `SV-255567r961863_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to effectively respond, and important forensic information may be lost. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations. In addition, auditing may be limited to a specific set of events to facilitate audit reduction, analysis, and reporting. Organizations can establish time thresholds in which audit actions are changed, for example, near-real-time, within minutes, or within hours. The individuals or roles to change the auditing are dependent on the security configuration of the network device. For example, it may be configured to allow only some administrators to change the auditing, while other administrators can review audit logs but not reconfigure auditing. Because this capability is so powerful, organizations should be extremely cautious about only granting this capability to fully authorized security personnel. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are able to be selected based on selectable event criteria for Audit Log, Syslog, and Audit Console. If, after navigating to Settings >> Advanced >> Audit Log, there is no facility to change the auditing to be performed within the system log based on selectable event criteria, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255568`

### Rule: The DBN-6300 must compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-255568r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the configuration of the NTP server. Navigate to Settings >> Initial Configuration >> Time. View the "Time" settings window. If an NTP server address is not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255569`

### Rule: The DBN-6300 must synchronize its internal system clock to the NTP server when the time difference is greater than one second.

**Rule ID:** `SV-255569r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in CCI-001891 because a comparison must be done in order to determine the time difference. The organization-defined time period will depend on multiple factors, most notably the granularity of time stamps in audit logs. For example, if time stamps only show to the nearest second, there is no need to have accuracy of a tenth of a second in clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the configuration of the NTP server. Navigate to Settings >> Initial Configuration >> Time. View the "Time" settings window. If an NTP server address is not configured, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-255570`

### Rule: The DBN-6300 must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-255570r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the time zone is configured for "UTC". Navigate to Settings >> Initial Configuration >> Time. View the "Time Zone" box. If the Time Zone is not set to "UTC", this is a finding.

## Group: SRG-APP-000375-NDM-000300

**Group ID:** `V-255571`

### Rule: The DBN-6300 must record time stamps for audit records that meet a granularity of one second for a minimum degree of precision.

**Rule ID:** `SV-255571r961446_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without sufficient granularity of time stamps, it is not possible to adequately determine the chronological order of records. Time stamps generated by the application include date and time. Granularity of time measurements refers to the degree of synchronization between information system clocks and reference clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the configuration of the NTP server. Navigate to Settings >> Initial Configuration >> Time. View the "Time" settings window. If an NTP server address is not configured, this is a finding.

## Group: SRG-APP-000381-NDM-000305

**Group ID:** `V-255572`

### Rule: The DBN-6300 must audit the enforcement actions used to restrict access associated with changes to the device.

**Rule ID:** `SV-255572r984111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the device configuration, it will be difficult to identify attempted attacks, and an audit trail will not be available for forensic investigation for after-the-fact actions. Enforcement actions are the methods or mechanisms used to prevent unauthorized changes to configuration settings. Enforcement action methods may be as simple as denying access to a file based on the application of file permissions (access restriction). Audit items may consist of lists of actions blocked by access restrictions or changes identified after the fact. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account removal. Confirm the presence of a syslog message on the syslog server containing the date and time of this last logon. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a logon just occurred is not there, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-255573`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-255573r961554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSL is configured to use SSL for the web management tool. Navigate to Settings >> Initial Configuration >> Security. If the check box for "Enforce secure communications (SSL) for user interface access" is not checked, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-255574`

### Rule: Applications used for nonlocal maintenance sessions must implement cryptographic mechanisms to protect the confidentiality of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-255574r961557_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SSL is configured to use SSL for the web management tool. Navigate to Settings >> Initial Configuration >> Security. If the check box for "Enforce secure communications (SSL) for user interface access" is not checked, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-255575`

### Rule: The DBN-6300 must generate audit records when successful/unsuccessful attempts to modify administrator privileges occur.

**Rule ID:** `SV-255575r961800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). Administrative roles cannot be changed on the device console; thus, this only applies to the User Interface (UI) web management tool. All account activities (creation, modification, disabling, and removal, and other account activities, including successful/unsuccessful attempts to modify administrator privileges) on the DBN-6300 are written out to an audit log. This log carries a wealth of information that provides valuable forensic help, including the origin IP and port and destination and port where the event occurred, as well as the type of event and when it occurred. This data is all used to help establish the identity of any individual or process associated with the event. This can be verified by accessing the audit logs remotely by downloading the System State Report. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account administrator privilege modification. Confirm the presence of a syslog message on the syslog server containing the account administrator privilege modification. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that an account administrator privilege modification has occurred is not there, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-255576`

### Rule: The DBN-6300 must generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-255576r961812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account administrator privilege modification. Confirm the presence of a syslog message on the syslog server containing the deletion of account administrator privileges. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the deletion of account administrator privileges is not there, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-255577`

### Rule: The DBN-6300 must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-255577r961824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300 Audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account administrator privilege modification. Confirm the presence of a syslog message on the syslog server containing information pertinent to successful or unsuccessful logon attempts. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing information pertinent to successful or unsuccessful logon attempts is not there, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-255578`

### Rule: The DBN-6300 must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-255578r961827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any kind of privileged activity or any type of system-level access. Confirm the presence of a syslog message on the syslog server containing information pertinent to any kind of privileged activity or any type of system-level access. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information pertinent to any kind of privileged activity or any type of system-level access that was processed is not there, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-255579`

### Rule: The DBN-6300 must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-255579r961830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process any function using administrator access. Confirm the presence of a syslog message on the syslog server containing information pertinent to an event using administrator access that was processed. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information pertinent to any kind of administrator access is not there, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-255580`

### Rule: The DBN-6300 must generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-255580r961833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, a user should log on from two different workstations. Confirm the presence of a syslog message on the syslog server containing logon information pertinent to logons from the same user from two different workstations. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information pertinent to a user logging on concurrently from two different workstations is not there, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255581`

### Rule: The DBN-6300 must generate audit records for all account creation, modification, disabling, and termination events.

**Rule ID:** `SV-255581r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, execute four processes: account creation, account modification, account termination, and account disabling. Confirm the presence of a syslog message on the syslog server containing information pertinent to account creation, account modification, account termination, and account disabling. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing information pertinent to the account creation, account modification, account termination, and account disabling is not there, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-255582`

### Rule: The DBN-6300 must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-255582r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. The intent of this control is to ensure that log information does not get overwritten if the limited log storage capacity is reached and also to protect the log records in general if the system/component being logged is compromised (hence the notion of off-loading onto a different system or media) but the intent is not to hold the information in more than one or multiple locations. This requirement is intended to address the primary repository, which is on the centralized Syslog server. This requirement is only applicable to the server used as the Syslog server. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. If the DBN-6300 is not connected to the syslog server, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-255583`

### Rule: The DBN-6300 must generate audit log events for a locally developed list of auditable events.

**Rule ID:** `SV-255583r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", that the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes"; the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console; and the items for any locally developed list of auditable events is checked. Following this verification, process an account removal. Confirm the presence of a syslog message on the syslog server containing the date and time of this last logon. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a logon has just occurred is not there, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-255584`

### Rule: Accounts for device management must be configured on the authentication server and not the network device itself, except for the account of last resort.

**Rule ID:** `SV-255584r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the LDAP authentication server is configured correctly. Navigate to Settings >> Initial Configuration >> Authentication. Verify that the LDAP server entry is correct and the button for "LDAP Based Authentication" is enabled. Verify that the "Native takes precedence" button is set to "Disabled". If the LDAP server entry is not present and enabled, and the "Native takes precedence" button is not set to "Disabled", this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-255585`

### Rule: The DBN-6300 must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-255585r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice. Self-signed certificates are not allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Public Key Certificate is installed and has been obtained from an appropriate certificate policy through an approved service provider. Navigate to CLI and verify that there is a registry entry similar to below: Reg set /sysconfig/tls/trustedcas EOF (enter/paste certificate here) EOF If an entry is not found in the registry with the appropriate certificate, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-255586`

### Rule: The DBN-6300 must be configured to send log data to a syslog server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-255586r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail that documents the creation of accounts and notifies administrators and ISSOs. Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes. With the DBN-6300, audit records are automatically backed up on a real-time basis via syslog when enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes"; the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console; and the items for any locally developed list of auditable events is checked. Following this verification, process any type of account management activity. Confirm the presence of a syslog message on the syslog server containing the information regarding the account management function that was used. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a logon has just occurred is not there, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-264431`

### Rule: The DBN-6300 NDM must be using a version supported by the vendor.

**Rule ID:** `SV-264431r992090_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

