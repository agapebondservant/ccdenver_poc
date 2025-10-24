# STIG Benchmark: Trend Micro TippingPoint IDPS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DoD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-NET-000318-IDPS-00068

**Group ID:** `V-242167`

### Rule: To protect against unauthorized data mining, the TPS must prevent code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-242167r839140_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. TPS component(s) with the capability to prevent code injections must be included in the TPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section and type "database". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000318-IDPS-00182

**Group ID:** `V-242168`

### Rule: To protect against unauthorized data mining, the TPS must prevent code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-242168r839141_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. TPS component(s) with the capability to prevent code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". Under "Filter criteria", select all "Filter categories". 4. Select the "Filter Name" section and type "database", and select HTTP under "Filter Taxonomy Criteria as the Protocol". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000318-IDPS-00183

**Group ID:** `V-242169`

### Rule: To protect against unauthorized data mining, the TPS must prevent SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-242169r839142_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. TPS component(s) with the capability to prevent SQL code injections must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for SQL injection attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section and type "database". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000319-IDPS-00184

**Group ID:** `V-242170`

### Rule: To protect against unauthorized data mining, the TPS must detect code injection attacks launched against data storage objects, including, at a minimum, databases, database records, queries, and fields.

**Rule ID:** `SV-242170r839143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. Web applications frequently access databases to store, retrieve, and update information. An attacker can construct inputs that the database will execute. This is most commonly referred to as a code injection attack. This type of attack includes XPath and LDAP injections. TPS component(s) with anomaly detection must be included in the IDPS implementation to protect against unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for atypical database queries or accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section and type "database". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000319-IDPS-00185

**Group ID:** `V-242171`

### Rule: To protect against unauthorized data mining, the TPS must detect code injection attacks launched against application objects including, at a minimum, application URLs and application code.

**Rule ID:** `SV-242171r839144_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack applications may result in the compromise of information. Injection attacks allow an attacker to inject code into a program or query or inject malware onto a computer to execute remote commands that can read or modify a database, or change data on a website. These attacks include buffer overrun, XML, JavaScript, and HTML injections. TPS component(s) with anomaly detection must be included in the IDPS implementation. These components must include rules and anomaly detection algorithms to monitor for atypical application behavior, commands, and accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section and type "database", and select HTTP under "Filter Taxonomy Criteria as the Protocol". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000319-IDPS-00186

**Group ID:** `V-242172`

### Rule: To protect against unauthorized data mining, the TPS must detect SQL injection attacks launched against data storage objects, including, at a minimum, databases, database records, and database fields.

**Rule ID:** `SV-242172r839145_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Data mining is the analysis of large quantities of data to discover patterns and is used in intelligence gathering. Failure to detect attacks that use unauthorized data mining techniques to attack databases may result in the compromise of information. SQL injection attacks are the most prevalent attacks against web applications and databases. These attacks inject SQL commands that can read, modify, or compromise the meaning of the original SQL query. An attacker can spoof identity; expose, tamper, destroy, or make existing data unavailable; or gain unauthorized privileges on the database server. TPS component(s) with anomaly detection must be included in the IDPS implementation to monitor for and detect unauthorized data mining. These components must include rules and anomaly detection algorithms to monitor for SQL injection attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section and type "database". If the filter settings are not set for each to "Use Category Settings" or there are filter items disabled that are outside of recommended Trend Micro settings, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000018-IDPS-00018

**Group ID:** `V-242173`

### Rule: The Trend Micro TippingPoint Security Management System (SMS) must be configured to send security IPS policy to the Trend Micro Threat Protection System (TPS).

**Rule ID:** `SV-242173r840498_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The flow of all communications traffic must be monitored and controlled so it does not introduce any unacceptable risk to the network infrastructure or data. Restricting the flow of communications traffic, also known as Information flow control, regulates where information is allowed to travel as opposed to who is allowed to access the information and without explicit regard to subsequent accesses to that information. The Trend Micro SMS will include policy filters, rules, signatures, and behavior analysis algorithms that inspects and restricts traffic based on the characteristics of the information and/or the information path as it crosses internal network boundaries. The Trend Micro SMS monitors for harmful or suspicious information flows and restricts or blocks this traffic based on attribute- and content-based inspection of the source, destination, headers, and/or content of the communications traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "Default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is used, but not configured in a compliant manner, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then verify compliance with the site's SSP requirements.

