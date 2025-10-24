# STIG Benchmark: HPE Aruba Networking AOS NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-266903`

### Rule: AOS must limit the number of concurrent sessions to a maximum of three for each administrator account and/or administrator account type.

**Rule ID:** `SV-266903r1039730_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system. At a minimum, limits must be set for Secure Shell (SSH), Hypertext Transfer Protocol Secure (HTTPS), and account of last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show mgmt-user admin If "Max-concurrent-sessions" is not set to "3", this is a finding.

## Group: SRG-APP-000026-NDM-000208

**Group ID:** `V-266908`

### Rule: AOS must automatically audit account creation.

**Rule ID:** `SV-266908r1039745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Upon gaining access to a network device, an attacker will often first attempt to create a persistent method of reestablishing access. One way to accomplish this is to create a new account. Notification of account creation helps to mitigate this risk. Auditing account creation provides the necessary reconciliation that account management procedures are being followed. Without this audit trail, personnel without the proper authorization may gain access to critical network nodes. Satisfies: SRG-APP-000026-NDM-000208, SRG-APP-000027-NDM-000209, SRG-APP-000028-NDM-000210, SRG-APP-000029-NDM-000211, SRG-APP-000091-NDM-000223, SRG-APP-000319-NDM-000283, SRG-APP-000381-NDM-000305, SRG-APP-000495-NDM-000318, SRG-APP-000503-NDM-000320, SRG-APP-000505-NDM-000322</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show logging level If the security logging level is not set to debug, this is a finding.

## Group: SRG-APP-000033-NDM-000212

**Group ID:** `V-266909`

### Rule: AOS must be configured to assign appropriate user roles or access levels to authenticated users.

**Rule ID:** `SV-266909r1039960_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Successful identification and authentication must not automatically give an entity full access to a network device or security domain. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DOD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset or set of resources. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Some network devices are preconfigured with security groups. Other network devices enable operators to create custom security groups with custom permissions. For example, an information system security manager (ISSM) may require read-only access to audit the network device. Operators may create an audit security group, define permissions and access levels for members of the group, and then assign the ISSM's user persona to the audit security group. This is still considered privileged access, but the ISSM's security group is more restrictive than the network administrator's security group. Network devices that rely on authentication, authorization, and accounting (AAA) brokers for authentication and authorization services may need to identify the available security groups or access levels available on the network devices and convey that information to the AAA operator. Once the AAA broker identifies the user persona on the centralized directory service, the user's security group memberships can be retrieved. The AAA operator may need to create a mapping that links target security groups from the directory service to the appropriate security groups or access levels on the network device. Once these mappings are configured, authorizations can happen dynamically based on each user's directory service group membership.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: Navigate to Configuration >> System >> Admin tab and expand the "Admin Authentication Options". If root is not the Default role, "Enable" is not checked, or the Server group is not configured to the enterprise server group for admin authorization, this is a finding.

## Group: SRG-APP-000097-NDM-000227

**Group ID:** `V-266910`

### Rule: AOS must enforce approved authorizations for controlling the flow of management information within the network device based on information flow control policies.

**Rule ID:** `SV-266910r1039751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy. Satisfies: SRG-APP-000097-NDM-000227, SRG-APP-000038-NDM-000213</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show running-config | begin "interface gigabit" Note the configured IP access-group session Access Control List (ACL) for each active interface. For each configured ACL: show ip access-list <ACL name> If each ACL does not end in an "any any deny log" for both IPv4 and IPv6, this is a finding.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-266911`

### Rule: AOS must be configured to enforce the limit of three consecutive invalid login attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-266911r1039754_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify the AOS configuration with the following command: show aaa password-policy mgmt 2. Verify that "Maximum Number of failed attempts in 3 minute window to lockout password based user" is set to "3 attempts" and "Time duration to lockout the password based user upon crossing the 'lock-out' threshold" is set to "15 minutes". If one or both of these settings are set to any other value, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-266912`

### Rule: AOS must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the device.

