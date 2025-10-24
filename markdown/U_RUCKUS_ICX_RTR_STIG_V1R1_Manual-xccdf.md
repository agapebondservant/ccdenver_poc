# STIG Benchmark: RUCKUS ICX Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-RTR-000001

**Group ID:** `V-273569`

### Rule: The RUCKUS ICX router must be configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies.

**Rule ID:** `SV-273569r1110905_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, and devices) within information systems. Enforcement occurs, for example, in boundary protection devices (e.g., gateways, routers, guards, encrypted tunnels, and firewalls) that employ rule sets or establish how configuration settings that restrict information system services, provide a packet filtering capability based on header information, or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that access control lists (ACLs) and filters are configured to allow or deny traffic for specific source and destination addresses as well as ports and protocols. In this example, SSL traffic is permitted to a specific internal host. interface ethernet 1/1/10 port-name Link_to_DISN ip address x.12.1.10 255.255.255.0 ip access-group Filter_Perimeter in ! ip access-list extended Filter_Perimeter sequence 10 permit tcp any any established sequence 20 permit tcp host x.12.1.9 host x.12.1.10 eq bgp sequence 30 permit tcp host x.12.1.9 eq bgp host x.12.1.10 sequence 40 permit icmp host x.12.1.9 host x.12.1.10 echo sequence 50 permit icmp host x.12.1.9 host x.12.1.10 echo-reply sequence 60 permit tcp any host x.12.1.22 eq ssl sequence 70 deny ip any any log If the router is not configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies, this is a finding.

## Group: SRG-NET-000018-RTR-000002

**Group ID:** `V-273570`

### Rule: The RUCKUS ICX BGP router must be configured to reject inbound route advertisements for any Bogon prefixes.

**Rule ID:** `SV-273570r1110906_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements for Bogon prefixes can result in the local autonomous system (AS) becoming a transit for malicious traffic as it will in turn advertise these prefixes to neighbor autonomous systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a prefix list exists in the config: SSH@ICX(config)# show ip prefix-lists ip prefix-list PREFIX-FLTR: 1 entries seq 5 deny 0.0.0.0/8 le 32 seq 10 deny 10.0.0.0/8 le 32 ... seq 999 permit 0.0.0.0/0 le 8 Confirm that prefix list is applied to BGP: router bgp neighbor x.x.x.x prefix-list PREFIX-FLTR in If the router is not configured to reject inbound route advertisements for any Bogon prefixes, this is a finding.

## Group: SRG-NET-000018-RTR-000003

**Group ID:** `V-273571`

### Rule: The RUCKUS ICX BGP router must be configured to reject inbound route advertisements for any prefixes belonging to the local autonomous system (AS).

**Rule ID:** `SV-273571r1110907_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements belonging to the local AS can result in traffic looping or being black holed, or at a minimum using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review BGP neighbor configuration using "show running-config | begin router bgp". If any BGP neighbor is configured for the "neighbor x.x.x. allowas-in" command, this is a finding.

## Group: SRG-NET-000018-RTR-000004

**Group ID:** `V-273572`

### Rule: The RUCKUS ICX BGP router must be configured to reject inbound route advertisements from a customer edge (CE) router for prefixes that are not allocated to that customer.

**Rule ID:** `SV-273572r1110908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a best practice, a service provider should only accept customer prefixes that have been assigned to that customer and any peering autonomous systems. A multi-homed customer with BGP speaking routers connected to the internet or other external networks could be breached and used to launch a prefix de-aggregation attack. Without ingress route filtering of customers, the effectiveness of such an attack could impact the entire IP core and its customers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify there are filters defined to only accept routes for prefixes that belong to specific customers. 1. Verify a prefix-list exists for the customer ("show running-config | include prefix") similar to the following: ip prefix-list customer1 seq 5 permit x.x.1.0/24 le 32 ip prefix-list customer1 seq 10 deny 0.0.0.0/0 ge 8 2. Confirm the prefix list has been applied to eBGP neighbor similar to the following: route-map bgp_cust1 permit 10 match ip address prefix-list customer1 router bgp local-as 1001 neighbor x.x.x.x remote-as 500 neighbor x.x.x.x route-map in bgp_cust1 If the RUCKUS ICX router is not configured to reject prefixes not allocated to the customer, this is a finding.

## Group: SRG-NET-000018-RTR-000005

**Group ID:** `V-273573`

### Rule: The RUCKUS ICX BGP router must be configured to reject outbound route advertisements for any prefixes that do not belong to any customer or the local autonomous system (AS).

**Rule ID:** `SV-273573r1111031_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Advertisement of routes by an autonomous system for networks that do not belong to any of its customers pulls traffic away from the authorized network. This causes a denial of service (DoS) on the network that allocated the block of addresses and may cause a DoS on the network that is inadvertently advertising it as the originator. It is also possible that a misconfigured or compromised router within the GIG IP core could redistribute IGP routes into BGP, thereby leaking internal routes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify there is a filter defined to only advertise routes for prefixes that belong to any customers or the local AS. This requirement is not applicable for the DODIN Backbone. 1. Verify a prefix-list is configured for routes belonging to the local AS. ICX# show ip prefix-lists ip prefix-list local-AS: 2 entries seq 5 permit x.1.1.0/24 seq 10 permit x.1.2.0/24 2. Verify the prefix-list is applied to outbound routes to neighbors. ICX# show ip bgp config Current BGP configuration: router bgp local-as 1000 neighbor x.x.x.x remote-as 1001 neighbor x.x.x.x prefix-list local-AS out If the router does not filter out prefix advertisements that do not belong on the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000006

**Group ID:** `V-273574`

### Rule: The RUCKUS ICX BGP router must be configured to reject route advertisements from BGP peers that do not list their autonomous system (AS) number as the first AS in the AS_PATH attribute.

**Rule ID:** `SV-273574r1110883_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure the IP core is not used as a transit network for unauthorized or possibly even internet traffic. All autonomous system boundary routers (ASBRs) must ensure updates received from eBGP peers list their AS number as the first AS in the AS_PATH attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify the router is configured to deny updates received from eBGP peers that do not list their AS number as the first AS in the AS_PATH attribute. router bgp local-as 1000 neighbor 10.1.1.1 remote-as 1100 neighbor 10.1.1.1 enforce-first-as enable If the router is not configured to enforce the first AS in the AS_PATH attribute for eBGP peers, this is a finding.

## Group: SRG-NET-000018-RTR-000007

**Group ID:** `V-273575`

### Rule: The RUCKUS ICX Multicast Source Discovery Protocol router must be configured to filter received source-active multicast advertisements for any undesirable multicast groups and sources.

**Rule ID:** `SV-273575r1110884_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The interoperability of BGP extensions for interdomain multicast routing and MSDP enables seamless connectivity of multicast domains between autonomous systems. MP-BGP advertises the unicast prefixes of the multicast sources used by Protocol Independent Multicast (PIM) routers to perform RPF checks and build multicast distribution trees. MSDP is a mechanism used to connect multiple PIM sparse-mode domains, allowing RPs from different domains to share information about active sources. When RPs in peering multicast domains hear about active sources, they can pass on that information to their local receivers, thereby allowing multicast data to be forwarded between the domains. Configuring an import policy to block multicast advertisements for reserved, Martian, single-source multicast, and any other undesirable multicast groups, as well as any source-group (S, G) states with Bogon source addresses, would assist in avoiding unwanted multicast traffic from traversing the core.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for SA filter on MSDP peer: ICX# show msdp peer x.x.x.x | include Input Input SA Filter:Applicable Input (S,G) route-map:MSDP_SA_filter Input RP route-map:None If any configured MSDP peer is not configured to filter undesirable multicast groups and sources, this is a finding.

## Group: SRG-NET-000018-RTR-000008

**Group ID:** `V-273576`

### Rule: The RUCKUS ICX Multicast Source Discovery Protocol router must be configured to filter source-active multicast advertisements to external MSDP peers to avoid global visibility of local-only multicast sources and groups.

**Rule ID:** `SV-273576r1110885_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To avoid global visibility of local information, there are a number of source-group (S, G) states in a PIM-SM domain that must not be leaked to another domain, such as multicast sources with private address, administratively scoped multicast addresses, and the auto-RP groups (224.0.1.39 and 224.0.1.40). Allowing a multicast distribution tree, local to the core, to extend beyond its boundary could enable local multicast traffic to leak into other autonomous systems and customer networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for SA filter on MSDP peer: ICX# show msdp peer x.x.x.x | include Output  Output SA Filter:Applicable Output (S,G) route-map:out_MSDP_SA_filter Output RP route-map:None If any configured MSDP peer is not configured to filter outbound advertisements to avoid local-only multicast sources and groups, this is a finding.

## Group: SRG-NET-000018-RTR-000009

**Group ID:** `V-273577`

### Rule: The RUCKUS ICX MSDP router must be configured to limit the amount of source-active messages it accepts on a per peer basis.

**Rule ID:** `SV-273577r1110886_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To reduce any risk of a denial-of-service (DoS) attack from a rogue or misconfigured MSDP router, the router must be configured to limit the number of source-active messages it accepts from each peer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check for SA filter on MSDP peer: ICX# show msdp peer x.x.x.x | include Input Input SA Filter:Applicable Input (S,G) route-map:MSDP_SA_filter Input RP route-map:None If any configured MSDP peer is not configured to limit source-active messages using an inbound filter, this is a finding.

## Group: SRG-NET-000018-RTR-000010

**Group ID:** `V-273578`

### Rule: The RUCKUS ICX BGP router must be configured to reject route advertisements from CE routers with an originating AS in the AS_PATH attribute that does not belong to that customer.

**Rule ID:** `SV-273578r1110887_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure the local AS is not used as a transit network for unauthorized traffic. To ensure that the local AS does not carry any prefixes that do not belong to any customers, all PE routers must be configured to reject routes with an originating AS other than that belonging to the customer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review ICX router configuration for AS_PATH filter statements for BGP: ip as-path access-list BGP_filter seq 5 permit ^yy$ ip as-path access-list BGP_filter seq 10 deny .* ! router bgp local-as xx neighbor x.4.4.4 remote-as yy neighbor x.4.4.4 filter-list BGP_filter in ! If the ICX router is not configured to reject updates from CE routers with an originating AS in the AS_PATH attribute that does not belong to that customer, this is a finding.

