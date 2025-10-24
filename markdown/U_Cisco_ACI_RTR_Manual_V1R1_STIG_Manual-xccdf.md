# STIG Benchmark: Cisco ACI Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-RTR-000001

**Group ID:** `V-272061`

### Rule: The Cisco ACI must be configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies.

**Rule ID:** `SV-272061r1115721_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, and devices) within information systems. In Cisco ACI, the administrator uses "contracts" to define security policies that control traffic between different endpoint groups (EPGs), essentially acting as a more granular and flexible ACL mechanism by specifying source and destination addresses, ports, and protocols based on the desired network segmentation needs. Add multiple filter rules to create a comprehensive set of allowed traffic patterns.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that ACLs are configured to allow or deny traffic for specific source and destination addresses as well as ports and protocols. For example, the configuration below will allow web traffic (HTTP) from the "WebServer" EPG to the "Database" EPG. tenant TENANT1 context Application filter WEB_TRAFFIC_FILTER filter ip permit source <web_server_ip_range> destination <database_ip_range> protocol tcp port 80 contract WEBACCESS filter WEB_TRAFFIC_FILTER epg WebServer contract WEBACCESS epg Database contract WEBACCESS If the switch is not configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies, this is a finding.

## Group: SRG-NET-000018-RTR-000003

**Group ID:** `V-272062`

### Rule: The BGP Cisco ACI must be configured to reject inbound route advertisements for any prefixes belonging to the local autonomous system (AS).

**Rule ID:** `SV-272062r1115716_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements belonging to the local AS can result in traffic looping or being black holed, or at a minimum using a nonoptimized path. For Cisco APIC, the default setting to prevent route loops from occurring. Sites must use different AS numbers. If this occurs, routing updates from one site is dropped when the other site receives them by default. To prevent such a situation from occurring, sites must not enable the "BGP Autonomous System override" feature to override the default setting. They must also not enable the "Disable Peer AS Check".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify it will reject routes belonging to the local AS. 1. Verify a prefix list has been configured containing prefixes belonging to the local AS. route-map LOCAL_AS_FILTER permit 10 match ip address prefix <local-AS-prefix> set community no-advertise 2. Review the route-map to the inbound BGP policy. bgp neighbor <peer-IP> address-family ipv4 unicast inbound route-map LOCAL_AS_FILTER If the switch is not configured to reject inbound route advertisements belonging to the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000005

**Group ID:** `V-272063`

### Rule: The BGP Cisco ACI must be configured to reject outbound route advertisements for any prefixes that do not belong to any customers or the local autonomous system (AS).

**Rule ID:** `SV-272063r1115719_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Advertisement of routes by an autonomous system for networks that do not belong to any of its customers pulls traffic away from the authorized network. This causes a denial of service (DoS) on the network that allocated the block of addresses and may cause a DoS on the network that is inadvertently advertising it as the originator. It is also possible that a misconfigured or compromised router within the GIG IP core could redistribute IGP routes into BGP, thereby leaking internal routes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ACI configuration to verify it will reject routes belonging to the local AS. 1. Verify a prefix list has been configured containing prefixes belonging to the local AS. In the example below, x.13.1.0/24 is the global address space allocated to the local AS. ip prefix-list PREFIX_FILTER seq 74 deny x.13.1.0/24 le 32 2. Verify the prefix list has been applied to all external BGP peers as shown in the example below: router bgp <AS_number> neighbor <peer_IP> prefix-list LOCAL_AS_PREFIX_FILTER out If the ACI is not configured to reject inbound route advertisements belonging to the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000006

**Group ID:** `V-272064`

### Rule: The BGP Cisco ACI must be configured to reject route advertisements from BGP peers that do not list their autonomous system (AS) number as the first AS in the AS_PATH attribute.

**Rule ID:** `SV-272064r1113970_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure the IP core is not used as a transit network for unauthorized or possibly even internet traffic. All autonomous system boundary routers (ASBRs) must ensure updates received from eBGP peers list their AS number as the first AS in the AS_PATH attribute. Cisco ACI BGP usually enforces the "first-as" rule by default.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
By default, Cisco ACI enforces the first AS in the AS_PATH attribute for all route advertisements. Review the configuration to verify the default BGP configuration on the ACI fabric is does not explicitly state: no enforce first-as If the device is not configured to reject updates from peers that do not list their AS number as the first AS in the AS_PATH attribute, this is a finding.

## Group: SRG-NET-000018-RTR-000007

**Group ID:** `V-272065`

### Rule: The Multicast Source Discovery Protocol (MSDP) Cisco ACI must be configured to filter received source-active multicast advertisements for any undesirable multicast groups and sources.

**Rule ID:** `SV-272065r1115723_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The interoperability of BGP extensions for interdomain multicast routing and MSDP enables seamless connectivity of multicast domains between autonomous systems. MP-BGP advertises the unicast prefixes of the multicast sources used by Protocol Independent Multicast (PIM) routers to perform RPF checks and build multicast distribution trees. MSDP is a mechanism used to connect multiple PIM sparse-mode domains, allowing RPs from different domains to share information about active sources. MSDP helps ACI border leaf switches identify the location of multicast sources in external networks, allowing them to properly route multicast traffic to interested receivers within the ACI fabric. MSDP within a layer 3 context, allowing the ACI fabric to discover multicast sources located in other multicast domains when connecting to external networks through "L3Out" connections, enabling efficient multicast traffic forwarding across different network segments.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is a DODIN or JRSS system, this is not applicable. Verify the ip route-map command with specific filter criteria under the relevant BGP neighbor configuration is configured to block any unwanted multicast prefixes from being advertised as shown in the example below: router bgp 100 neighbor 10.1.1.2 remote-as 200 address-family ipv4 unicast route-map BLOCK_MULTICAST permit If the ACI is not configured to reject outbound route advertisements that do not belong to any customers or the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000008

**Group ID:** `V-272066`

### Rule: The Cisco ACI Multicast Source Discovery Protocol (MSDP) must be configured to filter source-active (SA) multicast advertisements to external MSDP peers to avoid global visibility of local-only multicast sources and groups.

**Rule ID:** `SV-272066r1115725_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To avoid global visibility of local information, there are a number of source-group (S, G) states in a PIM-SM domain that must not be leaked to another domain, such as multicast sources with private address, administratively scoped multicast addresses, and the auto-RP groups (224.0.1.39 and 224.0.1.40). Allowing a multicast distribution tree, local to the core, to extend beyond its boundary could enable local multicast traffic to leak into other autonomous systems and customer networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ACI implementation does not use MSDP, this is not applicable. ip msdp sa-filter in <msdp_peer_address> list OUTBOUND_MSDP_SA_FILTER If the device is not configured with an export policy to filter local source-active multicast advertisements, this is a finding.

