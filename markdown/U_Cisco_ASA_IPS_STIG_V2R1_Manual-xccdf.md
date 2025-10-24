# STIG Benchmark: Cisco ASA IPS Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000074-IDPS-00059

**Group ID:** `V-239873`

### Rule: The Cisco ASA must be configured to produce audit records containing sufficient information to establish what type of event occurred.

**Rule ID:** `SV-239873r665932_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Associating an event type with each event log entry provides a means of investigating an attack or identifying an improperly configured IDPS. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify that a logging option has been selected. Verify that the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Setting. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA is not configured to produce log records containing information to establish what type of event occurred, this is a finding.

## Group: SRG-NET-000075-IDPS-00060

**Group ID:** `V-239874`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish when the events occurred.

**Rule ID:** `SV-239874r682908_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the time (date/time) an event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Associating the date and time the event occurred with each event log entry provides a means of investigating an attack or identifying an improperly configured IDPS. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify a logging option has been selected. Verify the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Setting. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA is not configured to produce log records containing information to establish when the events occurred, this is a finding.

## Group: SRG-NET-000076-IDPS-00061

**Group ID:** `V-239875`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish where the event was detected.

**Rule ID:** `SV-239875r665938_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating where the event was detected with the event log entries provides a means of investigating an attack or identifying an improperly configured IDPS. This information can be used to determine what systems may have been affected. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify that a logging option has been selected. Verify that the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Setting. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA is not configured to produce log records containing information to establish where the event was detected, this is a finding.

## Group: SRG-NET-000077-IDPS-00062

**Group ID:** `V-239876`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish the source of the event.

**Rule ID:** `SV-239876r665941_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating the source of the event with detected events in the logs provides a means of investigating an attack or suspected attack. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify that a logging option has been selected. Verify that the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Setting. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA Firepower is not configured to produce log records containing information to establish the source of the event, this is a finding.

## Group: SRG-NET-000078-IDPS-00063

**Group ID:** `V-239877`

### Rule: The Cisco ASA must be configured to produce audit records containing information to establish the outcome of events associated with detected harmful or potentially harmful traffic.

**Rule ID:** `SV-239877r665944_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating event outcome with detected events in the log provides a means of investigating an attack or suspected attack. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The logs should identify what servers, destination addresses, applications, or databases were potentially attacked by logging communications traffic between the target and the attacker. All commands that were entered by the attacker (such as account creations, changes in permissions, files accessed, etc.) during the session should also be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify that a logging option has been selected. Verify that the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies > Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Setting. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA is not configured to produce log records containing information to establish the outcome of events associated with detected harmful or potentially harmful traffic, this is a finding.

## Group: SRG-NET-000113-IDPS-00013

**Group ID:** `V-239878`

### Rule: The Cisco ASA must be configured to log events based on policy access control rules, signatures, and anomaly analysis.

**Rule ID:** `SV-239878r665947_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The IDPS must have the capability to capture and log detected security violations and potential security violations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a Network Analysis policy exists. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click Advanced Settings. The access control policy advanced settings page appears. Step 4: Click the edit icon next to Network Analysis and Intrusion Policies. The Network Analysis and Intrusion Policies pop-up window appears. Step 5: Click Network Analysis Policy List. The Network Analysis Policy List pop-up window appears. Verify that a policy exists. By default, the system uses the Balanced Security and Connectivity network analysis policy. Note: A network analysis policy governs how traffic is decoded and preprocessed so that it can be further evaluated for anomalous traffic that might signal an intrusion attempt. An intrusion policy uses intrusion and preprocessor rules (sometimes referred to collectively as intrusion rules) to examine the decoded packets for attacks based on patterns. Both network analysis and intrusion policies are invoked by a parent access control policy. As the system analyzes traffic, the network analysis phase occurs before and separately from the intrusion prevention phase. ------------------------------------------------- Verify logging for connection events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy you want to view. The access control policy editor appears. Step 3: Click the edit icon next to a rule to view. Verify that a logging option has been selected. Verify that the Syslog check box has been selected. --------------------------------------------------- Verify logging for Intrusion events is enabled. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Intrusion Policy >> Intrusion Policy. The Intrusion Policy page appears. Step 2: Click Advanced Settings. The Advanced Settings page appears. Step 3: Verify that Syslog Alerting under External Responses is enabled. If the Cisco ASA is not configured to log events based on policy access control rules, signatures, and anomaly analysis, this is a finding.

