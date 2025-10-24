# STIG Benchmark: Forescout Network Device Management Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-230930`

### Rule: Forescout must limit the number of concurrent sessions to one for each administrator account.

**Rule ID:** `SV-230930r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial of service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions must be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Forescout requires a limit of one session per user. This requirement may be verified by demonstration or configuration review. 1. Log on to the Forescout Administrator UI. 2. From the menu, select Tools >> Options >> CounterAct user profiles >> Password and Sessions >> Session. 3. Verify the "allow only one login session per user", "Terminate existing session upon new login", and "Console and web portal sessions cannot exist concurrently". If Forescout does not enforce one session per user, this is a finding.

## Group: SRG-APP-000317-NDM-000282

**Group ID:** `V-230931`

### Rule: Forescout must terminate the account of last resort password when members with access to the password leave the group.

**Rule ID:** `SV-230931r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A shared/group account credential is a shared form of authentication that allows multiple individuals to access the network device using a single account. If shared/group account credentials are not terminated when individuals leave the group, the user that left the group can still gain access even though they are no longer authorized. There may also be instances when specific user actions need to be performed on the network device without unique administrator identification or authentication. Examples of credentials include passwords and group membership certificates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation to verify a procedure exists to change the account of last resort and root account password when users with knowledge of the password leave the group. If a procedure does not exist to change the account of last resort and root account password when users with knowledge of the password leave the group, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-230932`

### Rule: Forescout must be configured with only one web account and one CLI account of last resort with limited access and used only when the authentication server is unavailable.

**Rule ID:** `SV-230932r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the "account of last resort" since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit must be added to the envelope as a record. Administrators must secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only one local account exists and that it has full administrator privileges. 1. Log on to the Forescout Administrator UI. 2. From the menu, select Tools >> Options >> CounterACT User Profiles. If local accounts in the CounterACT User profile or CLI exist other than the accounts of last resort, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-230933`

### Rule: Forescout must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must lock out the user account from accessing the device for 15 minutes.

**Rule ID:** `SV-230933r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Forescout is configured either to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period, or to use an authentication server to perform this function. 1. Log on to the Forescout Administrator UI. 2. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 3. Verify the "Lock account after" radio button is selected. 4. Verify that "3" password failures for "15 minutes" is configured. If the limit of three consecutive invalid logon attempts by a user during a 15-minute time period is not enforced, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-230934`

### Rule: Forescout must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-230934r615887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. The banner must be formatted in accordance with DTM-08-060.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Log on to the Forescout Administrator UI. 2. Select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 3. Select the Login tab and check the "Display this Notice and Consent Message after login" option. 4. Select the "Before login, prompt user to accept these Terms and Conditions" and view the text. If the banner is not present or not in exact compliance with the current verbiage and spacing in DTM-08-060, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-230935`

### Rule: Forescout must retain the Standard Mandatory DoD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-230935r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to the device allowing the administrator access to the network device. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DoD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of CLI access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, then entering the password is also acceptable. The web management tool configuration setting works for both the CLI and the web management tool.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Forescout retains the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and takes explicit actions to log on for further access. Attempt to log on to the Forescout device as a system administrator using the web management tool. If Forescout does not retain the Standard Mandatory DoD-approved Notice and Consent Banner on the screen until users acknowledge the usage conditions and take explicit actions to log on for further access, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-230936`

### Rule: Forescout must generate log records when successful attempts to access privileges occur.

**Rule ID:** `SV-230936r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under "User Operations", verify "Include user operations" is checked. If Forescout does not generate log records when successful attempts to access privileges occur, this is a finding.

## Group: SRG-APP-000495-NDM-000318

**Group ID:** `V-230937`

### Rule: Forescout must generate log records when attempts to modify administrator privileges occur.

**Rule ID:** `SV-230937r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records when attempts to modify administrator privileges occur, this is a finding.

## Group: SRG-APP-000499-NDM-000319

**Group ID:** `V-230938`

### Rule: Forescout must generate log records when attempts to delete administrator privileges occur.