## Group: SRG-NET-000019-IDPS-00187

**Group ID:** `V-242175`

### Rule: The Trend Micro TPS must immediately use updates made to policy filters, rules, signatures, and anomaly analysis algorithms for traffic detection and prevention functions which are all contained in the Digital Vaccine (DV) updates.

**Rule ID:** `SV-242175r710068_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information flow policies regarding dynamic information flow control include, for example, allowing or disallowing information flows based on changes to the PPSM CAL, vulnerability assessments, or mission conditions. Changing conditions include changes in the threat environment and detection of potentially harmful or adverse events. Changes to the TPS must take effect when made by an authorized administrator and the new configuration is put in place or committed, including upon restart or the application or reboot of the system. With some devices, the changes take effect as the configuration is changed, while with others, the new configuration must be submitted to the device. In any case, the behavior of the TPS must immediately be affected to reflect the configuration change.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Profiles" and then "Digital Vaccines". 2. Check the latest DV version that is downloaded/imported and is active. Go the Trend Micro support system located here: https://tmc.tippingpoint.com/TMC/Releases 3. Under Digital Vaccines, select the DV major version (3.2.0 currently). 4. Ensure the latest signature release is the current one that is applied to the SMS and is active to all TPS systems in the network. If the latest one is not applied as the Active DV version, this is a finding.

## Group: SRG-NET-000113-IDPS-00013

**Group ID:** `V-242176`

### Rule: The TPS must provide audit record generation capability for detection events based on implementation of policy filters, rules, signatures, and anomaly analysis.

**Rule ID:** `SV-242176r710071_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the capability to generate audit records, it would be difficult to establish, correlate, and investigate the events relating to an incident, or identify those responsible for one. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The TPS must have the capability to capture and log detected security violations and potential security violations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000113-IDPS-00082

**Group ID:** `V-242177`

### Rule: The TPS must provide audit record generation capability for events where communication traffic is blocked or restricted based on policy filters, rules, signatures, and anomaly analysis.

**Rule ID:** `SV-242177r710074_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To support the centralized analysis capability, the IDPS components must be able to provide the information in a format (e.g., Syslog) that can be extracted and used, allowing the application to effectively review and analyze the log records.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Additional Criteria" section. 5. Uncheck "permit" and "rate limit", then click Search. 6. Once the results are presented, check the "Action Set" column to filter by action type. If any items state "Block" but not "Block/Notify", this is a finding.

## Group: SRG-NET-000074-IDPS-00059

**Group ID:** `V-242178`

### Rule: The SMS must produce audit records containing sufficient information to establish what type of event occurred, including, at a minimum, event descriptions, policy filter, rule or signature invoked, port, protocol, and criticality level/alert code or description by sending all audit and system logs to a centralized syslog server.

**Rule ID:** `SV-242178r710348_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing what type of event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Associating an event type with each event log entry provides a means of investigating an attack or identifying an improperly configured TPS. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000075-IDPS-00060

**Group ID:** `V-242179`

### Rule: The SMS must produce audit records containing information to establish when (date and time) the events occurred by sending all audit and system logs to a centralized syslog server.

**Rule ID:** `SV-242179r710080_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without establishing the time (date/time) an event occurred, it would be difficult to establish, correlate, and investigate the events leading up to an outage or attack. Associating the date and time the event occurred with each event log entry provides a means of investigating an attack or identifying an improperly configured TPS. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000076-IDPS-00061

**Group ID:** `V-242180`

### Rule: The SMS must produce audit records containing information to establish where the event was detected, including, at a minimum, network segment, destination address, and TPS component which detected the event by sending all audit and system logs to a centralized syslog server.

**Rule ID:** `SV-242180r710347_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating where the event was detected with the event log entries provides a means of investigating an attack or identifying an improperly configured IDPS. This information can be used to determine what systems may have been affected. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000077-IDPS-00062

**Group ID:** `V-242181`

### Rule: The SMS must produce audit records containing information to establish the source of the event, including, at a minimum, originating source address by sending all audit and system logs to a centralized syslog server.