## Group: SRG-NET-000334-IDPS-00191

**Group ID:** `V-239879`

### Rule: The Cisco ASA must be configured to off-load log records to a centralized log server.

**Rule ID:** `SV-239879r856155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. This also prevents the log records from being lost if the logs stored locally are accidentally or intentionally deleted, altered, or corrupted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a syslog server has been defined. Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies > Actions Alerts. The Alerts page appears. Step 2: Verify the IP address and port number of the syslog server. If the Cisco ASA is not configured to send log records to a centralized log server, this is a finding.

## Group: SRG-NET-000113-IDPS-00189

**Group ID:** `V-239880`

### Rule: The Cisco ASA must be configured to send log records to the syslog server for specific facility and severity level.

**Rule ID:** `SV-239880r665953_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records with a severity code it is difficult to track and handle detection events. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The IDPS must have the capability to collect and log the severity associated with the policy, rule, or signature. IDPS products often have either pre-configured and/or a configurable method for associating an impact indicator or severity code with signatures and rules, at a minimum.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Navigate to Configuration >> ASA Firepower Configuration >> Policies >> Actions Alerts. The Alerts page appears. Step 2: Verify a facility has been selected for the syslog server. If the Cisco ASA Firepower is not configured to send log records to the syslog server for specific facility and severity level, this is a finding.

## Group: SRG-NET-000089-IDPS-00010

**Group ID:** `V-239881`

### Rule: The Cisco ASA must be configured to queue log records locally In the event that the central audit server is down or not reachable.

**Rule ID:** `SV-239881r665956_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the IDPS is at risk of failing to process audit logs as required, it take action to mitigate the failure. Audit processing failures include: software/hardware errors; failures in the audit capturing mechanisms; and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure. The IDPS performs a critical security function, so its continued operation is imperative. Since availability of the IDPS is an overriding concern, shutting down the system in the event of an audit failure should be avoided, except as a last resort. The SYSLOG protocol does not support automated synchronization, however this functionality may be provided by Network Management Systems (NMSs) which are not within the scope of this SRG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that TCP is being used to send log data to the syslog server. Step 1: Navigate to Devices >> Platform Settings >> Syslog Servers. Step 2: Verify that TCP is listed under the Protocol tab has been selected. If the Cisco ASA is not configured to use TCP to send log data to the syslog server, this is a finding.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-239882`

### Rule: The Cisco ASA must be configured to block outbound traffic containing denial-of-service (DoS) attacks by ensuring an intrusion prevention policy has been applied to outbound communications traffic.

