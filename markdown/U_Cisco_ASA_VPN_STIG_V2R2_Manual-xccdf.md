# STIG Benchmark: Cisco ASA VPN Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000077-VPN-000280

**Group ID:** `V-239945`

### Rule: The Cisco ASA must be configured to generate log records containing information to establish what type of VPN events occurred.

**Rule ID:** `SV-239945r666241_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. VPN gateways often have a separate audit log for capturing VPN status and other information about the traffic (as opposed to the log capturing administrative and configuration actions). Audit record content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the VPN gateway logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured VPN gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if VPN events are logged as shown in the example below. logging class vpn trap notifications logging class vpnc trap notifications logging class vpnfo trap notifications logging class webfo trap notifications logging class webvpn trap notifications logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA is not configured to log entries containing information to establish what type of VPN events occurred, this is a finding.

## Group: SRG-NET-000078-VPN-000290

**Group ID:** `V-239946`

### Rule: The Cisco ASA must be configured to generate log records containing information to establish when the events occurred.

**Rule ID:** `SV-239946r666244_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. VPN gateways often have a separate audit log for capturing VPN status and other information about the traffic (as opposed to the log capturing administrative and configuration actions). Associating event types with detected events in the network audit logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured VPN gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the logging timestamp command has been configured as shown below. logging enable logging timestamp If the ASA is not configured to generate traffic log entries containing information to establish when the events occurred, this is a finding.

## Group: SRG-NET-000336-VPN-001280

**Group ID:** `V-239947`

### Rule: The Cisco ASA must be configured to queue log records locally in the event that the central audit server is down or not reachable.

**Rule ID:** `SV-239947r1001254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the system were to continue processing after audit failure, actions can be taken on the system that cannot be tracked and recorded for later forensic analysis. Because of the importance of ensuring mission/business continuity, organizations may determine that the nature of the audit failure is not so severe that it warrants a complete shutdown of the application supporting the core organizational missions/business operations. In those instances, partial application shutdowns or operating in a degraded mode with reduced capability may be viable alternatives. This requirement only applies to components where this is specific to the function of the device (e.g., IDPS sensor logs, firewall logs). This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ASA is configured to send syslog messages to a TCP-based syslog server, and if the syslog server is down new connections are blocked. To continue to allow new connections and queue log records verify that the logging permit-hostdown and the queue size has been increased (default is 512). logging enable … … … logging queue 8192 logging host NDM_INTERFACE 10.1.22.2 6/1514 logging permit-hostdown If the ASA is not configured to queue log records locally in the event that the central audit server is down or not reachable, this is a finding.

## Group: SRG-NET-000335-VPN-001270

**Group ID:** `V-239948`

### Rule: The Cisco ASA must be configured to generate an alert that can be forwarded as an alert to organization-defined personnel and/or firewall administrator of all log failure events.

**Rule ID:** `SV-239948r878129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Alerts provide organizations with urgent messages. Automated alerts can be conveyed in a variety of ways, including, for example, telephonically, via electronic mail, via text message, or via websites. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. While this requirement also applies to the event monitoring system (e.g., Syslog, Security Information and Event Management [SIEM], or SNMP servers), the VPN Gateway must also be configured to generate a message to the administrator console. The VPN daemon facility and log facility are messages in the log, which capture actions performed or errors encountered by system processes. The ISSM or ISSO may designate the firewall/system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco ASA configuration to verify that it is compliant with this requirement as shown in the example below. logging trap critical logging host NDM_INTERFACE 10.1.48.10 6/1514 Note: The parameter "critical" can replaced with a lesser severity (i.e., error, warning, notice, informational). A logging list can be used as an alternative to the severity level. If the Cisco ASA is not configured to generate an alert that can be forwarded to organization-defined personnel and/or firewall administrator of all log failure events, this is a finding.

## Group: SRG-NET-000164-VPN-000560

**Group ID:** `V-239949`

### Rule: The Cisco ASA must be configured to validate certificates via a trustpoint that identifies a DoD or DoD-approved certificate authority.

