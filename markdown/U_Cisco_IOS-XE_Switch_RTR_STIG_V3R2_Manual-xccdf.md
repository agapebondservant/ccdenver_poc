# STIG Benchmark: Cisco IOS XE Switch RTR Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-RTR-000001

**Group ID:** `V-220986`

### Rule: The Cisco switch must be configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies.

**Rule ID:** `SV-220986r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, and devices) within information systems. Enforcement occurs, for example, in boundary protection devices (e.g., gateways, switches, guards, encrypted tunnels, and firewalls) that employ rule sets or establish configuration settings that restrict information system services, provide a packet-filtering capability based on header information, or provide a message-filtering capability based on message content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that ACLs are configured to allow or deny traffic for specific source and destination addresses as well as ports and protocols. For example, the configuration below will allow only printer traffic into subnet 10.1.12.0/24 and SQL traffic into subnet 10.1.13.0/24. ICMP is allowed for troubleshooting and OSPF is the routing protocol used within the network. interface GigabitEthernet0/1 no switchport ip address 10.2.1.1 255.255.255.252 ip access-group FILTER_SERVER_TRAFFIC in … … … ip access-list extended FILTER_SERVER_TRAFFIC permit tcp any 10.1.12.0 0.0.0.255 eq lpd 631 9100 permit tcp any 10.1.13.0 0.0.0.255 eq 1433 1434 4022 permit icmp any any permit ospf any any deny ip any any Alternate: Inter-VLAN routing interface Vlan12 ip address 10.1.12.1 255.255.255.0 ip access-group FILTER_PRINTER_VLAN out ! interface Vlan13 ip address 10.1.13.1 255.255.255.0 ip access-group FILTER_SQL_VLAN out … … … ip access-list extended FILTER_PRINTER_VLAN permit tcp any any eq lpd 631 9100 permit icmp any any deny ip any any ip access-list extended FILTER_SQL_VLAN permit tcp any any eq 1433 1434 4022 permit icmp any any deny ip any any If the switch is not configured to enforce approved authorizations for controlling the flow of information within the network based on organization-defined information flow control policies, this is a finding.

## Group: SRG-NET-000168-RTR-000078

**Group ID:** `V-220990`

### Rule: The Cisco switch must be configured to enable routing protocol authentication using FIPS 198-1 algorithms with keys not exceeding 180 days of lifetime.

**Rule ID:** `SV-220990r929064_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network or used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication using FIPS 198-1 algorithms for routing updates. If the keys used for authentication are guessed, the malicious user could create havoc within the network by advertising incorrect routes and redirecting traffic. Some routing protocols allow the use of key chains for authentication. A key chain is a set of keys that is used in succession, with each having a lifetime of no more than 180 days. Changing the keys frequently reduces the risk of them eventually being guessed. If a time period occurs during which no key is activated, neighbor authentication cannot occur, and therefore routing updates will fail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration using the configuration examples below for BGP and OSPF. EIGRP, RIP, and IS-IS only support MD5 and will incur a permanent finding for those protocols. Note: The 180-day key lifetime is Not Applicable for the DODIN Backbone. The remainder of the requirement still applies. Verify that neighbor router authentication is enabled for all routing protocols. If neighbor authentication is not enabled this is a finding. Verify that authentication is configured to use FIPS 198-1 message authentication algorithms. If the routing protocol authentication is not configured to use FIPS 198-1 algorithms this is a finding. Verify that the protocol key lifetime is configured to not exceed 180 days. If any protocol key lifetime is configured to exceed 180 days this is a finding. BGP Example: key chain <KEY-CHAIN-NAME> tcp key <KEY-ID> send-id <ID> recv-id <ID> cryptographic-algorithm hmac-sha256 key-string <KEY> accept-lifetime 00:00:00 Jan 1 2022 duration 180 send-lifetime 00:00:00 Jan 1 2022 duration 180 ! ! router bgp <ASN> no synchronization bgp log-neighbor-changes neighbor x.x.x.x remote-as <ASN> neighbor x.x.x.x ao <KEY-CHAIN-NAME> Note: TCP-AO is used to replace MD5 in BGP authentication. OSPF Example: key chain OSPF_KEY_CHAIN key 1 key-string xxxxxxx send-lifetime 00:00:00 Jan 1 2018 23:59:59 Mar 31 2018 accept-lifetime 00:00:00 Jan 1 2018 01:05:00 Apr 1 2018 cryptographic-algorithm hmac-sha-256 key 2 key-string yyyyyyy send-lifetime 00:00:00 Apr 1 2018 23:59:59 Jun 30 2018 accept-lifetime 23:55:00 Mar 31 2018 01:05:00 Jul 1 2018 cryptographic-algorithm hmac-sha-256 … … … interface GigabitEthernet0/1 ip address x.x.x.x 255.255.255.0 ip ospf authentication key-chain OSPF_KEY_CHAIN

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-220991`

### Rule: The Cisco switch must be configured to have all inactive layer 3 interfaces disabled.

**Rule ID:** `SV-220991r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a switch by connecting to a configured interface that is not in use. If an interface is no longer used, the configuration must be deleted and the interface disabled. For sub-interfaces, delete sub-interfaces that are on inactive interfaces and delete sub-interfaces that are themselves inactive. If the sub-interface is no longer necessary for authorized communications, it must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that inactive interfaces have been disabled as shown below: interface GigabitEthernet3 no switchport shutdown ! interface GigabitEthernet4 no switchport shutdown If an interface is not being used but is configured or enabled, this is a finding.

## Group: SRG-NET-000362-RTR-000109

**Group ID:** `V-220994`

### Rule: The Cisco switch must not be configured to have any zero-touch deployment feature enabled when connected to an operational network.

**Rule ID:** `SV-220994r856401_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices that are configured via a zero-touch deployment or auto-loading feature can have their startup configuration or image pushed to the device for installation via TFTP or Remote Copy (rcp). Loading an image or configuration file from the network is taking a security risk because the file could be intercepted by an attacker who could corrupt the file, resulting in a denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the device configuration to determine if auto-configuration or zero-touch deployment via Cisco Networking Services (CNS) is enabled. Auto-Configuration Example: version 15.0 service config … … … boot-start-marker boot network tftp://x.x.x.x/R5-config boot-end-marker CNS Zero-Touch Example: cns trusted-server config x.x.x.x cns trusted-server image x.x.x.x cns config initial x.x.x.x 80 cns exec 80 cns image If a configuration auto-loading feature or zero-touch deployment feature is enabled, this is a finding. Note: Auto-configuration or zero-touch deployment features can be enabled when the switch is offline for the purpose of image loading or building out the configuration. In addition, this would not be applicable to the provisioning of virtual switches via a software-defined network (SDN) orchestration system.

## Group: SRG-NET-000362-RTR-000110

**Group ID:** `V-220995`

### Rule: The Cisco switch must be configured to protect against or limit the effects of denial-of-service (DoS) attacks by employing control plane protection.

**Rule ID:** `SV-220995r1107540_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Route Processor (RP) is critical to all network operations because it is the component used to build all forwarding paths for the data plane via control plane processes. It is also instrumental with ongoing network management functions that keep the routers and links available for providing network services. Any disruption to the RP or the control and management planes can result in mission-critical network outages. A DoS attack targeting the RP can result in excessive CPU and memory utilization. To maintain network stability and RP security, the router must be able to handle specific control plane and management plane traffic that is destined to the RP. In the past, one method of filtering was to use ingress filters on forwarding interfaces to filter both forwarding path and receiving path traffic, as well as limiting traffic destined to the device. However, this method does not scale well as the number of interfaces grows and the size of the ingress filters grows. Control plane policing increases the security of routers and multilayer switches by protecting the RP from unnecessary or malicious traffic. Filtering and rate limiting the traffic flow of control plane packets can be implemented to protect routers against reconnaissance and DoS attacks, allowing the control plane to maintain packet forwarding and protocol states despite an attack or heavy load on the router or multilayer switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Cisco switch configuration to verify it is compliant with this requirement. Step 1: To verify that the CoPP policy map has been saved, issue the "show running-config" command in privileged EXEC mode and verify the following line exists in the output: policy-map system-cpp-policy Step 2: To view the policy map and verify the correct policer rates are set according to organization-defined standards, run the following command: show policy-map control-plane Note: Starting from Cisco IOS XE Fuji 16.8.1a, the creation of user-defined class-maps is not supported. A user can only enable/disable a CPU queue or change the policer rate of a CPU queue. If the Cisco switch is not configured to protect against known types of DoS attacks by employing organization-defined security safeguards, this is a finding.

## Group: SRG-NET-000362-RTR-000111

**Group ID:** `V-220998`

### Rule: The Cisco switch must be configured to have Gratuitous ARP disabled on all external interfaces.

**Rule ID:** `SV-220998r856403_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A gratuitous ARP is an ARP broadcast in which the source and destination MAC addresses are the same. It is used to inform the network about a host IP address. A spoofed gratuitous ARP message can cause network mapping information to be stored incorrectly, causing network malfunction.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to determine if gratuitous ARP is disabled. The following command should not be found in the switch configuration: ip gratuitous-arps Note: With Cisco IOS, Gratuitous ARP is enabled and disabled globally. If gratuitous ARP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000362-RTR-000112

**Group ID:** `V-220999`

### Rule: The Cisco switch must be configured to have IP directed broadcast disabled on all interfaces.

**Rule ID:** `SV-220999r856404_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An IP directed broadcast is a datagram sent to the broadcast address of a subnet that is not directly attached to the sending machine. The directed broadcast is routed through the network as a unicast packet until it arrives at the target subnet, where it is converted into a link-layer broadcast. Because of the nature of the IP addressing architecture, only the last switch in the chain, which is connected directly to the target subnet, can conclusively identify a directed broadcast. IP directed broadcasts are used in the extremely common and popular smurf, or denial-of-service (DoS), attacks. In a smurf attack, the attacker sends Internet Control Message Protocol (ICMP) echo requests from a falsified source address to a directed broadcast address, causing all the hosts on the target subnet to send replies to the falsified source. By sending a continuous stream of such requests, the attacker can create a much larger stream of replies, which can completely inundate the host whose address is being falsified. This service should be disabled on all interfaces when not needed to prevent smurf and DoS attacks. Directed broadcast can be enabled on internal facing interfaces to support services such as Wake-On-LAN. Case scenario may also include support for legacy applications where the content server and the clients do not support multicast. The content servers send streaming data using UDP broadcast. Used in conjunction with the IP multicast helper-map feature, broadcast data can be sent across a multicast topology. The broadcast streams are converted to multicast and vice versa at the first-hop switches and last-hop switches before entering and leaving the multicast transit area respectively. The last-hop switch must convert the multicast to broadcast. Hence, this interface must be configured to forward a broadcast packet (i.e., a directed broadcast address is converted to the all nodes broadcast address).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it is compliant with this requirement. IP directed broadcast command must not be found on any interface as shown in the example below: interface GigabitEthernet0/1 no switchport ip address x.x.x.x 255.255.255.0 ip directed-broadcast … … … Interface Vlan11 no switchport ip address x.x.x.x 255.255.255.0 ip directed-broadcast If IP directed broadcast is not disabled on all interfaces, this is a finding.

## Group: SRG-NET-000362-RTR-000113

**Group ID:** `V-221000`

### Rule: The Cisco switch must be configured to have Internet Control Message Protocol (ICMP) unreachable messages disabled on all external interfaces.

**Rule ID:** `SV-221000r856405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Switches automatically send ICMP messages under a wide variety of conditions. Host unreachable ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration to verify the no ip unreachables command has been configured on all external interfaces as shown in the configuration example below: interface GigabitEthernet0/1 ip address x.x.x.x 255.255.255.0 no ip unreachables If ICMP unreachable notifications are sent from any external or null0 interface, this is a finding. Alternative – DODIN Backbone: Verify that the PE switch is configured to rate limit ICMP unreachable messages as shown in the example below: ip icmp rate-limit unreachable 60000 ip icmp rate-limit unreachable DF 1000 Note: In the example above, packet-too-big message (ICMP Type 3 Code 4) can be sent once every second, while all other destination unreachable messages can be sent once every minute. This will avoid disrupting Path MTU Discovery for traffic traversing the backbone while mitigating the risk of an ICMP unreachable DoS attack. If the PE switch is not configured to rate limit ICMP unreachable messages, this is a finding.

## Group: SRG-NET-000362-RTR-000114

**Group ID:** `V-221001`

### Rule: The Cisco switch must be configured to have Internet Control Message Protocol (ICMP) mask reply messages disabled on all external interfaces.

**Rule ID:** `SV-221001r856406_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Switches automatically send ICMP messages under a wide variety of conditions. Mask Reply ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that ip mask-reply command is not enabled on any external interfaces as shown in the example below: interface GigabitEthernet0/1 ip address x.x.x.x 255.255.255.0 ip mask-reply If the ip mask-reply command is configured on any external interface, this is a finding.

## Group: SRG-NET-000362-RTR-000115

**Group ID:** `V-221002`

### Rule: The Cisco switch must be configured to have Internet Control Message Protocol (ICMP) redirect messages disabled on all external interfaces.

**Rule ID:** `SV-221002r856407_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ICMP supports IP traffic by relaying information about paths, routes, and network conditions. Switches automatically send ICMP messages under a wide variety of conditions. Redirect ICMP messages are commonly used by attackers for network mapping and diagnosis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that the no ip redirects command has been configured on all external interfaces as shown in the example below: interface GigabitEthernet0/1 ip address x.x.x.x 255.255.255.0 no ip redirects If ICMP Redirect messages are enabled on any external interfaces, this is a finding.

## Group: SRG-NET-000078-RTR-000001

**Group ID:** `V-221003`

### Rule: The Cisco switch must be configured to log all packets that have been dropped at interfaces via an ACL.

**Rule ID:** `SV-221003r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. It is essential for security personnel to know what is being done or attempted to be done, and by whom, to compile an accurate risk assessment. Auditing the actions on network devices provides a means to recreate an attack or identify a configuration mistake on the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all ACLs used to filter traffic and verify that packets being dropped at interfaces via an ACL are logged as shown in the configuration below: ip access-list extended INGRESS_FILTER permit tcp any any established permit tcp host x.11.1.1 eq bgp host x.11.1.2 permit tcp host x.11.1.1 host x.11.1.2 eq bgp permit tcp any host x.11.1.5 eq www permit icmp host x.11.1.1 host x.11.1.2 echo permit icmp any any echo-reply … … … deny ip any any log If packets being dropped are not logged, this is a finding.

