# STIG Benchmark: RUCKUS ICX Layer 2 Switch Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000131-L2S-000014

**Group ID:** `V-273672`

### Rule: The RUCKUS ICX switch must be configured to disable nonessential capabilities.

**Rule ID:** `SV-273672r1110975_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised switch introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each switch is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to determine if services or functions not required for operation, or not related to switch functionality, are enabled. 1. Check that web authentication is enabled. Router#show webauth The result returned will be blank. 2. Check that web services are enabled. Router#show web HTTP server status: Disabled HTTPS server status: Disabled No web connection. 3. Check if the telnet service is enabled. Router#show telnet Telnet server status: Disabled Telnet connections: 4. Check if the tftp service is enabled. Router#show running-config | include tftp no tftp client enable tftp disable If unnecessary services and functions are enabled on the switch, this is a finding.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-273673`

### Rule: The RUCKUS ICX switch must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-273673r1110976_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration for RADIUS server configuration, FlexAuth configuration, and applicable port configuration (optional). aaa authentication dot1x default radius radius-server host 192.168.1.24 auth-port 1812 acct-port 1813 default key 2 $UGlkRGktdG5v dot1x mac-auth no-login authentication auth-order mac-auth dot1x auth-default-vlan 100 restricted-vlan 666 re-authentication reauth-timeout 60 auth-fail-action restricted-vlan dot1x enable dot1x enable ethernet 1/1/14 to 1/1/15 dot1x port-control auto ethernet 1/1/14 to 1/1/15 mac-authentication enable mac-authentication enable ethernet 1/1/13 mac-authentication password-format xxxx.xxxx.xxxx mac-authentication dot1x-override mac-authentication dot1x-disable interface ethernet 1/1/14 port-name dot1x-test use-radius-server 192.168.1.24 no inline power ! Note: Port configuration is only necessary when specifying which RADIUS server is to be used. If user ports are not configured to control LAN access via 802.1X, this is a finding.

## Group: SRG-NET-000168-L2S-000019

**Group ID:** `V-273674`

### Rule: The RUCKUS ICX switch must disable the Multiple VLAN Registration Protocol (MVRP).

**Rule ID:** `SV-273674r1110977_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>MVRP provides central management of VLAN domains, thus reducing administration in a switched network. When configuring a new VLAN in MVRP, the VLAN is distributed through all switches in the domain. This reduces the need to configure the same VLAN everywhere. MVRP pruning preserves bandwidth by preventing VLAN traffic (unknown MAC, broadcast, multicast) from being sent down trunk links when not needed, that is, there are no access switch ports in neighboring switches belonging to such VLANs. An attack could allow unauthorized access to previously blocked VLANs or allow the addition of unauthorized switches into the domain. There is no authentication method available for MVRP to reduce this risk.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify if MVRP is enabled. Router(config)#show mvrp No mvrp configuration found Router(config) If MVRP protocol response from show mvrp command indicates Enabled, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-273675`

### Rule: The RUCKUS ICX switch must manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-273675r1111323_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition that occurs when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify QoS has been enabled to ensure that sufficient capacity is available for mission-critical traffic. Router# show running-config | include burst ip icmp attack-rate burst-normal 5000 burst-max 10000 lockup 300 ip tcp burst-normal 30 burst-max 100 lockup 300 If the switch is not configured to manage excess bandwidth to limit the effects of packet flooding types of DoS attacks, this is a finding.

## Group: SRG-NET-000343-L2S-000016

**Group ID:** `V-273676`

### Rule: The RUCKUS ICX switch must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-273676r1111002_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers [outside a datacenter], VoIP phones, and VTC codecs). Gateways and SOA applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the switch configuration has 802.1x authentication implemented for all access switch ports connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. MAC Authentication must be configured on those switch ports connected to devices that do not provide an 802.1x supplicant. show running-config authentication auth-default-vlan 100 re-authentication reauth-period 2000 dot1x enable dot1x enable ethernet 1/1/1 to 1/1/3 dot1x max-req 6 dot1x timeout tx-period 60 dot1x timeout quiet-period 30 mac-authentication enable mac-authentication enable ethernet 1/1/18 to 1/1/19 If 802.1x authentication or MAC Authentication is not configured on all access switch ports connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000362-L2S-000021

