# STIG Benchmark: IBM Aspera Platform 4.2 Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000333-ALG-000049

**Group ID:** `V-252556`

### Rule: The IBM Aspera Platform must be configured to support centralized management and configuration.

**Rule ID:** `SV-252556r981636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Network components requiring centralized audit log management must have the capability to support centralized management. The DoD requires centralized management of all network component audit record content. This requirement does not apply to audit logs generated on behalf of the device itself (management). Support of centralized management of the IBM Aspera Platform is accomplished via use of IBM Aspera Console.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera Platform is configured to support centralized management and configuration. Navigate to the IBM Aspera Console webpage, login with an administrator account, and review the Nodes tab. If all nodes managed by the organization are not listed, this is a finding. If the IBM Aspera Platform implementation does not include IBM Aspera Console, this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-252557`

### Rule: The IBM Aspera Platform must not have unnecessary services and functions enabled.

**Rule ID:** `SV-252557r817841_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the ALG. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The primary function of an ALG is to provide application specific content filtering and/or proxy services. The ALG application suite may integrate related content filtering and analysis services and tools (e.g., IPS, proxy, malware inspection, black/white lists). Some gateways may also include email scanning, decryption, caching, and DLP services. However, services and capabilities which are unrelated to this primary functionality must not be installed (e.g., DNS, email client or server, FTP server, or web server). Next Generation ALGs (NGFW) and Unified Threat Management (UTM) ALGs integrate functions which have been traditionally separated. These products integrate content filtering features to provide more granular policy filtering. There may be operational drawbacks to combining these services into one device. Another issue is that NGFW and UTM products vary greatly with no current definitive industry standard.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that only mission essential features are in use. Interview the systems administrator to determine if the following Aspera features are in use: Aspera Shares Aspera Faspex If either Aspera Shares or Aspera Faspex are in use and are not documented with the ISSM as a mission requirement, this is a finding.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-252558`

### Rule: IBM Aspera Console must implement multifactor authentication for remote access to non-privileged accounts such that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-252558r981642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password; or the use of a CAC/PIV card and PIN coupled with a password. Satisfies: SRG-NET-000339-ALG-000090, SRG-NET-000340-ALG-000091, SRG-NET-000349-ALG-000106</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser, navigate to the default IBM Aspera Console web page. Use the SAML link and authenticate using known working credentials. If entry of a factor provided by a device separate from the system gaining access is NOT required, this is a finding.

## Group: SRG-NET-000098-ALG-000056

**Group ID:** `V-252559`

### Rule: The IBM Aspera Console must protect audit information from unauthorized read access.

**Rule ID:** `SV-252559r817847_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or to simply identify an improperly configured network element. Thus, it is imperative that the collected log data from the various network elements, as well as the auditing tools, be secured and can only be accessed by authorized personnel. This does not apply to audit logs generated on behalf of the device itself (management). Satisfies: SRG-NET-000098-ALG-000056, SRG-NET-000099-ALG-000057, SRG-NET-000100-ALG-000058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the log files for IBM Aspera Console do not have world access with the following command: $ sudo find /opt/aspera/console/log/ \( -perm -0001 -o -perm -0002 -o -perm -0004 \) -print If results are returned from the above command, this is a finding.

## Group: SRG-NET-000101-ALG-000059

**Group ID:** `V-252560`

### Rule: The IBM Aspera Console must protect audit tools from unauthorized access.

**Rule ID:** `SV-252560r817850_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network elements providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order make access decisions regarding the access to audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This does not apply to audit logs generated on behalf of the device itself (management). Refer to the IBM Aspera Console Admin Guide for data requirements for the SAML assertion including default attribute names, the IBM Aspera Console User Field, and required format within the assertion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser, navigate to the IBM Aspera Console web page. The IBM Aspera Console will automatically redirect to the IdP for authentication if it is configured for SAML authentication. If it does not redirect for authentication via the configured IdP, this is a finding. If redirected to the IdP login page, attempt to authenticate using the IdP with known working credentials to determine if the IdP is providing an appropriate SAML assertion for access.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-252561`

### Rule: IBM Aspera Console must be configured with a preestablished trust relationship and mechanisms with appropriate authorities (e.g., Active Directory or AAA server) which validate user account access authorizations and privileges.

**Rule ID:** `SV-252561r831492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User account and privilege validation must be centralized in order to prevent unauthorized access using changed or revoked privileges. IBM Aspera Console must use an IdP for authentication for security best practices. The IdP must not be installed on the IBM Aspera Console virtual machine, particularly if it resides on the untrusted zone of the Enclave. Refer to the IBM Aspera Console Admin Guide for data requirements for the SAML assertion including default attribute names, the IBM Aspera Console User Field, and required format within the assertion. For security best practices also ensure that the system hosting IBM Aspera Console uses Network Time Protocol or another system to keep times synchronized with the IdP/SAML Provider providing the SAML assertions. Clock drift between The IBM Aspera Console server and the IdP/SAML Provider will result in expired assertions and the inability to be successfully authenticated into IBM Aspera Console. Satisfies: SRG-NET-000138-ALG-000063, SRG-NET-000138-ALG-000088, SRG-NET-000138-ALG-000089, SRG-NET-000140-ALG-000094, SRG-NET-000147-ALG-000095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a web browser, navigate to the IBM Aspera Console web page. IBM Aspera Console will automatically redirect to the IdP for authentication if it is configured for SAML authentication. If it does not redirect for authentication via the configured IdP, this is a finding. If redirected to the IdP login page, attempt to authenticate using the IdP with known working credentials to determine if the IdP is providing an appropriate SAML assertion for access. If unable to log in using known working credentials, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252562`

### Rule: The IBM Aspera Console feature must be configured to use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-252562r817856_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). For implementations using the IBM Aspera Console feature, the default configuration of Console has TLS 1.0 and 1.1 enabled to support older browsers. Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000400-ALG-000097</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console only uses TLS 1.2 or greater with the following command: $ sudo grep SSLProtocol /opt/aspera/common/apache/conf/extra/httpd-ssl.conf SSLProtocol TLSv1.2 If the values for SSLProtocol vary from the above example, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-252563`

### Rule: IBM Aspera Console interactive session must be terminated after 10 minutes of inactivity for non-privileged and privileged sessions.

**Rule ID:** `SV-252563r971530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Satisfies: SRG-NET-000213-ALG-000107, SRG-NET-000517-ALG-000006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console interactive sessions are terminated after 10 minutes of inactivity for non-privileged and privileged sessions: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Security" section. - Verify the "Session timeout" option is set to "10" minutes or less. If the "Session Timeout" option is set to more than "10" minutes, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252564`

### Rule: IBM Aspera Console must enforce password complexity by requiring at least fifteen characters, with at least one upper case letter, one lower case letter, one number, and one symbol.