## Group: SRG-NET-000019-RTR-000002

**Group ID:** `V-273580`

### Rule: The RUCKUS ICX perimeter router must be configured to enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy.

**Rule ID:** `SV-273580r1110910_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates authorized information to travel within a network and between interconnected networks. Controlling the flow of network traffic is critical so it does not introduce any unacceptable risk to the network infrastructure or data. An example of a flow control restriction is blocking outside traffic claiming to be from within the organization. For most routers, internal information flow control is a product of system design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check perimeter router configuration for port connected to DISN for access-list filter to control flow of information between interconnected networks in accordance with applicable policy. In this example, SSL traffic is permitted to a specific internal host: interface ethernet 1/1/10 port-name Link_to_DISN ip address x.12.1.10 255.255.255.0 ip access-group Filter_Perimeter in ! ip access-list extended Filter_Perimeter sequence 10 permit tcp any any established sequence 20 permit tcp host x.12.1.9 host x.12.1.10 eq bgp sequence 30 permit tcp host x.12.1.9 eq bgp host x.12.1.10 sequence 40 permit icmp host x.12.1.9 host x.12.1.10 echo sequence 50 permit icmp host x.12.1.9 host x.12.1.10 echo-reply sequence 60 permit tcp any host x.12.1.22 eq ssl sequence 70 deny ip any any log If the router does not enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-273581`

### Rule: The RUCKUS ICX multicast router must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-273581r1110911_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DOD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and know which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network's multicast topology diagram and examine the running configuration to determine whether PIM has been enabled on any unnecessary ports (disabled by default). interface ethernet 1/1/3 ip address x.95.5.1/24 ip pim-sparse If PIM is enabled on unnecessary interfaces, this is a finding.

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-273582`

### Rule: The RUCKUS ICX multicast router must be configured to bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-273582r1110912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PIM is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. PIM traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, unauthorized routers can join the PIM domain, discover and use the rendezvous points, and also advertise their rendezvous points into the domain. This can result in a denial of service by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify on all PIM enabled interfaces, there is a neighbor filter applied: interface ethernet 1/1/10 ip address x.12.1.10 255.255.255.0 ip pim-sparse ip pim neighbor-filter PIM_NEIGHBORS ! ip access-list standard PIM_NEIGHBORS sequence 10 permit host x.1.2.6 ! If an interface is enabled for PIM without a neighbor filter list, this is a finding.

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-273583`

### Rule: The RUCKUS ICX multicast edge router must be configured to establish boundaries for administratively scoped multicast traffic.

**Rule ID:** `SV-273583r1110888_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify boundaries are established for administratively scoped multicast traffic: ip access-list standard MULTICAST_SCOPE sequence 10 deny 239.0.0.0 0.255.255.255 sequence 20 permit any ! interface ethernet 1/1/10 ip address x.12.1.10 255.255.255.0 ip pim-sparse ip pim neighbor-filter PIM_NEIGHBORS ip multicast-boundary MULTICAST_SCOPE ! If the multicast boundary is not established, this is a finding.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-273584`

### Rule: The RUCKUS ICX router must be configured to have all inactive interfaces disabled.

**Rule ID:** `SV-273584r1110889_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use. If an interface is no longer used, the configuration must be deleted and the interface disabled. For sub-interfaces, delete sub-interfaces that are on inactive interfaces and delete sub-interfaces that are themselves inactive. If the sub-interface is no longer necessary for authorized communications, it must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify inactive interfaces are disabled: interface ethernet 1/1/11 disable ! If inactive interfaces are not disabled, this is a finding.

## Group: SRG-NET-000019-RTR-000008

**Group ID:** `V-273585`

### Rule: The RUCKUS ICX perimeter router must be configured to protect an enclave connected to an alternate gateway by using an inbound filter that only permits packets with destination addresses within the site's address space.

**Rule ID:** `SV-273585r1111051_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enclaves with alternate gateway connections must take additional steps to ensure there is no compromise on the enclave network or NIPRNet. Without verifying the destination address of traffic coming from the site's alternate gateway, the perimeter router could be routing transit data from the internet into the NIPRNet. This could also make the perimeter router vulnerable to a denial-of-service (DoS) attack as well as provide a back door into the NIPRNet. The DOD enclave must ensure the ingress filter applied to external interfaces on a perimeter router connecting to an Approved Gateway is secure through filters permitting packets with a destination address belonging to the DOD enclave's address block.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration of each router interface connecting to an alternate gateway. 1. Verify an ACL exists to allow only desired traffic (example includes SSL hosts). ip access-list extended FILTER_ISP sequence 10 permit tcp any any established sequence 20 permit icmp host x.12.1.16 host x.12.1.17 echo sequence 30 permit icmp host x.12.1.16 host x.12.1.17 echo-reply sequence 40 permit tcp any host x.12.1.22 eq ssl sequence 50 permit tcp any host x.12.1.23 eq ssl sequence 60 permit esp any host x.12.1.24 sequence 70 permit ahp any host x.12.1.24 sequence 80 deny ip any any log ! 2. Check that ACL is applied to alternative gateway interface. interface ethernet 1/1/10 ip address x.12.1.10 255.255.255.0 ip access-group FILTER_ISP in ! If the alternative gateway interface is not configured with an ACL permitting only the destination addresses in the sites address space, this is a finding.

## Group: SRG-NET-000019-RTR-000009

**Group ID:** `V-273586`

### Rule: The RUCKUS ICX perimeter router must be configured to not be a Border Gateway Protocol (BGP) peer to an alternate gateway service provider.

**Rule ID:** `SV-273586r1111032_rule`
**Severity:** high

**Description:**
<VulnDiscussion>ISPs use BGP to share route information with other autonomous systems (i.e., other ISPs and corporate networks). If the perimeter router was configured to BGP peer with an ISP, NIPRNet routes could be advertised to the ISP, thereby creating a backdoor connection from the internet to the NIPRNet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Determine the IP address of the alternate gateway service provider and confirm that the ICX is not configured with that address as a BGP peer. If the ICX is configured with the alternate gateway service provider IP address as a BGP peer, this is a finding.

## Group: SRG-NET-000019-RTR-000010

**Group ID:** `V-273587`

### Rule: The RUCKUS ICX perimeter router must be configured to not redistribute static routes to an alternate gateway service provider into BGP or an IGP peering with the NIPRNet or to other autonomous systems.

**Rule ID:** `SV-273587r1111281_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the static routes to the alternate gateway are being redistributed into an Exterior Gateway Protocol or Interior Gateway Protocol to a NIPRNet gateway, this could make traffic on NIPRNet flow to that particular router and not to the Internet Access Pointerface routers. This could not only wreak havoc with traffic flows on NIPRNet, but it could overwhelm the connection from the router to the NIPRNet gateway(s) and also cause traffic destined for outside of NIPRNet to bypass the defenses of the Internet Access Points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review ICX router configuration for statements redistributing static routes into IGP or BGP: router bgp local-as 1001 neighbor x.4.4.4 remote-as 1000 redistribute static ! router ospf redistribute static ! If static routes with the alternate gateway service provider as the next hop exist and static routes are redistributed into an IGP or BGP (without a route-map filter), this is a finding.

## Group: SRG-NET-000019-RTR-000011

**Group ID:** `V-273588`

### Rule: The RUCKUS ICX out-of-band management (OOBM) gateway router must be configured to have separate Interior Gateway Protocol (IGP) instances for the managed network and management network.

**Rule ID:** `SV-273588r1110913_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, implementation of several safeguards for containment of management and production traffic boundaries must occur. Since the managed and management network are separate routing domains, configuration of separate IGP routing instances is critical on the router to segregate traffic from each network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify there is a separate VRF for management and production domains: ICX# show vrf Total number of VRFs configured: 2 Status Codes - A:active, D:pending deletion, I:inactive Name Default RD vrf|v4|v6 Routes Interfaces Mgmt 1:1 A | A| A 12 ve111 ve211 ve311* Prod 10:12 A | A| A 4 ve1117 port-id tn1* Total number of IPv4 unicast route for all non-default VRF is 8 Total number of IPv6 unicast route for all non-default VRF is 8 If the OOBM gateway router does not have separate VRFs for management and production or the interfaces are associated with the wrong VRF, this is a finding.

## Group: SRG-NET-000019-RTR-000012

**Group ID:** `V-273589`

### Rule: The RUCKUS ICX out-of-band management (OOBM) gateway router must be configured to not redistribute routes between the management network routing domain and the managed network routing domain.

**Rule ID:** `SV-273589r1110914_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, several safeguards must be implemented for containment of management and production traffic boundaries; otherwise, it is possible that management traffic will not be separated from production traffic. Since the managed network and the management network are separate routing domains, separate Interior Gateway Protocol (IGP) routing instances must be configured on the router, one for the managed network and one for the OOBM network. In addition, the routes from the two domains must not be redistributed to each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration for static routes with the "next-hop-vrf" keyword. If static routes with "next-hop-vrf" are used and IGP/BGP routes redistribute these static routes, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-273590`

### Rule: The RUCKUS ICX multicast Rendezvous Pointerface (RP) router must be configured to filter Protocol Independent Multicast (PIM) Register messages received from the Designated Router (DR) for any undesirable multicast groups and sources.

**Rule ID:** `SV-273590r1110891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that register messages are accepted only for authorized multicast groups and sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check configuration for presence of accept-register filter for PIM: ICX# show ip pim sparse Global PIM Sparse Mode Settings Maximum Mcache : 12288 Current Count : 0 Hello interval : 30 Neighbor timeout : 105 Join/Prune interval : 60 Inactivity interval : 180 Hardware Drop Enabled : Yes Prune Wait Interval : 3 Bootstrap Msg interval : 60 Candidate-RP Msg interval : 60 Register Suppress Time : 60 Register Probe Time : 10 Register Stop Delay : 10 SPT Threshold : 1 SSM Enabled : No Register Rate Limit : 1 pps Register Filter : PIM_REG_FILTER Route Precedence : uc-non-default uc-default mc-non-default mc-default Join/Prune Policy : No Slow Path Disable All : No Slow Path Enable SSM : No Slow Path Filter Acl : None If the RP router peering with PIM-SM routers is not configured with a policy to block registration messages for any undesirable multicast groups and sources, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-273591`