**Group ID:** `V-273677`

### Rule: The RUCKUS ICX switch must have Root Protect enabled on all switch ports connecting to access layer switches and hosts.

**Rule ID:** `SV-273677r1111058_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) does not provide any means for the network administrator to securely enforce the topology of the switched network. Any switch can be the root bridge in a network. However, a more optimal forwarding topology places the root bridge at a specific predetermined location. With the standard STP, any bridge in the network with a lower bridge ID takes the role of the root bridge. The administrator cannot enforce the position of the root bridge but can set the root bridge priority to 0 to secure the root bridge position. The root guard feature provides a way to enforce the root bridge placement in the network. If the bridge receives superior STP Bridge Protocol Data Units (BPDUs) on a root guard-enabled port, root guard moves this port to a root-inconsistent STP state and no traffic can be forwarded across this port while it is in this state. To enforce the position of the root bridge it is imperative that root guard is enabled on all ports where the root bridge should never appear.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review port configuration to verify that Root Protect is enabled on ports connecting to access layer switches and hosts. interface ethernet x/x/x spanning-tree root-protect If Root Protect is not configured on ports connecting to access layer switches and hosts, this is a finding.

## Group: SRG-NET-000362-L2S-000022

**Group ID:** `V-273678`

### Rule: The RUCKUS ICX switch must have Bridge Protocol Data Unit (BPDU) Guard enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-273678r1110981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An example is a firewall that blocks all traffic rather than allowing all traffic when a firewall component fails (e.g., fail closed and do not forward traffic). This prevents an attacker from forcing a failure of the system to obtain access. Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review switch port configuration on all untrusted access ports. ! interface ethernet x/x/x spanning-tree root-protect stp-bpdu-guard ! If untrusted access switch ports are not configured for BPDU Guard, this is a finding.

## Group: SRG-NET-000362-L2S-000023

**Group ID:** `V-273679`

### Rule: The RUCKUS ICX switch must have Spanning Tree Protocol (STP) Loop Detect enabled on all nondesignated STP switch ports

**Rule ID:** `SV-273679r1110982_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The STP loop Detect feature provides additional protection against STP loops. An STP loop is created when an STP blocking port in a redundant topology erroneously transitions to the forwarding state. In its operation, STP relies on continuous reception and transmission of BPDUs based on the port role. The designated port transmits BPDUs, and the nondesignated port receives BPDUs. When one of the ports in a physically redundant topology no longer receives BPDUs, the STP conceives that the topology is loop-free. Eventually, the blocking port from the alternate or backup port becomes a designated port and moves to a forwarding state. This situation creates a loop. The loop detect feature makes additional checks. If BPDUs are not received on a nondesignated port and loop detect is enabled, that port is moved into the STP loop-inconsistent blocking state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that STP Loop Detect is enabled. Verify: ICX7150-24P Switch#show run ! vlan 10 by port tagged ethernet 1/1/1 to 1/1/2 ethernet 1/1/5 ethernet 1/1/7 ethernet 1/1/9 ethernet 1/1/11 spanning-tree loop-detection ! If STP Loop Detect is not configured globally or on nondesignated STP ports, this is a finding.

## Group: SRG-NET-000362-L2S-000024

**Group ID:** `V-273680`

### Rule: The RUCKUS ICX switch must have Unknown Unicast Flood Blocking (UUFB) enabled.

