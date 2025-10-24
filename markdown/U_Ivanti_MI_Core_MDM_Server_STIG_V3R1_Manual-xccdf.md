# STIG Benchmark: Ivanti EPMM Server Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-UEM-000001

**Group ID:** `V-251400`

### Rule: The Ivanti EPMM server must limit the number of concurrent sessions per privileged user account to three or less concurrent sessions.

**Rule ID:** `SV-251400r1004719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be defined based upon mission needs and the operational environment for each system. Satisfies: FMT_SMF.1.1(2) b Reference: PP-MDM-431010</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following procedure to limit concurrent sessions per privileged users: On the Admin page for each privileged user, verify Actions Edit Role select "Enforce single session (all spaces)" is selected. If "Enforce single session (all spaces)" is not selected for each user, this is a finding.

## Group: SRG-APP-000003-UEM-000003

**Group ID:** `V-251401`

### Rule: The Ivanti EPMM server must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-251401r1004720_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock, but may be at the application level where the application interface window is secured instead. Satisfies: FMT_SMF.1.1(2) c.8 Reference: PP-MDM-411047</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the session timeout is set to 15 minutes or less. In the Admin Portal, go to Settings >> General >> Timeout. Verify the session timeout is set to 5, 10, or 15. If the session timeout is not set to 5, 10, or 15, this is a finding.

## Group: SRG-APP-000065-UEM-000036

**Group ID:** `V-251402`

### Rule: The Ivanti EPMM server must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-251402r1004723_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Satisfies: FMT_SMF.1(2)b. Reference: PP-MDM-431028</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ivanti EPMM server is configured to enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period. In the Core server, navigate to the following: Settings >> Security >> Password Policy. Verify the number of failed attempts is set to 3 and Auto-Lock Time is set to 900 seconds. If the number of failed attempts is not set to 3 and Auto-Lock Time is not set to 900 seconds, this is a finding.

## Group: SRG-APP-000068-UEM-000037

**Group ID:** `V-251403`

### Rule: The Ivanti EPMM server must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the application.

**Rule ID:** `SV-251403r1004724_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DoD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: FTA_TAB.1.1, FMT_SMF.1.1(2) c.2 Reference: PP-MDM-411056</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review MDM server documentation and configuration settings to determine if the MDM server is using the warning banner and the wording of the banner is the required text. On the MDM console, do the following: 1. Connect to the MobileIron Core Server using SSH. 2. Type in a user name and press enter. 3. Verify the required banner is displayed before the password prompt. The required text is found in the Vulnerability Discussion. If the required banner is not presented, this is a finding. 1. Connect to the MobileIron Core Server system manager portal using a web browser. 2. Verify the required banner is displayed on the web page. The required text is found in the Vulnerability Discussion. If the required banner is not presented, this is a finding. 1. Connect to the MobileIron Core Server administrator portal using a web browser. 2. Verify the required banner is displayed on the web page. If the required banner is not presented, this is a finding.

## Group: SRG-APP-000108-UEM-000062

**Group ID:** `V-251404`

### Rule: The Ivanti EPMM server must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-251404r1004725_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both. Satisfies: FAU_ALT_EXT.1.1 Reference: PP-MDM-412059</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Core is configured to alert the ISSO and SA in the event of an audit processing failure: In the Core console, go to Logs >> Event Settings >> Add New System Event. Verify System Storage Threshold has been reached is checked. If System Storage Threshold has been reached is not checked, this is a finding.

## Group: SRG-APP-000125-UEM-000074

**Group ID:** `V-251405`

### Rule: The Ivanti EPMM server must back up audit records at least every seven days onto a log management server.