### Rule: The RUCKUS ICX multicast Rendezvous Pointerface (RP) router must be configured to filter Protocol Independent Multicast (PIM) Join messages received from the Designated Router (DR) for any undesirable multicast groups.

**Rule ID:** `SV-273591r1110892_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that join messages are only accepted for authorized multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check PIM sparse Join/Prune policy configuration for required filters: ICX# show ip pim jp Vrf Instance : default-vrf --------------------------- (RP,G) JP policy --------- (RP,G) JP policy count: 1 RP-Address ACL Name (RP,G) Join Drops (RP,G) Prune Drops 10.1.1.1 FILTER_PIM_JOINS 0 0 (*,G) and (S,G) JP policy --------- ACL Name (*,G) Join Drops (*,G) Prune Drops (S,G) Join Drops (S,G) Prune Drops EXT_FILTER_PIM_JOINS 0 0 0 0 If the RP is not configured to filter PIM register messages, this is a finding.

## Group: SRG-NET-000078-RTR-000001

**Group ID:** `V-273594`

### Rule: The RUCKUS ICX router must be configured to log all packets that have been dropped.

**Rule ID:** `SV-273594r1110893_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being done or attempted to be done, and by whom, to compile an accurate risk assessment. Auditing the actions on network devices provides a means to recreate an attack or identify a configuration mistake on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check ACL deny statements for log keywords and that logging is enabled on applicable bindings: ICX# show ip access Block_host_v4 Extended IP access list Block_host_v4: 3 entries 10: permit ipv6 any any 20: deny ip host 192.168.10.253 any log 30: permit ip any any ICX# show running-config vlan 10 ... ip access-group Block_host_v4 in ethernet 1/3/1 logging enable If ACL deny statements lack the log keyword or logging is not enabled in the "ip access-group..." command, this is a finding.

## Group: SRG-NET-000131-RTR-000083

**Group ID:** `V-273596`

### Rule: The RUCKUS ICX router must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-273596r1110915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration for the following command: manager [registrar|registrar-list] If this command exists, this is a finding.

## Group: SRG-NET-000168-RTR-000078

**Group ID:** `V-273597`

### Rule: The RUCKUS ICX router must be configured to authenticate all routing protocol messages using NIST-validated FIPS 198-1 message authentication code algorithm.

**Rule ID:** `SV-273597r1110916_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. Since MD5 is vulnerable to "birthday" attacks and may be compromised, routing protocol authentication must use FIPS 198-1 validated algorithms and modules to encrypt the authentication key. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols. Satisfies: SRG-NET-000168-RTR-000078, SRG-NET-000168-RTR-000077</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration for routing protocol authentication and encryption. OSPF: router ospf area 0 ! interface ethernet 1/1/1 ip ospf area 0 ip ospf authentication hmac-sha-256 key-id 10 key 2 $Nlx9cy1TR31TIS0tfURuXA== ipv6 address fd00:12::2/32 ! BGP: keychain mykeychain tcp key-id 1 password 2 $Uyt9R3NVfURuXH1a authentication-algorithm aes-128-cmac send-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 no accept-ao-mismatch send-id 1 recv-id 1 router bgp local-as xxxx neighbor x.x.x.x remote-as 10 neighbor x.x.x.x ao mykeychain If OSPF or BGP is configured and does not use authentication/encryption, this is a finding.

## Group: SRG-NET-000193-RTR-000112

**Group ID:** `V-273601`

### Rule: The RUCKUS ICX PE router must be configured to enforce a Quality-of-Service (QoS) policy to limit the effects of packet flooding denial-of-service (DoS) attacks.

**Rule ID:** `SV-273601r1110917_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to determine whether DDoS attack prevention is configured (values may vary): ICX#show running-config | include burst ip icmp attack-rate burst-normal 500 burst-max 1000 lockup 300 ip tcp burst-normal 30 burst-max 100 lockup 300 If DSCP trust is required, verify that it has been applied to the necessary interfaces. ICX# show running-config interface ethernet x/x/x interface ethernet x/x/x trust dscp If DDoS protection is not configured or DSCP trust is required but not configured, this is a finding.

## Group: SRG-NET-000193-RTR-000113

**Group ID:** `V-273602`

### Rule: The RUCKUS ICX PE router must be configured to enforce a Quality-of-Service (QoS) policy in accordance with the QoS DODIN Technical Profile.

**Rule ID:** `SV-273602r1110894_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the QoS-ToS mapping of the PE router. If the DSCP mapping to priority queues does not comply with the GiG Technical Profile, this is a finding.

## Group: SRG-NET-000193-RTR-000114

**Group ID:** `V-273603`

### Rule: The RUCKUS ICX P router must be configured to enforce a Quality-of-Service (QoS) policy in accordance with the QoS GIG Technical Profile.

**Rule ID:** `SV-273603r1110895_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the QoS-ToS mapping of the P router. If the DSCP mapping to priority queues does not comply with the GiG Technical Profile, this is a finding.

## Group: SRG-NET-000202-RTR-000001

**Group ID:** `V-273604`

### Rule: The RUCKUS ICX perimeter router must be configured to deny network traffic by default and allow network traffic by exception.

**Rule ID:** `SV-273604r1110881_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only connections that are essential and approved are allowed. This requirement applies to both inbound and outbound network communications traffic. All inbound and outbound traffic must be denied by default. Firewalls and perimeter routers should only allow traffic through that is explicitly permitted. The initial defense for the internal network is to block any traffic at the perimeter that is attempting to make a connection to a host residing on the internal network. In addition, allowing unknown or undesirable outbound traffic by the firewall or router will establish a state that will permit the return of this undesirable traffic inbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that external interfaces are configured with ACLs that permit traffic by exception. ip access-list extended EXT-ACL sequence 10 permit sshow host x.x.x.x host y.y.y.y log sequence 20 permit ip x.x.x.0 0.0.0.255 any sequence 30 deny ip any any log interface ethernet x/x/x ip access-group EXT-ACL in logging enable If the ACL or filter is not configured to allow specific ports and protocols and deny all other traffic, this is a finding. If the filter is not configured inbound on all external interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000001

**Group ID:** `V-273605`

### Rule: The RUCKUS ICX router must be configured to restrict traffic destined to itself.

**Rule ID:** `SV-273605r1110875_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The route processor handles traffic destined to the router, the key component used to build forwarding paths, and is instrumental with all network management functions. Hence, any disruption or denial-of-service (DoS) attack to the route processor can result in mission critical network outages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the external and internal Access Control Lists (ACLs) to verify the router is configured to only allow specific management and control plane traffic from specific sources destined to itself (addresses and protocols may vary). 1. Review the access lists. ip access-list extended EXT-ACL sequence 10 permit tcp host x.11.1.1 eq bgp host x.11.1.2 sequence 20 permit tcp host x.11.1.1 host x.11.1.2 eq bgp sequence 30 permit icmp host x.11.1.1 host x.11.1.2 echo sequence 40 permit icmp host x.11.1.1 host x.11.1.2 echo-reply sequence 50 deny ip host x.11.1.1 host x.11.1.2 log permit … … … … deny ip any any log ! ip access-list extended INT-ACL sequence 10 permit icmp any any sequence 20 permit ospf host 10.1.12.1 host 10.1.12.2 sequence 30 permit tcp 10.2.1.0 0.0.0.255 host 10.1.12.2 eq ssh sequence 40 permit tcp 10.2.1.0 0.0.0.255 host 10.1.12.2 eq radius sequence 50 permit udp 10.2.1.0 0.0.0.255 host 10.1.12.2 eq snmp sequence 60 permit udp 10.2.1.0 0.0.0.255 host 10.1.12.2 eq ntp sequence 70 deny ip any host 10.1.12.2 log permit … … … … deny ip any any log ! 2. Verify ACLs are applied to desired interfaces. interface ethernet x/x/x ip address x.11.1.2/31 ip access-group EXT-ACL in logging enable ! interface ethernet x/x/x ip address 10.1.12.2 255.255.255.0 ip access-group INT-ACL in logging enable If the router is not configured to restrict traffic destined to itself, this is a finding.

## Group: SRG-NET-000205-RTR-000002

**Group ID:** `V-273606`

### Rule: The RUCKUS ICX router must be configured to drop all fragmented Internet Control Message Protocol (ICMP) packets destined to itself.

**Rule ID:** `SV-273606r1110918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Fragmented ICMP packets can be generated by hackers for denial-of-service (DoS) attacks such as Ping O' Death and Teardrop. It is imperative that all fragmented ICMP packets are dropped.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify router management interfaces are configured to drop fragmented packets. Interface ethernet 1/1/1 ip access-group EXT_ACL in logging enable ip access-group frag deny If the router is not configured with a receive-path filter to drop all fragmented ICMP packets, this is a finding. Note: If the platform does not support the receive path filter, verify that all layer 3 interfaces have an ingress ACL to control what packets are allowed to be destined to the router for processing.

## Group: SRG-NET-000205-RTR-000003

**Group ID:** `V-273607`

### Rule: The RUCKUS ICX perimeter router must be configured to filter traffic destined to the enclave in accordance with the guidelines contained in DOD Instruction 8551.1.

**Rule ID:** `SV-273607r1110919_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Vulnerability assessments must be reviewed by the system administrator, and protocols must be approved by the information assurance (IA) staff before entering the enclave. Access control lists (ACLs) are the first line of defense in a layered security approach. They permit authorized packets and deny unauthorized packets based on port or service type. They enhance the posture of the network by not allowing packets to reach a potential target within the security domain. The lists provided are highly susceptible ports and services that should be blocked or limited as much as possible without adversely affecting customer requirements. Auditing packets attempting to penetrate the network but that are stopped by an ACL will allow network administrators to broaden their protective ring and more tightly define the scope of operation. If the perimeter is in a Deny-by-Default posture and what is allowed through the filter is in accordance with DOD Instruction 8551.1, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to PPS being blocked would be satisfied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the external and internal Access Control Lists (ACLs) to verify the router is configured to filter traffic destined to the enclave in accordance with the guidelines contained in DOD Instruction 8551.1. If the router does not filter traffic in accordance with the guidelines contained in DOD 8551, this is a finding.

