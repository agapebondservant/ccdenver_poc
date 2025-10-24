# STIG Benchmark: Ivanti Sentry 9.x NDM Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-250982`

### Rule: Sentry must limit the number of concurrent sessions for the CLISH interface to an organization-defined number for each administrator account and/or administrator account type.

**Rule ID:** `SV-250982r1028209_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the CLISH has a max number of SSH sessions enabled. 1. Log in to the Sentry System Manager. 2. Go to Settings >> CLI. 3. Verify a Max SSH Sessions integer (1-10) is set based on security guidance. If the Max SSH Sessions integer is not set correctly, this is a finding.

## Group: SRG-APP-000001-NDM-000200

**Group ID:** `V-250983`

### Rule: Sentry must be configured to limit the network access of the Sentry System Manager Portal behind the corporate firewall and whitelist source IP range.

**Rule ID:** `SV-250983r1028210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device management includes the ability to control the number of administrators and management sessions that manage a device. Limiting the number of allowed administrators and sessions per administrator based on account type, role, or access type is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for administrative accounts and does not address concurrent sessions by a single administrator via multiple administrative accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. At a minimum, limits must be set for SSH, HTTPS, account of last resort, and root account sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a secondary interface has been added for System Manager Portal Access of Sentry. 1. Log in to the Sentry System Manager. 2. Go to Settings >> Network >> Interfaces. 3. Verify a Management Interface for internal access of the System Manager Portal has been added as one of the interfaces. If the Management Interface for internal access of the System Manager Portal has not been added as one of the Interfaces, this is a finding.

## Group: SRG-APP-000003-NDM-000202

**Group ID:** `V-250984`

### Rule: Sentry must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-250984r1028211_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session lock is a temporary network device or administrator-initiated action taken when the administrator stops work but does not log out of the network device. Rather than relying on the user to manually lock their management session prior to vacating the vicinity, network devices need to be able to identify when a management session has idled and take action to initiate the session lock. Once invoked, the session lock shall remain in place until the administrator reauthenticates. No other system activity aside from reauthentication shall unlock the management session. Note that CCI-001133 requires that administrative network sessions be disconnected after 10 minutes of idle time. So this requirement may only apply to local administrative sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the System manager Timeout is set to 15 minutes. 1. Log in to the Sentry System Manager. 2. Navigate to Settings >> Timeout. 3. Verify the System Manager timeout is set to 15. If the System Manager timeout is not set to 15, this is a finding.

## Group: SRG-APP-000038-NDM-000213

**Group ID:** `V-250985`

### Rule: Sentry must enforce approved authorizations for controlling the flow of management information within the network device based on information flow control policies.

**Rule ID:** `SV-250985r1028212_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A mechanism to detect and prevent unauthorized communication flow must be configured or provided as part of the system design. If management information flow is not enforced based on approved authorizations, the network device may become compromised. Information flow control regulates where management information is allowed to travel within a network device. The flow of all management information must be monitored and controlled so it does not introduce any unacceptable risk to the network device or data. Application-specific examples of enforcement occur in systems that employ rule sets or establish configuration settings that restrict information system services or message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics). Applications providing information flow control must be able to enforce approved authorizations for controlling the flow of management information within the system in accordance with applicable policy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Sentry configuration to determine if it enforces approved authorizations for controlling the flow of management information within the network. Sentry receives a request from MobileIron Core and enforces verification before handling the request to validate that it is from a trusted MobileIron Core. Therefore, if the deployment uses MobileIron Core, to verify that Sentry trusts MobileIron Core in the deployment: 1. Run the following command in Sentry CLI: show sentry EMM-source-verify If this is set to "false", this is a finding. 2. Run the following command in Sentry CLI: show sentry emm-ips If the Core IP is not specified, this is a finding. 3. Verify Sentry has an ACL for Core in Sentry System Manager. Then: 1. In the Standalone Sentry System Manager, go to Security >> Access Control Lists. 2. Verify that an ACL is created for Core. If it is not, this is a finding. 3. Determine if Sentry is configured with specified backend services such as Exchange Active Sync or App Tunnels. If the backend service is not specified, this is a finding. Refer to section "Configuring Standalone Sentry for ActiveSync" and "Configuring Standalone Sentry for AppTunnel" in "Sentry 9.8 Guide for MobileIron Core" to ensure these services are configured in Sentry settings in Core where applicable.

## Group: SRG-APP-000065-NDM-000214

**Group ID:** `V-250986`

### Rule: Sentry must be configured to enforce the limit of three consecutive invalid logon attempts, after which time it must block any login attempt for 15 minutes.

**Rule ID:** `SV-250986r1028213_rule`
**Severity:** low

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Sentry configuration to verify that it enforces the limit of three consecutive invalid logon attempts. 1. Log in to Sentry System Manager portal. 2. Go to the "Security" tab. 3. Go to "Password Policy". 4. Look for "Number of Failed Attempts" and determine if the value is set to 3. If it is not, this is a finding. 5. Verify the Auto-Lock Time value is set to 900 seconds or more. If the Auto-Lock Time is not set to 900 seconds or more, this is a finding.

## Group: SRG-APP-000068-NDM-000215

**Group ID:** `V-250987`

### Rule: Sentry must display the Standard Mandatory DOD Notice and Consent Banner in the Sentry web interface before granting access to the device.

**Rule ID:** `SV-250987r1028214_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Sentry displays "I've read and consent to terms in IS user agreem't" when logging in to the command line. 1. Log in to the Sentry System Manager or the CLI interface. 2. Verify the required login banner is displayed. If the banner is not shown, this is a finding.

