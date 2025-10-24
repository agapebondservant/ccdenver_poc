# STIG Benchmark: Fortinet FortiGate Firewall Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000019-FW-000003

**Group ID:** `V-234133`

### Rule: The FortiGate firewall must use filters that use packet headers and packet attributes, including source and destination IP addresses and ports.

**Rule ID:** `SV-234133r611399_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Information flow control regulates where information is allowed to travel within a network and between interconnected networks. Blocking or restricting detected harmful or suspicious communications between interconnected networks enforces approved authorizations for controlling the flow of traffic. The firewall that filters traffic outbound to interconnected networks with different security policies must be configured with filters (i.e., rules, access control lists [ACLs], screens, and policies) that permit, restrict, or block traffic based on organization-defined traffic authorizations. Filtering must include packet header and packet attribute information, such as IP addresses and port numbers. Configure filters to perform certain actions when packets match specified attributes, including the following actions: - Apply a policy - Accept, reject, or discard the packets - Classify the packets based on their source address - Evaluate the next term in the filter - Increment a packet counter - Set the packets’ loss priority - Specify an IPsec SA (if IPsec is used in the implementation) - Specify the forwarding path - Write an alert or message to the system log.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify there are no policies configured with source and destination interface set to "any", and source and destination address set to "all" and the Action set to ACCEPT. If there are policies configured with source and destination interface set to "any", and source and destination address set to "all" and the Action set to ACCEPT, this is a finding.

## Group: SRG-NET-000061-FW-000001

**Group ID:** `V-234134`

### Rule: The FortiGate firewall must use organization-defined filtering rules that apply to the monitoring of remote access traffic for the traffic from the VPN access points.

**Rule ID:** `SV-234134r611402_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote access devices (such as those providing remote access to network devices and information systems) that lack automated capabilities increase risk and make remote user access management difficult at best. Remote access is access to DoD non-public information systems by an authorized user (or an information system) communicating through an external, non-organization-controlled network. Automated monitoring of remote access sessions allows organizations to detect cyberattacks and ensure ongoing compliance with remote access policies by auditing connection activities of remote access capabilities from a variety of information system components (e.g., servers, workstations, notebook computers, smart phones, and tablets).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FortiGate is not configured to support VPN access, this requirement is Not Applicable. Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all VPN-related policies are configured with organization-defined filtering rules. 4. For each VPN-related policy, verify the logging option is configured to log All Sessions (for most verbose logging). If there are no VPN policies configured with organization-defined filtering rules, this is a finding.

## Group: SRG-NET-000074-FW-000009

**Group ID:** `V-234135`

### Rule: The FortiGate firewall must generate traffic log entries containing information to establish what type of events occurred.

**Rule ID:** `SV-234135r611405_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Audit event content that may be necessary to satisfy this requirement includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Associating event types with detected events in the network element logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Local Traffic. 3. Verify events are generated containing date, time, alert level related to System and Local Traffic Log. In addition to System log settings, verify that individual firewall policies are configured with most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to log All Sessions (for most verbose logging). If there are no events generated containing date, time, alert level, user, message type, and other information, this is a finding.

## Group: SRG-NET-000075-FW-000010

**Group ID:** `V-234136`

### Rule: The FortiGate firewall must generate traffic log entries containing information to establish when (date and time) the events occurred.

**Rule ID:** `SV-234136r611408_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing when events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis of network traffic patterns, it is essential for security personnel to know when flow control events occurred (date and time) within the infrastructure. Associating event types with detected events in the network traffic logs provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Events, or Local Traffic. 3. Verify events are generated containing date, time, and alert level related to System and Local Traffic Log. In addition to System log settings, verify individual firewall policies are configured with most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to log All Sessions (for most verbose logging). If the log events do not contain information to establish date and time, this is a finding.

## Group: SRG-NET-000076-FW-000011

**Group ID:** `V-234137`

### Rule: The FortiGate firewall must generate traffic log entries containing information to establish the network location where the events occurred.