## Group: SRG-NET-000205-RTR-000004

**Group ID:** `V-273608`

### Rule: The RUCKUS ICX perimeter router must be configured to filter ingress traffic at the external interface on an inbound direction.

**Rule ID:** `SV-273608r1111033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access lists are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of routers makes use of access lists for restricting access to services on the router itself as well as for filtering traffic passing through the router. Inbound versus Outbound: Note that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The router can protect itself before damage is inflicted. - The input port is still known and can be filtered on. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify ACLs are applied to desired external interfaces on the inbound direction: interface ethernet x/x/x ip address x.11.1.2/31 ip access-group EXT-ACL in logging enable ! If the perimeter router is not configured to filter ingress traffic on the external interface(s), this is a finding.

## Group: SRG-NET-000205-RTR-000005

**Group ID:** `V-273609`

### Rule: The RUCKUS ICX perimeter router must be configured to filter egress traffic at the internal interface on an inbound direction.

**Rule ID:** `SV-273609r1111034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access lists are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of routers makes use of access lists for restricting access to services on the router itself as well as for filtering traffic passing through the router. Inbound versus Outbound: Note that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The router can protect itself before damage is inflicted. - The input port is still known and can be filtered on. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify ACLs are applied to desired internal interfaces on the inbound direction: interface ethernet x/x/x port-name internal-interface ip address x.11.1.2/31 ip access-group INT-ACL in logging enable ! If the perimeter router is not configured to filter traffic leaving the network on the inbound direction of internal interface(s), this is a finding.

## Group: SRG-NET-000205-RTR-000006

**Group ID:** `V-273610`

### Rule: The RUCKUS ICX BGP router must be configured to reject outbound route advertisements for any prefixes belonging to the IP core.

**Rule ID:** `SV-273610r1110922_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outbound route advertisements belonging to the core can result in traffic either looping or being black holed, or at a minimum, using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify there is a filter defined to block route advertisements for prefixes that belong to the IP core. 1. Verify a prefix-list has been configured containing prefixes belonging to the IP core. ip prefix-list FILTER_CORE_PREFIXES seq 10 deny x.1.1.0/24 le 32 ip prefix-list FILTER_CORE_PREFIXES seq 20 deny x.1.2.0/24 le 32 ip prefix-list FILTER_CORE_PREFIXES seq 30 permit 0.0.0.0/0 ge 8 2. Verify the prefix-list has been applied to all external BGP peers as shown in the example below: router bgp local-as xxxx neighbor x.0.0.1 remote-as yy neighbor x.0.0.1 ao mykeychain address-family ipv4 unicast neighbor x.0.0.1 prefix-list FILTER_CORE_PREFIXES out If the router is not configured to reject outbound route advertisements for prefixes belonging to the IP core, this is a finding.

## Group: SRG-NET-000205-RTR-000007

**Group ID:** `V-273611`

### Rule: The RUCKUS ICX PE router must be configured to block any traffic destined to IP core infrastructure.

**Rule ID:** `SV-273611r1110876_rule`
**Severity:** high

**Description:**
<VulnDiscussion>IP/MPLS networks providing VPN and transit services must provide, at the least, the same level of protection against denial-of-service (DoS) attacks and intrusions as layer 2 networks. Although the IP core network elements are hidden, security should never rely entirely on obscurity. IP addresses can be guessed. Core network elements must not be accessible from any external host. Protecting the core from any attack is vital for the integrity and privacy of customer traffic as well as the availability of transit services. A compromise of the IP core can result in an outage or, at a minimum, nonoptimized forwarding of customer traffic. Protecting the core from an outside attack also prevents attackers from using the core to attack any customer. Hence, it is imperative that all routers at the edge deny traffic destined to any address belonging to the IP core infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify an ingress ACL is applied to all CE-facing interfaces and verify the ingress ACL rejects and logs packets destined to the IP core address block. 1. Review the router configuration to verify that an ingress ACL is applied to all external or CE-facing interfaces. interface ethernet 1/1/1 ip address x.1.1.2/30 ip access-group BLOCK_TO_CORE in logging enable ! 2. Verify the ingress ACL discards and logs packets destined to the IP core address space. ip access-list extended BLOCK_TO_CORE sequence 10 deny ip any 10.x.0.0 0.0.255.255 log remark permit other traffic sequence 20 permit ip any any ! If the PE router is not configured to block any traffic with a destination address assigned to the IP core infrastructure, this is a finding.

## Group: SRG-NET-000205-RTR-000008

**Group ID:** `V-273612`

### Rule: The RUCKUS ICX PE router must be configured with Unicast Reverse Path Forwarding (uRPF) loose mode enabled on all CE-facing interfaces.

**Rule ID:** `SV-273612r1110923_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The uRPF feature is a defense against spoofing and denial-of-service (DoS) attacks by verifying if the source address of any ingress packet is reachable. To mitigate attacks that rely on forged source addresses, all provider edge routers must enable uRPF loose mode to guarantee that all packets received from a CE router contain source addresses that are in the route table.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if uRPF loose mode is enabled on all CE-facing interfaces. 1. Check that RPF is configured globally (requires reload when initially set). reverse-path-check 2. Review the router configuration to determine if uRPF loose mode is enabled on all CE-facing interfaces. Interface ethernet 1/1/1 rpf-mode loose If uRPF loose mode is not enabled on all CE-facing interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000009

**Group ID:** `V-273613`

### Rule: The RUCKUS ICX management network gateway must be configured to transport management traffic to the Network Operations Center (NOC) via dedicated circuit.

**Rule ID:** `SV-273613r1110924_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the production network is managed in-band or out-of-band (OOBM), the management network could be housed at a NOC that is located remotely at single or multiple interconnected sites. NOC interconnectivity, as well as connectivity between the NOC and the managed network, must be enabled using IPsec tunnels or dedicated circuits to provide the separation and integrity of the managed traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the network topology diagram to determine connectivity between the managed network and the NOC. Review the management network gateway router configuration to validate the path and interface that the management traffic traverses. If management traffic is not transported between the managed network and the NOC via dedicated circuit, this is a finding.

## Group: SRG-NET-000205-RTR-000010

**Group ID:** `V-273614`

### Rule: The RUCKUS ICX out-of-band management (OOBM) gateway router must be configured to forward only authorized management traffic to the Network Operations Center (NOC).

**Rule ID:** `SV-273614r1110925_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM network is an IP network used exclusively for the transport of operations, administration, maintenance, and provisioning (OAM&P) data from the network being managed to the operations support system (OSS) components located at the NOC. Its design provides connectivity to each managed network device, enabling network management traffic to flow between the managed network elements and the NOC. This allows the use of paths separate from those used by the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the network topology diagram to determine connectivity between the managed network and the NOC. Review the OOBM gateway router configuration to validate the path the management traffic traverses. Verify only management traffic is forwarded through the OOBM interface or IPsec tunnel. If an OOBM link is used, verify the only authorized management traffic is transported to the NOC by reviewing the outbound ACL applied to the OOBM interface as shown in the example below: 1. Note the outbound ACL applied to the OOBM interface. interface ethernet 1/1/1 port-name OOBM-to-NOC ip access-group MGMT_TRAFFIC_ACL out logging enable ! 2. Review the outbound ACL and verify only management traffic is forwarded to the NOC. ip access-list extended MGMT_TRAFFIC_ACL sequence 10 permit tcp x.1.34.0 0.0.0.255 10.22.2.0 0.0.0.255 eq radius sequence 20 permit tcp x.1.34.0 0.0.0.255 10.22.2.0 0.0.0.255 eq ssh sequence 30 permit udp x.1.34.0 0.0.0.255 10.22.2.0 0.0.0.255 eq snmp sequence 40 permit udp x.1.34.0 0.0.0.255 10.22.2.0 0.0.0.255 eq shell sequence 50 permit icmp x.1.34.0 0.0.0.255 10.22.2.0 0.0.0.255 sequence 60 deny ip any any log ! If traffic other than authorized management traffic is permitted through the OOBM interface, this is a finding.

## Group: SRG-NET-000205-RTR-000011

**Group ID:** `V-273615`

### Rule: The RUCKUS ICX out-of-band management (OOBM) gateway router must be configured to block any traffic destined to itself that is not sourced from the OOBM network or the Network Operations Center (NOC).

