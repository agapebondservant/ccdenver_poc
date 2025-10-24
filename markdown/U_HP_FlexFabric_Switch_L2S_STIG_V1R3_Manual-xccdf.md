# STIG Benchmark: HP FlexFabric Switch L2S Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000131-L2S-000014

**Group ID:** `V-65961`

### Rule: The HP FlexFabric Switch must be configured to disable non-essential capabilities.

**Rule ID:** `SV-80451r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised switch introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each switch is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to determine if services or functions not required for operation, or not related to switch functionality, are enabled. If unnecessary services and functions are enabled on the HP FlexFabric Switch, this is a finding. [HP] display ftp-server FTP is not configured. [HP] display current-configuration | include telnet Note: When Telnet server is enabled, the output for this command is telnet server enable.

## Group: SRG-NET-000343-L2S-000016

**Group ID:** `V-66051`

### Rule: HP FlexFabric Switch must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-80541r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication or MAC authentication can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all access switch ports connecting to LAN outlets are configured for 802.1x or MAC authentication as shown in these configuration examples. 802.1x example: interface Ten-GigabitEthernet1/0/4 port link-mode bridge port access vlan 200 dot1x MAC authentication example: interface Ten-GigabitEthernet1/0/5 port link-mode bridge port access vlan 200 mac-authentication If all access switch ports connecting to LAN outlets are not configured for 802.1x or MAC authentication, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-66057`

### Rule: The HP FlexFabric Switch must manage excess bandwidth to limit the effects of packet flooding types of denial of service (DoS) attacks.

**Rule ID:** `SV-80547r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding DDoS attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check if the HP FlexFabric Switch is configured to protect against known DoS attacks by implementing a control plane QoS policy to rate limit specify traffic types destined to the switch. [HP] display qos policy control-plane pre-defined [HP] display qos policy user-defined If the HP FlexFabric Switch is not configured with a control plane QoS policy, this is a finding.

## Group: SRG-NET-000331-L2S-000001

**Group ID:** `V-66059`

### Rule: The HP FlexFabric Switch must provide the capability for authorized users to select a user session to capture.

**Rule ID:** `SV-80549r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to select a user session to capture/record or view/hear, investigations into suspicious or harmful events would be hampered by the volume of information captured. The volume of information captured may also adversely impact the operation for the network. Session audits may include port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the HP FlexFabric Switch is capable of capturing ingress and egress packets from any designated switch port for the purpose of monitoring a specific user session. If the HP FlexFabric Switch is not capable of capturing ingress and egress packets from a designated switch port, this is a finding. [HP]display mirroring-group X Mirroring group X: Type: Remote source Status: Active Mirroring port: GigabitEthernet1/0/1 Both Monitor port: GigabitEthernet1/0/2

## Group: SRG-NET-000332-L2S-000002

**Group ID:** `V-66061`

### Rule: The HP FlexFabric Switch must provide the capability for authorized users to remotely view, in real time, all content related to an established user session from a component separate from the HP FlexFabric Switch.

