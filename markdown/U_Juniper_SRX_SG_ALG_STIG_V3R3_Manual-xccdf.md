# STIG Benchmark: Juniper SRX Services Gateway ALG Security Technical Implementation Guide

---

**Version:** 3

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000015-ALG-000016

**Group ID:** `V-214518`

### Rule: For User Role Firewalls, the Juniper SRX Services Gateway Firewall must employ user attribute-based security policies to enforce approved authorizations for logical access to information and system resources.

**Rule ID:** `SV-214518r997541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Successful authentication must not automatically give an entity access to an asset or security boundary. The lack of authorization-based access control could result in the immediate compromise and unauthorized access to sensitive information. All DOD systems must be properly configured to incorporate access control methods that do not rely solely on authentication for authorized access. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. The Juniper Technical Library, Understanding User Role Firewalls, explains this Juniper SRX functionality in detail. This function integrates user-based firewall policies. Administrators can permit or restrict network access of employees, contractors, partners, and other users based on the roles they are assigned. User role firewalls enable greater threat mitigation, provide more informative forensic resources, improve record archiving for regulatory compliance, and enhance routine access provisioning. User role firewalls are more feasible with sites that do not have production workload and are used for employees to access network resources as opposed to large-scale datacenter environments. User role firewalls trigger two actions, retrieval of user and/or role information associated with the traffic, and determine the action to take based on six match criteria within the context of the zone pair. The source-identity field distinguishes a user role firewall from other types of firewalls. If the source identity is specified in any policy for a particular zone pair, it is a user role firewall. The user and role information must be retrieved before policy lookup occurs. If the source identity is not specified in any policy, user and role lookup is not required. To retrieve user and role information, authentication tables are searched for an entry with an IP address corresponding to the traffic. If an entry is found, the user is classified as an authenticated user. If not found, the user is classified as an unauthenticated user. The username and roles associated with an authenticated user are retrieved for policy matching. Both the authentication classification and the retrieved user and role information are used to match the source-identity field. Characteristics of the traffic are matched to the policy specifications. Within the zone context, the first policy that matches the user or role and the five standard match criteria determines the action to be applied to the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If user-based firewall policies are not used, this is Not Applicable. To verify the existence of user-based firewall policies, view a summary of all policies configured on the firewall. [edit] show security policies If the source identity is not specified in any policy for a particular zone pair, this is a finding.

## Group: SRG-NET-000492-ALG-000027

**Group ID:** `V-214519`

### Rule: The Juniper SRX Services Gateway must generate log records when firewall filters, security screens and security policies are invoked and the traffic is denied or restricted.

**Rule ID:** `SV-214519r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that log usage of objects by subjects and other objects, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Security objects are data objects which are controlled by security policy and bound to security attributes. By default, the Juniper SRX will not forward traffic unless it is explicitly permitted via security policy. Logging for Firewall security-related sources such as screens and security policies must be configured separately. To ensure firewall filters, security screens and security policies send events to a Syslog server and local logs, security logging must be configured one each firewall term.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify what is logged in the Syslog, view the Syslog server (Syslog server configuration is out of scope for this STIG); however, the reviewer must also verify that packets are being logged to the local log using the following commands. From operational mode, enter the following command. show firewall log View the Action column; the configured action of the term matches the action taken on the packet: A (accept), D (discard). If events in the log do not reflect the action taken on the packet, this is a finding.

## Group: SRG-NET-000493-ALG-000028

**Group ID:** `V-214520`

### Rule: The Juniper SRX Services Gateway Firewall must generate audit records when unsuccessful attempts to access security zones occur.

