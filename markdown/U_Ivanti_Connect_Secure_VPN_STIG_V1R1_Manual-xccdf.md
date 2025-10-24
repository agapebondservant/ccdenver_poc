# STIG Benchmark: Ivanti Connect Secure VPN Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-VPN-000040

**Group ID:** `V-258583`

### Rule: The ICS must be configured to ensure inbound and outbound traffic is configured with a security policy in compliance with information flow control policies.

**Rule ID:** `SV-258583r930437_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. VPN traffic received from another enclave with different security policy or level of trust must not bypass be inspected by the firewall before being forwarded to the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Users >> Resource Policies >> VPN Tunneling >> Access Control. 1. Verify that an Access Control Policy exists. 2. Verify the Access Control Policy is not configured to allows all IPv4/IPv6 addresses or all TCP/UDP ports. If the ICS does not use one or more Access Control Policies to restrict inbound and outbound traffic compliance with the sites documented information flow control policy, this is a finding.

## Group: SRG-NET-000041-VPN-000110

**Group ID:** `V-258584`

### Rule: The ICS must display the Standard Mandatory DOD Notice and Consent Banner before granting access to users.

**Rule ID:** `SV-258584r930440_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the network device ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. Satisfies: SRG-NET-000041-VPN-000110, SRG-NET-000042-VPN-000120, SRG-NET-000043-VPN-000130</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the network device is configured to present a DOD-approved banner that is formatted in accordance with DTM-08-060. Verify the remote access VPN user access sign-in notice is configured and displayed. This may or may not be the same as the admin portal. 1. In the ICS Web UI, navigate to Authentication >> Signing In >> Sign-In Notifications. Verify the use of the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details". Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't". 2. In the ICS Web UI, navigate to Authentication >> Signing In >> Sign-In Policies. 3. Click the "*/" (or whatever custom URL is used for remote access VPN user access). Under "Configure SignIn Notifications", if the "Pre-Auth Sign-in Notification" is not checked, or if the previously mentioned notification text is not assigned to this policy, this is a finding.

## Group: SRG-NET-000053-VPN-000170

**Group ID:** `V-258585`

### Rule: The ICS must be configured to limit the number of concurrent sessions for user accounts to one.

**Rule ID:** `SV-258585r930443_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VPN gateway management includes the ability to control the number of users and user sessions that utilize a VPN gateway. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. The intent of this policy is to ensure the number of concurrent sessions is deliberately set to a number based on the site's mission and not left unlimited.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Users >> User Realms >> User Realms. 1. If using the default user realm, click "User". Otherwise, click the configured user realm that will be used for user remote access VPN using DOD CAC authentication. 2. Click the "Authentication Policy" tab, then click "Limits". If the ICS does not limit the number of concurrent sessions for user accounts to "1", this is a finding.

## Group: SRG-NET-000062-VPN-000200

**Group ID:** `V-258586`

### Rule: The ICS must be configured to use TLS 1.2, at a minimum.

**Rule ID:** `SV-258586r930446_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. NIST SP 800-52 Rev2 provides guidance for client negotiation on either DOD-only or public-facing servers. Satisfies: SRG-NET-000062-VPN-000200, SRG-NET-000371-VPN-001650, SRG-NET-000530-VPN-002340, SRG-NET-000540-VPN-002350</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the ICS uses TLS 1.2 to protect remote access transmissions. In the ICS Web UI, navigate to System >> Configuration >> Inbound SSL Options. 1. Under Allowed SSL and TLS Version, verify "Accept only TLS 1.2 (maximize security)" is checked. 2. Navigate to System >> Configuration >> Outbound SSL Options. 3. Under Allowed SSL and TLS Version, verify "Accept only TLS 1.2 (maximize security)" is checked. If the ICS does not use TLS 1.2, at a minimum, this is a finding.

## Group: SRG-NET-000078-VPN-000290

**Group ID:** `V-258587`

### Rule: The ICS must be configured to generate log records containing sufficient information about where, when, identity, source, or outcome of the events.

