# STIG Benchmark: Palo Alto Networks ALG Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.letterkenny.FSO.mbx.stig-customer-support-mailbox@mail.mil.

## Group: SRG-NET-000061-ALG-000009

**Group ID:** `V-228832`

### Rule: The Palo Alto Networks security platform, if used to provide intermediary services for remote access communications traffic (TLS or SSL decryption), must ensure inbound and outbound traffic is monitored for compliance with remote access security policies.

**Rule ID:** `SV-228832r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access traffic allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by inspecting connection activities of remote access capabilities. Remote access methods include both unencrypted and encrypted traffic (e.g., web portals, web content filter, TLS, and webmail). With inbound TLS inspection, the traffic must be inspected prior to being allowed on the enclave's web servers hosting TLS or HTTPS applications. With outbound traffic inspection, traffic must be inspected prior to being forwarded to destinations outside of the enclave, such as external email traffic. This requirement does not mandate the decryption and inspection of SSL/TLS; it requires that if this is performed in the device, the decrypted traffic be inspected and conform to security policies. If SSL/TLS traffic is decrypted in the device, it must be inspected. The Palo Alto Networks security platform can be configured to decrypt and inspect SSL/TLS connections going through the device. With SSL Decryption, SSL-encrypted traffic is decrypted and App-ID and the Antivirus, Vulnerability, Anti-Spyware, URL Filtering, and File-Blocking Profiles can be applied to decrypted traffic before being re-encrypted and being forwarded. This is not limited to SSL encrypted HTTP traffic (HTTPS); other protocols "wrapped" in SSL/TLS can be decrypted and inspected. Decryption is policy-based and can be used to decrypt, inspect, and control both inbound and outbound SSL and SSH connections. Decryption policies allow the administrator to specify traffic for decryption according to destination, source, or URL category and in order to block or restrict the specified traffic according to security settings.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS, and webmail), this is not applicable. Go to Policies >> Decryption; note each configured decryption policy. Go to Policies >> Security View the configured security policies. If there is a decryption policy that does not have a corresponding security policy, this is a finding. The matching policy may not be obvious and it may be necessary for the Administrator to identify the corresponding security policy.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-228833`

### Rule: The Palo Alto Networks security platform, if used as a TLS gateway/decryption point or VPN concentrator, must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-228833r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform does not serve as an intermediary for remote access traffic (e.g., web content filter, TLS, and webmail), this is not applicable. Use the command line interface to determine if the device is operating in FIPS mode. Enter the CLI command "show fips-mode" or the command show fips-cc (for more recent releases). If fips-mode or fips-cc is set to "off", this is a finding.

## Group: SRG-NET-000062-ALG-000092

**Group ID:** `V-228834`

### Rule: The Palo Alto Networks security platform that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.

**Rule ID:** `SV-228834r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. Private key data associated with software certificates is required to be generated and protected in at least a FIPS 140-2 Level 1 validated cryptographic module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the command line interface to determine if the device is operating in FIPS mode. If fips-mode or fips-cc is set to "off", this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-228835`

### Rule: The Palo Alto Networks security platform, if used as a TLS gateway/decryption point or VPN concentrator, must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-228835r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform is not used as a TLS gateway/decryption point or VPN concentrator, this is not applicable. Use the command line interface to determine if the device is operating in FIPS mode. Enter the CLI command "show fips-mode" or the command show fips-cc (for more recent releases).

## Group: SRG-NET-000077-ALG-000046

**Group ID:** `V-228836`

### Rule: The Palo Alto Networks security platform must log violations of security policies.

**Rule ID:** `SV-228836r557387_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, security personnel need to know the source of the event. In addition to logging where sources of events such as IP addresses, processes, and node or device names, it is important to log the name or identifier of each specific policy or rule that is violated. In the Palo Alto Networks security platform, traffic logs record information about each traffic flow, and threat logs record the threats or problems with the network traffic, such as virus or spyware detection. Note that the antivirus, anti-spyware, and vulnerability protection profiles associated with each rule determine which threats are logged (locally or remotely).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Policies >> Security View the configured security policies. For any Security Policy where the "Action" column shows "deny", view the "Options" column; if there are no icons in the column, this is a finding. Note: The "Action" column and the "Option" column are usually near the right edge; it may be necessary to use the slide to view them.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-228837`

### Rule: The Palo Alto Networks security platform must only enable User-ID on trusted zones.

**Rule ID:** `SV-228837r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User-ID can use Windows Management Instrumentation (WMI) probing as a method of mapping users to IP addresses. If this is used, the User-ID Agent will send a probe to each learned IP address in its list to verify that the same user is still logged in. The results of the probe will be used to update the record on the agent and then be passed on to the firewall. WMI probing is a Microsoft feature that collects user information from Windows hosts and contains a username and encrypted password hash of a Domain Administrator account. If User-ID and WMI probing are enabled on an external untrusted zone (such as the Internet), probes could be sent outside the protected network, resulting in an information disclosure of the User-ID Agent service account name, domain name, and encrypted password hash. This information has the potential to be cracked and exploited by an attacker to gain unauthorized access to protected resources. For this important reason, User-ID should never be enabled on an untrusted zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that Windows Management Instrumentation (WMI) probing is unchecked for all untrusted zones: Go to Network >> Zones, view each zone. If the Zone is untrusted and if the UserID Enabled column is checked, this is a finding. Go to Network >> Network Profiles >> Interface Mgmt View the configured Interface Management Profiles. Note which Interface Management Profiles have the "User-ID" field enabled (checked). Go Network >> Interfaces Each interface is listed; note that there are four tabs - Ethernet, VLAN, Loopback, and Tunnel. Each type can have an Interface Management Profile applied to it. View each interface that is in an untrusted security zone; if each one has no Interface Management Profile applied, this is not a finding. If each interface in an untrusted security zone has an Interface Management Profile applied to it, the Interface Management Profile must be one that does not have User-ID enabled; if it does, this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-228838`

### Rule: The Palo Alto Networks security platform must disable WMI probing if it is not used.