**Rule ID:** `SV-251405r1004726_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes ensuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media from the system being audited on an organizationally defined frequency helps ensure, in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions. Satisfies: FAU_STG_EXT.1.1, FMT_SMF.1.1(2) Refinement b</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Splunk is configured for automated log export. Step 1: Verify the Splunk Forwarder is enabled. 1. Log in to System Manager. 2. Go to Settings >> Services. 3. Verify that the "Enable" toggle is ON and "Running" is displayed. If "Enable" toggle is not ON or "Running" is not displayed, this is a finding. Step 2: Verify that Splunk Indexer is configured. 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Indexer. 3. Verify that there is an entry and the Status is "Connected". If there is no entry for Splunk Indexer or the Status is "Not Connected", this is a finding. Step 3: Verify "Audit Log" is enabled in the Splunk "data to index". 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Data to open the "Data to Index" window. 3. Verify "Audit Log" is included in the "Data To Index". If "Audit Log" is not included in the "Data To Index", this is a finding. Note: Syslog can be used instead of Splunk.

## Group: SRG-APP-000149-UEM-000083

**Group ID:** `V-251406`

### Rule: The Ivanti EPMM server must be configured to use a DoD Central Directory Service to provide multifactor authentication for network access to privileged and non-privileged accounts.

**Rule ID:** `SV-251406r1004727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire MDM server infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the MDM server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos). Satisfies: FIA Reference: PP-MDM-414003</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MDM console, do the following: 1. Log in to the MobileIron Core Server administrator portal as a user with the security configuration administrator role using a web browser. 2. Select "Services" on the web page. 3. Select "LDAP" on the web page. 4. Click the edit icon on an existing LDAP configuration to be tested. 5. Select "Test" on the LDAP server configuration dialog. 6. Enter a valid LDAP user ID and select "Submit". 7. Verify the LDAP query is successful and shows user attributes in a dialog box. Note: All administrator accounts must be configured for LDAP authentication unless a select number of local accounts have been approved by the AO. Verify AO approval if local accounts (not using LDAP authentication) are configured on the Core server. If the MDM server does not leverage the MDM platform user accounts and groups for MDM server user identification and authentication, this is a finding.

## Group: SRG-APP-000164-UEM-000094

**Group ID:** `V-251407`

### Rule: The Ivanti EPMM server must enforce a minimum 15-character password length.

**Rule ID:** `SV-251407r1004728_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431018</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a 15-character length for local user accounts has been configured: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify the Min Password Length is set to 15. If the Min Password Length is not set to 15, this is a finding.

## Group: SRG-APP-000165-UEM-000095

**Group ID:** `V-251408`

### Rule: The Ivanti EPMM server must prohibit password reuse for a minimum of four generations.

**Rule ID:** `SV-251408r1004729_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431025</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Core is configured to enforce password history reuse of four last passwords: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify "Enforce Password History (Last 4 passwords)" is enabled. If "Enforce Password History (Last 4 passwords)" is not enabled, this is a finding.

## Group: SRG-APP-000166-UEM-000096

**Group ID:** `V-251409`

### Rule: The Ivanti EPMM server must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-251409r1004730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431020</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the local user account uses at least one uppercase character: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify "Upper Case" is checked. If "Upper Case" is not checked, this is a finding.

## Group: SRG-APP-000167-UEM-000097

**Group ID:** `V-251410`

### Rule: The Ivanti EPMM server must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-251410r1004731_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431019</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the local user account uses at least one lowercase character: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify "Lower Case" is checked. If "Lower Case" is not checked, this is a finding.

## Group: SRG-APP-000168-UEM-000098

**Group ID:** `V-251411`

### Rule: The Ivanti EPMM server must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-251411r1004732_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431021</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the local user account uses at least one numeric character: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify "Numeric" is checked. If "Numeric" is not checked, this is a finding.

## Group: SRG-APP-000169-UEM-000099

**Group ID:** `V-251412`

### Rule: The Ivanti EPMM server must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-251412r1004733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *. Satisfies: FMT_SMF.1(2)b Reference: PP-MDM-431022</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the local user account uses at least one special character: 1. Log in to the Core console. 2. Security >> Password Policy. 3. Verify "Special" is checked. If "Special" is not checked, this is a finding.

## Group: SRG-APP-000179-UEM-000110

**Group ID:** `V-251413`

### Rule: The Ivanti EPMM server must use FIPS-validated SHA-2 or higher hash function to protect the integrity of keyed-hash message authentication code (HMAC), Key Derivation Functions (KDFs), Random Bit Generation, and hash-only applications.

