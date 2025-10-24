# STIG Benchmark: VMware NSX-T Tier-0 Gateway Firewall Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000074-FW-000009

**Group ID:** `V-251737`

### Rule: The NSX-T Tier-0 Gateway Firewall must generate traffic log entries containing information to establish the details of the event.

**Rule ID:** `SV-251737r810078_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without sufficient information to analyze the event, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit event content that must be included to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. The Firewall must also generate traffic log records when traffic is denied, restricted, or discarded as well as when attempts are made to send packets between security zones that are not authorized to communicate. Satisfies: SRG-NET-000074-FW-000009, SRG-NET-000075-FW-000010, SRG-NET-000076-FW-000011, SRG-NET-000077-FW-000012, SRG-NET-000078-FW-000013, SRG-NET-000399-FW-000008, SRG-NET-000492-FW-000006, SRG-NET-000493-FW-000007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode and no stateless rules exist, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules. For each Tier-0 Gateway and for each rule, click the gear icon and verify the Logging setting. If Logging is not Enabled, this is a finding.

## Group: SRG-NET-000089-FW-000019

**Group ID:** `V-251738`

### Rule: The NSX-T Tier-0 Gateway Firewall must be configured to use the TLS or LI-TLS protocols to configure and secure communications with the central audit server.

**Rule ID:** `SV-251738r919225_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network element is at risk of failing to process traffic logs as required, it takes action to mitigate the failure. Collected log data be secured and access restricted to authorized personnel. Methods of protection may include encryption or logical separation. In accordance with DOD policy, the traffic log must be sent to a central audit server. Ensure at least primary and secondary syslog servers are configured on the firewall. If the product inherently has the ability to store log records locally, the local log must also be secured. However, this requirement is not met since it calls for a use of a central audit server. This does not apply to traffic logs generated on behalf of the device itself (management). Some devices store traffic logs separately from the system logs. Satisfies: SRG-NET-000089-FW-000019, SRG-NET-000098-FW-000021, SRG-NET-000333-FW-000014</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX-T Edge Node shell hosting the Tier-0 Gateway, run the following command(s): > get logging-servers If any configured logging-servers are not configured with protocol of "li-tls" or "tls" and level of "info", this is a finding. If no logging-servers are configured, this is a finding. Note: This check must be run from each NSX-T Edge Node hosting the Tier-0 Gateway, as they are configured individually.

## Group: SRG-NET-000192-FW-000029

**Group ID:** `V-251739`

### Rule: The NSX-T Tier-0 Gateway Firewall must block outbound traffic containing denial-of-service (DoS) attacks to protect against the use of internal information systems to launch any DoS attacks against other networks or endpoints.

**Rule ID:** `SV-251739r919228_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks can take multiple forms but have the common objective of overloading or blocking a network or host to deny or seriously degrade performance. If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of a firewall at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. The firewall must include protection against DoS attacks that originate from inside the enclave that can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. These attacks can be simple "floods" of traffic to saturate circuits or devices, malware that consumes CPU and memory on a device or causes it to crash, or a configuration issue that disables or impairs the proper function of a device. For example, an accidental or deliberate misconfiguration of a routing table can misdirect traffic for multiple networks. Satisfies: SRG-NET-000192-FW-000029, SRG-NET-000193-FW-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode and no stateless rules exist, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> General Settings >> Firewall >> Flood Protection to view Flood Protection profiles. If there are no Flood Protection profiles of type "Gateway", this is a finding. For each gateway flood protection profile, verify the TCP Half Open Connection limit, UDP Active Flow Limit, ICMP Active Flow Limit, and Other Active Connection Limit are set to "None". If they are not, this is a finding. For each gateway flood protection profile, examine the "Applied To" field to view the Tier-0 Gateways to which it is applied. If a gateway flood protection profile is not applied to all applicable Tier-0 Gateways through one or more policies, this is a finding.

## Group: SRG-NET-000202-FW-000039

**Group ID:** `V-251740`

### Rule: The NSX-T Tier-1 Gateway Firewall must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

**Rule ID:** `SV-251740r810087_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent malicious or accidental leakage of traffic, organizations must implement a deny-by-default security posture at the network perimeter. Such rulesets prevent many malicious exploits or accidental leakage by restricting the traffic to only known sources and only those ports, protocols, or services that are permitted and operationally necessary. This configuration, which is in the Manager function of the NSX-T implementation, helps prevent the firewall instance from failing to a state that may cause unauthorized access to make changes to the firewall filtering functions. As a managed boundary interface, the firewall must block all inbound and outbound network traffic unless a filter is installed to explicitly allow it. The configured filters must comply with the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and Vulnerability Assessment (VA). Satisfies: SRG-NET-000202-FW-000039, SRG-NET-000235-FW-000133, SRG-NET-000236-FW-000027, SRG-NET-000205-FW-000040</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules. Choose each Tier-1 Gateway in drop-down, then select Policy_Default_Infra Section >> Action. If the default_rule is set to "Allow", this is a finding.