**Rule ID:** `SV-239949r666253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without path validation, an informed trust decision by the relying party cannot be made when presented with any certificate not already explicitly trusted. To meet this requirement, the information system must create trusted channels between itself and remote trusted authorized IT product (e.g., syslog server) entities that protect the confidentiality and integrity of communications. The information system must create trusted paths between itself and remote administrators and users that protect the confidentiality and integrity of communications. A trust anchor is an authoritative entity represented via a public key and associated data. It is most often used in the context of public key infrastructures, X.509 digital certificates, and DNSSEC. However, applications that do not use a trusted path are not approved for non-local and remote management of DoD information systems. When there is a chain of trust, usually the top entity to be trusted becomes the trust anchor; it can be, for example, a Certification Authority (CA). A certification path starts with the subject certificate and proceeds through a number of intermediate certificates up to a trusted root certificate, typically issued by a trusted CA. This requirement verifies that a certification path to an accepted trust anchor is used for certificate validation and that the path includes status information. Path validation is necessary for a relying party to make an informed trust decision when presented with any certificate not already explicitly trusted. Status information for certification paths includes certificate revocation lists or online certificate status protocol responses. Validation of the certificate status information is out of scope for this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If PKI certificates are not implemented on the ASA, this requirement is not applicable. Step 1: Review the ASA configuration to determine if a CA trust point has been configured as shown in the example below. crypto ca trustpoint CA_X Step 2: Verify the CA is a DoD or DoD-approved service provider by entering the following command: show crypto ca certificates The output will list the following information for each certificate: Associated Trustpoints: (will map to a configured trustpoint from Step 1) Common Name (CN) of the issuer Organization Unit (OU) of the issuer Organization (O) of the issuer Validity Date If the ASA is not configured to obtain its public key certificates from a DoD or DoD-approved service provider, this is a finding.

## Group: SRG-NET-000512-VPN-002220

**Group ID:** `V-239951`

### Rule: The Cisco ASA must be configured to use Internet Key Exchange (IKE) for all IPsec security associations.

**Rule ID:** `SV-239951r666259_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without IKE, the Security Parameter Index (SPI) is manually specified for each security association. IKE peers will negotiate the encryption algorithm and authentication or hashing methods as well as generate the encryption keys. An IPsec SA is established using either IKE or manual configuration. When using IKE, the security associations are established when needed and expire after a period of time or volume of traffic threshold. If manually configured, they are established as soon as the configuration is complete at both endpoints and they do not expire. When using IKE, the SPI for each security association is a pseudo-randomly derived number. With manual configuration of the IPsec security association, both the cipher key and authentication key are static. Hence, if the keys are compromised, the traffic being protected by the current IPsec tunnel can be decrypted as well as traffic in any future tunnels established by this SA. Furthermore, the peers are not authenticated prior to establishing the SA, which could result in a rogue device establishing an IPsec SA with either of the VPN endpoints. IKE provides primary authentication to verify the identity of the remote system before negotiation begins. This feature is lost when the IPsec security associations are manually configured, which results in a non-terminating session using static pre-shared keys.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that IKE is configured for the IPsec Phase 1 policy and enabled on applicable interfaces. crypto ikev2 policy 1 encryption … crypto ikev2 enable OUTSIDE Step 2: Verify that IKE is configured for the IPsec Phase 2. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp encryption … Note: Although IKEv2 is preferred, IKEv1 will meet the intent of this requirement. If the IKE is not configured for all IPsec security associations, this is a finding.

## Group: SRG-NET-000132-VPN-000460

**Group ID:** `V-239952`

### Rule: The Cisco ASA must be configured to use Internet Key Exchange v2 (IKEv2) for all IPsec security associations.

**Rule ID:** `SV-239952r666262_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. Use of IKEv2 leverages DoS protections because of improved bandwidth management and leverages more secure encryption algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is configured to use IKEv2 for IPsec VPN security associations. Step 1: Verify that IKE is configured for the IPsec Phase 1 policy and enabled on applicable interfaces. crypto ikev2 policy 1 encryption … crypto ikev2 enable OUTSIDE Step 2: Verify that IKE is configured for the IPsec Phase 2. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp encryption … If the ASA is not configured to use IKEv2 for all IPsec VPN security associations, this is a finding.

## Group: SRG-NET-000510-VPN-002180

**Group ID:** `V-239953`

### Rule: The Cisco ASA must be configured to use NIST FIPS-validated cryptography for Internet Key Exchange (IKE) Phase 1.

**Rule ID:** `SV-239953r916122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The VPN gateway must implement cryptographic modules adhering to the higher standards approved by the federal government since this provides assurance they have been tested and validated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA uses a NIST FIPS-validated cryptography for IKE Phase 1 as shown in the example below. crypto ikev2 policy 1 encryption aes-256 If the ASA is not configured to use NIST FIPS-validated cryptography for IKE Phase 1, this is a finding.

## Group: SRG-NET-000371-VPN-001640

**Group ID:** `V-239954`

### Rule: The Cisco ASA must be configured to specify Perfect Forward Secrecy (PFS) for the IPsec Security Association (SA) during IKE Phase 2 negotiation.

**Rule ID:** `SV-239954r916233_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PFS generates each new encryption key independently from the previous key. Without PFS, compromise of one key will compromise all communications. The Phase 2 (Quick Mode) Security Association (SA) is used to create an IPsec session key. Hence, its rekey or key regeneration procedure is very important. The Phase 2 rekey can be performed with or without Perfect Forward Secrecy (PFS). With PFS, every time a new IPsec Security Association is negotiated during the Quick Mode, a new Diffie-Hellman (DH) exchange occurs. The new DH shared secret will be included with original keying material (SYKEID_d, initiator nonce, and responder nonce from Phase 1 for generating a new IPsec session key. If PFS is not used, the IPsec session key will always be completely dependent on the original keying material from Phase 1. Hence, if an older key is compromised at any time, it is possible that all new keys may be compromised. The DH exchange is performed in the same manner as was done in Phase 1 (Main or Aggressive Mode). However, the Phase 2 exchange is protected by encrypting the Phase 2 packets with the key derived from the Phase 1 negotiation. Because DH negotiations during Phase 2 are encrypted, the new IPsec session key has an added element of secrecy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review crypto maps that reference an IPsec proposal. Verify the ASA is configured to specify PFS as shown in the example below. crypto map IPSEC_CRYPTO_MAP 1 set pfs group5 crypto map IPSEC_CRYPTO_MAP 1 set peer x.x.x.x crypto map IPSEC_CRYPTO_MAP 1 set ikev2 ipsec-proposal IPSEC_TRANS If the ASA is not configured to specify PFS for the IPsec SA during IKE Phase 2 negotiation, this is a finding.

## Group: SRG-NET-000510-VPN-002160

**Group ID:** `V-239955`

### Rule: The Cisco ASA must be configured to use a FIPS-validated cryptographic module to generate cryptographic hashes.

**Rule ID:** `SV-239955r916125_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FIPS 140-2/140-3 precludes the use of invalidated cryptography for the cryptographic protection of sensitive or valuable data within federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plain text. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2/140-3 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2/140-3 standard. The cryptographic module used must have at least one validated hash algorithm. This validated hash algorithm must be used to generate cryptographic hashes for all cryptographic security function within the product being evaluated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is configured to use a FIPS-validated cryptographic module to generate cryptographic hashes. Step 1: Verify that a FIPS-validated hash is used for IKE Phase 1 as shown in the example below. crypto ikev2 policy 1 … … … integrity sha384 Step 2: Verify that a FIPS-validated hash is used for the IPsec SA. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp integrity sha-384 If the ASA is not configured to use a FIPS-validated cryptographic module to generate cryptographic hashes, this is a finding.

