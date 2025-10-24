# STIG Benchmark: Juniper EX Series Switches Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-RTR-000001

**Group ID:** `V-253973`

### Rule: The Juniper router must be configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies.

**Rule ID:** `SV-253973r843952_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, and devices) within information systems. Enforcement occurs, for example, in boundary protection devices (e.g., gateways, routers, guards, encrypted tunnels, and firewalls) that employ rule sets or establish configuration settings that restrict information system services, provide a packet filtering capability based on header information, or provide a message filtering capability based on message content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that stateless firewall filters are configured to allow or deny traffic for specific source and destination addresses as well as ports and protocols. Verify the IP addresses are appropriate for the target environment. IP addresses are configured in lists at [edit policy-options] or are directly embedded into each term. [edit policy-options] prefix-list inside-addresses-ipv4 { <inside IPv4 subnet>/<mask>; <inside IPv4 subnet>/<mask>; } prefix-list inside-addresses-ipv6 { <inside IPv6 subnet>/<prefix>; <inside IPv6 subnet>/<prefix>; } For example: [edit firewall] family inet { filter authorized-outbound-ipv4 { term permitted-http { from { source-prefix-list { inside-addresses-ipv4; } destination-address { <destination IPv4 address>/<mask>; } protocol tcp; destination-port http; } then accept; } : <other terms> : term permitted-source-addresses { from { source-prefix-list { inside-addresses-ipv4; } protocol-except tcp; destination-port-except http; } then accept; } term default-deny { then { log; syslog; discard; } } } } family inet6 { filter authorized-outbound-ipv6 { term permitted-http { from { source-prefix-list { inside-addresses-ipv6; } destination-address { <destination IPv6 address>/<prefix>; } next-header tcp; destination-port http; } then accept; } : <other terms> : term permitted-source-addresses { from { source-prefix-list { inside-addresses-ipv6; } next-header-except tcp; destination-port-except http; } then accept; } term default-deny { then { log; syslog; discard; } } } } Verify filters are applied to the correct interface. For example, the "authorized-outbound" filter, as written, should be applied to the ingress of internal interfaces: [edit interfaces] <internal interface name> { unit <number> { family inet { filter { input authorized-outbound-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { input authorized-outbound-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" and "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. If the router is not configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies, this is a finding.

## Group: SRG-NET-000018-RTR-000002

**Group ID:** `V-253974`

### Rule: The Juniper BGP router must be configured to reject inbound route advertisements for any Bogon prefixes.

**Rule ID:** `SV-253974r843955_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements for Bogon prefixes can result in the local autonomous system (AS) becoming a transit for malicious traffic as it will in turn advertise these prefixes to neighbor autonomous systems. The list of Bogon addresses can change, based upon new address range assignments, and must be reviewed to ensure filters remain current.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP router configuration to verify that it will reject routes of any currently defined Bogon prefixes. Example route-filter-list of Bogon addresses with corresponding policy-statement referencing the list: [edit policy-options] route-filter-list bogon { /* This host on this network */ 0.0.0.0/8 orlonger; /* CGN Addresses */ 100.64.0.0/10 orlonger; /* Loopback */ 127.0.0.0/8 orlonger; /* IPv4 link-local or APIPA */ 169.254.0.0/16 orlonger; /* IETF Protocol Assignments (/24) and DS-Lite (/29) */ 192.0.0.0/24 orlonger; /* IPv4 documentation addresses: TEST-NET-1 */ 192.0.2.0/24 orlonger; /* 6to4 Relay Anycast descr in RFC3068 */ 192.88.99.0/24 orlonger; /* Benchmark testing descr in RFC2544 */ 198.18.0.0/15 orlonger; /* IPv4 documentation addresses: TEST-NET-2 */ 198.51.100.0/24 orlonger; /* IPv4 documentation addresses: TEST-NET-3 */ 203.0.113.0/24 orlonger; /* Multicast */ 224.0.0.0/24 orlonger; /* Reserved */ 240.0.0.0/4 orlonger; /* RFC1918 Addresses */ 10.0.0.0/8 orlonger; 172.16.0.0/12 orlonger; 192.168.0.0/16 orlonger; <add additional routes as needed> } route-filter-list bogon-ipv6 { /* Includes unspecified (::/128) and loopback (::1/128) */ ::/8 orlonger; /* IPv4-mapped */ ::ffff:0:0/96 orlonger; /* IPv4 Compatible */ ::/96 orlonger; /* 6Bone */ 3ffe::/16 orlonger; /* IPv4-IPv6 Translate */ 64:ff9b::/96 orlonger; /* Reserved - 100::/8 includes Discard-Only (100::/64) */ 100::/8 orlonger; 200::/7 orlonger; 400::/6 orlonger; 800::/5 orlonger; 1000::/4 orlonger; 4000::/3 orlonger; 6000::/3 orlonger; 8000::/3 orlonger; a000::/3 orlonger; c000::/3 orlonger; e000::/4 orlonger; f000::/5 orlonger; f800::/6 orlonger; fe00::/9 orlonger; /* IETF Protocol Assignments */ 2001::/23 orlonger; /* TEREDO */ 2001::/32 orlonger; /* Benchmarking */ 2001:2::/48 orlonger; /* Documentation */ 2001:db8::/32 orlonger; /* ORCHID */ 2001:10::/28 orlonger; /* 6to4 */ 2002::/16 orlonger; /* Unique-Local */ fc00::/7 orlonger; /* Linked-Scoped Unicast */ fe80::/10 orlonger; /* Site local (deprecated) - now reserved */ fec0::/10 orlonger; /* Multicast */ ff00::/8 orlonger; <add additional routes as needed> } Note: The comments (/* comment */) are annotations used to easily identify each list item. Annotations are not required. To add annotations, navigate to the appropriate hierarchy level ("edit policy-options route-filter-list <list name>" in this example) and use the "annotate" command (annotate <list item> "desired comment"). policy-statement bgp-discard { term 1 { from { route-filter-list bogon; route-filter-list bogon-ipv6; } then reject; } <add additional terms as needed> } Note: Using a route-filter-list permits list reuse as well as easing management because the policy-statement only need reference the list once. Other terms within the same policy-statement can be added without affecting the Bogon list. The prefix filter must be referenced inbound on the appropriate BGP neighbor statements. Verify the eBGP import statement prevents Junos from importing routes into the route table. Junos accepts import statements at three hierarchy levels: Global protocol, group, and neighbor (peer). Global is the most general, followed by group, and neighbor is the most restrictive. Junos applies only the most restrictive policy so if a policy is configured at the protocol, group, and neighbor level, only the neighbor policy is applied. [edit protocols bgp] group eBGP { <other group configuration> import bgp-discard; neighbor 192.0.2.2 { <other neighbor configuration> import bgp-discard; } } import bgp-discard; <other BGP configuration> If the router is not configured to reject inbound route advertisements for any Bogon prefixes, this is a finding.

## Group: SRG-NET-000018-RTR-000003

**Group ID:** `V-253975`

### Rule: The Juniper BGP router must be configured to reject inbound route advertisements for any prefixes belonging to the local autonomous system (AS).

**Rule ID:** `SV-253975r843958_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements belonging to the local AS can result in traffic looping, being black holed, or at a minimum using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP router configuration to verify that it will reject routes belonging to the local AS. Example route-filter-list of local AS addresses with corresponding policy-statement referencing the list. Verify the routes are appropriate for the target environment. [edit policy-options] route-filter-list local-routes { 192.0.2.0/24 orlonger; 192.0.3.0/24 orlonger; } route-filter-list local-routes-ipv6 { 2001:db8:2::/64 orlonger; 2001:db8:3::/64 orlonger; } policy-statement bgp-discard { term 1 { from { route-filter-list bogon; route-filter-list bogon-ipv6; } then reject; } term 2 { from { route-filter-list local-routes; route-filter-list local-routes-ipv6; } then reject; } term 3 { from protocol [ ospf direct ]; then reject; } } The example shows using route-filter-lists to ease management. The policy-statement also supports the route directly in the match condition. For example, "route-filter 192.0.2.0/24 orlonger" (in place of route-filter-list local-routes). Note: To reject routes learned via OSPF or directly-connected routes, include a term with a protocol (OSPF and directly-connected routes shown). The policy-statement includes the Bogon term to demonstrate adding terms to a policy without affecting existing terms. The prefix filter must be referenced inbound on the appropriate BGP neighbor statements. Verify the eBGP import statement prevents Junos from importing routes into the route table. Junos accepts import statements at three hierarchy levels: Global protocol, group, and neighbor (peer). Global is the most general, followed by group, and neighbor is the most restrictive. Junos applies only the most restrictive policy so if a policy is configured at the protocol, group, and neighbor level, only the neighbor policy is applied. [edit protocols bgp] group eBGP { <other group configuration> import bgp-discard; neighbor 192.0.2.2 { <other neighbor configuration> import bgp-discard; } } import bgp-discard; <other BGP configuration> If the router is not configured to reject inbound route advertisements belonging to the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000004

**Group ID:** `V-253976`

### Rule: The Juniper BGP router must be configured to reject inbound route advertisements from a customer edge (CE) router for prefixes that are not allocated to that customer.

**Rule ID:** `SV-253976r843961_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a best practice, a service provider should only accept customer prefixes that have been assigned to that customer and any peering autonomous systems. A multi-homed customer with BGP speaking routers connected to the internet or other external networks could be breached and used to launch a prefix deaggregation attack. Without ingress route filtering of customers, the effectiveness of such an attack could impact the entire IP core and its customers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP router configuration to verify there are filters defined to only accept routes for prefixes that belong to specific customers. Example route-filter-list of customer addresses with corresponding policy-statement referencing the list: [edit policy-options] route-filter-list customer1-routes { <customer route 1/mask> orlonger; <customer route 2/mask> orlonger; } route-filter-list customer1-routes-ipv6 { <customer route 1/prefix> orlonger; <customer route 1/prefix> orlonger; } <additional route-filter-list for other customers> policy-statement bgp-accept-cust1-routes { term 1 { from { route-filter-list customer1-routes; route-filter-list customer1-routes-ipv6; } then accept; } term 2 { then reject; } } <additional policies for other customers> Note: The example shows using route-filter-lists to ease management. The policy-statement also supports the route directly in the match condition. For example, "route-filter <customer route 1/mask> orlonger" (in place of route-filter-list customer-routes). Verify the eBGP import statement prevents Junos from importing routes into the route table. Junos accepts import statements at three hierarchy levels: Global protocol, group, and neighbor (peer). Global is the most general, followed by group, and neighbor is the most restrictive. Junos applies only the most restrictive policy so if a policy is configured at the protocol, group, and neighbor level, only the neighbor policy is applied. [edit protocols bgp] group customer1 { <other group configuration> import bgp-accept-cust1-routes; neighbor <address> { <other neighbor configuration> import bgp-accept-cust1-routes; } } import <import policy name>; <other BGP configuration> If the router is not configured to reject inbound route advertisements from each CE router for prefixes that are not allocated to that customer, this is a finding. Note: Routes to PE-CE links within a VPN are needed for troubleshooting end-to-end connectivity across the MPLS/IP backbone. Hence, these prefixes are an exception to this requirement.

## Group: SRG-NET-000018-RTR-000005

**Group ID:** `V-253977`

### Rule: The Juniper BGP router must be configured to reject outbound route advertisements for any prefixes that do not belong to any customers or the local autonomous system (AS).

**Rule ID:** `SV-253977r843964_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Advertisement of routes by an AS for networks that do not belong to any of its customers pulls traffic away from the authorized network. This causes a denial of service (DoS) on the network that allocated the block of addresses and may cause a DoS on the network that is inadvertently advertising it as the originator. It is also possible that a misconfigured or compromised router within the GIG IP core could redistribute IGP routes into BGP, thereby leaking internal routes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the BGP router configuration to verify there is a filter defined to only advertise routes for prefixes belonging to any customer or the local AS. Example route-filter-list of customer addresses with corresponding policy-statement referencing the list: [edit policy-options] route-filter-list customer1-routes { <customer route 1/mask> exact; <customer route 2/mask> exact; } route-filter-list customer1-routes-ipv6 { <customer route 1/prefix> exact; <customer route 2/prefix> exact; } <additional route-filter-lists for other customers> policy-statement bgp-advertise-cust-routes { term 1 { from { route-filter-list customer1-routes; route-filter-list customer1-routes-ipv6; } then accept; } <additional terms for other customers> term default { then reject; } } Note: The example shows using route-filter-lists to ease management. The policy-statement also supports the route directly in the match condition. For example, "route-filter <customer route 1/mask> exact" (in place of route-filter-list customer-routes). The prefix filter must be referenced outbound on the appropriate BGP neighbor statements. Verify the eBGP export statement prevents Junos from exporting routes from the route table into BGP. Junos accepts export statements at three hierarchy levels: Global protocol, group, and neighbor (peer). Global is the most general, followed by group, and neighbor is the most restrictive. Junos applies only the most restrictive policy so if a policy is configured at the protocol, group, and neighbor level, only the neighbor policy is applied. [edit protocols bgp] group eBGP { <other group configuration> export bgp-advertise-cust-routes; neighbor <address> { <other neighbor configuration> export bgp-advertise-cust-routes; } } export bgp-advertise-cust-routes; <other BGP configuration> If the router is not configured to reject outbound route advertisements that do not belong to any customers or the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000006

**Group ID:** `V-253978`

### Rule: The Juniper BGP router must be configured to reject route advertisements from BGP peers that do not list their autonomous system (AS) number as the first AS in the AS_PATH attribute.

**Rule ID:** `SV-253978r843967_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure the IP core is not used as a transit network for unauthorized or possibly even internet traffic. All autonomous system boundary routers (ASBRs) must ensure updates received from eBGP peers list their AS number as the first AS in the AS_PATH attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP router configuration to verify the router is configured to deny updates received from eBGP peers that do not list their AS number as the first AS in the AS_PATH attribute. Verify the configuration of "enforce-first-as" at either the BGP global or group level. [edit protocols bgp] group eBGP { enforce-first-as; neighbor <address>; } enforce-first-as; If the router is not configured to reject updates from peers that do not list their AS number as the first AS in the AS_PATH attribute, this is a finding.

## Group: SRG-NET-000018-RTR-000007

**Group ID:** `V-253979`

### Rule: The Juniper router configured for Multicast Source Discovery Protocol (MSDP) must filter received source-active multicast advertisements for any undesirable multicast groups and sources.

**Rule ID:** `SV-253979r843970_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The interoperability of BGP extensions for interdomain multicast routing and MSDP enables seamless connectivity of multicast domains between autonomous systems. MP-BGP advertises the unicast prefixes of the multicast sources used by Protocol Independent Multicast (PIM) routers to perform RPF checks and build multicast distribution trees. MSDP is a mechanism used to connect multiple PIM sparse-mode domains, allowing RPs from different domains to share information about active sources. When RPs in peering multicast domains hear about active sources, they can pass on that information to their local receivers, thereby allowing multicast data to be forwarded between the domains. Configuring an import policy to block multicast advertisements for reserved, martian, single-source multicast, and any other undesirable multicast groups, as well as any source-group (S, G) states with Bogon source addresses, would assist in avoiding unwanted multicast traffic from traversing the core.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if there is an import policy to block source-active multicast advertisements for any undesirable multicast groups, as well as any (S, G) states with undesirable source addresses. Verify that an inbound source-active filter is bound to each MSDP peer. [edit protocols msdp] peer <address> { import source-active-filter; } Review the policy-statement referenced by the source-active filter to verify that undesirable multicast groups, auto-RP, single source multicast (SSM) groups, and advertisements from undesirable sources are blocked. [edit policy-options] policy-statement source-active-filter { term unauth-groups { from { route-filter 224.0.1.2/32 exact; route-filter 224.0.2.2/32 exact; } then reject; } term unauth-sources { from { source-address-filter 10.0.0.0/8 orlonger; source-address-filter 127.0.0.0/8 orlonger; } then reject; } } If the router is not configured with an import policy to block undesirable SA multicast advertisements, this is a finding.

## Group: SRG-NET-000018-RTR-000008

**Group ID:** `V-253980`

### Rule: The Juniper router configured for Multicast Source Discovery Protocol (MSDP) must filter source-active multicast advertisements to external MSDP peers to avoid global visibility of local-only multicast sources and groups.

**Rule ID:** `SV-253980r843973_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To avoid global visibility of local information, there are a number of source-group (S, G) states in a PIM-SM domain that must not be leaked to another domain, such as multicast sources with private address, administratively scoped multicast addresses, and the auto-RP groups (224.0.1.39 and 224.0.1.40). Allowing a multicast distribution tree, local to the core, to extend beyond its boundary could enable local multicast traffic to leak into other autonomous systems and customer networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if there is export policy to block local source-active multicast advertisements. Verify that an outbound source-active filter is bound to each MSDP peer. [edit protocols msdp] peer <address> { export source-active-filter; } Review the policy-statement referenced by the source-active filters and verify that MSDP source-active messages being sent to MSDP peers do not leak advertisements that are local. [edit policy-options] policy-statement source-active-filter { term unauth-groups { from { route-filter 224.0.1.2/32 exact; route-filter 224.0.2.2/32 exact; } then reject; } term unauth-sources { from { source-address-filter 10.0.0.0/8 orlonger; source-address-filter 127.0.0.0/8 orlonger; } then reject; } } If the router is not configured with an export policy to block local source-active multicast advertisements, this is a finding.

## Group: SRG-NET-000018-RTR-000009

**Group ID:** `V-253981`

### Rule: The Juniper router configured for MSDP must limit the amount of source-active messages it accepts on per-peer basis.

**Rule ID:** `SV-253981r843976_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To reduce any risk of a denial-of-service (DoS) attack from a rogue or misconfigured MSDP router, the router must be configured to limit the number of source-active messages it accepts from each peer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it is configured to limit the amount of source-active messages it accepts on a per-peer basis. [edit protocols] msdp { active-source-limit { maximum <1..1000000>; threshold <1..1000000>; log-warning <percent to log warning>; } local-address <lo0 address>; <additional configuration> peer <address> { active-source-limit { maximum <1..1000000>; threshold <1..1000000>; log-warning <percent to log warning>; } authentication-key "hashed PSK"; ## SECRET-DATA } } Note: Both the global, and the peer limit, are applied to every MSDP peer, and Junos applies the most restrictive limit. The maximum value sets the upper limit for source-active messages and the threshold value determines when Junos begins Random Early Detection (RED) dropping to alleviate congestion. The log-warning value is a percent where Junos begins generating syslog messages. If the router is not configured to limit the source-active messages it accepts, this is a finding.

## Group: SRG-NET-000018-RTR-000010

**Group ID:** `V-253982`

### Rule: The Juniper router configured for BGP must reject route advertisements from CE routers with an originating AS in the AS_PATH attribute that does not belong to that customer.

**Rule ID:** `SV-253982r843979_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure that the local AS is not used as a transit network for unauthorized traffic. To ensure that the local AS does not carry any prefixes that do not belong to any customers, all PE routers must be configured to reject routes with an originating AS other than that belonging to the customer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify the router is configured to deny updates received from CE routers with an originating AS in the AS_PATH attribute that does not belong to that customer. Review the router configuration and verify that there is an as-path access-list statement defined. Each peer requires a regular expression (REGEX) defining the expected AS_PATH attribute. Each neighbor has an import policy applied to filter updates that do not match the expected path attribute. Assuming AS 65535 is an authorized neighbor's originating AS, verify an as-path REGEX is defined ('.* 65535') and a policy-statement configured to accept that REGEX. [edit policy-options] policy-statement bgp_originate_65535 { term 1 { from as-path orig_65535; then accept; } term 2 { then reject; } } as-path orig_65535 ".* 65535"; Note: The REGEX matches zero or more prepended AS in the AS_PATH beginning with the defined AS number (the originator is the right-most AS in the path). The AS_PATH attribute is a space-delimited list, so a space between the leading AS numbers (.*) and the originating AS (65535) is required. Verify that the as-path access list is referenced by the filter-list inbound for the appropriate BGP neighbors. [edit protocols bgp] group eBGP { neighbor <address> { import bgp_originate_65535; } } If the router is not configured to reject updates from CE routers with an originating AS in the AS_PATH attribute that does not belong to that customer, this is a finding.

## Group: SRG-NET-000019-RTR-000001

**Group ID:** `V-253983`

### Rule: The Juniper router must be configured to disable the auxiliary port unless it is connected to a secured modem providing encryption and authentication.

