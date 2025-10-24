# STIG Benchmark: Fortinet FortiGate Firewall NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-234162`

### Rule: The FortiGate device must automatically audit account creation.

**Rule ID:** `SV-234162r879525_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the System category of Event Logging is enabled, then account creation is audited. To check that System and Event Logging are enabled, log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Scroll down to Log Settings. 4. Verify Event Logging is set to "All" (for most verbose logging) or "Customize", and includes at least the System activity event. If Event Logging is not set to "All" or "Customize" with System enabled, then account creation will not be audited, and this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If event and system parameters are set to disable, the account creation is not audited, and this is a finding.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-234163`

### Rule: The FortiGate device must automatically audit account modification.

**Rule ID:** `SV-234163r879526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Since the accounts in the network device are privileged or system-level accounts, account management is vital to the security of the network device. Account management by a designated authority ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel with the appropriate and necessary privileges. Auditing account modification, along with an automatic notification to appropriate individuals, will provide the necessary reconciliation that account management procedures are being followed. If modifications to management accounts are not audited, reconciliation of account management procedures cannot be tracked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the System category of Event Logging is enabled, then account modification is audited. To check that Event and System Logging are enabled, log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Scroll down to Log Settings. 4. Verify Event Logging is set to "All" (for most verbose logging) or "Customize", and include at least the System activity event. If Event Logging is not set to "All" or "Customize" with System enabled, then account modification is not audited, and this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system\|user' The output should be: set event enable set system enable set user enable If event, system, and user parameters are set to disable, then account modification is not audited, and this is a finding.

## Group: SRG-APP-000029-NDM-000211

**Group ID:** `V-234164`

### Rule: The FortiGate device must automatically audit account removal actions.

**Rule ID:** `SV-234164r879528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Account management, as a whole, ensures access to the network device is being controlled in a secure manner by granting access to only authorized personnel. Auditing account removal actions will support account management procedures. When device management accounts are terminated, user or service accessibility may be affected. Auditing also ensures authorized active accounts remain enabled and available for use when required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the System category of Event Logging is enabled, then account removal is audited. To check that System and Event Logging is configured, log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Scroll down to Log Settings. 4. Verify Event Logging is set to "All" (for most verbose logging) or "Customize" and include at least the System activity event. If the Event Logging is not set to "All" or "Customize" with System enabled, then account removal is not audited, and this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If event and system parameters are set to disable, then account removal is not audited, and this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-234165`

### Rule: The FortiGate device must have only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-234165r879589_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privilege-level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the "account of last resort" since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit must be added to the envelope as a record. Administrators must secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Verify the admin account is the only account configured as Type Local. If more than one local user account exists, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-234166`

### Rule: The FortiGate device must allow full access to only those individuals or roles designated by the ISSM.

**Rule ID:** `SV-234166r879533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Identify the administrator who is authorized to access System Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to System is set to Read/Write. Then, 1. Click System. 2. Click Administrators. 3. Click other administrators and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to System is set to Read or None. If any low-privileged administrator not designated by the ISSM has Read/Write access to System, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-234167`

### Rule: The FortiGate device must audit the execution of privileged functions.

**Rule ID:** `SV-234167r879720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-234168`

### Rule: The FortiGate device must enforce the limit of three consecutive invalid logon attempts, after which time it must lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-234168r879546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Confirm the output from the following command: # show full-configuration system global | grep -i admin-lockout The output should be: set admin-lockout-duration 900 set admin-lockout-threshold 3 If the admin-lockout-duration is not set to 900 and admin-lockout-threshold is not set to 3, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-234169`

### Rule: The FortiGate device must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-234169r879547_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the FortiGate GUI login page. Verify DoD-approved banner is displayed on the login landing page. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the correct DoD required banner text is not displayed, this is a finding. and Open a CLI console via SSH and connect to the FortiGate device: Verify the FortiGate CLI displays the Standard Mandatory DoD Notice and Consent Banner before granting access to the system via SSH. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. At any time, the USG may inspect and seize data stored on this IS. Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." If the DoD-approved banner is not displayed before granting access, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-234170`

