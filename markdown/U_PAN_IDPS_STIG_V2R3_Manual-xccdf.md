# STIG Benchmark: Palo Alto Networks IDPS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000018-IDPS-00018

**Group ID:** `V-207688`

### Rule: The Palo Alto Networks security platform must enable Antivirus, Anti-spyware, and Vulnerability Protection for all authorized traffic.

**Rule ID:** `SV-207688r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The flow of all communications traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Restricting the flow of communications traffic, also known as Information flow control, regulates where information is allowed to travel as opposed to who is allowed to access the information and without explicit regard to subsequent accesses to that information. Traffic that is prohibited by the PPSM and Vulnerability Assessments must be denied by the policies configured in the Palo Alto Networks security platform; this is addressed in a separate requirement. Traffic that is allowed by the PPSM and Vulnerability Assessments must still be inspected by the IDPS capabilities of the Palo Alto Networks security platform known as Content-ID. Content-ID is enabled on a per rule basis using individual or group profiles to facilitate policy-based control over content traversing the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of authorized applications, endpoints, services, and protocols that has been added to the PPSM database. Identify which traffic flows are authorized. Go to Objects >> Security Profiles >> Antivirus If there are no Antivirus Profiles configured other than the default, this is a finding. Go to Objects >> Security Profiles >> Anti-Spyware View the configured Anti-Spyware Profiles. If none are configured, this is a finding. Go to Objects >> Security Profiles >> Vulnerability Protection View the configured Vulnerability Protection Profiles. If none are configured, this is a finding. Review each of the configured security policies in turn. For any Security Policy that allows traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the Antivirus Profile, Anti-Spyware, and Vulnerability Protection symbols, this is a finding.

## Group: SRG-NET-000077-IDPS-00062

**Group ID:** `V-207689`

### Rule: The Palo Alto Networks security platform must produce audit records containing information to establish the source of the event, including, at a minimum, originating source address.

**Rule ID:** `SV-207689r767016_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating the source of the event with detected events in the logs provides a means of investigating an attack or suspected attack. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. Palo Alto Networks security platform has four options for the source of log records - "FQDN", "hostname", "ipv4-address", and "ipv6-address". This requirement only allows the use of "ipv4-address" and "ipv6-address" as options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Setup >> Management In the "General Settings" window, if the "hostname" field does not contain a unique identifier, this is a finding. Go to Device >> Setup >> Management In the "Logging and Reporting Settings" pane, if the "Send Hostname in Syslog" does not show either "ipv4-address" or "ipv6-address", this is a finding.

## Group: SRG-NET-000078-IDPS-00063

**Group ID:** `V-207690`

### Rule: The Palo Alto Networks security platform must capture traffic of detected/dropped malicious code.

**Rule ID:** `SV-207690r559743_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating event outcome with detected events in the log provides a means of investigating an attack or suspected attack. The logs should identify what servers, destination addresses, applications, or databases were potentially attacked by logging communications traffic between the target and the attacker. All commands that were entered by the attacker (such as account creations, changes in permissions, files accessed, etc.) during the session should also be logged when capturing for forensic analysis. Packet captures of attack traffic can be used by forensic tools for analysis for example, to determine if an alert is real or a false alarm or for forensics for threat intelligence. Configure the packet capture filters so that the CPU is not overloaded. There are many reasons for a packet capture. This requirement addresses the case where the capture is based on forensics for a detected malicious attack and the traffic is being captured in association with that traffic. Filtering should be engaged to facilitate forensics.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus View the configured Antivirus Profiles. If the Packet Capture check box is not checked, this is a finding. Go to Objects >> Security Profiles >> Anti-Spyware View the configured Anti-Spyware Profiles. If the "Packet Capture" field does not show extended-capture, this is a finding. Go to Objects >> Security Profiles >> Vulnerability Protection View the configured Vulnerability Protection Profiles. If the "Packet Capture" field does not show extended-capture, this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the "Profile" column. If the "Profile" column does not display the Antivirus Profile, Anti-Spyware, and Vulnerability Protection symbols, this is a finding.

## Group: SRG-NET-000089-IDPS-00069

**Group ID:** `V-207691`

### Rule: In the event of a logging failure caused by the lack of audit record storage capacity, the Palo Alto Networks security platform must continue generating and storing audit records if possible, overwriting the oldest audit records in a first-in-first-out manner.

**Rule ID:** `SV-207691r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the Palo Alto Networks security platform is at risk of failing to process audit logs as required, it takes action to mitigate the failure. The Palo Alto Networks security platform performs a critical security function, so its continued operation is imperative. Since availability of the Palo Alto Networks security platform is an overriding concern, shutting down the system in the event of an audit failure should be avoided, except as a last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: overwriting the oldest audit records in a first-in-first-out manner is the default setting of the Palo Alto Networks security platform. Go to Device >> Setup In the "Logging and Reporting Settings" pane, if the "Stop Traffic when LogDb Full" checkbox is selected, this is a finding.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-207692`

### Rule: The Palo Alto Networks security platform must have a DoS Protection Profile for outbound traffic applied to a policy for traffic originating from the internal zone going to the external zone.

**Rule ID:** `SV-207692r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Palo Alto Networks security platform must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. Installation of Palo Alto Networks security platform detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. To comply with this requirement, the Palo Alto Networks security platform must inspect outbound traffic for indications of known and unknown DoS attacks. Sensor log capacity management along with techniques which prevent the logging of redundant information during an attack also guard against DoS attacks. This requirement is used in conjunction with other requirements which require configuration of security policies, signatures, rules, and anomaly detection techniques and are applicable to both inbound and outbound traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> DoS Protection If there are no DoS Protection Profiles configured, this is a finding. There may be more than one configured DoS Protection Profile; ask the Administrator which DoS Protection Profile is intended to protect outside networks from internally-originated DoS attacks. If there is no such DoS Protection Profile, this is a finding.