**Rule ID:** `SV-252564r817862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console enforces password complexity by requiring at least 15 characters, with at least one uppercase letter, one lowercase letter, one number, and one symbol: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Console Password Options" section. - Verify the "Password Requirement Regular Expression" has the following value: (?=.*\d)(?=.*([a-z]))(?=.*([A-Z]))(?=.*(\W|_)).{15,} - Verify the "Password Requirement Message" has the following text: "Passwords must be at least fifteen characters long, with at least one upper case letter, one lower case letter, one number, and one symbol". If the "Password Requirement Regular Expression" value is not "(?=.*\d)(?=.*([a-z]))(?=.*([A-Z]))(?=.*(\W|_)).{15,}", this is a finding. If the "Password Requirement Message" value is not "Passwords must be at least fifteen characters long, with at least one upper case letter, one lower case letter, one number, and one symbol", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252565`

### Rule: IBM Aspera Console must lock accounts after three unsuccessful login attempts within a 15-minute timeframe.

**Rule ID:** `SV-252565r831494_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console locks accounts after three unsuccessful login attempts within a 15-minute timeframe: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Security" section. - Verify the "Deactivate Users" section is set to "3" or less failed login attempts within "15" minutes or less. If the "Deactivate Users" section is set to more than "3" failed login attempts, this is a finding. If the "Deactivate Users" section is set to more than "15" minutes, this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-252566`

### Rule: IBM Aspera Console must prevent concurrent logins for all accounts.

**Rule ID:** `SV-252566r817868_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of current sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be the same as the requirements specified for the application for which it serves as intermediary. This policy only applies to application gateways/firewalls (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console prevents concurrent logins for all accounts: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Security" section. - Verify the "Prevent concurrent login" option is checked. If the "Prevent concurrent login" option is not checked, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252567`

### Rule: IBM Aspera Console passwords must be prohibited from reuse for a minimum of five generations.

**Rule ID:** `SV-252567r817871_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to reuse their password consecutively when that password has exceeded its defined lifetime, the end result is a password that is not changed per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console passwords are prohibited from reuse for a minimum of five generations: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Console Password Options" section. - Verify the "Password Expiration" option is checked. - Verify the "Password Reuse Limit" option is set to "5" or more. If the "Password Expiration" option is not checked, this is a finding. If the "Password Reuse Limit" is set to less than "5" or is set to "0", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252568`

### Rule: IBM Aspera Console user account passwords must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-252568r817874_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the Aspera system does not limit the lifetime of passwords and force users to change update them, there is a risk passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera Console user account passwords have a 60-day maximum password lifetime restriction: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Console Password Options" section. - Verify the "Password Expiration" option is checked. - Verify the "Password Duration" option is set to "60" days or less. If the "Password Expiration" option is not checked, this is a finding. If the "Password Duration" is set to more than "60" days or is set to "0", this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252569`

### Rule: The IBM Aspera Console must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-252569r817877_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The IBM Aspera Console is configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Review the port configurations of the server with the following command: $ sudo /opt/aspera/common/asctl/asctl all:info | grep port: http_port: 80 https_port: 443 port: 4406 base_port: 3500 Ask the system administrator for the site or program PPSM CLSA. Verify the services configured for use match the PPSM Component Local Services Assessment (CLSA). If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-252570`

### Rule: The IBM Aspera Console must be configured to use NIST FIPS-validated cryptography to protect the integrity of file transfers.

**Rule ID:** `SV-252570r831495_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). Satisfies: SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that encryption is required for all transfers by the IBM Aspera Console: - Log in to the IBM Aspera Console web page as a user with administrative privilege. - Select the "Configuration" tab. - Select the "Defaults" tab. - Scroll down to the "Transfer Defaults" section. - Verify that the "Transport Encryption" option is set to "aes-128". If the "Transport Encryption" option is set to "none", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252571`

### Rule: The IBM Aspera Console private/secret cryptographic keys file must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-252571r831496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /opt/aspera/console/config/secret.yml file is group-owned by root with the following command: $ sudo stat -c "%G" /opt/aspera/console/config/secret.yml root If "root" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252572`

### Rule: The IBM Aspera Console private/secret cryptographic keys file must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-252572r831497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /opt/aspera/console/config/secret.yml file is owned by root with the following command: $ sudo stat -c "%U" /opt/aspera/console/config/secret.yml root If "root" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252573`

### Rule: The IBM Aspera Console private/secret cryptographic keys file must have a mode of 0600 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252573r831498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the /opt/aspera/console/config/secret.yml file has a mode of "0600" or less permissive with the following command: $ sudo stat -c "%a %n" /opt/aspera/console/config/secret.yml 600 /opt/aspera/console/config/secret.yml If the resulting mode is more permissive than "0600", this is a finding.

## Group: SRG-NET-000102-ALG-000060

**Group ID:** `V-252574`

### Rule: The IBM Aspera Console feature audit tools must be protected from unauthorized modification or deletion.

**Rule ID:** `SV-252574r817892_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting audit data also includes identifying and protecting the tools used to view and manipulate log data. Therefore, protecting audit tools is necessary to prevent unauthorized operation on audit data. Network elements providing tools to interface with audit data will leverage user permissions and roles identifying the user accessing the tools and the corresponding rights the user enjoys in order to make access decisions regarding the modification of audit tools. Audit tools include, but are not limited to, vendor-provided and open source audit tools needed to successfully view and manipulate audit information system activity and records. Audit tools include custom queries and report generators. This does not apply to audit logs generated on behalf of the device itself (management). Satisfies: SRG-NET-000102-ALG-000060, SRG-NET-000103-ALG-000061</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the world ownership of subdirectories within the /opt/aspera/console directory. Only the "public" subdirectory should have any access outside of the owner or group. sudo find /opt/aspera/console -perm -0002 -exec ls -lLd {} \; If any files or directories have world write permissions, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-252575`

### Rule: IBM Aspera Faspex interactive session must be terminated after 10 minutes of inactivity for non-privileged and privileged sessions.

**Rule ID:** `SV-252575r971530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Satisfies: SRG-NET-000213-ALG-000107, SRG-NET-000517-ALG-000006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex interactive session are terminated after 10 minutes of inactivity for non-privileged and privileged sessions: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Session timeout" option is set to "10" minutes or less. If the "Session timeout" option is set to more than "10" minutes, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252576`

### Rule: The IBM Aspera Faspex private/secret cryptographic keys file must have a mode of 0600 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252576r831500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/faspex/config/secret.yml file has a mode of "0600" or less permissive with the following command: $ sudo stat -c "%a %n" /opt/aspera/faspex/config/secret.yml 600 /opt/aspera/faspex/config/secret.yml If the resulting mode is more permissive than "0600", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252577`

### Rule: IBM Aspera Faspex must allow the use of a temporary password for logins with an immediate change to a permanent password.

**Rule ID:** `SV-252577r831501_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without providing this capability, an account may be created without a password. Non-repudiation cannot be guaranteed once an account is created if a user is not forced to change the temporary password upon initial login. Temporary passwords are typically used to allow access when new accounts are created or passwords are changed. It is common practice for administrators to create temporary passwords for user accounts which allow the users to log in, yet force them to change the password once they have successfully authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex allows the use of a temporary password for logins with an immediate change to a permanent password: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Require new users to change password on first login" option is checked. If the "Require new users to change password on first login" option is not checked, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-252578`