**Rule ID:** `SV-239882r991802_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The IDPS must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. Installation of IDPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. To comply with this requirement, the IDPS must inspect outbound traffic for indications of known and unknown DoS attacks. Sensor log capacity management, along with techniques that prevent the logging of redundant information during an attack, also guards against DoS attacks. This requirement is used in conjunction with other requirements which require configuration of security policies, signatures, rules, and anomaly detection techniques and are applicable to both inbound and outbound traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an intrusion policy has been applied to access control rules. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy configured for intrusion inspection using access control rules. Step 3: Click the edit icon next to the rule you want to view. The access control rule editor appears. Step 4: Verify that the rule action is set to Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a system-provided or custom intrusion policy has been selected. Note: An access control policy can have multiple access control rules associated with intrusion policies. --------------------------------------------------- Verify that the ASA is configured to redirect all traffic to the FirePOWER service module. Step 1: Verify that the FirePOWER service module has been deployed in inline mode as shown in the example below. policy-map global_policy class FIREPOWER_SFR sfr fail-open Step 2: Verify that all traffic is redirected. access-list FIREPOWER_REDIRECT extended permit ip any any … … … class-map FIREPOWER_SFR match access-list FIREPOWER_REDIRECT Note: Inbound and outbound traffic that is allowed by the ASA firewall is forwarded to the FirePOWER module. If the Cisco ASA FirePOWER module is configured in inline mode, the packet is inspected and dropped if it does not conform to access control policies. If the packet is compliant with access control policies, it is sent back to the ASA firewall for processing. If the ASA is not configured to block outbound traffic containing DoS attacks by ensuring an intrusion prevention policy has been applied to outbound communications traffic, this is a finding.

## Group: SRG-NET-000228-IDPS-00196

**Group ID:** `V-239883`

### Rule: The Cisco ASA must be configured to use Advanced Malware Protection (AMP) features to detect and block the transmission of malicious software and malware.

**Rule ID:** `SV-239883r665962_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To monitor for and detect known prohibited mobile code or approved mobile code that violates permitted usage requirements, the IDPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a file policy is applied to an access control policy. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies > Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy enabled for AMP or file control. Step 3: Click the edit icon next to the rule you want to edit. The access control rule editor appears. Step 4: Verify that the rule action is Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a file policy has been selected to inspect traffic. ------------------------------------------------- Verify that the file policy blocks malware. Step 1: Select Configuration >> ASA FirePOWER Configuration >> Policies >> Files. The File Policies page appears. Step 2: Click the edit icon next to the file policy for malware. The File Policy Rules tab appears. Step 3: Verify that application protocols have been selected or any. Note: Any detects files in HTTP, SMTP, IMAP, POP3, FTP, and NetBIOS-ssn (SMB) traffic. Step 4: Verify that the rule action is Block Malware. If the ASA is not configured to use AMP features to detect and block the transmission of malicious software and malware, this is a finding.

## Group: SRG-NET-000229-IDPS-00163

**Group ID:** `V-239884`

### Rule: The Cisco ASA must block any prohibited mobile code at the enclave boundary when it is detected.

**Rule ID:** `SV-239884r665965_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To block known prohibited mobile code or approved mobile code that violates permitted usage requirements, the IDPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a file policy is applied to an access control policy. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy enabled for AMP or file control. Step 3: Click the edit icon next to the rule you want to edit. The access control rule editor appears. Step 4: Verify that the rule action is Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a file policy has been selected to inspect traffic. ------------------------------------------------- Verify that the file policy blocks malware. Step 1: Select Configuration >> ASA FirePOWER Configuration >> Policies >> Files. The File Policies page appears. Step 2: Click the edit icon next to the file policy for malware. The File Policy Rules tab appears. Step 3: Verify that application protocols have been selected or any. Note: Any detects files in HTTP, SMTP, IMAP, POP3, FTP, and NetBIOS-ssn (SMB) traffic. Step 4: Verify that the rule action is Block Malware. If the ASA is not configured to block any prohibited mobile code at the enclave boundary, this is a finding.

## Group: SRG-NET-000246-IDPS-00205

**Group ID:** `V-239885`

### Rule: The Cisco ASA must be configured to install updates for signature definitions and vendor-provided rules.

**Rule ID:** `SV-239885r1016324_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be updated, including application software files, anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. Updates must be installed in accordance with the CCB procedures for the local organization. However, at a minimum: 1. Updates designated as critical security updates by the vendor must be installed immediately. 2. Updates for signature definitions, detection heuristics, and vendor-provided rules must be installed immediately. 3. Updates for application software are installed in accordance with the CCB procedures. 4. Prior to automatically installing updates, either manual or automated integrity and authentication checking is required, at a minimum, for application software updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Select Configuration >> ASA FirePOWER Configuration >> Updates. Step 2: Select the Rule Updates tab. The Rule Updates page appears. Step 3: Verify that Enable Recurring Rule Update Imports has been selected. Step 4: Verify that Daily, Weekly, or Monthly has been selected in the Import Frequency field. Step 5: Verify that the following have been selected: - Reapply intrusion policies after the rule update import completes - Reapply access control policies after the rule update import completes Note: The Cisco Vulnerability Database (VDB) is a database of known vulnerabilities to which hosts may be susceptible. The Cisco Vulnerability Research Team (VRT) issues periodic updates to the VDB. Verify with the ASA administrator that product updates are installed on a regular basis. If the ASA is not configured to install updates for signature definitions and vendor-provided rules, this is a finding.