## Group: SRG-NET-000362-FW-000028

**Group ID:** `V-251741`

### Rule: The NSX-T Tier-0 Gateway Firewall must employ filters that prevent or limit the effects of all types of commonly known denial-of-service (DoS) attacks, including flooding, packet sweeps, and unauthorized port scanning.

**Rule ID:** `SV-251741r856690_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Not configuring a key boundary security protection device, such as the firewall, against commonly known attacks is an immediate threat to the protected enclave because they are easily implemented by those with little skill. Directions for the attack are obtainable on the internet and in hacker groups. Without filtering enabled for these attacks, the firewall will allow these attacks beyond the protected boundary. Configure the perimeter and internal boundary firewall to guard against the three general methods of well-known DoS attacks: flooding attacks, protocol sweeping attacks, and unauthorized port scanning. Flood attacks occur when the host receives too much traffic to buffer and it slows down or crashes. Popular flood attacks include ICMP flood and SYN flood. A TCP flood attack of SYN packets initiating connection requests can overwhelm the device until it can no longer process legitimate connection requests, resulting in denial of service. An ICMP flood can overload the device with so many echo requests (ping requests) that it expends all its resources responding and can no longer process valid network traffic, also resulting in denial of service. An attacker might use session table floods and SYN-ACK-ACK proxy floods to fill up the session table of a host. In an IP address sweep attack, an attacker sends ICMP echo requests (pings) to multiple destination addresses. If a target host replies, the reply reveals the target's IP address to the attacker. In a TCP sweep attack, an attacker sends TCP SYN packets to the target device as part of the TCP handshake. If the device responds to those packets, the attacker gets an indication that a port in the target device is open, which makes the port vulnerable to attack. In a UDP sweep attack, an attacker sends UDP packets to the target device. If the device responds to those packets, the attacker gets an indication that a port in the target device is open, which makes the port vulnerable to attack. In a port scanning attack, an unauthorized application is used to scan the host devices for available services and open ports for subsequent use in an attack. This type of scanning can be used as a DoS attack when the probing packets are sent excessively.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode and no stateless rules exist, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Security Profiles >> Flood Protection to view Flood Protection profiles. If there are no Flood Protection profiles of type "Gateway", this is a finding. For each gateway flood protection profile, verify the TCP Half Open Connection limit, UDP Active Flow Limit, ICMP Active Flow Limit, and Other Active Connection Limit are set to "not set" or SYN Cache and RST Spoofing is not "Enabled" on a profile, this is a finding. For each gateway flood protection profile, examine the Applied To field to view the Tier-0 Gateways to which it is applied. If a gateway flood protection profile is not applied to all Tier-0 Gateways through one or more policies, this is a finding.

## Group: SRG-NET-000364-FW-000031

**Group ID:** `V-251742`

### Rule: The NSX-T Tier-0 Gateway Firewall must apply ingress filters to traffic that is inbound to the network through any active external interface.

**Rule ID:** `SV-251742r856691_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic to the trusted networks may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Firewall filters control the flow of network traffic, ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet) must be kept separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Tier-0 Gateway is deployed in an Active/Active HA mode and no stateless rules exist, this is Not Applicable. From the NSX-T Manager web interface, go to Security >> Gateway Firewall >> Gateway Specific Rules. Choose each T0-Gateway in the drop-down and review the firewall rules "Applied To" field to verify no rules are selectively applied to interfaces instead of the Gateway Firewall entity. If any Gateway Firewall rules are applied to individual interfaces, this is a finding.

## Group: SRG-NET-000364-FW-000042

**Group ID:** `V-251743`

### Rule: The NSX-T Tier-0 Gateway Firewall must configure SpoofGuard to block outbound IP packets that contain illegitimate packet attributes.

**Rule ID:** `SV-251743r810096_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not filtered, hostile activity intended to harm other networks may not be detected and prevented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Segments and for each Segment, view Segment Profiles >> SpoofGuard. If a Segment is not configured with a SpoofGuard profile that has Port Binding enabled, this is a finding.