## Group: SRG-NET-000018-RTR-000009

**Group ID:** `V-272067`

### Rule: The Multicast Source Discovery Protocol (MSDP) Cisco ACI must be configured to limit the amount of source-active (SA) messages it accepts on per-peer basis.

**Rule ID:** `SV-272067r1113973_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To reduce any risk of a denial-of-service (DoS) attack from a rogue or misconfigured MSDP router, the router must be configured to limit the number of source-active messages it accepts from each peer. To limit the amount of SA messages a Cisco ACI switch accepts from each MSDP peer, configure the "ip msdp sa-limit" command on the switch, specifying the maximum number of SA messages allowed per peer; this essentially acts as a per-peer limit to prevent overwhelming the device with multicast source information from a single source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the ACI implementation does not use MSDP, this is not applicable. Review the switch configuration to determine if it is configured to limit the amount of source-active messages it accepts on a per-peer basis. show ip msdp If the ACI is not configured to limit the source-active messages it accepts, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-272068`

### Rule: The multicast Cisco ACI must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-272068r1114267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DOD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and thereby know which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the network's multicast topology diagram. 2. Review the switch configuration to verify only the PIM interfaces as shown in the multicast topology diagram are enabled for PIM as shown in the example below: Example: configure terminal interface Ethernet1/1 no ip pim If an interface is not required to support multicast routing and it is enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-272069`

### Rule: The multicast Cisco ACI must be configured to bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-272069r1114269_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PIM is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. PIM traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, unauthorized routers can join the PIM domain, discover and use the rendezvous points, and also advertise their rendezvous points into the domain. This can result in a denial of service (DoS) by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. Review the network's multicast topology diagram. 2. Review the switch configuration to verify only the PIM interfaces as shown in the multicast topology diagram are enabled for PIM as shown in the example below: Example: configure terminal interface Ethernet1/1 ip pim If a multicast interface is required to support PIM and it is not enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-272070`

### Rule: The multicast edge Cisco ACI must be configured to establish boundaries for administratively scoped multicast traffic.

**Rule ID:** `SV-272070r1113976_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations. Administratively scoped multicast addresses fall within the range of 239.0.0.0 to 239.255.255.255.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the multicast routing table and troubleshoot any issues with multicast traffic flow. show ip mroute If the ACI is not configured to establish boundaries for administratively scoped multicast traffic, this is a finding.

## Group: SRG-NET-000019-RTR-000011

**Group ID:** `V-272071`

### Rule: The out-of-band management (OOBM) gateway Cisco ACI must be configured to have separate OSPF instances for the managed network and management network.

**Rule ID:** `SV-272071r1114084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, implementation of several safeguards for containment of management and production traffic boundaries must occur. Since the managed and management network are separate routing domains, configuration of separate OSPF routing instances is critical on the router to segregate traffic from each network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this review is for the DODIN Backbone, mark as not applicable. Verify separate routing instances in the Cisco APIC as shown in the following example: interface GigabitEthernet 0/0 ip address 10.0.0.1 255.255.255.0 no shutdown ip route-map "mgmt-routes" permit router bgp 100 // Management network routing instance interface GigabitEthernet 0/1 ip address 192.168.1.1 255.255.255.0 no shutdown ip route-map "managed-routes" permit router bgp 200 // Managed network routing instance If separate routing instances are not configured for the managed and management networks, this is a finding.

## Group: SRG-NET-000019-RTR-000012

**Group ID:** `V-272072`

### Rule: The Cisco ACI out-of-band management (OOBM) must be configured to not redistribute routes between the management network routing domain and the managed network routing domain.

**Rule ID:** `SV-272072r1113978_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, several safeguards must be implemented for containment of management and production traffic boundaries; otherwise, it is possible management traffic will not be separated from production traffic. Since the managed network and the management network are separate routing domains, separate Interior Gateway Protocol routing instances must be configured on the router, one for the managed network and one for the OOBM network. In addition, the routes from the two domains must not be redistributed to each other. To configure out-of-band management access on a Cisco APIC using the API: 1. Navigate to Tenants >> mgmt. 2. Expand "Quick Start" and select Out-of-Band Management Access >> Configure Out-of-Band Management Access. 3. Here, define the nodes in the OOB network, their IP addresses, allowed subnets for external hosts, and communication filters to control access, essentially creating a dedicated network for managing the devices outside the primary production network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this review is for the DODIN Backbone, mark as not applicable. Verify redistribution is disabled on the OOB routing instance: router bgp 100 // Management network routing instance redistribute static route-map deny redistribute connected route-map deny redistribute connected route-map deny If redistribute is not disabled for the OOB instance, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-272073`

### Rule: The Cisco ACI multicast rendezvous point (RP) must be configured to filter Protocol Independent Multicast (PIM) Register messages received from the designated router (DR) for any undesirable multicast groups and sources.