## Group: SRG-NET-000249-IDPS-00176

**Group ID:** `V-239886`

### Rule: The Cisco ASA must be configured to block malicious code.

**Rule ID:** `SV-239886r665971_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the IDPS to delete and/or quarantine based on local organizational incident handling procedures minimizes the impact of this code on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that a file policy is applied to an access control policy. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy enabled for AMP or file control. Step 3: Click the edit icon next to the rule you want to edit. The access control rule editor appears. Step 4: Verify that the rule action is Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a file policy has been selected to inspect traffic. ------------------------------------------------- Verify that the file policy blocks malware. Step 1: Select Configuration >> ASA FirePOWER Configuration >> Policies >> Files. The File Policies page appears. Step 2: Click the edit icon next to the file policy for malware. The File Policy Rules tab appears. Step 3: Verify that application protocols have been selected or any. Note: Any detects files in HTTP, SMTP, IMAP, POP3, FTP, and NetBIOS-ssn (SMB) traffic. Step 4: Verify that the rule action is Block Malware. If the ASA is not configured to block malicious code, this is a finding.

## Group: SRG-NET-000249-IDPS-00221

**Group ID:** `V-239887`

### Rule: The Cisco ASA must be configured to block traffic from IP addresses that have a known bad reputation based on the latest reputation intelligence.

**Rule ID:** `SV-239887r665974_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the network element to delete and/or quarantine based on local organizational incident handling procedures minimizes the impact of this code on the network. Malicious code includes, but is not limited to, viruses, worms, trojan horses, and spyware. The code provides the ability for a malicious user to read from and write to files and folders on a computer's hard drive. Malicious code may also be able to run and attach programs, which may allow the unauthorized distribution of malicious mobile code. Sometimes it is necessary to generate a log event and then automatically delete the malicious code; however, for critical attacks or where forensic evidence is deemed necessary, the preferred action is for the file to be quarantined for further investigation. This requirement is limited to network elements that perform security functions, such as ALG and IDPS.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Object Management. Step 2: Click the Security Intelligence tab. Step 3: Next to the Intelligence Feed, click the edit icon. Step 4: Verify that a frequency has been selected and not disabled. Note: The Security Intelligence block listing feature is the easiest method to maintain a blacklist. Security Intelligence uses reputation intelligence to quickly block connections to or from IP addresses, URLs, and domain names. The Intelligence Feed, which tracks IP addresses representing security threats such as malware, spam, botnets, and phishing. Because the Intelligence Feed is regularly updated, using it ensures that the system uses up-to-date information to filter malicious network traffic. If the ASA is not configured to block traffic from IP addresses that have a known bad reputation based on the latest reputation intelligence, this is a finding.

## Group: SRG-NET-000249-IDPS-00222

**Group ID:** `V-239888`

### Rule: The Cisco ASA must be configured to send an alert to organization-defined personnel and/or the firewall administrator when malicious code is detected.