## Group: SRG-NET-000510-VPN-002170

**Group ID:** `V-239956`

### Rule: The Cisco ASA must be configured to use a FIPS-validated cryptographic module to implement IPsec encryption services.

**Rule ID:** `SV-239956r916128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>FIPS 140-2/140-3 precludes the use of invalidated cryptography for the cryptographic protection of sensitive or valuable data within federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plain text. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2/140-3 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2/140-3 standard. The cryptographic module used must have one FIPS-validated encryption algorithm (i.e., validated Advanced Encryption Standard [AES]). This validated algorithm must be used for encryption for cryptographic security function within the product being evaluated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA uses a FIPS-validated cryptographic module to implement IPsec encryption services. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp encryption aes-256 If the ASA is not configured to use a FIPS-validated cryptographic module to implement IPsec encryption services, this is a finding.

## Group: SRG-NET-000074-VPN-000250

**Group ID:** `V-239957`

### Rule: The Cisco ASA must be configured to use a Diffie-Hellman (DH) Group of 16 or greater for Internet Key Exchange (IKE) Phase 1.

**Rule ID:** `SV-239957r916149_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of an approved DH algorithm ensures the IKE (Phase 1) proposal uses FIPS-validated key management techniques and processes in the production, storage, and control of private/secret cryptographic keys. The security of the DH key exchange is based on the difficulty of solving the discrete logarithm from which the key was derived. Hence, the larger the modulus, the more secure the generated key is considered to be.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if DH Group of 16 or greater has been specified for IKE Phase 1 as shown in the example below. crypto ikev2 policy 1 encryption aes-256 … group 24 If DH Group of 16 or greater has not been specified for IKE Phase 1, this is a finding.

## Group: SRG-NET-000168-VPN-000600

**Group ID:** `V-239958`

### Rule: The Cisco ASA must be configured to use FIPS-validated SHA-2 at 384 bits or higher for Internet Key Exchange (IKE) Phase 1.

**Rule ID:** `SV-239958r916134_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DOD systems should not be configured to use SHA-2 for integrity of remote access sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that SHA-2 at 384 bits or higher is specified for IKE Phase 1 as shown in the example below. crypto ikev2 policy 1 … integrity sha384 If the ASA is not configured to use SHA-2 at 384 bits or higher for IKE Phase 1, this is a finding.

## Group: SRG-NET-000230-VPN-000780

**Group ID:** `V-239959`

### Rule: The Cisco ASA must be configured to use FIPS-validated SHA-2 or higher for Internet Key Exchange (IKE) Phase 2.

**Rule ID:** `SV-239959r1005430_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Authenticity protection provides protection against man-in-the-middle attacks/session hijacking and the insertion of false information into sessions. Although allowed by SP800-131Ar2 for some applications, SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and government standards. Unless required for legacy use, DOD systems should not be configured to use SHA-1 for integrity of remote access sessions. This requirement focuses on communications protection for the application session rather than for the network packet and establishes grounds for confidence at both ends of communications sessions in ongoing identities of other parties and in the validity of information transmitted. Depending on the required degree of confidentiality and integrity, web services/SOA will require the use of mutual authentication (two-way/bidirectional). An IPsec Security Association (SA) is established using either IKE or manual configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that SHA-2 or higher is specified for IKE Phase 2 as shown in the example below. Step 1: Review the crypto map for IKE Phase 2. crypto map IPSEC_MAP 10 set ikev2 ipsec-proposal AES_SHA Step 2: Verify that the proposal specifies SHA-2 or higher. crypto ipsec ikev2 ipsec-proposal AES_SHA protocol esp encryption … protocol esp integrity sha-384 sha-256 If the ASA is not configured to use SHA-2 or higher for IKE Phase 2, this is a finding.

## Group: SRG-NET-000019-VPN-000040

**Group ID:** `V-239960`

### Rule: The Cisco ASA VPN gateway must be configured to restrict what traffic is transported via the IPsec tunnel according to flow control policies.