**Rule ID:** `SV-251413r1004734_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Nonlocal maintenance and diagnostic activities are activities conducted by individuals communicating through either an external network (e.g., the internet) or an internal network. Note: Although allowed by SP800-131Ar1 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DoD systems should not be configured to use SHA-1 for integrity of remote access sessions. To protect the integrity of the authenticator and authentication mechanism used for the cryptographic module used by the network device, the application, operating system, or protocol must be configured to use one of the following hash functions for hashing the password or other authenticator in accordance with SP 800-131Ar1: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, and SHA3-512. Applications also include HMAC, KDFs, Random Bit Generation, and hash-only applications (e.g., hashing passwords and use for compute a checksum). For digital signature verification, SP800-131Ar1 allows SHA-1 for legacy use only, but this is discouraged by DoD. Separate requirements for configuring applications and protocols used by each product (e.g., SNMPv3, SSH, NTP, and other protocols and applications that require server/client authentication) are required to implement this requirement. Satisfies: FCS_COP.1.1(2)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify MobileIron Core is in FIPS mode. ssh to command line console of the Core. Enable >> show fips. Verify FIPS mode is configured. If FIPS mode is not configured, this is a finding.

## Group: SRG-APP-000295-UEM-000169

**Group ID:** `V-251414`

### Rule: The Ivanti EPMM server must automatically terminate a user session after an organization-defined period of user inactivity.

**Rule ID:** `SV-251414r1004735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination addresses the termination of user-initiated logical sessions in contrast to the termination of network connections that are associated with communications sessions (i.e., network disconnect). A logical session (for local, network, and remote access) is initiated whenever a user (or process acting on behalf of a user) accesses an organizational information system. Such user sessions can be terminated (and thus terminate user access) without terminating network sessions. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. This capability is typically reserved for specific application system functionality where the system owner, data owner, or organization requires additional assurance. Based upon requirements and events specified by the data or application owner, the application developer must incorporate logic into the application that will provide a control mechanism that disconnects users upon the defined event trigger. The methods for incorporating this requirement will be determined and specified on a case-by-case basis during the application design and development stages. Satisfies: FMT_SMF.1.1(2) b Reference: PP-MDM-431014</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server or platform configuration and verify the server is configured to lock after 15 minutes of inactivity. If, in the Admin Portal, Settings >> General >> Timeout is not set to 15 minutes or less, this is a finding. The current value for the session timeout will be displayed in minutes.

## Group: SRG-APP-000358-UEM-000228

**Group ID:** `V-251415`

### Rule: The Ivanti EPMM server must be configured to transfer Ivanti EPMM server logs to another server for storage, analysis, and reporting. Note: Ivanti EPMM server logs include logs of UEM events and logs transferred to the Ivanti EPMM server by UEM agents of managed devices. 

