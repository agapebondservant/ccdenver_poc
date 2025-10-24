# STIG Benchmark: Dell OS10 Switch Layer 2 Switch Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-269953`

### Rule: The Dell OS10 Switch must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-269953r1052245_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection. Satisfies: SRG-NET-000148-L2S-000015, SRG-NET-000343-L2S-000016</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the switch configuration has 802.1x authentication implemented for all access switch ports connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. Verify that 802.1x authentication is enabled globally by reviewing the configuration for the presence of: dot1x system-auth-control Verify that 802.1x authentication is enabled on the host-facing access interfaces by looking for the following two dot1x settings: ! interface ethernet1/1/3 dot1x port-control auto dot1x re-authentication If 802.1x authentication is not on configured on all access switch ports connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-269954`

### Rule: The Dell OS10 Switch must manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-269954r1052477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages). Satisfies: SRG-NET-000193-L2S-000020, SRG-NET-000705-L2S-000110</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that QoS has been enabled to ensure that sufficient capacity is available for mission-critical traffic such as voice and enforce the traffic priorities specified by the Combatant Commanders/Services/Agencies. To verify that QoS has been enabled, review the configuration for each applicable interface to determine if service policies have been configured: ! interface ethernet1/1/1 ... ... service-policy input type qos 6Q_PolicyMapIn_dscp service-policy output type queuing 6Q_PolicyMapOut_100G ! If the switch is not configured to implement a QoS policy, this is a finding.

## Group: SRG-NET-000362-L2S-000021

**Group ID:** `V-269955`

### Rule: The Dell OS10 Switch must have Root Guard enabled on all switch ports connecting to access layer switches and hosts.

**Rule ID:** `SV-269955r1052251_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) does not provide any means for the network administrator to securely enforce the topology of the switched network. Any switch can be the root bridge in a network. However, a more optimal forwarding topology places the root bridge at a specific predetermined location. With the standard STP, any bridge in the network with a lower bridge ID takes the role of the root bridge. The administrator cannot enforce the position of the root bridge but can set the root bridge priority to zero to secure the root bridge position. The root guard feature provides a way to enforce the root bridge placement in the network. If the bridge receives superior STP Bridge Protocol Data Units (BPDUs) on a root guard-enabled port, root guard moves this port to a root-inconsistent STP state, and no traffic can be forwarded across this port while it is in this state. To enforce the position of the root bridge it is imperative that root guard is enabled on all ports where the root bridge should never appear.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch topology as well as the switch configuration to verify that Root Guard is enabled on all switch ports connecting to access layer switches and hosts. For each switch port connecting to access layer switches and hosts, execute the following: OS10# show running-configuration interface ethernet <interface number> Verify Root Guard is enabled: spanning-tree guard root If the switch has not enabled Root Guard on all switch ports connecting to access layer switches and hosts, this is a finding.

## Group: SRG-NET-000362-L2S-000022

**Group ID:** `V-269956`

### Rule: The Dell OS10 Switch must have BPDU Guard enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-269956r1052254_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a rogue switch is introduced into the topology and transmits a Bridge Protocol Data Unit (BPDU) with a lower bridge priority than the existing root bridge, it will become the new root bridge and cause a topology change, rendering the network in a suboptimal state. The STP PortFast BPDU guard enhancement allows network designers to enforce the STP domain borders and keep the active topology predictable. The devices behind the ports that have STP PortFast enabled are not able to influence the STP topology. At the reception of BPDUs, the BPDU guard operation disables the port that has PortFast configured. The BPDU guard transitions the port into err disable state and sends a log message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch topology as well as the switch configuration to verify that BPDU Guard is enabled on all user-facing or untrusted access switch ports. For each user-facing or untrusted access switch port, execute the following: OS10# show running-configuration interface ethernet <interface number> Verify Root Guard is enabled: spanning-tree bpduguard enable If the switch has not enabled BPDU Guard on all user-facing or untrusted access switch ports, this is a finding.

## Group: SRG-NET-000362-L2S-000023

**Group ID:** `V-269957`

### Rule: The Dell OS10 Switch must have STP Loop Guard enabled on all nondesignated STP switch ports.

**Rule ID:** `SV-269957r1052257_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Spanning Tree Protocol (STP) loop guard feature provides additional protection against STP loops. An STP loop is created when an STP blocking port in a redundant topology erroneously transitions to the forwarding state. In its operation, STP relies on continuous reception and transmission of Bridge Protocol Data Unit (BPDUs) based on the port role. The designated port transmits BPDUs, and the nondesignated port receives BPDUs. When one of the ports in a physically redundant topology no longer receives BPDUs, the STP conceives that the topology is loop free. Eventually, the blocking port from the alternate or backup port becomes a designated port and moves to a forwarding state. This situation creates a loop. The loop guard feature makes additional checks. If BPDUs are not received on a nondesignated port and loop guard is enabled, that port is moved into the STP loop-inconsistent blocking state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that STP Loop Guard is enabled on at least all nondesignated STP ports. Verify that the spanning-tree guard loop setting is enabled on each interface. interface ethernet1/1/1 no shutdown switchport mode trunk switchport access vlan 100 flowcontrol receive off spanning-tree guard loop ! If STP Loop Guard is not configured globally or on nondesignated STP ports, this is a finding.

