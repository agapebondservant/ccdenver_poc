# STIG Benchmark: Juniper SRX SG IDPS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000246-IDPS-00205

**Group ID:** `V-66009`

### Rule: The Juniper Networks SRX Series Gateway IDPS must install updates for predefined signature objects, applications signatures, IDPS policy templates, and device software when new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-80499r1_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failing to update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be updated, including application software files, anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. Updates must be installed in accordance with the CCB procedures for the local organization. However, at a minimum: 1. Updates designated as critical security updates by the vendor must be installed immediately. 2. Updates for predefined signature objects, applications signatures, IDPS policy templates, and device software must be installed immediately. 3. Updates for application software are installed in accordance with the CCB procedures. 4. Prior to automatically installing updates, either manual or automated integrity and authentication checking is required, at a minimum, for application software updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To check the version of the security package installed, enter the following command from the root on the device: show security idp security-package-version Compare the installed release with the latest available and approved release. If a new release is available and not installed, this is a finding.

## Group: SRG-NET-000113-IDPS-00013

**Group ID:** `V-66377`

### Rule: The Juniper Networks SRX Series Gateway IDPS must provide audit record generation capability for detecting events based on implementation of policy filters, rules, and signatures.

**Rule ID:** `SV-80867r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The Juniper SRX with IDP-enabled policies has the capability to capture and log detected security violations and potential security violations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify that the configuration is working properly, use the following command: [edit] show security alarms View the configured alarms to verify at least one option for potential-violation is set to “idp”. If a potential-violation alarm is not defined for “idp”, this is a finding.

## Group: SRG-NET-000018-IDPS-00018

**Group ID:** `V-66383`

### Rule: The Juniper Networks SRX Series Gateway IDPS must enforce approved authorizations by restricting or blocking the flow of harmful or suspicious communications traffic within the network as defined in the PPSM CAL and vulnerability assessments.

**Rule ID:** `SV-80873r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The flow of all communications traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Restricting the flow of communications traffic, also known as Information flow control, regulates where information is allowed to travel as opposed to who is allowed to access the information and without explicit regard to subsequent accesses to that information. The IDPS will include policy filters, rules, signatures, and behavior analysis algorithms that inspects and restricts traffic based on the characteristics of the information and/or the information path as it crosses internal network boundaries. The IDPS monitors for harmful or suspicious information flows and restricts or blocks this traffic based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. The PPSM CAL addresses internal network boundaries restrictions based on traffic type and content such as ports, protocols and services. The Juniper SRX denies all traffic. IDPS inspection will only be performed on the traffic matching the security policies where IDPS is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the list of authorized Junos applications, endpoints, services, and protocols that are installed on the PPSM CAL. Use the following command to show the IDP-specific policies: [edit] show security idp Next, use the show security policies command to display a summary of all the security policies. [edit] show security policies Note: Also inspect the organization's central events log server (e.g., syslog server) for Deny events that match the restrictions in the PPSM CAL. If security policies do not exist to block or restrict communications traffic that is identified as harmful or suspicious by the PPSM and vulnerability assessment, this is a finding.

## Group: SRG-NET-000019-IDPS-00019

**Group ID:** `V-66385`

### Rule: The Juniper Networks SRX Series Gateway IDPS must restrict or block harmful or suspicious communications traffic between interconnected networks based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.