**Rule ID:** `SV-80551r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to remotely view/hear all content related to a user session, investigations into suspicious user activity would be hampered. Real-time monitoring allows authorized personnel to take action before additional damage is done. The ability to observe user sessions as they are happening allows for interceding in ongoing events that after-the-fact review of captured content would not allow.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the HP FlexFabric Switch is capable of capturing ingress and egress packets from any designated switch port for the purpose of remotely monitoring a specific user session. If the HP FlexFabric Switch is not capable of capturing ingress and egress packets from a designated switch port for the purpose of remotely monitoring a specific user session, this is a finding.

## Group: SRG-NET-000362-L2S-000021

**Group ID:** `V-66063`

### Rule: The HP FlexFabric Switch must have Root Guard enabled on all ports where the root bridge should not appear.

**Rule ID:** `SV-80553r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) does not provide any means for the network administrator to securely enforce the topology of the switched network. Any switch can be the root bridge in a network. However, a more optimal forwarding topology places the root bridge at a specific predetermined location. With the standard STP, any bridge in the network with a lower bridge ID takes the role of the root bridge. The administrator cannot enforce the position of the root bridge but can set the root bridge priority to 0 in an effort to secure the root bridge position. The root guard feature provides a way to enforce the root bridge placement in the network. If the bridge receives superior STP Bridge Protocol Data Units (BPDUs) on a root guard-enabled port, root guard moves this port to a root-inconsistent STP state and no traffic can be forwarded across this port while it is in this state. To enforce the position of the root bridge it is imperative that root guard is enabled on all ports where the root bridge should never appear.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch topology as well as the configuration to verify that root guard is enabled on switch ports facing users or switches that are downstream from the root bridge. If the switch has not enabled Root Guard on all ports where the root bridge should not appear, this is a finding. [HP]display stp -------[CIST Global Info][Mode MSTP]------- Bridge ID : 0.bcea-fa14-f0a4 Bridge times : Hello 2s MaxAge 20s FwdDelay 15s MaxHops 20 Root ID/ERPC : 0.bcea-fa14-f0a4, 0 RegRoot ID/IRPC : 0.bcea-fa14-f0a4, 0 RootPort ID : 0.0 BPDU-Protection : Disabled Bridge Config- Digest-Snooping : Disabled TC or TCN received : 19824 Time since last TC : 0 days 1h:3m:4s ----[Port1(GigabitEthernet1/0/1)][DISCARDING]---- Port protocol : Enabled Port role : Designated Port (Boundary) Port ID : 128.1 Port cost(Legacy) : Config=auto, Active=20 Desg.bridge/port : 0.bcea-fa14-f0a4, 128.1 Port edged : Config=disabled, Active=disabled Point-to-Point : Config=auto, Active=true Transmit limit : 10 packets/hello-time TC-Restriction : Disabled Role-Restriction : Disabled Protection type : ROOT

## Group: SRG-NET-000362-L2S-000022

**Group ID:** `V-66065`

### Rule: The HP FlexFabric Switch must have BPDU Guard enabled on all user-facing access ports.

**Rule ID:** `SV-80555r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a rogue switch is introduced into the topology and transmits a Bridge Protocol Data Unit (BPDU) with a lower bridge priority than the existing root bridge, it will become the new root bridge and cause a topology change, rendering the network in a suboptimal state. The Spanning Tree Protocol (STP) PortFast BPDU guard enhancement allows network designers to enforce the STP domain borders and keep the active topology predictable. The devices behind the ports that have STP PortFast enabled are not able to influence the STP topology. At the reception of BPDUs, the BPDU guard operation disables the port that has PortFast configured. The BPDU guard transitions the port into errdisable state and sends a log message.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that BPDU Protection is enabled on all user-facing switch ports. If the HP FlexFabric Switch has not enabled BPDU protection, this is a finding. [HP] display stp -------[CIST Global Info][Mode MSTP]------- Bridge ID : 32768.7848-596a-6580 Bridge times : Hello 2s MaxAge 20s FwdDelay 15s MaxHops 20 Root ID/ERPC : 32768.7848-596a-6580, 0 RegRoot ID/IRPC : 32768.7848-596a-6580, 0 RootPort ID : 0.0 BPDU-Protection : Enabled Bridge Config- Digest-Snooping : Disabled TC or TCN received : 0 Time since last TC : 3 days interface GigabitEthernet1/0/1 stp edged-port

## Group: SRG-NET-000362-L2S-000023

**Group ID:** `V-66067`

### Rule: The HP FlexFabric Switch must have STP Loop Protection enabled all non-designated STP switch ports.

**Rule ID:** `SV-80557r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Spanning Tree Protocol (STP) loop Protection feature provides additional protection against STP loops. An STP loop is created when an STP blocking port in a redundant topology erroneously transitions to the forwarding state. In its operation, STP relies on continuous reception and transmission of BPDUs based on the port role. The designated port transmits BPDUs, and the non-designated port receives BPDUs. When one of the ports in a physically redundant topology no longer receives BPDUs, the STP conceives that the topology is loop free. Eventually, the blocking port from the alternate or backup port becomes a designated port and moves to a forwarding state. This situation creates a loop. The loop Protection feature makes additional checks. If BPDUs are not received on a non-designated port and loop guard is enabled, that port is moved into the STP loop-inconsistent blocking state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that STP Loop Protection is enabled. If STP Loop Protection is not configured globally or at a minimum on non-designated STP ports, this is a finding. [HPinterface Ten-GigabitEthernet1/0/8] port link-mode bridge stp loop-protection