**Rule ID:** `SV-234137r611411_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing where events occurred, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. To compile an accurate risk assessment and provide forensic analysis, it is essential for security personnel to know where events occurred, such as network element components, modules, device identifiers, node names, and functionality. Associating information about where the event occurred within the network provides a means of investigating an attack, recognizing resource utilization or capacity thresholds, or identifying an improperly configured network element.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Forward Traffic, or Local Traffic. 3. Double-click on an Event to view Log Details. 4. Verify traffic log events contain source and destination IP addresses, and interfaces. In addition to System log settings, verify that individual firewall policies are configured with most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to log All Sessions (for most verbose logging). If the traffic log events do not contain source and destination IP addresses, or interfaces, this is a finding.

## Group: SRG-NET-000077-FW-000012

**Group ID:** `V-234138`

### Rule: The FortiGate firewall must generate traffic log entries containing information to establish the source of the events, such as the source IP address at a minimum.

**Rule ID:** `SV-234138r611414_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without establishing the source of the event, it is impossible to establish, correlate, and investigate the events leading up to an outage or attack. In order to compile an accurate risk assessment and provide forensic analysis, security personnel need to know the source of the event. In addition to logging where events occur within the network, the traffic log events must also identify sources of events, such as IP addresses, processes, and node or device names.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Forward Traffic or Local Traffic. 3. Double-click on an Event to view Log Details. 4. Verify traffic log events contain source and destination IP addresses, and interfaces. In addition to System log settings, verify that individual IPv4 policies are configured with most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to log All Sessions (for most verbose logging). If the log events do not contain IP address of source devices, this is a finding.

## Group: SRG-NET-000078-FW-000013

**Group ID:** `V-234139`

### Rule: The FortiGate firewall must generate traffic log entries containing information to establish the outcome of the events, such as, at a minimum, the success or failure of the application of the firewall rule.

**Rule ID:** `SV-234139r611417_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without information about the outcome of events, security personnel cannot make an accurate assessment as to whether an attack was successful or if changes were made to the security state of the network. Event outcomes can include indicators of event success or failure and event-specific results. They also provide a means to measure the impact of an event and help authorized personnel to determine the appropriate response.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Forward Traffic or Local Traffic. 3. Double-click on an Event to view Log Details. 4. Verify log events contain status information like success or failure of the application of the firewall rule. In addition to System log settings, verify that individual IPv4 policies are configured with most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to log All Sessions (for most verbose logging). If the log events do not contain status information, like success or failure of the application of the firewall rule, this is a finding.

## Group: SRG-NET-000089-FW-000019

**Group ID:** `V-234140`

### Rule: In the event that communication with the central audit server is lost, the FortiGate firewall must continue to queue traffic log records locally.

**Rule ID:** `SV-234140r863251_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network element is at risk of failing to process traffic logs as required, it takes action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend on the nature of the failure mode. In accordance with DoD policy, the traffic log must be sent to a central audit server. When logging functions are lost, system processing cannot be shut down because firewall availability is an overriding concern given the role of the firewall in the enterprise. The system should either be configured to log events to an alternative server or queue log records locally. Upon restoration of the connection to the central audit server, action should be taken to synchronize the local log data with the central audit server. If the central audit server uses User Datagram Protocol (UDP) communications instead of a connection-oriented protocol such as TCP, a method for detecting a lost connection must be implemented.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify at least two logging options are configured. It can be any combination of local and/or remote logging. Via the GUI: Login via the FortiGate GUI with super-admin privileges. - Navigate to Log and Report. - Navigate to Log Settings. - Verify the FortiGate Local Log disk settings. - Verify the Remote and Archiving settings. or Via the CLI: Open a CLI console via SSH or from the "CLI Console" button in the GUI. Run the following commands to verify which logging settings are enabled: # show full-configuration log disk setting | grep -i 'status\|diskfull' - The output should indicate enabled. # show full-configuration log fortianalyzer setting | grep -i 'status\|server' # show full-configuration log fortianalyzer2 setting | grep -i 'status\|server' # show full-configuration log fortianalyzer3 setting | grep -i 'status\|server' # show full-configuration log syslogd setting | grep -i 'status\|server' # show full-configuration log syslogd2 setting | grep -i 'status\|server' # show full-configuration log syslogd3 setting | grep -i 'status\|server' # show full-configuration log syslogd4 setting | grep -i 'status\|server' - The output should indicate enabled and an IP address. If the FortiGate is not logging to at least two locations (local and remote OR remote(x2) only), this is a finding.