**Rule ID:** `SV-239960r666286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. VPN traffic received from another enclave with different security policy or level of trust must not bypass being inspected by the firewall before being forwarded to the private network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Determine the ACL that is used to define what traffic will be transported via the IPsec tunnel. crypto map IPSEC_MAP 10 match address SITE1_SITE2 crypto map IPSEC_MAP 10 set peer x.x.x.x Step 2: Verify that the traffic defined in the ACL is in accordance with flow control policies. access-list SITE1_SITE2 extended permit ip 192.168.1.0 255.255.255.0 192.168.2.0 255.255.255.0 If the VPN gateway is not configured to restrict what traffic is transported via the IPsec tunnel, this is a finding.

## Group: SRG-NET-000148-VPN-000540

**Group ID:** `V-239961`

### Rule: The Cisco ASA VPN gateway must be configured to identify all peers before establishing a connection.

**Rule ID:** `SV-239961r666289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of identification claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the VPN Gateway authenticate all peers before establishing a connection as shown in the example below. tunnel-group x.x.x.x type ipsec-l2l tunnel-group x.x.x.x ipsec-attributes ikev2 remote-authentication pre-shared-key ***** ikev2 local-authentication pre-shared-key ***** Note: Authentication can be either pre-shared key or certificate. If the VPN Gateway does not uniquely identify and authenticate all peers establishing a connection, this is a finding.

## Group: SRG-NET-000565-VPN-002400

**Group ID:** `V-239962`

### Rule: The Cisco ASA VPN gateway must use cryptographic algorithms approved by NSA to protect NSS when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-239962r878134_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. The VPN gateway must implement cryptographic modules adhering to the higher standards approved by the Federal Government since this provides assurance they have been tested and validated. NIST cryptographic algorithms are approved by NSA to protect NSS. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the CSfC program have been changed to more stringent protocols and configured with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm Suite (CNSA Suite) replaces Suite B.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the VPN gateway is configured to use cryptography that is compliant with CSNA/CNSSP when transporting classified traffic across an unclassified network. Step 1: Verify CSNA/CNSSP-15 parameters have been configured for IKE Phase 1 as shown in the example below. crypto ikev2 policy 2 encryption aes-256 integrity null group 19 prf sha384 Step 2: Determine the crypto map for IKE Phase 2 used in compliance with CSNA/CNSSP-15. crypto map CSNA_MAP 10 set ikev2 ipsec-proposal aes-256 Step 3: Verify the proposal specifies AES 256 parameters. crypto ipsec ikev2 ipsec-proposal AES-256 protocol esp encryption aes-256 If the VPN gateway is not configured to use cryptography that is compliant with CSNA/CNSSP-15 parameters when transporting classified traffic across an unclassified network, this is a finding.

## Group: SRG-NET-000337-VPN-001290

**Group ID:** `V-239963`

### Rule: The Cisco ASA VPN gateway must be configured to renegotiate the IPsec Security Association after eight hours or less.

**Rule ID:** `SV-239963r1015263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IPsec security association (SA) and its corresponding key will expire either after the number of seconds or amount of traffic volume has exceeded the configured limit. A new SA is negotiated before the lifetime threshold of the existing SA is reached to ensure that a new SA is ready for use when the old one expires. The longer the lifetime of the IPsec SA, the longer the lifetime of the session key used to protect IP traffic. The SA is less secure with a longer lifetime because an attacker has a greater opportunity to collect traffic encrypted by the same key and subject it to cryptanalysis. However, a shorter lifetime causes IPsec peers to renegotiate Phase 2, more often resulting in the expenditure of additional resources. Specify the lifetime (in seconds) of an Internet Key Exchange (IKE) SA. When the SA expires, it is replaced by a new SA, the Security Parameter Index (SPI), or terminated if the peer cannot be contacted for renegotiation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the VPN gateway renegotiates the security association after eight hours or less as shown in the example below. crypto map IPSEC_MAP 10 match address SITE1_SITE2 crypto map IPSEC_MAP 10 set peer x.x.x.x … … … crypto map IPSEC_MAP 10 set security-association lifetime seconds 3600 If the VPN Gateway does not renegotiate the security association after eight hours or less, this is a finding.

## Group: SRG-NET-000337-VPN-001300

**Group ID:** `V-239964`

### Rule: The Cisco ASA VPN gateway must be configured to renegotiate the IKE security association after 24 hours or less.

**Rule ID:** `SV-239964r1015264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a VPN gateway creates an IPsec security association (SA), resources must be allocated to maintain the SA. These resources are wasted during periods of IPsec endpoint inactivity, which could result in the gateway’s inability to create new SAs for other endpoints, thereby preventing new sessions from connecting. The Internet Key Exchange (IKE) idle timeout may also be set to allow SAs associated with inactive endpoints to be deleted before the SA lifetime has expired, although this setting is not recommended at this time. The value of one hour or less is a common best practice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the VPN gateway renegotiates the IKE security association after 24 hours or less as shown in the example below. crypto ikev2 policy 2 encryption … … … … lifetime seconds 86400 If the VPN gateway does not renegotiate the IKE security association after 24 hours or less, this is a finding.

## Group: SRG-NET-000166-VPN-000580

**Group ID:** `V-239965`

### Rule: The Cisco ASA remote access VPN server must be configured to use a separate authentication server than that used for administrative access.

