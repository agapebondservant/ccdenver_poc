# STIG Benchmark: SDN Using NV Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: NET-SDN-001

**Group ID:** `V-73073`

### Rule: Southbound API control plane traffic between the SDN controller and SDN-enabled network elements must be mutually authenticated using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-87725r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Southbound APIs such as OpenFlow provide the forwarding tables to network devices such as switches and routers, both physical and virtual (hypervisor-based). The SDN controllers use the concept of flows to identify network traffic based on predefined rules that can be statically or dynamically programmed by the SDN control software, thereby determining how traffic should flow through network devices based on usage patterns, applications, and policy that can optimize traffic paths based on business requirements and not network infrastructure design. If an SDN-aware router or switch received erroneous forwarding information from a rogue controller, traffic could be black-holed or even forwarded to a malicious user to sniff traffic and perform a man-in-the-middle attack. Hence, it is imperative that mutual authentication is enabled between the SDN controller and the SDN-aware network elements for all southbound API traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the components within the SDN framework that send and receive southbound API messages and verify that the messages are authenticated using a FIPS-approved message authentication code algorithm. FIPS-approved algorithms for authentication are the cipher-based message authentication code (CMAC) and the keyed-hash message authentication code (HMAC). AES and 3DES are NIST-approved CMAC algorithms. The following are NIST-approved HMAC algorithms: SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256. If the SDN controller or SDN-enabled network elements do not authenticate received southbound API messages using a FIPS-approved message authentication code algorithm, this is a finding.

## Group: NET-SDN-002

**Group ID:** `V-73075`

### Rule: Northbound API traffic received by the SDN controller must be authenticated using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-87727r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SDN controller determines how traffic should flow through physical and virtual network devices based on application profiles, network infrastructure resources, security policies, and business requirements that it receives via the northbound API. It also receives network service requests from orchestration and management systems to deploy and configure network elements via this API. In turn, the northbound API presents a network abstraction to these orchestration and management systems. If attackers could leverage a vulnerable northbound API, they would have control over the SDN infrastructure through the controller by inserting polices. If the SDN controller were to receive fictitious information from a rogue application or orchestration system, non-optimized network paths would be produced that could disrupt network operations, resulting in inefficient application and business processes. Hence, it is imperative that all northbound API traffic received by the SDN controller is authenticated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration of the SDN controllers and verify that the northbound API messages received are authenticated using a FIPS-approved message authentication code algorithm. FIPS-approved algorithms for authentication are the cipher-based message authentication code (CMAC) and the keyed-hash message authentication code (HMAC). AES and 3DES are NIST-approved CMAC algorithms. The following are NIST-approved HMAC algorithms: SHA-1, SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, and SHA-512/256. If the SDN controllers do not authenticate received northbound API messages using a FIPS-approved message authentication code algorithm, this is a finding.

## Group: NET-SDN-003

**Group ID:** `V-73077`

### Rule: Access to the SDN management and orchestration systems must be authenticated using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-87729r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SDN controller receives network service requests from orchestration and management systems to deploy and configure network elements via the northbound API. In turn, the Northbound API presents a network abstraction to these systems. If either the orchestration or management system were breached, a rogue user could make modifications to the business or security policy that could disrupt network operations, resulting in inefficient application and business processes as well as bypassing security controls. In addition, invalid network service requests could be processed that could exhaust compute, storage, and network resources, leaving no resources available for legitimate business requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all management and orchestration systems within the SDN framework and verify that access to these components requires DOD PKI certificate-based authentication. If access to the SDN management and orchestration systems does not require DOD PKI certificate-based authentication, this is a finding.

## Group: NET-SDN-004

**Group ID:** `V-73079`

### Rule: Southbound API control plane traffic must traverse an out-of-band path or be encrypted using a FIPS-validated cryptographic module.