## Group: SRG-NET-000362-L2S-000024

**Group ID:** `V-66069`

### Rule: The HP FlexFabric Switch must have unknown storm-constrain enabled.

**Rule ID:** `SV-80559r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access layer switches use the Content Addressable Memory (CAM) table to direct traffic to specific ports based on the VLAN number and the destination MAC address of the frame. When a router has an ARP entry for a destination host and forwards it to the access layer switch and there is no entry corresponding to the frame's destination MAC address in the incoming VLAN, the frame will be sent to all forwarding ports within the respective VLAN, which causes flooding. Large amounts of flooded traffic can saturate low-bandwidth links, causing network performance issues or complete connectivity outage to the connected devices. Unknown unicast flooding has been a nagging problem in networks that have asymmetric routing and default timers. To mitigate the risk of a connectivity outage, the storm-constrain feature must be implemented on all access layer switches. The storm-constrain feature will block unknown unicast traffic flooding and only permit egress traffic with MAC addresses that are known to exit on the port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that unknown storm-constrain is enabled on all access switch ports. If any access switch ports do not have storm-constrain enabled, this is a finding. [HP] display storm-constrain Abbreviation: BC - broadcast; MC - multicast; UC - unicast FW - forwarding Flow Statistic Interval: 10 (in seconds) Port Type Lower Upper Unit CtrlMode Status Trap Log SwitchNum -------------------------------------------------------------------------------- XGE1/0/10 UC 1 1 pps shutdown FW on on 0

## Group: SRG-NET-000362-L2S-000025

**Group ID:** `V-66071`

### Rule: The HP FlexFabric Switch must have DHCP snooping for all user VLANs to validate DHCP messages from untrusted sources as well as rate-limit DHCP traffic.

**Rule ID:** `SV-80561r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In an enterprise network, devices under administrative control are trusted sources. These devices include the switches, routers, and servers in the network. Host ports and unknown Dynamic Host Configuration Protocol (DHCP) servers are considered untrusted sources. An unknown DHCP server on the network on an untrusted port is called a spurious DHCP server-- any device (PC, Wireless Access Point) that is loaded with DHCP server enabled. The DHCP snooping feature determines whether traffic sources are trusted or untrusted. The potential exists for a spurious DHCP server to respond to DHCPDISCOVER messages before the real server has time to respond. DHCP snooping allows switches on the network to trust the port a DHCP server is connected to and not trust the other ports. The DHCP snooping feature validates DHCP messages received from untrusted sources and filters out invalid messages as well as rate-limits DHCP traffic from trusted and untrusted sources. DHCP snooping feature builds and maintains a binding database, which contains information about untrusted hosts with leased IP addresses, and it utilizes the database to validate subsequent requests from untrusted hosts. Other security features, such as IP Source Guard and Dynamic ARP Inspection (DAI), also use information stored in the DHCP snooping binding database. Hence, it is imperative that the DHCP snooping feature is enabled on all VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration and verify that DHCP snooping is enabled on a per-VLAN basis. If the HP FlexFabric Switch does not have DHCP snooping enabled for all user VLANs to validate DHCP messages from untrusted sources as well as rate-limit DHCP traffic, this is a finding. Note: Enabling DHCP snooping on a range of VLANs is permissible. Sample output: [HP]dhcp snooping enable [HP-GigabitEthernet1/0/1]dhcp snooping rate-limit

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-66073`

### Rule: The HP FlexFabric Switch must have IP Source Guard enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-80563r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard provides source IP address filtering on a Layer 2 port to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted Layer 2 access ports. Initially, all IP traffic on the protected port is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that IP Source Guard is enabled on all untrusted access switch ports. If the HP FlexFabric Switch does not have IP Source Guard enabled on all user-facing or untrusted access switch ports, this is a finding. [HP]dis ip source binding static Total entries found: 0 IP Address MAC Address Interface VLAN Type

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-66075`