### Rule: IBM Aspera Faspex must be configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-252578r817904_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the network ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the login function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to ALGs (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services. Satisfies: SRG-NET-000041-ALG-000022, SRG-NET-000043-ALG-000024</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Faspex default webpage displays the Standard Mandatory DoD-approved Notice and Consent Banner. Using a web browser, go to the default IBM Aspera Faspex website. If the Standard Mandatory DoD-approved Notice and Consent Banner is not present, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252579`

### Rule: IBM Aspera Faspex must disable account identifiers after 35 days of inactivity.

**Rule ID:** `SV-252579r817907_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications because attackers may exploit an inactive identifier and potentially obtain undetected access to the system. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex disables account identifiers after 35 days of inactivity: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Under the "Faspex accounts" "Remove users" section, verify the following: - Verify the "Local users" option is checked. - Verify the "Local users" options is set to "35" days or less. - Verify the "DS users" option is checked. - Verify the "DS users" options is set to "35" days or less. - Verify the "SAML users" option is checked. - Verify the "SAML users" options is set to "35" days or less. If the "Local users" options is set to more than "35" days or the option is not checked, this is a finding. If the "DS users" options is set to more than "35" days or the option is not checked, this is a finding. If the "SAML users" options is set to more than "35" days or the option is not checked, this is a finding.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-252580`

### Rule: IBM Aspera Faspex must implement multifactor authentication for remote access to non-privileged accounts such that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-252580r981642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password; or the use of a CAC/PIV card and PIN coupled with a password. Satisfies: SRG-NET-000339-ALG-000090, SRG-NET-000340-ALG-000091, SRG-NET-000349-ALG-000106</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Using a web browser, navigate to the default IBM Aspera Faspex web page. Use the SAML link and authenticate using known working credentials. If entry of a factor provided by a device separate from the system gaining access is NOT required, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252581`

### Rule: IBM Aspera Faspex must lock accounts after three unsuccessful login attempts within a 15-minute timeframe.

**Rule ID:** `SV-252581r831503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex locks accounts after three unsuccessful login attempts within a 15-minute timeframe: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Faspex accounts" "Lock users" section is set to "3" or less failed login attempts within "15" minutes or less. If the "Lock users" section is set to more than "3" failed login attempts, this is a finding. If the "Lock users" section is set to more than "15" minutes, this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-252582`

### Rule: IBM Aspera Faspex must prevent concurrent logins for all accounts.

**Rule ID:** `SV-252582r817916_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting the number of current sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be the same as the requirements specified for the application for which it serves as intermediary. This policy only applies to application gateways/firewalls (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex prevents concurrent logins for all accounts: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Faspex accounts" "Prevent concurrent login" option is checked. If the "Prevent concurrent login" is not checked, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252583`

### Rule: IBM Aspera Faspex must require password complexity features to be enabled.

**Rule ID:** `SV-252583r818123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex requires password complexity: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Faspex accounts" "Use strong passwords" option is checked. If the "Use strong passwords" option is not checked, this is a finding. If the "Use strong passwords" option is checked, downgrade this requirement to a CAT III.

## Group: SRG-NET-000169-ALG-000102

**Group ID:** `V-252584`

### Rule: IBM Aspera Faspex must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-252584r818985_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. By identifying and authenticating non-organizational users, their access to network resources can be restricted accordingly. IBM Aspera Faspex external users must register for an account and be authenticated before downloading a package. This authentication is conducted by the IBM Aspera Faspex server using password authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. To ensure that all external recipients of Faspex packages must register for an account before they can download packages or files within packages: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" option from the left menu. - Verify that the option "Require external users to register" is checked. If this option is not checked, this is a finding. Also ensure IBM Aspera Faspex is configured for "Moderated" self-registration when permitting use by external users. To do this, verify the "Moderated" option is selected from the picklist for "Self registration" under the Registrations heading. If this option is not checked, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252585`

### Rule: IBM Aspera Faspex passwords must be prohibited from reuse for a minimum of five generations.

**Rule ID:** `SV-252585r817925_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. If the information system or application allows the user to reuse their password consecutively when that password has exceeded its defined lifetime, the end result is a password that is not changed per policy requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex passwords are prohibited from reuse for a minimum of five generations: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Faspex accounts" "Prevent passwords reuse" option is checked. - Verify the "Faspex accounts" "Prevent passwords reuse" options is set to "5" or more. If the "Prevent passwords reuse" options is less than "5" or the option is not checked, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252586`

### Rule: IBM Aspera Faspex user account passwords must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-252586r817928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the Aspera system does not limit the lifetime of passwords and force users to change update them, there is a risk passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex user account passwords have a 60-day maximum password lifetime restriction: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section. - Verify the "Faspex accounts" "Passwords expire" option is checked. - Verify the "Faspex accounts" "Passwords expire" options is set to "60" days or less. If the "Passwords expire" options is set to more than "60" days or the option is not checked, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252587`

### Rule: The IBM Aspera Faspex feature must be configured to use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-252587r817931_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). For implementations using the IBM Aspera Faspex feature, the default configuration of Faspex has TLS 1.0, 1.1 and 1.2 enabled to support older browsers. Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000400-ALG-000097</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Faspex only uses TLS 1.2 or greater with the following command: $ sudo grep SSLProtocol /opt/aspera/common/apache/conf/extra/httpd-ssl.conf SSLProtocol TLSv1.2 If the values for SSLProtocol vary from the above example, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252588`

### Rule: IBM Aspera Faspex must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-252588r817934_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. The IBM Aspera Faspex is configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Review the port configurations of the server with the following command: $ sudo /opt/aspera/common/asctl/asctl all:info | grep port: http_port: 80 https_port: 443 port: 4406 base_port: 3000 http_fallback_port:8080 Ask the system administrator for the site or program PPSM CLSA. Verify the services configured for use match the PPSM Component Local Services Assessment (CLSA). If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-252589`

### Rule: IBM Aspera Faspex must be configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-252589r831504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway. IBM Aspera Faspex will list preestablished trust relationships for IdPs on the default Faspex login page. This configuration supports the ability to have more than one preestablished trust relationship, and it requires the user to choose from the valid preestablished IdPs as listed on the default web page. If IBM Aspera Faspex is configured to automatically redirect to a single IdP, visiting the default webpage will do so. Refer to the IBM Aspera Faspex Admin Guide for data requirements for the SAML assertion including default attribute names, the IBM Faspex User Field, and required format within the assertion. For security best practices, also ensure that the system hosting Aspera Faspex uses Network Time Protocol or another system to keep times synchronized with the IdP server providing the SAML assertions. Clock drift between the IBM Aspera Faspex server and the IdP/SAML Provider will result in expired assertions and the inability to be successfully authenticated into IBM Aspera Faspex. Satisfies: SRG-NET-000138-ALG-000063, SRG-NET-000138-ALG-000088, SRG-NET-000138-ALG-000089, SRG-NET-000140-ALG-000094, SRG-NET-000147-ALG-000095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Using a web browser, navigate to the default IBM Aspera Faspex web page. If you are neither redirected to an IdP nor provided with a list of one or more IdPs to choose from on the standard IBM Aspera Faspex webpage, this is a finding. If redirected to the IdP login, attempt to authenticate using the IdP with known working credentials to determine if the IdP is providing an appropriate SAML assertion for access. If unable to log in using known working credentials, this is a finding. If not redirected to a single IdP but provided a list of configured IdPs, choose one for authentication with known working credentials to determine if the IdP is providing an appropriate SAML assertion for access. If unable to log in using known working credentials, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-252590`