## Group: SRG-NET-000098-FW-000021

**Group ID:** `V-234141`

### Rule: The FortiGate firewall must protect traffic log records from unauthorized access while in transit to the central audit server.

**Rule ID:** `SV-234141r835165_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auditing and logging are key components of any security architecture. Logging the actions of specific events provides a means to investigate an attack, recognize resource utilization or capacity thresholds, or identify an improperly configured firewall. Thus, it is imperative that the collected log data be secured and access be restricted to authorized personnel. Methods of protection may include encryption or logical separation. This does not apply to traffic logs generated on behalf of the device itself (management). Some devices store traffic logs separately from the system logs.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privileges. 1. Open a CLI console via SSH or from the GUI widget. 2. Run the following command: # show full-configuration log syslogd setting The output should include: set server {123.123.123.123} set mode reliable set enc-algorithm {medium-high | high} If the syslogd mode is not set to reliable, this is a finding. If the set enc-algorithm is not set to high or medium-high, this is a finding.

## Group: SRG-NET-000099-FW-000161

**Group ID:** `V-234142`

### Rule: The FortiGate firewall must protect the traffic log from unauthorized modification of local log records.

**Rule ID:** `SV-234142r611426_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This can be achieved through multiple methods, which will depend on system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This does not apply to traffic logs generated on behalf of the device itself (management). Traffic logs and Management logs are separate on FortiGate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with an administrator that has no Log and Report access. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: $ config log setting 3. Ensure that the command fails. If an Administrator without Log and Report privileges can configure log settings, this is a finding.

## Group: SRG-NET-000100-FW-000023

**Group ID:** `V-234143`

### Rule: The FortiGate firewall must protect the traffic log from unauthorized deletion of local log files and log records.

**Rule ID:** `SV-234143r611429_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If audit data were to become compromised, forensic analysis and discovery of the true source of potentially malicious system activity would be impossible to achieve. To ensure the veracity of audit data, the information system and/or the application must protect audit information from unauthorized modification. This can be achieved through multiple methods, which will depend on system architecture and design. Some commonly employed methods include ensuring log files receive the proper file system permissions and limiting log data locations. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. This does not apply to traffic logs generated on behalf of the device itself (management). Traffic logs and Management logs are separate on FortiGate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with an administrator that has no Log and Report access. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: $ execute log delete 3. Ensure that the command fails. If an Administrator without Log and Report privileges can delete locally stored logs, this is a finding.

## Group: SRG-NET-000131-FW-000025

**Group ID:** `V-234144`

### Rule: The FortiGate firewall must disable or remove unnecessary network services and functions that are not used as part of its role in the architecture.

**Rule ID:** `SV-234144r611432_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the firewall. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Some services may be security related, but based on the firewall’s role in the architecture, must not be installed on the same hardware. For example, the device may serve as a router, VPN, or other perimeter services. However, if these functions are not part of the documented role of the firewall in the enterprise or branch architecture, the software and licenses must not be installed on the device. This mitigates the risk of exploitation of unconfigured services or services that are not kept updated with security fixes. If left unsecured, these services may provide a threat vector. Some services are not authorized for combination with the firewall and individual policy must be in place to instruct the administrator to remove these services. Examples of these services are Network Time Protocol (NTP), domain name server (DNS), email server, FTP server, web server, and Dynamic Host Configuration Protocol (DHCP). Only remove unauthorized services. This control is not intended to restrict the use of firewalls with multiple authorized roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration system interface 3. Review configuration for unnecessary services. If unnecessary services are configured, this is a finding.

## Group: SRG-NET-000192-FW-000029

**Group ID:** `V-234145`

### Rule: The FortiGate firewall must block outbound traffic containing denial-of-service (DoS) attacks to protect against the use of internal information systems to launch any DoS attacks against other networks or endpoints.