**Rule ID:** `SV-214520r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without generating log records that are specific to the security and mission needs of the organization, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. Access for different security levels maintains separation between resources (particularly stored data) of different security domains. The Juniper SRX Firewall implements security zones which are configured with different security policies based on risk and trust levels.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify what is logged in the Syslog, view the Syslog server (Syslog server configuration is out of scope for this STIG); however, the reviewer must also verify that packets are being logged to the local log using the following commands. From operational mode, enter the following command. show firewall log View the Action column; the configured action of the term matches the action taken on the packet: A (accept), D (discard). If events in the log do not reflect the action taken on the packet, this is a finding.

## Group: SRG-NET-000333-ALG-000049

**Group ID:** `V-214521`

### Rule: The Juniper SRX Services Gateway Firewall must be configured to support centralized management and configuration of the audit log.

**Rule ID:** `SV-214521r997542_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the audit records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The DOD requires centralized management of all network component audit record content. Network components requiring centralized audit log management must have the capability to support centralized management. The content captured in audit records must be managed from a central location (necessitating automation). Centralized management of audit records and logs provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Ensure at least one Syslog server and local files are configured to support requirements. However, the Syslog itself must also be configured to filter event records so it is not overwhelmed. A best practice when configuring the external Syslog server is to add similar log-prefixes to the log file names to help and researching of central Syslog server. Another best practice is to add a match condition to limit the recorded events to those containing the regular expression (REGEX). This requirement does not apply to audit logs generated on behalf of the device itself (management). While the Juniper SRX inherently has the capability to generate log records, by default only the high facility levels are captured and only to local files.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that traffic logs are being sent to the syslog server, check the syslog server files. If traffic logs are not being sent to the syslog server, this is a finding.

## Group: SRG-NET-000089-ALG-000055

**Group ID:** `V-214522`

### Rule: In the event that communications with the Syslog server is lost, the Juniper SRX Services Gateway must continue to queue traffic log records locally.

**Rule ID:** `SV-214522r1038960_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the network element is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure mode. Since availability is an overriding concern given the role of the Juniper SRX in the enterprise, the system must not be configured to shut down in the event of a log processing failure. The system will be configured to log events to local files which will provide a log backup. If communication with the syslog server is lost or the server fails, the network device must continue to queue log records locally. Upon restoration of the connection to the centralized collection server, action should be taken to synchronize the local log data with the collection server. By default, both traffic log and system log events are sent to a local log file named messages. You can create a separate log file that contains only traffic log messages so that you do not need to filter for traffic log messages. This makes it easier to track usage patterns or troubleshoot issues for a specific policy. A best practice is to add log-prefixes to the log file names to help in researching the events and filters to prevent log overload. Another best practice is to add a match condition to limit the recorded events to those containing the regular expression (REGEX).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging has been enabled and configured. [edit] show log <LOG-NAME> match "RT_FLOW_SESSION" If a local log file or files is not configured to capture "RT_FLOW_SESSION" events, this is a finding.

## Group: SRG-NET-000131-ALG-000085

**Group ID:** `V-214523`

### Rule: The Juniper SRX Services Gateway Firewall must disable or remove unnecessary network services and functions that are not used as part of its role in the architecture.

**Rule ID:** `SV-214523r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Network devices are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the SRX. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Services that may be related security-related, but based on the role of the device in the architecture do not need to be installed. For example, the Juniper SRX can have an Antivirus, Web filter, IDS, or ALG license. However, if these functions are not part of the documented role of the SRX in the enterprise or branch architecture, then these the software and licenses should not be installed on the device. This mitigates the risk of exploitation of unconfigured services or services that are not kept updated with security fixes. If left unsecured, these services may provide a threat vector. Only remove unauthorized services. This control is not intended to restrict the use of Juniper SRX devices with multiple authorized roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the documentation and architecture for the device. <root> show system license If unneeded services and functions are installed on the device, but are not part of the documented role of the device, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-214524`

### Rule: The Juniper SRX Services Gateway Firewall must not be configured as an NTP server since providing this network service is unrelated to the role as a firewall.

**Rule ID:** `SV-214524r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the SRX. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The Juniper SRX is a highly configurable platform that can fulfil many roles in the Enterprise or Branch architecture depending on the model installed. Some services are employed for management services; however, these services can often also be provided as a network service on the data plane. Examples of these services are NTP, DNS, and DHCP. Also, as a Next Generation Firewall (NGFW) and Unified Threat Management (UTM) device, the SRX integrate functions which have been traditionally separated. The SRX may integrate related content filtering, security services, and analysis services and tools (e.g., IPS, proxy, malware inspection, black/white lists). Depending on licenses purchased, gateways may also include email scanning, decryption, caching, VPN, and DLP services. However, services and capabilities which are unrelated to this primary functionality must not be installed (e.g., DNS, email server, FTP server, or web server).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check both the zones and the interface stanza to ensure NTP is not configured as a service option. [edit] show security zones and, for each interface used, enter: show security zones <zone-name> interface <interface-name> If NTP is included in any of the zone or interface stanzas, this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-214525`

### Rule: The Juniper SRX Services Gateway Firewall must not be configured as a DNS proxy since providing this network service is unrelated to the role as a Firewall.

**Rule ID:** `SV-214525r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the SRX. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The Juniper SRX is a highly configurable platform that can fulfil many roles in the Enterprise or Branch architecture depending on the model installed. Some services are employed for management services; however, these services can often also be provided as a network service on the data plane. Examples of these services are NTP, DNS, and DHCP. Also, as a Next Generation Firewall (NGFW) and Unified Threat Management (UTM) device, the SRX integrate functions which have been traditionally separated. The SRX may integrate related content filtering, security services, and analysis services and tools (e.g., IPS, proxy, malware inspection, black/white lists). Depending on licenses purchased, gateways may also include email scanning, decryption, caching, VPN, and DLP services. However, services and capabilities which are unrelated to this primary functionality must not be installed (e.g., DNS, email server, FTP server, or web server).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check both the zones and the interface stanza to ensure DNS proxy server services are not configured. [edit} show system services dns If a stanza exists for DNS (e.g., forwarders option), this is a finding.