**Rule ID:** `SV-87731r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Southbound APIs such as OpenFlow provide the forwarding tables to network devices such as switches and routers, both physical and virtual (hypervisor-based). The SDN controllers use the concept of flows to identify network traffic based on predefined rules that can be statically or dynamically programmed by the SDN control software, thereby determining how traffic should flow through network devices based on usage patterns, applications, and policy that can optimize traffic paths based on business requirements and not network infrastructure design. If an SDN-aware router or switch received erroneous forwarding information from a rogue controller, traffic could be black-holed or even forwarded to a malicious user to sniff traffic and perform a man-in-the-middle attack. Hence, it is imperative to secure flow table updates by encrypting all southbound API traffic or deploying an out-of-band network for this traffic to traverse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the southbound API control plane traffic between the SDN controllers and the SDN-enabled network elements traverses an out-of-band path. If not, verify that the southbound API traffic is encrypted using a FIPS-validated cryptographic module. If the southbound API traffic does not traverse an out-of-band path or is not encrypted using a FIPS-validated cryptographic module, this is a finding. Note: An out-of-band path would be a path between two nodes that traverses one or more links on an out-of-band network; that is, a dedicated layer 2 infrastructure separate from a production network.

## Group: NET-SDN-005

**Group ID:** `V-73081`

### Rule: Northbound API traffic must traverse an out-of-band path or be encrypted using a FIPS-validated cryptographic module.

**Rule ID:** `SV-87733r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The SDN controller receives network service requests from orchestration and management systems to deploy and configure network elements via the northbound API. In turn, the northbound API presents a network abstraction to these systems. If either the orchestration or management system were breached, a rogue user could make modifications to the business or security policy that could disrupt network operations, resulting in inefficient application and business processes and bypassing security controls. In addition, invalid network service requests could be processed that could exhaust compute, storage, and network resources, leaving no resources available for legitimate business requirements. Hence, it is imperative that all southbound API traffic is secured by encrypting the traffic or deploying an out-of-band network for this traffic to traverse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the northbound API traffic between the SDN controllers and the SDN management/orchestration systems traverses an out-of-band path. If not, verify that the northbound API traffic is encrypted using a FIPS-validated cryptographic module. If the northbound API traffic does not traverse an out-of-band path or is not encrypted using a FIPS-validated cryptographic module, this is a finding. Note: An out-of-band path would be a path between two nodes that traverses one or more links on an out-of-band network; that is, a dedicated layer 2 infrastructure separate from a production network.

## Group: NET-SDN-006

**Group ID:** `V-73083`

### Rule: Southbound API management plane traffic for provisioning and configuring virtual network elements within the SDN infrastructure must be authenticated using a FIPS-approved message authentication code algorithm.

**Rule ID:** `SV-87735r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Management and orchestration systems within the SDN framework instantiate, deploy, and configure virtual network elements. These systems also define the virtual network topology by specifying the connectivity between the network elements and the workloads, both virtual and physical. If a hypervisor host within the SDN infrastructure were to receive fictitious information from a rogue management or orchestration system as a result of no authentication, the virtual network topology could be altered by deploying rogue network elements to create non-optimized network paths, resulting in inefficient application and business processes. By altering the network topology, the attacker would have the ability force traffic to bypass security controls.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that all southbound API management plane traffic is authenticated using a FIPS-approved message authentication code algorithm. Review SDN management and orchestration systems, as well as all hypervisor hosts that compose the NVP framework, to determine if a FIPS-approved message authentication code algorithm is used to ensure the authenticity and integrity of messages used to deploy and configure software-defined network elements. If southbound API management plane traffic is not authenticated using a FIPS-approved message authentication code algorithm, this is a finding.

## Group: NET-SDN-007

**Group ID:** `V-73085`

### Rule: Southbound API management plane traffic for provisioning and configuring virtual network elements within the SDN infrastructure must traverse an out-of-band path or be encrypted using a using a FIPS-validated cryptographic module.

**Rule ID:** `SV-87737r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Management and orchestration systems within the SDN framework instantiate, deploy, and configure network elements within the SDN infrastructure. These systems also define the virtual network topology by specifying the connectivity between the network elements and the workloads, both virtual and physical. If a hypervisor host within the SDN infrastructure were to receive fictitious information from a rogue management or orchestration system, the virtual network topology could be altered by deploying rogue network elements to create non-optimized network paths, resulting in inefficient application and business processes. By altering the network topology, the attacker would have the ability to force traffic to bypass security controls. Spoofed management plane traffic generated by a rogue management system could result in a denial-of-service attack on the hypervisor hosts, exhausting the computing resources and disrupting workload processing or even creating a network outage. Hence, it is imperative that all SDN management plane traffic is secured by encrypting the traffic or deploying an out-of-band network for this traffic to traverse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the southbound API management plane traffic traverses an out-of-band path. If not, verify that the southbound API management plane traffic is encrypted using a using a FIPS-validated cryptographic module. If the southbound API management plane traffic does not traverse an out-of-band path or is not encrypted using a using a FIPS-validated cryptographic module, this is a finding.

