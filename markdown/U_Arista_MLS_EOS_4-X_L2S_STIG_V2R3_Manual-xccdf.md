# STIG Benchmark: Arista MLS EOS 4.X L2S Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-255968`

### Rule: The Arista MLS layer 2 switch must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-255968r882246_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection. Satisfies: SRG-NET-000148-L2S-000015, SRG-NET-000343-L2S-000016</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista MLS switch configuration has 802.1x authentication implemented for all access switch ports connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. MAC Authentication Bypass (MAB) must be configured on switch ports connected to devices that do not provide an 802.1x supplicant. Verify the Arista MLS switch configuration for 802.1x is configured globally and, on the required host-based access ports or MAB, is configured on ports that require RADIUS and MAC-based supplicants. switch# show run | section dot1x logging level DOT1X informational  aaa authentication dot1x default group radius  dot1x system-auth-control ! interface Ethernet6 description 802.1X Access Network switchport access vlan 100 dot1x pae authenticator dot1x reauthentication dot1x port-control auto dot1x host-mode single-host dot1x timeout quiet-period 10 ! interface Ethernet7 description STIG MAC-Based Authentication speed 100full dot1x pae authenticator dot1x port-control auto dot1x mac based authentication ! If 802.1x authentication or MAB is not configured on all access switch ports connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-255969`

### Rule: The Arista MLS layer 2 switch must be configured for Storm Control to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-255969r991773_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding distributed DoS (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages). Satisfies: SRG-NET-000193-L2S-000020, SRG-NET-000362-L2S-000024, SRG-NET-000512-L2S-000001</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista MLS switch is configured for storm-control on applicable Ethernet interfaces. switch#show storm-control Port Type Level Rate(Mbps) Status Drops Reason Et10/2 all 75 7500 active 0 Et4 multicast 55 5500 active 0 Et4 broadcast 50 5000 active switch# If the Arista MLS switch is not configured to implement a storm-control policy, this is a finding.

## Group: SRG-NET-000362-L2S-000021

**Group ID:** `V-255970`

### Rule: The Arista MLS switch must have Root Guard enabled on all switch ports connecting to access layer switches and hosts.

**Rule ID:** `SV-255970r882252_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) does not provide any means for the network administrator to securely enforce the topology of the switched network. Any switch can be the root bridge in a network. However, a more optimal forwarding topology places the root bridge at a specific predetermined location. With the standard STP, any bridge in the network with a lower bridge ID takes the role of the root bridge. The administrator cannot enforce the position of the root bridge but can set the root bridge priority to 0 in an effort to secure the root bridge position.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch topology as well as the configuration to verify that root guard is enabled on switch ports facing switches that are downstream from the root bridge. Example: switch#sh run | sec guard root interface Ethernet37 spanning-tree guard root If the Arista MLS switch has not enabled guard root on all ports connecting to the access layer where the root bridge must not appear, this is a finding.

## Group: SRG-NET-000362-L2S-000022

**Group ID:** `V-255971`

### Rule: The Arista MLS layer 2 switch must have BPDU Guard enabled on all switch ports connecting to access layer switches and hosts.

**Rule ID:** `SV-255971r882255_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a rogue switch is introduced into the topology and transmits a Bridge Protocol Data Unit (BPDU) with a lower bridge priority than the existing root bridge, it will become the new root bridge and cause a topology change, rendering the network in a suboptimal state. The STP PortFast BPDU guard enhancement allows network designers to enforce the STP domain borders and keep the active topology predictable. The devices behind the ports that have STP PortFast enabled are not able to influence the STP topology. At the reception of BPDUs, the BPDU guard operation disables the port that has PortFast configured. The BPDU guard transitions the port into a disabled state and sends a log message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS to verify that BPDU Guard is enabled on all user-facing or untrusted access switch ports. switch#show run | section bpdu interface Ethernet37 spanning-tree bpduguard enable If the Arista MLS switch has not enabled BPDU Guard, this is a finding.

## Group: SRG-NET-000362-L2S-000023

**Group ID:** `V-255972`

### Rule: The Arista MLS switch must have STP Loop Guard enabled on all nondesignated STP switch ports.

