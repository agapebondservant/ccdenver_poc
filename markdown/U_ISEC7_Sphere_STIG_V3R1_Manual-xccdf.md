# STIG Benchmark: ISEC7 Sphere Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-224760`

### Rule: The ISEC7 SPHERE must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-224760r1013798_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to denial-of-service (DoS) attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify the maxConnections setting is set according to organizational guidelines. Verify the maxThreads setting is set according to organizational guidelines. If the maxConnections setting is not set according to organizational guidelines or the maxThreads setting is not set according to organizational guidelines, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-224761`

### Rule: The ISEC7 SPHERE must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-224761r1013800_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system, but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system-level and results in a system lock, but may be at the application-level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Validate the session timeout has been set to the correct value. Alternatively, allow the console to sit for 15 minutes and confirm the user is prompted to login again when attempting to navigate to a new screen. If the SPHERE Console timeout has not been set for 15 minutes or less, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-224762`

### Rule: The ISEC7 SPHERE must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-224762r1013803_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to Transport Layer Security (TLS) gateways (also known as Secure Sockets Layer [SSL] gateways), web servers, and web applications and is not applicable to virtual private network (VPN) devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol and thus are in scope for this requirement. NIST SP 800-52 provides guidance for client negotiation on either DOD-only or on public-facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify "protocols" is set to +TLSv1.2, +TLSv1.3. If "protocols" is not set to +TLSv1.2 or higher, this is a finding.

## Group: SRG-APP-000068

**Group ID:** `V-224763`

### Rule: The ISEC7 SPHERE must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the ISEC7 SPHERE.

**Rule ID:** `SV-224763r1013805_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Note if the appropriate Standard mandatory DOD Notice and Consent Banner is displayed. Alternatively, if already logged in to the ISEC7 SPHERE Console, navigate to Administration >> User Self Service >> Page Customizations. Verify that a Page Customization exists to display the Standard mandatory DOD Notice and Consent Banner. If a Page Customization does not exist, or it does not contain the required DOD banner, this is a finding.

## Group: SRG-APP-000090

**Group ID:** `V-224764`

### Rule: The ISEC7 SPHERE server must be configured to have at least one user in the following Administrator roles: Security Administrator, Site Administrator, and Help Desk User.

**Rule ID:** `SV-224764r1013808_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to restrict which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE console. Navigate to Administration >> Configuration >> Access Permissions. Verify for each Role (Security Administrator, Site Administrator, and Help Desk User) that at least one user or AD group has been assigned. If for each Role (Security Administrator, Site Administrator, Help Desk User) there is not at least one user (or AD group) assigned, this is a finding.

## Group: SRG-APP-000108

**Group ID:** `V-224765`

### Rule: The ISEC7 SPHERE must alert the information system security officer (ISSO) and system administrator (SA) (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-224765r1013811_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. This requirement applies to each audit data storage repository (i.e., distinct information system component where audit records are stored), the centralized audit storage capacity of organizations (i.e., all audit data storage repositories combined), or both.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE console. Navigate to Administration >> Configuration >> Notifications >> Recipient Lists. Select "Edit" next to the Systems Notifications. Verify the email address or distribution list has been added. If a recipient email address or distribution list has not been added to System Notifications, this is a finding.

## Group: SRG-APP-000125

**Group ID:** `V-224766`

### Rule: The ISEC7 SPHERE must back up audit records at least every seven days onto a different system or system component than the system or component being audited, provide centralized management and configuration of the content to be captured in audit records generated by all ISEC7 SPHERE components, and offload audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-224766r1013812_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Backing up audit records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to assure in the event of a catastrophic system failure, the audit records will be retained. This helps to ensure a compromise of the information system being audited does not also result in a compromise of the audit records. This requirement only applies to applications that have a native backup capability for audit records. Operating system backup requirements cover applications that do not provide native backup functions. Satisfies: SRG-APP-000125, SRG-APP-000356, SRG-APP-000358</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the central log repository and verify the ISEC7 logs have been written to the location of the log server. Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify that the log directory path is set to the desired location. Alternatively: On the ISEC7 SPHERE server, browse to the install directory. Default is %Install Drive%/Program Files/ISEC7 SPHERE. Select the conf folder. Open config.properties and verify the logPath is set to the desired location. If ISEC7 SPHERE logs are not written to an audit log management server, this is a finding.

