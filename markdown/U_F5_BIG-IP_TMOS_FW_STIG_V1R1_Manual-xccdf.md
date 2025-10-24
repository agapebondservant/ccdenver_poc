# STIG Benchmark: F5 BIG-IP TMOS Firewall Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000061-FW-000001

**Group ID:** `V-266254`

### Rule: The F5 BIG-IP appliance that filters traffic from the VPN access points must be configured with organization-defined filtering rules that apply to the monitoring of remote access traffic.

**Rule ID:** `SV-266254r1024572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices (such as those providing remote access to network devices and information systems) that lack automated capabilities increase risk and make remote user access management difficult at best. Remote access is access to DOD nonpublic information systems by an authorized user (or an information system) communicating through an external, nonorganization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyber attacks and also ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the VPN is terminated directly on the BIG-IP, an Access Control List can be used to filter remote VPN traffic. From the BIG-IP GUI: 1. Access. 2. Profiles/Policies. 3. Access Profiles. 4. Click "Edit" on the VPN profile. 5. Access Control Lists are assigned in an "Advanced Resource Assign" object in the Visual Policy Editor. If the VPN is terminated directly on the BIG-IP appliance configured with organization-defined filtering rules that apply to the monitoring of remote access traffic, and there is no Access Control List assigned in the Access Profile, this is a finding. If the VPN is not terminated directly on the BIG-IP and the BIG-IP filters traffic from the VPN access points: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If the BIG-IP appliance filters traffic from the VPN access points and there are no rules configured with organization-defined filtering rules that apply to the monitoring of remote access traffic, this is a finding.

## Group: SRG-NET-000019-FW-000003

**Group ID:** `V-266255`

### Rule: The F5 BIG-IP appliance must be configured to use filters that use packet headers and packet attributes, including source and destination IP addresses and ports, to prevent the flow of unauthorized or suspicious traffic between interconnected networks with different security policies, including perimeter firewalls and server VLANs.

**Rule ID:** `SV-266255r1024867_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. The firewall that filters traffic outbound to interconnected networks with different security policies must be configured with filters (e.g., rules, access control lists [ACLs], screens, and policies) that permit, restrict, or block traffic based on organization-defined traffic authorizations. Filtering must include packet header and packet attribute information, such as IP addresses and port numbers. Configure filters to perform certain actions when packets match specified attributes, including the following actions: - Apply a policy. - Accept, reject, or discard the packets. - Classify the packets based on their source address. - Evaluate the next term in the filter. - Increment a packet counter. - Set the packets' loss priority. - Specify an IPsec SA (if IPsec is used in the implementation). - Specify the forwarding path. - Write an alert or message to the system log.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules in the policy do not use packet headers and packet attributes, including source and destination IP addresses and ports, this is a finding.

## Group: F5BI-FW-300005

**Group ID:** `V-266256`

### Rule: The F5 BIG-IP appliance must generate traffic log entries containing information to establish the details of the event, including success or failure of the application of the firewall rule.

