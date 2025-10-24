# STIG Benchmark: Ivanti Connect Secure NDM Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-258598`

### Rule: The ICS must be configured to implement cryptographic mechanisms using a FIPS 140-2/140-3 approved algorithm.

**Rule ID:** `SV-258598r1028331_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions. When JITC mode is enabled, it also enables FIPS mode is also automatically enabled. However, this requirement focuses only on the use of FIPS validated encryption algorithms and protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Security >> Inbound SSL Options. Verify "Turn on FIPS mode" checkbox is enabled (checked). If the use of FIPS 140-2/140-3 approved algorithms is not enabled, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-258599`

### Rule: The ICS must be configured to send admin log data to a redundant central log server.

**Rule ID:** `SV-258599r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat. Satisfies: SRG-APP-000516-NDM-000350, SRG-APP-000360-NDM-000295, SRG-APP-000515-NDM-000325</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ICS is configured with address information so it sends admin log event records to a central log server. In the ICS Web UI, navigate to System >> Log/Monitoring >> Events >> Settings. Under "Syslog Servers", verify a server name/IP address, facility of LOCAL0, type TLS, and the management source interface are defined. In the ICS Web UI, navigate to System >> Log/Monitoring >> Admin Access >> Settings. Under "Syslog Servers", verify server names/IP addresses are added. Also ensure facility of LOCAL0, type TLS, and them management source interface are not defined. If the ICS is not configured to send log admin log events data to redundant central log servers, this is a finding.

## Group: SRG-APP-000340-NDM-000288

**Group ID:** `V-258600`

### Rule: The ICS must be configured to prevent nonprivileged users from executing privileged functions.

**Rule ID:** `SV-258600r997506_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing nonprivileged users from executing privileged functions mitigates the risk that unauthorized individuals or processes may gain unnecessary access to information or privileges. Privileged functions include, for example, establishing accounts, performing system integrity checks, or administering cryptographic key management activities. Nonprivileged users are individuals that do not possess appropriate authorizations. Satisfies: SRG-APP-000340-NDM-000288, SRG-APP-000380-NDM-000304, SRG-APP-000378-NDM-000302, SRG-APP-000133-NDM-000244, SRG-APP-000123-NDM-000240, SRG-APP-000121-NDM-000238, SRG-APP-000231-NDM-000271, SRG-APP-000408-NDM-000314, SRG-APP-000329-NDM-000287, SRG-APP-000153-NDM-000249, SRG-APP-000119-NDM-000236, SRG-APP-000120-NDM-000237, SRG-APP-000033-NDM-000212, SRG-APP-000516-NDM-000335, SRG-APP-000516-NDM-000336, SRG-APP-000177-NDM-000263, SRG-APP-000080-NDM-000220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Realms and Roles are configured as needed to meet mission requirements. In the ICS Web UI, navigate to Administrators >> Admin Realms >> Admin Realms. 1. Click the admin realm that is currently being used on the ICS for administrator logins. By default, it is "Admin Users". 2. In the "General" tab, under Servers >> Directory/Attribute, verify it does not say "none". 3. In the "Role Mapping" tab, under "when users meet these conditions", verify the following: - "Group" must be used, and the local site's administrator active directory group must be selected and assigned to the ".Administrators" role. Note that this role could be different if using something other than the default ".Administrators" role. - Verify separate usernames are not used. Verify an allow-all username of * is used. If a realm or role is not configured to prevent nonprivileged users from executing privileged functions, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-258601`

### Rule: The ICS must be configured to audit the execution of privileged functions such as accounts additions and changes.

**Rule ID:** `SV-258601r997507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-APP-000343-NDM-000289, SRG-APP-000495-NDM-000318, SRG-APP-000499-NDM-000319, SRG-APP-000503-NDM-000320, SRG-APP-000504-NDM-000321, SRG-APP-000505-NDM-000322, SRG-APP-000506-NDM-000323, SRG-APP-000319-NDM-000283, SRG-APP-000381-NDM-000305, SRG-APP-000100-NDM-000230, SRG-APP-000029-NDM-000211, SRG-APP-000028-NDM-000210, SRG-APP-000027-NDM-000209, SRG-APP-000038-NDM-000213, SRG-APP-000099-NDM-000229, SRG-APP-000098-NDM-000228, SRG-APP-000097-NDM-000227, SRG-APP-000096-NDM-000226, SRG-APP-000095-NDM-000225, SRG-APP-000026-NDM-000208, SRG-APP-000412-NDM-000331, SRG-APP-000411-NDM-000330, SRG-APP-000435-NDM-000315, SRG-APP-000156-NDM-000250, SRG-APP-000224-NDM-000270, SRG-APP-000179-NDM-000265, SRG-APP-000142-NDM-000245</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Log/Monitoring >> Admin Access >> Settings, under the section "Select Events to Log". If Administrator changes is enabled for events logging, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-258602`