**Rule ID:** `SV-273615r1111064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, several safeguards must be implemented for containment of management and production traffic boundaries. It is imperative that hosts from the managed network are not able to access the OOBM gateway router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify traffic destined to itself is only sourced by the OOBM or the NOC. In the example below, the OOBM backbone network is 10.11.1.0/24, the NOC address spaces is 10.12.1.0/24, and the OOBM LAN address space at remote site connecting to the managed network is 10.13.1.0/24. 1. Note the inbound ACL applied to the OOBM interfaces. interface ethernet 1/2/1 port-name OOBM-to-NOC ip address 10.11.1.8 255.255.255.0 ip access-group TRAFFIC_FROM_NOC in logging enable ! interface ethernet 1/2/2 port-name OOBM_LAN_ACCESS_SWITCH ip address 10.13.1.1 255.255.255.0 ip access-group TRAFFIC_TO_NOC in logging enable 2. Review the inbound ACL bound to any OOB interface connecting to the OOBM backbone and verify traffic destined to itself is only from the OOBM or NOC address space. ip access-list extended TRAFFIC_FROM_NOC sequence 10 permit ip 10.11.1.0 0.0.0.255 host 10.11.1.8 sequence 20 permit ip 10.12.1.0 0.0.0.255 host 10.11.1.8 sequence 30 permit ip 10.11.1.0 0.0.0.255 host 10.13.1.1 sequence 40 permit ip 10.12.1.0 0.0.0.255 host 10.13.1.1 sequence 50 deny ip any host 10.11.1.8 log sequence 60 deny ip any host 10.13.1.1 log sequence 70 permit ip 10.11.1.0 0.0.0.255 10.13.1.0 0.0.0.255 sequence 80 permit ip 10.12.1.0 0.0.0.255 10.13.1.0 0.0.0.255 sequence 90 deny ip any any log ! 3. Review the inbound ACL bound to any OOBM LAN interfaces and verify traffic destined to itself is from the OOBM LAN address space. ip access-list extended TRAFFIC_TO_NOC sequence 10 permit ip 10.13.1.0 0.0.0.255 host 10.13.1.1 sequence 20 permit ip 10.13.1.0 0.0.0.255 host 10.11.1.8 sequence 30 deny ip any host 10.13.1.1 log sequence 40 deny ip any host 10.11.1.8 log sequence 50 permit ip 10.13.1.0 0.0.0.255 10.11.1.0 0.0.0.255 sequence 60 permit ip 10.13.1.0 0.0.0.255 10.12.1.0 0.0.0.255 sequence 70 deny ip any any log ! If the router does not block any traffic destined to itself that is not sourced from the OOBM network or the NOC, this is a finding.

## Group: SRG-NET-000205-RTR-000012

**Group ID:** `V-273616`

### Rule: The RUCKUS ICX router must be configured to only permit management traffic that ingresses and egresses the OOBM interface.

**Rule ID:** `SV-273616r1110927_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. An OOBM interface does not forward transit traffic, thereby providing complete separation of production and management traffic. Since all management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an OOBM port, the interface functioning as the management interface must be configured so that management traffic does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the OOBM interface does not forward transit traffic. 1. Verify the managed interface has an inbound and outbound ACL configured. 2. Verify the ingress filter only allows management, IGP, and ICMP traffic. Note: If the management interface is a true OOBM interface, this requirement is not applicable. If the router does not restrict traffic that ingresses and egresses the management interface, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-273618`

### Rule: The RUCKUS ICX perimeter router must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field via egress filter or by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-273618r1111065_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet; thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify uRPF or an egress ACL has been configured on all internal interfaces to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field. uRPF example: reverse-path-check ! interface ethernet 1/1/1 port-name downstream_link_to_LAN ip address 10.1.25.5 255.255.255.0 rpf-mode loose Egress ACL example: interface ethernet 1/2/2 port-name downstream_link_to_LAN ip address 10.1.25.5 255.255.255.0 ip access-group EGRESS_FILTER in logging enable ! … … … ip access-list extended EGRESS_FILTER sequence 10 permit udp 10.1.15.0 0.0.0.255 any eq dns sequence 20 permit tcp 10.1.15.0 0.0.0.255 any eq ftp sequence 30 permit tcp 10.1.15.0 0.0.0.255 any eq ftp-data sequence 40 permit tcp 10.1.15.0 0.0.0.255 any eq http sequence 50 permit tcp 10.1.15.0 0.0.0.255 any eq ssl sequence 60 permit icmp 10.1.15.0 0.0.0.255 any sequence 70 permit icmp 10.1.15.0 0.0.0.255 any echo sequence 80 deny ip any any ! If uRPF or an egress ACL to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field has not been configured on all internal interfaces in an enclave, this is a finding.

## Group: SRG-NET-000205-RTR-000015

**Group ID:** `V-273619`

### Rule: The RUCKUS ICX perimeter router must be configured to block all packets with any IP options.

**Rule ID:** `SV-273619r1110928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast switched and henceforth must be punted to the router processor. Hackers who initiate denial-of-service (DoS) attacks on routers commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the router. The end result is a reduction in the effects of the DoS attack on the router and on downstream routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it will drop all packets with IP options as shown below. ip options drop If the router is not configured to drop all packets with IP options, this is a finding.

## Group: SRG-NET-000205-RTR-000016

**Group ID:** `V-273620`

### Rule: The RUCKUS ICX PE router must be configured to ignore or block all packets with any IP options.

**Rule ID:** `SV-273620r1110929_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast switched and therefore must be punted to the router processor. Hackers who initiate denial-of-service (DoS) attacks on routers commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the router. The end result is a reduction in the effects of the DoS attack on the router and on downstream routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it will drop all packets with IP options as shown below: ip options drop If the router is not configured to drop all packets with IP options, this is a finding.

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-273621`

### Rule: The RUCKUS ICX router must be configured to implement message authentication for all control plane protocols.

**Rule ID:** `SV-273621r1110930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols used to exchange routing or packet forwarding information. This includes BGP, RIP, OSPF, EIGRP, IS-IS, and LDP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration. Verify neighbor router authentication is enabled for all routing protocols. The configuration examples below depicts OSPF and BGP authentication. OSPF: keychain mykeychain key-id 1 password 2 $b2I9LT0tQGk2Mg== authentication-algorithm hmac-sha-256 send-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 accept-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 ! interface ethernet 1/1/1 ip address x.x.x.x x.x.x.x ip ospf area 0 ip ospf authentication keychain mykeychain ! BGP: keychain mykeychain tcp key-id 1 password 2 $Nlx9UyEtLVNiVSEtbn0ic24tfWJuVW4= authentication-algorithm aes-128-cmac send-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 accept-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 no accept-ao-mismatch send-id 1 recv-id 1 ! ! router bgp local-as 1001 neighbor x.0.0.1 remote-as 10 neighbor x.0.0.1 ao mykeychain If authentication is not enabled on all routing protocols, this is a finding.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-273622`

### Rule: The RUCKUS ICX BGP router must be configured to use a unique key for each autonomous system (AS) that it peers with.

**Rule ID:** `SV-273622r1110931_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between eBGP neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP configuration to determine if it is peering with multiple autonomous systems. Interview the information security systems manager (ISSM) and router administrator to determine if unique keys are being used. keychain AS-xxxx tcp key-id 1 password 2 $Uyt9R3NVfURuXH1a authentication-algorithm aes-128-cmac send-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 no accept-ao-mismatch send-id 1 recv-id 1 keychain AS-yyyy tcp key-id 1 password 2 $Uyt9R3123URuXH1a authentication-algorithm aes-128-cmac send-lifetime start 03-05-2024 00:00:00 end 09-01-2024 00:00:00 no accept-ao-mismatch send-id 2 recv-id 2 router bgp local-as xxxx neighbor x.0.0.1 remote-as 10 neighbor x.0.0.1 ao AS-xxxx neighbor y.0.0.1 remote-as 11 neighbor y.0.0.1 as AS-yyyy If unique keys are not being used, this is a finding.

## Group: SRG-NET-000230-RTR-000003

**Group ID:** `V-273623`

### Rule: The RUCKUS ICX router must be configured to use keys with a duration not exceeding 180 days for authenticating routing protocol messages.

**Rule ID:** `SV-273623r1110932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the keys used for routing protocol authentication are guessed, the malicious user could create havoc within the network by advertising incorrect routes and redirecting traffic. Some routing protocols allow the use of key chains for authentication. A key chain is a set of keys used in succession, with each having a lifetime of no more than 180 days. Changing the keys frequently reduces the risk of them eventually being guessed. Keys cannot be used during time periods for which they are not activated. If a time period occurs during which no key is activated, neighbor authentication cannot occur, and therefore routing updates will fail. Therefore, ensure that for a given key chain, key activation times overlap to avoid any period of time during which no key is activated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the start times for each key within the configured key chains used for routing protocol authentication as shown in the example below: keychain OSPF_KEY_CHAIN key-id 1 password xxxxxxx send-lifetime start 03-05-24 00:00:00 end 09-01-24 00:00:00 accept-lifetime start 03-05-24 00:00:00 end 09-01-24 00:00:00 interface ethernet 1/1/1 ip ospf area 0 ip ospf authentication keychain OSPF_KEY_CHAIN Note: Keychains must be configured to authenticate routing protocol messages as it is the only way to set an expiration. If any key has a lifetime of more than 180 days, this is a finding.

## Group: SRG-NET-000343-RTR-000002

**Group ID:** `V-273626`

### Rule: The RUCKUS Multicast Source Discovery Protocol (MSDP) router must be configured to authenticate all received MSDP packets.

**Rule ID:** `SV-273626r1110933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network routers presents additional risks to the core, whether from a rogue or misconfigured MSDP-enabled router. MSDP password authentication is used to validate each segment sent on the TCP connection between MSDP peers, protecting the MSDP session against the threat of spoofed packets being injected into the TCP connection stream.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the running configuration to determine whether MSDP peers are configured for authentication. ICX(config-msdp-router)# msdp-peer x.x.x.x connect-source loopback 1 ICX(config-msdp-router)# msdp-peer x.x.x.x connect-source loopback 1 ao chain1 If MSDP peers are not configured for authentication, this is a finding.

## Group: SRG-NET-000362-RTR-000109

**Group ID:** `V-273627`

### Rule: The RUCKUS ICX Router must not be configured to have any zero-touch deployment feature enabled when connected to an operational network.

**Rule ID:** `SV-273627r1110934_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices configured via a zero-touch deployment or auto-loading feature can have their startup configuration or image pushed to the device for installation via TFTP or Remote Copy (rcp). Loading an image or configuration file from the network is taking a security risk because the file could be intercepted by an attacker who could corrupt the file, resulting in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the startup config ("show conf") and examine whether any interfaces are configured with the keyword "dynamic". If the startup config does not exist, this is a finding.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-273628`

### Rule: The RUCKUS ICX router must be configured to protect against or limit the effects of denial-of-service (DoS) attacks by employing control plane protection.

**Rule ID:** `SV-273628r1111067_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Route Processor (RP) is critical to all network operations because it is the component used to build all forwarding paths for the data plane via control plane processes. It is also instrumental with ongoing network management functions that keep the routers and links available for providing network services. Any disruption to the RP or the control and management planes can result in mission-critical network outages. A DoS attack targeting the RP can result in excessive CPU and memory utilization. To maintain network stability and RP security, the router must be able to handle specific control plane and management plane traffic destined to the RP. In the past, one method of filtering was to use ingress filters on forwarding interfaces to filter both forwarding path and receiving path traffic. However, this method does not scale well as the number of interfaces grows and the size of the ingress filters grows. Control plane policing increases the security of routers and multilayer switches by protecting the RP from unnecessary or malicious traffic. Filtering and rate limiting the traffic flow of control plane packets can be implemented to protect routers against reconnaissance and DoS attacks, allowing the control plane to maintain packet forwarding and protocol states despite an attack or heavy load on the router or multilayer switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to determine whether distributed denial-of-service (DDoS) attack prevention is configured (values may vary): ICX#show running-config | include burst ip icmp attack-rate burst-normal 500 burst-max 1000 lockup 300 ip tcp burst-normal 30 burst-max 100 lockup 300 If DDoS protection is not configured, this is a finding.

