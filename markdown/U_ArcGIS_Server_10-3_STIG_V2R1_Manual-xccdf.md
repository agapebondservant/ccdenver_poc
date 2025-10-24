# STIG Benchmark: ArcGIS for Server 10.3 Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000015

**Group ID:** `V-237320`

### Rule: The ArcGIS Server must protect the integrity of remote access sessions by enabling HTTPS with DoD-approved certificates.

**Rule ID:** `SV-237320r879520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure the application implements cryptographic mechanisms to protect the integrity of remote access sessions. Substitute the target environment’s values for [bracketed] variables. Navigate to IIS Manager >> [Default Website] >> Open “Bindings...” Verify “https” is listed as a binding. If “https” is not identified as a binding, this is a finding. Navigate to IIS Manager >> [Default Website] >> “SSL Settings” Verify that “Require SSL” is checked. If “Require SSL” is not checked, this is a finding. This control is not applicable for ArcGIS Servers which are deployed as part of a solution which ensures user web service traffic flows through third-party DoD compliant transport encryption devices (such as a load balancer that supports TLS encryption using DoD-approved certificates.) This control is not applicable for ArcGIS Servers which are not deployed with the ArcGIS Web Adaptor component.

## Group: SRG-APP-000023

**Group ID:** `V-237321`

### Rule: The ArcGIS Server must use Windows authentication for supporting account management functions.

**Rule ID:** `SV-237321r879522_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enterprise environments make application account management challenging and complex. A manual process for account management functions adds the risk of a potential oversight or other error. A comprehensive application account management process that includes automation helps to ensure accounts designated as requiring attention are consistently and promptly addressed. Examples include, but are not limited to, using automation to take action on multiple accounts designated as inactive, suspended or terminated or by disabling accounts located in non-centralized account stores such as multiple servers. This requirement applies to all account types, including individual/user, shared, group, system, guest/anonymous, emergency, developer/manufacturer/vendor, temporary, and service. The application must be configured to automatically provide account management functions and these functions must immediately enforce the organization's current account policy. The automated mechanisms may reside within the application itself or may be offered by the operating system or other infrastructure providing automated account management capabilities. Automated mechanisms may be comprised of differing technologies that when placed together contain an overall automated mechanism supporting an organization's automated account management requirements. Account management functions include: assignment of group or role membership; identifying account type; specifying user access authorizations (i.e., privileges); account removal, update, or termination; and administrative alerts. The use of automated mechanisms can include, for example: using email or text messaging to automatically notify account managers when users are terminated or transferred; using the information system to monitor account usage; and using automated telephonic notification to report atypical system account usage. Satisfies: SRG-APP-000023, SRG-APP-000025, SRG-APP-000026, SRG-APP-000065, SRG-APP-000164, SRG-APP-000165, SRG-APP-000166, SRG-APP-000167, SRG-APP-000168, SRG-APP-000169, SRG-APP-000170, SRG-APP-000171, SRG-APP-000173, SRG-APP-000174</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure mechanisms for supporting account management functions are provided. Substitute the target environment’s values for [bracketed] variables. Verify ArcGIS for Server is utilizing Windows Users & Roles as its security store. Navigate to [https://server.domain.com/arcgis]/admin/security/config (logon when prompted.) Verify the “User Store Configuration” value = “Type: Windows”. If the “User Store Configuration” value is set to “Type: Built-In”, this is a finding. Verify the “Role Store Configuration” value = “Type: Windows”. If the “Role store Configuration” value is set to “Type: Built-In”, this is a finding. If the "Type" parameter of the "User Store Configuration" or "Role Store Configuration" is set to "Built-In", this is a finding. This test requires the account performing the check to have "Administrator" privilege to the ArcGIS for Server site. This check can be performed remotely via HTTPS. This configuration is only valid when ArcGIS for Server has been deployed onto a Windows 2008 or later operating system that is a member of an Active Directory domain. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000033

**Group ID:** `V-237322`

### Rule: The ArcGIS Server must use Windows authentication to enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-237322r879530_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions. Satisfies: SRG-APP-000033, SRG-APP-000038, SRG-APP-000080, SRG-APP-000148, SRG-APP-000149, SRG-APP-000150, SRG-APP-000151, SRG-APP-000152, SRG-APP-000153, SRG-APP-000158, SRG-APP-000163, SRG-APP-000172, SRG-APP-000176, SRG-APP-000177, SRG-APP-000178, SRG-APP-000180, SRG-APP-000190, SRG-APP-000220</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that the application enforces approved authorizations for logical access to information system resources. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]/admin/security/config (logon when prompted.) Verify the "User Store Configuration" value = "Type: Windows". If the "User Store Configuration" value is set to "Type: Built-In", this is a finding. Verify the "Role Store Configuration" value = "Type: Windows". If the "Role store Configuration" value is set to "Type: Built-In", this is a finding. Verify the "Authentication Tier" value is set to "WEB_ADAPTOR". If the "Authentication Tier" value is set to "GIS_SERVER", this is a finding. Open IIS Manager on the system that hosts the ArcGIS Web Adaptor. Select the "[arcgis]" application. Open "SSL Settings". Verify the "Client Certificates" property is set to "Require". If the "Client Certificates" property is not set to "Require", this is a finding. This test requires the account performing the check to have "Administrator" privilege to the ArcGIS for Server site. This check can be performed remotely via HTTPS. This configuration is only valid when ArcGIS for Server has been deployed onto a Windows 2008 or later operating system that is a member of an Active Directory domain. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD-compliant certificate authentication solutions.

## Group: SRG-APP-000089

**Group ID:** `V-237323`

### Rule: The ArcGIS Server must provide audit record generation capability for DoD-defined auditable events within all application components.

**Rule ID:** `SV-237323r879559_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Audit records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the application will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions. Satisfies: SRG-APP-000089, SRG-APP-000016, SRG-APP-000027, SRG-APP-000028, SRG-APP-000029, SRG-APP-000091, SRG-APP-000095, SRG-APP-000097, SRG-APP-000098, SRG-APP-000099, SRG-APP-000100, SRG-APP-000226, SRG-APP-000319, SRG-APP-000343, SRG-APP-000381, SRG-APP-000492, SRG-APP-000493, SRG-APP-000494, SRG-APP-000495, SRG-APP-000496, SRG-APP-000497, SRG-APP-000498, SRG-APP-000499, SRG-APP-000500, SRG-APP-000501, SRG-APP-000502, SRG-APP-000503, SRG-APP-000504, SRG-APP-000505, SRG-APP-000507, SRG-APP-000508, SRG-APP-000509, SRG-APP-000510</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure mechanisms for providing audit record generation capability for DoD-defined auditable events within application components are provided. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]/admin/logs/settings (log on when prompted). Verify the "Log Level" value is set to "VERBOSE". If this value is set to any value other than "VERBOSE", this is a finding.

## Group: SRG-APP-000118

**Group ID:** `V-237324`

### Rule: The ArcGIS Server must protect audit information from any type of unauthorized read access, modification or deletion.

**Rule ID:** `SV-237324r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118, SRG-APP-000119, SRG-APP-000120</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure mechanisms are provided that protect audit information from any type of unauthorized read access, modification or deletion. Substitute the target environment’s values for [bracketed] variables. Within Windows Explorer, access the "Security" (tab) property of the "[C:\arcgisserver]\logs" folder. Verify only the "ArcGIS Server Account" has full control of this folder. Verify any other accounts that have read or other rights to this folder are authorized and documented. If unauthorized accounts have read or other rights to this folder, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-237325`

### Rule: The ArcGIS Server must be configured to disable non-essential capabilities.

**Rule ID:** `SV-237325r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure that non-essential capabilities are disabled. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]admin/system/handlers/rest/servicesdirectory (log on when prompted). Verify that the "Services Directory" property is set to "Disabled". If the "Services Directory" property is set to "Enabled", this is a finding.