### Rule: If SNMP is used, the ICS must be configured to use SNMPv3 with FIPS-140-2/3 validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-258602r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SNMP is not used, this is not applicable. In the ICS Web UI, navigate to System >> Log/Monitoring >> SNMP. Under "SNMP version data", verify v2c is not selected. If the ICS does not use properly configured SNMPv3, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-258603`

### Rule: The ICS must be configured to authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-258603r961506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Status >> Dashboard. 1. Click the "Overview" tab. 2. Under "Appliance Details" and "System Date and Time", select "Edit". 3. Verify the "Use Pool of NTP servers" is checked with NTP server IPs defined. 4. Verify the NTP server IP/hostname is defined with a key. If the ICS does not authenticate NTP sources using authentication that is cryptographically based, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-258604`

### Rule: The ICS must be configured to record time stamps for audit records that can be mapped to Greenwich Mean Time (GMT).

**Rule ID:** `SV-258604r961443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If time stamps are not consistently applied and there is no common time reference, it is difficult to perform forensic analysis. Time stamps generated by the application include date and time. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Status >> Dashboard. 1. Click the "Overview" tab. 2. Under "Appliance Details" and "System Date and Time", select "Edit". 3. Verify the "Time Zone" is set to "(GMT) Coordinated Universal Time". If the ICS must be configured to record time stamps for audit records that can be mapped to GMT, this is a finding.

## Group: SRG-APP-000357-NDM-000293

**Group ID:** `V-258605`

### Rule: The ICS must be configured to allocate local audit record storage capacity in accordance with organization-defined audit record storage requirements.

**Rule ID:** `SV-258605r961392_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to ensure network devices have a sufficient storage capacity in which to write the audit logs, they need to be able to allocate audit record storage capacity. The task of allocating audit record storage capacity is usually performed during initial device setup if it is modifiable. The value for the organization-defined audit record storage requirement will depend on the amount of storage available on the network device, the anticipated volume of logs, the frequency of transfer from the network device to centralized log servers, and other factors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Log Monitoring >> User Access >> Settings. Under the "Minimum Log Size", verify the Max Log Size is equal to or greater than the site's required limit as documented in the SSP (the default is 200 MB). If the ICS is not configured with a Max Log Size that is equal to or greater than the site's required limit, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-258606`

### Rule: The ICS must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-258606r997508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Verify the setting for "Password must have at least __ letters" is checked. 2. Verify the value for the setting for "Password must have at least __ special characters" is set to "1". If the ICS does not require that at least one special character be used for passwords, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-258607`

### Rule: The ICS must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-258607r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. Click the tab "Users" and verify that more than one user does not exist. If the ICS is not configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-258608`

### Rule: The ICS must be configured to terminate after 10 minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-258608r961068_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Upon the termination of a session, the Ivanti ICS inherently ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Administrators >> Admins Role >> Delegated Admin Roles. 1. Click the configured admin role being used for CAC/PKI token admin logins (by default it is .Administrators). 2. Click the Session Options tab. 3. In the "Session Lifetime" section, verify the Idle Timeout is set to "10". If the ICS does not terminate after 10 minutes of inactivity except to fulfill documented and validated mission requirements, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-258609`

### Rule: The ICS must be configured to use DOD PKI as multifactor authentication (MFA) for interactive logins.

