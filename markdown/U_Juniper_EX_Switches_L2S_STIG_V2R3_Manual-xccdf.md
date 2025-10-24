# STIG Benchmark: Juniper EX Series Switches Layer 2 Switch Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000131-L2S-000014

**Group ID:** `V-253948`

### Rule: The Juniper EX switch must be configured to disable non-essential capabilities.

**Rule ID:** `SV-253948r843877_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised switch introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each switch is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify the switch does not have an unnecessary or non-secure services enabled. For example, the following directives should not be in the configuration (deleted) or, if present, must be disabled (inactive): Verify the following commands are not present: [edit system services] finger; ftp; rlogin; telnet; xnm-clear-text; tftp; rest { http; } web-management { http; https; } Note: If the services listed above are marked "inactive", they are not enabled. For example, although the FTP stanza is present in the following snippet, it is disabled (inactive): [edit system services] inactive: ftp; Because J-Web was not included in the FIPS certification, verify the web-management process is disabled. [edit system services] web-management disable; If any unnecessary services are enabled, this is a finding.

## Group: SRG-NET-000148-L2S-000015

**Group ID:** `V-253949`

### Rule: The Juniper EX switch must be configured to uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-253949r843880_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Controlling LAN access via 802.1x authentication can assist in preventing a malicious user from connecting an unauthorized PC to an access interface to inject or receive data from the network without detection. 802.1x includes Static MAC Bypass and MAC RADIUS for those devices that do not offer a supplicant.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the switch configuration has 802.1x authentication implemented for all access interfaces connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. Static MAC Bypass or MAC RADIUS must be configured on access interfaces connected to devices that do not support an 802.1x supplicant. Junos supports three supplicant types: 'single-secure' (authenticate and permit only a single device), 'multiple' (separately authenticate and permit multiple devices), and 'single' (authenticate the first supplicant and permit all others). Verify that the RADIUS server(s) are configured. RADIUS servers can be configured globally at [edit access radius-server] or defined for each group. [edit access] radius-server { <RADIUS IPv4 or IPv6 address> secret "PSK"; ## SECRET-DATA } profile dot1x_radius { authentication-order radius; radius { authentication-server <RADIUS IPv4 or IPv6 address>; } --or-- radius-server { <RADIUS IPv4 or IPv6 address> secret "PSK"; ## SECRET-DATA } } Verify 802.1x or MAC RADIUS is configured on all host-facing access interfaces when RADIUS is available as shown in the following example: [edit protocols dot1x] authenticator { authentication-profile-name dot1x_radius; interface { ge-0/0/0.0 { <<< Connected device with 802.1x supplicant supplicant single-secure; } ge-0/0/1.0 { <<< Connected device with 802.1x supplicant and interface support for MAC RADIUS supplicant multiple; mac-radius; } ge-0/0/2.0 { <<< Connected device without 802.1x supplicant mac-radius { restrict; } } } } Note: Junos simultaneously supports both 802.1x and MAC RADIUS on the same access interface. To prevent 802.1x and have the interface use only MAC RADIUS, configure the "restrict" qualifier. If RADIUS is unavailable or not configured: [edit protocols] dot1x { authenticator { static { <MAC address>/48 { vlan-assignment <vlan name>; interface <interface name>.<logical unit>; } } } } If the switch does not uniquely identify all network-connected endpoint devices before establishing any connection for access interfaces connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000168-L2S-000019

**Group ID:** `V-253950`

### Rule: The Juniper layer 2 switch must be configured to disable all dynamic VLAN registration protocols.

**Rule ID:** `SV-253950r843883_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Dynamic VLAN registration protocols provide centralized management of VLAN domains, which can reduce administration in a switched network. Interfaces are assigned to VLANs and the VLAN is dynamically registered on the trunked interface. Removing the last active interface from the VLAN automatically prunes the VLAN from the trunked interface, preserving bandwidth. Member switches remain synchronized via the exchange of Protocol Data Units (PDU). Protocols like Cisco VLAN Trunk Protocol (VTP) and IEEE 802.1ak Multiple VLAN Registration Protocol (MVRP) permit dynamically registering/de-registering VLANs on trunked interfaces. Without authentication, forged PDUs can allow access to previously inaccessible VLANs, or inclusion of unauthorized VLANs or switches. Only VTP currently supports authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify if dynamic VLAN registration protocols are enabled. If dynamic VLAN registration protocols are enabled, verify that authentication has been configured. Juniper switches do not support VTP. Although Juniper switches support MVRP, it is disabled by default (there is no [edit protocols mvrp] stanza). Verify MVRP is not enabled as shown below. [edit protocols] mvrp { interface <name>; } If dynamic VLAN registration protocols have been configured on the switch and are not authenticating messages with a hash function using the most secured cryptographic algorithm available, this is a finding.

## Group: SRG-NET-000193-L2S-000020

**Group ID:** `V-253951`

