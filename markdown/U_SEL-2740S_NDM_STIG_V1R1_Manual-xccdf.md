# STIG Benchmark: SEL-2740S NDM Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000089-NDM-000221

**Group ID:** `V-92291`

### Rule: The SEL-2740S must be configured to create log records for DoD-defined events.

**Rule ID:** `SV-102379r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. Audit records can be generated from various components within the network device (e.g., process, module). Certain specific device functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating audit records. DoD has defined the list of events for which the device will provide an audit record generation capability as the following: (i) Successful and unsuccessful attempts to access, modify, or delete privileges, security objects, security levels, or categories of information (e.g., classification levels); (ii) Access actions, such as successful and unsuccessful logon attempts, privileged activities or other system level access, starting and ending time for user access to the system, concurrent logons from different workstations, successful and unsuccessful accesses to objects, all program initiations, and all direct access to the information system; and (iii) All account creation, modification, disabling, and termination actions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure SEL-2740S Syslog servers are configured by doing the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Go to the "Configuration Objects" page and select the switch. 3. Check Syslog Server IP addresses are in the settings fields configured for the log services. 4. Check Syslog flows exist and are accurate for the SEL-2740S DUT and additional neighbor devices' flows exist and are correct. If the SEL-2740S is not configured with Syslog server entries to ensure auditability, this is a finding.

## Group: SRG-APP-000108-NDM-000232

**Group ID:** `V-92293`

### Rule: The SEL-2740S must alert the ISSO and SA (at a minimum) in the event of an audit processing failure.

**Rule ID:** `SV-102381r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without this notification, the security personnel may be unaware of an impending failure of the audit capability and system operation may be adversely affected. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the configuration node of the SEL-2740S in the flow controller and verify the alarm contact behavior is configured as a log service under All Categories in the configuration object for the desired switch. If the switch is not configured to alert the ISSO and SA in the event of an audit processing failure, this is a finding.

## Group: SRG-APP-000125-NDM-000241

**Group ID:** `V-92295`

### Rule: The SEL-2740S must be configured to send log data to a Syslog server or collected by another parent OTSDN Controller.

**Rule ID:** `SV-102383r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Protection of log data includes assuring log data is not accidentally lost or deleted. Regularly backing up audit records to a different system or onto separate media than the system being audited helps to assure, in the event of a catastrophic system failure, the audit records will be retained.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure SEL-2740S Syslog servers are configured by doing the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Go to the "Configuration Objects" page. 3. Check Syslog Server IP addresses are in the settings fields for the switch node in log services. 4. Check Syslog flows exist and are accurate for the SEL-2740S DUT and additional neighbor devices' flows exist and are correct. If the SEL-2740S is not configured with Syslog server entries to ensure auditability, this is a finding.

## Group: SRG-APP-000371-NDM-000296

**Group ID:** `V-92297`

### Rule: The SEL-2740S must be configured to compare internal information system clocks at least every 24 hours with an authoritative time server.

**Rule ID:** `SV-102385r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Sources outside of the configured acceptable allowance (drift) may be inaccurate. Additionally, unnecessary synchronization may have an adverse impact on system performance and may indicate malicious activity. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740S NTP servers are configured do the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Go to the "configuration object" settings page. 3. Check NTP Server IP addresses in the settings fields. The SEL-2740S support primary and backup NTP servers so enter the IP address of the backup if desired so there are both primary and backup displayed. 4. Check NTP flows for the SEL-2740S DUT and additional neighbor devices exist and are correct. If the SEL-2740S is not configured to maintain internal system clocks with an authoritative time server, this is a finding.

## Group: SRG-APP-000372-NDM-000297

**Group ID:** `V-92299`

### Rule: The SEL-2740S must be configured to synchronize internal system clocks with an authoritative time source.