**Rule ID:** `SV-228838r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>User-ID can use Windows Management Instrumentation (WMI) probing as a method of mapping users to IP addresses. If this is used, the User-ID Agent will send a probe to each learned IP address in its list to verify that the same user is still logged in. The results of the probe will be used to update the record on the agent and then be passed on to the firewall. WMI probing is a Microsoft feature that collects user information from Windows hosts, and contains a username and encrypted password hash of a Domain Administrator account. WMI probing on external/untrusted zones can result in the User-ID agent sending WMI probes to external/untrusted hosts. An attacker can capture these probes and obtain the username, domain name and encrypted password hash associated with the User-ID account. If WMI probing is not used as a method of user to IP address mapping, it must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator if User-ID uses WMI Probing; if it does, this is not a finding. Go to Device >> User Identification On the "User Mapping" tab, in the "Palo Alto Networks User ID Agent" pane, view the "Enable Probing" check box. If it is selected, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-228839`

### Rule: The Palo Alto Networks security platform must not enable the DNS proxy.

**Rule ID:** `SV-228839r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Palo Alto Networks security platform can act as a DNS proxy and send the DNS queries on behalf of the clients. DNS queries that arrive on an interface IP address can be directed to different DNS servers based on full or partial domain names. However, unrelated or unneeded proxy services increase the attack vector surface and add excessive complexity to securing the device. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check if DNS Proxy is configured: Go to Network >> DNS Proxy If there are entries in the pane, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-228840`

### Rule: The Palo Alto Networks security platform must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-228840r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. The DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols, or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. It is the responsibility of the enclave owner to have the applications the enclave uses registered in the PPSM database. The Palo Alto Networks security platform must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. If the device is in a Deny-by-Default posture and what is allowed through the filter is IAW DoD Instruction 8551, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to PPS being blocked are satisfied. Since the enclave or system may support custom applications, it may be necessary to configure a Custom Application. This requires detailed analysis of the application traffic and requires validation testing before deployment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of authorized applications, endpoints, services, and protocols that has been added to the PPSM database. Go to Policies >> Security Review each of the configured security policies in turn. If any of the policies allows traffic that is prohibited by the PPSM CAL, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-228841`

### Rule: The Palo Alto Networks security platform that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-228841r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses. The Palo Alto Networks security platform can be configured to use Open Certificate Status Protocol (OCSP) and/or certificate revocation lists (CRLs) to verify the revocation status of certificates and the device itself can be configured as an OCSP responder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform does not provide intermediary services for TLS or application protocols that use TLS (e.g., HTTPS), this is not applicable. Go to Device >> Certificate Management >> OCSP Responder If no OCSP Responder is configured, this is a finding. Go to Device >> Setup >> Management In the "Management Interface Settings" pane, if "HTTP OCSP" is not listed under "Services", this is a finding.

## Group: SRG-NET-000192-ALG-000121

**Group ID:** `V-228842`

### Rule: The Palo Alto Networks security platform must protect against the use of internal systems for launching Denial of Service (DoS) attacks against external networks or endpoints.

**Rule ID:** `SV-228842r944363_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks from DOD sources risk the reputation of the organization. Thus, it is important to protecting against the DOD system being used to lauch an attack on external systems. Though Zone Protections are applied on the ingress interface, at a minimum, DOD requires a zero-trust approach. These attacks may use legitimate internal or rogue endpoints from inside the enclave. These attacks can be simple "floods" of traffic to saturate circuits or devices, malware that consumes CPU and memory on a device or causes it to crash, or a configuration issue that disables or impairs the proper function of a device. For example, an accidental or deliberate misconfiguration of a routing table can misdirect traffic for multiple networks. It is important to set the Flood Protection parameters that are suitable for the enclave or system. The Administrator should characterize the traffic regularly (perform a traffic baseline) and tune these parameters based on that information.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator if the device is using a Zone-Based Protection policy or a DoS Protection policy to protect against DoS attacks originating from the enclave. If it is using a DoS Protection policy, perform the following: Navigate to Objects >> Security Profiles >> DoS Protection. If there are no DoS Protection Profiles configured, this is a finding. There may be more than one configured DoS Protection Profile; ask the Administrator which DoS Protection Profile is intended to protect outside networks from internally-originated DoS attacks. If there is no such DoS Protection Profiles, this is a finding. If it is using a Zone-Based Protection policy, perform the following: Navigate to Network >> Network Profiles >> Zone Protection. If there are no Zone Protection Profiles configured, this is a finding. There may be more than one configured Zone Protection Profile; ask the Administrator which Zone Protection Profile is intended to protect outside networks from internally-originated DoS attacks. If there is no such Zone Protection Profile, this is a finding. Navigate to Network >> Zones. If the Zone Protection Profile column to monitor and protect zones contacting egress interfaces, this is a finding. If it lists an incorrect Zone Protection Profile, this is also a finding.

## Group: SRG-NET-000192-ALG-000121

**Group ID:** `V-228843`

### Rule: The Palo Alto Networks security platform must block phone home traffic.

**Rule ID:** `SV-228843r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A variety of Distributed Denial of Service (DDoS) attacks and other attacks use "botnets" as an attack vector. A botnet is a collection of software agents (referred to as "bot"), residing on compromised computers. Attacks are orchestrated by a "bot herder" to command these agents to launch attacks. Part of the command and control communication between the controller and the bots is a message sent from a bot that informs the controller that it is operating. This is referred to as a "phone home" message. On the Palo Alto Networks security platform, a security policy can include an Anti-spyware Profile for “phone home” detection (detection of traffic from installed spyware). The device has two pre-configured Anti-spyware Profiles; Default and Strict. The Default Anti-spyware Profile sends an alert for detected phone-home traffic for all severity levels except the low and informational severity threat levels, while the Strict Anti-spyware Profile blocks phone-home traffic for the critical, high, and medium severity threat levels. Phone home traffic must either be blocked or intercepted by the DNS Sinkholing feature. Therefore, a custom Anti-spyware Profile or the Strict Anti-spyware Profile must be used instead of the Default Anti-spyware Profile. Note that there are specific implementation requirements for DNS Sinkholing to operate properly; refer to the Palo Alto Networks documentation for details.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator which Anti-Spyware profile is used: Go to Objects >> Security Profiles >> Anti-Spyware Select the Anti-Spyware Profile. In the "Anti-Spyware Profile" window, in the "DNS Signatures" tab, in the Action on "DNS queries" field, if either "block" or "sinkhole" is not selected, this is a finding. Ask the Administrator which Security Policy Rule allows traffic from client hosts in the trust zone to the untrust zone: Go to Policies >> Security Select the identified policy rule. View the "Security Policy Rule" window. Select the "Actions" tab. In the "Profile Setting" section, in the "Anti-Spyware" field, if there is no Anti-Spyware Profile or the Anti-Spyware Profile is not the correct one, this is a finding.