## Group: SRG-NET-000362-L2S-000024

**Group ID:** `V-269958`

### Rule: The Dell OS10 Switch must have Unknown Unicast Flood Blocking (UUFB) enabled.

**Rule ID:** `SV-269958r1052260_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access layer switches use the Content Addressable Memory (CAM) table to direct traffic to specific ports based on the VLAN number and the destination MAC address of the frame. When a router has an Address Resolution Protocol (ARP) entry for a destination host and forwards it to the access layer switch and there is no entry corresponding to the frame's destination MAC address in the incoming VLAN, the frame will be sent to all forwarding ports within the respective VLAN, which causes flooding. Large amounts of flooded traffic can saturate low-bandwidth links, causing network performance issues or complete connectivity outage to the connected devices. Unknown unicast flooding has been a nagging problem in networks that have asymmetric routing and default timers. To mitigate the risk of a connectivity outage, the Unknown Unicast Flood Blocking (UUFB) feature must be implemented on all access layer switches. The UUFB feature will block unknown unicast traffic flooding and only permit egress traffic with MAC addresses that are known to exit on the port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configuration to verify that unknown unicast traffic is blocked by storm control is on all host-facing switch ports. For each host-facing switch port: interface ethernet1/1/1 switchport access vlan 100 storm-control unknown-unicast 1 If the switch has not enabled unknown unicast storm control on all host-facing switch ports, this is a finding.

## Group: SRG-NET-000362-L2S-000025

**Group ID:** `V-269959`

### Rule: The Dell OS10 Switch must have DHCP snooping for all user VLANs to validate DHCP messages from untrusted sources.

**Rule ID:** `SV-269959r1052263_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In an enterprise network, devices under administrative control are trusted sources. These devices include the switches, routers, and servers in the network. Host ports and unknown DHCP servers are considered untrusted sources. An unknown DHCP server on the network on an untrusted port is called a spurious DHCP server, any device (PC, Wireless Access Point) that is loaded with DHCP server enabled. The DHCP snooping feature determines whether traffic sources are trusted or untrusted. The potential exists for a spurious DHCP server to respond to DHCPDISCOVER messages before the real server has time to respond. DHCP snooping allows switches on the network to trust the port a DHCP server is connected to and not trust the other ports. The DHCP snooping feature validates DHCP messages received from untrusted sources and filters out invalid messages as well as rate-limits DHCP traffic from trusted and untrusted sources. DHCP snooping feature builds and maintains a binding database, which contains information about untrusted hosts with leased IP addresses, and it uses the database to validate subsequent requests from untrusted hosts. Other security features, such as IP Source Guard and Dynamic Address Resolution Protocol (ARP) Inspection (DAI), also use information stored in the DHCP snooping binding database. Hence, it is imperative that the DHCP snooping feature is enabled on all VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configuration and verify that DHCP snooping is enabled on all user VLANs. Verify that DHCP snooping is enabled globally: ip dhcp snooping Verify that interfaces attached to trusted DHCP servers are configured: interface ethernet 1/1/4 ip dhcp snooping trust Verify that static DHCP snooping entries are in the binding table: ip dhcp snooping binding mac 00:04:96:70:8a:12 vlan 100 ip 100.1.1.2 interface ethernet 1/1/1 Note that OS10 supports three types of source address validation of trusted DHCP servers: source IP address validation, source IP and MAC address validation, and DHCP source MAC address validation. If the switch does not have DHCP snooping enabled for all user VLANs to validate DHCP messages from untrusted sources, this is a finding.

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-269960`

### Rule: The Dell OS10 Switch must have Source Address Validation (SAV) enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-269960r1052266_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard provides source IP address filtering on a Layer 2 port to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted Layer 2 access ports. Initially, all IP traffic on the protected port is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configuration and verify that SAV is enabled on all user-facing or untrusted access switch ports. Verify that DHCP snooping is enabled globally: ip dhcp snooping Verify that interfaces attached to trusted DHCP servers are configured: interface ethernet 1/1/4 ip dhcp snooping trust Enable source IP and MAC address validation in INTERFACE mode for each untrusted and user-facing port: ip dhcp snooping source-address-validation ipmac If the switch does not have DHCP snooping is enabled globally, a trusted DHCP server port specified, and Source Address Validation enabled for all user-facing or untrusted access switch ports, this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-269961`