## Group: SRG-NET-000076-RTR-000001

**Group ID:** `V-221004`

### Rule: The Cisco switch must be configured to produce audit records containing information to establish where the events occurred.

**Rule ID:** `SV-221004r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as switch components, modules, device identifiers, node names, and functionality. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that events are logged containing information to establish where the events occurred as shown in the example below: ip access-list extended INGRESS_FILTER permit tcp any any established permit tcp host x.11.1.1 eq bgp host x.11.1.2 permit tcp host x.11.1.1 host x.11.1.2 eq bgp permit tcp any host x.11.1.5 eq www permit icmp host x.11.1.1 host x.11.1.2 echo permit icmp any any echo-reply … … … deny ip any any log-input Note: When the log-input parameter is configured on deny statements, the log record will contain the interface where ingress packet has been dropped. If the switch is not configured to produce audit records containing information to establish to establish where the events occurred, this is a finding.

## Group: SRG-NET-000077-RTR-000001

**Group ID:** `V-221005`

### Rule: The Cisco switch must be configured to produce audit records containing information to establish the source of the events.

**Rule ID:** `SV-221005r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, security personnel need to know the source of the event. In addition to logging where events occur within the network, the audit records must also identify sources of events such as IP addresses, processes, and node or device names.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that events are logged containing information to establish the source of the events as shown in the example below: ip access-list extended INGRESS_FILTER permit tcp any any established permit tcp host x.11.1.1 eq bgp host x.11.1.2 permit tcp host x.11.1.1 host x.11.1.2 eq bgp permit tcp any host x.11.1.5 eq www permit icmp host x.11.1.1 host x.11.1.2 echo permit icmp any any echo-reply … … … deny ip any any log-input Note: When the log-input parameter is configured on deny statements, the log record will contain the layer 2 address of the forwarding device for any packet being dropped. If the switch is not configured to produce audit records containing information to establish the source of the events, this is a finding.

## Group: SRG-NET-000019-RTR-000001

**Group ID:** `V-221006`

### Rule: The Cisco switch must be configured to disable the auxiliary port unless it is connected to a secured modem providing encryption and authentication.

**Rule ID:** `SV-221006r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The use of POTS lines to modems connecting to network devices provides clear text of authentication traffic over commercial circuits that could be captured and used to compromise the network. Additional war dial attacks on the device could degrade the device and the production network. Secured modem devices must be able to authenticate users and must negotiate a key exchange before full encryption takes place. The modem will provide full encryption capability (Triple DES) or stronger. The technician who manages these devices will be authenticated using a key fob and granted access to the appropriate maintenance port; thus, the technician will gain access to the managed device. The token provides a method of strong (two-factor) user authentication. The token works in conjunction with a server to generate one-time user passwords that will change values at second intervals. The user must know a personal identification number (PIN) and possess the token to be allowed access to the device.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration and verify that the auxiliary port is disabled unless a secured modem providing encryption and authentication is connected to it. line aux 0 no exec Note: Transport input none is the default; hence it will not be shown in the configuration. If the auxiliary port is not disabled or is not connected to a secured modem when it is enabled, this is a finding.

## Group: SRG-NET-000202-RTR-000001

**Group ID:** `V-221007`

### Rule: The Cisco perimeter switch must be configured to deny network traffic by default and allow network traffic by exception.

**Rule ID:** `SV-221007r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only connections that are essential and approved are allowed. This requirement applies to both inbound and outbound network communications traffic. All inbound and outbound traffic must be denied by default. Firewalls and perimeter switches should only allow traffic through that is explicitly permitted. The initial defense for the internal network is to block any traffic at the perimeter that is attempting to make a connection to a host residing on the internal network. In addition, allowing unknown or undesirable outbound traffic by the firewall or switch will establish a state that will permit the return of this undesirable traffic inbound.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that the inbound ACL applied to all external interfaces is configured to allow specific ports and protocols and deny all other traffic. Step 1: Verify that an inbound ACL is applied to all external interfaces as shown in the example below: interface GigabitEthernet0/2 ip address x.11.1.2 255.255.255.254 ip access-group EXTERNAL_ACL in Step 2: Review inbound ACL to verify that it is configured to deny all other traffic that is not explicitly allowed. ip access-list extended EXTERNAL_ACL permit tcp any any established permit tcp host x.11.1.1 eq bgp host x.11.1.2 permit tcp host x.11.1.1 host x.11.1.2 eq bgp permit icmp host x.11.1.1 host x.11.1.2 echo permit icmp host x.11.1.1 host x.11.1.2 echo-reply … … … deny ip any any log-input If the ACL is not configured to allow specific ports and protocols and deny all other traffic, this is a finding. If the ACL is not configured inbound on all external interfaces, this is a finding.

## Group: SRG-NET-000019-RTR-000002

**Group ID:** `V-221008`

### Rule: The Cisco perimeter switch must be configured to enforce approved authorizations for controlling the flow of information between interconnected networks in accordance with applicable policy.

**Rule ID:** `SV-221008r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates authorized information to travel within a network and between interconnected networks. Controlling the flow of network traffic is critical so it does not introduce any unacceptable risk to the network infrastructure or data. An example of a flow control restriction is blocking outside traffic claiming to be from within the organization. For most switches, internal information flow control is a product of system design.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that ACLs are configured to allow or deny traffic for specific source and destination addresses as well as ports and protocols. In the example below, the switch is peering BGP with DISN. ICMP echo and echo-reply packets are allowed for troubleshooting connectivity. WWW traffic is permitted inbound to the NIPRNet host-facing web server (x.12.1.22). interface GigabitEthernet0/1 description Link to DISN ip address x.12.1.10 255.255.255.0 ip access-group FILTER_PERIMETER in … … … ip access-list extended FILTER_PERIMETER permit tcp any any established permit tcp host x.12.1.9 host x.12.1.10 eq bgp permit tcp host x.12.1.9 eq bgp host x.12.1.10 permit icmp host x.12.1.9 host x.12.1.10 echo permit icmp host x.12.1.9 host x.12.1.10 echo-reply permit tcp any host x.12.1.22 eq www deny ip any any log-input If the switch is not configured to enforce approved authorizations for controlling the flow of information between interconnected networks, this is a finding.

## Group: SRG-NET-000364-RTR-000109

**Group ID:** `V-221009`

### Rule: The Cisco perimeter switch must be configured to only allow incoming communications from authorized sources to be routed to authorized destinations.

**Rule ID:** `SV-221009r856408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic can be restricted directly by an access control list (ACL), which is a firewall function, or by Policy Routing. Policy Routing is a technique used to make routing decisions based on a number of different criteria other than just the destination network, including source or destination network, source or destination address, source or destination port, protocol, packet size, and packet classification. This overrides the switch's normal routing procedures used to control the specific paths of network traffic. It is normally used for traffic engineering but can also be used to meet security requirements; for example, traffic that is not allowed can be routed to the Null0 or discard interface. Policy Routing can also be used to control which prefixes appear in the routing table. This requirement is intended to allow network administrators the flexibility to use whatever technique is most effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if the switch allows only incoming communications from authorized sources to be routed to authorized destinations. The hypothetical example below allows inbound NTP from server x.1.12.9 only to host x.12.1.21. ip access-list extended FILTER_PERIMETER permit tcp any any established … … … permit udp host x.12.1.9 host x.12.1.21 eq ntp deny ip any any log-input If the switch does not restrict incoming communications to allow only authorized sources and destinations, this is a finding.

## Group: SRG-NET-000364-RTR-000110

**Group ID:** `V-221010`

### Rule: The Cisco perimeter switch must be configured to block inbound packets with source Bogon IP address prefixes.

**Rule ID:** `SV-221010r863263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with Bogon IP source addresses should never be allowed to traverse the IP core. Bogon IP networks are RFC1918 addresses or address blocks that have never been assigned by the IANA or have been reserved.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that an ingress ACL applied to all external interfaces is blocking packets with Bogon source addresses. Step 1: Verify an ACL has been configured containing the current Bogon prefixes as shown in the example below: ip access-list extended FILTER_PERIMETER deny ip 0.0.0.0 0.255.255.255 any log-input deny ip 10.0.0.0 0.255.255.255 any log-input deny ip 100.64.0.0 0.63.255.255 any log-input deny ip 127.0.0.0 0.255.255.255 any log-input deny ip 169.254.0.0 0.0.255.255 any log-input deny ip 172.16.0.0 0.15.255.255 any log-input deny ip 192.0.0.0 0.0.0.255 any log-input deny ip 192.0.2.0 0.0.0.255 any log-input deny ip 192.168.0.0 0.0.255.255 any log-input deny ip 198.18.0.0 0.1.255.255 any log-input deny ip 198.51.100.0 0.0.0.255 any log-input deny ip 203.0.113.0 0.0.0.255 any log-input deny ip 224.0.0.0 31.255.255.255 any log-input deny ip 240.0.0.0 15.255.255.255 any log-input permit tcp any any established permit tcp host x.12.1.9 host x.12.1.10 eq bgp permit tcp host x.12.1.9 eq bgp host x.12.1.10 permit icmp host x.12.1.9 host x.12.1.10 echo permit icmp host x.12.1.9 host x.12.1.10 echo-reply … … … deny ip any any log-input Step 2: Verify that the inbound ACL applied to all external interfaces will block all traffic from Bogon source addresses. interface GigabitEthernet0/1 description Link to DISN ip address x.12.1.10 255.255.255.254 ip access-group FILTER_PERIMETER in If the switch is not configured to block inbound packets with source Bogon IP address prefixes, this is a finding.

## Group: SRG-NET-000205-RTR-000014

**Group ID:** `V-221011`

### Rule: The Cisco perimeter switch must be configured to restrict it from accepting outbound IP packets that contain an illegitimate address in the source address field via egress filter or by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-221011r945858_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. DDoS attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet, thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify uRPF or an egress ACL has been configured on all internal interfaces to restrict the switch from accepting outbound IP packets that contain an illegitimate address in the source address field. uRPF example: interface GigabitEthernet0/1 description downstream link to LAN ip address 10.1.25.5 255.255.255.0 ip verify unicast source reachable-via rx Egress ACL example: interface GigabitEthernet0/1 description downstream link to LAN ip address 10.1.25.5 255.255.255.0 ip access-group EGRESS_FILTER in … … … ip access-list extended EGRESS_FILTER permit udp 10.1.15.0 0.0.0.255 any eq domain permit tcp 10.1.15.0 0.0.0.255 any eq ftp permit tcp 10.1.15.0 0.0.0.255 any eq ftp-data permit tcp 10.1.15.0 0.0.0.255 any eq www permit icmp 10.1.15.0 0.0.0.255 any permit icmp 10.1.15.0 0.0.0.255 any echo deny ip any any If uRPF or an egress ACL to restrict the switch from accepting outbound IP packets that contain an illegitimate address in the source address field has not been configured on all internal interfaces in an enclave, this is a finding.

## Group: SRG-NET-000205-RTR-000003

**Group ID:** `V-221012`

### Rule: The Cisco perimeter switch must be configured to filter traffic destined to the enclave in accordance with the guidelines contained in DoD Instruction 8551.1.

**Rule ID:** `SV-221012r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Vulnerability assessments must be reviewed by the System Administrator, and protocols must be approved by the Information Assurance (IA) staff before entering the enclave. ACLs are the first line of defense in a layered security approach. They permit authorized packets and deny unauthorized packets based on port or service type. They enhance the posture of the network by not allowing packets to reach a potential target within the security domain. The lists provided are highly susceptible ports and services that should be blocked or limited as much as possible without adversely affecting customer requirements. Auditing packets attempting to penetrate the network that are stopped by an ACL will allow network administrators to broaden their protective ring and more tightly define the scope of operation. If the perimeter is in a Deny-by-Default posture and what is allowed through the filter is in accordance with DoD Instruction 8551.1, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to PPS being blocked would be satisfied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that the ingress ACL is in accordance with DoD 8551.1. Step 1: Verify that an inbound ACL is configured on all external interfaces. interface GigabitEthernet0/2 ip address x.11.1.2 255.255.255.254 ip access-group EXTERNAL_ACL_INBOUND in Step 2. Review the inbound ACL to verify that it is filtering traffic in accordance with DoD 8551.1. ip access-list extended EXTERNAL_ACL_INBOUND permit tcp any any established permit tcp host x.11.1.1 eq bgp host x.11.1.2 permit tcp host x.11.1.1 host x.11.1.2 eq bgp permit icmp host x.11.1.1 host x.11.1.2 echo permit icmp host x.11.1.1 host x.11.1.2 echo-reply … … < must be in accordance with DoD Instruction 8551.1> … deny ip any any log-input If the switch does not filter traffic in accordance with the guidelines contained in DoD 8551.1, this is a finding.

## Group: SRG-NET-000205-RTR-000004

**Group ID:** `V-221013`

### Rule: The Cisco perimeter switch must be configured to filter ingress traffic at the external interface on an inbound direction.

**Rule ID:** `SV-221013r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access lists are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of switches makes use of access lists for restricting access to services on the switch itself as well as for filtering traffic passing through the switch. Inbound versus Outbound: It should be noted that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The switch can protect itself before damage is inflicted. - The input port is still known and can be filtered upon. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that an inbound ACL is configured on all external interfaces as shown in the example below: interface GigabitEthernet0/2 ip address x.11.1.2 255.255.255.254 ip access-group EXTERNAL_ACL_INBOUND in If the switch is not configured to filter traffic entering the network at all external interfaces in an inbound direction, this is a finding.

## Group: SRG-NET-000205-RTR-000005

**Group ID:** `V-221014`

### Rule: The Cisco perimeter switch must be configured to filter egress traffic at the internal interface on an inbound direction.

**Rule ID:** `SV-221014r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access lists are used to separate data traffic into that which it will route (permitted packets) and that which it will not route (denied packets). Secure configuration of switches makes use of access lists for restricting access to services on the switch itself as well as for filtering traffic passing through the switch. Inbound versus Outbound: It should be noted that some operating systems default access lists are applied to the outbound queue. The more secure solution is to apply the access list to the inbound queue for three reasons: - The switch can protect itself before damage is inflicted. - The input port is still known and can be filtered upon. - It is more efficient to filter packets before routing them.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that the egress ACL is bound to the internal interface in an inbound direction. interface interface GigabitEthernet0/2 description downstream link to LAN ip address 10.1.25.5 255.255.255.0 ip access-group EGRESS_FILTER in If the switch is not configured to filter traffic leaving the network at the internal interface in an inbound direction, this is a finding.