## Group: SRG-APP-000142

**Group ID:** `V-237326`

### Rule: The ArcGIS Server must be configured to prohibit or restrict the use of organization-defined functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-237326r879588_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure the application prohibits or restricts the use of PPSM CAL defined ports, protocols, and/or services. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]admin/security/config (log on when prompted). Verify the "Protocol" parameter is not set to "HTTP Only". If the "Protocol" parameter is set to "HTTP Only", this is a finding.

## Group: SRG-APP-000156

**Group ID:** `V-237327`

### Rule: The ArcGIS Server must implement replay-resistant authentication mechanisms for network access to privileged accounts and non-privileged accounts.

**Rule ID:** `SV-237327r879597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. A privileged account is any information system account with authorizations of a privileged user. A non-privileged account is any operating system account with authorizations of a non-privileged user. Satisfies: SRG-APP-000156, SRG-APP-000157, SRG-APP-000295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that the application implements replay-resistant authentication mechanisms for network access to privileged accounts. Substitute the target environment’s values for [bracketed] variables. Within IIS >> within the [“arcgis”] application >> Authentication >> Verify that “Windows Authentication” is “Enabled”. Verify that “Anonymous Authentication” is “Disabled”. If “Windows Authentication” is not enabled, or “Anonymous Authentication” is enabled, this is a finding. Within IIS >> within the [“arcgis”] application >> Authentication >> Select “Windows Authentication” >> “Providers”. Verify “Negotiate” or “Negotate:Kerberos” are at the top of the list, with NTLM at the bottom of the list. If “NTLM” is at the top of the “Providers” list, this is a finding. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000175

**Group ID:** `V-237328`

### Rule: The ArcGIS Server, when using PKI-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-237328r879612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. A trust anchor is an authoritative entity represented via a public key and associated data. It is used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used to for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure PKI-based authenticated endpoints validate certificates by constructing a certification path. Substitute the target environment’s values for [bracketed] variables. 1. On each GIS Server in the ArcGIS Server Site, left-shift + right-click on Internet Explorer >> Run as a different user >> log on using the "[ArcGIS Server]" account. Within Internet Explorer, click Tools >> Internet Options. Open the "Advanced" tab. Within the "Security" section, verify "Check for publisher's certificate revocation" is checked. If "Check for publisher's certificate revocation" is not checked, this is a finding. 2. Within the "Security" section, verify "Check for server certificate revocation" is checked. If "Check for server certificate revocation" is not checked, this is a finding. Access to the "[ArcGIS Server]" account is required to perform this check.

## Group: SRG-APP-000179

**Group ID:** `V-237329`

### Rule: The ArcGIS Server must use mechanisms meeting the requirements of applicable federal laws, Executive orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

**Rule ID:** `SV-237329r879616_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified, and therefore cannot be relied upon to provide confidentiality or integrity and DoD data may be compromised. Applications utilizing encryption are required to use FIPS compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements. Encryption provides a means to secure the remote connection to prevent unauthorized access to the data traversing the remote access connection thereby providing a degree of confidentiality. Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. Satisfies: SRG-APP-000179, SRG-APP-000014, SRG-APP-000219, SRG-APP-000224</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure the application uses mechanisms that meet the requirements of applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]admin/system/handlers/rest/servicesdirectory (logon when prompted.) Browse to “machines” >> [machine name] >> Click “edit”. Verify that the name of the SSL certificate listed in the box for “Web server SSL Certificate” is not set to “SelfSignedCertificate”. If the name of the SSL certificate listed in the box for “Web server SSL Certificate” is set to “SelfSignedCertificate”, this is a finding. Browse to “security” >> “config”. Verify “Protocol” parameter is not set to “HTTP Only”. If the “Protocol” parameter is set to “HTTP Only”, this is a finding. On the local system where the GIS Server is installed, open the “[C:\Program Files\]ArcGIS\Server\framework\runtime\tomcat\conf\server.xml” file. Search for the parameter “ciphers=”. Verify the property of the “ciphers=” parameter is set DoD-approved cipher suite value(s). A list of all possible values is located here: http://www.openssl.org/docs/apps/ciphers.html#CIPHER_SUITE_NAMES. An example of a valid configuration is provided below: <Connector SSLEnabled="true" clientAuth="false" keyAlias=["MyValidCertificate"] keystoreFile=["C:\arcgisserver\config-store\machines\SERVER.DOMAIN.COM\arcgis.keystore"] keystorePass="password" maxThreads="150" port="6443" protocol="org.apache.coyote.http11.Http11Protocol" scheme="https" secure="true" sslProtocol="TLS" ciphers="TLS_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA"/> If the “ciphers” parameter is not found, this is a finding. If the “ciphers” parameter contains any non-DoD-approved ciphers, this is a finding. On each GIS Server system and on each Web Adaptor system, Run the command “rsop” as Administrator on the Windows Command line. Within the “Resultant Set of Policy” results, verify “Computer Configuration” >> “Windows Settings” >> “Security Settings” >> “Local Policies” >> “Security Options” >> “System cryptography: Use FIPS 140 compliant cryptographic algorithms, including encryption, hashing and signing algorithms” is set to “Enabled”. If “System cryptography: Use FIPS 140 compliant cryptographic algorithms, including encryption, hashing and signing algorithms” not set to “Enabled”, this is a finding. This control is not applicable for ArcGIS Servers which are deployed as part of a solution which ensures user web service traffic flows through third-party DoD compliant transport encryption devices (such as a load balancer that supports TLS encryption using DoD-approved certificates.)

