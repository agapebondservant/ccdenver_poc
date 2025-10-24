# STIG Benchmark: Arista MLS DCS-7000 Series RTR Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000002

**Group ID:** `V-217488`

### Rule: The Arista Multilayer Switch must enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy.

**Rule ID:** `SV-217488r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates authorized information to travel within a network and between interconnected networks. Controlling the flow of network traffic is critical so it does not introduce any unacceptable risk to the network infrastructure or data. An example of a flow control restriction is blocking outside traffic claiming to be from within the organization. For most routers, internal information flow control is a product of system design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each router enforces approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy. This requirement may be met through the use of IP access control lists. To verify IP access lists are configured, execute the "show ip access-lists summary" command, and check that the list is configured and is active on applicable interfaces. To verify the lists control the flow of information in accordance with organizational policy, enter the "show ip access-list [name]" command, and review the associated permit and deny statements. If the router does not enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-217489`

### Rule: The Arista Multilayer Switch must disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-217489r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap, while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DoD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network has documented their multicast topology and thereby knows which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IPv4 or IPv6 multicast routing is enabled, verify all interfaces enabled for PIM are documented in the network's multicast topology diagram. Review the router configuration via the "show running-config" command to determine if multicast routing is enabled and which interfaces are enabled for PIM, identified via the "ip pim sparse-mode" statement in the interface configuration. Alternatively, from the interface configuration mode, enter "show active all" and verify that the statement "no ip pim sparse-mode" is present, if PIM is not required for the active interface. If an interface is not required to support multicast routing and it is enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-217490`

### Rule: The Arista Multilayer Switch must bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-217490r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protocol Independent Multicast (PIM) is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. Protocol Independent Multicast traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, unauthorized routers can join the PIM domain and discover and use the rendezvous points and also advertise their rendezvous points into the domain. This can result in a denial of service by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast topology diagram and determine if router interfaces are enabled for IPv4 or IPv6 multicast routing. If the router is enabled for multicast routing, verify all interfaces enabled for PIM have a neighbor filter bound to the interface. The neighbor filter must only accept PIM control plane traffic from the documented PIM neighbors. To verify a neighbor filter is active, execute the "show running-config" command and find the "ip pim neighbor-filter [name]" statement in the interface configuration mode. If PIM neighbor filters are not bound to all interfaces that have PIM enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-217491`

### Rule: The Arista Multilayer Switch must establish boundaries for IPv6 Admin-Local, IPv6 Site-Local, IPv6 Organization-Local scope, and IPv4 Local-Scope multicast traffic.

**Rule ID:** `SV-217491r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast topology diagram to determine if there are any documented Admin-Local (FFx4::/16), Site-Local (FFx5::/16), or Organization-Local (FFx8::/16) multicast boundaries for IPv6 traffic or any Local-Scope (239.255.0.0/16) boundaries for IPv4 traffic. Verify the appropriate boundaries are configured on the applicable multicast-enabled interfaces via an "ip multicast boundary" statement in the interface configuration. If the appropriate boundaries are not configured on applicable multicast-enabled interfaces, this is a finding.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-217492`

### Rule: The Arista Multilayer Switch must be configured so inactive router interfaces are disabled.

**Rule ID:** `SV-217492r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify inactive interfaces on the router are disabled by executing a "show interface status" command and confirming the line "disabled" is present on any interface where the interface is inactive. If there are any inactive interfaces enabled on the router, this is a finding.

## Group: SRG-NET-000019-RTR-000009

**Group ID:** `V-217493`

### Rule: The Arista Multilayer Switch must protect an enclave connected to an Alternate Gateway by using an inbound filter that only permits packets with destination addresses within the sites address space.

**Rule ID:** `SV-217493r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Enclaves with Alternate Gateway connections must take additional steps to ensure there is no compromise on the enclave network or NIPRNet. Without verifying the destination address of traffic coming from the site's Alternate Gateway, the perimeter router could be routing transit data from the Internet into the NIPRNet. This could also make the perimeter router vulnerable to a DoS attack as well as provide a backdoor into the NIPRNet. The DoD enclave must ensure the ingress filter applied to external interfaces on a perimeter router connecting to an Approved Gateway is secure through filters permitting packets with a destination address belonging to the DoD enclave's address block.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of each router interface connecting to an Alternate Gateway via the "show running-config" command. Verify each permit statement of the ingress filter only permits packets with destination addresses of the site's NIPRNet address space or a destination address belonging to the address block assigned by the Alternate Gateway network service provider. If the ingress filter permits packets with addresses other than those specified, such as destination addresses of the site's NIPRNet address space or a destination address belonging to the address block assigned by the Alternate Gateway network service provider, this is a finding.

