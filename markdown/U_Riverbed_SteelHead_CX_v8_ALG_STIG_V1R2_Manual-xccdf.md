# STIG Benchmark: Riverbed SteelHead CX v8 ALG Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000521-ALG-000002

**Group ID:** `V-238497`

### Rule: If TLS optimization is used, the Riverbed Optimization System (RiOS) providing Signed SMB and/or Encrypted MAPI must ensure the integrity and confidentiality of data transmitted over the WAN.

**Rule ID:** `SV-238497r654938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the end-to-end security of TLS is required to ensure integrity and confidentiality of the data in transit. Signed SMB and encrypted MAPI traffic use techniques to protect against unauthorized man-in-the-middle devices from making modifications to their exchanged data. Additionally, encrypted MAPI traffic and encrypted SMB3 traffic ensure data confidentiality by transmitting data with protection across the network. To securely optimize this traffic, a properly configured client and server-side SteelHead appliance with the SteelHead WAN optimization platform must: - decrypt and remove signatures on received LAN side data from the client or server. - perform bandwidth and application layer optimization. - use the secure inner channel feature to maintain data integrity and confidentiality of data transmitted over the WAN. - convert the received optimized data back to its native form. - encrypt and apply signatures for LAN side transmission of data to the client or server. To query the Windows domain controller for the necessary cryptographic information to optimize this traffic, the server-side SteelHead appliance must join a Windows domain. The SteelHead appliance can require other configurations, both on the SteelHead appliance, and in the Windows domain. This cryptographic information is only useful for the lifetime of an individual connection or session. The information is obtained at the beginning of a connection, and transferred to the client-side SteelHead appliance as needed, using the secure inner channel feature. You must configure the secure inner channel to ensure maximum security. Only the server-side SteelHead appliance is required to join the domain, and it does so using a machine account in the same way that a Windows device joins the domain using a machine account. The SteelHead appliance joins the domain this way to obtain a client user session key (CUSK) or server user session key (SUSK), which allows the SteelHead appliance to sign and/or decrypt MAPI on behalf of the Windows user that is establishing the relevant session. The server-side SteelHead appliance must join a domain that is either: - the user domain. The domain must have a trust with the domains that include the application servers (file server, Exchange server, and so on) you want to optimize. - A domain with a bi-directional trust with the user domain. The domain might include some or all of the Windows application servers (file server, Exchange server) for SteelHead appliance optimization. Production deployments can have multiple combinations of client and server Windows operating system versions, and can include different configuration settings for signed SMB and encrypted MAPI. NTLM is not approved for use for DoD implementations. Therefore it is possible that the security authentication between clients and servers can use Kerberos, or a combination of the two.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the RiOS providing Signed SMB and Encrypted MAPI optimization services is configured to ensure the integrity and confidentiality of data transmitted over the WAN. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Windows Domain Auth Verify that a Domain is defined under "Kerberos" Navigate to Configure >> Optimization >> CIFS (SMB1). Verify that "Enable SMB Signing", "NTLM Delegation Mode", and "Enable Kerberos Authentication Support" are selected. Navigate to Configure >> Optimization >> SMB2/3. Verify that "Enable SMB2 and SMB3 Signing", "NTLM Delegation Mode", and "Enable Kerberos Authentication Support" are selected. Navigate to Configure >> Optimization >> MAPI. Verify that "Enable Encrypted Optimization", "NTLM Delegation Mode", and "Enable Kerberos Authentication Support" are selected. If any SMB Signing or Encrypted MAPI is selected and the status of "In Domain Mode, Status: In a Domain" is not displayed, this is a finding.

## Group: SRG-NET-000061-ALG-000009

**Group ID:** `V-238498`

### Rule: The Riverbed Optimization System (RiOS) must be configured to ensure inbound and outbound traffic is forwarded to be inspected by the firewall and IDPS in compliance with remote access security policies.

**Rule ID:** `SV-238498r654941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated monitoring of remote access traffic allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by inspecting connection activities of remote access capabilities. Remote access methods include both unencrypted and encrypted traffic. Inbound traffic must be inspected prior to being allowed on the enclave's trusted networks. Outbound traffic inspection must occur prior to being forwarded to destinations outside of the enclave. Optimally, the SteelHead must be architecturally placed at the perimeter in front of the perimeter router. Thus, traffic is directed for firewall and IDPS inspection for inbound and outbound traffic in compliance with DoD policy. Additionally, from an operational perspective, this architecture avoids the need to open many ports and services in the firewall to accommodate TCP options 76 and 78 and ports 7800, 7810, and 7870. Some other configurations may involve even more ports and services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the architectural placement of the device. Verify the traffic from the device is directed to the firewall and IDS or IPS for inspection. If RiOS is not configured to ensure inbound and outbound traffic is forwarded to be inspected by the firewall and IDPS in compliance with remote access security policies, this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-238499`