**Rule ID:** `SV-102387r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inaccurate time stamps make it more difficult to correlate events and can lead to an inaccurate analysis. Determining the correct time a particular event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronizing internal information system clocks provides uniformity of time stamps for information systems with multiple system clocks and systems connected over a network. Organizations should consider setting time periods for different types of systems (e.g., financial, legal, or mission-critical systems). Organizations should also consider endpoints that may not have regular access to the authoritative time server (e.g., mobile, teleworking, and tactical endpoints). This requirement is related to the comparison done every 24 hours in CCI-001891 because a comparison must be done in order to determine the time difference. The organization-defined time period will depend on multiple factors, most notably the granularity of time stamps in audit logs. For example, if time stamps only show to the nearest second, there is no need to have accuracy of a tenth of a second in clocks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740S NTP servers are configured do the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Go to the "configuration object" page. 3. Check NTP Server IP addresses in the settings fields. 4. Check NTP flows for the SEL-2740S DUT and additional neighbor devices exist and are correct. If the SEL-2740S is not configured to maintain internal system clocks with an authoritative time server, this is a finding.

## Group: SRG-APP-000373-NDM-000298

**Group ID:** `V-92301`

### Rule: The SEL-2740S must be configured to maintain internal system clocks with a backup authoritative time server.

**Rule ID:** `SV-102389r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The loss of connectivity to a particular authoritative time source will result in the loss of time synchronization (free-run mode) and increasingly inaccurate time stamps on audit events and other functions. Multiple time sources provide redundancy by including a secondary source. Time synchronization is usually a hierarchy; clients synchronize time to a local source while that source synchronizes its time to a more accurate source. The network device must utilize an authoritative time server and/or be configured to use redundant authoritative time sources. This requirement is related to the comparison done in CCI-001891. DoD-approved solutions consist of a combination of a primary and secondary time source using a combination or multiple instances of the following: a time server designated for the appropriate DoD network (NIPRNet/SIPRNet); United States Naval Observatory (USNO) time servers; and/or the Global Positioning System (GPS). The secondary time source must be located in a different geographic region than the primary time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740S NTP servers are configured do the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Go to the "configuration object" page and select the desired switch. 3. Check NTP Server IP addresses in the settings fields that both a primary and backup NTP server is configured. 4. Check NTP flows for the SEL-2740S DUT and additional neighbor devices exist and are correct. If the SEL-2740S is not configured to maintain internal system clocks with a backup authoritative time server, this is a finding.

## Group: SRG-APP-000412-NDM-000331

**Group ID:** `V-92303`

### Rule: The SEL-2740S must be adopted by OTSDN Controllers for secure communication identifiers and initial trust for configuration of remote maintenance and diagnostic communications.

**Rule ID:** `SV-102391r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>This requires the use of secure protocols instead of their unsecured counterparts, such as SSH instead of telnet, SCP instead of FTP, and HTTPS instead of HTTP. If unsecured protocols (lacking cryptographic mechanisms) are used for sessions, the contents of those sessions will be susceptible to eavesdropping, potentially putting sensitive data (including administrator passwords) at risk of compromise and potentially allowing hijacking of maintenance sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740's credentials and identifiers are accurate, do the following: 1. Log in with Admin rights into parent OTSDN Controller. 2. Download the latest settings for the SEL-2740S device under test (DUT). 3. Go to the "Administration" page. 4. Go to the "X.509 Entries" page. 5. Check that each certificate is necessary, status is valid and reconcile with the parent OTSDN controller(s) for the network. If the SEL-2740S is not configured with the proper X.509 certificates or contains unnecessary certificate entries, this is a finding.

## Group: SRG-APP-000435-NDM-000315

**Group ID:** `V-92305`

### Rule: The SEL-2740S must be configured to permit the maintenance and diagnostics communications to specified OTSDN Controller(s).

**Rule ID:** `SV-102393r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of network devices to mitigate the impact of DoS attacks that have occurred or are ongoing on device availability. For each network device, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the device opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks. The security safeguards cannot be defined at the DoD level because they vary according to the capabilities of the individual network devices and the security controls applied on the adjacent networks (e.g., firewalls performing packet filtering to block DoS attacks).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740S necessary diagnostics and maintenance communications, do the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Confirm the desired switch is adopted by checking that there is a green solid border around the switch in the UI on the topology page. 3. Click the switch node and then the Device View button. 4. Confirm a new browser page opens for the diagnostic collection of the switch. If the SEL-2740S is not successfully talking to the flow controller, this is a finding.

## Group: SRG-APP-000516-NDM-000344

**Group ID:** `V-92307`

### Rule: The SEL-2740S must be adopted by OTSDN Controller(s) and obtain its public key certificates from an appropriate certificate policy through an approved service provider.

**Rule ID:** `SV-102395r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For user certificates, each organization obtains certificates from an approved, shared service provider, as required by OMB policy. For federal agencies operating a legacy public key infrastructure cross-certified with the Federal Bridge Certification Authority at medium assurance or higher, this Certification Authority will suffice.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the SEL-2740S X.509 certificate is properly configured on the SEL-2740S by checking the "Certificates" page on the OTSDN Controller. If the SEL-2740S public keys were not provided by an approved certificate policy or authority, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-92309`