### Rule: The FortiGate device must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-234170r879548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to the device allowing the administrator access to the network device. This ensures the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of CLI access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, then entering the password is also acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Attempt to access the FortiGate device using HTTPS URL. 2. Verify Standard Mandatory DoD Notice and Consent Banner is displayed and retained on the screen. 3. Verify a user has to explicitly ACCEPT the banner before to log on for further access. If Standard Mandatory DoD Notice and Consent Banner is not retained, and a user is not forced to ACCEPT the banner to log on for further access, this is a finding. And, 1. Attempt to login to the FortiGate via SSH: 2. Enter username. 3. Verify the Standard Mandatory DoD Notice and Consent Banner before prompting to enter a password. If Standard Mandatory DoD Notice and Consent Banner is not retained before entering the password to log on for further access, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-234171`

### Rule: The FortiGate device must log all user activity.

**Rule ID:** `SV-234171r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement supports non-repudiation of actions taken by an administrator and is required to maintain the integrity of the configuration management process. All configuration changes to the network device are logged, and administrators authenticate with two-factor authentication before gaining administrative access. Together, these processes will ensure the administrators can be held accountable for the configuration changes they implement. To meet this requirement, the network device must log administrator access and activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege: To verify that logging is enabled: 1. Click Log and Report. 2. Click Log Settings. 3. Scroll down to Log Settings and ensure that Event Logging is set to "All" or "Customize" with System activity events checked. If Event Logging is not set to ALL or Customize with System activity event checked, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-234172`

### Rule: The FortiGate device must generate audit records when successful/unsuccessful attempts to modify administrator privileges occur.

**Rule ID:** `SV-234172r879866_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-234173`

### Rule: The FortiGate device must generate audit records when successful/unsuccessful attempts to delete administrator privileges occur.

**Rule ID:** `SV-234173r879870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-234174`

### Rule: The FortiGate device must generate audit records when successful/unsuccessful logon attempts occur.

**Rule ID:** `SV-234174r879874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-234175`

### Rule: The FortiGate device must generate audit records for privileged activities or other system-level access.

**Rule ID:** `SV-234175r879875_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-234176`

### Rule: The FortiGate device must generate audit records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-234176r879876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-234177`

### Rule: The FortiGate device must generate audit records when concurrent logons from different workstations occur.

**Rule ID:** `SV-234177r879877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log eventfilter | grep -i 'event\|system' The output should be: set event enable set system enable If the event and system parameters are set to disable, this is a finding.

## Group: SRG-APP-000100-NDM-000230

**Group ID:** `V-234178`

### Rule: The FortiGate device must generate audit records containing information that establishes the identity of any individual or process associated with the event.

**Rule ID:** `SV-234178r879568_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., administrators or processes acting on behalf of administrators) associated with the events, security personnel cannot determine responsibility for the potentially harmful event. Event identifiers (if authenticated or otherwise known) include, but are not limited to, user database tables, primary key values, user names, or process identifiers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following commands: # show full-configuration log setting | grep -i anonymize The output should be: set user-anonymize disable If the log setting user-anonymize is set to enable, this is a finding.

## Group: SRG-APP-000101-NDM-000231

**Group ID:** `V-234179`

### Rule: The FortiGate device must generate audit records containing the full-text recording of privileged commands.

**Rule ID:** `SV-234179r879569_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Reconstruction of harmful events or forensic analysis is not possible if audit records do not contain enough information. Organizations consider limiting the additional audit information to only that information explicitly needed for specific audit requirements. The additional information required is dependent on the type of information (i.e., sensitivity of the data and the environment within which it resides). At a minimum, the organization must audit full-text recording of privileged commands. The organization must maintain audit trails in sufficient detail to reconstruct events to determine the cause and impact of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system global | grep -i cli-audit The output should be: set cli-audit-log enable If cli-audit-log is set to disable, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-234180`

### Rule: The FortiGate device must allocate audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-234180r879730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log disk setting | grep -i max-log-file-size The output should be: set max-log-file-size {INTEGER} If max-log-file-size for local disk storage is not set to the organization-defined audit record storage, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-234181`