**Rule ID:** `SV-255972r1107168_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Spanning Tree Protocol (STP) loop guard feature provides additional protection against STP loops. An STP loop is created when an STP blocking port in a redundant topology erroneously transitions to the forwarding state. In its operation, STP relies on continuous reception and transmission of BPDUs based on the port role. The designated port transmits BPDUs, and the nondesignated port receives BPDUs. When one of the ports in a physically redundant topology no longer receives BPDUs, the STP conceives that the topology is loop free. Eventually, the blocking port from the alternate or backup port becomes a designated port and moves to a forwarding state. This situation creates a loop. The loop guard feature makes additional checks. If BPDUs are not received on a nondesignated port and loop guard is enabled, that port is moved into the STP loop-inconsistent blocking state. In topologies where fiber optic interconnections are used, physical misconnections can occur that allow a link to appear to be up when there is a mismatched set of transmit/receive pairs. When such a physical misconfiguration occurs, protocols such as STP can cause network instability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration to verify that STP Loop Guard is enabled. It can be enabled globally or applied to an interface. Note: Arista uses STP Loop guard to protect against one-way connections. switch# sh run | sec spanning-tree spanning-tree guard loop default Or, interface Ethernet6 spanning-tree guard loop If STP Loop Guard is not configured globally or on nondesignated STP ports, this is a finding.

## Group: SRG-NET-000362-L2S-000025

**Group ID:** `V-255973`

### Rule: The Arista MLS layer 2 switch must have DHCP snooping for all user VLANs to validate DHCP messages from untrusted sources.

**Rule ID:** `SV-255973r882261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In an enterprise network, devices under administrative control are trusted sources. These devices include the switches, routers, and servers in the network. Host ports and unknown DHCP servers are considered untrusted sources. An unknown DHCP server on the network on an untrusted port is called a spurious DHCP server, any device (PC, Wireless Access Point) that is loaded with DHCP server enabled. The DHCP snooping feature determines whether traffic sources are trusted or untrusted. The potential exists for a spurious DHCP server to respond to DHCPDISCOVER messages before the real server has time to respond. DHCP snooping allows switches on the network to trust the port a DHCP server is connected to and not trust the other ports. The DHCP snooping feature validates DHCP messages received from untrusted sources and filters out invalid messages as well as rate-limits DHCP traffic from trusted and untrusted sources. DHCP snooping feature builds and maintains a binding database, which contains information about untrusted hosts with leased IP addresses, and it utilizes the database to validate subsequent requests from untrusted hosts. Other security features, such as IP Source Guard and Dynamic Address Resolution Protocol (ARP) Inspection (DAI), also use information stored in the DHCP snooping binding database. Hence, it is imperative that the DHCP snooping feature is enabled on all user VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration and verify that DHCP snooping is enabled on all user VLANs. Verify the Arista MLS has the DHCP Snooping feature enabled globally by executing "show ip dhcp snooping". switch(config)# show ip dhcp snooping DHCP Snooping is enabled DHCP Snooping is operational DHCP Snooping is configured on following VLANs: 650 DHCP Snooping is operational on following VLANs: 650 If the Arista MLS switch does not have DHCP snooping enabled for all user VLANs to validate DHCP messages from untrusted sources, this is a finding.

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-255974`

### Rule: The Arista MLS layer 2 switch must have IP Source Guard enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-255974r882264_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard (IPSG) provides source IP address filtering on a layer 2 port to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted Layer 2 access ports. Initially, all IP traffic on the protected port is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration to verify that IPSG is enabled on all user-facing or untrusted access switch ports. Step 1: The Arista MLS switch command verifies the IPSG configuration and operational states. switch(config)#show ip verify source Interface Operational State --------------- ------------------------ Ethernet1 IP source guard enabled Ethernet2 IP source guard disabled Step 2: The following command displays all VLANs configured in no IP verify source VLAN: switch(config)#show ip verify source vlan IPSG disabled on VLANS: 1-2 VLAN Operational State --------------- ------------------------ 1 IP source guard disabled 2 Error: vlan classification failed If the Arista MLS switch does not have IP Source Guard enabled on all untrusted access switch ports, this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-255975`

### Rule: The Arista MLS layer 2 switch must have Dynamic Address Resolution Protocol (ARP) Inspection (DAI) enabled on all user VLANs.

**Rule ID:** `SV-255975r882267_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts Address Resolution Protocol (ARP) requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration to verify that Dynamic Address Resolution Protocol (ARP) Inspection (DAI) feature is enabled on all user VLANs. Verify ARP inspection for user VLANs by the following command: sh ip arp inspection vlan VLAN 2200 ------------ Configuration: Enabled Operation State: Active If static ARP inspection is not enabled on all user VLANs, this is a finding.

## Group: SRG-NET-000512-L2S-000002

**Group ID:** `V-255976`

### Rule: The Arista MLS layer 2 switch must have IGMP or MLD Snooping configured on all VLANs.

**Rule ID:** `SV-255976r882270_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP and MLD snooping provides a way to constrain multicast traffic at Layer 2. By monitoring the IGMP or MLD membership reports sent by hosts within a VLAN, the snooping application can set up Layer 2 multicast forwarding tables to deliver specific multicast traffic only to interfaces connected to hosts interested in receiving the traffic, thereby significantly reducing the volume of multicast traffic that would otherwise flood the VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration to verify that IGMP or MLD snooping has been configured. Determine which snooping feature is used. For IGMP: Verify the PIM that also enables IGMP on an Arista MLS switch VLAN interface by using the "sh run interface vlan8" command: switch(config)#sh run int vlan8 interface VLAN8 ip igmp pim ipv4 sparse-mode switch(config)#exit For MLD: Verify the Arista MLS switch is configured for MLD snooping on an interface for version 1 and 2. Version 2 is the default MLD version. switch#sh run | section mld mld snooping vlan 200 If the Arista switch is not configured to implement IGMP or MLD snooping for each VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000003

