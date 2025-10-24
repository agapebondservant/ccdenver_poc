# STIG Benchmark: F5 BIG-IP TMOS VPN Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000074-VPN-000250

**Group ID:** `V-266277`

### Rule: The F5 BIG-IP appliance must be configured to use a Diffie-Hellman (DH) Group of 16 or greater for Internet Key Exchange (IKE) Phase 1.

**Rule ID:** `SV-266277r1024911_rule`
**Severity:** high

**Description:**
<VulnDiscussion>NIST cryptographic algorithms approved by NSA to protect NSS. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the CSfC program, the approved algorithms have been changed to more stringent protocols configure with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm Suite (CNSA Suite) replaces Suite B.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the IKE Peer Name. 5. In "IKE Phase 1 Algorithms", verify "MODP4096" or higher is selected for "Perfect Forward Secrecy". If the BIG-IP appliance is not configured to use a Diffie-Hellman (DH) Group of 16 or greater for Internet Key Exchange (IKE) Phase 1, this is a finding.

## Group: SRG-NET-000317-VPN-001090

**Group ID:** `V-266278`

### Rule: The F5 BIG-IP appliance IPsec VPN Gateway must use AES256 or higher encryption for the Internet Key Exchange (IKE) proposal to protect confidentiality of remote access sessions.

**Rule ID:** `SV-266278r1024913_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, NIST has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the Name of the IKE peer. 5. Verify an AES256 encryption algorithm is selected under IKE Phase 1 Algorithms >> Encryption Algorithm. If the BIG-IP appliance is not configured to use AES256 or greater encryption for the IKE proposal, this is a finding.

## Group: SRG-NET-000525-VPN-002330

**Group ID:** `V-266279`

### Rule: The F5 BIG-IP appliance IPsec VPN must use AES256 or greater encryption for the IPsec proposal.

**Rule ID:** `SV-266279r1024915_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. A block cipher mode is an algorithm that features the use of a symmetric key block cipher algorithm to provide an information service, such as confidentiality or authentication. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, NIST has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click on the Name of the IPsec Policy. 5. Verify an AES256 or greater encryption algorithm is selected. If the BIG-IP appliance is not configured to use AES256 or greater encryption for the IPsec proposal, this is a finding.

## Group: SRG-NET-000019-VPN-000040

**Group ID:** `V-266280`

### Rule: The F5 BIG-IP appliance IPsec VPN must ensure inbound and outbound traffic is configured with a security policy.

**Rule ID:** `SV-266280r1024917_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. VPN traffic received from another enclave with different security policy or level of trust must not bypass be inspected by the firewall before being forwarded to the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click on IPsec Policy for site to site IPsec. 5. Verify that "ESP" is selected in the IPsec Protocol section. If the BIG-IP is not configured to ensure inbound and outbound traffic is configured with a security policy in compliance with information flow control policies, this is a finding.

## Group: SRG-NET-000512-VPN-002220

**Group ID:** `V-266281`

### Rule: The F5 BIG-IP appliance IPsec VPN Gateway must use Internet Key Exchange (IKE) for IPsec VPN Security Associations (SAs).

**Rule ID:** `SV-266281r1024756_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without IKE, the SPI is manually specified for each security association. IKE peers will negotiate the encryption algorithm and authentication or hashing methods as well as generate the encryption keys. An IPsec SA is established using either IKE or manual configuration. When using IKE, the security associations are established when needed and expire after a period of time or volume of traffic threshold. If manually configured, they are established as soon as the configuration is complete at both end points and they do not expire. When using IKE, the Security Parameter Index (SPI) for each security association is a pseudo-randomly derived number. With manual configuration of the IPsec security association, both the cipher key and authentication key are static. Hence, if the keys are compromised, the traffic being protected by the current IPsec tunnel can be decrypted as well as traffic in any future tunnels established by this SA. Furthermore, the peers are not authenticated prior to establishing the SA, which could result in a rogue device establishing an IPsec SA with either of the VPN end points. IKE provides primary authentication to verify the identity of the remote system before negotiation begins. This feature is lost when the IPsec security associations are manually configured, which results in a nonterminating session using static pre-shared keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. Manual Security Associations. 4. Verify there are no Manual Security Associations listed. If the BIG-IP appliance is not configured to use IKE for IPsec VPN SAs, this is a finding.