## Group: SRG-NET-000229-IDPS-00163

**Group ID:** `V-207693`

### Rule: The Palo Alto Networks security platform must detect and deny any prohibited mobile or otherwise malicious code at the enclave boundary.

**Rule ID:** `SV-207693r768712_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus. If no Antivirus Profiles are configured other than the default, this is a finding. View the configured Antivirus Profiles for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB). If the "Action" is anything other than "drop" or "reset-both", this is a finding. Go to Policies >> Security. Review each of the configured security policies in turn. For any Security Policy that affects traffic from an outside (untrusted) zone, view the "Profile" column. If the "Profile" column does not display the “Antivirus Profile” symbol, this is a finding.

## Group: SRG-NET-000246-IDPS-00205

**Group ID:** `V-207694`

### Rule: The Palo Alto Networks security platform must install updates for application software files, signature definitions, detection heuristics, and vendor-provided rules when new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-207694r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be updated, including application software files, anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. Updates must be installed in accordance with the CCB procedures for the local organization. However, at a minimum: Updates designated as critical security updates by the vendor must be installed immediately. Updates for signature definitions, detection heuristics, and vendor-provided rules must be installed immediately. Updates for application software are installed in accordance with the CCB procedures. Prior to automatically installing updates, either manual or automated integrity and authentication checking is required, at a minimum, for application software updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Since some networks cannot connect to the vendor site for automatic updates, a manual process can be used. To verify that the Palo Alto Networks security platform is using the current Applications and Threats database should be checked by viewing the Dashboard and the version and date compared to the latest release. Go to Dashboard; in the General Information pane, view the Threat Version and Antivirus Version. If they are not the most current version as listed on the Palo Alto Networks support site, this is a finding. The following check applies if the network is authorized to connect to the Vendor site for automatic updates. To verify that automatic updates are configured, Go to Device >> Dynamic Updates If no entries for "Applications and Threats" are present, this is a finding. If the "Applications and Threats" entry states "Download Only", this is a finding.

## Group: SRG-NET-000249-IDPS-00176

**Group ID:** `V-207695`

### Rule: The Palo Alto Networks security platform must detect and drop any prohibited mobile or otherwise malicious code at internal boundaries.

**Rule ID:** `SV-207695r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. The Palo Alto Networks security platform allows customized profiles to be used to perform antivirus inspection for traffic between zones. Antivirus, anti-spyware, and vulnerability protection features require a specific license. There is a default Antivirus Profile; the profile inspects all of the listed protocol decoders for viruses, and generates alerts for SMTP, IMAP, and POP3 protocols while dropping for FTP, HTTP, and SMB protocols. However, these default actions cannot be edited and the values for the FTP, HTTP, and SMB protocols do not meet the requirement, so customized profiles must be used.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Antivirus. If there are no Antivirus Profiles configured other than the default, this is a finding. View the configured Antivirus Profiles; for each protocol decoder (SMTP, IMAP, POP3, FTP, HTTP, SMB). If the "Action" is anything other than "drop" or "reset-both", this is a finding. Go to Policies >> Security. Review each of the configured security policies in turn. For any Security Policy that affects traffic between internal Zones (interzone), view the "Profile" column. If the "Profile" column does not display the “Antivirus Profile” symbol, this is a finding.