## Group: SRG-NET-000192-ALG-000121

**Group ID:** `V-228844`

### Rule: The Palo Alto Networks security platform must deny outbound IP packets that contain an illegitimate address in the source address field.

**Rule ID:** `SV-228844r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious actor as a platform to launch cyber attacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack (usually DDoS) other computers or networks. DDoS attacks frequently leverage IP source address spoofing, in which packets with false source IP addresses send traffic to multiple hosts, who then send return traffic to the hosts with the IP addresses that were forged. This can generate significant, even massive, amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. Enclaves must enforce egress filtering. In egress filtering, packets leaving the enclave are discarded if the source IP address is not part of the IP address network(s), also known as prefixes, which are assigned to the enclave. A more specific form of egress filtering is to allow only those hosts and protocols that have been identified and authorized to exit the enclave. All traffic leaving the enclave, regardless of the destination, must be filtered by the premise router's egress filter to verify that the source IP address belongs to the enclave. Configure a security policy that allows only traffic originating from the IP address prefixes assigned to the enclave to exit the enclave. The implicit deny cross zone traffic rule will then be used, in part, to deny illegitimate source address traffic originating from an internal zone to go to another zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an anti-spoofing policy is configured for each outgoing zone that drops any traffic when the source IP does not match the list of allowed IP ranges for each outgoing zone. Navigate to the “Zone Protection Profile” configuration screen Select the “Packet-Based Attack Protection” tab Select the “IP Drop” tab If the “Spoofed IP Address” box is not checked for each outgoing zone, this is a finding.

## Group: SRG-NET-000202-ALG-000124

**Group ID:** `V-228845`

### Rule: The Palo Alto Networks security platform must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

**Rule ID:** `SV-228845r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only those connections that are essential and approved are allowed. As a managed boundary interface between networks, the Palo Alto Networks security platform must block all inbound and outbound network traffic unless a policy filter is installed to explicitly allow it. The allow policy filters must comply with the site's security policy. A deny-all, permit–by-exception network communications traffic policy ensures that only those connections that are essential and approved are allowed. By default, there are two security policies on the Palo Alto Networks firewall: Allow traffic within the same zone (intra-zone) Deny traffic from one zone to another zone (inter-zone). No policy that circumvents the inter-zone policy is allowed. Traffic through the device is permitted by policies developed to allow only that specific traffic that the system or enclave requires.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Policies >> Security Review each of the configured security policies in turn. Select each policy in turn; in the "Security Policy Rule" window, if the "Source Address" has "Any" selected, the "Destination Address" has "Any" selected, the "Application" has "Any" selected, and the "Action" Setting is "Allow", this is a finding. If any Security Policy is too broad (allowing all traffic either inbound or outbound), this is also a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-228846`

### Rule: The Palo Alto Networks security platform must terminate communications sessions after 15 minutes of inactivity.

**Rule ID:** `SV-228846r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Idle sessions can accumulate, leading to an exhaustion of memory in network elements processing traffic flows. Note that the 15 minute period is a maximum value; Administrators can choose shorter timeout values to account for system- or network-specific requirements. On a Palo Alto Networks security platform, a session is defined by two uni-directional flows, each uniquely identified by a 6-tuple key: source-address, destination-address, source-port, destination-port, protocol, and security-zone. Besides the six attributes that identify a session, each session has few more notable identifiers: end hosts - the source IP and destination IP which will be marked as client(source IP) and server(destination IP) and flow direction - each session is bi-directional and is identified by a two uni-directional flows, the first flow is client-to-server(c2s) and the returning flow is server-to-client(s2c). Sessions between endpoints are kept active by either normal traffic or by keepalive messages (also sometimes referred to as heartbeat messages). On the Palo Alto Networks security platform, the session timeout period is the time (seconds) required for the application to time out due to inactivity. Session timeouts are configured globally and on a per-application basis. When configured, timeouts for an application override the global TCP or UDP session timeouts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check global values: Go to Device >> Setup >> Session In the "Session Timeouts" pane, if the TCP field has a value of greater than "900", this is a finding. Obtain the list of authorized applications for the system or network. To check application-specific values: Go to Objects >> Applications Select, in turn, each authorized application. In the "Application" window, in the "Options" pane, view the "TCP" and "UDP Timeout" fields, if the value is greater than "900", this is a finding. Many applications will not have one of these two fields.

## Group: SRG-NET-000246-ALG-000132

**Group ID:** `V-228847`

### Rule: The Palo Alto Networks security platform must update malicious code protection mechanisms and signature definitions whenever new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-228847r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to minimize any potential negative impact to the organization caused by malicious code, malicious code must be identified and eradicated. Malicious code includes viruses, worms, Trojan horses, and Spyware.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the device is using the most current protection mechanisms and signature definitions. If the device has authorized connectivity to the Palo Alto site, the automated process can be used. Go to Device >> Dynamic Updates View the list of updates, and note the date of the most recent one. Select "Check Now" at the bottom of the page; if new updates appear, this is a finding. If the device does not have connectivity to the Palo Alto site, a manual process must be used. Log on to the Palo Alto Support site (registration required). Select the “Dynamic Updates” hyperlink. Check for the most current update (the version and release date of each update is listed). Go to Device >> Dynamic Updates View the list of updates and note the date of the most recent one. If the device does not have the most current updates installed, this is a finding.

## Group: SRG-NET-000249-ALG-000134

**Group ID:** `V-228848`

### Rule: The Palo Alto Networks security platform must drop malicious code upon detection.

**Rule ID:** `SV-228848r559740_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code is designed to compromise information systems; therefore, it must be prevented from being transferred to uninfected hosts. The Palo Alto Networks security platform allows customized profiles to be used to perform antivirus inspection for traffic between zones. Antivirus, anti-spyware, and vulnerability protection features require a specific license. There is a default Antivirus Profile; the profile inspects all of the listed protocol decoders for viruses, and generates alerts for SMTP, IMAP, and POP3 protocols while dropping for FTP, HTTP, and SMB protocols. However, these default actions cannot be edited and the values for the FTP, HTTP, and SMB protocols do not meet the requirement, so customized profiles must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus If there are no Antivirus Profiles configured other than the default, this is a finding. View the configured Antivirus Profiles; for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB) if the "Action" is anything other than “drop” or "reset-both", this is a finding. Go to Policies >> Security. Review each of the configured security policies in turn. For any Security Policy that allows traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding.

