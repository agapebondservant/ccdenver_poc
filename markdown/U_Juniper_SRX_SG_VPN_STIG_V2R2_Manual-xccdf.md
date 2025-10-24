# STIG Benchmark: Juniper SRX Services Gateway VPN Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000053

**Group ID:** `V-214668`

### Rule: The Juniper SRX Services Gateway VPN must limit the number of concurrent sessions for user accounts to one (1) and administrative accounts to three (3), or set to an organization-defined number.

**Rule ID:** `SV-214668r382774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network element management includes the ability to control the number of users and user sessions that utilize a network element. Limiting the number of allowed users and sessions per user is helpful in limiting risks related to DoS attacks. This requirement addresses concurrent sessions for information system accounts and does not address concurrent sessions by single users via multiple system accounts. The maximum number of concurrent sessions should be defined based upon mission needs and the operational environment for each system. The intent of this policy is to ensure the number of concurrent sessions is deliberately set to a number based on the site's mission and not left unlimited.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the VPN Internet Key Exchange (IKE) gateway limits concurrent sessions. [edit] show security ike View the value for the connections-limit. If the VPN IKE gateway does not limit the number of concurrent sessions for user accounts to one (1) and administrative accounts to three (3), or is set to an organization-defined number, this is a finding.

## Group: SRG-NET-000517

**Group ID:** `V-214669`

### Rule: The Juniper SRX Services Gateway VPN must renegotiate the IPsec security association after 8 hours or less.

**Rule ID:** `SV-214669r856572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IPsec SA and its corresponding key will expire either after the number of seconds or amount of traffic volume has exceeded the configured limit. A new SA is negotiated before the lifetime threshold of the existing SA is reached to ensure that a new SA is ready for use when the old one expires. The longer the lifetime of the IPsec SA, the longer the lifetime of the session key used to protect IP traffic. The SA is less secure with a longer lifetime because an attacker has a greater opportunity to collect traffic encrypted by the same key and subject it to cryptanalysis. However, a shorter lifetime causes IPsec peers to renegotiate Phase II more often resulting in the expenditure of additional resources. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all IPsec security associations configured globally or within IPsec profiles on the VPN gateway and examine the configured idle time. The default is 3600. [edit] show security ipsec proposal View the value of the lifetime-seconds option. If the IPsec proposal lifetime-seconds are not renegotiated after 8 hours or less of idle time, this is a finding. If the IPsec proposal lifetime-seconds is not configured, this is a finding.

## Group: SRG-NET-000517

**Group ID:** `V-214670`

### Rule: The Juniper SRX Services Gateway VPN must renegotiate the IKE security association after 24 hours or less.

**Rule ID:** `SV-214670r856574_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a VPN gateway creates an IPsec Security Association (SA), resources must be allocated to maintain the SA. These resources are wasted during periods of IPsec endpoint inactivity, which could result in the gateway’s inability to create new SAs for other endpoints, thereby preventing new sessions from connecting. The Internet Key Exchange (IKE) idle timeout may also be set to allow SAs associated with inactive endpoints to be deleted before the SA lifetime has expired, although this setting is not recommended at this time. The value of one hour or less is a common best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all IPsec security associations configured globally or within IPsec profiles on the VPN gateway and examine the configured idle time. The idle time value must be one hour or less. If idle time is not configured, determine the default used by the gateway. The default value is 28800 seconds which is compliant. [edit] show security ike proposal View the value of the lifetime-seconds option. If the IKE security associations are not renegotiated after 24 hours or less of idle time, this is a finding.

## Group: SRG-NET-000061

**Group ID:** `V-214671`

### Rule: The Juniper SRX Services Gateway VPN device also fulfills the role of IDPS in the architecture, the device must inspect the VPN traffic in compliance with DoD IDPS requirements.

**Rule ID:** `SV-214671r382780_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated, capabilities increase risk and makes remote user access management difficult at best. Remote access is access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain documentation from the site representative that the Juniper SRX is configured in compliance with the Juniper SRX Services Gateway IDPS STIG. If the device has not been configured to comply with DoD IDPS requirements, this is a finding.

## Group: SRG-NET-000062

**Group ID:** `V-214672`