**Rule ID:** `SV-239888r665977_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. The IDPS generates an immediate (within seconds) alert which notifies designated personnel of the incident. Sending a message to an unattended log or console does not meet this requirement since that will not be seen immediately. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. The ISSM or ISSO may designate the firewall administrator and/or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify email server and email addresses have been defined. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: From the Create Alert drop-down menu, choose Create Email Alert. Step 3: Verify the email address is that of the system administrator. ---------------------------------------- Verify that Advanced Malware Protection is configured to generate alerts. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: Click the Advanced Malware Protections Alerts tab. Step 3: In the Alerts section, verify that an email alert has been selected. Note: The above example is using the Firepower Management Center. If the ASA is not configured to send an alert to organization-defined personnel and/or the firewall administrator when malicious code is detected, this is a finding.

## Group: SRG-NET-000251-IDPS-00178

**Group ID:** `V-239889`

### Rule: The Cisco ASA must be configured to automatically install updates to signature definitions and vendor-provided rules.

**Rule ID:** `SV-239889r1016325_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to automatically update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. An automatic update process ensures this important task is performed without the need for system administrator intervention. The IDPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be automatically updated, including anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. If a DOD patch management server or update repository having the tested/verified updates is available for the IDPS component, the components must be configured to automatically check this server/site for updates and install new updates. If a DOD server/site is not available, the component must be configured to automatically check a trusted vendor site for updates. A trusted vendor is either commonly used by DOD, specifically approved by DOD, the vendor from which the equipment was purchased, or approved by the local program's CCB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Step 1: Select Configuration >> ASA FirePOWER Configuration >> Updates. Step 2: Select the Rule Updates tab. The Rule Updates page appears. Step 3: Verify that Enable Recurring Rule Update Imports has been selected. Step 4: Verify that Daily, Weekly, or Monthly has been selected in the Import Frequency field. Step 5: Verify that the following have been selected: - Reapply intrusion policies after the rule update import completes - Reapply access control policies after the rule update import completes Note: The Cisco Vulnerability Database (VDB) is a database of known vulnerabilities to which hosts may be susceptible. The Cisco Vulnerability Research Team (VRT) issues periodic updates to the VDB. Verify with the ASA administrator that product updates are installed on a regular basis. If the ASA is not configured to install updates for signature definitions and vendor-provided rules, this is a finding.

## Group: SRG-NET-000390-IDPS-00212

**Group ID:** `V-239890`

### Rule: The Cisco ASA must be configured to block inbound traffic containing unauthorized activities or conditions.

**Rule ID:** `SV-239890r856156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system inbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an intrusion policy has been applied to access control rules. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy configured for intrusion inspection using access control rules. Step 3: Click the edit icon next to the rule you want to view. The access control rule editor appears. Step 4: Verify that the rule action is set to Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a system-provided or custom intrusion policy has been selected. Note: An access control policy can have multiple access control rules associated with intrusion policies. --------------------------------------------------- Verify that the ASA is configured to redirect all traffic to the FirePOWER service module. Step 1: Verify that the FirePOWER service module has been deployed in inline mode as shown in the example below. policy-map global_policy class FIREPOWER_SFR sfr fail-open Step 2: Verify that all traffic is redirected. access-list FIREPOWER_REDIRECT extended permit ip any any … … … class-map FIREPOWER_SFR match access-list FIREPOWER_REDIRECT Note: Inbound and outbound traffic that is allowed by the ASA firewall is forwarded to the FirePOWER module. If the Cisco ASA FirePOWER module is configured in inline mode, the packet is inspected and dropped if it does not conform to access control policies. If the packet is compliant with access control policies, it is sent back to the ASA firewall for processing. If the ASA is not configured to block inbound traffic containing unauthorized activities or conditions, this is a finding.

## Group: SRG-NET-000391-IDPS-00213

**Group ID:** `V-239891`

### Rule: The Cisco ASA must be configured to block outbound traffic containing unauthorized activities or conditions.

**Rule ID:** `SV-239891r856157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system outbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify that an intrusion policy has been applied to access control rules. Step 1: Navigate to Configuration >> ASA FirePOWER Configuration >> Policies >> Access Control Policy. The Access Control Policy page appears. Step 2: Click the edit icon next to the access control policy configured for intrusion inspection using access control rules. Step 3: Click the edit icon next to the rule you want to view. The access control rule editor appears. Step 4: Verify that the rule action is set to Interactive Block or Interactive Block with reset. Step 5: Select the Inspection tab. The Inspection tab appears. Step 6: Verify that a system-provided or custom intrusion policy has been selected. Note: An access control policy can have multiple access control rules associated with intrusion policies. --------------------------------------------------- Verify that the ASA is configured to redirect all traffic to the FirePOWER service module. Step 1: Verify the FirePOWER service module has been deployed in inline mode as shown in the example below. policy-map global_policy class FIREPOWER_SFR sfr fail-open Step 2: Verify all traffic is redirected. access-list FIREPOWER_REDIRECT extended permit ip any any … … … class-map FIREPOWER_SFR match access-list FIREPOWER_REDIRECT Note: Inbound and outbound traffic that is allowed by the ASA firewall is forwarded to the FirePOWER module. If the Cisco ASA FirePOWER module is configured in inline mode, the packet is inspected and dropped if it does not conform to access control policies. If the packet is compliant with access control policies, it is sent back to the ASA firewall for processing. If the ASA is not configured to block outbound traffic containing unauthorized activities or conditions, this is a finding.

