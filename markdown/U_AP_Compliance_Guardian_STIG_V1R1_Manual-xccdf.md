# STIG Benchmark: AvePoint Compliance Guardian Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-256839`

### Rule: Compliance Guardian must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-256839r890127_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be satisfied by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Compliance Guardian Manager Maximum User Session setting. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the System Configuration section, click "General Settings". - Select "Security - System Security Policy". - Verify that the "Specify a maximum simultaneous logons for the same user" is set to "5". If the maximum number of user sessions is higher than 5, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-256840`

### Rule: Compliance Guardian must initiate a session timeout after a 15-minute period of inactivity.

**Rule ID:** `SV-256840r890130_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications must identify when a user's session has idled and initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system level and results in a system lock but may be at the application level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Compliance Guardian Manager Session Timeout setting. - Log on to Compliance Guardian with admin account. - On the Control Panel page, in the System Configuration section, click "General Settings". - Select "Security - System Security Policy". - Verify the "Please specify a session time-out value". The user will be logged off automatically if there is no activity for the specified period. Logon will expire in option. If the session timeout value is not set to 15 minutes or less, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-256841`

### Rule: Compliance Guardian must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-256841r890133_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to Transport Layer Security (TLS) gateways (also known as Secure Sockets Layer [SSL] gateways), web servers, and web applications and is not applicable to virtual private network (VPN) devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol and thus are in scope for this requirement. NIST SP 800-52 provides guidance for client negotiation on either DOD-only or on public-facing servers. Satisfies: SRG-APP-000014, SRG-APP-000560, SRG-APP-000565, SRG-APP-000645</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the .Net Framework version on Compliance Guardian servers. - On servers where Compliance Guardian is installed, open "Registry Editor". - Refer to the Microsoft document to verify the .Net Framework version supports TLS 1.2. The Microsoft Document URL is: https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client#bkmk_net. - .NET Framework 4.6.2 or later supports TLS 1.2 natively. If the .Net Framework version doesn't support TLS 1.2, this is a finding. Check the Compliance Guardian servers only have TLS 1.2 protocol enabled. - On the Compliance Guardian servers, open "Registry Editor". - Navigate to HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols. - Verify TLS 1.0, TLS 1.1, and any SSL protocols are not enabled. If TLS 1.0, TLS 1.1, or any SSL protocols are enabled, this is a finding. Check that Compliance Guardian servers have strong cryptography setting enabled. - On the Compliance Guardian servers, open "Registry Editor". - Navigate to HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319. Verify "SystemDefaultTlsVersions" = dword:00000001 and "SchUseStrongCrypto" = dword:00000001, otherwise this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-256842`

### Rule: Compliance Guardian must provide automated mechanisms for supporting account management functions.

**Rule ID:** `SV-256842r890136_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include dial-up, broadband, and wireless. Satisfies: SRG-APP-000023, SRG-APP-000025, SRG-APP-000065, SRG-APP-000163, SRG-APP-000164, SRG-APP-000165, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000170, SRG-APP-000171, SRG-APP-000173, SRG-APP-000174, SRG-APP-000190, SRG-APP-000234, SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000295, SRG-APP-000318, SRG-APP-000319, SRG-APP-000320, SRG-APP-000345, SRG-APP-000397, SRG-APP-000401, SRG-APP-000503, SRG-APP-000505, SRG-APP-000506, SRG-APP-000509</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Compliance Guardian supports integration with Active Directory (AD) for automated account management. Check the Compliance Guardian configuration to ensure AD Integration is enabled. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the General Security section, click "Authentication Manager". - Navigate to "AD Integration". - Verify that the "AD Integration" option is enabled. If the AD Integration option is not enabled, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-256843`

### Rule: Compliance Guardian must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-256843r890139_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services); however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Compliance Guardian Manager communication port setting. - On the Compliance Guardian Manager server, open "Compliance Guardian Manager Configuration Tool" from the Start Menu. - Click "Control Service Configuration" on the left. - Verify the Website Port. If any ports used by the Compliance Guardian Manager Services are not in accordance with the PPSM CAL or are not AO approved, this is a finding. Check the Compliance Guardian Agent communication port setting. - On the Compliance Guardian Agent server, open "Compliance Guardian Agent Configuration Tool". - Navigate to the "Host And Port" panel. - Verify the Agent Port. If the Agent Port is are not in accordance with the PPSM CAL or are not AO approved, this is a finding. Check the Compliance Guardian Control Service update port setting. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the License and Update section, click "Update Manager", then click "Settings". - Verify the "Specify a port number" to install the update. If the Update Port is not in accordance with the PPSM CAL or is not AO approved, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-256844`

### Rule: Compliance Guardian must use multifactor authentication for network access to privileged accounts.