## Group: SRG-APP-000223

**Group ID:** `V-237330`

### Rule: The ArcGIS Server must recognize only system-generated session identifiers.

**Rule ID:** `SV-237330r879638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications utilize sessions and session identifiers to control application behavior and user access. If an attacker can guess the session identifier, or can inject or manually insert session information, the session may be compromised. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure the application recognizes only system generated session identifiers. Substitute the target environment’s values for [bracketed] variables. Navigate to [https://server.domain.com/arcgis]/admin/security/config (logon when prompted.) Verify the “User Store Configuration” value = “Type: Windows”. If the “User Store Configuration” value is set to “Type: Built-In”, this is a finding. Verify the “Role Store Configuration” value = “Type: Windows”. If the “Role store Configuration” value is set to “Type: Built-In”, this is a finding. Verify the “Authentication Tier” value is set to “WEB_ADAPTOR”. If the “Authentication Tier” value is set to “GIS_SERVER”, this is a finding. This test requires the account performing the check to have "Administrator" privilege to the ArcGIS for Server site. This check can be performed remotely via HTTPS. This configuration is only valid when ArcGIS for Server has been deployed onto a Windows 2008 or later operating system that is a member of an Active Directory domain that disables identifiers that show more than 35 days of inactivity. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000231

**Group ID:** `V-237331`

### Rule: The ArcGIS Server must use a full disk encryption solution to protect the confidentiality and integrity of all information.

**Rule ID:** `SV-237331r879642_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information at rest refers to the state of information when it is located on a secondary storage device (e.g., disk drive and tape drive) within an organizational information system. Mobile devices, laptops, desktops, and storage devices can be either lost or stolen, and the contents of their data storage (e.g., hard drives and non-volatile memory) can be read, copied, or altered. Applications and application users generate information throughout the course of their application use. This requirement addresses protection of user-generated data, as well as, operating system-specific configuration data. Organizations may choose to employ different mechanisms to achieve confidentiality and integrity protections, as appropriate, in accordance with the security category and/or classification of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure mechanisms that protect the confidentiality and integrity of all information at rest are provided. Substitute the target environment’s values for [bracketed] variables. 1. Log on to https://[server.domain.com]:6443/arcgis/admin/data/items/fileShares ("Primary Site Administrator" account access is required.) Open each "Child Items" entry >> click "Edit". Note the "path" value. For example, "path": "\\[server.domain.com\share". Verify the infrastructure system(s) that supply each path implement FIPS 140-2 compliant encryption at rest, such as through the use of BitLocker full disk encryption. If any infrastructure system(s) that supply each path do not implement FIPS 140-2 compliant encryption at rest, such as through the use of BitLocker full disk encryption, this is a finding. 2. Log on to https://[server.domain.com]:6443/arcgis/admin/data/items/enterpriseDatabases ("Primary Site Administrator" account access is required.) Open each "Child Items" entry >> click "Edit". Note the "info" values "SERVER", "DBCLIENT", and "DATABASE", for example: 'SERVER=dbserver', 'DBCLIENT=sqlserver', 'DATABASE=vtest'; Verify on each "SERVER", "DBCLIENT", and "DATABASE", that these systems implement FIPS 140-2 compliant encryption at rest, such as through the use of SQL Server TDE (Transparent Data Encryption). If any "SERVER", "DBCLIENT", and "DATABASE" do not implement FIPS 140-2 compliant encryption at rest, such as through the use of SQL Server TDE (Transparent Data Encryption), this is a finding.

