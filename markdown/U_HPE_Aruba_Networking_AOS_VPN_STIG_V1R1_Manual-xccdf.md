# STIG Benchmark: HPE Aruba Networking AOS VPN Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000371-VPN-001640

**Group ID:** `V-266982`

### Rule: AOS, when used as an IPsec VPN Gateway, must specify Perfect Forward Secrecy (PFS) during Internet Key Exchange (IKE) negotiation.

**Rule ID:** `SV-266982r1040712_rule`
**Severity:** high

**Description:**
<VulnDiscussion>PFS generates each new encryption key independently from the previous key. Without PFS, compromise of one key will compromise all communications. The phase 2 (Quick Mode) Security Association (SA) is used to create an IPsec session key. Hence, its rekey or key regeneration procedure is very important. The phase 2 rekey can be performed with or without Perfect Forward Secrecy (PFS). With PFS, every time a new IPsec Security Association is negotiated during the Quick Mode, a new Diffie-Hellman (DH) exchange occurs. The new DH shared secret will be included with original keying material (SYKEID_d, initiator nonce, and responder nonce} from phase 1 for generating a new IPsec session key. If PFS is not used, the IPsec session key will always be completely dependent on the original keying material from the Phase-1. Hence, if an older key is compromised at any time, it is possible that all new keys may be compromised. The DH exchange is performed in the same manner as was done in phase 1 (Main or Aggressive Mode). However, the phase 2 exchange is protected by encrypting the phase 2 packets with the key derived from the phase 1 negotiation. Because DH negotiations during phase 2 are encrypted, the new IPsec session key has an added element of secrecy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show crypto-local ipsec-map If each active IPsec map does not show PFS enabled, this is a finding.

## Group: SRG-NET-000063-VPN-000220

**Group ID:** `V-266983`

### Rule: AOS, when used as a VPN Gateway, must be configured to use IPsec with SHA-2 at 384 bits or greater for hashing to protect the integrity of remote access sessions.

**Rule ID:** `SV-266983r1040715_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without strong cryptographic integrity protections, information can be altered by unauthorized users without detection. SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. DOD systems must not be configured to use SHA-1 for integrity of remote access sessions. The remote access VPN provides access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Satisfies: SRG-NET-000063-VPN-000220, SRG-NET-000074-VPN-000250, SRG-NET-000168-VPN-000600, SRG-NET-000230-VPN-000780</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify the AOS configuration with the following command: show crypto-local ipsec-map Note the IKEv2 Policy number for each configured map. 2. For each configured policy number, run the following command: show crypto isakmp policy <IKEv2 Policy #> If each configured IKEv2 policy hash algorithm is not configured with SHA-2 at 384 bit, this is a finding.

## Group: SRG-NET-000164-VPN-000560

**Group ID:** `V-266984`

### Rule: AOS, when used as a VPN Gateway and using public key infrastructure (PKI)-based authentication, must validate certificates by constructing a certification path (which includes status information) to an accepted trust anchor.

**Rule ID:** `SV-266984r1040891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. To meet this requirement, the information system must create trusted channels between itself and remote trusted authorized IT product (e.g., syslog server) entities that protect the confidentiality and integrity of communications. The information system must create trusted paths between itself and remote administrators and users that protect the confidentiality and integrity of communications. A trust anchor is an authoritative entity represented via a public key and associated data. It is most often used in the context of public key infrastructures, X.509 digital certificates, and Domain Name System Security Extensions (DNSSEC). However, applications that do not use a trusted path are not approved for nonlocal and remote management of DOD information systems. Use of SSHv2 to establish a trusted channel is approved. Use of FTP, TELNET, HTTP, and SNMPV1 is not approved because they violate the trusted channel rule set. Use of web management tools that are not validated by common criteria may also violate the trusted channel rule set. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a certificate authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify the AOS configuration with the following command: show crypto-local pki trusted CA 2. Note the name(s) of each trust CA. show crypto-local pki trustedCA <name> 3. Verify that each trusted CA is a valid DOD PKI CA. If the trusted CAs are not DOD PKI or no DOD PKI CAs are present, this is a finding.

