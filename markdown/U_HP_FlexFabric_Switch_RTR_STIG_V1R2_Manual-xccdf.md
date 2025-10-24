# STIG Benchmark: HP FlexFabric Switch RTR Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-65965`

### Rule: The HP FlexFabric Switch must be configured so inactive HP FlexFabric Switch interfaces are disabled.

**Rule ID:** `SV-80455r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram and determine which HP FlexFabric Switch interfaces should be inactive. If there are inactive HP FlexFabric Switch interfaces that are enabled, this is a finding. [HP]display current-configuration interface interface GigabitEthernet0/1 port link-mode route pim sm ip address 192.168.10.1 255.255.255.0 packet-filter 3010 inbound

## Group: SRG-NET-000019-RTR-000011

**Group ID:** `V-66099`

### Rule: The HP FlexFabric Switch must not redistribute static routes to alternate gateway service provider into an Exterior Gateway Protocol or Interior Gateway Protocol to the NIPRNet or to other Autonomous System.

**Rule ID:** `SV-80589r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the static routes to the alternate gateway are being redistributed into an Exterior Gateway Protocol or Interior Gateway Protocol to a NIPRNet gateway, this could make traffic on NIPRNet flow to that particular router and not to the Internet Access Point routers. This could not only wreak havoc with traffic flows on NIPRNet, but it could overwhelm the connection from the router to the NIPRNet gateway(s) and also cause traffic destined for outside of NIPRNet to bypass the defenses of the Internet Access Points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the External/internal gateway protocol database on the HP FlexFabric Switch to ensure no static routes are being redistributed via these protocols. If there are static routes being re-distributed, this is a finding. [HP] display ospf lsdb OSPF Process 1 with HP FlexFabric Switch ID 5.9.2.0 Link State Database Area: 0.0.0.1 Type LinkState ID AdvHP FlexFabric Switch Age Len Sequence Metric HP FlexFabric Switch 1.1.1.1 1.1.1.1 1644 48 80000155 0 HP FlexFabric Switch 5.9.2.0 5.9.2.0 233 48 8000013E 0 HP FlexFabric Switch 2.2.2.2 2.2.2.2 294 72 8000014F 0 AS External Database Type LinkState ID AdvHP FlexFabric Switch Age Len Sequence Metric External 16.0.0.0 5.9.2.0 233 36 80000001 1 External 15.252.0.0 5.9.2.0 233 36 80000001 1 Note: In the example above we see two external entries with the advertising HP FlexFabric Switch as the HP FlexFabric Switch. This exists when the HP FlexFabric Switch is configured to redistribute static route.

## Group: SRG-NET-000019-RTR-000009

**Group ID:** `V-66101`

### Rule: The HP FlexFabric Switch must protect an enclave connected to an Alternate Gateway by using an inbound filter that only permits packets with destination addresses within the sites address space.

