# STIG Benchmark: HPE Aruba Networking AOS Wireless Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000062

**Group ID:** `V-266557`

### Rule: AOS must use Transport Layer Security (TLS) 1.2, at a minimum, to protect the confidentiality of sensitive data during electronic dissemination using remote access.

**Rule ID:** `SV-266557r1040161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using older unauthorized versions or incorrectly configuring protocol negotiation makes the gateway vulnerable to known and unknown attacks that exploit vulnerabilities in this protocol. This requirement applies to TLS gateways (also known as Secure Sockets Layer [SSL] gateways). Application protocols such as Hypertext Transfer Protocol Secure (HTTPS), Secure File Transfer Protocol (SFTP), and others use TLS as the underlying security protocol and thus are in scope for this requirement. National Institute of Standards and Technology (NIST) Special Publication 800-52 provides guidance for client negotiation on either DOD-only or public-facing servers. Satisfies: SRG-NET-000062, SRG-NET-000530</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show web-server profile If "tlsv1.2" is not returned for "SSL/TLS Protocol Config", this is a finding.

## Group: SRG-NET-000069

**Group ID:** `V-266559`

### Rule: AOS must protect wireless access to the network using authentication of users and/or devices.

**Rule ID:** `SV-266559r1040167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing devices and users to connect to the system without first authenticating them allows untrusted access and can lead to a compromise or attack. The security boundary of a wireless local area network (WLAN) extends from the client device to the network boundary where network access is controlled. This boundary represents the portion of the network most vulnerable to attack and must be protected. Within this boundary there must be two distinct, but related, security protection mechanisms: authentication and data-in-transit encryption. These protections ensure access control and protection from eavesdropping for both the WLAN system and the DOD network enclave. Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., Extensible Authentication Protocol (EAP)/Transport Layer Security (TLS) and Protected EAP [PEAP]), which provide credential protection and mutual authentication. Satisfies: SRG-NET-000069, SRG-NET-000070</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show wlan ssid-profile For each WLAN SSID: show wlan ssid-profile <SSID profile name> If a WPA Passphrase is set or if Encryption is not set with wpa2-aes or wpa3-cnsa, this is a finding.

## Group: SRG-NET-000070

**Group ID:** `V-266560`

### Rule: The network element must protect wireless access to the system using Federal Information Processing Standard (FIPS)-validated Advanced Encryption Standard (AES) block cipher algorithms with an approved confidentiality mode.

**Rule ID:** `SV-266560r1040170_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Allowing devices and users to connect to the system without first authenticating them allows untrusted access and can lead to a compromise or attack. Because wireless communications can be intercepted, encryption must be used to protect the confidentiality of information in transit. Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., Extensible Authentication Protocol (EAP)/Transport Layer Security (TLS) and Protected EAP [PEAP]), which provide credential protection and mutual authentication. This requirement applies to operating systems that control wireless devices. A block cipher mode is an algorithm that features the use of a symmetric key block cipher algorithm to provide an information service, such as confidentiality or authentication. AES is the FIPS-validated cipher block cryptographic algorithm approved for use in the DOD. For an algorithm implementation to be listed on a FIPS 140-2/140-3 cryptographic module validation certificate as an approved security function, the algorithm implementation must meet all the requirements of FIPS 140-2/140-3 and must successfully complete the cryptographic algorithm validation process. Currently, the National Institute of Standards and Technology (NIST) has approved the following confidentiality modes to be used with AES: ECB, CBC, OFB, CFB, CTR, XTS-AES, FF1, FF3, CCM, GCM, KW, KWP, and TKW. Satisfies: SRG-NET-000070, SRG-NET-000151</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show fips show ap system-profile For each configured ap system profile: show ap system-profile <profile-name> | include FIPS If FIPS is not enabled, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-266577`

### Rule: AOS must be configured to disable nonessential capabilities.