### Rule: The Dell OS10 Switch must have Dynamic Address Resolution Protocol (ARP) Inspection (DAI) enabled on all user VLANs.

**Rule ID:** `SV-269961r1052492_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts ARP requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that DAI feature is enabled on all user VLANs. Verify that each user VLAN has arp inspection enabled. ! interface vlan200 no shutdown arp inspection ! interface vlan201 no shutdown arp inspection If ARP inspection is not enabled on all user VLANs, this is a finding.

## Group: SRG-NET-000512-L2S-000001

**Group ID:** `V-269962`

### Rule: The Dell OS10 Switch must have Storm Control configured on all host-facing switch ports.

**Rule ID:** `SV-269962r1052327_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a LAN, creating excessive traffic and degrading network performance. Traffic storm control prevents network disruption by suppressing ingress traffic when the number of packets reaches a configured threshold level. Traffic storm control monitors ingress traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configuration to verify that storm control is enabled on all host-facing switch ports. For each host-facing switch port: interface ethernet1/1/1 switchport access vlan 100 storm-control broadcast 1000 storm-control multicast rate 100 Mbps storm-control unknown-unicast rate 600 Kbps Note that the rates may be entered in bits per second or packets per second units. If the switch has not enabled storm control on all host-facing switch ports, this is a finding.

## Group: SRG-NET-000512-L2S-000002

**Group ID:** `V-269963`

### Rule: The Dell OS10 Switch must have IGMP or MLD Snooping configured on all VLANs

**Rule ID:** `SV-269963r1052275_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP and MLD snooping provides a way to constrain multicast traffic at Layer 2. By monitoring the IGMP or MLD membership reports sent by hosts within a VLAN, the snooping application can set up Layer 2 multicast forwarding tables to deliver specific multicast traffic only to interfaces connected to hosts interested in receiving the traffic, thereby significantly reducing the volume of multicast traffic that would otherwise flood the VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configuration to verify that IGMP or MLD snooping has been configured for IPv4 and IPv6 multicast traffic, respectively. Verify that IGMP and MLD snooping have not been disabled globally by checking that the following have not been configured: no ip igmp snooping enable no ipv6 mld snooping enable Verify that IGMP or MLD snooping have not been disabled on any of the individual VLANs: Interface vlan 100 no ip igmp snooping no ipv6 mld snooping If the switch is not configured to implement IGMP or MLD snooping for each VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000003

**Group ID:** `V-269964`

### Rule: The Dell OS10 Switch must implement Rapid Spanning Tree Protocol (STP) where VLANs span multiple switches with redundant links.

**Rule ID:** `SV-269964r1052278_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>STP is implemented on bridges and switches to prevent Layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Rapid STP should be deployed by implementing either Rapid Per-VLAN-Spanning-Tree (Rapid-PVST) or Multiple Spanning-Tree Protocol (MSTP); the latter scales much better when there are many VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In cases where VLANs do not span multiple switches, it is a best practice to not implement STP. Avoiding the use of STP will provide the most deterministic and highly available network topology. If STP is required, then review the switch configuration to verify that Rapid STP has been implemented. OS10# show running-configuration ... ... spanning-tree mode rstp Note: MSTP can be configured as an alternate mode. MSTP uses RSTP for rapid convergence and enables multiple VLANs to be grouped into and mapped to the same spanning-tree instance, thereby reducing the number of spanning-tree instances needed to support many VLANs. OS10# show running-configuration ... ... spanning-tree mode mst If Rapid STP or MSTP have not been implemented where STP is required, this is a finding.