**Rule ID:** `SV-230938r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records when attempts to delete administrator privileges occur, this is a finding.

## Group: SRG-APP-000503-NDM-000320

**Group ID:** `V-230939`

### Rule: Forescout must generate log records showing when successful logon attempts occur.

**Rule ID:** `SV-230939r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records when successful logon attempts occur, this is a finding.

## Group: SRG-APP-000504-NDM-000321

**Group ID:** `V-230940`

### Rule: Forescout must generate log records for privileged activities or other system-level access.

**Rule ID:** `SV-230940r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records when for privileged activities or other system-level access, this is a finding.

## Group: SRG-APP-000505-NDM-000322

**Group ID:** `V-230941`

### Rule: Forescout must generate log records showing starting and ending time for administrator access to the system.

**Rule ID:** `SV-230941r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records showing starting and ending time for administrator access to the system, this is a finding.

## Group: SRG-APP-000506-NDM-000323

**Group ID:** `V-230942`

### Rule: Forescout must generate log records when concurrent logons from different workstations occur.

**Rule ID:** `SV-230942r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Log records can be generated from various components within the network device (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog trigger is configured. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Under User Operations, verify "Include user operations" is checked. If Forescout does not generate log records when concurrent logons from different workstations occur, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-230943`

### Rule: The Forescout must configure a remote syslog where audit records are stored on a centralized logging target that is different from the system being audited.

**Rule ID:** `SV-230943r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Send Events To. 3. Click the IP address of the site's centralized syslog server. 4. Verify "Use TLS" is checked. 5. Verify OCSP, Identity, Facility, and Severity, as required by the SSP, are configured. If the site's syslog server is not configured or if it is not configure to use TLS and OCSP, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-230944`

### Rule: Forescout must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-230944r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while the source synchronizes time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Forescout is configured to synchronize internal clocks with the organization's primary and secondary NTP servers. 1. Open an SSH session and authenticate to the Forescout command line. 2. Verify a primary and secondary NTP server has been configured with the command "fstool ntp test". If Forescout is not configured to synchronize internal information system clocks with the organization's primary and secondary NTP servers, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-230945`

### Rule: Forescout must be configured to use Coordinated Universal Time (UTC).

**Rule ID:** `SV-230945r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Forescout records time stamps for log records that can be mapped to UTC. This requirement may be verified by demonstration or configuration review. Verify by connecting to the appliance via SSH using standard user/operator privilege. 1. Type "date" at the command prompt. 2. Verify the date references accurate time and "UTC" shows just before the year. If Forescout does not record time stamps for log records that can be mapped to UTC, this is a finding.

## Group: SRG-APP-000378-NDM-000302

**Group ID:** `V-230946`

### Rule: Forescout must prohibit installation of software without explicit privileged permission by only authorized individuals.

**Rule ID:** `SV-230946r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing anyone to install software, without explicit privileges, creates the risk that untested or potentially malicious software will be installed on the system. This requirement applies to code changes and upgrades for all network devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device prohibits installation of software without explicit privileged status. This requirement may be verified by demonstration or configuration review. 1. From the menu, select Tools >> Options >> User Console and Options. 2. Select (highlight) the user profile to be reviewed (group or user) and then select Edit >> Permissions. 3. Check a sampling of users against the current SSP to verify only the users that should have privilege to update software have the Software Upgrade privilege selected. If installation of software is not prohibited without explicit privileged status, this is a finding.

## Group: SRG-APP-000380-NDM-000304

**Group ID:** `V-230947`

### Rule: Forescout must enforce access restrictions associated with changes to device configuration.