## Group: SRG-NET-000317-VPN-001090

**Group ID:** `V-266985`

### Rule: AOS, when used as an IPsec VPN Gateway, must use Advanced Encryption Standard (AES) encryption for the Internet Key Exchange (IKE) proposal to protect confidentiality of remote access sessions.

**Rule ID:** `SV-266985r1040721_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. AES is the Federal Information Processing Standard (FIPS)-validated cipher block cryptographic algorithm approved for use in DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, the National Institute of Standards and Technology (NIST) has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW. Satisfies: SRG-NET-000317-VPN-001090, SRG-NET-000371-VPN-001650, SRG-NET-000400-VPN-001940, SRG-NET-000525-VPN-002330</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Verify the AOS configuration with the following commands: show crypto-local ipsec-map Note the IKEv2 Policy number for each configured map. 2. For each configured policy number, run the following command: show crypto isakmp policy <IKEv2 Policy #> If each configured IKEv2 policy is not configured with AES256 or greater encryption, this is a finding.

## Group: SRG-NET-000352-VPN-001460

**Group ID:** `V-266986`

### Rule: AOS, when used as a VPN Gateway, must use an approved Commercial Solution for Classified (CSfC) when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-266986r1040894_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The National Security Agency/Central Security Service's (NSA/CSS) CSfC program enables commercial products to be used in layered solutions to protect classified National Security Systems (NSS) data. Currently, Suite B cryptographic algorithms are specified by the National Institute of Standards and Technology (NIST) and are used by the NSA's Information Assurance Directorate in solutions approved for protecting classified and unclassified NSS. However, quantum-resistant algorithms will be required for future required Suite B implementations. Satisfies: SRG-NET-000352-VPN-001460, SRG-NET-000565-VPN-002390, SRG-NET-000565-VPN-002400</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If AOS is not being used for CSFC, this requirement is not applicable. 1. Verify the AOS configuration with the following command: show crypto-local ipsec-map Note the IKEv2 Policy number for each configured map. 2. For each configured policy number, run the following command: show crypto isakmp policy <IKEv2 Policy #> 3. Verify each configured transform-set by running the following command: show crypto ipsec transform-set If the configured IPsec map, ISAKMP policy, and transform-set do not contain the following, this is a finding: ECDCA 384 certificate IKEv2 policy with AES256, SHA-384, ECDSA-384, Group 20 Transform set with AES-256-GCM

## Group: SRG-NET-000148-VPN-000540

**Group ID:** `V-266987`

### Rule: AOS, when used as a VPN Gateway, must uniquely identify all network-connected endpoint devices before establishing a connection.

**Rule ID:** `SV-266987r1040727_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions. This requirement applies to applications that connect locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers outside a datacenter, Voice Over Internet Protocol [VoIP] phones, and video teleconference codecs). Gateways and service-oriented architecture (SOA) applications are examples of where this requirement would apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: 1. Site-to-site VPN: Using the CLI: show crypto isakmp sa If the IPsec security association is not operating with certificates ("-c"), this is a finding. 2. Hardware client VPN: Using the web GUI, navigate to Configuration >> Access Points >> Remote APs. Review each provisioned Remote Access Point (RAP) and verify that each AP has "c" in the FLAGS column. If certificate authentication is not configured for each RAP, this is a finding.

## Group: SRG-NET-000343-VPN-001370

**Group ID:** `V-266988`

### Rule: AOS, when used as a VPN Gateway, must authenticate all network-connected endpoint devices before establishing a connection.