**Rule ID:** `SV-251415r1004742_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Note: UEM server logs include logs of UEM events and logs transferred to the UEM server by UEM agents of managed devices. Satisfies: FMT_SMF.1.1(2) c.8, FAU_STG_EXT.1.1(1) Reference: PP-MDM-411054</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Splunk is configured for automated log export. Step 1: Verify that the Splunk Forwarder is enabled. 1. Log in to System Manager. 2. Go to Settings >> Services. 3. Verify that the "Enable" toggle is ON and "Running" is displayed. If "Enable" toggle is not ON or "Running" is not displayed, this is a finding. Step 2: Verify that Splunk Indexer is configured. 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Indexer. 3. Verify that there is an entry and the Status is "Connected". If there is no entry for Splunk Indexer or the Status is "Not Connected", this is a finding. Step 3: Verify "Audit Log" is enabled in the Splunk "data to index". 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Data to open the "Data to Index" window. 3. Verify "Audit Log" is included in the "Data To Index". If "Audit Log" is not included in the "Data To Index", this is a finding. Note: Syslog can be used instead of Splunk.

## Group: SRG-APP-000412-UEM-000283

**Group ID:** `V-251416`

### Rule: The Ivanti EPMM server must configure web management tools with FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to protect the confidentiality of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-251416r1004743_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Nonlocal maintenance and diagnostic activities are activities conducted by individuals communicating through either an external network (e.g., the internet) or an internal network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify MobileIron Core is in FIPS mode. ssh to command line console of the Core. Enable >> show fips. Verify FIPS mode is configured. If FIPS mode is not configured, this is a finding.

## Group: SRG-APP-000427-UEM-000298

**Group ID:** `V-251417`

### Rule: The Ivanti EPMM server must only allow the use of DoD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-251417r1004744_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA). Satisfies: FIA_X509_EXT.1.1(1)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the MDM server is configured with TLS server certificate chain to a DOD certificate Authority. Go into the Certificate Manager >> System Manager >> Security >> Certificate Management >> Portal HTTPS. Verify DoD certificates are installed. If DoD digital certificates are not installed on Core, this is a finding.

## Group: SRG-APP-000456-UEM-000330

**Group ID:** `V-251418`

### Rule: The Ivanti EPMM server must be maintained at a supported version.

**Rule ID:** `SV-251418r1004745_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The UEM vendor maintains specific product versions for a specific period of time. MDM/EMM server versions no longer supported by the vendor will not receive security updates for new vulnerabilities, which leaves them subject to exploitation. Satisfies: FPT_TUD_EXT.1.1, FPT_TUD_EXT.1.2 Reference: PP-MDM-414005</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Core server version is a supported version. This requirement is Not Applicable for the cloud version of Core. Find the list of currently supported on-prem versions of Core server here: https://help.ivanti.com/mi/help/en_us/EML/3.16.1/rni/Content/EmailPlusiOSReleaseNotes/Support_and_compatibilit.htm Log onto the Core console and determine the installed version of Core: 1. Click on the round person icon in the top right corner of the Core console. 2. In the drop-down menu, select "About". 3. View the version of Core that is installed. 4. Verify the version is a supported version. If the installed version of the Core server is not a supported version, this is a finding.

## Group: SRG-APP-000472-UEM-000347

**Group ID:** `V-251419`

### Rule: The Ivanti EPMM server must be configured with the periodicity of the following commands to the agent of six hours or less: - query connectivity status - query the current version of the managed device firmware/software - query the current version of installed mobile applications - read audit logs kept by the managed device. 

**Rule ID:** `SV-251419r1004746_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification, security functions may not operate correctly and this failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters. This requirement applies to applications performing security functions and the applications performing security function verification/testing. Satisfies: FAU_NET_EXT.1.1, FMT_SMF.1.1(2) c.3 Reference: PP-MDM-411057</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server configuration settings and verify the server is configured with a periodicity for reachable events of six hours or less for the following commands to the agent: - query connectivity status; - query the current version of the MD firmware/software; - query the current version of the hardware model of the device; - query the current version of installed mobile applications; - read audit logs kept by the MD. Verify the sync interval for a device: 1. In the Admin Portal, go to Policies & Config >> Policies. 2. Select the default sync policy. 3. Verify that the Sync Interval is set to 360 minutes or less. If the Sync interval is not set to 360 minutes or less, this is a finding.

## Group: SRG-APP-000514-UEM-000389

**Group ID:** `V-251420`

### Rule: The Ivanti EPMM server must use a FIPS-validated cryptographic module to generate cryptographic hashes.

**Rule ID:** `SV-251420r1004747_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-2 precludes the use of invalidated cryptography for the cryptographic protection of sensitive or valuable data within Federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2 standard. The cryptographic module used must have at least one validated hash algorithm. This validated hash algorithm must be used to generate cryptographic hashes for all cryptographic security function within the product being evaluated. Satisfies: FCS_COP.1.1(2)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MDM console, do the following: 1. SSH to MobileIron Core Server from any SSH client. 2. Enter the administrator credentials you set when you installed MobileIron Core. 3. Enter show fips. 4. Verify "FIPS 140 mode is enabled" is displayed. If the MobileIron Server Core does not report that FIPS mode is enabled, this is a finding.