**Rule ID:** `SV-266912r1039757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show banner If the Standard Mandatory DOD Notice and Consent Banner is not set, this is a finding.

## Group: SRG-APP-000069-NDM-000216

**Group ID:** `V-266913`

### Rule: AOS must retain the Standard Mandatory DOD Notice and Consent Banner on the screen until the administrator acknowledges the usage conditions and takes explicit actions to log on for further access.

**Rule ID:** `SV-266913r1039760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The banner must be acknowledged by the administrator prior to the device allowing the administrator access to the network device. This provides assurance that the administrator has seen the message and accepted the conditions for access. If the consent banner is not acknowledged by the administrator, DOD will not be in compliance with system use notifications required by law. To establish acceptance of the network administration policy, a click-through banner at management session logon is required. The device must prevent further activity until the administrator executes a positive action to manifest agreement. In the case of command line interface (CLI) access using a terminal client, entering the username and password when the banner is presented is considered an explicit action of acknowledgement. Entering the username, viewing the banner, and then entering the password is also acceptable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show running-config | include "banner enforce-accept" If "banner enforce-accept" is not set, this is a finding.

## Group: SRG-APP-000142-NDM-000245

**Group ID:** `V-266928`

### Rule: AOS must be configured to prohibit the use of all unnecessary and/or nonsecure functions, ports, protocols, and/or services.

**Rule ID:** `SV-266928r1039805_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable unused or unnecessary physical and logical ports/protocols on information systems. Network devices are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the network device must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved. Some network devices have capabilities enabled by default; if these capabilities are not necessary, they must be disabled. If a particular capability is used, it must be documented and approved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show firewall-cp show running-config | include ospf Verify that OSPF is not enabled and only unnecessary and/or nonsecure functions, ports, protocols, and/or services are denied. If OSPF is enabled or any unnecessary and/or nonsecure functions, ports, protocols, and/or services are allowed, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-266929`

### Rule: AOS must be configured to use DOD public key infrastructure (PKI) as multifactor authentication (MFA) for interactive logins.

**Rule ID:** `SV-266929r1039808_rule`
**Severity:** high

**Description:**
<VulnDiscussion>MFA is when two or more factors are used to confirm the identity of an individual who is requesting access to digital information resources. Valid factors include something the individual knows (e.g., username and password), something the individual has (e.g., a smart card or token), or something the individual is (e.g., a fingerprint or biometric). Legacy information system environments only use a single factor for authentication, typically a username and password combination. Although two pieces of data are used in a username and password combination, this is still considered single factor because an attacker can obtain access by learning what the user knows. Common attacks against single-factor authentication are attacks on user passwords. These attacks include brute force password guessing, password spraying, and password credential stuffing. MFA, along with strong user account hygiene, helps mitigate the threat of having account passwords discovered by an attacker. Even in the event of a password compromise, with MFA implemented and required for interactive login, the attacker still needs to acquire something the user has or replicate a piece of the user's biometric digital presence. Private industry recognizes and uses a wide variety of MFA solutions. However, DOD PKI is the only prescribed method approved for DOD organizations to implement MFA. For authentication purposes, centralized DOD certificate authorities (CA) issue PKI certificate key pairs (public and private) to individuals using the prescribed x.509 format. The private certificates that have been generated by the issuing CA are downloaded and saved to smart cards which, within DOD, are referred to as common access cards (CAC) or personal identity verification (PIV) cards. This happens at designated DOD badge facilities. The CA maintains a record of the corresponding public keys for use with PKI-enabled environments. Privileged user smart cards, or "alternate tokens", function in the same manner, so this requirement applies to all interactive user sessions (authorized and privileged users). Note: This requirement is used in conjunction with a centralized authentication server (e.g., Authentication, Authorization, and Accounting [AAA], Remote Authentication Dial-In User Service [RADIUS], Lightweight Directory Access Protocol [LDAP]), a separate but equally important requirement. The MFA configuration of this requirement provides identification and the first phase of authentication (the challenge and validated response, thereby confirming the PKI certificate that was presented by the user). The centralized authentication server will provide the second phase of authentication (the digital presence of the PKI ID as a valid user in the requested security domain) and authorization. The centralized authentication server will map validated PKI identities to valid user accounts and determine access levels for authenticated users based on security group membership and role. In cases where the centralized authentication server is not used by the network device for user authorization, the network device must map the authenticated identity to the user account for PKI-based authentication. Satisfies: SRG-APP-000149-NDM-000247, SRG-APP-000080-NDM-000220, SRG-APP-000153-NDM-000249, SRG-APP-000177-NDM-000263</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> System >> Admin and expand "Admin Authentication Options". 2. Verify what "Server group" is handling admin authentication. 3. Verify that Client certificate is enabled. 4. Expand "Admin Authentication Servers". 5. Select the Server Group identified from the "Options" section. 6. Verify that each authentication server configured in Server Group <server group name> is configured with the Key attribute: of userPrincipalName. If Client certificate is not enabled and the management authentication servers are not configured with userPrincipalName, this is a finding.