**Rule ID:** `SV-266988r1040893_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC codecs). Gateways and SOA applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific preauthorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: 1. Site-to-site VPN: Using the CLI: show crypto isakmp sa If the IPsec security association is not operating with certificates ("-c"), this is a finding. 2. Hardware client VPN: Using the web GUI, navigate to Configuration >> Access Points >> Remote APs. Review each provisioned RAP and verify that each AP has "c" in the FLAGS column. If certificate authentication is not configured for each RAP, this is a finding.

## Group: SRG-NET-000041-VPN-000110

**Group ID:** `V-266989`

### Rule: The Remote Access VPN Gateway and/or client must display the Standard Mandatory DOD Notice and Consent Banner before granting remote access to the network.

**Rule ID:** `SV-266989r1040733_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the network ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. In most VPN implementations, the banner is configured in the management backplane (NDM Security Requirements Guide) and serves as the presentation for the VPN client connection as well as for administrator logon to the device management tool/backplane. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to VPN gateways that have the concept of a user account and have the logon function residing on the VPN gateway. The banner must be formatted in accordance with applicable DOD policy. Use the following verbiage for VPN gateways that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't." Satisfies: SRG-NET-000041-VPN-000110, SRG-NET-000042-VPN-000120, SRG-NET-000043-VPN-000130</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show bannervia If the Standard Mandatory DOD Notice and Consent Banner is not set, this is a finding.

## Group: SRG-NET-000213-VPN-000720

**Group ID:** `V-266990`

### Rule: AOS, when used as a VPN Gateway, must terminate all network connections associated with a communications session at the end of the session.

**Rule ID:** `SV-266990r1040736_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Idle Transmission Control Protocol (TCP) sessions can be susceptible to unauthorized access and hijacking attacks. By default, routers do not continually test whether a previously connected TCP endpoint is still reachable. If one end of a TCP connection idles out or terminates abnormally, the opposite end of the connection may still believe the session is available. These "orphaned" sessions use up valuable router resources and can be hijacked by an attacker. To mitigate this risk, routers must be configured to send periodic keep-alive messages to check that the remote end of a session is still connected. If the remote device fails to respond to the TCP keep-alive message, the sending router will clear the connection and free resources allocated to the session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show configuration effective | include dpd If DPD is not configured, this is a finding.

## Group: SRG-NET-000132-VPN-000480

**Group ID:** `V-266991`

### Rule: For site-to-site VPN implementations using AOS, the Layer 2 Tunneling Protocol (L2TP) must be blocked or denied at the security boundary with the private network so unencrypted L2TP packets cannot traverse into the private network of the enclave.

**Rule ID:** `SV-266991r1040739_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unlike Generic Routing Encapsulation (GRE) (a simple encapsulating header), L2TP is a full-fledged communications protocol with control channel, data channels, and a robust command structure. In addition to Point-to-Point Protocol (PPP), other link layer types (called pseudowires) can be and are defined for delivery in L2TP by separate Internet Engineering Task Force Request for Comments (RFC) documents. Further complexity is created by the capability to define vender-specific parameters beyond those defined in the L2TP specifications. The endpoint devices of an L2TP connection can be an L2TP Access Concentrator (LAC), in which case it inputs/outputs the layer 2 protocol to/from the L2TP tunnel. Otherwise, it is an L2TP Network Server (LNS), in which case it inputs/outputs the layer 3 (IP) protocol to/from the L2TP tunnel. The specifications describe three reference models: LAC-LNS, LAC-LAC, and LNS-LNS, the first of which is the most common case. The LAC-LNS model allows a remote access user to reach their home network or internet service provider from a remote location. The remote access user connects to a LAC device, which tunnels the connection home to a waiting LNS. The LAC could also be located on the remote user's laptop, which connects to an LNS at home using a generic internet connection. The other reference models may be used for more obscure scenarios. Although the L2TP protocol does not contain encryption capability, it can be operated over IPsec, which would provide authentication and confidentiality. A remote user in the LAC-LNS model would most likely obtain a dynamically assigned IP address from the home network to ultimately use through the tunnel back to the home network. The outer IP source address used to send the L2TP tunnel packet to the home network is likely to be unknown or highly variable. Also, because the LNS provides the remote user with a dynamic IP address, the firewall at the home network would have to be dynamically updated to accept this address in conjunction with the outer tunnel address. There is also the issue of authentication of the remote user prior to divulging an acceptable IP address. Because of all of these complications, the strict filtering rules applied to the IP-in-IP and GRE tunneling cases will likely not be possible in the L2TP scenario. In addition to the difficulty of enforcing addresses and endpoints (as explained above), the L2TP protocol itself is a security concern if allowed through a security boundary. In particular: 1. L2TP potentially allows link layer protocols to be delivered from afar. These protocols were intended for link-local scope only and are less defended and not as well known. 2. The L2TP tunnels can carry IP packets that are very difficult to see and filter because of the additional layer 2 overhead. 3. L2TP is highly complex and variable (vender-specific variability) and therefore would be a viable target that is difficult to defend. It is better left outside of the main firewall where less damage occurs if the L2TP-processing node is compromised. 4. Filtering cannot be used to detect and prevent other unintended layer 2 protocols from being tunneled. The strength of the application layer code would have to be relied on to achieve this task. 5. Regardless of whether the L2TP is handled inside or outside of the main network, a secondary layer of IP filtering is required; therefore, bringing it inside does not save resources. It is not recommended to allow unencrypted L2TP packets across the security boundary into the network's protected areas. Reference the Backbone Transport STIG for additional L2TP guidance and use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show ip access-list vpnlogon show firewall-cp If L2TP or UDP 1701 are permitted, this is a finding.

