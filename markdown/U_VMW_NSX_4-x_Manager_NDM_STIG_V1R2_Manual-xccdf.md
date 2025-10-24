# STIG Benchmark: VMware NSX 4.x Manager NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000027-NDM-000209

**Group ID:** `V-265289`

### Rule: The NSX Manager must configure logging levels for services to ensure audit records are generated.

**Rule ID:** `SV-265289r994090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., module or policy filter). Satisfies: SRG-APP-000027-NDM-000209, SRG-APP-000495-NDM-000318, SRG-APP-000499-NDM-000319, SRG-APP-000503-NDM-000320, SRG-APP-000504-NDM-000321, SRG-APP-000505-NDM-000322, SRG-APP-000506-NDM-000323, SRG-APP-000516-NDM-000334</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following commands: > get service async_replicator | find Logging > get service auth | find Logging > get service http | find Logging > get service manager | find Logging > get service telemetry | find Logging Expected result: Logging level: info If any service listed does not have logging level configured to "info", this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-265292`

### Rule: The NSX Manager must assign users/accounts to organization-defined roles configured with approved authorizations.

**Rule ID:** `SV-265292r994099_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. Users must be assigned to roles which are configured with approved authorizations and access permissions. The NSX Manager must be configured granularly based on organization requirements to only allow authorized administrators to execute privileged functions. Role assignments should control which administrators can view or change the device configuration, system files, and locally stored audit information. Satisfies: SRG-APP-000033-NDM-000212, SRG-APP-000038-NDM-000213, SRG-APP-000119-NDM-000236, SRG-APP-000120-NDM-000237, SRG-APP-000133-NDM-000244, SRG-APP-000231-NDM-000271, SRG-APP-000329-NDM-000287, SRG-APP-000340-NDM-000288, SRG-APP-000378-NDM-000302, SRG-APP-000380-NDM-000304, SRG-APP-000408-NDM-000314, SRG-APP-000516-NDM-000335</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Settings >> User Management >> User Role Assignment. View each user and group and verify the role assigned has authorization limits as appropriate to the role and in accordance with the site's documentation. If any user/group or service account are assigned to roles with privileges that are beyond those required and authorized by the organization, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-265293`

### Rule: The NSX Manager must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-265293r994102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following commands: > get auth-policy api lockout-reset-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy api lockout-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy api max-auth-failures Expected result: 3 If the output does not match the expected result, this is a finding. > get auth-policy cli lockout-period Expected result: 900 seconds If the output does not match the expected result, this is a finding. > get auth-policy cli max-auth-failures Expected result: 3 If the output does not match the expected result, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-265294`

### Rule: The NSX Manager must display the Standard Mandatory DOD Notice and Consent Banner before granting access.

**Rule ID:** `SV-265294r994105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to present a DOD-approved banner that is formatted in accordance with DTM-08-060. From the NSX Manager web interface, go to System >> Settings >> General Settings >> User Interface. Review the Login Consent Settings. If the "Consent Message Description" does not contain the Standard Mandatory DOD Notice and Consent Banner verbiage, this is a finding. The Standard Mandatory DOD Notice and Consent Banner verbiage is as follows: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-265295`

### Rule: The NSX Manager must retain the Standard Mandatory DOD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-265295r994108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to the device allowing the administrator access to the network device. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DOD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of CLI access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, then entering the password is also acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Settings >> General Settings >> User Interface. Review the Login Consent Settings. Verify "Login Consent" is not On. Verify "Require Explicit User Consent" is set to Yes. If the Standard Mandatory DOD Notice and Consent Banner is not retained on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access, this is a finding.

## Group: SRG-APP-000080-NDM-000220

**Group ID:** `V-265296`

### Rule: The NSX Manager must be configured to integrate with an identity provider that supports multifactor authentication (MFA).

**Rule ID:** `SV-265296r994111_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Common attacks against single-factor authentication are attacks on user passwords. These attacks include brute force password guessing, password spraying, and password credential stuffing. This requirement also supports nonrepudiation of actions taken by an administrator. This requirement ensures the NSX Manager is configured to use a centralized authentication services to authenticate users prior to granting administrative access. As of NSX 4.1 and vCenter 8.0 Update 2, NSX Manager administrator access can also be configured by connecting VMware NSX to the Workspace ONE Access Broker in VMware vCenter for federated identity. Refer to the NSX product documentation to configure this access option. Satisfies: SRG-APP-000080-NDM-000220, SRG-APP-000149-NDM-000247, SRG-APP-000516-NDM-000336</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Settings >> Users Management >> Authentication Providers. Verify that the "VMware Identity Manager" and "OpenID Connect" tabs are configured. If NSX is not configured to integrate with an identity provider that supports MFA, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-265313`

### Rule: The NSX Manager must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-265313r1051115_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to the System >> Settings >> User Management >> Local Users and view the status column. If any local account other than the account of last resort are active, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-265315`

### Rule: The NSX Manager must only enable TLS 1.2 or greater.