## Group: NET-SDN-008

**Group ID:** `V-73087`

### Rule: Southbound API management plane traffic for configuring SDN parameters on physical network elements must be authenticated using DOD PKI certificate-based authentication.

**Rule ID:** `SV-87739r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Physical SDN-enabled switches are dependent on the SDN controller for their forwarding tables as well as their configuration and service parameters. This information is provided to the switches via SDN management plane protocols such as Network Configuration Protocol (NETCONF) and Open vSwitch Database Management Protocol (OVSDB). The latter provides configuration support for OpenFlow-enabled switches such as Open vSwitch, as well as many vendor switches. Without authenticating management packets, physical switches within the SDN infrastructure could receive fictitious information from a rogue management system that could shut down interfaces, thereby altering the physical network topology. By altering the network topology, the attacker would have the ability to force traffic to bypass security controls. Legitimate traffic could be dropped by deploying access control lists to active interfaces. Spoofed management plane traffic generated by a rogue management system could result in a denial-of-service attack on the switches, resulting in a network outage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review both management and orchestration systems, as well as all SDN controllers and physical SDN-enabled network elements that compose the network virtualization platform (NVP), to determine if certificate-based authentication is used to ensure the authenticity and integrity of southbound API management messages. If southbound API management plane traffic is not authenticated using DOD PKI certificates, this is a finding.

## Group: NET-SDN-009

**Group ID:** `V-73089`

### Rule: Southbound API management plane traffic for configuring SDN parameters on physical network elements must be encrypted using a FIPS-validated cryptographic module.

**Rule ID:** `SV-87741r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Physical SDN-enabled switches are dependent on the SDN controller for their forwarding tables, as well as their configuration and service parameters. This information is provided to the switches via SDN management plane protocols such as Network Configuration Protocol (NETCONF) and Open vSwitch Database Management Protocol (OVSDB). The latter provides configuration support for OpenFlow-enabled switches such as Open vSwitch, as well as many vendor switches. If a switch within the SDN infrastructure were to receive fictitious information from a rogue management system, the physical network topology could be altered by shutting down interfaces. Legitimate traffic could be dropped by deploying access control lists to active interfaces. By altering the network topology, the attacker would have the ability to force traffic to bypass security controls. Spoofed management plane traffic generated by a rogue management system could result in a denial-of-service attack on the switches, resulting in a network outage. Hence, it is imperative that all SDN management plane traffic is secured by encrypting the traffic using a FIPS-validated cryptographic module.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine if the southbound API management plane traffic is encrypted using a FIPS-validated cryptographic module. If the Southbound API management plane traffic is not encrypted using a FIPS-validated cryptographic module, this is a finding.

## Group: NET-SDN-010

**Group ID:** `V-73091`

### Rule: Physical SDN controllers and servers hosting SDN applications must reside within the management network with multiple paths that are secured by a firewall to inspect all ingress traffic.

