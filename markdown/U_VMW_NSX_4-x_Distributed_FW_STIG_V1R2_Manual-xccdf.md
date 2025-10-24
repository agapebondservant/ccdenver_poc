# STIG Benchmark: VMware NSX 4.x Distributed Firewall Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000074-FW-000009

**Group ID:** `V-265612`

### Rule: The NSX Distributed Firewall must generate traffic log entries that can be sent by the ESXi hosts to the central syslog.

**Rule ID:** `SV-265612r993933_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit event content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the network element logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. Satisfies: SRG-NET-000074-FW-000009, SRG-NET-000075-FW-000010, SRG-NET-000076-FW-000011, SRG-NET-000077-FW-000012, SRG-NET-000078-FW-000013, SRG-NET-000492-FW-000006, SRG-NET-000493-FW-000007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, navigate to Security >> Policy Management >> Distributed Firewall >> All Rules. For each rule, click the gear icon and verify the logging setting. If logging is not enabled for any rule, this is a finding.

## Group: SRG-NET-000193-FW-000030

**Group ID:** `V-265618`

### Rule: The NSX Distributed Firewall must limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-265618r993951_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall experiencing a DoS attack will not be able to handle production traffic load. The high utilization and CPU caused by a DoS attack will also have an effect on control keep-alives and timers used for neighbor peering resulting in route flapping and will eventually black hole production traffic. The device must be configured to contain and limit a DoS attack's effect on the device's resource utilization. The use of redundant components and load balancing are examples of mitigating "flood-type" DoS attacks through increased capacity. Satisfies: SRG-NET-000193-FW-000030, SRG-NET-000192-FW-000029, SRG-NET-000362-FW-000028</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, navigate to Security >> Settings >> General Settings >> Firewall >> Flood Protection to view Flood Protection profiles. If there are no Flood Protection profiles of type "Distributed Firewall", this is a finding. If the TCP Half Open Connection limit, UDP Active Flow Limit, ICMP Active Flow Limit, and Other Active Connection Limit are "not set" or SYN Cache and RST Spoofing is not Enabled on a profile, this is a finding. For each distributed firewall flood protection profile, examine the "Applied To" field to view the workloads it is protecting. If a distributed firewall flood protection profile is not applied to all workloads through one or more policies, this is a finding.

## Group: SRG-NET-000202-FW-000039

**Group ID:** `V-265619`

### Rule: The NSX Distributed Firewall must deny network communications traffic by default and allow network communications traffic by exception.

**Rule ID:** `SV-265619r993954_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent malicious or accidental leakage of traffic, organizations must implement a deny-by-default security posture at the network perimeter. Such rulesets prevent many malicious exploits or accidental leakage by restricting the traffic to only known sources and only those ports, protocols, or services that are permitted and operationally necessary. As a managed boundary interface, the firewall must block all inbound and outbound network traffic unless a filter is installed to explicitly allow it. The allow filters must comply with the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and Vulnerability Assessment (VA). Satisfies: SRG-NET-000202-FW-000039, SRG-NET-000235-FW-000133</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, navigate to Security >> Policy Management >> Distributed Firewall >> Category Specific Rules >> APPLICATION >> Default Layer3 Section >> Default Layer3 Rule >> Action. If the Default Layer3 Rule is set to "ALLOW", this is a finding.

## Group: SRG-NET-000364-FW-000040

**Group ID:** `V-265628`

### Rule: The NSX Distributed Firewall must be configured to inspect traffic at the application layer.