## Group: SRG-NET-000019-VPN-000040

**Group ID:** `V-266992`

### Rule: AOS, when used as a VPN Gateway, must ensure inbound and outbound traffic is configured with a security policy in compliance with information flow control policies.

**Rule ID:** `SV-266992r1040904_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic, which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. VPN traffic received from another enclave with different security policy or level of trust must not bypass being inspected by the firewall before being forwarded to the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show running-config | begin "interface gigabit" Note the configured IP access-group session ACL for each active interface. For each configured ACL: show ip access-list <ACL name> If each ACL does not end in an "any any deny log" for both IPv4 and IPv6, this is a finding.

## Group: SRG-NET-000053-VPN-000170

**Group ID:** `V-266993`

### Rule: AOS, when used as a VPN Gateway, must limit the number of concurrent sessions for user accounts to one or to an organization-defined number.

**Rule ID:** `SV-266993r1040745_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VPN gateway management includes the ability to control the number of users and user sessions that utilize a VPN gateway. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to denial-of-service attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based on mission needs and the operational environment for each system. The intent of this policy is to ensure the number of concurrent sessions is deliberately set to a number based on the site's mission and not left unlimited.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show running-config | begin "user-role <vpn user role>" If the vpn user role is not configured to max-sessions 1 (or an organization-defined number), this is a finding.

## Group: SRG-NET-000166-VPN-000580

**Group ID:** `V-266994`

### Rule: The Remote Access VPN Gateway must use a separate authentication server (e.g., Lightweight Directory Access Protocol [LDAP], Remote Authentication Dial-In User Service [RADIUS], Terminal Access Controller Access-Control System+ [TACACS+] to perform user authentication.