## Group: SRG-NET-000249-IDPS-00222

**Group ID:** `V-207696`

### Rule: The Palo Alto Networks security platform must send an immediate (within seconds) alert to, at a minimum, the SA when malicious code is detected.

**Rule ID:** `SV-207696r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. The IDPS generates an immediate (within seconds) alert which notifies designated personnel of the incident. Sending a message to an unattended log or console does not meet this requirement since that will not be seen immediately. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. When the Palo Alto Networks security platform blocks malicious code, it also generates a record in the threat log. This message has a medium severity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The following is an example of how to check if the device is sending messages to e-mail; this is one option that meets the requirement. If sending messages to an SNMP server or Syslog servers is used, follow the vendor guidance on how to verify that function. Go to Device >> Server Profiles >> Email If there is no Email Server Profile configured, this is a finding. Go to Objects >> Log forwarding If there is no Email Forwarding Profile configured, this is a finding. Go to Policies >> Security View the Security Policy that is used to detect malicious code (the "Profile" column does display the Antivirus Profile symbol); in the "Options" column, if the Email Forwarding Profile is not used, this is a finding.

## Group: SRG-NET-000251-IDPS-00178

**Group ID:** `V-207697`

### Rule: The Palo Alto Networks security platform must automatically install updates to signature definitions, detection heuristics, and vendor-provided rules.

**Rule ID:** `SV-207697r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to automatically update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. An automatic update process ensures this important task is performed without the need for SCA intervention. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be automatically updated, including anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. If a DoD patch management server or update repository having the tested/verified updates is available for the device component, the components must be configured to automatically check this server/site for updates and install new updates. If a DoD server/site is not available, the component must be configured to automatically check a trusted vendor site for updates. A trusted vendor is either commonly used by DoD, specifically approved by DoD, the vendor from which the equipment was purchased, or approved by the local program's CCB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that automatic updates are configured: Go to Device >> Dynamic Updates If no entries for "Applications and Threats" are present, this is a finding. If the "Applications and Threats" entry states "Download Only", this is a finding.

## Group: SRG-NET-000273-IDPS-00198

**Group ID:** `V-207698`

### Rule: The Palo Alto Networks security platform must block outbound ICMP Destination Unreachable, Redirect, and Address Mask reply messages.

**Rule ID:** `SV-207698r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Control Message Protocol (ICMP) messages are used to provide feedback about problems in the network. These messages are sent back to the sender to support diagnostics. However, some messages can also provide host information and network topology that may be exploited by an attacker. Three ICMP messages are commonly used by attackers for network mapping: Destination Unreachable, Redirect, and Address Mask Reply. These responses must be blocked on external interfaces; however, blocking the Destination Unreachable response will prevent Path Maximum Transmission Unit Discovery (PMTUD), which relies on the response "ICMP Destination Unreachable--Fragmentation Needed but DF Bit Set". PMTUD is a useful function and should only be "broken" after careful consideration. An acceptable alternative to blocking all Destination Unreachable responses is to filter Destination Unreachable messages generated by the IDPS to allow ICMP Destination Unreachable-Fragmentation Needed but DF Bit Set (Type 3, Code 4) and apply this filter to the external interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator if any security policy allows ICMP from an internal zone or DMZ to an outside zone. If there is none, this is not a finding. If there is a security policy that allows ICMP from an internal zone or DMZ to an outside zone, then a policy must be configured to deny outbound ICMP Destination Unreachable, Redirect, and Address Mask reply messages. Go to Objects >> Applications; if there are not three custom Applications to identify ICMP Type 3, 5, and 18, this is a finding. Go to Policies >> Security; if there is no Security Policy using these three custom Applications with the resulting action of "deny", this is a finding. This Security Policy must appear above any Security Policy that allows ICMP from an internal zone or DMZ to an outside zone; if it does not, this is a finding.

## Group: SRG-NET-000273-IDPS-00204

**Group ID:** `V-207699`

### Rule: The Palo Alto Networks security platform must block malicious ICMP packets.

**Rule ID:** `SV-207699r557390_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Control Message Protocol (ICMP) messages are used to provide feedback about problems in the network. These messages are sent back to the sender to support diagnostics. However, ICMP can be misused to provide a covert channel. ICMP tunneling is when an attacker injects arbitrary data into an echo packet and sends to a remote computer. The remote computer injects an answer into another ICMP packet and sends it back. The creates a covert channel where an attacker can hide commands sent to a compromised host or a compromised host can exfiltrate data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator which Security Policy blocks traceroutes and ICMP probes. Go to Policies >> Security View the identified Security Policy. If the "Source Zone" field is not external and the "Source Address" field is not any, this is a finding. If the "Destination Zone" fields do not include the internal and DMZ zones and the "Destination Address" field is not "any", this is a finding. Note: the exact number and name of zones is specific to the network. If the "Application" fields do not include "icmp", "ipv6-icmp", and "traceroute", this is a finding. If the "Actions" field does not show "Deny" as the resulting action, this is a finding.

