# STIG Benchmark: DBN-6300 IDPS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via e-mail to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000089-IDPS-00010

**Group ID:** `V-237556`

### Rule: In the event of a logging failure, caused by loss of communications with the central logging server, the DBN-6300 must queue audit records locally until communication is restored or until the audit records are retrieved manually or using automated synchronization tools.

**Rule ID:** `SV-237556r645496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the IDPS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure. The DBN-6300 performs a critical security function; therefore, its continued operation is imperative. Since availability of the DBN-6300 is an overriding concern, shutting down the system in the event of an audit failure should be avoided, except as a last resort. The SYSLOG protocol does not support automated synchronization; however, this functionality may be provided by Network Management Systems (NMSs), which are not within the scope of this STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit records are automatically backed up on a real-time basis via syslog when enabled. Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log and verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process a successful account action (of any kind). Confirm the presence of a syslog message on the syslog server containing the information for whatever successful account action was taken. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a successful account action that was taken and had just occurred is not there, this is a finding.

## Group: SRG-NET-000089-IDPS-00069

**Group ID:** `V-237557`

### Rule: In the event of a logging failure caused by the lack of log record storage capacity, the DBN-6300 must continue generating and storing audit records if possible, overwriting the oldest audit records in a first-in-first-out manner.

**Rule ID:** `SV-237557r645499_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the IDPS is at risk of failing to process audit logs as required, it takes action to mitigate the failure. The DBN-6300 performs a critical security function, so its continued operation is imperative. Since availability of the IDPS is an overriding concern, shutting down the system in the event of an audit failure should be avoided, except as a last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit records are automatically backed up on a real-time basis via syslog when enabled. Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log and verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process a successful account action (of any kind). Confirm the presence of a syslog message on the syslog server containing the information for whatever successful account action was taken. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information that a successful account action that was taken and had just occurred is not there, this is a finding.

## Group: SRG-NET-000113-IDPS-00013

**Group ID:** `V-237558`

### Rule: The DBN-6300 must generate log events for detection events based on anomaly analysis.

**Rule ID:** `SV-237558r645502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The IDPS must have the capability to capture and log detected security violations and potential security violations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected when an event/alert occurs and this event does not appear in the syslog server, this is a finding.

## Group: SRG-NET-000246-IDPS-00205

**Group ID:** `V-237559`

### Rule: The DBN-6300 must install system updates when new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-237559r982258_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be updated, including application software files, anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. Updates must be installed in accordance with the CCB procedures for the local organization. However, at a minimum: 1. Updates designated as critical security updates by the vendor must be installed immediately. 2. Updates for signature definitions, detection heuristics, and vendor-provided rules must be installed immediately. 3. Updates for application software must be installed in accordance with the CCB procedures. 4. Prior to automatically installing updates, either manual or automated integrity and authentication checking is required, at a minimum, for application software updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To verify the current version is installed, navigate to the main screen of the DBN-6300. View the current running code that is visible in the upper-right corner of the screen. Log on to the organization's DB Networks SFTP site and view the version number of the current release. If the current code version does not match the version of the latest available release, this is a finding.

## Group: SRG-NET-000318-IDPS-00068

**Group ID:** `V-237560`

### Rule: To help detect unauthorized data mining, the DBN-6300 must detect code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-237560r856496_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a SQL injection attack. IDPS component(s) with the capability to detect code injections must be included in the IDPS implementation to detect unauthorized data mining. These components must include behavior-based anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the organization's documentation to determine which databases are required to be protected. If the documentation does not exist, this is a finding. Navigate to Learning >> Time Regions and view the table of detected databases. For each database requiring protection, view the "State". Unprotected databases show a red shield. Protected databases show a green shield. If databases that are required to be protected are not being protected, this is a finding.

## Group: SRG-NET-000318-IDPS-00183

**Group ID:** `V-237561`

### Rule: To protect against unauthorized data mining, the DBN-6300 must monitor for and detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-237561r856497_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. The DBN-6300 is a passive listening device, and operates only as a detector, inspecting database traffic from a mirrored/SPAN port or tap for the purpose of analyzing every SQL statement visible on that network segment, and is therefore not in a position to block the flow of network traffic. Any blocking will be performed by a different device on the network based on the analysis provided by the DBN-6300. Protection against attacks launched against data storage objects, databases, database records and database fields will be managed by other devices, potentially based on information provided by the IDPS-6300.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the organization's documentation to determine which databases are required to be protected. If the documentation does not exist, this is a finding. Navigate to Learning >> Time Regions and view the table of detected databases. For each database requiring protection, view the "State". Unprotected databases show a red shield. Protected databases show a green shield. If databases that are required to be protected are not being protected, this is a finding.

## Group: SRG-NET-000319-IDPS-00184

**Group ID:** `V-237562`

### Rule: To protect against unauthorized data mining, the DBN-6300 must detect SQL code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-237562r856498_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. IDPS component(s) with anomaly detection must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that the DBN-6300 is configured to detect code injection attacks. Navigate to Application >> Time Learning. Validate that the database or databases of interest has/have the "state" shield set to green (in detection mode). If the "state" shield is not set to green, this is a finding (as the database or databases are not in detection mode).

## Group: SRG-NET-000319-IDPS-00185

**Group ID:** `V-237563`

### Rule: To protect against unauthorized data mining, the DBN-6300 must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code/input fields.

**Rule ID:** `SV-237563r856499_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject SQL code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database or change data on a website. IDPS component(s) with anomaly detection must be included in the IDPS implementation. These components must include behavior-based anomaly detection algorithms to monitor for atypical application behavior, which may include commands and accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the organization's documentation to determine which databases are required to be protected. If the documentation does not exist, this is a finding. Navigate to Learning >> Time Regions and view the table of detected databases. For each database requiring protection, view the "State". Unprotected databases show a red shield. Protected databases show a green shield. If databases that are required to be protected are not being protected, this is a finding.