**Rule ID:** `SV-80875r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDPS enforces approved authorizations by controlling the flow of information between interconnected networks to prevent harmful or suspicious traffic does spread to these interconnected networks. Information flow control policies and restrictions govern where information is allowed to travel as opposed to who is allowed to access the information. The IDPS includes policy filters, rules, signatures, and behavior analysis algorithms that inspects and restricts traffic based on the characteristics of the information and/or the information path as it crosses external/perimeter boundaries. IDPS components are installed and configured such that they restrict or block detected harmful or suspect information flows based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic. Once an attack object in the IPS policy is matched, the SRX can execute an action on that specific session, along with actions on future sessions. The ability to execute an action on that particular session is known as an IDPS action. IDPS actions can be one of the following: No-Action, Drop-Packet, Drop-Connection, Close-Client, Close-Server, Close-Client-and-Server, DSCP-Marking, Recommended, or Ignore. IP actions are actions that can be enforced on future sessions. These actions include IP-Close, IP-Block, and IP-Notify This includes traffic between interfaces that are associated within the same security zone (intra-zone traffic). Traffic is permitted between security zones by configuring security policies from a source security zone to the destination security zone. IDPS inspection will only be performed on the traffic matching the security policies where IDPS is enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify custom rules exist to drop packets or terminate sessions upon detection of malicious code. [edit] show security idp policy View the rulebase action option for the IDP policies. View the action options of the zone configurations with the IDP option. If rulebases in active policies are configured for No-Action or Ignore when harmful or suspicious content is detected by signatures, rules, or policies, this is a finding.

## Group: SRG-NET-000113-IDPS-00189

**Group ID:** `V-66387`

### Rule: The Juniper Networks SRX Series Gateway IDPS must provide audit record generation with a configurable severity and escalation level capability.

**Rule ID:** `SV-80877r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records with a severity code it is difficult to track and handle detection events. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The IDPS must have the capability to collect and log the severity associated with the policy, rule, or signature. IDPS products often have either pre-configured and/or a configurable method for associating an impact indicator or severity code with signatures and rules, at a minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Use the following command to view the IDP rules: [edit] show security idp status The IDP traffic log can also be inspected to verify that IDP detection events contain a severity level in the log record. If active IDP rules exist that do not include a severity level, this is a finding.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-66395`

### Rule: The Juniper Networks SRX Series Gateway IDPS must block outbound traffic containing known and unknown DoS attacks by ensuring that rules are applied to outbound communications traffic.

**Rule ID:** `SV-80885r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDPS must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. To comply with this requirement, the IDPS must inspect outbound traffic for indications of known and unknown DoS attacks. Sensor log capacity management along with techniques which prevent the logging of redundant information during an attack also guard against DoS attacks. This requirement is used in conjunction with other requirements which require configuration of security policies, signatures, rules, and anomaly detection techniques and are applicable to both inbound and outbound traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the names of the IDP policies by asking the site representative. From operational mode, enter the following command to verify outbound zones are configured with an IDP policy. show security policies If zones bound to the outbound interfaces, including VPN zones, are not configured with an IDP policy, this is a finding.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-66399`

### Rule: The Juniper Networks SRX Series Gateway IDPS must block outbound traffic containing known and unknown DoS attacks by ensuring that signature-based objects are applied to outbound communications traffic.

**Rule ID:** `SV-80889r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDPS must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. To perform signature-based attacks on the Juniper SRX IDPS device, create a signature-based attack object.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From operational mode, enter the following command to verify that the signature-based attack object was created: show security idp policies If signature-based attack objects are not created, bound to a zone, and active, this is a finding.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-66401`

### Rule: The Juniper Networks SRX Series Gateway IDPS must block outbound traffic containing known and unknown DoS attacks by ensuring that anomaly-based attack objects are applied to outbound communications traffic.

**Rule ID:** `SV-80891r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDPS must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. To perform anomaly-based attacks on the Juniper SRX IDPS device, create an anomaly-based attack object.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From operational mode, enter the following command to verify that the anomaly-based attack object was created. show idp security policies If anomaly-based attack objects are not created, bound to a zone, and active, this is a finding.

## Group: SRG-NET-000228-IDPS-00196

**Group ID:** `V-66403`

### Rule: The Juniper Networks SRX Series Gateway IDPS must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment.

**Rule ID:** `SV-80893r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an email attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To monitor for and detect known prohibited mobile code or approved mobile code that violates permitted usage requirements, the IDPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From operational mode, enter the following command to verify that the signature-based attack object was created: show security idp policies If signature-based attack objects are not created and used, this is a finding.

## Group: SRG-NET-000229-IDPS-00163

**Group ID:** `V-66405`

### Rule: The Juniper Networks SRX Series Gateway IDPS must block any prohibited mobile code at the enclave boundary when it is detected.

**Rule ID:** `SV-80895r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an email attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To block known prohibited mobile code or approved mobile code that violates permitted usage requirements, the IDPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From operational mode, enter the following command to verify outbound zones are configured with an IDP policy: show security idp policies If zones bound to the outbound interfaces, including VPN zones, are not configured with policy filters, rules, signatures, and anomaly analysis, this is a finding.