**Rule ID:** `SV-258587r930449_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. VPN gateways often have a separate audit log for capturing VPN status and other information about the traffic (as opposed to the log capturing administrative and configuration actions). Associating event types with detected events in the network audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured VPN gateway. Satisfies: SRG-NET-000078-VPN-000290, SRG-NET-000079-VPN-000300, SRG-NET-000088-VPN-000310, SRG-NET-000089-VPN-000330, SRG-NET-000091-VPN-000350, SRG-NET-000077-VPN-000280, SRG-NET-000313-VPN-001050, SRG-NET-000492-VPN-001980</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Log/Monitoring >> User Access >> Settings. Under "Select Events to Log", verify all items are checked. If the ICS must be configured to generate log records containing information investigate the events, this is a finding.

## Group: SRG-NET-000138-VPN-000490

**Group ID:** `V-258588`

### Rule: The ICS must be configured to uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-258588r930452_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals' in-group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN or proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Users >> User Realms >> User Realms. 1. Click the user realm that is currently being used on the ICS for standard remote access VPN logins. 2. View "General" tab, under Servers >> Authentication. Verify a certificate authentication server is configured. 3. View "General" tab, under Servers >> Directory/Attribute. Verify there is an entry defined. 4. View "Role Mapping" tab, under "when users meet these conditions", verify "Group" is used with the local user active directory group selected and assigned to the role that was created. If the ICS does not use DOD PKI for network access to nonprivileged accounts, this is a finding.

## Group: SRG-NET-000140-VPN-000500

**Group ID:** `V-258589`

### Rule: The ICS must be configured to use multifactor authentication (e.g., DOD PKI) for network access to nonprivileged accounts.

**Rule ID:** `SV-258589r930455_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, nonprivileged users must use multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Use of password for user remote access for nonprivileged account is not authorized. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A nonprivileged account is any information system account with authorizations of a nonprivileged user. Network access is any access to a network element by a user (or a process acting on behalf of a user) communicating through a network. The DOD CAC with DOD-approved PKI is an example of multifactor authentication. Satisfies: SRG-NET-000140-VPN-000500, SRG-NET-000342-VPN-001360</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Users >> User Realms >> User Realms. 1. Click the user realm that is currently being used on the ICS for standard remote access VPN logins. 2. View "General" tab, under Servers >> Authentication. Verify a certificate authentication server is configured. 3. View "General" tab, under Servers >> Directory/Attribute. Verify there is an entry defined. 4. View "Role Mapping" tab, under "when users meet these conditions", verify "Group" is used with the local user active directory group selected and assigned to the role that was created. If the ICS does not use DOD PKI for network access to nonprivileged accounts, this is a finding.

## Group: SRG-NET-000164-VPN-000560

**Group ID:** `V-258590`

### Rule: The ICS, when utilizing PKI-based authentication, must be configured to validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-258590r930458_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. To meet this requirement, the information system must create trusted channels between itself and remote trusted authorized IT product (e.g., syslog server) entities that protect the confidentiality and integrity of communications. The information system must create trusted paths between itself and remote administrators and users that protect the confidentiality and integrity of communications. A trust anchor is an authoritative entity represented via a public key and associated data. It is most often used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. However, applications that do not use a trusted path are not approved for nonlocal and remote management of DOD information systems. Use of SSHv2 to establish a trusted channel is approved. Use of FTP, TELNET, HTTP, and SNMPV1 is not approved since they violate the trusted channel rule set. Use of web management tools that are not validated by common criteria may also violate the trusted channel rule set. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement. Satisfies: SRG-NET-000164-VPN-000560, SRG-NET-000512-VPN-002230, SRG-NET-000580-VPN-002410</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Configuration >> Certificates >> Trusted Client CAs. 1. Click the first DOD client CA. 2. Verify the item "Use OCSP with CRL fallback" is selected under the "Client certificate status checking" setting. 3. Check each client certificate CA. Verify the setting "Use OCSP with CRL fallback" is selected. For PKI-based authentication, if the ICS does not validate certificates by constructing a certification path (which includes revocation status information) to an accepted trust anchor, this is a finding.

## Group: SRG-NET-000213-VPN-000721

**Group ID:** `V-258591`

### Rule: The ICS must terminate remote access network connections after an organization-defined time period.