### Rule: If TLS WAN optimization is used, Riverbed Optimization System (RiOS) providing SSL Optimization must protect private keys ensuring that they stay in the data center by ensuring end-to-end security.

**Rule ID:** `SV-238499r654944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting the end-to-end security of TLS is required to ensure integrity and confidentiality of the data in transit. The Riverbed Optimization System TLS optimization solution accelerates data transfers that are encrypted using TLS, provided SteelHead appliances that are deployed locally to both the client-side and server-side of the network. All of the same optimized connections that are applied to normal non-encrypted TCP traffic can also apply to encrypted TLS traffic. SteelHead appliances with RiOS accomplish this without compromising end-to-end security and the established trust model. Private keys remain in the data center and are not exposed in remote locations where they might be compromised. The RiOS TLS optimization solution starts with SteelHead appliances that have a configured trust relationship, enabling them to exchange information securely over their own dedicated TLS connection. Each client uses unchanged server addresses and each server uses unchanged client addresses; no application changes or explicit proxy configuration is required. RiOS uses a unique technique to split the TLS handshake. The handshake is the sequence of message exchanges at the start of a TLS connection. In an ordinary TLS handshake, the client and server first establish identity using public-key cryptography, and then negotiate a symmetric session key to use for data transfer. When using RiOS TLS acceleration, the initial TLS message exchanges take place between the client application (for example, a Web browser) and the server side SteelHead appliance. SteelHead WAN optimization platform works to ensure that TLS acceleration delivers the following: - sensitive cryptographic information is kept in the secure vault - a separate, encrypted store on the disk. - built-in support for popular Certificate Authorities (CAs) such as VeriSign, Thawte, Entrust, and GlobalSign. In addition, SteelHead appliances allow the installation of other commercial or privately operated CAs. - import of server proxy certificates and keys in PEM, PKCS12, or DER formats. SteelHead appliances also support the generation of new keys and self-signed certificates. If your certificates and keys are in another format, you must first convert them to a supported format before you can import them into the SteelHead appliance. - separate control of cipher suites for client connections, server connections, and peer connections. - bulk export or bulk import server configurations (including keys and certificates) from or to, respectively, the server-side SteelHead appliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS providing TLS optimization services is configured to ensure end-to-end security and protect private keys from unauthorized access. Navigate to the device Management Console. Navigate to Configure >> Optimization >> SSL Main Settings. Verify that "Enable SSL Optimization" is checked. Verify that "SSL Server Certificates:" contains the certificates for SSL services that the organization wants to optimize. If "Enable SSL Optimization" is not checked or there are no "SSL Sever Certificates", this is a finding.

## Group: SRG-NET-000062-ALG-000011

**Group ID:** `V-238500`

### Rule: If TLS optimization is used, the Riverbed Optimization System (RiOS) providing intermediary services for TLS communications traffic must use encryption services that implement NIST FIPS-validated cryptography to protect the confidentiality of TLS.

**Rule ID:** `SV-238500r654947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Encryption provides a means to secure the remote connection so as to prevent unauthorized access to the data traversing the remote access connection, thereby providing a degree of confidentiality. The encryption strength of the mechanism is selected based on the security categorization of the information. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to support TLS version 1.1 as a minimum and preferably TLS version 1.2. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Advanced. Verify that "Peer Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Client Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Server Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If any of the above Ciphers contains strings or groups other than what is listed, this is a finding.