## Group: SRG-APP-000149-NDM-000247

**Group ID:** `V-250988`

### Rule: Sentry must be configured to use DOD PKI as multi-factor authentication (MFA) for interactive logins.

**Rule ID:** `SV-250988r1028216_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Multi-factor authentication (MFA) is when two or more factors are used to confirm the identity of an individual who is requesting access to digital information resources. Valid factors include something the individual knows (e.g., username and password), something the individual has (e.g., a smartcard or token), or something the individual is (e.g., a fingerprint or biometric). Legacy information system environments only use a single factor for authentication, typically a username and password combination. Although two pieces of data are used in a username and password combination, this is still considered single factor because an attacker can obtain access simply by learning what the user knows. Common attacks against single-factor authentication are attacks on user passwords. These attacks include brute force password guessing, password spraying, and password credential stuffing. MFA, along with strong user account hygiene, helps mitigate against the threat of having account passwords discovered by an attacker. Even in the event of a password compromise, with MFA implemented and required for interactive login, the attacker still needs to acquire something the user has or replicate a piece of user’s biometric digital presence. Private industry recognizes and uses a wide variety of MFA solutions. However, DOD public key infrastructure (PKI) is the only prescribed method approved for DOD organizations to implement MFA. For authentication purposes, centralized DOD certificate authorities (CA) issue PKI certificate key pairs (public and private) to individuals using the prescribed x.509 format. The private certificates that have been generated by the issuing CA are downloaded and saved to smartcards which, within DOD, are referred to as common access cards (CAC) or personal identity verification (PIV) cards. This happens at designated DOD badge facilities. The CA maintains a record of the corresponding public keys for use with PKI-enabled environments. Privileged user smartcards, or "alternate tokens", function in the same manner, so this requirement applies to all interactive user sessions (authorized and privileged users). Note: This requirement is used in conjunction with the use of a centralized authentication server (e.g., AAA, RADIUS, LDAP), a separate but equally important requirement. The MFA configuration of this requirement provides identification and the first phase of authentication (the challenge and validated response, thereby confirming the PKI certificate that was presented by the user). The centralized authentication server will provide the second phase of authentication (the digital presence of the PKI ID as a valid user in the requested security domain) and authorization. The centralized authentication server will map validated PKI identities to valid user accounts and determine access levels for authenticated users based on security group membership and role. In cases where the centralized authentication server is not utilized by the network device for user authorization, the network device must map the authenticated identity to the user account for PKI-based authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Sentry Configuration to ensure Certificate Authentication has been configured. 1. Log in to the Sentry System Manager. 2. Go to Security tab >> Advanced >> Sign-in Authentication. 3. Determine if Certificate Authentication is activated and configured. If Certificate Authentication is not activated and configured, this is a finding.

## Group: SRG-APP-000164-NDM-000252

**Group ID:** `V-250989`

### Rule: Sentry device must enforce a minimum 15-character password length.

**Rule ID:** `SV-250989r1029559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review Sentry configuration to verify that a minimum 15-character password is set. 1. Log in to Sentry System Manager portal. 2. Go to the "Security" tab. 3. Go to Identity Source >> Password Policy. 4. Verify the "Minimum Password Length" is set to 15 or more. If the password character length is not set 15 or more, this is a finding.