**Rule ID:** `SV-230947r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to device configuration may have significant effects on the overall security of the system. For Forescout, ensure only authorized users have access to user profile permissions. All other admins are blocked from access via the console tools and/or web portal based on permissions set on the Edit user profile.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces access restrictions associated with changes to device configuration. 1. Log on to the Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> User Console and Options. 3. Select (highlight) the user profile to be reviewed (group or user) and then select Edit >> Permissions. 4. Check user against the current SSP and ensure only the users that should have the privilege to make changes have the CounterACT Appliance Configuration; CounterACT Appliance Control; Module Control; Multiple CounterACT Appliance Management; Policy Control; Policy Management; and User Management privileges selected. If the network device does not enforce such access restrictions, this is a finding.

## Group: SRG-APP-000381-NDM-000305

**Group ID:** `V-230948`

### Rule: Forescout must audit the enforcement actions used to restrict access associated with changes to the device.

**Rule ID:** `SV-230948r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without auditing the enforcement of access restrictions against changes to the device configuration, it will be difficult to identify attempted attacks, and an audit trail will not be available for forensic investigation for after-the-fact actions. Forescout must only be configures such that only authorized users have access to user profile permissions. All other admins are blocked from access via the console tools and/or web portal based on permissions set on the Edit user profile.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device audits the enforcement actions used to restrict access associated with changes to the device. This requirement may be verified by demonstration, configuration review, or validated test results. 1. Log on to the Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> User Console and Options. 3. Select (highlight) the user profile to be reviewed (group or user) and then select Edit >> Permissions. 4. Check user against current SSP and ensure only the users with privileges to make changes have the Least Privilege required permissions. If the network device does not audit the enforcement actions used to restrict access associated with changes to the device, this is a finding.

## Group: SRG-APP-000131-NDM-000243

**Group ID:** `V-230949`

### Rule: Forescout must prevent the installation of patches, service packs, plug-ins, or modules without verification the update has been digitally signed using a certificate that is recognized and approved by the organization.

**Rule ID:** `SV-230949r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Changes to any software components can have significant effects on the overall security of the network device. Verifying software components have been digitally signed using a certificate that is recognized and approved by the organization ensures the software has not been tampered with and has been provided by a trusted vendor. Accordingly, patches, service packs, or application components must be signed with a certificate recognized and approved by the organization. Verifying the authenticity of the software prior to installation validates the integrity of the patch or upgrade received from a vendor. This ensures the software has not been tampered with and has been provided by a trusted vendor. Self-signed certificates are disallowed by this requirement. The device should not have to verify the software again. This requirement does not mandate DoD certificates for this purpose; however, the certificate used to verify the software must be from an approved CA. Customer portal updates file download section on the vendor website has the MD5 hashes for the updates files. Currently, this is the method used by DoD to pull down files rather than using the internal connection to the Forescout server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify by inspecting the SSP or documentation to determine if there is a procedure for validating the MD5 hash against the Forescout updates.forescout.com portal to ensure that the software has come from the Forescout server. If the site does not have a documented process to prevent the installation of patches, service packs, or application components without verification the software component has been digitally signed using a certificate recognized and approved by the organization, this is a finding.

## Group: SRG-APP-000133-NDM-000244

**Group ID:** `V-230950`

### Rule: Forescout must limit privileges to change the modules and OSs resident within software libraries.

**Rule ID:** `SV-230950r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to any software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals must be allowed administrative access to the network device for implementing any changes or upgrades. If the network device were to enable non-authorized users to make changes to software libraries, those changes could be implemented without undergoing testing, validation, and approval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if there are users defined in Forescout that are not authorized to change the software libraries. Verify that Administrator privileges have been restricted for these users. This is verified by reviewing the administrator account profiles and auditing the assigned privilege for updated Forescout software. 1. Log on to the Forescout Console and select Tools >> Options >> Console User Profiles. 2. Select the user group that is not authorized access according to the SSP. 3. Select "Edit" and the "Permissions" tab 4. Verify the users do not have the "Plugin Management" and "Software Upgrade" options selected. If Forescout is not configured to limit privileges to change the software resident within software libraries for unauthorized users, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-230951`

### Rule: Forescout must  enforce access restrictions associated with changes to the firmware, OS, USB port, and console port.

**Rule ID:** `SV-230951r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals must be allowed administrative access to the network device for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, ACLs, and policy filters. There is a USB port and a console RJ45 port. The Console port is secured by the CLI security configuration. The USB port is only accessible via the CLI, not the web manager tool. The user will be prompted to see if it should be turned on. It is off by default and requires authorized login from the CLI.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Forescout to determine if only authorized administrators have permissions for changes, deletions, and updates on the network device. Inspect the maintenance log to verify changes are being made only by the system administrators. 1. Log on to the Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> CounterACT User Profiles. 3. Select (highlight) the user profile to be reviewed (group or user) and then select "Edit". 4. Verify the non-administrator account selected does not have "update" on the "Permissions" tab for "Forescout Appliance Configuration". If unauthorized users are allowed to change the hardware or software, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-230952`

### Rule: Forescout must be configured to use an authentication server for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-230952r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, log records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Forescout configuration to determine if administrative accounts for device management exist on the device other than the account of last resort and root account. 1. Log on to the Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Console Preferences. 3. Select (highlight) the user profile to be reviewed (group or user) and then select "Edit". 4. Verify each user profile is for an approved administrator. 5. Verify each external LDAP group account profile by verifying on the trusted external directory group membership. If any administrative accounts other than the account of last resort and root account exist on the device, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-230953`