**Rule ID:** `SV-266994r1040748_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VPN interacts directly with public networks and devices and should not contain user authentication information for all users. Authentication, Authorization, and Accounting (AAA) network security services provide the primary framework through which a network administrator can set up access control and authorization on network points of entry or network access servers. It is not advisable to configure access control on the VPN gateway or remote access server. Separation of services provides added assurance to the network if the access control server is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show aaa authentication via auth-profile Note each referenced VIA authentication profile. For each referenced VIA authentication profile: show aaa authentication via auth-profile <name> Note the server-group. For each server-group: show aaa server-group <name> If the remote access authentication profile is not set to use a separate authentication server, this is a finding.

## Group: SRG-NET-000138-VPN-000490

**Group ID:** `V-266995`

### Rule: The VPN Gateway must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-266995r1040751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals' in-group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN or proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management). Satisfies: SRG-NET-000138-VPN-000490, SRG-NET-000166-VPN-000590, SRG-NET-000341-VPN-001350</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show aaa authentication via connection-profile Note each referenced VIA connection profile. For each referenced connection profile: show aaa authentication via connection-profile <name> | include "IKEv2 Authentication method" If the authentication method is not set to "eap-tls", this is a finding.

## Group: SRG-NET-000213-VPN-000721

**Group ID:** `V-266996`

### Rule: The Remote Access VPN Gateway must terminate remote access network connections after an organization-defined time period.

**Rule ID:** `SV-266996r1040892_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is in response to the DOD Office of Inspector General Audit of Maintaining Cybersecurity in the Coronavirus Disease-2019 Telework Environment. Best practice is to terminate inactive user sessions after a period; however, when setting timeouts to any VPN connection, the organization must consider the risk to the mission and the purpose of the VPN. VPN connections that provide user access to the network are the prime candidates for VPN session termination and are the primary focus of this requirement. To determine if and when the VPN connections warrant termination, the organization must perform a risk assessment to identify the use case for the VPN and determine if periodic VPN session termination puts the mission at significant risk. The organization must document the results and the determination of the risk assessment in the VPN section of the System Security Plan. The organization must also configure VPN session terminations in accordance with the risk assessment. Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. Quickly terminating an idle session will also free up resources committed by the managed network element. Terminating network connections associated with communications sessions includes, for example, deallocating associated TCP/IP address/port pairs at the operating system level and deallocating networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. This requirement applies to any network element that tracks individual sessions (e.g., stateful inspection firewall, ALG, or VPN).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show aaa authentication via connection-profile Note each referenced VIA connection profile. For each referenced connection profile: show aaa authentication via connection-profile <name> | include "VIA max session timeout" If the max session timeout is not set to the organization-defined time, this is a finding.

## Group: SRG-NET-000337-VPN-001300

**Group ID:** `V-266997`

### Rule: AOS, when used as a VPN Gateway, must renegotiate the security association after 24 hours or less or as defined by the organization.

**Rule ID:** `SV-266997r1040757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a VPN gateway creates an IPsec security association (SA), resources must be allocated to maintain the SA. These resources are wasted during periods of IPsec endpoint inactivity, which could result in the gateway's inability to create new SAs for other endpoints, thereby preventing new sessions from connecting. The Internet Key Exchange (IKE) idle timeout may also be set to allow SAs associated with inactive endpoints to be deleted before the SA lifetime has expired, although this setting is not recommended at this time. The value of one hour or less is a common best practice. Satisfies: SRG-NET-000337-VPN-001300, SRG-NET-000337-VPN-001290</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show crypto-local ipsec-map show crypto dynamic-map If the configured IPSec maps are not configured to support a security association lifetime of 28,800 seconds (8 hours), this is a finding.

## Group: SRG-NET-000132-VPN-000470

**Group ID:** `V-266998`

### Rule: The Remote Access VPN Gateway must be configured to prohibit Point-to-Point Tunneling Protocol (PPTP) and Layer 2 Forwarding (L2F).

**Rule ID:** `SV-266998r1040760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PPTP and L2F are obsolete methods for implementing virtual private networks. Both protocols may be easy to use and readily available, but they have many well-known security issues and exploits. Encryption and authentication are both weak.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show ip access-list vpnlogon show firewall-cp If PPTP or TCP 1723 are permitted, this is a finding.

## Group: SRG-NET-000205-VPN-000710

**Group ID:** `V-266999`