### Rule: IBM Aspera Faspex must be configured to use NIST FIPS-validated cryptography to protect the integrity of file transfers.

**Rule ID:** `SV-252590r831505_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). Satisfies: SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Ensure that encryption is required for all transfers by the IBM Aspera Faspex: - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section from the left menu. - Scroll down to the "Encryption" section. - Verify that the "Encrypt transfers" option is checked. If the "Encrypt transfers" option is not checked, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252591`

### Rule: IBM Aspera Faspex must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-252591r831506_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Faspex implements cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection. - Log in to the IBM Aspera Faspex web page as a user with administrative privilege. - Select the "Server" tab. - Select the "Configuration" tab. - Select the "Security" section from the left menu. - Scroll down to the "Encryption" section. - Verify that the "Use encryption-at-rest" radio button is set to "Always". If the "Use encryption-at-rest" radio button is set to "Never" or "Optional", this is a finding.

## Group: SRG-NET-000098-ALG-000056

**Group ID:** `V-252592`

### Rule: IBM Aspera Faspex must protect audit information from unauthorized modification.

**Rule ID:** `SV-252592r817946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions, and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This does not apply to audit logs generated on behalf of the device itself (management). Satisfies: SRG-NET-000098-ALG-000056, SRG-NET-000099-ALG-000057, SRG-NET-000100-ALG-000058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify that the log files for IBM Aspera Faspex have no world access. $ sudo find /opt/aspera/faspex/log/ \( -perm -0001 -o -perm -0002 -o -perm -0004 \) -print If results are returned from the above command, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252593`

### Rule: The IBM Aspera Faspex private/secret cryptographic keys file must be group-owned by faspex to prevent unauthorized read access.

**Rule ID:** `SV-252593r831507_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/faspex/config/secret.yml file is group-owned by faspex with the following command: $ sudo stat -c "%G" /opt/aspera/faspex/config/secret.yml faspex If "faspex" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252594`

### Rule: The IBM Aspera Faspex private/secret cryptographic keys file must be owned by faspex to prevent unauthorized read access.

**Rule ID:** `SV-252594r831508_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/faspex/config/secret.yml file is owned by faspex with the following command: $ sudo stat -c "%U" /opt/aspera/faspex/config/secret.yml faspex If "faspex" is not returned as a result, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252595`

### Rule: The IBM Aspera Faspex Server must restrict users from using transfer services by default.

**Rule ID:** `SV-252595r817955_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. IBM Aspera High Speed Transfer Server and IBM Aspera High Speed Transfer Endpoint inherently use file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Faspex restricts users from using transfer services by default with the following commands: Check that the aspera.conf file is configured to deny transfer in and out by default. $ sudo /opt/aspera/bin/asuserdata -a | grep authorization | grep value authorization_transfer_in_value: "deny" authorization_transfer_out_value: "deny" If the results produce an "allow" value, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252596`

### Rule: The IBM Aspera Faspex Server must restrict users read, write, and browse permissions by default.

**Rule ID:** `SV-252596r817958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. IBM Aspera High Speed Transfer Server and IBM Aspera High Speed Transfer Endpoint inherently use file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Faspex feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Faspex restricts users read, write, and browse permissions by default with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep -w 'read_allowed\|write_allowed\|dir_allowed' read_allowed: "false" write_allowed: "false" dir_allowed: "false" If no results are returned or if the results produce a "true" value, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-252597`

### Rule: The IBM Aspera Shares interactive session must be terminated after 10 minutes of inactivity for non-privileged and privileged sessions.

**Rule ID:** `SV-252597r971530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Satisfies: SRG-NET-000213-ALG-000107, SRG-NET-000517-ALG-000006</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Shares interactive session are terminated after 10 minutes of inactivity for non-privileged and privileged sessions: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "Security" section. - Select the "User Security" option. - Verify the "Session timeout" option is set to "10" minutes or less. If the "Session timeout" option is set to more than "10" minutes, this is a finding.

## Group: SRG-NET-000041-ALG-000022

**Group ID:** `V-252598`

### Rule: IBM Aspera Shares must be configured to display the Standard Mandatory DoD-approved Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-252598r817964_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible network element ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via login interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to network elements that have the concept of a user account and have the login function residing on the network element. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for network elements that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." This policy only applies to gateways (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services offloaded from the application. Publicly access systems are used in DoD to provide benefit information, pay information, or public services. There may also be self-registration and authorization services provided by these gateways. Satisfies: SRG-NET-000041-ALG-000022, SRG-NET-000043-ALG-000024</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Shares default webpage displays the Standard Mandatory DoD-approved Notice and Consent Banner. Using a web browser, go to the default IBM Aspera Shares website. If the Standard Mandatory DoD-approved Notice and Consent Banner is not present, this is a finding.

## Group: SRG-NET-000339-ALG-000090

**Group ID:** `V-252599`

### Rule: IBM Aspera Shares must implement multifactor authentication for remote access to non-privileged accounts such that one of the factors is provided by a device separate from the system gaining access.

**Rule ID:** `SV-252599r981642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For remote access to non-privileged accounts, the purpose of requiring a device that is separate from the information system gaining access for one of the factors during multifactor authentication is to reduce the likelihood of compromising authentication credentials stored on the system. Multifactor solutions that require devices separate from information systems gaining access include, for example, hardware tokens providing time-based or challenge-response authenticators and smart cards such as the U.S. Government Personal Identity Verification card and the DoD common access card. A privileged account is defined as an information system account with authorizations of a privileged user. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. An example of compliance with this requirement is the use of a one-time password token and PIN coupled with a password; or the use of a CAC/PIV card and PIN coupled with a password. Satisfies: SRG-NET-000339-ALG-000090, SRG-NET-000340-ALG-000091, SRG-NET-000349-ALG-000106</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Using a web browser, navigate to the default IBM Aspera Shares web page. Use the SAML link and authenticate using known working credentials. If entry of a factor provided by a device separate from the system gaining access is NOT required, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252600`

### Rule: IBM Aspera Shares must lock accounts after three unsuccessful login attempts within a 15-minute timeframe.

**Rule ID:** `SV-252600r831511_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute-forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Shares locks accounts after three unsuccessful login attempts within a 15-minute timeframe: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "Security" section. - Select the "User Security" option. - Verify the "Failed login count" is set to "3" or less. - Verify the "Failed login interval" is set to "15" or less. If the "Failed login count" is set to more than "3", this is a finding. If the "Failed login interval" is set to more than "15" minutes, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252601`

### Rule: IBM Aspera Shares must require password complexity features to be enabled.

**Rule ID:** `SV-252601r817973_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Shares requires password complexity: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "Security" section. - Select the "User Security" option. - Verify the "Require strong passwords" option is checked. If the "Require strong passwords" option is not checked, this is a finding. If the "Require strong passwords" option is checked, downgrade this requirement to a CAT III.