**Rule ID:** `SV-80591r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enclaves with Alternate Gateway (AG) connections must take additional steps to ensure there is no compromise on the enclave network or NIPRNet. Without verifying the destination address of traffic coming from the site's AG, the perimeter router could be routing transit data from the Internet into the NIPRNet. This could also make the perimeter router vulnerable to a DoS attack as well as provide a backdoor into the NIPRNet. The DoD enclave must ensure the ingress filter applied to external interfaces on a perimeter router connecting to an AG is secure through filters permitting packets with a destination address belonging to the DoD enclave's address block.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of each HP FlexFabric Switch interface connecting to an Alternate Gateway. Verify that the ACL configured to block unauthorized networks are configured on the interface. Verify each permit statement of the ingress filter only permits packets with destination addresses of the site's NIPRNet address space or a destination address belonging to the address block assigned by the Alternate Gateway network service provider. If the ACL is not configured to only permit packets with destination addresses within the sites address space, this is a finding. [HP]display interface gig0/1 interface GigabitEthernet0/1 port link-mode route ip address 192.168.10.1 255.255.255.0 packet-filter 3010 inbound

## Group: SRG-NET-000019-RTR-000010

**Group ID:** `V-66103`

### Rule: If Border Gateway Protocol (BGP) is enabled on the HP FlexFabric Switch, the HP FlexFabric Switch must not be a BGP peer with a HP FlexFabric Switch from an Autonomous System belonging to any Alternate Gateway (AG).

**Rule ID:** `SV-80593r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The perimeter router will not use a routing protocol to advertise NIPRNet addresses to Alternate Gateways. Most ISPs use Border Gateway Protocol (BGP) to share route information with other autonomous systems, that is, any network under a different administrative control and policy than a local site. If BGP is configured on the perimeter router, no BGP neighbors will be defined to peer routers from an AS belonging to any Alternate Gateway. The only allowable method is a static route to reach the Alternate Gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the HP FlexFabric Switch connecting to the AG. Verify there are no BGP neighbors configured to the remote AS that belongs to the AG service provider. There should be no BGP peers displayed. If there are BGP neighbors configured that belong to the AG service provider, this is a finding. [HP] display bgp peer ipv4 BGP local FlexFabric Switch ID: 2.2.2.0 Local AS number: 1472 Total number of peers: 1 Peers in established state: 0 * - Dynamically created peer Peer AS MsgRcvd MsgSent OutQ PrefRcv Up/Down State

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-66107`

### Rule: The HP FlexFabric Switch must be configured to disable non-essential capabilities.

**Rule ID:** `SV-80597r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify that non-essential services are not enabled, if these services are enabled, this is a finding: [HP] display ftp-server FTP is not configured. [HP] display current-configuration | include telnet Note: When Telnet server is enabled, the output for this command is telnet server enable.

## Group: SRG-NET-000025-RTR-000020

**Group ID:** `V-66109`

### Rule: The HP FlexFabric Switch must enable neighbor authentication for all control plane protocols.

**Rule ID:** `SV-80599r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network, or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration; for every protocol that affects the routing or forwarding tables (where information is exchanged between neighbors), verify that neighbor HP FlexFabric Switch authentication is enabled. If neighbor authentication for all router control plane protocols is not configured, this is a finding. The information below shows OSPF and OSPFv3 authentication is enabled on interface gigabit ethernet 0/0 [HP] display current-configuration interface GigabitEthernet 0/0 # interface GigabitEthernet0/0 port link-mode route description R1 ACTIVE combo enable copper ip address 201.6.1.62 255.255.255.252 ospf authentication-mode md5 1 cipher ********** ospfv3 200 area 0.0.0.0 ospfv3 ipsec-profile jitc ipv6 address 2115:B:1::3E/126

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-66111`

### Rule: The HP FlexFabric Switch must encrypt all methods of configured authentication for routing protocols.

**Rule ID:** `SV-80601r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network, or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the HP FlexFabric Switch configuration to ensure that it is using a NIST validated FIPS 140-2 cryptography encryption mechanism by implementing OSPFv3 with IPsec. [HP] display current-configuration interface interface GigabitEthernet0/0 port link-mode route description R1 ACTIVE combo enable copper ospfv3 200 area 0.0.0.0 ospfv3 ipsec-profile jitc ipv6 address 2115:B:1::3E/126 If the routing protocol authentication mechanism is not a validated FIPS 140-2 cryptography, this is a finding. Note: OSPFv3 requires IPsec to enable authentication using either the IPv6 Authentication Header (AH) or the Encapsulating Security Payload (ESP) header.

## Group: SRG-NET-000168-RTR-000078

**Group ID:** `V-66113`

### Rule: The HP FlexFabric Switch must use NIST-validated FIPS 140-2 cryptography to implement authentication encryption mechanisms for routing protocols.

**Rule ID:** `SV-80603r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network, or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. Since MD5 is vulnerable to "birthday" attacks and may be compromised, routing protocol authentication must use FIPS 140-2 validated algorithms and modules to encrypt the authentication key. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the HP FlexFabric Switch configuration to ensure that it is using a NIST validated FIPS 140-2 cryptography encryption mechanism by implementing OSPFv3 with IPsec. [HP] display current-configuration interface interface GigabitEthernet0/0 port link-mode route description R1 ACTIVE combo enable copper ospfv3 200 area 0.0.0.0 ospfv3 ipsec-profile jitc ipv6 address 2115:B:1::3E/126 If the routing protocol authentication mechanism is not a validated FIPS 140-2 cryptography, this is a finding. Note: OSPFv3 requires IPsec to enable authentication using either the IPv6 Authentication Header (AH) or the Encapsulating Security Payload (ESP) header.