**Rule ID:** `SV-87743r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Management and orchestration systems deploy and configure network devices such as switches and routers, both physical and virtual. SDN controllers are made aware of the deployments and are able to define the network topology through abstraction. The controllers are then able to provide forwarding table information to each router or switch instance within the SDN infrastructure. If an SDN-aware router or switch received erroneous forwarding information from a rogue controller, traffic could be black-holed or even forwarded to a malicious user to sniff traffic and to perform a man-in-the-middle attack. If attackers could leverage a vulnerable northbound API, they would have control over the SDN infrastructure through the controller by creating their own polices. If the SDN controller were to receive fictitious information from a rogue application, non-optimized network paths would be produced that could disrupt network operations, resulting in inefficient application and business processes. If either the orchestration or management system were breached, invalid network service requests could be processed that could exhaust compute, storage, and network resources, leaving no resources available for legitimate business requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the SDN infrastructure topology to verify that the all physical SDN controllers, management appliances, and servers hosting SDN applications reside within the management network that has multiple paths and is also secured by a firewall. If these physical NVP components do not reside within the management network with multiple paths, and are not secured by a firewall, this is a finding. Note: If the SDN physical components reside within an out-of-band network, this requirement would not be applicable.

## Group: NET-SDN-011

**Group ID:** `V-73093`

### Rule: SDN-enabled routers and switches must provide link state information to the SDN controller to create new forwarding decisions for the network elements.

**Rule ID:** `SV-87745r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Southbound APIs such as OpenFlow provide the forwarding tables to network devices such as switches and routers. SDN controllers have an abstraction of the network topology based on discovery and provisioning information provided by management and orchestration systems. The SDN controllers use the concept of flows to identify network traffic based on predefined rules that can be statically or dynamically programmed by the SDN control software. With the network topology abstraction, they are able to determine how traffic should flow through network devices based on application data, business policy, bandwidth, and path availability. If the SDN-enabled network elements do not provide updated link state information, the SDN controller is not able to reconverge the network to verify there is reachability to all destinations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configurations for all SDN-enabled routers and switches and verify that link state information is provided to the SDN controllers. If the SDN-enabled routers and switches do not provide link state information to the SDN controllers, this is a finding. Note: This requirement is not applicable if the SDN deployment model does not rely on the controller for network forwarding or convergence.

## Group: NET-SDN-012

**Group ID:** `V-73095`

### Rule: Quality of service (QoS) must be implemented on the underlying IP network to provide preferred treatment for traffic between the SDN controllers and SDN-enabled switches and hypervisors.

**Rule ID:** `SV-87747r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>With the network topology abstraction, the SDN controllers are able to determine how traffic should flow through network devices based on application data, business policy, bandwidth, and path availability. When updated link state information is provided by the network elements, the SDN controller must recalculate the optimized paths for network reconvergence and provide the new forwarding tables to the network elements. When network congestion occurs, all traffic has an equal chance of being dropped. QoS provisioning categorizes network traffic, prioritizes it according to its relative importance, and provides preferential treatment using various priority queuing techniques. Prioritization of both link state updates and control plane traffic must be implemented to verify that during periods of severe network congestion, the network can converge.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement will not be applicable if an out-of-band network is used to transport SDN control and management plane traffic. Review the router and multilayer switch configurations to verify that SDN control and management plane packets are receiving the appropriate amount of priority to ensure this traffic has preference over normal production traffic. If not all routers and multilayer switches impose preferred treatment for SDN control and management plane traffic during periods of congestion, this is a finding.

## Group: NET-SDN-013

**Group ID:** `V-73097`

### Rule: SDN controllers must be deployed as clusters and on separate physical hosts to eliminate single point of failure.

**Rule ID:** `SV-87749r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SDN relies heavily on control messages between a controller and the forwarding devices for network convergence. The controller uses node and link state discovery information to calculate and determine optimum pathing within the SDN network infrastructure based on application, business, and security policies. Operating in the proactive flow instantiation mode, the SDN controller populates forwarding tables to the SDN-aware forwarding devices. At times, the SDN controller must function in reactive flow instantiation mode; that is, when a forwarding device receives a packet for a flow not found in its forwarding table, it must send it to the controller to receive forwarding instructions. With total dependence on the SDN controller for determining forwarding decisions and path optimization within the SDN infrastructure for both proactive and reactive flow modes of operation, having a single point of failure is not acceptable. A controller failure with no failover backup leaves the network in an unmanaged state. Hence, it is imperative that the SDN controllers are deployed as clusters on separate physical hosts to guarantee network high availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network virtualization platform topology and the SDN configuration to verify that SDN controllers have been deployed as clusters on separate physical hosts. If the SDN controllers have not been deployed as clusters on separate physical hosts, this is a finding.

## Group: NET-SDN-014

**Group ID:** `V-73099`

### Rule: Physical devices hosting an SDN controller must be connected to two switches for high-availability.