## Group: SRG-NET-000169-ALG-000102

**Group ID:** `V-252602`

### Rule: IBM Aspera Shares must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-252602r817976_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication enables anyone to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. By identifying and authenticating non-organizational users, their access to network resources can be restricted accordingly. IBM Aspera Faspex external users must register for an account and be authenticated before downloading a package. This authentication is conducted by the IBM Aspera Faspex server using password authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. To ensure that all external recipients of Shares packages must register for an account before they can download packages or files within packages: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "Security" section. - Select the "User Security" option from the left menu. - Verify that the "Self Registration" option is set to "Moderated" or "None". If the "Self Registration" option is set to "Unmoderated", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252603`

### Rule: IBM Aspera Shares user account passwords must have a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-252603r817979_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed periodically. If the Aspera system does not limit the lifetime of passwords and force users to change update them, there is a risk passwords could be compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Shares user account passwords have a 60-day maximum password lifetime restriction: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "Security" section. - Select the "User Security" option. - Verify the "Password expiration interval" is set to "60" or less. If the "Password expiration interval" is greater than "60" or is blank, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252604`

### Rule: The IBM Aspera Shares feature must be configured to use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-252604r817982_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). For implementations using the IBM Aspera Shares feature, the default nginx configuration of Shares has TLS 1.0, 1.1 and 1.2 enabled to support older browsers. Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000400-ALG-000097</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify IBM Aspera Shares only uses TLS 1.2 or greater with the following command: $ sudo grep ssl_protocols /opt/aspera/shares/etc/nginx/nginx.conf ssl_protocols TLSv1.2; If the results of the command display versions below "TLSv1.2", this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252605`

### Rule: IBM Aspera Shares must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-252605r817985_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. The IBM Aspera Shares is configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Review the port configurations of the server with the following command: $ sudo cat /opt/aspera/shares/etc/nginx/nginx.conf | grep listen listen 80; listen [::]:80; listen 443; listen [::]:443; Ask the system administrator for the site or program PPSM CLSA. Verify the services configured for use match the PPSM Component Local Services Assessment (CLSA). If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-252606`

### Rule: IBM Aspera Shares must be configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-252606r831512_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway. Refer to the IBM Aspera Shares Admin Guide for data requirements for the SAML assertion including default attribute names, the IBM Aspera Shares User Field, and required format within the assertion. For security best practices, also ensure that the system hosting IBM Aspera Shares uses Network Time Protocol or another system to keep times synchronized with the IdP/SAML Provider providing the SAML assertions. Clock drift between The IBM Aspera Shares server and the IdP/SAML Provider will result in expired assertions and the inability to be successfully authenticated into IBM Aspera Shares. Satisfies: SRG-NET-000138-ALG-000063, SRG-NET-000138-ALG-000088, SRG-NET-000138-ALG-000089, SRG-NET-000140-ALG-000094, SRG-NET-000147-ALG-000095</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Using a web browser, navigate to the default IBM Aspera Shares web page. Attempt to authenticate using the IdP provided under "SAML" heading of login page with known working credentials to determine if the IdP is providing an appropriate SAML assertion for access. If unable to log in using known working credentials, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-252607`

### Rule: IBM Aspera Shares feature must be configured to use NIST FIPS-validated cryptography to protect the integrity of file transfers.

**Rule ID:** `SV-252607r831513_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). Satisfies: SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Ensure that encryption is required for all transfers by the IBM Aspera Shares: - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "System Settings" section. - Select the "Transfers" option. - Verify the "Encryption" option is set to at least "AES-128". If the "Encryption" option is set to "optional" or not set, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252608`

### Rule: IBM Aspera Shares must implement cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection.

**Rule ID:** `SV-252608r831514_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify the IBM Aspera Shares implements cryptographic mechanisms to prevent unauthorized disclosure or modification of all information that requires at rest protection. - Log in to the IBM Aspera Shares web page as a user with administrative privilege. - Select the "Admin" tab. - Scroll down to the "System Settings" section. - Select the "Transfers" option. - Verify the "Encryption at rest" option is set to "Required". If the "Encryption at rest" option is set to "Optional" or is not set, this is a finding.

## Group: SRG-NET-000098-ALG-000056

**Group ID:** `V-252609`

### Rule: IBM Aspera Shares must protect audit information from unauthorized deletion.

**Rule ID:** `SV-252609r817997_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then forensic analysis and discovery of the true source of potentially malicious system activity is impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This requirement can be achieved through multiple methods, which will depend upon system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions, and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This requirement does not apply to audit logs generated on behalf of the device itself (device management). Satisfies: SRG-NET-000098-ALG-000056, SRG-NET-000099-ALG-000057, SRG-NET-000100-ALG-000058</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify that the log files for IBM Aspera Shares have no world access. $ sudo find /opt/aspera/shares/u/stats-collector/var/log \( -perm -0001 -o -perm -0002 -o -perm -0004 \) -print $ sudo find /opt/aspera/shares/u/shares/log \( -perm -0001 -o -perm -0002 -o -perm -0004 \) -print $ sudo find /opt/aspera/shares/var/log \( -perm -0001 -o -perm -0002 -o -perm -0004 \) -print If results are returned from the above commands, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252610`

### Rule: The IBM Aspera Shares private/secret cryptographic keys file must be group-owned by nobody to prevent unauthorized read access.

**Rule ID:** `SV-252610r831515_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/shares/u/shares/config/aspera/secret.rb file is group-owned by nobody with the following command: $ sudo stat -c "%G" /opt/aspera/shares/u/shares/config/aspera/secret.rb nobody If "nobody" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252611`

### Rule: The IBM Aspera Shares private/secret cryptographic keys file must be owned by nobody to prevent unauthorized read access.

**Rule ID:** `SV-252611r831516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/shares/u/shares/config/aspera/secret.rb file is owned by nobody with the following command: $ sudo stat -c "%U" /opt/aspera/shares/u/shares/config/aspera/secret.rb nobody If "nobody" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252612`

### Rule: The IBM Aspera Shares private/secret cryptographic keys file must have a mode of 0400 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252612r831517_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the IBM Aspera Shares feature of the Aspera Platform is not installed, this is Not Applicable. Verify the /opt/aspera/shares/u/shares/config/aspera/secret.rb file has a mode of "0400" or less permissive with the following command: $ sudo stat -c "%a %n" /opt/aspera/shares/u/shares/config/aspera/secret.rb 400 /opt/aspera/shares/u/shares/config/aspera/secret.rb If the resulting mode is more permissive than "0400", this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-252613`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-252613r818009_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol thus are in scope for this requirement. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera High-Speed Transfer Endpoint only uses TLS 1.2 or greater with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep ssl_protocol ssl_protocol: "tlsv1.2" ssl_protocol: "tlsv1.2" If both entries do not return "tlsv1.2" or greater , this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252614`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-252614r818012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The IBM Aspera High-Speed Transfer Endpoint is configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Review the port configurations of the HSTE with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep port: transfer_protocol_options_bind_udp_port: "33001" trunk_mcast_port: "0" trunk_mcast_port: "0" port: "4406" port: "40001" mgmt_port: "0" http_port: "8080" https_port: "8443" http_port: "9091" https_port: "9092" ssh_port: "33001" db_port: "31415" scalekv_sstore_port: "31415" scalekv_baseport: "43001" aej_port: "0" rproxy_rules_rule_proxy_port: "33001" initd_db_port: "31416" wss_port: "9093" Ask the system administrator for the site or program PPSM CLSA. Verify the services configured for use match the PPSM Component Local Services Assessment (CLSA). If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-252615`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must be configured to protect the authenticity of communications sessions.