### Rule: The HP FlexFabric Switch must have Dynamic ARP Inspection (DAI) enabled on all user VLANs.

**Rule ID:** `SV-80565r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts Address Resolution Protocol (ARP) requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that Dynamic ARP Inspection (DAI) feature is enabled on all user VLANs. If DAI is not enabled on all user VLANs, this is a finding. [HP]display arp detection ARP detection is enabled in the following VLANs: 2 [HP]display arp detection statistics interface Ten-GigabitEthernet 1/0/11 State: U-Untrusted T-Trusted ARP packets dropped by ARP inspect checking: Interface(State) IP Src-MAC Dst-MAC Inspect XGE1/0/11(T) 0 0 0 0 [HP]

## Group: SRG-NET-000512-L2S-000003

**Group ID:** `V-66077`

### Rule: The HP FlexFabric Switch must implement Rapid STP where VLANs span multiple switches with redundant links.

**Rule ID:** `SV-80567r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) is implemented on bridges and switches to prevent layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Rapid STP should be deployed by implementing either Rapid or Multiple Spanning-Tree Protocol (MSTP) -- the latter scales much better when there are many VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In cases where VLANs do not span multiple switches, it is a best practice to not implement STP. Avoiding the use of STP will provide the most deterministic and highly available network topology. If STP is required, then review the HP FlexFabric Switch configuration to verify that Rapid STP has been implemented. If Rapid STP has not been implemented where STP is required, this is a finding. [HP]display stp vlan X

## Group: SRG-NET-000512-L2S-000004

**Group ID:** `V-66079`

### Rule: The HP FlexFabric Switch must enable Device Link Detection Protocol (DLDP) to protect against one-way connections.

