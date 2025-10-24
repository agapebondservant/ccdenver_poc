# STIG Benchmark: Cisco ACI Layer 2 Switch Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-272029`

### Rule: The Cisco ACI layer 2 switch must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-272029r1114259_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication can assist in preventing a malicious user from connecting an unauthorized PC to a switch port to inject or receive data from the network without detection. In ACI, VLANs are used for traffic segmentation and identification, but their primary function is for identifying traffic, not directly configuring the leaf switch ports. </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the switch configuration has 802.1x authentication implemented for all access switch ports connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. MAC Authentication Bypass (MAB) must be configured on those switch ports connected to devices that do not support an 802.1x supplicant. 1. Navigate to Fabric >> Port Profiles. 2. Select the port profile that is used for host-facing access ports. 3. Within the port profile configuration, locate the 802.1x settings and verify 802.1x is and MAB are enabled. 4. Navigate to the Endpoints section. 5. Choose the leaf nodes that host the host-facing ports and verify the port profile is applied. If 802.1x authentication or MAB is not configured on all access switch ports connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000168-L2S-000019

**Group ID:** `V-272030`

### Rule: The Cisco ACI layer 2 switches should authenticate all VLAN Trunk Protocol (VTP) messages with a hash function using the most secured cryptographic algorithm available.

**Rule ID:** `SV-272030r1114331_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VTP provides central management of VLAN domains, thus reducing administration in a switched network. When configuring a new VLAN on a VTP server, the VLAN is distributed through all switches in the domain. This reduces the need to configure the same VLAN everywhere. VTP pruning preserves bandwidth by preventing VLAN traffic (unknown MAC, broadcast, multicast) from being sent down trunk links when not needed, that is, there are no access switch ports in neighboring switches belonging to such VLANs. An attack can force a digest change for the VTP domain enabling a rogue device to become the VTP server, which could allow unauthorized access to previously blocked VLANs or allow the addition of unauthorized switches into the domain. Authenticating VTP messages with a cryptographic hash function can reduce the risk of the VTP domains being compromised.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify if VTP authentication is configured. 1. Navigate to Fabric >> Fabric Policies >> Policies >> Pod >> VLAN. 2. Verify that a VTP password is configured. If a password is not configured, this is a finding.

## Group: SRG-NET-000343-L2S-000016

**Group ID:** `V-272032`

### Rule: The Cisco ACI layer 2 switch must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-272032r1114076_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed architectures (e.g., service-oriented architectures [SOA]), the decisions regarding the validation of authentication claims may be made by services separate from the services acting on those decisions. In such situations, it is necessary to provide authentication decisions (as opposed to the actual authenticators) to the services that need to act on those decisions. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs). Gateways and SOA applications are examples of where this requirement would apply. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the switch configuration has 802.1x authentication implemented for all access switch ports connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. MAC Authentication Bypass (MAB) must be configured on those switch ports connected to devices that do not support an 802.1x supplicant. Verify the 802.1X Port Authentication policy is configured correctly: 1. On the menu bar, click Fabric >> External Access Policies >> Policies >> Interface >> 802.1X Port Authentication. 2. Right-click "802.1X Port Authentication" and review each 802.1X Port Authentication Policy. - In the Host Mode field, verify "Single Host" is selected. - In the MAC Auth field, verify "EAP_FALLBACK_MAB" is selected. Verify 802.1X Node Authentication is associated with the 802.1X Port Authentication Policy to a Fabric Access Group: 1. On the menu bar, click Fabric >> External Access Policies >> Policies >> Switch >> 802.1X Node Authentication. 2. Right-click "802.1X Node Authentication" and review each 802.1X Node Authentication Policy. - In the Failed-auth EPG field, verify the tenant, application profile, and EPG to deploy to in the case of failed authentication is configured. - In the Failed-auth VLAN. verify the VLAN to deploy to in the case of failed authentication is selected. Verify the 802.1X Node Authentication Policy is applied to each Leaf Switch Policy Group: 1. Navigate to Fabric >> External Access Policies >> Switches >> Leaf Switches >> Policy Groups. 2. Right-click "Policy Groups" to inspect each Access Switch Policy Group. Verify the 802.1X Node Authentication Policy to a Leaf Interface Profile: 1. Navigate to Fabric >> External Access Policies >> Interfaces >> Leaf Interfaces >> Profiles. 2. Right-click "Profiles" and select Leaf Interface Profile. 3. Expand the Interface Selectors table to review the Access Port Selector(s). If 802.1x authentication or MAB is not configured on all access switch ports connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000362-L2S-000024

**Group ID:** `V-272033`

### Rule: The Cisco ACI layer 2 switch must have Unknown Unicast Flood Blocking (UUFB) set to "Hardware Proxy".

**Rule ID:** `SV-272033r1114238_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access layer switches use the Content Addressable Memory (CAM) table to direct traffic to specific ports based on the VLAN number and the destination MAC address of the frame. When a router has an Address Resolution Protocol (ARP) entry for a destination host and forwards it to the access layer switch and there is no entry corresponding to the frame's destination MAC address in the incoming VLAN, the frame will be sent to all forwarding ports within the respective VLAN, which causes flooding. Large amounts of flooded traffic can saturate low bandwidth links, causing network performance issues or complete connectivity outage to the connected devices. Unknown unicast flooding has been a problem in networks that have asymmetric routing and default timers. To mitigate the risk of a connectivity outage, the Unknown Unicast Flood Blocking (UUFB) feature must be implemented on all access layer switches. The UUFB feature will block unknown unicast traffic flooding and only permit egress traffic with MAC addresses that are known to exit on the port. For Cisco ACI, L2 Unknown Unicast decides whether the bridge domain should flood packets that are destined to an unknown MAC address (Flood) or should send it to a spine node for COOP database lookup (Hardware Proxy).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify each Bridge Domain used is configured to block unknown unicast traffic. 1. Navigate to Tenant>> Networking >> Bridge Domains >> Policy >> General and inspect each Tenant's Bridge Domain configuration. 2. Expand Networking and right-click each Bridge Domain. - Verify the L2 Unknown Unicast box is set to "Hardware Proxy". If any user-facing or untrusted access switch ports do not have UUFB set to "Hardware Proxy", this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-272037`

### Rule: The Cisco ACI layer 2 switch must enable port security.

**Rule ID:** `SV-272037r1113943_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The port security feature protects the ACI fabric from being flooded with unknown MAC addresses by limiting the number of MAC addresses learned per port. The port security feature support is available for physical ports, port channels, and virtual port channels.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the port security policies for compliance: 1. In the GUI menu bar, click Fabric >> Access Policies. 2. In the Navigation pane, expand Policies >> Interface >> Port Security. 3. Select each port security policy used and verify the following: - Port Security Timeout is set to "600 seconds". - Violation Action is set to "Protect mode". - Maximum Endpoints is set to "1". Verify port security is active on all appropriate host-facing interfaces: 1. In the Navigation pane, click Fabric >> Inventory >> Topology. 2. Verify that each leaf has been configured to use a correctly configured port security policy. If port security is not configured and enabled, this is a finding.