## Group: SRG-NET-000249-ALG-000145

**Group ID:** `V-228849`

### Rule: The Palo Alto Networks security platform must delete or quarantine malicious code in response to malicious code detection.

**Rule ID:** `SV-228849r559739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Taking an appropriate action based on local organizational incident handling procedures minimizes the impact of this code on the network. This requirement is limited to ALGs web content filters and packet inspection firewalls that perform malicious code detection as part of their functionality. The Palo Alto Networks security platform allows customized profiles to be used to perform antivirus inspection for traffic between zones. Antivirus, anti-spyware, and vulnerability protection features require a specific license. There is a default Antivirus Profile; the profile inspects all of the listed protocol decoders for viruses, and generates alerts for SMTP, IMAP, and POP3 protocols while dropping traffic for FTP, HTTP, and SMB protocols. However, these default actions cannot be edited and the values for the FTP, HTTP, and SMB protocols do not meet the requirement, so customized profiles must be used. Inspection is done through stream-based analysis, which means files are not cached or stored in their entirety on the firewall, but analyzed in real-time as they pass through the firewall. Therefore, any detected virus will automatically be deleted when detected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus If there are no Antivirus Profiles configured other than the default, this is a finding. View the configured Antivirus Profiles; for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB), if the "Action" is anything other than “drop” or "reset-both", this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding.

## Group: SRG-NET-000249-ALG-000146

**Group ID:** `V-228850`

### Rule: The Palo Alto Networks security platform must send an immediate (within seconds) alert to the system administrator, at a minimum, in response to malicious code detection.

**Rule ID:** `SV-228850r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability; then the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. The device must generate an immediate (within seconds) alert that notifies designated personnel of the incident. Since sending a message to an unattended log or console does not meet this requirement, the threat logs must be sent to an attended console or to e-mail. When the Palo Alto Networks security platform blocks malicious code, it also generates a record in the threat log. This message has a medium severity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following is an example of how to check if the device is sending messages to e-mail; this is one option that meets the requirement. If sending messages to an SNMP server or Syslog servers is used, follow the vendor guidance on how to verify that function: Go to Device >> Server Profiles >> Email If there is no Email Server Profile configured, this is a finding. Go to Objects >> Log forwarding If there is no Email Forwarding Profile configured, this is a finding. Go to Policies >> Security View the Security Policy that is used to detect malicious code (the "Profile" column does displays the "Antivirus Profile" symbol) in the "Options" column. If the Email Forwarding Profile is not used, this is a finding.

## Group: SRG-NET-000251-ALG-000131

**Group ID:** `V-228851`

### Rule: The Palo Alto Networks security platform must automatically update malicious code protection mechanisms.

**Rule ID:** `SV-228851r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Dynamic Updates If no entries for Applications and Threats are present, this is a finding. If the Applications and Threats entry states Download Only, this is a finding. This can be downgraded if a manual process is used. If a manual process is used, compare the Applications and Threats database for the most recent version. Go to Dashboard >> General Information, if the application, threat, and URL filtering definition versions are not the most current ones listed on the vendor support site, this is a finding.

## Group: SRG-NET-000288-ALG-000109

**Group ID:** `V-228852`

### Rule: The Palo Alto Networks security platform must deny or restrict detected prohibited mobile code.

**Rule ID:** `SV-228852r559734_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. This applies to mobile code that may originate either internal to or external from the enclave. Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. The Palo Alto Networks security platform allows customized profiles to be used to perform antivirus inspection for traffic between zones. Antivirus, anti-spyware, and vulnerability protection features require a specific license. There is a default Antivirus Profile; the profile inspects all of the listed protocol decoders for viruses, and generates alerts for SMTP, IMAP, and POP3 protocols while denying for FTP, HTTP, and SMB protocols. However, these default actions cannot be edited and the values for the FTP, HTTP, and SMB protocols do not meet the requirement, so customized profiles must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus If there are no Antivirus Profiles configured other than the default, this is a finding. View the configured Antivirus Profiles; for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB); if the "Action" is anything other than “deny” or "reset-both", this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding.

## Group: SRG-NET-000289-ALG-000110

**Group ID:** `V-228853`

### Rule: The Palo Alto Networks security platform must prevent the download of prohibited mobile code.

**Rule ID:** `SV-228853r559712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MMobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. This applies to mobile code that may originate either internal to or external from the enclave. Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. The Palo Alto Networks security platform allows customized profiles to be used to perform antivirus inspection for traffic between zones. Antivirus, anti-spyware, and vulnerability protection features require a specific license. There is a default Antivirus Profile; the profile inspects all of the listed protocol decoders for viruses, and generates alerts for SMTP, IMAP, and POP3 protocols while denying for FTP, HTTP, and SMB protocols. However, these default actions cannot be edited and the values for the FTP, HTTP, and SMB protocols do not meet the requirement, so customized profiles must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus If there are no Antivirus Profiles configured other than the default, this is a finding. View the configured Antivirus Profiles; for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB), if the "Action" is anything other than “drop” or “reset-both”, this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding.

## Group: SRG-NET-000313-ALG-000010

**Group ID:** `V-228854`

### Rule: The Palo Alto Networks security platform, if used as a TLS gateway/decryption point or VPN concentrator, must control remote access methods (inspect and filter traffic).

**Rule ID:** `SV-228854r831594_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated control capabilities, increase risk and makes remote user access management difficult at best. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). If the Palo Alto Networks security platform is used as a TLS gateway/decryption point or VPN concentrator, configure the device to inspect and filter decrypted traffic. For each type of SSL/TLS traffic that is decrypted, the resulting traffic must be inspected and filtered. For example, HTTPS traffic that is decrypted must have the HTTP traffic inspected and filtered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform is not used as a TLS gateway/decryption point or VPN concentrator, this is not applicable. Go to Policies >> Decryption Note each configured decryption policy. Go to Policies >> Security View the configured security policies. If there is a decryption policy that does not have a corresponding security policy, this is a finding. The matching policy may not be obvious, and it may be necessary for the Administrator to identify the corresponding security policy.

## Group: SRG-NET-000314-ALG-000013

**Group ID:** `V-228855`

### Rule: The Palo Alto Networks security, if used as a TLS gateway/decryption point or VPN concentrator, must provide the capability to immediately disconnect or disable remote access to the information system.