## Group: SRG-NET-000318-IDPS-00068

**Group ID:** `V-207700`

### Rule: To protect against unauthorized data mining, the Palo Alto Networks security platform must detect and prevent SQL and other code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-207700r856614_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. IDPS component(s) with the capability to prevent code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection If there are no Vulnerability Protection Profiles configured, this is a finding. Ask the Administrator which Vulnerability Protection Profile is used to protect database assets by blocking and alerting on attacks. View the configured Vulnerability Protection Profile; check the "Severity" and "Action" columns. If the Vulnerability Protection Profile used for database protection does not block all critical, high, and medium threats, this is a finding. If the Vulnerability Protection Profile used for database protection does not alert on low and informational threats, this is a finding. Ask the Administrator which Security Policy is used to protect database assets. Go to Policies >> Security View the configured Security Policy; view the "Profile" column. If the "Profile" column does not display the Vulnerability Protection Profile symbol, this is a finding. Moving the cursor over the symbol will list the exact Vulnerability Protection Profiles applied. If the specific Vulnerability Protection Profile is not listed, this is a finding.

## Group: SRG-NET-000318-IDPS-00182

**Group ID:** `V-207701`

### Rule: To protect against unauthorized data mining, the Palo Alto Networks security platform must detect and prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-207701r864179_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. IDPS component(s) with the capability to prevent code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection. If there are no Vulnerability Protection Profiles configured, this is a finding.

## Group: SRG-NET-000334-IDPS-00191

**Group ID:** `V-207702`

### Rule: The Palo Alto Networks security platform must off-load log records to a centralized log server.

**Rule ID:** `SV-207702r856616_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. This also prevents the log records from being lost if the logs stored locally are accidentally or intentionally deleted, altered, or corrupted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view a syslog server profile: Go to Device >> Server Profiles >> Syslog If there are no Syslog Server Profiles present, this is a finding. Select each Syslog Server Profile; if no server is configured, this is a finding. View the log-forwarding profile to determine which logs are forwarded to the syslog server. Go to Objects >> Log forwarding If no Log Forwarding Profile is present, this is a finding. The "Log Forwarding Profile" window has five columns. If there are no Syslog Server Profiles present in the "Syslog" column for the Traffic Log Type, this is a finding. If there are no Syslog Server Profiles present for each of the severity levels of the Threat Log Type, this is a finding. Go to Device >> Log Settings >> System Logs The list of Severity levels is displayed. If any of the Severity levels does not have a configured Syslog Profile, this is a finding. Go to Device >> Log Settings >> Config Logs If the "Syslog" field is blank, this is a finding.

## Group: SRG-NET-000362-IDPS-00196

**Group ID:** `V-207703`

### Rule: The Palo Alto Networks security platform must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis (traffic thresholds).

**Rule ID:** `SV-207703r856617_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. This requirement applies to the communications traffic functionality of the IDPS as it pertains to handling communications traffic, rather than to the IDPS device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> DoS Protection If there are no DoS Protection Profiles configured, this is a finding. Go to Policies >> DoS Protection If there are no DoS Protection Policies, this is a finding. There may be more than one configured DoS Protection Policy; ask the Administrator which DoS Protection Policy is intended to protect internal networks and DMZ networks from externally-originated DoS attacks. If there is no such DoS Protection Policy, this is a finding. If the DoS Protection Policy has no DoS Protection Profile, this is a finding.

## Group: SRG-NET-000362-IDPS-00198

**Group ID:** `V-207704`

### Rule: The Palo Alto Networks security platform must use a Vulnerability Protection Profile that blocks any critical, high, or medium threats.