### Rule: The Juniper SRX Services Gateway VPN must use AES encryption for the IPsec proposal to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-214672r382783_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. The Advance Encryption Standard (AES) encryption is critical to ensuring the privacy of the IPsec session; it is imperative that AES is used for encryption operations. Remote access is access to DoD-non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. While there is much debate about the security and performance of AES, there is a consensus that AES is significantly more secure than other algorithms currently supported by IPsec implementations. AES is available in three key sizes: 128, 192, and 256 bits, versus the 56 bit DES. Therefore, there are approximately 1021 times more AES 128-bit keys than DES 56-bit keys. In addition, AES uses a block size of 128 bits—twice the size of DES or 3DES.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all Internet Key Exchange (IKE) proposals are set to use the AES encryption algorithm. [edit] show security ipsec View the value of the encryption algorithm for each defined proposal. If the value of the encryption algorithm for any IPsec proposal is not set to use an AES algorithm, this is a finding.

## Group: SRG-NET-000062

**Group ID:** `V-214673`

### Rule: The Juniper SRX Services Gateway VPN must use AES encryption for the Internet Key Exchange (IKE) proposal to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-214673r382783_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. The Advance Encryption Standard (AES) algorithm is critical to ensuring the privacy of the IKE session responsible for establishing the security association and key exchange for an IPsec tunnel. AES is used for encryption operations. Remote access is access to DoD-non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless connections. While there is much debate about the security and performance of AES, there is a consensus that AES is significantly more secure than other algorithms currently supported by IPsec implementations. AES is available in three key sizes: 128, 192, and 256 bits, versus the 56 bit DES. Therefore, there are approximately 1021 times more AES 128-bit keys than DES 56-bit keys. In addition, AES uses a block size of 128 bits—twice the size of DES or 3DES.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all IKE proposals are set to use the AES encryption algorithm. [edit] show security ike View the value of the encryption algorithm for each defined proposal. If the value of the encryption algorithm for any IKE proposal is not set to use an AES algorithm, this is a finding.

## Group: SRG-NET-000062

**Group ID:** `V-214674`

### Rule: The Juniper SRX Services Gateway VPN must implement a FIPS-140-2 validated Diffie-Hellman (DH) group.

**Rule ID:** `SV-214674r382783_rule`
**Severity:** medium

**Description:**
<VulnDiscussion> Use of an approved DH algorithm ensures the Internet Key Exchange (IKE) (phase 1) proposal uses FIPS-validated key management techniques and processes in the production, storage, and control of private/secret cryptographic keys. The security of the DH key exchange is based on the difficulty of solving the discrete logarithm in which the key was derived from. Hence, the larger the modulus, the more secure the generated key is considered to be.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all IKE proposals are set to use a FIPS-validated dh-group. [edit] show security ike <P1-PROPOSAL-NAME> View the IKE options dh-group option. If the IKE option is not set to a FIPS-140-2 validated dh-group, this is a finding.

## Group: SRG-NET-000063

**Group ID:** `V-214675`

### Rule: The Juniper SRX Services Gateway VPN must be configured to use IPsec with SHA1 or greater to negotiate hashing to protect the integrity of remote access sessions.