**Rule ID:** `SV-87751r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SDN relies heavily on control messages between a controller and the forwarding devices for network convergence. The controller uses node and link state discovery information to calculate and determine optimum pathing within the SDN network infrastructure based on application, business, and security policies. Operating in the proactive flow instantiation mode, the SDN controller populates forwarding tables to the SDN-aware forwarding devices. At times, the SDN controller must function in reactive flow instantiation mode; that is, when a forwarding device receives a packet for a flow not found in its forwarding table, it must send it to the controller to receive forwarding instructions. With total dependence on the SDN controller for determining forwarding decisions and path optimization within the SDN infrastructure for both proactive and reactive flow modes of operation, having a single point of failure is not acceptable. Hence, it is imperative that all physical devices hosting an SDN controller are connected to two switches using NIC teaming to guarantee network high availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology as well as the physical connection between the physical device hosting an SDN controller and the switches. The device must have NIC teaming enabled and must be dual homed, with each upstream link connected to a different switch. If the physical device hosting an SDN controller is not connected to two switches using NIC teaming, this is a finding.

## Group: NET-SDN-015

**Group ID:** `V-73101`

### Rule: SDN-enabled routers and switches must rate limit the amount of unknown data plane packets that are punted to the SDN controller.

**Rule ID:** `SV-87753r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>SDN-enabled forwarding devices are dependent on the SDN controller for their forwarding tables as well as their configuration and service parameters. The controller uses node and link state discovery information to calculate and determine optimum pathing within the SDN network infrastructure based on application, business, and security policies. Operating in the proactive flow instantiation mode, the SDN controller pre-populates forwarding tables to the forwarding devices. At times, the SDN controller must function in reactive flow instantiation mode; that is, when a forwarding device receives a packet for a flow not found in its forwarding table, it must send or punt it to the controller to receive forwarding instructions. Upon receiving the punted packet, the controller must determine how to forward the packet, create a rule, and populate a new forwarding table to the forwarding device. High rates of punted packets result in excessive controller CPU and memory utilization. Hence, a denial-of-serve attack targeting the SDN controller can be perpetrated either inadvertently or maliciously, involving high rates of packets for new flows that must be punted to the controller.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the parameters provided by the SDN manager or controller when deploying router or switch instances to determine if they set a threshold on the number of unknown data plane packets that are allowed to be punted by a virtual router or switch to the controller within a specific amount of time. Review the configuration of all physical SDN-enabled switches and routers and verify that packet-in messages are rate limited. If SDN-enabled routers and switches do not rate limit the amount of unknown data plane packets that are punted to the SDN controller, this is a finding.

## Group: NET-SDN-016

**Group ID:** `V-73103`

### Rule: Servers hosting SDN controllers must have logging enabled.

**Rule ID:** `SV-87755r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for both network and security personnel to be aware of the state of the SDN infrastructure to maintain network stability. Associating logged events that have occurred within the SDN controller as well as network state information provided by the SDN-enabled components is essential to compile an accurate risk assessment and troubleshoot network outages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all servers hosting an SDN controller and verify that logging has been enabled. If logging is not enabled on all servers hosting an SDN controller, this is a finding.

## Group: NET-SDN-018

**Group ID:** `V-73105`

### Rule: Servers hosting SDN controllers must have an HIDS implemented to detect unauthorized changes.

**Rule ID:** `SV-87757r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The SDN controller is the backbone of the SDN infrastructure. If the server hosting the SDN controller is breached or if unauthorized changes are made to the device, the SDN controller may not have the appropriate resources to function properly or may even be disabled. A host intrusion detection system (HIDS) can monitor and report system configuration changes and prevent malicious or anomalous activity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review all servers hosting an SDN controller and verify that an HIDS has been installed and enabled. If an HIDS has not been installed and enabled on all servers hosting an SDN controller, this is a finding.

## Group: NET-SDN-020

**Group ID:** `V-73107`

### Rule: All Virtual Extensible Local Area Network (VXLAN) enabled switches must be configured with the appropriate VXLAN network identifier (VNI) to ensure VMs can send and receive all associated traffic for their Layer 2 domain.