## Group: SRG-NET-000512-L2S-000001

**Group ID:** `V-272038`

### Rule: The Cisco ACI layer 2 switch must have Storm Control configured on all host-facing switch ports.

**Rule ID:** `SV-272038r1114350_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a LAN, creating excessive traffic and degrading network performance. Traffic storm control prevents network disruption by suppressing ingress traffic when the number of packets reaches configured threshold levels. Traffic storm control monitors ingress traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that storm control is enabled on all host-facing interfaces as shown in the example below. 1. Navigate to Fabric >> Access Policies >> Policies >> Interface >> Storm Control. 2. Review each Storm Control policy. 3. Navigate to the Application Profile containing the EPGs to be protected. 4. Select each EPG and go to the "Policies" tab to verify that a storm control policy that is configured for to protect broadcast, at a minimum, has been applied. If storm control is not enabled for host-facing interfaces for broadcast traffic at a, minimum, for broadcast traffic, this is a finding.

## Group: SRG-NET-000512-L2S-000002

**Group ID:** `V-272039`

### Rule: The Cisco ACI layer 2 switch must have Internet Group Management Protocol (IGMP) or Multicast Listener Discovery (MLD) snooping configured on all VLANs.

**Rule ID:** `SV-272039r1113945_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP and MLD snooping provides a way to constrain multicast traffic at layer 2. By monitoring the IGMP or MLD membership reports sent by hosts within a VLAN, the snooping application can set up Layer 2 multicast forwarding tables to deliver specific multicast traffic only to interfaces connected to hosts interested in receiving the traffic, thereby significantly reducing the volume of multicast traffic that would otherwise flood the VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the switch configuration enables IGMP or MLD snooping for IPv4 and IPv6 multicast traffic. Below is an example of the steps to verify that IGMP snooping is enabled for each VLAN: apic1(config-tenant-template-ip-igmp-snooping)# show run all If the switch is not configured to implement IGMP or MLD snooping for each VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-272042`