## Group: SRG-APP-000234

**Group ID:** `V-237332`

### Rule: The ArcGIS Server must be configured such that emergency accounts are never automatically removed or disabled.

**Rule ID:** `SV-237332r879644_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Emergency accounts are administrator accounts which are established in response to crisis situations where the need for rapid account activation is required. Therefore, emergency account activation may bypass normal account authorization processes. If these accounts are automatically disabled, system maintenance during emergencies may not be possible, thus adversely affecting system availability. Emergency accounts are different from infrequently used accounts (i.e., local logon accounts used by system administrators when network or normal logon/access is not available). Infrequently used accounts also remain available and are not subject to automatic termination dates. However, an emergency account is normally a different account which is created for use by vendors or system maintainers. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure emergency accounts are never automatically removed or disabled. Substitute the target environment’s values for [bracketed] variables. Log on to the ArcGIS Server Administrator Directory ([https://[server.domain.com])/arcgis/admin) (log on when promoted) with an account that has administrative access. Navigate to security >> psa. Verify that the Primary Site Administrator account has not been disabled. If the "Primary Site Administrator" account has been disabled, this is a finding.

## Group: SRG-APP-000267

**Group ID:** `V-237333`

### Rule: The ArcGIS Server must reveal error messages only to the ISSO, ISSM, and SA.

**Rule ID:** `SV-237333r879656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can identify the application. Additionally, Personally Identifiable Information (PII) and operational information must not be revealed through error messages to unauthorized personnel or their designated representatives. The structure and content of error messages must be carefully considered by the organization and development team. The extent to which the information system is able to identify and handle error conditions is guided by organizational policy and operational requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure the application reveals error messages only to authorized personnel. Substitute the target environment’s values for [bracketed] variables. 1. Inspect the Security Properties of the [C:\arcgisserver\logs] folder. Verify that the [ArcGIS Server] account has full control of the folder and only authorized personnel have access to the folder. 2. Log on to ArcGIS Server Manager >> Security >> Roles >> Publisher. Verify that only [authorized personnel accounts] are granted this role. 3. Log on to ArcGIS Server Manager >> Security >> Roles >> Administrator (log on when prompted.) Verify that only [authorized personnel accounts] are granted this role. Verify any other accounts that have read or other rights to this folder are authorized and documented. If unauthorized accounts have read or other rights to this folder, this is a finding.