## Group: SRG-NET-000205-RTR-000015

**Group ID:** `V-221015`

### Rule: The Cisco perimeter switch must be configured to block all packets with any IP options.

**Rule ID:** `SV-221015r945859_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast switched and henceforth must be punted to the switch processor. Hackers who initiate denial-of-service (DoS) attacks on switches commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the switch. The end result is a reduction in the effects of the DoS attack on the switch and on downstream switches.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it will block all packets with IP options. ip access-list extended EXTERNAL_ACL permit tcp any any established deny ip any any option any-options permit … … … … deny ip any any log-input If the switch is not configured to drop all packets with IP options, this is a finding.

## Group: SRG-NET-000364-RTR-000111

**Group ID:** `V-221016`

### Rule: The Cisco perimeter switch must be configured to have Link Layer Discovery Protocol (LLDP) disabled on all external interfaces.

**Rule ID:** `SV-221016r856411_rule`
**Severity:** low

**Description:**
<VulnDiscussion>LLDP is a neighbor discovery protocol used to advertise device capabilities, configuration information, and device identity. LLDP is media-and-protocol-independent as it runs over layer 2; therefore, two network nodes that support different layer 3 protocols can still learn about each other. Allowing LLDP messages to reach external network nodes provides an attacker a method to obtain information of the network infrastructure that can be useful to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify LLDP is not enabled globally via the command. lldp run By default LLDP is not enabled globally. If LLDP is enabled, proceed to Step 2. Step 2: Verify LLDP is not enabled on any external interface as shown in the example below: interface GigabitEthernet0/1 ip address x.1.12.1 255.255.255.252 no lldp transmit Note: LLDP is enabled by default on all interfaces once it is enabled globally; hence the command "lldp transmit" will not be visible on the interface configuration. If LLDP transmit is enabled on any external interface, this is a finding.

## Group: SRG-NET-000364-RTR-000111

**Group ID:** `V-221017`

### Rule: The Cisco perimeter switch must be configured to have Cisco Discovery Protocol (CDP) disabled on all external interfaces.

**Rule ID:** `SV-221017r856412_rule`
**Severity:** low

**Description:**
<VulnDiscussion>CDP is a Cisco proprietary neighbor discovery protocol used to advertise device capabilities, configuration information, and device identity. CDP is media-and-protocol-independent as it runs over layer 2; therefore, two network nodes that support different layer 3 protocols can still learn about each other. Allowing CDP messages to reach external network nodes provides an attacker a method to obtain information of the network infrastructure that can be useful to plan an attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify if CDP is enabled globally as shown below: cdp run By default, CDP is not enabled globally or on any interface. If CDP is enabled globally, proceed to Step 2. Step 2: Verify CDP is not enabled on any external interface as shown in the example below: interface GigabitEthernet2 ip address z.1.24.4 255.255.255.252 … … … cdp enable If CDP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000364-RTR-000112

**Group ID:** `V-221018`

### Rule: The Cisco perimeter switch must be configured to have Proxy ARP disabled on all external interfaces.

**Rule ID:** `SV-221018r856413_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When Proxy ARP is enabled on a switch, it allows that switch to extend the network (at Layer 2) across multiple interfaces (LAN segments). Because proxy ARP allows hosts from different LAN segments to look like they are on the same segment, proxy ARP is only safe when used between trusted LAN segments. Attackers can leverage the trusting nature of proxy ARP by spoofing a trusted host and then intercepting packets. Proxy ARP should always be disabled on switch interfaces that do not require it, unless the switch is being used as a LAN bridge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if IP Proxy ARP is disabled on all external interfaces as shown in the example below: interface GigabitEthernet0/1 description link to DISN ip address x.1.12.2 255.255.255.252 no ip proxy-arp Note: By default Proxy ARP is enabled on all interfaces; hence, if enabled, it will not be shown in the configuration. If IP Proxy ARP is enabled on any external interface, this is a finding.

## Group: SRG-NET-000364-RTR-000113

**Group ID:** `V-221019`

### Rule: The Cisco perimeter switch must be configured to block all outbound management traffic.

**Rule ID:** `SV-221019r945857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For in-band management, the management network must have its own subnet in order to enforce control and access boundaries provided by Layer 3 network nodes, such as switches and firewalls. Management traffic between the managed network elements and the management network is routed via the same links and nodes as that used for production or operational traffic. Safeguards must be implemented to ensure that the management traffic does not leak past the perimeter of the managed network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The perimeter switch of the managed network must be configured with an outbound ACL on the egress interface to block all management traffic as shown in the example below: Step 1: Verify that all external interfaces has been configured with an outbound ACL as shown in the example below: interface GigabitEthernet0/2 description link to DISN ip address x.11.1.2 255.255.255.254 ip access-group EXTERNAL_ACL_OUTBOUND out Step 2: Verify that the outbound ACL discards management traffic as shown in the example below: ip access-list extended EXTERNAL_ACL_OUTBOUND deny tcp any any eq tacacs log-input deny tcp any any eq 22 log-input deny udp any any eq snmp log-input deny udp any any eq snmptrap log-input deny udp any any eq syslog log-input permit tcp any any eq www log-input deny ip any any log-input If management traffic is not blocked at the perimeter, this is a finding.

## Group: SRG-NET-000205-RTR-000012

**Group ID:** `V-221020`

### Rule: The Cisco switch must be configured to only permit management traffic that ingresses and egresses the out-of-band management (OOBM) interface.

**Rule ID:** `SV-221020r991945_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OOBM access switch will connect to the management interface of the managed network elements. The management interface can be a true OOBM interface or a standard interface functioning as the management interface. In either case, the management interface of the managed network element will be directly connected to the OOBM network. An OOBM interface does not forward transit traffic, thereby providing complete separation of production and management traffic. Since all management traffic is immediately forwarded into the management network, it is not exposed to possible tampering. The separation also ensures that congestion or failures in the managed network do not affect the management of the device. If the device does not have an OOBM port, the interface functioning as the management interface must be configured so that management traffic does not leak into the managed network and that production traffic does not leak into the management network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is only applicable where management access to the switch is via an OOBM interface which is not a true OOBM interface. Step 1: Verify that the managed interface has an inbound and outbound ACL configured. interface GigabitEthernet0/7 no switchport description link to OOBM access switch ip address 10.11.1.22 255.255.255.0 ip access-group INGRESS_MANAGEMENT_ACL in ip access-group EGRESS_MANAGEMENT_ACL in Step 2: Verify that the ingress ACL only allows management and ICMP traffic. ip access-list extended INGRESS_MANAGEMENT_ACL permit tcp any host 10.11.1.22 eq tacacs permit tcp any host 10.11.1.22 eq 22 permit udp any host 10.11.1.22 eq snmp permit udp any host 10.11.1.22 eq snmptrap permit udp any host 10.11.1.22 eq ntp permit icmp any host 10.11.1.22 deny ip any any log-input Step 3: Verify that the egress ACL blocks any transit traffic. ip access-list extended EGRESS_MANAGEMENT_ACL deny ip any any log-input Note: On Cisco switches, local generated packets are not inspected by outgoing interface access-lists. Hence, the above configuration would simply drop any packets not generated by the switch; hence, blocking any transit traffic. If the switch does not restrict traffic that ingresses and egresses the management interface, this is a finding.

## Group: SRG-NET-000362-RTR-000124

**Group ID:** `V-221021`

### Rule: The Cisco BGP switch must be configured to enable the Generalized TTL Security Mechanism (GTSM).

**Rule ID:** `SV-221021r856414_rule`
**Severity:** low

**Description:**
<VulnDiscussion>As described in RFC 3682, GTSM is designed to protect a switch's IP-based control plane from DoS attacks. Many attacks focused on CPU load and line-card overload can be prevented by implementing GTSM on all Exterior Border Gateway Protocol-speaking switches. GTSM is based on the fact that the vast majority of control plane peering is established between adjacent switches; that is, the Exterior Border Gateway Protocol peers are either between connecting interfaces or between loopback interfaces. Since TTL spoofing is considered nearly impossible, a mechanism based on an expected TTL value provides a simple and reasonably robust defense from infrastructure attacks based on forged control plane traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP configuration to verify that TTL security has been configured for each external neighbor as shown in the example below: router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 password xxxxxxxx neighbor x.1.1.9 ttl-security hops 1 neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 password xxxxxxxx neighbor x.2.1.7 ttl-security hops 1 If the switch is not configured to use GTSM for all Exterior Border Gateway Protocol peering sessions, this is a finding.

## Group: SRG-NET-000230-RTR-000002

**Group ID:** `V-221022`

### Rule: The Cisco BGP switch must be configured to use a unique key for each autonomous system (AS) that it peers with.

**Rule ID:** `SV-221022r945862_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the same keys are used between eBGP neighbors, the chance of a hacker compromising any of the BGP sessions increases. It is possible that a malicious user exists in one autonomous system who would know the key used for the eBGP session. This user would then be able to hijack BGP sessions with other trusted neighbors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the BGP configuration to determine if it is peering with multiple autonomous systems. Interview the ISSM and switch administrator to determine if unique keys are being used. router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 password yyyyyyyy neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 password zzzzzzzzz If unique keys are not being used, this is a finding.

## Group: SRG-NET-000018-RTR-000002

**Group ID:** `V-221023`

### Rule: The Cisco BGP switch must be configured to reject inbound route advertisements for any Bogon prefixes.

**Rule ID:** `SV-221023r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements for Bogon prefixes can result in the local autonomous system (AS) becoming a transit for malicious traffic as it will in turn advertise these prefixes to neighbor autonomous systems.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that it will reject BGP routes for any Bogon prefixes. Step 1: Verify a prefix list has been configured containing the current Bogon prefixes as shown in the example below: ip prefix-list PREFIX_FILTER seq 5 deny 0.0.0.0/8 le 32 ip prefix-list PREFIX_FILTER seq 10 deny 10.0.0.0/8 le 32 ip prefix-list PREFIX_FILTER seq 15 deny 100.64.0.0/10 le 32 ip prefix-list PREFIX_FILTER seq 20 deny 127.0.0.0/8 le 32 ip prefix-list PREFIX_FILTER seq 25 deny 169.254.0.0/16 le 32 ip prefix-list PREFIX_FILTER seq 30 deny 172.16.0.0/12 le 32 ip prefix-list PREFIX_FILTER seq 35 deny 192.0.2.0/24 le 32 ip prefix-list PREFIX_FILTER seq 40 deny 192.88.99.0/24 le 32 ip prefix-list PREFIX_FILTER seq 45 deny 192.168.0.0/16 le 32 ip prefix-list PREFIX_FILTER seq 50 deny 198.18.0.0/15 le 32 ip prefix-list PREFIX_FILTER seq 55 deny 198.51.100.0/24 le 32 ip prefix-list PREFIX_FILTER seq 60 deny 203.0.113.0/24 le 32 ip prefix-list PREFIX_FILTER seq 65 deny 224.0.0.0/4 le 32 ip prefix-list PREFIX_FILTER seq 70 deny 240.0.0.0/4 le 32 ip prefix-list PREFIX_FILTER seq 75 permit 0.0.0.0/0 ge 8 Step 2: Verify that the prefix list has been applied to all external BGP peers as shown in the example below: router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 prefix-list PREFIX_FILTER in neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 prefix-list PREFIX_FILTER in Route Map Alternative: Verify that the route map applied to the external neighbors references the configured Bogon prefix list shown above. router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 route-map FILTER_PREFIX_MAP neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 route-map FILTER_PREFIX_MAP … route-map FILTER_PREFIX_MAP permit 10 match ip address prefix-list PREFIX_FILTER If the switch is not configured to reject inbound route advertisements for any Bogon prefixes, this is a finding.

## Group: SRG-NET-000018-RTR-000003

**Group ID:** `V-221024`

### Rule: The Cisco BGP switch must be configured to reject inbound route advertisements for any prefixes belonging to the local autonomous system (AS).

**Rule ID:** `SV-221024r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Accepting route advertisements belonging to the local AS can result in traffic looping or being black-holed, or at a minimum, using a non-optimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that it will reject routes belonging to the local AS. Step 1: Verify a prefix list has been configured containing prefixes belonging to the local AS. In the example below x.13.1.0/24 is the global address space allocated to the local AS. ip prefix-list PREFIX_FILTER seq 5 deny 0.0.0.0/8 le 32 … … … ip prefix-list PREFIX_FILTER seq 74 deny x.13.1.0/24 le 32 ip prefix-list PREFIX_FILTER seq 75 permit 0.0.0.0/0 ge 8 Step 2: Verify that the prefix list has been applied to all external BGP peers as shown in the example below: router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 prefix-list PREFIX_FILTER in neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 prefix-list PREFIX_FILTER in If the switch is not configured to reject inbound route advertisements belonging to the local AS, this is a finding.

## Group: SRG-NET-000018-RTR-000004

**Group ID:** `V-221025`

### Rule: The Cisco BGP switch must be configured to reject inbound route advertisements from a customer edge (CE) switch for prefixes that are not allocated to that customer.

**Rule ID:** `SV-221025r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As a best practice, a service provider should only accept customer prefixes that have been assigned to that customer and any peering autonomous systems. A multi-homed customer with BGP speaking switches connected to the Internet or other external networks could be breached and used to launch a prefix de-aggregation attack. Without ingress route filtering of customers, the effectiveness of such an attack could impact the entire IP core and its customers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that there are ACLs defined to only accept routes for prefixes that belong to specific customers. Step 1: Verify prefix list has been configured for each customer containing prefixes belonging to each customer as shown in the example below: ip prefix-list PREFIX_FILTER_CUST1 seq 5 permit x.13.1.0/24 le 32 ip prefix-list PREFIX_FILTER_CUST1 seq 10 deny 0.0.0.0/0 ge 8 ip prefix-list PREFIX_FILTER_CUST2 seq 5 permit x.13.2.0/24 le 32 ip prefix-list PREFIX_FILTER_CUST2 seq 10 deny 0.0.0.0/0 ge 8 Step 2: Verify that the prefix lists has been applied to all to the applicable CE peers as shown in the example below: router bgp xx no synchronization bgp log-neighbor-changes neighbor x.12.4.14 remote-as 64514 neighbor x.12.4.14 prefix-list FILTER_PREFIXES_CUST1 in neighbor x.12.4.16 remote-as 64516 neighbor x.12.4.16 prefix-list FILTER_PREFIXES_CUST2 in Note: Routes to PE-CE links within a VPN are needed for troubleshooting end-to-end connectivity across the MPLS/IP backbone. Hence, these prefixes are an exception to this requirement. If the switch is not configured to reject inbound route advertisements from each CE switch for prefixes that are not allocated to that customer, this is a finding.