**Rule ID:** `SV-87759r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VXLAN is a Layer 2 network that overlays a Layer 3 network; that is, it creates a Layer 2 adjacency across a routed IP fabric. Each Layer 2 overlay network is known as a VXLAN segment and is identified by a unique segment ID called a VXLAN Network Identifier (VNI). The VXLAN network enables virtual machines with the same VNI deployed on different hosts to communicate with each other. Virtual machines are identified uniquely by the combination of the MAC addresses of their virtual network interface card (NIC) and VNI. Hence, it is possible to have duplicate MAC addresses within the SDN infrastructure while in different VXLAN segments. Within the VXLAN architecture, virtual tunnel endpoints (VTEPs) perform the encapsulation and de-encapsulation of the layer-2 traffic. The VXLAN segments are independent of the underlying network topology; conversely, the underlying IP network between VTEPs is independent of the VXLAN overlay. It routes the encapsulated packets based on the outer IP address header, which has the initiating VTEP as the source IP address and the terminating VTEP as the destination IP address. The VTEP must be configured with the appropriate VNIs to enable the VTEP to build forwarding tables for active VXLAN segments (Layer 2 domains) by learning MAC addresses per VNI packet flows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the VXLAN topology and documentation for the SDN deployment that identifies each VXLAN segment and distributed logical switch. Review the configuration of all physical VXLAN-enabled switches to verify that the applicable VNIs are defined. If the applicable VNIs have not been defined on all VXLAN-enabled switches, this is a finding. Note: This requirement is applicable to the implementation of technologies similar to VXLAN (e.g., NVGRE, STT) for the purpose of transporting traffic between virtual machines residing on different physical hosts.

## Group: NET-SDN-021

**Group ID:** `V-73109`

### Rule: Virtual Extensible Local Area Network (VXLAN) identifiers must be mapped to the appropriate VLAN identifiers.

**Rule ID:** `SV-87761r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VXLAN is a Layer 2 network that overlays a Layer 3 network; that is, it creates a Layer 2 adjacency across a routed IP fabric. Each Layer 2 overlay network is known as a VXLAN segment and is identified by a unique segment ID called a VXLAN Network Identifier (VNI). The VXLAN network enables virtual machines with the same VNI deployed on different hosts to communicate with each other. Virtual machines are identified uniquely by the combination of the MAC addresses of their virtual network interface card (NIC) and VNI. Hence, it is possible to have duplicate MAC addresses within the SDN infrastructure while in different VXLAN segments. Within the VXLAN architecture, virtual tunnel endpoints (VTEPs) perform the encapsulation and de-encapsulation of the layer-2 traffic. The VXLAN segments are independent of the underlying network topology; conversely, the underlying IP network between VTEPs is independent of the VXLAN overlay. It routes the encapsulated packets based on the outer IP address header, which has the initiating VTEP as the source IP address and the terminating VTEP as the destination IP address. VTEP-enabled switches will determine the VNI to insert into the VXLAN header based on the 802.1Q VLAN tag of each frame received from the hypervisor host connected via trunk link or the VLAN assignment of an access switchport. The mapping of VLAN to VNI is configured on the switch. Since the VNI is used to segregate all Layer 2 domains, the correct mapping is critical to ensure all traffic for each Layer 2 domain within the SDN infrastructure is forwarded correctly and that broadcast and multicast traffic does not leak into the wrong domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the VXLAN topology and documentation for the SDN deployment that identifies each VXLAN segment via VNI, VLAN membership, and the VLAN-to-VNI mapping to be implemented. Review the VTEP configuration of all physical VXLAN-enabled switches to verify that the appropriate VLAN-to-VNI mapping has been defined. If the correct VLAN-to-VNI mapping has not been configured on all VXLAN-enabled switches, this is a finding. Note: This requirement is only applicable to VNIs that must be defined on each VXLAN-enabled switch. In addition, this requirement is applicable to the implementation of technologies similar to VXLAN (e.g., NVGRE, STT) for the purpose of transporting traffic between virtual machines residing on different physical hosts.

## Group: NET-SDN-022

**Group ID:** `V-73111`

### Rule: The proper multicast group for each Virtual Extensible Local Area Network (VXLAN) identifier must be mapped to the appropriate virtual tunnel endpoint (VTEP) so the VTEP will join the associated multicast groups.