## Group: SRG-APP-000156-NDM-000250

**Group ID:** `V-266930`

### Rule: AOS must implement replay-resistant authentication mechanisms for network access to privileged accounts.

**Rule ID:** `SV-266930r1039811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Techniques to address this include protocols using nonces (e.g., numbers generated for a specific one-time use) or challenges (e.g., Transport Layer Security [TLS], Web Services Security [WS_Security]). Additional techniques include time-synchronous or challenge-response one-time authenticators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> System >> Admin and expand "Admin Authentication Options". 2. Verify what "Server group" is handling admin authentication. 3. Expand "Admin Authentication Servers". 4. Select the Server Group identified from the "Options" section. 5. Verify that each authentication server configured in Server Group <server group name> is configured with secure LDAP using port 636 and connection type ldap-s. If each management authentication server is not configured to use secure LDAP, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-266931`

### Rule: AOS must enforce a minimum 15-character password length.

**Rule ID:** `SV-266931r1039814_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum password length required" is not set to "15 characters", this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-266932`

### Rule: AOS must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-266932r1039817_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum number of Upper Case characters" is not set to "1 characters", this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-266933`

### Rule: AOS must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-266933r1039820_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum number of Lower Case characters" is not set to "1 characters", this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-266934`

### Rule: AOS must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-266934r1039823_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum number of Digits" is not set to "1 digits", this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-266935`

### Rule: AOS must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-266935r1039826_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum number of Special characters" is not set to "1 characters", this is a finding.

## Group: SRG-APP-000172-NDM-000259

**Group ID:** `V-266937`

### Rule: AOS must transmit only encrypted representations of passwords.