**Rule ID:** `SV-272073r1114086_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that register messages are accepted only for authorized multicast groups and sources. By configuring route maps, the distribution of RP information that is distributed throughout the network can be controlled. Specify the BSRs or mapping agents to be listened to on each client router and the list of candidates to be advertised (listened to) on each BSR and mapping agent to ensure that what is advertised is what is expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the configuration to check for PIM compliance. APIC1(config)#show running-configuration pim Example: ip access-list extended PIM_REGISTER_FILTER deny ip any 232.0.0.0 0.255.255.255 permit ip host 10.1.2.6 any permit ip host 10.1.2.7 any deny ip any any ip pim accept-register list PIM_REGISTER_FILTER If the RP router peering with PIM-SM routers is not configured with a policy to block registration messages for any undesirable multicast groups and sources, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-272074`

### Rule: The multicast rendezvous point (RP) Cisco ACI must be configured to filter Protocol Independent Multicast (PIM) Join messages received from the designated router (DR) for any undesirable multicast groups.

**Rule ID:** `SV-272074r1114271_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that join messages are only accepted for authorized multicast groups. In a Cisco ACI fabric, the border leaf switches are responsible for handling external multicast traffic and are where access control lists (ACLs) to filter PIM Join messages would be applied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the configuration to verify PIM compliance. APIC1(config)#show running-configuration pim Example: ! ACL to deny specific multicast groups ip access-list extended PIM_JOIN_FILTER deny ip multicast group 224.0.0.1 deny ip multicast group 224.0.0.2 permit ip any any ! ACL to the L3Out interface on the border leaf switch interface L3Out_to_External ip access-group PIM_JOIN_FILTER in If the RP is not configured to filter join messages received from the DR for any undesirable multicast groups, this is a finding.

## Group: SRG-NET-000078-RTR-000001

**Group ID:** `V-272075`

### Rule: The Cisco ACI must be configured to log all packets that have been dropped.

**Rule ID:** `SV-272075r1114309_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being done or attempted to be done, and by whom, to compile an accurate risk assessment. Auditing the actions on network devices provides a means to recreate an attack or identify a configuration mistake on the device. To configure Cisco ACI to log all dropped packets, enable the "OpFlex Drop Log" feature, which allows logging of any packet dropped in the data path, essentially capturing all dropped packets due to policy mismatches or other reasons within the network fabric. This is done by setting the "log" directive within security policies when defining filter rules on contracts within the tenant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the APIC GUI to navigate to each tenant. Within each contract, review each rule with "Action" set to "Deny". Verify these rules have the "Directive" set to "Log". If packets being dropped at interfaces are not logged, this is a finding.

## Group: SRG-NET-000131-RTR-000083

**Group ID:** `V-272076`

### Rule: The Cisco ACI must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-272076r1113982_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Call Home feature is disabled: 1. Navigate to the "Admin" section in the GUI, then expand All >> Communication Management >> Call Home. 2. In the General tab, verify the Admin State is set to "Off". If the Call Home feature is configured to send messages to unauthorized individuals such as Cisco TAC, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-272077`

### Rule: The Cisco ACI must be configured to use encryption for routing protocol authentication.

**Rule ID:** `SV-272077r1114087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols. To configure a Cisco ACI to use encryption for routing protocol authentication, set up a "pre-shared key" (PSK) on the APIC, which will then be used to generate encryption keys for the routing protocol authentication process, essentially encrypting the authentication messages exchanged between switches within the fabric. This feature is typically referred to as "CloudSec Encryption" within the ACI platform.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify PSKs are configured: apic1(config-cloudsec)# show cloudsec summary If PSKs are not configured to use encryption for routing protocol authentication, this is a finding.

## Group: SRG-NET-000168-RTR-000078

**Group ID:** `V-272078`

### Rule: The Cisco ACI must be configured to authenticate all routing protocol messages using a NIST-validated FIPS 198-1 message authentication code algorithm.

**Rule ID:** `SV-272078r1114273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. Since MD5 is vulnerable to "birthday" attacks and may be compromised, routing protocol authentication must use FIPS 198-1 validated algorithms and modules to encrypt the authentication key. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If EIGRP, RIP, and IS-IS protocols are used (these protocols only support MD5 authentication), this is a finding. Review the switch configuration using the show bgp and show ospf commands to verify BGP and OSPF. The configuration should be similar to the example below: Key-Chain bgp_keys tcp Key 1 -- text 0 "070e234f" send-id 2 recv-id 2 cryptographic-algorithm hmac-sha256 send lifetime 3600 If authentication protocols that affects the routing or forwarding tables are not configured to use key chain (TCP-AO) authentication with 180 maximum lifetime, this is a finding.

## Group: SRG-NET-000205-RTR-000002

**Group ID:** `V-272079`

### Rule: The Cisco ACI must be configured to drop all fragmented Internet Control Message Protocol (ICMP) packets destined to itself.

**Rule ID:** `SV-272079r1114312_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Fragmented ICMP packets can be generated by hackers for DoS attacks such as Ping O' Death and Teardrop. It is imperative that all fragmented ICMP packets are dropped.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this review is for the DODIN Backbone, mark as not applicable. Review the external and internal ACLs to verify that the router is configured to only allow specific management and control plane traffic from specific sources destined to itself. 1. Navigate Tenant >> Contract >> Filter. 2. Select the "Drop Fragmented ICMP" filter. 3. Verify ICMP and Fragmented are selected to be denied. If all fragmented ICMP packets destined to Cisco ACI IP addresses are not dropped, this is a finding.

## Group: SRG-NET-000205-RTR-000006

**Group ID:** `V-272080`

### Rule: The BGP Cisco ACI must be configured to reject outbound route advertisements for any prefixes belonging to the IP core.

**Rule ID:** `SV-272080r1113986_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outbound route advertisements belonging to the core can result in traffic either looping or being black holed, or at a minimum, using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this review is for the DODIN Backbone, mark as not applicable. Verify the router is configured to deny router-advertisements. apic1(config-tenant-fhs-secpol)# router-advertisement-guard If the router is not configured to reject outbound route advertisements for prefixes belonging to the IP core, this is a finding.