## Group: SRG-NET-000019-RTR-000012

**Group ID:** `V-66115`

### Rule: The HP FlexFabric Switch must enforce that Interior Gateway Protocol (IGP) instances configured on the out-of-band management gateway only peer with their own routing domain.

**Rule ID:** `SV-80605r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the out-of-band management network, implementation of several safeguards for containment of management and production traffic boundaries must occur. Since the managed and management network are separate routing domains, configuration of separate Interior Gateway Protocol routing instances is critical on the router to segregate traffic from each network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the management interface belongs to a different OSPF instance (process) than the production network. If the management interface does not belong to a different OSPF instance, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-66117`

### Rule: The HP FlexFabric Switch must enforce that the managed network domain and the management network domain are separate routing domains and the Interior Gateway Protocol (IGP) instances are not redistributed or advertised to each other.

**Rule ID:** `SV-80607r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the out-of-band management network, several safeguards must be implemented for containment of management and production traffic boundaries, otherwise, it is possible that management traffic will not be separated from production traffic. Since the managed network and the management network are separate routing domains, separate Interior Gateway Protocol routing instances must be configured on the router, one for the managed network and one for the out-of-band management network. In addition, the routes from the two domains must not be redistributed to each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the management interface belongs to a different OSPF instance (process) than the production network. If the management interface does not belong to a different OSPF instance, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-66119`

### Rule: The HP FlexFabric Switch must enforce that any interface used for out-of-band management traffic is configured to be passive for the Interior Gateway Protocol (IGP) that is utilized on that management interface.

**Rule ID:** `SV-80609r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The out-of-band management access switch will connect to the management interface of the managed network elements. The management interface can be a true out-of-band management interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will directly connect to the out-of-band management network. An out-of-band management interface does not forward transit traffic, thereby, providing complete separation of production and management traffic. Since all management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an out-of-band management port, the interface functioning as the management interface must be configured so that management traffic, both data plane and control plane, does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the OOBM interface belongs to a different OSPF instance (process) than the production network. If the management interface does not belong to a different OSPF instance, this is a finding. Note: By default an OOBM interface is passive to a routing protocol.

## Group: SRG-NET-000026-RTR-000031

**Group ID:** `V-66121`

### Rule: The HP FlexFabric Switch must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field via egress filter or by enabling Unicast Reverse Path Forwarding.

**Rule ID:** `SV-80611r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious actor as a platform to launch cyber attacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack (usually DDoS) other computers or networks. DDoS attacks frequently leverage IP source address spoofing, in which packets with false source IP addresses send traffic to multiple hosts, which then send return traffic to the hosts with the IP addresses that were forged. This can generate significant, even massive, amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. The router must not accept any outbound IP packets that contain an illegitimate address in the source address field by enabling Unicast Reverse Path Forwarding (uRPF) strict mode or by implementing an egress ACL. Unicast Reverse Path Forwarding (uRPF) provides an IP address spoof protection capability. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display the switch configuration to verify that either the command ip urpf strict has been configured or an egress filter has been configured on all internal-facing interfaces to drop all outbound packets with an illegitimate source address. If uRPF or an egress filter to restrict the switch from accepting outbound IP packets that contain an illegitimate address in the source address field has not been configured on all internal-facing interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-66123`

### Rule: The HP FlexFabric Switch must manage excess bandwidth to limit the effects of packet flooding types of denial of service (DoS) attacks.

**Rule ID:** `SV-80613r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding DDoS attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or by botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the system administrator to determine the requirements for bandwidth and traffic prioritization. Display the HP FlexFabric Switch configuration to ensure that the HP FlexFabric Switch is configured with these requirements. If excess bandwidth is not managed to limit the effects of packet flooding types of denial of service (DoS) attacks, this is a finding [HP] display current interface serial10/0 # interface Serial10/0 description IUT 2M-SERIAL virtualbaudrate 2048000 qos reserved-bandwidth pct 100 qos flow-interval 1 qos apply policy JITC-2M-SERIAL outbound undo ipv6 nd ra halt #

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-66125`

### Rule: The HP FlexFabric Switch must configure the maximum hop limit value to at least 32.

**Rule ID:** `SV-80615r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message to be used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached their destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if the maximum hop limit has been configured. If the maximum hop limit is not configured, this is a finding. If it has been configured, then it must be set to at least 32; otherwise this is a finding. [5900CP]display current-configuration | i hop-limit ipv6 hop-limit 255 Note: The default value for the maximum hop limit is 64.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-66127`

### Rule: The HP FlexFabric Switch must protect against or limit the effects of denial of service (DoS) attacks by employing control plane protection.

**Rule ID:** `SV-80617r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Route Processor (RP) is critical to all network operations because it is the component used to build all forwarding paths for the data plane via control plane processes. It is also instrumental with ongoing network management functions that keep the routers and links available for providing network services. Any disruption to the Route Processor or the control and management planes can result in mission-critical network outages. A DoS attack targeting the Route Processor can result in excessive CPU and memory utilization. To maintain network stability and Route Processor security, the router must be able to handle specific control plane and management plane traffic that is destined to the Route Processor. In the past, one method of filtering was to use ingress filters on forwarding interfaces to filter both forwarding path and receiving path traffic. However, this method does not scale well as the number of interfaces grows and the size of the ingress filters grow. Control plane policing increases the security of routers and multilayer switches by protecting the Route Processor from unnecessary or malicious traffic. Filtering and rate limiting the traffic flow of control plane packets can be implemented to protect routers against reconnaissance and DoS attacks, allowing the control plane to maintain packet forwarding and protocol states despite an attack or heavy load on the router or multilayer switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that there is a control plane policy configured on the HP FlexFabric to rate limit control plane traffic using the following command: display qos policy control-plane slot 1. If the HP FlexFabric Switch is not configured to rate limit control plane traffic, this is a finding.