## Group: SRG-NET-000318-IDPS-00068

**Group ID:** `V-66407`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must prevent code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-80897r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. IDPS component(s) with the capability to prevent code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify attack group is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to block the packets or terminate the session associated with code injection attacks that could be launched against databases, this is a finding.

## Group: SRG-NET-000318-IDPS-00182

**Group ID:** `V-66409`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must prevent code injection attacks launched against application objects, including, at a minimum, application URLs and application code.

**Rule ID:** `SV-80899r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. IDPS component(s) with the capability to prevent code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify attack group is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to block the packets or terminate the session associated with code injection attacks that could be launched against applications, this is a finding.

## Group: SRG-NET-000318-IDPS-00183

**Group ID:** `V-66411`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-80901r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. IDPS component(s) with the capability to prevent SQL code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for SQL injection attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to block the packets or terminate the session associated with SQL injection attacks that could be launched against data storage objects, this is a finding.

## Group: SRG-NET-000319-IDPS-00184

**Group ID:** `V-66413`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must detect code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-80903r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. IDPS component(s) with anomaly detection must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to monitor for code injection attacks that could be launched against data storage objects, this is a finding.

## Group: SRG-NET-000319-IDPS-00185

**Group ID:** `V-66415`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must detect code injection attacks launched against application objects, including, at a minimum, application URLs and application code.

**Rule ID:** `SV-80905r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. IDPS component(s) with anomaly detection must be included in the IDPS implementation. These components must include rules and anomaly detection algorithms to monitor for atypical application behavior, commands, and accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group or rule is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to monitor for code injection attacks that could be launched against application objects, this is a finding.

## Group: SRG-NET-000319-IDPS-00186

**Group ID:** `V-66417`

### Rule: To protect against unauthorized data mining, the Juniper Networks SRX Series Gateway IDPS must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-80907r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. IDPS component(s) with anomaly detection must be included in the IDPS implementation to monitor for and detect unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for SQL injection attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group or rule is configured. [edit] show security idp policies If an attack group or rule(s) is not implemented to monitor for SQL injection attacks that could be launched against data storage objects, this is a finding.

## Group: SRG-NET-000362-IDPS-00196

**Group ID:** `V-66419`

### Rule: The Juniper Networks SRX Series Gateway IDPS must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing rate-based attack prevention behavior analysis.

**Rule ID:** `SV-80909r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. Detection components that use rate-based behavior analysis can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. Rate-based behavior analysis can detect sophisticated, Distributed DoS (DDoS) attacks by correlating traffic information from multiple network segments or components. The Juniper SRX must be configured with screens using the Firewall STIG, but must also be configured for anomaly-based protection using various locally developed anomaly-based attack objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From operational mode, enter the following command to verify that the anomaly-based attack object was created: show idp security policies If anomaly-based attack objects are not created, bound to a zone, and active, this is a finding.

## Group: SRG-NET-000362-IDPS-00197

**Group ID:** `V-66421`

### Rule: The Juniper Networks SRX Series Gateway IDPS must protect against or limit the effects of known and unknown types of Denial of Service (DoS) attacks by employing anomaly-based detection.

**Rule ID:** `SV-80911r2_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of IDPS components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks. Detection components that use pattern recognition pre-processors can detect attacks when signatures for the attack do not exist or are not installed. These attacks include zero-day attacks which are new attacks for which vendors have not yet developed signatures. This requirement applies to the communications traffic functionality of the IDPS as it pertains to handling communications traffic, rather than to the IDPS device itself. The Juniper SRX must be configured with screens using the Firewall STIG, but must also be configured for anomaly-based protection using various locally developed anomaly-based attack objects.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the anomaly-based attack object was created. [edit] show idp security policies If anomaly-based attack objects are not created, bound to a zone, and active, this is a finding.

