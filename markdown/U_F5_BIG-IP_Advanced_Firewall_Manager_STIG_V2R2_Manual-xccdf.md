# STIG Benchmark: F5 BIG-IP Advanced Firewall Manager Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-ALG-000017

**Group ID:** `V-214498`

### Rule: The BIG-IP AFM module must be configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-214498r395865_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network. The flow of all network traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Information flow control policies and enforcement mechanisms are commonly employed by organizations to control the flow of information between designated sources and destinations (e.g., networks, individuals, devices) within information systems. Examples of information flow control restrictions include keeping export-controlled information from being transmitted in the clear to the Internet or blocking information marked as classified but being transported to an unapproved destination. Application Layer Gateways (ALGs) enforce approved authorizations by employing security policy and/or rules that restrict information system services, provide packet filtering capability based on header or protocol information and/or message filtering capability based on data content (e.g., implementing key word searches or using document characteristics).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP AFM module is not used to support user access control intermediary services for virtual servers, this is not applicable. Verify the BIG-IP AFM module is configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. Navigate to the BIG-IP System manager >> Security >> Network Firewall >> Active Rules. Verify an active rule is configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. If the BIG-IP AFM module is not configured to enforce approved authorizations for controlling the flow of information within the network based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic, this is a finding.

## Group: SRG-NET-000019-ALG-000018

**Group ID:** `V-214499`

### Rule: The BIG-IP AFM module must be configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-214499r395868_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. This requirement applies to the flow of information between the Application Layer Gateway (ALG) when used as a gateway or boundary device which allows traffic flow between interconnected networks of differing security policies. The ALG installed and configured in such a way that restricts or blocks information flows based on guidance in the Ports, Protocols, & Services (PPSM) regarding restrictions for boundary crossing for ports, protocols, and services. Information flow restrictions may be implemented based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. The ALGs must be configured with policy filters (e.g., security policy, rules, and/or signatures) that restrict or block information system services; provide a packet filtering capability based on header information; and/or perform message filtering based on message content. The policy filters used depend upon the type of application gateway (e.g., web, email, or TLS).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP AFM module is not used to support user access control intermediary services for virtual servers, this is not applicable. Verify the BIG-IP AFM module is configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. Navigate to the BIG-IP System manager >> Security >> Network Firewall >> Active Rules. Verify an active rule is configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. If the BIG-IP AFM module is not configured to restrict or block harmful or suspicious communications traffic by controlling the flow of information between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic, this is a finding.

## Group: SRG-NET-000074-ALG-000043

**Group ID:** `V-214500`

### Rule: The BIG-IP AFM module must be configured to produce audit records containing information to establish what type of events occurred.

**Rule ID:** `SV-214500r395919_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit record content that may be necessary to satisfy this requirement includes, for example, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the gateway logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element. This requirement does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP AFM module is configured to produce audit records containing information to establish what type of events occurred. Navigate to the BIG-IP System manager >> Security >> Event Logs >> Logging Profiles. Verify list of Profiles 'Enabled' for 'Network Firewall'. If the BIG-IP AFM module does not produce audit records containing information to establish what type of events occurred, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-214501`

### Rule: The BIG-IP AFM module must be configured to only allow incoming communications from authorized sources routed to authorized destinations.

**Rule ID:** `SV-214501r831450_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Access control policies and access control lists implemented on devices that control the flow of network traffic (e.g., application-level firewalls and Web content filters) ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the Internet or CDS) must be kept separate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the BIG-IP AFM module is not used to support user access control intermediary services for virtual servers, this is not applicable. Verify the BIG-IP AFM module is configured to only allow incoming communications from authorized sources routed to authorized destinations. Navigate to the BIG-IP System manager >> Local Traffic >> Virtual Servers >> Virtual Servers List tab. Select the applicable Virtual Servers(s) from the list to verify. Navigate to the Security >> Policies tab. Verify that "Network Firewall" is assigned a local Network Firewall Policy. Verify configuration of the identified Network Firewall policy: Navigate to the BIG-IP System manager >> Security >> Network Firewall >> Active Rules. Select the Network Firewall policy that was assigned to the Virtual Server. Review the configuration of the "Protocol", "Source", "Destination", and "Action" sections at a minimum to ensure that the policy is only allowing incoming communications from authorized sources enroute to authorized destinations. If the BIG-IP AFM module is not configured to only allow incoming communications from unauthorized sources routed to unauthorized destinations, this is a finding.

## Group: SRG-NET-000380-ALG-000128

**Group ID:** `V-214502`

### Rule: The BIG-IP AFM module must be configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives.

**Rule ID:** `SV-214502r831451_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A common vulnerability of network elements is unpredictable behavior when invalid inputs are received. This requirement guards against adverse or unintended system behavior caused by invalid inputs where information system responses to the invalid input may be disruptive or cause the system to fail into an unsafe state. The behavior will be derived from the organizational and system requirements and includes, but is not limited to, notification of the appropriate personnel, creating an audit record, and rejecting invalid input. This requirement applies to gateways and firewalls that perform content inspection or have higher layer proxy functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the BIG-IP AFM module is configured to handle invalid input in a predictable and documented manner that reflects organizational and system objectives. This can be demonstrated by the SA sending an invalid input to a virtual server. Provide evidence that the virtual server was able to handle the invalid input and maintain operation. If the BIG-IP AFM module is not configured to handle invalid inputs in a predictable and documented manner that reflects organizational and system objectives, this is a finding.

## Group: SRG-NET-000512-ALG-000062

**Group ID:** `V-270900`

### Rule: The version of F5 BIG-IP must be a supported version.

**Rule ID:** `SV-270900r1056144_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions that are used to install patches across the enclave and to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means that the period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified period from the availability of the update. The specific period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
BIG-IP versions supported by this STIG (version 15.1x and earlier) are no longer supported by the vendor. If the system is running BIG-IP version 15.1x or earlier, this is a finding.

