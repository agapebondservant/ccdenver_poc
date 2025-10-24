# STIG Benchmark: VMware NSX-T Tier-0 Gateway RTR Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-RTR-000003

**Group ID:** `V-251744`

### Rule: The NSX-T Tier-0 Gateway must be configured to reject inbound route advertisements for any prefixes belonging to the local autonomous system (AS).

**Rule ID:** `SV-251744r810116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements belonging to the local AS can result in traffic looping or being black holed, or at a minimum using a non-optimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using eBGP, this is Not Applicable. From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand Tier-0 Gateway >>BGP. Near to BGP Neighbors, click on the number present to open the dialog. For each neighbor examine any router filters to determine if any inbound route filters are applied. If the In Filter is not configured with a prefix list that rejects prefixes belonging to the local AS, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-251745`

### Rule: The NSX-T Tier-0 Gateway must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-251745r810119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DoD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and thereby know which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway >> Interfaces, and click on the number of interfaces present to open the interfaces dialog. Expand each interface that is not required to support multicast routing, then expand "Multicast" and verify PIM is disabled. If PIM is enabled on any interfaces that are not supporting multicast routing, this is a finding.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-251746`

### Rule: The NSX-T Tier-0 Gateway must be configured to have all inactive interfaces removed.

**Rule ID:** `SV-251746r810122_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. If an interface is no longer used, the configuration must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway >> Interfaces, and click on the number of interfaces present to open the interfaces dialog. Review each interface present to determine if they are not in use or inactive. If there are any interfaces present on a Tier-0 Gateway that are not in use or inactive, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-251747`

### Rule: The NSX-T Tier-0 Gateway must be configured to have the DHCP service disabled if not in use.

**Rule ID:** `SV-251747r810125_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway expand the Tier-0 Gateway to view the DHCP configuration. If a DHCP profile is configured and not in use, this is a finding.

## Group: SRG-NET-000193-RTR-000112

**Group ID:** `V-251748`

### Rule: The NSX-T Tier-0 Gateway must be configured to enforce a Quality-of-Service (QoS) policy to limit the effects of packet flooding denial-of-service (DoS) attacks.

**Rule ID:** `SV-251748r810128_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, QoS, or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Segments. For every Segment connected to a Tier-0 Gateway, Expand Segment >> Expand Segment Profiles >> Record QOS Segment Profile. Go to Segment Profiles >> Expand QOS Segment Profile recorded in previous steps. If there are traffic priorities specified by the Combatant Commands/Services/Agencies needed to ensure sufficient capacity for mission-critical traffic and none are configured, this is a finding.

## Group: SRG-NET-000205-RTR-000001

**Group ID:** `V-251749`

### Rule: The NSX-T Tier-0 Gateway must be configured to restrict traffic destined to itself.

**Rule ID:** `SV-251749r810131_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The route processor handles traffic destined to the router, the key component used to build forwarding paths, and is also instrumental with all network management functions. Hence, any disruption or DoS attack to the route processor can result in mission critical network outages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules and choose each Tier-0 Gateway in the drop-down. Review each Tier-0 Gateway Firewalls rules to verify rules exist to restrict traffic to itself. If a rule or rules do not exist to restrict traffic to external interface IPs, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-251750`

### Rule: Unicast Reverse Path Forwarding (uRPF) must be enabled on the NSX-T Tier-0 Gateway.

**Rule ID:** `SV-251750r810134_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyber attacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet; thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand Tier-0 Gateway >> Interfaces, and then click on the number of interfaces present to open the interfaces dialog. Expand each interface to view the URPF Mode configuration. If URPF Mode is not set to "Strict" on any interface, this is a finding.

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-251751`

### Rule: The NSX-T Tier-0 Gateway must be configured to implement message authentication for all control plane protocols.

**Rule ID:** `SV-251751r856692_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP or OSPF, this is Not Applicable. Since the NSX-T Tier-0 Gateway does not reveal if a BGP password is configured, interview the router administrator to determine if a password is configured on BGP neighbors. If BGP neighbors do not have a password configured, this is a finding. To verify OSPF areas are using authentication do the following: From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway expand the "Tier-0 Gateway". Expand "OSPF", click the number next to Area Definition, and view the Authentication field for each area. If OSPF area definitions do not have Password or MD5 set for authentication, this is a finding. Note: OSPF support was introduced in version 3.1.1.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-251752`