**Rule ID:** `SV-265315r994168_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. Configuration of TLS on the NSX also ensures that passwords are not transmitted in the clear. TLS 1.0 and 1.1 are deprecated protocols with well-published shortcomings and vulnerabilities. TLS 1.2 or greater must be enabled on all interfaces and TLS 1.1 and 1.0 disabled where supported. Satisfies: SRG-APP-000156-NDM-000250, SRG-APP-000172-NDM-000259</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Viewing TLS protocol enablement must be done via the API. Execute the following API call using curl or another REST API client: GET https://<nsx-mgr>/api/v1/cluster/api-service Example result: "protocol_versions": [ { "name": "TLSv1.1", "enabled": false }, { "name": "TLSv1.2", "enabled": true }, { "name": "TLSv1.3", "enabled": true } ] If TLS 1.1 is enabled, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-265316`

### Rule: The NSX Manager must enforce a minimum 15-character password length for local accounts.

**Rule ID:** `SV-265316r994171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the minimum password length is not 15 or greater, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-265317`

### Rule: The NSX Manager must enforce password complexity by requiring that at least one uppercase character be used for local accounts.

**Rule ID:** `SV-265317r994174_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the minimum uppercase characters is not 1 or more, this is a finding. Note: If a maximum number of uppercase characters has been configured a minimum will not be shown.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-265318`

### Rule: The NSX Manager must enforce password complexity by requiring that at least one lowercase character be used for local accounts.

**Rule ID:** `SV-265318r994177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the minimum lowercase characters is not 1 or more, this is a finding. Note: If a maximum number of lowercase characters has been configured, a minimum will not be shown.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-265319`

### Rule: The NSX Manager must enforce password complexity by requiring that at least one numeric character be used for local accounts.

**Rule ID:** `SV-265319r994180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the minimum numeric characters is not 1 or more, this is a finding. Note: If a maximum number of numeric characters has been configured, a minimum will not be shown.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-265320`

### Rule: The NSX Manager must enforce password complexity by requiring that at least one special character be used for local accounts.

**Rule ID:** `SV-265320r994183_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the minimum special characters is not 1 or more, this is a finding. Note: If a maximum number of special characters has been configured, a minimum will not be shown.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-265321`

### Rule: The NSX Manager must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-265321r1043189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get password-complexity If the number of consecutive characters allowed for reuse is not eight or more, this is a finding. Note: If this has not previously been configured it will not be shown in the output.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-265327`

### Rule: The NSX Manager must terminate all network connections associated with a session after five minutes of inactivity.

**Rule ID:** `SV-265327r994204_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take immediate control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-APP-000190-NDM-000267, SRG-APP-000186-NDM-000266, SRG-APP-000400-NDM-000313</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get service http | find Session Expected result: Session timeout: 300 If the session timeout is not configured to 300 or less, this is a finding. From an NSX Manager shell, run the following command: > get cli-timeout Expected result: 300 seconds If the CLI timeout is not configured to 300 or less, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-265338`

### Rule: The NSX Manager must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-265338r994237_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Configuration >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and verify the NTP servers listed. or From an NSX Manager shell, run the following command: > get ntp-server If the output does not contain at least two authoritative time sources, this is a finding. If the output contains unknown or nonauthoritative time sources, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-265339`

### Rule: The NSX Manager must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC).

**Rule ID:** `SV-265339r994240_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Configuration >> Fabric >> Profiles >> Node Profiles. Note: This check must be run from each NSX Manager as they are configured individually if done from the command line. Click "All NSX Nodes" and verify the time zone. or From an NSX Manager shell, run the following command: > get clock If system clock is not configured with the UTC time zone, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-265346`

### Rule: The NSX Manager must be configured to protect against denial-of-service (DoS) attacks by limit the number of concurrent sessions to an organization-defined number.

**Rule ID:** `SV-265346r994261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. Limiting the number of concurrent open sessions helps limit the risk of DoS attacks. Organizations may define the maximum number of concurrent sessions for system accounts globally or by connection type. By default, the NSX Manager has a protection mechanism in place to prevent the API from being overloaded. This setting also addresses concurrent sessions for integrations into NSX API to monitor or configure NSX. Satisfies: SRG-APP-000435-NDM-000315, SRG-APP-000001-NDM-000200</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get service http | find limit Expected result: Client API concurrency limit: 40 connections Global API concurrency limit: 199 connections If the NSX does not limit the number of concurrent sessions to an organization-defined number, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-265348`

### Rule: The NSX Manager must be configured to send logs to a central log server.

**Rule ID:** `SV-265348r994267_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000515-NDM-000325, SRG-APP-000357-NDM-000293, SRG-APP-000516-NDM-000350</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and verify the Syslog servers listed. or From an NSX Manager shell, run the following command: > get logging-servers Note: This command must be run from each NSX Manager as they are configured individually. If no logging severs are configured or unauthorized logging servers are configured, this is a finding. If the log level is not set to INFO, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-265349`

### Rule: The NSX Manager must not provide environment information to third parties.