## Group: SRG-NET-000019-RTR-000010

**Group ID:** `V-217494`

### Rule: If Border Gateway Protocol (BGP) is enabled on The Arista Multilayer Switch, The Arista Multilayer Switch must not be a BGP peer with a router from an Autonomous System belonging to any Alternate Gateway.

**Rule ID:** `SV-217494r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The perimeter router will not use a routing protocol to advertise NIPRNet addresses to Alternate Gateways. Most ISPs use Border Gateway Protocol (BGP) to share route information with other autonomous systems, that is, any network under a different administrative control and policy than a local site. If BGP is configured on the perimeter router, no BGP neighbors will be defined to peer routers from an AS belonging to any Alternate Gateway. The only allowable method is a static route to reach the Alternate Gateway.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement applies only to DoDIN enclaves. Review the configuration of the router connecting to the Alternate Gateway via the "show router bgp [processID]" command. Verify there are no BGP neighbors configured to the remote AS that belongs to the Alternate Gateway service provider. If there are BGP neighbors connecting the remote AS of the Alternate Gateway service provider, this is a finding.

## Group: SRG-NET-000019-RTR-000011

**Group ID:** `V-217495`

### Rule: The Arista Multilayer Switch must not redistribute static routes to alternate gateway service provider into an Exterior Gateway Protocol or Interior Gateway Protocol to the NIPRNet or to other Autonomous System.

**Rule ID:** `SV-217495r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the static routes to the alternate gateway are being redistributed into an Exterior Gateway Protocol or Interior Gateway Protocol to a NIPRNet gateway, this could make traffic on NIPRNet flow to that particular router and not to the Internet Access Point routers. This could not only wreak havoc with traffic flows on NIPRNet, but it could overwhelm the connection from the router to the NIPRNet gateway(s) and also cause traffic destined for outside of NIPRNet to bypass the defenses of the Internet Access Points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement applies only to DoDIN enclaves. Review the configuration of the route connecting to the Alternate Gateway. Verify redistribution of static routes to the Alternate Gateway is not occurring by reviewing the running configuration via the "show running-config" command. In the appropriate routing protocol configuration, there must not be a "redistribute static" statement. If there is a redistribute static statement, there must be an accompanying route map to prevent redistribution of routes to the alternate gateway. If the static routes to the Alternate Gateway are being redistributed into an Exterior Gateway Protocol or Interior Gateway Protocol to a NIPRNet gateway, this is a finding.

## Group: SRG-NET-000019-RTR-000012

**Group ID:** `V-217496`

### Rule: The Arista Multilayer Switch must enforce that Interior Gateway Protocol instances configured on the out-of-band management gateway router only peer with their own routing domain.

**Rule ID:** `SV-217496r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the out-of-band management network, implementation of several safeguards for containment of management and production traffic boundaries must occur. Since the managed and management network are separate routing domains, configuration of separate Interior Gateway Protocol routing instances is critical on the router to segregate traffic from each network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the out-of-band management interface is an adjacency in the Interior Gateway Protocol routing domain for the management network. This requirement does not apply to in-band management networks. The out-of-band management interface will not form an adjacency with the IGP running on the switch. If the Arista MLS is acting as the gateway for the management network, and management traffic is ingressing the switch via in-band dataplane interfaces, these interfaces may be in a dedicated VRF for the management network. To verify this VRF, run a "show vrf" and confirm the interfaces handling management traffic are displayed in the resulting output. Alternatively, if VRFs are not used, the management network must use a separate routing domain that is not advertised or redistributed to the managed network. This can be verified by checking the relevant configuration statements for the routing protocol instances and ensuring no redistribute statement exists that will bridge the managed and management networks. Using the "show ip route" command will also verify this requirement by displaying the routing tables. Stipulating the VRF via the "show ip route vrf [name]" will display a separate routing table for a configured VRF, distinct from the default routing table in the default VRF, provided by the "show ip route" command with an unspecified VRF. If the router does not enforce that Interior Gateway Protocol instances configured on the out-of-band management gateway router only peer with their own routing domain, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-217497`

