# STIG Benchmark: VMware NSX 4.x Tier-1 Gateway Firewall Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000074-FW-000009

**Group ID:** `V-265488`

### Rule: The NSX Tier-1 Gateway firewall must generate traffic log entries.

**Rule ID:** `SV-265488r994833_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit event content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the network element logs provides a means of investigating an attack, recognizing resource usage or capacity thresholds, or identifying an improperly configured network element. Satisfies: SRG-NET-000074-FW-000009, SRG-NET-000061-FW-000001, SRG-NET-000075-FW-000010, SRG-NET-000076-FW-000011, SRG-NET-000077-FW-000012, SRG-NET-000078-FW-000013, SRG-NET-000492-FW-000006, SRG-NET-000493-FW-000007</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules. For each Tier-1 Gateway and for each rule, click the gear icon and verify the logging setting. If logging is not "Enabled", this is a finding.

## Group: SRG-NET-000193-FW-000030

**Group ID:** `V-265493`

### Rule: The NSX Tier-1 Gateway firewall must manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-265493r994848_rule`
**Severity:** high

**Description:**
<VulnDiscussion>A firewall experiencing a DoS attack will not be able to handle production traffic load. The high usage and CPU caused by a DoS attack will also have an effect on control keep-alives and timers used for neighbor peering resulting in route flapping and will eventually black hole production traffic. The device must be configured to contain and limit a DoS attack's effect on the device's resource usage. The use of redundant components and load balancing are examples of mitigating "flood-type" DoS attacks through increased capacity. Satisfies: SRG-NET-000193-FW-000030, SRG-NET-000192-FW-000029, SRG-NET-000362-FW-000028</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Security >> Settings >> General Settings >> Firewall >> Flood Protection to view Flood Protection profiles. If there are no Flood Protection profiles of type "Gateway", this is a finding. For each gateway flood protection profile, if TCP Half Open Connection limit, UDP Active Flow Limit, ICMP Active Flow Limit, and Other Active Connection Limit are set to "None", this is a finding. For each gateway flood protection profile, examine the "Applied To" field to view the Tier-1 Gateways to which it is applied. If a gateway flood protection profile is not applied to all Tier-1 Gateways through one or more policies, this is a finding.

## Group: SRG-NET-000202-FW-000039

**Group ID:** `V-265494`

### Rule: The NSX Tier-1 Gateway firewall must deny network communications traffic by default and allow network communications traffic by exception.

**Rule ID:** `SV-265494r994851_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To prevent malicious or accidental leakage of traffic, organizations must implement a deny-by-default security posture at the network perimeter. Such rulesets prevent many malicious exploits or accidental leakage by restricting the traffic to only known sources and only those ports, protocols, or services that are permitted and operationally necessary. As a managed boundary interface, the firewall must block all inbound and outbound network traffic unless a filter is installed to explicitly allow it. The allow filters must comply with the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL) and Vulnerability Assessment (VA). Satisfies: SRG-NET-000202-FW-000039, SRG-NET-000205-FW-000040, SRG-NET-000235-FW-000133, SRG-NET-000364-FW-000031, SRG-NET-000364-FW-000032</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules >> Choose each Tier-1 Gateway in drop-down >> Policy_Default_Infra Section >> Action. If the default_rule is set to Allow, this is a finding.

## Group: SRG-NET-000333-FW-000014

**Group ID:** `V-265496`

### Rule: The NSX Tier-1 Gateway firewall must be configured to send traffic log entries to a central audit server.

**Rule ID:** `SV-265496r994857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the traffic log entries, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The DOD requires centralized management of all network component audit record content. Network components requiring centralized traffic log management must have the ability to support centralized management. The content captured in traffic log entries must be managed from a central location (necessitating automation). Centralized management of traffic log records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Ensure at least one syslog server is configured on the firewall. If the product inherently has the ability to store log records locally, the local log must also be secured. However, this requirement is not met since it calls for a use of a central audit server. Satisfies: SRG-NET-000333-FW-000014, SRG-NET-000098-FW-000021</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From an NSX Edge Node shell hosting the Tier-1 Gateway, run the following command: > get logging-servers Note: This check must be run from each NSX Edge Node hosting a Tier-1 Gateway, as they are configured individually. or If Node Profiles are used, from the NSX Manager web interface, go to System >> Configuration >> Fabric >> Profiles >> Node Profiles. Click "All NSX Nodes" and verify the syslog servers listed. If any configured logging servers are configured with a protocol of "udp", this is a finding. If any configured logging servers are not configured with a level of "info", this is a finding. If no logging-servers are configured, this is a finding.

## Group: SRG-NET-000364-FW-000040

**Group ID:** `V-265500`

### Rule: The NSX Tier-1 Gateway firewall must be configured to inspect traffic at the application layer.

**Rule ID:** `SV-265500r994869_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application inspection enables the firewall to control traffic based on different parameters that exist within the packets such as enforcing application-specific message and field length. Inspection provides improved protection against application-based attacks by restricting the types of commands allowed for the applications. Application inspection all enforces conformance against published RFCs. Some applications embed an IP address in the packet that needs to match the source address that is normally translated when it goes through the firewall. Enabling application inspection for a service that embeds IP addresses, the firewall translates embedded addresses and updates any checksum or other fields that are affected by the translation. Enabling application inspection for a service that uses dynamically assigned ports, the firewall monitors sessions to identify the dynamic port assignments, and permits data exchange on these ports for the duration of the specific session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX Manager web interface, go to Security >> Policy Management >> Gateway Firewall >> Gateway Specific Rules. For each Tier-1 Gateway, review rules that do not have a Context Profile assigned. For example, if a rule exists to allow SSH by service or custom port then it should have the associated SSH Context Profile applied. If any rules with services defined have an associated suitable Context Profile but do not have one applied, this is a finding.