## Group: SRG-APP-000166-NDM-000254

**Group ID:** `V-250990`

### Rule: Sentry must enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-250990r1029560_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex passwords helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password is, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, verify that Sentry Server enforces password complexity by requiring that at least one uppercase character be used. This requirement may be verified by demonstration, configuration review, or validated test results. If Sentry Server does not require that at least one uppercase character be used in each password, this is a finding. Verify the local Password Policy enforces an uppercase value: 1. Log in to the System Manager of Sentry. 2. Go to Security >> Identity Source >> Password. 3. Verify "Upper Case" is checked. If "Upper Case" is not checked, this is a finding.

## Group: SRG-APP-000167-NDM-000255

**Group ID:** `V-250991`

### Rule: Sentry must enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-250991r1029561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that Sentry Server enforces password complexity by requiring that at least one lowercase character be used. This requirement may be verified by demonstration, configuration review, or validated test results. If Sentry does not require that at least one lowercase character be used in each password, this is a finding. 1. Log in to the System Manager of Sentry. 2. Go to Security >> Identity Source >> Password. 3. Verify "Lower Case" is checked. If "Lower Case" is not checked, this is a finding.

## Group: SRG-APP-000168-NDM-000256

**Group ID:** `V-250992`

### Rule: Sentry must enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-250992r1029562_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that Sentry Server enforces password complexity by requiring that at least one numeric character be used. This requirement may be verified by demonstration, configuration review, or validated test results. If Sentry Server does not require that at least one numeric character be used in each password, this is a finding. 1. Log into the System Manager of Sentry. 2. Go to Security >> Identity Source >> Password. 3. Verify "Numeric" is checked. If "Numeric" is not checked, this is a finding.

## Group: SRG-APP-000169-NDM-000257

**Group ID:** `V-250993`

### Rule: Sentry must enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-250993r1029563_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Multifactor authentication (MFA) is required for all administrative and user accounts on network devices, except for an account of last resort and (where applicable) a root account. Passwords should only be used when MFA using PKI is not available, and for the account of last resort and root account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Where passwords are used, confirm that Sentry Server enforces password complexity by requiring that at least one special character be used. If Sentry Server does not require that at least one special character be used in each password, this is a finding. 1. Log in to the System Manager of Sentry. 2. Go to Security >> Identity Source >> Password. 3. Verify "Special Character" is checked. If "Special Character" is not checked, this is a finding.

## Group: SRG-APP-000177-NDM-000263

**Group ID:** `V-250994`

### Rule: Sentry, for PKI-based authentication, must be configured to map validated certificates to unique user accounts.

**Rule ID:** `SV-250994r1028230_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without mapping the PKI certificate to a unique user account, the ability to determine the identities of individuals or the status of their non-repudiation is considerably impacted during forensic analysis. A strength of using PKI as MFA is that it can help ensure only the assigned individual is using their associated user account. This can only be accomplished if the network device is configured to enforce the relationship which binds PKI certificates to unique user accounts. Local accounts (accounts created, stored, and maintained locally on the network device) should be avoided in lieu of using a centrally managed directory service. Local accounts empower the same workgroup who will be operating the network infrastructure to also control and manipulate access methods, thus creating operational autonomy. This undesirable approach breaks the concept of separation of duties. Additionally, local accounts are susceptible to poor cyber hygiene because they create another user database that must be maintained by the operator, whose primary focus is on running the network. Such examples of poor hygiene include dormant accounts that are not disabled or deleted, employees who have left the organization but whose accounts are still present, periodic password and hash rotation, password complexity shortcomings, increased exposure to insider threat, etc. For reasons such as this, local users on network devices are frequently the targets of cyber-attacks. Instead, organizations should explore examples of centrally managed account services. These examples include the implementation of AAA concepts like the use of external RADIUS and LDAP directory service brokers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an EDIPI is mapped to the Sentry Admin user accounts. 1. Log in to the Sentry System Manager. 2. Verify "Certificate Based Authentication" under Security Tab >> Sign-In Authentication. 3. Verify that a Certificate Attribute Mapping is mapped to EDIPI. 4. Go to Security tab >> Local Users. Click on an active Local User and configure an EDIPI. 5. Click "Apply". 6. Repeat step 4 for all local users. If EDIPI is not mapped to the Sentry Admin user accounts, this is a finding.

## Group: SRG-APP-000179-NDM-000265

**Group ID:** `V-250995`

### Rule: Sentry must use FIPS 140-2 approved algorithms for authentication to a cryptographic module.

**Rule ID:** `SV-250995r1028232_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not validated and therefore cannot be relied upon to provide confidentiality or integrity, and DOD data may be compromised. Sentry utilizing encryption is required to use FIPS-compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DOD requirements. However, authentication algorithms must configure security processes to use only FIPS-approved and NIST-recommended authentication algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the Sentry CLI console, do the following: 1. SSH to Sentry Server from any SSH client. 2. Enter the administrator credentials set at Sentry installation. 3. Enter "enable". 4. When prompted, enter the "enable secret" set at Sentry installation. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-APP-000190-NDM-000267