## Group: SRG-NET-000364-RTR-000109

**Group ID:** `V-66129`

### Rule: The HP FlexFabric Switch must only allow incoming communications from authorized sources to be routed to authorized destinations.

**Rule ID:** `SV-80619r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic can be restricted directly by an ACL (which is a firewall function) or by Policy Routing. Policy Routing is a technique used to make routing decisions based on a number of different criteria other than just the destination network, including source or destination network, source or destination address, source or destination port, protocol, packet size, and packet classification. This overrides the router's normal routing procedures used to control the specific paths of network traffic. It is normally used for traffic engineering, but can also be used to meet security requirements; for example, traffic that is not allowed can be routed to the Null0 or discard interface. Policy Routing can also be used to control which prefixes appear in the routing table. Traffic can be restricted directly by an ACL (which is a firewall function), or by Policy Routing. This requirement is intended to allow network administrators the flexibility to use whatever technique is most effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if the switch only allows incoming communications from authorized sources to be routed to authorized destinations. This requirement can be met by applying an ingress filter to an external-facing interface as shown in the following example: acl number 3001 rule 1 deny ip source 192.168.3.121 0 rule 2 permit ip source 192.100.1.0 0.0.0.255 destination 192.200.2.0 0.0.0.255 interface Ten-GigabitEthernet1/0/21 ip address 102.17.17.2 255.255.255.252 packet-filter 3001 inbound If the HP FlexFabric Switch allows incoming communications from unauthorized sources or to unauthorized destinations, this is a finding.

## Group: SRG-NET-000019-RTR-000002

**Group ID:** `V-66131`

### Rule: The HP FlexFabric Switch must enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy.

**Rule ID:** `SV-80621r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates authorized information to travel within a network and between interconnected networks. Controlling the flow of network traffic is critical so it does not introduce any unacceptable risk to the network infrastructure or data. An example of a flow control restriction is blocking outside traffic claiming to be from within the organization. For most routers, internal information flow control is a product of system design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if the switch enforces approved authorizations for controlling the flow of information between interconnected networks or VLANs in accordance with applicable policy. This requirement can be met through the use of IP access control lists which are applied to specific interfaces inbound or outbound as show in the following example: acl number 3001 rule 1 deny ip source 192.168.3.121 0 rule 2 permit ip source 192.100.1.0 0.0.0.255 destination 192.200.2.0 0.0.0.255 interface Ten-GigabitEthernet1/0/21 ip address 102.17.17.2 255.255.255.252 packet-filter 3001 inbound If the switch does not enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy, this is a finding.