## Group: SRG-NET-000362-RTR-000111

**Group ID:** `V-273629`

### Rule: The RUCKUS ICX router must be configured to have Gratuitous Address Resolution Protocol (ARP) disabled on all external interfaces.

**Rule ID:** `SV-273629r1111036_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A gratuitous ARP is an ARP broadcast in which the source and destination MAC addresses are the same. It is used to inform the network about a host IP address. A spoofed gratuitous ARP message can cause network mapping information to be stored incorrectly, causing network malfunction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RUCKUS ICX disables gratuitous ARP by default. Review the configuration to verify the command below does not appear. ip arp learn-gratuitous-arp If the above command is present in the configuration, this is a finding.

## Group: SRG-NET-000362-RTR-000112

**Group ID:** `V-273630`

### Rule: The RUCKUS ICX router must be configured to have IP directed broadcast disabled on all interfaces.

**Rule ID:** `SV-273630r1110896_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An IP directed broadcast is a datagram sent to the broadcast address of a subnet that is not directly attached to the sending machine. The directed broadcast is routed through the network as a unicast packet until it arrives at the target subnet, where it is converted into a link-layer broadcast. Because of the nature of the IP addressing architecture, only the last router in the chain, which is connected directly to the target subnet, can conclusively identify a directed broadcast. IP directed broadcasts are used in the extremely common and popular smurf, or denial-of-service (DoS), attacks. In a smurf attack, the attacker sends Internet Control Message Protocol (ICMP) echo requests from a falsified source address to a directed broadcast address, causing all the hosts on the target subnet to send replies to the falsified source. By sending a continuous stream of such requests, the attacker can create a much larger stream of replies, which can completely inundate the host whose address is being falsified. This service should be disabled on all interfaces when not needed to prevent smurf and DoS attacks. Directed broadcast can be enabled on internal facing interfaces to support services such as Wake-On-LAN. Case scenario may also include support for legacy applications where the content server and the clients do not support multicast. The content servers send streaming data using UDP broadcast. Used in conjunction with the IP multicast helper-map feature, broadcast data can be sent across a multicast topology. The broadcast streams are converted to multicast and vice versa at the first-hop routers and last-hop routers before entering and leaving the multicast transit area respectively. The last-hop router must convert the multicast to broadcast. Hence, this interface must be configured to forward a broadcast packet (i.e., a directed broadcast address is converted to the all nodes broadcast address).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it is compliant with this requirement. IP directed broadcast command is disabled by default. The following is an example of the feature being enabled: interface ethernet 1/1/1 ip address x.x.x.x 255.255.255.0 ip directed-broadcast If IP directed broadcast is enabled on any interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000113

**Group ID:** `V-273631`

### Rule: The RUCKUS ICX router must be configured to have Internet Control Message Protocol (ICMP) unreachable notifications disabled on all external interfaces.

**Rule ID:** `SV-273631r1110937_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Host unreachable ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if controls have been defined to ensure the router does not send ICMP unreachable notifications out to any external interfaces. show run verify "no ip icmp unreachable" is present If ICMP unreachable notifications are enabled on any external interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-273632`

### Rule: The RUCKUS ICX router must be configured to have Internet Control Message Protocol (ICMP) mask replies disabled on all external interfaces.

**Rule ID:** `SV-273632r1110938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to determine whether outgoing ICMP mask replies are blocked on external interfaces. enable egress-acl-on-cpu-traffic ip access-list extended BLOCK_ICMP_OUT sequence 10 deny icmp any any unreachable sequence 20 deny icmp any any mask-reply sequence 30 permit ip any any interface ethernet 1/1/1 ip address x.0.1.2 255.255.255.252 ip access-group BLOCK_ICMP_OUT out ! If outgoing ICMP mask replies are not blocked on external interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000115

**Group ID:** `V-273633`

### Rule: The RUCKUS ICX router must be configured to have Internet Control Message Protocol (ICMP) redirects disabled on all external interfaces.

**Rule ID:** `SV-273633r1110939_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Redirect ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The RUCKUS ICX router disables ICMP redirect messages by default. Review the configuration to verify the following command is not present: ip icmp redirects If the command above is present, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-273634`

### Rule: The RUCKUS ICX BGP router must be configured to use the maximum prefixes feature to protect against route table flooding and prefix de-aggregation attacks.

**Rule ID:** `SV-273634r1110940_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. In 1997, misconfigured routers in the Florida Internet Exchange network (AS7007) de-aggregated every prefix in their routing table and started advertising the first /24 block of each of these prefixes as their own. Faced with this additional burden, the internal routers became overloaded and crashed repeatedly. This caused prefixes advertised by these routers to disappear from routing tables and reappear when the routers came back online. As the routers came back after crashing, they were flooded with the routing table information by their neighbors. The flood of information would again overwhelm the routers and cause them to crash. This process of route flapping served to destabilize not only the surrounding network but also the entire Internet. Routers trying to reach those addresses would choose the smaller, more specific /24 blocks first. This caused backbone networks throughout North America and Europe to crash. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the de-aggregation risk. BGP maximum prefix must be used on all eBGP routers to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering AS. Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that the number of received prefixes from each eBGP neighbor is controlled. router bgp neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 maximum-prefix nnnnnnn neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 maximum-prefix nnnnnnn If the router is not configured to control the number of prefixes received from each peer to protect against route table flooding and prefix de-aggregation attacks, this is a finding.

## Group: SRG-NET-000362-RTR-000118

**Group ID:** `V-273635`

### Rule: The RUCKUS ICX BGP router must be configured to limit the prefix size on any inbound route advertisement to /24 or the least significant prefixes issued to the customer.

**Rule ID:** `SV-273635r1110897_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if it is compliant with this requirement. 1. Verify a route filter has been configured to reject prefixes longer than /24, or the least significant prefixes issued to the customers as shown in the example below: ip prefix-list FILTER_PREFIX_LENGTH seq 5 permit 0.0.0.0/0 ge 8 le 24 ip prefix-list FILTER_PREFIX_LENGTH seq 10 deny 0.0.0.0/0 le 32 2. Verify prefix filtering has been applied to each eBGP peer as shown in the following example: router bgp neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 prefix-list FILTER_PREFIX_LENGTH in If the router is not configured to limit the prefix size on any inbound route advertisement to /24, or the least significant prefixes issued to the customer, this is a finding.

## Group: SRG-NET-000362-RTR-000120

**Group ID:** `V-273637`

### Rule: The RUCKUS ICX multicast Rendezvous Pointerface (RP) Router must be configured to limit the multicast forwarding cache so that its resources are not saturated by managing an overwhelming number of Protocol Independent Multicast (PIM) and Multicast Source Discovery Protocol (MSDP) source-active entries.

**Rule ID:** `SV-273637r1110898_rule`
**Severity:** low

**Description:**
<VulnDiscussion>MSDP peering between networks enables sharing of multicast source information. Enclaves with an existing multicast topology using PIM-SM can configure their RP routers to peer with MSDP routers. As a first step of defense against a denial-of-service (DoS) attack, all RP routers must limit the multicast forwarding cache to ensure that router resources are not saturated managing an overwhelming number of PIM and MSDP source-active entries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the "show default value" output for the msdp-sa-cache value. If that number is zero, this is a finding.

## Group: SRG-NET-000362-RTR-000121

**Group ID:** `V-273638`

### Rule: The RUCKUS ICX multicast Rendezvous Pointerface (RP) must be configured to rate limit the number of Protocol Independent Multicast (PIM) Register messages.

**Rule ID:** `SV-273638r1110941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a new source starts transmitting in a PIM Sparse Mode network, the DR will encapsulate the multicast packets into register messages and forward them to the RP using unicast. This process can be taxing on the CPU for both the DR and the RP if the source is running at a high data rate and there are many new sources starting at the same time. This scenario can potentially occur immediately after a network failover. The rate limit for the number of register messages must be set to a relatively low value based on the known number of multicast sources within the multicast domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the RP to verify that it is rate limiting the number of PIM register messages. router pim rp-address x.0.1.1 register-rate-limit nn If the RP is not limiting PIM register messages, this is a finding.

## Group: SRG-NET-000362-RTR-000122

**Group ID:** `V-273639`

### Rule: The RUCKUS ICX Router must be configured to limit the number of mroute states resulting from Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Host Membership Reports.

**Rule ID:** `SV-273639r1110942_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The current multicast paradigm can let any host join any multicast group at any time by sending an IGMP or MLD membership report to the DR. In a Protocol Independent Multicast (PIM) Sparse Mode network, the DR will send a PIM Join message for the group to the RP. Without any form of admission control, this can pose a security risk to the entire multicast domain - specifically the multicast routers along the shared tree from the DR to the RP that must maintain the mroute state information for each group join request. Hence, it is imperative that the DR is configured to limit the number of mroute state information that must be maintained to mitigate the risk of IGMP or MLD flooding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the "show default value" output for the pim-hw-cache and pim6-hw-cache values. If either number is zero, this is a finding.

## Group: SRG-NET-000362-RTR-000123

**Group ID:** `V-273640`

### Rule: The RUCKUS ICX multicast Designated Router (DR) must be configured to increase the shortest-path tree (SPT) threshold or set it to infinity to minimalize source-group (S, G) state within the multicast topology where Any Source Multicast (ASM) is deployed.

**Rule ID:** `SV-273640r1110943_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASM can have many sources for the same groups (many-to-many). For many receivers, the path via the RP may not be ideal compared with the shortest path from the source to the receiver. By default, the last-hop router will initiate a switch from the shared tree to a source-specific SPT to obtain lower latencies. This is accomplished by the last-hop router sending an (S, G) Protocol Independent Multicast (PIM) Join toward S (the source). When the last-hop router begins to receive traffic for the group from the source via the SPT, it will send a PIM Prune message to the RP for the (S, G). The RP will then send a Prune message toward the source. The SPT switchover becomes a scaling issue for large multicast topologies that have many receivers and many sources for many groups because (S, G) entries require more memory than (*, G). Hence, it is imperative to minimize the amount of (S, G) state to be maintained by increasing the threshold that determines when the SPT switchover occurs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DR PIM configuration to verify that the SPT switchover threshold is increased (default is "1") or set to the maximum value. router pim rp-address 10.2.2.2 spt-threshold 4294967295 If the DR is not configured to increase the SPT threshold to minimalize (S, G) state, this is a finding.