## Group: SRG-NET-000512-L2S-000004

**Group ID:** `V-269965`

### Rule: The Dell OS10 Switch must enable Far-End Failure Detection (FEFD) to protect against one-way connections.

**Rule ID:** `SV-269965r1052281_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In topologies where fiber-optic interconnections are used, physical misconnections can occur that allow a link to appear to be up when there is a mismatched set of transmit/receive pairs. When such a physical misconfiguration occurs, protocols such as STP can cause network instability. UDLD is a Layer 2 protocol that can detect these physical misconfigurations by verifying that traffic is flowing bidirectionally between neighbors. Ports with UDLD enabled periodically transmit packets to neighbor devices. If the packets are not echoed back within a specific time frame, the link is flagged as unidirectional and the interface is shut down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Dell OS10 provides a proprietary protocol, FEFD, to protect against one-way connections. Verify that FEFD is configured on the appropriate ethernet interfaces by reviewing the FEFD status to verify the desired interfaces are in mode Normal or Aggressive. OS10# show fefd FEFD is globally 'OFF', interval is 15 seconds. INTERFACE MODE INTERVAL STATE ============================================================ eth1/1/1 NA NA Idle (Not running) eth1/1/2 NA NA Idle (Not running) eth1/1/3 NA NA Idle (Not running) eth1/1/4 NA NA Idle (Not running) eth1/1/5 NA NA Idle (Not running) eth1/1/6 Normal 15 Unknown eth1/1/7 Aggressive 15 Unknown eth1/1/8 NA NA Idle (Not running) … If FEFD is not configured on the appropriate interfaces, this is a finding.

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-269966`

### Rule: The Dell OS10 Switch must have all disabled switch ports assigned to an unused VLAN.

**Rule ID:** `SV-269966r1052284_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a disabled port that is assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result gains access to that VLAN as a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and examine all access switch ports. Each access switch port not in use should have membership to an inactive VLAN that is not used for any purpose and is not allowed on any trunk links. Verify that there is a shutdown VLAN configured for unused ports: ! interface vlan999 description "Unused VLAN" shutdown Verify that the unused switch ports are assigned to the inactive VLAN: ! interface ethernet1/1/57 shutdown switchport access vlan 999 flowcontrol receive off ! interface ethernet1/1/58 shutdown switchport access vlan 999 flowcontrol receive off Verify that no trunk links are configured to accept the unused VLAN ID: ! interface ethernet1/1/1 no shutdown switchport mode trunk switchport access vlan 100 flowcontrol receive off If there are any access switch ports not in use and not in an inactive VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000008

**Group ID:** `V-269967`

### Rule: The Dell OS10 Switch must not have the default VLAN assigned to any host-facing switch ports.

**Rule ID:** `SV-269967r1052287_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a VLAN-based network, switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with other networking devices using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. Therefore, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and verify that no access switch ports have been assigned membership to the default VLAN (i.e., VLAN 1). VLAN assignments can be verified via the “show vlan” command: OS10# show vlan Codes: * - Default VLAN, M - Management VLAN, R - Remote Port Mirroring VLANs, @ - Attached to Virtual Network, P - Primary, C - Community, I - Isolated, S - VLAN-Stack VLAN Q: A - Access (Untagged), T - Tagged NUM Status Description Q Ports * 1 Inactive 30 Inactive Management VLAN 100 Inactive A Eth1/1/1 200 Inactive A Eth1/1/3-1/1/58 201 Inactive A Eth1/1/2 OS10# If there are access switch ports assigned to the default VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000009