## Group: SRG-NET-000319-IDPS-00186

**Group ID:** `V-237564`

### Rule: To protect against unauthorized data mining, the DBN-6300 must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-237564r856500_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. IDPS component(s) with anomaly detection must be included in the IDPS implementation to monitor for and detect unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for SQL injection attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the organization's documentation to determine which databases are required to be protected. If the documentation does not exist, this is a finding. Navigate to Learning >> Time Regions and view the table of detected databases. For each database requiring protection, view the "State". Unprotected databases show a red shield. Protected databases show a green shield. If databases that are required to be protected are not being protected, this is a finding.

## Group: SRG-NET-000333-IDPS-00190

**Group ID:** `V-237565`

### Rule: The DBN-6300 must support centralized management and configuration of the content captured in audit records generated by all DBN-6300 components.

**Rule ID:** `SV-237565r982261_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the log records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an attack. Centralized management and storage of log records increases efficiency in maintenance and management of records and facilitates the backup and archiving of those records. The IDPS must be configured to support centralized management and configuration of the content to be captured in audit records generated by all network components. IDPS sensors and consoles must have the capability to support centralized logging. They must be configured to send log messages to centralized, redundant servers and be capable of being remotely configured to change logging parameters (such as facility and severity levels). DB Networks can (and does) use Splunk as the current Security Operations Center (SOC) alert notification mechanism, which is driven off the syslog on the DB Networks DBN-6300.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify integration with a network-wide monitoring capability. Obtain the IP address and port number for the centralized event management system (e.g., SIEM) from site personnel. Navigate to the "Admin" tab. Click on the "External Service Settings" button. Verify the IP address and port number for the centralized event management system are implemented. If the DBN-6300 is not configured to send syslog information to a centralized event management system that manages the DBN-6300 network-wide monitoring capability, this is a finding.

## Group: SRG-NET-000334-IDPS-00191

**Group ID:** `V-237566`

### Rule: The DBN-6300 must off-load log records to a centralized log server.

**Rule ID:** `SV-237566r856502_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. This also prevents the log records from being lost if the logs stored locally are accidentally or intentionally deleted, altered, or corrupted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit records are automatically backed up on a real-time basis via syslog when enabled. Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and that the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account action. Confirm the presence of a syslog message on the syslog server containing the details of this account action. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information with the details of this account action is not there, this is a finding.

## Group: SRG-NET-000383-IDPS-00208

**Group ID:** `V-237567`

### Rule: The DBN-6300 must integrate with a network-wide monitoring capability.

**Rule ID:** `SV-237567r856503_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An integrated, network-wide intrusion detection capability increases the ability to detect and prevent sophisticated distributed attacks based on access patterns and characteristics of access. Integration is more than centralized logging and a centralized management console. The enclave's monitoring capability may include multiple sensors, IPS, sensor event databases, behavior-based monitoring devices, application-level content inspection systems, malicious code protection software, scanning tools, audit record monitoring software, and network monitoring software. Some tools may monitor external traffic while others monitor internal traffic at key boundaries. These capabilities may be implemented using different devices and therefore can have different security policies and severity-level schema. This is valuable because content filtering, monitoring, and prevention can become a bottleneck on the network if not carefully configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify integration with a network-wide monitoring capability. Obtain the IP address and port number for the centralized event management system (e.g., SIEM) from site personnel. Navigate to the "Admin" tab. Click on the "External Service Settings" button. Verify the IP address and port number for the centralized event management system are implemented. If the DBN-6300 is not configured to send syslog information to a centralized event management system that manages the DBN-6300 network-wide monitoring capability, this is a finding.

## Group: SRG-NET-000390-IDPS-00212

**Group ID:** `V-237568`

### Rule: The DBN-6300 must continuously monitor inbound communications traffic between the application tier and the database tier for unusual/unauthorized activities or conditions at the SQL level.

**Rule ID:** `SV-237568r856504_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system inbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
View the organization's documentation to determine which databases are required to be protected. Ask the site representative if the device is used continuously or if periodic monitoring is performed. Navigate to Learning >> Time Regions and view the table of detected databases. For each database requiring protection, view the "State". Unprotected databases show a red shield. Protected databases show a green shield. If continuous monitoring is not performed by the organization, this is a finding.

