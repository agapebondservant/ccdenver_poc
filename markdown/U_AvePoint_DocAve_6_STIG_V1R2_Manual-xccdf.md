# STIG Benchmark: AvePoint DocAve 6 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-253510`

### Rule: DocAve must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-253510r836505_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application management includes the ability to control the number of users and user sessions that utilize an application. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement may be met via the application or by utilizing information system session control provided by a web server with specialized session management capabilities. If it has been specified that this requirement will be handled by the application, the capability to limit the maximum number of concurrent single user sessions must be designed and built into the application. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the DocAve Manager Maximum User Session setting. - Log on to DocAve with admin account. - On the Control Panel page, in the System Options section, click "Security Settings". - Select the "System Security Policy" tab. - Verify that Specify a maximum number of user sessions is set to "3" or less. If Maximum number of user sessions is not set to "3" or less, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-253511`

### Rule: DocAve must initiate a session lock after a 15-minute period of inactivity.

**Rule ID:** `SV-253511r836508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A session time-out lock is a temporary action taken when a user stops work and moves away from the immediate physical vicinity of the information system but does not log out because of the temporary nature of the absence. Rather than relying on the user to manually lock their application session prior to vacating the vicinity, applications must be able to identify when a user's application session has idled and take action to initiate the session lock. The session lock is implemented at the point where session activity can be determined and/or controlled. This is typically at the operating system-level and results in a system lock but may be at the application-level where the application interface window is secured instead.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the DocAve Manager Session Timeout setting. - Log on to DocAve with admin account. - On the Control Panel page, in the System Options section, click "Security Settings". - Select the "System Security Policy" tab. - Verify Logon Will Expire is set to "15" minutes or less. If the Logon Will Expire is not set to "15" minutes or less, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-253512`

### Rule: DocAve must use TLS 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-253512r836511_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to Transport Layer Security (TLS) gateways (also known as Secure Sockets Layer [SSL] gateways), web servers, and web applications and is not applicable to virtual private network (VPN) devices. DocAve uses HTTPS and NetTcp protocols as the underlying security protocol and thus is in scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the .Net Framework version on DocAve servers. - On the servers where DocAve is installed, open Registry Editor. - Refer to the official Microsoft document to verify the .Net Framework version supports TLS 1.2. The official Microsoft Document URL is: https://docs.microsoft.com/en-us/mem/configmgr/core/plan-design/security/enable-tls-1-2-client#bkmk_net. - .NET Framework 4.6.2 or later supports TLS 1.2 inherently. If the .Net Framework version doesn't support TLS 1.2, this is a finding. Check that DocAve servers only have TLS 1.2 protocol enabled. - On the DocAve servers, open Registry Editor. - Navigate to: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\SecurityProviders\SCHANNEL\Protocols. - Verify TLS 1.0, TLS 1.1, and any SSL protocols are not enabled. If TLS 1.0, TLS 1.1, or any SSL protocols are enabled, this is a finding. Check that DocAve servers have strong cryptography setting enabled. - On the DocAve servers, open Registry Editor. - Navigate to: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\.NETFramework\v4.0.30319. - Verify "SystemDefaultTlsVersions" = dword:00000001 and "SchUseStrongCrypto" = dword:00000001, otherwise this is a finding.

## Group: SRG-APP-000023

**Group ID:** `V-253513`

### Rule: DocAve must provide automated mechanisms for supporting account management functions.

**Rule ID:** `SV-253513r836514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access (e.g., Remote Desktop Protocol [RDP]) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
DocAve supports integration with Active Directory (AD) for automated account management. Check the DocAve configuration to ensure AD Integration is enabled. - Log on to DocAve with admin account. - On the Control Panel page, in the Authentication Manager section, click "Authentication Manager". - Navigate to AD Integration. - Verify that the AD Integration option is enabled. If the AD Integration option is not enabled, this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-253514`

### Rule: DocAve must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-253514r841862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the DocAve Manager communication port setting. - On the DocAve 6 Manager server, open DocAve 6 Manager Configuration Tool from the Start Menu. - Click "Control Service Configuration" on the left. - Verify the Website Port. - Click "Media Service Configuration" on the left. - Verify the Media Service Port and Media Service Data Port. - Click "Report Service Configuration" on the left. - Verify the Report Service Port. If any of these ports used by the DocAve Manager Services are not in accordance with the PPSM CAL, or otherwise AO Approved, this is a finding. Check the DocAve Agent communication port setting. - On the DocAve 6 Agent server, open DocAve 6 Agent Configuration Tool. - Navigate to the Host And Port panel. - Verify the Agent Port. If the Agent Port is are not in accordance with the PPSM CAL, or otherwise AO Approved, this is a finding. Check the DocAve Control Service update port setting. - Log on to DocAve with admin account. - On the Control Panel page, in the Update Manager section, click "Update Manager", then click "Update Settings". - Navigate to the Update Port section. - Verify the Update Port. If the Update Port is are not in accordance with the PPSM CAL, or otherwise AO Approved, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-253515`

### Rule: DocAve must use multifactor authentication for network access to privileged accounts.