**Rule ID:** `SV-214675r382846_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without strong cryptographic integrity protections, information can be altered by unauthorized users without detection. Remote access VPN provides access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all IPSec proposals are set to use the sha-256 hashing algorithm. [edit] show security ipsec proposal <IPSEC-PROPOSAL-NAME> View the value of the encryption algorithm for each defined proposal. If the value of the encryption algorithm option for all defined proposals is not set to use SHA1 or greater, this is a finding.

## Group: SRG-NET-000019

**Group ID:** `V-214676`

### Rule: The Juniper SRX Services Gateway VPN must ensure inbound and outbound traffic is configured with a security policy in compliance with information flow control policies.

**Rule ID:** `SV-214676r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated, capabilities increase risk and makes remote user access management difficult at best. Remote access is access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets). In phase-2, another negotiation is performed, detailing the parameters for the IPsec connection. New keying material using the Diffie-Hellman key exchange established in phase-1 is used to provide session keys used to protecting the VPN data flow. If Perfect-Forwarding-Secrecy (PFS) is used, a new Diffie-Hellman exchange is performed for each phase-2 negotiation. While this is slower, it makes sure that no keys are dependent on any other previously used keys; no keys are extracted from the same initial keying material. This is to make sure that, in the unlikely event that some key was compromised; no subsequent keys can be derived.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an IPsec policy is configured and used to control the VPN information flow. [edit] show security ipsec Inspect the security policy. If VPN traffic is not configured and controlled using an IPsec policy, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-214677`

### Rule: The Juniper SRX Services Gateway VPN must use Internet Key Exchange (IKE) for IPsec VPN Security Associations (SAs).

**Rule ID:** `SV-214677r385561_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without IKE, the SPI is manually specified for each security association. IKE peers will negotiate the encryption algorithm and authentication or hashing methods as well as generate the encryption keys. An IPsec SA is established using either Internet Key Exchange (IKE) or manual configuration. When using IKE, the security associations are established when needed and expire after a period of time or volume of traffic threshold. If manually configured, they are established as soon as the configuration is complete at both end points and they do not expire. When using IKE, the Security Parameter Index (SPI) for each security association is a pseudo-randomly derived number. With manual configuration of the IPsec security association, both the cipher key and authentication key are static. Hence, if the keys are compromised, the traffic being protected by the current IPsec tunnel can be decrypted as well as traffic in any future tunnels established by this SA. Furthermore, the peers are not authenticated prior to establishing the SA, which could result in a rogue device establishing an IPsec SA with either of the VPN end points. IKE provides primary authentication to verify the identity of the remote system before negotiation begins. This feature is lost when the IPsec security associations are manually configured, which results in a non-terminating session using static pre-shared keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the IKE protocol is specified for all IPsec VPNs. [edit] show security ipsec vpn If the IKE protocol is not specified as an option on all VPN gateways, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-214678`

### Rule: If IDPS inspection is performed separately from the Juniper SRX Services Gateway VPN device, the VPN must route sessions to an IDPS for inspection.

**Rule ID:** `SV-214678r864169_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices, such as those providing remote access to network devices and information systems, which lack automated, capabilities increase risk and makes remote user access management difficult at best. Remote access is access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities, from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Inspect the Juniper SRX configuration or the site's architecture drawings to verify all inbound VPN traffic is routed to the site's intrusion detection system. If all inbound VPN traffic is not inspected by the site's IDPS prior to being routed to its destination, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-214679`

### Rule: The Juniper SRX Services Gateway VPN must not accept certificates that have been revoked when using PKI for authentication.

**Rule ID:** `SV-214679r385561_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Situations may arise in which the certificate issued by a Certificate Authority (CA) may need to be revoked before the lifetime of the certificate expires. For example, the certificate is known to have been compromised. To achieve this, a list of certificates that have been revoked, known as a Certificate Revocation List (CRL), is sent periodically from the CA to the IPsec gateway. When an incoming Internet Key Exchange (IKE) session is initiated for a remote client or peer whose certificate is revoked, the CRL will be checked to see if the certificate is valid; if the certificate is revoked, IKE will fail and an IPsec security association will not be established for the remote endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the CA trust point defined on the VPN gateway to determine if it references a CRL and that revocation check has been enabled. An alternate mechanism for checking the validity of a certificate is the use of the Online Certificate Status Protocol (OCSP). Unlike CRLs, which provide only periodic certificate status checks, OCSP can provide timely information regarding the status of a certificate. If revoked certificates are accepted for PKI authentication, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-214680`

### Rule: The Juniper SRX Services Gateway VPN must specify Perfect Forward Secrecy (PFS).

**Rule ID:** `SV-214680r385561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PFS generates each new encryption key independently from the previous key. Without PFS, compromise of one key will compromise all communications. The phase 2 (Quick Mode) Security Association (SA) is used to create an IPsec session key. Hence, its rekey or key regeneration procedure is very important. The phase 2 rekey can be performed with or without Perfect Forward Secrecy (PFS). With PFS, every time a new IPsec Security Association is negotiated during the Quick Mode, a new Diffie-Hellman (DH) exchange occurs. The new DH shared secret will be included with original keying material (SYKEID_d, initiator nonce, and responder nonce from phase 1) for generating a new IPsec session key. If PFS is not used, the IPsec session key will always be completely dependent on the original keying material from the Phase-1. Hence, if an older key is compromised at any time, it is possible that all new keys may be compromised. The DH exchange is performed in the same manner as was done in phase 1 (Main or Aggressive Mode). However, the phase 2 exchange is protected by encrypting the phase 2 packets with the key derived from the phase 1 negotiation. Because DH negotiations during phase 2 are encrypted, the new IPsec session key has an added element of secrecy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine all IPsec profiles to verify PFS is enabled. [edit] show security ipsec policy If PFS is not configured, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-214681`