**Rule ID:** `SV-234145r611435_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks can take multiple forms but have the common objective of overloading or blocking a network or host to deny or seriously degrade performance. If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of a firewall at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. The firewall must include protection against DoS attacks that originate from inside the enclave that can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. These attacks can be simple "floods" of traffic to saturate circuits or devices, malware that consumes CPU and memory on a device or causes it to crash, or a configuration issue that disables or impairs the proper function of a device. For example, an accidental or deliberate misconfiguration of a routing table can misdirect traffic for multiple networks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Policy and Objects. 2. Go to IPv4 DoS Policy. 3. Verify different DoS policies that include Incoming Interface, Source Address, Destination Address, and Services have been created. 4. Verify the DoS policies are configured to block L3 and L4 anomalies. If the DoS policies are not configured to block the outbound traffic, this is a finding.

## Group: SRG-NET-000193-FW-000030

**Group ID:** `V-234146`

### Rule: The FortiGate firewall implementation must manage excess bandwidth to limit the effects of packet flooding types of denial-of-service (DoS) attacks.

**Rule ID:** `SV-234146r611438_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A firewall experiencing a DoS attack will not be able to handle production traffic load. The high utilization and CPU caused by a DoS attack will also have an effect on control keep-alives and timers used for neighbor peering resulting in route flapping and will eventually black hole production traffic. The device must be configured to contain and limit a DoS attack's effect on the device's resource utilization. The use of redundant components and load balancing are examples of mitigating "flood-type" DoS attacks through increased capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Policy and Objects. 2. Go to IPv4 DoS Policy. 3. Verify different DoS policies that include Incoming Interface, Source Address, Destination Address, and Services have been created. 4. Verify the DoS policies are configured to block L3 and L4 anomalies. If the DoS policies are not configured to block excess traffic, this is a finding.

## Group: SRG-NET-000205-FW-000040

**Group ID:** `V-234147`

### Rule: The FortiGate firewall must filter traffic destined to the internal enclave in accordance with the specific traffic that is approved and registered in the Ports, Protocols, and Services Management (PPSM) Category Assurance List (CAL), Vulnerability Assessments (VAs) for that the enclave.

**Rule ID:** `SV-234147r628789_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The enclave's internal network contains the servers where mission-critical data and applications reside. Malicious traffic can enter from an external boundary or originate from a compromised host internally. Vulnerability assessments must be reviewed by the SA and protocols must be approved by the IA staff before entering the enclave. Firewall filters (e.g., rules, access control lists [ACLs], screens, and policies) are the first line of defense in a layered security approach. They permit authorized packets and deny unauthorized packets based on port or service type. They enhance the posture of the network by not allowing packets to even reach a potential target within the security domain. The filters provided are highly susceptible ports and services that should be blocked or limited as much as possible without adversely affecting customer requirements. Auditing packets attempting to penetrate the network but stopped by the firewall filters will allow network administrators to broaden their protective ring and more tightly define the scope of operation. If the perimeter is in a deny-by-default posture and what is allowed through the filter is in accordance with the PPSM CAL and VAs for the enclave, and if the permit rule is explicitly defined with explicit ports and protocols allowed, then all requirements related to the database being blocked would be satisfied.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show firewall policy # show firewall policy6 Ensure policies are created that only allow approved traffic that is in accordance with the PPSM CAL and VAs for the enclave. If configured policies allow traffic that is not allowed per the PPSM CAL and VAs for the enclave, this is a finding.

## Group: SRG-NET-000235-FW-000133

**Group ID:** `V-234148`

### Rule: The FortiGate firewall must fail to a secure state if the firewall filtering functions fail unexpectedly.

**Rule ID:** `SV-234148r611444_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Firewalls that fail suddenly and with no incorporated failure state planning may leave the hosting system available but with a reduced security protection. Failure to a known safe state helps prevent systems from failing to a state that may cause unauthorized access to make changes to the firewall filtering functions. This applies to the configuration of the gateway or network traffic security function of the device. Abort refers to stopping the firewall filtering function before it has finished naturally. The term abort refers to both requested and unexpected terminations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show ips global | grep -i fail-open # show system global | grep -i failopen If ips fail-open is set to enable or av-failopen is not set to off or av-failopen-session is not set to disable, this is a finding.