**Rule ID:** `SV-256844r890142_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). Multifactor authentication decreases the attack surface by virtue of the fact that attackers must obtain two factors, a physical token or a biometric and a PIN, in order to authenticate. It is not enough to simply steal a user's password to obtain access. A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet). Satisfies: SRG-APP-000149, SRG-APP-000150, SRG-APP-000177, SRG-APP-000391, SRG-APP-000392, SRG-APP-000402, SRG-APP-000403</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Compliance Guardian supports Client Certificate Authentication for multifactor authentication, which requires that both Windows Authentication and Client Certificate Authentication are enabled in Compliance Guardian. Check the Compliance Guardian Client Certificate Authentication configuration. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the General Security section, click "Authentication Manager". - Verify that the Client Certificate Authentication option is enabled. If Client Certificate Authentication is not enabled, this is a finding. Check the Compliance Guardian Windows Authentication configuration. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the General Security section, click "Authentication Manager". - Verify that the "Windows Authentication" option is enabled. If "Windows Authentication" is not enabled, this is a finding.

## Group: SRG-APP-000315

**Group ID:** `V-256845`

### Rule: Compliance Guardian must control remote access methods.

**Rule ID:** `SV-256845r890145_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access applications (such as those providing remote access to network devices and information systems) which lack automated control capabilities, increase risk, and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include dial-up, broadband, and wireless. Remote access applications must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Compliance Guardian Manager configuration to ensure the restriction of inbound connections from nonsecure zones. - Log on to Compliance Guardian as admin account. - On the Control Panel page in the System Configuration section, click "General Settings". - Select "Security - System Security Policy". - Verify "Specify network security settings" option. If "Enable Network Security" is not selected, this is a finding. If "Enable Network Security" is selected, review the entries under Trusted Network. Verify only known, secure IPs are configured as "Allow". If "Restricted Network" is selected, review the entries under Restricted Network. If IP address restrictions are not configured or IP ranges configured to be allowed are not restrictive enough to prevent connections from nonsecure zones, this is a finding.

## Group: SRG-APP-000404

**Group ID:** `V-256846`

### Rule: Compliance Guardian must accept FICAM-approved third-party credentials.

**Rule ID:** `SV-256846r890148_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access may be denied to legitimate users if FICAM-approved third-party credentials are not accepted. This requirement typically applies to organizational information systems that are accessible to nonfederal government agencies and other partners. This allows federal government-relying parties to trust such credentials at their approved assurance levels. Third-party credentials are those credentials issued by nonfederal government entities approved by the Federal Identity, Credential, and Access Management (FICAM) Trust Framework Solutions initiative.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable if ADFS is not being utilized. ADFS can be used to federate with approved third-party users. Check the Compliance Guardian configuration option for ADFS Integration. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the General Security section, click "Authentication Manager". - Verify that the ADFS Integration option is enabled. If the ADFS Integration is not enabled, this is a finding.

## Group: SRG-APP-000405

**Group ID:** `V-256847`

### Rule: Compliance Guardian must conform to FICAM-issued profiles.

**Rule ID:** `SV-256847r890151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without conforming to FICAM-issued profiles, the information system may not be interoperable with FICAM-authentication protocols, such as SAML 2.0 and OpenID 2.0. This requirement addresses open identity management standards.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement is Not Applicable is ADFS is not being utilized. Check the Compliance Guardian configuration option for ADFS Integration. - Log on to Compliance Guardian with admin account. - On the Control Panel page in the General Security section, click "Authentication Manager". - Verify that the ADFS Integration option is enabled. If the ADFS Integration is not enabled, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-256848`

### Rule: Compliance Guardian must only allow the use of DOD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-256848r890154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CAs) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes the use of TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
There are three different settings in Compliance Guardian that are related to certificates. 1. The Compliance Guardian web server for the web UI. 2. The Compliance Guardian Manager communication certificate for communicating with Compliance Guardian Agents. 3. The Compliance Guardian Agent communication certificate for communicating with Compliance Guardian Manager. 1. Check the Compliance Guardian Web Site certificate setting. - On the Compliance Guardian Manager server, open Internet Information Services (IIS) Manager. - In IIS Manager, expand the Sites node in the Connections panel on the left and find Compliance Guardian Web Site. The default name of Compliance Guardian Control Web Site is ComplianceGuardian4Site. - Click "Bindings" in the Actions panel on the right to open the "Site Bindings" window. - Click "Edit" in Site Bindings window to open the "Edit Site Binding" window. - Verify the certificate information. If the certificate used is not a DOD- or AO-approved certificate, this is a finding. 2. Check the Compliance Guardian Manager communication certificate setting. - On the Compliance Guardian Manager server, open Compliance Guardian Manager Configuration Tool. - Click "Advanced Configuration" on the left. - Verify the certificate information. If the certificate used is not a DOD-approved certificate, this is a finding. 3. Check the Compliance Guardian Agent communication certificate setting. - On the Compliance Guardian Agent server, open Compliance Guardian Agent Configuration Tool. - Navigate to the SSL Certificate panel. - Verify the certificate information. If the certificate used is not a DOD-approved certificate, this is a finding.