**Group ID:** `V-250996`

### Rule: Sentry must terminate all network connections associated with a device management session at the end of the session, or the session must be terminated after 10 minutes of inactivity except to fulfill documented and validated mission requirement.

**Rule ID:** `SV-250996r1028233_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, or de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system-level network connection. This does not mean that the device terminates all sessions or network access; it only ends the inactive session and releases the resources associated with that session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Sentry System Manager has two interfaces, a CLI restricted shell and web-based GUI. In the Sentry MICS portal, verify that the Sentry CLI timeout is set to 10 minutes. 1. Log in to Sentry. 2. Go to Settings >> CLI. 3. Within CLI Configuration, verify the CLI Session Timeout(minutes) is set to greater than 10 minutes. If the CLI Session Timeout(minutes) is not set to greater than 10 minutes, this is a finding.

## Group: SRG-APP-000224-NDM-000270

**Group ID:** `V-250997`

### Rule: Sentry must generate unique session identifiers using a FIPS 140-2 approved random number generator.

**Rule ID:** `SV-250997r1028235_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sequentially generated session IDs can be easily guessed by an attacker. Employing the concept of randomness in the generation of unique session identifiers helps to protect against brute-force attacks to determine future session identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement is applicable to devices that use a web interface for device management.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry uses encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions. On the Sentry CLI console, do the following: 1. SSH to Sentry Server from any SSH client. 2. Enter the administrator credentials set at Sentry installation. 3. Enter "enable". 4. When prompted, enter the "enable secret" set at Sentry installation. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If the Sentry Server does not report that FIPS mode is "enabled", this is a finding.

## Group: SRG-APP-000360-NDM-000295

**Group ID:** `V-250998`

### Rule: Sentry must generate an immediate real-time alert of all audit failure events requiring real-time alerts.

**Rule ID:** `SV-250998r1028236_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is configured to send alerts for failure events in Sentry System Manager web GUI. 1. Log in to Sentry. 2. Go to Monitoring >> Alert Configuration. 3. Verify Alert monitoring is configured. If Alert Configuration settings are not configured, this is a finding. Refer to the "Alert Configuration" section of the "Sentry 9.8.0 Guide for MobileIron Core" for more information.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-250999`

### Rule: Sentry must be configured to synchronize internal information system clocks using redundant authoritative time sources.

**Rule ID:** `SV-250999r1029564_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DOD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DOD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is configured with multiple date and time servers (NTP). 1. Log in to Sentry. 2. Go to Settings >> Date and Time (NTP). 3. Verify the NTP servers are configured. If NTP servers are not configured, this is a finding. Refer to the "Date and Time (NTP)" section of the "Sentry 9.8.0 Guide for MobileIron Core" for more information.

## Group: SRG-APP-000395-NDM-000310

**Group ID:** `V-251000`

### Rule: The Sentry must be configured to authenticate SNMP messages using a FIPS-validated Keyed-Hash Message Authentication Code (HMAC).

**Rule ID:** `SV-251000r1028238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the Sentry console, do the following to verify FIPS mode is enabled: 1. SSH to Sentry Server from any SSH client. 2. Enter the administrator credentials set at Sentry installation. 3. Enter "enable". 4. When prompted, enter the "enable secret" set at Sentry installation. 5. Enter "show FIPS". 6. Verify "FIPS 140 mode is enabled" is displayed. If it is not, this is a finding. Then: 1. Log in to Sentry. 2. Go to Settings >> SNMP. 3. Verify SNMP server has been added. a. If SNMP server is not added, this is a finding. b. If SNMP server is added, go to step 4. 4. Verify SNMP Control is not disabled. a. If SNMP Control is disabled, this is a finding. b. If SNMP Control is not disabled, go to step 5. 5. Verify Protocol v3 is selected. a. If Protocol v3 is not selected, this is a finding. b. If Protocol v3 is selected, go to step 6. 6. Verify the SNMP v3 User has been added. a. If SNMP v3 User has not been added, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-251001`

### Rule: Sentry must be configured to implement cryptographic mechanisms using a FIPS 140-2 approved algorithm to protect the confidentiality of remote maintenance sessions.

**Rule ID:** `SV-251001r1028239_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On Sentry console, do the following to verify FIPS mode is activated to protect the confidentiality of remote maintenance sessions: 1. SSH to the Sentry. 2. Run the "show FIPS" command. 3. Verify FIPS 140 mode is not disabled. If FIPS 140-2 mode is disabled, this is a finding.