### Rule: The FortiGate device must off-load audit records on to a different system or media than the system being audited.

**Rule ID:** `SV-234181r879886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify remote logging is configured. Via the GUI: Login via the FortiGate GUI with super-admin privileges. - Navigate to Log and Report. - Navigate to Log Settings. - Verify the Remote and Archiving settings. or Via the CLI: Open a CLI console via SSH or from the "CLI Console" button in the GUI. Run the following commands to verify which logging settings are enabled: # show full-configuration log fortianalyzer setting | grep -i 'status\|server' # show full-configuration log fortianalyzer2 setting | grep -i 'status\|server' # show full-configuration log fortianalyzer3 setting | grep -i 'status\|server' # show full-configuration log syslogd setting | grep -i 'status\|server' # show full-configuration log syslogd2 setting | grep -i 'status\|server' # show full-configuration log syslogd3 setting | grep -i 'status\|server' # show full-configuration log syslogd4 setting | grep -i 'status\|server' - The output should indicate enabled and an IP address. If the FortiGate is not logging to a fortianalyzer or syslog server, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-234182`

### Rule: The FortiGate device must generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-234182r879733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected. Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Security Fabric. 2. Click Automation. 3. Verify Automation Stitches are configured to send alerts related to audit processing failure. 4. For each Automation Stitch, verify a valid Action Email has been configured. If Automation Stitches are not defined to trigger an immediate real-time alert of all audit processing failures, this is a finding. Note: Relevant events for an Automation Stitch are below: Disk Full Disk Log access failed Disk log directory deleted Disk log file deleted Disk log full over first warning Disk logs failed to back up Disk logs failed to back up to USB Disk partitioning or formatting Error Disk unavailable FortiAnalyzer connection down FortiAnalyzer connection failed FortiAnalyzer is not configured for Security Fabric service FortiAnalyzer log access failed Log disk failure imminent Log disk full Log disk unavailable Memory log access failed Memory log full over final warning level Memory log full over first warning level Memory log full over second warning level Memory logs failed to back up

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-234183`

### Rule: The FortiGate device must synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-234183r879746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system ntp | grep server The output should be: set server {IP address of NTP server 1} set server {IP address of NTP server 2} If the internal information system clocks are not configured to synchronize with the primary and secondary time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-234184`

### Rule: The FortiGate device must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-234184r879747_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Events. 3. On the Events page, double-click on an event for detail. 4. Verify in the log details that the mapped time zone reflects GMT. If the time zone is not mapped to GMT, this is a finding.

## Group: SRG-APP-000120-NDM-000237

**Group ID:** `V-234185`

### Rule: The FortiGate device must protect audit information from unauthorized deletion.

**Rule ID:** `SV-234185r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the network device must protect audit information from unauthorized deletion. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include: ensuring log files receive the proper file system permissions utilizing file system protections, restricting access, and backing up log data to ensure log data is retained. Network devices providing a user interface to audit data will leverage user permissions and roles identifying the user accessing the data, and the corresponding rights the user enjoys, to make access decisions regarding the deletion of audit data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Click on each administrator who is not authorized to access Log and Report Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to Log and Report is set to None or Read. If any low-privileged administrator has Read/Write access to Log and Report, this is a finding.

## Group: SRG-APP-000121-NDM-000238

**Group ID:** `V-234186`

### Rule: The FortiGate device must protect audit tools from unauthorized access.

**Rule ID:** `SV-234186r879579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles, identifying the user accessing the tools and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Click each administrator who is not authorized to access Log and Report Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify the permission to Log and Report is set to None. If any low-privileged administrator has Read/Write or Read access to Log and Report settings, this is a finding.

## Group: SRG-APP-000122-NDM-000239

**Group ID:** `V-234187`

### Rule: The FortiGate device must protect audit tools from unauthorized modification.

