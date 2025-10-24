# STIG Benchmark: SEL-2740S L2S Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-92263`

### Rule: The SEL-2740S  must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-102363r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via identification of connecting hosts can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SEL-2740S flow rules to ensure they contain the proper match criteria (MAC, IP, Port, SRC, DST, etc.) for the connected hosts restricting all other access to the network. If the SEL-2740S is configured with flows with wildcard or unnecessary packet forwarding rules, this is a finding.

## Group: SRG-NET-000512-L2S-000028

**Group ID:** `V-92277`

### Rule: The SEL-2740S must be configured to mitigate the risk of ARP cache poisoning attacks.

**Rule ID:** `SV-102365r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SEL-2740S must deter ARP cache poisoning attacks and configure the specific ARP flows that are only necessary to the control system network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SEL-2740S ARP flow rules between hosts and ensure they are necessary for the additional flow rules that exist for communications between hosts. Note: Necessary flows are all ARPs between valid and authorized hosts that should be allowed to talk to each other and the physical path those circuits are allowed to talk. If the SEL-2740S is configured with wildcard packet forwarding flows that are not for Security Information and Event Manager (SIEM) or unnecessary rules, this is a finding.

## Group: SRG-NET-000512-L2S-000029

**Group ID:** `V-92279`

### Rule: The SEL-2740S must be configured to capture all packets without flow rule match criteria.

**Rule ID:** `SV-102367r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The OTSDN switch must be capable of capturing frames that are not engineered to be in the network and send them to a Security Information and Event Manager (SIEM) or midpoint sensor for analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S to ensure that the "no match criteria" rule is set to capture the packet for analysis as a possible injection or intrusion. If the SEL-2740S is not configured to with the "no match criteria" rules for the Security Information and Event Manager (SIEM), this is a finding.

## Group: SRG-NET-000512-L2S-000030

**Group ID:** `V-92281`

### Rule: The SEL-2740S must be configured with backup flows for all host and switch flows to ensure proper failover scheme is in place for the network.

**Rule ID:** `SV-102369r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SEL-2740S must be capable of multiple fast failover, backup and in cases isolation of the traffic from a detected threat in the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S flow rules to ensure each flow has a Fast Failover Group configured. If the switch is not configured to provide backup flows, this is a finding.

## Group: SRG-NET-000512-L2S-000031

**Group ID:** `V-92283`

### Rule: The SEL-2740S must be configured to forward only frames from allowed network-connected endpoint devices.

**Rule ID:** `SV-102371r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By only allowing frames to be forwarded from known end-points mitigates risks associated with broadcast, unknown unicast, and multicast traffic storms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure only allowed traffic is being forwarded through the device, check the flow rules for source and destination information on each connected device and port. If there are any flow rules that are not restrictive, this is a finding.

## Group: SRG-NET-000131-L2S-000014

**Group ID:** `V-92313`

### Rule: The SEL-2740S must be configured to permit the allowed and necessary ports, functions, protocols, and services.

**Rule ID:** `SV-102401r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised switch introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each switch is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review SEL-2740S flow rules to ensure they contain the proper match criteria (MAC, IP, Port, SRC, DST, etc.) for the connected hosts restricting all other access to the network. If the SEL-2740S is configured with flows with wildcard or unnecessary packet forwarding rules, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-92315`

### Rule: The SEL-2740S -must be configured to limit excess bandwidth and denial of service (DoS) attacks.

**Rule ID:** `SV-102403r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding DDoS attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch by using readily available tools such as Low Orbit Ion Cannon or by using botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S to ensure that the meter rules and priorities are in place to ensure mission-critical traffic will not be impacted by increased traffic or bandwidth issues. If the SEL-2740S is not configured with meters and priorities necessary for mission-critical packets, this is a finding.

## Group: SRG-NET-000331-L2S-000001

**Group ID:** `V-92317`

### Rule: The SEL-2740S must be configured to packet capture flows.

**Rule ID:** `SV-102405r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to select a user session to capture/record or view/hear, investigations into suspicious or harmful events would be hampered by the volume of information captured. The volume of information captured may also adversely impact the operation for the network. Session audits may include port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S flow rules to ensure they only include the specific copy rules for capturing ingress and egress flows only on the designated port(s). Note: A span port can be created to capture based on Flows, ports, or combination. If the SEL-2740S is configured with flows with wildcard or unnecessary packet forwarding rules, this is a finding.

