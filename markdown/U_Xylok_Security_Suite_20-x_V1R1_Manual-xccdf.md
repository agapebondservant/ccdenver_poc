# STIG Benchmark: Xylok Security Suite 20.x Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000380

**Group ID:** `V-269569`

### Rule: Xylok Security Suite must protect application-specific data.

**Rule ID:** `SV-269569r1053482_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The /var/lib/xylok directory is essential for storing various types of data necessary for the operation and functionality of the Xylok Security Suite. It acts as a central repository for application data, ensuring that the suite can function effectively and maintain state and configuration between sessions. Proper management and protection of this directory is crucial to ensure the security and stability of the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Xylok lib file permissions with the following command: $ ls -l /var/lib/xylok If "db" file has permissions greater than "0700", this is a finding. If any other file or directory has permissions greater than "0755", this is a finding.

## Group: SRG-APP-000001

**Group ID:** `V-269570`

### Rule: Xylok Security Suite must limit system resources consumed by the application.

**Rule ID:** `SV-269570r1053485_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Not limiting system resources to Xylok presents a denial-of-service (DoS) risk. Each open instance of Xylok periodically retrieves a list of background tasks. Open sessions, even sessions not being actively used, consume a small amount of server resources and could result in Xylok becoming slow or entirely responsive. In addition, this risk impacts the host system for the container by consuming excessive CPU, allowing a DoS attack on Xylok to also impact other software hosted on the same physical machine. Satisfies: SRG-APP-000001, SRG-APP-000435</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Xylok is configured to limit its maximum CPU and memory usage with the following command, run from the host machine as a normal user: $ grep LIMIT_ /etc/xylok.conf Verify the following settings are configured: - LIMIT_MEM set to less than 100 percent of the host machine's memory. - LIMIT_CPU set to less than 1000. If any of the above settings are not present or are blank, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-269571`

### Rule: Xylok Security Suite must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-269571r1053488_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not log out because of the temporary nature of the absence. The session lock is implemented at the point where session activity can be determined and/or controlled. This is handled at the operating system-level and results in a system lock. Satisfies: SRG-APP-000003, SRG-APP-000190</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify session is configured to lock after 15 minutes of inactivity. Execute the following: $ grep SESSION_LENGTH /etc/xylok.conf SESSION_LENGTH=900 If "SESSION_LENGTH" is set to more than15 minutes or is missing, this is a finding. Note: The setting is in seconds. 900 sec = 15 min.

## Group: SRG-APP-000005

**Group ID:** `V-269572`

### Rule: Xylok Security Suite must expire a session upon browser closing.

**Rule ID:** `SV-269572r1053491_rule`
**Severity:** high