## Group: SRG-NET-000333-FW-000014

**Group ID:** `V-234149`

### Rule: The FortiGate firewall must send traffic log entries to a central audit server for management and configuration of the traffic log entries.

**Rule ID:** `SV-234149r863248_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the traffic log entries, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The DoD requires centralized management of all network component audit record content. Network components requiring centralized traffic log management must have the ability to support centralized management. The content captured in traffic log entries must be managed from a central location (necessitating automation). Centralized management of traffic log records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Ensure at least one syslog server is configured on the firewall. If the product inherently has the ability to store log records locally, the local log must also be secured. However, this requirement is not met since it calls for a use of a central audit server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Under Remote Logging and Archiving, verify FortiAnalyzer and/or syslog settings are enabled and configured with IP addresses of central FortiAnalyzer or Syslog server(s). or Log in to the FortiGate GUI with Super-Admin privilege. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log syslogd setting | grep -i status Check output for: set status enable 3. Run the following command: # show full-configuration log fortianalyzer setting | grep -i status check output for: set status enable If the FortiGate is not configured to send traffic logs to a central audit server, this is a finding.

## Group: SRG-NET-000335-FW-000017

**Group ID:** `V-234150`

### Rule: If communication with the central audit server is lost, the FortiGate firewall must generate a real-time alert to, at a minimum, the SCA and ISSO.

**Rule ID:** `SV-234150r852960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without a real-time alert (less than a second), security personnel may be unaware of an impending failure of the audit functions and system operation may be adversely impacted. Alerts provide organizations with urgent messages. Automated alerts can be conveyed in a variety of ways, including via a regularly monitored console, telephonically, via electronic mail, via text message, or via websites. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. Most firewalls use UDP to send audit records to the server and cannot tell if the server has received the transmission, thus the site must either implement a connection-oriented communications solution (e.g., TCP) or implement a heartbeat with the central audit server and send an alert if it is unreachable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Security Fabric. 2. Click Automation. 3. Verify Automation Stitches are configured to send alerts related to loss of communication with the central audit server. 4. For each Automation Stitch, verify a valid Action Email has been configured. If there are no organization-specific Automation Stitches defined to trigger on loss of communication with the central audit server, this is a finding.

## Group: SRG-NET-000362-FW-000028

**Group ID:** `V-234151`

### Rule: The FortiGate firewall must employ filters that prevent or limit the effects of all types of commonly known denial-of-service (DoS) attacks, including flooding, packet sweeps, and unauthorized port scanning.

**Rule ID:** `SV-234151r852961_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Not configuring a key boundary security protection device such as the firewall against commonly known attacks is an immediate threat to the protected enclave because they are easily implemented by those with little skill. Directions for the attack are obtainable on the internet and in hacker groups. Without filtering enabled for these attacks, the firewall will allow these attacks beyond the protected boundary. Configure the perimeter and internal boundary firewall to guard against the three general methods of well-known DoS attacks: flooding attacks, protocol sweeping attacks, and unauthorized port scanning. Flood attacks occur when the host receives too much traffic to buffer and slows down or crashes. Popular flood attacks include ICMP flood and SYN flood. A TCP flood attack of SYN packets initiating connection requests can overwhelm the device until it can no longer process legitimate connection requests, resulting in DoS. An ICMP flood can overload the device with so many echo requests (ping requests) that it expends all its resources responding and can no longer process valid network traffic, also resulting in DoS. An attacker might use session table floods and SYN-ACK-ACK proxy floods to fill up the session table of a host. In an IP address sweep attack, an attacker sends ICMP echo requests (pings) to multiple destination addresses. If a target host replies, the reply reveals the target’s IP address to the attacker. In a TCP sweep attack, an attacker sends TCP SYN packets to the target device as part of the TCP handshake. If the device responds to those packets, the attacker gets an indication that a port in the target device is open, which makes the port vulnerable to attack. In a UDP sweep attack, an attacker sends UDP packets to the target device. If the device responds to those packets, the attacker gets an indication that a port in the target device is open, which makes the port vulnerable to attack. In a port scanning attack, an unauthorized application is used to scan the host devices for available services and open ports for subsequent use in an attack. This type of scanning can be used as a DoS attack when the probing packets are sent excessively.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Policy and Objects. 2. Click IPv4 DoS Policy. 3. Verify different DoS policies that include Incoming Interface, Source Address, Destination Address, and Services have been created. 4. Double-.click on each policy. 5. Verify the DS policies are configured with appropriate thresholds for L3 and L4 anomalies. If the DoS policies are not configured to filter packets associated with flooding, packet sweeps, and unauthorized port scanning, this is a finding.

## Group: SRG-NET-000364-FW-000031

**Group ID:** `V-234152`

### Rule: The FortiGate firewall must apply ingress filters to traffic that is inbound to the network through any active external interface.

**Rule ID:** `SV-234152r852962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic to the trusted networks may contain malicious traffic that poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Firewall filters control the flow of network traffic and ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet) must be kept separated.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click the Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify the policies are configured for all Interfaces. 4. Verify the polices are configured with Action set either to DENY or ACCEPT based on the organizational requirement. If a Firewall Policy is not applied to all interfaces, this is a finding.