**Rule ID:** `SV-87763r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>VXLAN is a Layer 2 network that overlays a Layer 3 network; that is, it creates a Layer 2 adjacency across a routed IP fabric. Each Layer 2 overlay network is known as a VXLAN segment and is identified by a unique segment ID called a VXLAN Network Identifier (VNI). The VXLAN network enables virtual machines with the same VNI deployed on different hosts to communicate with each other. Virtual machines are identified uniquely by the combination of the MAC addresses of their virtual network interface card (NIC) and VNI. Hence, it is possible to have duplicate MAC addresses within the SDN infrastructure while in different VXLAN segments. Within the VXLAN architecture, VTEPs perform the encapsulation and de-encapsulation of the layer-2 traffic. The VXLAN segments are independent of the underlying network topology; conversely, the underlying IP network between VTEPs is independent of the VXLAN overlay. It routes the encapsulated packets based on the outer IP address header, which has the initiating VTEP as the source IP address and the terminating VTEP as the destination IP address. Each VXLAN segment is mapped to an IP multicast group in the transport IP network. Hence, VTEPs join IP multicast groups based on VNI membership. This is the method by which VTEPs can discover other VTEPs belonging to the same VXLAN segment. Each VTEP-enabled switch is configured to join the applicable multicast group for each VNI through Internet Group Management Protocol (IGMP). The IGMP joins will trigger Protocol Independent Multicast (PIM) joins, thereby signaling a multicast distribution tree for each group through the transport network based on the locations of participating VTEPs. The multicast group is used to transmit broadcast, unknown unicast, and multicast traffic through the IP network for each VXLAN segment, limiting all Layer 2 flooding to those switches that have end systems participating in the same VXLAN segment. Because the VNI is used to segregate all Layer 2 domains via the VXLAN header encapsulation by the VTEPs, and discovery of each VTEP member is dependent on a specific multicast group, it is imperative that the correct mapping of multicast groups to VNI is configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the VXLAN topology as well as documentation for the SDN deployment that identifies each VXLAN segment via VNI and the associated multicast groups. Review the VTEP configuration of all physical VXLAN-enabled switches to verify that the appropriate multicast group is defined for each VNI. If the appropriate multicast group is not configured for each member VNI, this is a finding. Note: This requirement is only applicable to VNIs that must be defined on each VXLAN-enabled switch. In addition, this requirement is applicable to the implementation of technologies similar to VXLAN (e.g., NVGRE, STT) for the purpose of transporting traffic between virtual machines residing on different physical hosts.

## Group: NET-SDN-024

**Group ID:** `V-73113`

### Rule: The virtual tunnel endpoint (VTEP) must be dual-homed to two physical network nodes.

**Rule ID:** `SV-87765r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If uplink connectivity for the VTEP to the Virtual Extensible Local Area Network (VXLAN) transport network fails, traffic to and from the VM servers resident on the affected hypervisor host is dropped. Whether it is a hardware (VXLAN-enabled switch) or software (hypervisor resident) VTEP, dedicating a pair of physical uplinks from the VTEP to two separate network nodes adds high availability and resiliency to the VXLAN implementation. If either an uplink or one of the attached network nodes fails, the VTEP would still have connectivity to the underlying IP network for VXLAN traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the VXLAN topology and the configuration of all hypervisor hosts and VXLAN-enabled switches to verify that every VTEP is dual-homed to two physical network nodes. If any VTEPs are not dual-homed to two physical network nodes, this is a finding. Note: This requirement is only applicable to VNIs that must be defined on each VXLAN-enabled switch. In addition, this requirement is applicable to the implementation of technologies similar to VXLAN (e.g., NVGRE, STT) for the purpose of transporting traffic between virtual machines residing on different physical hosts.

## Group: NET-SDN-025

**Group ID:** `V-73115`

### Rule: A secondary IP address must be specified for the virtual tunnel endpoint (VTEP) loopback interface when Virtual Extensible Local Area Network (VXLAN) enabled switches are deployed as a multi-chassis configuration.

