# STIG Benchmark: VMware NSX 4.x Tier-1 Gateway Router Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-RTR-000007

**Group ID:** `V-265518`

### Rule: The NSX Tier-1 Gateway router must be configured to have all inactive interfaces removed.

**Rule ID:** `SV-265518r999924_rule`
**Severity:** high

**Description:**
<VulnDiscussion>An inactive interface is rarely monitored or controlled and may expose a network to an undetected attack on that interface. Unauthorized personnel with access to the communication facility could gain access to a router by connecting to a configured interface that is not in use. If an interface is no longer used, the configuration must be deleted and the interface disabled. For sub-interfaces, delete sub-interfaces that are on inactive interfaces and delete sub-interfaces that are themselves inactive. If the sub-interface is no longer necessary for authorized communications, it must be deleted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-1 Gateways. For every Tier-1 Gateway, expand the Tier-1 Gateway. Click on the number in the Linked Segments to review the currently linked segments. For every Tier-1 Gateway, expand the Tier-1 Gateway. Expand Interfaces and GRE Tunnels, and click on the number of interfaces present to open the interfaces dialog. Review each interface or linked segment present to determine if they are not in use or inactive. If there are any linked segments or service interfaces present on a Tier-1 Gateway that are not in use or inactive, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-265529`

### Rule: The NSX Tier-1 Gateway router must be configured to have the DHCP service disabled if not in use.

**Rule ID:** `SV-265529r999926_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-1 Gateways. For every Tier-1 Gateway expand the Tier-1 Gateway to view the DHCP configuration. If a DHCP profile is configured and not in use, this is a finding.

## Group: SRG-NET-000512-RTR-000012

**Group ID:** `V-265604`

### Rule: The NSX Tier-1 Gateway router must be configured to advertise a hop limit of at least 32 in Router Advertisement messages for IPv6 stateless auto-configuration deployments.

**Rule ID:** `SV-265604r995285_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Neighbor Discovery protocol allows a hop limit value to be advertised by routers in a Router Advertisement message being used by hosts instead of the standardized default value. If a very small value was configured and advertised to hosts on the LAN segment, communications would fail due to the hop limit reaching zero before the packets sent by a host reached its destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If IPv6 forwarding is not enabled, this is Not Applicable. From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-1 Gateways. For every Tier-1 Gateway, expand Tier-1 Gateway >>Additional Settings. Click on the ND profile name to view the hop limit. If the hop limit is not configured to at least 32, this is a finding.

## Group: SRG-NET-000131-RTR-000035

**Group ID:** `V-265608`

### Rule: The NSX Tier-1 Gateway router must be configured to have multicast disabled if not in use.

**Rule ID:** `SV-265608r999927_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A compromised router introduces risk to the entire network infrastructure, as well as data resources that are accessible via the network. The perimeter defense has no oversight or control of attacks by malicious users within the network. Preventing network breaches from within is dependent on implementing a comprehensive defense-in-depth strategy, including securing each device connected to the network. This is accomplished by following and implementing all security guidance applicable for each node type. A fundamental step in securing each router is to enable only the capabilities required for operation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Networking >> Connectivity >> Tier-1 Gateways. For every Tier-1 Gateway, expand the Tier-1 Gateway then expand Multicast to view the Multicast configuration. If Multicast is enabled and not in use, this is a finding. If a Tier-1 Gateway is not linked to a Tier-0 Gateway, this is Not Applicable.