**Rule ID:** `SV-80569r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In topologies where fiber optic interconnections are used, physical misconnections can occur that allow a link to appear to be up when there is a mismatched set of transmit/receive pairs. When such a physical misconfiguration occurs, protocols such as STP can cause network instability. Device Link Detection Protocol (DLDP) is a layer 2 protocol that can detect these physical misconfigurations by verifying that traffic is flowing bidirectionally between neighbors. Ports with DLDP enabled periodically transmit packets to neighbor devices. If the packets are not echoed back within a specific time frame, the link is flagged as unidirectional and the interface is shut down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If any of the switch ports have fiber optic interconnections with neighbors, review the HP FlexFabric Switch configuration to verify that DLDP is enabled globally or on a per interface basis. If the HP FlexFabric Switch has fiber optic interconnections with neighbors and DLDP is not enabled, this is a finding. <HP> display dldp DLDP global status : disable DLDP interval : 5s DLDP work-mode : enhance DLDP authentication-mode : none DLDP unidirectional-shutdown : auto DLDP delaydown-timer : 1s The number of enabled ports is 2. [HP-Interface Ethernet1/1] DLDP port state : advertisement DLDP link state : up The neighbor number of the port is 0. [HP-Interface Ethernet1/2] DLDP port state : advertisement DLDP link state : up The neighbor number of the port is 0.

## Group: SRG-NET-000512-L2S-000005

**Group ID:** `V-66081`

### Rule: The HP FlexFabric Switch must have all trunk links enabled statically.

**Rule ID:** `SV-80571r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When trunk negotiation is enabled via Dynamic Trunk Protocol (DTP), considerable time can be spent negotiating trunk settings (802.1q or ISL) when a node or interface is restored. While this negotiation is happening, traffic is dropped because the link is up from a layer 2 perspective. Packet loss can be eliminated by setting the interface statically to trunk mode, thereby avoiding dynamic trunk protocol negotiation and significantly reducing any outage when restoring a failed link or switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration to verify that trunk negotiation is disabled by statically configuring all trunk links. Configuring a command to manually disable negotiation may also be required for some switch platforms. If trunk negotiation is enabled on any interface, this is a finding. Sample output: interface GigabitEthernet1/0/1 port link-type trunk port trunk permit vlan X

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-66085`

### Rule: The HP FlexFabric Switch must have all disabled switch ports assigned an unused VLAN.

**Rule ID:** `SV-80575r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a disabled port that is assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result gains access to that VLAN as a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configurations and examine all access switch ports. Each access switch port not in use should have membership to an inactive VLAN that is not used for any purpose and is not allowed on any trunk links. If there are any access switch ports not in use and not in an inactive VLAN, this is a finding. <HP>display vlan X VLAN ID: X VLAN type: Static Route interface: Configured: Description: VLAN 000X Name: VLAN 000X Tagged ports: None Untagged ports: GigabitEthernet1/0/1 GigabitEthernet1/0/2 GigabitEthernet1/0/3 GigabitEthernet1/0/4

## Group: SRG-NET-000512-L2S-000008

**Group ID:** `V-66087`

### Rule: The HP FlexFabric Switch must not have the default VLAN assigned to any host-facing switch ports.

**Rule ID:** `SV-80577r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a VLAN-based network, switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with other networking devices using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. As a consequence, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configurations and verify that no access switch ports have been assigned membership to the default VLAN (i.e., VLAN 1). A good method of ensuring there is not membership to the default VLAN is to have it disabled (i.e., shutdown) on the switch. If there are access switch ports assigned to the default VLAN, this is a finding. <HP>display vlan 1 VLAN ID: 1 VLAN type: Static Route interface: Configured: Description: VLAN 0001 Name: VLAN 0001 Tagged ports: None Untagged ports: GigabitEthernet1/0/1 GigabitEthernet1/0/2 GigabitEthernet1/0/3 GigabitEthernet1/0/4 [HP-GigabitEthernet1/0/12]shutdown

## Group: SRG-NET-000512-L2S-000009

**Group ID:** `V-66089`

### Rule: The HP FlexFabric Switch must have the default VLAN pruned from all trunk ports that do not require it.

**Rule ID:** `SV-80579r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default VLAN (i.e., VLAN 1) is a special VLAN used for control plane traffic such as Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP). VLAN 1 is enabled on all trunks and ports by default. With larger campus networks, care needs to be taken about the diameter of the STP domain for the default VLAN. Instability in one part of the network could affect the default VLAN, thereby influencing control-plane stability and therefore STP stability for all other VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration and verify that the default VLAN is pruned from trunk links that do not require it. If the default VLAN is not pruned from trunk links that should not be transporting frames for the VLAN, this is a finding. <HP>display vlan 1 VLAN ID: 1 VLAN type: Static Route interface: Configured Description: VLAN 0001 Name: VLAN 0001 Tagged ports: None Untagged ports: GigabitEthernet1/0/1 GigabitEthernet1/0/2 GigabitEthernet1/0/3 GigabitEthernet1/0/4 GigabitEthernet1/0/5 GigabitEthernet1/0/6 GigabitEthernet1/0/7 GigabitEthernet1/0/8

## Group: SRG-NET-000512-L2S-000010

**Group ID:** `V-66091`

### Rule: The HP FlexFabric Switch must not use the default VLAN for management traffic.