## Group: SRG-NET-000132-VPN-000460

**Group ID:** `V-266282`

### Rule: The IPsec BIG-IP appliance must use IKEv2 for IPsec VPN security associations.

**Rule ID:** `SV-266282r1024757_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Use of IKEv2 leverages denial of service (DoS) protections because of improved bandwidth management and leverages more secure encryption algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the name of the IKE peer. 5. Verify "Version 2" is selected for "Version". If the BIG-IP appliance is not configured to use IKEv2 for IPsec VPN security associations, this is a finding.

## Group: SRG-NET-000337-VPN-001290

**Group ID:** `V-266283`

### Rule: The F5 BIG-IP appliance IPsec VPN Gateway must renegotiate the IPsec Phase 1 security association after eight hours or less.

**Rule ID:** `SV-266283r1024758_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IPsec security association (SA) and its corresponding key will expire either after the number of seconds or amount of traffic volume has exceeded the configured limit. A new SA is negotiated before the lifetime threshold of the existing SA is reached to ensure that a new SA is ready for use when the old one expires. The longer the lifetime of the IPsec SA, the longer the lifetime of the session key used to protect IP traffic. The SA is less secure with a longer lifetime because an attacker has a greater opportunity to collect traffic encrypted by the same key and subject it to cryptanalysis. However, a shorter lifetime causes IPsec peers to renegotiate Phase II more often resulting in the expenditure of additional resources. Specify the lifetime (in seconds) of an Internet Key Exchange (IKE) SA. When the SA expires, it is replaced by a new SA, the security parameter index (SPI), or terminated if the peer cannot be contacted for renegotiation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the Name of the IKE peer. 5. Verify that the value for "Lifetime" under "IKE Phase 1 Algorithms" is set to 480 minutes or less, or an organization-defined time period. If the BIG-IP appliance is not configured to renegotiate the security association after 8 hours or less, or an organization-defined period, this is a finding.

## Group: SRG-NET-000337-VPN-001300

**Group ID:** `V-266284`

### Rule: The F5 BIG-IP appliance IPsec VPN must renegotiate the IKE Phase 2 security association after eight hours or less.

**Rule ID:** `SV-266284r1024759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a VPN gateway creates an IPsec Security Association (SA), resources must be allocated to maintain the SA. These resources are wasted during periods of IPsec endpoint inactivity, which could result in the gateway’s inability to create new SAs for other endpoints, thereby preventing new sessions from connecting. The Internet Key Exchange (IKE) idle timeout may also be set to allow SAs associated with inactive endpoints to be deleted before the SA lifetime has expired, although this setting is not recommended at this time. The value of one hour or less is a common best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click on the name of the IPsec Policy. 5. Verify that the value for "Lifetime" under "IKE Phase 2" is set to 480 minutes or less. If the BIG-IP appliance is not configured to renegotiate the security association after 8 hours or less, this is a finding.

## Group: SRG-NET-000400-VPN-001940

**Group ID:** `V-266285`

### Rule: For accounts using password authentication, the F5 BIG-IP appliance site-to-site IPsec VPN Gateway must use SHA-2 or later protocol to protect the integrity of the password authentication process.

**Rule ID:** `SV-266285r1024760_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Use of passwords for authentication is intended only for limited situations and must not be used as a replacement for two-factor CAC-enabled authentication. Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DOD systems must not be configured to use SHA-2 for integrity of remote access sessions. The information system must specify the hash algorithm used for authenticating passwords. Implementation of this requirement requires configuration of FIPS-approved cipher block algorithm and block cipher modes for encryption. Pre-shared key cipher suites may only be used in networks where both the client and server belong to the same organization. Cipher suites using pre-shared keys must not be used with TLS 1.0 or 1.1 and must not be used with TLS 1.2 when a government client or server communicates with nongovernment systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the Name of the IKE peer. 5. Verify that the value for "Authentication Algorithm" under "IKE Phase 1 Algorithms" is set to "SHA-256" or higher. If the BIG-IP appliance is not configured to use SHA-2 or later protocol to protect the integrity of the password authentication process, this is a finding.