## Group: SRG-NET-000018-RTR-000005

**Group ID:** `V-221026`

### Rule: The Cisco BGP switch must be configured to reject outbound route advertisements for any prefixes that do not belong to any customers or the local autonomous system (AS).

**Rule ID:** `SV-221026r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Advertisement of routes by an autonomous system for networks that do not belong to any of its customers pulls traffic away from the authorized network. This causes a denial of service (DoS) on the network that allocated the block of addresses and may cause a DoS on the network that is inadvertently advertising it as the originator. It is also possible that a misconfigured or compromised switch within the GIG IP core could redistribute Interior Gateway Protocol (IGP) routes into BGP, thereby leaking internal routes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that a prefix list has been configured containing prefixes belonging to customers as well as the local AS as shown in the example below: ip prefix-list CE_PREFIX_ADVERTISEMENTS seq 5 permit x.13.1.0/24 le 32 ip prefix-list CE_PREFIX_ADVERTISEMENTS seq 10 permit x.13.2.0/24 le 32 ip prefix-list CE_PREFIX_ADVERTISEMENTS seq 15 permit x.13.3.0/24 le 32 ip prefix-list CE_PREFIX_ADVERTISEMENTS seq 20 permit x.13.4.0/24 le 32 … … … ip prefix-list CE_PREFIX_ADVERTISEMENTS seq 80 deny 0.0.0.0/0 ge 8 Step 2: Verify that the prefix lists has been applied to all CE peers as shown in the example below: router bgp 64512 no synchronization bgp log-neighbor-changes neighbor x.12.4.14 remote-as 64514 neighbor x.12.4.14 prefix-list CE_PREFIX_ADVERTISEMENTS out neighbor x.12.4.16 remote-as 64516 neighbor x.12.4.16 prefix-list CE_PREFIX_ADVERTISEMENTS out If the switch is not configured to reject outbound route advertisements that do not belong to any customers or the local AS, this is a finding.

## Group: SRG-NET-000205-RTR-000006

**Group ID:** `V-221027`

### Rule: The Cisco BGP switch must be configured to reject outbound route advertisements for any prefixes belonging to the IP core.

**Rule ID:** `SV-221027r929070_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Outbound route advertisements belonging to the core can result in traffic either looping or being black holed, or at a minimum, using a nonoptimized path.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify that a prefix list has been configured containing prefixes belonging to the IP core. ip prefix-list FILTER_CORE_PREFIXES seq 5 deny x.1.1.0/24 le 32 ip prefix-list FILTER _CORE_PREFIXES seq 10 deny x.1.2.0/24 le 32 ip prefix-list FILTER _CORE_PREFIXES seq 15 permit 0.0.0.0/0 ge 8 Step 2: Verify that the prefix lists has been applied to all external BGP peers as shown in the example below: router bgp xx no synchronization bgp log-neighbor-changes neighbor x.1.4.12 remote-as yy address-family ipv4 neighbor x.1.4.12 prefix-list FILTER _CORE_PREFIXES out If the switch is not configured to reject outbound route advertisements for prefixes belonging to the IP core, this is a finding.

## Group: SRG-NET-000018-RTR-000006

**Group ID:** `V-221028`

### Rule: The Cisco BGP switch must be configured to reject route advertisements from BGP peers that do not list their autonomous system (AS) number as the first AS in the AS_PATH attribute.

**Rule ID:** `SV-221028r945854_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure the IP core is not used as a transit network for unauthorized or possibly even internet traffic. All autonomous system boundary switches (ASBRs) must ensure updates received from eBGP peers list their AS number as the first AS in the AS_PATH attribute.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify the switch is configured to deny updates received from eBGP peers that do not list their AS number as the first AS in the AS_PATH attribute. By default, Cisco IOS enforces the first AS in the AS_PATH attribute for all route advertisements. Review the switch configuration to verify that the command no bgp enforce-first-as is not configured. router bgp xx no synchronization no bgp enforce-first-as If the switch is not configured to reject updates from peers that do not list their AS number as the first AS in the AS_PATH attribute, this is a finding.

## Group: SRG-NET-000018-RTR-000010

**Group ID:** `V-221029`

### Rule: The Cisco BGP switch must be configured to reject route advertisements from CE switches with an originating AS in the AS_PATH attribute that does not belong to that customer.

**Rule ID:** `SV-221029r945855_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Verifying the path a route has traversed will ensure that the local AS is not used as a transit network for unauthorized traffic. To ensure that the local AS does not carry any prefixes that do not belong to any customers, all PE switches must be configured to reject routes with an originating AS other than that belonging to the customer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify the switch is configured to deny updates received from CE switches with an originating AS in the AS_PATH attribute that does not belong to that customer. Step 1: Review switch configuration and verify that there is an as-path access-list statement defined to only accept routes from a CE switch whose AS did not originate the route. The configuration should look similar to the following: ip as-path access-list 10 permit ^yy$ ip as-path access-list 10 deny .* Note: The characters “^” and “$” representing the beginning and the end of the expression respectively are optional and are implicitly defined if omitted. Step 2: Verify that the as-path access-list is referenced by the filter-list inbound for the appropriate BGP neighbors as shown in the example below: router bgp xx neighbor x.1.4.12 remote-as yy neighbor x.1.4.12 filter-list 10 in If the switch is not configured to reject updates from CE switches with an originating AS in the AS_PATH attribute that does not belong to that customer, this is a finding.

## Group: SRG-NET-000362-RTR-000117

**Group ID:** `V-221030`

### Rule: The Cisco BGP switch must be configured to use the maximum prefixes feature to protect against route table flooding and prefix de-aggregation attacks.

**Rule ID:** `SV-221030r856416_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade switch performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured switch, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements. In 1997, misconfigured switches in the Florida Internet Exchange network (AS7007) de-aggregated every prefix in their routing table and started advertising the first /24 block of each of these prefixes as their own. Faced with this additional burden, the internal switches became overloaded and crashed repeatedly. This caused prefixes advertised by these switches to disappear from routing tables and reappear when the switches came back online. As the switches came back after crashing, they were flooded with the routing table information by their neighbors. The flood of information would again overwhelm the switches and cause them to crash. This process of route flapping served to destabilize not only the surrounding network but also the entire Internet. Switches trying to reach those addresses would choose the smaller, more specific /24 blocks first. This caused backbone networks throughout North America and Europe to crash. Maximum prefix limits on peer connections combined with aggressive prefix-size filtering of customers' reachability advertisements will effectively mitigate the de-aggregation risk. BGP maximum prefix must be used on all eBGP switches to limit the number of prefixes that it should receive from a particular neighbor, whether customer or peering AS. Consider each neighbor and how many routes they should be advertising and set a threshold slightly higher than the number expected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that the number of received prefixes from each eBGP neighbor is controlled. router bgp xx neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 maximum-prefix nnnnnnn neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 maximum-prefix nnnnnnn If the switch is not configured to control the number of prefixes received from each peer to protect against route table flooding and prefix de-aggregation attacks, this is a finding.

## Group: SRG-NET-000362-RTR-000118

**Group ID:** `V-221031`

### Rule: The Cisco BGP switch must be configured to limit the prefix size on any inbound route advertisement to /24, or the least significant prefixes issued to the customer.

**Rule ID:** `SV-221031r856417_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The effects of prefix de-aggregation can degrade switch performance due to the size of routing tables and also result in black-holing legitimate traffic. Initiated by an attacker or a misconfigured switch, prefix de-aggregation occurs when the announcement of a large prefix is fragmented into a collection of smaller prefix announcements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it is compliant with this requirement. Step 1: Verify that a route filter has been configured to reject prefixes longer than /24, or the least significant prefixes issued to the customers as shown in the example below: ip prefix-list FILTER_PREFIX_LENGTH seq 5 permit 0.0.0.0/0 ge 8 le 24 ip prefix-list FILTER_PREFIX_LENGTH seq 10 deny 0.0.0.0/0 le 32 Step 2: Verify that prefix filtering has been applied to each eBGP peer as shown in the example: router bgp xx neighbor x.1.1.9 remote-as yy neighbor x.1.1.9 prefix-list FILTER_PREFIX_LENGTH in neighbor x.2.1.7 remote-as zz neighbor x.2.1.7 prefix-list FILTER_PREFIX_LENGTH in If the switch is not configured to limit the prefix size on any inbound route advertisement to /24, or the least significant prefixes issued to the customer, this is a finding.

## Group: SRG-NET-000512-RTR-000001

**Group ID:** `V-221032`

### Rule: The Cisco BGP switch must be configured to use its loopback address as the source address for iBGP peering sessions.

**Rule ID:** `SV-221032r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of the BGP switches. It is easier to construct appropriate ingress filters for switch management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the switch’s loopback address instead of the numerous physical interface addresses. When the loopback address is used as the source for eBGP peering, the BGP session will be harder to hijack since the source address to be used is not known globally, making it more difficult for a hacker to spoof an eBGP neighbor. By using traceroute, a hacker can easily determine the addresses for an eBGP speaker when the IP address of an external interface is used as the source address. The switches within the iBGP domain should also use loopback addresses as the source address when establishing BGP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the switch configuration to verify that a loopback address has been configured. interface Loopback0 ip address 10.1.1.1 255.255.255.255 Step 2: Verify that the loopback interface is used as the source address for all iBGP sessions. router bgp xx no synchronization no bgp enforce-first-as bgp log-neighbor-changes redistribute static neighbor 10.1.1.1 remote-as xx neighbor 10.1.1.1 password xxxxxxxx neighbor 10.1.1.1 update-source Loopback0 If the switch does not use its loopback address as the source address for all iBGP sessions, this is a finding.

## Group: SRG-NET-000512-RTR-000002

**Group ID:** `V-221033`

### Rule: The Cisco MPLS switch must be configured to use its loopback address as the source address for LDP peering sessions.

**Rule ID:** `SV-221033r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of backbone switches. It is easier to construct appropriate ingress filters for switch management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of from a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the switch's loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it is compliant with this requirement. Verify that a loopback address has been configured as shown in the example below: interface Loopback0 ip address 10.1.1.1 255.255.255.255 By default, switches will use its loopback address for LDP peering. If an address has not be configured on the loopback interface, it will use its physical interface connecting to the LDP peer. If the router-id command is specified that overrides this default behavior, verify that it is a loopback interface as shown in the example below: mpls ldp router-id Loopback0 If the switch is not configured to use its loopback address for LDP peering, this is a finding.

## Group: SRG-NET-000512-RTR-000003

**Group ID:** `V-221034`

### Rule: The Cisco MPLS switch must be configured to synchronize Interior Gateway Protocol (IGP) and LDP to minimize packet loss when an IGP adjacency is established prior to LDP peers completing label exchange.

**Rule ID:** `SV-221034r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Packet loss can occur when an IGP adjacency is established and the switch begins forwarding packets using the new adjacency before the LDP label exchange completes between the peers on that link. Packet loss can also occur if an LDP session closes and the switch continues to forward traffic using the link associated with the LDP peer rather than an alternate pathway with a fully synchronized LDP session. The MPLS LDP-IGP Synchronization feature provides a means to synchronize LDP with OSPF or IS-IS to minimize MPLS packet loss. When an IGP adjacency is established on a link but LDP-IGP synchronization is not yet achieved or is lost, the IGP will advertise the max-metric on that link.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch OSPF or IS-IS configuration and verify that LDP will synchronize with the link-state routing protocol as shown in the example below: OSPF Example: router ospf 1 mpls ldp sync IS-IS Example: router isis mpls ldp sync net 49.0001.1234.1600.5531.00 If the switch is not configured to synchronize IGP and LDP, this is a finding.

## Group: SRG-NET-000193-RTR-000001

**Group ID:** `V-221035`

### Rule: The MPLS switch with RSVP-TE enabled must be configured with message pacing to adjust maximum burst and maximum number of RSVP messages to an output queue based on the link speed and input queue size of adjacent core switches.

**Rule ID:** `SV-221035r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>RSVP-TE can be used to perform constraint-based routing when building LSP tunnels within the network core that will support QoS and traffic engineering requirements. RSVP-TE is also used to enable MPLS Fast Reroute, a network restoration mechanism that will reroute traffic onto a backup LSP in case of a node or link failure along the primary path. When there is a disruption in the MPLS core, such as a link flap or switch reboot, the result is a significant amount of RSVP signaling, such as "PathErr" and "ResvErr" messages that need to be sent for every LSP using that link. When RSVP messages are sent out, they are sent either hop by hop or with the switch alert bit set in the IP header. This means that every switch along the path must examine the packet to determine if additional processing is required for these RSVP messages. If there is enough signaling traffic in the network, it is possible for an interface to receive more packets for its input queue than it can hold, resulting in dropped RSVP messages and hence slower RSVP convergence. Increasing the size of the interface input queue can help prevent dropping packets; however, there is still the risk of having a burst of signaling traffic that can fill the queue. Solutions to mitigate this risk are RSVP message pacing or refresh reduction to control the rate at which RSVP messages are sent. RSVP refresh reduction includes the following features: RSVP message bundling, RSVP Message ID to reduce message processing overhead, reliable delivery of RSVP messages using Message ID, and summary refresh to reduce the amount of information transmitted every refresh interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine RSVP messages are rate limited. Step 1: Determine if MPLS TE is enabled globally and at least one interface as shown in the example below: mpls traffic-eng tunnels … … … interface GigabitEthernet0/2 no switchport ip address x.x.x.x 255.255.255.0 mpls traffic-eng tunnels mpls ip Step 2: If MPLS TE is enabled, verify that message pacing is enabled. ip rsvp signalling rate-limit period 30 burst 9 maxsize 2100 limit 50 Note: The command "ip rsvp msg-pacing" has been deprecated by the command "ip rsvp signalling rate-limit". If the switch with RSVP-TE enabled does not rate limit RSVP messages based on the link speed and input queue size of adjacent core switches, this is a finding.

