# STIG Benchmark: VMware NSX 4.x Tier-0 Gateway Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-265390`

### Rule: The NSX Tier-0 Gateway router must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-265390r994520_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it could be intercepted by unauthorized or unintended personnel. Limiting where within the network a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DOD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and thereby knows which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway >> Interfaces and GRE Tunnels, and click on the number of interfaces present to open the interfaces dialog. Expand each interface that is not required to support multicast routing, then expand "Multicast" and verify PIM is disabled. If PIM is enabled on any interfaces that are not supporting multicast routing, this is a finding.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-265393`

### Rule: The NSX Tier-0 Gateway router must be configured to have all inactive interfaces removed.

**Rule ID:** `SV-265393r994529_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use. If an interface is no longer used, the configuration must be deleted and the interface disabled. For sub-interfaces, delete sub-interfaces that are on inactive interfaces and delete sub-interfaces that are themselves inactive. If the sub-interface is no longer necessary for authorized communications, it must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway >> Interfaces and GRE Tunnels, and click on the number of interfaces present to open the interfaces dialog. Review each interface present to determine if they are not in use or inactive. If there are any interfaces present on a Tier-0 Gateway that are not in use or inactive, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-265404`

### Rule: The NSX Tier-0 Gateway router must be configured to have the Dynamic Host Configuration Protocol (DHCP) service disabled if not in use.

**Rule ID:** `SV-265404r999914_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway to view the DHCP configuration. If a DHCP profile is configured and not in use, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-265406`

### Rule: The NSX Tier-0 Gateway router must be configured to use encryption for Open Shortest Path First (OSPF) routing protocol authentication.

**Rule ID:** `SV-265406r994568_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, Enhanced Interior Gateway Routing Protocol [EIGRP], and Intermediate System to Intermediate System [IS-IS]) and exterior gateway protocols (such as Border Gateway Protocol [BGP]), multiprotocol label switching (MPLS)-related protocols (such as Label Distribution Protocol [LDP]), and multicast-related protocols. Typically routing protocols must be setup on both sides so knowing the authentication key does not necessarily mean an attacker would be able to setup a rogue router and peer with a legitimate one and inject malicious routes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using OSPF, this is Not Applicable. To verify OSPF areas are using authentication with encryption, do the following: From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the "Tier-0 Gateway". Expand "OSPF", click the number next to "Area Definition", and view the "Authentication" field for each area. If OSPF area definitions do not have the "Authentication" field set to "MD5" and a "Key ID" and "Password" configured, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-265428`

### Rule: The NSX Tier-0 Gateway router must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-265428r994634_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A malicious platform can use a compromised host in an enclave to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet; thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand Tier-0 Gateway >> Interfaces and GRE Tunnels, and then click on the number of interfaces present to open the interfaces dialog. Expand each interface to view the URPF Mode configuration. If URPF Mode is not set to "Strict" on any interface, this is a finding.

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-265431`

### Rule: The NSX Tier-0 Gateway router must be configured to implement message authentication for all control plane protocols.

**Rule ID:** `SV-265431r994643_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information. This includes Border Gateway Protocol (BGP), Routing Information Protocol (RIP), Open Shortest Path First (OSPF), Enhanced Interior Gateway Routing Protocol (EIGRP), Intermediate System to Intermediate System (IS-IS) and Label Distribution Protocol (LDP). Satisfies: SRG-NET-000230-RTR-000001, SRG-NET-000230-RTR-000002</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP or OSPF, this is Not Applicable. Since the router does not reveal if a BGP password is configured, interview the router administrator to determine if a password is configured on BGP neighbors. If BGP neighbors do not have a password configured, this is a finding. To verify OSPF areas are using authentication, do the following: From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway expand the "Tier-0 Gateway". Expand "OSPF", click the number next to "Area Definition", and view the "Authentication" field for each area. If OSPF area definitions do not have Password or MD5 set for authentication, this is a finding.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-265432`

### Rule: The NSX Tier-0 Gateway must be configured to use a unique password for each autonomous system (AS) with which it peers.

**Rule ID:** `SV-265432r994646_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between External Border Gateway Protocol (eBGP) neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP, this is Not Applicable. Since the NSX Tier-0 Gateway does not reveal the current password, interview the router administrator to determine if unique passwords are being used. If unique passwords are not being used for each AS, this is a finding.

## Group: SRG-NET-000362-RTR-000113

**Group ID:** `V-265441`

### Rule: The NSX Tier-0 Gateway router must be configured to have Internet Control Message Protocol (ICMP) unreachable notifications disabled on all external interfaces.

**Rule ID:** `SV-265441r999915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Host unreachable ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down. Review each Tier-0 Gateway Firewall rule to verify one exists to drop ICMP unreachable messages. If a rule does not exist to drop ICMP unreachable messages, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-265442`