**Rule ID:** `SV-265628r993981_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application inspection enables the firewall to control traffic based on different parameters that exist within the packets such as enforcing application-specific message and field length. Inspection provides improved protection against application-based attacks by restricting the types of commands allowed for the applications. Application inspection all enforces conformance against published RFCs. Some applications embed an IP address in the packet that needs to match the source address that is normally translated when it goes through the firewall. By enabling application inspection for a service that embeds IP addresses, the firewall translates embedded addresses and updates any checksum or other fields that are affected by the translation. By enabling application inspection for a service that uses dynamically assigned ports, the firewall monitors sessions to identify the dynamic port assignments, and permits data exchange on these ports for the duration of the specific session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, navigate to Security >> Distributed Firewall >> All Rules. Review rules that do not have a Context Profile assigned. For example, if a rule exists to allow SSH by service or custom port, then it should have the associated SSH Context Profile applied. If any rules with services defined have an associated suitable Context Profile but do not have one applied, this is a finding.

## Group: SRG-NET-000364-FW-000042

**Group ID:** `V-265630`

### Rule: The NSX Distributed Firewall must configure SpoofGuard to restrict it from accepting outbound packets that contain an illegitimate address in the source address.

**Rule ID:** `SV-265630r993987_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. SpoofGuard is a tool that is designed to prevent virtual machines from sending traffic with an IP address from which it is not authorized to send traffic. In the instance that a virtual machine's IP address does not match the IP address on the corresponding logical port and segment address binding in SpoofGuard, the virtual machine's virtual network interface card (vNIC) is prevented from accessing the network entirely. SpoofGuard can be configured at the port or segment level. There are several reasons SpoofGuard might be used, but for the distributed firewall it will guarantee that rules will not be inadvertently (or deliberately) bypassed. For distributed firewall (DFW) rules created using IP sets as sources or destinations, the possibility always exists that a virtual machine could have its IP address forged in the packet header, thereby bypassing the rules in question.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identity SpoofGuard profiles in use by doing the following: From the NSX Manager web interface, navigate to Networking >> Connectivity >> Segments >> NSX. For each segment, expand view Segment Profiles >> SpoofGuard to note the profiles in use. Review SpoofGuard profile configuration by doing the following: From the NSX Manager web interface, navigate to Networking >> Connectivity >> Segments >> Profiles >> Segment Profiles. Review the SpoofGuard profiles previously identified as assigned to segments to ensure the following configuration: Port Bindings: Yes If a segment is not configured with a SpoofGuard profile that has port bindings enabled, this is a finding.

## Group: SRG-NET-000364-FW-000042

**Group ID:** `V-265633`

### Rule: The NSX Distributed Firewall must configure an IP Discovery profile to disable trust on every use method.

**Rule ID:** `SV-265633r993996_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. IP Discovery in NSX uses DHCP and DHCPv6 snooping, Address Resolution Protocol (ARP) snooping, Neighbor Discovery (ND) snooping, and VM Tools to learn MAC and IP addresses. The discovered MAC and IP addresses are used to achieve ARP/ND suppression, which minimizes traffic between VMs connected to the same logical switch. The addresses are also used by the SpoofGuard and distributed firewall (DFW) components. DFW uses the address bindings to determine the IP address of objects in firewall rules. By default, the discovery methods ARP snooping and ND snooping operate in a mode called trust on first use (TOFU). In TOFU mode, when an address is discovered and added to the realized bindings list, that binding remains in the realized list forever. TOFU applies to the first "n" unique <IP, MAC, VLAN> bindings discovered using ARP/ND snooping, where "n" is the configurable binding limit. Users can disable TOFU for ARP/ND snooping. The methods will then operate in trust on every use (TOEU) mode. In TOEU mode, when an address is discovered, it is added to the realized bindings list and when it is deleted or expired, it is removed from the realized bindings list. DHCP snooping and VM Tools always operate in TOEU mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Identify IP Discovery profiles in use by doing the following: From the NSX Manager web interface, navigate to Networking >> Connectivity >> Segments >> NSX. For each segment, expand view Segment Profiles >> IP Discovery to note the profiles in use. Review IP Discovery profile configuration by doing the following: From the NSX Manager web interface, navigate to Networking >> Connectivity >> Segments >> Profiles >> Segment Profiles. Review the IP Discovery profiles previously identified as assigned to segments to ensure the following configuration: Duplicate IP Detection: Enabled ARP Snooping: Enabled ARP Binding Limit: 1 DHCP Snooping: Disabled DHCP Snooping - IPv6: Disabled VMware Tools: Disabled VMware Tools - IPv6: Disabled Trust on First Use: Enabled If a segment is not configured with an IP Discovery profile that is configured with the settings above, this is a finding.