### Rule: The Cisco ACI layer 2 switch must have all disabled switch ports assigned to an unused VLAN.

**Rule ID:** `SV-272042r1114329_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a disabled port that is assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result gains access to that VLAN as a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the switchport is configured for 802.1X, this is not applicable. 1. In the ACI GUI, navigate to Fabric >> Inventory >> Pod number. 2. Click the "Topology" tab to view the fabric topology. 3. Double-click the leaf switch or spine switch to view port-level connectivity. 4. Navigate to the VLAN section. 5. Review the switch configuration for the VLAN designated as the inactive VLAN. No applications or endpoints assigned. Review the disabled ports. 1. Navigate to Fabric >> Inventory >> Pod number, then navigate to the desired switch. 2. Navigate to the port profile and verify it is assigned to the designated unused VLAN. 3. Each access switch identified as not in use should have membership to a designated unused VLAN. If there are any access switch ports not in use and not in an inactive VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-272043`

### Rule: The Cisco ACI layer 2 switch must have all user-facing or untrusted ports configured as access switch ports.

**Rule ID:** `SV-272043r1113949_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Double encapsulation can be initiated by an attacker who has access to a switch port belonging to the native VLAN of the trunk port. Knowing the victim's MAC address, and with the victim attached to a different switch belonging to the same trunk group, thereby requiring the trunk link and frame tagging, the malicious user can begin the attack by sending frames with two sets of tags. The outer tag that will have the attacker's VLAN ID (probably the well-known and omnipresent default VLAN) is stripped off by the switch, and the inner tag that will have the victim's VLAN ID is used by the switch as the next hop and sent out the trunk port.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and examine all user-facing or untrusted switchports. Display information for all Ethernet interfaces, including access and trunk interfaces. Example: [apic1] configure terminal [apic1(config)#] show interface switchport If any of the user-facing switch ports are configured as a trunk, this is a finding.

## Group: SRG-NET-000512-L2S-000012

**Group ID:** `V-272044`

### Rule: The Cisco ACI layer 2 switch, for all 802.1q trunk links, must have the native VLAN assigned to an ID other than the default VLAN.

**Rule ID:** `SV-272044r1113950_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VLAN hopping can be initiated by an attacker who has access to a switch port belonging to the same VLAN as the native VLAN of the trunk link connecting to another switch that the victim is connected to. If the attacker knows the victim's MAC address, it can forge a frame with two 802.1q tags and a layer 2 header with the destination address of the victim. Since the frame will ingress the switch from a port belonging to its native VLAN, the trunk port connecting to the victim's switch will simply remove the outer tag because native VLAN traffic is to be untagged. The switch will forward the frame on to the trunk link unaware of the inner tag with a VLAN ID of which the victim's switch port is a member.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and examine all trunk links. Verify the native VLAN has been configured to a VLAN ID other than the ID of the default VLAN (i.e., VLAN 1) as shown in the example below: [apic1(config)#] show vlan dot1q tag native or [apic1(config)#] show interface If the native VLAN has the same VLAN ID as the default VLAN, this is a finding.

## Group: SRG-NET-000705-L2S-000110

**Group ID:** `V-272045`

### Rule: The Cisco ACI layer 2 switch must employ a first-hop-security (FHS) policy to protect against denial-of-service (DoS) attacks.