## Group: SRG-NET-000512-RTR-000004

**Group ID:** `V-221036`

### Rule: The Cisco MPLS switch must be configured to have TTL Propagation disabled.

**Rule ID:** `SV-221036r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The head end of the label-switched path (LSP), the label edge switch (LER) will decrement the IP packet's time-to-live (TTL) value by one and then copy the value to the MPLS TTL field. At each label-switched switch (LSR) hop, the MPLS TTL value is decremented by one. The MPLS switch that pops the label (either the penultimate LSR or the egress LER) will copy the packet's MPLS TTL value to the IP TTL field and decrement it by one. This TTL propagation is the default behavior. Because the MPLS TTL is propagated from the IP TTL, a traceroute will list every hop in the path, be it routed or label switched, thereby exposing core nodes. With TTL propagation disabled, LER decrements the IP packet's TTL value by one and then places a value of 255 in the packet's MPLS TTL field, which is then decremented by one as the packet passes through each LSR in the MPLS core. Because the MPLS TTL never drops to zero, none of the LSP hops triggers an ICMP TTL exceeded message, and consequently, these hops are not recorded in a traceroute. Hence, nodes within the MPLS core cannot be discovered by an attacker.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that TTL propagation is disabled as shown in the example below: no mpls ip propagate-ttl If the MPLS switch is not configured to disable TTL propagation, this is a finding.

## Group: SRG-NET-000512-RTR-000005

**Group ID:** `V-221037`

### Rule: The Cisco PE switch must be configured to have each Virtual Routing and Forwarding (VRF) instance bound to the appropriate physical or logical interfaces to maintain traffic separation between all MPLS L3VPNs.

**Rule ID:** `SV-221037r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The primary security model for an MPLS L3VPN infrastructure is traffic separation. The service provider must guarantee the customer that traffic from one VPN does not leak into another VPN or into the core, and that core traffic must not leak into any VPN. Hence, it is imperative that each CE-facing interface can only be associated to one VRF—that alone is the fundamental framework for traffic separation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the design plan for deploying L3VPN and VRF-lite. Step 2: Review the design plan for deploying L3VPN and VRF-lite. Review all CE-facing interfaces and verify that the proper VRF is defined via the "ip vrf forwarding" command. In the example below, COI1 is bound to interface GigabitEthernet0/1, while COI2 is bound to GigabitEthernet0/2. interface GigabitEthernet0/1 description link to COI1 no switchport ip vrf forwarding COI1 ip address x.1.0.1 255.255.255.0 ! interface GigabitEthernet0/2 description link to COI2 no switchport ip vrf forwarding COI2 ip address x.2.0.2 255.255.255.0 If any VRFs are not bound to the appropriate physical or logical interface, this is a finding.

## Group: SRG-NET-000512-RTR-000006

**Group ID:** `V-221038`

### Rule: The Cisco PE switch must be configured to have each Virtual Routing and Forwarding (VRF) instance with the appropriate Route Target (RT).

**Rule ID:** `SV-221038r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The primary security model for an MPLS L3VPN as well as a VRF-lite infrastructure is traffic separation. Each interface can only be associated to one VRF, which is the fundamental framework for traffic separation. Forwarding decisions are made based on the routing table belonging to the VRF. Control of what routes are imported into or exported from a VRF is based on the RT. It is critical that traffic does not leak from one COI tenant or L3VPN to another; hence, it is imperative that the correct RT is configured for each VRF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the design plan for MPLS/L3VPN and VRF-lite to determine what RTs have been assigned for each VRF. Review the switch configuration and verify that the correct RT is configured for each VRF. In the example below, route target 13:13 has been configured for customer 1. ip vrf CUST1 rd 13:13 route-target export 13:13 route-target import 13:13 If there are VRFs configured with the wrong RT, this is a finding.

## Group: SRG-NET-000512-RTR-000007

**Group ID:** `V-221039`

### Rule: The Cisco PE switch must be configured to have each VRF with the appropriate Route Distinguisher (RD).

**Rule ID:** `SV-221039r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An RD provides uniqueness to the customer address spaces within the MPLS L3VPN infrastructure. The concept of the VPN-IPv4 and VPN-IPv6 address families consists of the RD prepended before the IP address. Hence, if the same IP prefix is used in several different L3VPNs, it is possible for BGP to carry several completely different routes for that prefix, one for each VPN. Since VPN-IPv4 addresses and IPv4 addresses are different address families, BGP never treats them as comparable addresses. The purpose of the RD is to create distinct routes for common IPv4 address prefixes. On any given PE switch, a single RD can define a VRF in which the entire address space may be used independently, regardless of the makeup of other VPN address spaces. Hence, it is imperative that a unique RD is assigned to each L3VPN and that the proper RD is configured for each VRF.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the design plan for MPLS/L3VPN to determine what RD has been assigned for each VRF. Review the switch configuration and verify that the correct RD is configured for each VRF. In the example below, route distinguisher 13:13 has been configured for customer 1. ip vrf CUST1 rd 13:13 Note: This requirement is only applicable for MPLS L3VPN implementations. If the wrong RD has been configured for any VRF, this is a finding.

## Group: SRG-NET-000343-RTR-000001

**Group ID:** `V-221040`

### Rule: The Cisco PE switch providing MPLS Layer 2 Virtual Private Network (L2VPN) services must be configured to authenticate targeted Label Distribution Protocol (LDP) sessions used to exchange virtual circuit (VC) information using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-221040r863378_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>LDP provides the signaling required for setting up and tearing down pseudowires (virtual circuits used to transport Layer 2 frames) across an MPLS IP core network. Using a targeted LDP session, each PE switch advertises a virtual circuit label mapping that is used as part of the label stack imposed on the frames by the ingress PE switch during packet forwarding. Authentication provides protection against spoofed TCP segments that can be introduced into the LDP sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Cisco switch is not compliant with this requirement; hence, it is a finding. However, the severity level can be downgraded to a category 3 if the switch is configured to authenticate targeted LDP sessions using MD5 as shown in the configuration example below: mpls ldp neighbor 10.1.1.2 password xxxxxxx mpls label protocol ldp If the switch is not configured to authenticate targeted LDP sessions using MD5, the finding will remain as a CAT II.

## Group: SRG-NET-000512-RTR-000008

**Group ID:** `V-221041`

### Rule: The Cisco PE switch providing MPLS Virtual Private Wire Service (VPWS) must be configured to have the appropriate virtual circuit identification (VC ID) for each attachment circuit.

**Rule ID:** `SV-221041r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>VPWS is an L2VPN technology that provides a virtual circuit between two PE switches to forward Layer 2 frames between two customer-edge switches or switches through an MPLS-enabled IP core. The ingress PE switch (virtual circuit head-end) encapsulates Ethernet frames inside MPLS packets using label stacking and forwards them across the MPLS network to the egress PE switch (virtual circuit tail-end). During a virtual circuit setup, the PE switches exchange VC label bindings for the specified VC ID. The VC ID specifies a pseudowire associated with an ingress and egress PE switch and the customer-facing attachment circuits. To guarantee that all frames are forwarded onto the correct pseudowire and to the correct customer and attachment circuits, it is imperative that the correct VC ID is configured for each attachment circuit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the correct and unique VCID has been configured for the appropriate attachment circuit. In the example below, GigabitEthernet0/1 is the CE-facing interface that is configured for VPWS with the VCID of 55. interface GigabitEthernet0/1 xconnect x.2.2.12 55 encapsulation mpls If the correct VC ID has not been configured on both switches, this is a finding.

## Group: SRG-NET-000512-RTR-000009

**Group ID:** `V-221042`

### Rule: The Cisco PE switch providing Virtual Private LAN Services (VPLS) must be configured to have all attachment circuits defined to the virtual forwarding instance (VFI) with the globally unique VPN ID assigned for each customer VLAN.

**Rule ID:** `SV-221042r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>VPLS defines an architecture that delivers Ethernet multipoint services over an MPLS network. Customer Layer 2 frames are forwarded across the MPLS core via pseudowires using IEEE 802.1q Ethernet bridging principles. A pseudowire is a virtual bidirectional connection between two attachment circuits (virtual connections between PE and CE switches). A pseudowire contains two unidirectional label-switched paths (LSP) between two PE switches. Each MAC virtual forwarding table instance (VFI) is interconnected using pseudowires provisioned for the bridge domain, thereby maintaining privacy and logical separation between each VPLS bridge domain. The VFI specifies the pseudowires associated with connecting PE switches and the customer-facing attachment circuits belonging to a given VLAN. Resembling a Layer 2 switch, the VFI is responsible for learning MAC addresses and providing loop-free forwarding of customer traffic to the appropriate end nodes. Each VPLS domain is identified by a globally unique VPN ID; hence, VFIs of the same VPLS domain must be configured with the same VPN ID on all participating PE switches. To guarantee traffic separation for all customer VLANs and that all packets are forwarded to the correct destination, it is imperative that the correct attachment circuits are associated with the appropriate VFI and that each VFI is associated to the unique VPN ID assigned to the customer VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the implementation plan and the VPN IDs assigned to customer VLANs for the VPLS deployment. Step 2: Review the PE switch configuration to verify that customer attachment circuits are associated to the appropriate VFI. In the example below, the attached circuit at interface GigabitEthernet0/1 is associated to VPN ID 110. l2 vfi VPLS_A manual vpn id 110 bridge-domain 100 neighbor 10.3.3.3 encapsulation mpls neighbor 10.3.3.4 encapsulation mpls … … … interface GigabitEthernet0/1 no switchport no ip address service instance 10 ethernet encapsulation untagged bridge-domain 100 If the attachment circuits have not been bound to the VFI configured with the assigned VPN ID for each VLAN, this is a finding.

## Group: SRG-NET-000512-RTR-000010

**Group ID:** `V-221043`

### Rule: The Cisco PE switch must be configured to enforce the split-horizon rule for all pseudowires within a Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-221043r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A virtual forwarding instance (VFI) must be created on each participating PE switch for each customer VLAN using VPLS for carrier Ethernet services. The VFI specifies the VPN ID of a VPLS domain, the addresses of other PE switches in the domain, and the type of tunnel signaling and encapsulation mechanism for each peer PE switch. The set of VFIs formed by the interconnection of the emulated VCs is called a VPLS instance, which forms the logic bridge over the MPLS core network. The PE switches use the VFI with a unique VPN ID to establish a full mesh of emulated virtual circuits or pseudowires to all the other PE switches in the VPLS instance. The full-mesh configuration allows the PE switch to maintain a single broadcast domain. With a full-mesh configuration, signaling and packet replication requirements for each provisioned virtual circuit on a PE can be high. To avoid the problem of a packet looping in the provider core, thereby adding more overhead, the PE devices must enforce a split-horizon principle for the emulated virtual circuits; that is, if a packet is received on an emulated virtual circuit, it is not forwarded on any other virtual circuit.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE switch configuration to verify that split horizon is enabled. By default, split horizon is enabled; hence, the attribute no-split-horizon should not be seen on the neighbor command as shown in the example below: l2 vfi VPLS_A manual vpn id 110 bridge-domain 100 neighbor 10.3.3.3 encapsulation mpls no-split-horizon If split horizon is not enabled, this is a finding. Note: This requirement is only applicable to a mesh VPLS topology. VPLS solves the loop problem by using a split-horizon rule which states that member PE switches of a VPLS must forward VPLS traffic only to the local attachment circuits when they receive the traffic from the other PE switches. In a ring VPLS, split horizon must be disabled so that a PE switch can forward a packet received from one pseudowire to another pseudowire. To prevent the consequential loop, at least one span in the ring would not have a pseudowire for any given VPLS instance.

## Group: SRG-NET-000193-RTR-000002

**Group ID:** `V-221044`

### Rule: The Cisco PE switch providing Virtual Private LAN Services (VPLS) must be configured to have traffic storm control thresholds on CE-facing interfaces.

**Rule ID:** `SV-221044r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a VPLS bridge, creating excessive traffic and degrading network performance. Traffic storm control prevents VPLS bridge disruption by suppressing traffic when the number of packets reaches configured threshold levels. Traffic storm control monitors incoming traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that storm control is enabled on CE-facing interfaces deploying VPLS as shown in the example below: interface GigabitEthernet3 no switchport no ip address service instance 10 ethernet encapsulation untagged bridge-domain 100 storm-control broadcast cir 12000000 ! ! If storm control is not enabled at a minimum for broadcast traffic, this is a finding.

## Group: SRG-NET-000362-RTR-000119

**Group ID:** `V-221045`

### Rule: The Cisco PE switch must be configured to implement Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) snooping for each Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-221045r856419_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP snooping provides a way to constrain multicast traffic at Layer 2. By monitoring the IGMP membership reports sent by hosts within the bridge domain, the snooping application can set up Layer 2 multicast forwarding tables to deliver traffic only to ports with at least one interested member within the VPLS bridge, thereby significantly reducing the volume of multicast traffic that would otherwise flood an entire VPLS bridge domain. The IGMP snooping operation applies to both access circuits and pseudowires within a VPLS bridge domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that IGMP or MLD snooping has been configured for IPv4 and IPv6 multicast traffic respectively for each VPLS bridge domain. The example below are the steps to verify that IGMP snooping is enabled for a VPLS bridge domain. Step 1: Verify that IGMP snooping is enabled globally. By default, IGMP snooping is enabled globally; hence, the following command should not be in the switch configuration: no ip igmp snooping Step 2: If IGMP snooping is enabled globally, it will also be enabled by default for each VPLS bridge domain. Hence, the command “no ip igmp snooping” should not be configured for any VPLS bridge domain as shown in the example below: bridge-domain 100 no ip igmp snooping ! If the switch is not configured to implement IGMP or MLD snooping for each VPLS bridge domain, this is a finding.

## Group: SRG-NET-000192-RTR-000002

**Group ID:** `V-221046`

### Rule: The Cisco PE switch must be configured to limit the number of MAC addresses it can learn for each Virtual Private LAN Services (VPLS) bridge domain.

**Rule ID:** `SV-221046r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VPLS defines an architecture that delivers Ethernet multipoint services over an MPLS network. Customer Layer 2 frames are forwarded across the MPLS core via pseudowires using IEEE 802.1q Ethernet bridging principles. A pseudowire is a virtual bidirectional connection between two attachment circuits (virtual connections between PE and CE switches). A pseudowire contains two unidirectional label-switched paths (LSP). Each MAC forwarding table instance is interconnected using domain-specific LSPs, thereby maintaining privacy and logical separation between each VPLS domain. When a frame arrives on a bridge port (pseudowire or attachment circuit) and the source MAC address is unknown to the receiving PE switch, the source MAC address is associated with the pseudowire or attachment circuit and the forwarding table is updated accordingly. Frames are forwarded to the appropriate pseudowire or attachment circuit according to the forwarding table entry for the destination MAC address. Ethernet frames sent to broadcast and unknown destination addresses must be flooded out to all interfaces for the bridge domain; hence, a PE switch must replicate packets across both attachment circuits and pseudowires. A malicious attacker residing in a customer network could launch a source MAC address spoofing attack by flooding packets to a valid unicast destination, each with a different MAC source address. The PE switch receiving this traffic would try to learn every new MAC address and would quickly run out of space for the VFI forwarding table. Older, valid MAC addresses would be removed from the table, and traffic sent to them would have to be flooded until the storm threshold limit is reached. Hence, it is essential that a limit is established to control the number of MAC addresses that will be learned and recorded into the forwarding table for each bridge domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the PE switch configuration to determine if a MAC address limit has been set for each VPLS bridge domain. bridge-domain 100 mac limit maximum addresses nnnnn If a limit has not been configured, this is a finding.