**Rule ID:** `SV-258609r1007840_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MFA is when two or more factors are used to confirm the identity of an individual who is requesting access to digital information resources. Valid factors include something the individual knows (e.g., username and password), something the individual has (e.g., a smartcard or token), or something the individual is (e.g., a fingerprint or biometric). Legacy information system environments only use a single factor for authentication, typically a username and password combination. Although two pieces of data are used in a username and password combination, this is still considered single factor because an attacker can obtain access simply by learning what the user knows. Common attacks against single-factor authentication are attacks on user passwords. These attacks include brute force password guessing, password spraying, and password credential stuffing. MFA, along with strong user account hygiene, helps mitigate against the threat of having account passwords discovered by an attacker. Even in the event of a password compromise, with MFA implemented and required for interactive login, the attacker still needs to acquire something the user has or replicate a piece of user's biometric digital presence. Private industry recognizes and uses a wide variety of MFA solutions. However, DOD public key infrastructure (PKI) is the only prescribed method approved for DOD organizations to implement MFA. For authentication purposes, centralized DOD certificate authorities (CA) issue PKI certificate key pairs (public and private) to individuals using the prescribed x.509 format. The private certificates that have been generated by the issuing CA are downloaded and saved to smartcards which, within DOD, are referred to as common access cards (CAC) or personal identity verification (PIV) cards. This happens at designated DOD badge facilities. The CA maintains a record of the corresponding public keys for use with PKI-enabled environments. Privileged user smartcards, or "alternate tokens", function in the same manner, so this requirement applies to all interactive user sessions (authorized and privileged users). Note: This requirement is used in conjunction with the use of a centralized authentication server (e.g., AAA, RADIUS, LDAP), a separate but equally important requirement. The MFA configuration of this requirement provides identification and the first phase of authentication (the challenge and validated response, thereby confirming the PKI certificate that was presented by the user). The centralized authentication server will provide the second phase of authentication (the digital presence of the PKI ID as a valid user in the requested security domain) and authorization. The centralized authentication server will map validated PKI identities to valid user accounts and determine access levels for authenticated users based on security group membership and role. In cases where the centralized authentication server is not utilized by the network device for user authorization, the network device must map the authenticated identity to the user account for PKI-based authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Administrators >> Admin Realms >> Admin Realms. 1. Click the admin realm that is currently being used on the ICS for administrator logins; by default it is "Admin Users". 2. In the general tab, under Servers >> Authentication, verify that a certificate authenticate server is configured. 3. In the general tab, under Servers >> Directory/Attribute, verify it does not show "none". 4. In the role mapping tab, under "when users meet these conditions", verify the following is configured: - "Group" must be used, and the local site's administrator active directory group must be selected and assigned to the ".Administrators" role. Note: this role could be different if using something other than the default ".Administrators" role. - Use of groups instead of individual user accounts. - Ensure the allow-all username of * is not used. If the ICS must be configured to use DOD PKI as MFA for interactive logins, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-258610`

### Rule: The ICS must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-258610r997509_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Status >> Overview. Under "Appliance Details", and "System Date and Time", click "Edit". If the Time Source is not set to at least two NTP time sources, this is a finding. If the Time Sources are not specific to a DOD authoritative time source, this is a finding. If the Time Sources are not configured to use a SHA1 preshared key for authentication, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-258611`

### Rule: The ICS must be configured to obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-258611r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved and shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Certificates >> Device Certificates. 1. Verify there is a device certificate that is signed by a valid DOD CA. 2. Verify the certificate is used by all interfaces on the ICS. If the ICS does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-258612`

### Rule: The ICS must be configured to support organizational requirements to conduct weekly backups of information system documentation, including security-related documentation.

**Rule ID:** `SV-258612r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Maintenance >> Archiving >> Archive Servers. 1. Under "Archive Settings" verify an archive server is configured. 2. Under "Archive Schedule" verify "Archive System Configuration", and "Archive User Accounts" are selected. 3. Under "Archive Schedule" verify "Archive System Configuration", and "Archive User Accounts" are configured at a specific time and day of the week. 4. Under "Archive Schedule", if "Archive System Configuration", and "Archive User Accounts" are configured with a password for backup encryption. If the ICS does not support organizational requirements to conduct backups of information system documentation, including security-related documentation weekly, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-258613`

### Rule: The ICS must be configured to run an operating system release that is currently supported by Ivanti.

**Rule ID:** `SV-258613r961863_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Navigate to the ICS support site https://my.pulsesecure.net/. 1. Login using the valid support login. 2. Click the link for "Software Licensing and Download". 3. Click "License and System Download". 4. Click "Software Download". 5. Under "Product Lines", click "Pulse Connect Secure" and again, "Pulse Connect Secure". 6. Click the "End of Support" tab. 7. Now using the ICS Web UI, navigate to Maintenance >> System >> Platform. If the version running under Current Version is on the list of End of Support images on the Ivanti support site, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-258614`