### Rule: The SEL-2740S must be configured to establish trust relationships with parent OTSDN Controller(s).

**Rule ID:** `SV-102397r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Machine to machine initial trust must be established between the OTSDN controller and the SEL-2740S for authenticating all communications and configuration thereafter. Certificates must be created and safely stored. Backup OTSDN controller trust should also be established and locked down. Any time that these need to be modified the SEL-2740S must be factory default reset and adoption process must be re-executed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ensure the SEL-2740S is adopted by only the appropriate OTSDN Controller(s) by checking the "Topology" page on the OTSDN Controller for the SEL-2740S under test to ensure it is adopted by the appropriate OTSDN Controller(s). If the SEL-2740S is adopted by a rogue OTSDN Controller or does not appear as an adopted device in the network, this is a finding.

## Group: SRG-APP-000516-NDM-000317

**Group ID:** `V-92311`

### Rule: The SEL-2740S must be configured to send log data to a syslog server for the purpose of forwarding alerts to the administrators and the ISSO.

**Rule ID:** `SV-102399r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Once an attacker establishes initial access to a system, the attacker often attempts to create a persistent method of reestablishing access. One way to accomplish this is for the attacker to simply create a new account. Notification of account creation is one method for mitigating this risk. A comprehensive account management process will ensure an audit trail which documents the creation of accounts and notifies administrators and Information System Security Officers (ISSOs). Such a process greatly reduces the risk that accounts will be surreptitiously created and provides logging that can be used for forensic purposes.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To ensure SEL-2740S Syslog servers are configured do the following: 1. Log in with Permission Level 3 rights into parent OTSDN Controller. 2. Download the latest settings for the SEL-2740S device under test (DUT). 3. Go to the "Configuration Object" page and select the desired switch node. 4. Check the log services settings and confirm the desired Syslog Server IP addresses and severity levels are in the settings fields. 5. Check Syslog flows exist and are accurate for the SEL-2740S DUT and additional neighbor devices' flows exist and are correct. If the SEL-2740S is not configured with Syslog server entries to ensure auditability, this is a finding.

## Group: SRG-APP-000395-NDM-000347

**Group ID:** `V-94589`

### Rule: The SEL-2740S must authenticate Network Time Protocol sources using authentication that is cryptographically based.

**Rule ID:** `SV-104419r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If Network Time Protocol is not authenticated, an attacker can introduce a rogue NTP server. This rogue server can then be used to send incorrect time information to network devices, which will make log timestamps inaccurate and affect scheduled actions. NTP authentication is used to prevent this tampering by authenticating the time source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify NTP packets only traverse on the private network by traffic engineering both the physical path and redundant path between switch and NTP server. 1. Login to the OTSDN Controller with permission Level 3 rights into parent. 2. Go to the Configuration Objects settings page. 3. Review the NTP Server IP addresses in the settings fields. If the IP addresses are not within the private network, this is a finding.

## Group: SRG-APP-000516-NDM-000342

**Group ID:** `V-94591`

### Rule: The SEL-2740S must employ automated mechanisms to assist in the tracking of security incidents.

**Rule ID:** `SV-104421r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Despite the investment in perimeter defense technologies, enclaves are still faced with detecting, analyzing, and remediating network breaches and exploits that have made it past the network device. An automated incident response infrastructure allows network operations to immediately react to incidents by identifying, analyzing, and mitigating any network device compromise. Incident response teams can perform root cause analysis, determine how the exploit proliferated, and identify all affected nodes, as well as contain and eliminate the threat. The network device assists in the tracking of security incidents by logging detected security events. The audit log and network device application logs capture different types of events. The audit log tracks audit events occurring on the components of the network device. The application log tracks the results of the network device content filtering function. These logs must be aggregated into a centralized server and can be used as part of the organization's security incident tracking and analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the switch is configured to use a syslog server for the purpose of forwarding alerts to the administrators and the ISSO. 1. Login with Permission Level 3 into the OTSDN Controller. 2. Go to the Configuration Object page and select the subject switch node. 3. Check the log services settings and confirm hat a syslog server IP address is in the settings fields. If the SEL-2740S is not configured to use a syslog server, this is a finding.