**Rule ID:** `SV-266937r1039832_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Network devices can accomplish this by making direct function calls to encryption modules or by leveraging operating system encryption capabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show aaa authentication-server all show snmp user-table If the LDAP servers are not configured to use port 636, or if the SNMP users are not configured to use AES encryption, this is a finding.

## Group: SRG-APP-000175-NDM-000262

**Group ID:** `V-266938`

### Rule: AOS must be configured to use DOD-approved Online Certificate Status Protocol (OCSP) responders or Certificate Revocation Lists (CRLs) to validate certificates used for public key infrastructure (PKI)-based authentication.

**Rule ID:** `SV-266938r1039835_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Once issued by a DOD certificate authority (CA), PKI certificates are typically valid for three years or less within the DOD. However, there are many reasons a certificate may become invalid before the prescribed expiration date. For example, an employee may leave or be terminated and still possess the smartcard on which the PKI certificates were stored. Another example is that a smartcard containing PKI certificates may become lost or stolen. A more serious issue could be that the CA or server that issued the PKI certificates has become compromised, thereby jeopardizing every certificate keypair that was issued by the CA. These examples of revocation use cases and many more can be researched further using internet cybersecurity resources. PKI user certificates presented as part of the identification and authentication criteria (e.g., DOD PKI as multifactor authentication [MFA]) must be checked for validity by network devices. For example, valid PKI certificates are digitally signed by a trusted DOD CA. Additionally, valid PKI certificates are not expired, and valid certificates have not been revoked by a DOD CA. Network devices can verify the validity of PKI certificates by checking with an authoritative CA. One method of checking the status of PKI certificates is to query databases referred to as CRLs. These are lists that are published, updated, and maintained by authoritative DOD CAs. For example, once certificates are expired or revoked, issuing CAs place the certificates on a CRL. Organizations can download these lists periodically (i.e., daily or weekly) and store them locally on the devices themselves or onto another nearby local enclave resource. Storing them locally ensures revocation status can be checked even if internet connectivity is severed at the enclave's point of presence. However, CRLs can be large in storage size, and the use of CRLs can tax some computing resources. Another method of validating certificate status is to use the OCSP. Using OCSP, a requestor (i.e., the network device the user is trying to authenticate to) sends a request to an authoritative CA challenging the validity of a certificate that has been presented for identification and authentication. The CA receives the request and sends a digitally signed response indicating the status of the user's certificate as valid, revoked, or unknown. Network devices should only allow access for responses that indicate the certificates presented by the user were considered valid by an approved DOD CA. OCSP is the preferred method because it is fast, provides the most current status, and is lightweight.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show crypto-local pki rcp If any configured trusted root certificate authorities are not configured to use OCSP, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-266940`

### Rule: AOS must use FIPS 140-2/140-3 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-266940r1039841_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied on to provide confidentiality or integrity, and DOD data may be compromised. Network devices using encryption are required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2/140-3 is the current standard for validating that mechanisms used to access cryptographic modules use authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only authentication algorithms that are FIPS-approved and recommended by the National Institute of Standards and Technology (NIST). Satisfies: SRG-APP-000179-NDM-000265, SRG-APP-000224-NDM-000270, SRG-APP-000411-NDM-000330, SRG-APP-000412-NDM-000331</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show fips If "FIPS settings: Mode Enabled" is not returned, this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-266941`

### Rule: AOS must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after five minutes of inactivity except to fulfill documented and validated mission requirements.

**Rule ID:** `SV-266941r1039844_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. Quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated Transmission Control Protocol/Internet Protocol (TCP/IP) address/port pairs at the operating system level or deallocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session. Satisfies: SRG-APP-000190-NDM-000267, SRG-APP-000186-NDM-000266</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show running-config | include "loginsession timeout" show web-server profile If the login session timeout is not set to "5" (minutes), this is a finding. If "User session timeout <30-3600> (seconds)" is not set to "300", this is a finding.

## Group: SRG-APP-000329-NDM-000287

**Group ID:** `V-266948`

### Rule: AOS must enforce role-based access control policies over defined subjects and objects.

**Rule ID:** `SV-266948r1039865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Organizations can create specific roles based on job functions and the authorizations (i.e., privileges) to perform needed operations on organizational information systems associated with the organization-defined roles. When administrators are assigned to the organizational roles, they inherit the authorizations or privileges defined for those roles. RBAC simplifies privilege administration for organizations because privileges are not assigned directly to every administrator (which can be a significant number of individuals for mid- to large-size organizations) but are instead acquired through role assignments. RBAC can be implemented either as a mandatory or discretionary form of access control. The RBAC policies and the subjects and objects are defined uniquely for each network device, so they cannot be specified in the requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> System >> Admin. Expand "Admin Authentication Options". 2. Verify the following: - Default role: Is set to root. - Enable: Checkbox is checked. - The enterprise Server group is set to the configured enterprise LDAP server group. If any of the three settings above are not configured, this is a finding.

## Group: SRG-APP-000343-NDM-000289

**Group ID:** `V-266950`

### Rule: AOS must audit the execution of privileged functions.