**Rule ID:** `SV-253983r843982_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of POTS lines to modems connecting to network devices provides clear text of authentication traffic over commercial circuits that could be captured and used to compromise the network. Additional war dial attacks on the device could degrade the device and the production network. Secured modem devices must be able to authenticate users and must negotiate a key exchange before full encryption takes place. The modem will provide full encryption capability (Triple DES) or stronger. The technician who manages these devices will be authenticated using an authorized MFA token and granted access to the appropriate maintenance port; thus, the technician will gain access to the managed device (router, switch, etc.). The token provides a method of strong (two-factor) user authentication. The token works in conjunction with a server to generate one-time user passwords. The user must know a personal identification number (PIN) and possess the token to be allowed access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration and verify that the auxiliary port is disabled unless a secured modem providing encryption and authentication is connected to it. The Junos auxiliary port is disabled by default. Verify the auxiliary port is not configured (there will be no [edit system ports auxiliary] stanza) or that the auxiliary port is explicitly disabled. [edit system ports] auxiliary { disable; } If the auxiliary port is not disabled or is not connected to a secured modem when it is enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000002

**Group ID:** `V-253984`

### Rule: The Juniper router must be configured to enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy.

**Rule ID:** `SV-253984r843985_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates authorized information to travel within a network and between interconnected networks. Controlling the flow of network traffic is critical so it does not introduce any unacceptable risk to the network infrastructure or data. An example of a flow control restriction is blocking outside traffic claiming to be from within the organization. For most routers, internal information flow control is a product of system design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each router enforces approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy. Junos enforces information flow via stateless firewall filters and unicast Reverse Path Forwarding (uRPF). uRPF performs a forwarding table lookup to validate the incoming packet's source address is appropriate for the arriving interface. Verify uRPF is enabled on applicable interfaces. The example shows uRPF and the stateless firewall filter applied. Verify the interface and assigned addresses are appropriate for the target environment. [edit interfaces] <interface name> { unit <logical unit number> { family inet { rpf-check; filter { input deny-prod-to-mgt; } } family inet6 { rpf-check; filter { input deny-prod-to-mgt-v6; } } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. [edit firewall] family inet { filter deny-prod-to-mgt { term 1 { from { source-address { <production IPv4 subnet/mask>; } destination-address { <MGT IPv4 subnet/mask>; } } then { log; syslog; discard; } } term 2 { from { source-address { <production IPv4 subnet/mask>; } } then accept; } } } family inet6 { filter deny-prod-to-mgt-v6 { term 1 { from { source-address { <production IPv6 subnet/prefix>; } destination-address { <MGT IPv6 subnet/prefix>; } } then { log; syslog; discard; } } term 2 { from { source-address { <production IPv6 subnet/prefix>; } } then accept; } } } If the router does not enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-253985`

### Rule: The Juniper router must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-253985r843988_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DoD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some routers and passing through some routers to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and thereby know which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IPv4 or IPv6 multicast routing is enabled, verify all interfaces enabled for PIM are documented in the network's multicast topology diagram. Review the router configuration to determine if multicast routing is enabled and which interfaces are enabled for PIM. By default, PIM is not enabled on any interface. If not a PIM router, verify there is no PIM stanza at [edit protocols], PIM is disabled globally and/or for all interfaces, or that the stanza is inactive. [edit protocols] inactive: pim { << Stanza is removed or marked inactive disable; << If stanza is present and not inactive, verify globally disabled interface all { << If stanza is present, not inactive, and not globally disabled, disable for all interfaces disable; } } For PIM routers, verify only the required interfaces are configured. For example, the following configuration enables PIM on a specific interface and disables PIM for all others. [edit protocols] pim { interface <name>.<logical unit>; interface all { disable; } } Note: More specific interface configuration statements are preferred. In the example, the interface configuration is more specific than interface "all", so PIM is enabled only on that interface. If an interface is not required to support multicast routing and it is enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-253986`

### Rule: The Juniper router must be configured to bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-253986r843991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PIM is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. PIM traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, unauthorized routers can join the PIM domain, discover and use the rendezvous points, and also advertise their rendezvous points into the domain. This can result in a denial of service by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the multicast topology diagram and determine if router interfaces are enabled for IPv4 or IPv6 multicast routing. By default, PIM is not enabled on any interface. If not a PIM router, verify there is no PIM stanza at [edit protocols], PIM is disabled globally and/or for all interfaces, or that the stanza is inactive. [edit protocols] inactive: pim { << Stanza is removed or marked inactive disable; << If stanza is present and not inactive, verify globally disabled interface all { << If stanza is present, not inactive, and not globally disabled, disable for all interfaces disable; } } For PIM routers, verify only the required interfaces are configured. For example, the following configuration enables PIM on a specific interface and disables PIM for all others. [edit protocols] pim { interface <name>.<logical unit>; interface all { disable; } } Note: More specific interface configuration statements are preferred. In the example, the interface configuration is more specific than interface "all", so PIM is enabled only on that interface. If the router is enabled for multicast routing, verify all interfaces enabled for PIM have a neighbor filter bound to the interface. The neighbor filter must only accept PIM control plane traffic from the documented PIM neighbors. [edit policy-options] prefix-list PIM-NEIGHBOR-1 { <PIM neighbor address>/32; } <additional PIM neighbor lists> policy-statement PIM-NBR-1 { from { prefix-list PIM-NEIGHBOR-1; } then accept; } <additional policies> [edit protocols pim] interface <interface name>.<logical unit> { mode sparse; neighbor-policy PIM-NBR1; } interface all { disable; } If PIM neighbor filters are not bound to all interfaces that have PIM enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-253987`

### Rule: The Juniper multicast edge router must be configured to establish boundaries for administratively scoped multicast traffic.

**Rule ID:** `SV-253987r843994_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify that admin-scope multicast traffic is blocked at the external edge. Verify either a scope is defined for specific interfaces or a scope policy is applied. [edit routing-options multicast] scope <name IPv4> { prefix 239.0.0.0/8; interface [ <external interface 1> <external interface 2> ]; } scope <name IPv6> { prefix ff08::/16; interface [ <external interface 1> <external interface 2> ]; } -or- [edit policy-options] policy-statement <name> { term 1 { from { route-filter 239.0.0.0/8 orlonger; route-filter ff08::/16 orlonger; } then reject; } } [edit routing-options multicast] scope-policy <policy name> If the router is not configured to establish boundaries for administratively scoped multicast traffic, this is a finding.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-253988`

### Rule: The Juniper router must be configured to have all inactive interfaces disabled.

**Rule ID:** `SV-253988r843997_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use. If an interface is no longer used, the configuration must be deleted and the interface disabled. For logical interfaces, delete those that are on inactive interfaces and delete logical interfaces that are themselves inactive. If the logical interface is no longer necessary for authorized communications, it must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify unused interfaces are not configured (implicitly disabled) or are explicitly disabled. If explicitly disabling interfaces, verify multiple interfaces are disabled with the "interface-range" command or separately at each interface declaration. [edit interfaces] interface-range DISABLED_INTERFACES { member <interface name>; member-range <first interface> to <last interface>; disable; } <interface name> { disable; } Note: Individually disabled interfaces should not be included in any "interface-range" stanza. The "member-range" directive assigns the configured parameter(s) to contiguously numbered interfaces. Junos lists interfaces in order so a "missing" interface is not enabled. For instance, if ge-0/0/0 and ge-0/0/2 are configured, but there is no individual ge-0/0/1 stanza and that interface is not a member of an interface-range, then ge-0/0/1 is implicitly disabled. If an interface is not being used but is configured or enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000008

**Group ID:** `V-253989`

### Rule: The Juniper perimeter router must be configured to protect an enclave connected to an alternate gateway by using an inbound filter that only permits packets with destination addresses within the site's address space.

**Rule ID:** `SV-253989r844000_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Enclaves with alternate gateway connections must take additional steps to ensure there is no compromise on the enclave network or NIPRNet. Without verifying the destination address of traffic coming from the site's alternate gateway, the perimeter router could be routing transit data from the internet into the NIPRNet. This could also make the perimeter router vulnerable to a denial-of-service (DoS) attack as well as provide a back door into the NIPRNet. The DoD enclave must ensure the ingress filter applied to external interfaces on a perimeter router connecting to an Approved Gateway is secure through filters permitting packets with a destination address belonging to the DoD enclave's address block.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration of each router interface connecting to an alternate gateway. Verify each permit statement of the ingress filter only permits packets with destination addresses of the site's NIPRNet address space or a destination address belonging to the address block assigned by the alternate gateway network service provider. Verify each permit statement "from" stanza (filter match conditions) references either the "destination-address" or "destination-prefix-list" directive. Using prefix lists makes management easier because managing interior addresses must only be configured in one location (the prefix-list) vice many locations (each permitting filter term). For example: [edit policy-options] prefix-list inside_addresses-ipv4 { <IPv4 subnet / mask>; } prefix-list inside_addresses-ipv6 { <IPv6 subnet / prefix>; } [edit firewall] family inet { filter inbound-ipv4 { <deny terms>; permit-term1 { from { <match conditions>; destination-prefix-list inside_addresses-ipv4; } then accept; } <additional permit terms with a destination address definition> } } family inet6 { filter inbound-ipv6 { <deny terms>; permit-term1 { from { <match conditions>; destination-prefix-list inside_addresses-ipv6; } then accept; } <additional permit terms with a destination address definition> } } Verify the filter is applied inbound on exterior-facing interfaces. For example: [edit interfaces] <interface name> { unit <number> { family inet { filter { input inbound-ipv4; } address <IPv4 address / mask>; } family inet6 { filter { input inbound-ipv6; } address <IPv6 address / prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. If the ingress filter permits packets with addresses other than those specified, such as destination addresses of the site's NIPRNet address space or a destination address belonging to the address block assigned by the alternate gateway network service provider, this is a finding.

## Group: SRG-NET-000019-RTR-000009

**Group ID:** `V-253990`

### Rule: The Juniper perimeter router must not be configured to be a Border Gateway Protocol (BGP) peer to an alternate gateway service provider.

**Rule ID:** `SV-253990r844003_rule`
**Severity:** high

**Description:**
<VulnDiscussion>ISPs use BGP to share route information with other autonomous systems (i.e., other ISPs and corporate networks). If the perimeter router was configured to BGP peer with an ISP, NIPRNet routes could be advertised to the ISP; thereby creating a backdoor connection from the internet to the NIPRNet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration of the router connecting to the alternate gateway. Review the [edit protocols bgp] hierarchy and verify there are no BGP neighbors configured to the remote AS that belongs to the alternate gateway service provider. For example: [edit protocols bgp] group eBGP { type external; peer-as 2; neighbor <address-1> { <bgp neighbor configuration>; } neighbor <address-2> { <bgp neighbor configuration>; } } Note: Neither neighbor can belong to a peer AS belonging to the alternate gateway service provider. Verify static routing to the peer AS belonging to the alternate gateway service provider. For example: [edit routing-options] rib inet6.0 { static { route <peer AS IPv6 subnet>/<prefix> next-hop <peer AS router>; } } static { route <peer AS IPv4 subnet>/<mask> next-hop <peer AS router>; } If there are BGP neighbors connecting the remote AS of the alternate gateway service provider, this is a finding.

## Group: SRG-NET-000019-RTR-000010

**Group ID:** `V-253991`

### Rule: The Juniper perimeter router must not be configured to redistribute static routes to an alternate gateway service provider into BGP or an IGP peering with the NIPRNet or to other autonomous systems.

**Rule ID:** `SV-253991r844006_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the static routes to the alternate gateway are being redistributed into an Exterior Gateway Protocol or Interior Gateway Protocol to a NIPRNet gateway, this could make traffic on NIPRNet flow to that particular router and not to the Internet Access Point routers. This could not only wreak havoc with traffic flows on NIPRNet, but it could overwhelm the connection from the router to the NIPRNet gateway(s) and also cause traffic destined for outside of NIPRNet to bypass the defenses of the Internet Access Points.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the configuration of the router connecting to the alternate gateway and verify that redistribution of static routes to the alternate gateway is not occurring. Juniper routers use export policies to limit redistribution of routes. Verify a policy exists to filter route redistribution. [edit policy-options] policy-statement <name> { term 1 { from protocol static; then reject; } } Verify the export policy is applied to the EGP and/or IGP protocol. [edit protocols] bgp { export <policy-name>; group <group name> { type external; export <policy-name>; neighbor <address> { export <policy-name>; } } ospf { export <policy name>; } ospf3 { export <policy name>; } } Note: BGP supports export statements at the protocol level (global), the group level, and the neighbor level. Only the most specific policy is applied. If the static routes to the alternate gateway are being redistributed into BGP or any IGP peering with a NIPRNet gateway or another autonomous system, this is a finding.

## Group: SRG-NET-000019-RTR-000011

**Group ID:** `V-253992`

### Rule: The Juniper out-of-band management (OOBM) gateway router must be configured to have separate IGP instances for the managed network and management network.

**Rule ID:** `SV-253992r844009_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, implementation of several safeguards for containment of management and production traffic boundaries must occur. Since the managed and management network are separate routing domains, configuration of separate Interior Gateway Protocol routing instances is critical on the router to segregate traffic from each network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify that the OOBM interface is an adjacency in the Interior Gateway Protocol routing domain for the management network. Interfaces can only be assigned to one routing instance. [edit protocols ospf] interface <interface name>.<logical unit>; << Cannot be assigned to a virtual routing instance. [edit routing-instances] <name> { instance-type virtual-router; protocols { ospf { area <area number> { interface <interface name>.<logical unit>; << Cannot be assigned to the default routing instance at [edit protocols]. } } } } Note: If the same interface is assigned to the default routing instance and to a virtual routing instance, commit fails. Some platforms support a routing-instance using the reserved name "mgmt_junos". On these platforms, configure the "mgmt_junos" instance and apply at the [edit system] hierarchy. [edit system] management-instance; [edit routing-instances] mgmt_junos { routing-options { static { route 0.0.0.0/0 next-hop <next-hop address>; } } } Note: Not all platforms support routing instances. If the router does not enforce that Interior Gateway Protocol instances configured on the OOBM gateway router peer only with their own routing domain, this is a finding.

## Group: SRG-NET-000019-RTR-000012

**Group ID:** `V-253993`

### Rule: The Juniper out-of-band management (OOBM) gateway router must not be configured to redistribute routes between the management network routing domain and the managed network routing domain.

**Rule ID:** `SV-253993r844012_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, several safeguards must be implemented for containment of management and production traffic boundaries; otherwise, it is possible that management traffic will not be separated from production traffic. Since the managed network and the management network are separate routing domains, separate Interior Gateway Protocol routing instances must be configured on the router, one for the managed network and one for the OOBM network. In addition, the routes from the two domains must not be redistributed to each other.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify the Interior Gateway Protocol instance used for the managed network does not redistribute routes into the Interior Gateway Protocol instance used for the management network, and vice versa. Juniper routers use export policies to limit redistribution of routes. Verify a policy exists to filter route redistribution. Juniper policy-statements support terms, which provides greater granularity within a single policy. [edit policy-options] policy-statement deny-mgt-redist { term 1 { from protocol static; then reject; } term 2 { from { protocol ospf; route-filter <IPv4 subnet>/<mask> orlonger; route-filter <IPv6 subnet>/<prefix> orlonger; } then reject; } <additional terms permitting authorized routes for redistribution> } policy-statement deny-managed-routes { term 1 { from { route-filter <IPv4 subnet>/<mask> orlonger; route-filter <IPv6 subnet>/<prefix> orlonger; } then accept; } term 2 { then reject; } } Verify an export policy is applied to the IGP protocol for each routing instance (default and OOBM). [edit protocols] ospf { area <area number> { interface <NOT OOBM interface>.<logical unit>; } export deny-mgt-redist; } ospf3 { area <area number> { interface <NOT OOBM interface>.<logical unit>; } export deny-mgt-redist; } } [edit routing-instances] OOBM { instance-type virtual-router; protocols { ospf { area <area number> { interface <OOBM interface>.<logical unit>; } export deny-managed-routes; } ospf3 { area <area number> { interface <OOBM interface>.<logical unit>; } export deny-managed-routes; } } } If the Interior Gateway Protocol instance used for the managed network redistributes routes into the Interior Gateway Protocol instance used for the management network, or vice versa, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-253994`

### Rule: The Juniper multicast Rendezvous Point (RP) router must be configured to filter Protocol Independent Multicast (PIM) Register messages received from the Designated Router (DR) for any undesirable multicast groups and sources.

**Rule ID:** `SV-253994r844015_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that register messages are accepted only for authorized multicast groups and sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP router is configured to filter PIM register messages from unauthorized multicast groups and sources. [edit policy-options] policy-statement <name> { term filter_groups { from { route-filter <multicast address>/<mask> orlonger; route-filter <multicast address>/<mask> exact; <additional groups to filter> } then reject; } term filter_sources { from { source-address-filter <source host address>/32 exact; source-address-filter <source subnet address>/<mask> orlonger; <additional source addresses to filter> } then reject; } term accept_others { then accept; } } [edit protocols pim] rp { rp-register-policy <policy name>; } If the RP router peering with PIM-SM routers is not configured with a PIM import policy to block registration messages for any undesirable multicast groups and sources, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-253995`

### Rule: The Juniper multicast Rendezvous Point (RP) router must be configured to filter Protocol Independent Multicast (PIM) Join messages received from the Designated Router (DR) for any undesirable multicast groups.

**Rule ID:** `SV-253995r844018_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that join messages are only accepted for authorized multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP router is configured to filter PIM register messages. [edit policy-options] policy-statement <name> { term filter_groups { from { route-filter <multicast address>/<mask> orlonger; route-filter <multicast address>/<mask> exact; <additional groups to filter> } then reject; } term filter_sources { from { source-address-filter <source host address>/32 exact; source-address-filter <source subnet address>/<mask> orlonger; <additional source addresses to filter> } then reject; } term accept_others { then accept; } } [edit protocols] pim { mode sparse; import <policy name>; } Note: Alternative is to verify all designated routers are filtering IGMP Membership Report (a.k.a., join) messages received from hosts. If the RP router peering with PIM-SM routers is not configured with a PIM import policy to block registration messages for any undesirable multicast groups and Bogon sources, this is a finding.

## Group: SRG-NET-000076-RTR-000001

**Group ID:** `V-253996`

### Rule: The Juniper router must be configured to produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-253996r844021_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as router components, modules, device identifiers, node names, and functionality. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The router must log all packets that have been dropped via the stateless firewall filter. Verify all discarding firewall filter terms are configured to send events to syslog. Note: Stateless firewall filters support "log" and "syslog" actions. The "log" action maintains a temporary list of events and the "syslog" action generates events for local storage and/or external syslog servers. Verify at least "syslog" is associated with all discarding terms. For example: [edit firewall] family inet { filter <filter name> { term 1 { from { <match conditions>; } then { log; syslog; <<< At a minimum, the 'syslog' action must be enabled for all discarding terms. discard; } } } } family inet6 { filter <filter name> { term 1 { from { <match conditions>; } then { log; syslog; <<< At a minimum, the 'syslog' action must be enabled for all discarding terms. discard; } } } } If the router fails to log all packets that have been dropped via the firewall filter, this is a finding. Verify logging is enabled for local and/or external syslog. To meet this requirement, either the "any" or the "firewall" logging facility must be enabled. Note: To reduce log sizes and to segregate entries, a separate log file for firewall entries is permissible. [edit system syslog] host <external syslog address> { any info; log-prefix <hostname>; explicit-priority; } file messages { any info; } time-format year; Log output must contain an interface name identifying where the packet was filtered. Note: Logged firewall events include the interface and cannot be configured otherwise. There is no provision for changing the log message or for removing the interface name. If the logged output does not contain an interface name identifying where the packet was filtered, this is a finding.

## Group: SRG-NET-000077-RTR-000001

**Group ID:** `V-253997`

### Rule: The Juniper router must be configured to produce audit records containing information to establish the source of the events.

**Rule ID:** `SV-253997r844024_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis, security personnel need to know the source of the event. In addition to logging where events occur within the network, the audit records must also identify sources of events such as IP addresses, processes, and node or device names.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The router must log all packets that have been dropped via the stateless firewall filter. Verify all discarding firewall filter terms are configured to send events to syslog. Note: Stateless firewall filters support "log" and "syslog" actions. The "log" action maintains a temporary list of events and the "syslog" action generates events for local storage and/or external syslog servers. Verify at least "syslog" is associated with all discarding terms. For example: [edit firewall] family inet { filter <filter name> { term 1 { from { <match conditions>; } then { log; syslog; <<< At a minimum, the 'syslog' action must be enabled for all discarding terms. discard; } } } } family inet6 { filter <filter name> { term 1 { from { <match conditions>; } then { log; syslog; <<< At a minimum, the 'syslog' action must be enabled for all discarding terms. discard; } } } } If the router fails to log all packets that have been dropped via the firewall filter, this is a finding. Verify logging is enabled for local and/or external syslog. To meet this requirement, either the "any" or the "firewall" logging facility must be enabled. Note: To reduce log sizes and to segregate entries, a separate log file for firewall entries is permissible. [edit system syslog] host <external syslog address> { any info; log-prefix <hostname>; explicit-priority; } file messages { any info; } time-format year; Log output must contain the source IP address and port of the filtered packets. Note: Logged firewall events include the source, and destination, addresses and cannot be configured otherwise. There is no provision for changing the log message or for removing the source or destination address. If the logged output does not contain source IP address and port of the filtered packets, this is a finding.

## Group: SRG-NET-000078-RTR-000001

**Group ID:** `V-253998`

### Rule: The Juniper router must be configured to log all packets that have been dropped.