**Description:**
<VulnDiscussion>When the session expires as soon as the browser is closed, it prevents session hijacking and unauthorized users from accessing the account or data if they reopen the browser. Leaving a session open in the browser even after it is closed could expose the system to various types of attacks, like cross-site scripting (XSS) or malware designed to steal session cookies. Automatically expiring sessions mitigates this risk. Satisfies: SRG-APP-000005, SRG-APP-000220, SRG-APP-000295, SRG-APP-000413</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify session expires after browser is closed. Execute the following: $ grep SESSION_EXPIRE_AT_BROWSER_CLOSE /etc/xylok.conf SESSION_EXPIRE_AT_BROWSER_CLOSE=True If "SESSION_EXPIRE_AT_BROWSER_CLOSE" is not set to "True" or is missing, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-269573`

### Rule: Xylok Security Suite must prevent access except through HTTPS.

**Rule ID:** `SV-269573r1054093_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Preventing access, except via HTTPS, ensures security and protects sensitive data. HTTP_ONLY: If true, disables listening on the HTTPS port and allows all calls to happen over HTTP. This must be set to false. HTTPS encrypts data transmitted between the client (browser) and the server. Sensitive information, such as login credentials, personal data, and session cookies, is protected from being intercepted by malicious actors (e.g., through man-in-the-middle attacks) during transmission. When data is sent over HTTP (unencrypted), it can be intercepted and altered. HTTPS mitigates this by encrypting the communication. HTTPS uses digital certificates (SSL/TLS certificates) to authenticate the server’s identity. This ensures that users are connecting to the legitimate server rather than a malicious entity attempting to impersonate the site. HTTPS-only policies enable the use of HSTS, which forces browsers to only interact with the site using HTTPS and prevents users from being redirected to an HTTP version of the site. This can defend against certain attacks, like SSL stripping, which downgrade connections to HTTP. Satisfies: SRG-APP-000014, SRG-APP-000142, SRG-APP-000219, SRG-APP-000411, SRG-APP-000412, SRG-APP-000439, SRG-APP-000440, SRG-APP-000442, SRG-APP-000514, SRG-APP-000555, SRG-APP-000645 </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify HTTP_ONLY is set to "false": $ grep HTTP_ONLY /etc/xylok.conf HTTP_ONLY=false If "HTTP_ONLY=true" or is not configured, this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-269574`

### Rule: Xylok Security Suite must use a centralized user management solution.

**Rule ID:** `SV-269574r1053497_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Configuring Xylok Security Suite to integrate with an Enterprise Identity Provider enhances security, simplifies user management, ensures compliance, provides auditing capabilities, and offers a more seamless and consistent user experience. It aligns Xylok Security Suite with enterprise standards and contributes to a more efficient and secure environment. Satisfies: SRG-APP-000023, SRG-APP-000025, SRG-APP-000026, SRG-APP-000027, SRG-APP-000028, SRG-APP-000029, SRG-APP-000033, SRG-APP-000065, SRG-APP-000080, SRG-APP-000089, SRG-APP-000090, SRG-APP-000149, SRG-APP-000150, SRG-APP-000153, SRG-APP-000154, SRG-APP-000155, SRG-APP-000156, SRG-APP-000157, SRG-APP-000163, SRG-APP-000164, SRG-APP-000165, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000170, SRG-APP-000173, SRG-APP-000175, SRG-APP-000176, SRG-APP-000177, SRG-APP-000180, SRG-APP-000185, SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000318, SRG-APP-000319, SRG-APP-000320, SRG-APP-000345, SRG-APP-000391, SRG-APP-000392, SRG-APP-000401, SRG-APP-000402, SRG-APP-000403, SRG-APP-000404, SRG-APP-000405, SRG-APP-000503, SRG-APP-000505, SRG-APP-000506, SRG-APP-000508, SRG-APP-000700, SRG-APP-000705, SRG-APP-000710, SRG-APP-000815, SRG-APP-000820, SRG-APP-000825, SRG-APP-000830, SRG-APP-000835, SRG-APP-000840, SRG-APP-000845, SRG-APP-000850, SRG-APP-000855, SRG-APP-000860, SRG-APP-000865, SRG-APP-000870, SRG-APP-000875, SRG-APP-000910</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if Xylok is configured to use Active Directory (AD) authentication with the following command, run from the host machine as a normal user: $ grep -e "AD_SIGN_IN" -e "XYLOK_HOST" -e "AD_CLIENT_ID" /etc/xylok.conf Verify the following settings are present: - AD_SIGN_IN - XYLOK_HOST - AD_CLIENT_ID If any of the above settings are not present, blank, or "false" (case insensitive), this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-269575`

### Rule: Xylok Security Suite must display the Standard Mandatory DOD Notice and Consent Banner before granting access.

**Rule ID:** `SV-269575r1054094_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Users accessing Xylok must be informed their actions might be monitored, potentially opening the organization up to legal challenges. Implementing a Consent Banner helps Xylok Security Suite remain compliant with legal requirements and protect user privacy while informing users of their rights regarding their data. Satisfies: SRG-APP-000068, SRG-APP-000069</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Standard Mandatory DOD Notice and Consent Banner has been configured: $ grep BANNER /etc/xylok.conf If the Standard Mandatory DOD Notice and Consent Banner is not displayed, this is a finding.

## Group: SRG-APP-000118

**Group ID:** `V-269576`

### Rule: Xylok Security Suite must protect audit information from any type of unauthorized access.

**Rule ID:** `SV-269576r1053503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to their advantage. To ensure the veracity of audit data, the information system and/or the Xylok Security Suite must protect audit information from any and all unauthorized access. This includes read, write, and copy access. Satisfies: SRG-APP-000118, SRG-APP-000119, SRG-APP-000120, SRG-APP-000121, SRG-APP-000122, SRG-APP-000123</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Xylok log file directory permissions with the following command: $ ls -l /var/log/xylok If any of the directories have permissions greater than "0770", this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-269577`

### Rule: Xylok Security Suite must be running a supported version.

**Rule ID:** `SV-269577r1053506_rule`
**Severity:** high