## Group: SRG-NET-000392-IDPS-00214

**Group ID:** `V-239892`

### Rule: The Cisco ASA must be configured to send an alert to organization-defined personnel and/or the firewall administrator when intrusion events are detected.

**Rule ID:** `SV-239892r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of intrusion detection incidents that require immediate action and this delay may result in the loss or compromise of information. In accordance with CCI-001242, the IDPS is a real-time intrusion detection system. These systems must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the firewall administrator and/or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify email server and email addresses have been defined. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: From the Create Alert drop-down menu, choose Create Email Alert. Step 3: Verify that the email address is that of organization-defined personnel and/or the firewall administrator. If the Cisco ASA is not configured to send an alert to organization-defined personnel and/or the firewall administrator when intrusion events are detected, this is a finding.

## Group: SRG-NET-000392-IDPS-00215

**Group ID:** `V-239893`

### Rule: The Cisco ASA must be configured to send an alert to organization-defined personnel and/or the firewall administrator when threats are detected.

**Rule ID:** `SV-239893r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the firewall administrator and/or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify email server and email addresses have been defined. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: From the Create Alert drop-down menu, choose Create Email Alert. Step 3: Verify that the email address is that of organization-defined personnel and/or the firewall administrator. If the Cisco ASA is not configured to send an alert to organization-defined personnel and/or firewall administrator when threats are detected, this is a finding.

## Group: SRG-NET-000392-IDPS-00218

**Group ID:** `V-239894`

### Rule: The Cisco ASA must be configured to send an alert to organization-defined personnel and/or the firewall administrator when DoS incidents are detected.

**Rule ID:** `SV-239894r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alerts messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the firewall administrator and/or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify email server and email addresses have been defined. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: From the Create Alert drop-down menu, choose Create Email Alert. Step 3: Verify that the email address is that of organization-defined personnel and/or the firewall administrator. If the Cisco ASA is not configured to send an alert to organization-defined personnel and/or the firewall administrator when DoS incidents are detected, this is a finding.

## Group: SRG-NET-000392-IDPS-00219

**Group ID:** `V-239895`

### Rule: The Cisco ASA must generate an alert to organization-defined personnel and/or the firewall administrator when active propagation of malware or malicious code is detected.

**Rule ID:** `SV-239895r971533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of major detection incidents that require immediate action and this delay may result in the loss or compromise of information. CJCSM 6510.01B, "Cyber Incident Handling Program", lists nine Cyber Incident and Reportable Event Categories. DoD has determined that categories identified by CJCSM 6510.01B Major Indicators (category I, II, IV, and VII detection events) will require an alert when an event is detected. Alerts messages must include a severity level indicator or code as an indicator of the criticality of the incident. Since these incidents require immediate action, these messages are assigned a critical or level 1 priority/severity, depending on the system's priority schema. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the firewall/system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, and then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify email server and email addresses have been defined. Step 1: Navigate to Policies >> Actions >> Alerts. Step 2: From the Create Alert drop-down menu, choose Create Email Alert. Step 3: Verify that the email address is that of organization-defined personnel and/or the firewall administrator. If the Cisco ASA is not configured to send an alert to organization-defined personnel and/or the firewall administrator when active propagation of malware or malicious code is detected, this is a finding.

