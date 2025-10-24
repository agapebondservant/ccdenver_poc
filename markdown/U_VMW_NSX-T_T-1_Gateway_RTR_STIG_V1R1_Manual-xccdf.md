# STIG Benchmark: VMware NSX-T Tier 1 Gateway RTR Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-251770`

### Rule: The NSX-T Tier-1 Gateway must be configured to have all inactive interfaces removed.

**Rule ID:** `SV-251770r810210_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. If an interface is no longer used, the configuration must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-1 Gateways. For every Tier-1 Gateway, expand the Tier-1 Gateway. Click on the number in the Linked Segments to review the currently linked segments. For every Tier-1 Gateway, expand the Tier-1 Gateway. Expand Service Interfaces, then click on the number to review the Service Interfaces. Review each interface or linked segment present to determine if they are not in use or inactive. If there are any linked segments or service interfaces present on a Tier-1 Gateway that are not in use or inactive, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-251771`

### Rule: The NSX-T Tier-1 Gateway must be configured to have the DHCP service disabled if not in use.

**Rule ID:** `SV-251771r810213_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-1 Gateways. For every Tier-1 Gateway expand the Tier-1 Gateway to view the DHCP configuration. If a DHCP profile is configured and not in use, this is a finding.

## Group: SRG-NET-000193-RTR-000112

**Group ID:** `V-251772`

### Rule: The NSX-T Tier-1 Gateway must be configured to enforce a Quality-of-Service (QoS) policy to limit the effects of packet flooding denial-of-service (DoS) attacks.

**Rule ID:** `SV-251772r810216_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. Packet flooding distributed denial-of-service (DDoS) attacks are referred to as volumetric attacks and have the objective of overloading a network or circuit to deny or seriously degrade performance, which denies access to the services that normally traverse the network or circuit. Volumetric attacks have become relatively easy to launch using readily available tools such as Low Orbit Ion Cannon or botnets. Measures to mitigate the effects of a successful volumetric attack must be taken to ensure that sufficient capacity is available for mission-critical traffic. Managing capacity may include, for example, establishing selected network usage priorities or quotas and enforcing them using rate limiting, Quality of Service (QoS), or other resource reservation control methods. These measures may also mitigate the effects of sudden decreases in network capacity that are the result of accidental or intentional physical damage to telecommunications facilities (such as cable cuts or weather-related outages).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Segments. For every Segment connected to a Tier-1 Gateway, Expand Segment >> Expand Segment Profiles >> Record QOS Segment Profile. Go to Segment Profiles >> Expand QOS Segment Profile recorded in previous steps. If there are traffic priorities specified by the Combatant Commands/Services/Agencies needed to ensure sufficient capacity for mission-critical traffic and none are configured, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-251773`

### Rule: The NSX-T Tier-1 Gateway must be configured to have multicast disabled if not in use.

**Rule ID:** `SV-251773r810219_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to Networking >> Tier-1 Gateways. For every Tier-1 Gateway, expand the Tier-1 Gateway then expand Multicast to view the Multicast configuration. If Multicast is enabled and not in use, this is a finding.