## Group: SRG-NET-000362-RTR-000124

**Group ID:** `V-273641`

### Rule: The RUCKUS ICX BGP router must be configured to enable the Generalized TTL Security Mechanism (GTSM).

**Rule ID:** `SV-273641r1111068_rule`
**Severity:** low

**Description:**
<VulnDiscussion>GTSM is designed to protect a router's IP-based control plane from denial-of-service (DoS) attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all Exterior Border Gateway Protocol speaking routers. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent routers; that is, the Exterior Border Gateway Protocol peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP configuration to verify that TTL security has been configured for each external neighbor as shown in the example below: router bgp neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 ebgp-btsh If the router is not configured to use TTL security hack protection for all Exterior Border Gateway Protocol peering sessions, this is a finding.

## Group: SRG-NET-000364-RTR-000109

**Group ID:** `V-273642`

### Rule: The RUCKUS ICX perimeter router must be configured to only allow incoming communications from authorized sources to be routed to authorized destinations.

**Rule ID:** `SV-273642r1110944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic can be restricted directly by an access control list (ACL), which is a firewall function, or by Policy Routing. Policy Routing is a technique used to make routing decisions based on a number of different criteria other than just the destination network, including source or destination network, source or destination address, source or destination port, protocol, packet size, and packet classification. This overrides the router's normal routing procedures used to control the specific paths of network traffic. It is normally used for traffic engineering but can also be used to meet security requirements; for example, traffic that is not allowed can be routed to the Null0 or discard interface. Policy Routing can also be used to control which prefixes appear in the routing table. This requirement is intended to allow network administrators the flexibility to use whatever technique is most effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if the router allows only incoming communications from authorized sources to be routed to authorized destinations. The example below allows inbound NTP from server x.1.12.9 only to host x.12.1.21: ip access-list extended FILTER_PERIMETER sequence 10 permit tcp any any established sequence 20 permit udp host x.12.1.9 host x.12.1.21 eq ntp ... sequence 30 deny ip any any log ! interface ethernet x/x/x ip access-group FILTER_PERIMETER in logging enable If the router does not restrict incoming communications to allow only authorized sources and destinations, this is a finding.

## Group: SRG-NET-000364-RTR-000110

**Group ID:** `V-273643`

### Rule: The RUCKUS ICX perimeter router must be configured to block inbound packets with source Bogon IP address prefixes.

**Rule ID:** `SV-273643r1111037_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bogons include IP packets on the public internet that contain addresses that are not in any range allocated or delegated by the Internet Assigned Numbers Authority (IANA) or a delegated regional internet registry (RIR) and allowed for public Internet use. Bogons also include multicast, IETF reserved, and special purpose address space as defined in RFC 6890. Security of the internet's routing system relies on the ability to authenticate an assertion of unique control of an address block. Measures to authenticate such assertions rely on the validation the address block forms as part of an existing allocated address block and must be a trustable and unique reference in the IANA address registries. The intended use of a Bogon address would only be for the purpose of address spoofing in denial-of-service attacks. Hence, it is imperative that IP packets with a source Bogon address are blocked at the network's perimeter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that an ingress Access Control List (ACL) applied to all external interfaces is blocking packets with Bogon source addresses. 1. Verify an ACL has been configured containing the current Bogon prefixes as shown in the example below: ip access-list extended FILTER_PERIMETER sequence 10 deny ip 0.0.0.0 0.255.255.255 any log sequence 20 deny ip 10.0.0.0 0.255.255.255 any log sequence 30 deny ip 100.64.0.0 0.63.255.255 any log sequence 40 deny ip 127.0.0.0 0.255.255.255 any log sequence 50 deny ip 169.254.0.0 0.0.255.255 any log sequence 60 deny ip 172.16.0.0 0.15.255.255 any log sequence 70 deny ip 192.0.0.0 0.0.0.255 any log sequence 80 deny ip 192.0.2.0 0.0.0.255 any log sequence 90 deny ip 192.168.0.0 0.0.255.255 any log sequence 100 deny ip 192.18.0.0 0.1.255.255 any log sequence 110 deny ip 192.51.100.0 0.0.0.255 any log sequence 120 deny ip 203.0.113.0 0.0.0.255 any log sequence 130 deny ip 224.0.0.0 31.255.255.255 any log sequence 140 permit tcp any any established sequence 150 permit tcp host x.0.1.2 host x.0.1.1 eq bgp sequence 160 permit tcp host x.0.1.1 eq bgp host x.0.1.2 sequence 170 permit icmp host x.0.1.2 host x.0.1.1 echo sequence 180 permit icmp host x.0.1.1 host x.0.1.2 echo-reply ... sequence 190 deny ip any any log 2. Verify the inbound ACL applied to all external interfaces will block all traffic from Bogon source addresses. interface ethernet 1/1/1 port-name link_to_DISN ip access-group FILTER_PERIMETER in logging enable ! If the router is not configured to block inbound packets with source Bogon IP address prefixes, this is a finding.

## Group: SRG-NET-000364-RTR-000111

**Group ID:** `V-273644`

### Rule: The RUCKUS ICX perimeter router must be configured to have Link Layer Discovery Protocols (LLDPs) disabled on all external interfaces.

**Rule ID:** `SV-273644r1110900_rule`
**Severity:** low

**Description:**
<VulnDiscussion>LLDPs are primarily used to obtain protocol addresses of neighboring devices and discover platform capabilities of those devices. Use of SNMP with the LLDP Management Information Base (MIB) allows network management applications to learn the device type and the SNMP agent address of neighboring devices, thereby enabling the application to send SNMP queries to those devices. LLDPs are also media- and protocol-independent as they run over the data link layer; therefore, two systems that support different network-layer protocols can still learn about each other. Allowing LLDP messages to reach external network nodes is dangerous as it provides an attacker a method to obtain information of the network infrastructure that can be useful to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the global configuration to verify that LLDP has been disabled on external interfaces. (LLDP is enabled on all interfaces by default.) show running-config | include lldp no lldp enable ports ethernet 1/1/1 If LLDP is enabled on perimeter router external interfaces, this is a finding.

## Group: SRG-NET-000364-RTR-000112

**Group ID:** `V-273645`

### Rule: The RUCKUS ICX perimeter router must be configured to have Proxy ARP disabled on all external interfaces.

**Rule ID:** `SV-273645r1110946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Proxy ARP is enabled on a Cisco router, it allows that router to extend the network (at layer 2) across multiple interfaces (LAN segments). Because proxy ARP allows hosts from different LAN segments to look like they are on the same segment, proxy ARP is only safe when used between trusted LAN segments. Attackers can leverage the trusting nature of proxy ARP by spoofing a trusted host and then intercepting packets. Proxy ARP should always be disabled on router interfaces that do not require it, unless the router is being used as a LAN bridge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if IP Proxy ARP has been enabled (see below): ip proxy-arp Note: By default, Proxy ARP is disabled globally. If IP Proxy ARP is enabled, this is a finding.

## Group: SRG-NET-000364-RTR-000113

**Group ID:** `V-273646`

### Rule: The RUCKUS ICX perimeter router must be configured to block all outbound management traffic.

**Rule ID:** `SV-273646r1111039_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For in-band management, the management network must have its own subnet to enforce control and access boundaries provided by layer 3 network nodes, such as routers and firewalls. Management traffic between the managed network elements and the management network is routed via the same links and nodes as that used for production or operational traffic. Safeguards must be implemented to ensure the management traffic does not leak past the perimeter of the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. The perimeter router of the managed network must be configured with an access control list (ACL) or filter on the egress interface to block all management traffic. Verify all external interfaces have been configured with an outbound ACL as shown in the example below: EXTERNAL_ACL_OUTBOUND: 5 entries 10: deny tcp any any eq radius 20: deny tcp any any eq sshow log 30: deny tcp any any eq snmp log 40: deny udp any any eq syslog log 50: deny ip any any log interface ethernet x/x/x ip access-group EXTERNAL_ACL_OUTBOUND out logging enable If management traffic is not blocked at the perimeter, this is a finding.

## Group: SRG-NET-000364-RTR-000114

**Group ID:** `V-273647`

### Rule: The RUCKUS ICX multicast Designated Router (DR) must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join only multicast groups that have been approved by the organization.

**Rule ID:** `SV-273647r1111041_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify it is filtering IGMP or MLD report messages, allowing hosts to only join multicast groups from sources that have been approved. Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. This requirement is not applicable to Any Source Multicast (ASM) since the filtering is being performed by the Rendezvous Pointerface router. 1. Verify all host facing interfaces are configured to filter IGMP Membership Report messages (IGMP joins) as shown in the example below: ICX(conf)#interface ethernet 1/2/1 ICX(config-if-e10000-1/2/1)#ip igmp ver 3 ICX(config-if-e10000-1/2/1)#ip igmp access-group IGMP_JOIN_FILTER ICX(config-ig-e1000-1/2/1)#show access-list all 2. Verify the output below (the access control list, or ACL) denies unauthorized groups or permits only authorized groups. The example below denies all groups from the 239.0.0.0/16 range. Standard IP access list IGMP_JOIN_FILTER: 2 entries 10: deny 239.0.0.0 0.0.255.255 20: permit any If the DR is not filtering IGMP or MLD report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000115

**Group ID:** `V-273648`

### Rule: The RUCKUS ICX multicast Designated Router (DR) must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join a multicast group only from sources that have been approved by the organization.

**Rule ID:** `SV-273648r1111070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify it is filtering IGMP or MLD report messages, allowing hosts to only join multicast groups from sources that have been approved. Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. 1. Review the configuration for an ACL that denies unauthorized groups or permits only authorized sources. The example below denies all groups from the 239.8.0.0/16 range and permit from 0.0.0.0/8: ip access-list extended IGMP_JOIN_FILTER sequence 10 deny ip any 239.8.0.0 0.0.255.255 sequence 20 permit ip 0.0.0.0 0.255.255.255 any 2. Verify all host facing interfaces are configured to filter IGMP Membership Report messages (IGMP joins) as shown in the example below: interface ethernet x/x/x ip address x.0.1.2 255.255.255.252 ip pim-sparse ip igmp version 3 ip igmp access-group IGMP_JOIN_FILTER If the DR is not filtering IGMP or MLD report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000200