## Group: SRG-NET-000364-FW-000032

**Group ID:** `V-234153`

### Rule: The FortiGate firewall must apply egress filters to traffic outbound from the network through any internal interface.

**Rule ID:** `SV-234153r852963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not filtered, hostile activity intended to harm other networks or packets from networks destined to unauthorized networks may not be detected and prevented. Access control policies and access control lists implemented on devices, such as firewalls, that control the flow of network traffic ensure the flow of traffic is only allowed from authorized sources to authorized destinations. Networks with different levels of trust (e.g., the internet) must be kept separated. This requirement addresses the binding of the egress filter to the interface/zone rather than the content of the egress filter.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click the Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify the policies are configured for each Outgoing Interface. 4. Verify polices are configured with Action set either to DENY or ACCEPT based on the organizational requirement. If the Firewall Policies are not applied to all outbound interfaces, this is a finding.

## Group: SRG-NET-000364-FW-000035

**Group ID:** `V-234154`

### Rule: When employed as a premise firewall, FortiGate must block all outbound management traffic.

**Rule ID:** `SV-234154r852965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The management network must still have its own subnet in order to enforce control and access boundaries provided by layer 3 network nodes such as routers and firewalls. Management traffic between the managed network elements and the management network is routed via the same links and nodes as that used for production or operational traffic. Safeguards must be implemented to ensure the management traffic does not leak past the managed network's premise equipment. If a firewall is located behind the premise router, all management traffic must be blocked at that point, with the exception of management traffic destined to premise equipment.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FortiGate is not employed as a premise firewall, this requirement is Not Applicable. Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify there are Policies in which the Incoming Interface is the Management Network, and the Outgoing Interface is an EGRESS interface. 4. Verify these polices are configured with Action set to DENY. If there are not DENY Policies where the Incoming Interface is the Management Network, and the Outgoing Interface is an EGRESS interface, this is a finding.

## Group: SRG-NET-000364-FW-000036

**Group ID:** `V-234155`

### Rule: The FortiGate firewall must restrict traffic entering the VPN tunnels to the management network to only the authorized management packets based on destination address.