### Rule: The Juniper SRX Services Gateway VPN must use Encapsulating Security Payload (ESP) in tunnel mode.

**Rule ID:** `SV-214681r385561_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ESP provides confidentiality, data origin authentication, integrity, and anti-replay services within the IPsec suite of protocols. ESP in tunnel mode ensures a secure path for communications for site-to-site VPNs and gateway to endpoints, including header information. ESP can be deployed in either transport or tunnel mode. Transport mode is used to create a secured session between two hosts. It can also be used when two hosts simply want to authenticate each IP packet with IPsec authentication header (AH). With ESP transport mode, only the payload (transport layer) is encrypted, whereas with tunnel mode, the entire IP packet is encrypted and encapsulated with a new IP header. Tunnel mode is used to encrypt traffic between secure IPsec gateways or between an IPsec gateway and an end-station running IPsec software. Hence, it is the only method to provide a secured path to transport traffic between remote sites or end-stations and the central site.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all IPsec profiles and zones to verify ESP tunnel mode has been specified. [edit] show security ipsec proposal show security zones security-zone untrust If all IPsec proposals are not configured for the ESP protocol, this is a finding. If an Internet Key Exchange (IKE) is not bound to an external host-inbound service to direct all inbound VPN traffic to the VPN interface configured for IKE, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-214682`

### Rule: The Juniper SRX Services Gateway must disable or remove unnecessary network services and functions that are not used as part of its role in the architecture.

**Rule ID:** `SV-214682r382903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the SRX. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Services that may be related security-related, but based on the role of the device in the architecture do not need to be installed. For example, the Juniper SRX can have an Antivirus, Web filter, IDS, or ALG license. However, if these functions are not part of the documented role of the SRX in the enterprise or branch architecture, then these the software and licenses should not be installed on the device. This mitigates the risk of exploitation of unconfigured services or services that are not kept updated with security fixes. If left unsecured, these services may provide a threat vector. Only remove unauthorized services. This control is not intended to restrict the use of Juniper SRX devices with multiple authorized roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation and architecture for the device. <root> show system license If unneeded services and functions are installed on the device, but are not part of the documented role of the device, this is a finding.

## Group: SRG-NET-000132

**Group ID:** `V-214683`

### Rule: The Juniper SRX Services Gateway VPN must use IKEv2 for IPsec VPN security associations.

**Rule ID:** `SV-214683r385486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of IKEv2 leverages DoS protections because of improved bandwidth management and leverages more secure encryption algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only IKEv2 is used for the IKE security configuration on all configured gateways. Use of IKEv1 mitigates the risk to a CAT III finding. Show security ike gateway <VPN-GATEWAY> If IKEv2 is not used for IKE associations, this is a finding.

## Group: SRG-NET-000132

**Group ID:** `V-214684`

### Rule: The Juniper SRX Services Gateway VPN must be configured to prohibit or restrict the use of functions, ports, protocols, and/or services, as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-214684r385486_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The PPSM CAL and vulnerability assessments provide an authoritative source for ports, protocols, and services that are unauthorized or restricted across boundaries on DoD networks. The Juniper SRX must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Entering the following commands from the configuration level of the hierarchy. [edit] show security services If functions, ports, protocols, and services identified on the PPSM CAL are not disabled, this is a finding.

## Group: SRG-NET-000138

**Group ID:** `V-214685`

### Rule: The Juniper SRX Services Gateway VPN must uniquely identify and authenticate organizational users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-214685r385489_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following. (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals in group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN or proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site to identify the VPN access profile. Verify the access profile uses LDAP, not password configuration, for user remote access to the network. Ask the site representative if group accounts are allowed or configured. [edit] show security access profile <VPN-LDAP-PROFILE-NAME> If an access profile that uses LDAP is not configured as the first option in the authentication order, this is a finding. If group accounts are allowed for VPN logon, this is a finding.

## Group: SRG-NET-000140

**Group ID:** `V-214686`