### Rule: The Juniper EX switch must be configured to manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-253951r1082966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks can be mitigated by ensuring sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, quality of service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages). A Junos OS classifier identifies and separates traffic flows and provides the means to prioritize traffic later in the class-of-service (CoS) process. By default, Junos implements a standard CoS (QoS) strategy. Although some devices implement different queues or queue numbers, generally there is at least a four-queue model with two active queues: 95 percent Best Effort (BE) and 5 percent Network Control (NE). A behavior aggregate (BA) classifier performs this function by associating discriminating values with forwarding classes and loss priorities. Unless overridden, Junos OS applies the default CoS to all interfaces. Junos OS provides multiple predefined BA classifier types, which the site can combine and supplement with custom CoS configuration as needed to achieve overall traffic classification goals.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that Class-of-Service (CoS) has been enabled. Ensure sufficient capacity is available for mission-critical traffic to enforce the traffic priorities specified by the Combatant Commanders/Services/Agencies. By default, Junos implements a standard CoS (QoS) strategy. Although some devices implement different queues or queue numbers, generally there is at least a four-queue model with two active queues: 95 percent Best Effort (BE) and 5 percent Network Control (NC). Verify additional queues are configured to support the traffic priorities of the Combatant Commanders/Services/Agencies. The example CoS below adds a queue for one type of prioritized traffic. The example shows the interdependency of the classifiers, the schedulers, and the interfaces but the names, classifier code points, and scheduler rates are only examples. The names, code points, and rates must be appropriate for the target environment. Additional configuration is required for each type of prioritized traffic. Note: The example CoS names, scheduler rates, and DSCP values must not be considered requirements. The names, rates, and values must be appropriately configured for the target environment. user@host> show configuration class-of-service classifiers { dscp prioritized-traffic-classifier { import default; forwarding-class expedited-forwarding { loss-priority low code-points [ 101110 100100 ]; } } } interfaces { <interface> { scheduler-map prioritized-traffic-map; unit <logical unit> { classifiers { dscp prioritized-traffic-classifier; } } } <uplink interface> { scheduler-map prioritized-traffic-map; unit <logical unit> { classifiers { dscp prioritized-traffic-classifier; } } } scheduler-maps { prioritized-traffic-map { forwarding-class best-effort scheduler be-scheduler; forwarding-class expedited-forwarding scheduler ef-scheduler; forwarding-class network-control scheduler nc-scheduler; } } schedulers { be-scheduler { transmit-rate { remainder; } priority low; } ef-scheduler { shaping-rate percent 20; priority strict-high; } nc-scheduler { shaping-rate percent 5; priority strict-high; } } If the switch is not configured to implement a QoS policy, this is a finding.

## Group: SRG-NET-000331-L2S-000001

**Group ID:** `V-253952`

### Rule: The Juniper EX switch must be configured to permit authorized users to select a user session to capture.