**Rule ID:** `SV-234187r879580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network devices providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools, and the corresponding rights the user enjoys, to make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Click on each administrator who is not authorized to access Log and Report settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to Log and Report is set to None or Read. If any low-privileged administrator has Read/Write access to Log and Report, this is a finding.

## Group: SRG-APP-000378-NDM-000302

**Group ID:** `V-234188`

### Rule: The FortiGate device must prohibit installation of software without explicit privileged status.

**Rule ID:** `SV-234188r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing anyone to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. This requirement applies to code changes and upgrades for all network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Identify the administrator that is not authorized to access System Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to System is set to Read or None. If any unauthorized administrator has Read/Write access to System, this is a finding.

## Group: SRG-APP-000380-NDM-000304

**Group ID:** `V-234189`

### Rule: The FortiGate device must enforce access restrictions associated with changes to device configuration.

**Rule ID:** `SV-234189r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to device configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the device can potentially have significant effects on the overall security of the device. Accordingly, only qualified and authorized individuals should be allowed to obtain access to device components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Identify the administrator that is not authorized to access System Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify the permission to System is set to Read or None. If any unauthorized administrators have Read/Write access to System, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-234190`

### Rule: The FortiGate device must limit privileges to change the software resident within software libraries.

**Rule ID:** `SV-234190r879586_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. If the network device were to enable non-authorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with an Administrator that does not have System setting privileges. 1. Click System. 2. Attempt to click Firmware; this option will not be available. If the FortiGate device does not limit privileges to change the software resident within software libraries, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-234191`

### Rule: The FortiGate device must enforce access restrictions associated with changes to the system components.

**Rule ID:** `SV-234191r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, ACLs, and policy filters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Identify the administrator who is authorized to access System Settings and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to System is set to Read/Write. If the authorized administrator does not have Read/Write access to System, this is a finding. Then, 1. Click System. 2. Click Administrators. 3. Click other administrators and hover over the profile assigned to the role. 4. Click Edit. 5. Verify that the permission to System is set to Read or None. If any low-privileged administrator has Read/Write access to System, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-234192`

### Rule: The FortiGate device must use LDAP for authentication.

**Rule ID:** `SV-234192r916111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Verify all users except admin are assigned to a remote LDAP user group. If all administrators except admin are not configured to use remote LDAP authentication, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-234193`

### Rule: The FortiGate device must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-234193r879887_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the Fortinet Support Portal and review the Product Life Cycle Software "End of Support Date". Log in to the FortiGate with Super-Admin privilege in the GUI and review the Dashboard >> Status >> System Information widget for Firmware version. If the firmware listed in the FortiGate is not supported based on the Product Life Cycle page, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-234194`

### Rule: The FortiGate device must generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-234194r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log setting Compare the output to the locally developed list to ensure enabled events match the local list. 3. Run the following command: # show full-configuration log eventfilter Compare the output to the locally developed list to ensure enabled events match the local list. If the FortiGate device does not generate log records for a locally developed list of auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-234195`

### Rule: The FortiGate device must conduct backups of system-level information contained in the information system when changes occur.

**Rule ID:** `SV-234195r916221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click the admin menu available on the upper right-hand corner of the screen. 2. Click Configuration. 3. Click Revisions. 4. Verify a list of saved backed-up configurations are available. If saved backups of system configuration do not exist, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-234196`

### Rule: The FortiGate device must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-234196r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information was not backed up, and a system failure occurred, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click the admin menu available on the upper right-hand corner of the screen. 2. Click Configuration. 3. Click Revisions. 4. Verify at least one saved backed-up occurred within the last week. If a backup of system configuration was not performed within the last week, this is a finding.

## Group: SRG-APP-000408-NDM-000314

**Group ID:** `V-234197`

### Rule: FortiGate devices performing maintenance functions must restrict use of these functions to authorized personnel only.