## Group: SRG-NET-000131-ALG-000086

**Group ID:** `V-214526`

### Rule: The Juniper SRX Services Gateway Firewall must not be configured as a DHCP server since providing this network service is unrelated to the role as a Firewall.

**Rule ID:** `SV-214526r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information systems are capable of providing a wide variety of functions (capabilities or processes) and services. Some of these functions and services are installed and enabled by default. The organization must determine which functions and services are required to perform the content filtering and other necessary core functionality for each component of the SRX. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. The Juniper SRX is a highly configurable platform that can fulfil many roles in the Enterprise or Branch architecture depending on the model installed. Some services are employed for management services; however, these services can often also be provided as a network service on the data plane. Examples of these services are NTP, DNS, and DHCP. Also, as a Next Generation Firewall (NGFW) and Unified Threat Management (UTM) device, the SRX integrate functions which have been traditionally separated. The SRX may integrate related content filtering, security services, and analysis services and tools (e.g., IPS, proxy, malware inspection, black/white lists). Depending on licenses purchased, gateways may also include email scanning, decryption, caching, VPN, and DLP services. However, services and capabilities which are unrelated to this primary functionality must not be installed (e.g., DNS, email server, FTP server, or web server).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check both the zones and the interface stanza to ensure DHCP proxy server services are not configured. [edit] show system services dhcp If a stanza exists for DHCP (e.g., forwarders option), this is a finding.

## Group: SRG-NET-000132-ALG-000087

**Group ID:** `V-214527`

### Rule: The Juniper SRX Services Gateway Firewall must be configured to prohibit or restrict the use of unauthorized functions, ports, protocols, and/or services, as defined in the PPSM CAL, vulnerability assessments.

**Rule ID:** `SV-214527r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to prevent unauthorized connection of devices, unauthorized transfer of information, or unauthorized tunneling (i.e., embedding of data types within data types); organizations must disable or restrict unused or unnecessary physical and logical ports/protocols on information systems. DoD continually assesses the ports, protocols, and services that can be used for network communications. Some ports, protocols or services have known exploits or security weaknesses. Network traffic using these ports, protocols, and services must be prohibited or restricted in accordance with DoD policy. The PPSM CAL and vulnerability assessments provide an authoritative source for ports, protocols, and services that are unauthorized or restricted across boundaries on DoD networks. The Juniper SRX must be configured to prevent or restrict the use of prohibited ports, protocols, and services throughout the network by filtering the network traffic and disallowing or redirecting traffic as necessary. Default and updated policy filters from the vendors will disallow older version of protocols and applications and will address most known non-secure ports, protocols, and/or services.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Entering the following commands from the configuration level of the hierarchy. [edit] show security services If functions, ports, protocols, and services identified on the PPSM CAL are not disabled, this is a finding.