## Group: SRG-NET-000205-RTR-000007

**Group ID:** `V-221047`

### Rule: The Cisco PE switch must be configured to block any traffic that is destined to the IP core infrastructure.

**Rule ID:** `SV-221047r622190_rule`
**Severity:** high

**Description:**
<VulnDiscussion>IP addresses can be guessed. Core network elements must not be accessible from any external host. Protecting the core from any attack is vital for the integrity and privacy of customer traffic as well as the availability of transit services. A compromise of the IP core can result in an outage or, at a minimum, non-optimized forwarding of customer traffic. Protecting the core from an outside attack also prevents attackers from using the core to attack any customer. Hence, it is imperative that all switches at the edge deny traffic destined to any address belonging to the IP core infrastructure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the switch configuration to verify that an ingress ACL is applied to all external or CE-facing interfaces. interface GigabitEthernet0/2 no switchport ip address x.1.12.2 255.255.255.252 ip access-group BLOCK_TO_CORE in Step 2: Verify that the ingress ACL discards and logs packets destined to the IP core address space. ip access-list extended BLOCK_TO_CORE deny ip any 10.1.x.0 0.0.255.255 log-input permit ip any any ! If the PE switch is not configured to block any traffic with a destination address assigned to the IP core infrastructure, this is a finding. Note: Internet Control Message Protocol (ICMP) echo requests and traceroutes will be allowed to the edge from external adjacent neighbors.

## Group: SRG-NET-000205-RTR-000008

**Group ID:** `V-221048`

### Rule: The Cisco PE switch must be configured with Unicast Reverse Path Forwarding (uRPF) loose mode enabled on all CE-facing interfaces.

**Rule ID:** `SV-221048r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The uRPF feature is a defense against spoofing and denial-of-service (DoS) attacks by verifying if the source address of any ingress packet is reachable. To mitigate attacks that rely on forged source addresses, all provider edge switches must enable uRPF loose mode to guarantee that all packets received from a CE switch contain source addresses that are in the route table.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if uRPF loose mode is enabled on all CE-facing interfaces. interface GigabitEthernet0/2 no switchport ip address x.1.12.2 255.255.255.252 ip access-group BLOCK_TO_CORE in ip verify unicast source reachable-via any If uRPF loose mode is not enabled on all CE-facing interfaces, this is a finding.

## Group: SRG-NET-000205-RTR-000016

**Group ID:** `V-221049`

### Rule: The Cisco PE switch must be configured to ignore or drop all packets with any IP options.

**Rule ID:** `SV-221049r945860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Packets with IP options are not fast-switched and therefore must be punted to the switch processor. Hackers who initiate denial-of-service (DoS) attacks on switches commonly send large streams of packets with IP options. Dropping the packets with IP options reduces the load of IP options packets on the switch. The end result is a reduction in the effects of the DoS attack on the switch and on downstream switches.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it will ignore or drop all packets with IP options as shown in the examples below: ip options drop or ip options ignore If the switch is not configured to drop or block all packets with IP options, this is a finding.

## Group: SRG-NET-000193-RTR-000113

**Group ID:** `V-221050`

### Rule: The Cisco PE switch must be configured to enforce a Quality-of-Service (QoS) policy to provide preferred treatment for mission-critical applications.

**Rule ID:** `SV-221050r917445_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that a QoS policy has been configured to provide preferred treatment for mission-critical applications. Step 1: Verify that the class-maps are configured to match on DSCP values as shown in the configuration example below: class-map match-all C2_VOICE match ip dscp af47 class-map match-all VOICE match ip dscp ef class-map match-all VIDEO match ip dscp af41 class-map match-all CONTROL_PLANE match ip dscp cs6 class-map match-all PREFERRED_DATA match ip dscp af33 Step 2: Verify that the policy map reserves the bandwidth for each traffic type as shown in the example below: policy-map QOS_POLICY class C2_VOICE priority percent 10 class VOICE priority percent 15 class VIDEO bandwidth percent 25 class CONTROL_PLANE priority percent 10 class PREFERRED_DATA bandwidth percent 25 class class-default bandwidth percent 15 Step 3: Verify that an output service policy is bound to all interfaces as shown in the configuration example below: interface GigabitEthernet1/1 no switchport ip address 10.1.15.1 255.255.255.252 service-policy output QOS_POLICY ! interface GigabitEthernet1/2 no switchport ip address 10.1.15.4 255.255.255.252 service-policy output QOS_POLICY Note: Enclaves must mark or re-mark their traffic to be consistent with the DODIN backbone admission criteria to gain the appropriate level of service. A general DiffServ principle is to mark or trust traffic as close to the source as administratively and technically possible. However, certain traffic types might need to be re-marked before handoff to the DODIN backbone to gain admission to the correct class. If such re-marking is required, it is recommended that the re-marking be performed at the CE egress edge. Note: The GTP QOS document (GTP-0009) can be downloaded via the following link: https://intellipedia.intelink.gov/wiki/Portal:GIG_Technical_Guidance/GTG_GTPs/GTP_Development_List If the switch is not configured to enforce a QoS policy in accordance with the QoS GIG Technical Profile, this is a finding.

## Group: SRG-NET-000193-RTR-000114

**Group ID:** `V-221051`

### Rule: The Cisco P switch must be configured to enforce a Quality-of-Service (QoS) policy to provide preferred treatment for mission-critical applications.

**Rule ID:** `SV-221051r917448_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Different applications have unique requirements and toleration levels for delay, jitter, bandwidth, packet loss, and availability. To manage the multitude of applications and services, a network requires a QoS framework to differentiate traffic and provide a method to manage network congestion. The Differentiated Services Model (DiffServ) is based on per-hop behavior by categorizing traffic into different classes and enabling each node to enforce a forwarding treatment to each packet as dictated by a policy. Packet markings such as IP Precedence and its successor, Differentiated Services Code Points (DSCP), were defined along with specific per-hop behaviors for key traffic types to enable a scalable QoS solution. DiffServ QoS categorizes network traffic, prioritizes it according to its relative importance, and provides priority treatment based on the classification. It is imperative that end-to-end QoS is implemented within the IP core network to provide preferred treatment for mission-critical applications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that a QoS policy has been configured to provide preferred treatment for mission-critical applications. Step 1: Verify that the class-maps are configured to match on DSCP values as shown in the configuration example below: class-map match-all PREFERRED_DATA match ip dscp af33 class-map match-all CONTROL_PLANE match ip dscp cs6 class-map match-all VIDEO match ip dscp af41 class-map match-all VOICE match ip dscp ef class-map match-all C2_VOICE match ip dscp 47 Step 2: Verify that the policy map reserves the bandwidth for each traffic type as shown in the example below: policy-map QOS_POLICY class CONTROL_PLANE priority percent 10 class C2_VOICE priority percent 10 class VOICE priority percent 15 class VIDEO bandwidth percent 25 class PREFERRED_DATA bandwidth percent 25 class class-default bandwidth percent 15 Step 3: Verify that an output service policy is bound to all interfaces as shown in the configuration example below: interface GigabitEthernet1/1 no switchport ip address 10.1.15.5 255.255.255.252 service-policy output QOS_POLICY ! interface GigabitEthernet1/2 no switchport ip address 10.1.15.8 255.255.255.252 service-policy output QOS_POLICY Note: The GTP QOS document (GTP-0009) can be downloaded via the following link: https://intellipedia.intelink.gov/wiki/Portal:GIG_Technical_Guidance/GTG_GTPs/GTP_Development_List If the switch is not configured to enforce a QoS policy in accordance with the QoS GIG Technical Profile, this is a finding.

## Group: SRG-NET-000193-RTR-000112

**Group ID:** `V-221052`

### Rule: The Cisco switch must be configured to enforce a Quality-of-Service (QoS) policy to limit the effects of packet flooding denial-of-service (DoS) attacks.

**Rule ID:** `SV-221052r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it is configured to enforce a QoS policy to limit the effects of packet flooding DoS attacks. Step 1: Verify that a class map has been configured for the Scavenger class as shown in the example below: class-map match-all SCAVENGER match ip dscp cs1 Step 2: Verify that the policy map includes the SCAVENGER class with low priority as shown in the example below: policy-map QOS_POLICY class CONTROL_PLANE priority percent 10 class C2_VOICE priority percent 10 class VOICE priority percent 15 class VIDEO bandwidth percent 25 class PREFERRED_DATA bandwidth percent 25 class SCAVENGER bandwidth percent 5 class class-default bandwidth percent 10 Note: Traffic out of profile must be marked at the customer access layer or CE egress edge. If the switch is not configured to enforce a QoS policy to limit the effects of packet flooding DoS attacks, this is a finding.

## Group: SRG-NET-000019-RTR-000003

**Group ID:** `V-221053`

### Rule: The Cisco multicast switch must be configured to disable Protocol Independent Multicast (PIM) on all interfaces that are not required to support multicast routing.

**Rule ID:** `SV-221053r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Limiting where, within the network, a given multicast group's data is permitted to flow is an important first step in improving multicast security. A scope zone is an instance of a connected region of a given scope. Zones of the same scope cannot overlap while zones of a smaller scope will fit completely within a zone of a larger scope. For example, Admin-local scope is smaller than Site-local scope, so the administratively configured boundary fits within the bounds of a site. According to RFC 4007 IPv6 Scoped Address Architecture (section 5), scope zones are also required to be "convex from a routing perspective"; that is, packets routed within a zone must not pass through any links that are outside of the zone. This requirement forces each zone to be one contiguous island rather than a series of separate islands. As stated in the DoD IPv6 IA Guidance for MO3, "One should be able to identify all interfaces of a zone by drawing a closed loop on their network diagram, engulfing some switches and passing through some switches to include only some of their interfaces." Therefore, it is imperative that the network engineers have documented their multicast topology and thereby knows which interfaces are enabled for multicast. Once this is done, the zones can be scoped as required.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the network's multicast topology diagram. Step 2: Review the switch configuration to verify that only the PIM interfaces as shown in the multicast topology diagram are enabled for PIM as shown in the example below: interface GigabitEthernet1/1 no switchport ip address 10.1.3.3 255.255.255.0 ip pim sparse-mode If an interface is not required to support multicast routing and it is enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000004

**Group ID:** `V-221054`

### Rule: The Cisco multicast switch must be configured to bind a Protocol Independent Multicast (PIM) neighbor filter to interfaces that have PIM enabled.

**Rule ID:** `SV-221054r622190_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>PIM is a routing protocol used to build multicast distribution trees for forwarding multicast traffic across the network infrastructure. PIM traffic must be limited to only known PIM neighbors by configuring and binding a PIM neighbor filter to those interfaces that have PIM enabled. If a PIM neighbor filter is not applied to those interfaces that have PIM enabled, unauthorized switches can join the PIM domain, discover and use the rendezvous points, and also advertise their rendezvous points into the domain. This can result in a denial of service by traffic flooding or result in the unauthorized transfer of data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Verify all interfaces enabled for PIM have a neighbor ACL bound to the interface as shown in the example below: interface GigabitEthernet1/1 no switchport ip address 10.1.2.2 255.255.255.0 ip pim neighbor-filter PIM_NEIGHBORS ip pim sparse-mode Step 2: Review the configured ACL for filtering PIM neighbors as shown in the example below: ip access-list standard PIM_NEIGHBORS permit 10.1.2.6 If PIM neighbor ACLs are not bound to all interfaces that have PIM enabled, this is a finding.

## Group: SRG-NET-000019-RTR-000005

**Group ID:** `V-221055`

### Rule: The Cisco multicast edge switch must be configured to establish boundaries for administratively scoped multicast traffic.

**Rule ID:** `SV-221055r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If multicast traffic is forwarded beyond the intended boundary, it is possible that it can be intercepted by unauthorized or unintended personnel. Administrative scoped multicast addresses are locally assigned and are to be used exclusively by the enterprise network or enclave. Administrative scoped multicast traffic must not cross the enclave perimeter in either direction. Restricting multicast traffic makes it more difficult for a malicious user to access sensitive traffic. Admin-Local scope is encouraged for any multicast traffic within a network intended for network management, as well as for control plane traffic that must reach beyond link-local destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that admin-scope multicast traffic is blocked at the external edge as shown in the example below: interface GigabitEthernet1/2 ip address x.1.12.2 255.255.255.252 ip pim sparse-mode ip multicast boundary MULTICAST_SCOPE … … … ip access-list standard MULTICAST_SCOPE deny 239.0.0.0 0.255.255.255 permit any If the switch is not configured to establish boundaries for administratively scoped multicast traffic, this is a finding.