**Rule ID:** `SV-272045r1114353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS events may occur due to a variety of internal and external causes, such as an attack by an adversary or a lack of planning to support organizational needs with respect to capacity and bandwidth. FHS features enable a better IPv4 and IPv6 link security and management over the layer 2 links. In a service provider environment, these features closely control address assignment and derived operations. Setting include the following DOD required configurations: - Unknown Unicast Flood Blocking (UUFB) enabled. - DHCP snooping enabled for all user VLANs to validate DHCP messages from untrusted sources. - IP Source Guard enabled on all user-facing or untrusted access switch ports. - Dynamic Address Resolution Protocol (ARP) Inspection enabled on all user VLANs. Satisfies: SRG-NET-000362-L2S-000025, SRG-NET-000362-L2S-000026, SRG-NET-000362-L2S-000027</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the FHS policy is configured. Note: This is an example. The exact configuration may vary with the site's architecture. leaf4# show fhs bt all The following settings must be enabled at a minimum: - ip-inspection-admin-status enabled-both - source-guard-admin-status enabled-both - router-advertisement-guard-admin-status enabled - router-advertisement-guard - managed-config-check - managed-config-flag - other-config-check - other-config-flag - maximum-router-preference low - minimum-hop-limit 10 - maximum-hop-limit 100 Trust-control tcpolicy settings: - arp - dhcpv4-server - dhcpv6-server - ipv6-router - router-advertisement - neighbor-discovery If an FHS policy is not configured with all required settings, this is a finding.

## Group: SRG-NET-000715-L2S-000120

**Group ID:** `V-272046`

### Rule: The Cisco ACI layer 2 switch must implement physically or logically separate subnetworks to isolate organization-defined critical system components and functions.

**Rule ID:** `SV-272046r1114355_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command and control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions. Cisco ACI provides numerous features to cover different use cases to restrict traffic between EPGs to help organizations in the segmentation and micro-segmentation journey. This includes features such as: - Inter-VRF and Intra-VRF Contracts. - Policy-based Redirection and layer 4 to layer 7 Services Insertion. - Intra-EPG Isolation and Intra-EPG Contracts. - vzAny Contracts. - Endpoint Security Groups (ESG). Organizations must make use of one or more of these Cisco ACI contracts and segmentation capabilities to provide segmentation within the data center for east-west traffic flows, as well as for north-south traffic flows, combined in this former case with other security devices or solutions to implement a defense-in-depth strategy.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify one or more Cisco ACI contracts and/or segmentation capabilities to provide segmentation within the data center for east-west traffic and north-south traffic flows, combined in this former case with other security devices or solutions to implement a defense-in-depth strategy. The following is an example of deploying an EPG through an interface policy group to multiple interfaces to provide separation and isolation of traffic. Associate the target EPG with the interface policy group. The sample command sequence specifies an interface policy group pg3 associated with VLAN domain, domain1, and with VLAN 1261. The application EPG, epg47 is deployed to all interfaces associated with this policy group. Check the target ports to verify deployment of the policies of the interface policy group associated with application EPG. The output of the sample "show command" sequence indicates that policy group pg3 is deployed on Ethernet port 1/20 on leaf switch 1017. apic1# show run leaf 1017 int eth 1/20 # Command: show running-config leaf 1017 int eth 1/20 # Time: Mon Jun 27 22:12:10 2016 leaf 1017 interface ethernet 1/20 policy-group pg3 If physical or logical separation of subnetworks to isolate organization-defined critical system components and functions has not been implemented, this is a finding.

## Group: SRG-NET-000760-L2S-000160

**Group ID:** `V-272047`

### Rule: The Cisco ACI layer 2 switch must establish organization-defined alternate communication paths for system operations organizational command and control.

**Rule ID:** `SV-272047r1113953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An incident, whether adversarial- or nonadversarial-based, can disrupt established communication paths used for system operations and organizational command and control. Alternate communication paths reduce the risk of all communication paths being affected by the same incident. To compound the problem, the inability of organizational officials to obtain timely information about disruptions or to provide timely direction to operational elements after a communication path incident, can impact the ability of the organization to respond to such incidents in a timely manner. Establishing alternate communication paths for command and control purposes, including designating alternative decision makers if primary decision makers are unavailable and establishing the extent and limitations of their actions, can greatly facilitate the organization's ability to continue to operate and take appropriate actions during an incident. To establish alternate communication paths for system operations and organizational command and control within a Cisco ACI cluster using the CLI, configure a multi-pod ACI architecture with separate APIC clusters, ensuring redundancy across pods by using external IP-routed networks (Inter-Pod Network) to maintain connectivity even if one pod experiences a failure. This effectively creates diverse communication pathways for management and control functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the connection type is remotely attached through a layer 3 network, this is not applicable. Verify the cluster status. apic1# cluster_health If the status of the clustered nodes is not "OK", this is a finding.

