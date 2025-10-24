# STIG Benchmark: VMware NSX Distributed Logical Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-69127`

### Rule: The NSX Distributed Logical Router must be configured so inactive router interfaces are disabled.

**Rule ID:** `SV-83731r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify there are no inactive router interfaces enabled. Log onto vSphere Web Client with credentials authorized for administration. Navigate and select Networking and Security >> "NSX Edges" tab on the left-side menu. Double-click the EdgeID. Click on the "Manage" tab on the top of the new screen, then Settings on the far left >> Interfaces >> Check the "Status" column for the associated interface. If any inactive router interfaces are not disabled, this is a finding.

## Group: SRG-NET-000025-RTR-000020

**Group ID:** `V-69129`

### Rule: The NSX Distributed Logical Router must enable neighbor router authentication for control plane protocols.

**Rule ID:** `SV-83733r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A rogue router could send a fictitious routing update to convince a site's perimeter router to send traffic to an incorrect or even a rogue destination. This diverted traffic could be analyzed to learn confidential information about the site's network, or merely used to disrupt the network's ability to communicate with other networks. This is known as a "traffic attraction attack" and is prevented by configuring neighbor router authentication for routing updates. This requirement applies to all IPv4 and IPv6 protocols that are used to exchange routing or packet forwarding information; this includes all Interior Gateway Protocols (such as OSPF, EIGRP, and IS-IS) and Exterior Gateway Protocols (such as BGP), MPLS-related protocols (such as LDP), and Multicast-related protocols.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify for OSPF that Authentication is not set to "None" and for BGP password has been configured. Log onto vSphere Web Client with credentials authorized for administration. Navigate and select Networking and Security >> select the "NSX Edges" tab on the left-side menu. Double-click the edgeID in question, as denoted by the "Logical Router" type. Select the "Manage" tab on the top of the new screen >> Routing. If OSPF is configured, select OSPF >> Area Definitions. Select the configured areas. Click the "pencil" icon. Verify "authentication" is set to something other than "none". If Authentication is set to "None", this is a finding. If BGP is configured, select BGP >> Neighbors >> select the configured neighbor >> Click the "pencil" icon >> verify "password" is configured. If a password has not been configured for BGP, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-69133`

### Rule: The NSX Distributed Logical Router must be configured to disable non-essential capabilities.

**Rule ID:** `SV-83737r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify only necessary services are enabled. Log onto vSphere Web Client with credentials authorized for administration. Navigate and select Networking and Security >> select the "NSX Edges" tab on the left-side menu. Double-click the Edge ID. Navigate to Manage >> Verify the configurations under "Settings, Firewall, Routing, Bridging, and DHCP Relay" are enabled only as necessary to the deployment. If unnecessary services are enabled, this is a finding.

## Group: SRG-NET-000193-RTR-000111

**Group ID:** `V-69135`

### Rule: The NSX Distributed Logical Router must manage excess bandwidth to limit the effects of packet flooding types of denial of service (DoS) attacks.

**Rule ID:** `SV-83739r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Denial of service is a condition when a resource is not available for legitimate users. Packet flooding DDoS attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or by botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the traffic shaping policies are properly configured to manage excess bandwidth. Log into vSphere Web Client with credentials authorized for administration navigate and select Networking >> select the respective VDS under the appropriate datacenter >> Click the dropdown to expand the list of portgroups >> select the appropriate portgroup for your network. Navigate to >> Manage >> Settings >> Properties >> Edit >> Traffic Shaping Verify the necessary values are configured to reserve bandwidth for applications in the event of bandwidth congestion. Navigate to >> Manage >> Settings >> Properties >> Edit >> Traffic filtering and marking >> Verify the necessary values for DSCP are configured to mark bandwidth for applications in the event of a DoS attack. Select checkbox for "DSCP value: Update DSCP tag" >> enter in a number between 0 and 63. Select "+" symbol under Traffic qualifiers with "New System Traffic Qualifier" and select System traffic type >> "OK". Select "OK" to accept new Network Traffic Rule. If the traffic shaping and QoS policies are not properly configured to manage excess bandwidth and to reserve bandwidth for critical applications in the event of bandwidth congestion, this is a finding.