**Rule ID:** `SV-242181r710086_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating the source of the event with detected events in the logs provides a means of investigating an attack or suspected attack. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000078-IDPS-00063

**Group ID:** `V-242182`

### Rule: The SMS must produce audit records containing information to establish the outcome of events associated with detected harmful or potentially harmful traffic, including, at a minimum, capturing all associated communications traffic by sending all audit and system logs to a  centralized syslog server.

**Rule ID:** `SV-242182r710346_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Associating event outcome with detected events in the log provides a means of investigating an attack or suspected attack. While auditing and logging are closely related, they are not the same. Logging is recording data about events that take place in a system, while auditing is the use of log records to identify security-relevant information such as system or user accesses. In short, log records are audited to establish an accurate history. Without logging, it would be impossible to establish an audit trail. The logs should identify what servers, destination addresses, applications, or databases were potentially attacked by logging communications traffic between the target and the attacker. All commands that were entered by the attacker (such as account creations, changes in permissions, files accessed, etc.) during the session should also be logged.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000333-IDPS-00190

**Group ID:** `V-242183`

### Rule: TPS must support centralized management and configuration of the content captured in audit records generated by all TPS components by using the Security Management System (SMS).

**Rule ID:** `SV-242183r710092_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without the ability to centrally manage the content captured in the log records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an attack. Centralized management and storage of log records increases efficiency in maintenance and management of records as well as facilitates the backup and archiving of those records. The TPS must be configured to support centralized management and configuration of the content to be captured in audit records generated by all network components. IDPS sensors and consoles must have the capability to support centralized logging. They must be configured to send log messages to centralized, redundant servers and be capable of being remotely configured to change logging parameters (such as facility and severity levels).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Under the TPS serial CLI console type the following command: show sms. If the output of the command is not "Device is under SMS control", this is a finding.

## Group: SRG-NET-000334-IDPS-00191

**Group ID:** `V-242184`

### Rule: The TPS and SMS must off-load log records to a centralized log server.

**Rule ID:** `SV-242184r710095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Off-loading ensures audit information does not get overwritten if the limited audit storage capacity is reached and also protects the audit record in case the system/component being audited is compromised. This also prevents the log records from being lost if the logs stored locally are accidentally or intentionally deleted, altered, or corrupted.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000089-IDPS-00010

**Group ID:** `V-242185`

### Rule: In the event of a logging failure, caused by loss of communications with the central logging server, the SMS must queue audit records locally by using the syslog over TCP protocol until communication is restored or until the audit records are retrieved manually or using automated  synchronization tools.

**Rule ID:** `SV-242185r710345_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the TPS is at risk of failing to process audit logs as required, it takes action to mitigate the failure. Audit processing failures include: software/hardware errors, failures in the audit capturing mechanisms, and audit storage capacity being reached or exceeded. Responses to audit failure depend upon the nature of the failure. The TPS performs a critical security function, so its continued operation is imperative. Since availability of the TPS is an overriding concern, shutting down the system in the event of an audit failure should be avoided except as a last resort. The SYSLOG protocol does not support automated synchronization; however, this functionality may be provided by Network Management Systems (NMSs) which are not within the scope of this STIG.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If each syslog setting is not configured with TCP as the protocol, this is a finding.

## Group: SRG-NET-000089-IDPS-00069

**Group ID:** `V-242186`

### Rule: In the event of a logging failure caused by the lack of audit record storage capacity, the SMS must continue generating and storing audit records, overwriting the oldest audit records in a first-in-first-out manner using Audit Log maintenance.

**Rule ID:** `SV-242186r710101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical that when the TPS is at risk of failing to process audit logs as required, it takes action to mitigate the failure. The IDPS performs a critical security function, so its continued operation is imperative. Since availability of the TPS is an overriding concern, shutting down the system in the event of an audit failure should be avoided, except as a last resort.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Database". Each item in the database maintenance section has a configurable item to ensure when the newest logs will overwrite the oldest logs. This is configured through the number of rows: a. The Events log must be set to at least 30,000,000 rows, with an age of 90 days. b. The Audit Log must be set 1,000,000 rows and an age of 365 days. c. The Device Audit Log must be set 1,000,000 rows and an age of 365 days. d. The Device System Log must be set 1,000,000 rows and an age of 365 days. If these values are not set, this is a finding.

## Group: SRG-NET-000091-IDPS-00193

**Group ID:** `V-242187`

### Rule: The SMS and TPS must provide log information in a format that can be extracted and used by centralized analysis tools.