## Group: SRG-APP-000515-UEM-000390

**Group ID:** `V-251421`

### Rule: The Ivanti EPMM server must, at a minimum, off-load audit logs of interconnected systems in real time and off-load standalone systems weekly.

**Rule ID:** `SV-251421r1004748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: FMT_SMF.1.1(2) c.8, FAU_STG_EXT.1.1(1) Reference: PP-MDM-411054</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Splunk is configured for automated log export. Step 1: Verify that the Splunk Forwarder is enabled. 1. Log in to System Manager. 2. Go to Settings >> Services. 3. Verify that the "Enable" toggle is ON and "Running" is displayed. If "Enable" toggle is not ON or "Running" is not displayed, this is a finding. Step 2: Verify that Splunk Indexer is configured. 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Indexer. 3. Verify that there is an entry and the Status is "Connected". If there is no entry for Splunk Indexer or the Status is "Not Connected", this is a finding. Step 3: Verify "Audit Log" is enabled in the Splunk "data to index". 1. Log in to System Manager. 2. Go to Settings >> Data Export >> Splunk Data to open the "Data to Index" window. 3. Verify "Audit Log" is included in the "Data To Index". If "Audit Log" is not included in the "Data To Index", this is a finding.

## Group: SRG-APP-000516-UEM-000391

**Group ID:** `V-251422`

### Rule: The Ivanti EPMM server must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-251422r1004749_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the MDM server documentation, Mobile Device Management Protection Profile Guide. If Core is not configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs, this is a finding.

## Group: SRG-APP-000555-UEM-000393

**Group ID:** `V-251423`

### Rule: The Ivanti EPMM server must be configured to implement FIPS 140-2 mode for all server and agent encryption.

**Rule ID:** `SV-251423r1004750_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. A block cipher mode is an algorithm that features the use of a symmetric key block cipher algorithm to provide an information service, such as confidentiality or authentication. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in DoD. For an algorithm implementation to be listed on a FIPS 140-2 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2 and must successfully complete the cryptographic algorithm validation process. Currently, NIST has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW. Satisfies: FCS_COP.1.1(1), FTP_TRP.1.1(1) Reference: PP-MDM-414001</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the MDM console, do the following: 1. SSH to MobileIron Core Server from any SSH client. 2. Enter the administrator credentials you set when you installed MobileIron Core. 3. Enter show fips. 4. Verify "FIPS 140 mode is enabled" is displayed. 5. If the MobileIron Server Core does not report that FIPS mode is enabled, this is a finding.

## Group: SRG-APP-000345-UEM-000218

**Group ID:** `V-251774`

### Rule: The Ivanti EPMM server must configured to lock administrator accounts after three unsuccessful login attempts.

**Rule ID:** `SV-251774r1004738_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Satisfies:FMT_SMF.1(2)b Reference:PP-MDM-431030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ivanti EPMM server has been configured to lock administrator accounts after three unsuccessful login attempts. Log in to the Core Admin Console >> Settings >> Security >> Password Policy. Verify "Number of Failed attempts" is set to "3". If the Ivanti EPMM server does not lock administrator accounts after three unsuccessful login attempts, this is a finding.

## Group: SRG-APP-000345-UEM-000218

**Group ID:** `V-251777`

### Rule: The Ivanti EPMM server must be configured to lock an administrator's account for at least 15 minutes after the account has been locked because the maximum number of unsuccessful login attempts has been exceeded.

**Rule ID:** `SV-251777r1004741_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. Satisfies:FMT_SMF.1(2)b Reference:PP-MDM-431030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Ivanti EPMM server has been configured to lock an administrator's account for at least 15 minutes after the account has been locked because the maximum number of unsuccessful login attempts has been exceeded. Log in to the Core Admin Console >> Settings >> Security >> Password Policy. Verify "Auto-Lock Time" is set to 15 minutes (900 seconds). If the Ivanti EPMM server does not lock an administrator's account for at least 15 minutes after the account has been locked because the maximum number of unsuccessful login attempts has been exceeded, this is a finding.