**Rule ID:** `SV-266950r1039871_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Misuse of privileged functions, either intentionally or unintentionally by authorized users, or by unauthorized external entities that have compromised information system accounts, is a serious and ongoing concern and can have significant adverse impacts on organizations. Auditing the use of privileged functions is one way to detect such misuse and identify the risk from insider threats and the advanced persistent threat. Satisfies: SRG-APP-000343-NDM-000289, SRG-APP-000101-NDM-000231, SRG-APP-000504-NDM-000321</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show running-config | include audit-trail If the audit-trail is not enabled, this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-266952`

### Rule: AOS must generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-266952r1039877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability, and system operation may be adversely affected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show snmp trap-hosts show snmp trap-list | include wlsxProcessDied show snmp trap-list | include wlsxProcessRestart If a SNMP server is not configured and both process traps are not enabled, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-266953`

### Rule: AOS must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-266953r1039880_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must use an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show ntp servers If at least two NTP servers are not configured, this is a finding.

## Group: SRG-APP-000374-NDM-000299

**Group ID:** `V-266954`

### Rule: AOS must record time stamps for audit records that can be mapped to Coordinated Universal Time (UTC) or Greenwich Mean Time (GMT).

**Rule ID:** `SV-266954r1039962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Alerts provide organizations with urgent messages. Real-time alerts provide these messages immediately (i.e., the time from event detection to alert occurs in seconds or less).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show clock If the clock is not set to the appropriate time zone or UTC/GMT, this is a finding.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-266958`

### Rule: AOS must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-266958r1039895_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show snmp user-table If the configured SNMP user(s) are not using SHA, this is a finding.

## Group: SRG-APP-000400-NDM-000313

**Group ID:** `V-266959`

### Rule: AOS must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-266959r1039898_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Some authentication implementations can be configured to use cached authenticators. If cached authentication information is out of date, the validity of the authentication information may be questionable. The organization-defined time period should be established for each device depending on the nature of the device; for example, a device with just a few administrators in a facility with spotty network connectivity may merit a longer caching time period than a device with many administrators.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show configuration effective | include auth-survivability If "aaa auth-survivability enable" is returned and "auth-survivability" is enabled, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-266961`

### Rule: AOS must be configured to protect against known types of denial-of-service (DoS) attacks by employing organization-defined security safeguards.

**Rule ID:** `SV-266961r1039904_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DOD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (for example, firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: Navigate to Configuration >> Services >> Firewall. If the organization-defined safeguards are not enabled to protect against known DoS attacks, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-266966`

### Rule: AOS must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-266966r1039919_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show logging server If a configured syslog server is not returned, this is a finding.

## Group: SRG-APP-000170-NDM-000329

**Group ID:** `V-266967`

### Rule: AOS must require that when a password is changed, the characters are changed in at least eight of the positions within the password.

**Rule ID:** `SV-266967r1039961_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the application allows the user to consecutively reuse extensive portions of passwords, this increases the chances of password compromise by increasing the window of opportunity for attempts at guessing and brute-force attacks. The number of changed characters refers to the number of changes required with respect to the total number of positions in the current password. In other words, characters may be the same within the two passwords; however, the positions of the like characters must be different. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using public key infrastructure (PKI) is not available and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show aaa password-policy mgmt If "Minimum number of differing characters between passwords" is not set to "8 digits", this is a finding.

## Group: SRG-APP-000516-NDM-000334

**Group ID:** `V-266968`

### Rule: AOS must generate log records for a locally developed list of auditable events.

**Rule ID:** `SV-266968r1039963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or identify an improperly configured network device. If auditing is not comprehensive, it will not be useful for intrusion monitoring, security investigations, and forensic analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show logging level If the logging levels are not set to the organization-desired level, this is a finding.

## Group: SRG-APP-000516-NDM-000336

**Group ID:** `V-266970`

### Rule: AOS must be configured to use at least two authentication servers for the purpose of authenticating users prior to granting administrative access.