**Rule ID:** `SV-266256r1024869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit event content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the network element logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. Satisfies: SRG-NET-000074-FW-000009, SRG-NET-000075-FW-000010, SRG-NET-000076-FW-000011, SRG-NET-000077-FW-000012, SRG-NET-000078-FW-000013, SRG-NET-000492-FW-000006, SRG-NET-000493-FW-000007, SRG-NET-000333-FW-000014</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Event Logs. 3. Logging Profiles. 4. Edit the global-network profile. 5. Network Firewall tab. 6. Select a Log Publisher to use (for production environments, use Remote High Speed Logging). 7. Verify at least the "Accept", "Drop", and "Reject" Log Rule Matches boxes are checked, along with any other settings to be enabled. From the BIG-IP Console, type the following commands: tmsh list security log profile global-network Note: Verify the log-acl-match-accept, log-acl-match-drop, and log-acl-match-reject settings are enabled. If the BIG-IP is not configured to generate traffic log entries containing information to establish the details of the event, including success or failure of the application of the firewall rule, this is a finding.

## Group: SRG-NET-000089-FW-000019

**Group ID:** `V-266257`

### Rule: In the event that communication with the central audit server is lost, the F5 BIG-IP appliance must continue to queue traffic log records locally.

**Rule ID:** `SV-266257r1024871_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical that when the network element is at risk of failing to process traffic logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. In accordance with DOD policy, the traffic log must be sent to a central audit server. When logging functions are lost, system processing cannot be shut down because firewall availability is an overriding concern given the role of the firewall in the enterprise. The system must either be configured to log events to an alternative server or queue log records locally. Upon restoration of the connection to the central audit server, action must be taken to synchronize the local log data with the central audit server. If the central audit server uses UDP communications instead of a connection oriented protocol such as TCP, a method for detecting a lost connection must be implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If using Remote High Speed Logging (recommended): From the BIG-IP GUI: 1. Local Traffic. 2. Pools. 3. Pool List. 4. <Logging Pool Name> 5. Verify that "Enable Request Queueing" is set to "Yes". From the BIG-IP Console, type the following commands: tmsh list ltm pool <Logging Pool Name> queue-on-connection-limit Note: Verify this is enabled. If the BIG-IP appliance is not configured to queue traffic log records locally in the event that communication with the central audit server is lost, this is a finding.

## Group: SRG-NET-000098-FW-000021

**Group ID:** `V-266258`

### Rule: The F5 BIG-IP appliance must be configured to use TCP when sending log records to the central audit server.

**Rule ID:** `SV-266258r1024873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the default UDP protocol is used for communication between the hosts and devices to the central log server, then log records that do not reach the log server are not detected as a data loss. The use of TCP to transport log records to the log servers improves delivery reliability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. System. 2. Logs. 3. Configuration. 4. Log Destinations. 5. <Name>. 6. Verify "Protocol" is set to TCP. From the BIG-IP Console, type the following command(s): tmsh list sys log-config destination remote-high-speed-log <Name> protocol Note: Verify this is set to "tcp". If the BIG-IP appliance is not configured to use TCP when sending log records to the central audit server, this is a finding.

## Group: SRG-NET-000364-FW-000042

**Group ID:** `V-266259`

### Rule: The F5 BIG-IP appliance must be configured to restrict itself from accepting outbound packets that contain an illegitimate address in the source address field via an egress filter or by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-266259r1024876_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyber attacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Distributed denial-of-service (DDoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that in turn will then send return traffic to the hosts with the IP addresses that were forged. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet; thereby mitigating IP source address spoofing. F5 BIG-IP AFM Source checking: When source checking is enabled, the BIG-IP system verifies that the return path for an initial packet is through the same VLAN from which the packet originated. Note that the system only enables source checking if the global setting Auto Last Hop is disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Network. 2. VLANs. 3. VLAN List. 4. <Name> of internal VLAN. 5. Verify that "Source Check" is enabled. 6. Verify that Auto Last Hop is set to "Disabled". From the BIG-IP Console, type the following command(s): tmsh list net vlan <Name> auto-lasthop tmsh list net vlan <Name> source-checking If the BIG-IP appliance is not configured to disable Auto Last Hop, this is a finding.

## Group: SRG-NET-000362-FW-000028

**Group ID:** `V-266260`

### Rule: The F5 BIG-IP appliance must employ filters that prevent or limit the effects of all types of commonly known denial-of-service (DoS) attacks, including flooding, packet sweeps, and unauthorized port scanning.

**Rule ID:** `SV-266260r1024878_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Not configuring a key boundary security protection device such as the firewall against commonly known attacks is an immediate threat to the protected enclave because they are easily implemented by those with little skill. Directions for the attack can be obtained on the internet and in hacker groups. Without filtering enabled for these attacks, the firewall will allow these attacks beyond the protected boundary. Configure the perimeter and internal boundary firewall to guard against the three general methods of well-known DoS attacks: flooding attacks, protocol sweeping attacks, and unauthorized port scanning. Flood attacks occur when the host receives too much traffic to buffer and slows down or crashes. Popular flood attacks include ICMP flood and SYN flood. A TCP flood attack of SYN packets initiating connection requests can overwhelm the device until it can no longer process legitimate connection requests, resulting in denial of service. An ICMP flood can overload the device with so many echo requests (ping requests) that it expends all its resources responding and can no longer process valid network traffic, also resulting in denial of service. An attacker might use session table floods and SYN-ACK-ACK proxy floods to fill up the session table of a host. In an IP address sweep attack, an attacker sends ICMP echo requests (pings) to multiple destination addresses. If a target host replies, the reply reveals the target’s IP address to the attacker. In a TCP sweep attack, an attacker sends TCP SYN packets to the target device as part of the TCP handshake. If the device responds to those packets, the attacker receives an indication that a port in the target device is open, which makes the port vulnerable to attack. In a UDP sweep attack, an attacker sends UDP packets to the target device. If the device responds to those packets, the attacker receives an indication that a port in the target device is open, which makes the port vulnerable to attack. In a port scanning attack, an unauthorized application is used to scan the host devices for available services and open ports for subsequent use in an attack. This type of scanning can be used as a DoS attack when the probing packets are sent excessively. Satisfies: SRG-NET-000362-FW-000028, SRG-NET-000364-FW-000041, SRG-NET-000192-FW-000029, SRG-NET-000193-FW-000030</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. DoS Protection. 3. Device Protection. 4. Expand each of the applicable families (Network, DNS, SIP) depending on the traffic being handled by the BIG-IP and verify the "State" is set to "Mitigate" for all signatures in that family. If the BIG-IP appliance is not configured to block outbound traffic containing denial-of-service DoS attacks, this is a finding.