### Rule: The Arista Multilayer Switch must enforce that the managed network domain and the management network domain are separate routing domains and the Interior Gateway Protocol instances are not redistributed or advertised to each other.

**Rule ID:** `SV-217497r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the out-of-band management network, several safeguards must be implemented for containment of management and production traffic boundaries; otherwise, it is possible that management traffic will not be separated from production traffic. Since the managed network and the management network are separate routing domains, separate Interior Gateway Protocol routing instances must be configured on the router, one for the managed network and one for the out-of-band management network. In addition, the routes from the two domains must not be redistributed to each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Interior Gateway Protocol instance used for the managed network does not redistribute routes into the Interior Gateway Protocol instance used for the management network, and vice versa. This can be verified via the "show run section [routing protocol]" command. The output of this command will display the active configuration for the routing protocol on the switch. Verify the routing protocol configuration does not contain a statement redistributing or advertising routes from the managed domain into the management domain, or vice versa. Using the "show ip route" command will also verify this requirement by displaying the routing tables. Stipulating the VRF via the "show ip route vrf [name]" will display a separate routing table for a configured VRF, distinct from the default routing table in the default VRF, provided by the "show ip route" command with an unspecified VRF. If the Interior Gateway Protocol instance used for the managed network redistributes routes into the Interior Gateway Protocol instance used for the management network, or vice versa, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-217498`

### Rule: The Arista Multilayer Switch must enforce that any interface used for out-of-band management traffic is configured to be passive for the Interior Gateway Protocol that is utilized on that management interface.

**Rule ID:** `SV-217498r382735_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The out-of-band management access switch will connect to the management interface of the managed network elements. The management interface can be a true out-of-band management interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will directly connect to the out-of-band management network. An out-of-band management interface does not forward transit traffic, thereby providing complete separation of production and management traffic. Since all management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an out-of-band management port, the interface functioning as the management interface must be configured so that management traffic, both data plane and control plane, does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the management interface is configured as passive for the Interior Gateway Protocol instance for the managed network. The configuration of the routing protocol viewable via the "show running-config" command must include the following statement: passive-interface [management] [#] or passive-interface [default] Note that not all protocols support the concept of a passive interface, such as the use of BGP for an IGP. As the function of these protocols is different, if this statement is missing from a protocol that does not support this function, this is not a finding. If the management interface is not configured as passive for the Interior Gateway Protocol instance for the managed network, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-217499`

### Rule: The Arista Multilayer Switch must be configured to disable non-essential capabilities.

**Rule ID:** `SV-217499r382903_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if services or functions not required for operation, or not related to router functionality (e.g., DNS, email client or server, FTP server, or web server) are enabled. If unnecessary services and functions are enabled on the router, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-217500`

### Rule: The Arista Multilayer Switch must encrypt all methods of configured authentication for the OSPF routing protocol.