**Rule ID:** `SV-252615r818015_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For implementations using IBM Aspera High-Speed Transfer Endpoint, check for a <ssh_host_key_fingerprint> entry within the <server> section within The IBM Aspera High-Speed Transfer Endpoint installation configuration file at /opt/aspera/etc/aspera.conf using the following command: $ sudo more /opt/aspera/etc/aspera.conf | grep ssh_host_key_fingerprint If the command does not return XML containing the fingerprint, this is a finding. Test that the certificates used by Aspera Node service is a valid signed certificate (not self signed) by running the following command after substituting the FQDN for "servername": $ sudo /opt/aspera/bin/openssl s_client -connect servername:9092 If the certificate is not DoD issued, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252616`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must be configured to use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-252616r831518_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that FIPS compliance is required for all transfers by the IBM Aspera High-Speed Transfer Endpoint with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep fips transfer_encryption_fips_mode: "true" If results are blank or fips mode is reported as "false", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252617`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must enable content protection for each transfer user by encrypting passphrases used for server-side encryption at rest (SSEAR).

**Rule ID:** `SV-252617r831519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. The askmscli tool sets content-protection secrets only for each user, not for groups and not for all users on a node. Each transfer user requires their own content-protection secret for SSEAR.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint enables content protection for each transfer user by encrypting passphrases used for SSEAR with the following command: $ sudo /opt/aspera/bin/askmcli -u <transferuser> -H ssear v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 If the command returns "No records found for ssear", this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252618`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must enable password protection of the node database.

**Rule ID:** `SV-252618r818024_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. System administrators can set a secure password for clients to authenticate with a Redis database. When the authorization layer is enabled, Redis refuses any query by unauthenticated clients. A client can authenticate itself by sending the AUTH command followed by the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint enables password protection of the node database with the following commands: Initiate a cli connection to the node database. $ sudo /opt/aspera/bin/asredis -p 31415 127.0.0.1:31415> Type "info" in the cli to attempt to query the database. 127.0.0.1:31415>info NOAUTH Authentication required. If the command results do not state "Authentication required", this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-252619`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must have a master-key set to encrypt the dynamic token encryption key.

**Rule ID:** `SV-252619r831520_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. The master key must be a unique random 256-bit key. The example below uses openssl to generate the key. This Redis master key will be used to encrypt the dynamic token encryption key. Satisfies: SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint has a master-key set to encrypt the dynamic token encryption key with the following commands: $ sudo /opt/aspera/bin/askmcli -u <transferuser> -H Redis-master-key v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 $ sudo /opt/aspera/bin/askmcli -u asperadaemon -H Redis-master-key v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 If either command returns "No records found for Redis-master-key", this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-252620`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-252620r818030_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network element management includes the ability to control the number of users and user sessions that utilize a network element. Limiting the number of current sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be the same as the requirements specified for the application for which it serves as intermediary. This policy only applies to application gateways/firewalls (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services. The number of incoming transfer requests to the IBM Aspera High-Speed Transfer Endpoints permitted via a POST to the REST service can be limited by the setting of "transfer_manager_max_concurrent_sessions" in The IBM Aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Endpoint limits the number of concurrent sessions to an organization-defined number for all accounts and/or account types with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep concurrent transfer_manager_max_concurrent_sessions: "20" If the value returned (in this example 20 is the default) is not an organization-defined number, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252621`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must not store group content-protection secrets in plain text.

**Rule ID:** `SV-252621r831521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that you do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint does not store group content-protection secrets in plain text. For each group, run the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -g <groupname> | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252622`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must not store node content-protection secrets in plain text.

**Rule ID:** `SV-252622r831522_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that you do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint does not store node content-protection secrets in plain text with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252623`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must not store user content-protection secrets in plain text.

**Rule ID:** `SV-252623r831523_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that you do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Endpoint does not store user content-protection secrets in plain text. For each user, run the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -u <username> | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252624`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must restrict users from using transfer services by default.

**Rule ID:** `SV-252624r818042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. The IBM Aspera High Speed Transfer Endpoint inherently uses file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Endpoint restricts users from using transfer services by default with the following commands: Check that the aspera.conf file is configured to deny transfer in and out by default. $ sudo /opt/aspera/bin/asuserdata -a | grep authorization | grep value authorization_transfer_in_value: "deny" authorization_transfer_out_value: "deny" If the results produce an "allow" value, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252625`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must restrict users read, write, and browse permissions by default.

**Rule ID:** `SV-252625r818045_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. The IBM Aspera High Speed Transfer Endpoint inherently uses file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Endpoint restricts users read, write, and browse permissions by default with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep -w 'read_allowed\|write_allowed\|dir_allowed' read_allowed: "false" write_allowed: "false" dir_allowed: "false" If no results are returned or if the results produce a "true" value, this is a finding.

## Group: SRG-NET-000344-ALG-000098

**Group ID:** `V-252626`

### Rule: The IBM Aspera High-Speed Transfer Endpoint must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-252626r831524_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the cached authenticator information is out of date, the validity of the authentication information may be questionable. This requirement applies to all ALGs that may cache user authenticators for use throughout a session. It also applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Endpoint prohibits the use of cached authenticators after an organization-defined time period with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep 'token_life' token_life_seconds: "86400" Note: The example token life is for one day; this number must be defined by the organization. If no result is returned or if the result is not an organization-defined time period, this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-252627`

### Rule: The IBM Aspera High-Speed Transfer Server must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-252627r818051_rule`
**Severity:** high

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol thus are in scope for this requirement. NIST SP 800-52 specifies the preferred configurations for government systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IBM Aspera High-Speed Transfer Server only uses TLS 1.2 or greater with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep ssl_protocol ssl_protocol: "tlsv1.2" ssl_protocol: "tlsv1.2" If both entries do not return "tlsv1.2" or greater , this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252628`

### Rule: The IBM Aspera High-Speed Transfer Server must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-252628r818054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The ALG is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The IBM Aspera High-Speed Transfer Server is configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments. Review the port configurations of the HSTS with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep port: transfer_protocol_options_bind_udp_port: "33001" trunk_mcast_port: "0" trunk_mcast_port: "0" port: "4406" port: "40001" mgmt_port: "0" http_port: "8080" https_port: "8443" http_port: "9091" https_port: "9092" ssh_port: "33001" db_port: "31415" scalekv_sstore_port: "31415" scalekv_baseport: "43001" aej_port: "0" rproxy_rules_rule_proxy_port: "33001" initd_db_port: "31416" wss_port: "9093" Ask the system administrator for the site or program PPSM CLSA. Verify the services configured for use match the PPSM Component Local Services Assessment (CLSA). If there are any additional ports, protocols, or services that are not included in the PPSM CLSA, this is a finding. If there are any ports, protocols, or services that are prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-252629`