## Group: SRG-NET-000362-RTR-000120

**Group ID:** `V-221056`

### Rule: The Cisco multicast Rendezvous Point (RP) switch must be configured to limit the multicast forwarding cache so that its resources are not saturated by managing an overwhelming number of Protocol Independent Multicast (PIM) and Multicast Source Discovery Protocol (MSDP) source-active entries.

**Rule ID:** `SV-221056r863379_rule`
**Severity:** low

**Description:**
<VulnDiscussion>MSDP peering between networks enables sharing of multicast source information. Enclaves with an existing multicast topology using PIM-SM can configure their RP switches to peer with MSDP switches. As a first step of defense against a denial-of-service (DoS) attack, all RP switches must limit the multicast forwarding cache to ensure that switch resources are not saturated managing an overwhelming number of PIM and MSDP source-active entries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The Cisco switch does not have a mechanism to limit the multicast forwarding cache. However, the risk associated with this requirement can be fully mitigated by configuring the switch to: 1. Filter PIM register messages. 2. Rate limiting the number of PIM register messages. 3. Accept MSDP packets only from known MSDP peers. Step 1: Verify that the RP is configured to filter PIM register messages for any undesirable multicast groups and sources. The example below will deny any multicast streams for groups 239.5.0.0/16 and allow from only sources x.1.2.6 and x.1.2.7. ip pim rp-address 10.1.12.3 ip pim accept-register list PIM_REGISTER_FILTER … … … ip access-list extended PIM_REGISTER_FILTER deny ip any 239.5.0.0 0.0.255.255 permit ip host x.1.2.6 any permit ip host x.1.2.7 any deny ip any any Step 2: Verify that the RP is configured to rate limiting the number of PIM register messages as shown in the example below: ip pim rp-address 10.2.2.2 ip pim register-rate-limit nn Step 3: Review the switch configuration to determine if there is a receive path or interface filter to only accept MSDP packets from known MSDP peers as shown in the example below: Step 3a: Verify that interfaces used for MSDP peering have an inbound ACL as shown in the example. interface GigabitEthernet1/1 ip address x.1.28.8 255.255.255.0 ip access-group EXTERNAL_ACL_INBOUND in ip pim sparse-mode Step 3b: Verify that the ACL restricts MSDP peering to only known sources. ip access-list extended EXTERNAL_ACL_INBOUND permit tcp any any established permit tcp host x.1.28.2 host x.1.28.8 eq 639 deny tcp any host x.1.28.8 eq 639 log permit tcp host x.1.28.2 host 10.1.28.8 eq bgp permit tcp host x.1.28.2 eq bgp host x.1.28.8 permit pim host x.1.28.2 pim host x.1.28.8 … … … deny ip any any log Note: MSDP connections is via TCP port 639. If the RP switch is not configured to filter PIM register messages, rate limiting the number of PIM register messages, and accept MSDP packets only from known MSDP peers, this is a finding.

## Group: SRG-NET-000019-RTR-000013

**Group ID:** `V-221057`

### Rule: The Cisco multicast Rendezvous Point (RP) switch must be configured to filter Protocol Independent Multicast (PIM) Register messages received from the Designated switch (DR) for any undesirable multicast groups and sources.

**Rule ID:** `SV-221057r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that register messages are accepted only for authorized multicast groups and sources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP is configured to filter PIM register messages. The example below will deny any multicast streams for groups 239.5.0.0/16 and allow from only sources x.1.2.6 and x.1.2.7. ip pim rp-address 10.1.12.3 ip pim accept-register list PIM_REGISTER_FILTER … … … ip access-list extended PIM_REGISTER_FILTER deny ip any 239.5.0.0 0.0.255.255 permit ip host x.1.2.6 any permit ip host x.1.2.7 any deny ip any any If the RP switch peering with PIM-SM switches is not configured with a policy to block registration messages for any undesirable multicast groups and sources, this is a finding.

## Group: SRG-NET-000019-RTR-000014

**Group ID:** `V-221058`

### Rule: The Cisco multicast Rendezvous Point (RP) switch must be configured to filter Protocol Independent Multicast (PIM) Join messages received from the Designated Cisco switch (DR) for any undesirable multicast groups.

**Rule ID:** `SV-221058r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. An attacker can flood a network segment with multicast packets, over-using the available bandwidth and thereby creating a denial-of-service (DoS) condition. Hence, it is imperative that join messages are only accepted for authorized multicast groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the RP is configured to filter PIM join messages for any undesirable multicast groups. In the example below, groups from 239.8.0.0/16 are not allowed. ip pim rp-address 10.2.2.2 ip pim accept-rp 10.2.2.2 FILTER_PIM_JOINS … … … ip access-list standard FILTER_PIM_JOINS deny 239.8.0.0 0.0.255.255 permit any ! If the RP is not configured to filter join messages received from the DR for any undesirable multicast groups, this is a finding.

## Group: SRG-NET-000362-RTR-000121

**Group ID:** `V-221059`

### Rule: The Cisco multicast Rendezvous Point (RP) must be configured to rate limit the number of Protocol Independent Multicast (PIM) Register messages.

**Rule ID:** `SV-221059r856422_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When a new source starts transmitting in a PIM Sparse Mode network, the DR will encapsulate the multicast packets into register messages and forward them to the RP using unicast. This process can be taxing on the CPU for both the DR and the RP if the source is running at a high data rate and there are many new sources starting at the same time. This scenario can potentially occur immediately after a network failover. The rate limit for the number of register messages should be set to a relatively low value based on the known number of multicast sources within the multicast domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the RP to verify that it is rate limiting the number of PIM register messages. ip pim rp-address 10.2.2.2 ip pim register-rate-limit nn If the RP is not limiting PIM register messages, this is a finding.

## Group: SRG-NET-000364-RTR-000114

**Group ID:** `V-221060`

### Rule: The Cisco multicast Designated switch (DR) must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join only multicast groups that have been approved by the organization.

**Rule ID:** `SV-221060r863380_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is filtering IGMP or MLD Membership Report messages, allowing hosts to join only those groups that have been approved. Step 1: Verify that all host-facing layer 3 and VLAN interfaces are configured to filter IGMP Membership Report messages (IGMP joins) as shown in the example below: interface Vlan3 ip address 10.3.3.3 255.255.255.0 ip pim sparse-mode ip igmp access-group IGMP_JOIN_FILTER ip igmp version 3 Step 2: Verify that the ACL denies unauthorized groups or permits only authorized groups. The example below denies all groups from 239.8.0.0/16 range. ip access-list standard IGMP_JOIN_FILTER deny 239.8.0.0 0.0.255.255 permit any Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. This requirement is not applicable to Any Source Multicast (ASM) since the filtering is being performed by the Rendezvous Point switch. If the DR is not filtering IGMP or MLD Membership Report messages, this is a finding.

## Group: SRG-NET-000364-RTR-000115

**Group ID:** `V-221061`

### Rule: The Cisco multicast Designated switch (DR) must be configured to filter the Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Report messages to allow hosts to join a multicast group only from sources that have been approved by the organization.

**Rule ID:** `SV-221061r863381_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Real-time multicast traffic can entail multiple large flows of data. Large unicast flows tend to be fairly isolated (i.e., someone doing a file download here or there), whereas multicast can have broader impact on bandwidth consumption, resulting in extreme network congestion. Hence, it is imperative that there is multicast admission control to restrict which multicast groups hosts are allowed to join via IGMP or MLD.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the DR to verify that it is filtering IGMP or MLD report messages, allowing hosts to only join multicast groups from sources that have been approved. Step 1: Verify that all host-facing layer 3 and VLAN interfaces are configured to filter IGMP Membership Report messages (IGMP joins) as shown in the example below: interface Vlan3 ip address 10.3.3.3 255.255.255.0 ip pim sparse-mode ip igmp access-group IGMP_JOIN_FILTER ip igmp version 3 Step 2: Verify that the ACL denies unauthorized sources or allows only authorized sources. The example below denies all groups from 232.8.0.0/16 range and permits sources only from the x.0.0.0/8 network. ip access-list extended IGMP_JOIN_FILTER deny ip any 232.8.0.0 0.0.255.255 permit ip x.0.0.0 0.255.255.255 any deny ip any any Note: This requirement is only applicable to Source Specific Multicast (SSM) implementation. If the DR is not filtering IGMP or MLD report messages, this is a finding.

## Group: SRG-NET-000362-RTR-000122

**Group ID:** `V-221062`

### Rule: The Cisco multicast Designated switch (DR) must be configured to limit the number of mroute states resulting from Internet Group Management Protocol (IGMP) and Multicast Listener Discovery (MLD) Host Membership Reports.

**Rule ID:** `SV-221062r856425_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The current multicast paradigm can let any host join any multicast group at any time by sending an IGMP or MLD membership report to the DR. In a Protocol Independent Multicast (PIM) Sparse Mode network, the DR will send a PIM Join message for the group to the RP. Without any form of admission control, this can pose a security risk to the entire multicast domain, specifically the multicast switches along the shared tree from the DR to the RP that must maintain the mroute state information for each group join request. Hence, it is imperative that the DR is configured to limit the number of mroute state information that must be maintained to mitigate the risk of IGMP or MLD flooding.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DR configuration to verify that it is limiting the number of mroute states via IGMP or MLD. Verify IGMP limits have been configured globally or on each host-facing layer 3 and VLAN interface via the ip igmp limit command as shown in the example below: interface Vlan3 ip address 10.3.3.3 255.255.255.0 … … … ip igmp limit nn If the DR is not limiting multicast join requests via IGMP or MLD on a global or interfaces basis, this is a finding.

## Group: SRG-NET-000362-RTR-000123

**Group ID:** `V-221063`

### Rule: The Cisco multicast Designated switch (DR) must be configured to set the shortest-path tree (SPT) threshold to infinity to minimalize source-group (S, G) state within the multicast topology where Any Source Multicast (ASM) is deployed.

**Rule ID:** `SV-221063r945856_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>ASM can have many sources for the same groups (many-to-many). For many receivers, the path via the RP may not be ideal compared with the shortest path from the source to the receiver. By default, the last-hop switch will initiate a switch from the shared tree to a source-specific SPT to obtain lower latencies. This is accomplished by the last-hop switch sending an (S, G) Protocol Independent Multicast (PIM) Join toward S (the source). When the last-hop switch begins to receive traffic for the group from the source via the SPT, it will send a PIM Prune message to the RP for the (S, G). The RP will then send a Prune message toward the source. The SPT switchover becomes a scaling issue for large multicast topologies that have many receivers and many sources for many groups because (S, G) entries require more memory than (*, G). Hence, it is imperative to minimize the amount of (S, G) state to be maintained by increasing the threshold that determines when the SPT switchover occurs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the DR configuration to verify that the SPT switchover threshold is increased (default is "0") or set to infinity (never switch over). ip pim rp-address 10.2.2.2 ip pim spt-threshold infinity If the DR is not configured to increase the SPT threshold or set to infinity to minimalize (S, G) state, this is a finding.

## Group: SRG-NET-000364-RTR-000116

**Group ID:** `V-221064`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to only accept MSDP packets from known MSDP peers.

**Rule ID:** `SV-221064r856427_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network switches presents additional risks to the DISN Core, whether from a rogue or misconfigured MSDP-enabled switch. To guard against an attack from malicious MSDP traffic, the receive path or interface filter for all MSDP-enabled RP switches must be configured to only accept MSDP packets from known MSDP peers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if there is a receive path or interface filter to only accept MSDP packets from known MSDP peers. Step 1: Verify that interfaces used for MSDP peering have an inbound ACL as shown in the example below: interface GigabitEthernet1/1 no switchport ip address x.1.28.8 255.255.255.0 ip access-group EXTERNAL_ACL_INBOUND in ip pim sparse-mode Step 2: Verify that the ACL restricts MSDP peering to only known sources. ip access-list extended EXTERNAL_ACL_INBOUND permit tcp any any established permit tcp host x.1.28.2 host x.1.28.8 eq 639 deny tcp any host x.1.28.8 eq 639 log permit tcp host x.1.28.2 host 10.1.28.8 eq bgp permit tcp host x.1.28.2 eq bgp host x.1.28.8 permit pim host x.1.28.2 host x.1.28.8 … … … deny ip any any log Note: MSDP connections is via TCP port 639. If the switch is not configured to only accept MSDP packets from known MSDP peers, this is a finding.

## Group: SRG-NET-000343-RTR-000002

**Group ID:** `V-221065`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to authenticate all received MSDP packets.

**Rule ID:** `SV-221065r856428_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MSDP peering with customer network switches presents additional risks to the core, whether from a rogue or misconfigured MSDP-enabled switch. MSDP password authentication is used to validate each segment sent on the TCP connection between MSDP peers, protecting the MSDP session against the threat of spoofed packets being injected into the TCP connection stream.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if received MSDP packets are authenticated. ip msdp peer x.1.28.8 remote-as 8 ip msdp password peer x.1.28.8 xxxxxxxxxxxx If the switch does not require MSDP authentication, this is a finding.

## Group: SRG-NET-000018-RTR-000007

**Group ID:** `V-221066`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to filter received source-active multicast advertisements for any undesirable multicast groups and sources.

**Rule ID:** `SV-221066r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The interoperability of BGP extensions for interdomain multicast routing and MSDP enables seamless connectivity of multicast domains between autonomous systems. MP-BGP advertises the unicast prefixes of the multicast sources used by Protocol Independent Multicast (PIM) switches to perform RPF checks and build multicast distribution trees. MSDP is a mechanism used to connect multiple PIM sparse-mode domains, allowing RPs from different domains to share information about active sources. When RPs in peering multicast domains hear about active sources, they can pass on that information to their local receivers, thereby allowing multicast data to be forwarded between the domains. Configuring an import policy to block multicast advertisements for reserved, Martian, single-source multicast, and any other undesirable multicast groups, as well as any source-group (S, G) states with Bogon source addresses, would assist in avoiding unwanted multicast traffic from traversing the core.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if there is import policy to block source-active multicast advertisements for any undesirable multicast groups, as well as any (S, G) states with undesirable source addresses. Step 1: Verify that an inbound source-active filter is bound to each MSDP peer. ip msdp peer x.1.28.2 remote-as 2 ip msdp sa-filter in x.1.28.2 list INBOUND_MSDP_SA_FILTER Step 2: Review the access lists referenced by the source-active filter to verify that undesirable multicast groups, auto-RP, single source multicast (SSM) groups, and advertisements from undesirable sources are blocked. ip access-list extended INBOUND_MSDP_SA_FILTER deny ip any host 224.0.1.3 deny ip any host 224.0.1.24 deny ip any host 224.0.1.22 deny ip any host 224.0.1.2 deny ip any host 224.0.1.35 deny ip any host 224.0.1.60 deny ip any host 224.0.1.39 deny ip any host 224.0.1.40 deny ip any 232.0.0.0 0.255.255.255 deny ip any 239.0.0.0 0.255.255.255 deny ip 10.0.0.0 0.255.255.255 any deny ip 127.0.0.0 0.255.255.255 any deny ip 172.16.0.0 0.15.255.255 any deny ip 192.168.0.0 0.0.255.255 any permit ip any any If the switch is not configured with an import policy to filter undesirable SA multicast advertisements, this is a finding.