## Group: SRG-NET-000202-FW-000039

**Group ID:** `V-266261`

### Rule: The F5 BIG-IP appliance must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

**Rule ID:** `SV-266261r1024579_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To prevent malicious or accidental leakage of traffic, organizations must implement a deny-by-default security posture at the network perimeter. Such rulesets prevent many malicious exploits or accidental leakage by restricting the traffic to only known sources and only those ports, protocols, or services that are permitted and operationally necessary. As a managed boundary interface, the firewall must block all inbound and outbound network traffic unless a filter is installed to explicitly allow it. The allow filters must comply with the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and Vulnerability Assessment (VA).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Options. 3. Network Firewall. 4. Firewall Options. 5. Verify "Virtual Server & Self IP Contexts" is set to "Drop" or "Reject". 6. Verify "Global Context" is set to "Drop" or "Reject". If the BIG-IP appliance is not configured to deny network communications traffic by default and allow network communications traffic by exception, this is a finding.

## Group: SRG-NET-000392-FW-000042

**Group ID:** `V-266262`

### Rule: The F5 BIG-IP appliance must generate an alert that can be forwarded to, at a minimum, the information system security officer (ISSO) and information system security manager (ISSM) when denial-of-service (DoS) incidents are detected.

**Rule ID:** `SV-266262r1024580_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The firewall generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs), which require real-time alerts. These messages must include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DOD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The firewall must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Event Logs. 3. Logging Profiles. 4. Edit the global-network profile. 5. DoS Protection tab. 6. Verify the "Publisher" for each DoS type is configured to use a remote log destination (for production environments, use Remote High Speed Logging). From the BIG-IP Console, type the following commands: tmsh list security log profile global-network | grep dos Verify each DoS publisher is configured to use a remote log destination. If the BIG-IP is not configured to generate an alert when DoS incidents are detected, this is a finding.

## Group: SRG-NET-000364-FW-000040

**Group ID:** `V-266263`

### Rule: The F5 BIG-IP appliance must be configured to inspect all inbound and outbound traffic at the application layer.