**Group ID:** `V-269968`

### Rule: The Dell OS10 Switch must have the default VLAN pruned from all trunk ports that do not require it.

**Rule ID:** `SV-269968r1052290_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default VLAN (i.e., VLAN 1) is a special VLAN used for control plane traffic such as Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP). VLAN 1 is enabled on all trunks and ports by default. With larger campus networks, use caution regarding the diameter of the STP domain for the default VLAN. Instability in one part of the network could affect the default VLAN, thereby influencing control-plane stability and therefore STP stability for all other VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the OS10 switch configuration and verify that the default VLAN is pruned from the allowed VLANs on trunk links that do not require it: interface ethernet 1/1/1 no shutdown switchport mode trunk switchport access vlan 99 switchport trunk allowed vlan 2100-2102 If the default VLAN is not pruned from trunk links that should not be transporting frames for the VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000010

**Group ID:** `V-269969`

### Rule: The Dell OS10 Switch must not use the default VLAN for management traffic.

**Rule ID:** `SV-269969r1052293_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with directly connected switches using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. Therefore, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the OS10 switch configuration and verify that the default VLAN is not used to access the switch for management: interface vlan30 description "Management VLAN" no shutdown ip address 10.10.1.1/24 If the default VLAN is being used to access the switch, this is a finding.

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-269970`

### Rule: The Dell OS10 Switch must have all user-facing or untrusted ports configured as access switch ports.

**Rule ID:** `SV-269970r1052296_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configurations and examine all user-facing or untrusted switch ports. The example below shows both trunk port and user-facing access ports: interface ethernet 1/1/1 no shutdown switchport mode trunk switchport access vlan 99 switchport trunk allowed vlan 2100-2102 ! interface ethernet1/1/2 no shutdown switchport access vlan 201 flowcontrol receive off ! interface ethernet1/1/3 no shutdown switchport access vlan 200 flowcontrol receive off Note: The default switchport mode is access, so it will not be displayed when viewing the configuration of the user-facing ports. If any of the user-facing switch ports are configured as a trunk, this is a finding.

## Group: SRG-NET-000512-L2S-000013

**Group ID:** `V-269971`

### Rule: The Dell OS10 Switch must not have any switch ports assigned to the native VLAN.

**Rule ID:** `SV-269971r1052299_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim’s MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker’s VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim’s VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Dell OS10 Switch configurations and examine all access switch ports. Verify that they do not belong to the native VLAN of the trunk ports. The native VLAN on trunk ports is set by the switchport access vlan command on those ports. In the example below, the native VLAN is 99 and the access ports must be configured to other VLANs. interface ethernet 1/1/1 no shutdown switchport mode trunk switchport access vlan 99 switchport trunk allowed vlan 2100-2102 ! interface ethernet1/1/2 no shutdown switchport access vlan 201 flowcontrol receive off ! interface ethernet1/1/3 no shutdown switchport access vlan 200 flowcontrol receive off If any access switch ports have been assigned to the same VLAN ID as the native VLAN, this is a finding.

## Group: SRG-NET-000715-L2S-000120

**Group ID:** `V-269972`

### Rule: The Dell OS10 Switch must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

**Rule ID:** `SV-269972r1052302_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command-and-control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions. Satisfies: SRG-NET-000715-L2S-000120, SRG-NET-000512-L2S-000012</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and verify that no access switch ports have been assigned membership to the default VLAN (i.e., VLAN 1). VLAN assignments can be verified via the “show vlan” command: OS10# show vlan Codes: * - Default VLAN, M - Management VLAN, R - Remote Port Mirroring VLANs, @ - Attached to Virtual Network, P - Primary, C - Community, I - Isolated, S - VLAN-Stack VLAN Q: A - Access (Untagged), T - Tagged NUM Status Description Q Ports * 1 Inactive 30 Inactive Management VLAN 100 Inactive A Eth1/1/1 200 Inactive A Eth1/1/3-1/1/58 201 Inactive A Eth1/1/2 OS10# If there are access switch ports assigned to the default VLAN, this is a finding.