## Group: SRG-NET-000205-RTR-000012

**Group ID:** `V-272081`

### Rule: The Cisco ACI must be configured to only permit management traffic that ingresses and egresses the OOBM interface.

**Rule ID:** `SV-272081r1114276_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To configure OOB management on an ACI fabric, use the Application Policy Infrastructure Controller (APIC), which is the central management point for the network. When setting up OOB access, a specific "contract" that controls which traffic is allowed on the OOB management network is typically defined. All management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an OOBM port, the interface functioning as the management interface must be configured so that management traffic does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the "show" command to verify the contract is attached to the management interface and that only permitted management traffic is allowed. If the router does not restrict traffic that ingresses and egresses the management interface, this is a finding. 1. Verify the OOB contract is configured to explicitly permit only management traffic. apic1(config)# contract MGMT_OOB apic1(config)# filter ingress apic1(config)# protocol icmp apic1(config)# protocol tcp port 22, 80, 443 apic1(config)# protocol udp port 68, 67 apic1(config)# filter egress apic1(config)# protocol icmp apic1(config)# protocol tcp port 22, 80, 443 apic1(config)# protocol udp port 68, 67 2. Verify the contract attached to the OOB Interface. apic1(config)# interface <leaf_switch_name>/<oob_interface_number> apic1(config-if)# contract mgmt_oob

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-272082`

### Rule: The Cisco ACI must be configured to implement message authentication and secure communications for all control plane protocols.

**Rule ID:** `SV-272082r1114265_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols used to exchange routing or packet forwarding information. This includes BGP, RIP, OSPF, EIGRP, IS-IS and LDP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify secure communications and message authentication on all control plane protocols is configured. 1. Verify Secure Communication: Navigate to Fabric >> Fabric Policies >> Pod Policies >> Policies >> Management. Verify SSH and SSL protocols are enabled for APIC management. 2. Verify Message Authentication: Navigate to Fabric >> Fabric Policies >> Pod Policies >> Policies >> Interconnect. Verify IPsec for FI communication is enabled. 3. Verify OpFlex for Southbound Communication is set to TLS. 4. Navigate to Fabric >> Fabric Policies >> Pod Policies >> Policies >> Trust Domain. Verify the Trust Domain is enabled and configured. Verify BGP neighbor authentication keys on Cisco ACI border leaf switches are configured to use a different authentication key for each AS peer. 1. Navigate to Tenants >> All Tenants >> your_tenant >> Networking >> L3Outs >> your_l3out. 2. Expand Logical Node Profiles >> node_profile. 3. Select Logical Interface Profiles >> interface_profile (where the BGP peering is configured). 4. Within the Logical Interface Profile, review each BGP Peer Connectivity profiles for each individual BGP peer. 5. In the BGP Peer Connectivity Profile settings, review the Password to verify each peer has a unique password. If message authentication and secure communications is not configured for all control plane protocols, this is a finding.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-272083`

### Rule: The BGP Cisco ACI must be configured to use a unique key for each autonomous system (AS) it peers with.

**Rule ID:** `SV-272083r1114278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between eBGP neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration. Verify the neighbor authentication keys on ACI border leaf switches use a different authentication key for each AS peer. Route maps can also show this view. ip tcp authentication key chain AS100 key 1 send-id 10 recv-id 10 key 2 send-id 20 recv-id 20 ip tcp authentication key chain AS200 key 1 send-id 30 recv-id 30 key 2 send-id 40 recv-id 40 router bgp 100 neighbor 10.0.0.1 ao AS100 router bgp 200 neighbor 10.0.1.1 ao AS200 If unique keys are not being used, this is a finding.

## Group: SRG-NET-000230-RTR-000003

**Group ID:** `V-272084`

### Rule: The Cisco ACI must be configured to use keys with a duration of 180 days or less for authenticating routing protocol messages.

**Rule ID:** `SV-272084r1114357_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the keys used for routing protocol authentication are guessed, the malicious user could create havoc within the network by advertising incorrect routes and redirecting traffic. Some routing protocols allow the use of key chains for authentication. A key chain is a set of keys that is used in succession, with each having a lifetime of no more than 180 days. Changing the keys frequently reduces the risk of them eventually being guessed. Keys cannot be used during time periods for which they are not activated. If a time period occurs during which no key is activated, neighbor authentication cannot occur, and therefore, routing updates will fail. Therefore, ensure that for a given key chain, key activation times overlap to avoid any period of time during which no key is activated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If any key has a lifetime of more than 180 days (expressed in seconds), this is a finding. Review the switch configuration using the show bgp and show ospf commands to view BGP and OSPF. The configuration will be similar to the example below. Key-Chain bgp_keys tcp Key 1 -- text 0 "070e234f" send lifetime 3600 recv-lifetime 3600 If any key has a lifetime of 180 days or less, this is a finding.

## Group: SRG-NET-000343-RTR-000002

**Group ID:** `V-272085`

### Rule: The Multicast Source Discovery Protocol (MSDP) Cisco ACI must be configured to authenticate all received MSDP packets.