**Rule ID:** `SV-266263r1024879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application inspection enables the firewall to control traffic based on different parameters that exist within the packets such as enforcing application-specific message and field length. Inspection provides improved protection against application-based attacks by restricting the types of commands allowed for the applications. Application inspection all enforces conformance against published RFCs. Some applications embed an IP address in the packet that needs to match the source address that is normally translated when it goes through the firewall. Enabling application inspection for a service that embeds IP addresses, the firewall translates embedded addresses and updates any checksum or other fields that are affected by the translation. Enabling application inspection for a service that uses dynamically assigned ports, the firewall monitors sessions to identify the dynamic port assignments and permits data exchange on these ports for the duration of the specific session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules in the policy do not use packet headers and packet attributes, including source and destination IP addresses and ports to inspect all inbound and outbound traffic at the application layer, this is a finding.

## Group: SRG-NET-000364-FW-000031

**Group ID:** `V-266264`

### Rule: The F5 BIG-IP appliance must be configured to filter inbound traffic on all external interfaces.

**Rule ID:** `SV-266264r1024582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic to the trusted networks may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Firewall filters control the flow of network traffic, ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet) must be kept separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules in the policy do not filter inbound traffic on all active external interfaces, this is a finding.

## Group: SRG-NET-000364-FW-000032

**Group ID:** `V-266265`

### Rule: The F5 BIG-IP appliance must be configured to filter outbound traffic on all internal interfaces.

**Rule ID:** `SV-266265r1024583_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not filtered, hostile activity intended to harm other networks or packets from networks destined to unauthorized networks may not be detected and prevented. Access control policies and access control lists implemented on devices, such as firewalls, that control the flow of network traffic ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet) must be kept separated. This requirement addresses the binding of the egress filter to the interface/zone rather than the content of the egress filter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules in the policy do not filter outbound traffic on all internal interface, this is a finding.

## Group: SRG-NET-000364-FW-000035

**Group ID:** `V-266266`

### Rule: The F5 BIG-IP appliance must be configured to block all outbound management traffic.

**Rule ID:** `SV-266266r1024584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The management network must still have its own subnet to enforce control and access boundaries provided by Layer 3 network nodes such as routers and firewalls. Management traffic between the managed network elements and the management network is routed via the same links and nodes as that used for production or operational traffic. Safeguards must be implemented to ensure that the management traffic does not leak past the managed network's premise equipment. If a firewall is located behind the premise router, all management traffic must be blocked at that point, with the exception of management traffic destined to premise equipment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules in the policy do not block all outbound management traffic, this is a finding.

## Group: SRG-NET-000205-FW-000040

**Group ID:** `V-266267`

### Rule: The BIG-IP appliance perimeter firewall must be configured to filter traffic destined to the enclave in accordance with the specific traffic that is approved and registered in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and vulnerability assessments.

**Rule ID:** `SV-266267r1024585_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The enclave's internal network contains the servers where mission-critical data and applications reside. Malicious traffic can enter from an external boundary or originate from a compromised host internally. Vulnerability assessments must be reviewed by the system administrator (SA) and protocols must be approved by the IA staff before entering the enclave. Firewall filters (e.g., rules, access control lists [ACLs], screens, and policies) are the first line of defense in a layered security approach. They permit authorized packets and deny unauthorized packets based on port or service type. They enhance the posture of the network by not allowing packets to even reach a potential target within the security domain. The filters provided are highly susceptible ports and services that must be blocked or limited as much as possible without adversely affecting customer requirements. Auditing packets attempting to penetrate the network but stopped by the firewall filters will allow network administrators to broaden their protective ring and more tightly define the scope of operation. If the perimeter is in a Deny-by-Default posture and what is allowed through the filter is in accordance with the PPSM CAL and VAs for the enclave, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to the database being blocked would be satisfied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the BIG-IP GUI: 1. Security. 2. Network Firewall. 3. Policies. 4. <Policy Name> If configured rules are not configured to only allow inbound traffic in accordance with the PPSM CAL, this is a finding.