**Rule ID:** `SV-234197r879781_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>There are security-related issues arising from software brought into the network device specifically for diagnostic and repair actions (e.g., a software packet sniffer installed on a device to troubleshoot system traffic, or a vendor installing or running a diagnostic application to troubleshoot an issue with a vendor-supported device). If maintenance tools are used by unauthorized personnel, they may accidentally or intentionally damage or compromise the system. This requirement addresses security-related issues associated with maintenance tools used specifically for diagnostic and repair actions on organizational network devices. Maintenance tools can include hardware, software, and firmware items. Maintenance tools are potential vehicles for transporting malicious code, either intentionally or unintentionally, into a facility and subsequently into organizational information systems. Maintenance tools can include, for example, hardware/software diagnostic test equipment and hardware/software packet sniffers. This requirement does not cover hardware/software components that may support information system maintenance, yet are a part of the system (e.g., the software implementing "ping," "ls," "ipconfig," or the hardware and software implementing the monitoring port of an Ethernet switch).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege: 1. Click System. 2. Click Administrators. 3. Identify the administrator designated to perform maintenance functions and hover over the profile assigned to the role. 4. Click Edit. 5. Verify the permission to System is set to Read/Write or Custom with Maintenance set to Read/Write. If an authorized administrator does not have Read/Write access to System Maintenance Settings, this is a finding. Then, 1. Click System. 2. Click Administrators. 3. Click all other low-privileged administrators and hover over the profile assigned to the role. 4. Click Edit. 5. Verify the permission to System Maintenance is customized set to Read or None. If any low-privileged administrator has Read/Write access to System Settings, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command for all low privileged admin user: # show system admin {ADMIN NAME} | grep -i accprofile The output should be: set accprofile {PROFILE NAME} Use the profile name from the output result of above command. # show system accprofile {PROFILE NAME} | grep -i sysgrp The output should be: set sysgrp read or set sysgrp none If any low privileged admin user has sysgrp parameter set to value Read/Write, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-234198`

### Rule: The FortiGate device must use DoD-approved Certificate Authorities (CAs) for public key certificates.

**Rule ID:** `SV-234198r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this CA will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Certificates. 3. Verify CAs are approved providers. If the public key certificates are not from an approved service provider, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-234199`

### Rule: The FortiGate device must prohibit the use of all unnecessary and/or non-secure functions, ports, protocols, and/or services.

**Rule ID:** `SV-234199r879588_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, then it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to FortiGate GUI with Super-Admin privileges. 1. Click Policy and Objects. 2. Click Services, and then review services, functions, and ports that are allowed by the firewall. 3. Next, open a CLI console, via SSH or available from the GUI. 4. Run the following commands: # show firewall policy # show firewall policy6 Review policies to ensure that no restricted services, ports, protocols or functions are allowed. FortiGate is configured to deny by default, so if a service, port, protocol, or function is not specifically allowed, it will be denied. If restricted functions, ports, protocols, and/or services are allowed by the firewall, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console over SSH or available from the GUI. 2. Run the following # show full-configuration system interface 3. Review configuration for unnecessary services. If unnecessary services are configured, this is a finding. Review the PPSM CAL and determine which functions, ports, protocols, and/or services must be disabled or restricted.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-234200`

### Rule: The FortiGate device must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-234200r879597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques used to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., TLS, WS_Security). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system global | grep -i 'tls\|ssh-v' The output should be: # set admin-https-ssl-versions tlsv1-2 tlsv1-3 # set admin-ssh-v1 disable # set ssl-min-proto-version TLSv1-2 #end If admin-https-ssl-versions is not set to tlsv1-2 tlsv1-3 or admin-ssh-v1 is enable, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-234201`

### Rule: The FortiGate device must authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-234201r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click SNMP. 3. Verify the SNMPv3 settings are configured and enabled. 4. Select each SNMPv3 user and click Edit. 5. On Security Level, verify the SNMPv3 user is configured to use SHA256 as the Authentication Algorithm. If the FortiGate device is not configured to authenticate SNMP messages using a FIPS-validated HMAC, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system snmp user | grep -i 'security-level\ |auth-proto' For each SNMPv3 user, the output should be similar to: set security-level auth set auth-proto sha256 If the security-level parameter is not set to auth or auth-priv, and the auth-proto is not set to SHA, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-234202`