### Rule: The Juniper SRX Services Gateway VPN must use multifactor authentication (e.g., DoD PKI) for network access to non-privileged accounts.

**Rule ID:** `SV-214686r385492_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Use of password for user remote access for non-privileged account is not authorized. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A non-privileged account is any information system account with authorizations of a non-privileged user. Network access is any access to an application by a user (or process acting on behalf of a user) where said access is obtained through a network connection. The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site to identify the VPN access profile. Verify the access profile uses LDAP, not password configuration, for user remote access to the network. Ask the site if the LDAP server used authenticates users through PKI authentication. [edit] show security access profile <dynamic-profile-name> If an access profile that uses LDAP is not configured as the first option in the authentication order, this is a finding. If password access is configured for VPN user access, this is a finding. If the LDAP server used does not use PKI authentication, this is a finding.

## Group: SRG-NET-000168

**Group ID:** `V-214687`

### Rule: The Juniper SRX Services Gateway VPN must use FIPS 140-2 compliant mechanisms for authentication to a cryptographic module.

**Rule ID:** `SV-214687r385516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unapproved mechanisms that are used for authentication to the cryptographic module are not verified, and therefore cannot be relied upon to provide confidentiality or integrity and DoD data may be compromised. Network elements utilizing encryption are required to use FIPS compliant mechanisms for authenticating to cryptographic modules. FIPS 140-2 is the current standard for validating that mechanisms used to access cryptographic modules utilize authentication that meets DoD requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IPsec is defined and configured using FIPS-complaint protocols. [edit] show security ipsec vpn If the IPSEC policy and VP are not configured to use FIPS 140-2 compliant mechanisms for authentication to a cryptographic module, this is a finding.

## Group: SRG-NET-000169

**Group ID:** `V-214688`

### Rule: The Juniper SRX Services Gateway VPN must uniquely identify and authenticate non-organizational users (or processes acting on behalf of non-organizational users).

**Rule ID:** `SV-214688r385519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Lack of authentication and identification enables non-organizational users to gain access to the network or possibly a network element that provides opportunity for intruders to compromise resources within the network infrastructure. This requirement only applies to components where this is specific to the function of the device or has the concept of a non-organizational user.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that groups are not used for authentication. [edit] show security access profile <dynamic-profile-name> If LDAP is not configured as the first authentication-order, this is a finding.

## Group: SRG-NET-000213

**Group ID:** `V-214689`

### Rule: The Juniper SRX Services Gateway VPN must terminate all network connections associated with a communications session at the end of the session.

**Rule ID:** `SV-214689r695324_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Idle TCP sessions can be susceptible to unauthorized access and hijacking attacks. By default, routers do not continually test whether a previously connected TCP endpoint is still reachable. If one end of a TCP connection idles out or terminates abnormally, the opposite end of the connection may still believe the session is available. These “orphaned” sessions use up valuable router resources and can also be hijacked by an attacker. To mitigate this risk, routers must be configured to send periodic keep alive messages to check that the remote end of a session is still connected. If the remote device fails to respond to the TCP keep alive message, the sending router will clear the connection and free resources allocated to the session. The TCP keep-alive for remote access is implemented in the Juniper SRX Firewall STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site representative which proposal implements Suite B. [edit] show security ike gateway <ike-peer-name> View the configured options. If the dead-peer-detection is not configured, this is a finding.

## Group: SRG-NET-000352

**Group ID:** `V-214690`

### Rule: The Juniper SRX Services Gateway VPN Internet Key Exchange (IKE) must use cryptography that is compliant with Suite B parameters when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-214690r856575_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated. RFC 6379 Suite B Cryptographic Suites for IPsec defines four cryptographic user interface suites for deploying IPsec. Each suite provides choices for Encapsulating Security Payload (ESP) and IKE. The four suites are differentiated by the choice of IKE authentication and key exchange, cryptographic algorithm strengths, and whether ESP is to provide both confidentiality and integrity or integrity only. The suite names are based on the Advanced Encryption Standard (AES) mode and AES key length specified for ESP. Two suites are defined for transporting classified information up to SECRET level—one for both confidentiality and integrity and one for integrity only. There are also two suites defined for transporting classified information up to TOP SECRET level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site representative which proposal implements Suite B. [edit] show security ike <suiteb-proposal-name> View the configured options. If the value of the authentication-method and other options are not set for Suite B compliance, this is a finding.