**Rule ID:** `SV-266970r1039931_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Centralized management of authentication settings increases the security of remote and nonlocal access methods. This control is particularly important protection against the insider threat. With robust centralized management, audit records for administrator account access to the organization's network devices can be more readily analyzed for trends and anomalies. The alternative method of defining administrator accounts on each device exposes the device configuration to remote access authentication attacks and system administrators with multiple authenticators for each network device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> System >> Admin and expand "Admin Authentication Options". 2. Verify what "Server group" is handling admin authentication. 3. Expand "Admin Authentication Servers". 4. Select the Server Group identified from the "Options" section. 5. Verify that at least two authentication servers are configured in the Server Group. If the admin authentication server group does not have at least two configured authentication servers, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-266971`

### Rule: AOS must be configured to conduct backups of system-level information contained in the information system when changes occur.

**Rule ID:** `SV-266971r1039934_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>System-level information includes default and customized settings and security attributes, including Access Control Lists (ACLs) that relate to the network device configuration, as well as software required for the execution and operation of the device. Information system backup is a critical step in ensuring system integrity and availability. If the system fails and there is no backup of the system-level information, a denial-of-service condition is possible for all who use this critical network component. This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the site's backup policy to verify plans and procedures are in place to back up AOS configurations when changes occur. If the site does not have a policy to back up AOS configurations when changes occur, this is a finding.

## Group: SRG-APP-000516-NDM-000341

**Group ID:** `V-266972`

### Rule: AOS must support organizational requirements to conduct backups of information system documentation, including security-related documentation, when changes occur or weekly, whichever is sooner.

**Rule ID:** `SV-266972r1039937_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system backup is a critical step in maintaining data assurance and availability. Information system and security-related documentation contains information pertaining to system configuration and security settings. If this information were not backed up, and a system failure were to occur, the security settings would be difficult to reconfigure quickly and accurately. Maintaining a backup of information system and security-related documentation provides for a quicker recovery time when system outages occur. This control requires the network device to support the organizational central backup process for user account information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the site's backup policy to verify plans and procedures are in place to back up AOS configurations when changes occur or weekly, whichever is sooner. If the site does not have a policy to back up AOS configurations when changes occur or weekly, whichever is sooner, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-266973`

### Rule: AOS must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-266973r1039940_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by Office of Management and Budget policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this certificate authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system administrator and determine if the network device obtains public key certificates from an appropriate certificate policy through an approved service provider. If the network device does not obtain its public key certificates from an appropriate certificate policy through an approved service provider, this is a finding.

## Group: SRG-APP-000148-NDM-000346

**Group ID:** `V-266975`

### Rule: AOS must be configured with only one local account to be used as the account of last resort in the event the authentication server is unavailable.

**Rule ID:** `SV-266975r1039946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authentication for administrative (privileged-level) access to the device is required at all times. An account can be created on the device's local database for use when the authentication server is down or connectivity between the device and the authentication server is not operable. This account is referred to as the account of last resort since it is intended to be used as a last resort and when immediate administrative access is absolutely necessary. The account of last resort logon credentials must be stored in a sealed envelope and kept in a safe. The safe must be periodically audited to verify the envelope remains sealed. The signature of the auditor and the date of the audit should be added to the envelope as a record. Administrators should secure the credentials and disable the root account (if possible) when not needed for system administration functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show mgmt-user If any user other than "admin" is present, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-266976`

### Rule: AOS must authenticate Network Time Protocol (NTP) sources using authentication that is cryptographically based.

**Rule ID:** `SV-266976r1039949_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If NTP is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify the AOS configuration with the following command: show ntp status If "Authentication" shows "disabled", this is a finding. 2. show running-config | include ntp If at least one trusted NTP authentication-key is not configured and at least one NTP server configured to use the key, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-266977`

### Rule: AOS must be configured to send log data to at least two central log servers for the purpose of forwarding alerts to the administrators and the information system security officer (ISSO).

**Rule ID:** `SV-266977r1039952_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can be used to detect weaknesses in security that enable the network Information Assurance team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, is important to learn whether someone is an internal employee or an outside threat. Satisfies: SRG-APP-000516-NDM-000350, SRG-APP-000223-NDM-000269</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show logging server If at least two central log servers are not configured, this is a finding.