**Description:**
<VulnDiscussion>It is critical to the security and stability of Xylok to ensure that updates and patches are deployed through a trusted software supply chain. Key elements to having a trusted supply chain include ensuring that versions deployed come from known, trusted sources. Additionally, it is important to check for and apply security-relevant updates in a timely manner. To help users manage updates, Xylok manages versions via their internal portal. Satisfies: SRG-APP-000131, SRG-APP-000456</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the latest install is being used. Log on to the GUI and locate the version from the lower left corner. Compare this version with the latest release on the Xylok portal (https://downloads.xylok.io). If the current version is not the latest version from the Xylok portal, this is a finding.

## Group: SRG-APP-000133

**Group ID:** `V-269578`

### Rule: The Xylok Security Suite READONLY configuration must be True.

**Rule ID:** `SV-269578r1054098_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, the Xylok container is created not allowing users to modify any files inside the container. The only paths that can be altered are mounted from the host. Mount the database files from the host, so that the database server running inside the container can write data. If READONLY=false, then a user could go into the container as root and change other files. This approach helps protect the application from both external attacks and internal threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Xylok's default read-only status is disabled by using the following command: $ grep READONLY /etc/xylok.conf If "READONLY" is set to False (case insensitive), is commented out or is missing, this is not a finding.

## Group: SRG-APP-000141

**Group ID:** `V-269579`

### Rule: Xylok Security Suite must disable nonessential capabilities.

**Rule ID:** `SV-269579r1053512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Xylok has unnecessary functionality enabled, the server may allow arbitrary code to run within the Xylok container. This would allow the user to potentially launch malicious acts against other hosts from inside the Xylok container. ENABLE_PP_TEST_API setting in the Xylok Security Suite refers to a configuration flag that enables a specific test API related to the policy processing (PP) functionalities of the suite. This setting is used primarily in development or testing environments to enable specific testing functionalities. Satisfies: SRG-APP-000141, SRG-APP-000246, SRG-APP-000247, SRG-APP-000384</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that Xylok's default ENABLE_PP_TEST_API status is disabled by using the following command: $ grep ENABLE_PP_TEST_API /etc/xylok.conf If "ENABLE_PP_TEST_API" exists (case insensitive), this is a finding.

## Group: SRG-APP-000266

**Group ID:** `V-269580`

### Rule: The Xylok Security Suite configuration for DEBUG must be False.

**Rule ID:** `SV-269580r1053515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing too much information in error messages risks compromising the data and security of the Xylok Security Suite and system. If DEBUG is set to True, it will show stack traces in error messages to assist with contact Xylok Support, but potentially reveal secure information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify DEBUG is configured. Execute the following: $ grep DEBUG /etc/xylok.conf DEBUG=False If "DEBUG" is not set to False or is missing, this is a finding.

## Group: SRG-APP-000328

**Group ID:** `V-269581`

### Rule: Xylok Security Suite must not allow local user or groups.

**Rule ID:** `SV-269581r1054095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Active Directory’s (AD's) design to create but not delete local groups supports operational efficiency, system integrity, and compliance needs. Manual checks will help identify user accounts that are no longer active or orphaned accounts which could pose security risks. Within Xylok there must not be a local users/groups. Manually verifying local users and groups ensures that unauthorized users do not gain access to sensitive resources. Satisfies: SRG-APP-000328, SRG-APP-000715, SRG-APP-000720, SRG-APP-000725, SRG-APP-000730, SRG-APP-000735</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the local accounts and groups are associated with AD and that user privileges are correct. Check accounts as a logged in administrator in Xylok. 1. Verify there are no local users. Navigate to User Menu <username> >> Database Admin >> Users. If any local user(s) exist or users(s) are not current in AD, this is a finding. If any users have privileged access that do not require that access, this is a finding. 2. Verify there are no removed or local groups. Navigate to User Menu <username> >> Database Admin >> Groups . Verify the only groups exist are created by AD and are currently being used by AD. If any groups exist that are not actively being used by AD, this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-269582`

### Rule: The Xylok Security Suite configuration file must be protected.

**Rule ID:** `SV-269582r1053521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the configuration file is a fundamental aspect of maintaining the security, integrity, and stability of Xylok Security Suite. By implementing robust protection mechanisms, Xylok can safeguard sensitive information, ensure compliance, and enhance operational reliability while minimizing the risks associated with unauthorized access and misconfigurations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Xylok configuration file permissions with the following command: $ ls -l /etc/xylok.conf If this file has permissions greater than "0644", this is a finding.

## Group: SRG-APP-000381

**Group ID:** `V-269583`

### Rule: Xylok Security Suite must audit the enforcement actions used to restrict access associated with changes to it.

**Rule ID:** `SV-269583r1053524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, auditing is not set up. Verifying that the host operating system generates audit records for events affecting /etc/xylok.conf is a critical security practice for Xylok. It enhances security monitoring, ensures accountability, supports compliance, maintains operational integrity, mitigates risks, and improves integration with security monitoring tools. Without auditing the enforcement of access restrictions against changes to the Xylok Security Suite configuration, it will be difficult to identify attempted attacks and an audit trail will not be available for forensic investigation for after-the-fact actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the host machine as a normal user, verify the host OS generates audit records for all account creations, modifications, disabling, and termination events that affect "/etc/xylok.conf" with the following command: Note: Directions are for Red Hat Enterprise Linux (RHEL) 8 and similar. If using a different OS, the steps may vary. $ sudo grep /etc/xylok.conf /etc/audit/audit.rules -w /etc/xylok.conf -p warx -k xylok_config If the command does not return a line, or the line is commented out, this is a finding

## Group: SRG-APP-000427

**Group ID:** `V-269584`

### Rule: Xylok Security Suite must only allow the use of DOD Public Key Infrastructure (PKI) established certificate authorities (CAs) for verification of the establishment of protected sessions.

**Rule ID:** `SV-269584r1054096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted CAs can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of Transport Layer Security (TLS) certificates. This requirement focuses on communications protection for the Xylok Security Suite session rather than for the network packet. This requirement applies to applications that use communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOAs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the certificate Xylok uses for SSL is correctly signed with the following command. In this command, replace "xylok.local" with the domain named used to access the Xylok instance. $ openssl s_client -showcerts -servername xylok.local -connect xylok.local:443 </dev/null CONNECTED(00000003) depth=2 C = US, O = Internet Security Research Group, CN = ISRG Root X1 verify return:1 depth=1 C = US, O = Let's Encrypt, CN = E5 verify return:1 depth=0 CN = xylok.local verify return:1 --- Certificate chain 0 s:CN = xylok.local i:C = US, O = Let's Encrypt, CN = E5 a:PKEY: id-ecPublicKey, 256 (bit); sigalg: ecdsa-with-SHA384 v:NotBefore: Jun 12 16:44:03 2024 GMT; NotAfter: Sep 10 16:44:02 2024 GMT -----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- 1 s:C = US, O = Let's Encrypt, CN = E5 i:C = US, O = Internet Security Research Group, CN = ISRG Root X1 a:PKEY: id-ecPublicKey, 384 (bit); sigalg: RSA-SHA256 v:NotBefore: Mar 13 00:00:00 2024 GMT; NotAfter: Mar 12 23:59:59 2027 GMT -----BEGIN CERTIFICATE----- ... -----END CERTIFICATE----- --- Server certificate subject=CN = xylok.local issuer=C = US, O = Let's Encrypt, CN = E5 --- No client certificate CA names sent Peer signing digest: SHA256 Peer signature type: ECDSA Server Temp Key: X25519, 253 bits --- SSL handshake has read 2367 bytes and written 380 bytes Verification: OK --- New, TLSv1.3, Cipher is TLS_AES_128_GCM_SHA256 Server public key is 256 bit This TLS version forbids renegotiation. Compression: NONE Expansion: NONE No ALPN negotiated Early data was not sent Verify return code: 0 (ok) --- --- Post-Handshake New Session Ticket arrived: SSL-Session: Protocol : TLSv1.3 Cipher : TLS_AES_128_GCM_SHA256 Session-ID: E03F9C6A59BD7375CF86B43387C63F9BBD16EAA2A9970E64F70E20317D403D22 Session-ID-ctx: Resumption PSK: 15BFB16AF236A045FE9F5A0F64834A1B3EA76EE4185936D83560BAE940D01FF4 PSK identity: None PSK identity hint: None SRP username: None TLS session ticket lifetime hint: 604800 (seconds) TLS session ticket: 0000 - d4 7d 77 f4 01 dd ba 65-57 59 76 e0 ab 8a 75 63 .}w....eWYv...uc 0010 - 19 6e cf 1b 44 db 35 c5-27 6b d8 b8 39 76 10 47 .n..D.5.'k..9v.G 0020 - f1 75 a5 4b 3a fb 2b 82-b9 f7 3c c5 7f 82 41 d0 .u.K:.+...<...A. 0030 - 3d 40 f1 f4 0d ef 8e 55-ee 2f 09 4b 96 d9 16 5a =@.....U./.K...Z 0040 - f2 7d cb af bd 55 4b f9-c8 2d 0d 8f 39 16 af 8c .}...UK..-..9... 0050 - 71 df 92 cc d1 1a ed 5d-71 eb a3 7f f0 8b 65 8c q......]q.....e. 0060 - 5b 16 18 0c 61 b2 cc c7-4b [...a...K Start Time: 1719438481 Timeout : 7200 (sec) Verify return code: 0 (ok) Extended master secret: no Max Early Data: 0 --- read R BLOCK DONE If the output indicates a "verify error", Xylok is using a self-signed certificate and this is a finding. If the first certificate displayed is not a DOD-approved CA or other approved authority, this is a finding.

## Group: SRG-APP-000441

**Group ID:** `V-269585`

### Rule: Xylok Security Suite must maintain the confidentiality and disable the use of SMTP.

**Rule ID:** `SV-269585r1053530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Disabling the use of SMTP within the Xylok Security Suite is a strategic decision aimed at enhancing security, ensuring compliance, and reducing operational risks. By eliminating the potential vulnerabilities associated with email communications, Xylok can better protect sensitive data and maintain a robust security posture.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify USE_SMTP is configured by executing the following: $ grep USE_SMTP /etc/xylok.conf If "USE_SMTP" is not set to "False" or is missing, this is a finding.

## Group: SRG-APP-000745

**Group ID:** `V-269586`

### Rule: Xylok Security Suite must use a central log server for auditing records.

**Rule ID:** `SV-269586r1053533_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Integrating a central log server for managing audit records within the Xylok Security Suite enhances security monitoring, incident response, and compliance efforts. By providing centralized logging, real-time analysis, and automated alerting, a central log server allows Xylok to maintain a robust security posture and effectively respond to potential threats, ultimately contributing to the organization's overall security strategy. Satisfies: SRG-APP-000745, SRG-APP-000115, SRG-APP-000125, SRG-APP-000181, SRG-APP-000358, SRG-APP-000362, SRG-APP-000363, SRG-APP-000364, SRG-APP-000365, SRG-APP-000366, SRG-APP-000367, SRG-APP-000368, SRG-APP-000369, SRG-APP-000370, SRG-APP-000376, SRG-APP-000750, SRG-APP-000755, SRG-APP-000760, SRG-APP-000765, SRG-APP-000770, SRG-APP-000775, SRG-APP-000780, SRG-APP-000785, SRG-APP-000790, SRG-APP-000795, SRG-APP-000800, SRG-APP-000805, SRG-APP-000515</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify SIEM. On the host server, ensure /etc/rsyslog.d/101-xylok.conf exists and contains the following contents: $ModLoad imfile $InputFileName /var/log/xylok/api/current $InputFileTag xylok-api: $InputFileStateFile /tmp/xylok-api-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor $InputFileName /var/log/xylok/db/current $InputFileTag xylok-db: $InputFileStateFile /tmp/xylok-db-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor $InputFileName /var/log/xylok/mx/current $InputFileTag xylok-mx: $InputFileStateFile /tmp/xylok-mx-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor $InputFileName /var/log/xylok/primary/current $InputFileTag xylok-primary: $InputFileStateFile /tmp/xylok-primary-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor $InputFileName /var/log/xylok/web/current $InputFileTag xylok-web: $InputFileStateFile /tmp/xylok-web-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor $InputFileName /var/log/xylok/worker/current $InputFileTag xylok-worker: $InputFileStateFile /tmp/xylok-worker-log-state $InputFileSeverity info $InputFileFacility local3 $InputRunFileMonitor If the file contents do not monitor all logs in /var/log/xylok/, this is a finding. If the rsyslog destination is not configured to send logs to a valid syslog server, this is a finding. Note: The rsyslog destination host may appear in a different file, often following a format similar to “*.* @siem.example.com:514.

## Group: SRG-APP-000516

**Group ID:** `V-269740`

### Rule: Xylok Security Suite must use a valid DOD-issued certification.

**Rule ID:** `SV-269740r1054081_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the use of a certificate validation process, the site is vulnerable to accepting certificates that have expired or have been revoked. This would allow unauthorized individuals access to the web server. This also defeats the purpose of the multi-factor authentication provided by the PKI process.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Xylok Security Suite is using a valid DOD-issued certification with the following command: $ openssl x509 -noout -text -in /opt/xylok/certs/cert.crt Certificate: Data: Version: 3 (0x2) Serial Number: 1 (0x1) Signature Algorithm: sha256WithRSAEncryption Issuer: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Validity Not Before: Mar 20 18:46:41 2012 GMT Not After : Dec 30 18:46:41 2029 GMT Subject: C = US, O = U.S. Government, OU = DoD, OU = PKI, CN = DoD Root CA 3 Subject Public Key Info: Public Key Algorithm: rsaEncryption If the Issuer is not an approved authority, this is a finding.