### Rule: Forescout must be running an operating system release that is currently supported by the vendor.

**Rule ID:** `SV-230953r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities. In Oct 2021, there is plan to make Version 7 end-of-life. This will be stated on the product lifecycle page of the Forescout website. All versions of V8 and above are authorized for use in DoD. Version 8 or later is mandatory after October 2021.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that Forescout is still running supported operating system versions and that all vulnerability patches and updates have been applied. Verify the installed version is supported by Forescout by checking the Forescout support website lifecycle page. Currently, Version 8 or later is mandatory after October 2021. If Forescout is running an operating system release that is not supported by the vendor, this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-230954`

### Rule: If the network device uses role-based access control, Forescout must enforce organization-defined, role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-230954r616548_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. Forescout has three predefined user roles: Admin, Web Access, and Console User. The Admin role has access to all data and management functions. By default, the Console role has access to the management console and the Web role has access to the view-only portal. However, both roles may be assigned one or more permissions, each with its own set of privileges to the data and functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the administrative accounts assigned to each role are documented within the SSP and have been configured correctly with least privilege. 1. Log on to Forescout UI. 2. Select Tools >> Options >> CounterACT User Profiles. 3. Select username >> Edit >> Permissions. Check the SSP against created users and ensure least privilege has been configured properly. Options include Custom accounts for Console Access and Web Access. Each access account is then further established with permissions based on the user's authorizations. If Forescout does not enforce organization-defined, role-based access control policies over defined subjects and objects, this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-230955`

### Rule: Forescout must generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-230955r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack; to recognize resource utilization or capacity thresholds; or to identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the syslog triggers are configured in accordance with SSP requirements. 1. Log on to Forescout Administrator UI with admin or operator credentials. 2. From the menu, select Tools >> Options >> Modules >> Syslog >> Syslog Triggers. 3. Ensure the proper NAC events and System Logs and Events are selected in compliance with the SSP. If Forescout does not generate log records for a locally developed list of auditable events, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-230956`

### Rule: Forescout must be configured to conduct backups of system-level information contained in the information system when changes occur.

**Rule ID:** `SV-230956r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who utilize this critical network component. Perform scheduled backups of the Forescout system to FTP, SFTP, and SCP sites. Using scheduled backups provides extra safety and protection against hard drive failures and data loss. The system backup feature saves all CounterACT device and Console settings. This data includes the following: - Configuration - License - Operating System configuration - Plugins/Modules These categories include, for example: - Forescout platform IP address - License information - Channel - Email - Internal network parameters - Basic and advanced NAC Policy definitions - Legitimate traffic definitions - Report schedules</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Forescout to determine if the network device is configured to conduct backups of system-level information contained in the information system when changes occur or weekly, whichever is sooner. 1. Open the Forescout Console and select Tools >> Advanced >> Backup. 2. On the “System Backup” tab, verify the "Enable System Backup" radio button is selected. 3. Verify the Backup schedule is selected to at least "weekly". If Forescout does not support the organizational requirement to conduct backups of system-level data according to the defined frequency, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-230957`

