# STIG Benchmark: Axonius Federal Systems Ax-OS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000001

**Group ID:** `V-276001`

### Rule: Ax-OS must limit the number of concurrent sessions to 10 for all accounts and/or account types.

**Rule ID:** `SV-276001r1122653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Operating system management includes the ability to control the number of users and user sessions that utilize an operating system. Limiting the number of allowed users and sessions per user is helpful in reducing the risks related to denial-of-service (DoS) attacks. Satisfies: SRG-APP-000001, SRG-APP-000246, SRG-APP-000247, SRG-APP-000435</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Axonius Toolbox (accessed via Secure Shell [SSH]) Main Actions Menu, select the following options: Compliance Actions >> Advanced Compliance Actions >> Maximum Concurrent Logins If "Current Status: Disable" is shown, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-276002`

### Rule: Ax-OS must automatically terminate a graphical user interface (GUI) user session after 15 minutes.

**Rule ID:** `SV-276002r1122656_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the application server must be configured to close the sessions when a configured condition or trigger event is met. Session termination ends all processes associated with a user's logical session except those specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use. Satisfies: SRG-APP-000003, SRG-APP-000190, SRG-APP-000295</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> Privacy and Security >> Session. Under the Session Menu, verify the "Enable session timeout" slide bar is enabled. Verify "Session idle timeout (minutes)" is set to "15". If "Session idle timeout (minutes)" is not set to 15 minutes or less, this is a finding.

## Group: SRG-APP-000003

**Group ID:** `V-276003`

### Rule: Ax-OS must automatically terminate a Secure Shell (SSH) user session after 15 minutes.

**Rule ID:** `SV-276003r1122659_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the application server must be configured to close the sessions when a configured condition or trigger event is met. Session termination ends all processes associated with a user's logical session except those specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Axonius Toolbox (accessed via SSH) Main Actions Menu, select the following options: Compliance Actions >> Advanced Compliance Actions >> Idle session timeout If "Idle session timeout" is not enabled, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-276004`

### Rule: Ax-OS must implement DOD-approved encryption to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-276004r1122662_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or information system) communicating through an external, nonorganization-controlled network. Remote access methods include, for example, dial-up, broadband, and wireless. Encryption provides a means to secure the remote connection to prevent unauthorized access to data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Axonius Toolbox (accessed via Secure Shell [SSH]) Main Actions Menu, select the following options: System Actions >> Advanced System Actions If "Enable FIPS Mode" is present, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-276005`

### Rule: Ax-OS must enforce approved authorizations for logical access to information and system resources in accordance with applicable access control policies.

**Rule ID:** `SV-276005r1122665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Strong access controls are critical to securing the application server. The application server must employ access control policies (e.g., identity-based, role-based, and attribute-based policies) and access enforcement mechanisms (e.g., access control lists, access control matrices, and cryptography) to control access between users (or processes acting on behalf of users) and objects (e.g., applications, files, records, processes, and application domains) in the application server. Without stringent logical access and authorization controls, an adversary may have the ability, with little effort, to compromise the application server and associated supporting infrastructure. Satisfies: SRG-APP-000033, SRG-APP-000158, SRG-APP-000211, SRG-APP-000233, SRG-APP-000340, SRG-APP-000342, SRG-APP-000328, SRG-APP-000380, SRG-APP-000386, SRG-APP-000472, SRG-APP-000473, SRG-APP-000715, SRG-APP-000720, SRG-APP-000725, SRG-APP-000730, SRG-APP-000735</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Role-Based Access Control hierarchy is to be defined by the authorizing official (AO). Separation of duties must be configured. Select the gear icon (System Settings) >> Access Management >> LDAP & SAML. Depending on the multifactor type configured, under LDAP or SAML, locate "User Assignment Settings". If only one assigned role exists, this is a finding.

## Group: SRG-APP-000070

**Group ID:** `V-276006`

### Rule: Ax-OS must display the Standard Mandatory DOD Notice and Consent Banner before granting access to Ax-OS.

**Rule ID:** `SV-276006r1122668_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for desktops, laptops, and other devices accommodating banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-APP-000070, SRG-APP-000068</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> GUI >> Login. Under Login Page Settings >> Custom message (up to 3000 characters), verify the Standard Mandatory DOD Notice and Consent Banner is displayed. If the banner is not displayed, this is a finding.

## Group: SRG-APP-000070

**Group ID:** `V-276007`

### Rule: Ax-OS must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the Toolbox.

**Rule ID:** `SV-276007r1122671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the publicly accessible application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for desktops, laptops, and other devices accommodating banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Access the Axonius Toolbox via Secure Shell (SSH) and verify the Standard Mandatory DOD Notice and Consent Banner is displayed. If the banner is not displayed, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-276008`