**Rule ID:** `SV-217500r385516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network, or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration for the following configuration statement under the interface configuration for any interface participating in the OSPF topology. SHA1 must be used instead of MD5 in all cases when that option is available. ip ospf authentication message-digest ip ospf message-digest-key [number] md5 [type] [key] For IPv6 Authentication, one of the following statements must be present under the ipv6 router OSPF configuration statement, or on any interface running OSPFv3, depending on the type of encryption established. There are two methods of authentication for OSPFv3 in this scenario; the first uses authentication header (AH), and the second uses Authentication Header with Encapsulating Security Payload. OSPFv3 authentication can be configured for an interface or an area, and interface configuration will override area configuration. Users may configure a key or a passphrase. interface ethernet1 ipv6 ospf authentication ipsec spi [spi number] [md5/sha1] [passphrase/key] [0/7] [passphrase/key] OR interface ethernet1 ipv6 ospf encryption ipsec spi [spi number] esp null [md5/sha1] [passphrase/key] [0/7] [passphrase/key] In an area configuration, the following text must be included under the "ipv6 router ospf [process ID]" configuration section. ipv6 router ospf 200 area [area number] authentication ipsec spi [spi number] [md5/sha1] [passphrase/key] [0/7] [passphrase/key] OR for ESP ipv6 router ospf 200 area 0 encryption ipsec spi [spi] esp null [md5/sha1] [0/7] [key] | passphrase [0/7] [key] If either of these statements is not present, OSPF is not using encryption for authentication, and this is a finding.

## Group: SRG-NET-000364-RTR-000109

**Group ID:** `V-217501`

### Rule: The Arista Multilayer Switch must only allow incoming communications from authorized sources to be routed to authorized destinations.

**Rule ID:** `SV-217501r856151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic can be restricted directly by an ACL (which is a firewall function) or by Policy Routing. Policy Routing is a technique used to make routing decisions based on a number of different criteria other than just the destination network, including source or destination network, source or destination address, source or destination port, protocol, packet size, and packet classification. This overrides the router's normal routing procedures used to control the specific paths of network traffic. It is normally used for traffic engineering but can also be used to meet security requirements; for example, traffic that is not allowed can be routed to the Null0 or discard interface. Policy Routing can also be used to control which prefixes appear in the routing table. Traffic can be restricted directly by an ACL (which is a firewall function), or by Policy Routing. This requirement is intended to allow network administrators the flexibility to use whatever technique is most effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if the router only allows incoming communications from authorized sources to be routed to authorized destinations. To verify an ACL is configured to allow only incoming communications from authorized sources, execute a "show ip access-list" command and verify the pertinent permit and deny statements are in place. Validate the access list is configured on the appropriate interface via the "show ip access-list summary" command or by reviewing the interface configuration viewable in the "show running-config" command. If PBR is being used, verify the appropriate policy maps have been configured by reviewing the switch running-config via the "show running-config" command. If the router does not restrict incoming communications to allow only authorized sources and destinations, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-217502`

### Rule: The Arista Multilayer Switch must not enable the RIP routing protocol.

**Rule ID:** `SV-217502r385516_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if RIP is enabled via the "show running-config" command. RIP is disabled by default on an Arista switch and is only enabled when explicitly configured. If a configuration statement enabling RIP is in the Arista Multilayer Switch configuration, this is a finding.

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-217523`

### Rule: The Arista Multilayer Switch must enable neighbor router authentication for control plane protocols except RIP.

**Rule ID:** `SV-217523r945861_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration; for every protocol that affects the routing or forwarding tables (where information is exchanged between neighbors), verify that neighbor router authentication is enabled. For BGP, this can be verified via the "show running-config" command and validating that any configured neighbor has an associated password statement. For OSPF, under the interface configuration mode, verify the following statements are configured: ip ospf authentication message-digest ip ospf message-digest-key [number] md5 [type] [key] For IS-IS, under the interface configuration mode, verify the following statements are configured: isis authentication mode md5 [level-1|level-2] isis authentication key [key-string] [level-1|level-2] Alternatively, under “show isis interface” the authentication mode on the interface must show as being set to MD5. Additionally, the global IS-IS router configuration must be set. From the output of “show isis summary” verify that the authentication mode for Level-1 and/or Level-2 as applicable, is set to MD5. If authentication is not enabled for BGP, OSPF, and IS-IS, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-217524`

### Rule: The Arista Multilayer Switch must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field via egress filter or by enabling Unicast Reverse Path Forwarding.