**Rule ID:** `SV-266577r1040221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for network elements to provide, or enable by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Network elements are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions and functions).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show firewall-cp Verify that nonessential capabilities, functions, ports, protocols, and/or services are denied. If any nonessential capabilities, functions, ports, protocols, and/or services are allowed, this is a finding.

## Group: SRG-NET-000193

**Group ID:** `V-266591`

### Rule: AOS must manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-266591r1040263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A network element experiencing a DoS attack will not be able to handle production traffic load. The high utilization and CPU caused by a DoS attack will also have an effect on control keep-alives and timers used for neighbor peering, resulting in route flapping, and will eventually sinkhole production traffic. The device must be configured to contain and limit a DoS attack's effect on the device's resource utilization. The use of redundant components and load balancing are examples of mitigating "flood-type" DoS attacks through increased capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: Navigate to Configuration >> Services >> Firewall. If the organization-defined safeguards are not enabled to protect against known DoS attacks, this is a finding.

## Group: SRG-NET-000338

**Group ID:** `V-266627`

### Rule: AOS must require devices to reauthenticate when organization-defined circumstances or situations requiring reauthentication.

**Rule ID:** `SV-266627r1040371_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity on the network. In addition to the reauthentication requirements associated with session locks, organizations may require reauthentication of devices, including (but not limited to), the following other situations: (i) When authenticators change; (ii) When roles change; (iii) When security categories of information systems change; (iv) After a fixed period of time; or (v) Periodically. This requirement only applies to components where this is specific to the function of the device or has the concept of device authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show crypto-local ipsec-map If the configured IPSec maps are not configured to support a security association lifetime of 28,800 seconds (8 hours), this is a finding.

## Group: SRG-NET-000343

**Group ID:** `V-266632`

### Rule: The network element must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-266632r1040624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers outside a datacenter, Voice over Internet Protocol phones, and video teleconferencing codecs). Gateways and service-oriented architecture applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific preauthorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the AP is not being used as a Remote AP, this check is not applicable. Verify the AOS configuration with the following commands: 1. Site-to-site VPN: show crypto-local ipsec-map If a CA certificate and Server certificate are not configured for each IPsec map, this is a finding. 2. Hardware client VPN: show "remote ap profile" If certificate authentication is not configured for each RAP profile, this is a finding.

## Group: SRG-NET-000352

**Group ID:** `V-266639`

### Rule: AOS must use cryptographic algorithms approved by the National Security Agency (NSA) to protect national security systems (NSS) when transporting classified traffic across an unclassified network.

**Rule ID:** `SV-266639r1040407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Use of weak or untested encryption algorithms undermines the purposes of using encryption to protect data. National Institute of Standards and Technology (NIST) cryptographic algorithms are approved by NSA to protect NSS. Based on an analysis of the impact of quantum computing, cryptographic algorithms specified by CNSSP-15 and approved for use in products in the Commercial Solutions for Classified (CSfC) program have been changed to more stringent protocols and configured with increased bit sizes and other secure characteristics to protect against quantum computing threats. The Commercial National Security Algorithm (CNSA) Suite replaces Suite B. Satisfies: SRG-NET-000352, SRG-NET-000565</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If AOS is not being used for CSFC, this requirement is not applicable. 1. Verify the AOS configuration with the following command: show crypto-local ipsec-map Note the IKEv2 Policy number for each configured map. 2. For each configured policy number, run the following command: show crypto isakmp policy <IKEv2 Policy #> 3. Verify each configured transform-set with the following command: show crypto ipsec transform-set If the configured IPsec map, ISAKMP policy, and transform-set do not contain the following, this is a finding: ECDCA 384 certificate IKEv2 policy with AES256, SHA-384, ECDSA-384, Group 20 Transform set with AES-256-GCM

## Group: SRG-NET-000369

**Group ID:** `V-266644`

### Rule: AOS, in conjunction with a remote device, must prevent the device from simultaneously establishing nonremote connections with the system and communicating via some other connection to resources in external networks.

**Rule ID:** `SV-266644r1040422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Split tunneling would in effect allow unauthorized external connections, making the system more vulnerable to attack and to exfiltration of organizational information. This requirement applies to virtual private network (VPN) concentrators and clients. It is implemented within remote devices (e.g., notebook computers) through configuration settings to disable split tunneling in those devices and by preventing those configuration settings from being readily configurable by users. This requirement is implemented within the information system by the detection of split tunneling (or configuration settings that allow split tunneling) in the remote device and by prohibiting the connection if the remote device is using split tunneling. The use of VPNs for remote connections, when adequately provisioned with appropriate security controls, may provide the organization with sufficient assurance that it can effectively treat such connections as nonremote connections from the confidentiality and integrity perspective. VPNs thus provide a means for allowing nonremote communications paths from remote devices. The use of an adequately provisioned VPN does not eliminate the need for preventing split tunneling.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following commands: show running-configuration | include split-tunnel show running-config | include double-encrypt If any instances of forward-mode split-tunnel are found or if double-encrypt is not enabled, this is a finding.