**Rule ID:** `SV-272085r1114092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network routers presents additional risks to the core, whether from a rogue or misconfigured MSDP-enabled router. MSDP password authentication is used to validate each segment sent on the TCP connection between MSDP peers, protecting the MSDP session against the threat of spoofed packets being injected into the TCP connection stream.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Management Access configuration to determine if received MSDP packets are authenticated: 1. Navigate to Fabric >> Fabric Policies >> Policies >> Pod >> Management Access. 2. Verify the option for "Strict Security on APIC OOB Subnet" is selected. If the router does not require MSDP authentication, this is a finding.

## Group: SRG-NET-000362-RTR-000111

**Group ID:** `V-272086`

### Rule: The Cisco ACI must be configured to have gratuitous ARP (GARP) disabled on all external interfaces.

**Rule ID:** `SV-272086r1114094_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A GARP is an ARP broadcast in which the source and destination MAC addresses are the same. It is used to inform the network about a host IP address. A spoofed gratuitous ARP message can cause network mapping information to be stored incorrectly, causing network malfunction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration for each L3OUT Bridge Domain to determine if gratuitous ARP is disabled: 1. In the APIC GUI Navigation pane, select "Tenant" and inspect each Tenant's Bridge Domain configuration. 2. Expand "Networking" and right-click each Bridge Domain. 3. View the Layer 3 configuration tab. Verify GARP-based detection is not enabled. If GARP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-272087`

### Rule: The Cisco ACI must be configured to have Internet Control Message Protocol (ICMP) mask replies disabled on all external interfaces.

**Rule ID:** `SV-272087r1113993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify the ip mask-reply command is not enabled on any external interfaces as shown in the example below: apic1(config)# interface Ethernet0/1 apic(config-if)# no ip icmp mask-reply If the ip mask-reply command is configured on any external interface, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-272088`

### Rule: The BGP Cisco ACI must be configured to use the maximum prefixes feature to protect against route table flooding and prefix de-aggregation attacks.

**Rule ID:** `SV-272088r1114096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the de-aggregation risk. BGP maximum prefix must be used on all eBGP routers to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering AS. Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BGP configuration for each tenant: ip route protocol BGP View the BGP peer configuration maximum prefix value: neighbor 10.0.0.1 maximum-prefix nnnnnnn If the router is not configured to control the number of prefixes received from each peer to protect against route table flooding and prefix de-aggregation attacks, this is a finding.

## Group: SRG-NET-000362-RTR-000118

**Group ID:** `V-272089`

### Rule: The BGP Cisco ACI must be configured to limit the prefix size on any inbound route advertisement to /24 or the least significant prefixes issued to the customer.

**Rule ID:** `SV-272089r1114282_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the RP to verify it is rate limiting the number of PIM register messages. tenant <tenant_name> prefix-list ALLOW_SUBNET ip prefix 10.0.0.0/24 permit match-rule filter_rule match prefix allow_subnet tenant <tenant_name> l3extInstP <l3extInstP_name> route-profile FILTER_PROFILE If the router is not configured to limit the prefix size on any inbound route advertisement to /24, or the least significant prefixes issued to the customer, this is a finding.

## Group: SRG-NET-000362-RTR-000120

**Group ID:** `V-272090`

### Rule: The Cisco ACI multicast rendezvous point (RP) must be configured to limit the multicast forwarding cache so that its resources are not saturated by managing an overwhelming number of Protocol Independent Multicast (PIM) and Multicast Source Discovery Protocol (MSDP) source-active entries.

**Rule ID:** `SV-272090r1114314_rule`
**Severity:** low

**Description:**
<VulnDiscussion>MSDP peering between networks enables sharing of multicast source information. Enclaves with an existing multicast topology using PIM-SM can configure their RP routers to peer with MSDP routers. As a first step of defense against a denial-of-service (DoS) attack, all RP routers must limit the multicast forwarding cache to ensure router resources are not saturated managing an overwhelming number of PIM and MSDP source-active entries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PIM configuration: ip pim register-rate-limit 10 If the RP router is not configured to filter PIM register messages, rate limiting the number of PIM register messages, and accept MSDP packets only from known MSDP peers, this is a finding.

## Group: SRG-NET-000362-RTR-000121

**Group ID:** `V-272091`

### Rule: The multicast rendezvous point (RP) must be configured to rate limit the number of Protocol Independent Multicast (PIM) Register messages.

**Rule ID:** `SV-272091r1114102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a new source starts transmitting in a PIM Sparse Mode network, the designated router (DR) will encapsulate the multicast packets into register messages and forward them to the RP using unicast. This process can be taxing on the CPU for both the DR and the RP if the source is running at a high data rate and there are many new sources starting at the same time. This scenario can potentially occur immediately after a network failover. The rate limit for the number of register messages should be set to a relatively low value based on the known number of multicast sources within the multicast domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the RP to verify that it is rate limiting the number of PIM register messages: tenant <tenant-name> vrf <vrf-name> ip pim register rate limit 10 If the RP is not limiting PIM register messages, this is a finding.

## Group: SRG-NET-000362-RTR-000122

**Group ID:** `V-272092`

### Rule: The Cisco ACI must be configured to limit the mroute states created by Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) reports on a Cisco APIC Bridge Domain (BD) or interface.

**Rule ID:** `SV-272092r1114104_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Limiting mroute states helps prevent excessive multicast traffic flooding on the network by controlling the number of multicast groups a segment can join. By limiting multicast routes, the APIC can better manage its internal resources and prevent potential performance issues due to excessive multicast traffic. Depending on the ACI configuration, set a global IGMP state limit which would apply across all interfaces, or it may be necessary to configure limits on individual interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify it is limiting the number of mroute states via IGMP or MLD. Verify IGMP limits have been configured globally or on each host-facing interface via the ip igmp limit command as shown in the example: interface GigabitEthernet0/0 ip igmp limit nn Review the relevant Bridge Domain (BD) or interface. Verify it is configured to limit the number of multicast routes (mroute states) generated by IGMP or MLD reports. tenant <tenant_name> apic(config-tenant)# bridge-domain <BD_name> apic(config-bd)# interface <interface_name> apic(config-if)# ip mroute limit <maximum_mroute_count> If the ACI is not limiting multicast requests via IGMP or MLD on a global or interfaces basis, this is a finding.