**Rule ID:** `SV-234155r852966_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protect the management network with a filtering firewall configured to block unauthorized traffic. This requirement is similar to the out-of-band management (OOBM) model, in which the production network is managed in-band. The management network could also be housed at a Network Operations Center (NOC) that is located locally or remotely at a single or multiple interconnected sites. NOC interconnectivity, as well as connectivity between the NOC and the managed networks’ premise routers, would be enabled using either provisioned circuits or VPN technologies such as IPsec tunnels or MPLS VPN services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If FortiGate is not configured to support VPN access, this requirement is Not Applicable. Log in to the FortiGate GUI with Super- or Firewall Policy-Admin privilege. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify there are Policies where the Incoming Interface is a management-related VPN Tunnel interface, and the Outgoing Interface is the Management Network interface. 4. Verify such policies with Action IPSEC meet organization requirements to only allow connectivity to specific, authorized Management Network hosts and ensure that traffic is encrypted through the IPsec tunnel. 5. Verify at least one of these polices are configured with Action set to DENY. If there are not DENY Policies in which the Incoming Interface is a management-related VPN Tunnel interface, and the Outgoing Interface is the Management Network interface, this is a finding. If there are no IPSEC Policies for which the Incoming Interface is a management-related VPN Tunnel interface, and the Outgoing Interface is the Management Network interface that meets organization requirements, this is a finding.

## Group: SRG-NET-000364-FW-000040

**Group ID:** `V-234156`

### Rule: The FortiGate firewall must be configured to inspect all inbound and outbound traffic at the application layer.

**Rule ID:** `SV-234156r611468_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Application inspection enables the firewall to control traffic based on different parameters that exist within the packets such as enforcing application-specific message and field length. Inspection provides improved protection against application-based attacks by restricting the types of commands allowed for the applications. Application inspection enforces conformance against published RFCs. Some applications embed an IP address in the packet that needs to match the source address that is normally translated when it goes through the firewall. Enabling application inspection for a service that embeds IP addresses, the firewall translates embedded addresses and updates any checksum or other fields that are affected by the translation. Enabling application inspection for a service that uses dynamically assigned ports, the firewall monitors sessions to identify the dynamic port assignments, and permits data exchange on these ports for the duration of the specific session.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate CLI with Super-Admin privilege, and then run the command: # show system session-helper. Review the output and ensure it matches the following: config system session-helper edit 1 set name pptp set protocol 6 set port 1723 next edit 2 set name h323 set protocol 6 set port 1720 next edit 3 set name ras set protocol 17 set port 1719 next edit 4 set name tns set protocol 6 set port 1521 next edit 5 set name tftp set protocol 17 set port 69 next edit 6 set name rtsp set protocol 6 set port 554 next edit 7 set name rtsp set protocol 6 set port 7070 next edit 8 set name rtsp set protocol 6 set port 8554 next edit 9 set name ftp set protocol 6 set port 21 next edit 10 set name mms set protocol 6 set port 1863 next edit 11 set name pmap set protocol 6 set port 111 next edit 12 set name pmap set protocol 17 set port 111 next edit 13 set name sip set protocol 17 set port 5060 next edit 14 set name dns-udp set protocol 17 set port 53 next edit 15 set name rsh set protocol 6 set port 514 next edit 16 set name rsh set protocol 6 set port 512 next edit 17 set name dcerpc set protocol 6 set port 135 next edit 18 set name dcerpc set protocol 17 set port 135 next edit 19 set name mgcp set protocol 17 set port 2427 next edit 20 set name mgcp set protocol 17 set port 2727 next end If the output does not match, this is a finding.

## Group: SRG-NET-000364-FW-000042

**Group ID:** `V-234157`

### Rule: The FortiGate firewall must be configured to restrict it from accepting outbound packets that contain an illegitimate address in the source address field via an egress filter or by enabling Unicast Reverse Path Forwarding (uRPF).

**Rule ID:** `SV-234157r611471_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A compromised host in an enclave can be used by a malicious platform to launch cyberattacks on third parties. This is a common practice in "botnets", which are a collection of compromised computers using malware to attack other computers or networks. Denial-of-Service (DoS) attacks frequently leverage IP source address spoofing to send packets to multiple hosts that, in turn, send return traffic to the hosts with the forged IP addresses. This can generate significant amounts of traffic. Therefore, protection measures to counteract IP source address spoofing must be taken. When uRPF is enabled in strict mode, the packet must be received on the interface that the device would use to forward the return packet, thereby mitigating IP source address spoofing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The FortiGate has RPF enabled by default, but it can be disabled for IPv4, IPv4 ICMP, IPv6, and IPv6-ICMP with the "set asymroute enable" commands. Log in to the FortiGate CLI with Super-Admin privilege, and then run the command: # get system settings | grep asymroute Unless this device is intentionally setup for asymmetric routing, if any of the settings are set to "enable" this is a finding.

## Group: SRG-NET-000392-FW-000042

**Group ID:** `V-234158`

### Rule: The FortiGate firewall must generate an alert that can be forwarded to, at a minimum, the Information System Security Officer (ISSO) and Information System Security Manager (ISSM) when denial-of-service (DoS) incidents are detected.

**Rule ID:** `SV-234158r852967_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action, and this delay may result in the loss or compromise of information. The firewall generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs), which require real-time alerts. These messages should include a severity-level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The firewall must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The firewall must be configured to send events to a syslog server. Anomaly events, such as a DoS attack are sent with a severity of critical. The syslog server will notify the ISSO and ISSM. To verify the syslog configuration, log in to the FortiGate GUI with Super-Admin privileges. 1. Open a CLI console, via SSH or available from the GUI. 2. Run the following command: # show full-configuration log syslogd setting | grep -i 'mode\|server' The output should be: set server {123.123.123.123} set mode reliable To ensure a secure connection, a certificate must be loaded, encryption enabled, and the SSL version set. To verify, while still in the CLI, run the following command: # get log syslogd setting Check for the following: set enc-algorithm {MEDIUM-HIGH | HIGH} set certificate If the syslogd is not configured to send logs to a central syslog server, this is a finding.