**Group ID:** `V-255977`

### Rule: The Arista MLS layer 2 Arista MLS switch must implement Rapid STP where VLANs span multiple switches with redundant links.

**Rule ID:** `SV-255977r882273_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) is implemented on bridges and switches to prevent layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Multiple Spanning-Tree (802.1s) instead of Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Multiple Spanning-Tree Protocol (MSTP) should be deployed by implementing either Rapid Per-VLAN-Spanning-Tree (Rapid-PVST) or Multiple Spanning-Tree MST, the latter scales topologies much better when there are many VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In cases where VLANs do not span multiple switches, it is a best practice to not implement STP. Avoiding the use of STP will provide the most deterministic and highly available network topology. If STP is required, review the Arista MLS switch configuration to verify that Rapid STP has been implemented. switch(config)#sh run | sec spanning-tree spanning-tree mode rstp ! Note: MSTP can be configured as an alternate mode. MSTP uses RSTP for rapid convergence and enables multiple VLANs to be grouped into and mapped to the same spanning-tree instance, thereby reducing the number of spanning-tree instances needed to support a large number of VLANs. If MSTP or Rapid STP has not been implemented where STP is required, this is a finding.

## Group: SRG-NET-000512-L2S-000005

**Group ID:** `V-255979`

### Rule: The Arista MLS layer 2 switch must have all trunk links enabled statically.

**Rule ID:** `SV-255979r882279_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When trunk negotiation is enabled via Dynamic Trunk Protocol (DTP), considerable time can be spent negotiating trunk settings (802.1q or ISL) when a node or interface is restored. While this negotiation is happening, traffic is dropped because the link is up from a layer 2 perspective. Packet loss can be eliminated by setting the interface statically to trunk mode, thereby avoiding dynamic trunk protocol negotiation and significantly reducing any outage when restoring a failed link or switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration to verify that all Ethernet interfaces designated as trunk links are statically configured to specify only member tagged VLAN traffic is allowed and all nonmember VLAN traffic will be dropped unless untagged traffic is associated with the interface's native VLAN. switch#show run | section trunk ! interface Ethernet6 description STIG Static Trunk speed forced 10000full switchport trunk native vlan 2102 switchport trunk allowed vlan 2100-2102 switchport mode trunk ! If trunk negotiation is enabled on any interface, this is a finding.

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-255980`

### Rule: The Arista MLS layer 2 switch must have all disabled switch ports assigned to an unused VLAN.

**Rule ID:** `SV-255980r991774_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a disabled port that is assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result gains access to that VLAN as a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Review the switch configuration and examine all access switch ports. Verify the unused port is configured to be intentionally shut down and assigned to an inactive VLAN. switch(config)#sh run int eth8 interface Ethernet8 description PORT IS INTENTIONALLY SHUTDOWN switchport access vlan 999 shutdown switch(config)# Step 2: Verify traffic from the inactive VLAN is not allowed on any trunk links as shown in the example below: switch(config)#sh run int eth9 interface Ethernet9 switchport trunk native vlan 1000 switchport trunk allowed vlan 2-998, 1001-4094 switchport mode trunk switch(config)# If any access switch ports are not in use and not in an inactive shutdown, this is a finding. Note: Switch ports configured for 802.1x are exempt from this requirement.

## Group: SRG-NET-000512-L2S-000008

**Group ID:** `V-255981`

### Rule: The Arista MLS layer 2 switch must not have the default VLAN assigned to any host-facing switch ports.