## Group: SRG-NET-000213-ALG-000107

**Group ID:** `V-214528`

### Rule: The Juniper SRX Services Gateway Firewall must terminate all communications sessions associated with user traffic after 15 minutes or less of inactivity.

**Rule ID:** `SV-214528r971530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Terminating an idle session within a short time period reduces the window of opportunity for unauthorized personnel to take control of a management session enabled on the console or console port that has been left unattended. In addition, quickly terminating an idle session will also free up resources committed by the managed network element. This control does not imply that the device terminates all sessions or network access; it only ends the inactive session. Since many of the inactivity timeouts pre-defined by Junos OS are set to 1800 seconds, an explicit custom setting of 900 must be set for each application used by the DoD implementation. Since a timeout cannot be set directly on the predefined applications, the timeout must be set on the any firewall rule that uses a pre-defined application (i.e., an application that begins with junos-), otherwise the default pre-defined timeout will be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check both the applications and protocols to ensure session inactivity timeout for communications sessions is set to 900 seconds or less. First get a list of security policies, then enter the show details command for each policy-name found. [edit] show security policies show security policy <policy-name> details Example: Application: any IP protocol: 0, ALG: 0, Inactivity timeout: 0 Verify an activity timeout is configured for either "any" application or, at a minimum, the pre-defined applications (i.e., application names starting with junos-). To verify locally created applications, first get a list of security policies, then enter the show details command for each policy-name found. [edit] Show applications show applications application <application-name> If an inactivity timeout value of 900 seconds or less is not set for each locally created application and pre-defined applications, this is a finding.

## Group: SRG-NET-000362-ALG-000112

**Group ID:** `V-214529`

### Rule: The Juniper SRX Services Gateway Firewall providing content filtering must protect against known and unknown types of denial-of-service (DoS) attacks by implementing statistics-based screens.

**Rule ID:** `SV-214529r997544_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Juniper SRX Firewall DoS protections can be configured by either using a Screen or within the global flow options. Screens, also known as IDS-options, block various layer 3 and 4 attacks. Screen objects are configured with various screen-specific options and then assigned to a zone. The Juniper SRX can be configured with Screens to protect against the following statistics-based DoS attacks: IP sweeps, port scans, and flood attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to see the screen options currently configured: [edit] show security screen ids-option show security zone match "screen" If security screens are not configured or if the security zone is not configured with screen options, this is a finding.

## Group: SRG-NET-000362-ALG-000120

**Group ID:** `V-214530`

### Rule: The Juniper SRX Services Gateway Firewall must implement load balancing on the perimeter firewall, at a minimum, to limit the effects of known and unknown types of denial-of-service (DoS) attacks on the network.