**Rule ID:** `SV-217524r945858_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious actor as a platform to launch cyber attacks on third parties. This is a common practice in "botnets", which are collections of compromised computers using malware to attack (usually DDoS) other computers or networks. DDoS attacks frequently leverage IP source address spoofing, in which packets with false source IP addresses send traffic to multiple hosts, which then send return traffic to the hosts with the IP addresses that were forged. This can generate significant, even massive, amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. The router must not accept any outbound IP packets that contain an illegitimate address in the source address field by enabling Unicast Reverse Path Forwarding (uRPF) strict mode or by implementing an egress ACL. Unicast Reverse Path Forwarding (uRPF) provides an IP address spoof protection capability. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is only applicable to external-facing interfaces of a network edge router. Review the router configuration to verify uRPF or an egress filter to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field has been configured on all external interfaces. This is only applicable to perimeter routers. If uRPF or an egress filter to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field has not been configured on all internal interfaces in an enclave, this is a finding. To verify that uRPF is configured, review the running-config for the interfaces required. The statement "ip-verify unicast source reachable" must be in the configuration. To verify use of an egress filter, verify an IP access list is configured that permits traffic sourced from within the organization address space and that the access list is applied to the egress interface.

## Group: SRG-NET-000362-RTR-000124

**Group ID:** `V-217525`

### Rule: The Arista Multilayer Switch must ensure all Exterior Border Gateway Protocol (eBGP) routers are configured to use Generalized TTL Security Mechanism (GTSM) or are configured to meet RFC3682.

**Rule ID:** `SV-217525r856153_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As described in RFC 3682, Generalized TTL Security Mechanism (GTSM) is designed to protect a router's IP-based control plane from DoS attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all Exterior Border Gateway Protocol-speaking routers. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent routers; that is, the Exterior Border Gateway Protocol peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration. If it is not configured to use Generalized TTL Security Mechanism (GTSM) or is not configured to provide equivalent functionality as per RFC3682 for all Exterior Border Gateway Protocol peering sessions, this is a finding. The Arista MLS does not have a command to enable GTSM. Instead, any EBGP neighbor statement must include the "ebgp-multihop [hop]" configuration statement, viewable in the "router bgp [AS number]" section of the running config. For adjacent peers, this number must be 255. Additionally, the control-plane ACL must have a statement that matches against the neighbor's correct TTL to allow inbound packets to the Switch. The neighbor TTL must be 255 for an adjacent peer or the result of 255-(number of hops) for a multihop peer.

## Group: SRG-NET-000018-RTR-000001

**Group ID:** `V-220130`

### Rule: The Arista Multilayer Switch must enforce information flow control using explicit security attributes (for example, IP addresses, port numbers, protocol, Autonomous System, or interface) on information, source, and destination objects.

**Rule ID:** `SV-220130r856154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Restrictions can be enforced based on source and destination IP addresses as well as the ports and services being requested. This requirement should enforce the deny-by-default policy whereby only the known and accepted traffic will be allowed outbound and inbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If explicit security attributes (for example, IP addresses, port numbers, protocol, Autonomous System, or interface) are not used to enforce information flow control, this is a finding. Review the configuration of any access control list on the switch to determine if explicit attributes are being utilized. The ACL must include explicit attributes such as ip addresses, port numbers, protocols, etc. Note that the Arista MLS includes a deny-by-default statement that is not displayed in the CLI. This statement exists at the end of every ACL.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-220131`

### Rule: The Arista Multilayer Switch must manage excess bandwidth to limit the effects of packet flooding types of denial of service (DoS) attacks.

**Rule ID:** `SV-220131r539011_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding DDoS attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and interview the system administrator; verify that a mechanism for traffic prioritization and bandwidth reservation exists. This arrangement must ensure that sufficient capacity is available for mission-critical traffic and enforce the traffic priorities specified by the Combatant Commanders/Services/Agencies. To review the configuration, execute a "show qos interfaces" command to see the qos configuration for all interfaces or "show qos interfaces [type] [number] to review the configuration for a specific interface. QoS must be configured according to organizational policies. If no such scheme exists or it is not configured, this is a finding.

## Group: SRG-NET-000512-RTR-000100

**Group ID:** `V-220133`

### Rule: The Arista Multilayer Switch must configure the maximum hop limit value to at least 32.

**Rule ID:** `SV-220133r539012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message to be used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached their destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if the maximum hop limit has been configured. If it has been configured, then it must be set to at least 32. If it has not been configured, the default value must be determined. The default value for the Arista MLS is 64. Review the interface configuration via the "show running-config" command for the statement ipv6 nd ra hop-limit 32 If the default value is below 32 and the maximum hop limit value has not been configured (set to at least 32), this is a finding. In any case, maximum hop limit must be at least 32.

## Group: SRG-NET-000512

**Group ID:** `V-264429`

### Rule: The Arista MLS RTR must be using a version supported by the vendor.

**Rule ID:** `SV-264429r992084_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