## Group: SRG-APP-000380

**Group ID:** `V-237334`

### Rule: The ArcGIS Server must enforce access restrictions associated with changes to application configuration.

**Rule ID:** `SV-237334r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to provide logical access restrictions associated with changes to application configuration may have significant effects on the overall security of the system. When dealing with access restrictions pertaining to change control, it should be noted that any changes to the hardware, software, and/or firmware components of the information system and/or application can potentially have significant effects on the overall security of the system. Accordingly, only qualified and authorized individuals should be allowed to obtain access to application components for the purposes of initiating changes, including upgrades and modifications. Logical access restrictions include, for example, controls that restrict access to workflow automation, media libraries, abstract layers (e.g., changes implemented into third-party interfaces rather than directly into information systems), and change windows (e.g., changes occur only during specified times, making unauthorized changes easy to discover).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that the application enforces access restrictions associated with changes to application configuration. Substitute the target environment’s values for [bracketed] variables. Logon to ArcGIS Server Manager ([https://server.domain.com/arcgis]/manager]) (logon when prompted) >> “Security” >> “Roles” >> “Administrator” role. Verify that only authorized personnel are listed as members of the “Administrator” role. If unauthorized personnel are members of the “Administrator” role, this is a finding. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000383

**Group ID:** `V-237335`

### Rule: The organization must disable organization-defined functions, ports, protocols, and services within the ArcGIS Server deemed to be unnecessary and/or nonsecure.

**Rule ID:** `SV-237335r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types), organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. Additionally, it is sometimes convenient to provide multiple services from a single component (e.g., email and web services; however, doing so increases risk over limiting the services provided by any one component. To support the requirements and principles of least functionality, the application must support the organizational requirements providing only essential capabilities and limiting the use of ports, protocols, and/or services to only those required, authorized, and approved to conduct official business or to address authorized quality of life issues.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that organization-defined unnecessary or insecure ports, functions, and services are disabled. Substitute the target environment’s values for [bracketed] variables. Using an ArcGIS Server account that is a member of the ArcGIS Server Administrator role, logon to the ArcGIS Server Administrator Directory at https://[server.domain.com:6443]/arcgis/admin. Browse to “security” >> “config”. Verify “Protocol” parameter is not set to “HTTP Only”. If the “Protocol” parameter is set to “HTTP Only”, this is a finding. This control is not applicable for ArcGIS Servers which are deployed as part of a solution which ensures user web service traffic flows through third-party DoD compliant transport encryption devices (such as a load balancer that supports TLS encryption using DoD-approved certificates.)

## Group: SRG-APP-000391

**Group ID:** `V-237336`

### Rule: The ArcGIS Server must accept and electronically verify Personal Identity Verification (PIV) credentials.

**Rule ID:** `SV-237336r879764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems. Satisfies: SRG-APP-000391, SRG-APP-000392</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that the application accepts Personal Identity Verification (PIV) credentials. Substitute the target environment’s values for [bracketed] variables. Within IIS >> within the [“arcgis”] application >> Authentication >> Verify that “Windows Authentication” is “Enabled”. Verify that “Anonymous Authentication” is “Disabled”. If “Windows Authentication” is not enabled, or “Anonymous Authentication” is enabled, this is a finding. Within IIS >> within the [“arcgis”] application >> SSL Settings >> Verify the setting “Client Certificates:” is set to “Accept” or “Require” If “Client Certificates:” is set to “Ignore” this is a finding. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000395

**Group ID:** `V-237337`

### Rule: The ArcGIS Server Windows authentication must authenticate all endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-237337r879768_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. A local connection is any connection with a device communicating without the use of a network. A network connection is any connection with a device that communicates through a network (e.g., local area or wide area network, Internet). A remote connection is any connection with a device communicating through an external network (e.g., the Internet). Because of the challenges of applying this requirement of a large scale, organizations are encouraged to only apply the requirement to those limited number (and type) of devices that truly need to support this capability. Satisfies: SRG-APP-000395, SRG-APP-000317, SRG-APP-000345, SRG-APP-000389, SRG-APP-000390, SRG-APP-000394</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS for Server configuration to ensure that the application authenticates all network connected endpoint devices before establishing any connection. Substitute the target environment’s values for [bracketed] variables. Within IIS >> within the [“arcgis”] application >> Authentication >> Verify that “Windows Authentication” is “Enabled”. Verify that “Anonymous Authentication” is “Disabled”. If “Windows Authentication” is not enabled, or “Anonymous Authentication” is enabled, this is a finding. This control is not applicable for ArcGIS Server deployments configured to allow anonymous access. This control is not applicable for ArcGIS Server deployments which are integrated with and protected by one or more third party DoD compliant certificate authentication solutions.

## Group: SRG-APP-000416

**Group ID:** `V-237338`

### Rule: The ArcGIS Server SSL settings must use NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-237338r879944_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The application must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. Satisfies: SRG-APP-000416, SRG-APP-000439, SRG-APP-000440, SRG-APP-000441, SRG-APP-000442, SRG-APP-000514</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure the application implements NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards. Substitute the target environment’s values for [bracketed] variables. Within IIS >> within the [“arcgis”] application >> SSL Settings >> Verify that “Require SSL” is checked. If “Require SSL” is not checked, this is a finding. Note: To comply with this control, the Active Directory domain on which the ArcGIS Server and the IIS system are deployed must implement policies which enforce FIPS 140-2 compliance. This control is not applicable for ArcGIS Servers which are deployed as part of a solution which ensures user web service traffic flows through third-party DoD compliant transport encryption devices (such as a load balancer that supports TLS encryption using DoD-approved certificates.) This control is not applicable for ArcGIS Servers which are not deployed with the ArcGIS Web Adapter component.

## Group: SRG-APP-000427

**Group ID:** `V-237339`

### Rule: The ArcGIS Server keystores must only contain certificates of PKI established certificate authorities for verification of protected sessions.

**Rule ID:** `SV-237339r879798_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. This requirement focuses on communications protection for the application session rather than for the network packet. This requirement applies to applications that utilize communications sessions. This includes, but is not limited to, web-based applications and Service-Oriented Architectures (SOA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure the application only allows the use of DoD PKI established certificate authorities for verification of the establishment of protected sessions. Substitute the target environment’s values for [bracketed] variables. 1. Use a Java-compatible tool to access the java keystore at [C:\Program Files\ArcGIS\Server\framework\runtime\jre\lib\security\cacerts]. The password for the keystore is "changeit". Verify that the Java Keystore [C:\Program Files\ArcGIS\Server\framework\runtime\jre\lib\security\cacerts] does not contain any non-DoD-approved certificates. If any non-DoD-approved certificate authorities are listed as trusted, this is a finding. 2. Log on to the machine hosting ArcGIS Server. Open Certificate Manager. (You can do this by clicking the "Start" button, typing "certmgr.msc" into the "Search" box, and pressing the "ENTER" key.) In the "Certificate Manager" window, click "Trusted Root Certificate Authorities", then click" Certificates". Verify that the Windows Keystore does not contain any non-DoD-approved certificates. If any non-DoD-approved certificate authorities are listed as trusted, this is a finding. 3. Use a Java-compatible tool to access the Java Keystore at [C:\arcgisserver\config-store\machines\machine_name\arcgis.keystore]. The password is the value of the "password" field within the [C:\arcgisserver\config-store\security\super\super.json] file. Verify that the Java Keystore [C:\arcgisserver\config-store\machines\machine_name\arcgis.keystore] does not contain any non-DoD-approved certificates. If any non-DoD-approved certificate authorities are listed as trusted, this is a finding.

## Group: SRG-APP-000431

**Group ID:** `V-237340`

### Rule: The ArcGIS Server must maintain a separate execution domain for each executing process.

**Rule ID:** `SV-237340r879802_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications can maintain separate execution domains for each executing process by assigning each process a separate address space. Each process has a distinct address space so that communication between processes is performed in a manner controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces. An example is a web browser with process isolation that provides tabs that are separate processes using separate address spaces to prevent one tab crashing the entire browser. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure all published services maintain a separate execution domain for each process. Substitute the target environment’s values for [bracketed] variables. In PowerShell, run the following command, replacing the [bracketed] values with the path of the ArcGIS Server Site "config-store": Get-ChildItem -recurse [C:\arcgisserver\]config-store\services\*.json | Select-String -pattern "`"isolationLevel`": `"LOW`"" If any values are returned, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-237341`

### Rule: The ArcGIS Server must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-237341r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ArcGIS Server configuration to ensure it is deployed onto a Windows 2008 R2 or Windows 2012 R2 Active Directory Member server upon which the Windows Server 2012/2012 R2 Member Server Security Technical Implementation Guide or Windows Server 2008 R2 Member Server Security Technical Implementation Guide has been applied (respectively). If the server on which ArcGIS Server is deployed is not a Windows 2008 R2 or Windows 2012 R2 Active Directory member server which has the Windows Server 2012/2012 R2 Member Server Security Technical Implementation Guide or Windows Server 2008 R2 Member Server Security Technical Implementation Guide has been applied (respectively), this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-257297`

### Rule: The version of ArcGIS running on the system must be a supported version.

**Rule ID:** `SV-257297r919430_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and also to applications themselves that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
ArcGIS 10.3 is no longer supported by the vendor. If the server is running ArcGIS 10.3, this is a finding.