### Rule: Ax-OS password manager must be disabled.

**Rule ID:** `SV-276008r1122674_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality that is not required for every mission but cannot be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> Access Management >> External Password Managers. If the "Use Password Manager" slide bar is enabled, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-276009`

### Rule: Ax-OS must use multifactor authentication for network access to the customer account.

**Rule ID:** `SV-276009r1122677_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator (SA) demonstrate accessing the Axonius Toolbox (accessed via Secure Shell [SSH]). Verify the SA is using a password-protected SSH key to log in to the system. If the SA is not using a password-protected SSH key to log in to the system, this is a finding.

## Group: SRG-APP-000149

**Group ID:** `V-276010`

### Rule: Ax-OS must use multifactor authentication for network access to the files account.

**Rule ID:** `SV-276010r1122680_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without the use of multifactor authentication, the ease of access to privileged functions is greatly increased. Multifactor authentication requires using two or more factors to achieve authentication. Factors include: (i) something a user knows (e.g., password/PIN); (ii) something a user has (e.g., cryptographic identification device, token); or (iii) something a user is (e.g., biometric). A privileged account is defined as an information system account with authorizations of a privileged user. Network access is defined as access to an information system by a user (or a process acting on behalf of a user) communicating through a network (e.g., local area network, wide area network, or the internet).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Have the system administrator (SA) demonstrate logging in to the Axonius host via Secure File Transfer Protocol (SFTP). Verify the SA is using a password-protected Secure Shell (SSH) key to log in to the system. If the SA is not using a password-protected SSH key to log in to the system, this is a finding.

## Group: SRG-APP-000150

**Group ID:** `V-276011`

### Rule: Ax-OS must use multifactor authentication for network access to nonprivileged accounts.

**Rule ID:** `SV-276011r1123259_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, nonprivileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A nonprivileged account is any information system account with authorizations of a nonprivileged user. Network access is any access to an application by a user (or process acting on behalf of a user) that is obtained through a network connection. Applications that integrate with the DOD Active Directory and use the DOD Common Access Card (CAC) are examples of compliant multifactor authentication solutions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> Access Management >> LDAP & SAML. Under LDAP & SAML, if the slide bar for "Allow LDAP Logins" or "Allow SAML Logins" is not selected, this is a finding. If the LDAP or SAML configuration does not point to an authentication source approved by the authorizing official (AO), this is a finding.

## Group: SRG-APP-000150

**Group ID:** `V-276012`

### Rule: Ax-OS must have no local accounts for the user interface.

**Rule ID:** `SV-276012r1122686_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, nonprivileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A nonprivileged account is any information system account with authorizations of a nonprivileged user. Network access is any access to an application by a user (or process acting on behalf of a user) that is obtained through a network connection. Applications that integrate with the DOD Active Directory and use the DOD Common Access Card (CAC) are examples of compliant multifactor authentication solutions. Satisfies: SRG-APP-000150, SRG-APP-000023, SRG-APP-000024, SRG-APP-000025, SRG-APP-000065, SRG-APP-000148, SRG-APP-000153, SRG-APP-000154, SRG-APP-000155, SRG-APP-000156, SRG-APP-000157, SRG-APP-000163, SRG-APP-000175, SRG-APP-000176, SRG-APP-000177, SRG-APP-000178, SRG-APP-000180, SRG-APP-000183, SRG-APP-000318, SRG-APP-000345, SRG-APP-000389, SRG-APP-000391, SRG-APP-000392, SRG-APP-000394, SRG-APP-000395, SRG-APP-000400, SRG-APP-000401, SRG-APP-000402, SRG-APP-000403, SRG-APP-000404, SRG-APP-000405, SRG-APP-000410, SRG-APP-000427, SRG-APP-000580, SRG-APP-000700, SRG-APP-000705, SRG-APP-000710, SRG-APP-000740, SRG-APP-000815, SRG-APP-000820, SRG-APP-000825, SRG-APP-000830, SRG-APP-000835, SRG-APP-000840, SRG-APP-000845, SRG-APP-000850, SRG-APP-000855, SRG-APP-000860, SRG-APP-000865, SRG-APP-000870, SRG-APP-000875, SRG-APP-000880, SRG-APP-000885, SRG-APP-000890</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Role-Based Access Control hierarchy is to be defined by the authorizing official (AO). Separation of duties must be configured. Select the gear icon (System Settings) >> User and Role Management >> Users. In the list of users, verify the list is empty. If the list is not empty, this is a finding.

## Group: SRG-APP-000219

**Group ID:** `V-276013`

### Rule: Ax-OS must protect the authenticity of communications sessions.