**Rule ID:** `SV-80581r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with directly connected switches using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. As a consequence, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration and verify that the default VLAN is not used to access the switch for management. If the default VLAN is being used to access the HP FlexFabric Switch, this is a finding. <HP>display vlan 1 VLAN ID: 1 VLAN type: Static Route interface: Configured Description: VLAN 0001 Name: VLAN 0001 Tagged ports: None Untagged ports: GigabitEthernet1/0/1 GigabitEthernet1/0/2 GigabitEthernet1/0/3 GigabitEthernet1/0/4 GigabitEthernet1/0/5 GigabitEthernet1/0/6 GigabitEthernet1/0/7 GigabitEthernet1/0/8

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-66093`

### Rule: The HP FlexFabric Switch must have all user-facing or untrusted ports configured as access switch ports.

**Rule ID:** `SV-80583r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configuration and ensure all user-facing or untrusted ports are configured as access port. If any of the user-facing switch ports are configured as a trunk, this is a finding [HP]display current-configuration interface gigabitEthernet 1/0/1 Brief information on interface(s) under bridge mode: Link: ADM - administratively down; Stby - standby Speed or Duplex: (a)/A - auto; H - half; F - full Type: A - access; T - trunk; H - hybrid Interface Link Speed Duplex Type PVID Description XGE1/0/1 UP 1G(a) F(a) A 100 XGE1/0/2 UP 1G(a) F(a) A 100 XGE1/0/3 UP 1G(a) F(a) A 100 XGE1/0/4 UP 1G(a) F(a) A 100

## Group: SRG-NET-000512-L2S-000012

**Group ID:** `V-66095`

### Rule: The HP FlexFabric Switch must have the native VLAN assigned to a VLAN ID other than the default VLAN ID for all 802.1q trunk links.

**Rule ID:** `SV-80585r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VLAN hopping can be initiated by an attacker who has access to a switch port belonging to the same VLAN as the native VLAN of the trunk link connecting to another switch that the victim is connected to. If the attacker knows the victim’s MAC address, it can forge a frame with two 802.1q tags and a layer 2 header with the destination address of the victim. Since the frame will ingress the switch from a port belonging to its native VLAN, the trunk port connecting to the victim’s switch will simply remove the outer tag because native VLAN traffic is to be untagged. The switch will forward the frame on to the trunk link unaware of the inner tag with a VLAN ID of which the victim’s switch port is a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the HP FlexFabric Switch configurations and examine all trunk links. Verify the native VLAN has been configured to a VLAN ID other than the default VLAN 1. Connect to switch via console or SSH. <HP> display current interface Bridge-Aggregation # interface Bridge-Aggregation1 description To-DistroEast(10G) port link-type trunk undo port trunk permit vlan 1 port trunk permit vlan 2100 to 2102 4017 port trunk pvid vlan 4017 link-aggregation mode dynamic If any of the trunk links are assigned to VLAN 1, this is a finding.

## Group: SRG-NET-000512-L2S-000013

**Group ID:** `V-66097`

### Rule: The HP FlexFabric Switch must not have any access switch ports assigned to the native VLAN.

**Rule ID:** `SV-80587r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim’s MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker’s VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim’s VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify all access switch ports are not part of the native VLAN (VLAN 1). If any access switch port is assigned to the native VLAN (VLAN 1), this is a finding. <HP>display interface GigabitEthernet brief Brief information on interface(s) under bridge mode: Link: ADM - administratively down; Stby - standby Speed or Duplex: (a)/A - auto; H - half; F - full Type: A - access; T - trunk; H - hybrid Interface Link Speed Duplex Type PVID Description GE1/0/1 UP 1G(a) F(a) A 1 GE1/0/2 UP 1G(a) F(a) A 100 GE1/0/3 UP 10M(a) F(a) A 100 XGE1/0/1 UP 10G(a) F(a) A 200 XGE1/0/2 UP 10G(a) F(a) A 200 If any access switch port are configured for the native vlan. This is a finding.