**Rule ID:** `SV-265349r994270_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Providing technical details about an environment's infrastructure to third parties could unknowingly expose sensitive information to bad actors if intercepted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Settings >> General Settings >> Customer Program >> Customer Experience Improvement Program. If Joined is set to "Yes", this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-265350`

### Rule: The NSX Manager must be configured to conduct backups on an organizationally defined schedule.

**Rule ID:** `SV-265350r994273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups. Satisfies: SRG-APP-000516-NDM-000341, SRG-APP-000516-NDM-000340</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Lifecycle Management >> Backup and Restore to view the backup configuration. If backup is not configured and scheduled on a recurring frequency, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-265351`

### Rule: The NSX Manager must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-265351r994276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by Office of Management and Budget (OMB) policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NSX Manager uses a certificate for each manager and one for the cluster VIP. In some cases these are the same, but each node and cluster VIP certificate must be checked individually. Browse to the NSX Manager web interface for each node and cluster VIP and view the certificate and its issuer of the website. or From an NSX Manager shell, run the following commands: > get certificate api > get certificate cluster Save the output to a .cer file to examine. If the certificate the NSX Manager web interface or cluster is using is not issued by an approved certificate authority and is not currently valid, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-265352`

### Rule: The NSX Manager must be running a release that is currently supported by the vendor.

**Rule ID:** `SV-265352r994279_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to the System >> Lifecycle Management >> Upgrade. If the NSX Manager current version is not the latest approved for use in DOD and supported by the vendor, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-265353`

### Rule: The NSX Manager must disable SSH.

**Rule ID:** `SV-265353r994282_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The NSX shell provides temporary access to commands essential for server maintenance. Intended primarily for use in break-fix scenarios, the NSX shell is well suited for checking and modifying configuration details, not always generally accessible, using the web interface. The NSX shell is accessible remotely using SSH. Under normal operating conditions, SSH access to the managers must be disabled as is the default. As with the NSX shell, SSH is also intended only for temporary use during break-fix scenarios. SSH must therefore be disabled under normal operating conditions and must only be enabled for diagnostics or troubleshooting. Remote access to the managers must therefore be limited to the web interface and API at all other times.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Manager shell, run the following command: > get service ssh Expected results: Service name: ssh Service state: stopped Start on boot: False If the SSH server is not stopped or starts on boot, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-265354`

### Rule: The NSX Manager must disable SNMP v2.

**Rule ID:** `SV-265354r994285_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SNMPv3 supports commercial-grade security, including authentication, authorization, access control, and privacy. Previous versions of the protocol contained well-known security weaknesses that were easily exploited. As such, SNMPv1/2 receivers must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to the System >> Configuration >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and view the SNMP Polling and Traps configuration. If SNMP v2c Polling or Traps are configured, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-265355`

### Rule: The NSX Manager must enable the global FIPS compliance mode for load balancers.

**Rule ID:** `SV-265355r994288_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for load balancing, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data at risk of compromise.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to the Home >> Monitoring Dashboards >> Compliance Report. Review the compliance report for code 72024 with description load balancer FIPS global setting disabled. Note: This may also be checked via the API call GET https://<nsx-mgr>/policy/api/v1/infra/global-config If the global FIPS setting is disabled for load balancers, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-265358`

### Rule: The NSX Manager must be configured as a cluster.

**Rule ID:** `SV-265358r994297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a known state can address safety or security in accordance with the mission needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the SDN controller. Preserving network element state information helps to facilitate continuous network operations minimal or no disruption to mission-essential workload processes and flows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to System >> Configuration >> Appliances. Verify three NSX Managers are deployed, a VIP or external load balancer is configured, and the cluster is in a healthy state. If three NSX Managers are not deployed, a VIP or external load balancer is not configured, and the cluster is not in a healthy state, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-265359`

### Rule: The NSX Managers must be deployed on separate physical hosts.

**Rule ID:** `SV-265359r994300_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SDN relies heavily on control messages between a controller and the forwarding devices for network convergence. The controller uses node and link state discovery information to calculate and determine optimum pathing within the SDN network infrastructure based on application, business, and security policies. Operating in the proactive flow instantiation mode, the SDN controller populates forwarding tables to the SDN-aware forwarding devices. At times, the SDN controller must function in reactive flow instantiation mode; that is, when a forwarding device receives a packet for a flow not found in its forwarding table, it must send it to the controller to receive forwarding instructions. With total dependence on the SDN controller for determining forwarding decisions and path optimization within the SDN infrastructure for both proactive and reactive flow modes of operation, having a single point of failure is not acceptable. A controller failure with no failover backup leaves the network in an unmanaged state. Hence, it is imperative that the SDN controllers are deployed as clusters on separate physical hosts to guarantee high network availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be performed in vCenter. From the vSphere Client, go to Administration >> Hosts and Clusters >> Select the cluster where the NSX Managers are deployed >> Configure >> Configuration >> VM/Host Rules. If the NSX Manager cluster does not have rules applied to it that separate the nodes onto different physical hosts, this is a finding.