### Rule: The NSX-T Tier-0 Gateway must be configured to use a unique key for each autonomous system (AS) with which it peers.

**Rule ID:** `SV-251752r856693_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between eBGP neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP, this is Not Applicable. Since the NSX-T Tier-0 Gateway does not reveal the current password, interview the router administrator to determine if unique keys are being used. If unique keys are not being used for each AS, this is a finding.

## Group: SRG-NET-000362-RTR-000113

**Group ID:** `V-251753`

### Rule: The NSX-T Tier-0 Gateway must be configured to have Internet Control Message Protocol (ICMP) unreachable notifications disabled on all external interfaces.

**Rule ID:** `SV-251753r856694_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Host unreachable ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down. Review each Tier-0 Gateway Firewall rule to verify one exists to drop ICMP unreachable messages. If a rule does not exist to drop ICMP unreachable messages, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-251754`

### Rule: The NSX-T Tier-0 Gateway must be configured to have Internet Control Message Protocol (ICMP) mask replies disabled on all external interfaces.

**Rule ID:** `SV-251754r856695_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down. Review each Tier-0 Gateway Firewall rule to verify one exists to drop ICMP mask replies. If a rule does not exist to drop ICMP mask replies, this is a finding.

## Group: SRG-NET-000362-RTR-000115

**Group ID:** `V-251755`

### Rule: The NSX-T Tier-0 Gateway must be configured to have Internet Control Message Protocol (ICMP) redirects disabled on all external interfaces.

**Rule ID:** `SV-251755r856696_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Redirect ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules, and choose each Tier-0 Gateway in the drop-down. Review each Tier-0 Gateway Firewalls rules to verify one exists to drop ICMP redirects. If a rule does not exist to drop ICMP redirects, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-251756`

### Rule: The NSX-T Tier-0 Gateway must be configured to use the BGP maximum prefixes feature to protect against route table flooding and prefix de-aggregation attacks.

**Rule ID:** `SV-251756r856697_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. In 1997, misconfigured routers in the Florida Internet Exchange network (AS7007) de-aggregated every prefix in their routing table and started advertising the first /24 block of each of these prefixes as their own. Faced with this additional burden, the internal routers became overloaded and crashed repeatedly. This caused prefixes advertised by these routers to disappear from routing tables and reappear when the routers came back online. As the routers came back after crashing, they were flooded with the routing table information by their neighbors. The flood of information would again overwhelm the routers and cause them to crash. This process of route flapping served to destabilize not only the surrounding network but also the entire internet. Routers trying to reach those addresses would choose the smaller, more specific /24 blocks first. This caused backbone networks throughout North America and Europe to crash. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the de-aggregation risk. BGP maximum prefix must be used on all eBGP routers to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering AS. Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using BGP, this is Not Applicable. From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway with BGP enabled, expand the Tier-0 Gateway. Expand BGP, click on the number next to BGP Neighbors, and then view the Router Filters for each neighbor. If Maximum Routes is not configured or a route filter does not exist for each BGP neighbor, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-251757`

### Rule: The NSX-T Tier-0 Gateway must be configured to use its loopback address as the source address for iBGP peering sessions.

**Rule ID:** `SV-251757r810155_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the BGP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router’s loopback address instead of the numerous physical interface addresses. When the loopback address is used as the source for eBGP peering, the BGP session will be harder to hijack since the source address to be used is not known globally—making it more difficult for a hacker to spoof an eBGP neighbor. By using traceroute, a hacker can easily determine the addresses for an eBGP speaker when the IP address of an external interface is used as the source address. The routers within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is not using iBGP, this is Not Applicable. From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway with BGP enabled, expand the Tier-0 Gateway. Expand BGP, click on the number next to BGP Neighbors, then view the source address for each neighbor. If the Source Address is not configured as the NSX-T Tier-0 Gateway loopback address for the iBGP session, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-251758`

### Rule: The NSX-T Tier-0 Gateway must be configured to have routing protocols disabled if not in use.

**Rule ID:** `SV-251758r810158_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway to view if BGP or OSPF is enabled. If BGP and/or OSPF is enabled and not in use, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-251759`

### Rule: The NSX-T Tier-0 Gateway must be configured to have multicast disabled if not in use.

**Rule ID:** `SV-251759r810161_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-0 Gateways. For every Tier-0 Gateway, expand the Tier-0 Gateway, then expand Multicast to view the Multicast configuration. If Multicast is enabled and not in use, this is a finding.