**Rule ID:** `SV-276013r1122689_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. Application communication sessions are protected using transport encryption protocols such as Transport Layer Security (TLS). TLS provides web applications with a means to authenticate user sessions and encrypt application traffic. Session authentication can be single (one way) or mutual (two way) in nature. Single authentication authenticates the server for the client, whereas mutual authentication provides a means for the client and server to authenticate each other. This requirement applies to applications that use communications sessions. This includes, but is not limited to, web-based applications and service-oriented architectures (SOAs). This requirement addresses communications protection at the application session versus the network packet. It also establishes grounds for confidence at both ends of communications sessions in relation to the ongoing identities of other parties and validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of TL) mutual authentication (two-way/bidirectional). Satisfies: SRG-APP-000219, SRG-APP-000910</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> Privacy and Security >> Certificate and Encryption. Under SSL Certificate, if the certificate has not been changed from the self-signed default certificate, unless otherwise approved by the authorizing official (AO), this is a finding. Under Certificate Verifications Settings, if "Use OCSP" is not selected, this is a finding. Under SSL Trust & CA Settings, if "Use custom certificate" is not selected and configured for a DOD PKI (or other AO-approved certificate), this is a finding. Under Mutual TLS Settings, if the "Enable mutual TLS" slide bar is not enabled, and the "Enforce client certificate validation" box is unchecked, this is a finding. Under Encryption Settings, if the "Allow legacy SSL cipher suites for adapters" is checked, this is a finding.

## Group: SRG-APP-000358

**Group ID:** `V-276014`

### Rule: Ax-OS must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-276014r1122692_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. Satisfies: SRG-APP-000358, SRG-APP-000086, SRG-APP-000090, SRG-APP-000097, SRG-APP-000108, SRG-APP-000111, SRG-APP-000115, SRG-APP-000116, SRG-APP-000118, SRG-APP-000120, SRG-APP-000121, SRG-APP-000122, SRG-APP-000123, SRG-APP-000125, SRG-APP-000181, SRG-APP-000267, SRG-APP-000275, SRG-APP-000291, SRG-APP-000292, SRG-APP-000293, SRG-APP-000294, SRG-APP-000320, SRG-APP-000357, SRG-APP-000359, SRG-APP-000360, SRG-APP-000362, SRG-APP-000363, SRG-APP-000364, SRG-APP-000365, SRG-APP-000366, SRG-APP-000367, SRG-APP-000368, SRG-APP-000369, SRG-APP-000370, SRG-APP-000376, SRG-APP-000515, SRG-APP-000745, SRG-APP-000750, SRG-APP-000755, SRG-APP-000760, SRG-APP-000765, SRG-APP-000770, SRG-APP-000775, SRG-APP-000780, SRG-APP-000785, SRG-APP-000790, SRG-APP-000795, SRG-APP-000800, SRG-APP-000945, SRG-APP-000950, SRG-APP-000955</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Select the gear icon (System Settings) >> External Integrations >> Syslog. Under the Syslog menu, if the "Use Syslog" slide bar is not selected, this is a finding. Under the Syslog menu, if "Syslog instance" has not been configured for an external log server(or otherwise proven Syslog is being captured by an external log server), this is a finding.

## Group: SRG-APP-000414

**Group ID:** `V-276015`

### Rule: Ax-OS must implement privileged access authorization to all information systems and infrastructure components for selected organization-defined vulnerability scanning activities.

**Rule ID:** `SV-276015r1122695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In certain situations, the nature of the vulnerability scanning may be more intrusive, or the information system component that is the subject of the scanning may contain highly sensitive information. Privileged access authorization to selected system components facilitates more thorough vulnerability scanning and also protects the sensitive nature of such scanning. The vulnerability scanning application must use privileged access authorization for the scanning account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Axonius Toolbox (accessed via Secure Shell [SSH]) Main Actions Menu, select the following options: Compliance Actions >> Advanced Compliance Actions >> Update Tenable Scan Account Permissions Enter the scanning account username. If no scanning account has been set, this is a finding.

## Group: SRG-APP-000925

**Group ID:** `V-276016`

### Rule: Ax-OS must compare the internal system clocks on an organization-defined frequency with an organization-defined authoritative time source.

**Rule ID:** `SV-276016r1123260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Synchronization of internal system clocks with an authoritative source provides uniformity of time stamps for systems with multiple system clocks and systems connected over a network. Satisfies: SRG-APP-000925, SRG-APP-000371, SRG-APP-000372, SRG-APP-000374, SRG-APP-000920</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the Axonius Toolbox (accessed via Secure Shell [SSH]) Main Actions Menu, select the following options: System Actions >> Advanced System Actions >> NTP Sources If any NTP sources listed are not an authoritative time source approved by the authorizing official (AO), this is a finding.