## Group: SRG-NET-000018-RTR-000008

**Group ID:** `V-221067`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to filter source-active multicast advertisements to external MSDP peers to avoid global visibility of local-only multicast sources and groups.

**Rule ID:** `SV-221067r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To avoid global visibility of local information, there are a number of source-group (S, G) states in a PIM-SM domain that must not be leaked to another domain, such as multicast sources with private address, administratively scoped multicast addresses, and the auto-RP groups (224.0.1.39 and 224.0.1.40). Allowing a multicast distribution tree, local to the core, to extend beyond its boundary could enable local multicast traffic to leak into other autonomous systems and customer networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if there is export policy to block local source-active multicast advertisements. Step 1: Verify that an outbound source-active filter is bound to each MSDP peer as shown in the example below: ip msdp peer 10.1.28.8 remote-as 8 ip msdp sa-filter out 10.1.28.8 list OUTBOUND_MSDP_SA_FILTER Step 2: Review the access lists referenced by the source-active filters and verify that MSDP source-active messages being sent to MSDP peers do not leak advertisements that are local. ip access-list extended OUTBOUND_MSDP_SA_FILTER deny ip 10.0.0.0 0.255.255.255 any permit ip any any If the switch is not configured with an export policy to filter local source-active multicast advertisements, this is a finding.

## Group: SRG-NET-000018-RTR-000009

**Group ID:** `V-221068`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to limit the amount of source-active messages it accepts on a per-peer basis.

**Rule ID:** `SV-221068r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>To reduce any risk of a denial-of-service (DoS) attack from a rogue or misconfigured MSDP switch, the switch must be configured to limit the number of source-active messages it accepts from each peer.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if it is configured to limit the amount of source-active messages it accepts on a per-peer basis. ip msdp peer x.1.28.2 remote-as nn ip msdp sa-filter in 10.1.28.2 list MSDP_SA_FILTER ip msdp sa-limit X.1.28.2 nnn If the switch is not configured to limit the source-active messages it accepts, this is a finding.

## Group: SRG-NET-000512-RTR-000011

**Group ID:** `V-221069`

### Rule: The Cisco Multicast Source Discovery Protocol (MSDP) switch must be configured to use a loopback address as the source address when originating MSDP traffic.

**Rule ID:** `SV-221069r622190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Using a loopback address as the source address offers a multitude of uses for security, access, management, and scalability of MSDP switches. It is easier to construct appropriate ingress filters for switch management plane traffic destined to the network management subnet since the source addresses will be from the range used for loopback interfaces instead of a larger range of addresses used for physical interfaces. Log information recorded by authentication and syslog servers will record the switch’s loopback address instead of the numerous physical interface addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the switch configuration to verify that a loopback address has been configured. interface Loopback12 ip address x.12.2.2 255.255.255.255 Step 2: Verify that the loopback interface is used as the source address for all MSDP packets generated by the switch. ip msdp peer x.44.2.34 connect-source Loopback12 remote-as nn If the switch does not use its loopback address as the source address when originating MSDP traffic, this is a finding.

## Group: SRG-NET-000512-RTR-000100

**Group ID:** `V-237750`

### Rule: The Cisco switch must be configured to have Cisco Express Forwarding enabled.

**Rule ID:** `SV-237750r648776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Cisco Express Forwarding (CEF) switching mode replaces the traditional Cisco routing cache with a data structure that mirrors the entire system routing table. Because there is no need to build cache entries when traffic starts arriving for new destinations, CEF behaves more predictably when presented with large volumes of traffic addressed to many destinations such as a SYN flood attacks that. Because many SYN flood attacks use randomized source addresses to which the hosts under attack will reply to, there can be a substantial amount of traffic for a large number of destinations that the switch will have to handle. Consequently, switches configured for CEF will perform better under SYN floods directed at hosts inside the network than switches using the traditional cache. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch to verify that CEF is enabled. IPv4 Example: ip cef IPv6 Example: ipv6 cef If the switch is not configured to have CEF enabled, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-237752`

### Rule: The Cisco switch must be configured to advertise a hop limit of at least 32 in Switch Advertisement messages for IPv6 stateless auto-configuration deployments.

**Rule ID:** `SV-237752r648780_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if the hop limit has been configured for Router Advertisement messages as shown in the example. ipv6 hop-limit 128 If hop-limit has been configured and has not been set to at least 32, it is a finding.

## Group: SRG-NET-000512-RTR-000013

**Group ID:** `V-237756`

### Rule: The Cisco switch must not be configured to use IPv6 Site Local Unicast addresses.

**Rule ID:** `SV-237756r999760_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>As currently defined, site local addresses are ambiguous and can be present in multiple sites. The address itself does not contain any indication of the site to which it belongs. The use of site-local addresses has the potential to adversely affect network security through leaks, ambiguity, and potential misrouting as documented in section 2 of RFC3879. RFC3879 formally deprecates the IPv6 site-local unicast prefix FEC0::/10 as defined in RFC3513.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to ensure FEC0::/10 IPv6 addresses are not defined. If IPv6 Site Local Unicast addresses are defined, this is a finding.

## Group: SRG-NET-000512-RTR-000014

**Group ID:** `V-237759`

### Rule: The Cisco perimeter switch must be configured to suppress Router Advertisements on all external IPv6-enabled interfaces.

**Rule ID:** `SV-237759r648792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Many of the known attacks in stateless autoconfiguration are defined in RFC 3756 were present in IPv4 ARP attacks. To mitigate these vulnerabilities, links that have no hosts connected such as the interface connecting to external gateways must be configured to suppress router advertisements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to verify that Router Advertisements are suppressed on all external IPv6-enabled interfaces as shown in the example below. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 nd ra suppress If the switch is not configured to suppress Router Advertisements on all external IPv6-enabled interfaces, this is a finding.

## Group: SRG-NET-000364-RTR-000200

**Group ID:** `V-237762`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 undetermined transport packets.

**Rule ID:** `SV-237762r950991_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>One of the fragmentation weaknesses known in IPv6 is the undetermined transport packet. This packet contains an undetermined protocol due to fragmentation. Depending on the length of the IPv6 extension header chain, the initial fragment may not contain the layer four port information of the packet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to determine if it is configured to drop IPv6 undetermined transport packets. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops undetermined transport packets as shown in the example below. ipv6 access-list FILTER_IPV6 deny ipv6 any any log undetermined-transport permit ipv6 … … … … deny ipv6 any any log If the switch is not configured to drop IPv6 undetermined transport packets, this is a finding.

## Group: SRG-NET-000364-RTR-000201

**Group ID:** `V-237764`

### Rule: The Cisco perimeter switch must be configured drop IPv6 packets with a Routing Header type 0, 1, or 3-255. 

**Rule ID:** `SV-237764r856665_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The routing header can be used maliciously to send a packet through a path where less robust security is in place, rather than through the presumably preferred path of routing protocols. Use of the routing extension header has few legitimate uses other than as implemented by Mobile IPv6. The Type 0 Routing Header (RFC 5095) is dangerous because it allows attackers to spoof source addresses and obtain traffic in response, rather than the real owner of the address. Secondly, a packet with an allowed destination address could be sent through a Firewall using the Routing Header functionality, only to bounce to a different node once inside. The Type 1 Routing Header is defined by a specification called "Nimrod Routing", a discontinued project funded by DARPA. Assuming that most implementations will not recognize the Type 1 Routing Header, it must be dropped. The Type 3–255 Routing Header values in the routing type field are currently undefined and should be dropped inbound and outbound. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to determine if it is configured to drop IPv6 packets containing a Routing Header of type 0, 1, or 3-255. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets with a Routing Header type 0, 1, or 3-255 as shown in the example below. ipv6 access-list FILTER_IPV6 permit ipv6 any host 2001:DB8::1:1:1234 routing-type 2 deny ipv6 any any log routing permit ipv6 … … … … deny ipv6 any any log Note: The example above allows routing-type 2 in the event Mobility IPv6 is deployed. If the switch is not configured to drop IPv6 packets containing a Routing Header of type 0, 1, or 3-255, this is a finding.

## Group: SRG-NET-000364-RTR-000202

**Group ID:** `V-237766`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 packets containing a Hop-by-Hop header with invalid option type values.

**Rule ID:** `SV-237766r856667_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These options are intended to be for the Destination Options header only. The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize and hence could cause a Denial-of-Service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to determine if it is compliant with this requirement. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets containing a Hop-by-Hop header with option type values of 0x04 (Tunnel Encapsulation Limit), 0xC9 (Home Address Destination), or 0xC3 (NSAP Address) as shown in the example below. ipv6 access-list FILTER_IPV6 deny hbh any any dest-option-type 4 log deny hbh any any dest-option-type 195 log deny hbh any any dest-option-type home-address log permit ipv6 … … … … deny ipv6 any any log If the switch is not configured to drop IPv6 packets containing a Hop-by-Hop header with invalid option type values, this is a finding.

## Group: SRG-NET-000364-RTR-000203

**Group ID:** `V-237772`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 packets containing a Destination Option header with invalid option type values.

**Rule ID:** `SV-237772r856669_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>These options are intended to be for the Hop-by-Hop header only. The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize. Hence, this could cause a Denial-of-Service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to determine if it is compliant with this requirement. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets containing a Destination Option header with option type values of 0x05 (Switch Alert) or 0xC2 (Jumbo Payload) as shown in the example below. ipv6 access-list FILTER_IPV6 deny 60 any any dest-option-type 5 log deny 60 any any dest-option-type 194 log permit ipv6 … … … … deny ipv6 any any log If the switch is not configured to drop IPv6 packets containing a Destination Option header with option type values of 0x05 (Switch Alert) or 0xC2 (Jumbo Payload), this is a finding.

## Group: SRG-NET-000364-RTR-000204

**Group ID:** `V-237774`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 packets containing an extension header with the Endpoint Identification option.

**Rule ID:** `SV-237774r856671_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a Denial-of-Service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. This option type is associated with the Nimrod Routing system and has no defining RFC document.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration to determine if it is compliant with this requirement. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets containing an extension header with the Endpoint Identification option as shown in the example below. ipv6 access-list FILTER_IPV6 deny any any dest-option-type 138 log permit ipv6 … … … … deny ipv6 any any log If the switch is not configured to drop IPv6 packets containing an extension header with the Endpoint Identification option, this is a finding.

## Group: SRG-NET-000364-RTR-000205

**Group ID:** `V-237776`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 packets containing the NSAP address option within Destination Option header.

**Rule ID:** `SV-237776r856673_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a Denial-of-Service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. This option type from RFC 1888 (OSI NSAPs and IPv6) has been deprecated by RFC 4048.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration and determine if filters are bound to the applicable interfaces to drop IPv6 packets containing a Destination Option header with option type value of 0xC3 (NSAP address). Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets containing the NSAP address option within Destination Option header as shown in the example below. ipv6 access-list FILTER_IPV6 deny 60 any any dest-option-type 195 log permit ipv6 … … … … deny ipv6 any any log If the switch is not configured to drop IPv6 packets containing the NSAP address option within Destination Option header, this is a finding.

## Group: SRG-NET-000364-RTR-000206

**Group ID:** `V-237778`

### Rule: The Cisco perimeter switch must be configured to drop IPv6 packets containing a Hop-by-Hop or Destination Option extension header with an undefined option type.

**Rule ID:** `SV-237778r856675_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The optional and extensible natures of the IPv6 extension headers require higher scrutiny since many implementations do not always drop packets with headers that it cannot recognize, and hence could cause a Denial-of-Service on the target device. In addition, the type, length, value (TLV) formatting provides the ability for headers to be very large. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for the DODIN Backbone. Review the switch configuration and determine if filters are bound to the applicable interfaces to drop all inbound IPv6 packets containing an undefined option type value regardless of whether they appear in a Hop-by-Hop or Destination Option header. Undefined values are 0x02, 0x03, 0x06, 0x9 – 0xE, 0x10 – 0x22, 0x24, 0x25, 0x27 – 0x2F, and 0x31 – 0xFF. Step 1: Verify that an inbound IPv6 ACL has been configured on the external interface. interface gigabitethernet1/0 ipv6 address 2001::1:0:22/64 ipv6 traffic-filter FILTER_IPV6 in Step 2: Verify that the ACL drops IPv6 packets containing a Hop-by-Hop or Destination Option extension header with an undefined option type as shown in the example below. ipv6 access-list FILTER_IPV6 deny any any dest-option-type 2 deny any any dest-option-type 3 deny any any dest-option-type 6 deny any any dest-option-type 9 deny any any dest-option-type 10 deny any any dest-option-type 11 deny any any dest-option-type 12 deny any any dest-option-type 13 deny any any dest-option-type 14 deny any any dest-option-type 16 … deny any any dest-option-type 34 deny any any dest-option-type 36 deny any any dest-option-type 37 deny any any dest-option-type 39 … deny any any dest-option-type 47 deny any any dest-option-type 49 … deny any any dest-option-type 255 permit … … … … deny ipv6 any any log Note: Because hop-by-hop and destination options have the same exact header format, they can be combined under the dest-option-type keyword. Since Hop-by-Hop and Destination Option headers have non-overlapping types, you can use dest-option-type to match either. If the switch is not configured to drop IPv6 packets containing a Hop-by-Hop or Destination Option extension header with an undefined option type, this is a finding.