**Rule ID:** `SV-239965r666301_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The VPN interacts directly with public networks and devices and should not contain user authentication information for all users. AAA network security services provide the primary framework through which a network administrator can set up access control and authorization on network points of entry or network access servers. It is not advisable to configure access control on the VPN gateway or remote access server. Separation of services provides added assurance to the network if the access control server is compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the example below, radius server at 10.1.1.2 is used for administrative access authentication while the LDAP server will be used for granting remote access to the network. aaa-server LDAP protocol ldap aaa-server LDAP (INSIDE) host 10.1.1.1 … … … aaa-server RADIUS_GROUP protocol radius aaa-server RADIUS_GROUP (INSIDE) host 10.1.1.2 key ***** … … … aaa authentication serial console RADIUS_GROUP LOCAL aaa authentication ssh console RADIUS_GROUP LOCAL If the ASA is not configured to use a separate authentication server than that used for administrative access, this is a finding.

## Group: SRG-NET-000320-VPN-001120

**Group ID:** `V-239966`

### Rule: The Cisco ASA remote access VPN server must be configured to use LDAP over SSL to determine authorization for granting access to the network.

**Rule ID:** `SV-239966r1001252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protecting authentication communications between the client, the VPN Gateway, and the authentication server keeps this critical information from being exploited. In distributed information systems, authorization processes and access control decisions may occur in separate parts of the systems. In such instances, authorization information is transmitted securely so timely access control decisions can be enforced at the appropriate locations. To support the access control decisions, it may be necessary to transmit as part of the access authorization information, supporting security attributes. This is due to the fact that in distributed information systems, there are various access control decisions that need to be made and different entities (e.g., services) make these decisions in a serial fashion, each requiring some security attributes to make the decisions. This applies to VPN gateways that have the concept of a user account and have the login function residing on the VPN gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that authorization is enforced as shown in the example below. tunnel-group ANY_CONNECT type remote-access tunnel-group ANY_CONNECT general-attributes authorization-server-group LDAP authorization-required Step 2: Verify that LDAP over SSL has been enabled. aaa-server LDAP protocol ldap aaa-server LDAP (INSIDE) host 10.1.1.1 ldap-over-ssl enable If the ASA is not configured to use LDAP over SSL to determine authorization for granting access to the network, this is a finding.

## Group: SRG-NET-000138-VPN-000490

**Group ID:** `V-239967`

### Rule: The Cisco ASA remote access VPN server must be configured to identify and authenticate users before granting access to the network.

**Rule ID:** `SV-239967r666307_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be identified and authenticated to prevent potential misuse and compromise of the system. Organizational users include organizational employees or individuals the organization deems to have equivalent status of employees (e.g., contractors). Organizational users (and any processes acting on behalf of users) must be uniquely identified and authenticated for all accesses except the following: (i) Accesses explicitly identified and documented by the organization. Organizations document specific user actions that can be performed on the information system without identification or authentication; and (ii) Accesses that occur through authorized use of group authenticators without individual authentication. Organizations may require unique identification of individuals' in-group accounts (e.g., shared privilege accounts) or for detailed accountability of individual activity. This requirement only applies to components where this is specific to the function of the device or has the concept of an organizational user (e.g., VPN or proxy capability). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA is configured to uniquely identify and authenticate users before granting access to the network as shown in the example below. tunnel-group ANY_CONNECT type remote-access tunnel-group ANY_CONNECT webvpn-attributes authentication certificate If the ASA is not configured to identify and authenticate users before granting access to the network, this is a finding.

## Group: SRG-NET-000140-VPN-000500

**Group ID:** `V-239968`

### Rule: The Cisco ASA remote access VPN server must be configured to enforce certificate-based authentication before granting access to the network.

**Rule ID:** `SV-239968r954210_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, non-privileged users must utilize multifactor authentication to prevent potential misuse and compromise of the system. Multifactor authentication uses two or more factors to achieve authentication. Use of password for user remote access for non-privileged account is not authorized. Factors include: (i) Something you know (e.g., password/PIN); (ii) Something you have (e.g., cryptographic identification device, token); or (iii) Something you are (e.g., biometric). A non-privileged account is any information system account with authorizations of a non-privileged user. Network access is any access to a network element by a user (or a process acting on behalf of a user) communicating through a network. The DoD CAC with DoD-approved PKI is an example of multifactor authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that it enforces certificate-based authentication before granting access to the network as shown in the example below. tunnel-group ANY_CONNECT type remote-access tunnel-group ANY_CONNECT webvpn-attributes authentication certificate If the ASA configuration does not enforce certificate-based authentication before granting access to the network, this is a finding.

## Group: SRG-NET-000166-VPN-000590

**Group ID:** `V-239969`

### Rule: The Cisco ASA remote access VPN server must be configured to map the distinguished name (DN) from the client’s certificate to entries in the authentication server to determine authorization to access the network.