## Group: SRG-NET-000511-IDPS-00012

**Group ID:** `V-237569`

### Rule: The DBN-6300 must off-load log records to a centralized log server in real time.

**Rule ID:** `SV-237569r856505_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Off-loading ensures audit information is not overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. Off-loading is a common process in information systems with limited audit storage capacity. The audit storage on the IDPS is used only in a transitory fashion until the system can communicate with the centralized log server designated for storing the audit records, at which point the information is transferred. However, DoD requires that the log be transferred in real time, which indicates that the time from event detection to off-loading is seconds or less. This does not apply to audit logs generated on behalf of the device itself (management).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Audit records are automatically backed up on a real-time basis via syslog when enabled. Verify the DBN-6300 is connected to the syslog server. Navigate to Settings >> Advanced >> Syslog. Verify that the syslog services are set to "on", the syslog server information is valid, and the syslog server has connected. Navigate to Settings >> Advanced >> Audit Log. Verify that the Audit Syslog, "Use System Syslog" button is set to "Yes" and the Audit Configuration Categories are all checked for Audit Log, Syslog, and Audit Console. Following this verification, process an account action. Confirm the presence of a syslog message on the syslog server containing the details of this account action. If the DBN-6300 is not connected to the syslog server, or if the syslog server is connected but the message containing the information with the details of this account action is not there, this is a finding.

## Group: SRG-NET-000512-IDPS-00194

**Group ID:** `V-237570`

### Rule: When implemented for protection of the database tier, the DBN-6300 must be logically connected for maximum database traffic visibility.

**Rule ID:** `SV-237570r645538_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the IDPS to implement organization-wide security implementation guides and security checklists ensures compliance with federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the network element. Security-related parameters are those parameters impacting the security state of the network element, including the parameters required to satisfy other security control requirements. For the network element, security-related parameters include settings for communications traffic management configurations. If the DBN-6300 is installed incorrectly in the site's network architecture, vulnerable databases may not be detected and consequently may remain unprotected. To ensure optimum protection, the DBN-6300 must be logically installed between the application and database tiers of the network. The device has multiple interfaces that allow several connections to accommodate various network architectures. The device is installed as a passive listening device on all applicable subnetworks using the available ports. When placed correctly, the device monitors the "last mile" prior to database access, which is where SQL is optimally monitored.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site representative if the DBN-6300 is used to protect the database tier. If the DBN-6300 is not used to protect the database tier, this is not a finding. Ask the site for documentation of which database tier is required to be protected. Verify connectivity of the capture ports to the correct database tier that is required to be protected. If the DBN-6300 is not connected to protect the database tier for maximum database traffic visibility of the organization's databases, this is a finding.

## Group: SRG-NET-000512-IDPS-00194

**Group ID:** `V-237571`

### Rule: When implemented for discovery protection against unidentified or rogue databases, the DBN-6300 must provide a catalog of all visible databases and database services.

**Rule ID:** `SV-237571r645541_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the DBN-6300 is installed incorrectly in the site's network architecture, vulnerable or unknown databases may not be detected and consequently may remain vulnerable and unprotected. For proper functionality of the DBN-6300, it is necessary to examine the discovered databases to see that an expected wide variety and number of them are covered. If the DBN-6300 is not able to see and detect database services, it will not be able to monitor the databases against threats.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Ask the site representative if the DBN-6300 is used to provide discovery protection against unidentified or rogue databases. If the DBN-6300 is not used for discovery protection against unidentified or rogue databases, this is not a finding. Click on the "Database" tab and select the "Database Services" sub-menu. This will reveal all of the currently discovered database services. If the DBN-6300, which is used to provide protection against unidentified or rogue databases, does not provide a catalog of all visible databases and database services, this is a finding.

## Group: SRG-NET-000512-IDPS-00194

**Group ID:** `V-264430`

### Rule: The DBN-6300 IDPS must be using a version supported by the vendor.

**Rule ID:** `SV-264430r992087_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Systems running an unsupported software/firmware version lack current security fixes required to mitigate the risks associated with recent vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer updated. Compare the version running to the supported version by the vendor. If the system is using an unsupported version from the vendor, this is a finding.

