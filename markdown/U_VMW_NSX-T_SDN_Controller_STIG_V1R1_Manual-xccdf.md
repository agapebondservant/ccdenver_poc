# STIG Benchmark: VMware NSX-T SDN Controller Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000236-SDN-000365

**Group ID:** `V-251734`

### Rule: The NSX-T Controller must be configured as a cluster in active/active mode to preserve any information necessary to determine cause of a system failure and to maintain network operations with least disruption to workload processes and flows.

**Rule ID:** `SV-251734r810060_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure in a known state can address safety or security in accordance with the mission needs of the organization. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the SDN controller. Preserving network element state information helps to facilitate continuous network operations minimal or no disruption to mission-essential workload processes and flows.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the NSX-T Manager web interface, go to System >> Appliances. Verify there are three NSX-T Managers deployed, a VIP or external load balancer is configured, and the cluster is in a healthy state. If there are not three NSX-T Managers deployed and a VIP or external load balancer configured and the cluster is in a healthy state, this is a finding.

## Group: SRG-NET-000512-SDN-001050

**Group ID:** `V-251735`

### Rule: The NSX-T Controller cluster must  be on separate physical hosts.

**Rule ID:** `SV-251735r810063_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>SDN relies heavily on control messages between a controller and the forwarding devices for network convergence. The controller uses node and link state discovery information to calculate and determine optimum pathing within the SDN network infrastructure based on application, business, and security policies. Operating in the proactive flow instantiation mode, the SDN controller populates forwarding tables to the SDN-aware forwarding devices. At times, the SDN controller must function in reactive flow instantiation mode; that is, when a forwarding device receives a packet for a flow not found in its forwarding table, it must send it to the controller to receive forwarding instructions. With total dependence on the SDN controller for determining forwarding decisions and path optimization within the SDN infrastructure for both proactive and reactive flow modes of operation, having a single point of failure is not acceptable. A controller failure with no failover backup leaves the network in an unmanaged state. Hence, it is imperative that the SDN controllers are deployed as clusters on separate physical hosts to guarantee network high availability.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be performed in vCenter. From the vSphere Client, go to Administration >> Hosts and Clusters >> Select the cluster where the NSX-T Managers are deployed >> Configure >> Configuration >> VM/Host Rules. If the NSX-T Manager cluster does not have rules applied to it that separate the nodes onto different physical hosts, this is a finding.