## Group: SRG-APP-000148

**Group ID:** `V-224767`

### Rule: ISEC7 SPHERE must disable or delete local account created during application installation and configuration.

**Rule ID:** `SV-224767r1013815_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The ISEC7 local account password complexity controls do not meet DOD requirements; therefore, admins have the capability to configure the account out of compliance, which could allow attacker to gain unauthorized access to the server and access to command MDM servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE console. Navigate to Administration >> Configuration >> Account Management >> Users. Select "Edit" next to the local account Admin. Verify "Log in disabled" has been selected. If "Log in disabled" has not been selected, this is a finding.

## Group: SRG-APP-000175

**Group ID:** `V-224768`

### Rule: When using PKI-based authentication for user access, the ISEC7 SPHERE must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-224768r1013818_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. To meet this requirement, the information system must create trusted channels between itself and remote trusted authorized IT product (e.g., syslog server) entities that protect the confidentiality and integrity of communications. The information system must create trusted paths between itself and remote administrators and users that protect the confidentiality and integrity of communications. A trust anchor is an authoritative entity represented via a public key and associated data. It is most often used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. However, applications that do not use a trusted path are not approved for nonlocal and remote management of DOD information systems. Use of SSHv2 to establish a trusted channel is approved. Use of FTP, TELNET, HTTP, and SNMPV1 is not approved since they violate the trusted channel rule set. Use of web management tools that are not validated by common criteria my also violate trusted channel rule set. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the server(s) hosting the ISEC7 SPHERE application. Open the Microsoft Management Console and add the Local Computer Certificates snap-in. Open the Trusted Root Certification Authorities >> Certificates. Verify the DOD Root PKI Certificates Authorities have been added to the server. If the DOD Root PKI Certificates Authorities have not been added to the server, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-224769`

### Rule: The ISEC7 SPHERE must accept Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-224769r1013821_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Settings. Verify the CAC login box has been checked. On the ISEC7 SPHERE server, browse to the install directory. Default is %Install Drive%/Program Files/ISEC7 SPHERE Select the conf folder. Open config.properties and confirm the following lines exist: cacUserUIDRegex=^CN=[^0-9]*\\.([0-9]+), cacUserUIDProperty=UserPrincipalName Browse to %Install Drive%/Program Files >> ISEC7 SPHERE >> Tomcat >> conf Confirm the server.xml file has clientAuth="required" under the Connection. If the required commands do not exist in config.properties or if clientAuth does not ="required" in the server.xml file, this is a finding.

## Group: SRG-APP-000395

**Group ID:** `V-224770`

### Rule: Before establishing a local, remote, and/or network connection with any endpoint device, the ISEC7 SPHERE must use a bidirectional authentication mechanism configured with a FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to authenticate with the device.

**Rule ID:** `SV-224770r1013824_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without device-to-device authentication, communications with malicious devices may be established. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Currently, DOD requires the use of AES for bidirectional authentication since it is the only FIPS-validated AES cipher block algorithm. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network; the internet). A remote connection is any connection with a device communicating through an external network (e.g., the internet). Because of the challenges of applying this requirement on a large scale, organizations are encouraged to apply the requirement only to those limited number (and type) of devices that truly need to support this capability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Confirm that the browser session is secured using a DOD issued certificate. Internet Explorer: Click the Padlock icon at the end of the url field. Select "View Certificates". Confirm that the Issued By is a valid DOD Certificate Authority. Google Chrome: Click the Padlock icon at the front of the url field. Select "Certificate". Confirm that the Issued By is a valid DOD Certificate Authority. Alternately, log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Identify which type of Keystore is being used. Windows MY: Open the Microsoft Management Console. Add the Certificates Snap-In for the ISEC7 Service Account. Navigate to the Personal Certificates Store. Verify the certificate is issued by a DOD Trusted Certificate Authority. JavaKeystore PKCS12: Using a Keystore browser such as Portecle, open the ISEC7 SPHERE keystore. Enter the Keystore password when prompted. Open the installed certificate and verify it was issued by a DOD Trusted Certificate Authority. If certificates used by the server are not DOD-issued certificates, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-224771`