**Rule ID:** `SV-273680r1110983_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access layer switches use the Content Addressable Memory (CAM) table to direct traffic to specific ports based on the VLAN number and the destination MAC address of the frame. When a router has an Address Resolution Protocol (ARP) entry for a destination host and forwards it to the access layer switch and there is no entry corresponding to the frame's destination MAC address in the incoming VLAN, the frame will be sent to all forwarding ports within the respective VLAN, which causes flooding. Large amounts of flooded traffic can saturate low-bandwidth links, causing network performance issues or complete connectivity outage to the connected devices. Unknown unicast flooding has been an ongoing problem in networks that have asymmetric routing and default timers. To mitigate the risk of a connectivity outage, the UUFB feature must be implemented on all access layer switches. The UUFB feature will block unknown unicast traffic flooding and only permit egress traffic with MAC addresses that are known to exit on the port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration to verify ports are configured to block unknown unicast traffic. ! interface ethernet 1/1/8 block unknown-unicast ! If any access switch ports do not have UUFB enabled, this is a finding.

## Group: SRG-NET-000362-L2S-000025

**Group ID:** `V-273681`

### Rule: The RUCKUS ICX switch must have DHCP snooping for all user VLANs to validate DHCP messages from untrusted sources.

**Rule ID:** `SV-273681r1111008_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In an enterprise network, devices under administrative control are trusted sources. These devices include the switches, routers, and servers in the network. Host ports and unknown DHCP servers are considered untrusted sources. An unknown DHCP server on the network on an untrusted port is called a spurious DHCP server, any device (PC, Wireless Access Point) loaded with DHCP server enabled. The DHCP snooping feature determines whether traffic sources are trusted or untrusted. The potential exists for a spurious DHCP server to respond to DHCPDISCOVER messages before the real server has time to respond. DHCP snooping allows switches on the network to trust the port a DHCP server is connected to and not trust the other ports. The DHCP snooping feature validates DHCP messages received from untrusted sources and filters out invalid messages as well as rate-limits DHCP traffic from trusted and untrusted sources. DHCP snooping feature builds and maintains a binding database, which contains information about untrusted hosts with leased IP addresses, and it uses the database to validate subsequent requests from untrusted hosts. Other security features, such as IP Source Guard and Dynamic Address Resolution Protocol (ARP) Inspection (DAI), also use information stored in the DHCP snooping binding database. Hence, it is imperative that the DHCP snooping feature is enabled on all VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review switch configuration for DHCP snooping on all user VLANs. ! ip dhcp snooping vlan 100 ! interface ethernet x/x/x port-name toward_dhcp_srvr dhcp snooping trust If DHCP Snooping is not configured on user VLANs to validate DHCP messages from untrusted sources, this is a finding.

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-273682`

### Rule: The RUCKUS ICX switch must have IP Source Guard enabled on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-273682r1111010_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard provides source IP address filtering on a layer 2 port to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted layer 2 access ports. Initially, all IP traffic on the protected port is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration for source-guard enabled on user-facing or untrusted ports. interface ethernet 1/1/47 port-name FlexAuth_port authentication source-guard-protection enable ! interface ethernet 1/1/48 source-guard enable ! If all user-facing or untrusted switch ports are not configured for IP Source Guard, this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-273683`

### Rule: The RUCKUS ICX switch must have Dynamic Address Resolution Protocol (ARP) Inspection (DAI) enabled on all user VLANs.

**Rule ID:** `SV-273683r1110986_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts ARP requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review list of VLANs with ARP inspection configured. ICX#show ip arp inspection IP ARP inspection enabled on 1 VLAN(s): VLAN(s): 16 If ARP Inspection is not enabled on all user VLANs, this is a finding.

## Group: SRG-NET-000512-L2S-000001

**Group ID:** `V-273684`

### Rule: The RUCKUS ICX switch must have Storm Control configured on all host-facing switch ports.

**Rule ID:** `SV-273684r1110987_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a LAN, creating excessive traffic and degrading network performance. Traffic storm control prevents network disruption by suppressing ingress traffic when the number of packets reaches configured threshold levels. Traffic storm control monitors ingress traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration for the desired storm control settings on host-facing ports. ! interface ethernet 1/1/5 broadcast limit 8787 multicast limit 777 unknown-unicast limit 888 ! If host facing ports are not configured for storm control protection, this is a finding.