## Group: SRG-NET-000070

**Group ID:** `V-266703`

### Rule: When AOS is used as a wireless local area network (WLAN) controller, WLAN Extensible Authentication Protocol-Transport Layer Security (EAP-TLS) implementation must use certificate-based public key infrastructure (PKI) authentication to connect to DOD networks.

**Rule ID:** `SV-266703r1040640_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD certificate-based PKI authentication is strong, two-factor authentication that relies on carefully evaluated cryptographic modules. Implementations of EAP-TLS that are not integrated with certificate-based PKI could have security vulnerabilities. For example, an implementation that uses a client certificate on a laptop without a second factor could enable an adversary with access to the laptop to connect to the WLAN without a PIN or password. Systems that do not use the certificate-based PKI are also much more likely to be vulnerable to weaknesses in the underlying public key infrastructure (PKI) that supports EAP-TLS. Certificate-based PKI authentication must be used to connect WLAN client devices to DOD networks. The certificate-based PKI authentication should directly support the WLAN EAP-TLS implementation. At least one layer of user authentication must enforce network authentication requirements (e.g., CAC authentication) before the user is able to access DOD information resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> WLANs and select the desired WLAN in the WLANs field. 2. Under the selected WLAN, select "Security". Note which Auth servers are configured. 3. Navigate to Configuration >> Authentication. 4. In the "All Servers" field, select each WLAN authentication server noted earlier. 5. Verify each configured authentication server is configured to support EAP-TLS with DOD PKI. If each WLAN authentication server is not configured to support EAP-TLS with DOD PKI, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-266704`

### Rule: The site must conduct continuous wireless Intrusion Detection System (IDS) scanning.