**Rule ID:** `SV-207704r856618_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attacks, network resources will be unavailable to users. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the IDPS component vendor. These attacks include SYN-flood, ICMP-flood, and Land Attacks. This requirement applies to the communications traffic functionality of the IDPS as it pertains to handling communications traffic, rather than to the IDPS device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Objects >> Security Profiles >> Vulnerability Protection If there are no Vulnerability Protection Profiles configured, this is a finding. Ask the Administrator which Vulnerability Protection Profile is used for interzone traffic. View the configured Vulnerability Protection Profiles; check the "Severity" and "Action" columns. If the Vulnerability Protection Profile used for interzone traffic does not block all critical, high, and medium threats, this is a finding. Go to Policies >> Security Review each of the configured security policies in turn. For any Security Policy that affects traffic between Zones (interzone), view the Profile column. If the Profile column does not display the Vulnerability Protection Profile symbol, this is a finding.

## Group: SRG-NET-000383-IDPS-00208

**Group ID:** `V-207705`

### Rule: Palo Alto Networks security platform components, including sensors, event databases, and management consoles must integrate with a network-wide monitoring capability.

**Rule ID:** `SV-207705r856619_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An integrated, network-wide intrusion detection capability increases the ability to detect and prevent sophisticated distributed attacks based on access patterns and characteristics of access. Integration is more than centralized logging and a centralized management console. The enclave's monitoring capability may include multiple sensors, IPS, sensor event databases, behavior-based monitoring devices, application-level content inspection systems, malicious code protection software, scanning tools, audit record monitoring software, and network monitoring software. Some tools may monitor external traffic while others monitor internal traffic at key boundaries. These capabilities may be implemented using different devices and therefore can have different security policies and severity-level schema. This is valuable because content filtering, monitoring, and prevention can become a bottleneck on the network if not carefully configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Go to Device >> Server Profiles >> NetFlow If no NetFlow Server Profiles are configured, this is a finding. This step assumes that it is an Ethernet interface that is being monitored. The verification is the same for Ethernet, VLAN, Loopback and Tunnel interfaces. Ask the Administrator which interface is being monitored; there may be more than one. Go to Network >> Interfaces >> Ethernet Select the interface that is being monitored. If the "NetFlow Profile" field is "None", this is a finding.

## Group: SRG-NET-000384-IDPS-00209

**Group ID:** `V-207706`

### Rule: The Palo Alto Networks security platform must detect use of network services that have not been authorized or approved by the ISSM and ISSO, at a minimum.

**Rule ID:** `SV-207706r856620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing. To comply with this requirement, the IDPS may be configured to detect services either directly or indirectly (i.e., by detecting traffic associated with a service).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. If there is no list of unauthorized network services, this is a finding. If there are no configured security policies that specifically match the list of unauthorized network services, this is a finding. If the security policies do not deny the traffic associated with the unauthorized network services, this is a finding.

## Group: SRG-NET-000385-IDPS-00210

**Group ID:** `V-207707`

### Rule: The Palo Alto Networks security platform must generate a log record when unauthorized network services are detected.

**Rule ID:** `SV-207707r856621_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. To verify if a Security Policy logs denied traffic: Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, if neither the "Log at Session Start" nor the "Log at Session End" check boxes are checked, this is a finding.

## Group: SRG-NET-000385-IDPS-00211

**Group ID:** `V-207708`

### Rule: The Palo Alto Networks security platform must generate an alert to the ISSO and ISSM, at a minimum, when unauthorized network services are detected.

**Rule ID:** `SV-207708r856622_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the list of network services that have not been authorized or approved by the ISSM and ISSO. For each prohibited network service, view the security policies that denies traffic associated with it and logs the denied traffic. Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to block unauthorized network services. Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, view the Log Forwarding Profile. If there is no Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000390-IDPS-00212

**Group ID:** `V-207709`

### Rule: The Palo Alto Networks security platform must continuously monitor inbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-207709r856623_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system inbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the network architecture diagrams and identify where traffic crosses from one internal zone to another and review the configuration of the Palo Alto Networks security platform. The specific security policy is based on the authorized endpoints, applications, and protocols. If it does not filter traffic passing between zones, this is a finding.

## Group: SRG-NET-000391-IDPS-00213

**Group ID:** `V-207710`

### Rule: The Palo Alto Networks security platform must continuously monitor outbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-207710r856624_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system outbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain the network architecture diagrams and identify where traffic crosses from one internal zone to another and review the configuration of the Palo Alto Networks security platform. If it does not filter traffic passing between zones, this is a finding.

## Group: SRG-NET-000392-IDPS-00214

**Group ID:** `V-207711`

### Rule: The Palo Alto Networks security platform must send an alert to, at a minimum, the ISSO and ISSM when intrusion detection events are detected which indicate a compromise or potential for compromise.

**Rule ID:** `SV-207711r856625_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of intrusion detection incidents that require immediate action and this delay may result in the loss or compromise of information. An Intrusion Detection and Prevention System must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. For each violation of a security policy, an alert to, at a minimum, the ISSO and ISSM, must be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile. If there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to block unauthorized network services. Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, view the Log Forwarding Profile. If there is no Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000392-IDPS-00215