## Group: SRG-NET-000512-L2S-000002

**Group ID:** `V-273685`

### Rule: The RUCKUS ICX switch must have IGMP or MLD Snooping configured on all VLANs.

**Rule ID:** `SV-273685r1110988_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP and MLD snooping provides a way to constrain multicast traffic at layer 2. By monitoring the IGMP or MLD membership reports sent by hosts within a VLAN, the snooping application can set up layer 2 multicast forwarding tables to deliver specific multicast traffic only to interfaces connected to hosts interested in receiving the traffic, thereby significantly reducing the volume of multicast traffic that would otherwise flood the VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration for IGMP and MLD snooping. ! ip multicast ipv6 multicast ! If IGMP or MLD snooping are not configured for all VLANs, this is a finding.

## Group: SRG-NET-000512-L2S-000003

**Group ID:** `V-273686`

### Rule: The RUCKUS ICX switch must implement Rapid Spanning Tree Protocol (STP) where VLANs span multiple switches with redundant links.

**Rule ID:** `SV-273686r1110989_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>STP is implemented on bridges and switches to prevent layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Rapid STP should be deployed by implementing either Rapid Per-VLAN-Spanning-Tree (Rapid-PVST) or Multiple Spanning-Tree Protocol (MSTP), the latter scales much better when there are many VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration for VLANs that are not set for 802.1w (Rapid Spanning Tree). vlan 10 name testing by port tagged ethernet 1/1/17 untagged ethernet 1/1/18 spanning-tree 802-1w ! If 802.1w is not configured on VLANs that span multiple switches with redundant links, this is a finding.

## Group: SRG-NET-000512-L2S-000004

**Group ID:** `V-273687`

### Rule: The RUCKUS ICX switch must enable Unidirectional Link Detection (UDLD) to protect against one-way connections.

**Rule ID:** `SV-273687r1110990_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In topologies where fiber optic interconnections are used, physical misconnections can occur that allow a link to appear to be up when there is a mismatched set of transmit/receive pairs. When such a physical misconfiguration occurs, protocols such as STP can cause network instability. UDLD is a layer 2 protocol that can detect these physical misconfigurations by verifying that traffic is flowing bidirectionally between neighbors. Ports with UDLD enabled periodically transmit packets to neighbor devices. If the packets are not echoed back within a specific time frame, the link is flagged as unidirectional and the interface is shut down.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review configuration for UDLD configuration ("link keep-alive"). Router# show link-keepalive Total link-keepalive enabled ports: 4 Keepalive Retries: 3 Keepalive Interval: 1 Sec. Port Physical Link Logical Link State Link-vlan 1/1/1 up up FORWARDING 3 1/1/2 up up FORWARDING 1/1/3 down down DISABLED 1/1/4 up down DISABLED If UDLD is not configured to protect against one-way connections, this is a finding.

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-273688`

### Rule: The RUCKUS ICX switch must have all disabled switch ports assigned to an unused VLAN.