**Rule ID:** `SV-239969r929014_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. This requirement only applies to components where this is specific to the function of the device or has the concept of a user (e.g., VPN or ALG). This does not apply to authentication for the purpose of configuring the device itself (i.e., device management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the tunnel group configured for remote access and verify that the DN or UPN from the client’s certificate is used to map to entries in the authentication server to determine authorization as shown in the example below. tunnel-group ANY_CONNECT type remote-access tunnel-group ANY_CONNECT general-attributes authorization-server-group LDAP authorization-required username-from-certificate use-entire-name If the ASA is not configured to map the distinguished name or UPN from the client’s certificate to entries in the authentication server to determine authorization, this is a finding.

## Group: SRG-NET-000041-VPN-000110

**Group ID:** `V-239970`

### Rule: The Cisco ASA remote access VPN server must be configured to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the network.

**Rule ID:** `SV-239970r666316_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Display of a standardized and approved use notification before granting access to the network ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. In most VPN implementations, the banner is configured in the management backplane (NDM SRG) and serves as the presentation for the VPN client connection as well as for administrator logon to the device management tool/backplane. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. This requirement applies to VPN gateways that have the concept of a user account and have the logon function residing on the VPN gateway. The banner must be formatted in accordance with applicable DoD policy. Use the following verbiage for VPN gateways that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ASA is configured to display the Standard Mandatory DoD Notice and Consent Banner before granting remote access to the network as shown in the example below. group-policy GROUP_POLICY_ANYCONNECT attributes banner value I've read & consent to terms in IS user agreem't. If the ASA is not configured to display the Standard Mandatory DoD Notice and Consent Banner before granting remote access to the network, this is a finding.

## Group: SRG-NET-000079-VPN-000300

**Group ID:** `V-239971`

### Rule: The Cisco ASA remote access VPN server must be configured to generate log records containing information that establishes the identity of any individual or process associated with the event.

**Rule ID:** `SV-239971r666319_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information that establishes the identity of the subjects (i.e., users or processes acting on behalf of users) associated with the events, security personnel cannot determine responsibility for the potentially harmful event.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if VPN events are logged as shown in the example below. logging class vpn trap notifications logging class vpnc trap notifications logging class vpnfo trap notifications logging class webfo trap notifications logging class webvpn trap notifications logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA is not configured to log entries containing information to establish the identity of any individual or process associated with the event, this is a finding.

## Group: SRG-NET-000088-VPN-000310

**Group ID:** `V-239972`

### Rule: The Cisco ASA remote access VPN server must be configured to generate log records containing information to establish where the events occurred.

**Rule ID:** `SV-239972r666322_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment, and provide forensic analysis, it is essential for security personnel to know where events occurred, such as VPN gateway components, modules, device identifiers, node names, and functionality. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured VPN gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to determine if VPN events are logged as shown in the example below. logging class vpn trap notifications logging class vpnc trap notifications logging class vpnfo trap notifications logging class webfo trap notifications logging class webvpn trap notifications logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA does not generate log records containing information to establish where the events occurred, this is a finding.

## Group: SRG-NET-000089-VPN-000330

**Group ID:** `V-239973`

### Rule: The Cisco ASA remote access VPN server must be configured to generate log records containing information to establish the source of the events.

**Rule ID:** `SV-239973r666325_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, security personnel need to know the source of the event. In addition to logging where events occur within the network, the log records must also identify sources of events such as IP addresses, processes, and node or device names.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA generates log records containing information to establish the source of the events as shown in the example below. logging class vpn trap notifications logging class vpnc trap notifications logging class vpnfo trap notifications logging class webfo trap notifications logging class webvpn trap notifications logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA does not generate log records containing information to establish the source of the events, this is a finding.

## Group: SRG-NET-000091-VPN-000350

**Group ID:** `V-239974`

### Rule: The Cisco ASA remote access VPN server must be configured to produce log records containing information to establish the outcome of the events.

**Rule ID:** `SV-239974r666328_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the network. Event outcomes can include indicators of event success or failure and event-specific results (e.g., the security state of the network after the event occurred). As such, they also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA generates log records containing information to establish the outcome of the events as shown in the example below. logging class vpn trap notifications logging class vpnc trap notifications logging class vpnfo trap notifications logging class webfo trap notifications logging class webvpn trap notifications logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA does not generate log records containing information to establish the source of the events, this is a finding.

## Group: SRG-NET-000062-VPN-000200

**Group ID:** `V-239975`

### Rule: The Cisco ASA remote access VPN server must be configured to use TLS 1.2 or higher to protect the confidentiality of remote access connections.

**Rule ID:** `SV-239975r666331_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. NIST SP 800-52 provides guidance for client negotiation on either DoD-only or public-facing servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the TLS ASA is configured to use TLS 1.2 or higher as shown in the example below. ssl server-version tlsv1.2 dtlsv1.2 Note: ASA supports TLS version 1.2 starting from software version 9.3.1 for secure message transmission for Clientless SSL VPN and AnyConnect VPN. If the ASA is not configured to use TLS 1.2 or higher to protect the confidentiality of sensitive data during transmission, this is a finding.

## Group: SRG-NET-000063-VPN-000210

**Group ID:** `V-239976`

### Rule: The Cisco ASA remote access VPN server must be configured to use a FIPS-validated algorithm and hash function to protect the integrity of TLS remote access sessions.

**Rule ID:** `SV-239976r769253_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without integrity protection, unauthorized changes may be made to the log files and reliable forensic analysis and discovery of the source of malicious system activity may be degraded. Remote access (e.g., RDP) is access to DoD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Remote access methods include broadband and wireless. Integrity checks include cryptographic checksums, digital signatures, or hash functions. Federal Information Processing Standard (FIPS) 186-4, Digital Signature Standard (DSS), specifies three NIST-approved algorithms: DSA, RSA, and ECDSA. All three are used to generate and verify digital signatures in conjunction with an approved hash function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the remote access ASA uses a FIPS-validated algorithms and hash function as shown in the example below. ssl server-version tlsv1.2 ssl cipher tlsv1.2 fips If the remote access ASA does not use a digital signature generated using FIPS-validated algorithms and hash function, this is a finding.