**Group ID:** `V-207712`

### Rule: The Palo Alto Networks security platform must send an alert to, at a minimum, the ISSO and ISSM when threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected.

**Rule ID:** `SV-207712r856626_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. Each Security Policy created in response to an IAVM or CTO must log violations of that particular Security Policy. For each violation of a security policy, an alert to, at a minimum, the ISSO and ISSM, must be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to enforce policies issued by authoritative sources. Go to Policies >> Security Select the name of the security policy to view it. In the "Actions" tab, in the "Log Setting" section, view the Log Forwarding Profile. If there is no Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000392-IDPS-00216

**Group ID:** `V-207713`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when rootkits or other malicious software which allows unauthorized privileged or non-privileged access is detected.

**Rule ID:** `SV-207713r856627_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alert messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to filter traffic into the Internal or DMZ zones. If the "Profile" column does not display the Antivirus Profile symbol, this is a finding. If the "Profile" column does not display the Vulnerability Protection Profile symbol, this is a finding. If the "Profile" column does not display the Anti-spyware symbol, this is a finding. If the "Options" column does not display the Log Forwarding Profile symbol, this is a finding.

## Group: SRG-NET-000392-IDPS-00218

**Group ID:** `V-207714`

### Rule: The Palo Alto Networks security platform must send an alert to, at a minimum, the ISSO and ISSM when denial of service incidents are detected.

**Rule ID:** `SV-207714r856628_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alert messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. Go to Policies >> DoS Protection If there are no DoS Protection Policies, this is a finding. There may be more than one configured DoS Protection Policy. If there is no such DoS Protection Policy, this is a finding. In the "Log Forwarding" field, if there is no configured Log Forwarding Profile, this is a finding.

## Group: SRG-NET-000392-IDPS-00219

**Group ID:** `V-207715`

### Rule: The Palo Alto Networks security platform must generate an alert to, at a minimum, the ISSO and ISSM when new active propagation of malware infecting DoD systems or malicious code adversely affecting the operations and/or security of DoD systems is detected.

**Rule ID:** `SV-207715r856629_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alert messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The Palo Alto Networks security platform must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the Administrator how the ISSO and ISSM are receiving alerts (E-mail, SNMP Trap, or Syslog). View the configured Server Profile; if there is no Server Profile for the method explained, this is a finding. View the Log Forwarding Profiles; this is under Objects >> Log Forwarding. Determine which Server Profile is associated with each Log Forwarding Profile. View the Security Policies that are used to filter traffic between zones or subnets. If the "Profile" column does not display the Antivirus Profile symbol, this is a finding. If the "Options" column does not display the Log Forwarding Profile symbol, this is a finding.

## Group: SRG-NET-000511-IDPS-00012

**Group ID:** `V-207716`

### Rule: The Palo Alto Networks security platform must off-load log records to a centralized log server in real-time.

**Rule ID:** `SV-207716r856630_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Off-loading is a common process in information systems with limited audit storage capacity. The audit storage on the device is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real-time which indicates that the time from event detection to off-loading is seconds or less. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To view a syslog server profile: Go to Device >> Server Profiles >> Syslog If there are no Syslog Server Profiles present, this is a finding. Select each Syslog Server Profile; if no server is configured, this is a finding. View the log-forwarding profile to determine which logs are forwarded to the syslog server. Go to Objects >> Log forwarding If no Log Forwarding Profile is present, this is a finding. The Log Forwarding Profile window has five columns. If there are no Syslog Server Profiles present in the "Syslog" column for the Traffic Log Type, this is a finding. If there are no Syslog Server Profiles present for each of the severity levels of the Threat Log Type, this is a finding. Go to Device >> Log Settings >> System Logs The list of Severity levels is displayed. If any of the Severity levels does not have a configured Syslog Profile, this is a finding. Go to Device >> Log Settings >> Config Logs. If the "Syslog" field is blank, this is a finding.