**Rule ID:** `SV-255981r991775_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a VLAN-based network, switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with other networking devices using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. As a consequence, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configurations and verify no access switch ports have been assigned membership to the default VLAN (i.e., VLAN 1). switch(config)#sh vlan VLAN Name Status Ports ----- -------------------------------- --------- ------------------------------- 1 default 8 VLAN0008 active Cpu 25 VLAN0025 active Cpu 100 VLAN0100 active Cpu 1000 VLAN1000 active Eth1, Eth2 If access switch ports are assigned to the default VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000009

**Group ID:** `V-255982`

### Rule: The Arista MLS layer 2 switch must have the default VLAN pruned from all trunk ports that do not require it.

**Rule ID:** `SV-255982r991776_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default VLAN (i.e., VLAN 1) is a special VLAN used for control plane traffic such as Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP). VLAN 1 is enabled on all trunks and ports by default. With larger campus networks, care needs to be taken about the diameter of the STP domain for the default VLAN. Instability in one part of the network could affect the default VLAN, thereby influencing control-plane stability and therefore STP stability for all other VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration and verify the default VLAN is pruned from trunk links that do not require it. Step 1: Review the Arista MLS switch configuration by using the following commands to ensure the default VLAN 1 state is suspended: switch(config)#vlan 1 switch(config-vlan-1)#sh act vlan !! STIG suspend vlan 1 #state suspend vlan 1 switch(config-vlan-1)#exit Step 2: Review the configuration to ensure default VLAN 1 is pruned from any trunk active links by using the command "show vlan brief": switch(config-vlan-4090)# switch(config-vlan-4090)#sh vlan brie VLAN Name Status Ports ----- -------------------------------- --------- ------------------------------- 1 default 8 VLAN0008 active Cpu 25 VLAN0025 active Cpu 100 VLAN0100 active Cpu 1000 VLAN1000 active 4090 VLAN4090 active If the default VLAN state is not suspended and pruned from trunk links that should not be transporting frames for the VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000010

**Group ID:** `V-255983`

### Rule: The Arista MLS layer 2 switch must not use the default VLAN for management traffic.

**Rule ID:** `SV-255983r991777_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with directly connected switches using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. As a consequence, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Arista MLS configuration for a Management_Network VRF instance globally on the switch with the following example: switch(config)#sh run | sec vrf ip name-server vrf default 192.168.10.20 ! vrf instance Management_Network ! interface Ethernet12 description MANAGEMENT NETWORK PORT no switchport vrf Management_Network ip address 10.10.40.254/30 ! ip routing vrf Management_Network If the VRF is not configured to prevent the default VLAN from being used to access the switch, this is a finding.

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-255984`

### Rule: The Arista MLS layer 2 switch must have all user-facing or untrusted ports configured as access switch ports.

**Rule ID:** `SV-255984r991778_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configurations and examine all user-facing or untrusted switch ports configured as access switch ports. switch(config)# show run interface ethernet 13 - 15 interface Ethernet13 switchport access vlan 100 interface Ethernet14 switchport access vlan 100 interface Ethernet14 switchport access vlan 100 If any of the user-facing switch ports are configured as a trunk, this is a finding.

## Group: SRG-NET-000512-L2S-000012

**Group ID:** `V-255985`

### Rule: The Arista MLS layer 2 switch must have the native VLAN assigned to an ID other than the default VLAN for all 802.1q trunk links.

**Rule ID:** `SV-255985r991779_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VLAN hopping can be initiated by an attacker who has access to a switch port belonging to the same VLAN as the native VLAN of the trunk link connecting to another switch that the victim is connected to. If the attacker knows the victim’s MAC address, it can forge a frame with two 802.1q tags and a layer 2 header with the destination address of the victim. Since the frame will ingress the switch from a port belonging to its native VLAN, the trunk port connecting to the victim’s switch will simply remove the outer tag because native VLAN traffic is to be untagged. The switch will forward the frame on to the trunk link unaware of the inner tag with a VLAN ID of which the victim’s switch port is a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Arista MLS switch configuration for all trunk ports to have a unique native VLAN ID that is not the default VLAN 1 by using the following example: switch(config)#sh run | sec native vlan interface Ethernet4 description STIG Disable_VLAN 1 and native vlan to 1000 switchport trunk native vlan 1000 switchport trunk allowed vlan 2-4094 If the native VLAN has the same VLAN ID as the default VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000013

**Group ID:** `V-255986`

### Rule: The Arista MLS layer 2 switch must not have any switch ports assigned to the native VLAN.

**Rule ID:** `SV-255986r991780_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim’s MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker’s VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim’s VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration for all trunking ports to determine the native VLAN by using the following example (for vlan 1000): switch(config-if-Et4)#sh run int eth4 interface Ethernet4 description STIG Disable_VLAN 1 and native vlan to 1000 switchport trunk native vlan 1000 switchport trunk allowed vlan 2-999,1001-4094 switch(config-if-Et4)# Review the configuration to ensure no access switch ports are configured in the native VLAN by using the following example (for vlan 1000): swtich#sh vlan brief VLAN Name Status Ports ----- -------------------------------- --------- ------------------------------- 1 default 8 VLAN0008 active Cpu 25 VLAN0025 active Cpu 100 VLAN0100 active Cpu 1000 VLAN1000 active 4090 VLAN4090 active If any access switch ports have been assigned to the same VLAN ID as the native VLAN, this is a finding.