**Rule ID:** `SV-253515r836520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). Multifactor authentication decreases the attack surface by virtue of the fact that attackers must obtain two factors, a physical token or a biometric and a PIN, in order to authenticate. It is not enough to simply steal a user's password to obtain access. A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
DocAve supports Client Certificate Authentication for multi-factor authentication, which requires both Windows Authentication and Client Certificate Authentication enabled in DocAve. Settings must be configured in IIS and DocAve. The IIS configuration under DCAV-00-000057 should be performed first. Check the DocAve Client Certificate Authentication configuration. - Log on to DocAve with admin account. - On the Control Panel page, in the Authentication Manager section, click "Authentication Manager". - Verify that "Client Certificate Authentication" is enabled. If "Client Certificate Authentication" is not enabled, this is a finding. Check the DocAve Windows Authentication configuration. - Log on to DocAve with admin account. - On the Control Panel page, in the Authentication Manager section, click "Authentication Manager". - Verify that "Windows Authentication" is enabled. If "Windows Authentication" is not enabled, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-253516`

### Rule: The underlying IIS platform must be configured for Smart Card (CAC) Authorization.

**Rule ID:** `SV-253516r836523_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) Something a user knows (e.g., password/PIN); (ii) Something a user has (e.g., cryptographic identification device, token); or (iii) Something a user is (e.g., biometric). Multifactor authentication decreases the attack surface by virtue of the fact that attackers must obtain two factors, a physical token or a biometric and a PIN, in order to authenticate. It is not enough to simply steal a user's password to obtain access. A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Web Server (IIS) features required for Client Certificate Authentication are installed. - On the DocAve 6 Manager server, open Server Manager, then click add/remove roles. - Expand Web Server (IIS) >> Web Server >> Security. - Verify that the "Client Certificate Mapping Authentication" and "Windows Authentication" features are installed. If the features are not installed, this is a finding. On the DocAve Manager server, open IIS Manager. - Expand Sites and select the site used for DocAve. The default site name is DocAve6. - Open the SSL Settings of [DocAve6] site under IIS. - Verify the "Require SSL" checkbox is selected. - Verify the "Require" radio button under "Client Certificates" is selected. Return to the Site Settings Home. If the "Require SSL" checkbox is not selected, or the "Require" radio button under "Client Certificates" is not selected, this is a finding. - Open the Authentication Settings of [DocAve6] site under IIS. - Verify "Windows Authentication", is set to "Enable". Return to the Site Settings Home. If "Windows Authentication", is not set to "Enable", this is a finding. - Expand the [DocAve6] site, select Trust. - Open the SSL Settings under IIS. - Check the "Require SSL" checkbox. - Select the "Require" radio button under "Client Certificates". Return to the Site Settings Home. If the "Require SSL" checkbox is not selected, or the "Require" radio button under "Client Certificates" is not selected, this is a finding.

## Group: SRG-APP-000315

**Group ID:** `V-253517`

### Rule: DocAve must control remote access methods.

**Rule ID:** `SV-253517r836526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access applications, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and makes remote user access management difficult at best. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Remote access applications must be capable of taking enforcement action if the audit reveals unauthorized activity. Automated control of remote access sessions allows organizations to ensure ongoing compliance with remote access policies by enforcing connection rules of remote access applications on a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the DocAve Manager configuration to ensure restrict inbound connections from nonsecure zones. - Log on to DocAve as admin account. - On the Control Panel page, under System Options, select "Security Settings". - Navigate to "Network Security" section. If Enable Network Security is not selected, this is a finding. If Enable Network Security is selected, review the entries under Trusted Network. Verify only known, secure IPs are configured as Allow. If IP ranges configured to be Allowed are not restrictive enough to prevent connections from nonsecure zones, this is a finding.

## Group: SRG-APP-000427

**Group ID:** `V-253518`

### Rule: DocAve must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-253518r836529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
There are three different settings in DocAve that are related to certificates: - The DocAve web server for the web UI; - The DocAve Manager communication certificate for communicate with DocAve Agents; - The DocAve Agent communication certificate for communicate with DocAve Manager. Check the DocAve Web Site certificate setting. - On the DocAve 6 Manager server, open Internet Information Services (IIS) Manager. - In IIS Manager, expand the Sites node in the Connections panel on the left and find DocAve 6 Control Service Web Site. The default name of DocAve Control Web Site is DocAve6. - Click "Bindings" in the Actions panel on the right to open the Site Bindings window. - Click "Edit" in Site Bindings window to open the Edit Site Binding window. - Verify the certificate information. If the certificate used is not a DoD- (or AO-) approved certificate, this is a finding. Check the DocAve Manager communication certificate setting. - On the DocAve 6 Manager server, open DocAve 6 Manager Configuration Tool. - Click "Advanced Configuration" on the left. - Verify the certificate information. If the certificate used is not a DoD approved certificate, this is a finding. Check the DocAve Agent communication certificate setting. - On the DocAve 6 Agent server, open DocAve 6 Agent Configuration Tool. - Navigate to the SSL Certificate panel. - Verify the certificate information. If the certificate used is not a DoD-approved certificate, this is a finding.