**Rule ID:** `SV-242187r710104_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Centralized review and analysis of log records from multiple SMS and TPS components gives the organization the capability to better detect distributed attacks and provides increased data points for behavior analysis techniques. These techniques are invaluable in monitoring for indicators of complex attack patterns.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device System - SMS system

## Group: SRG-NET-000131-IDPS-00011

**Group ID:** `V-242188`

### Rule: The SMS must be configured to remove or disable non-essential capabilities on SMS and TPS which are not required for operation or not related to IDPS functionality (e.g., web server, SSH, telnet, and TAXII).

**Rule ID:** `SV-242188r710107_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An IDPS can be capable of providing a wide variety of capabilities. Not all of these capabilities are necessary. Unnecessary services, functions, and applications increase the attack surface (sum of attack vectors) of a system. These unnecessary capabilities are often overlooked and therefore may remain unsecured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Devices" tab". 2. Select the Device to be modified. 3. Click "Device Configuration" and "Services". If SSH is enabled, this is a finding. Under "FIPS Settings", if the box is unchecked, this is a finding.

## Group: SRG-NET-000228-IDPS-00196

**Group ID:** `V-242189`

### Rule: The TPS must detect, at a minimum, mobile code that is unsigned or exhibiting unusual behavior, has not undergone a risk assessment, or is prohibited for use based on a risk assessment.

**Rule ID:** `SV-242189r839149_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the TPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor or locally created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To monitor for and detect known prohibited mobile code or approved mobile code that violates permitted usage requirements, the TPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". 4. Ensure the deployment mode of "default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 5. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000229-IDPS-00163

**Group ID:** `V-242190`

### Rule: The TPS must block any prohibited mobile code at the enclave boundary when it is detected.

**Rule ID:** `SV-242190r839150_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Mobile code is defined as software modules obtained from remote systems, transferred across a network, and then downloaded and executed on a local system without explicit installation or execution by the recipient. Examples of mobile code include JavaScript, VBScript, Java applets, ActiveX controls, Flash animations, Shockwave videos, and macros embedded within Microsoft Office documents. Mobile code can be exploited to attack a host. It can be sent as an e-mail attachment or embedded in other file formats not traditionally associated with executable code. While the IDPS cannot replace the anti-virus and host-based IDS (HIDS) protection installed on the network's endpoints, vendor- or locally- created sensor rules can be implemented, which provide preemptive defense against both known and zero-day vulnerabilities. Many of the protections may provide defenses before vulnerabilities are discovered and rules or blacklist updates are distributed by anti-virus or malicious code solution vendors. To block known prohibited mobile code or approved mobile code that violates permitted usage requirements, the IDPS must implement policy filters, rules, signatures, and anomaly analysis.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000235-IDPS-00169

**Group ID:** `V-242191`

### Rule: The TPS must fail to a secure state which maintains access control mechanisms when the IDPS hardware, software, or firmware fails on initialization/shutdown or experiences a sudden abort during normal operation (also known as "Fail closed").

**Rule ID:** `SV-242191r710116_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to a known safe state helps prevent systems from failing to a state that may cause loss of data or unauthorized access to system resources. Preserving information system state information also facilitates system restart and return to the operational mode of the organization with less disruption to mission-essential processes. This requirement applies to the device itself, not the network traffic. Abort refers to stopping a program or function before it has finished naturally. The term abort refers to both requested and unexpected terminations. Since it is usually not possible to test this capability in a production environment, systems should be validated either in a testing environment or prior to installation. This requirement is usually a function of the design of the TPS component. Compliance can be verified by acceptance/validation processes or vendor attestation.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Devices". 2. Select the device that will be modified, then select "Network Configuration". If any of the Intrinsic HA items state Permit All, this is a finding.

## Group: SRG-NET-000362-IDPS-00198

**Group ID:** `V-242192`

### Rule: The TPS must protect against or limit the effects of known types of Denial of Service (DoS) attacks by employing signatures.

**Rule ID:** `SV-242192r840191_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the network does not provide safeguards against DoS attack, network resources will be unavailable to users. Installation of TPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume, type, or protocol usage. Detection components that use signatures can detect known attacks by using known attack signatures. Signatures are usually obtained from and updated by the IDPS component vendor. These attacks include SYN-flood, ICMP-flood, and Land Attacks. This requirement applies to the communications traffic functionality of the IDPS as it pertains to handling communications traffic, rather than to the IDPS device itself.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select the Filter Category "Traffic Normalization, Exploits, and Vulnerabilities", select the "Filter Name" section and type "ddos". If the following filter names produced in the search list are not set to Block+Notify, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000192-IDPS-00140