### Rule: AOS, when used as a VPN Gateway, must be configured to route sessions to an intrusion detection and prevention system (IDPS) for inspection.

**Rule ID:** `SV-266999r1040763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, that lack automated capabilities increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities from a variety of information system components (e.g., servers, workstations, notebook computers, smartphones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show running-config | include default-gateway show running-config | include "ipv4 route" show running-config | include "ipv6 route" If any routes exist that do not route sessions to an IDPS for inspection, this is a finding.

## Group: SRG-NET-000369-VPN-001620

**Group ID:** `V-267000`

### Rule: AOS, when used as a VPN Gateway, must disable split-tunneling for remote client VPNs.

**Rule ID:** `SV-267000r1040766_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. A VPN hardware or software client with split tunneling enabled provides an unsecured backdoor to the enclave from the internet. With split tunneling enabled, a remote client has access to the internet while at the same time has established a secured path to the enclave via an IPsec tunnel. A remote client connected to the internet that has been compromised by an attacker on the internet provides an attack base to the enclave's private network via the IPsec tunnel. Hence, it is imperative that the VPN gateway enforces a no split-tunneling policy to all remote clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show wlan virtual-ap For each active WLAN virtual-ap profile: show wlan virtual-ap <name> | include "Forward mode" show ap system-profile For each active AP system-profile: show ap system-profile <name> | include "Double Encrypt" show aaa authentication via connection-profile For each referenced profile: show aaa authentication via connection-profile <name> | include "Enable split tunneling" If any instances of remote access or virtual-ap profile forward mode of split-tunnel are found or if double-encrypt is not enabled per active AP system profile, this is a finding.

## Group: SRG-NET-000512-VPN-002220

**Group ID:** `V-267001`

### Rule: AOS, when used as an IPsec VPN Gateway, must use Internet Key Exchange (IKE) for IPsec VPN security associations (SAs).

**Rule ID:** `SV-267001r1040895_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without IKE, the SPI is manually specified for each security association. IKE peers will negotiate the encryption algorithm and authentication or hashing methods as well as generate the encryption keys. An IPsec SA is established using either IKE or manual configuration. When using IKE, the security associations are established when needed and expire after a period of time or volume of traffic threshold. If manually configured, they are established as soon as the configuration is complete at both end points, and they do not expire. When using IKE, the Security Parameter Index (SPI) for each security association is a pseudo-randomly derived number. With manual configuration of the IPsec security association, both the cipher key and authentication key are static. Hence, if the keys are compromised, the traffic being protected by the current IPsec tunnel can be decrypted as well as traffic in any future tunnels established by this SA. Furthermore, the peers are not authenticated prior to establishing the SA, which could result in a rogue device establishing an IPsec SA with either of the VPN endpoints. IKE provides primary authentication to verify the identity of the remote system before negotiation begins. This feature is lost when the IPsec security associations are manually configured, which results in a nonterminating session using static preshared keys. Satisfies: SRG-NET-000512-VPN-002220, SRG-NET-000132-VPN-000460, SRG-NET-000147-VPN-000530</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show crypto-local ipsec-map If each configured IPsec map is not configured with IKE, this is a finding.

## Group: SRG-NET-000345-VPN-002430

**Group ID:** `V-268313`

### Rule: AOS, when used as a VPN Gateway, must not accept certificates that have been revoked when using PKI for authentication.

**Rule ID:** `SV-268313r1040899_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Situations may arise in which the certificate issued by a certificate authority (CA) may need to be revoked before the lifetime of the certificate expires (for example, when the certificate is known to have been compromised). When an incoming Internet Key Exchange (IKE) session is initiated for a remote client or peer whose certificate is revoked, the revocation list configured for use by the VPN server is checked to determine if the certificate is valid. If the certificate is revoked, IKE will fail, and an IPsec security association will not be established for the remote endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show crypto-local pki rcp If any configured trusted root certificate authorities are not configured to use OCSP, this is a finding.