**Rule ID:** `SV-258591r930461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This SRG requirement is in response to the DoD OIG Audit of Maintaining Cybersecurity in the Coronavirus Disease-2019 Telework Environment. Best practice is to terminate inactive user sessions after a period; however, when setting timeouts to any VPN connection, the organization must take into consideration the risk to the mission and the purpose of the VPN. VPN connections that provide user access to the network are the prime candidates for VPN session termination and are the primary focus of this requirement. To determine if and when the VPN connections warrant termination, the organization must perform a risk assessment to identify the use case for the VPN and determine if periodic VPN session termination puts the mission at significant risk. The organization must document the results and the determination of the risk assessment in the VPN section of the SSP. The organization must also configure VPN session terminations in accordance with the risk assessment. This SRG requirement is in response to the DOD OIG Audit of Maintaining Cybersecurity in the Coronavirus Disease-2019 Telework Environment. Best practice is to terminate inactive user sessions after a period; however, when setting timeouts to any VPN connection, the organization must take into consideration the risk to the mission and the purpose of the VPN. VPN connections that provide user access to the network are the prime candidates for VPN session termination and are the primary focus of this requirement. To determine if and when the VPN connections warrant termination, the organization must perform a risk assessment to identify the use case for the VPN and determine if periodic VPN session termination puts the mission at significant risk. The organization must document the results and the determination of the risk assessment in the VPN section of the SSP. The organization must also configure VPN session terminations in accordance with the risk assessment. Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, de-allocating associated TCP/IP address/port pairs at the operating system level, and de-allocating networking assignments at the application level if multiple application sessions are using a single, operating system level network connection. This requirement applies to any network element that tracks individual sessions (e.g., stateful inspection firewall, ALG, or VPN).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the user role being used for CAC/PKI token VPN client logins is configured with a session timeout. In the ICS Web UI, navigate to Administrators >> Users Roles >> User Roles. 1. Click the configured user role being used for CAC/PKI token VPN client logins. 2. Click the "Session Options" tab. In the "Session Lifetime" section, if Idle Timeout is not set to "10", this is a finding.

## Group: SRG-NET-000334-VPN-001260

**Group ID:** `V-258592`

### Rule: The ICS must be configured to send user traffic log data to redundant central log server.

**Rule ID:** `SV-258592r930464_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The aggregation of log data kept on a syslog server can be used to detect attacks and trigger an alert to the appropriate security personnel. The stored log data can used to detect weaknesses in security that enable the network IA team to find and address these weaknesses before breaches can occur. Reviewing these logs, whether before or after a security breach, are important in showing whether someone is an internal employee or an outside threat. This requirement applies only to components where this is specific to the function of the device (e.g., IDPS sensor logs, firewall logs). This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify user access log events are being sent to the central log server. In the ICS Web UI, navigate to System >> Log/Monitoring >> User Access >> Settings. 1. Under "Select Events to Log", verify all items are checked. 2. Under "Syslog Servers", verify redundant server name/IP address, facility of LOCAL0, type TLS, and the source interface are defined. If the ICS must be configured to send admin log data to redundant central log server, this is a finding.

## Group: SRG-NET-000335-VPN-001270

**Group ID:** `V-258593`

### Rule: The ICS must be configured to forward all log failure events where the detection and/or prevention function is unable to write events to local log record or send an SNMP trap that can be forwarded to the SCA and ISSO.

**Rule ID:** `SV-258593r930467_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Automated alerts can be conveyed in a variety of ways, including, for example, telephonically, via electronic mail, via text message, or via websites. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. The VPN daemon facility and log facility are messages in the log, which capture actions performed or errors encountered by system processes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SNMP is used, verify the configuration is compliant. If SNMP is not used, this is not a finding. In the ICS Web UI, navigate to System >> Log/Monitoring >> SNMP. 1. Under "Agent Properties", verify "SNMP Traps" is checked. 2. Under "SNMP Version data", verify "v3" is selected. 3. Under "User 1", verify a user configuration in AuthPriv is using at least SHA and CFB-AES-128. 4. Verify "Optional Traps Critical and Major Log Events" are checked. 5. Verify the SNMP server IPv4/IPv6 address is configured under "SNMP Trap Servers". If SNMP is incorrectly configured, this is a finding.

## Group: SRG-NET-000343-VPN-001370

**Group ID:** `V-258594`

### Rule: The ICS must be configured to authenticate all clients before establishing a connection.

**Rule ID:** `SV-258594r930470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For ICS, user authentication uses authentication servers, realms, roles, and sign-in policies. To the device, both machine and user authentication are treated as user logins and certificates (machine certs and CAC) are supported for authentication. Although both machine and human users are considered "users" to the device. The system supports separating admin from user/computer authentication by duplicating auth servers and only associating a single server to an admin realm or a user realm but not both. This supports the DOD best practice of authenticating admin authentication using a separate authentication server from user authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify client certificates are installed and assigned to applicable user/computer realm to enable client authentication for all remote clients. In the Ivanti ICS Web UI, navigate to Users >> User Realms >> User Realms. 1. Click the user realm that is currently being used on the ICS for standard remote access VPN logins. 2. In the "General" tab, under Servers >> Authentication, verify it is defined with a certificate authenticate server. 3. In the "General" tab, under Servers >> Directory/Attribute, verify "none" is not displayed. 4. In the "Role Mapping" tab, under "when users meet these conditions", verify "Group" must be used, and the local site's administrator active directory group must be selected and assigned to the role that was created. If the ICS is not configured to authenticate all client devices before establishing a connection, this is a finding.