### Rule: The ICS must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-258614r997510_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. If the minimum length is not 15 characters, this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-258615`

### Rule: The ICS must be configured to transmit only encrypted representations of passwords.

**Rule ID:** `SV-258615r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. This is applicable to the account of last resort which uses a password. Secure password while in transit for admin access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Inbound SSL Options. Under "Allowed SSL and TLS Version", if "Accept only TLS 1.2 (maximize security)" is checked. Navigate to System >> Configuration >> Outbound SSL Options. Under "Allowed SSL and TLS Version", if "Accept only TLS 1.2 (maximize security)" is checked. If the ICS does not transmit only encrypted representations of passwords, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-258616`

### Rule: The ICS must be configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-258616r1028335_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Verify the setting for "new password must differ from the previous password position" is checked. 2. Verify the value for the setting for "new password must differ from the previous password position" is set to "8". If the ICS is not configured to require that when a password is changed, the characters are changed in at least eight of the positions within the password, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-258617`

### Rule: The ICS must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-258617r997512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Verify the setting for "Password must have at least __ digits" is checked. 2. Verify the value for the setting for "Password must have at least __ digits" is not set to "1". If the ICS is not configured to enforce password complexity by requiring that at least one numeric character be used, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-258618`

### Rule: The ICS must be configured to enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-258618r997513_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Verify the setting for "Password must have at least __ letters" is checked. 2. Verify the setting for "Password must have mix of UPPERCASE and lowercase letters" is checked. 3. Verify the value for the setting for "Password must have at least __ letters" is set to "2". If the ICS is not configured to enforce password complexity by requiring that at least one lowercase character be used, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-258619`

### Rule: The ICS must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-258619r997514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Verify the setting for "Password must have at least __ letters" is checked. 2. Verify the setting for "Password must have mix of UPPERCASE and lowercase letters" is checked. 3. Verify value for the setting for "Password must have at least __ letters" is set to "2". If the ICS is not configured to enforce password complexity by requiring that at least one upper-case character be used, this is a finding.

## Group: SRG-APP-000175-NDM-000262

**Group ID:** `V-258620`

### Rule: The ICS must be configured to use DOD approved OCSP responders or CRLs to validate certificates used for PKI-based authentication.

**Rule ID:** `SV-258620r997515_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once issued by a DOD certificate authority (CA), public key infrastructure (PKI) certificates are typically valid for three years or shorter within the DOD. However, there are many reasons a certificate may become invalid before the prescribed expiration date. For example, an employee may leave or be terminated and still possess the smartcard on which the PKI certificates were stored. Another example is that a smartcard containing PKI certificates may become lost or stolen. A more serious issue could be that the CA or server which issued the PKI certificates has become compromised, thereby jeopardizing every certificate keypair that was issued by the CA. These examples of revocation use cases and many more can be researched further using internet cybersecurity resources. PKI user certificates presented as part of the identification and authentication criteria (e.g., DOD PKI as multifactor authentication [MFA]) must be checked for validity by network devices. For example, valid PKI certificates are digitally signed by a trusted DOD CA. Additionally, valid PKI certificates are not expired, and valid certificates have not been revoked by a DOD CA. Network devices can verify the validity of PKI certificates by checking with an authoritative CA. One method of checking the status of PKI certificates is to query databases referred to as certificate revocation lists (CRL). These are lists which are published, updated, and maintained by authoritative DOD CAs. For example, once certificates are expired or revoked, issuing CAs place the certificates on a certificate revocation list (CRL). Organizations can download these lists periodically (i.e. daily or weekly) and store them locally on the devices themselves or even onto another nearby local enclave resource. Storing them locally ensures revocation status can be checked even if internet connectivity is severed at the enclave's point of presence (PoP). However, CRLs can be rather large in storage size and further, the use of CRLs can be rather taxing on some computing resources. Another method of validating certificate status is to use the online certificate status protocol (OCSP). Using OCSP, a requestor (i.e. the network device which the user is trying to authenticate to) sends a request to an authoritative CA challenging the validity of a certificate that has been presented for identification and authentication. The CA receives the request and sends a digitally signed response indicating the status of the user's certificate as valid, revoked, or unknown. Network devices should only allow access for responses that indicate the certificates presented by the user were considered valid by an approved DOD CA. OCSP is the preferred method because it is fast, provides the most current status, and is lightweight.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Certificates >> Trusted Client CAs. 1. Click the first DOD client CA. 2. Verify the item "Use OCSP with CRL fallback" is selected under the "Client certificate status checking" setting. 3. Check each other client certificate CA. Verify the setting "Use OCSP with CRL fallback" is selected. If the ICS is not configured to use DOD approved OCSP responders or CRLs to validate certificates used for PKI-based authentication, this is a finding.

## Group: SRG-APP-000091-NDM-000223

**Group ID:** `V-258621`

### Rule: The ICS must be configured to generate audit records when successful/unsuccessful attempts to access privileges occur.

**Rule ID:** `SV-258621r960885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating audit records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the information system (e.g., module or policy filter).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Log/Monitoring >> Admin Access >> Settings. 1. Under the section "Select Events to Log", verify "Administrator Logins" is checked. If the ICS is not configured to generate audit records when successful/unsuccessful attempts to access privileges occur, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-258622`

### Rule: The ICS must be configured to limit the number of concurrent sessions to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-258622r960735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Administrators >> Admins Realms >> Admin Realms. 1. Click the configured admin realm being used for CAC/PKI token admin logins. 2. Click the "Authentication Policy" tab. 3. Click "Limits". If there is any number other than 1 in "Maximum number of sessions per user", this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-258623`