### Rule: Forescout must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-230957r616550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who utilize this critical network component. Perform scheduled backups of the Forescout system to FTP, SFTP, and SCP sites. Using scheduled backups provides extra safety and protection against hard drive failures and data loss. The system backup feature saves all CounterACT device and Console settings. This data includes the following: - Configuration - License - Operating System configuration - Plugins/Modules These categories include, for example: - Forescout platform IP address - License information - Channel - Email - Internal network parameters - Basic and advanced NAC Policy definitions - Legitimate traffic definitions - Report schedules</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check Forescout to determine if the network device is configured to conduct backups. 1. Open the Forescout Console and select Tools >> Advanced >> Backup. 2. On the “System Backup” tab, verify the "Enable System Backup" radio button is selected. 3. Verify the Backup schedule is selected to at least "weekly". If Forescout does not support organizational requirements to conduct backups of information system documentation, including security-related documentation when changes occur or weekly, whichever is sooner, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-230958`

### Rule: Forescout must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-230958r616552_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Forescout obtains public key certificates from an appropriate certificate policy through an approved service provider. To review the Web server certificate presented for captive portal/authentication: 1. Open a command line SSH to Forescout appliance or Enterprise Manager. 2. Run the following command: >fstool cert test 3. Verify all Web server certificate(s) are printed and reviewable. 4. Verify the signing authority is from an approved certificate authority. If the network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-230959`

### Rule: Forescout must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-230959r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Forescout is capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. Wireless is an example only of a service that is frequently unnecessary in many Forescout implementations. Reword more generically and be sure to look for module that are not part of the UC ACL default and may have been installed by the site and therefore are not authorized for use in DoD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the plugin tool and remove all unneeded or unsecure services. 1. Connect to the Forescout Console and select Tools >> Options >> Plugins. 2. Review the list of plugins. If an unnecessary or nonsecure service is "Enabled", select the plugin and then select "Configure". If no configuration is present, this is a finding. If any unnecessary or nonsecure functions are enabled, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-230960`

### Rule: Forescout must disable the Request Customer Verification setting.

**Rule ID:** `SV-230960r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. This option connects to a user verification server at Forescout infrastructure used for verification of customer profiles and must not be used in DoD. If accidentally checked, this must error out.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the Password and Sessions login options, ensure "request customer verification" is not enabled. 1. Log on to the Forescout Administrator UI. 2. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 3. Ensure the option for "request customer verification" is unchecked. If the Request Customer Verification setting is enabled, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-230961`

### Rule: Forescout must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-230961r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Forescout configuration to determine if the network device authenticates SNMP endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based. 1. Select Tools >> Options >> Switch. 2. Select a network device and review the "SNMP" tab. 3. Verify that the "SNMPv3" option is selected and the "HMAC-SHA" authentication protocol is selected. 4. Verify that the "use privacy" radio button is selected and "AES-128" is also selected from the drop-down box. If Forescout does not authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC), this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-230962`

### Rule: Before establishing a connection with a Network Time Protocol (NTP) server, Forescout must authenticate using a bidirectional, cryptographically based authentication method that uses a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the NTP server.

**Rule ID:** `SV-230962r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source. Currently, AES block cipher algorithm is approved for use in DoD for both applying cryptographic protection (e.g., encryption) and removing or verifying the protection that was previously applied (e.g., decryption). NTP devices use MD5 authentication keys. The MD5 algorithm is not specified in either the FIPS or NIST recommendation. However, MD5 is preferred to no authentication at all. The trusted-key statement permits authenticating NTP servers. The product must be configured to support separate keys for each NTP server. Severs must have a PKI device certificate involved for use in the device authentication process. Configurable to use SHA-1 when SNMPv3 is configured which is recommended by the vendor and required by DoD. Vendor cautions that this may impact performance with other devices. Downgrade to not a finding if correctly configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Forescout configuration to determine if Forescout authenticates SNMP endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based. 1. Select Tools >> Options >> Switch. 2. Select a network device and review the "SNMP" tab. 3. Verify the "SNMPv3" option is selected and the "HMAC-SHA" authentication protocol is selected. 4. Verify the "use privacy" radio button is selected and "AES-128" is also selected from the drop-down box. If SNMPv3 with HMAC-SHA is configured, this is not a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-230963`

### Rule: Forescout must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-230963r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and, where applicable, a root account. Passwords must only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 2. Verify the first "password must contain at least" is checked. 3. Verify there is a minimum of one in the "upper case alphabetic characters" configuration box. If the Forescout does not enforce password complexity by requiring that at least one uppercase character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-230964`

### Rule: Forescout must enforce password complexity by requiring that at least one lower-case character be used.