## Group: SRG-NET-000362-IDPS-00198

**Group ID:** `V-66423`

### Rule: The Juniper Networks SRX Series Gateway IDPS must protect against or limit the effects of known types of Denial of Service (DoS) attacks by employing signatures.

**Rule ID:** `SV-80913r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the IDPS component vendor. These attacks include SYN-flood, ICMP-flood, and Land Attacks. This requirement applies to the communications traffic functionality of the IDPS as it pertains to handling communications traffic, rather than to the IDPS device itself. The Juniper SRX must be configured with screens using the Firewall STIG to protect against flood and DOS attacks type attacks, but must also be configured for anomaly-based protection</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group or rule is configured. [edit] show security idp policies If an attack group(s) or rules are not implemented to detect flood and DOS attacks, this is a finding.

## Group: SRG-NET-000392-IDPS-00214

**Group ID:** `V-66425`

### Rule: The IDPS must send an alert to, at a minimum, the ISSO and ISSM when intrusion detection events are detected that indicate a compromise or potential for compromise.

**Rule ID:** `SV-80915r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of intrusion detection incidents that require immediate action and this delay may result in the loss or compromise of information. In accordance with CCI-001242, the IDPS is a real-time intrusion detection system. These systems must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The Juniper SRX IDPS can be configured for email alerts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group or rule is configured. [edit] show security idp policies If an attack group or rule is not implemented to detect root-level intrusion attacks or the match condition is not configured for an alert, this is a finding.

## Group: SRG-NET-000392-IDPS-00216

**Group ID:** `V-66427`

### Rule: The Juniper Networks SRX Series Gateway IDPS must generate an alert to, at a minimum, the ISSO and ISSM when root-level intrusion events that provide unauthorized privileged access are detected.

**Rule ID:** `SV-80917r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alerts messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The Juniper SRX IDPS can be configured for email alerts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an attack group or rule is configured. [edit] show security idp policies If an attack group or rules are not configured to detect root-level intrusion attacks or the match condition is not configured for an alert, this is a finding.

## Group: SRG-NET-000392-IDPS-00218

**Group ID:** `V-66429`

### Rule: The IDPS must send an alert to, at a minimum, the ISSO and ISSM when DoS incidents are detected.

**Rule ID:** `SV-80919r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alerts messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The Juniper SRX IDPS can be configured for email alerts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify alerts are configured to implement this requirement. [edit] show security alarms potential-violation If alerts are not configured to notify the ISSO and ISSM of potential-violation IDP events, this is a finding.

## Group: SRG-NET-000251-IDPS-00178

**Group ID:** `V-66431`

### Rule: The Juniper Networks SRX Series Gateway IDPS must automatically install updates to signature definitions.

**Rule ID:** `SV-80921r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to automatically update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. An automatic update process ensures this important task is performed without the need for Security Control Auditor (SCA) intervention. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be automatically updated, including anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. If a DoD patch management server or update repository having the tested/verified updates is available for the IDPS component, the components must be configured to automatically check this server/site for updates and install new updates. If a DoD server/site is not available, the component must be configured to automatically check a trusted vendor site for updates. A trusted vendor is either commonly used by DoD, specifically approved by DoD, the vendor from which the equipment was purchased, or approved by the local program's CCB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify automatic updates are configured. [edit] show security idp If updates are not automatically installed, this is a finding.

## Group: SRG-NET-000248-IDPS-00206

**Group ID:** `V-66433`

### Rule: The Juniper Networks SRX Series Gateway IDPS must perform real-time monitoring of files from external sources at network entry/exit points.

**Rule ID:** `SV-80923r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Real-time monitoring of files from external sources at network entry/exit points helps to detect covert malicious code before it is downloaded to or executed by internal and external endpoints. Using malicious code, such as viruses, worms, Trojan horses, and spyware, an attacker may gain access to sensitive data and systems. IDPSs innately meet this requirement for real-time scanning for malicious code when properly configured to meet the requirements of this STIG. However, most products perform communications traffic inspection at the packet level.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify a dynamic custom attack group which includes attack objects for malicious code monitoring of files. show security idp dynamic-attack-group If a custom attack group exists containing members which include malicious code attack categories, this is a finding.