## Group: SRG-APP-000515-NDM-000325

**Group ID:** `V-251002`

### Rule: Sentry must offload audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-251002r1028240_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Sentry is configured to offload audit records to a different system. 1. Log in to Sentry. 2. Go to Settings >> Syslog. 3. Verify that a syslog server is configured. If the syslog server is not configured, this is a finding.

## Group: SRG-APP-000516-NDM-000335

**Group ID:** `V-251003`

### Rule: Sentry must enforce access restrictions associated with changes to the system components.

**Rule ID:** `SV-251003r1028241_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Changes to the hardware or software components of the network device can have significant effects on the overall security of the network. Therefore, only qualified and authorized individuals should be allowed administrative access to the network device for implementing any changes or upgrades. This requirement applies to updates of the application files, configuration, ACLs, and policy filters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only authorized administrators have permissions for changes, deletions, and updates on the Sentry. 1. Log in to System Manager. 2. Go to Security >> Local Users. 3. Verify no unauthorized users are listed. If unauthorized users are listed, this is a finding.

## Group: SRG-APP-000516-NDM-000340

**Group ID:** `V-251004`

### Rule: Sentry must be configured to conduct backups of system level information contained in the information system when changes occur.

**Rule ID:** `SV-251004r1028242_rule`
**Severity:** low

**Description:**
<VulnDiscussion>This control requires the network device to support the organizational central backup process for system-level information associated with the network device. This function may be provided by the network device itself; however, the preferred best practice is a centralized backup rather than each network device performing discrete backups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify/validate Sentry support for periodic backups. This is done via the virtual machine. Check with the virtual team to verify backups are scheduled. If the backups are not scheduled, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-251005`

### Rule: Sentry must obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-251005r1028243_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the Sentry has a public certificate from an approved Certificate Authority. From MobileIron Core: 1. Log in to the MobileIron Core. 2. Navigate to "Services". 3. Select "Sentry". 4. On each configured Sentry, select "View Certificate". 5. Validate the Public Key is issued from an approved Certificate Authority. From Sentry: 1. Log in to the Sentry. 2. Navigate to "Security". 3. Scroll down to "Certificate Mgmt". 4. Select "View Certificate". If approved certificates have not been uploaded, this is a finding.

## Group: SRG-APP-000516-NDM-000350

**Group ID:** `V-251006`

### Rule: Sentry must be configured to send log data to a central log server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-251006r1028244_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without syslog enabled it will be difficult for an ISSO to correlate the users behavior and identify potential threats within the logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To identify/validate Sentry support for syslog forwarding, follow the navigation steps below. 1. Log in to the Sentry. 2. Navigate to "Settings". 3. Scroll down to "Syslog". 4. Verify that a syslog server has been configured correctly. a. Verify Server IP address. b. Verify Port. c. Verify Facility Types. d. Verify Admin state is enabled. If syslog forwarding has not been implemented, this is a finding.

## Group: SRG-APP-000516-NDM-000351

**Group ID:** `V-251007`

### Rule: Sentry must be running an operating system release that is currently supported by MobileIron.

**Rule ID:** `SV-251007r1028245_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Network devices running an unsupported operating system lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Sentry is a supported version. 1. Enter the Sentry System Manager Portal URL in a web browser. 2. View the version number in the top right corner. 3. Check the MI Support page (help.mobileiron.com) to ensure the MI Sentry is a supported version. If the version number of the Sentry appliance is not supported, this is a finding.