**Rule ID:** `SV-214530r997546_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Load balancing provides service redundancy, which reduces the susceptibility of the ALG to many DoS attacks. This requirement applies to the network traffic functionality of the device as it pertains to handling network traffic. Some types of attacks may be specialized to certain network technologies, functions, or services. For each technology, known and potential DoS attacks must be identified and solutions for each type implemented. The Juniper SRX provides a number of methods for load balancing the traffic flow. The device can be configured for filter based forwarding, per flow load balancing, per-packet load balancing, or High Availability (HA) using additional hardware. Since the firewall is considered a critical security system, it is imperative that perimeter firewalls, at a minimum, be safeguarded with redundancy measures such as HA.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Since load balancing is a highly complex configuration that can be implemented using a wide variety of configurations, ask the site representative to demonstrate the method used and the configuration. If load balancing is not implemented on the perimeter firewall, this is a finding.

## Group: SRG-NET-000362-ALG-000126

**Group ID:** `V-214531`

### Rule: The Juniper SRX Services Gateway Firewall must protect against known types of denial-of-service (DoS) attacks by implementing signature-based screens.

**Rule ID:** `SV-214531r997548_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of content filtering gateways and application layer firewalls at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks. Juniper SRX Firewall DoS protections can be configured by either using a Screen or within the global flow options. Screens, also known as IDS-options, block various layer 3 and 4 attacks. Screen objects are configured with various screen-specific options and then assigned to a zone. The Juniper SRX can be configured with Screens to protect against the following signature-based DoS attacks: ICMP based attacks such as ping of death, IP based attacks such as IP spoofing and teardrop, and TCP based attacks such as TCP headers and land.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command to see the screen options currently configured: [edit] show security screen ids-option show security zone match "screen" If security screens are not configured or if the security zone is not configured with screen options, this is a finding.

## Group: SRG-NET-000192-ALG-000121

**Group ID:** `V-214532`

### Rule: The Juniper SRX Services Gateway Firewall must block outbound traffic containing known and unknown denial-of-service (DoS) attacks to protect against the use of internal information systems to launch any DoS attacks against other networks or endpoints.

**Rule ID:** `SV-214532r997549_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS attacks can take multiple forms but have the common objective of overloading or blocking a network or host to deny or seriously degrade performance. If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. The Juniper SRX must include protection against DoS attacks that originate from inside the enclave, which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. These attacks can be simple "floods" of traffic to saturate circuits or devices, malware that consumes CPU and memory on a device or causes it to crash, or a configuration issue that disables or impairs the proper function of a device. For example, an accidental or deliberate misconfiguration of a routing table can misdirect traffic for multiple networks. The Juniper SRX Firewall uses Screens and Security Policies to detect known DoS attacks with known attack vectors. However, these Screens and policies must be applied to outbound traffic using zones and interface stanzas. Traffic exits the Juniper SRX by way of interfaces. Security zones are configured for one or more interfaces with the same security requirements for filtering data packets. A security zone implements a security policy for one or multiple network segments. These policies must be applied to inbound traffic as it crosses both the network perimeter and as it crosses internal security domain boundaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain and review the list of outbound interfaces and zones. This is usually part of the System Design Specification or Accreditation Package. Review each of the configured outbound interfaces and zones. Verify zones that communicate outbound have been configured with DoS screens. [edit] show security zones <security-zone-name> If the zone for the security screen has not been applied to all outbound interfaces, this is a finding.

## Group: SRG-NET-000364-ALG-000122

**Group ID:** `V-214533`

### Rule: The Juniper SRX Services Gateway Firewall must only allow inbound communications from organization-defined authorized sources routed to organization-defined authorized destinations.

**Rule ID:** `SV-214533r997550_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unrestricted traffic may contain malicious traffic which poses a threat to an enclave or to other connected networks. Additionally, unrestricted traffic may transit a network, which uses bandwidth and other resources. Traffic enters the Juniper SRX by way of interfaces. Security zones are configured for one or more interfaces with the same security requirements for filtering data packets. A security zone implements a security policy for one or multiple network segments. These policies must be applied to inbound traffic as it crosses the network perimeter and as it crosses internal security domain boundaries.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain and review the list of authorized sources and destinations. This is usually part of the System Design Specification or Accreditation Package. Review each of the configured security policies in turn. [edit] show security policies <security-policy-name> If any existing policies allow traffic that is not part of the authorized sources and destinations list, this is a finding.