## Group: SRG-NET-000362-RTR-000123

**Group ID:** `V-272093`

### Rule: The Cisco ACI multicast shortest-path tree (SPT) threshold must be set to the default.

**Rule ID:** `SV-272093r1113999_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>On a Cisco ACI, the "ip pim spt-threshold" is not set to infinity by default; it is typically set to a finite value, with the default usually being zero, meaning it will always use the SPT for PIM calculations. The standard configuration for "ip pim spt-threshold" on Cisco devices is usually set to zero. This threshold determines when a router will use the SPT to forward multicast traffic in PIM Sparse Mode. While technically possible, setting the threshold to "infinity" would mean the router would never use the SPT, which is generally not the intended behavior. In a Cisco ACI fabric, the SPT threshold typically does not need to be manually configured to increase it for multicast, as the system automatically calculates the SPT based on the network topology, and the border leaf switches handle the SPT switchover functionality; however, in specific scenarios where there are a large number of multicast sources, or multicast traffic flow must be optimized, adjusting the SPT threshold may be considered depending on the network requirements. Thus, it is not recommended that this be configured. While technically possible, setting the threshold to "infinity" would mean the router would never use the SPT, which is generally not the intended behavior.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the SPT switchover threshold is not explicitly configured. If the "ip pim spt-threshold <value> command is configured for any value other than zero, this is a finding.

## Group: SRG-NET-000362-RTR-000124

**Group ID:** `V-272094`

### Rule: Cisco ACI must be configured to enable the Generalized TTL Security Mechanism (GTSM) for BGP sessions.

**Rule ID:** `SV-272094r1114284_rule`
**Severity:** low

**Description:**
<VulnDiscussion>GTSM is designed to protect a router's IP-based control plane from denial-of-service (DoS) attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all Exterior Border Gateway Protocol speaking routers. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent routers, that is, the Exterior Border Gateway Protocol peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP configuration to verify that TTL security has been configured for each external neighbor as shown in the example below: policy BGP_Peer_Profile no neighbor 10.1.1.1 ebgp-multihop neighbor 10.1.1.1 ttl-security If the Cisco ACI is not configured to use GTSM for all Exterior BGP peering sessions, this is a finding.

## Group: SRG-NET-000364-RTR-000114

**Group ID:** `V-272095`

### Rule: The Cisco ACI multicast must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join only multicast groups that have been approved by the organization.

**Rule ID:** `SV-272095r1115727_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Source Specific Multicast (SSM) implementation. This requirement is not applicable to Any Source Multicast (ASM) since the filtering is being performed by the rendezvous point switch. Review the configuration of the designated router (DR) to verify that it is filtering IGMP or MLD Membership Report messages, allowing hosts to join only those groups that have been approved. If the Cisco ACI is not filtering IGMP or MLD Membership Report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000115

**Group ID:** `V-272096`

### Rule: The Cisco ACI multicast must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join a multicast group only from sources that have been approved by the organization.

**Rule ID:** `SV-272096r1114286_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable to Source Specific Multicast (SSM) implementation. This requirement is not applicable to Any Source Multicast (ASM) since the filtering is being performed by the rendezvous point switch. Review the configuration to verify that it is filtering IGMP or MLD Membership Report messages, allowing hosts to join only those groups that have been approved. switch BD-1 ip igmp snooping ip igmp snooping policy ApprovedSources ip igmp snooping policy ApprovedSources source-filter 10.0.0.1 interface Vlan10 ip igmp snooping policy ApprovedSources If the Cisco API is not filtering IGMP or MLD Membership Report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000116

**Group ID:** `V-272097`

### Rule: Cisco ACI Multicast Source Discovery Protocol (MSDP) must be configured to only accept MSDP packets from known MSDP peers.

**Rule ID:** `SV-272097r1114289_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network routers presents additional risks to the DISN Core, whether from a rogue or misconfigured MSDP-enabled router. To guard against an attack from malicious MSDP traffic, the receive path or interface filter for all MSDP-enabled RP routers must be configured to only accept MSDP packets from known MSDP peers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if there is a receive path or interface filter to only accept MSDP packets from known MSDP peers. 1. Verify that interfaces used for MSDP peering have an inbound ACL as shown in the example below: interface GigabitEthernet1/1 ip address x.1.28.8 255.255.255.0 ip access-group EXTERNAL_ACL_INBOUND in 2. Verify that the ACL restricts MSDP peering to only known sources. ip access-list extended EXTERNAL_ACL_INBOUND permit tcp host x.1.28.2 permit tcp host x.1.28.2 If the switch is not configured to only accept MSDP packets from known MSDP peers, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-272098`

### Rule: The Cisco ACI must be configured to use its loopback address as the source address for internal Border Gateway Protocol (iBGP) peering sessions.

**Rule ID:** `SV-272098r1114004_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the BGP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router's loopback address instead of the numerous physical interface addresses. When the loopback address is used as the source for external BGP (eBGP) peering, the BGP session will be harder to hijack since the source address to be used is not known globally, making it more difficult for a hacker to spoof an eBGP neighbor. By using traceroute, a hacker can easily determine the addresses for an eBGP speaker when the IP address of an external interface is used as the source address. The routers within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify a loopback address has been configured. tenant <tenant-name> networking l3out <l3out-name> protocol BGP neighbor 10.1.1.1 update-source Loopback0 If the switch does not use its loopback address as the source address for all iBGP sessions, this is a finding.

## Group: SRG-NET-000512-RTR-000011

**Group ID:** `V-272099`

### Rule: The Multicast Source Discovery Protocol (MSDP) Cisco ACI must be configured to use its loopback address as the source address when originating MSDP traffic.