## Group: SRG-NET-000352-VPN-001460

**Group ID:** `V-258595`

### Rule: The ICS must be configured to use an approved Commercial Solution for Classified (CSfC) when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-258595r930473_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The National Security Agency/Central Security Service's (NSA/CSS) CSfC Program enables commercial products to be used in layered solutions to protect classified National Security Systems (NSS) data. Currently, Suite B cryptographic algorithms are specified by NIST and are used by NSA's Information Assurance Directorate in solutions approved for protecting classified and unclassified NSS. However, quantum resistant algorithms will be required for future required Suite B implementations. Satisfies: SRG-NET-000352-VPN-001460, SRG-NET-000565-VPN-002400, SRG-NET-000565-VPN-002390</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ICS VPN Gateway is not being used to carry classified data (e.g., Secret, Top Secret, etc.), this is Not Applicable. 1. Navigate to System >> Configuration >> Inbound SSL Options. Verify that under "Allowed Encryption Strength", if "SuiteB - Accept only SuiteB ciphers" is checked. 2. Navigate to System >> Configuration >> Certificates >> Device Certificates. Verify the certificate being used by the ICS is an ECC P-384 Public Key. If the ICS is not configured to use only SuiteB ciphers with ECC P-384 keys for transporting classified traffic, this is a finding.

## Group: SRG-NET-000369-VPN-001620

**Group ID:** `V-258596`

### Rule: The ICS must be configured to disable split-tunneling for remote client VPNs.

**Rule ID:** `SV-258596r930476_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. A VPN hardware or software client with split tunneling enabled provides an unsecured backdoor to the enclave from the internet. With split tunneling enabled, a remote client has access to the internet while at the same time has established a secured path to the enclave via an IPsec tunnel. A remote client connected to the internet that has been compromised by an attacker on the internet, provides an attack base to the enclave's private network via the IPsec tunnel. Hence, it is imperative that the VPN gateway enforces a no split-tunneling policy to all remote clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to Users >> Resource Policies >> Split Tunneling Networks. If there are any split-tunnel network policies, this is a finding.

## Group: SRG-NET-000550-VPN-002360

**Group ID:** `V-258597`

### Rule: The ICS that provides a Simple Network Management Protocol (SNMP) Network Management System (NMS) must configure SNMPv3 to use FIPS-validated AES cipher block algorithm.

**Rule ID:** `SV-258597r930479_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without device-to-device authentication, communications with malicious devices may be established. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. SNMPv3 supports authentication, authorization, access control, and privacy, while previous versions of the protocol contained well-known security weaknesses, which were easily exploited. SNMPv3 can be configured for identification and bidirectional, cryptographically based authentication. A typical SNMP implementation includes three components: managed device, SNMP agent, and NMS. The SNMP agent is the SNMP process that resides on the managed device and communicates with the network management system. The NMS is a combination of hardware and software that is used to monitor and administer a network. The SNMP data is stored in a highly structured, hierarchical format known as a management information base (MIB). The SNMP manager collects information about network connectivity, activity, and events by polling managed devices. SNMPv3 defines a user-based security model (USM), and a view-based access control model (VACM). SNMPv3 USM provides data integrity, data origin authentication, message replay protection, and protection against disclosure of the message payload. SNMPv3 VACM provides access control to determine whether a specific type of access (read or write) to the management information is allowed. Implement both VACM and USM for full protection. SNMPv3 server services must not be configured on products whose primary purpose is not to provide SNMP services. SNMP client services may be configured on the VPN gateway, application, or operating system to allow limited monitoring or querying of the device from by an SNMP server for management purposes. SNMP of any version will not be used to make configuration changes to the device. SNMPv3 must be disabled by default and enabled only if used. SNMP v3 provides security feature enhancements to SNMP, including encryption and message authentication. Currently, the AES cipher block algorithm can be used for both applying cryptographic protection (e.g., encryption) and removing or verifying the protection that was previously applied (e.g., decryption) in DOD. The use of FIPS-approved algorithms for both cryptographic mechanisms is required. If any version of SNMP is used for remote administration, default SNMP community strings such as "public" and "private" should be removed before real community strings are put into place. If the defaults are not removed, an attacker could retrieve real community strings from the device using the default string.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the ICS Web UI, navigate to System >> Log/Monitoring >> SNMP. Under "User 1", if a user configuration in AuthPriv is not using at least SHA and CFB-AES-128, this is a finding.