## Group: SRG-NET-000399-FW-000008

**Group ID:** `V-234159`

### Rule: The FortiGate firewall must allow authorized users to record a packet-capture-based IP, traffic type (TCP, UDP, or ICMP), or protocol.

**Rule ID:** `SV-234159r611477_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to capture, record, and log content related to a user session, investigations into suspicious user activity would be hampered. This configuration ensures the ability to select specific sessions to capture in order to support general auditing/incident investigation or to validate suspected misuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Network. 2. Click Packet Capture. 3. Verify different Packet Capture Filters are configured and that capture packets based on interface, host, VLAN, or protocol. If FortiGate does not allow an authorized administrator to capture packets based on interface, host, VLAN, or protocol, this is a finding.

## Group: SRG-NET-000492-FW-000006

**Group ID:** `V-234160`

### Rule: The FortiGate firewall must generate traffic log records when traffic is denied, restricted, or discarded.

**Rule ID:** `SV-234160r611480_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that log usage of objects by subjects and other objects, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Security objects are data objects that are controlled by security policy and bound to security attributes. The firewall must not forward traffic unless it is explicitly permitted via security policy. Logging for firewall security-related sources such as screens and security policies must be configured separately. To ensure security objects such as firewall filters (i.e., rules, access control lists [ACLs], screens, and policies) send events to a syslog server and local logs, security logging must be configured on each firewall term.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Verify the Log Settings for Event Logging is configured to ALL. In addition to System log settings, verify that individual firewall policies are configured with the most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to Log All Sessions (for most verbose logging). 4. Verify the Implicit Deny Policy is configured to Log Violation Traffic. If the Traffic Log setting is not configured to ALL, and the Implicit Deny Policies are not configured to LOG VIOLATION TRAFFIC, this is a finding.

## Group: SRG-NET-000493-FW-000007

**Group ID:** `V-234161`

### Rule: The FortiGate firewall must generate traffic log records when attempts are made to send packets between security zones that are not authorized to communicate.

**Rule ID:** `SV-234161r611483_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Access for different security levels maintains separation between resources (particularly stored data) of different security domains. The firewall can be configured to use security zones configured with different security policies based on risk and trust levels. These zones can be leveraged to prevent traffic from one zone from sending packets to another zone. For example, information from certain IP sources will be rejected if the destination matches specified security zones that are not authorized.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log in to the FortiGate GUI with Super-Admin privilege. 1. Click Log and Report. 2. Click Log Settings. 3. Verify the Log Settings for Event Logging and Local Traffic Log are configured to ALL. In addition to System log settings, verify individual firewall policies are configured with the most suitable Logging Options. 1. Click Policy and Objects. 2. Click IPv4 or IPv6 Policy. 3. Verify all Policy rules are configured with Logging Options set to Log All Sessions (for most verbose logging). 4. Verify the Implicit Deny Policy is configured to Log Violation Traffic. If the Traffic Log setting is not configured to ALL, and the Implicit Deny Policies are not configured to LOG VIOLATION TRAFFIC, this is a finding.