**Group ID:** `V-242193`

### Rule: The TPS must block outbound traffic containing known and unknown DoS attacks by ensuring that security policies, signatures, rules, and anomaly detection techniques are applied to outbound communications traffic.

**Rule ID:** `SV-242193r710122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The TPS must include protection against DoS attacks that originate from inside the enclave which can affect either internal or external systems. These attacks may use legitimate or rogue endpoints from inside the enclave. Installation of TPS detection and prevention components (i.e., sensors) at key boundaries in the architecture mitigates the risk of DoS attacks. These attacks can be detected by matching observed communications traffic with patterns of known attacks and monitoring for anomalies in traffic volume/type. To comply with this requirement, the TPS must inspect outbound traffic for indications of known and unknown DoS attacks. Sensor log capacity management, along with techniques which prevent the logging of redundant information during an attack, also guard against DoS attacks. This requirement is used in conjunction with other requirements which require configuration of security policies, signatures, rules, and anomaly detection techniques and are applicable to both inbound and outbound traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". Under "advanced DDoS", if a DDoS filter does not exist, this is a finding.

## Group: SRG-NET-000273-IDPS-00198

**Group ID:** `V-242194`

### Rule: The TPS must block outbound ICMP Destination Unreachable, Redirect, and Address Mask reply messages.

**Rule ID:** `SV-242194r840196_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Control Message Protocol (ICMP) messages are used to provide feedback about problems in the network. These messages are sent back to the sender to support diagnostics. However, some messages can also provide host information and network topology that may be exploited by an attacker. A TPS must be configured to "silently drop" the packet and not send an ICMP control message back to the source. In some cases, it may be necessary to direct the traffic to a null interface. Three ICMP messages are commonly used by attackers for network mapping: Destination Unreachable, Redirect, and Address Mask Reply. These responses must be blocked on external interfaces; however, blocking the Destination Unreachable response will prevent Path Maximum Transmission Unit Discovery (PMTUD), which relies on the response "ICMP Destination Unreachable--Fragmentation Needed but DF Bit Set". PMTUD is a useful function and should only be "broken" after careful consideration. An acceptable alternative to blocking all Destination Unreachable responses is to filter Destination Unreachable messages generated by the IDPS to allow ICMP Destination Unreachable--Fragmentation Needed but DF Bit Set (Type 3, Code 4) and apply this filter to the external interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select all "Filter categories". Select the "Filter Name" section. If the following filter names are not set to Block+Notify, this is a finding: - 0137: ICMP: Unreachable (All codes) - 0157: ICMP: Redirect Net - 0158: ICMP: Redirect Host - 0159: ICMP: Redirect for TOS and Network - 0160: ICMP: Redirect for TOS and Host - 0161: ICMP: Redirect Undefined Code - 5084: ICMP: Address Mask Request (type 17) - 41039: ICMP: Address Mask Reply (Type 18) If there are no ICMP Destination Unreachable, Redirect, and Address Mask reply message policies defined, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000273-IDPS-00204

**Group ID:** `V-242195`

### Rule: The TPS must block malicious ICMP packets by properly configuring ICMP signatures and rules.

**Rule ID:** `SV-242195r840193_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Internet Control Message Protocol (ICMP) messages are used to provide feedback about problems in the network. These messages are sent back to the sender to support diagnostics. However, some messages can also provide host information, network topology, and a covert channel that may be exploited by an attacker. Given the prevalence of ICMP traffic on the network, monitoring for malicious ICMP traffic would be cumbersome. Vendors provide signatures and rules which filter for known ICMP traffic exploits.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Search". 4. Under "Filter criteria", select the Filter Category "Traffic Normalization, Exploits, and Vulnerabilities". Select the "Filter Name" section and type "ICMP". If the following filter names produced in the search list are not set to Block+Notify, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000251-IDPS-00178

**Group ID:** `V-242196`

### Rule: The TPS must automatically install updates to signature definitions, detection heuristics, and vendor-provided rules.

**Rule ID:** `SV-242196r710131_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failing to automatically update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. An automatic update process ensures this important task is performed without the need for system administrator intervention. The TPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, TPS components must be automatically updated, including anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. If a DoD patch management server or update repository having the tested/verified updates is available for the TPS component, the components must be configured to automatically check this server/site for updates and install new updates. If a DoD server/site is not available, the component must be configured to automatically check a trusted vendor site for updates. A trusted vendor is either commonly used by DoD, specifically approved by DoD, the vendor from which the equipment was purchased or approved by the local program's CCB.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles", and "Digital Vaccines". 2. Under "Auto DV Activation", if "Automatic Download", and "Automatic Activation" are not enabled, this is a finding.