## Group: SRG-NET-000249-IDPS-00176

**Group ID:** `V-66435`

### Rule: The Juniper Networks SRX Series Gateway IDPS must drop packets or disconnect the connection when malicious code is detected.

**Rule ID:** `SV-80925r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the IDPS to discard and/or redirect based on local organizational incident handling procedures minimizes the impact of this code on the network. Once an attack object in the IPS policy is matched, the SRX can execute an action on that specific session, along with actions on future sessions. The ability to execute an action on that particular session is known as an IDPS action. IDPS actions can be one of the following: No-Action, Drop-Packet, Drop-Connection, Close-Client, Close-Server, Close-Client-and-Server, DSCP-Marking, Recommended, or Ignore. IP actions are actions that can be enforced on future sessions. These actions include IP-Close, IP-Block, and IP-Notify</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify custom rules exist to drop packets or terminate sessions upon detection of malicious code. [edit] show security idp policy View the rulebase action option for the IDP policies. If rulebases for IDP policies which detect malicious code are not configured with an action of Drop-Packet, Drop-Connection, or some form of session termination, this is a finding.

## Group: SRG-NET-000249-IDPS-00222

**Group ID:** `V-66437`

### Rule: The Juniper Networks SRX Series Gateway IDPS must send an immediate alert to, at a minimum, the Security Control Auditor (SCA) when malicious code is detected.

**Rule ID:** `SV-80927r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. The IDPS generates an immediate (within seconds) alert which notifies designated personnel of the incident. Sending a message to an unattended log or console does not meet this requirement since that will not be seen immediately. These messages should include a severity level indicator or code as an indicator of the criticality of the incident.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify an alert is sent when malicious code is detected. [edit] show security idp policy View the rulebase options for the IDP policies. If the rulebase options for the IDP policies that detect malicious code do not contain the "alert" option, this is a finding.

## Group: SRG-NET-000512-IDPS-00194

**Group ID:** `V-66439`

### Rule: The Juniper Networks SRX Series Gateway IDPS must have only active Juniper Networks licenses.

**Rule ID:** `SV-80929r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the IDP or UTM licenses are allowed to lapse, the Juniper SRX IDPS can still inspect traffic and continue to use the outdated signature database for rules, objects, and dynamic groups. However, updates to the signature database cannot be downloaded from Juniper Networks. This puts the network at risk since the updates are used to addresses new CERT and IAVM vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In operational mode, enter show system license. If the license expiration for idp-sig and all other licenses installed are past today's date, this is a finding.

## Group: SRG-NET-000512-IDPS-00194

**Group ID:** `V-66441`

### Rule: The Juniper Networks SRX Series Gateway IDPS must either forward the traffic from inbound connections to be more deeply inspected for malicious code and Layer 7 threats, or the Antivirus and Unified Threat Management (UTM) license must be installed, active, and policies and rules configured.

**Rule ID:** `SV-80931r1_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>UTM is an industry term that was coined to define Layer 7 protection against client-side threats. This does not include IPS (which also has protection against server-to-client attacks) but rather technologies such as network-based antivirus protection, URL filtering, antispam solutions, and content filtering. IPS is primarily focused on network-based attacks on protocols, and is stream based, meaning that it processes traffic inline without modifying it as a stream. This works great from a performance perspective to detect attacks against services and applications. UTM, on the other hand, is meant more for protecting against files that are transmitted on top of the network streams. Although IPS might be more geared for detecting an overflow of the parser of the network stream, it isn’t as well geared for detecting threats within files. That is, it certainly can detect such file-based attacks, but attackers can go to great lengths to encode, encrypt, and obfuscate files to perform some malicious action—and it is very difficult to detect these attacks in Stream mode.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify UTM and AV policies are configured. [edit] show security utm If a stanza does not exist for at least one UTM and one AV policy, this is a finding. If the IDPS does not have UTM and AV capabilities and traffic is not forwarded to be inspected for AV and UTM threats, this is a finding.