**Rule ID:** `SV-228855r831595_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to immediately disconnect or disable remote access, an attack or other compromise taking place would not be immediately stopped. Remote access functionality must have the capability to immediately disconnect current users remotely accessing the information system and/or disable further remote access. The remote access functionality may implement features such as automatic disconnect (or user-initiated disconnect) in case of adverse information based on an indicator of compromise or attack. If the Palo Alto Networks security platform is used as a TLS gateway/decryption point or VPN concentrator, configure the device to deny decrypted traffic that violates the enclave or system policies. For each type of SSL/TLS traffic that is decrypted, the resulting traffic must be inspected and filtered.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform is not used as a TLS gateway/decryption point or VPN concentrator, this is not applicable. Go to Policies >> Decryption Note each configured decryption policy. Go to Policies >> Security View the configured security policies. If there is a decryption policy that does not have a corresponding security policy, this is a finding. The matching policy may not be obvious, and it may be necessary for the Administrator to identify the corresponding security policy. Select the Security Policy Rules applied to the decrypted traffic. If it allows traffic that is prohibited, this is a finding.

## Group: SRG-NET-000318-ALG-000014

**Group ID:** `V-228856`

### Rule: To protect against data mining, the Palo Alto Networks security platform must detect and prevent SQL and other code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-228856r831596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection If there are no Vulnerability Protection Profiles configured, this is a finding. Ask the Administrator which Vulnerability Protection Profile is used to protect database assets by blocking and alerting on attacks. View the configured Vulnerability Protection Profile Check the "Severity" and "Action" columns. If the Vulnerability Protection Profile used for database protection does not block all critical, high, and medium threats, this is a finding. If the Vulnerability Protection Profile used for database protection does not alert on low and informational threats, this is a finding. Ask the Administrator which Security Policy is used to protect database assets: Go to Policies >> Security View the configured Security Policy. View the "Profile" column. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding. Moving the cursor over the symbol will list the exact Vulnerability Protection Profiles applied. If the specific Vulnerability Protection Profile is not listed, this is a finding.

## Group: SRG-NET-000318-ALG-000151

**Group ID:** `V-228857`

### Rule: To protect against data mining, the Palo Alto Networks security platform must detect and prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-228857r831597_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to prevent attacks launched against organizational information from unauthorized data mining may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. Most current applications are deployed as a multi-tier architecture. The multi-tier model uses separate server machines to provide the different functions of presentation, business logic, and database. The multi-tier architecture provides added security because a compromised web server does not provide direct access to the application itself or to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection If there are no Vulnerability Protection Profiles configured, this is a finding. Ask the Administrator which Vulnerability Protection Profile is used to protect application assets by blocking and alerting on attacks. View the configured Vulnerability Protection Profile; check the "Severity" and "Action" columns. If the Vulnerability Protection Profile used for database protection does not block all critical, high, and medium threats, this is a finding. If the Vulnerability Protection Profile used for database protection does not alert on low and informational threats, this is a finding. Ask the Administrator which Security Policy is used to protect application assets: Go to Policies >> Security View the configured Security Policy; view the "Profile" column. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding. Moving the cursor over the symbol will list the exact Vulnerability Protection Profiles applied. If the specific Vulnerability Protection Profile is not listed, this is a finding.

## Group: SRG-NET-000334-ALG-000050

**Group ID:** `V-228858`

### Rule: The Palo Alto Networks security platform must off-load audit records onto a different system or media than the system being audited.

**Rule ID:** `SV-228858r831598_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading is a common process in information systems with limited audit storage capacity. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view a syslog server profile: Go to Device >> Server Profiles >> Syslog If there are no Syslog Server Profiles present, this is a finding. Select each Syslog Server Profile; if no server is configured, this is a finding. View the log-forwarding profile to determine which logs are forwarded to the syslog server: Go to Objects >> Log forwarding If no Log Forwarding Profile is present, this is a finding. The "Log Forwarding Profile" window has five columns. If there are no Syslog Server Profiles present in the Syslog column for the Traffic Log Type, this is a finding. If there are no Syslog Server Profiles present for each of the severity levels of the Threat Log Type, this is a finding. Go to Device >> Log Settings >> System The list of Severity levels is displayed. If any of the Severity levels does not have a configured Syslog Profile, this is a finding. Go to Device >> Log Settings >> Config If the "Syslog" field is blank, this is a finding. Note: Any one failure of a check results in a finding, but failing more than one still results in only one finding. There cannot be multiple findings for a single requirement.

## Group: SRG-NET-000355-ALG-000117

**Group ID:** `V-228859`

### Rule: The Palo Alto Networks security platform being used for TLS/SSL decryption using PKI-based user authentication must only accept end entity certificates issued by DoD PKI or DoD-approved PKI Certificate Authorities (CAs) for the establishment of protected sessions.

**Rule ID:** `SV-228859r831599_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-DoD approved PKIs have not been evaluated to ensure that they have security controls and identity vetting procedures in place that are sufficient for DoD systems to rely on the identity asserted in the certificate. PKIs lacking sufficient security controls and identity vetting procedures risk being compromised and issuing certificates that enable adversaries to impersonate legitimate users. The authoritative list of DoD-approved PKIs is published at http://iase.disa.mil/pki-pke/interoperability. DoD-approved PKI CAs may include Category I, II, and III certificates. Category I DoD-Approved External PKIs are PIV issuers. Category II DoD-Approved External PKIs are Non-Federal Agency PKIs cross certified with the Federal Bridge Certification Authority (FBCA). Category III DoD-Approved External PKIs are Foreign, Allied, or Coalition Partner PKIs. Deploying the ALG with TLS enabled will require the installation of DoD and/or DoD-Approved CA certificates in the trusted root certificate store of each proxy to be used for TLS traffic. If the Palo Alto Networks security platform is used for TLS/SSL decryption, configure the Palo Alto Networks security platform to only accept end entity certificates issued by DoD PKI or DoD-approved PKI CAs for the establishment of protected sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform is not used for TLS/SSL decryption, this is not applicable. If the Palo Alto Networks security platform accepts non-DoD approved PKI end entity certificates, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-228860`

### Rule: The Palo Alto Networks security platform must protect against Denial of Service (DoS) attacks from external sources.