**Rule ID:** `SV-87767r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>A multi-chassis configuration (i.e., vPC domain, MLAG, MCLAG, etc.) can be used to attach a hypervisor host to a pair of VXLAN-enabled switches. For example, a vPC consists of two vPC peer switches connected by a vPC peer link. A vPC domain is formed by the two switches; one switch is primary and the other is secondary. A switch can only be part of one vPC domain, and only two switches can make up a vPC domain. A vPC allows links that are physically connected to two different switches to appear as a single port channel to a third device, which can be another switch or a server that supports Link Aggregation Control Protocol (LACP) as defined in IEEE 802.1AX, 802.1aq, and 802.3ad. With vPC deployment, the loopback interface that is acting as the source-interface for the VTEP will use the secondary IP address to function as the anycast IP address if the hypervisor host is dual-attached through the vPC. When a host is single-attached (orphan port), the VXLAN-encapsulated traffic will be sent using the loopback’s primary address.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the VXLAN topology to determine if any hypervisor hosts are dual-homed to two VXLAN-enabled switches deployed as multi-chassis configuration (e.g., vPC domain, MLAG, MCLAG, etc.) to function as a single VTEP. For VXLAN-enabled switches deployed as a multi-chassis configuration, review the configuration to verify that a secondary IP address has been defined for the VTEP loopback interface. If a secondary IP address has not been configured for the VTEP, this is a finding.

## Group: NET-SDN-027

**Group ID:** `V-73117`

### Rule: Two or more edge gateways must be deployed connecting the network virtualization platform (NVP) and the physical network.

**Rule ID:** `SV-87769r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An edge gateway is deployed to allow north-south traffic to flow between the virtualized network and the physical network, including destinations outside of the data center or enclave boundaries. The gateway establishes routing adjacencies between the virtual routers and physical routers. The gateway can also filter the north-south traffic to enforce security policies for communication between the physical and virtual workloads. Deploying two or more edge gateways eliminates the risk of a single point of failure, thereby ensuring there is always reachability between virtual machines and the physical network infrastructure and reducing the risk of black-holing north-south traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram for both the physical infrastructure and the NVP to determine if two or more edge gateways have been deployed between the virtual and physical networks. If two or more edge gateways connecting the NVP and the physical network have not been deployed, this is a finding. Note: This requirement is not applicable if hardware switches are deployed as VTEP devices that also function as gateways between VXLANs and between VXLAN and non-VXLAN infrastructures.

## Group: NET-SDN-028

**Group ID:** `V-73119`

### Rule: Virtual edge gateways must be deployed across multiple hypervisor hosts.

**Rule ID:** `SV-87771r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An edge gateway is deployed to allow north-south traffic to flow between the virtualized network and the physical network, including destinations outside of the data center or enclave boundaries. The gateway can also filter the north-south traffic to enforce security policies for communication between the physical and virtual workloads. If the edge gateways deployed as virtual machines are resident on the same host, the host becomes a single point of failure for all communication between the virtual workload and the physical network infrastructure. Deploying the edge gateways across multiple hypervisor hosts eliminates the risk of a single point of failure, thereby ensuring there is always reachability between virtual machines and the physical network infrastructure and reducing the risk of black-holing north-south traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network virtualization platform topology and the SDN manager to verify that each virtual edge gateway has been deployed across multiple hypervisor hosts. If each virtual edge gateway has not been deployed across multiple hypervisor hosts, this is a finding.

## Group: NET-SDN-029

**Group ID:** `V-73121`

### Rule: The virtual edge gateways must be deployed with routing adjacencies established with two or more physical routers.

**Rule ID:** `SV-87773r1_rule`
**Severity:** low

**Description:**
<VulnDiscussion>An edge gateway is deployed to allow north-south traffic to flow between the virtualized network and the physical network, including destinations outside of the data center or enclave boundaries. The gateway establishes routing adjacencies between the virtual routers and physical routers. The gateway can also filter the north-south traffic to enforce security policies for communication between the physical and virtual workloads. Implementing the edge gateway in either active/standby or equal-cost multipath (ECMP) mode ensures there is always a virtual router to forward north-south traffic, assuming there is always a routing adjacency with a router in the physical network infrastructure. Having an adjacency with only one physical router creates a single point of failure regardless of the number of links deployed, there would be no connectivity between the virtual and physical workloads if a node failure occurred. Hence, it is imperative that each edge gateway is deployed with connectivity to two physical routers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the network topology diagram for both the physical infrastructure and the network virtualization platform (NVP) to determine if the virtual edge gateways have routing adjacencies with two or more physical routers. In addition, verify that the router adjacencies are established by having the administrator enter the appropriate commands that will show the neighbor relationship between the edge gateway and upstream routers. If the virtual edge gateway does not have routing adjacencies established with two or more physical routers, this is a finding.