## Group: SRG-NET-000332-L2S-000002

**Group ID:** `V-92319`

### Rule: The SEL-2740S must be configured to capture flows for real-time visualization tools.

**Rule ID:** `SV-102407r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to remotely view/hear all content related to a user session, investigations into suspicious user activity would be hampered. Real-time monitoring allows authorized personnel to take action before additional damage is done. The ability to observe user sessions as they are happening allows for interceding in ongoing events that after-the-fact review of captured content would not allow.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S flow rules to ensure they only include the specific copy rules for capturing ingress and egress flows only on the designated port(s). Note: A span port can be created to capture based on Flows, ports, or combination. If the SEL-2740S is configured with flows with wildcard or unnecessary packet forwarding rules, this is a finding.

## Group: SRG-NET-000362-L2S-000024

**Group ID:** `V-92321`

### Rule: The SEL-2740S must be configured to prevent packet flooding and bandwidth saturation.

**Rule ID:** `SV-102409r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access layer switches use the Content Addressable Memory (CAM) table to direct traffic to specific ports based on the VLAN number and the destination MAC address of the frame. When a router has an Address Resolution Protocol (ARP) entry for a destination host and forwards it to the access layer switch and there is no entry corresponding to the frame's destination MAC address in the incoming VLAN, the frame will be sent to all forwarding ports within the respective VLAN, which causes flooding. Large amounts of flooded traffic can saturate low-bandwidth links, causing network performance issues or complete connectivity outage to the connected devices. Unknown unicast flooding has been a nagging problem in networks that have asymmetric routing and default timers. To mitigate the risk of a connectivity outage, the Unknown Unicast Flood Blocking (UUFB) feature must be implemented on all access layer switches. The UUFB feature will block unknown unicast traffic flooding and only permit egress traffic with MAC addresses that are known to exit on the port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S flows to ensure the meter rules are in place to prevent packet flooding and bandwidth saturation. If the switch is not configured to prevent packet flooding, this is a finding.

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-92323`

### Rule: SEL-2740S flow rules must include the host IP addresses that are bound to designated SEL-2740S ports for ensuring trusted host access.

**Rule ID:** `SV-102411r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard provides source IP address filtering on a Layer 2 port to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted Layer 2 access ports. Initially, all IP traffic on the protected port is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S flow rules to ensure all include IP addresses assigned to given hosts and are bound to the SEL-2740S ports. If the SEL-2740S flow rules are not configured with hosts' IP addresses for packets ingressing or egressing the ports, this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-92325`

### Rule: The SEL-2740S must be configured with ARP flow rules that are statically created with valid IP-to-MAC address bindings.

**Rule ID:** `SV-102413r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts Address Resolution Protocol (ARP) requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SEL-2740S configuration to verify that Dynamic Address Resolution Protocol (ARP) flow rules have valid IP-to-MAC address bindings. If the SEL-2740S Dynamic Address Resolution Protocol (ARP) flow rules are not configured with the valid IP-to-MAC address bindings, this is a finding.

## Group: SRG-NET-000343-L2S-000016

**Group ID:** `V-94587`

### Rule: The SEL-2740S must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-104417r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This finding can be downgraded to a CAT III if there is no horizontal cabling from the switch to the general work area. Verify that all cabling is contained within the telecom room, wiring closet, or equipment room. If there is cabling from the switch to LAN outlets (i.e.RJ-45 wall plates) in the general work area, this is a CAT II finding. If all cabling is contained within the telecom room, wiring closet, or equipment room, this is a CAT III finding.