**Rule ID:** `SV-272099r1114110_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of MSDP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router's loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the loopback interface is used as the source address for all MSDP packets generated by the router. 1. Navigate to Fabric >> Fabric Policies >> Policies >> Pod >> Management Access on the APIC GUI to find the relevant settings. 2. Verify the loopback interface IP address is used as the source address. If the router does not use its loopback address as the source address when originating MSDP traffic, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-272100`

### Rule: The Cisco ACI must be configured to advertise a hop limit of at least 32 in Cisco ACI Advertisement messages for IPv6 stateless auto-configuration deployments.

**Rule ID:** `SV-272100r1114112_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery Protocol allows a hop limit value to be advertised by routers in a router advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Enter the "show ipv6 int" command on the leaf switch to verify the configuration was pushed out correctly to the leaf switch. interface Ethernet 1/1 ipv6 router advertisement hop-limit 32 If a hop limit of at least 32 is not advertised in Cisco ACI advertisement messages for IPv6 stateless auto-configuration deployments, this is a finding.

## Group: SRG-NET-000512-RTR-000013

**Group ID:** `V-272101`

### Rule: The Cisco ACI must not be configured to use IPv6 site local unicast addresses.

**Rule ID:** `SV-272101r1114007_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As currently defined, site local addresses are ambiguous and can be present in multiple sites. The address itself does not contain any indication of the site to which it belongs. The use of site-local addresses has the potential to adversely affect network security through leaks, ambiguity, and potential misrouting as documented in section 2 of RFC3879. RFC3879 formally deprecates the IPv6 site-local unicast prefix FEC0::/10 as defined in RFC3513. Specify the appropriate IPv6 address range within the relevant configuration objects like bridge domains and L3Out, ensuring the addresses fall within the allocated site local unicast prefix, and enable IPv6 routing on the fabric level, allowing the ACI switches to learn and route traffic based on these IPv6 addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to ensure FEC0::/10 IP addresses are not defined. apic1(config) show ipv6 interface gigabitethernet 0/0/0 If IPv6 site local unicast addresses are defined, this is a finding.

## Group: SRG-NET-000715-RTR-000120

**Group ID:** `V-272102`

### Rule: The Cisco ACI must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

**Rule ID:** `SV-272102r1114291_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command and control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions. In Cisco ACI, subnetwork addresses are configured logically using the policy model, defining separate subnets within different endpoint groups (EPGs) within a tenant, effectively creating logically separate network segments without needing to physically partition the network on the underlying hardware; this separation is achieved through policy-based routing and access control based on the EPGs assigned to different applications or workloads.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify logical separation using EPGs, bridge domains, and/or tenants is configured. The following is an example of an EPG: apic1(config)# leaf 1017 apic1(config-leaf)# interface ethernet 1/13 apic1(config-leaf-if)# vlan-domain member dom1 apic1(config-leaf-if)# switchport trunk allowed vlan 20 tenant t1 application AP1 epg EPG1 If subnetworks are not configured to isolate organization-defined critical system components and functions, this is a finding.

## Group: SRG-NET-000760-RTR-000160

**Group ID:** `V-272103`

### Rule: The Cisco ACI must establish organization-defined alternate communication paths for system operations organizational command and control.

**Rule ID:** `SV-272103r1114294_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An incident, whether adversarial- or nonadversarial-based, can disrupt established communication paths used for system operations and organizational command and control. Alternate communication paths reduce the risk of all communications paths being affected by the same incident. To compound the problem, the inability of organizational officials to obtain timely information about disruptions or to provide timely direction to operational elements after a communication path incident, can impact the ability of the organization to respond to such incidents in a timely manner. Establishing alternate communication paths for command and control purposes, including designating alternative decision makers if primary decision makers are unavailable and establishing the extent and limitations of their actions, can greatly facilitate the organization's ability to continue to operate and take appropriate actions during an incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SSP and the ACI configuration to verify logical separation using EPGs, bridge domains, and/or tenants is configured. The following is an example of an EPG: apic1(config)# leaf 1017 apic1(config-leaf)# interface ethernet 1/13 apic1(config-leaf-if)# vlan-domain member dom1 apic1(config-leaf-if)# switchport trunk allowed vlan 20 tenant t1 application AP1 epg EPG1 If organization-defined alternate communication paths for system operations organizational command and control have not been established, this is a finding.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-272104`

### Rule: The Cisco ACI must be configured to protect against or limit the effects of denial-of-service (DoS) attacks by employing control plane protection.