## Group: SRG-NET-000565-VPN-002400

**Group ID:** `V-266286`

### Rule: The F5 BIG-IP appliance IPsec VPN must use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-266286r1024761_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. The VPN gateway must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. NIST cryptographic algorithms approved by NSA to protect NSS. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the CSfC program, the approved algorithms have been changed to more stringent protocols configure with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm Suite (CNSA Suite) replaces Suite B.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the name of the IKE peer. 5. Verify that "IKE Phase 1 Algorithms" use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network. From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click on the name of the IPsec Policy. 5. Verify that "IKE Phase 2" use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network. If the BIG-IP appliance is not configured to use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network, this is a finding.

## Group: SRG-NET-000230-VPN-000780

**Group ID:** `V-266287`

### Rule: The F5 BIG-IP appliance IPsec VPN must be configured to use FIPS-validated SHA-2 or higher for Internet Key Exchange (IKE).

**Rule ID:** `SV-266287r1024762_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DOD systems must not be configured to use SHA-2 for integrity of remote access sessions. This requirement is applicable to the configuration of IKE Phase 1 and Phase 2.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IKE Peers. 4. Click on the name of the IKE peer. 5. Verify "SHA-1" or "MD5" is not selected for the following: IKE Phase 1 Algorithms >> Authentication Algorithm IKE Phase 1 Algorithms >> Pseudo-Random Function From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click the name of the IPsec Policy. 5. Verify "SHA-1" is not selected for the following: IKE Phase 2 >> Authentication Algorithm If the BIG-IP appliance is not configured to use FIPS-validated SHA-2 or higher for IKE, this is a finding.

## Group: SRG-NET-000371-VPN-001640

**Group ID:** `V-266288`

### Rule: The F5 BIG-IP appliance IPsec VPN Gateway must specify Perfect Forward Secrecy (PFS) during Internet Key Exchange (IKE) negotiation.

**Rule ID:** `SV-266288r1024921_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PFS generates each new encryption key independently from the previous key. Without PFS, compromise of one key will compromise all communications. The phase 2 (Quick Mode) Security Association (SA) is used to create an IPsec session key. Hence, its rekey or key regeneration procedure is very important. The phase 2 rekey can be performed with or without PFS. With PFS, every time a new IPsec Security Association is negotiated during the Quick Mode, a new Diffie-Hellman (DH) exchange occurs. The new DH shared secret will be included with original keying material (SYKEID_d, initiator nonce, and responder nonce) from phase 1 for generating a new IPsec session key. If PFS is not used, the IPsec session key will always be completely dependent on the original keying material from the Phase-1. Hence, if an older key is compromised at any time, it is possible that all new keys may be compromised. The DH exchange is performed in the same manner as was done in phase 1 (Main or Aggressive Mode). However, the phase 2 exchange is protected by encrypting the phase 2 packets with the key derived from the phase 1 negotiation. Because DH negotiations during phase 2 are encrypted, the new IPsec session key has an added element of secrecy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. IPsec. 3. IPsec Policies. 4. Click on the name of the IPsec Policy. 5. Verify "NONE" is not selected in "IKE Phase 2 >> Perfect Forward Secrecy". If the BIG-IP appliance is not configured to specify PFS during IKE negotiation, this is a finding.