## Group: SRG-NET-000234-VPN-000810

**Group ID:** `V-239977`

### Rule: The Cisco ASA remote access VPN server must be configured to generate unique session identifiers using a FIPS-validated Random Number Generator (RNG) based on the Deterministic Random Bit Generators (DRBG) algorithm.

**Rule ID:** `SV-239977r666337_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Both IPsec and TLS gateways use the RNG to strengthen the security of the protocols. Using a weak RNG will weaken the protocol and make it more vulnerable. Use of a FIPS validated RNG that is not DRGB mitigates to a CAT III.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ASA configuration to verify that FIPS mode has been enabled as shown in the example below. ASA Version x.x ! hostname ASA1 fips enable If the ASA is not configured to be enabled in FIPS mode, this is a finding.

## Group: SRG-NET-000063-VPN-000220

**Group ID:** `V-239978`

### Rule: The Cisco ASA remote access VPN server must be configured to use SHA-2 at 384 bits or greater for hashing to protect the integrity of IPsec remote access sessions.

**Rule ID:** `SV-239978r916146_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without strong cryptographic integrity protections, information can be altered by unauthorized users without detection. SHA-1 is considered a compromised hashing standard and is being phased out of use by industry and Government standards. DOD systems must not be configured to use SHA-1 for integrity of remote access sessions. The remote access VPN provides access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the ASA uses SHA-2 at 384 bits or greater for hashing to protect the integrity of IPsec remote access sessions as shown in the example below. Step 1: Verify that SHA-2 at 384 bits or greater is used for IKE Phase 1 as shown in the example below. crypto ikev2 policy 1 … … … integrity sha384 Step 2: Verify that SHA-2 at 384 bits or greater is used for the IPsec Security Association. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp integrity sha-384 If the ASA does not use SHA-2 at 384 bits or greater for hashing to protect the integrity of IPsec remote access sessions, this is a finding.

## Group: SRG-NET-000317-VPN-001090

**Group ID:** `V-239979`

### Rule: The Cisco VPN remote access server must be configured to use AES256 or greater encryption for the Internet Key Exchange (IKE) Phase 1 to protect confidentiality of remote access sessions.

**Rule ID:** `SV-239979r987747_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, NIST has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify IKE Phase 1 is set to use an AES256 or greater encryption algorithm as shown in the example below. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp encryption aes-256 If the value of the encryption algorithm for IKE Phase 1 is not set to use an AES256 or greater algorithm, this is a finding.

## Group: SRG-NET-000525-VPN-002330

**Group ID:** `V-239980`

### Rule: The Cisco ASA VPN remote access server must be configured to use AES256 or greater encryption for the IPsec security association to protect the confidentiality of remote access sessions.

**Rule ID:** `SV-239980r916158_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without confidentiality protection mechanisms, unauthorized individuals may gain access to sensitive information via a remote access session. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. A block cipher mode is an algorithm that features the use of a symmetric key block cipher algorithm to provide an information service, such as confidentiality or authentication. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, NIST has approved the following confidentiality modes to be used with approved block ciphers in a series of special publications: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all IPsec proposals are set to use the AES256 or greater encryption algorithm as shown in the example below. crypto ipsec ikev2 ipsec-proposal IPSEC_TRANS protocol esp encryption aes-256 If the value of the encryption algorithm for any IPsec proposal is not set to use an AES256 or greater algorithm, this is a finding.

## Group: SRG-NET-000341-VPN-001350

**Group ID:** `V-239981`

### Rule: The Cisco VPN remote access server must be configured to accept Common Access Card (CAC) credential credentials.

**Rule ID:** `SV-239981r856175_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DoD has mandated the use of the CAC to support identity management and personal authentication for systems covered under HSPD 12, as well as a primary component of layered protection for national security systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA accepts CAC credentials as shown in the example below. tunnel-group ANY_CONNECT type remote-access tunnel-group ANY_CONNECT webvpn-attributes authentication certificate If the ASA does not accept PIV credentials, this is a finding.

## Group: SRG-NET-000369-VPN-001620

**Group ID:** `V-239982`

### Rule: The Cisco ASA VPN remote access server must be configured to disable split-tunneling for remote clients.

**Rule ID:** `SV-239982r1005432_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. A VPN hardware or software client with split tunneling enabled provides an unsecured backdoor to the enclave from the internet. With split tunneling enabled, a remote client has access to the internet while at the same time has established a secured path to the enclave via an IPsec tunnel. A remote client connected to the internet that has been compromised by an attacker in the internet provides an attack base to the enclave’s private network via the IPsec tunnel. Hence, it is imperative that the VPN gateway enforces a no split-tunneling policy to all remote clients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA disables split-tunneling for remote clients VPNs as shown in the example below. group-policy ANY_CONNECT_GROUP attributes … … … split-tunnel-policy tunnelall If the ASA does not disable split-tunneling for remote clients VPNs, this is a finding. Note: Certain cloud products require direct connectivity to operate correctly. These items may be excluded from the split tunneling restriction if documented and approved. If split-tunneling for remote client VPNs is enabled by the above exception, verify only authorized external destinations are excluded from tunneling as shown in the example below: Webvpn anyconnect-custom-attr dynamic-split-exclude-domains description DoD IL5 Authorized Destinations anyconnect-custom-data dynamic-split-exclude-domains DoD-IL5 dod.teams.microsoft.us,azureedge.net,core.usgovcloudapi.net,streaming.media.usgovcloudapi.net,wvd.azure.us,cdn.office365.us anyconnect-custom dynamic-split-exclude-domains value DoD-IL5 If any unauthorized exempted connections exist, this is a finding.