### Rule: The ICS must be configured to display the Standard Mandatory DOD Notice and Consent Banner before granting access to manage the device.

**Rule ID:** `SV-258623r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users. The banner is retained until acknowledgement by default when the banner is selected in the sign-in policy. Satisfies: SRG-APP-000068-NDM-000215, SRG-APP-000069-NDM-000216</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to present a DOD-approved banner that is formatted in accordance with DTM-08-060. In the ICS Web UI, navigate to Authentication >> Signing In >> Sign-In Policies/ 1. Click the */admin/ (or whatever custom URL is used for CAC/PKI token admin access). 2. Verify the DOD banner is entered exactly as required with no alterations. "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests -- not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details". If the banner is not used, displayed, or the text/format is altered, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-258624`

### Rule: The ICS must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-258624r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Authentication >> Auth Servers >> Administrators. 1. Under the section "Account Lockout", verify "Enable Account Lockout for users" is checked. 2. Under the section "Account Lockout", verify "Maximum wrong password attempts" is set to "3". 3. Under the section "Account Lockout", verify "Account Lockout Period in Minutes" is set to "15". If the ICS must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-258625`

### Rule: The ICS must be configured to conduct backups of system level information contained in the information system when changes occur.

**Rule ID:** `SV-258625r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including ACLs that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial of service condition is possible for all who utilize this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Maintenance >> Archiving >> Archive Servers. Under "Archive Settings", if there is no archive server configured, this is a finding. Under "Archive Schedule", if "Archive System Configuration", and "Archive User Accounts" are not selected, this is a finding. Under "Archive Schedule", if "Archive System Configuration", and "Archive User Accounts" are not configured at a specific time and day of the week, this is a finding. Under "Archive Schedule", if "Archive System Configuration", and "Archive User Accounts" are not configured with a password for backup encryption, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-268324`

### Rule: The ICS must be configured to protect against known types of denial-of-service (DoS) attacks by enabling JITC mode.

**Rule ID:** `SV-268324r1028339_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This configuration protects the confidentiality of Web UI session and guards against DoS attacks. If JITC (DODIN APL) Mode is enabled, then the following protections are enforced: - Log support for detection and prevention of SMURF/SYN Flood/SSL Replay Attack. - Disable ICMPv6 echo response for multicast echo request. - Disable ICMPv6 destination unreachable response. - Password Strengthening. - Notification for unsuccessful admin login attempts. - Re-authentication of admin users. - Notification on admin status change. When JITC and FIPS mode is enabled, it enables DoS attacks such as flooding and replay attack audit logs inherently. JITC and FIPS mode are required for ICS use in DOD. When NDcPP option is enabled, only NDcPP allowed crypto algorithms are allowed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Security >> Inbound SSL Options. 1. Verify "Turn on JITC mode" checkbox is enabled (checked). 2. Verify "Turn on NDcPP mode" checkbox is enabled (checked). If JITC mode is not enabled, this is a finding.