## Group: SRG-NET-000365-ALG-000123

**Group ID:** `V-214534`

### Rule: The Juniper SRX Services Gateway Firewall must be configured to fail securely in the event of an operational failure of the firewall filtering or boundary protection function.

**Rule ID:** `SV-214534r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If a boundary protection device fails in an unsecure manner (open), information external to the boundary protection device may enter, or the device may permit unauthorized information release. Secure failure ensures when a boundary control device fails, all traffic will be subsequently denied. Fail secure is a condition achieved by employing information system mechanisms to ensure in the event of operational failures of boundary protection devices at managed interfaces (e.g., routers, firewalls, guards, and application gateways residing on protected subnetworks commonly referred to as demilitarized zones), information systems do not enter into unsecure states where intended security properties no longer hold.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Request documentation of the architecture and Juniper SRX configuration. Verify the site has configured the SRX to fail closed, thus preventing traffic from flowing through without filtering and inspection. If the site has not configured the SRX to fail closed, this is a finding.

## Group: SRG-NET-000202-ALG-000124

**Group ID:** `V-214535`

### Rule: The Juniper SRX Services Gateway Firewall must deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

**Rule ID:** `SV-214535r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A deny-all, permit-by-exception network communications traffic policy ensures that only those connections which are essential and approved are allowed. As a managed interface, the ALG must block all inbound and outbound network communications traffic to the application being managed and controlled unless a policy filter is installed to explicitly allow the traffic. The allow policy filters must comply with the site's security policy. A deny all, permit by exception network communications traffic policy ensures that only those connections which are essential and approved, are allowed. By default, Junos denies all traffic through an SRX Series device using an implicit default security policy exists that denies all packets. Organizations must configure security policies that permits or redirects traffic in compliance with DoD policies and best practices. Sites must not change the factory-default security policies.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the default-policy has not been changed and is set to deny all traffic. [edit] show security policies default-policy If the default-policy is not set to deny-all, this is a finding.

## Group: SRG-NET-000273-ALG-000129

**Group ID:** `V-214536`

### Rule: The Juniper SRX Services Gateway Firewall must configure ICMP to meet DoD requirements.

**Rule ID:** `SV-214536r557389_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Providing too much information in error messages risks compromising the data and security of the application and system. Organizations carefully consider the structure/content of error messages. The required information within error messages will vary based on the protocol and error condition. Information that could be exploited by adversaries includes ICMP messages that reveal the use of firewalls or access-control lists.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify ICMP messages are configured to meet DoD requirements. [edit] show firewall family inet If ICMP messages are not configured in compliance with DoD requirements, this is a finding.

## Group: SRG-NET-000390-ALG-000139

**Group ID:** `V-214537`

### Rule: The Juniper SRX Services Gateway Firewall must continuously monitor all inbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-214537r1018647_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. The Juniper SRX is a highly scalable system which, by default, provides stateful or stateless continuous monitoring when placed in the architecture at either the perimeter or internal boundaries. Unusual/unauthorized activities or conditions may include unusual use of unusual protocols or ports and attempted communications from trusted zones to external addresses. Interfaces with identical security requirements can be grouped together into a single security zone. By default, once a security policy is applied to a zone, the Juniper SRX continuously monitors the associated zone for unusual/unauthorized activities or conditions based on the firewall filter or screen associated with that zone.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each inbound zone, verify a firewall screen or security policy is configured. [edit] show security zone show security policies If communications traffic for each inbound zone is not configured with a firewall screen and/or security policy, this is a finding.

## Group: SRG-NET-000391-ALG-000140

**Group ID:** `V-214538`

### Rule: The Juniper SRX Services Gateway Firewall must continuously monitor outbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-214538r1056075_rule`
**Severity:** high

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored, hostile activity may not be detected and prevented. Output from application and traffic monitoring serves as input to continuous monitoring and incident response programs. The Juniper SRX is a highly scalable system that can provide stateful or stateless continuous monitoring when placed in the architecture at the perimeter or internal boundaries. Unusual/unauthorized activities or conditions may include use of unusual protocols or ports and attempted communications from trusted zones to external addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each outbound zone, verify a firewall screen or security policy is configured. [edit] show security zones show security policies If communications traffic for each outbound zone is not configured with a firewall screen or security policy, this is a finding.