**Rule ID:** `SV-228860r944366_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources may be unavailable to users. Installation of content filtering gateways and application-layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks that are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. PAN-OS can use either Zone-Based Protection or End Host Protection to mitigate DoS attacks. Zone-Based Protection protects against most common floods, reconnaissance attacks, and other packet-based attacks and is applied to any zone. End Host Protection is specific to defined end hosts. Zone Protections are always applied on the ingress interface, so if you wish to protect against floods or scans from the internet, you would apply the profile on the zone containing the untrusted internet interface. Security administrators wishing to harden their networks even further can apply Zone Protections to both internal and external interfaces to ensure that protective measures are being applied across the entire environment. It is important to set the Flood Protection parameters that are suitable for the enclave or system. The Administrator should perform a traffic baseline to tune these parameters based. See https://knowledgebase.paloaltonetworks.com/KCSArticleDetail?id=kA10g000000ClVkCAK.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator if the device is using a Zone-Based Protection policy or a DoS Protection policy. If it is using a Zone-Based Protection policy, perform the following: Navigate to Network >> Network Profiles >> Zone Protection. If there are no Zone Protection Profiles configured, this is a finding. Note: There may be more than one configured Zone Protection Profile; ask the Administrator which Zone Protection Profile is intended to protect inside networks and DMZ networks from externally-originated DoS attacks. Navigate to Network >> Zones. If the "Zone Protection Profile" column for the internal zone or the DMZ is blank, this is a finding. If it lists an incorrect Zone Protection Profile, this is also a finding. If it is using a DoS Protection policy, perform the following: Navigate to Objects >> Security Profiles >> DoS Protection. There may be more than one configured DoS Protection Policy; ask the Administrator which DoS Protection Policy is intended to protect internal networks and DMZ networks from externally-originated DoS attacks. Navigate to Policies >> DoS Protection. If there is no DoS Protection Policy to protect internal networks and DMZ networks from externally-originated DoS attacks, this is a finding. If the DoS Protection Policy has no DoS Protection Profile, this is a finding.

## Group: SRG-NET-000362-ALG-000126

**Group ID:** `V-228861`

### Rule: The Palo Alto Networks security platform must use a Vulnerability Protection Profile that blocks any critical, high, or medium threats.

**Rule ID:** `SV-228861r831603_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources may be unavailable to users. Installation of content filtering gateways and application-layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection If there are no Vulnerability Protection Profiles configured, this is a finding. Ask the Administrator which Vulnerability Protection Profile is used for interzone traffic. View the configured Vulnerability Protection Profiles. Check the "Severity" and "Action" columns. If the Vulnerability Protection Profile used for interzone traffic does not block all critical, high, and medium threats, this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-228862`

### Rule: The Palo Alto Networks security platform must only allow incoming communications from organization-defined authorized sources forwarded to organization-defined authorized destinations.

**Rule ID:** `SV-228862r831604_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application-level firewalls and Web content filters), ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet or CDS) must be kept separate. Security policies on the Palo Alto Networks security platform match source, destination, application and a service. The application and service columns specify what applications can be identified on a defined set of ports, or on all available ports. The service column allows administrator to define one of the following: Application-default - The service application-default sets security policy to allow the application on the standard ports associated with the application. Pre-defined service “service-http” and “service-https” - The pre-defined services use TCP ports 80 and 8080 for HTTP, and TCP port 443 for HTTPS. Use this security policy if you want to restrict web browsing and HTTPS to these ports. Any - Use this service to deny applications. Custom service - Use this to define TCP/UDP port numbers to restrict applications to specific ports.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain and review the list of authorized sources and destinations. This is usually part of the System Design Specification or Accreditation Package. Go to Policies >> Security; review each of the configured security policies in turn. If any of the policies allows traffic that is not part of the authorized sources and destinations list, this is a finding.

## Group: SRG-NET-000370-ALG-000125

**Group ID:** `V-228863`

### Rule: The Palo Alto Networks security platform must identify and log internal users associated with prohibited outgoing communications traffic.

**Rule ID:** `SV-228863r831605_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying the users who initiated the traffic, it would be difficult to identify those responsible for the prohibited communications. This requirement applies to those network elements that perform Data Leakage Prevention (DLP) (e.g., ALGs, proxies, or application-level firewalls). The Palo Alto Networks Security Platform uses User-ID to map a user's identity to an IP address. This allows Administrators to configure and enforce firewall policies based on users and user groups in addition to network zones and addresses. If the user changes devices or the device is assigned a different IP address, User-ID tracks those changes and maintains the user to IP address mapping information. This supports non-repudiation. Before a security policy can be written for groups of users, the relationships between the users and the groups they are members of must be established. This information can be retrieved from an LDAP directory, such as Active Directory or eDirectory.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log into device Command Line Interface. Enter the command "show user ip-user-mapping all". If the output is blank, this is a finding. An alternate means to verify that User-ID is properly configured, view the URL Filtering and Traffic logs is to view the logs. To view the URL Filtering logs: Go to Monitor >> Logs >> URL Filtering To view the Traffic logs: Go to Monitor >> Logs >> Traffic User traffic originating from a trusted zone contains a username in the "Source User" column. If the "Source User" column is blank, this is a finding. Alternatively, verify that usernames are displayed in reports. Go to Monitor >> Reports Select the "Denied Applications Report". If the "Source User" fields are empty, this is a finding.

## Group: SRG-NET-000383-ALG-000135

**Group ID:** `V-228864`

### Rule: The Palo Alto Networks security platform must be configured to integrate with a system-wide intrusion detection system.

**Rule ID:** `SV-228864r831606_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without coordinated reporting between separate devices, it is not possible to identify the true scale and possible target of an attack. Integration of the Palo Alto Networks security platform with a system-wide intrusion detection system supports continuous monitoring and incident response programs. This requirement applies to monitoring at internal boundaries using TLS gateways, web content filters, email gateways, and other types of ALGs. The Palo Alto Networks security platform can work as part of the network monitoring capabilities to off-load inspection functions from the external boundary IDPS by performing more granular content inspection of protocols at the upper layers of the OSI reference model. NetFlow is an industry-standard protocol that enables the firewall to record statistics on the IP traffic that traverses its interfaces. The Palo Alto Networks security platform can export the statistics as NetFlow fields to a NetFlow collector. The NetFlow collector is a server you use to analyze network traffic for security, administration, accounting and troubleshooting purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Server Profiles >> NetFlow If no NetFlow Server Profiles are configured, this is a finding. This step assumes that it is one of the Ethernet interfaces that is being monitored. The verification is the same for Ethernet, VLAN, Loopback and Tunnel interfaces. Ask the administrator which interface is being monitored; there may be more than one. Go to Network >> Interfaces >> Ethernet Select the interface that is being monitored. If the "Netflow Profile" field is "None", this is a finding.