## Group: SRG-NET-000062-ALG-000092

**Group ID:** `V-238501`

### Rule: If TLS optimization is used, the Riverbed Optimization System (RiOS) that stores secret or private keys must use FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys.

**Rule ID:** `SV-238501r654950_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Private key data is used to prove that the entity presenting a public key certificate is the certificate's rightful owner. Compromise of private key data allows an adversary to impersonate the key holder. Private key data associated with software certificates, including those issued to an ALG, is required to be generated and protected in at least a FIPS 140-2 Level 1 validated cryptographic module. The Riverbed RiOS secure vault contains sensitive information from your SteelHead appliance configuration, including SSL private keys and the data store encryption key. These configuration settings are encrypted on the disk using AES 256-bit encryption. The secure vault always runs in FIPS mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Riverbed Optimization System (RiOS) is configured to support FIPS-approved key management technology and processes in the production and control of private/secret cryptographic keys. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Advanced. Verify that "Peer Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Client Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Server Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If any of the above Ciphers contains strings or groups other than what is listed, this is a finding.

## Group: SRG-NET-000062-ALG-000150

**Group ID:** `V-238502`

### Rule: The Riverbed Optimization System (RiOS) that provides intermediary services for TLS must be configured to comply with the required TLS settings in NIST SP 800-52.

**Rule ID:** `SV-238502r654953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SP 800-52 provides guidance on using the most secure version and configuration of the TLS/SSL protocol. Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks which exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as SSL gateways) and is not applicable to VPN devices. Application protocols such as HTTPS and DNSSEC use TLS as the underlying security protocol thus are in scope for this requirement. NIS SP 800-52 provides guidance. SP 800-52 sets TLS version 1.1 as a minimum version, thus all versions of SSL are not allowed (including for client negotiation) either on DoD-only or on public facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to support TLS version 1.1 as a minimum and preferably TLS version 1.2. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Advanced. Verify that "Peer Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Client Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Server Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If any of the above Ciphers contains strings or groups other than what is listed, this is a finding.

## Group: SRG-NET-000063-ALG-000012

**Group ID:** `V-238503`

### Rule: The Riverbed Optimization System (RiOS) providing intermediary services for remote access communications traffic must use NIST FIPS-validated cryptography to protect the integrity of remote access sessions.

**Rule ID:** `SV-238503r654956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access is access to DoD-nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. Remote access methods include, for example, proxied remote encrypted traffic (e.g., TLS gateways, web content filters, and webmail proxies). Cryptographic mechanisms used for protecting the integrity of information include, for example, signed hash functions using asymmetric cryptography enabling distribution of the public key to verify the hash information while maintaining the confidentiality of the secret key used to generate the hash. This requirement applies to ALGs providing remote access proxy services as part of its intermediary services (e.g., OWA or TLS gateway).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to support TLS version 1.1 as a minimum and preferably TLS version 1.2. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Advanced. Verify that "Peer Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Client Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Server Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If any of the above Ciphers contains strings or groups other than what is listed, this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-238504`

### Rule: The Riverbed Optimization System (RiOS) must not have unrelated or unnecessary services enabled on the host.