## Group: SRG-NET-000246-IDPS-00205

**Group ID:** `V-242197`

### Rule: The SMS must install updates on the TPS for application software files, signature definitions, detection heuristics, and vendor-provided rules when new releases are available in accordance with organizational configuration management policy and procedures.

**Rule ID:** `SV-242197r754437_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Failing to update malicious code protection mechanisms, including application software files, signature definitions, and vendor-provided rules, leaves the system vulnerable to exploitation by recently developed attack methods and programs. The TPS is a key malicious code protection mechanism in the enclave infrastructure. To ensure this protection is responsive to changes in malicious code threats, IDPS components must be updated, including application software files, anti-virus signatures, detection heuristics, vendor-provided rules, and vendor-provided signatures. Updates must be installed in accordance with the CCB procedures for the local organization. However, at a minimum: 1. Updates designated as critical security updates by the vendor must be installed immediately. 2. Updates for signature definitions, detection heuristics, and vendor-provided rules must be installed immediately. 3. Updates for application software are installed in accordance with the CCB procedures. 4. Prior to automatically installing updates, either manual or automated integrity and authentication checking is required, at a minimum, for application software updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles", and "Digital Vaccines". 2. Under "Auto DV Activation" if "Automatic Download", and "Automatic Activation" are not enabled, this is a finding.

## Group: SRG-NET-000249-IDPS-00176

**Group ID:** `V-242198`

### Rule: The TPS must block malicious code.

**Rule ID:** `SV-242198r839154_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the TPS to delete and/or quarantine based on local organizational incident handling procedures minimizes the impact of this code on the network.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000248-IDPS-00206

**Group ID:** `V-242199`

### Rule: The TPS must generate a log record so an alert can be configured to, at a minimum, the system administrator when malicious code is detected.

**Rule ID:** `SV-242199r754438_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. The TPS generates an immediate (within seconds) alert which notifies designated personnel of the incident. Sending a message to an unattended log or console does not meet this requirement since that will not be seen immediately. These messages should include a severity level indicator or code as an indicator of the criticality of the incident. Satisfies: SRG-NET-000248-IDPS-00206, SRG-NET-000249-IDPS-00222, SRG-NET-000385-IDPS-00210</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Shared Settings". 2. Under "Action Sets, if "Remote Syslog", are not enabled for both the "Block+Notify" and "Block+Notify+Trace", this is a finding.

## Group: SRG-NET-000383-IDPS-00208

**Group ID:** `V-242200`

### Rule: SMS and TPS components, including sensors, event databases, and management consoles must integrate with a network-wide monitoring capability.

**Rule ID:** `SV-242200r710143_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An integrated, network-wide intrusion detection capability increases the ability to detect and prevent sophisticated distributed attacks based on access patterns and characteristics of access. Integration is more than centralized logging and a centralized management console. The enclave's monitoring capability may include multiple sensors, IPS, sensor event databases, behavior-based monitoring devices, application-level content inspection systems, malicious code protection software, scanning tools, audit record monitoring software, and network monitoring software. Some tools may monitor external traffic while others monitor internal traffic at key boundaries. These capabilities may be implemented using different devices and therefore can have different security policies and severity-level schema. This is valuable because content filtering, monitoring, and prevention can become a bottleneck on the network if not carefully configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS interface, go to the "Admin" tab, and select "Server Properties". 2. Select the "syslog" tab. If a syslog server is not configured to send the following audit logs, this is a finding: - Device Audit - Device System - SMS Audit - SMS system

## Group: SRG-NET-000384-IDPS-00209

**Group ID:** `V-242201`

### Rule: The TPS must detect network services that have not been authorized or approved by the ISSO or ISSM, at a minimum, through use of a site-approved TPS device profile.