**Rule ID:** `SV-273688r1111017_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a disabled port assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result gains access to that VLAN as a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and examine all access switch ports. Each access switch port not in use must have membership to an inactive VLAN that is not used for any purpose and is not allowed on any trunk links. 1. Show the VLAN. Router#show vlan 888 PORT-VLAN 888, Name [None], Priority level0, Off Untagged Ports: (U1/M1) 5 6 7 8 9 10 11 12 13 14 15 16 Untagged Ports: (U1/M1) 17 18 19 20 Tagged Ports: None Mac-Vlan Ports: None Monitoring: Disabled SSH@ICX7550-48ZP-Router# 2. Confirm unused interfaces are disabled. Router#show interface br ethernet 1/1/5 to 1/1/20 Port Link State Dupl Speed Trunk Tag Pvid Pri MAC Name 1/1/5 Disable None None None None No 888 0 28b3.7129.8e5e 1/1/6 Disable None None None None No 888 0 28b3.7129.8e5f 1/1/7 Disable None None None None No 888 0 28b3.7129.8e60 1/1/8 Disable None None None None No 888 0 28b3.7129.8e61 ... If unused ports are not disabled and assigned to an unused VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000008

**Group ID:** `V-273689`

### Rule: The RUCKUS ICX switch must not have the default VLAN assigned to any host-facing switch ports.

**Rule ID:** `SV-273689r1111059_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a VLAN-based network, switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with other networking devices using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. Therefore, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and verify that no access switch ports have been assigned membership to the default VLAN. Router#show vlans PORT-VLAN 5, Name DEFAULT-VLAN], Priority level0, in single spanning tree domain Untagged Ports: None Tagged Ports: (U1/M1) 1 2 5 7 9 11 Mac-Vlan Ports: None Monitoring: Disabled If there are access switch ports assigned to the default VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000009

**Group ID:** `V-273690`

### Rule: The RUCKUS ICX switch must have the default VLAN pruned from all trunk ports that do not require it.

**Rule ID:** `SV-273690r1110993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The default VLAN (i.e., VLAN 1) is a special VLAN used for control plane traffic such as Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP). VLAN 1 is enabled on all trunks and ports by default. With larger campus networks, care needs to be taken about the diameter of the STP domain for the default VLAN. Instability in one part of the network could affect the default VLAN, thereby influencing control-plane stability and therefore STP stability for all other VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that the default VLAN is pruned from trunk links that do not require it. device#show vlan 888 PORT-VLAN 888, Name DEFAULT-VLAN, Priority level0, On Untagged Ports: (U1/M1) 1 2 3 4 5 6 7 8 9 10 11 12 Untagged Ports: (U1/M1) 13 14 15 16 17 18 19 20 21 22 23 24 Untagged Ports: (U1/M1) 25 26 27 28 29 30 31 32 33 34 35 36 Untagged Ports: (U1/M1) 37 38 39 40 41 43 44 45 46 47 48 Untagged Ports: (U1/M2) 1 2 3 4 5 6 7 8 Tagged Ports: None Mac-Vlan Ports: None Monitoring: Disabled device# If the default VLAN is not pruned from trunk links that should not be transporting frames for the VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000010

**Group ID:** `V-273691`

### Rule: The RUCKUS ICX switch must not use the default VLAN for management traffic.

**Rule ID:** `SV-273691r1111060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Switches use the default VLAN (i.e., VLAN 1) for in-band management and to communicate with directly connected switches using Spanning-Tree Protocol (STP), Dynamic Trunking Protocol (DTP), VLAN Trunking Protocol (VTP), and Port Aggregation Protocol (PAgP)—all untagged traffic. Therefore, the default VLAN may unwisely span the entire network if not appropriately pruned. If its scope is large enough, the risk of compromise can increase significantly.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review switch configuration to confirm the management VLAN is designated and is not VLAN 1. ! vlan 235 name mgmt-vlan tagged ethernet 1/2/1 ! If the management VLAN is the same as the default VLAN or VLAN 1, this is a finding.

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-273692`

### Rule: The RUCKUS ICX switch must have all user-facing or untrusted ports configured as access switch ports.

**Rule ID:** `SV-273692r1110995_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and examine all user-facing or untrusted switch ports. device#show vlans Total PORT-VLAN entries: 2 Maximum PORT-VLAN entries: 1024 Legend: [Stk=Stack-Id, S=Slot] PORT-VLAN 222, Name Access, Priority level0, On Untagged Ports: (U1/M1) 1 2 3 4 5 6 7 8 9 10 11 12 Untagged Ports: (U1/M1) 13 14 15 17 18 19 20 21 22 23 24 25 Untagged Ports: (U1/M1) 26 27 28 29 30 31 32 33 34 35 36 37 Untagged Ports: (U1/M1) 38 39 40 41 43 44 45 46 47 48 Untagged Ports: (U1/M2) 1 2 3 4 5 6 7 8 Tagged Ports: (U1/M2) 1 Mac-Vlan Ports: None Monitoring: Disabled PORT-VLAN 333, Name trunk, Priority level0, Off Untagged Ports: None Tagged Ports: (U1/M2) 1 Mac-Vlan Ports: None Monitoring: Disabled device# If all user-facing or untrusted ports are not configured as access (i.e., untagged) ports, this is a finding.