## Group: SRG-NET-000191-RTR-000081

**Group ID:** `V-66133`

### Rule: The HP FlexFabric Switch must ensure all Exterior Border Gateway Protocol (eBGP) HP FlexFabric Switches are configured to use Generalized TTL Security Mechanism (GTSM).

**Rule ID:** `SV-80623r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As described in RFC 3682, GTSM is designed to protect a router's IP-based control plane from DoS attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all eBGP speaking routers. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent routers; that is, the eBGP peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration. If the HP FlexFabric Switch is not configured to use GTSM for all eBGP peering sessions, this is a finding. [HP] display current-configuration # bgp 2000 graceful-restart peer 10.10.10.1 as-number 2000 peer 10.10.10.1 ttl-security hops 254 peer 201.6.1.193 as-number 1473 peer 201.6.1.193 route-update-interval 0 peer 201.6.1.193 password cipher $c$3$6jyBDW1nVs/F0410R54zhmhD1HYhs5I= peer 2115:B:1::C1 as-number 1473 peer 2115:B:1::C1 route-update-interval 0

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-66135`

### Rule: The HP FlexFabric Switch must disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-80625r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DoD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network has documented their multicast topology and thereby knows which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast topology diagram and determine which HP FlexFabric Switch interfaces should have Protocol Independent Multicast enabled. Disable PIM on interfaces that should not have it enabled. If PIM is enabled interfaces that are not required to support multicast routing, this is a finding. [HP]display current-configuration interface interface GigabitEthernet0/1 port link-mode route pim sm ip address 192.168.10.1 255.255.255.0 packet-filter 3010 inbound [HP FlexFabric SwitchD] display pim neighbor Total Number of Neighbors = 3 Neighbor Interface Uptime Expires Dr-Priority 192.168.10.2 GE0/1 00:02:22 00:01:27 1

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-66137`

### Rule: The HP FlexFabric Switch must bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-80627r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protocol Independent Multicast (PIM) is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. Protocol Independent Multicast traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, an unauthorized routers can join the PIM domain and discover and use the rendezvous points, and also advertise their rendezvous points into the domain. This can result in a denial of service by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast topology diagram and determine if the HP FlexFabric Switch interfaces are enabled for IPv4 or IPv6 multicast routing. If the HP FlexFabric Switch is enabled for multicast routing, verify all interfaces enabled for PIM have a neighbor filter bound to the interface. The neighbor filter must only accept PIM control plane traffic from the documented PIM neighbors. If a PIM neighbor filter is not configured on all multicast-enabled interfaces, this is a finding. display interface GigabitEthernet 0/1 interface GigabitEthernet0/1 port link-mode route description IUT 4GE-HMIM ip address 15.252.78.69 255.255.255.0 pim sm pim neighbor-policy 2000 ipv6 pim sm ipv6 pim neighbor-policy 2000 [HP]display acl 2000 Basic ACL 2000, named -none-, 3 rules, ACL's step is 5 rule 0 permit source 224.200.100.10 0 rule 5 permit source 224.200.101.11 0 rule 10 deny

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-66139`

### Rule: The HP FlexFabric Switch must establish boundaries for IPv6 Admin-Local, IPv6 Site-Local, IPv6 Organization-Local scope, and IPv4 Local-Scope multicast traffic.

**Rule ID:** `SV-80629r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast topology diagram to determine if there are any documented Admin-Local (FFx4::/16), Site-Local (FFx5::/16), or Organization-Local (FFx8::/16) multicast boundaries for IPv6 traffic or any Local-Scope (239.255.0.0/16) boundaries for IPv4 traffic. Verify the appropriate boundaries are configured on the applicable multicast-enabled interfaces. If appropriate multicast scope boundaries have not been configured, this is a finding. [HP] display current-configuration interface GigabitEthernet 0/2 interface GigabitEthernet0/2 port link-mode route description OVERSUBSCRIBE ip address 201.6.36.1 255.255.255.0 multicast boundary 239.255.0.0 16 ipv6 multicast boundary scope 4 ipv6 multicast boundary scope 5 ipv6 multicast boundary scope 8 ipv6 address 2115:C:24::1/120