## Group: SRG-NET-000392-ALG-000141

**Group ID:** `V-214539`

### Rule: The Juniper SRX Services Gateway Firewall must generate an alert to, at a minimum, the ISSO and ISSM when unusual/unauthorized activities or conditions are detected during continuous monitoring of communications traffic as it traverses inbound or outbound  across internal security boundaries.

**Rule ID:** `SV-214539r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. In accordance with CCI-001242, the ALG which provides content inspection services is a real-time intrusion detection system. These systems must generate an alert when detection events from real-time monitoring occur as required by CCI-2262 and CCI-2261. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Unusual/unauthorized activities or conditions may include large file transfers, long-time persistent connections, unusual protocols and ports in use, and attempted communications with suspected malicious external addresses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each zone, verify a log event, SNMP trap, or SNMP notification is generated and sent to be forwarded to, at a minimum, the ISSO and ISSM when unusual/unauthorized activities or conditions are detected during continuous monitoring of communications traffic as it traverses inbound or outbound across internal security boundaries. [edit] show security zones show security polices If each inbound and outbound zone policy does not generate an alert that can be forwarded to, at a minimum, the ISSO and ISSM when unusual/unauthorized activities or conditions are detected during continuous monitoring of communications traffic as it traverses inbound or outbound across internal security boundaries, this is a finding.

## Group: SRG-NET-000392-ALG-000142

**Group ID:** `V-214540`

### Rule: The Juniper SRX Services Gateway Firewall must generate an alert that can be forwarded to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources are detected.

**Rule ID:** `SV-214540r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Alerts must be sent immediately to designated individuals. Alerts may be sent via NMS, SIEM, Syslog configuration, SNMP trap or notice, or manned console message. Authoritative sources include USSTRATCOM warning and tactical directives/orders including Fragmentary Order (FRAGO), Communications Tasking Orders (CTOs), IA Vulnerability Notices, Network Defense Tasking Message (NDTM), DOD GIG Tasking Message (DGTM), and Operations Order (OPORD).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of threats identified by authoritative sources from the ISSM or ISSO. For each threat, ensure a security policy, screen, or filter that denies or mitigates the threat includes the log or syslog option. Verify a log event, SNMP trap, or SNMP notification is generated and sent to be forwarded to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources are detected. [edit] show security zones show security polices If an alert is not generated that can be forwarded to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources are detected, this is a finding.

## Group: SRG-NET-000392-ALG-000148

**Group ID:** `V-214541`

### Rule: The Juniper SRX Services Gateway Firewall must generate an alert that can be forwarded to, at a minimum, the ISSO and ISSM when DoS incidents are detected.

**Rule ID:** `SV-214541r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. The ALG generates an alert that notifies designated personnel of the Indicators of Compromise (IOCs) which require real-time alerts. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. These indicators reflect the occurrence of a compromise or a potential compromise. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category 1, 2, 4, or 7 detection events) will require an alert when an event is detected. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The ALG must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a security policy with an associated screen that denies or mitigates the threat of DoS attacks includes the log or syslog option. Verify a log event, SNMP trap, or SNMP notification is generated and sent to be forwarded to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources are detected. [edit] show security zones show security polices If an alert is not generated that can be forwarded to, at a minimum, the ISSO and ISSM when DoS incidents are detected, this is a finding.