## Group: SRG-NET-000384-ALG-000136

**Group ID:** `V-228865`

### Rule: The Palo Alto Networks security platform must detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum.

**Rule ID:** `SV-228865r831607_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. If there is no list of unauthorized network services, this is a finding. If there are no configured security policies that specifically match the list of unauthorized network services, this is a finding. If the security policies do not deny the traffic associated with the unauthorized network services, this is a finding.

## Group: SRG-NET-000385-ALG-000137

**Group ID:** `V-228866`

### Rule: The Palo Alto Networks security platform must generate a log record when unauthorized network services are detected.

**Rule ID:** `SV-228866r831608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. To verify if a Security Policy logs denied traffic: Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, if neither the "Log at Session Start" nor the "Log at Session End" check boxes are checked, this is a finding.

## Group: SRG-NET-000385-ALG-000138

**Group ID:** `V-228867`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when unauthorized network services are detected.

**Rule ID:** `SV-228867r831609_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The Palo Alto Networks security platform must either send the alert to an SNMP or Syslog console that is actively monitored by authorized personnel (including the ISSO and ISSM) or use e-mail to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to block unauthorized network services. Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, view the Log Forwarding Profile. If there is no Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000390-ALG-000139

**Group ID:** `V-228868`

### Rule: The Palo Alto Networks security platform must continuously monitor inbound communications traffic crossing internal security boundaries.

**Rule ID:** `SV-228868r831610_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. Internal monitoring includes the observation of events occurring on the network crosses internal boundaries at managed interfaces such as web content filters. Depending on the type of ALG, organizations can monitor information systems by monitoring audit activities, application access patterns, characteristics of access, content filtering, or unauthorized exporting of information across boundaries. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses. Most current applications are deployed as a multi-tier architecture. The multi-tier model uses separate server machines to provide the different functions of presentation, business logic, and database. The multi-tier architecture provides added security because a compromised web server does not provide direct access to the application itself or to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the network architecture diagrams and identify where traffic crosses from one internal zone to another and review the configuration of the Palo Alto Networks security platform. The specific security policy is based on the authorized endpoints, applications, and protocols. If it does not monitor traffic passing between zones, this is a finding.

## Group: SRG-NET-000391-ALG-000140

**Group ID:** `V-228869`

### Rule: The Palo Alto Networks security platform must continuously monitor outbound communications traffic crossing internal security boundaries.

**Rule ID:** `SV-228869r831611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. Internal monitoring includes the observation of events occurring on the network crosses internal boundaries at managed interfaces such as web content filters. Depending on the type of ALG, organizations can monitor information systems by monitoring audit activities, application access patterns, characteristics of access, content filtering, or unauthorized exporting of information across boundaries. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses. Most current applications are deployed as a multi-tier architecture. The multi-tier model uses separate server machines to provide the different functions of presentation, business logic, and database. The multi-tier architecture provides added security because a compromised web server does not provide direct access to the application itself or to the database.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the network architecture diagrams and identify where traffic crosses from one internal zone to another and review the configuration of the Palo Alto Networks security platform. If it does not monitor traffic passing between zones, this is a finding.

## Group: SRG-NET-000392-ALG-000142

**Group ID:** `V-228870`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.

**Rule ID:** `SV-228870r831612_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The device generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) that require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Current USSTRATCOM warning and tactical directives/orders include Fragmentary Order (FRAGO), Communications Tasking Orders (CTOs), IA Vulnerability Notices, Network Defense Tasking Message (NDTM), DOD GIG Tasking Message (DGTM), and Operations Order (OPORD).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to enforce policies issued by authoritative sources. Go to Policies >> Security; select the name of the security policy to view it. In the Actions tab, in the Log Setting section, view the Log Forwarding Profile. If there is no Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000392-ALG-000143

**Group ID:** `V-228871`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when rootkits or other malicious software which allows unauthorized privileged access is detected.

**Rule ID:** `SV-228871r831613_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The Palo Alto Networks security platform generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) that require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Category 1; Root Level Intrusion (Incident)-Unauthorized privileged access to an IS. Category 4; Malicious Logic (Incident)-Installation of software designed and/or deployed by adversaries with malicious intentions for the purpose of gaining access to resources or information without the consent or knowledge of the user. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to filter traffic into the Internal or DMZ zones. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding. If the "Profile" column does not display the "Anti-spyware" symbol (which looks like a magnifying glass on a shield), this is a finding. If the "Options" column does not display the "Log Forwarding Profile" symbol, this is a finding.

## Group: SRG-NET-000392-ALG-000147

**Group ID:** `V-228872`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when rootkits or other malicious software which allows unauthorized non-privileged access is detected.

**Rule ID:** `SV-228872r831614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The device generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) that require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to filter traffic into the Internal or DMZ zones. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding. If the "Profile" column does not display the "Anti-spyware" symbol (which looks like a magnifying glass on a shield), this is a finding. If the "Options" column does not display the "Log Forwarding Profile" symbol, this is a finding.

## Group: SRG-NET-000392-ALG-000148

**Group ID:** `V-228873`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected.

**Rule ID:** `SV-228873r831615_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Configure a Server Profile for use with Log Forwarding Profile(s);if email is used, the ISSO and ISSM must be recipients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (email, SNMP Trap, or Syslog). View the configured Server Profile: Go to Device >> Server Profiles; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile. If there are no Log Forwarding Profiles configured, this is a finding. Go to Policies >> DoS Protection If there are no DoS Protection Policies, this is a finding. There may be more than one configured DoS Protection Policy. If there is no such DoS Protection Policy, this is a finding. In the "Log Forwarding" field, if there is no configured Log Forwarding Profile, this is a finding. Alternately, a Zone Protection Profile can be used either instead of or in addition to a DoS Protection Policy. Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile.

## Group: SRG-NET-000392-ALG-000149

**Group ID:** `V-228874`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting DoD systems or malicious code adversely affecting the operations and/or security of DoD systems is detected.

**Rule ID:** `SV-228874r831616_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The device generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) that require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile, if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles: Go to Objects >> Log Forwarding Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to filter traffic between zones or subnets. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Options" column does not display the "Log Forwarding Profile" symbol, this is a finding.