### Rule: The NSX Tier-0 Gateway router must be configured to have Internet Control Message Protocol (ICMP) mask replies disabled on all external interfaces.

**Rule ID:** `SV-265442r999916_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down menu. Review each Tier-0 Gateway Firewall rule to verify one exists to drop ICMP mask replies. If a rule does not exist to drop ICMP mask replies, this is a finding.

## Group: SRG-NET-000362-RTR-000115

**Group ID:** `V-265443`

### Rule: The NSX Tier-0 Gateway router must be configured to have Internet Control Message Protocol (ICMP) redirects disabled on all external interfaces.

**Rule ID:** `SV-265443r999917_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Redirect ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down menu. Review each Tier-0 Gateway Firewalls rules to verify one exists to drop ICMP redirects. If a rule does not exist to drop ICMP redirects, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-265444`

### Rule: The NSX Tier-0 Gateway router must be configured to use the Border Gateway Protocol (BGP) maximum prefixes feature to protect against route table flooding and prefix de-aggregation attacks.

**Rule ID:** `SV-265444r994682_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. In 1997, misconfigured routers in the Florida Internet Exchange network (AS7007) de-aggregated every prefix in their routing table and started advertising the first /24 block of each of these prefixes as their own. Faced with this additional burden, the internal routers became overloaded and crashed repeatedly. This caused prefixes advertised by these routers to disappear from routing tables and reappear when the routers came back online. As the routers came back after crashing, they were flooded with the routing table information by their neighbors. The flood of information would again overwhelm the routers and cause them to crash. This process of route flapping served to destabilize not only the surrounding network but also the entire internet. Routers trying to reach those addresses would choose the smaller, more specific /24 blocks first. This caused backbone networks throughout North America and Europe to crash. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the de-aggregation risk. BGP maximum prefix must be used on all eBGP routers to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering autonomous system (AS). Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP, this is Not Applicable. From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway with BGP enabled, expand the Tier-0 Gateway. Expand BGP, click on the number next to "BGP Neighbors", and then view the router filters for each neighbor. If "Maximum Routes" is not configured, or a route filter does not exist for each BGP neighbor, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-265468`

### Rule: The NSX Tier-0 Gateway router must be configured to use its loopback address as the source address for Internal Border Gateway Protocol (IBGP) peering sessions.

**Rule ID:** `SV-265468r994754_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the Border Gateway Protocol (BGP) routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router’s loopback address instead of the numerous physical interface addresses. The routers within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using iBGP, this is Not Applicable. From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway with BGP enabled, expand the Tier-0 Gateway. Expand BGP, click on the number next to BGP Neighbors, then view the source address for each neighbor. If the Source Address is not configured as the Tier-0 Gateway loopback address for the iBGP session, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-265479`

### Rule: The NSX Tier-0 Gateway router must be configured to advertise a hop limit of at least 32 in Router Advertisement messages for IPv6 stateless auto-configuration deployments.

**Rule ID:** `SV-265479r994787_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery (ND) protocol allows a hop limit value to be advertised by routers in a Router Advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IPv6 forwarding is not enabled, this is Not Applicable. From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand Tier-0 Gateway >>Additional Settings. Click on the ND profile name to view the hop limit. If the hop limit is not configured to at least 32, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-265483`

### Rule: The NSX Tier-0 Gateway router must be configured to have routing protocols disabled if not in use.

**Rule ID:** `SV-265483r999918_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway to view if border gateway protocol (BGP) or Open Shortest Path First (OSPF) is enabled. If BGP and/or OSPF is enabled and not in use, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-265484`

### Rule: The NSX Tier-0 Gateway router must be configured to have multicast disabled if not in use.

**Rule ID:** `SV-265484r999919_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway, then expand "Multicast" to view the multicast configuration. If multicast is enabled and not in use, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-265485`

### Rule: The NSX Tier-0 Gateway router must be configured to use encryption for border gateway protocol (BGP) routing protocol authentication.

**Rule ID:** `SV-265485r994805_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as Open Shortest Path First [OSPF], Enhanced Interior Gateway Routing Protocol [EIGRP], and Intermediate System to Intermediate System [IS-IS]) and Exterior Gateway Protocols (such as BGP), multiprotocol label switching (MPLS)-related protocols (such as Label Distribution Protocol [LDP]), and multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP, this is Not Applicable. To verify BGP neighbors are using authentication with encryption, do the following: From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-0 Gateways. For every Tier-0 Gateway, expand the "Tier-0 Gateway". Expand "BGP", click the number next to "BGP Neighbors" and expand each BGP neighbor. Expand the "Timers and Password" section and review the Password field. If any BGP neighbors do not have a password configured, this is a finding.