### Rule: The FortiGate device must authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-234202r879768_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If NTP is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # diagnose sys ntp status The output should be similar to: ipv4 server(URL of NTP server) 123.123.123.123 -- reachable(0xbf) S:1 T:242 selected server-version=4, stratum=2 reference time is e213a5fb.2250b45e -- UTC Wed Mar 11 18:01:31 2020 clock offset is 0.000801 sec, root delay is 0.000381 sec root dispersion is 0.053268 sec, peer dispersion is 287 msec If the output does not return server-version is equal to 4, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-234203`

### Rule: The FortiGate device must enforce a minimum 15-character password length.

**Rule ID:** `SV-234203r879601_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Navigate to Password Policy. 4. Verify Password scope is enabled for Admin. 5. Verify the Minimum length is set to 15. If the Password scope is OFF and the Minimum length is not set to 15, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege: 1. Open a CLI console, via SSH or available from the GUI 2. Run the following command: # show full-configuration system password-policy | grep -i minimum set minimum-length 15 If the minimum-length parameter is not set to 15, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-234204`

### Rule: The FortiGate device must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-234204r879603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Navigate to Password Policy. 4. Verify Password scope is enabled for Admin and Character requirements is toggled to right. 5. Verify the Uppercase value is set to 1 or greater. If the Uppercase parameter is not set to 1 or greater, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system password-policy | grep -i upper-case If the min-upper-case-letter parameter is not set to 1 or greater, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-234205`

### Rule: The FortiGate device must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-234205r917456_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Navigate to Password Policy. 4. Verify Password scope is enabled for Admin and Character requirements is toggled to right. 5. Verify the Lowercase value is set to 1 or greater. If the Lowercase parameter is not set to 1 or greater, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system password-policy | grep -i lower-case If the min-lower-case-letter parameter is not set to 1 or greater, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-234206`

### Rule: The FortiGate device must enforce password complexity by requiring at least one numeric character be used.

**Rule ID:** `SV-234206r879605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Navigate to Password Policy. 4. Verify Password scope is enabled for Admin and Character requirements is toggled to right. 5. Verify the Numbers value is set to 1 or greater. If the Numbers parameter is not set to 1 or greater, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system password-policy | grep -i number If the min-number parameter is not set to 1 or greater, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-234207`

### Rule: The FortiGate device must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-234207r879606_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Navigate to Password Policy. 4. Verify Password scope is enabled for Admin and Character requirements is toggled to right. 5. Verify the Special value is set to 1 or greater. If the Special parameter is not set to 1 or greater, this is a finding. or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system password-policy | grep -i non-alphanumeric If the min-non-alphanumeric parameter is not set to 1 greater, this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-234208`

### Rule: The FortiGate device must use LDAPS for the LDAP connection.