**Rule ID:** `SV-253998r844027_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being done or attempted to be done, and by whom, to compile an accurate risk assessment. Auditing the actions on network devices provides a means to recreate an attack or identify a configuration mistake on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router interface firewall filters to verify all deny statements are logged. At a minimum, all discarding filter terms must have the "syslog" action enabled. Verify all discarding firewall filter terms are configured with (minimally) the "syslog" action: [edit firewall] family inet { filter <filter name> { term <name> { from { <match conditions>; } then { log; syslog; <<< Must be enabled for local and external syslog. discard; } } } } family inet6 { filter <filter name> { term <name> { from { <match conditions>; } then { log; syslog; <<< Must be enabled for local and external syslog. discard; } } } } If packets being dropped are not logged, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-253999`

### Rule: The Juniper router must be configured to have all nonessential capabilities disabled.

**Rule ID:** `SV-253999r844030_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if services or functions not required for operation, or not related to router functionality (e.g., DNS, email client or server, FTP server, or web server) are enabled. By default, unnecessary services like finger, telnet, TFTP and FTP are not enabled and will not be listed at [edit system services]. For example, the following services should NOT be enabled as shown: [edit system services] finger; ftp; rlogin; telnet; tftp-server; web-management; Note: If the services listed above are marked "inactive", they are not enabled. If unnecessary services and functions are enabled on the router, this is a finding.

## Group: SRG-NET-000131-RTR-000083

**Group ID:** `V-254000`

### Rule: The Juniper router must not be configured to have any feature enabled that calls home to the vendor.

**Rule ID:** `SV-254000r844033_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Call home services will routinely send data such as configuration and diagnostic information to the vendor for routine or emergency analysis and troubleshooting. There is a risk that transmission of sensitive data sent to unauthorized persons could result in data loss or downtime due to an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the call home service is disabled on the device. Verify [edit system] does NOT contain a phone-home hierarchy as shown: [edit system] host-name <hostname>; : <other system configuration> : phone-home { server https://<applicable URL>; rfc-compliant; } If a call home service is enabled, this is a finding.

## Group: SRG-NET-000168-RTR-000077

**Group ID:** `V-254001`

### Rule: The Juniper router must be configured to use encryption for routing protocol authentication.

**Rule ID:** `SV-254001r844036_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration. For every protocol that affects the routing or forwarding tables (where information is exchanged between neighbors), verify that neighbor router authentication is encrypting the authentication key. [edit protocols] ospf { area <area number> { interface <interface name>.<logical unit> { authentication { md5 1 key "$8$aes256-gcm$hmac-sha2-256$100$hvt9Fpk6EEU$I2FKFJNrdKHpp1xesMB0aA$l9BsHxOYO4+B8f7erRj8Hw$A9PYzx53Ius"; ## SECRET-DATA } } interface <interface name>.<logical unit> { ipsec-sa <SA name>; } } } ospf3 { area <area number> { interface <interface name>.<logical unit> { ipsec-sa <SA name>; } } } Note: OSPFv3 only supports IPsec SA authentication; OSPFv2 supports both IPsec SA and MD5 authentication. MD5 authentication is only included to support devices that do not support IPsec SA authentication. Verify the OSPFv3 SA. [edit security ipsec] security-association <SA name> { mode transport; manual { direction bidirectional { protocol (ah | esp | bundle); spi (256..16639); <<< The SPI is an integer value that must match the peer encryption { algorithm (hmac-sha1-96 | hmac-sha-256-128); key hexadecimal "$8$aes256-gcm$hmac-sha2-256$100$QAP67/2oV/s$nz+2A3zRz40fwxMJdbbA0Q$R5A/koX36OvUWBB543QwAA$tQrR3fkCL2oQ3V1O2Tw2lYl7THNuqBQ6hpyi8naLlXMaKQM0SdJYefQU41rB3zpjisVIWBwS+S8+O146luRf3Q"; ## SECRET-DATA } } } } Note: OSPFv3 SA uses manual transport mode encapsulating security payload (ESP) associations. If authentication is not encrypting the authentication key, this is a finding.

## Group: SRG-NET-000168-RTR-000078

**Group ID:** `V-254002`

### Rule: The Juniper router must be configured to authenticate all routing protocol messages using NIST-validated FIPS 198-1 message authentication code algorithm.

**Rule ID:** `SV-254002r904444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. However, using clear-text authentication provides little benefit since an attacker can intercept traffic and view the authentication key. This would allow the attacker to use the authentication key in an attack. Since MD5 is vulnerable to "birthday" attacks and may be compromised, routing protocol authentication must use FIPS 198-1 validated algorithms and modules to encrypt the authentication key. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols. IP Security (IPsec) Security Association (SA) routing protocol authentication provides strong protection against unauthorized ("rogue") routing updates. IPsec SAs offer Authentication Header (AH) or Encapsulated Security Payload (ESP) to protect the routing updates. IPsec SA is required by newer routing protocols like OSPFv3 for authentication. IPsec SA routing protocol authentication supports FIPS 198-1 validated algorithms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify routing protocol authentication is enabled using a FIPS 198-1 validated hashed message authentication code (HMAC). For protocols supporting IPsec SA: [edit security ipsec] security-association <SA name> { <snip> NOTE: Versions of Junos not supporting RFC5709 must be configured to use MD5 authentication, but this is still a CAT III finding since MD5 is not compliant. For protocols not supporting IPsec SA (OSPFv2 example shown) [edit protocols ospf] area <area number> { interface <name> { authentication { <algorithm> <key number> key “<hashed value>”; } } } If a NIST-validated FIPS 198-1 message authentication code algorithm is not being used to authenticate routing protocols, this is a finding. Routing protocols using authentication with non-NIST-validated FIPS 198-1 algorithms may be downgraded to CAT III.

## Group: SRG-NET-000192-RTR-000002

**Group ID:** `V-254003`

### Rule: The Juniper PE router must be configured to limit the number of MAC addresses it can learn for each Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-254003r844042_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VPLS defines an architecture that delivers Ethernet multipoint services over an MPLS network. Customer layer 2 frames are forwarded across the MPLS core via pseudowires using IEEE 802.1q Ethernet bridging principles. A pseudowire is a virtual bidirectional connection between two attachment circuits (virtual connections between PE and CE routers). A pseudowire contains two unidirectional label-switched paths (LSP). Each MAC forwarding table instance is interconnected using domain-specific LSPs, thereby maintaining privacy and logical separation between each VPLS domain. When a frame arrives on a bridge port (pseudowire or attachment circuit) and the source MAC address is unknown to the receiving PE router, the source MAC address is associated with the pseudowire or attachment circuit and the forwarding table is updated accordingly. Frames are forwarded to the appropriate pseudowire or attachment circuit according to the forwarding table entry for the destination MAC address. Ethernet frames sent to broadcast and unknown destination addresses must be flooded out to all interfaces for the bridge domain; hence, a PE router must replicate packets across both attachment circuits and pseudowires. A malicious attacker residing in a customer network could launch a source MAC address spoofing attack by flooding packets to a valid unicast destination, each with a different MAC source address. The PE router receiving this traffic would try to learn every new MAC address and would quickly run out of space for the VFI forwarding table. Older, valid MAC addresses would be removed from the table, and traffic sent to them would have to be flooded until the storm threshold limit is reached. Hence, it is essential that a limit is established to control the number of MAC addresses that will be learned and recorded into the forwarding table for each bridge domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE router configuration to determine if a MAC address limit has been set for each bridge domain. Verify the MAC address limit is globally defined for the VPLS protocol or at each interface assigned to the routing instance. [edit routing-instance] <instance name> { protocols { vpls { interface-mac-limit { <value>; } interface <interface name>.<logical unit> { interface-mac-limit { <value>; } } } } } Note: Only EX9200-series devices currently support VPLS. If a limit has not been configured, this is a finding.

## Group: SRG-NET-000193-RTR-000001

**Group ID:** `V-254004`

### Rule: The Juniper MPLS router with RSVP-TE enabled must be configured to enable refresh reduction features.

**Rule ID:** `SV-254004r844045_rule`
**Severity:** low

**Description:**
<VulnDiscussion>RSVP-TE can be used to perform constraint-based routing when building LSP tunnels within the network core that will support QoS and traffic engineering requirements. RSVP-TE is also used to enable MPLS Fast Reroute, a network restoration mechanism that will reroute traffic onto a backup LSP in case of a node or link failure along the primary path. When there is a disruption in the MPLS core, such as a link flap or router reboot, the result is a significant amount of RSVP signaling, such as "PathErr" and "ResvErr" messages that need to be sent for every LSP using that link. When RSVP messages are sent out, they are sent either hop by hop or with the router alert bit set in the IP header. This means that every router along the path must examine the packet to determine if additional processing is required for these RSVP messages. If there is enough signaling traffic in the network, it is possible for an interface to receive more packets for its input queue than it can hold, resulting in dropped RSVP messages and hence slower RSVP convergence. Increasing the size of the interface input queue can help prevent dropping packets; however, there is still the risk of having a burst of signaling traffic that can fill the queue. Solutions to mitigate this risk are RSVP message pacing or refresh reduction to control the rate at which RSVP messages are sent. RSVP refresh reduction includes the following features: RSVP message bundling, RSVP Message ID to reduce message processing overhead, Reliable delivery of RSVP messages using Message ID, and summary refresh to reduce the amount of information transmitted every refresh interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that the router has been configured to enable refresh reduction features. Junos OS controls RSVP refresh reduction features using two commands: aggregate: RSVP message bundling and summary refresh. reliable: RSVP message ID, reliable message delivery, and summary refresh. Starting in Junos 15.2, refresh reduction is enabled by default and the "aggregate" command is deprecated. Configuring the "aggregate" command generates a warning message in the configuration file (## Warning: "aggregate" is deprecated). On Junos earlier than 15.2, verify the "aggregate" command is enabled. On Junos 15.2 and later, no command is required. Junos earlier than 15.2: [edit protocols] rsvp { interface <interface name>.<logical unit> { aggregate; reliable; << If RSVP message ID and reliable message delivery are required. } } Junos 15.2 but pre-16.1R1: [edit protocols] rsvp { interface <interface name>.<logical unit> { reliable; << If RSVP message ID and reliable message delivery are required. } } Starting in Junos 16.1R1, all refresh reduction features are enabled by default. Verify the 'no-reliable' command is configured only if RSVP message ID and reliable message delivery are not required. To enable all refresh reduction features, no commands are necessary. Junos 16.1R1 and later: [edit protocols] rsvp { interface <interface name>.<logical unit> { <other configuration> } } If the router with RSVP-TE enabled does not have message pacing configured based on the link speed and input queue size of adjacent core routers, this is a finding.

## Group: SRG-NET-000193-RTR-000002

**Group ID:** `V-254005`

### Rule: The Juniper PE router providing Virtual Private LAN Services (VPLS) must be configured to have traffic storm control thresholds on CE-facing interfaces.

**Rule ID:** `SV-254005r844048_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a VPLS bridge, creating excessive traffic and degrading network performance. Traffic storm control prevents VPLS bridge disruption by suppressing traffic when the number of packets reaches configured threshold levels. Traffic storm control monitors incoming traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that storm control is enabled on CE-facing interfaces deploying VPLS. Verify that a stateless firewall filter has been applied to each VPLS routing instances. [edit] routing-instances { <name> { forwarding-options { family vpls { flood { input <filter name>; } } } } } Verify the filter defines traffic types associated with storm control (i.e., broadcast, multicast, and unknown unicast storms). firewall { family vpls { filter <filter name> { term <term name> { from { traffic-type broadcast; } then { policer <policer name>; accept; } } term <term name> { from { traffic-type multicast; } then { policer <policer name>; accept; } } term <term name> { from { traffic-type unknown-unicast; } then { policer <policer name>; accept; } } } } } Verify that the policer rate limits in accordance with local requirements. firewall { policer <policer name> { if-exceeding { bandwidth-limit <value>; burst-size-limit <value>; } then discard; } } Note: Only EX9200-series devices currently support VPLS. If storm control is not enabled for broadcast traffic, this is a finding.

## Group: SRG-NET-000193-RTR-000112

**Group ID:** `V-254006`

### Rule: The Juniper PE router must be configured to enforce a Quality-of-Service (QoS) policy to limit the effects of packet flooding denial-of-service (DoS) attacks.

**Rule ID:** `SV-254006r844051_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, QoS, or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and interview the System Administrator to verify that a mechanism for traffic prioritization and bandwidth reservation exists. For example: [edit class-of-service] classifiers { dscp <classifier name> { forwarding-class NC { loss-priority low code-points 110000; } forwarding-class EF { loss-priority high code-points [ 101101 101111 100101 100111 110011 ]; loss-priority low code-points [ 101000 100000 101001 101011 100001 100011 110001 ]; } forwarding-class AF41 { loss-priority high code-points [ 100010 100100 100110 ]; loss-priority low code-points [ 011000 101110 011100 011110 ]; } forwarding-class AF31 { loss-priority high code-points [ 011101 011111 011010 010101 010111 010010 001101 001010 010000 ]; loss-priority low code-points [ 001001 001011 010001 010011 011001 011011 ]; } forwarding-class BE { loss-priority high code-points 000000; } forwarding-class Default { loss-priority high code-points 001000; } forwarding-class dscp15 { loss-priority high code-points 001111; } } } Note: Some platforms apply DSCP values to both IPv4 and IPv6 traffic with a single classifier definition (as shown). Those platforms that support separating classifiers will require a "dscp-ipv6" stanza. host-outbound-traffic { forwarding-class NC; dscp-code-point 110000; } shared-buffer { ingress { percent 50; buffer-partition lossless { percent 5; } buffer-partition lossless-headroom { percent 0; } buffer-partition lossy { percent 95; } } egress { percent 100; buffer-partition lossless { percent 50; } buffer-partition lossy { percent 45; } buffer-partition multicast { percent 5; } } } Note: Some platforms only support shared-buffer percent, and cannot separate between ingress and egress. Not all devices require a shared-buffer stanza. forwarding-classes { class NC queue-num 7; class EF queue-num 6; class AF41 queue-num 5; class AF31 queue-num 4; class BE queue-num 0; class Default queue-num 1; class dscp15 queue-num 6; } traffic-control-profiles { <control profile name 1> { scheduler-map <scheduler map name 1>; shaping-rate percent 100; } <control profile name 2> { scheduler-map <scheduler map name 2>; guaranteed-rate percent 20; } } forwarding-class-sets { <set name 1> { class NC; class EF; class AF41; class AF31; class Default; class dscp15; } <set name 2> { class BE; } } interfaces { <interface name> { forwarding-class-set { <set name 1> { output-traffic-control-profile <control profile name 1>; } <set name 2> { output-traffic-control-profile <control profile name 2>; } } classifiers { dscp <classifier name>; } rewrite-rules { dscp <rewrite rule name>; } } } rewrite-rules { dscp <rewrite rule name> { forwarding-class dscp15 { loss-priority high code-point 101101; } forwarding-class EF { loss-priority low code-point 110001; } forwarding-class AF41 { loss-priority high code-point 100110; } forwarding-class NC { loss-priority low code-point 110000; } forwarding-class AF31 { loss-priority high code-point 010000; } forwarding-class Default { loss-priority high code-point 001000; } } } Note: Some platforms require rewriting all DSCP values if rewriting one (smaller platforms). Most support only rewriting a single DSCP value, which would eliminate all but one rewrite rule. scheduler-maps { <scheduler map name 1> { forwarding-class NC scheduler NC; forwarding-class EF scheduler EF; forwarding-class AF41 scheduler AF41; forwarding-class AF31 scheduler AF31; forwarding-class Default scheduler Default; } <scheduler map name 2> { forwarding-class BE scheduler BE; } } schedulers { NC { buffer-size percent 5; priority strict-high; } EF { shaping-rate percent 20; buffer-size percent 19; priority strict-high; } AF41 { shaping-rate percent 15; buffer-size percent 14; priority strict-high; } AF31 { shaping-rate percent 31; buffer-size percent 29; priority strict-high; } BE { transmit-rate percent 20; buffer-size percent 20; priority low; } Default { shaping-rate percent 10; buffer-size percent 9; priority strict-high; } } This arrangement must ensure that sufficient capacity is available for mission-critical traffic and enforce the traffic priorities specified by the Combatant Commands/Services/Agencies. If no such scheme exists or it is not configured, this is a finding.

## Group: SRG-NET-000193-RTR-000113

**Group ID:** `V-254007`

### Rule: The Juniper PE router must be configured to enforce a Quality-of-Service (QoS) policy in accordance with the QoS DODIN Technical Profile.

**Rule ID:** `SV-254007r844054_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify that a QoS policy has been configured to provide preferred treatment for mission-critical applications in accordance with the QoS GIG Technical Profile. Verify that the classifiers are configured to match on DSCP. Note: Juniper routers also support classifying on MPLS EXP and IEEE 802.1 values. Verify that the schedulers are configured to set DSCP values for the defined classifiers in accordance with the QoS GIG Technical Profile. Verify that forwarding class sets or scheduler maps are applied all interfaces. Note: The GTP QOS document (GTP-0009) can be downloaded via the following link: https://intellipedia.intelink.gov/wiki/Portal:GIG_Technical_Guidance/GTG_GTPs/GTP_Development_List To classify on L4 ports or protocols, use stateless firewall filters to direct matched traffic into the required forwarding class. [edit class-of-service] classifiers { dscp <classifier name> { forwarding-class NC { loss-priority low code-points 110000; } forwarding-class EF { loss-priority high code-points [ 101101 101111 100101 100111 110011 ]; loss-priority low code-points [ 101000 100000 101001 101011 100001 100011 110001 ]; } forwarding-class AF41 { loss-priority high code-points [ 100010 100100 100110 ]; loss-priority low code-points [ 011000 101110 011100 011110 ]; } forwarding-class AF31 { loss-priority high code-points [ 011101 011111 011010 010101 010111 010010 001101 001010 010000 ]; loss-priority low code-points [ 001001 001011 010001 010011 011001 011011 ]; } forwarding-class BE { loss-priority high code-points 000000; } forwarding-class Default { loss-priority high code-points 001000; } forwarding-class dscp15 { loss-priority high code-points 001111; } } } Note: Some platforms apply DSCP values to both IPv4 and IPv6 traffic with a single classifier definition (as shown). Those platforms that support separating classifiers will require a "dscp-ipv6" stanza. host-outbound-traffic { forwarding-class NC; dscp-code-point 110000; } shared-buffer { ingress { percent 50; buffer-partition lossless { percent 5; } buffer-partition lossless-headroom { percent 0; } buffer-partition lossy { percent 95; } } egress { percent 100; buffer-partition lossless { percent 50; } buffer-partition lossy { percent 45; } buffer-partition multicast { percent 5; } } } Note: Some platforms only support shared-buffer percent, and cannot separate between ingress and egress. Not all devices require a shared-buffer stanza. forwarding-classes { class NC queue-num 7; class EF queue-num 6; class AF41 queue-num 5; class AF31 queue-num 4; class BE queue-num 0; class Default queue-num 1; class dscp15 queue-num 6; } traffic-control-profiles { <control profile name 1> { scheduler-map <scheduler map name 1>; shaping-rate percent 100; } <control profile name 2> { scheduler-map <scheduler map name 2>; guaranteed-rate percent 20; } } forwarding-class-sets { <set name 1> { class NC; class EF; class AF41; class AF31; class Default; class dscp15; } <set name 2> { class BE; } } interfaces { <interface name> { forwarding-class-set { <set name 1> { output-traffic-control-profile <control profile name 1>; } <set name 2> { output-traffic-control-profile <control profile name 2>; } } classifiers { dscp <classifier name>; } rewrite-rules { dscp <rewrite rule name>; } } } rewrite-rules { dscp <rewrite rule name> { forwarding-class dscp15 { loss-priority high code-point 101101; } forwarding-class EF { loss-priority low code-point 110001; } forwarding-class AF41 { loss-priority high code-point 100110; } forwarding-class NC { loss-priority low code-point 110000; } forwarding-class AF31 { loss-priority high code-point 010000; } forwarding-class Default { loss-priority high code-point 001000; } } } Note: Some platforms require rewriting all DSCP values if rewriting one (smaller platforms). Most support only rewriting a single DSCP value, which would eliminate all but one rewrite rule. scheduler-maps { <scheduler map name 1> { forwarding-class NC scheduler NC; forwarding-class EF scheduler EF; forwarding-class AF41 scheduler AF41; forwarding-class AF31 scheduler AF31; forwarding-class Default scheduler Default; } <scheduler map name 2> { forwarding-class BE scheduler BE; } } schedulers { NC { buffer-size percent 5; priority strict-high; } EF { shaping-rate percent 20; buffer-size percent 19; priority strict-high; } AF41 { shaping-rate percent 15; buffer-size percent 14; priority strict-high; } AF31 { shaping-rate percent 31; buffer-size percent 29; priority strict-high; } BE { transmit-rate percent 20; buffer-size percent 20; priority low; } Default { shaping-rate percent 10; buffer-size percent 9; priority strict-high; } } If the router is not configured to implement a QoS policy in accordance with the QoS GIG Technical Profile, this is a finding.

## Group: SRG-NET-000193-RTR-000114

**Group ID:** `V-254008`

### Rule: The Juniper P router must be configured to enforce a Quality-of-Service (QoS) policy in accordance with the QoS GIG Technical Profile.

**Rule ID:** `SV-254008r844057_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration and verify that a QoS policy has been configured to provide preferred treatment for mission-critical applications in accordance with the QoS GIG Technical Profile. Verify that the classifiers are configured to match on DSCP. Note: Juniper routers also support classifying on MPLS EXP and IEEE 802.1 values. Verify that the schedulers are configured to set DSCP values for the defined classifiers in accordance with the QoS GIG Technical Profile. Verify that classifiers are applied all interfaces. Note: The GTP QOS document (GTP-0009) can be downloaded via the following link: https://intellipedia.intelink.gov/wiki/Portal:GIG_Technical_Guidance/GTG_GTPs/GTP_Development_List To classify on L4 ports or protocols, use stateless firewall filters to direct matched traffic into the required forwarding class. [edit class-of-service] classifiers { dscp <classifier name> { forwarding-class NC { loss-priority low code-points 110000; } forwarding-class EF { loss-priority high code-points [ 101101 101111 100101 100111 110011 ]; loss-priority low code-points [ 101000 100000 101001 101011 100001 100011 110001 ]; } forwarding-class AF41 { loss-priority high code-points [ 100010 100100 100110 ]; loss-priority low code-points [ 011000 101110 011100 011110 ]; } forwarding-class AF31 { loss-priority high code-points [ 011101 011111 011010 010101 010111 010010 001101 001010 010000 ]; loss-priority low code-points [ 001001 001011 010001 010011 011001 011011 ]; } forwarding-class BE { loss-priority high code-points 000000; } forwarding-class Default { loss-priority high code-points 001000; } forwarding-class dscp15 { loss-priority high code-points 001111; } } } Note: Some platforms apply DSCP values to both IPv4 and IPv6 traffic with a single classifier definition (as shown). Those platforms that support separating classifiers will require a "dscp-ipv6" stanza. host-outbound-traffic { forwarding-class NC; dscp-code-point 110000; } shared-buffer { ingress { percent 50; buffer-partition lossless { percent 5; } buffer-partition lossless-headroom { percent 0; } buffer-partition lossy { percent 95; } } egress { percent 100; buffer-partition lossless { percent 50; } buffer-partition lossy { percent 45; } buffer-partition multicast { percent 5; } } } Note: Some platforms only support shared-buffer percent, and cannot separate between ingress and egress. Not all devices require a shared-buffer stanza. forwarding-classes { class NC queue-num 7; class EF queue-num 6; class AF41 queue-num 5; class AF31 queue-num 4; class BE queue-num 0; class Default queue-num 1; class dscp15 queue-num 6; } traffic-control-profiles { <control profile name 1> { scheduler-map <scheduler map name 1>; shaping-rate percent 100; } <control profile name 2> { scheduler-map <scheduler map name 2>; guaranteed-rate percent 20; } } forwarding-class-sets { <set name 1> { class NC; class EF; class AF41; class AF31; class Default; class dscp15; } <set name 2> { class BE; } } interfaces { <interface name> { forwarding-class-set { <set name 1> { output-traffic-control-profile <control profile name 1>; } <set name 2> { output-traffic-control-profile <control profile name 2>; } } classifiers { dscp <classifier name>; } rewrite-rules { dscp <rewrite rule name>; } } } rewrite-rules { dscp <rewrite rule name> { forwarding-class dscp15 { loss-priority high code-point 101101; } forwarding-class EF { loss-priority low code-point 110001; } forwarding-class AF41 { loss-priority high code-point 100110; } forwarding-class NC { loss-priority low code-point 110000; } forwarding-class AF31 { loss-priority high code-point 010000; } forwarding-class Default { loss-priority high code-point 001000; } } } Note: Some platforms require rewriting all DSCP values if rewriting one (smaller platforms). Most support only rewriting a single DSCP value, which would eliminate all but one rewrite rule. scheduler-maps { <scheduler map name 1> { forwarding-class NC scheduler NC; forwarding-class EF scheduler EF; forwarding-class AF41 scheduler AF41; forwarding-class AF31 scheduler AF31; forwarding-class Default scheduler Default; } <scheduler map name 2> { forwarding-class BE scheduler BE; } } schedulers { NC { buffer-size percent 5; priority strict-high; } EF { shaping-rate percent 20; buffer-size percent 19; priority strict-high; } AF41 { shaping-rate percent 15; buffer-size percent 14; priority strict-high; } AF31 { shaping-rate percent 31; buffer-size percent 29; priority strict-high; } BE { transmit-rate percent 20; buffer-size percent 20; priority low; } Default { shaping-rate percent 10; buffer-size percent 9; priority strict-high; } } If the router is not configured to implement a QoS policy in accordance with the QoS GIG Technical Profile, this is a finding.

## Group: SRG-NET-000202-RTR-000001

**Group ID:** `V-254009`

### Rule: The Juniper perimeter router must be configured to deny network traffic by default and allow network traffic by exception.

**Rule ID:** `SV-254009r844060_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only connections that are essential and approved are allowed. This requirement applies to both inbound and outbound network communications traffic. All inbound and outbound traffic must be denied by default. Firewalls and perimeter routers should only allow traffic through that is explicitly permitted. The initial defense for the internal network is to block any traffic at the perimeter that is attempting to make a connection to a host residing on the internal network. In addition, allowing unknown or undesirable outbound traffic by the firewall or router will establish a state that will permit the return of this undesirable traffic inbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that the firewall filter is configured to allow specific ports and protocols and deny all other traffic. Associating any firewall filter to an interface will create a deny-all, permit-by-exception posture because each filter includes an implicit "deny all" final term. Verify firewall filters applied inbound on external interfaces are configured with terms permitting specific traffic. For example: [edit firewall] family inet { filter permitted_inbound_traffic_ipv4 { term 1 { from { destination-prefix-list { INSIDE_ADDRESSES_IPv4; } protocol tcp; destination-port [ http https ]; } then accept; } term 2 { from { destination-prefix-list { INSIDE_ADDRESSES_IPv4; } protocol udp; destination-port [ domain radius ]; } then accept; } } } family inet6 { filter permitted_inbound_traffic_ipv6 { term 1 { from { destination-prefix-list { INSIDE_ADDRESSES_IPv6; } next-header tcp; destination-port [ http https ]; } then accept; } term 2 { from { destination-prefix-list { INSIDE_ADDRESSES_IPv6; } next-header udp; destination-port [ domain radius ]; } then accept; } } } Note: Although the example filter is sufficient to meet this requirement, an explicit "deny-all" term is required for logging. For example, add the following final term to both filters (IPv4 and IPv6) to enable logging of discarded packets: [edit firewall family (inet|inet6) filter <name>] term default { then { log; syslog; discard; } } The filter must be configured inbound on all external interfaces. [edit interfaces] <external interface> { unit <number> { family inet { filter input permitted_inbound_traffic_ipv4; address <IPv4 address/mask>; } family inet6 { filter input permitted_inbound_traffic_ipv6; address <IPv6 address/prefix>; } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the filter is not configured to allow specific ports and protocols and deny all other traffic, this is a finding. If the filter is not configured inbound on all external interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000001

**Group ID:** `V-254010`

### Rule: The Juniper router must be configured to restrict traffic destined to itself.

**Rule ID:** `SV-254010r844063_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The routing engine (RE) handles traffic destined to the router—the key component used to build forwarding paths and is also instrumental with all network management functions. Hence, any disruption or DoS attack to the RE can result in mission critical network outages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the firewall filter for the router receive path and verify that it will only process specific management plane and control plane traffic from specific sources. For example: [edit policy-options] auth_mgt_networks-ipv4 { <IPv4 subnet / mask>; } auth_mgt_networks-ipv6 { <IPv6 subnet / prefix>; } device_mgt_address-ipv4 { <IPv4 address>/32; } device_mgt_address-ipv6 { <IPv6 address>/128; } [edit firewall] family inet { filter protect_re-ipv4 { term 1 { from { source-prefix-list auth_mgt_networks-ipv4; destination-prefix-list device_mgt_address-ipv4; <additional match criteria>; } } <additional permit terms> term default { then { log; syslog; discard; } } } } family inet6 { filter protect_re-ipv6 { term 1 { from { source-prefix-list auth_mgt_networks-ipv6; destination-prefix-list device_mgt_address-ipv6; <additional match criteria>; } } <additional permit terms> term default { then { log; syslog; discard; } } } } Note: Additional match criteria includes protocol (next-header for IPv6), source and destination ports, ICMP type and code, etc. When applied to the loopback interface, the filter affects identified traffic regardless of ingress interface. Ensure the filter addresses all traffic destined to the RE like routing protocols, ICMP messages, SSH and SCP traffic, SNMP, etc. Verify filters are applied to loopback, all L3 interfaces, or both. For example: [edit interfaces] lo0 { unit 0 { family inet { filter { input protect_re-ipv4; } address <IPv4 address>/32; } family inet6 { filter { input protect_re-ipv6; } address <IPv6 address>/32; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured with a receive-path filter to restrict traffic destined to itself, this is a finding. Note: If the platform does not support the receive path filter, verify that all layer 3 interfaces have an ingress firewall filter to control what packets are allowed to be destined to the router for processing.

## Group: SRG-NET-000205-RTR-000002

**Group ID:** `V-254011`

### Rule: The Juniper router must be configured to drop all fragmented Internet Control Message Protocol (ICMP) packets destined to itself.

**Rule ID:** `SV-254011r844066_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Fragmented ICMP packets can be generated by hackers for DoS attacks such as Ping O' Death and Teardrop. It is imperative that all fragmented ICMP packets are dropped.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the firewall filter for the router receive path. Firewall filters applied to the loopback interface affects traffic destined for the Route Engine (RE) regardless of ingress interface. Individual firewall filters are also supported on each ingress interface. Note: Verify the firewall filter applied to the loopback interface addresses all traffic destined for the RE (e.g., BGP, OSPF, etc.). Verify that it will drop all fragmented ICMP packets destined to itself. For example: [edit policy-options] prefix-list router-addresses-ipv4 { <interface IPv4 address>/32; <other router interface addresses>; } [edit firewall family inet] filter protect_re { term 1 { from { destination-prefix-list { router-addresses-ipv4; } is-fragment; protocol icmp; } then { log; syslog; discard; } } <additional terms for RE destined traffic> } [edit interfaces lo0 unit 0] family inet { filter { input protect_re; } address <IPv4 address>/32; } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured with a receive-path filter to drop all fragmented ICMP packets, this is a finding. Note: If the platform does not support the receive path filter, verify that all layer 3 interfaces have an ingress filter to control what packets are allowed to be destined to the router for processing.

## Group: SRG-NET-000205-RTR-000003

**Group ID:** `V-254012`

### Rule: The Juniper perimeter router must be configured to filter traffic destined to the enclave in accordance with the guidelines contained in DoD Instruction 8551.1.

**Rule ID:** `SV-254012r844069_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Vulnerability assessments must be reviewed by the System Administrator, and protocols must be approved by the Information Assurance (IA) staff before entering the enclave. Stateless firewall filters are the first line of defense in a layered security approach. They permit authorized packets and deny unauthorized packets based on port or service type. They enhance the posture of the network by not allowing packets to reach a potential target within the security domain. The lists provided are highly susceptible ports and services that should be blocked or limited as much as possible without adversely affecting customer requirements. Auditing packets attempting to penetrate the network but that are stopped by a firewall filter will allow network administrators to broaden their protective ring and more tightly define the scope of operation. If the perimeter is in a Deny-by-Default posture and what is allowed through the filter is in accordance with DoD Instruction 8551.1, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to PPS being blocked would be satisfied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that the ingress filter is in accordance with DoD 8551. For example, assuming TCP 80 and 443 are permitted inbound: [edit policy-options] prefix-list inside-addresses-ipv4 { <interior IPv4 subnet / mask>; } prefix-list inside-addresses-ipv4 { <interior IPv6 subnet / prefix>; } [edit firewall] family inet { filter inbound-ipv4 { term 1 { from { destination-prefix-list inside-addresses-ipv4; protocol tcp; destination-port [ 80 443 ]; } then accept; } <other terms as required> term default-deny { then { log; syslog; discard; } } } } family inet6 { filter inbound-ipv6 { term 1 { from { destination-prefix-list inside-addresses-ipv6; next-header tcp; destination-port [ 80 443 ]; } then accept; } <other terms as required> term default-deny { then { log; syslog; discard; } } } } If the router does not filter traffic in accordance with the guidelines contained in DoD 8551, this is a finding.

## Group: SRG-NET-000205-RTR-000004

**Group ID:** `V-254013`

### Rule: The Juniper perimeter router must be configured to filter ingress traffic at the external interface on an inbound direction.

**Rule ID:** `SV-254013r844072_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewall filters are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of routers makes use of firewall filters for restricting access to services on the router itself as well as for filtering traffic passing through the router. Inbound versus Outbound: It should be noted that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The router can protect itself before damage is inflicted. - The input port is still known and can be filtered upon. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that the ingress firewall filter is bound to the external interface in an inbound direction. [edit interfaces] <external interface> { unit <number> { family inet { filter { input inbound-ipv4; } } family inet6 { filter { input inbound-ipv6; } } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to filter traffic entering the network at the external interface in an inbound direction, this is a finding.

## Group: SRG-NET-000205-RTR-000005

**Group ID:** `V-254014`

### Rule: The Juniper perimeter router must be configured to filter egress traffic at the internal interface on an inbound direction.

**Rule ID:** `SV-254014r844075_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewall filters are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of routers makes use of firewall filters for restricting access to services on the router itself as well as for filtering traffic passing through the router. Inbound versus Outbound: It should be noted that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The router can protect itself before damage is inflicted. - The input port is still known and can be filtered upon. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that the egress firewall filter is bound to the internal interface in an inbound direction. [edit interfaces] <internal interface> { unit <number> { family inet { filter { input outbound-ipv4; } } family inet6 { filter { input outbound-ipv6; } } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output' change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to filter traffic leaving the network at the internal interface in an inbound direction, this is a finding.

## Group: SRG-NET-000205-RTR-000006

**Group ID:** `V-254015`

### Rule: The Juniper BGP router must be configured to reject outbound route advertisements for any prefixes belonging to the IP core.

**Rule ID:** `SV-254015r844078_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outbound route advertisements belonging to the core can result in traffic either looping or being black holed, or at a minimum, using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP router configuration to verify that there is a filter defined to block route advertisements for prefixes that belong to the IP core. Verify an appropriate prefix-list containing the IP core prefixes is referenced in a policy-statement. For example: [edit policy-options] prefix-list ip-core-ipv4 { 192.0.2.0/24; } prefix-list ip-core-ipv6 { 2001:db8:2::/64; } policy-statement advertise-bgp-prefix { term exclude-ipv4-core { from { prefix-list ip-core-ipv4; } then reject; } term exclude-ipv6-core { from { prefix-list ip-core-ipv6; } then reject; } term default { then accept; } } The prefix filter must be referenced outbound on the appropriate BGP neighbor statements. For example: [edit protocols] bgp { group eBGP { type external; export advertise-bgp-prefix; neighbor 192.0.2.11 { export advertise-bgp-prefix; } } export advertise-bgp-prefix; } Note: Juniper routers support global, group, and neighbor export statements with the more specific definition taking precedence. Ensure more specific export policies (e.g., neighbor and group) do not reverse higher level export statements. If the router is not configured to reject outbound route advertisements that belong to the IP core, this is a finding.

## Group: SRG-NET-000205-RTR-000007

**Group ID:** `V-254016`

### Rule: The Juniper PE router must be configured to block any traffic that is destined to IP core infrastructure.

**Rule ID:** `SV-254016r844081_rule`
**Severity:** high

**Description:**
<VulnDiscussion>IP/MPLS networks providing VPN and transit services must provide, at the least, the same level of protection against denial-of-service (DoS) attacks and intrusions as layer 2 networks. Although the IP core network elements are hidden, security should never rely entirely on obscurity. IP addresses can be guessed. Core network elements must not be accessible from any external host. Protecting the core from any attack is vital for the integrity and privacy of customer traffic as well as the availability of transit services. A compromise of the IP core can result in an outage or, at a minimum, nonoptimized forwarding of customer traffic. Protecting the core from an outside attack also prevents attackers from using the core to attack any customer. Hence, it is imperative that all routers at the edge deny traffic destined to any address belonging to the IP core infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE router configuration to verify that an ingress firewall filter is applied to all CE-facing interfaces. Verify that the ingress firewall filter rejects and logs packets destined to the IP core address block. For example: [edit policy-options] prefix-list ipv4-core { 192.0.2.0/24; } prefix-list ipv6-core { 2001:db8:2::/64; } [edit firewall] family inet { filter deny-core-ipv4 { term 1 { from { destination-prefix-list { ipv4-core; } } then { log; syslog; discard; } } term default { then accept; } } } family inet6 { filter deny-core-ipv6 { term 1 { from { destination-prefix-list { ipv6-core; } } then { log; syslog; discard; } } term default { then accept; } } } Verify the firewall filter is applied to CE-facing interfaces: [edit interfaces] ge-0/0/0 { unit 0 { family inet { filter { input deny-core-ipv4; } address <IPv4 address/mask>; } family inet6 { filter { input deny-core-ipv6; } address <IPv6 address/prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the PE router is not configured to block any traffic with a destination address assigned to the IP core infrastructure, this is a finding. Note: Internet Control Message Protocol (ICMP) echo requests and traceroutes will be allowed to the edge from external adjacent peers.

## Group: SRG-NET-000205-RTR-000008

**Group ID:** `V-254017`

### Rule: The Juniper PE router must be configured with Unicast Reverse Path Forwarding (uRPF) loose mode, or a firewall filter, enabled on all CE-facing interfaces.

**Rule ID:** `SV-254017r844084_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The uRPF feature, and ingress firewall filters, are defenses against spoofing and denial-of-service (DoS) attacks by verifying if the source address of any ingress packet is reachable. To mitigate attacks that rely on forged source addresses, all provider edge routers must enable uRPF or ingress firewall filters to guarantee that all packets received from a CE router contain source addresses that are in the route table.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE router configuration to determine if uRPF loose mode is enabled on all CE-facing interfaces. [edit interfaces] ge-0/0/12 { unit 0 { family inet { rpf-check { mode loose; } address <IPv4 address>/<mask>; } family inet6 { rpf-check { mode loose; } address <IPv6 address>/<prefix>; } } } For those platforms that do not support uRPF, verify an ingress stateless firewall filter is applied to all CE-facing interfaces. Because the prefixes assigned to each customer is known, verify each customer's prefix list contains only their prefixes and is referenced in an appropriate firewall filter. For example: [edit policy-options] prefix-list cust1-prefixes-ipv4 { 192.0.2.0/24; } prefix-list cust1-prefixes-ipv6 { 2001:db8:2::/64; } [edit firewall] family inet { filter cust1-prefixes-ipv4 { term 1 { from { source-prefix-list { cust1-prefixes-ipv4; } } then accept; } term default { then { log; syslog; discard; } } } } family inet6 { filter cust1-prefixes-ipv6 { term 1 { from { source-prefix-list { cust1-prefixes-ipv6; } } then accept; } term default { then { log; syslog; discard; } } } } Verify the appropriate filter is applied to each CE-facing interface. For example: [edit interfaces] ge-0/0/0 { unit 0 { family inet { filter { input cust1-prefixes-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { input cust1-prefixes-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If uRPF or an ingress firewall filter is not enabled on all CE-facing interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000009

**Group ID:** `V-254018`

### Rule: The Juniper out-of-band management (OOBM) gateway must be configured to transport management traffic to the Network Operations Center (NOC) via dedicated circuit, MPLS/VPN service, or IPsec tunnel.

**Rule ID:** `SV-254018r844087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Using dedicated paths, the OOBM backbone connects the OOBM gateway routers located at the edge of the managed network and at the NOC. Dedicated links can be deployed using provisioned circuits or MPLS layer 2 and layer 3 VPN services or implementing a secured path with gateway-to-gateway IPsec tunnels. The tunnel mode ensures that the management traffic will be logically separated from any other traffic traversing the same path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the network topology diagram to determine connectivity between the managed network and the NOC. Review the OOBM gateway router configuration to validate the path and interface that the management traffic traverses. MPLS-based VPN (L2 or L3) must have a working provider MPLS network including routing (for reachability) and Label Switched Paths (LSP). Additionally, the PE router will maintain separation for each CE router in individual routing instances. If using a dedicated circuit, verify the interface transporting NOC traffic is properly connected. CE routers will not peer with PE routers when using L2 VPN. Verify the CE router peers with the appropriate CE router, generally with an IGP (e.g., OSPF), and not the PE router. [edit interfaces] <exterior interface> { unit <number> { family inet { address <IPv4 address>/<mask>; } } } lo0 { unit 0 { family inet { address <IPv4 address>/32; } } } [edit protocols ospf] area <number> { interface lo0.0; interface <exterior interface>.<number>; } CE routers will peer with PE routers, generally with eBGP, when using L3 VPN. Verify the CE router advertises the appropriate interior networks to the PE. [edit interfaces] <exterior interface>:0 { unit <number> { family inet { address <IPv4 address>/<mask>; } } } lo0 { family inet { address <IPv4 address>/<mask>; } } [edit routing-options] router-id <ID>; autonomous-system <AS #>; [edit protocols bgp] group PE1 { type external; export <policy name>; peer-as <peer AS #>; neighbor <neighbor address>; << Reachable from the exterior interface } [edit policy-options policy-statement <statement name>] term 1 { from { protocol <protocol>; << Include the appropriate protocol (e.g., 'direct' for directly connected routes) route-filter <subnet>/<mask> <match condition>; << Include only interior routes that must be advertised to the L3 VPN } then accept; } Note: The policy-statement is applied as an export filter, using a route-filter to limit the exported routes. For example, assume 192.0.2.0/24 is the advertised route, and that it is directly connected. Using "protocol direct" will export all directly-connected routes, but no routes learned via an IGP (e.g., OSPF). Using "route-filter 192.0.2.0/24 orlonger then accept" will accept that /24 (or longer mask) and deny all others. Verify the match condition is appropriate for the desired advertisement. If management traffic is not transported between the managed network and the NOC via dedicated circuit, MPLS/VPN service, or IPsec tunnel, this is a finding.

## Group: SRG-NET-000205-RTR-000010

**Group ID:** `V-254019`

### Rule: The Juniper out-of-band management (OOBM) gateway router must be configured to forward only authorized management traffic to the Network Operations Center (NOC).

**Rule ID:** `SV-254019r844090_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM network is an IP network used exclusively for the transport of OAM&P data from the network being managed to the OSS components located at the NOC. Its design provides connectivity to each managed network device, enabling network management traffic to flow between the managed network elements and the NOC. This allows the use of paths separate from those used by the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the network topology diagram to determine connectivity between the managed network and the NOC. Review the OOBM gateway router configuration to validate the path that the management traffic traverses. Verify that only management traffic is forwarded through the OOBM interface or IPsec tunnel. Verify the destination address is configured either via a prefix-list or directly assigned addresses in each firewall filter term match condition. [edit policy-options] prefix-list NOC-ipv4 { <IPv4 address>/<mask>; } prefix-list NOC-ipv6 { <IPv6 address>/<prefix>; } [edit firewall] family inet { filter permit-NOC-ipv4 { term 1 { from { destination-prefix-list { NOC-ipv4; } protocol <protocol>; destination-port [ <port 1> <port 2> ]; } then accept; } <additional permitted traffic terms> term default { then { log; syslog; discard; } } } } family inet6 { filter permit-NOC-ipv6 { term 1 { from { destination-prefix-list { NOC-ipv6; } next-header <protocol>; destination-port [ <port 1> <port 2> ]; } then accept; } <additional permitted traffic terms> term default { then { log; syslog; discard; } } } } [edit interfaces] <OOBM interface> { unit <number> { family inet { filter { output NOC-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { output NOC-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If using an IPsec tunnel, verify the route with the tunnel interface as the next-hop destination. [edit routing-options] rib inet6.0 { static { route <NOC IPv6 network> next-hop <(tunnel interface | NOC IPv6 tunnel endpoint address)>; } } static { route <NOC IPv4 network> next-hop <(tunnel interface | NOC IPv6 tunnel endpoint address)>; } If traffic other than authorized management traffic is permitted through the OOBM interface or IPsec tunnel, this is a finding.

## Group: SRG-NET-000205-RTR-000011

**Group ID:** `V-254020`

### Rule: The Juniper out-of-band management (OOBM) gateway router must be configured to block any traffic destined to itself that is not sourced from the OOBM network or the NOC.

**Rule ID:** `SV-254020r844093_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the gateway router is not a dedicated device for the OOBM network, several safeguards must be implemented for containment of management and production traffic boundaries. It is imperative that hosts from the managed network are not able to access the OOBM gateway router.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the firewall filter for the router receive path. Verify that only traffic sourced from the OOBM network or the NOC is allowed to access the router. [edit policy-options] prefix-list OOBM-ipv4 { <IPv4 address>/<mask>; } prefix-list OOBM-ipv6 { <IPv6 address>/<prefix>; } prefix-list router-ipv4 { <IPv4 address>/<mask>; } prefix-list router-ipv6 { <IPv6 address>/<prefix>; } [edit firewall] family inet { filter protect-re-ipv4 { term 1 { from { source-prefix-list OOBM-ipv4; destination-prefix-list router-ipv4; } then accept; } <additional terms for authorized traffic like OSPF or BGP> term default { then { log; syslog; discard; } } } } family inet6 { filter protect-re-ipv6 { term 1 { from { source-prefix-list OOBM-ipv6; destination-prefix-list router-ipv6; } then accept { } <additional terms for authorized traffic like OSPF or BGP> term default { then { log; syslog; discard; } } } } Verify the firewall filter is applied to the loopback interface. [edit interfaces] lo0 { unit 0 { family inet { filter { input protect-re-ipv4; } address <IPv4 address/mask>; } family inet6 { filter { input protect-re-ipv6; } address <IPv6 address/prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router does not block any traffic destined to itself that is not sourced from the OOBM network or the NOC, this is a finding. Note: If the platform does not support the receive path filter, verify that all non-OOBM interfaces have an ingress firewall filter to restrict access to that interface address or any of the router’s loopback addresses to only traffic sourced from the management network. An exception would be to allow packets destined to these interfaces used for troubleshooting, such as ping and traceroute.

## Group: SRG-NET-000205-RTR-000012

**Group ID:** `V-254021`

### Rule: The Juniper router must be configured to only permit management traffic that ingresses and egresses the OOBM interface.

**Rule ID:** `SV-254021r844096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. An OOBM interface does not forward transit traffic, thereby providing complete separation of production and management traffic. Because all management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an OOBM interface, the interface functioning as the management interface must be configured so that management traffic does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the managed interface has an inbound and outbound firewall filter configured. In this example, the firewall filter uses prefix-lists rather than directly embedding the addresses in the filter term. Verify that the ingress filter only allows management, IGP, and ICMP traffic. Caveat: If the management interface is a true OOBM interface, this requirement is not applicable. [edit policy-options] prefix-list OOBM-ipv4 { 192.0.2.0/24; } prefix-list OOBM-ipv6 { 2001:db8:2::/64; } [edit firewall] family inet { filter inbound-OOBM-ipv4 { term 1 { from { source-prefix-list { OOBM-ipv4; } protocol [ icmp ospf ]; } then accept; } term 2 { from { source-prefix-list { OOBM-ipv4; } protocol tcp; destination-port ssh; } then accept; } <additional permit terms> term default { then { log; syslog; discard; } } } filter outbound-OOBM-ipv4 { term 1 { from { destination-prefix-list { OOBM-ipv4; } protocol [ icmp ospf ]; } then accept; } term 2 { from { destination-prefix-list { OOBM-ipv4; } protocol tcp; source-port ssh; } then accept; } <additional permit terms> term default { then { log; syslog; discard; } } } } family inet6 { filter inbound-OOBM-ipv6 { term 1 { from { source-prefix-list { OOBM-ipv6; } next-header [ icmp6 ospf ]; } then accept; } term 2 { from { source-prefix-list { OOBM-ipv6; } next-header tcp; destination-port ssh; } then accept; } <additional permit terms> term default { then { log; syslog; discard; } } } filter outbound-OOBM-ipv6 { term 1 { from { destination-prefix-list { OOBM-ipv6; } next-header [ icmp6 ospf ]; } then accept; } term 2 { from { destination-prefix-list { OOBM-ipv6; } next-header tcp; source-port ssh; } then accept; } <additional permit terms> term default { then { log; syslog; discard; } } } } If no true OOBM interface is available, verify the OOBM firewall filter is applied to the revenue interface configured for OOBM use. <revenue OOBM interface> { unit <number> { family inet { filter { input inbound-OOBM-ipv4; output outbound-OOBM-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { input inbound-OOBM-ipv6; output outbound-OOBM-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router does not restrict traffic that ingresses and egresses the management interface, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-254022`

### Rule: The Juniper perimeter router must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field via egress filter or by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-254022r844099_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. DDoS attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet; thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify uRPF or an egress filter has been configured on all internal interfaces to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field. [edit interfaces] <internal interface name> { unit <number> { family inet { rpf-check; address <IPv4 address>/<mask>; } family inet6 { rpf-check; address <IPv6 address>/<prefix>; } } } For those platforms that do not support uRPF, verify an egress stateless firewall filter is applied to all internal interfaces. In this example, the egress (from the enclave) filter is applied in the input direction of internal interfaces to prevent the router from accepting packets sourced from any address except the internal subnets. For example: [edit policy-options] prefix-list internal-prefixes-ipv4 { 192.0.2.0/24; } prefix-list internal-prefixes-ipv6 { 2001:0:2::/64; } [edit firewall] family inet { filter internal-inbound-ipv4 { term 1 { from { source-prefix-list { internal-prefixes-ipv4; } } then accept; } term default { then { log; syslog; discard; } } } } family inet6 { filter internal-inbound-ipv6 { term 1 { from { source-prefix-list { internal-prefixes-ipv6; } } then accept; } term default { then { log; syslog; discard; } } } } Verify the appropriate filter is applied to each internal interface. For example: [edit interfaces] <internal interface name> { unit <number> { family inet { filter { input internal-inbound-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { input internal-inbound-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If uRPF or an egress filter to restrict the router from accepting outbound IP packets that contain an illegitimate address in the source address field has not been configured on all internal interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000015

**Group ID:** `V-254023`

### Rule: The Juniper perimeter router must be configured to block all packets with any IP options.

**Rule ID:** `SV-254023r844102_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast switched and must be punted to the route engine (RE). Hackers who initiate denial-of-service (DoS) attacks on routers commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the router. The end result is a reduction in the effects of the DoS attack on the router and on downstream routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if it will block all packets with IP options. [edit firewall family inet] filter <name> { term 1 { from { ip-options any; } then { log; syslog; discard; } } <additional accept terms> term default { then { log; syslog; discard; } } } [edit interfaces] <interface name> { unit <number> { family inet { filter input <filter name>; address <IPv4 address>/<mask>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop all packets with IP options, this is a finding.

## Group: SRG-NET-000205-RTR-000016

**Group ID:** `V-254024`

### Rule: The Juniper PE router must be configured to ignore or block all packets with any IP options.

**Rule ID:** `SV-254024r844105_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast switched and, therefore, must be punted to the route engine (RE). Hackers who initiate denial-of-service (DoS) attacks on routers commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the router. The end result is a reduction in the effects of the DoS attack on the router and on downstream routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it will block all packets with IP options. [edit firewall family inet] filter <name> { term 1 { from { ip-options any; } then { log; syslog; discard; } } <additional accept terms> term default { then { log; syslog; discard; } } } [edit interfaces] <interface name> { unit <number> { family inet { filter input <filter name>; address <IPv4 address>/<mask>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop all packets with IP options, this is a finding.

## Group: SRG-NET-000230-RTR-000001

**Group ID:** `V-254025`

### Rule: The Juniper router must be configured to implement message authentication for all control plane protocols.

**Rule ID:** `SV-254025r844108_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration. For every protocol that affects the routing or forwarding tables (where information is exchanged between neighbors), verify that neighbor router authentication is enabled. [edit security ipsec] security-association <sa name> { manual { direction bidirectional { protocol esp; spi <SPI value>; authentication { algorithm hmac-sha-256-128; key ascii-text "$8$aes256-gcm$hmac-sha2-256$100$SpJ/ERRFEsc$y1Wqf1zM3d3xI+ZVB9WzTw$lgM06LJZN3FcVbTaSkDz4g$bZVi57MkUWg"; ## SECRET-DATA } } } } [edit protocols] bgp { group <group name> { type external; local-as <local AS number>; neighbor <neighbor 1 address> { authentication-key "$8$aes256-gcm$hmac-sha2-256$100$cFQ99Gy83Og$SCMVXvnfna7/cZqH9fCECQ$bCVokm+es94xFJONmbKFNA$4561Uc/r"; ## SECRET-DATA } neighbor <neighbor 2 address> { ipsec-sa <SA name>; } } } Note: Juniper BGP routers support either an MD5 key, rotating MD5 keys, or an IPsec security association (SA). Verify the PSK for each MD5 and SA is different between all neighbors. ospf { area <area number> { interface <interface name>.<logical unit> { authentication { md5 1 key "$8$aes256-gcm$hmac-sha2-256$100$hvt9Fpk6EEU$I2FKFJNrdKHpp1xesMB0aA$l9BsHxOYO4+B8f7erRj8Hw$A9PYzx53Ius"; ## SECRET-DATA } } interface <interface name>.<logical unit> { interface-type p2p; ipsec-sa <SA name>; } } } Note: Juniper OSPF routers support either an MD5 key or an IPsec SA. ospf3 { area <area number> { interface <interface name>.<logical unit> { ipsec-sa <SA name>; } } } Note: Juniper OSPFv3 routers only support IPsec SA. If authentication is not enabled, this is a finding.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-254026`

### Rule: The Juniper BGP router must be configured to use a unique key for each autonomous system (AS) that it peers with.

**Rule ID:** `SV-254026r844111_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between eBGP neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the ISSM and router administrator to determine if unique keys are being used. [edit security ipsec] security-association <sa name> { manual { direction bidirectional { protocol esp; spi <SPI value>; authentication { algorithm hmac-sha-256-128; key ascii-text "$8$aes256-gcm$hmac-sha2-256$100$SpJ/ERRFEsc$y1Wqf1zM3d3xI+ZVB9WzTw$lgM06LJZN3FcVbTaSkDz4g$bZVi57MkUWg"; ## SECRET-DATA } } } } [edit protocols bgp] group <group name> { type external; local-as <local AS number>; neighbor <neighbor 1 address> { authentication-key "$8$aes256-gcm$hmac-sha2-256$100$cFQ99Gy83Og$SCMVXvnfna7/cZqH9fCECQ$bCVokm+es94xFJONmbKFNA$4561Uc/r"; ## SECRET-DATA } neighbor <neighbor 2 address> { ipsec-sa <sa name>; } } Note: Juniper BGP routers support either an MD5 key, rotating MD5 keys, or an IPsec security association (SA). Verify the PSK for each MD5 and SA is different between all neighbors. If unique keys are not being used, this is a finding.

## Group: SRG-NET-000230-RTR-000003

**Group ID:** `V-254027`

### Rule: The Juniper router must be configured to use keys with a duration not exceeding 180 days for authenticating routing protocol messages.

**Rule ID:** `SV-254027r844114_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the keys used for routing protocol authentication are guessed, the malicious user could create havoc within the network by advertising incorrect routes and redirecting traffic. Some routing protocols allow the use of key chains for authentication. A key chain is a set of keys that is used in succession, with each having a lifetime of no more than 180 days. Changing the keys frequently reduces the risk of them eventually being guessed. Keys cannot be used during time periods for which they are not activated. If a time period occurs during which no key is activated, neighbor authentication cannot occur, and therefore routing updates will fail. Therefore, ensure that for a given key chain, key activation times overlap to avoid any period of time during which no key is activated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. For each authenticated routing protocol session, review the configured key expiration dates. [edit security] authentication-key-chains { key-chain <name> { key 1 { secret "$9$vNbM7Vg4ZjkPJGn/AtOB7-d"; ## SECRET-DATA start-time "2021-1-1.00:00:00 -0700"; algorithm md5; } key 2 { secret "$9$MAQL7VgoGqmTwYmTz3tpWLxNwY4aZjk."; ## SECRET-DATA start-time "2021-5-31.00:00:00 -0700"; algorithm md5; } } } [edit protocols] bgp { group eBGP { authentication-key-chain <name>; neighbor 1.2.3.4 { authentication-key-chain <name>; } } authentication-key-chain <name>; } Note: BGP supports authentication globally, at the group level, and individually for each neighbor. The most specific authentication configuration is applied. ospf { area 0.0.0.2 { interface ge-0/0/0.0 { authentication { md5 0 key "$9$vG08xd24Zk.5bs.5QFAtM8X7bsgoJDHq" start-time "2021-1-1.00:00:00 -0700"; ## SECRET-DATA md5 1 key "$9$m5z6p0IreW9AeWLxwsP5QF9AuO1hyl" start-time "2021-5-31.00:00:00 -0700"; ## SECRET-DATA } } } } If any key has a lifetime of more than 180 days, this is a finding.

## Group: SRG-NET-000343-RTR-000001

**Group ID:** `V-254028`

### Rule: The router providing MPLS L2VPN services must be configured to authenticate targeted LDP sessions used to exchange VC information using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-254028r844260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Label Distribution Protocol (LDP) provides the signaling required for setting up and tearing down pseudowires (virtual circuits used to transport layer 2 frames) across an MPLS IP core network. Using a targeted LDP session, each PE router advertises a virtual circuit label mapping that is used as part of the label stack imposed on the frames by the ingress PE router during packet forwarding. Authentication provides protection against spoofed TCP segments that can be introduced into the LDP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if LDP messages are being authenticated for the targeted LDP sessions. [edit protocols] ldp { interface <interface 1 name>.<logical unit>; interface <interface 2 name>.<logical unit>; session <Session destination address> { authentication-algorithm <aes-128-cmac-96|hmac-sha-1-96>; authentication-key-chain <name>; } } If authentication is not being used for the LDP sessions using a FIPS-approved message authentication code algorithm, this is a finding.

## Group: SRG-NET-000343-RTR-000002

**Group ID:** `V-254029`

### Rule: The Juniper Multicast Source Discovery Protocol (MSDP) router must be configured to authenticate all received MSDP packets.

**Rule ID:** `SV-254029r844120_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network routers presents additional risks to the core, whether from a rogue or misconfigured MSDP-enabled router. MSDP password authentication is used to validate each segment sent on the TCP connection between MSDP peers, protecting the MSDP session against the threat of spoofed packets being injected into the TCP connection stream.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if received MSDP packets are authenticated. [edit protocols] msdp { active-source-limit { maximum <1..1000000>; threshold <1..1000000>; log-warning <percent to log warning>; } <additional configuration> peer <address> { authentication-key "hashed PSK"; ## SECRET-DATA } } If the router does not require MSDP authentication, this is a finding.

## Group: SRG-NET-000362-RTR-000109

**Group ID:** `V-254030`

### Rule: The Juniper router must not be configured to have any zero-touch deployment feature enabled when connected to an operational network.

**Rule ID:** `SV-254030r844123_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices configured via a zero-touch deployment or auto-loading feature can have their startup configuration or image pushed to the device for installation via TFTP or Remote Copy (rcp). Loading an image or configuration file from the network is taking a security risk because the file could be intercepted by an attacker who could corrupt the file, resulting in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if a configuration auto-loading or zero-touch deployment feature is enabled. Verify the Juniper router is not configured with the factory default configuration. The Zero Touch Provisioning (ZTP) feature requires the factory default configuration. Juniper ZTP leverages Dynamic Host Configuration Protocol (DHCP) options to provide not only the interface address, but also the location of the upgrade image and configuration file. Interfaces configured for DHCP will not attempt to establish a ZTP session simply because DHCP is enabled but, instead, also require a factory default configuration. Therefore, if DHCP is authorized, removing the following [edit system] options, setting a root password, and committing will prevent the device from attempting ZTP. Verify the following are removed. [edit system] : : auto-configuration; << Delete this command. phone-home { << Delete this stanza. server <server URL>; rfc-compliant; } If a configuration auto-loading feature or zero-touch deployment feature is enabled, this is a finding. Note: Auto-configuration or zero-touch deployment features can be enabled when the router is offline for the purpose of image loading or building out the configuration. In addition, this would not be applicable to the provisioning of virtual routers via a software-defined network (SDN) orchestration system.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-254031`

### Rule: The Juniper router must be configured to protect against or limit the effects of denial-of-service (DoS) attacks by employing control plane protection.

**Rule ID:** `SV-254031r844126_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Routing Engine (RE) is critical to all network operations because it is the component used to build all forwarding paths for the data plane via control plane processes. It is also instrumental with ongoing network management functions that keep the routers and links available for providing network services. Any disruption to the RE or the control and management planes can result in mission-critical network outages. A DoS attack targeting the RE can result in excessive CPU and memory utilization. To maintain network stability and RE security, the router must be able to handle specific control plane and management plane traffic that is destined to the RE. In the past, one method of filtering was to use ingress filters on forwarding interfaces to filter both forwarding path and receiving path traffic. However, this method does not scale well as the number of interfaces grows and the size of the ingress filters grows. Control plane policing increases the security of routers and multilayer switches by protecting the RE from unnecessary or malicious traffic. Filtering and rate limiting the traffic flow of control plane packets can be implemented to protect routers against reconnaissance and DoS attacks, allowing the control plane to maintain packet forwarding and protocol states despite an attack or heavy load on the router or multilayer switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine whether control plane protection has been implemented on the device by verifying traffic types have been classified based on importance levels and a policy has been configured to filter and rate limit the traffic according to each class. Verify firewall filters include policers (rate limiting) based upon importance levels. Although the policer names shown in the example are the bandwidth limit, any legal name can be used. [edit firewall] family inet { filter <name> { term accept-tcp-initial { from { source-prefix-list { management-networks-ipv4; } destination-prefix-list { router-addresses-ipv4; } protocol tcp; destination-port ssh; tcp-initial; } then { policer policer-32k; << Lower rate for connection attempts to help prevent SYN flood attacks. accept; } } term accept-ssh { from { source-prefix-list { management-networks-ipv4; } destination-prefix-list { router-addresses-ipv4; } protocol tcp; destination-port ssh; } then { policer policer-1g; << Higher rate after connection establishment for remote management and/or secure file transfer. accept; } } term accept-snmp { from { source-prefix-list { snmp-servers-ipv4; } destination-prefix-list { router-addresses-ipv4; } protocol udp; destination-port snmp; } then { policer policer-1m; accept; } } <additional terms> term default-deny { then { log; syslog; discard; } } } } family inet6 { filter <name> { term accept-tcp-initial { from { source-prefix-list { management-networks-ipv6; } destination-prefix-list { router-addresses-ipv6; } next-header tcp; destination-port ssh; tcp-initial; } then { policer policer-32k; << Lower rate for connection attempts to help prevent SYN flood attacks. accept; } } term accept-ssh { from { source-prefix-list { management-networks-ipv6; } destination-prefix-list { router-addresses-ipv6; } next-header tcp; destination-port ssh; } then { policer policer-1g; << Higher rate after connection establishment for remote management. accept; } } term accept-snmp { from { source-prefix-list { snmp-servers-ipv6; } destination-prefix-list { router-addresses-ipv6; } next-header udp; destination-port snmp; } then { policer policer-1m; accept; } } <additional terms> term default-deny { then { log; syslog; discard; } } } } Note: Verify the applied filter has terms for all permitted traffic (e.g., OSPF, BGP, etc.). policer policer-1g { if-exceeding { bandwidth-limit 1g; burst-size-limit 100k; } then discard; } policer policer-1m { if-exceeding { bandwidth-limit 1m; burst-size-limit 15k; } then discard; } policer policer-32k { if-exceeding { bandwidth-limit 32k; burst-size-limit 1500; } then discard; } [edit interfaces] lo0 { unit <number> { family inet { filter { input <filter name>; } address <IPv4 address>/32; } family inet6 { filter { input <filter name>; } address <IPv6 address>/128/ } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router does not have control plane protection implemented, this is a finding.

## Group: SRG-NET-000362-RTR-000111

**Group ID:** `V-254032`

### Rule: The Juniper router must be configured to have Gratuitous ARP disabled on all external interfaces.

**Rule ID:** `SV-254032r844129_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A gratuitous ARP is an ARP broadcast in which the source and destination MAC addresses are the same. It is used to inform the network about a host IP address. A spoofed gratuitous ARP message can cause network mapping information to be stored incorrectly, causing network malfunction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if gratuitous ARP is disabled on all external interfaces. [edit interfaces] <external interface> { no-gratuitous-arp-reply; no-gratuitous-arp-request; unit <number> { family inet { address <IPv4 address>/<mask>; } family inet6 { address <IPv6 address>/<mask>; } } } If gratuitous ARP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000362-RTR-000112

**Group ID:** `V-254033`

### Rule: The Juniper router must be configured to have IP directed broadcast disabled on all interfaces.

**Rule ID:** `SV-254033r844132_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An IP directed broadcast is a datagram sent to the broadcast address of a subnet that is not directly attached to the sending machine. The directed broadcast is routed through the network as a unicast packet until it arrives at the target subnet, where it is converted into a link-layer broadcast. Because of the nature of the IP addressing architecture, only the last router in the chain, which is connected directly to the target subnet, can conclusively identify a directed broadcast. IP directed broadcasts are used in the extremely common and popular smurf, or denial-of-service (DoS), attacks. In a smurf attack, the attacker sends Internet Control Message Protocol (ICMP) echo requests from a falsified source address to a directed broadcast address, causing all the hosts on the target subnet to send replies to the falsified source. By sending a continuous stream of such requests, the attacker can create a much larger stream of replies, which can completely inundate the host whose address is being falsified. This service should be disabled on all interfaces when not needed to prevent smurf and DoS attacks. Directed broadcast can be enabled on internal facing interfaces to support services such as Wake-On-LAN. Case scenario may also include support for legacy applications where the content server and the clients do not support multicast. The content servers send streaming data using UDP broadcast. Used in conjunction with the IP multicast helper-map feature, broadcast data can be sent across a multicast topology. The broadcast streams are converted to multicast and vice versa at the first-hop routers and last-hop routers before entering and leaving the multicast transit area respectively. The last-hop router must convert the multicast to broadcast. Hence, this interface must be configured to forward a broadcast packet (i.e., a directed broadcast address is converted to the all-nodes broadcast address).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if IP directed broadcast is enabled. By default, IP directed broadcast is disabled on all L3 interfaces, including Integrated Routing and Bridging (IRB) interfaces. Verify "targeted-broadcast" is not enabled as shown. [edit interfaces] <L3 interface> { unit <number> { family inet { targeted-broadcast; << Must not be present. address <IPv4 address>/<mask>; } } } irb { unit <number> { family inet { targeted-broadcast; << Must not be present. address <IPv4 address>/<mask>; } } } If IP directed broadcast is enabled on layer 3 interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000113

**Group ID:** `V-254034`

### Rule: The Juniper router must be configured to have Internet Control Message Protocol (ICMP) unreachable notifications disabled on all external interfaces.

**Rule ID:** `SV-254034r844135_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Host unreachable ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if controls have been defined to ensure the router does not send ICMP unreachable notifications out to any external interfaces. [edit policy-options] prefix-list router-address-ipv4 { <external interface address>/32; <internal subnet>/<mask>; } [edit firewall family inet] filter <name> { term 1 { from { source-prefix-list { router-address-ipv4; } protocol icmp; icmp-type unreachable; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } [edit interfaces] <external interface> { unit <number> { family inet { filter { output <filter name>; } address <IPv4 address>/<mask>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If ICMP unreachable notifications are enabled on any external interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-254035`

### Rule: The Juniper router must be configured to have Internet Control Message Protocol (ICMP) mask replies disabled on all external interfaces.

**Rule ID:** `SV-254035r844138_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if controls have been defined to ensure the router does not send ICMP Mask Reply messages out to any external interfaces. [edit policy-options] prefix-list router-address-ipv4 { <external interface address>/32; <internal subnet>/<mask>; } [edit firewall family inet] filter <name> { term 1 { from { source-prefix-list { router-address-ipv4; } protocol icmp; icmp-type mask-reply; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } [edit interfaces] <external interface> { unit <number> { family inet { filter { output <filter name>; } address <IPv4 address>/<mask>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If ICMP Mask Reply messages are enabled on any external interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000115

**Group ID:** `V-254036`

### Rule: The Juniper router must be configured to have Internet Control Message Protocol (ICMP) redirects disabled on all external interfaces.

**Rule ID:** `SV-254036r844141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Routers automatically send ICMP messages under a wide variety of conditions. Redirect ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if controls have been defined to ensure the router does not send ICMP Redirect messages out to any external interfaces. Verify the global "no-redirects" statement is enabled under [edit system] or that individual interface "no-redirects" statements are configured on external interfaces. [edit system] no-redirects; [edit interfaces] <external interface name> { unit <number> { family inet { no-redirects; address <IPv4 address>.<mask>; } family inet6 { no-redirects; address <IPv6 address>.<prefix>; } } } If ICMP Redirect messages are enabled on any external interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-254037`

### Rule: The Juniper BGP router must be configured to use the prefix limit feature to protect against route table flooding and prefix deaggregation attacks.

**Rule ID:** `SV-254037r844144_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix deaggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix deaggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. In 1997, misconfigured routers in the Florida Internet Exchange network (AS7007) deaggregated every prefix in their routing table and started advertising the first /24 block of each of these prefixes as their own. Faced with this additional burden, the internal routers became overloaded and crashed repeatedly. This caused prefixes advertised by these routers to disappear from routing tables and reappear when the routers came back online. As the routers came back after crashing, they were flooded with the routing table information by their neighbors. The flood of information would again overwhelm the routers and cause them to crash. This process of route flapping served to destabilize not only the surrounding network but also the entire internet. Routers trying to reach those addresses would choose the smaller, more specific /24 blocks first. This caused backbone networks throughout North America and Europe to crash. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the deaggregation risk. BGP maximum prefix must be used on all eBGP routers to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering AS. Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that the number of received prefixes from each eBGP neighbor is controlled. [edit protocols] bgp { group <group name> { type external; local-as <local AS number>; neighbor <neighbor 1 address> { family inet { unicast { prefix-limit { maximum 10; teardown; } } } family inet6 { unicast { prefix-limit { maximum 10; teardown; } } } authentication-key "$8$aes256-gcm$hmac-sha2-256$100$cFQ99Gy83Og$SCMVXvnfna7/cZqH9fCECQ$bCVokm+es94xFJONmbKFNA$4561Uc/r"; ## SECRET-DATA } neighbor <neighbor 2 address> { family inet { unicast { prefix-limit { maximum 10; teardown; } } } family inet6 { unicast { prefix-limit { maximum 10; teardown; } } } ipsec-sa <SA name>; } } } If the router is not configured to control the number of prefixes received from each peer to protect against route table flooding and prefix deaggregation attacks, this is a finding.

## Group: SRG-NET-000362-RTR-000118

**Group ID:** `V-254038`

### Rule: The Juniper BGP router must be configured to limit the prefix size on any inbound route advertisement to /24 or the least significant prefixes issued to the customer.

**Rule ID:** `SV-254038r844147_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The effects of prefix deaggregation can degrade router performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured router, prefix deaggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify that there is a filter to reject inbound route advertisements that are greater than /24, or the least significant prefixes issued to the customer, whichever is larger. Verify each BGP neighbor implements an import policy. BGP import policies are supported in three locations: Global (at [edit protocols bgp]), group (at [edit protocols bgp group <name>]), and for each neighbor (at [edit protocols bgp group <name> neighbor <neighbor address>]) with the most specific import statement being applied. Multiple policy statements may be necessary to address each customer's requirements. [edit policy-options] policy-statement reject-long-prefixes { term 1 { from { route-filter 0.0.0.0/0 prefix-length-range /25-/32; } then reject; } <additional terms> } [edit protocols] bgp { group <group name> { type external; import <policy statement name>; << Applied instead of global BGP policy unless a more specific neighbor import filter exists. Excludes all terms in the global filter. local-as <local AS number>; neighbor <neighbor 1 address> { import <policy statement name>; << Most specific import filter. If configured, only this filter applies to this neighbor (all other terms in all other filters ignored). authentication-key "$8$aes256-gcm$hmac-sha2-256$100$cFQ99Gy83Og$SCMVXvnfna7/cZqH9fCECQ$bCVokm+es94xFJONmbKFNA$4561Uc/r"; ## SECRET-DATA } neighbor <neighbor 2 address> { import <policy statement name>; << Most specific import filter. If configured, only this filter applies to this neighbor (all other terms in all other filters ignored). ipsec-sa <SA name>; } } import <policy statement name>; << Least specific import filter. } If the router is not configured to limit the prefix size on any inbound route advertisement to /24 or the least significant prefixes issued to the customer, this is a finding.

## Group: SRG-NET-000362-RTR-000119

**Group ID:** `V-254039`

### Rule: The Juniper PE router must be configured to implement Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) snooping for each Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-254039r844150_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP snooping provides a way to constrain multicast traffic at layer 2. By monitoring the IGMP membership reports sent by hosts within the bridge domain, the snooping application can set up layer 2 multicast forwarding tables to deliver traffic only to ports with at least one interested member within the VPLS bridge, thereby significantly reducing the volume of multicast traffic that would otherwise flood an entire VPLS bridge domain. The IGMP snooping operation applies to both access circuits and pseudowires within a VPLS bridge domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that IGMP or MLD snooping has been configured for IPv4 and IPv6 multicast traffic respectively for each VPLS bridge domain (VFI instance). [edit routing-instances <name>] protocols { igmp-snooping { vlan <VLAN name>; } mld-snooping { vlan <VLAN name>; } } Note: Only EX9200-series devices currently support VPLS. If the router is not configured to implement IGMP or MLD snooping for each VPLS bridge domain, this is a finding.

## Group: SRG-NET-000362-RTR-000120

**Group ID:** `V-254040`

### Rule: The Juniper multicast RP router must be configured to limit the multicast forwarding cache so that its resources are not saturated by managing an overwhelming number of PIM and MSDP source-active entries.

**Rule ID:** `SV-254040r844261_rule`
**Severity:** low

**Description:**
<VulnDiscussion>MSDP peering between networks enables sharing of multicast source information. Enclaves with an existing multicast topology using PIM-SM can configure their RP routers to peer with MSDP routers. As a first step of defense against a denial-of-service (DoS) attack, all RP routers must limit the multicast forwarding cache to ensure that router resources are not saturated managing an overwhelming number of PIM and MSDP source-active entries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if forwarding cache thresholds are defined. [edit routing-options] multicast { forwarding-cache { threshold { suppress <1..200000>; reuse <1..200000>; log-warning <percent to generate warning>; } } } If the RP router is not configured to limit the multicast forwarding cache to ensure that its resources are not saturated, this is a finding.

## Group: SRG-NET-000362-RTR-000121

**Group ID:** `V-254041`

### Rule: The Juniper multicast Rendezvous Point (RP) must be configured to rate limit the number of Protocol Independent Multicast (PIM) Register messages.

**Rule ID:** `SV-254041r844156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a new source starts transmitting in a PIM Sparse Mode network, the DR will encapsulate the multicast packets into register messages and forward them to the RP using unicast. This process can be taxing on the CPU for both the DR and the RP if the source is running at a high data rate and there are many new sources starting at the same time. This scenario can potentially occur immediately after a network failover. The rate limit for the number of register messages should be set to a relatively low value based on the known number of multicast sources within the multicast domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the RP to verify that it is rate limiting the number of multicast register messages. [edit protocols pim] rp { register-limit { maximum <1..65535>; } <additional configuration> } If the RP is not limiting multicast register messages, this is a finding.

## Group: SRG-NET-000362-RTR-000122

**Group ID:** `V-254042`

### Rule: The Juniper multicast Designated Router (DR) must be configured to limit the number of mroute states resulting from Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Host Membership Reports.

**Rule ID:** `SV-254042r844159_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The current multicast paradigm can let any host join any multicast group at any time by sending an IGMP or MLD membership report to the DR. In a Protocol Independent Multicast (PIM) Sparse Mode network, the DR will send a PIM Join message for the group to the RP. Without any form of admission control, this can pose a security risk to the entire multicast domain - specifically the multicast routers along the shared tree from the DR to the RP that must maintain the mroute state information for each group join request. Hence, it is imperative that the DR is configured to limit the number of mroute state information that must be maintained to mitigate the risk of IGMP or MLD flooding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DR configuration to verify that it is limiting the number of mroute states via IGMP or MLD. Verify the group-limit parameter is appropriate for the target network. [edit protocols] igmp { interface <name>.<logical unit> { group-limit <1..32767>; } } mld { interface <name>.<logical unit> { group-limit <1..32767>; } } If the DR is not limiting multicast join requests via IGMP or MLD, this is a finding.

## Group: SRG-NET-000362-RTR-000123

**Group ID:** `V-254043`

### Rule: The Juniper multicast Designated Router (DR) must be configured to increase the shortest-path tree (SPT) threshold or set it to infinity to minimalize source-group (S, G) state within the multicast topology where Any Source Multicast (ASM) is deployed.

**Rule ID:** `SV-254043r844162_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASM can have many sources for the same groups (many-to-many). For many receivers, the path via the RP may not be ideal compared with the shortest path from the source to the receiver. By default, the last-hop router will initiate a switch from the shared tree to a source-specific SPT to obtain lower latencies. This is accomplished by the last-hop router sending an (S, G) Protocol Independent Multicast (PIM) Join toward S (the source). When the last-hop router begins to receive traffic for the group from the source via the SPT, it will send a PIM Prune message to the RP for the (S, G). The RP will then send a Prune message toward the source. The SPT switchover becomes a scaling issue for large multicast topologies that have many receivers and many sources for many groups because (S, G) entries require more memory than (*, G). Hence, it is imperative to minimize the amount of (S, G) state to be maintained by increasing the threshold that determines when the SPT switchover occurs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the multicast last-hop router configuration to verify that the SPT switchover threshold is increased (default is "0") or set to infinity (never switch over). Verify the policy statement includes specific multicast groups or all groups (as shown). [edit policy-options] policy-statement <name> { term 1 { from { route-filter 234.0.0.0/8 orlonger; } then accept; } } Verify the infinity policy is applied. [edit protocols pim] spt-threshold { infinity <policy name>; } If any multicast router is not configured to increase the SPT threshold or set to infinity to minimalize (S, G) state, this is a finding.

## Group: SRG-NET-000362-RTR-000124

**Group ID:** `V-254044`

### Rule: The Juniper BGP router must be configured to enable the Generalized TTL Security Mechanism (GTSM).

**Rule ID:** `SV-254044r844165_rule`
**Severity:** low

**Description:**
<VulnDiscussion>GTSM is designed to protect a router's IP-based control plane from DoS attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all Exterior Border Gateway Protocol speaking routers. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent routers; that is, the Exterior Border Gateway Protocol peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration. Verify a firewall filter term discards BGP packets with a TTL less than 255. [edit firewall family inet] filter gtsm { term 1 { from { protocol tcp; ttl 255; destination-port bgp; } then accept; } term 2 { from { protocol tcp; destination-port bgp; } then { log; syslog; discard; } } <additional accept terms> term default { then { log; syslog; discard; } } } Some routers support the "ttl-except" directive that can replace the two term filter shown above. For example: [edit firewall family inet] filter gtsm { term 1 { from { protocol tcp; ttl-except 255; destination-port bgp; } then { log; syslog; discard; } } <additional accept terms> term default { then { log; syslog; discard; } } } Verify the filter is applied to BGP neighbor interfaces. [edit interfaces] <bgp interface> { unit <number> { family inet { filter input gtsm; } address <IPv4 address>.<mask>; } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to use GTSM for all Exterior Border Gateway Protocol peering sessions, this is a finding.

## Group: SRG-NET-000364-RTR-000109

**Group ID:** `V-254045`

### Rule: The Juniper perimeter router must be configured to only allow incoming communications from authorized sources to be routed to authorized destinations.

**Rule ID:** `SV-254045r844168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic can be restricted directly by stateless firewall filter, or filter based forwarding. Filter based forwarding is a technique used to make routing decisions based on a number of different criteria other than just the destination network, including source or destination network, source or destination address, source or destination port, protocol, packet size, and packet classification. This overrides the router's normal routing procedures used to control the specific paths of network traffic. It is normally used for traffic engineering but can also be used to meet security requirements; for example, traffic that is not allowed can be routed to the discard interface. Filter based forwarding can also be used to control which prefixes appear in the routing table. This requirement is intended to allow network administrators the flexibility to use whatever technique is most effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if the router allows only incoming communications from authorized sources to be routed to authorized destinations. [edit policy-options] prefix-list inside-addresses-ipv4 { 192.0.2.0/25; 192.0.2.130/32; } prefix-list inside-addresses-ipv6 { 2001:db8:1::/64; 2001:db8:a1::/64; } [edit firewall] family inet { filter authorized-outbound-ipv4 { <additional terms> term permitted-source-addresses { from { source-prefix-list { inside-addresses-ipv4; } } then accept; } term default-deny { then { log; syslog; discard; } } } filter authorized-inbound-ipv4 { <additional terms> term permitted-destination-addresses { from { destination-prefix-list { inside-addresses-ipv4; } } then accept; } term default-deny { then { log; syslog; discard; } } } } family inet6 { filter authorized-outbound-ipv6 { <additional terms> term permitted-source-addresses { from { source-prefix-list { inside-addresses-ipv6; } } then accept; } term default-deny { then { log; syslog; discard; } } } filter authorized-inbound-ipv6 { <additional terms> term permitted-destination-addresses { from { destination-prefix-list { inside-addresses-ipv6; } } then accept; } term default-deny { then { log; syslog; discard; } } } } Note: The same firewall filtering process can be configured to control traffic destined to the router, or between internal subnets. Verify the firewall filters are applied to the correct interface in the appropriate direction. [edit interfaces] <external interface> { unit <number> { family inet { filter { input authorized-inbound-ipv4; } address <IPv4 address>.<mask>; } family inet6 { filter { input authorized-inbound-ipv6; } address <IPv6 address>.<prefix>; } } } <internal interface> { unit <number> { family inet { filter { input authorized-outbound-ipv4; } address <IPv4 address>.<mask>; } family inet6 { filter { input authorized-outbound-ipv6; } address <IPv6 address>.<prefix>; } } } If the router does not restrict incoming communications to allow only authorized sources and destinations, this is a finding.

## Group: SRG-NET-000364-RTR-000110

**Group ID:** `V-254046`

### Rule: The Juniper perimeter router must be configured to block inbound packets with source Bogon IP address prefixes.

**Rule ID:** `SV-254046r844171_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Bogons include IP packets on the public internet that contain addresses that are not in any range allocated or delegated by the Internet Assigned Numbers Authority (IANA) or a delegated regional Internet registry (RIR) and allowed for public internet use. Bogons also include multicast, IETF reserved, and special purpose address space as defined in RFC 6890. Security of the internet's routing system relies on the ability to authenticate an assertion of unique control of an address block. Measures to authenticate such assertions rely on the validation the address block forms as part of an existing allocated address block, and must be a trustable and unique reference in the IANA address registries. The intended use of a Bogon address would only be for the purpose of address spoofing in denial-of-service attacks. Hence, it is imperative that IP packets with a source Bogon address are blocked at the network’s perimeter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Verify that the ingress filter is blocking packets with Bogon source addresses. Bogon addresses are added to prefix lists to ease management, and prefix lists are associated with firewall filters. Verify appropriate prefix lists for IPv4 and IPv6 Bogon addresses. For example: [edit policy-options] prefix-list bogon-addresses-ipv4 { /* This host on this network */ 0.0.0.0/8; /* CGN Addresses */ 100.64.0.0/10; /* Loopback */ 127.0.0.0/8; /* IPv4 link-local or APIPA */ 169.254.0.0/16; /* IETF Protocol Assignments */ 192.0.0.0/24; /* IPv4 documentation addresses: TEST-NET-1 */ 192.0.2.0/24; /* 6to4 Relay Anycast descr in RFC3068 */ 192.88.99.0/24; /* Benchmark testing descr in RFC2544 */ 198.18.0.0/15; /* IPv4 documentation addresses: TEST-NET-2 */ 198.51.100.0/24; /* IPv4 documentation addresses: TEST-NET-3 */ 203.0.113.0/24; /* Multicast */ 224.0.0.0/24; /* Reserved */ 240.0.0.0/4; /* RFC1918 Addresses */ 10.0.0.0/8; 172.16.0.0/12; 192.168.0.0/16; <add additional routes as needed> } route-filter-list bogon-ipv6 { /* Unspecified */ ::/128; /* Loopback */ ::1/128; /* IPv4 Compatible */ 0::/96; /* IPv4-mapped */ ::ffff:0:0/96; /* 6Bone */ 3ffe::/16; /* IPv4-IPv6 Translate */ 64:ff9b::/96; /* Discard-Only */ 100::/64; /* ORCHID */ 2001:10::/28; /* Documentation */ 2001:db8::/32; /* Benchmarking */ 2001:2::/48; /* TEREDO */ 2001::/32; /* IETF Protocol Assignments */ 2001::/23; /* 6to4 */ 2002::/16; /* Unique-Local */ fc00::/7; /* Site local (deprecated) - now reserved */ fec0::/10; /* Multicast */ ff00::/8; <add additional routes as needed> } Note: The comments associated with addresses is configured with the "annotate" command. Annotations will appear in the standard hierarchical configuration display but do not appear when using "display set". The annotations are not required but added to this check to show what each address represents. Verify IPv4 and IPv6 firewall filters incorporate Bogon address restrictions. [edit firewall] family inet { filter inbound-ipv4 { term 1 { from { source-prefix-list bogon-ipv4; } then { log; syslog; discard; } } <permitted traffic terms> } } family inet6 { filter inbound-ipv6 { term 1 { from { source-prefix-list bogon-ipv6; } then { log; syslog; discard; } } <permitted traffic terms> } } Review the router configuration to verify that it is configured to block IP packets with a Bogon source address. Verify the firewall filter enforcing Bogon restrictions is applied inbound on exterior-facing interfaces. For example: [edit interfaces] <interface name> { unit <number> { family inet { filter { input inbound-ipv4; } address <IPv4 address>/<mask>; } family inet6 { filter { input inbound-ipv6; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; Reference minimum IPv4 Bogon Prefixes 0.0.0.0/8 10.0.0.0/8 100.64.0.0/10 127.0.0.0/8 169.254.0.0/16 172.16.0.0/12 192.0.0.0/24 192.0.2.0/24 192.88.99.0/24 192.168.0.0/16 198.18.0.0/15 198.51.100.0/24 203.0.113.0/24 224.0.0.0/4 240.0.0.0/4 Reference minimum IPv6 Bogon Prefixes ::/128 ::1/128 0::/96 ::ffff:0:0/96 3ffe::/16 64:ff9b::/96 100::/64 2001:10::/28 2001:db8::/32 2001:2::/48 2001::/32 2001::/23 2002::/16 fc00::/7 fe80::/10 fec0::/10 ff00::/8 If the router is not configured to block inbound IP packets containing a Bogon source address, this is a finding. Note: At a minimum, IP packets containing a source address from the special purpose address space as defined in RFC 6890 must be blocked. The 6Bone prefix (3ffe::/16) is also be considered a Bogon address. Perimeter routers connected to commercial ISPs for internet or other non-DoD network sources will need to be reviewed for a full Bogon list. The IPv4 full Bogon list contains prefixes that have been allocated to RIRs but not assigned by those RIRs. Reference the following link: http://www.team-cymru.org/Services/Bogons/fullbogons-ipv4.txt The IPv6 full Bogon list contains prefixes that have not been allocated to RIRs, or those that have been allocated to RIRs but have not been assigned by those RIRs. Reference the following link: https://www.team-cymru.org/Services/Bogons/fullbogons-ipv6.txt

## Group: SRG-NET-000364-RTR-000111

**Group ID:** `V-254047`

### Rule: The Juniper perimeter router must be configured to have Link Layer Discovery Protocols (LLDPs) disabled on all external interfaces.

**Rule ID:** `SV-254047r844174_rule`
**Severity:** low

**Description:**
<VulnDiscussion>LLDPs are primarily used to obtain protocol addresses of neighboring devices and discover platform capabilities of those devices. Use of SNMP with the LLDP Management Information Base (MIB) allows network management applications to learn the device type and the SNMP agent address of neighboring devices, thereby enabling the application to send SNMP queries to those devices. LLDPs are also media- and protocol-independent as they run over the data link layer; therefore, two systems that support different network-layer protocols can still learn about each other. Allowing LLDP messages to reach external network nodes is dangerous as it provides an attacker a method to obtain information of the network infrastructure that can be useful to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review all router configurations to ensure LLDPs are not included in the global configuration or LLDPs are not included for each active external interface. Examples of LLDPs are Cisco Discovery Protocol (CDP), Link Layer Discovery Protocol (LLDP), and Link Layer Discovery Protocol - Media Endpoint Discovery (LLDP-MED). Junos does not support CDP, but supports both LLDP and LLDP-MED, configured at [edit protocols]. Verify external interfaces are either not configured or explicitly disabled. For example: To globally disable LLDP and LLDP-MED: [edit protocols] <no LLDP or LLDP-MED hierarchy> -or- lldp { interface all { disable; } } lldp-med { interface all { disable; } } If LLDP or LLDP-MED is authorized, verify external interfaces are not configured or are explicitly disabled. For example: [edit protocols] lldp { interface all { disable; } interface ge-0/0/0; <<< Verify ge-0/0/0 is not an external interface. interface ge-0/0/1 { disable; <<< Assuming ge-0/0/1 is an external interface, it is disabled globally (interface all disable) or explicitly disabled as shown. } } lldp-med { interface all { disable; interface ge-0/0/0; <<< Verify ge-0/0/0 is not an external interface. interface ge-0/0/1 { disable; <<< Assuming ge-0/0/1 is an external interface, it is disabled globally (interface all disable) or explicitly disabled as shown. } } Note: Both LLDP and LLDP-MED are globally disabled on all interfaces but Junos will apply the most specific configuration. Therefore, both LLDP and LLDP-MED are enabled only on ge-0/0/0 and disabled on all other interfaces as configured in the example. If LLDPs are configured globally or on any external interface, this is a finding.

## Group: SRG-NET-000364-RTR-000112

**Group ID:** `V-254048`

### Rule: The Juniper perimeter router must be configured to have Proxy ARP disabled on all external interfaces.

**Rule ID:** `SV-254048r844177_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Proxy ARP is enabled on a router, it allows that router to extend the network (at layer 2) across multiple interfaces (LAN segments). Because proxy ARP allows hosts from different LAN segments to look like they are on the same segment, proxy ARP is only safe when used between trusted LAN segments. Attackers can leverage the trusting nature of proxy ARP by spoofing a trusted host and then intercepting packets. Proxy ARP should always be disabled on router interfaces that do not require it, unless the router is being used as a LAN bridge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if Proxy ARP is disabled on all external interfaces. By default, Proxy ARP is disabled on all interfaces. Verify "proxy-arp" has not been enabled on external interfaces as shown in the example: [edit interfaces] <external interface> { unit 0 { proxy-arp [restricted|unrestricted]; << Must not be configured on external interfaces. <additional configuration> } } If Proxy ARP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000364-RTR-000113

**Group ID:** `V-254049`

### Rule: The Juniper perimeter router must be configured to block all outbound management traffic.

**Rule ID:** `SV-254049r844180_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For in-band management, the management network must have its own subnet to enforce control and access boundaries provided by layer 3 network nodes, such as routers and firewalls. Management traffic between the managed network elements and the management network is routed via the same links and nodes as that used for production or operational traffic. Safeguards must be implemented to ensure that the management traffic does not leak past the perimeter of the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. The perimeter router of the managed network must be configured with a firewall filter on the egress interface to block all management traffic. [edit firewall] family inet { filter <name> { term block-UDP-MGT-SRC { from { protocol udp; source-port [ snmp snmptrap 2055 9995 9996 ]; } then { syslog; discard; } } term block-TCP-MGT-SRC { from { protocol tcp; source-port [ ssh tacacs ]; } then { syslog; discard; } } term block-UDP-MGT-DST { from { protocol udp; destination-port [ snmp snmptrap 2055 9995 9996 ]; } then { syslog; discard; } } term block-TCP-MGT-DST { from { protocol tcp; destination-port [ ssh tacacs ]; } then { syslog; discard; } } <additional terms> term accept-other { then accept; } } } family inet6 { filter <name> { term block-UDP-MGT-SRC { from { next-header udp; source-port [ snmp snmptrap 2055 9995 9996 ]; } then { syslog; discard; } } term block-TCP-MGT-SRC { from { next-header tcp; source-port [ ssh tacacs ]; } then { syslog; discard; } } term block-UDP-MGT-DST { from { next-header udp; destination-port [ snmp snmptrap 2055 9995 9996 ]; } then { syslog; discard; } } term block-TCP-MGT-DST { from { next-header tcp; destination-port [ ssh tacacs ]; } then { syslog; discard; } } <additional terms> term accept-other { then accept; } } } Note: Some platforms support the "port" match criterion. For those platforms, only a single term is required to flag on both source- and destination-port. For example: [edit firewall] family [inet|inet6] { filter <name> { term <name> { from { : port [ port1 port2... ]; } then { syslog; discard; } } <additional terms> } } Verify the filter is applied to external interfaces. [edit interfaces] <external interface> { unit <number> { family inet { filter { output <name>; } address <IPv4 address>/<mask>; } family inet6 { filter { output <name>; } address <IPv6 address>/<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If management traffic is not blocked at the perimeter, this is a finding.

## Group: SRG-NET-000364-RTR-000114

**Group ID:** `V-254050`

### Rule: The Juniper multicast Designated Router (DR) must be configured to filter the IGMP and MLD Report messages to allow hosts to join only multicast groups that have been approved by the organization.

**Rule ID:** `SV-254050r844262_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone downloading a file here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is filtering IGMP or MLD report messages, allowing hosts to join only those groups that have been approved. Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. This requirement is not applicable to Any Source Multicast (ASM) since the filtering is being performed by the Rendezvous Point router. [edit policy-options] policy-statement <name> { term unauth-groups { from { route-filter 224.0.1.2/32 exact; route-filter 224.0.2.2/32 exact; } then reject; } term allow-others { then accept; } } policy-statement <name IPv6> { term unauth-groups { from { route-filter fec0:1:1:4::/64 exact; } then reject; } term allow-others { then accept; } } [edit protocols] igmp { interface <name>.<logical unit> { group-policy <policy name>; } } mld { interface <name>.<logical unit> { group-policy <policy name IPv6>; } } If the DR is not filtering IGMP or MLD report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000115

**Group ID:** `V-254051`

### Rule: The Juniper multicast Designated Router (DR) must be configured to filter the IGMP and MLD Report messages to allow hosts to join a multicast group only from sources that have been approved by the organization.

**Rule ID:** `SV-254051r844263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone downloading a file here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is filtering IGMP or MLD report messages, allowing hosts to only join multicast groups from sources that have been approved. Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. [edit policy-options] policy-statement <name> { term unauth-sources { from { source-address-filter <IPv4 address>/<mask> orlonger; } then reject; } term allow-others { then accept; } } policy-statement <name IPv6> { term unauth-sources { from { source-address-filter <IPv6 address>/<prefix> orlonger; } then reject; } term allow-others { then accept; } } [edit protocols] igmp { interface <name>/<logical unit> { group-policy <policy name>; } } mld { interface <name>/<logical unit> { group-policy <policy name IPv6>; } } If the DR is not filtering IGMP or MLD report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000116

**Group ID:** `V-254052`

### Rule: The Juniper Multicast Source Discovery Protocol (MSDP) router must be configured to only accept MSDP packets from known MSDP peers.

**Rule ID:** `SV-254052r844189_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network routers presents additional risks to the DISN Core, whether from a rogue or misconfigured MSDP-enabled router. To guard against an attack from malicious MSDP traffic, the receive path or interface filter for all MSDP-enabled RP routers must be configured to only accept MSDP packets from known MSDP peers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if there is a receive path or interface filter to only accept MSDP packets from known MSDP peers. [edit firewall] family inet { filter <name> { term 1 { from { source-prefix-list { msdp-peers; } protocol tcp; destination-port msdp; } then accept; } term 2 { from { source-prefix-list { msdp-peers; } protocol tcp; source-port msdp; } then accept; } <additional terms> term default { then { syslog; discard; } } } } family inet6 { filter <name> { term 1 { from { source-prefix-list { msdp-peers-ipv6; } next-header tcp; destination-port msdp; } then accept; } term 2 { from { source-prefix-list { msdp-peers-ipv6; } next-header tcp; source-port msdp; } then accept; } <additional terms> term default { then { syslog; discard; } } } } Note: Some platforms support the "port" keyword that filters on both source- and destination-port, which eliminates the need for separate terms. For instance: filter <name> { term 1 { from { source-prefix-list { <prefix list name>; } [protocol|next-header] tcp; port msdp; } then accept; } <additional terms> term default { then { syslog; discard; } } } Verify the filter is applied to external interfaces or loopback. [edit interfaces] <external interface> { unit <number> { family inet { filter { input <IPv4 filter name>; } address <IPv4 address>/<mask>; } family inet6 { filter { input <IPv6 filter name>; } address <IPv6 address>/<prefix>; } } } lo0 { unit <number> { family inet { filter { input <IPv4 filter name>; } address <IPv4 address>/32; } family inet6 { filter { input <IPv6 filter name>; } address <IPv6 address>/128; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to only accept MSDP packets from known MSDP peers, this is a finding.

## Group: SRG-NET-000364-RTR-000200

**Group ID:** `V-254053`

### Rule: The Juniper perimeter router must be configured to drop fragmented IPv6 packets where the first fragment does not include the entire IPv6 header chain.

**Rule ID:** `SV-254053r844192_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One of the fragmentation weaknesses known in IPv6 is the "undetermined transport" packet, which is the first fragment where the entire IPv6 header chain is not included. Fragmenting IPv6 datagrams and not including the upper-layer header makes it difficult to identify the traffic. RFC7112 and RFC8200 require the entire IPv6 header chain be present in the first fragment and defines the header chain as: "The IPv6 Header Chain contains an initial IPv6 header, zero or more IPv6 Extension Headers, and optionally, a single upper-layer header. If an upper-layer header is present, it terminates the header chain; otherwise, the "No Next Header" value (Next Header = 59) terminates it." Both RFCs consider a second IPv6 header and an ESP header as "upper-layer headers" when determining where the IPv6 header chain terminates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. There is no check for dropping RFC 7112 nonconformant fragmented IPv6 packets because Juniper EX switches drop these packets without offering or requiring a configurable option in the CLI. Review the router configuration to determine if it is configured to drop fragmented transit IPv6 traffic. [edit firewall family inet6] filter <filter name> { term <name> { from { next-header fragment; } then { syslog; discard; } } } Note: Some platforms also support "is-fragment" or "fragment-flags is-fragment" in addition to "next-header fragment" as shown in the example. If the router is not configured to drop first-fragment IPv6 packets without the entire header chain, this is a finding.

## Group: SRG-NET-000364-RTR-000201

**Group ID:** `V-254054`

### Rule: The Juniper perimeter router must be configured drop IPv6 packets with a Routing Header type 0, 1, or 3255.

**Rule ID:** `SV-254054r844195_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The routing header can be used maliciously to send a packet through a path where less robust security is in place, rather than through the presumably preferred path of routing protocols. Use of the routing extension header has few legitimate uses other than as implemented by Mobile IPv6. The Type 0 Routing Header (RFC 5095) is dangerous because it allows attackers to spoof source addresses and obtain traffic in response, rather than the real owner of the address. Secondly, a packet with an allowed destination address could be sent through a Firewall using the Routing Header functionality, only to bounce to a different node once inside. The Type 1 Routing Header is defined by a specification called "Nimrod Routing", a discontinued project funded by DARPA. Assuming that most implementations will not recognize the Type 1 Routing Header, it must be dropped. The Type 3–255 Routing Header values in the routing type field are currently undefined and should be dropped inbound and outbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if it is configured to drop IPv6 packets containing a Routing Header of type 0, 1, or 3–255. [edit firewall family inet6] filter <name> { term 1 { from { next-header routing; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for Routing extension headers. Therefore, all packets with the Routing extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing a Routing Header of type 0, 1, or 3–255, this is a finding.

## Group: SRG-NET-000364-RTR-000202

**Group ID:** `V-254055`

### Rule: The Juniper perimeter router must be configured to drop IPv6 packets containing a Hop-by-Hop header with invalid option type values.

**Rule ID:** `SV-254055r844198_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These options are intended to be for the Destination Options header only. The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize and hence could cause a denial-of-service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if filters are bound to the applicable interfaces to drop IPv6 packets containing a Hop-by-Hop header with option type values of 0x04 (Tunnel Encapsulation Limit), 0xC9 (Home Address Destination), or 0xC3 (NSAP Address). [edit firewall family inet6] filter <name> { term 1 { from { next-header [ hop-by-hop dstopts ]; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for Hop-by-Hop or Destination Options extension headers. Therefore, all packets with the Hop-by-Hop or Destination Options extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing a Hop-by-Hop header with invalid option type values, this is a finding.

## Group: SRG-NET-000364-RTR-000203

**Group ID:** `V-254056`

### Rule: The Juniper perimeter router must be configured to drop IPv6 packets containing a Destination Option header with invalid option type values.

**Rule ID:** `SV-254056r844201_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These options are intended to be for the Hop-by-Hop header only. The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize. Hence, this could cause a denial-of-service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration and determine if filters are bound to the external interfaces to drop IPv6 packets containing a Destination Option header with option type values of 0x05 (Router Alert) or 0xC2 (Jumbo Payload). [edit firewall family inet6] filter <name> { term 1 { from { next-header [ hop-by-hop dstopts ]; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for Hop-by-Hop or Destination Options extension headers. Therefore, all packets with the Hop-by-Hop or Destination Options extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing a Destination Option header with invalid option type values, this is a finding.

## Group: SRG-NET-000364-RTR-000204

**Group ID:** `V-254057`

### Rule: The Juniper perimeter router must be configured to drop IPv6 packets containing an extension header with the Endpoint Identification option.

**Rule ID:** `SV-254057r844204_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a denial-of-service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. This option type is associated with the Nimrod Routing system and has no defining RFC document.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router switch configuration and determine if filters are bound to the applicable interfaces to drop IPv6 packets containing an option type values of 0x8A (Endpoint Identification) regardless of whether it appears in a Hop-by-Hop or Destination Option header. [edit firewall family inet6] filter <name> { term 1 { from { next-header [ hop-by-hop dstopts ]; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for Hop-by-Hop or Destination Options extension headers. Therefore, all packets with the Hop-by-Hop or Destination Options extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing an extension header with the Endpoint Identification option, this is a finding.

## Group: SRG-NET-000364-RTR-000205

**Group ID:** `V-254058`

### Rule: The Juniper perimeter router must be configured to drop IPv6 packets containing the NSAP address option within Destination Option header.

**Rule ID:** `SV-254058r844207_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a denial-of-service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. This option type from RFC 1888 (OSI NSAPs and IPv6) has been deprecated by RFC 4048.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration and determine if filters are bound to the applicable interfaces to drop IPv6 packets containing a Destination Option header with option type value of 0xC3 (NSAP address). Verify the router drops all destination-options extension headers. [edit firewall family inet6] filter <name> { term 1 { from { next-header dstopts; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for Destination Options extension headers. Therefore, all packets with the Destination Options extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing the NSAP address option within Destination Option header, this is a finding.

## Group: SRG-NET-000364-RTR-000206

**Group ID:** `V-254059`

### Rule: The Juniper perimeter router must be configured to drop IPv6 packets containing a Hop-by-Hop or Destination Option extension header with an undefined option type.

**Rule ID:** `SV-254059r844210_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a denial-of-service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration and determine if filters are bound to the applicable interfaces to drop all inbound IPv6 packets containing an undefined option type value regardless of whether they appear in a Hop-by-Hop or Destination Option header. Undefined values are 0x02, 0x03, 0x06, 0x9 – 0xE, 0x10 – 0x22, 0x24, 0x25, 0x27 – 0x2F, and 0x31 – 0xFF. Verify the router drops all hop-by-hop and destination-options extension headers. [edit firewall family inet6] filter <name> { term 1 { from { next-header [ hop-by-hop dstopts ]; } then { log; syslog; discard; } } <additional terms> term default { then { log; syslog; discard; } } } Note: Juniper routers do not support configuring option types for either the Hop-by-Hop or Destination Options extension headers. Therefore, all packets with the Hop-by-Hop or Destination Options extension header are dropped. Verify the filter is applied to applicable interfaces. [edit interfaces] <interface name> { unit <number> { family inet6 { filter { input <filter name>; } address <IPv6 address>.<prefix>; } } } Note: Some Juniper devices support both monolithic filters and filter lists. Filter lists separate each term, or set of terms, into a separate filter that is applied sequentially to an interface. If using filter lists, the keywords "input" or "output" change to "input-list" or "output-list". Verify the final list item is a deny-all filter. The deny-all filter is created once per family and can be reused across multiple lists. For example: input-list [ permit_mgt permit_routing_protocols default-deny ]; If the router is not configured to drop IPv6 packets containing a Hop-by-Hop or Destination Option extension header, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-254060`

### Rule: The Juniper BGP router must be configured to use its loopback address as the source address for iBGP peering sessions.

**Rule ID:** `SV-254060r844213_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the BGP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router’s loopback address instead of the numerous physical interface addresses. When the loopback address is used as the source for eBGP peering, the BGP session will be harder to hijack since the source address to be used is not known globally—making it more difficult for a hacker to spoof an eBGP neighbor. By using traceroute, a hacker can easily determine the addresses for an eBGP speaker when the IP address of an external interface is used as the source address. The routers within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that a loopback address has been configured. Verify that a loopback interface is used as the source address for all iBGP sessions. bgp { group iBGP { type internal; local-interface lo0.0; : } } If the router does not use its loopback address as the source address for all iBGP sessions, this is a finding.

## Group: SRG-NET-000512-RTR-000002

**Group ID:** `V-254061`

### Rule: The Juniper MPLS router must be configured to use its loopback address as the source address for LDP peering sessions.

**Rule ID:** `SV-254061r844216_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of backbone routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of from a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router's loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to determine if it uses its loopback address as the source address for LDP peering sessions. Verify that a loopback address has been configured as shown in the following example: [edit interfaces] lo0 { unit 0 { family inet { address <IPv4 address>/32; } family inet6 { address <IPv6 address>/128; } } } An MPLS router will use the LDP router ID as the source address for LDP hellos and when establishing TCP sessions with LDP peers; hence, it is necessary to verify that the LDP router ID is the same as the loopback address. By default, routers will assign the LDP router ID using the highest IP address on the router, with preference given to loopback addresses. If the router-id command is specified that overrides this default behavior, verify that it is the IP address of the designated loopback interface. [edit routing-options] router-id <lo0 address>; If the router is not configured do use its loopback address for LDP peering, this is a finding.

## Group: SRG-NET-000512-RTR-000003

**Group ID:** `V-254062`

### Rule: The Juniper MPLS router must be configured to synchronize IGP and LDP to minimize packet loss when an IGP adjacency is established prior to LDP peers completing label exchange.

**Rule ID:** `SV-254062r844219_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Packet loss can occur when an IGP adjacency is established and the router begins forwarding packets using the new adjacency before the LDP label exchange completes between the peers on that link. Packet loss can also occur if an LDP session closes and the router continues to forward traffic using the link associated with the LDP peer rather than an alternate pathway with a fully synchronized LDP session. The MPLS LDP-IGP Synchronization feature provides a means to synchronize LDP with OSPF or IS-IS to minimize MPLS packet loss. When an IGP adjacency is established on a link but LDP-IGP synchronization is not yet achieved or is lost, the IGP will advertise the max-metric on that link.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router OSPF or IS-IS configuration. Verify that LDP will synchronize with the link-state routing protocol. [edit protocols] ospf { area <number> { interface <name>.<logical unit> { authentication { md5 <key number> key "$8$aes256-gcm$hmac-sha2-256$100$LfJ7NdAYx/0$+4wGg1QJKLzkaAmVCGxBUQ$n0XxNofUtXE8aoJBhFNDDQ$uIDW/H+VY6U"; ## SECRET-DATA } ldp-synchronization { hold-time 10; } } interface <name>.<logical unit> { ipsec-sa <name>; ldp-synchronization { hold-time 10; } } } } ldp { interface <name>.<logical unit>; } -OR- isis { interface <name>.<logical unit> { ldp-synchronization { hold-time 10; } } level 1 authentication-key-chain <name>; level 2 authentication-key-chain <name>; } mpls { interface <name>.<logical unit>; } If the router is not configured to synchronize IGP and LDP, this is a finding.

## Group: SRG-NET-000512-RTR-000004

**Group ID:** `V-254063`

### Rule: The Juniper MPLS router must be configured to have TTL Propagation disabled.

**Rule ID:** `SV-254063r844222_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The head end of the label-switched path (LSP), the label edge router (LER) will decrement the IP packet's time-to-live (TTL) value by one and then copy the value to the MPLS TTL field. At each label-switched router (LSR) hop, the MPLS TTL value is decremented by one. The MPLS router that pops the label (either the penultimate LSR or the egress LER) will copy the packet's MPLS TTL value to the IP TTL field and decrement it by one. This TTL propagation is the default behavior. Because the MPLS TTL is propagated from the IP TTL, a traceroute will list every hop in the path, be it routed or label switched, thereby exposing core nodes. With TTL propagation disabled, LER decrements the IP packet's TTL value by one and then places a value of 255 in the packet's MPLS TTL field, which is then decremented by one as the packet passes through each LSR in the MPLS core. Because the MPLS TTL never drops to zero, none of the LSP hops triggers an ICMP TTL exceeded message and consequently, these hops are not recorded in a traceroute. Hence, nodes within the MPLS core cannot be discovered by an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that TTL propagation is disabled. [edit protocols mpls] no-propagate-ttl; If the router is not configured to disable TTL propagation, this is a finding.

## Group: SRG-NET-000512-RTR-000005

**Group ID:** `V-254064`

### Rule: The Juniper PE router must be configured to have each Virtual Routing and Forwarding (VRF) instance bound to the appropriate physical or logical interfaces to maintain traffic separation between all MPLS L3VPNs.

**Rule ID:** `SV-254064r844225_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The primary security model for an MPLS L3VPN infrastructure is traffic separation. The service provider must guarantee the customer that traffic from one VPN does not leak into another VPN or into the core, and that core traffic must not leak into any VPN. Hence, it is imperative that each CE-facing interface can only be associated to one VRF—that alone is the fundamental framework for traffic separation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the design plan for deploying L3VPN and VRF-lite. Review all CE-facing interfaces and verify that the proper VRF is defined. [edit interfaces] <ce-facing interface> { description "To customer 1"; unit <number> { family inet { address <IPv4 address>/<mask>; } family inet6 { address <IPv6 address>/<prefix>; } } } [edit routing-instances] <instance name> { description "To customer 1"; instance-type vrf; interface <ce-facing interface>.<logical unit>; route-distinguisher <Number in (16 bit:32 bit) or (32 bit 'L':16 bit) or (IP address:16 bit) format>; vrf-target <Target community to use in import and export>; vrf-table-label; protocols { ospf { area <number> { interface <ce-facing interface>.<logical unit>; } } } } Note: In L3 VPN, the CE router forms an adjacency with the PE router (OSPF in the example). If any VRFs are not bound to the appropriate physical or logical interface, this is a finding.

## Group: SRG-NET-000512-RTR-000006

**Group ID:** `V-254065`

### Rule: The Juniper PE router must be configured to have each Virtual Routing and Forwarding (VRF) instance with the appropriate Route Target (RT).

**Rule ID:** `SV-254065r844228_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The primary security model for an MPLS L3VPN as well as a VRF-lite infrastructure is traffic separation. Each interface can only be associated to one VRF, which is the fundamental framework for traffic separation. Forwarding decisions are made based on the routing table belonging to the VRF. Control of what routes are imported into or exported from a VRF is based on the RT. It is critical that traffic does not leak from one COI tenant or L3VPN to another; hence, it is imperative that the correct RT is configured for each VRF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the correct RT is configured for each VRF. Review the design plan for MPLS/L3VPN and VRF-lite to determine what RTs have been assigned for each VRF. Review the route-distinguisher and vrf-target statements under each configured VRF and verify that the correct RTs have been defined for each VRF. Assuming the assigned RT for "customer 1" is "cust1:33:33", verify vrf-target matches. [edit routing-instances] <instance name> { description "To customer 1"; instance-type vrf; interface <ce-facing interface>.<logical unit>; route-distinguisher 33:33; << Must match the design plan for "customer 1". vrf-target cust1:33:33; << Must match the design plan for "customer 1". vrf-table-label; protocols { ospf { area <number> { interface <ce-facing interface>.<logical unit>; } } } } Note: In L3 VPN, the CE router forms an adjacency with the PE router (OSPF in the example). If there are VRFs configured with the wrong RT, this is a finding.

## Group: SRG-NET-000512-RTR-000007

**Group ID:** `V-254066`

### Rule: The Juniper PE router must be configured to have each VRF with the appropriate Route Distinguisher (RD).

**Rule ID:** `SV-254066r844231_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An RD provides uniqueness to the customer address spaces within the MPLS L3VPN infrastructure. The concept of the VPN-IPv4 and VPN-IPv6 address families consists of the RD prepended before the IP address. Hence, if the same IP prefix is used in several different L3VPNs, it is possible for BGP to carry several completely different routes for that prefix, one for each VPN. Since VPN-IPv4 addresses and IPv4 addresses are different address families, BGP never treats them as comparable addresses. The purpose of the RD is to create distinct routes for common IPv4 address prefixes. On any given PE router, a single RD can define a VRF in which the entire address space may be used independently, regardless of the makeup of other VPN address spaces. Hence, it is imperative that a unique RD is assigned to each L3VPN and that the proper RD is configured for each VRF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the RDs that have been assigned for each VRF according to the plan provided by the ISSM. Review all VRFs configured on CE-facing interfaces and verify that the proper RD has been configured for each. Assuming the assigned RD for "customer 1" is "33:33", verify the route-distinguisher matches. [edit routing-instances] <instance name> { description "To customer 1"; instance-type vrf; interface <ce-facing interface>.<logical unit>; route-distinguisher 33:33; << Must match the design plan for "customer 1". vrf-target cust1:33:33; << Must match the design plan for "customer 1". vrf-table-label; protocols { ospf { area <number> { interface <ce-facing interface>.<logical unit>; } } } } Note: In L3 VPN, the CE router forms an adjacency with the PE router (OSPF in the example). If the wrong RD has been configured for any VRF, this is a finding.

## Group: SRG-NET-000512-RTR-000008

**Group ID:** `V-254067`

### Rule: The Juniper PE router providing MPLS Virtual Private Wire Service (VPWS) must be configured to have the appropriate virtual circuit identification (VC ID) for each attachment circuit.

**Rule ID:** `SV-254067r844234_rule`
**Severity:** high

**Description:**
<VulnDiscussion>VPWS is an L2VPN technology that provides a virtual circuit between two PE routers to forward layer 2 frames between two customer-edge routers or switches through an MPLS-enabled IP core. The ingress PE router (virtual circuit head-end) encapsulates Ethernet frames inside MPLS packets using label stacking and forwards them across the MPLS network to the egress PE router (virtual circuit tail-end). During a virtual circuit setup, the PE routers exchange VC label bindings for the specified VC ID. The VC ID specifies a pseudowire associated with an ingress and egress PE router and the customer-facing attachment circuits. To guarantee that all frames are forwarded onto the correct pseudowire and to the correct customer and attachment circuits, it is imperative that the correct VC ID is configured for each attachment circuit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the ingress and egress PE router configuration for each virtual circuit that has been provisioned. Verify that the correct and unique VCID has been configured for the appropriate attachment circuit. [edit interfaces] <interface name> { encapsulation ethernet-ccc; unit <number> { <additional configuration> } } [edit protocols] l2circuit { neighbor 1.1.1.1 { interface <interface name>.<logical unit> { virtual-circuit-id <1..4294967295>; } } } If the correct VC ID has not been configured on both routers, this is a finding. Note: Ethernet over MPLS in VLAN mode transports Ethernet traffic from a source 802.1Q VLAN to a destination 802.1Q VLAN over a core MPLS network. The VC ID must be unique and the same on each end as it is used to connect the endpoints of the VC.

## Group: SRG-NET-000512-RTR-000009

**Group ID:** `V-254068`

### Rule: The Juniper PE router providing Virtual Private LAN Services (VPLS) must be configured to have all attachment circuits defined to the virtual forwarding instance (VFI) with the globally unique VPN ID assigned for each customer VLAN.

**Rule ID:** `SV-254068r844237_rule`
**Severity:** high

**Description:**
<VulnDiscussion>VPLS defines an architecture that delivers Ethernet multipoint services over an MPLS network. Customer layer 2 frames are forwarded across the MPLS core via pseudowires using IEEE 802.1q Ethernet bridging principles. A pseudowire is a virtual bidirectional connection between two attachment circuits (virtual connections between PE and CE routers). A pseudowire contains two unidirectional label-switched paths (LSP) between two PE routers. Each MAC virtual forwarding table instance (VFI) is interconnected using pseudowires provisioned for the bridge domain, thereby maintaining privacy and logical separation between each VPLS bridge domain. The VFI specifies the pseudowires associated with connecting PE routers and the customer-facing attachment circuits belonging to a given VLAN. Resembling a layer 2 switch, the VFI is responsible for learning MAC addresses and providing loop-free forwarding of customer traffic to the appropriate end nodes. Each VPLS domain is identified by a globally unique VPN ID; hence, VFIs of the same VPLS domain must be configured with the same VPN ID on all participating PE routers. To guarantee traffic separation for all customer VLANs and that all packets are forwarded to the correct destination, it is imperative that the correct attachment circuits are associated with the appropriate VFI and that each VFI is associated to the unique VPN ID assigned to the customer VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the implementation plan and the VPN IDs assigned to customer VLANs for the VPLS deployment. Review the PE router configuration to verify that customer attachment circuits (i.e., VLANs) are associated to the appropriate VPLS ID. Review the implementation plan and the VPLS IDs assigned to customer VLANs for the VPLS deployment. Review the PE router configuration to verify that customer attachment circuits are associated to the appropriate routing instance configured for the customers VPLS ID. [edit] routing-instances { <instance name> { interface <interface name>.<logical unit>; protocols { vpls { vpls-id <VPLS ID>; neighbor <neighbor address>; } } } } } Note: Only EX9200-series devices currently support VPLS. If the attachment circuits have not been bound to the appropriate routing-instance with the assigned VPN ID for each associated VLAN, this is a finding.

## Group: SRG-NET-000512-RTR-000010

**Group ID:** `V-254069`

### Rule: The Juniper PE router must be configured to enforce the split-horizon rule for all pseudowires within a Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-254069r844240_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A virtual forwarding instance (VFI) must be created on each participating PE router for each customer VLAN using VPLS for carrier Ethernet services. The VFI specifies the VPN ID of a VPLS domain, the addresses of other PE routers in the domain, and the type of tunnel signaling and encapsulation mechanism for each peer PE router. The set of VFIs formed by the interconnection of the emulated VCs is called a VPLS instance, which forms the logic bridge over the MPLS core network. The PE routers use the VFI with a unique VPN ID to establish a full mesh of emulated virtual circuits or pseudowires to all the other PE routers in the VPLS instance. The full-mesh configuration allows the PE router to maintain a single broadcast domain. With a full-mesh configuration, signaling and packet replication requirements for each provisioned virtual circuit on a PE can be high. To avoid the problem of a packet looping in the provider core, thereby adding more overhead, the PE devices must enforce a split-horizon principle for the emulated virtual circuits; that is, if a packet is received on an emulated virtual circuit, it is not forwarded on any other virtual circuit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE router configuration to verify that split horizon is enabled. By default, Juniper devices configured as PE routers and VPLS enforce split horizon operation. Except for H-VPLS, Juniper devices do not support disabling split horizon operation. LDP signaled VPLS requires a full mesh topology, which can lead to scaling issues. Hierarchical VPLS (H-VPLS) partitions the VPLS domains into mesh groups, reducing the required number of pseudo wires. However, the inner VPLS domain may require split horizon be disabled. Juniper devices support these scenarios with the "local-switching" command. Ensure mesh groups supporting H-VPLS do not have the "local-switching" directive enabled, unless required, as shown in the following example. Generally, only inner mesh groups (that is, a group "nested" within another) may require split horizon be disabled. [edit routing-instances <name> protocols vpls] mesh-group <name> { : local-switching; : } Note: Only EX9200-series devices currently support VPLS. If split horizon is disabled but not required to be, this is a finding. Note: In a ring VPLS, split horizon is disabled so that a PE router can forward a packet received from one pseudowire to another pseudowire. To prevent the consequential loop, at least one span in the ring would not have a pseudowire for any given VPLS instance.

## Group: SRG-NET-000512-RTR-000011

**Group ID:** `V-254070`

### Rule: The Juniper Multicast Source Discovery Protocol (MSDP) router must be configured to use its loopback address as the source address when originating MSDP traffic.

**Rule ID:** `SV-254070r844243_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of MSDP routers. It is easier to construct appropriate ingress filters for router management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the router’s loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to verify that a loopback address has been configured. Verify that a loopback interface is used as the source address for all MSDP packets generated by the router. [edit protocols] msdp { active-source-limit { maximum <1..1000000>; threshold <1..1000000>; log-warning <percent to log warning>; } local-address <lo0 address>; <additional configuration> peer <address> { active-source-limit { maximum <1..1000000>; threshold <1..1000000>; log-warning <percent to log warning>; } authentication-key "hashed PSK"; ## SECRET-DATA } } Note: Both the global, and the peer limit, are applied to every MSDP peer, and Junos applies the most restrictive limit. The maximum value sets the upper limit for source-active messages and the threshold value determines when Junos begins Random Early Detection (RED) dropping to alleviate congestion. The log-warning value is a percent where Junos begins generating syslog messages. If the router does not use its loopback address as the source address when originating MSDP traffic, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-254071`

### Rule: The Juniper router must be configured to advertise a hop limit of at least 32 in Router Advertisement messages for IPv6 stateless auto-configuration deployments.

**Rule ID:** `SV-254071r844246_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to determine if the hop limit has been configured for Router Advertisement messages. Verify each interface configured for router advertisements contains a hop limit of at least 32. [edit protocols] router-advertisement { interface ge-0/0/0.0 { : current-hop-limit 32; <<< Supported values: 0 - 255 : } } If it has been configured and has not been set to at least 32, it is a finding.

## Group: SRG-NET-000512-RTR-000013

**Group ID:** `V-254072`

### Rule: The Juniper router must not be configured to use IPv6 Site Local Unicast addresses.

**Rule ID:** `SV-254072r844249_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As currently defined, site local addresses are ambiguous and can be present in multiple sites. The address itself does not contain any indication of the site to which it belongs. The use of site-local addresses has the potential to adversely affect network security through leaks, ambiguity, and potential misrouting as documented in section 2 of RFC3879. RFC3879 formally deprecates the IPv6 site-local unicast prefix FEC0::/10 as defined in RFC3513.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the router configuration to ensure FEC0::/10 IP addresses are not defined. Show the interface configuration using "show configuration interfaces" (from operational mode) or "show interfaces" (configuration mode at the top of the hierarchy). When showing the configuration, piping (|) to match or find (similar to *nix 'grep') will limit the search. For example, to limit the search to lines that include "FEC0": (operational mode) show configuration interfaces | match fec0 Returns the lines with 'fec0' but no surrounding context There should be no returned lines (operational mode) show configuration interfaces | find fec0 Returns the configuration with the first line containing 'fec0' Returns context (meaning can scroll up / down in the configuration) There should be no returned configuration If IPv6 Site Local Unicast addresses are defined, this is a finding.

## Group: SRG-NET-000512-RTR-000014

**Group ID:** `V-254073`

### Rule: The Juniper perimeter router must be configured to suppress Router Advertisements on all external IPv6-enabled interfaces.

**Rule ID:** `SV-254073r844252_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many of the known attacks in stateless autoconfiguration are defined in RFC 3756 were present in IPv4 ARP attacks. To mitigate these vulnerabilities, links that have no hosts connected such as the interface connecting to external gateways must be configured to suppress router advertisements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the router configuration to verify Router Advertisements are suppressed on all external IPv6-enabled interfaces. By default, IPv6 router advertisements are disabled. Verify all configured interfaces are not external facing. [edit protocols] router-advertisement { interface <internal interface>.<logical unit> { managed-configuration; : : prefix <internal IPv6 prefix>; } } If the router is not configured to suppress Router Advertisements on all external IPv6-enabled interfaces, this is a finding.

## Group: SRG-NET-000512-RTR-000100

**Group ID:** `V-254074`

### Rule: The Juniper router must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-254074r844255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network device to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network device. Security-related parameters are those parameters impacting the security state of the network device, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the router is configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs. If it is not configured in accordance with the designated security configuration settings, this is a finding.