**Rule ID:** `SV-238504r654959_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Because Wan Optimization is optimally installed in the architecture at the perimeter, installation of unnecessary functions and services on the same host increases the risk by implementing these functions before the network inspection functions and excessive open ports on the firewall for these functions and services to operation. Loading functions that are outside the scope and unrelated to the WAN optimization function is unauthorized and may create an attack vector. Related services include content filtering, traffic analysis, decryption, caching, and traffic inspection tools (e.g., firewall, IDS), unrelated services include email, DNS, web server. When the solution is implemented using a Steelhead CX hardware appliance implementation consisting of the RiOS installed on the SteelHead, administrators are not able to install any software that is not part of a Riverbed upgrade. RiOS enforces this by performing a validity check when an upgrade is attempted. However, the RiOS application suite is available in a virtual appliance version which can be installed on an organization-provided host. This type of implementation adds risk because more ports may need to be opened in the firewall if placed in the recommended logical position in the architecture after the router and before the firewall and IDS. The traffic should then be routed for inspection after traversing the wan optimizer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If RiOS is installed on the SteelHead appliance, this is a finding. Inspect the services and applications that are installed on the host with the RiOS application suite. Ask the site representative if a security review using the applicable STIG has been performed on the operating system and applications that are co-hosted. If unrelated or unnecessary services are installed on the same host as the RiOS, this is a finding. If a security review using the applicable STIG has not been performed on the operating system and applications co-hosted on with the RiOS, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-238505`

### Rule: Riverbed Optimization System (RiOS) must not have unnecessary services and functions enabled.

**Rule ID:** `SV-238505r654962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrelated or unneeded proxy services increase the attack vector and add excessive complexity to the securing of Riverbed Optimization System (RiOS) version 8.x.x. Multiple application proxies can be installed on many ALGs. However, proxy types must be limited to related functions. At a minimum, the web and email gateway represent different security domains/trust levels. Organizations should also consider separation of gateways that service the DMZ and the trusted network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to disable unrelated or unneeded application proxy services. Obtain documentation for which applications are approved/disapproved for optimization by the organization. Navigate to the device Management Console Navigate to Optimize >> Optimization Verify that the approved or disapproved applications are enabled or disabled according to organization requirements. If optimization features are not enabled or disabled according to the organizations requirements, this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-238506`

### Rule: The Riverbed Optimization System (RiOS) must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-238506r654965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. ALGs are capable of providing a wide variety of functions and services. Some of the functions and services provided by default may not be necessary to support essential organizational operations. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. Riverbed Optimization System (RiOS) is a key network element for preventing these non-compliant ports, protocols, and services from causing harm to DoD information systems. The network ALG must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services. However, sources for further policy filters are the IAVMs and the PPSM requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to disable unrelated or unneeded application proxy services. Obtain documentation for which applications are approved/disapproved for optimization by the organization. Navigate to the device Management Console Navigate to Optimize >> Optimization Verify that the approved or disapproved applications are enabled or disabled according to organization requirements. If optimization features are not enabled or disabled according to the organizations requirements, this is a finding.

## Group: SRG-NET-000164-ALG-000100

**Group ID:** `V-238507`

### Rule: The Riverbed Optimization System (RiOS) that provides intermediary services for TLS must validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-238507r654968_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that RiOS is configured to validate certificates used for TLS functions by performing certificate path validation. Navigate to the device Management Console. Navigate to Configure >> Optimization >> CRL Management. Verify that "Enable Automatic CRL Polling For CAs" and "Enable Automatic CRL Polling For Peering CAs" is checked. If "Enable Automatic CRL Polling For CAs" and/or "Enable Automatic CRL Polling For Peering CAs" is not set, this is a finding.

## Group: SRG-NET-000230-ALG-000113

**Group ID:** `V-238508`

### Rule: The Riverbed Optimization System (RiOS) must protect the authenticity of communications sessions by configuring securing pairing trusts for SSL and secure protocols.

**Rule ID:** `SV-238508r654971_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This authenticity protection control focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the Riverbed Optimization System (RiOS) is configured to support TLS version 1.1 as a minimum and preferably TLS version 1.2. Navigate to the device Management Console. Navigate to Configure >> Optimization >> Advanced. Verify that "Peer Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Client Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" Verify that "Server Ciphers:" "Rank 1" contains the following string: "TLSv1.2+FIPS:kRSA+FIPS:!eNULL:!aNULL" If any of the above Ciphers contains strings or groups other than what is listed, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-264432`

### Rule: The Riverbed ALG must be using a version supported by the vendor.

**Rule ID:** `SV-264432r992093_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