### Rule: The ISEC7 SPHERE must allow the use of DOD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-224771r1013827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Server. Navigate to %Install Drive%/Program Files/ISEC7 SPHERE/tomcat/bin. Run tomcat9w.bat and select the JAVA tab in the window that opens. Under "Java options" verify "-Djavax.net.ssl.trustStoreType=Windows-ROOT" is listed. If "-Djavax.net.ssl.trustStoreType=Windows-ROOT" is not listed, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-224772`

### Rule: The ISEC7 SPHERE must protect the confidentiality and integrity of transmitted information during preparation for transmission and during reception using cryptographic mechanisms.

**Rule ID:** `SV-224772r1013830_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPSEC. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa. Satisfies: SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify protocols is set to +TLSv1.2, +TLSv1.3. If protocols is not set to +TLSv1.2 or higher, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-224773`

### Rule: The ISEC7 SPHERE must be configured to leverage the enterprise directory service accounts and groups for ISEC7 SPHERE server admin identification and authentication.

**Rule ID:** `SV-224773r1013833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A comprehensive account management process that includes automation helps to ensure the accounts designated as requiring attention are consistently and promptly addressed. If an attacker compromises an account, the entire infrastructure is at risk. Providing automated support functions for the management of accounts will ensure only active accounts will be granted access with the proper authorization levels. These objectives are best achieved by configuring the server to leverage an enterprise authentication mechanism (e.g., Microsoft Active Directory Kerberos).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> LDAP. Verify that a LDAP entry has been configured to the enterprise. Select "Edit" and confirm the "Use for Login" check box has been selected. Navigate to Administration >> Configuration >> Settings. Verify that Log in using (Default) has been set to the enterprise connection. If a LDAP entry has not been configured to the enterprise or Log in using (Default) has not been set to the enterprise connection, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-224774`

### Rule: The ISEC7 SPHERE must configure the timeout for the console to be 15 minutes or less.

**Rule ID:** `SV-224774r1013835_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user (MDM system administrator) stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications need to be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Validate the session timeout has been set to the correct value. Alternatively, allow the console to sit for 15 minutes and confirm that the user is prompted to log in once again when attempting to navigate to a new screen. If the SPHERE Console timeout has not been set for 15 minutes or less, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-224775`

### Rule: The ISEC7 SPHERE, Tomcat installation, and ISEC7 Suite monitor must be configured to use the Windows Trust Store for the storage of digital certificates and keys.

**Rule ID:** `SV-224775r1013838_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A trust store provides requisite encryption and access control to protect digital certificates from unauthorized access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify that the type of Keystore being used is: Windows-MY If the type of Keystore being used is not Windows-MY, this is a finding.

## Group: SRG-APP-000585

**Group ID:** `V-224776`

### Rule: If cipher suites using pre-shared keys are used for device authentication, the ISEC7 SPHERE must have a minimum security strength of 112 bits or higher, must only be used in networks where both the client and server are government systems, must prohibit client negotiation to TLS 1.1, TLS 1.0, SSL 2.0, or SSL 3.0 and must prohibit or restrict the use of protocols that transmit unencrypted authentication information or use flawed cryptographic algorithm for transmission.

**Rule ID:** `SV-224776r1013841_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Pre-shared keys are symmetric keys that are already in place prior to the initiation of a Transport Layer Security (TLS) session (e.g., as the result of a manual distribution). In general, pre-shared keys should not be used. However, the use of pre-shared keys may be appropriate for some closed environments that have stung key management best practices. Pre-shared keys may be appropriate for constrained environments with limited processing, memory, or power. If pre-shared keys are appropriate and supported, the following additional guidelines must be followed. Consult 800-52 for recommended pre-shared key cipher suites for pre-shared keys. Pre-shared keys must be distributed in a secure manner, such as a secure manual distribution or using a key establishment certificate. These cipher suites employ a pre-shared key for device authentication (for both the server and the client) and may also use RSA or ephemeral Diffie-Hellman (DHE) algorithms for key establishment. Because these cipher suites require pre-shared keys, these suites are not generally applicable to classic secure website applications and are not expected to be widely supported in TLS clients or TLS servers. NIST suggests that these suites be considered in particular for infrastructure applications, particularly if frequent authentication of the network entities is required. These cipher suites may be used with TLS versions 1.1 or 1.2. Note that cipher suites using GCM, SHA-256, or SHA-384 are only available in TLS 1.2. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to Transport Layer Security (TLS) gateways (also known as Secure Sockets Layer [SSL] gateways), web servers, and web applications. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol and thus are in scope for this requirement. NIST SP 800-52 provides guidance for client negotiation, either on DOD-only or on public-facing servers. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to manipulation, potentially allowing alteration and hijacking of maintenance sessions. Satisfies: SRG-APP-000585, SRG-APP-000590, SRG-APP-000560, SRG-APP-000645</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Verify protocols is set to +TLSv1.2, +TLSv1.3. If protocols is not set to +TLSv1.2 or higher, this is a finding.