**Rule ID:** `SV-266704r1040625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DOD networks are at risk and DOD data could be compromised if wireless scanning is not conducted to identify unauthorized wireless local area network (WLAN) clients and access points connected to or attempting to connect to the network. DOD Components must ensure that a wireless intrusion detection system (WIDS) is implemented that allows for monitoring of WLAN activity and the detection of WLAN-related policy violations on all unclassified and classified DOD wired and wireless LANs. The WIDS must be implemented regardless of whether or not an authorized WLAN has been deployed. The WIDS must be capable of monitoring IEEE 802.11 transmissions within all DOD LAN environments and detecting nearby unauthorized WLAN devices. The WIDS is not required to monitor non-IEEE 802.11 transmissions. The WIDS must continuously scan for and detect authorized and unauthorized WLAN activities 24 hours a day, seven days a week. Note: Exceptions to WIDS implementation criteria may be made by the authorizing official (AO) for DOD wired and wireless LAN operating environments. This exception allows the AO to implement periodic scanning conducted by designated personnel using hand-held scanners during walkthrough assessments. Periodic scanning may be conducted as the alternative to the continuous scanning only in special circumstances, where it has been determined on a case-by-case basis that continuous scanning is either infeasible or unwarranted. The AO exception must be documented. The "infeasible" criteria includes the following use case examples: - It is not my building - This scenario means that for contractual or other similar reasons, the DOD component is not allowed to install a WIDS. - There is no power or space is limited - This scenarios means that for space, weight, and power (SWAP) reasons, the addition of continuous scanning capabilities cannot be accomplished because it would exceed SWAP availability. Power would also affect the decision to waive continuous scanning requirements if the entire LAN is only in operation periodically (e.g., the wired/wireless LAN is enabled on a vehicle that is only operating when the vehicle is being used for a specific operation). - The exception for "Minimal Impact WLAN Systems" that do not provide connectivity to WLAN-enabled PEDs (e.g., backhaul systems), have no available FIPS 140-validated 802.1X EAP-TLS supplicant, support a very small number of users for a specific mission (e.g., 10 or less users), are standalone networks, or are highly specialized WLAN systems that are isolated from the DODIN (e.g., hand-held personal digital assistants [PDAs] used as radio-frequency identification [RFID] readers, a network of WLAN-enabled Voice over Internet Protocol [VoIP] phones) allows the AO to waive any of the security requirements in the Instruction. This includes using nonstandard/proprietary FIPS-validated encryption, using an alternative FIPS-validated EAP type, and not having a continuous WIDS. - The cost of the continuous WIDS capability is more expensive that the total cost of the LAN without a WIDS. The AO must conduct a wireless threat risk assessment where analysis has shown that the threat environment is extremely unlikely to nonexistent to meet the "unwarranted" exception criteria.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the site information system security officer (ISSO). Determine if scanning by a WIDS is being conducted and if it is continuous or periodic. If a continuous scanning WIDS is used, there is no finding. If periodic scanning is used, verify the exception to policy is documented and signed by the AO. Verify the exception meets one of the required criteria. If periodic scanning is being performed but requirements have not been met, this is a finding. If no WIDS scanning is being performed at the site, this is a finding.

## Group: SRG-NET-000131

**Group ID:** `V-266705`

### Rule: AOS, when configured as a WLAN bridge, must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-266705r1040645_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call-home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack. (Refer to SRG-NET-000131-RTR-000083.)</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration using the web interface: 1. Navigate to Configuration >> System >> More tab. 2. Expand "Phone Home ". If "Phone Home" is enabled, this is a finding.

## Group: SRG-NET-000205

**Group ID:** `V-266707`

### Rule: AOS, when used as a WLAN bridge or controller, must be configured to only permit management traffic that ingresses and egresses the out-of-band management (OOBM) interface.

**Rule ID:** `SV-266707r1040611_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. (Refer to SRG-NET-000205-RTR-000012.) Network boundaries, also known as managed interfaces, include, for example, gateways, routers, firewalls, guards, network-based malicious code analysis, and virtualization systems, or encrypted tunnels implemented within a security architecture (e.g., routers protecting firewalls or application gateways residing on protected subnetworks). Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones (DMZs). Methods used for prohibiting interfaces within organizational information systems include, for example, restricting external web traffic to designated web servers within managed interfaces and prohibiting external traffic that appears to be spoofing internal addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the AOS configuration with the following command: show ip route verbose If any the management traffic network is not configured with a route to the OOBM gateway, this is a finding.

## Group: SRG-NET-000512

**Group ID:** `V-266708`

### Rule: AOS wireless local area network (WLAN) service set identifiers (SSIDs) must be changed from the manufacturer's default to a pseudo random word that does not identify the unit, base, organization, etc.

**Rule ID:** `SV-266708r1040614_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An SSID that identifies the unit, site, or purpose of the WLAN or is set to the manufacturer default may cause an operational security vulnerability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review AOS WLAN configuration by navigating to Configuration >> WLANs. If the WLAN SSIDs listed in the "NAME (SSID)" column are not pseudo random words, this is a finding.