**Rule ID:** `SV-272104r1114297_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The route processor (RP) is critical to all network operations because it is the component used to build all forwarding paths for the data plane via control plane processes. It is also instrumental in ongoing network management functions that keep the routers and links available for providing network services. Any disruption to the RP or the control and management planes can result in mission-critical network outages. A DoS attack targeting the RP can result in excessive CPU and memory utilization. To maintain network stability and RP security, the router must be able to handle specific control plane and management plane traffic destined to the RP. In the past, one method of filtering was to use ingress filters on forwarding interfaces to filter both forwarding path and receiving path traffic. However, this method does not scale well as the number of interfaces grows and the size of the ingress filters grows. Control plane policing increases the security of routers and multilayer switches by protecting the RP from unnecessary or malicious traffic. Filtering and rate limiting the traffic flow of control plane packets can be implemented to protect routers against reconnaissance and DoS attacks, allowing the control plane to maintain packet forwarding and protocol states despite an attack or heavy load on the router or multilayer switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify Cisco ACI is configured to employ control plane protection. 1. Verify traffic types have been classified based on importance levels. The following is an example configuration: class-map match-all CoPP_CRITICAL match access-group name CoPP_CRITICAL class-map match-any CoPP_IMPORTANT match access-group name CoPP_IMPORTANT match protocol arp class-map match-all CoPP_NORMAL match access-group name CoPP_NORMAL class-map match-any CoPP_UNDESIRABLE match access-group name CoPP_UNDESIRABLE class-map match-all CoPP_DEFAULT match access-group name CoPP_DEFAULT 2. Review the Access Control Lists (ACLs) referenced by the class maps to determine if the traffic is being classified appropriately. The following is an example configuration: ip access-list extended CoPP_CRITICAL remark our control plane adjacencies are critical permit ospf host [OSPF neighbor A] any permit ospf host [OSPF neighbor B] any permit pim host [PIM neighbor A] any permit pim host [PIM neighbor B] any permit pim host [RP addr] any permit igmp any 224.0.0.0 15.255.255.255 permit tcp host [BGP neighbor] eq bgp host [local BGP addr] permit tcp host [BGP neighbor] host [local BGP addr] eq bgp deny ip any any ip access-list extended CoPP_IMPORTANT permit tcp host [TACACS server] eq tacacs any permit tcp [management subnet] 0.0.0.255 any eq 22 permit udp host [SNMP manager] any eq snmp permit udp host [NTP server] eq ntp any deny ip any any ip access-list extended CoPP_NORMAL remark we will want to rate limit ICMP traffic deny icmp any host x.x.x.x fragments permit icmp any any echo permit icmp any any echo-reply permit icmp any any time-exceeded permit icmp any any unreachable deny ip any any ip access-list extended CoPP_UNDESIRABLE remark other management plane traffic that should not be received permit udp any any eq ntp permit udp any any eq snmp permit tcp any any eq 22 permit tcp any any eq 23 remark other control plane traffic not configured on router permit eigrp any any permit udp any any eq rip deny ip any any ip access-list extended CoPP_DEFAULT permit ip any any Note: Explicitly defining undesirable traffic with ACL entries enables the network operator to collect statistics. Excessive ARP packets can potentially monopolize route processor resources, starving other important processes. Currently, ARP is the only layer 2 protocol that can be specifically classified using the match protocol command. 3. Review the policy-map to determine if the traffic is being policed appropriately for each classification. The following is an example configuration: policy-map CONTROL_PLANE_POLICY class CoPP_CRITICAL police 512000 8000 conform-action transmit exceed-action transmit class CoPP_IMPORTANT police 256000 4000 conform-action transmit exceed-action drop class CoPP_NORMAL police 128000 2000 conform-action transmit exceed-action drop class CoPP_UNDESIRABLE police 8000 1000 conform-action drop exceed-action drop class CoPP_DEFAULT police 64000 1000 conform-action transmit exceed-action drop 4. Verify that the CoPP policy is enabled. The following is an example configuration: (config)# leaf 101 (config-leaf)# int eth 1/10 (config-leaf-if)# service-policy type control-plane-if Note: Control Plane Protection (CPPr) can be used to filter as well as police control plane traffic destined to the RP. CPPr is very similar to CoPP and has the ability to filter and police traffic using finer granularity by dividing the aggregate control plane into three separate categories: (1) host, (2) transit, and (3) CEF-exception. Hence, a separate policy-map could be configured for each traffic category. If the Cisco router is not configured to protect against known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

## Group: SRG-NET-000193-RTR-000001

**Group ID:** `V-272105`

### Rule: The MPLS Cisco ACI with Resource Reservation Protocol Traffic Engineering (RSVP-TE) enabled must be configured with message pacing or refresh reduction to adjust the maximum number of RSVP messages to an output queue based on the link speed and input queue size of adjacent core Cisco ACIs.

**Rule ID:** `SV-272105r1114299_rule`
**Severity:** low

**Description:**
<VulnDiscussion>RSVP-TE can be used to perform constraint-based routing when building LSP tunnels within the network core that will support QoS and traffic engineering requirements. RSVP-TE is also used to enable MPLS Fast Reroute, a network restoration mechanism that will reroute traffic onto a backup LSP in case of a node or link failure along the primary path. When there is a disruption in the MPLS core, such as a link flap or router reboot, the result is a significant amount of RSVP signaling, such as "PathErr" and "ResvErr" messages that need to be sent for every LSP using that link. RSVP messages are sent out using either hop-by-hop or with the router alert bit set in the IP header. This means that every router along the path must examine the packet to determine if additional processing is required for these RSVP messages. If there is enough signaling traffic in the network, it is possible for an interface to receive more packets for its input queue than it can hold, resulting in dropped RSVP messages and hence slower RSVP convergence. Increasing the size of the interface input queue can help prevent dropping packets; however, there is still the risk of having a burst of signaling traffic that can fill the queue. Solutions to mitigate this risk are RSVP message pacing or refresh reduction to control the rate at which RSVP messages are sent. RSVP refresh reduction includes the following features: RSVP message bundling, RSVP Message ID to reduce message processing overhead, reliable delivery of RSVP messages using Message ID, and summary refresh to reduce the amount of information transmitted every refresh interval. To configure a rate-limit on RSVP bandwidth on a Cisco ACI interface, use the command "ip rsvp bandwidth" within the interface configuration mode, specifying the desired bandwidth value in kilobits per second (kbps), which will act as the maximum reservable bandwidth for RSVP traffic on that interface. For more granular control, consider creating a dedicated RSVP policy to further define how bandwidth is allocated based on specific traffic characteristics. Optionally, specify a percentage of the interface bandwidth by using the "percent" keyword with the command.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine RSVP messages are rate limited. 1. Determine if MPLS TE is enabled globally and at least one interface. To display statistics information for all the interfaces and VRFs in the system, navigate to Tenant >> infra >> Networking >> SR-MPLS Infra L3Outs. 2. Verify the rsvp bandwidth is set. ip rsvp bandwidth 1000000 If the router with RSVP-TE enabled does not rate limit RSVP messages based on the link speed and input queue size of adjacent core routers, this is a finding.