**Group ID:** `V-273650`

### Rule: The RUCKUS ICX perimeter router must be configured to drop IPv6 undetermined transport packets.

**Rule ID:** `SV-273650r1110949_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One of the fragmentation weaknesses known in IPv6 is the undetermined transport packet. This packet contains an undetermined protocol due to fragmentation. Depending on the length of the IPv6 extension header chain, the initial fragment may not contain the layer four port information of the packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review configuration for the command below: ipv6 deny-undetermined-transport any any If the router is not configured to drop IPv6 undetermined transport packets, this is a finding.

## Group: SRG-NET-000364-RTR-000201

**Group ID:** `V-273651`

### Rule: The RUCKUS ICX perimeter router must be configured drop IPv6 packets with a Routing Header type 0, 1, or 3-255.

**Rule ID:** `SV-273651r1111046_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The routing header can be used maliciously to send a packet through a path where less robust security is in place, rather than through the presumably preferred path of routing protocols. Use of the routing extension header has few legitimate uses other than as implemented by Mobile IPv6. The Type 0 Routing Header (RFC 5095) is dangerous because it allows attackers to spoof source addresses and obtain traffic in response, rather than the real owner of the address. Secondly, a packet with an allowed destination address could be sent through a Firewall using the Routing Header functionality, only to bounce to a different node once inside. The Type 1 Routing Header is defined by a specification called "Nimrod Routing," a discontinued project funded by Defense Advanced Research Projects Activity (DARPA). Assuming that most implementations will not recognize the Type 1 Routing Header, it must be dropped. The Type 3-255 Routing Header values in the routing type field are currently undefined and must be dropped inbound and outbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration for the command below (which drops all routing-types except 2): Ipv6 drop routing-type If the perimeter router is not configured to drop all routing header types other than 2, this is a finding.

## Group: SRG-NET-000364-RTR-000202

**Group ID:** `V-273652`

### Rule: The RUCKUS ICX perimeter router must be configured to drop IPv6 packets containing a hop-by-hop and destination options header with invalid or undefined option type values.

**Rule ID:** `SV-273652r1111072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These options are intended for the destination options header only. The optional and extensible natures of the IPv6 extension headers require higher scrutiny because many implementations do not always drop packets with headers that cannot be recognized. This could cause a denial of service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. Satisfies: SRG-NET-000364-RTR-000202, SRG-NET-000364-RTR-000203, SRG-NET-000364-RTR-000204, SRG-NET-000364-RTR-000205, SRG-NET-000364-RTR-000206</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the perimeter router configuration to determine whether an ACL is configured to drop IPv6 packets containing hop-by-hop or destination options extension headers. 1. Review the perimeter router configuration to determine whether an ACL is configured to drop IPv6 packets containing hop-by-hop or destination options extension headers. ipv6 access-list BLOCK_OPTIONS sequence 10 deny 0 any any log sequence 20 deny 60 any any log sequence 30 permit ipv6 any any ! 2. Verify the ACL has been applied to external interfaces. interface ethernet x/x/x ipv6 address x::x/x ipv6 access-group BLOCK_OPTIONS in logging enable If the perimeter router is not configured to drop IPv6 packets with hop-by-hop or destination options extension headers, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-273654`

### Rule: The RUCKUS ICX BGP Router must be configured to use its loopback address as the source address for internal border gateway protocol (iBGP) peering sessions.

**Rule ID:** `SV-273654r1111048_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the BGP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router's loopback address instead of the numerous physical interface addresses. When the loopback address is used as the source for eBGP peering, the BGP session will be harder to hijack because the source address to be used is not known globally. This makes it more difficult for a hacker to spoof an eBGP neighbor. By using traceroute, a hacker can easily determine the addresses for an eBGP speaker when the IP address of an external interface is used as the source address. The routers within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to verify BGP configuration uses the loopback address as the source address for iBGP peering sessions. interface loopback 1 ip address x.x.1.1 255.255.255.255 ! router bgp local-as 10 neighbor x.x.x.x remote-as 10 neighbor x.x.x.x update-source loopback 1 If the router is not using a loopback address as the source for iBGP peering sessions, this is a finding.

## Group: SRG-NET-000512-RTR-000007

**Group ID:** `V-273660`

### Rule: The RUCKUS ICX Router must be configured to have each VRF with the appropriate Route Distinguisher (RD).

**Rule ID:** `SV-273660r1110952_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An RD provides uniqueness to the customer address spaces within the MPLS L3VPN infrastructure. The concept of the VPN-IPv4 and VPN-IPv6 address families consists of the RD prepended before the IP address. Hence, if the same IP prefix is used in several different L3VPNs, it is possible for BGP to carry several completely different routes for that prefix, one for each VPN. Since VPN-IPv4 addresses and IPv4 addresses are different address families, BGP never treats them as comparable addresses. The purpose of the RD is to create distinct routes for common IPv4 address prefixes. On any given PE router, a single RD can define a VRF in which the entire address space may be used independently, regardless of the makeup of other VPN address spaces. Hence, it is imperative that a unique RD is assigned to each L3VPN and that the proper RD is configured for each VRF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View VRF configuration to determine whether each RD has been configured correctly. If VRFs are configured with incorrect RDs, this is a finding.

## Group: SRG-NET-000512-RTR-000011

**Group ID:** `V-273664`

### Rule: The RUCKUS ICX Multicast Source Discovery Protocol (MSDP) Router must be configured to use its loopback address when originating MSDP traffic.

**Rule ID:** `SV-273664r1110903_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of MSDP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router's loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to verify that MSDP uses a loopback address as its source. interface loopback 1 ip address x.x.x.x 255.255.255.255 ! router msdp msdp-peer x.x.x.x connect-source loopback 1 ! If the MSDP router does not use its loopback address as the source address for MSDP traffic, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-273665`

### Rule: The RUCKUS ICX Router must be configured to advertise a hop limit of at least 32 in Router Advertisement messages for IPv6 stateless autoconfiguration deployments.

**Rule ID:** `SV-273665r1110904_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if the hop limit has been configured for Router Advertisement messages (default value = 64). Ipv6 hop-limit xx If it has been configured and has not been set to at least "32", it is a finding.

## Group: SRG-NET-000512-RTR-000013

**Group ID:** `V-273666`

### Rule: The RUCKUS ICX Router must not be configured to use IPv6 Site Local Unicast addresses.

**Rule ID:** `SV-273666r1110953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As currently defined, site local addresses are ambiguous and can be present in multiple sites. The address itself does not contain any indication of the site to which it belongs. The use of site-local addresses has the potential to adversely affect network security through leaks, ambiguity, and potential misrouting as documented in section 2 of RFC3879. RFC3879 formally deprecates the IPv6 site-local unicast prefix FEC0::/10 as defined in RFC3513.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to verify site local unicast addresses (FEC0::/10) have not been defined. If site local unicast addresses are defined, this is a finding.

## Group: SRG-NET-000512-RTR-000014

**Group ID:** `V-273667`

### Rule: The RUCKUS ICX Router must be configured to suppress Router Advertisements on all external IPv6-enabled interfaces. 

**Rule ID:** `SV-273667r1111050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many of the known attacks in stateless autoconfiguration are defined in RFC 3756 were present in IPv4 ARP attacks. To mitigate these vulnerabilities, links that have no hosts connected such as the interface connecting to external gateways must be configured to suppress router advertisements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review configuration of external IPv6 interfaces for the command below: interface ethernet x/x/x ipv6 nd suppress-ra If the perimeter router is not configured to suppress router advertisements on all external interfaces, this is a finding.

## Group: SRG-NET-000705-RTR-000110

**Group ID:** `V-273669`

### Rule: The RUCKUS ICX router must employ organization-defined controls by type of denial of service (DoS) to achieve the DoS objective.

**Rule ID:** `SV-273669r1111074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS events may occur due to a variety of internal and external causes, such as an attack by an adversary or a lack of planning to support organizational needs with respect to capacity and bandwidth. Such attacks can occur across a wide range of network protocols (e.g., IPv4, IPv6). A variety of technologies are available to limit or eliminate the origination and effects of DoS events. For example, boundary protection devices can filter certain types of packets to protect system components on internal networks from being directly affected by or the source of DoS attacks. Employing increased network capacity and bandwidth combined with service redundancy also reduces the susceptibility to DoS events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to determine whether distributed denial-of-service (DDoS) attack prevention is configured (values may vary): ICX#show running-config | include burst ip icmp attack-rate burst-normal 500 burst-max 1000 lockup 300 ip tcp burst-normal 30 burst-max 100 lockup 300 If DSCP trust is required, verify it has been applied to the necessary interfaces. ICX# show running-config interface ethernet x/x/x interface ethernet x/x/x trust dscp If DDoS protection is not configured or Differentiated Services Code Point (DSCP) trust is required but not configured, this is a finding.

## Group: SRG-NET-000715-RTR-000120

**Group ID:** `V-273670`

### Rule: The RUCKUS ICX router must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

**Rule ID:** `SV-273670r1110956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command and control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the router is configured to implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions. If the router is not configured to implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions, this is a finding.

## Group: SRG-NET-000760-RTR-000160

**Group ID:** `V-273671`

### Rule: The RUCKUS ICX router must establish organization-defined alternate communications paths for system operations organizational command and control.

**Rule ID:** `SV-273671r1110957_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An incident, whether adversarial- or nonadversarial-based, can disrupt established communications paths used for system operations and organizational command and control. Alternate communications paths reduce the risk of all communications paths being affected by the same incident. To compound the problem, the inability of organizational officials to obtain timely information about disruptions or to provide timely direction to operational elements after a communications path incident, can impact the ability of the organization to respond to such incidents in a timely manner. Establishing alternate communications paths for command and control purposes, including designating alternative decision makers if primary decision makers are unavailable and establishing the extent and limitations of their actions, can greatly facilitate the organization's ability to continue to operate and take appropriate actions during an incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the router is configured to establish organization-defined alternate communications paths for system operations organizational command and control. If the router is not configured to establish organization-defined alternate communications paths for system operations organizational command and control, this is a finding.