## Group: SRG-NET-000512-L2S-000012

**Group ID:** `V-273693`

### Rule: The RUCKUS ICX layer 2 switch must have the native VLAN assigned to an ID other than the default VLAN for all 802.1q trunk links.

**Rule ID:** `SV-273693r1110996_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VLAN hopping can be initiated by an attacker who has access to a switch port belonging to the same VLAN as the native VLAN of the trunk link connecting to another switch that the victim is connected to. If the attacker knows the victim's MAC address, it can forge a frame with two 802.1q tags and a layer 2 header with the destination address of the victim. Since the frame will ingress the switch from a port belonging to its native VLAN, the trunk port connecting to the victim's switch will simply remove the outer tag because native VLAN traffic is to be untagged. The switch will forward the frame on to the trunk link unaware of the inner tag with a VLAN ID of which the victim's switch port is a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the ports associated with the default VLAN. device#show vlans Total PORT-VLAN entries: 2 Maximum PORT-VLAN entries: 1024 Legend: [Stk=Stack-Id, S=Slot] PORT-VLAN 4505, Name DEFAULT-VLAN, Priority level0, On Untagged Ports: (U1/M1) Untagged Ports: (U1/M1) Untagged Ports: (U1/M1) Untagged Ports: (U1/M1) Untagged Ports: (U1/M2) Tagged Ports: None Mac-Vlan Ports: None Monitoring: Disabled device# If any 802.1q trunk interfaces (with tagged VLANs) also have the default VLAN assigned as the native VLAN (i.e., untagged), this is a finding.

## Group: SRG-NET-000512-L2S-000013

**Group ID:** `V-273694`

### Rule: The RUCKUS ICX switch must not have any switch ports assigned to the native VLAN.

**Rule ID:** `SV-273694r1110997_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine switch port configuration to determine whether a native VLAN (i.e., untagged) is assigned. ! vlan 4000 name DEFAULT-VLAN by port no untagged ethernet 1/2/1 spanning-tree ! ! vlan 10 by port tagged ethernet 1/2/1 untagged ethernet 1/1/1 ! ! vlan 20 by port tagged ethernet 1/2/1 untagged ethernet 1/1/2 ! If any switch ports have a native VLAN (i.e., untagged) also assigned, this is a finding.

## Group: SRG-NET-000715-L2S-000120

**Group ID:** `V-273696`

### Rule: The RUCKUS ICX switch must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

**Rule ID:** `SV-273696r1110998_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command and control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions. Satisfies: SRG-NET-000715-L2S-000120, SRG-NET-000760-L2S-000160</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the RUCKUS ICX switch configuration. Router# Show Vlans PORT-VLAN 5, Name Organization_A, Priority level0, in single spanning tree domain Untagged Ports: None 2 Tagged Ports: (U1/M1) 4 6 8 10 12 14 Mac-Vlan Ports: None Monitoring: Disabled PORT-VLAN 10, Name Organization_B, Priority level0, in single spanning tree domain Untagged Ports: None 20 21 22 Tagged Ports: (U1/M1) 1 3 5 7 9 11 Mac-Vlan Ports: None Monitoring: Disabled PORT-VLAN 12, Name IP_Phone, Priority level0, in single spanning tree domain Untagged Ports: None Tagged Ports: (U1/M1) 30 31 32 33 34 35 Mac-Vlan Ports: None Monitoring: Disabled If the RUCKUS ICX switch is not configured to implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions, this is a finding.