## Group: SRG-NET-000492-VPN-001980

**Group ID:** `V-239983`

### Rule: The Cisco ASA VPN remote access server must be configured to generate log records when successful and/or unsuccessful VPN connection attempts occur.

**Rule ID:** `SV-239983r666355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Log records can be generated from various components within the information system (e.g., module or policy filter). This requirement only applies to components where this is specific to the function of the device, such as application layer gateway (ALG), which provides these access control and auditing functions on behalf of an application. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA generates log records when successful and/or unsuccessful VPN connection attempts occur as shown in the example below. logging host INDM_INTERFACE 10.1.1.12 logging class svc trap notifications Note: A logging list can be used as an alternative to using class. If the ASA does not generate log records when successful and/or unsuccessful VPN connection attempts occur, this is a finding.

## Group: SRG-NET-000580-VPN-002410

**Group ID:** `V-239984`

### Rule: The Cisco ASA VPN remote access server must be configured to validate certificates used for Transport Layer Security (TLS) functions by performing RFC 5280-compliant certification path validation.

**Rule ID:** `SV-239984r666358_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A certificate's certification path is the path from the end entity certificate to a trusted root certification authority (CA). Certification path validation is necessary for a relying party to make an informed decision regarding acceptance of an end entity certificate. Certification path validation includes checks such as certificate issuer trust, time validity, and revocation status for each certificate in the certification path. Revocation status information for CA and subject certificates in a certification path is commonly provided via certificate revocation lists (CRLs) or online certificate status protocol (OCSP) responses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA validates TLS certificates by performing RFC 5280-compliant certification path validation. Review the ASA configuration to determine if a CA trust point has been configured as shown in the example below. crypto ca trustpoint CA_X enrollment … validation-usage ipsec-client validation-usage ssl-client If the ASA does not validate certificates used for TLS functions by performing RFC 5280-compliant certification path validation, this is a finding.

## Group: SRG-NET-000565-VPN-002390

**Group ID:** `V-239985`

### Rule: The Cisco ASA VPN remote access server must be configured to use an approved High Assurance Commercial Solution for Classified (CSfC) cryptographic algorithm for remote access to a classified network.

**Rule ID:** `SV-239985r878134_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Use of improperly configured or lower assurance equipment and solutions could compromise high-value information. The National Security Agency/Central Security Service's (NSA/CSS) CSfC program enables commercial products to be used in layered solutions to protect classified National Security Systems (NSS) data. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the CSfC program have been changed to more stringent protocols and configured with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm Suite (CNSA Suite) replaces Suite B.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the ASA uses an approved High Assurance CSfC cryptographic algorithm for remote access to a classified network. Step 1: Verify IKE Phase 1 is configured in compliance with CSNA/CNSSP-15 parameters as shown in the example below. crypto ikev2 policy 2 encryption aes-256 integrity null group 19 prf sha384 Step 2: Determine the crypto map for IKE Phase 2 used is in compliance with CSNA/CNSSP-15 as in the example below. crypto map CSNA_MAP 10 set ikev2 ipsec-proposal AES-256 Step 3: Verify the proposal specifies CSNA/CNSSP-15 parameters. crypto ipsec ikev2 ipsec-proposal AES-256 protocol esp encryption aes-256 If the ASA is not configured to use an approved High Assurance CSfC cryptographic algorithm for remote access to a classified network, this is a finding.

## Group: SRG-NET-000345-VPN-002430

**Group ID:** `V-268314`

### Rule: The Cisco ASA must be configured to not accept certificates that have been revoked when using PKI for authentication.

**Rule ID:** `SV-268314r1015320_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Situations may arise in which the certificate issued by a Certificate Authority (CA) may need to be revoked before the lifetime of the certificate expires. For example, the certificate is known to have been compromised. When an incoming Internet Key Exchange (IKE) session is initiated for a remote client or peer whose certificate is revoked, the revocation list configured for use by the VPN server is checked to see if the certificate is valid; if the certificate is revoked, IKE will fail and an IPsec security association will not be established for the remote endpoint.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If PKI certificates are not implemented on the ASA, this requirement is not applicable. Verify the ASA does not accept certificates that have been revoked. Revocation checking using CRL example: crypto ca trustpoint CA_X revocation-check crl Note: By default, the ASA will use the distribution points listed in CDP extension of the certificate that is being validated. Revocation checking using OCSP example: crypto ca trustpoint CA_X revocation-check ocsp Note: By default, the ASA will use the OSCP responder address found in the Authority Information Access (AIA) field of the client's certificate. Deployment with CAC would be an exception. If the ASA accepts certificates that have been revoked, this is a finding.