### Rule: The IBM Aspera High-Speed Transfer Server must be configured to protect the authenticity of communications sessions.

**Rule ID:** `SV-252629r818057_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For implementations using IBM Aspera High-Speed Transfer Server, check for a <ssh_host_key_fingerprint> entry within the <server> section within The IBM Aspera High-Speed Transfer Server installation configuration file at /opt/aspera/etc/aspera.conf using the following command: $ sudo more /opt/aspera/etc/aspera.conf | grep ssh_host_key_fingerprint If the command does not return XML containing the fingerprint, this is a finding. Test that the certificates used by Aspera Node service is a valid signed certificate (not self signed) by running the following command after substituting the FQDN for "servername": $ sudo /opt/aspera/bin/openssl s_client -connect servername:9092 If the certificate is not DoD issued, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252630`

### Rule: The IBM Aspera High-Speed Transfer Server must be configured to use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-252630r831525_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway). Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure that FIPS compliance is required for all transfers by the IBM Aspera High-Speed Transfer Server with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep fips transfer_encryption_fips_mode: "true" If results are blank or fips mode is reported as "false", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252631`

### Rule: The IBM Aspera High-Speed Transfer Server must configure the SELinux context type to allow the "aspshell".

**Rule ID:** `SV-252631r831526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without verification of the security functions, security functions may not operate correctly and the failure may go unnoticed. Security function is defined as the hardware, software, and/or firmware of the information system responsible for enforcing the system security policy and supporting the isolation of code and data on which the protection is based. Security functionality includes, but is not limited to, establishing system accounts, configuring access authorizations (i.e., permissions, privileges), setting events to be audited, and setting intrusion detection parameters.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera HSTS configures the SELinux context type for "aspshell" with the following commands: $ sudo ls -l /bin/aspshell lrwxrwxrwx. 1 root root 24 Sep 1 17:38 /bin/aspshell -> /opt/aspera/bin/aspshell If /bin/aspshell is not simlinked to /opt/aspera/bin/aspshell, this is a finding. $ sudo ls -Z /opt/aspera/bin/aspshell -rwxr-xr-x. root root system_u:object_r:shell_exec_t:S0 /bin/aspshell If the context type of "/opt/aspera/bin/aspshell" is not "shell_exec_t", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252632`

### Rule: The IBM Aspera High-Speed Transfer Server must enable content protection for each transfer user by encrypting passphrases used for server-side encryption at rest (SSEAR).

**Rule ID:** `SV-252632r831527_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. The askmscli tool sets content-protection secrets only for each user, not for groups and not for all users on a node. Each transfer user requires their own content-protection secret for SSEAR.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server enables content protection for each transfer user by encrypting passphrases used for SSEAR with the following command: $ sudo /opt/aspera/bin/askmcli -u <transferuser> -H ssear v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 If the command returns "No records found for ssear", this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252633`

### Rule: The IBM Aspera High-Speed Transfer Server must enable password protection of the node database.

**Rule ID:** `SV-252633r818069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. System administrators can set a secure password for clients to authenticate with a Redis database. When the authorization layer is enabled, Redis refuses any query by unauthenticated clients. A client can authenticate itself by sending the AUTH command followed by the password.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server enables password protection of the node database with the following commands: Initiate a cli connection to the node database. $ sudo /opt/aspera/bin/asredis -p 31415 127.0.0.1:31415> Type "info" in the cli to attempt to query the database. 127.0.0.1:31415>info NOAUTH Authentication required. If the command results do not state "Authentication required", this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-252634`

### Rule: The IBM Aspera High-Speed Transfer Server must enable the use of dynamic token encryption keys.

**Rule ID:** `SV-252634r818072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. The dynamic token encryption key is used for encrypting authorization tokens dynamically for improved security and time-limited validity which limits the chances of a key becoming compromised. NOTE: A dynamic token encryption key can be set for an individual user or a system group. Satisfies: SRG-NET-000062-ALG-000011, SRG-NET-000400-ALG-000097</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server enables the use of dynamic token encryption keys with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep dynamic token_dynamic_key: "true" If the "dynamic_key" setting is not set to "true", this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-252635`

### Rule: The IBM Aspera High-Speed Transfer Server must have a master-key set to encrypt the dynamic token encryption key.

**Rule ID:** `SV-252635r831528_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. The master key must be a unique random 256-bit key. The example below uses openssl to generate the key. This Redis master key will be used to encrypt the dynamic token encryption key. Satisfies: SRG-NET-000063-ALG-000012, SRG-NET-000510-ALG-000025, SRG-NET-000510-ALG-000111</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server has a master-key set to encrypt the dynamic token encryption key with the following commands: $ sudo /opt/aspera/bin/askmcli -u <transferuser> -H Redis-master-key v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 $ sudo /opt/aspera/bin/askmcli -u asperadaemon -H Redis-master-key v0: (SHA-512) 6fcb5c284590f67af12334cf27f94a6dc5fb2f27627b9ba8dc20c210df3edd7a596cd3c9961a5c36bfd8e57a9ae15a6859559f8e11c3059704859cabb59d8340 If either command returns "No records found for Redis-master-key", this is a finding.

## Group: SRG-NET-000053-ALG-000001

**Group ID:** `V-252636`

### Rule: The IBM Aspera High-Speed Transfer Server must limit the number of concurrent sessions to an organization-defined number for all accounts and/or account types.

**Rule ID:** `SV-252636r818078_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network element management includes the ability to control the number of users and user sessions that utilize a network element. Limiting the number of current sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions must be the same as the requirements specified for the application for which it serves as intermediary. This policy only applies to application gateways/firewalls (e.g., identity management or authentication gateways) that provide user account services as part of the intermediary services. The number of incoming transfer requests to the IBM Aspera High-Speed Transfer Server permitted via a POST to the REST service can be limited by the setting of "transfer_manager_max_concurrent_sessions" in The IBM Aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Server limits the number of concurrent sessions to an organization-defined number for all accounts and/or account types with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep concurrent transfer_manager_max_concurrent_sessions: "20" If the value returned (in this example 20 is the default) is not the organization-defined number, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252637`

### Rule: The IBM Aspera High-Speed Transfer Server must not store group content-protection secrets in plain text.

**Rule ID:** `SV-252637r831529_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that you do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server does not store group content-protection secrets in plain text. For each group, run the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -g <groupname> | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252638`

### Rule: The IBM Aspera High-Speed Transfer Server must not store node content-protection secrets in plain text.

**Rule ID:** `SV-252638r831530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that users do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server does not store node content-protection secrets in plain text with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252639`

### Rule: The IBM Aspera High-Speed Transfer Server must not store user content-protection secrets in plain text.

**Rule ID:** `SV-252639r831531_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for network traffic management configurations. Aspera recommends that users do not store content-protection secrets in aspera.conf.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM High-Speed Transfer Server does not store user content-protection secrets in plain text. For each user, run the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -u <username> | grep secret | grep transfer transfer_encryption_content_protection_secret: "AS_NULL" If the "transfer_encryption_content_protection_secret" is not "AS_NULL", this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252640`

### Rule: The IBM Aspera High-Speed Transfer Server must not use the root account for transfers.

**Rule ID:** `SV-252640r818090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By incorporating a least privilege approach to the configuration of the Aspera HSTS platform, this will reduce the exposure of privileged accounts. By default, all system users can establish a FASP connection and are only restricted by file permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server restricts the use of the root account for transfers with the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -u root | grep allowed | grep true If results are returned from the above command, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252641`

### Rule: The IBM Aspera High-Speed Transfer Server must restrict Aspera transfer users to a limited part of the server's file system.

**Rule ID:** `SV-252641r818093_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By restricting the transfer users to a limited part of the server's file system, this prevents unauthorized data transfers. By default, all system users can establish a FASP connection and are only restricted by file permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server restricts Aspera transfer users to a limited part of the server's file system. Check that each user is restricted to a specific transfer folder with the following command: Warning: If an invalid user/group name is entered, the asuserdata command will return results that may appear accurate. Ensure that the user/group name is valid and entered into the command correctly. $ sudo /opt/aspera/bin/asuserdata -u <username> | grep absolute canonical_absolute: "<specifictranferfolder>" absolute: "<sepcifictransferfolder>" If the transfer user's docroot is set to "<Empty String>" or is blank, this is a finding.