## Group: SRG-NET-000510

**Group ID:** `V-214691`

### Rule: The Juniper SRX Services Gateway VPN IKE must use NIST FIPS-validated cryptography to implement encryption services for unclassified VPN traffic.

**Rule ID:** `SV-214691r856576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The network element must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all Internet Key Exchange (IKE) proposals are set to use the AES encryption algorithm. [edit] show security ike View the value of the encryption algorithm for each defined proposal. If the value of the authentication method and other options are not set to use FIPS-compliant values, this is a finding.

## Group: SRG-NET-000230

**Group ID:** `V-214692`

### Rule: The Juniper SRX Services Gateway VPN must configure Internet Key Exchange (IKE) with SHA1 or greater to protect the authenticity of communications sessions.

**Rule ID:** `SV-214692r383107_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional). An IPsec Security Associations (SA) is established using either IKE or manual configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View all IKE proposals using in the VPN configuration. [edit] show security ike proposal If the authentication algorithm in all IKE proposals is not set to SHA1 or higher, this is a finding.

## Group: SRG-NET-000355

**Group ID:** `V-214693`

### Rule: The Juniper SRX Services Gateway VPN must only allow the use of DoD PKI established certificate authorities for verification of the establishment of protected sessions.

**Rule ID:** `SV-214693r856577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted certificate authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of Internet Key Exchange (IKE) authentication certificates. This requirement focuses on communications protection for the application session rather than for the network packet. Network elements that perform these functions must be able to identify which session identifiers were generated when the sessions were established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the all IKE proposals are set to use the AES encryption algorithm. [edit] show security ike View the value of the authentication-method for each defined proposal. If the value of the authentication-method for each defined proposal is not set to use AES, this is a finding.

## Group: SRG-NET-000364

**Group ID:** `V-214694`

### Rule: The Juniper SRX Services Gateway VPN must only allow incoming VPN communications from organization-defined authorized sources routed to organization-defined authorized destinations.

**Rule ID:** `SV-214694r856578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices, such as firewalls, that control the flow of network traffic, ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet) must be kept separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Request documentation of the Juniper SRX configuration drawings to determine which ports are configured for external/outbound traffic. Verify outbound interfaces have been configured with DoS screens. [edit] show security zones <security-zone-name> If the VPN zone(s) is configured to allow unauthorized/untrusted traffic to unauthorized zones, this is a finding.

## Group: SRG-NET-000369

**Group ID:** `V-214695`

### Rule: The Juniper SRX Services Gateway VPN must disable split-tunneling for remote clients VPNs.

**Rule ID:** `SV-214695r856579_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. A VPN hardware or software client with split tunneling enabled provides an unsecured backdoor to the enclave from the Internet. With split tunneling enabled, a remote client has access to the Internet while at the same time has established a secured path to the enclave via an IPsec tunnel. A remote client connected to the Internet that has been compromised by an attacker in the Internet, provides an attack base to the enclave’s private network via the IPsec tunnel. Hence, it is imperative that the VPN gateway enforces a no split-tunneling policy to all remote clients. Traffic to the protected resource will go through the specified dynamic VPN tunnel and will therefore be protected by the Juniper SRX firewall’s security policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify split-tunneling is disabled. [edit] show security dynamic-vpn access-profile <dynamic-vpn-access-profile> If split-tunneling is not disabled, this is a finding.

## Group: SRG-NET-000147

**Group ID:** `V-214696`

### Rule: The Juniper SRX Services Gateway VPN must use anti-replay mechanisms for security associations.

**Rule ID:** `SV-214696r856580_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Anti-replay is an IPsec security mechanism at a packet level which helps to avoid unwanted users from intercepting and modifying an ESP packet. The SRX adds a sequence number to the ESP encapsulation which is verified by the VPN peer so packets are received within a correct sequence. This will cause issues if packets are not received in the order in which they were sent out. By default the SRX has a replay window of 64 or 32, depending on the platform. The SRX drops packets received out of order that are not received within this window. However, this default may be overridden by setting the option no-anti-replay as follows: set security vpn name ike no-anti-replay.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify anti-replay service is enabled. [edit] show security ipsec security-associations index 16384 detail If anti-replay service is not enabled, this is a finding.