**Rule ID:** `SV-230964r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 2. Verify the second "password must contain at least" is checked. 3. Verify there is a minimum of one in the "lower case alphabetic characters" configuration box. If the Forescout does not enforce password complexity by requiring that at least one lower-case character be used, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-230965`

### Rule: Forescout must enforce a minimum 15-character password length.

**Rule ID:** `SV-230965r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device enforces a minimum 15-character password length. This requirement may be verified by demonstration or configuration review. 1. Log on to the Forescout Administrator UI. 2. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 3. Verify the "minimum length" is configured for "15". If Forescout does not enforce a minimum 15-character password length, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-230966`

### Rule: Forescout must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-230966r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 2. Verify the third "password must contain at least" is checked. 3. Verify there is 1 (or higher) in the "digits" configuration box. If the Forescout does not enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-230967`

### Rule: Forescout must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-230967r615886_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 2. Verify the fourth "password must contain at least" is checked. 3. Verify there is 1 (or higher) in the "in the special character" configuration box. If the Forescout does not enforce password complexity by requiring that at least one special character be used, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-230968`

### Rule: Forescout must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-230968r615886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 2. Verify the fifth "password must contain at least" is checked. 3. Verify there is 1 (or higher) in the "repeated characters or digits" configuration box. If Forescout does not enforce the requirement that when the password is changed, the characters are changed in at least eight of the positions within the password, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-230969`

### Rule: Forescout must use FIPS 140-2 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-230969r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised. Network devices utilizing encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on using the CLIAdmin credentials established upon initial configuration. Verify FIPS mode by typing the command "fstool version". If Forescout does not use FIPS 140-2 approved algorithms for authentication to a cryptographic module, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-230970`

### Rule: Forescout must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-230970r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the device is configured to terminate management sessions after 10 minutes of inactivity, verify the timeout value is configured. 1. Go to the Enterprise Manager Console. 2. From the menu, select Tools >> Options >> CounterACT User Profiles >> Password and Sessions. 3. Verify the "User Inactivity Timeout" check box is selected and the associated setting is set to "10 minutes". If applicable, verify exceptions to this requirement are documented and signed. If Forescout does not terminate the connection associated with an Enterprise Manager Console at the end of the session or after 10 minutes of inactivity, this is a finding.

## Group: SRG-APP-000231-NDM-000271

**Group ID:** `V-230971`

### Rule: Forescout must only allow authorized administrators to view or change the device configuration, system files, and other files stored either in the device or on removable media (such as a flash drive).

**Rule ID:** `SV-230971r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requirement addresses the confidentiality and integrity of system information at rest (e.g., network device rule sets) when it is located on a storage device within the network device or as a component of the network device. This protection is required to prevent unauthorized alteration, corruption, or disclosure of information when not stored directly on the network device. Files on the network device or on removable media used by the device must have their permissions set to allow read or write access to those accounts specifically authorized to access or change them. Note that different administrative accounts or roles will have varying levels of access. File permissions must be set so that only authorized administrators can read or change their contents. Whenever files are written to removable media and the media removed from the device, the media must be handled appropriately for the classification and sensitivity of the data stored on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
List the contents of Forescout’s local storage, including any drives supporting removable media (such as flash drives), and check the file permissions of all files on those drives. 1. Review accounts with incorrect update privileges to Forescout appliance configuration by selecting Tools >> Options >> CounterACT User Profiles. 2. Select a user to edit. 3. Select the "Permissions" tab. 4. Verify the "CounterAct Appliance Configuration" and "CounterACT Appliance Control" radio buttons are set to "View only". If any files allow read or write access by accounts not specifically authorized access or access using non-privileged accounts, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-230972`

### Rule: Forescout must be configured to send log data to a central log server for the purpose of forwarding alerts to the administrators and the Information System Security Officer (ISSO).

**Rule ID:** `SV-230972r615886_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can be used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Forescout logs periodically to ensure proper auditing functions are still enabled and have not been changed. A proper security policy performs periodic checks to help ensure the proper information is being gathered in the event of a security breach, or internal/external threat. If the Forescout auditing functions are disabled or have been changed, this is a finding.