## Group: SRG-NET-000138-ALG-000063

**Group ID:** `V-252642`

### Rule: The IBM Aspera High-Speed Transfer Server must restrict the transfer user(s) to the "aspshell".

**Rule ID:** `SV-252642r818096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, all system users can establish a FASP connection and are only restricted by file permissions. Restrict the user's file operations by assigning them to use aspshell, which permits only the following operations: Running Aspera uploads and downloads to or from this computer. Establishing connections in the application. Browsing, listing, creating, renaming, or deleting contents. To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. 1) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication. 2) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement applies to ALGs that provide user proxy services, including identification and authentication. This service must use the site's directory service (e.g., Active Directory). Directory services must not be installed onto the gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server restricts the transfer user(s) to the "aspshell" with the following command: $ sudo grep <username> /etc/passwd <username>:x:1001:1001:...:/home/<username>:/bin/aspshell If the transfer user is not limited to the "aspshell", this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252643`

### Rule: The IBM Aspera High-Speed Transfer Server must restrict users from using transfer services by default.

**Rule ID:** `SV-252643r818099_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. The IBM Aspera High Speed Transfer Server inherently uses file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server restricts users from using transfer services by default with the following commands: Check that the aspera.conf file is configured to deny transfer in and out by default. $ sudo /opt/aspera/bin/asuserdata -a | grep authorization | grep value authorization_transfer_in_value: "deny" authorization_transfer_out_value: "deny" If the results produce an "allow" value, this is a finding.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-252644`

### Rule: The IBM Aspera High-Speed Transfer Server must restrict users read, write, and browse permissions by default.

**Rule ID:** `SV-252644r818102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DoD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. ALGs must use these policies and mechanisms to control access on behalf of the application for which it is acting as intermediary. The IBM Aspera High Speed Transfer Server inherently uses file and group ownership of files and directories to support authorization for all supported operating systems. As an additional step and security best practice, ensure all transfers in or out of the authenticated connection are configured to be controlled based on privileges granted to specific users and groups within IBM Aspera configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Server restricts users read, write, and browse permissions by default with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep -w 'read_allowed\|write_allowed\|dir_allowed' read_allowed: "false" write_allowed: "false" dir_allowed: "false" If no results are returned or if the results produce a "true" value, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-252645`

### Rule: The IBM Aspera High-Speed Transfer Server must set the default docroot to an empty folder.

**Rule ID:** `SV-252645r818105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By restricting the default document root for the Aspera HSTS, this allows for explicit access to be defined on a per user basis. By default, all system users can establish a FASP connection and are only restricted by file permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Aspera High-Speed Transfer Server set the default docroot to an empty folder. Check that the default docroot points to an empty folder with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep absolute canonical_absolute: "<someemptyfolder>" absolute: "<someemptyfolder>" If the default docroot is set to "<Empty String>", this is a finding. Review the default docroot file path from the previous command to ensure it is empty. $ sudo find <somefilepath> -maxdepth 0 -empty -exec echo {} is empty. \; <somefilepath> is empty. If the command does not return "<somefilepath> is empty.", this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252646`

### Rule: The IBM Aspera High-Speed Transfer Server private/secret cryptographic keys file must be group-owned by root to prevent unauthorized read access.

**Rule ID:** `SV-252646r831532_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. The rootkeystore.db functions as a backup and main source of truth for encrypted secrets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rootkeystore.db file is group-owned by root with the following command: $ sudo stat -c "%G" /opt/aspera/etc/rootkeystore.db root If "root" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252647`

### Rule: The IBM Aspera High-Speed Transfer Server private/secret cryptographic keys file must be owned by root to prevent unauthorized read access.

**Rule ID:** `SV-252647r831533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. The rootkeystore.db functions as a backup and main source of truth for encrypted secrets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rootkeystore.db file is owned by root with the following command: $ sudo stat -c "%U" /opt/aspera/etc/rootkeystore.db root If "root" is not returned as a result, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-252648`

### Rule: The IBM Aspera High-Speed Transfer Server private/secret cryptographic keys file must have a mode of 0600 or less permissive to prevent unauthorized read access.

**Rule ID:** `SV-252648r831534_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. The rootkeystore.db functions as a backup and main source of truth for encrypted secrets.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the rootkeystore.db file has a mode of "0600" or less permissive with the following command: $ sudo stat -c "%a %n" /opt/aspera/etc/rootkeystore.db 600 /opt/aspera/etc/rootkeystore.db If the resulting mode is more permissive than "0600", this is a finding.

## Group: SRG-NET-000344-ALG-000098

**Group ID:** `V-252649`

### Rule: The IBM Aspera High-Speed Transfer Server must prohibit the use of cached authenticators after an organization-defined time period.

**Rule ID:** `SV-252649r831535_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the cached authenticator information is out of date, the validity of the authentication information may be questionable. This requirement applies to all ALGs that may cache user authenticators for use throughout a session. It also applies to ALGs that provide user authentication intermediary services (e.g., authentication gateway or TLS gateway). This does not apply to authentication for the purpose of configuring the device itself (device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IBM Aspera High-Speed Transfer Server prohibits the use of cached authenticators after an organization-defined time period with the following command: $ sudo /opt/aspera/bin/asuserdata -a | grep 'token_life' token_life_seconds: "86400" Note: The example token life is for one day; this number must be defined by the organization. If no result is returned or if the result is not an organization-defined time period, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-269982`

### Rule: The IBM Aspera Console feature must be a version supported by the vendor.

**Rule ID:** `SV-269982r1038948_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the version supported by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