**Rule ID:** `SV-253952r1082341_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to select a user session to capture/record or view/hear, investigations into suspicious or harmful events would be hampered by the volume of information captured. The volume of information captured may also adversely impact the operation for the network. Session audits may include port mirroring, tracking websites visited, and recording information and/or file transfers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the switch configuration has an analyzer to capture ingress and egress packets from any designated access interface for the purpose of monitoring a specific user session. Packet capture using the [edit forwarding-options analyzer <analyzer name>] configuration will only be present and enabled when actively monitoring sessions. If actively capturing packets, verify an analyzer is present. [edit forwarding-options] analyzer { <analyzer name> { input { ingress { interface <input interface>.<logical unit>; -or- interface irb.<logical unit>; } egress { interface <input interface>.<logical unit>; -or- interface irb.<logical unit>; } } output { interface <output interface>.<logical unit>; } } } Note: Simultaneously mirroring both ingress and egress traffic may exceed the output interface capacity. Packet mirroring consumes resources and should only be enabled when actively monitoring sessions. If active monitoring is not currently required, the lack of an analyzer, or the presence of an inactive (disabled) analyzer, is not a finding. If the switch is not configured to capture ingress and egress packets from a designated access interface, this is a finding.

## Group: SRG-NET-000332-L2S-000002

**Group ID:** `V-253953`

### Rule: The Juniper EX switch must be configured to permit authorized users to remotely view, in real time, all content related to an established user session from a component separate from the layer 2 switch.

**Rule ID:** `SV-253953r1082342_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to remotely view/hear all content related to a user session, investigations into suspicious user activity would be hampered. Real-time monitoring allows authorized personnel to take action before additional damage is done. The ability to observe user sessions as they are happening allows for interceding in ongoing events that after-the-fact review of captured content would not allow.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify if the switch configuration has an analyzer to capture ingress and egress packets from any designated switch port for the purpose of remotely monitoring a specific user session. Packet capture using the [edit forwarding-options analyzer <analyzer name>] configuration will only be present and enabled when actively monitoring sessions. The Juniper switch supports either output interface or output vlan. To output to a VLAN that is trunked to a remote location, configure the switch with the destination VLAN, configure the uplink interface as trunked, and include the remote analyzer VLAN in the uplink trunk. If actively capturing packets, verify an analyzer is present. [edit vlans] <destination VLAN name> { vlan-id <VLAN ID>; } [edit interfaces] <interface name> { unit 0 { family ethernet-switching { interface-mode trunk; vlan { members <destination VLAN name>; } } } } [edit forwarding-options] analyzer { <analyzer name> { input { ingress { interface <input interface>.<logical unit>; -or- interface irb.<logical unit>; } egress { interface <input interface>.<logical unit>; -or- interface irb.<logical unit>; } output { vlan { <destination VLAN name>; } } } } Note: Simultaneously mirroring both ingress and egress traffic may exceed the output interface capacity. Packet mirroring consumes resources and should only be enabled when actively monitoring sessions. If active monitoring is not currently required, the lack of an analyzer, or the presence of an inactive (disabled) analyzer, is not a finding. If the switch is not configured to capture ingress and egress packets from a designated access interface for the purpose of remotely monitoring a specific user session, this is a finding.

## Group: SRG-NET-000343-L2S-000016

**Group ID:** `V-253954`

### Rule: The Juniper EX switch must be configured to authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-253954r1082969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without authenticating devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. Device authentication is a solution enabling an organization to manage devices. It is an additional layer of authentication ensuring only specific pre-authorized devices can access the system. This requirement applies to applications that connect either locally, remotely, or through a network to an endpoint device (including, but not limited to, workstations, printers, servers (outside a datacenter), VoIP Phones, and VTC CODECs. Gateways and SOA applications are examples of where this requirement would apply. For Juniper EX, configure 802.1 x authentication on all host-facing access interfaces. To authenticate those devices that do not support an 802.1x supplicant, Static MAC Bypass or MAC RADIUS must be configured. Junos supports three supplicant types: single-secure (authenticate and permit only a single device), multiple (separately authenticate and permit multiple devices), and single (authenticate the first supplicant and permit all others). The authentication order must be appropriate for the target environment. Authentication must be configured on all access interfaces connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the switch configuration has 802.1x authentication implemented for all access interfaces connecting to LAN outlets (i.e., RJ-45 wall plates) or devices not located in the telecom room, wiring closets, or equipment rooms. Static MAC Bypass or MAC RADIUS must be configured on access interfaces connected to devices that do not support an 802.1x supplicant. Junos supports three supplicant types: single-secure (authenticate and permit only a single device), multiple (separately authenticate and permit multiple devices), and single (authenticate the first supplicant and permit all others). Verify the available RADIUS server(s) are configured. RADIUS servers can be configured globally at [edit access radius-server] or defined for each group. user@host> show configuration access radius-server { <RADIUS IPv4 or IPv6 address> secret "PSK"; ## SECRET-DATA } profile dot1x_radius { authentication-order radius; radius { authentication-server <RADIUS IPv4 or IPv6 address>; <<< Must be defined if using global RADIUS server. Optional if RADIUS is defined specifically for the profile. } radius-server { <RADIUS IPv4 or IPv6 address> secret "PSK"; ## SECRET-DATA <<< Must be defined if not using global RADIUS server. Takes precedence if both profile and global RADIUS is configured. } } Verify 802.1x or MAC RADIUS is configured on all host-facing access interfaces when RADIUS is available as shown in the following example. The default authentication order is dot1x, mac-radius, and captive-portal. This order is applied to all interfaces without the authentication order directive configured (int-01 shown below). For interfaces with connected devices that do not support 802.1x (int-02 below), it may be necessary to change the authentication order because the device authentication attempt may timeout before the switch fails over from dot1x to mac-radius. When restricting to mac-radius authentication only (int-03 below), the authentication order cannot be set. user@host> show configuration protocols dot1x authenticator { authentication-profile-name dot1x_radius; interface { <int-01 name> { <<< Connected device with 802.1x supplicant supplicant single-secure; } <int-02 name> { <<< Connected device with 802.1x supplicant and interface support for MAC RADIUS, MAC RADIUS authentication preferred authentication-order [ mac-radius dot1x captive-portal ]; supplicant multiple; mac-radius; } <int-03 name> { <<< Connected device without 802.1x supplicant mac-radius { restrict; } } } } Note: The interface names, supplicant type, MAC RADIUS support, and authentication order must be appropriate for the target environment. If RADIUS is unavailable or not configured: user@host> show configuration protocols dot1x authenticator { static { <MAC address>/48 { vlan-assignment <vlan name>; interface <interface name>.<logical unit>; } } } If 802.1x authentication, Static MAC Bypass, or MAC RADIUS is not configured on all access interfaces connecting to LAN outlets or devices not located in the telecom room, wiring closets, or equipment rooms, this is a finding.

## Group: SRG-NET-000362-L2S-000021

**Group ID:** `V-253955`

### Rule: The Juniper EX switch must be configured to enable Root Protection on STP switch ports connecting to access layer switches.

**Rule ID:** `SV-253955r1082970_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) does not provide any means for the network administrator to securely enforce the topology of the switched network. Any switch can be the root bridge in a network. However, a more optimal forwarding topology places the root bridge at a specific predetermined location. With the standard STP, any bridge in the network with a lower bridge ID takes the role of the root bridge. The administrator cannot enforce the position of the root bridge but can set the root bridge priority to zero in an effort to secure the root bridge position. The Root Protection feature provides a way to enforce the root bridge placement in the network. If the bridge receives superior STP Bridge Protocol Data Units (BPDUs) on a Root Protection-enabled interface, Root Protection ignores the superior BPDU and places the interface into block and a root-inconsistent state. To enforce the position of the root bridge it is imperative that Root Protection is enabled on all interfaces where the root bridge should never appear. Note: Although Loop Protection can be applied to all nondesignated ports, JUEX-L2-000100 requires that Loop Protection be applied to all user-facing access switch ports. Thus, Loop Protection must only be applied to all nondesignated ports that are not also user-facing access switch ports. Loop Protection and Root Protection cannot be applied to the same port. Additionally, note that configuring BPDU Protection and Root Protection on the same interface is supported because BPDU protection includes Root Protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch topology as well as the switch configuration to verify that Root Protection is enabled on all interfaces connecting to access layer switches. [edit protocols] mstp { interface <interface name> { no-root-port; } } If Root Protection is not enabled on all interfaces connecting to access layer switches, this is a finding.

## Group: SRG-NET-000362-L2S-000022

**Group ID:** `V-253956`

### Rule: The Juniper EX switch must be configured to enable BPDU Protection on all user-facing or untrusted access switch ports.

**Rule ID:** `SV-253956r843901_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a rogue switch is introduced into the topology and transmits a Bridge Protocol Data Unit (BPDU) with a lower bridge priority than the existing root bridge, it will become the new root bridge and cause a topology change, rendering the network in a suboptimal state. BPDU Protection allows network designers to enforce the STP domain borders and keep the active topology predictable. The devices behind interfaces that have BPDU Protection enabled are not able to influence the STP topology. At the reception of BPDUs, BPDU Protection disables the port and logs the condition.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that BPDU Protection is enabled on all user-facing or untrusted access switch interfaces. BPDU Protection discards all BPDUs received on a configured interface and stops forwarding on that interface. In contrast, Root Protection discards only superior root BPDUs but accepts remaining BPDU types. Verify BDPU Protection (bpdu-block-on-edge) and the edge interfaces where no BPDUs are expected. [protocols] mstp { bpdu-block-on-edge; interface <interface name> { edge; } } Note: Configuring BPDU Protection and Root Protection on the same interface is supported, but redundant because BPDU protection includes Root Protection. If the switch has not enabled BPDU Protection, this is a finding.

## Group: SRG-NET-000362-L2S-000023

**Group ID:** `V-253957`

### Rule: The Juniper EX switch must be configured to enable STP Loop Protection on all non-designated STP switch ports.

**Rule ID:** `SV-253957r843904_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Spanning Tree Protocol (STP) Loop Protection feature provides additional protection against STP loops. An STP loop is created when an STP blocking port in a redundant topology erroneously transitions to the forwarding state. In its operation, STP relies on continuous reception and transmission of BPDUs based on the port role. The designated port transmits BPDUs, and the non-designated port receives BPDUs. When one of the ports in a physically redundant topology no longer receives BPDUs, the STP conceives that the topology is loop free. Eventually, the blocking port from the alternate or backup port becomes a designated port and moves to a forwarding state. This situation creates a loop. The loop protection feature makes additional checks. If BPDUs are not received on a non-designated port and loop protection is enabled, that port is moved into the STP loop-inconsistent blocking state.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that STP Loop Protection is enabled on all non-designated STP switch ports. Verify STP Loop Protection for RSTP and VSTP. [edit protocols] rstp { interface <interface name> { bpdu-timeout-action { block; } } } vstp { interface <interface name> { bpdu-timeout-action { block; } } } Verify Loop Protection for all instances on an MSTP interface: [protocols] mstp { interface <interface name> { bpdu-timeout-action { block; } } } Note: Loop Protection and Root Protection are mutually exclusive and cannot be simultaneously configured on the same interface. If STP Loop Protection is not configured on non-designated STP ports, this is a finding.

## Group: SRG-NET-000362-L2S-000025

**Group ID:** `V-253959`

### Rule: The Juniper EX switch must be configured to enable DHCP snooping for all user VLANs to validate DHCP messages from untrusted sources.

**Rule ID:** `SV-253959r843910_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In an enterprise network, devices under administrative control are trusted sources. These devices include the switches, routers, and servers in the network. Host interfaces and unknown DHCP servers are considered untrusted sources. An unknown DHCP server on the network on an untrusted interface is called a spurious DHCP server, any device (PC, Wireless Access Point) that is loaded with DHCP server enabled. The DHCP snooping feature determines whether traffic sources are trusted or untrusted. The potential exists for a spurious DHCP server to respond to DHCPDISCOVER messages before the real server has time to respond. DHCP snooping allows switches on the network to trust the interface a DHCP server is connected to and not trust the other interfaces. The DHCP snooping feature validates DHCP messages received from untrusted sources and filters out invalid messages as well as rate-limits DHCP traffic from trusted and untrusted sources. The DHCP snooping feature builds and maintains a binding database, which contains information about untrusted hosts with leased IP addresses, and it utilizes the database to validate subsequent requests from untrusted hosts. Other security features, such as IP Source Guard and Dynamic Address Resolution Protocol (ARP) Inspection (DAI), also use information stored in the DHCP snooping binding database. Hence, it is imperative that the DHCP snooping feature is enabled on all user-facing or untrusted VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that DHCP snooping is enabled on all user-facing or untrusted VLANs. DHCP snooping is enabled if dhcp-security is configured for any VLAN, and is automatically enabled whenever any other VLAN port security feature is configured (e.g., IP Source Guard or Dynamic ARP Inspection). Devices like printers, servers, and VoIP phones are under administrative control and connected to controlled access interfaces (802.1x, Static MAC Bypass, or MAC RADIUS), making them trusted sources in non-user-facing VLANs. Verify DHCP snooping on user-facing or untrusted VLANs. [edit vlans] <untrusted VLAN name> { vlan-id <VLAN ID>; forwarding-options { dhcp-security; } } If the switch does not have DHCP snooping enabled for all user-facing or untrusted VLANs to validate DHCP messages from untrusted sources, this is a finding.

## Group: SRG-NET-000362-L2S-000026

**Group ID:** `V-253960`

### Rule: The Juniper EX switch must be configured to enable IP Source Guard on all user-facing or untrusted access VLANs.

**Rule ID:** `SV-253960r843913_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IP Source Guard provides source IP address filtering on an untrusted layer 2 interface to prevent a malicious host from impersonating a legitimate host by assuming the legitimate host's IP address. The feature uses dynamic DHCP snooping and static IP source binding to match IP addresses to hosts on untrusted layer 2 access interfaces. Initially, all IP traffic on the protected interface is blocked except for DHCP packets. After a client receives an IP address from the DHCP server, or after static IP source binding is configured by the administrator, all traffic with that IP source address is permitted from that client. Traffic from other hosts is denied. This filtering limits a host's ability to attack the network by claiming a neighbor host's IP address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that IP Source Guard is enabled on all user-facing or untrusted VLANs. Configuring IP Source Guard automatically enables DHCP snooping. Devices like printers, servers, and VoIP phones are under enterprise control and connected to controlled access interfaces (802.1x, Static MAC Bypass, or MAC RADIUS), making them trusted sources in non-user-facing VLANs. Verify IP Source Guard on user-facing or untrusted VLANs. [edit vlans] <untrusted VLAN name> { vlan-id <VLAN ID>; forwarding-options { dhcp-security { ip-source-guard; } } } Note: IP Source Guard depends upon DHCP snooping or static MAC address bindings. If the switch does not have IP Source Guard enabled on all user-facing or untrusted VLANs, this is a finding.

## Group: SRG-NET-000362-L2S-000027

**Group ID:** `V-253961`

### Rule: The Juniper EX switch must be configured to enable Dynamic Address Resolution Protocol (ARP) Inspection (DAI) on all user VLANs.

**Rule ID:** `SV-253961r843916_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DAI intercepts Address Resolution Protocol (ARP) requests and verifies that each of these packets has a valid IP-to-MAC address binding before updating the local ARP cache and before forwarding the packet to the appropriate destination. Invalid ARP packets are dropped and logged. DAI determines the validity of an ARP packet based on valid IP-to-MAC address bindings stored in the DHCP snooping binding database. If the ARP packet is received on a trusted interface, the switch forwards the packet without any checks. On untrusted interfaces, the switch forwards the packet only if it is valid.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that Dynamic Address Resolution Protocol (ARP) Inspection (DAI) feature is enabled on all user VLANs. Configuring DAI automatically enables DHCP snooping. Devices like printers, servers, and VoIP phones are under enterprise control and connected to controlled access interfaces (802.1x, Static MAC Bypass, or MAC RADIUS), making them trusted sources in non-user-facing VLANs. Verify DAI on user-facing or untrusted VLANs. [edit vlans] <untrusted VLAN name> { vlan-id <VLAN ID>; forwarding-options { dhcp-security { arp-inspection; } } } Note: DAI depends upon DHCP snooping or static MAC address bindings. If DAI is not enabled on all user VLANs, this is a finding.

## Group: SRG-NET-000512-L2S-000001

**Group ID:** `V-253962`

### Rule: The Juniper EX switch must be configured to enable Storm Control on all host-facing access interfaces.

**Rule ID:** `SV-253962r843919_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A traffic storm occurs when packets flood a LAN, creating excessive traffic and degrading network performance. Traffic storm control prevents network disruption by suppressing ingress traffic when the number of packets reaches configured threshold levels. Traffic storm control monitors ingress traffic levels on a port and drops traffic when the number of packets reaches the configured threshold level during any one-second interval.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that storm control is enabled on host-facing access interfaces. Verify storm control profiles at [edit forwarding-options storm-control-profiles] with an appropriate bandwidth value (actual bandwidth value or a percentage). By default, ELS versions of Junos enable storm control with an 80 percent of bandwidth value, but permit setting different values as either an absolute level or a percentage of available bandwidth. Note: Although percentage of bandwidth remains supported, it is deprecated and subject to removal. Therefore, an absolute level should be used. Threshold values must be configured appropriately for the target network. Verify the default storm control profile or a custom profile with appropriate bandwidth percentage or level. [edit forwarding-options] storm-control-profiles profile-percent { all { bandwidth-percentage (1..100); } action-shutdown; } storm-control-profiles profile-level { all { bandwidth-level (100..100000000 kbps); } action-shutdown; } Note: Storm control profiles are created with the hierarchy "all" but support removing specific traffic types using the "no-<traffic type>" keyword. The currently supported exclusions: no-broadcast Disable broadcast storm control no-multicast Disable multicast storm control no-registered-multicast Disable registered multicast storm control no-unknown-unicast Disable unknown unicast storm control no-unregistered-multicast Disable unregistered multicast storm control If excluding traffic, verify at least broadcast storm control is enabled. Verify that storm control profiles are applied to layer 2 host-facing access interfaces. [edit interfaces] <interface name> { unit 0 { family ethernet-switching { storm-control <profile name>; recovery-timeout (10..3600 seconds); } } } Note: If a recovery-timeout is not specified, and the storm control profile enforces action-shutdown, affected interfaces are disabled until manually enabled by an authorized administrator. If storm control is not enabled on all host-facing access interfaces, this is a finding.

## Group: SRG-NET-000512-L2S-000002

**Group ID:** `V-253963`

### Rule: The Juniper EX switch must be configured to enable IGMP or MLD Snooping on all VLANs.

**Rule ID:** `SV-253963r843922_rule`
**Severity:** low

**Description:**
<VulnDiscussion>IGMP and MLD snooping provides a way to constrain multicast traffic at layer 2. By monitoring the IGMP or MLD membership reports sent by hosts within a VLAN, the snooping application can set up layer 2 multicast forwarding tables to deliver specific multicast traffic only to interfaces connected to hosts interested in receiving the traffic, thereby significantly reducing the volume of multicast traffic that would otherwise flood the VLAN.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration to verify that IGMP or MLD snooping has been configured for IPv4 and IPv6 multicast traffic respectively. Verify IGMP and MLD is globally configured for all VLANs: [edit protocols] igmp-snooping { vlan all { immediate-leave; interface <multicast router interface name>.<logical unit> { multicast-router-interface; } } } mld-snooping { vlan all { immediate-leave; interface <multicast router interface name>.<logical unit> { multicast-router-interface; } } } For VLAN-specific values, verify IGMP and MLD snooping is configured for each VLAN: [edit protocols] igmp-snooping { vlan vlan-name { immediate-leave; interface <multicast router interface name>.<logical unit> { multicast-router-interface; } interface <host interface name>.<logical unit> { host-only-interface; } } } mld-snooping { vlan vlan-name { immediate-leave; interface <multicast router interface name>.<logical unit> { multicast-router-interface; } interface <host interface name>.<logical unit> { host-only-interface; } } } If the switch is not configured to implement IGMP or MLD snooping for each VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000003

**Group ID:** `V-253964`

### Rule: If STP is used, the Juniper EX switch must be configured to implement Rapid STP, or Multiple STP, where VLANs span multiple switches with redundant links.

**Rule ID:** `SV-253964r843925_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spanning Tree Protocol (STP) is implemented on bridges and switches to prevent layer 2 loops when a broadcast domain spans multiple bridges and switches and when redundant links are provisioned to provide high availability in case of link failures. Convergence time can be significantly reduced using Rapid STP (802.1w) instead of STP (802.1d), resulting in improved availability. Rapid STP should be deployed by implementing either Rapid Spanning-Tree Protocol (RSTP) or Multiple Spanning-Tree Protocol (MSTP), the latter scales much better when there are many VLANs. In cases where VLANs do not span multiple switches, it is a best practice to not implement STP. Avoiding the use of STP will provide the most deterministic and highly available network topology. If STP is required, then review the switch configuration to verify that Rapid STP or Multiple STP has been implemented. RSTP and MSTP are similar, except MSTP is more granular, flexible, and scalable. RTSP and MSTP can be enabled simultaneously, but in general only one STP is configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If STP is required, then review the switch configuration to verify that Rapid STP or Multiple STP has been implemented. RSTP and MSTP are similar, except MSTP is more granular, flexible, and scalable. RTSP and MSTP can be enabled simultaneously, but in general only one STP is configured. RSTP: [edit protocols rstp] rstp { bridge-priority (0..61440 in 4k increments); << e.g. 0, 4k, 8k...60k interface <interface name> { edge; } interface <interface name-1> { mode point-to-point; } bpdu-block-on-edge; } -OR- MSTP: [edit protocols mstp] configuration-name <name>; revision-level (0..65535); max-age (6..40 seconds); hello-time (1..10 seconds); forward-delay (4..30 seconds); bridge-priority (0..61440 in 4k increments); << e.g. 0, 4k, 8k...60k bpdu-block-on-edge; interface <interface name> { edge; } interface <interface name-1> { mode point-to-point; } msti 3 { bridge-priority (0..61440 in 4k increments); << e.g. 0, 4k, 8k...60k vlan [ vlan-id-1 vlan-id-2 ]; } If Rapid STP or Multiple STP has not been implemented where an STP is required, this is a finding.

## Group: SRG-NET-000512-L2S-000004

**Group ID:** `V-253965`

### Rule: The Juniper EX switch must be configured to verify two-way connectivity on all interswitch trunked interfaces.

**Rule ID:** `SV-253965r843928_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In topologies where fiber optic interconnections are used, physical misconnections can occur that allow a link to appear to be up when there is a mismatched set of transmit/receive pairs. When such a physical misconfiguration occurs, protocols such as STP can cause network instability. OAM LFM and LAG are industry standard layer 2 protocols that can detect these physical misconfigurations by verifying that traffic is flowing bidirectionally between neighbors. Interfaces with OAM configured, and LAG interfaces, periodically transmit packets to neighbor devices. If the packets are not exchanged within a specific time frame, the link is flagged as unidirectional and the interface is shut down. OAM LFM and LAG require both connected devices to be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If any of the interfaces have fiber optic interconnections with neighbors, review the switch configuration to verify that OAM or LAG is enabled on those interfaces. Because OAM and LAG interfaces exchange packets, the neighbor device must also be configured with OAM or LAG. Verify OAM connectivity fault management: [edit protocols oam ethernet link-fault-management] interface <interface name>; Note: To enable LFM using default values, specifying the interface is sufficient. Verify OAM connectivity with custom actions (must match the target environment). action-profile <profile name> { event { link-adjacency-loss; protocol-down; link-event-rate { frame-error (1..1000 error(s) per 100 milli-second); frame-period (1..100 error(s) per 100 frames); frame-period-summary (1..1000 error(s) per second); symbol-period (1..100 error(s) per 100 symbol); } } action { syslog; link-down; } } interface <interface name-1> { apply-action-profile <profile name>; pdu-interval (100..1000 milliseconds); pdu-threshold (5..10); detect-loc; link-discovery active; } interface <interface name>; Verify LAG on appropriate interfaces: [edit interfaces] <interface name> { ether-options { 802.3ad ae<bundle number>; } } ae<bundle number> { aggregated-ether-options { lacp { active; periodic slow; } } unit 0 { family ethernet-switching { interface-mode trunk; vlan { members [ vlan_name ... vlan_name ]; } } } } Note: The bundle number is an integer value that matches the logical LAG interface. For example, physical interface "ge-0/0/0 ether-options 802.3ad ae0" is only associated with the logical LAG bundle "ae0". If the switch has fiber optic interconnections with neighbors and OAM or LAG is not enabled, this is a finding.

## Group: SRG-NET-000512-L2S-000007

**Group ID:** `V-253966`

### Rule: The Juniper EX switch must be configured to assign all explicitly disabled access interfaces to an unused VLAN.

**Rule ID:** `SV-253966r1082973_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is possible that a configured, but disabled access interface assigned to a user or management VLAN becomes enabled by accident or by an attacker and as a result, gains access to that VLAN as a member. Unconfigured Junos interfaces are not capable of passing network traffic and do not participate in any user configured VLANs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this is an access interface configured for 802.1x, this is not applicable. 1. Review the switch configurations and examine all configured access interfaces. 2. Verify each configured access interface not in use has membership in an inactive VLAN that is not used for any purpose and is not allowed on any trunk links. Unconfigured interfaces should not be configured "disabled" merely to meet this requirement because unconfigured interfaces are incapable of passing network traffic. Verify a VLAN is configured for unused interfaces. In the following example, VLAN name is "vlan-disabled", but that name should match local naming conventions. user@host> show configuration vlans vlan_disabled { vlan-id <VLAN ID>; } 3. Verify configured, but unused, interfaces are assigned to an unused VLAN either individually or via the "interface-range" command. Verify interfaces configured via "interface-range" are not also configured individually. Multiple interfaces simultaneously configured via interface-range. user@host> show configuration interfaces interface-range <name> { member <interface name>; member-range <starting interface name> to <ending interface name>; <<< Member ranges are contiguous from <start interface> to <end interface> inclusive disable; unit 0 { family ethernet-switching { vlan { members vlan_disabled; } } } } 4. Individually configured: user@host> show configuration interfaces <interface name> { disable; unit 0 { family ethernet-switching { vlan { members vlan_disabled; } } } } 5. In the following example, "vlan_disabled" is designated for all configured, but disabled interfaces, and must not be configured on any trunked interface. Verify the unused VLAN is NOT a member of any trunked interface as in the example below. user@host> show configuration interfaces <interface name> { unit <logical unit> { family { ethernet-switching { interface-mode trunk; vlan { members [ vlan_name vlan_disabled ]; } } } } } 6. Verify if there are unconfigured physical interfaces. These interfaces should not be configured merely to set them disabled because they are already incapable of passing network traffic, participating in protocols, and are not members of any user configured VLANS. user@host> show interfaces terse ge-0/0/0 up up ge-0/0/0.0 up up eth-switch ge-0/0/1 up up ge-0/0/1.0 up up eth-switch …<snip>… ge-0/0/5 up down ge-0/0/5.16386 up down ge-0/0/6 up down ge-0/0/6.16386 up down ge-0/0/7 up down ge-0/0/7.16386 up down 7. As shown in the example above, ge-0/0/5 through ge-0/0/7 are unconfigured interfaces. Verify there is no configuration stanza for these interfaces. user@host> show configuration interfaces ge-0/0/0 { unit 0 { family ethernet-switching { vlan { members <VLAN name>; } } } } ge-0/0/1 { unit 0 { family ethernet-switching { vlan { members <VLAN name>; } } } } …<snip>… xe-0/1/0 { ether-options { 802.3ad ae0; } } 8. The example above shows that ge-0/0/1 is the last configured access interface and the next configured interface is a 10GbE Link Aggregation Group (LAG) member. Because Junos lists interface names in ascending order, the example unconfigured interfaces (ge-0/0/5 through ge-0/0/7) would appear between the configured interfaces ge-0/0/1 and xe-0/1/0. Therefore, the subject interfaces, while present on the device, are not configured and are incapable of passing network traffic. If there are any configured, but disabled access interfaces not in an inactive VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000008

**Group ID:** `V-253967`

### Rule: The Juniper EX switch must not be configured with VLANs used for L2 control traffic assigned to any host-facing access interface.

**Rule ID:** `SV-253967r997518_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In a switched Ethernet network, some protocols use L2 Protocol Data Units (PDU) to communicate in-band management or other control information. This control traffic is inappropriate for host-facing access interfaces because those devices are not part of the switching infrastructure. Juniper switches do not automatically carry this L2 control traffic in the default VLAN or automatically assign the default VLAN to all trunks, reducing the scope of potential misuse. Preventing host-facing access interfaces from participating in the L2 control traffic communications further reduces the risk of inadvertent (or malicious) interference.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and verify all access interfaces are assigned to a configured VLAN not used for L2 control traffic. If assigning via interface-range, the configuration will be similar to the example. [edit interfaces] interface-range <name> { member <interface name>; member-range <starting interface name> to <ending interface name>; <<< Member ranges are contiguous from <start interface> to <end interface> inclusive unit 0 { family ethernet-switching { vlan { members <vlan name>; } } } } If assigning individually, the configuration will be similar to the example. [edit interfaces] <interface name> { unit 0 { family ethernet-switching { vlan { members <vlan name>; } } } } Verify the assigned VLANs are configured. [edit vlans] <vlan name> { vlan-id <VLAN ID>; } Note: Assigning interfaces to a VLAN automatically removes them from the default VLAN. If there are access interfaces assigned to the VLANs used for L2 control traffic, this is a finding.

## Group: SRG-NET-000512-L2S-000009

**Group ID:** `V-253968`

### Rule: The Juniper EX switch must be configured to prune the default VLAN from all trunked interfaces that do not require it.

**Rule ID:** `SV-253968r843937_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>All unassigned interfaces are placed into the default VLAN and devices connected to enabled, but unassigned interfaces can communicate within that VLAN. Although the default VLAN is not automatically assigned to any trunked interface, if the default VLAN must be trunked or a misconfigured trunk unintentionally includes the default VLAN, unauthorized devices connected to enabled but unassigned access interfaces could gain network connectivity beyond the local switch.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that the default VLAN is pruned from trunk links that do not require it. [edit interfaces] <interface name> { unit 0 { family ethernet-switching { interface-mode trunk; vlan { members [ vlan_name ... vlan_name ]; } } } } If the default VLAN is not pruned from trunk links that should not be transporting frames for that VLAN, this is a finding.

## Group: SRG-NET-000512-L2S-000010

**Group ID:** `V-253969`

### Rule: The Juniper EX switch must not use the default VLAN for management traffic.

**Rule ID:** `SV-253969r997519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, all unassigned interfaces are placed into the default VLAN and if used for management, could unintentionally expose sensitive traffic or protected resources to unauthorized devices.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and verify that the default VLAN is not used to access the switch for management. Verify access interfaces used for management are assigned to an appropriate VLAN as in the example below. [edit interfaces] <interface name> { unit 0 { family ethernet-switching { interface-mode access; vlan { members <vlan name>; } } } } If the default VLAN is being used to access the switch, this is a finding.

## Group: SRG-NET-000512-L2S-000011

**Group ID:** `V-253970`

### Rule: The Juniper EX switch must be configured to set all enabled user-facing or untrusted ports as access interfaces.

**Rule ID:** `SV-253970r1082976_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, unconfigured (or expressly disabled) Junos interfaces are unusable. Any enabled interface configured with the family ethernet-switching uses interface-mode access by default, which meets this requirement. Trunked interfaces must be explicitly configured for operational requirements (e.g., interswitch links), which makes them trusted and not user-facing. Configuring enabled user-facing or untrusted interfaces as trunked may expose network traffic to an unauthorized, or unintended, connected endpoint. Access interfaces can belong to a single VLAN rather than the multiple VLANs supported by trunks, which limits potential exposure to a smaller subset of the total network traffic. Access interfaces also behave differently than trunked interfaces, especially with respect to control plane traffic. For example, access interfaces can be marked as "edge" for protocols like Rapid Spanning Tree (RSTP) or Multiple Spanning Tree (MSTP) where specific protections can be applied to prevent the switch from accepting Bridge Protocol Data Units (BPDU) from unauthorized sources and causing a network topology change or disruption. Additionally, network level protection mechanisms, like 802.1x or sticky-mac, are applied to access interfaces and these protection mechanisms help prevent unauthorized network access.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and examine all enabled user-facing or untrusted interfaces configured with family ethernet-switching. 1. Interfaces implicitly configured with "interface-mode" access and family ethernet-switching. Note: The default interface-mode is "access". user@host> show configuration interfaces <interface name> { unit 0 { family ethernet-switching { } } } 2. Interfaces explicitly configured with "interface-mode" access and family ethernet-switching. user@host> show configuration interfaces <interface name> { unit 0 { family ethernet-switching { interface-mode access; } } } If any of the enabled user-facing access interfaces are configured as a trunk, this is a finding.

## Group: SRG-NET-000512-L2S-000012

**Group ID:** `V-253971`

### Rule: The Juniper EX switch must not have a native VLAN ID assigned, or have a unique native VLAN ID, for all 802.1q trunk links.

**Rule ID:** `SV-253971r843946_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By default, Juniper switches do not assign a native VLAN to any trunked interface. Allowing trunked interfaces to accept untagged data packets may unintentionally expose VLANs to unauthorized devices that could result in network exploration, unauthorized resource access, or a DoS condition. If a network function requires a native VLAN it must be unique.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configuration and examine all trunked interfaces to verify no native VLAN ID is assigned. If a native VLAN has been assigned, verify the VLAN is unique. By default, there are no native VLANs assigned to any trunked interface. Verify trunked interface do not have a native VLAN ID configured. [edit interfaces] <interface name> { unit 0 { family ethernet-switching { interface-mode trunk; vlan { members [ vlan_name ... vlan_name ]; } } } } If trunked interfaces require a native VLAN, verify it is unique. [edit interfaces] <interface name> { native-vlan-id <unique VLAN ID>; unit 0 { family ethernet-switching { interface-mode trunk; vlan { members [ vlan_name ... vlan_name ]; } } } } Note: By default, Juniper switches do not automatically assign a native VLAN. Configuring an interface with "interface-mode trunk" does not automatically assign the default VLAN. Verify any VLAN assigned as native for any trunked interface has been configured. [edit vlans] native_vlan_name { vlan-id <VLAN ID>; } If trunked interfaces do not have a native VLAN ID configured, this is not a finding. If a native VLAN is configured and does not have a unique VLAN ID, this is a finding.

## Group: SRG-NET-000512-L2S-000013

**Group ID:** `V-253972`

### Rule: The Juniper EX switch must not have any access interfaces assigned to a VLAN configured as native for any trunked interface.

**Rule ID:** `SV-253972r843949_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Trunked interfaces without an assigned native VLAN do not accept untagged data packets. Allowing trunked interfaces to accept untagged data packets may unintentionally expose VLANs to unauthorized devices that could result in network exploration, unauthorized resource access, or a DoS condition. If a network function requires a native VLAN, and access interfaces are members of the assigned VLAN, authorized devices connected to those interfaces may gain unauthorized access to protected resources.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the switch configurations and examine all access interfaces. Verify that they do not belong to any VLAN configured as native for any trunked interface. Example trunked interface with native VLAN ID 30 and an access interface configured for vlan_name: [edit interfaces] <trunk interface name> { native-vlan-id 30; unit 0 { family ethernet-switching { interface-mode trunk; vlan { members [ <vlan name> ... <vlan name> ]; } } } } <access interface name> { unit 0 { family ethernet-switching { interface-mode access; vlan { members vlan_name; } } } } Example VLANs (vlan-id 30 is configured on a trunked interface as native and must not be assigned to access interfaces): [edit vlans] vlan_30 { vlan-id 30; } vlan_name { vlan-id <VLAN ID not 30>; } If trunked interfaces are not configured with a native VLAN ID, this is not a finding. If any trunked interface is configured with a native VLAN ID, and any access interfaces have been assigned to the same VLAN, this is a finding.