## Group: SRG-NET-000402-ALG-000130

**Group ID:** `V-228875`

### Rule: The Palo Alto Networks security platform must block traceroutes and ICMP probes originating from untrusted networks (e.g., ISP and other non-DoD networks).

**Rule ID:** `SV-228875r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Only authorized personnel should be aware of errors and the details of the errors. Error messages are an indicator of an organization's operational state or can give configuration details about the network element. The traceroute utility will display routes and trip times on an IP network. An attacker can use traceroute responses to create a map of the subnets and hosts behind the boundary. The traditional traceroute relies on TTL - time exceeded responses from network elements along the path and an ICMP port-unreachable message from the target host. In some Operating Systems such as UNIX, trace route will use UDP port 33400 and increment ports on each response. Since blocking these UDP ports alone will not block trace route capabilities along with blocking potentially legitimate traffic on a network, it's unnecessary to block them explicitly. Because traceroutes typically rely on ICMP Type 11 - Time exceeded message, the time exceeded message will be the target for implicitly or explicitly blocking outbound from the trusted network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator which Security Policy blocks traceroutes and ICMP probes. Go to Policies >> Security View the identified Security Policy. If the "Source Zone" field is not external and the "Source Address" field is not any, this is a finding. If the "Destination Zone" fields do not include the internal and DMZ zones and the "Destination Address" field is not any, this is a finding. Note: The exact number and name of zones is specific to the network. If the "Application" fields do not include "icmp", "ipv6-icmp", and "traceroute", this is a finding. If the "Actions" field does not show "Deny" as the resulting action, this is a finding.

## Group: SRG-NET-000510-ALG-000025

**Group ID:** `V-228876`

### Rule: The Palo Alto Networks security platform providing encryption intermediary services must implement NIST FIPS-validated cryptography to generate cryptographic hashes.

**Rule ID:** `SV-228876r831617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform does not provide encryption intermediary services (e.g., HTTPS or TLS), this is not applicable. Use the command line interface to determine if the device is operating in FIPS mode. Enter the CLI command "show fips-mode" or the command show fips-cc (for more recent releases). If fips-mode or fips-cc is set to off, this is a finding.

## Group: SRG-NET-000510-ALG-000111

**Group ID:** `V-228877`

### Rule: The Palo Alto Networks security platform, if used for TLS/SSL decryption, must use NIST FIPS-validated cryptography to implement encryption.

**Rule ID:** `SV-228877r831618_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Palo Alto Networks security platform is not used for TLS/SSL decryption, this is not applicable. Use the command line interface to determine if the device is operating in FIPS mode. Enter the CLI command "show fips-mode" or the command show fips-cc (for more recent releases). If fips mode is set to off, this is a finding.

## Group: SRG-NET-000511-ALG-000051

**Group ID:** `V-228878`

### Rule: The Palo Alto Networks security platform must, at a minimum, off-load threat and traffic log records onto a centralized log server in real time.

**Rule ID:** `SV-228878r831619_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Off-loading is a common process in information systems with limited audit storage capacity. The audit storage on the Palo Alto Networks security platform is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real time, which indicates that the time from event detection to off-loading is seconds or less. For the purposes of this requirement, the terms "real time" and "near-real time" are equivalent. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view a syslog server profile: Go to Device >> Server Profiles >> Syslog If there are no Syslog Server Profiles present, this is a finding. Select each Syslog Server Profile; if no server is configured, this is a finding. View the log-forwarding profile to determine which logs are forwarded to the syslog server. Go to Objects >> Log forwarding If no Log Forwarding Profile is present, this is a finding. The "Log Forwarding Profile" window has five columns. If there are no Syslog Server Profiles present in the "Syslog" column for the Traffic Log Type, this is a finding. If there are no Syslog Server Profiles present for each of the severity levels of the Threat Log Type, this is a finding. Go to Device >> Log Settings >> System Logs The list of Severity levels is displayed. If any of the Severity levels does not have a configured Syslog Profile, this is a finding. Go to Device >> Log Settings >> Config Logs If the "Syslog field" is blank, this is a finding.

## Group: SRG-NET-000512-ALG-000064

**Group ID:** `V-228879`

### Rule: The Palo Alto Networks security platform must inspect inbound and outbound SMTP and Extended SMTP communications traffic (if authorized) for protocol compliance and protocol anomalies.

**Rule ID:** `SV-228879r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as SMTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. The device must be configured to inspect inbound and outbound SMTP and Extended SMTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If SMTP or ESMTP is authorized, ask the Administrator which Security Policy inspects authorized SMTP and ESMTP traffic. Go to Policies >> Security Select the identified Security Policy. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding.

## Group: SRG-NET-000512-ALG-000065

**Group ID:** `V-228880`

### Rule: The Palo Alto Networks security platform must inspect inbound and outbound FTP and FTPS communications traffic (if authorized) for protocol compliance and protocol anomalies.

**Rule ID:** `SV-228880r864182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as FTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. The device must be configured to inspect inbound and outbound FTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the protocol is not used in the implementation, this is not a finding. Go to Policies >> Decryption If there are no configured Decryption Policies, this is a finding. Ask the Administrator which Security Policy inspects authorized FTP traffic. Go to Policies >> Security Select the identified Security Policy. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding.

## Group: SRG-NET-000512-ALG-000066

**Group ID:** `V-228881`

### Rule: The Palo Alto Networks security platform must inspect inbound and outbound HTTP traffic (if authorized) for protocol compliance and protocol anomalies.

**Rule ID:** `SV-228881r557387_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application protocol anomaly detection examines application layer protocols such as HTTP to identify attacks based on observed deviations in the normal RFC behavior of a protocol or service. This type of monitoring allows for the detection of known and unknown exploits that exploit weaknesses of commonly used protocols. The device must be configured to inspect inbound and outbound HTTP communications traffic to detect protocol anomalies such as malformed message and command insertion attacks. All inbound and outbound traffic, including HTTPS, must be inspected. However, the intention of this policy is not to mandate HTTPS inspection by the device. Typically, HTTPS traffic is inspected either at the source, destination, and/or is directed for inspection by an organization-defined network termination point.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator which Security Policy inspects authorized HTTP traffic. Go to Policies >> Security Select the identified Security Policy. If the "Profile" column does not display the "Antivirus Profile" symbol, this is a finding. If the "Profile" column does not display the "Vulnerability Protection Profile" symbol, this is a finding.