## Group: SRG-APP-000610

**Group ID:** `V-224777`

### Rule: The ISEC7 SPHERE must use FIPS-validated SHA-2 or higher hash function for digital signature generation and verification (nonlegacy use).

**Rule ID:** `SV-224777r1013844_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. To protect the integrity of the authenticator and authentication mechanism used for the cryptographic module used by the network device, the application, operating system, or protocol must be configured to use one of the following hash functions for hashing the password or other authenticator in accordance with SP 800-131Ar1: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, and SHA3-512. For digital signature verification, SP800-131Ar1 allows SHA-1 for legacy use where needed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Confirm that the browser session is secured using a DOD issued certificate. Alternately, log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Identify which type of Keystore is being used. Windows MY: Open the Microsoft Management Console. Add the Certificates Snap-In for the ISEC7 Service Account. Navigate to the Personal Certificates Store. Verify the certificate is issued by a DOD Trusted Certificate Authority. JavaKeystore PKCS12: Using a Keystore browser such as Portecle, open the ISEC7 SPHERE keystore. Enter the Keystore password when prompted. Open the installed certificate and verify it was issued by a DOD Trusted Certificate Authority. If certificates used by the server are not DOD issued certificates, this is a finding.

## Group: SRG-APP-000630

**Group ID:** `V-224778`

### Rule: The ISEC7 SPHERE must use a FIPS-validated cryptographic module to provision digital signatures.

**Rule ID:** `SV-224778r1013847_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. FIPS 140-2 precludes the use of invalidated cryptography for the cryptographic protection of sensitive or valuable data within Federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2 standard. The cryptographic module used must have one FIPS-validated encryption algorithm (i.e., validated Advanced Encryption Standard [AES]). This validated algorithm must be used for encryption for cryptographic security function within the product being evaluated. SPHERE is using the standard JCE module coming with OpenJDK 17 (included in installer) or Oracle JRE either legacy 1.8 or latest release (see https://openjdk.java.net/groups/security/). There are two module providers, IBM and RSA. The check/fix are written assuming the RSA module is used. Any FIPS 140-2 compliant JCE module (.jar) can be replaced and configured and used with SPHERE. Satisfies: SRG-APP-000630, SRG-APP-000412, SRG-APP-000514</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Confirm that the browser session is secured using a DOD issued certificate. Alternately, log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Identify which type of Keystore is being used. Windows MY: Open the Microsoft Management Console. Add the Certificates Snap-In for the ISEC7 Service Account. Navigate to the Personal Certificates Store. Verify the certificate is issued by a DOD Trusted Certificate Authority. JavaKeystore PKCS12: Using a Keystore browser such as Portecle, open the ISEC7 SPHERE keystore. Enter the Keystore password when prompted. Open the installed certificate and verify it was issued by a DOD Trusted Certificate Authority. If certificates used by the server are not DOD issued certificates, this is a finding.

## Group: SRG-APP-000635

**Group ID:** `V-224779`

### Rule: The ISEC7 SPHERE must use a FIPS 140-2-validated cryptographic module to implement encryption services for unclassified information requiring confidentiality, generate cryptographic hashes, and to configure web management tools with FIPS-validated Advanced Encryption Standard (AES) cipher block algorithm to protect the confidentiality of maintenance and diagnostic communications for nonlocal maintenance sessions.

**Rule ID:** `SV-224779r1013850_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FIPS 140-2 precludes the use of invalidated cryptography for the cryptographic protection of sensitive or valuable data within Federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2 standard. The cryptographic module used must have one FIPS-validated encryption algorithm (i.e., validated Advanced Encryption Standard [AES]). This validated algorithm must be used for encryption for cryptographic security function within the product being evaluated. SPHERE is using the standard JCE module coming with OpenJDK 17 (included in installer) or Oracle JRE either legacy 1.8 or latest release. see https://openjdk.java.net/groups/security/ There are two module providers, IBM and RSA. The check/fix are written assuming the RSA module is used. Any FIPS 140-2 compliant JCE module (.jar) can be replaced and configured and used with SPHERE.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE Console. Confirm that the browser session is secured using a DOD issued certificate. Alternately, log in to the ISEC7 SPHERE Console. Navigate to Administration >> Configuration >> Apache Tomcat Settings. Identify which type of Keystore is being used. Windows MY: Open the Microsoft Management Console. Add the Certificates Snap-In for the ISEC7 Service Account. Navigate to the Personal Certificates Store. Verify the certificate is issued by a DOD Trusted Certificate Authority. JavaKeystore PKCS12: Using a Keystore browser such as Portecle, open the ISEC7 SPHERE keystore. Enter the Keystore password when prompted. Open the installed certificate and verify it was issued by a DOD Trusted Certificate Authority. If certificates used by the server are not DOD issued certificates, this is a finding.

## Group: SRG-APP-000171

**Group ID:** `V-224780`

### Rule: The Apache Tomcat Manager Web app password must be cryptographically hashed with a DOD-approved algorithm.

**Rule ID:** `SV-224780r1013853_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Apache Tomcat Manager Web app password is stored in plain text in CATALINA_HOME/conf/tomcat-users.xml and should be encrypted so it is not visible to an intruder. Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read and easily compromised. Use of passwords for authentication is intended only for limited situations and should not be used as a replacement for two-factor CAC-enabled authentication. Examples of situations where a user ID and password might be used include: - When the user does not use a CAC and is not a current DOD employee, member of the military, or DOD contractor. - When a user has been officially designated as temporarily unable to present a CAC for some reason (lost, damaged, not yet issued, broken card reader) (i.e., Temporary Exception User) and to satisfy urgent organizational needs must be temporarily permitted to use user ID/password authentication until the problem with CAC use has been remedied. - When the application is publicly available and or hosting publicly releasable data requiring some degree of need-to-know protection. If the password is already encrypted and not a plaintext password, this meets this requirement. Implementation of this requirement requires configuration of FIPS-approved cipher block algorithm and block cipher modes for encryption. This method uses a one-way hashing encryption algorithm with a salt value to validate a user's password without having to store the actual password. Performance and time required to access are factors that must be considered, and the one-way hash is the most feasible means of securing the password and providing an acceptable measure of password security. Verifying the user knows a password is performed using a password verifier. In its simplest form, a password verifier is a computational function that is capable of creating a hash of a password and determining if the value provided by the user matches the hash. A more secure version of verifying a user knowing a password is to store the result of an iterating hash function and a large random salt value as follows: H0 = H(pwd, H(salt)) Hn = H(Hn-1,H(salt)) In the above, "n" is a cryptographically-strong random [*3] number. "Hn" is stored along with the salt. When the application wishes to verify that the user knows a password, it simply repeats the process and compares "Hn" with the stored "Hn". A salt is essentially a fixed-length cryptographically strong random value. Another method is using a keyed-hash message authentication code (HMAC). HMAC calculates a message authentication code via a cryptographic hash function used in conjunction with an encryption key. The key must be protected as with any private key. This requirement applies to all accounts including authentication server, AAA, and local account, including the root account and the account of last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Apache Tomcat Manager Web app password is hashed using SHA-256 (or SHA-512). Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf\ Open tomcat-users.xml and verify the user password has been hashed with an obfuscated password. ex: <user password="310c55aa3d5b42217e7f0e80ce30467d$100000$529cceb1fbc80f4f461fc1bd56219d79d9c94d4a8fc46abad0646f27e753ff9e" roles="manager-gui,manager-script" username="admin"/> Open <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf\server.xml with Notepad.exe. Select Edit >> Find and search for CredentialHandler. Confirm the text: <CredentialHandler algorithm="PBKDF2WithHmacSHA512" keyLength="256" /> Close the file. If the Apache Tomcat Manager Web app password is not hashed using SHA-256 (or SHA-512), this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-224781`

### Rule: All Web applications included with Apache Tomcat that are not required must be removed.

**Rule ID:** `SV-224781r1013855_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify CATALINA_HOME/webapps Tomcat administrative tool has been configured to remove all Web applications that are not required. Log in to the ISEC7 SPHERE server. Browse to <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\webapps\ Confirm all folders in the directory with the exception of Manager and Host-Manager have been removed. If the CATALINA_HOME/webapps Tomcat administrative tool has not been configured to remove all Web applications that are not required, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-224782`

### Rule: LockOutRealm must not be removed from Apache Tomcat.

**Rule ID:** `SV-224782r1013858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LockOutRealm prevents brute force attacks against user passwords. Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\Program Files\Isec7 SPHERE\Tomcat\Config Open the server.xml file with Notepad. Select Edit >> Find and search for LockOutRealm. Confirm the following line is in the server.xml file: <Realm className="org.apache.catalina.realm.LockOutRealm"> If it is not found or has been commented out, this is a finding. If the LockOutRealm has been removed and cannot be used, this is a finding.

## Group: SRG-APP-000065

**Group ID:** `V-224783`

### Rule: The LockOutRealm must be configured with a login failure count of 3.

**Rule ID:** `SV-224783r1013861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LockOutRealm prevents brute force attacks against user passwords. Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. Access to LockOutRealm must be configured to control login attempts by local accounts. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the failureCount parameter is set to 3 in the LockOutRealm configuration. Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\Program Files\Isec7 SPHERE\Tomcat\Config. Open the server.xml file with Notepad. Select Edit >> Find and search for LockOutRealm. Verify the failureCount parameter is set to 3 in the following file: <Realm className="org.apache.catalina.realm.LockOutRealm" failureCount="3" lockOutTime="900" > If the failureCount parameter is not set to 3 in the LockOutRealm configuration, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-224784`

### Rule: The LockOutRealm must be configured with a login lockout time of 15 minutes.

**Rule ID:** `SV-224784r1013864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LockOutRealm prevents brute force attacks against user passwords. Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. Access to LockOutRealm must be configured to control login attempts by local accounts. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the lockOutTime parameter is set to 900 in the LockOutRealm configuration. Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\Program Files\Isec7 SPHERE\Tomcat\Config. Open the server.xml file with Notepad. Select Edit >> Find and search for LockOutRealm. Verify the lockOutTime parameter is set to 900 in the following file: <Realm className="org.apache.catalina.realm.LockOutRealm" failureCount="3" lockOutTime="900" > If the lockOutTime parameter is not set to 900 in the LockOutRealm configuration, this is a finding.

## Group: SRG-APP-000164

**Group ID:** `V-224785`

### Rule: The Manager Web app password must be configured as follows: 
-15 or more characters.
-at least one lower case letter. 
-at least one upper case letter. 
-at least one number.
-at least one special character.

**Rule ID:** `SV-224785r1013867_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. Satisfies: SRG-APP-000164, SRG-APP-000166, SRG-APP-000169</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Manager Web app password has been configured as follows: -15 or more characters. -at least one lower case letter. -at least one upper case letter. -at least one number. -at least one special character. Log in to the ISEC7 SPHERE server. Open a Web browser and go to https://localhost/manager/html. Log in with the custom administrator login and password. Verify password entered meets complexity requirements. If the Manager Web app password has not been configured as required, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-224786`

### Rule: The ISEC7 SPHERE must configure Enable HTTPS to use HTTP over SSL in Apache Tomcat.

**Rule ID:** `SV-224786r1013870_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPSEC. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Enable HTTPS has been configured to use HTTP over SSL: Open a web browser that is able to reach the ISEC7 SPHERE console. Verify that the address used has a prefix of "https://". Alternately: Log in to the ISEC7 SPHERE server. Open the server.xml file located at <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf with Notepad.exe. Select Edit >> Find and search for port="443". Confirm the connector is present and not commented out: If Enable HTTPS has not been configured to use HTTP over SSL, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-224788`

### Rule: Stack tracing must be disabled in Apache Tomcat.

**Rule ID:** `SV-224788r1013873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default error page shows a full stack trace, which is a disclosure of sensitive information. Removal of unneeded or nonsecure functions, ports, protocols, and services mitigate the risk of unauthorized connection of devices, unauthorized transfer of information, or other exploitation of these resources. The organization must perform a periodic scan/review of the application (as required by CCI-000384) and disable functions, ports, protocols, and services deemed to be unneeded or nonsecure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify stack tracing has been disabled in Apache Tomcat. Navigate to the ISEC7 SPHERE installation directory: <Drive>:\Program Files\ISEC7 SPHERE\web\WEB-INF. Open web.xml with Notepad.exe. Scroll to the end of the file. Confirm there are no comment tags <!--" and "--> and the following exists without comment tags: <error-page> <exception-type>java.lang.Exception</exception-type> <location>/exception.jsp</location> </error-page> If stack tracing has not been disabled in Apache Tomcat, this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-224789`

### Rule: The Apache Tomcat shutdown port must be disabled.

**Rule ID:** `SV-224789r1013876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat uses a port (defaults to 8005) as a shutdown port. Someone could Telnet to the machine using this port and send the default command SHUTDOWN. Tomcat and all web apps would shut down in that case, which is a denial-of-service attack and would cause an unwanted service interruption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the shutdown port is disabled. Log in to the SPHERE server. Browse to Program Files\Isec7 SPHERE\Tomcat\Conf. Open the server.xml with Notepad.exe. Select Edit >> Find, and then search for "Shutdown". Verify that the shutdown port has been disabled with entry below: shutdown="-1" If the shutdown port has not been disabled, this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-224790`

### Rule: The ISEC7 SPHERE must remove any unnecessary users or groups that have permissions to the server.xml file in Apache Tomcat.

**Rule ID:** `SV-224790r1013879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tomcat uses a port (defaults to 8005) as a shutdown port. Someone could Telnet to the machine using this port and send the default command SHUTDOWN. Tomcat and all web apps would shut down in that case, which is a denial-of-service attack and would cause an unwanted service interruption.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify unnecessary users or groups that have permissions to the Server.xml file in Apache Tomcat have been removed. Browse to ProgramFiles\Isec7 SPHERE\Tomcat\Conf and select "Server.xml". Right-click and select "Properties". Select the security tab and verify no unnecessary account or groups have been granted permissions to the file. Verify no unnecessary users or groups have permissions to the file. If unnecessary users or groups that have permissions to the Server.xml file in Apache Tomcat have not been removed, this is a finding.

## Group: SRG-APP-000090

**Group ID:** `V-224791`

### Rule: A manager role must be assigned to the Apache Tomcat Web apps (Manager, Host-Manager).

**Rule ID:** `SV-224791r1013882_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a manager role is not assigned to the Apache Tomcat web apps, the system administrator will not be able to manage and configure the web apps and security setting may not be configured correctly, with could leave the Apache Tomcat susceptible to attack by an intruder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a manager role has been assigned to the Apache Tomcat Web apps (Manager, Host-Manager). Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf\. Confirm a user with the manager role to <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf\tomcat-users.xml exists. example: <user username="admin" roles="manager-gui,manager-script" ..../> If a manager role has not been assigned to the Apache Tomcat Web apps, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-224792`

### Rule: SSL must be enabled on Apache Tomcat.

**Rule ID:** `SV-224792r1013885_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPSEC. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To configure SSL support on Tomcat, run the ISEC7 integrated installer or use the following manual procedure: Log in to the ISEC7 SPHERE server. Open the server.xml file located at <Drive>:\Program Files\ISEC7 SPHERE\Tomcat\conf with Notepad.exe. Select Edit >> Find and search for port="443". If the connector is not present add: ex: <Connector SSLEnabled="true" maxParameterCount="1000" maxThreads="200" port="443" protocol="org.apache.coyote.http11.Http11NioProtocol" scheme="https" secure="true" sslImplementationName="org.apache.tomcat.util.net.jsse.JSSEImplementation"> <SSLHostConfig certificateVerification="false" ciphers="HIGH:!aNULL:!MD5:!3DES:!ARIA:!SHA:!CAMELLIA:!AES128-CCM8:!AES128-CCM:!AES256-CCM8:!AES256-CCM:!DHE" honorCipherOrder="true" protocols="+TLSv1.2,+TLSv1.3"> <Certificate certificateKeyAlias="https" certificateKeystoreFile="" certificateKeystoreType="Windows-MY"/> </SSLHostConfig> </Connector> Modifying the certificateKeystoreFile path and certificateKeystorePassword as needed or leveraging the Windows-MY certificateKeystoreType instead. If the connector has been commented out, remove the comment characters. Save the file. Restart the ISEC7 SPHERE Web service.

## Group: SRG-APP-000439

**Group ID:** `V-224793`

### Rule: Tomcat SSL must be restricted except for ISEC7 SPHERE tasks.

**Rule ID:** `SV-224793r1013888_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Restricting the use of SSL helps ensure only authorized users and processes have access to Tomcat Web apps and reduces the attack surface of the ISEC7 EMM Suite. Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data nonlocally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, TLS VPNs, or IPSEC. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify Tomcat SSL is restricted to only ISEC7 SPHERE tasks. Log in to the ISEC7 SPHERE server. Navigate to <Drive>:\ProgramFiles\ISEC7 SPHERE\Tomcat\conf\. Edit the web.xml file with Notepad.exe. Verify the following entries are present: <security-constraint> <web-resource-collection> <web-resource-name>Unsecure</web-resource-name> <!-- Agent --> <url-pattern>/BNator/agent/*</url-pattern> <url-pattern>/app/agent/*</url-pattern> <url-pattern>/app/admin/agentinstaller.jnlp</url-pattern> <!-- Client --> <url-pattern>/app/clients/*</url-pattern> <url-pattern>/app/data/*</url-pattern> <!-- Remote Control --> <url-pattern>/rc/*</url-pattern> <!-- Traffic Push --> <url-pattern>/BNator/uss/trafficinfo/*</url-pattern> <url-pattern>/BNator/data/mds/trafficpush</url-pattern> <url-pattern>/BNator/favorites/*</url-pattern> <url-pattern>/app/resource/*</url-pattern> </web-resource-collection> </security-constraint> <security-constraint> <web-resource-collection> <web-resource-name>Secure</web-resource-name> <url-pattern>/*</url-pattern> </web-resource-collection> <user-data-constraint> <transport-guarantee>CONFIDENTIAL</transport-guarantee> </user-data-constraint> </security-constraint> If Tomcat SSL is not restricted to only ISEC7 SPHERE tasks, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-225096`

### Rule: The ISEC7 Sphere server must be maintained at a supported version.

**Rule ID:** `SV-225096r1013891_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Versions of ISEC7 Sphere server are maintained by ISEC7 for specific periods of time. Unsupported versions will not receive security updates for new vulnerabilities which leaves them subject to exploitation. A list of supported ISEC7 Sphere server versions is maintained by ISEC7 here: https://www.isec7-us.com/emm-suite-mobile-monitoring.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ISEC7 Sphere server version after logging into the console. Correlate the version with the latest supported version of ISEC7 Sphere server. If the installed version of ISEC7 Sphere server is not a supported version, this is a finding.