**Rule ID:** `SV-234208r879609_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration user ldap | grep -i ldaps The output should be: set secure ldaps If set secure is not set to ldaps, this is a finding.

## Group: SRG-APP-000080-NDM-000345

**Group ID:** `V-234209`

### Rule: The FortiGate device must not have any default manufacturer passwords when deployed.

**Rule ID:** `SV-234209r879554_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices not protected with strong password schemes provide the opportunity for anyone to crack the password and gain access to the device, which can result in loss of availability, confidentiality, or integrity of network traffic. Many default vendor passwords are well known or are easily guessed; therefore, not removing them prior to deploying the network device into production provides an opportunity for a malicious user to gain unauthorized access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Attempt to log in to the FortiGate GUI using the username admin with the default (blank) password. Attempt to log in to the CLI over SSH with the username admin with the default (blank) password. If either of these logins are successful, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-234210`

### Rule: The FortiGate device must use FIPS 140-2 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-234210r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # get system status | grep -i fips The output should be: FIPS-CC mode: enable If FIPS-CC mode parameter is not set to enable, this is a finding.

## Group: SRG-APP-000411-NDM-000330

**Group ID:** `V-234211`

### Rule: The FortiGate devices must use FIPS-validated Keyed-Hash Message Authentication Code (HMAC) to protect the integrity of nonlocal maintenance and diagnostic communications.

**Rule ID:** `SV-234211r879784_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Nonlocal maintenance and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. Currently, HMAC is the only FIPS-approved algorithm for generating and verifying message/data authentication codes in accordance with FIPS 198-1. Products that are FIPS 140-2 validated will have an HMAC that meets specification; however, the option must be configured for use as the only message authentication code used for authentication to cryptographic modules. Separate requirements for configuring applications and protocols used by each application (e.g., SNMPv3, SSHv2, NTP, HTTPS, and other protocols and applications that require server/client authentication) are required to implement this requirement. Where SSH is used, the SSHv2 protocol suite is required because it includes Layer 7 protocols such as SCP and SFTP, which can be used for secure file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Network, Interfaces. 2. Click the interface designated for device management traffic. 3. On Administrative Access, verify HTTPS and SSH are selected, and HTTP is not. If HTTPS and SSH are not selected for administrative access, or HTTP is selected, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system interface port{Management Port Integer #} | grep -i allowaccess The output should include: set allowaccess ping https ssh If the allowaccess parameter does not include https and ssh, this is a finding. If the allowaccess parameter includes http, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-234212`

### Rule: The FortiGate device must implement cryptographic mechanisms using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-234212r879785_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Network, Interfaces. 2. Click the interface designated for device management traffic. 3. On Administrative Access, verify HTTPS and SSH are selected. If HTTPS and SSH are not selected for administrative access, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command for all low privileged admin user: # show full-configuration system interface port{Management Port Integer #} | grep -i allowaccess The output should include: set allowaccess ping https ssh If https and ssh are not returned, this is a finding. If http is returned, this is a finding.

## Group: SRG-APP-000186-NDM-000266

**Group ID:** `V-234213`

### Rule: The FortiGate device must terminate idle sessions after 10 minutes of inactivity.

**Rule ID:** `SV-234213r879621_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a device management session or connection remains open after management is completed, it may be hijacked by an attacker and used to compromise or damage the network device. Nonlocal device management and diagnostic activities are those activities conducted by individuals communicating through a network, either an external network (e.g., the internet) or an internal network. In the event the remote node has abnormally terminated or an upstream link from the managed device is down, the management session will be terminated, thereby freeing device resources and eliminating any possibility of an unauthorized user being orphaned to an open idle session of the managed device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the FortiGate device terminates all network connections when non-local device maintenance is complete. Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Go to Administrative Settings. 4. Verify Idle Timeout is configured to 10 minutes. If the idle-timeout value is not 10 minutes, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration sys global | grep -i admintimeout The output should be: set admintimeout 10 If the admintimeout parameter is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-234214`

### Rule: The FortiGate device must terminate idle sessions after 10 minutes of inactivity.

**Rule ID:** `SV-234214r916342_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Settings. 3. Go to Administrative Settings. 4. Verify Idle Timeout is configured to 10 minutes. If the idle-timeout value is not 10 minutes, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration sys global | grep -i admintimeout The output should be: set admintimeout 10 If the admintimeout parameter is not set to 10 minutes, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-234215`

### Rule: The FortiGate device must generate unique session identifiers using a FIPS 140-2-approved random number generator.

**Rule ID:** `SV-234215r879639_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sequentially generated session IDs can be easily guessed by an attacker. Employing the concept of randomness in the generation of unique session identifiers helps to protect against brute-force attacks to determine future session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement is applicable to devices that use a web interface for device management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Session IDs are generated using the FIPS random generator if the device is in FIPS mode. To verify login to the FortiGate GUI with Super-Admin privilege: 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # get system status | grep -i fips The output should be: FIPS-CC mode: enable If FIPS-CC mode parameter is not set to enable, this is a finding.

## Group: SRG-APP-000231-NDM-000271

**Group ID:** `V-234216`

### Rule: The FortiGate device must only allow authorized administrators to view or change the device configuration, system files, and other files stored either in the device or on removable media (such as a flash drive).

**Rule ID:** `SV-234216r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement is intended to address the confidentiality and integrity of system information at rest (e.g., network device rule sets) when it is located on a storage device within the network device or as a component of the network device. This protection is required to prevent unauthorized alteration, corruption, or disclosure of information when not stored directly on the network device. Files on the network device or on removable media used by the device must have their permissions set to allow read or write access to those accounts that are specifically authorized to access or change them. Note that different administrative accounts or roles will have varying levels of access. File permissions must be set so that only authorized administrators can read or change their contents. Whenever files are written to removable media and the media removed from the device, the media must be handled appropriately for the classification and sensitivity of the data stored on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click System. 2. Click Administrators. 3. Click each administrator and hover over the profile that is assigned to the role. 4. Click Edit. 5. Verify that the permission on System is set to READ or Read/Write. If any unauthorized administrator has Read/Write access to System, this is a finding. or 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command for all low privileged admin users: # show system admin {ADMIN NAME} | grep -i accprofile The output should be: set accprofile {PROFILE NAME} Use the profile name from the output result of above command. # show system accprofile {PROFILE NAME} | grep -i sysgrp The output should be: set sysgrp none If any low privileged admin user has sysgrp parameter set to values other than NONE, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-234217`

### Rule: The FortiGate device must protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-234217r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS prohibit a resource from being available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD-level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Policy and Objects. 2. Click on IPv4 DoS Policy or IPv6 DoS Policy. 3. Identify the port designated for FortiGate device management. 4. Select the policy and click Edit. 5. Verify appropriate L3 Anomalies and L4 Anomalies are configured to meet the organization requirement. 6. Verify the policy is Enabled. If appropriate DoS policies are not defined or are disabled, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-234218`

### Rule: The FortiGate device must be configured to send log data to a central log server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-234218r917639_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can be used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, is important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that FortiGate is configured to send logs to a central log server. Log in via the FortiGate GUI with super-admin privileges. 1. Navigate to Log and Report. 2. Navigate to Log Settings. 3. Locate the Remote Logging and Archiving section. 4. Verify FortiGate is configured to log to a FortiAnalyzer or a syslog server. or Open a CLI console via SSH or from the "CLI Console" button in the GUI. Run the following commands and verify that at least one of the settings reflects "set status enable" in the output: # show full-configuration | grep -A1 'log fortianalyzer' # show full-configuration | grep -A1 'log syslogd.* setting' The CLI output will indicate "set status enable" if configured. If the FortiGate is not logging to a central log server, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-234219`

### Rule: The FortiGate device must limit the number of logon and user sessions.

**Rule ID:** `SV-234219r917462_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege and open a CLI console available from the GUI. or Connect via SSH. Run the following command: show full-configuration sys global | grep -i admin Check the output of the following lines: set admin-concurrent disable set admin-login-max <number as defined by the organization> If set admin-concurrent is not set to disable, this is a finding. If set admin-login-max is not set to a number defined by the organization, this is a finding. The default setting is 100.

## Group: SRG-APP-000131-NDM-000243

**Group ID:** `V-234220`

### Rule: The FortiGate device must only install patches or updates that are validated by the vendor via digital signature or hash.

**Rule ID:** `SV-234220r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the network device. Verifying software components have been digitally signed or hashed ensures that the software has not been tampered with and has been provided by a trusted vendor. Accordingly, patches, service packs, or application components must be signed with a certificate or verified with an integrity hash provided by the vendor. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and has been provided by a trusted vendor.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the process used to apply updates and patches to the system. If the system is updated via a FortiGuard or FortiManager server, those solutions meet the requirement and this is NOT a finding. If the system is not using a FortiGuard or FortiManager server, and a process is not defined to manually verify the update hash value with the vendor site, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-234221`

### Rule: The FortiGate device must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-234221r879607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system password-policy | grep -i change The output should be: # set change-4-characters enable If the change-4-characters parameter is set to disable, this is a finding. If the change-4-characters parameter is set to enable, this mitigates to a CAT III finding, as this is a mitigation to at least changing four characters when changing the account of last resort. This is a limitation of the device. It is not possible to mitigate to "Not A Finding".