**Rule ID:** `SV-242201r839155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Examples of network services include service-oriented architectures (SOAs), cloud-based services (e.g., infrastructure as a service, platform as a service, or software as a service), cross-domain, Voice Over Internet Protocol, Instant Messaging, auto-execute, and file sharing. To comply with this requirement, the IDPS may be configured to detect services either directly or indirectly (i.e., by detecting traffic associated with a service).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000385-IDPS-00211

**Group ID:** `V-242202`

### Rule: The IDPS must generate an alert to the ISSM and ISSO, at a minimum, when unauthorized network services are detected.

**Rule ID:** `SV-242202r839156_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or unapproved network services lack organizational verification or validation and therefore may be unreliable or serve as malicious rogues for valid services. Automated mechanisms can be used to send automatic alerts or notifications. Such automatic alerts or notifications can be conveyed in a variety of ways (e.g., telephonically, via electronic mail, via text message, or via websites). The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, then forward only validated alerts to the ISSO to the vulnerability discussion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000390-IDPS-00212

**Group ID:** `V-242203`

### Rule: The IDPS must continuously monitor inbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-242203r839157_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If inbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system inbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "Default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000391-IDPS-00213

**Group ID:** `V-242204`

### Rule: The TPS must continuously monitor outbound communications traffic for unusual/unauthorized activities or conditions.

**Rule ID:** `SV-242204r839158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If outbound communications traffic is not continuously monitored for unusual/unauthorized activities or conditions, there will be times when hostile activity may not be noticed and defended against. Although some of the components in the site's content scanning solution may be used for periodic scanning assessment, the IDPS sensors and other components must provide continuous, 24 hours a day, 7 days a week monitoring. Unusual/unauthorized activities or conditions related to information system outbound communications traffic include, for example, internal traffic that indicates the presence of malicious code within organizational information systems or propagating among system components, the unauthorized exporting of information, or signaling to external information systems. Anomalies within organizational information systems include, for example, large file transfers, long-time persistent connections, use of unusual protocols and ports, and communications with suspected or known malicious external entities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Inspection Profiles" and select the organization's profile. 2. If there is not one configured, select "Default". 3. Click "Edit Details". Ensure the deployment mode of "Default" is selected. The default deployment mode ensures all strict DoD vulnerabilities are blocked and alerted upon. 4. Navigate to "Profile Overview" and ensure the action set for each category is set to "Recommended". The recommended action set is set to ensure all suspicious and vulnerable traffic is blocked and alerted upon. If the "default" deployment mode is not configured, this is a finding. Note: If the site has set up a security profile (i.e., not using the default profile), then this should be inspected using the site's SSP for compliance.

## Group: SRG-NET-000392-IDPS-00214

**Group ID:** `V-242205`

### Rule: The TPS must send an alert to, at a minimum, the ISSM and ISSO when intrusion detection events are detected which indicate a compromise or potential for compromise.

**Rule ID:** `SV-242205r710158_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of intrusion detection incidents that require immediate action and this delay may result in the loss or compromise of information. In accordance with CCI-001242, the TPS is a real-time intrusion detection system. These systems must generate an alert when detection events from real-time monitoring occur. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, then forward only validated alerts to the ISSM and ISSO. The TPS must generate an alert to, at a minimum, the ISSM and ISSO when root level intrusion events which provide unauthorized privileged access are detected. Satisfies: SRG-NET-000392-IDPS-00214, SRG-NET-000392-IDPS-00216, SRG-NET-000392-IDPS-00218</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
1. In the Trend Micro SMS, navigate to "Profiles" and "Shared Settings". 2. Under "Action Sets", if a group email address for the ISSO is not added for both the "Block+Notify" and "Block+Notify+Trace", this is a finding.

## Group: SRG-NET-000392-IDPS-00215

**Group ID:** `V-242206`

### Rule: The site must register with the Trend Micro TippingPoint Threat Management Center (TMC) in order to receive alerts on threats identified by authoritative sources (e.g., IAVMs or CTOs) are detected which indicate a compromise or potential for compromise.

**Rule ID:** `SV-242206r710161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without an alert, security personnel may be unaware of an impending failure of the audit capability, and the ability to perform forensic analysis and detect rate-based and other anomalies will be impeded. Alerts may be transmitted, for example, telephonically, by electronic mail messages, or by text messaging. The IDPS must either send the alert to a management console that is actively monitored by authorized personnel or use a messaging capability to send the alert directly to designated personnel. The ISSM or ISSO may designate the system administrator or other authorized personnel to receive the alert within the specified time, validate the alert, then forward only validated alerts to the ISSM and ISSO.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The ISSM and ISSO must be registered to receive updates from the TMC site. If not, this is a finding.

