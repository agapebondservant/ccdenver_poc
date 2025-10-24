# STIG Benchmark: IBM MQ Appliance V9.0 AS Security Technical Implementation Guide

---

**Version:** 1

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000080-AS-000045

**Group ID:** `V-255775`

### Rule: The MQ Appliance messaging server must protect against an individual (or process acting on behalf of an individual) falsely denying having performed organization-defined actions to be covered by non-repudiation.

**Rule ID:** `SV-255775r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Non-repudiation of actions taken is required in order to messaging service application integrity. Examples of particular actions taken by individuals include creating information, sending a message, approving information (e.g., indicating concurrence or signing a contract), and receiving a message. Non-repudiation protects individuals against later claims by an author of not having authored a particular document, a sender of not having transmitted a message, a receiver of not having received a message, or a signatory of not having signed a document. Typical messaging server actions requiring non-repudiation will be related to application deployment among developers/users and administrative actions taken by admin personnel.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To run the "runmqsc [queue mgr name]" command for each running queue manager enter: DIS QMGR EVENT A list of all events will be displayed along with an indication if event logging is enabled. The events are as follows: Authority: AUTHOREV, Inhibit: INHIBITEV, Local: LOCALEV, Remote: REMOTEEV, Start and stop: STRSTPEV, Performance: PERFMEV, Command: CMDEV, Channel: CHLEV, Channel auto definition: CHADEV, SSL: SSLEV, Configuration: CONFIGEV If AUTHOREV event logging is not enabled, this is a finding.

## Group: SRG-APP-000015-AS-000010

**Group ID:** `V-255776`

### Rule: The MQ Appliance messaging server must implement cryptography mechanisms to protect the integrity of the remote access session.

**Rule ID:** `SV-255776r960762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is critical for protection of remote access sessions. If encryption is not being used for integrity, malicious users may gain the ability to modify the messaging server configuration. The use of cryptography for ensuring integrity of remote access sessions mitigates that risk. Messaging servers utilize a web management interface and scripted commands when allowing remote access. Web access requires the use of TLS and scripted access requires using ssh or some other form of approved cryptography. Messaging servers must have a capability to enable a secure remote admin capability. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. FIPS 140-2 approved TLS versions must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. Satisfies: SRG-APP-000015-AS-000010, SRG-APP-000126-AS-000085, SRG-APP-000231-AS-000133, SRG-APP-000231-AS-000156, SRG-APP-000428-AS-000265, SRG-APP-000429-AS-000157, SRG-APP-000441-AS-000258, SRG-APP-000442-AS-000259</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain queue security policy requirements from system admin. To verify the Advanced Message Security (AMS) policy for a specific queue manager's queues, enter: mqcli To list the policies for each queue, enter: runmqsc [QMgrName] To display all policies, enter: DIS POLICY(*) If no security policies are found or the specifics of the security policy does not meet documented queue security requirements, this is a finding.

## Group: SRG-APP-000358-AS-000064

**Group ID:** `V-255777`

### Rule: The MQ Appliance messaging server must off-load log records onto a different system or media from the system being logged.

**Rule ID:** `SV-255777r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Log record content that may be necessary to satisfy the requirement of this control includes, but is not limited to, time stamps, source and destination IP addresses, user/process identifiers, event descriptions, application-specific events, success/fail indications, filenames involved, access control or flow control rules invoked. Off-loading is a common process in information systems with limited log storage capacity. Centralized management of log records provides for efficiency in maintenance and management of records, as well as the backup and archiving of those records. Messaging servers and their related components are required to off-load log records onto a different system or media than the system being logged. An HA configuration provides real-time synchronous replication of the logs to a mirrored MQ Appliance.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system categorization to determine if redundancy is a requirement. If system categorization does not specify redundancy, interview system administrator to determine how they have configured the MQ appliance to off-load log files onto a different system. Perform on each member of the HA pair. To access the MQ Appliance CLI, enter: mqcli dspmq -s -o ha One of the appliances should be running as primary, the other as secondary. If HA is not configured with the primary and secondary running, or if there is no mechanism implemented to off-load log records, this is a finding.

## Group: SRG-APP-000372-AS-000212

**Group ID:** `V-255778`

### Rule: The MQ Appliance messaging server must synchronize internal MQ Appliance messaging server clocks to an authoritative time source when the time difference is greater than the organization-defined time period.

**Rule ID:** `SV-255778r981686_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronization of internal messaging server clocks is needed in order to correctly correlate the timing of events that occur across multiple systems. To meet this requirement, the organization will define an authoritative time source and have each system synchronize when the time difference is greater than a defined time period. The industry standard for the threshold is 1ms.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on as a privileged user to the WebGUI. Select Network icon. Interface NTP Service. Verify that refresh interval is set to "600" seconds. If refresh interval is not set to "600" seconds, this is a finding.

## Group: SRG-APP-000371-AS-000077

**Group ID:** `V-255779`

### Rule: The MQ Appliance messaging server must compare internal MQ Appliance messaging server clocks at least every 24 hours with an authoritative time source.

**Rule ID:** `SV-255779r981685_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Determining the correct time a particular application event occurred on a system is critical when conducting forensic analysis and investigating system events. Synchronization of system clocks is needed in order to correctly correlate the timing of events that occur across multiple systems. To meet this requirement, the organization will define an authoritative time source and have each system compare its internal clock at least every 24 hours.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on as a privileged user to the WebGUI. Select Network icon. Interface NTP Service. Verify: - NTP server destinations are configured. - "Enable Administrative state" box is checked. If "Enable Administrative state" is not checked or if no NTP servers are defined, this is a finding.

## Group: SRG-APP-000416-AS-000140

**Group ID:** `V-255780`

### Rule: The MQ Appliance messaging server must implement NSA-approved cryptography to protect classified information in accordance with applicable federal laws, Executive Orders, directives, policies, regulations, and standards.

**Rule ID:** `SV-255780r962034_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Cryptography is only as strong as the encryption modules/algorithms employed to encrypt the data. Use of weak or untested encryption algorithms undermines the purposes of utilizing encryption to protect data. NSA has developed Type 1 algorithms for protecting classified information. The Committee on National Security Systems (CNSS) National Information Assurance Glossary (CNSS Instruction No. 4009) defines Type 1 products as: "Cryptographic equipment, assembly or component classified or certified by NSA for encrypting and decrypting classified and sensitive national security information when appropriately keyed. Developed using established NSA business processes and containing NSA-approved algorithms are used to protect systems requiring the most stringent protection mechanisms." NSA-approved cryptography is required to be used for classified information system processing. The messaging server must utilize NSA-approved encryption modules when protecting classified data. This means using AES and other approved encryption modules.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication has been completed successfully by using DISPLAY commands. If the task was successful, the resulting output is like that shown in the following examples. For queue manager to queue manager connections: From queue manager [QM1], enter the following command: DISPLAY CHS(TO.[QM2]) SSLPEER SSLCERTI The resulting output should be like the following example: DISPLAY CHSTATUS(TO.[QM2]) SSLPEER SSLCERTI 4 : DISPLAY CHSTATUS(TO.[QM2]) SSLPEER SSLCERTI AMQ8417: Display Channel Status details. CHANNEL(TO.[QM2]) CHLTYPE(SDR) CONNAME([IP addr QM2]) CURRENT RQMNAME([QM2]) SSLCERTI("[distinguished name]") SSLPEER("[distinguished name]") STATUS(RUNNING) SUBSTATE(MQGET) XMITQ([QM2]) From the queue manager [QM2], enter the following command: DISPLAY CHS(TO.QM2) SSLPEER SSLCERTI The resulting output is like the following example: DISPLAY CHSTATUS(TO.[QM2]) SSLPEER SSLCERTI 5 : DISPLAY CHSTATUS(TO.[QM2]) SSLPEER SSLCERTI AMQ8417: Display Channel Status details. CHANNEL(TO.[QM2]) CHLTYPE(SDR) CONNAME([IP addr QM1]) CURRENT RQMNAME([QM1]) SSLCERTI("[distinguished name]") SSLPEER("[distinguished name]") STATUS(RUNNING) SUBSTATE(MQGET) XMITQ( ) In each case, the value of "SSLPEER" must match that of the Distinguished Name (DN) in the partner certificate. The issuer name must match the subject DN of the CA certificate that signed the personal certificate. For client to queue manager connections: C1=client1, QM1=queue manager 1 From the queue manager [QM1], enter the following command: DISPLAY CHSTATUS([C1].TO.[QM1]) SSLPEER SSLCERTI The resulting output is like the following example: DISPLAY CHSTATUS([C1].TO.[QM1]) SSLPEER SSLCERTI 5 : DISPLAY CHSTATUS([C1].TO.[QM1]) SSLPEER SSLCERTI AMQ8417: Display Channel Status details. CHANNEL([C1].TO.[QM1]) CHLTYPE(SVRCONN) CONNAME([IP addr QM1]) CURRENT SSLCERTI("[distinguished name]") SSLPEER("[distinguished name]") STATUS(RUNNING) SUBSTATE(RECEIVE) The "SSLPEER" field in the "DISPLAY CHSTATUS" output shows the subject DN of the remote client certificate. The issuer name matches the subject DN of the CA certificate that signed the personal certificate. If the connections on each end of the channel are not configured as described above, this is a finding.

## Group: SRG-APP-000400-AS-000246

**Group ID:** `V-255781`

### Rule: The MQ Appliance WebGUI interface to the messaging server must prohibit the use of cached authenticators after one hour.

**Rule ID:** `SV-255781r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the messaging server is using PKI authentication, a local revocation cache must be stored for instances when the revocation cannot be authenticated through the network, but if cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Display the SSL Server Profile associated with the WebGUI using the (CLI). Log on as an admin to the MQ appliance using SSH terminal access. Enter: co show web-mgmt To note the name of the ssl-server, enter: crypto ssl-server <ssl-server name> show Verify the following are displayed: caching on cache-timeout 3600 If the ssl-server configuration does not exist, or if caching is "off", or if the cache-timeout setting does not equal “3600” seconds (60 minutes), this is a finding.

## Group: SRG-APP-000095-AS-000056

**Group ID:** `V-255782`

### Rule: The MQ Appliance messaging server must produce log records containing information to establish what type of events occurred.

**Rule ID:** `SV-255782r960891_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information system logging capability is critical for accurate forensic analysis. Without being able to establish what type of event occurred, it would be difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible. Log record content that may be necessary to satisfy the requirement of this control includes time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked. Messaging servers must log all relevant log data that pertains to the messaging server. Examples of relevant data include, but are not limited to, Java Virtual Machine (JVM) activity, HTTPD/Web server activity, and messaging server-related system process activity. Satisfies: SRG-APP-000095-AS-000056, SRG-APP-000093-AS-000054, SRG-APP-000096-AS-000059, SRG-APP-000097-AS-000060, SRG-APP-000098-AS-000061, SRG-APP-000099-AS-000062, SRG-APP-000100-AS-000063, SRG-APP-000101-AS-000072</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Apply the following check to each queue manager on the MQ Appliance. Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To check config for each queue, enter: runmqsc [queue mgr name] At the runmqsc prompt, enter: DIS QMGR EVENT Verify the following events are enabled as required. AUTHOREV, INHIBITEV, STRSTPEV, CMDEV, SSLEV, CONFIGEV, PERFMEV If any of the required events are not enabled, this is a finding.

## Group: SRG-APP-000266-AS-000168

**Group ID:** `V-255783`

### Rule: The MQ Appliance messaging server must identify potentially security-relevant error conditions.

**Rule ID:** `SV-255783r961167_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The structure and content of error messages need to be carefully considered by the organization and development team. Any application providing too much information in error logs and in administrative messages to the screen risks compromising the data and security of the application and system. The extent to which the messaging server is able to identify and handle error conditions is guided by organizational policy and operational requirements. Adequate logging levels and system performance capabilities need to be balanced with data protection requirements. The structure and content of error messages needs to be carefully considered by the organization and development team. Messaging servers must have the capability to log at various levels which can provide log entries for potential security-related error events. An example is the capability for the messaging server to assign a criticality level to a failed logon attempt error message, a security-related error message being of a higher criticality. Instructions for using the amqsevt sample program to display instrumentation events may be found at the following URL: https://ibm.biz/BdsCzY. Satisfies: SRG-APP-000266-AS-000168, SRG-APP-000091-AS-000052</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq Run the "runmqsc [queue mgr name]" command for each running queue manager. Once at the runmqsc prompt, enter: DIS QMGR AUTHOREV AUTHOREV(ENABLED) - should be the result. If "AUTHOREV" logging is not "ENABLED", this is a finding.

## Group: SRG-APP-000343-AS-000030

**Group ID:** `V-255784`

### Rule: The MQ Appliance messaging server must provide access logging that ensures users who are granted a privileged role (or roles) have their privileged activity logged.

**Rule ID:** `SV-255784r961362_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In order to be able to provide a forensic history of activity, the messaging server must ensure users who are granted a privileged role or those who utilize a separate distinct account when accessing privileged functions or data have their actions logged. If privileged activity is not logged, no forensic logs can be used to establish accountability for privileged actions that occur on the system. Instructions for using the amqsevt sample program to display instrumentation events may be found at the following URL: https://ibm.biz/BdsCzY Satisfies: SRG-APP-000343-AS-000030, SRG-APP-000016-AS-000013, SRG-APP-000495-AS-000220, SRG-APP-000499-AS-000224, SRG-APP-000503-AS-000228, SRG-APP-000504-AS-000229, SRG-APP-000509-AS-000234</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each queue manager on the MQ Appliance for which configuration events logging should be enabled, establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To run the "runmqsc [queue mgr name]" command for each running queue manager, enter: runmqsc [queue mgr name] DIS QMGR CONFIGEV CONFIGEV(ENABLED) - should be the result. end If "CONFIGEV" is not "ENABLED", this is a finding.

## Group: SRG-APP-000108-AS-000067

**Group ID:** `V-255785`

### Rule: The MQ Appliance messaging server must alert the SA and ISSO, at a minimum, in the event of a log processing failure.

**Rule ID:** `SV-255785r960912_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Logs are essential to monitor the health of the system, investigate changes that occurred to the system, or investigate a security incident. When log processing fails, the events during the failure can be lost. To minimize the timeframe of the log failure, an alert needs to be sent to the SA and ISSO at a minimum. Log processing failures include, but are not limited to, failures in the messaging server log capturing mechanisms or log storage capacity being reached or exceeded. In some instances, it is preferred to send alarms to individuals rather than to an entire group. Messaging servers must be able to trigger an alarm and send an alert to, at a minimum, the SA and ISSO in the event there is a messaging server log processing failure. It is the responsibility of the MQ system administrator to monitor the SYSTEM.ADMIN.PERFM.EVENT queue and provide appropriate notification. All MQ installations provide a sample program, amqsevt. This program reads messages from event queues, and formats them into readable strings. An event logging failure would be indicated by one of the following return codes: MQRC_Q_FULL, MQRC_Q_MGR_NOT_ACTIVE, or MQRC_Q_DEPTH_HIGH Note: Any MQ monitoring solution that connects to MQ as a client may be used to monitor event queues. Satisfies: SRG-APP-000108-AS-000067, SRG-APP-000360-AS-000066</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each queue manager on the MQ Appliance for which performance events logging should be enabled, establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To run the "runmqsc [queue mgr name]" command for each running queue manager identified, enter: runmqsc [queue mgr name] DIS QMGR PERFMEV DIS QLOCAL(SYSTEM.ADMIN.PERFM.EVENT) QDPHIEV end If "QDPHIEV" or "PERFMEV" is not "ENABLED", this is a finding. Ask the system administrator to demonstrate how they monitor an alert on MQ failure events. Verify alarming is set for the following log events: MQRC_Q_FULL, MQRC_Q_MGR_NOT_ACTIVE, MQRC_Q_DEPTH_HIGH If the system admin does not monitor an alarm for the following error codes: MQRC_Q_FULL, MQRC_Q_MGR_NOT_ACTIVE, or MQRC_Q_DEPTH_HIGH, this is a finding.

## Group: SRG-APP-000359-AS-000065

**Group ID:** `V-255786`

### Rule: The MQ Appliance messaging server must provide an immediate warning to the SA and ISSO, at a minimum, when allocated log record storage volume reaches 75% of maximum log record storage capacity.

**Rule ID:** `SV-255786r961398_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process logs as required. Log processing failures include software/hardware errors, failures in the log capturing mechanisms, and log storage capacity being reached or exceeded. Notification of the storage condition will allow administrators to take actions so that logs are not lost. This requirement can be met by configuring the messaging server to utilize a dedicated logging tool that meets this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
For each queue manager on the MQ Appliance for which performance events logging should be enabled, establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To run the "runmqsc [queue mgr name]" command for each running queue manager identified, enter: runmqsc [queue mgr name] DIS QMGR PERFMEV DIS QLOCAL(SYSTEM.ADMIN.PERFM.EVENT) QDPHIEV end If "QDEPTHHI" is not "75", this is a finding. Ask the system administrator to demonstrate how they monitor an alert on MQ failure events. Verify alarming is set for the following log events: MQRC_Q_FULL, MQRC_Q_MGR_NOT_ACTIVE, MQRC_Q_DEPTH_HIGH If the system admin does not monitor an alarm for the following error codes: MQRC_Q_FULL, MQRC_Q_MGR_NOT_ACTIVE, or MQRC_Q_DEPTH_HIGH, this is a finding.

## Group: SRG-APP-000435-AS-000163

**Group ID:** `V-255787`

### Rule: The MQ Appliance messaging server must protect against or limit the effects of all types of Denial of Service (DoS) attacks by employing operationally-defined security safeguards.

**Rule ID:** `SV-255787r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>DoS is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. To reduce the possibility or effect of a DoS, the messaging server must employ defined security safeguards. These safeguards will be determined by the placement of the messaging server and the type of applications being hosted within the messaging server framework. There are many examples of technologies that exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy or clustering, may reduce the susceptibility to some DoS attacks. Note: IBM recommends that neither MQ server nor the MQ Appliance be placed in the DMZ where it could be vulnerable to DoS attacks. IBM recommends that this protection be provided by a firewall: https://ibm.biz/BdraMj For internal queue managers, You can restrict the total number of incoming connections by setting the MaxConnectionThreads property: https://ibm.biz/BdraMZ Satisfies: SRG-APP-000435-AS-000163, SRG-APP-000001-AS-000001</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Obtain documentation that specifies operational limits from system admin. Check the "SVRCONN" channels of each queue manager to confirm that "MAXINST" and "MAXINSTC" values are set to a value that reflects operational requirements. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq To run the "runmqsc [queue mgr name]" command for each running queue manager identified, enter: runmqsc [queue mgr name] To display available SVRCONN channels details, enter: DIS CHANNEL(*) CHLTYPE(SVRCONN) Display values for each channel: DIS CHANNEL(Channel Name) If the value of either "MAXINST" or "MAXINSTC" is greater than the organization-defined limit, this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-255788`

### Rule: The MQ Appliance messaging server must automatically terminate a SSH user session after organization-defined conditions or trigger events requiring a session disconnect.

**Rule ID:** `SV-255788r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of CLI user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the messaging server must be configured to close the sessions when a configured condition or trigger event is met. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli show rbm Verify that the cli-timeout displays the approved timeout value of 600 seconds (10 minutes) or less. If it does not, this is a finding.

## Group: SRG-APP-000295-AS-000263

**Group ID:** `V-255789`

### Rule: The MQ Appliance must automatically terminate a WebGUI user session after 600 seconds of idle time.

**Rule ID:** `SV-255789r961221_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An attacker can take advantage of WebGUI user sessions that are left open, thus bypassing the user authentication process. To thwart the vulnerability of open and unused user sessions, the messaging server must be configured to close the sessions when a configured condition or trigger event is met. Session termination terminates all processes associated with a user's logical session except those processes that are specifically created by the user (i.e., session owner) to continue after the session is terminated. Conditions or trigger events requiring automatic session termination can include, for example, periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on information system use.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the MQ Appliance CLI as a privileged user. To access the MQ Appliance CLI, enter: mqcli To enter configuration mode, enter: co web-mgmt show If the idle-timeout value is not "600" seconds or less, this is a finding.

## Group: SRG-APP-000400-AS-000246

**Group ID:** `V-255790`

### Rule: The MQ Appliance SSH interface to the messaging server must prohibit the use of cached authenticators after 600 seconds.

**Rule ID:** `SV-255790r961521_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When the messaging server is using PKI authentication, a local revocation cache must be stored for instances when the revocation cannot be authenticated through the network, but if cached authentication information is out of date, the validity of the authentication information may be questionable.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the MQ Appliance WebGUI, Go to Administration (gear icon) >> Access >> RBM Settings. Verify that cache setting is defined and specifies "600" seconds. If the time period is not set to "600" seconds, this is a finding.

## Group: SRG-APP-000427-AS-000264

**Group ID:** `V-255791`

### Rule: The MQ Appliance messaging server must only allow the use of DoD PKI-established certificate authorities for verification of the establishment of protected (messaging) sessions.

**Rule ID:** `SV-255791r961596_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DoD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DoD-approved CA, trust of this CA has not been established. The DoD will only accept PKI certificates obtained from a DoD-approved internal or external certificate authority. Reliance on CAs for the establishment of secure sessions includes, for example, the use of SSL/TLS certificates. The messaging server must only allow the use of DoD PKI-established certificate authorities for verification.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the MQ Appliance WebGUI, click on the Administration (gear) icon. Click on Main >> File Management. Click on the cert directory. Click on the "Details" action to the right of each cert to display its attributes. Verify that each certificate attribute meets organizationally approved requirements. If any certificates have not been issued by a DoD- or CNSS-approved PKI CA, this is a finding.

## Group: SRG-APP-000456-AS-000266

**Group ID:** `V-255792`

### Rule: The version of MQ Appliance messaging server running on the system must be a supported version.

**Rule ID:** `SV-255792r1001151_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Security flaws with software applications are discovered daily. Vendors are constantly updating and patching their products to address newly discovered security vulnerabilities. Organizations (including any contractor to the organization) are required to promptly install security-relevant software updates (e.g., patches, service packs, and hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed expeditiously. Organization-defined time periods for updating security-relevant software may vary based on a variety of factors including, for example, the security category of the information system or the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw). This requirement will apply to software patch management solutions used to install patches across the enclave and also to applications that are not part of that patch management solution. For example, many browsers today provide the capability to install their own patch software. Patch criticality, as well as system criticality, will vary. Therefore, the tactical situations regarding the patch management process will also vary. This means the time period used must be a configurable parameter. Time frames for application of security-relevant software updates may be dependent upon the Information Assurance Vulnerability Management (IAVM) process. The application will be configured to check for and install security-relevant software updates within an identified time period from the availability of the update. The specific time period will be defined by an authoritative source (e.g., IAVM, CTOs, DTMs, and STIGs).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
MQ Appliance messaging server version 9.x is no longer supported by the vendor. If the system is running MQ Appliance messaging server version 9.x, this is a finding.

## Group: SRG-APP-000514-AS-000137

**Group ID:** `V-255793`

### Rule: The MQ Appliance messaging server must use DoD- or CNSS-approved PKI Class 3 or Class 4 certificates.

**Rule ID:** `SV-255793r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Class 3 PKI certificates are used for servers and software signing rather than for identifying individuals. Class 4 certificates are used for business-to-business transactions. Utilizing unapproved certificates not issued or approved by DoD or CNS creates an integrity risk. The messaging server must utilize approved DoD or CNS Class 3 or Class 4 certificates for software signing and business-to-business transactions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
From the MQ Appliance WebGUI, click on the Administration (gear) icon. Click on Main >> File Management. Click on the cert directory. Click on the "Details" action to the right of each cert to display its attributes. Verify that each certificate attribute meets organizationally approved requirements. If any certificates have not been issued by a DoD- or CNSS-approved PKI CA, this is a finding.

## Group: SRG-APP-000404-AS-000249

**Group ID:** `V-255794`

### Rule: The MQ Appliance messaging server must accept FICAM-approved third-party credentials.

**Rule ID:** `SV-255794r981695_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Access may be denied to legitimate users if FICAM-approved third-party credentials are not accepted. This requirement typically applies to organizational information systems that are accessible to non-federal government agencies and other partners. This allows federal government relying parties to trust such credentials at their approved assurance levels. Third-party credentials are those credentials issued by non-federal government entities approved by the Federal Identity, Credential, and Access Management (FICAM) Trust Framework Solutions initiative. Satisfies: SRG-APP-000404-AS-000249, SRG-APP-000405-AS-000250</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Log on to the WebGUI as a privileged user. Click on the "MQ Console" icon. Click "Add" widget at the top right of the screen. Select queue manager intended for OCSP from the drop-down list. Select "Authentication Information". Verify that the authentication type is "OCSP". Click on the "Properties" button. Click "OCSP" on the side bar to verify that the OCSP responder URL is correct. If either the authentication type is not "OCSP" or the OCSP responder URL in not correct, this is a finding.

## Group: SRG-APP-000181-AS-000255

**Group ID:** `V-255795`

### Rule: The MQ Appliance messaging server must provide a log reduction capability that supports on-demand reporting requirements.

**Rule ID:** `SV-255795r961056_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The ability to generate on-demand reports, including after the log data has been subjected to log reduction, greatly facilitates the organization's ability to generate incident reports as needed to better handle larger-scale or more complex security incidents. Log reduction is a process that manipulates collected log information and organizes such information in a summary format that is more meaningful to analysts. The report generation capability provided by the application must support on-demand (i.e., customizable, ad-hoc, and as-needed) reports. To fully understand and investigate an incident within the components of the messaging server, the messaging server, when providing a reduction capability, must provide an on-demand reporting capability. Instructions for using the amqsevt sample program to display instrumentation events may be found at the following URL: https://ibm.biz/BdsCzY Satisfies: SRG-APP-000181-AS-000255, SRG-APP-000355-AS-000055</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Confirm that the following command is available and functioning on an authorized MQ client device: amqsevt -m [queue mgr name] {-q SYSTEM.ADMIN.QMGR.EVENT | -q SYSTEM.ADMIN.CONFIG.EVENT | -q SYSTEM.ADMIN.PERFM.EVENT | -q SYSTEM.ADMIN.CHANNEL.EVENT | -q SYSTEM.ADMIN.COMMAND.EVENT} -c -u [user name] If an MQ client application is not enabled to monitor one or more of the above event queues, this is a finding.

## Group: SRG-APP-000109-AS-000070

**Group ID:** `V-255796`

### Rule: The MQ Appliance messaging server must be configured to fail over to another system in the event of log subsystem failure.

**Rule ID:** `SV-255796r960915_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is dependent upon system MAC and availability. If the system MAC and availability do not specify redundancy requirements, this requirement is NA. It is critical that, when a system is at risk of failing to process logs as required, it detects and takes action to mitigate the failure. Messaging servers must be capable of failing over to another system which can handle application and logging functions upon detection of an application log processing failure. This will allow continual operation of the application and logging functions while minimizing the loss of operation for the users and loss of log data. To ensure proper configuration, system HA design steps must be taken and implemented. Reference vendor documentation for complete instructions on setting up HA: https://ibm.biz/BdicC7 Satisfies: SRG-APP-000109-AS-000070, SRG-APP-000109-AS-000068, SRG-APP-000125-AS-000084</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In the event of a MQ queue manager failure, an HA configuration must be used. Obtain system documentation identifying the HA configuration. Establish an SSH command line session to either of the pair as an admin user. To access the MQ Appliance CLI, enter: mqcli To run the dspmq command, enter: dspmq -s -o ha Each queue manager that is properly configured for HA should show HA(Replicated). If it does not, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-255797`

### Rule: The MQ Appliance messaging server must uniquely identify all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-255797r1000054_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without identifying devices, unidentified or unknown devices may be introduced, thereby facilitating malicious activity. For distributed messaging servers and components, the decisions regarding the validation of identification claims may be made by services separate from the messaging server. In such situations, it is necessary to provide the identification decisions (as opposed to the actual identifiers) to the services that need to act on those decisions. Note: Following are the cipher specs available for MQ: https://ibm.biz/BdrJGp</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication configuration is correct by using "DISPLAY" commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] To display available SVRCONN channels details, enter: DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the names of SVRCONN channels (client channels). Display values for each channel: DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies a FIPS approved cipher spec and that the value of "SSLAUTH" is set to "REQUIRED". MQ cipher specs are available here: https://ibm.biz/BdrJGp Utilize a FIPS approved cipher when specifying SSLCIPH. If either the "SSLCIPH" or "SSLAUTH" value for each channel is not correct, this is a finding.

## Group: SRG-APP-000172-AS-000121

**Group ID:** `V-255798`

### Rule: Access to the MQ Appliance messaging server must utilize encryption when using LDAP for authentication.

**Rule ID:** `SV-255798r961029_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Passwords need to be protected at all times, and encryption is the standard method for protecting passwords during transmission. Messaging servers have the capability to utilize LDAP directories for authentication. If LDAP connections are not protected during transmission, sensitive authentication credentials can be stolen. When the messaging server utilizes LDAP, the LDAP traffic must be encrypted. Note: Multiple alternative LDAP hosts may be listed in the CONNAME parameter, separated by commas. Review IBM product documentation for the LDAP fields required when setting up a communication link with the LDAP server. See https://ibm.biz/BdiBGu and https://ibm.biz/BdixXz for a detailed description of these options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, for each queue manager, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] To display the active authentication object, enter: DIS QMGR CONNAUTH Result: QMNAME([queue mgr name]) CONNAUTH([auth object name]) DIS AUTHINFO(auth object name) Verify that "AUTHTYPE(IDPWLDAP)", and "SECCOMM(YES)" are displayed, and that all parameters are correctly specified to use the organizationally approved LDAP server(s). If these parameter values cannot be verified, this is a finding.

## Group: SRG-APP-000177-AS-000126

**Group ID:** `V-255799`

### Rule: The MQ Appliance messaging server must map the authenticated identity to the individual messaging user or group account for PKI-based authentication.

**Rule ID:** `SV-255799r961044_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The cornerstone of PKI is the private key used to encrypt or digitally sign information. The key by itself is a cryptographic value that does not contain specific user information, but the key can be mapped to a user. Without mapping the certificate used to authenticate to the user account, the ability to determine the identity of the individual user or group will not be available for forensic analysis. Messaging servers must provide the capability to utilize and meet requirements of the DoD Enterprise PKI infrastructure for application authentication. Note: Two or more alternative LDAP hosts may be listed, in the CONNAME parameter, separated by commas. Review IBM product documentation for the LDAP fields required when setting up a communication link with the LDAP server. See https://ibm.biz/BdiBGu for a detailed description of these options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, for each queue manager, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS AUTHINFO(*) AUTHTYPE(CRLLDAP) CONNAME Verify that an "AUTHINFO" definition of "AUTHTYPE(CRLLDAP)" is displayed and that the CONNAME in parenthesis is the host name or IPv4 dotted decimal address of an organizationally approved LDAP server. If the "AUTHINFO" definition is not equal to "AUTHTYPE(CRLLDAP)", this is a finding.

## Group: SRG-APP-000163-AS-000111

**Group ID:** `V-255800`

### Rule: The MQ Appliance must disable identifiers (individuals, groups, roles, and devices) after 35 days of inactivity.

**Rule ID:** `SV-255800r981681_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Inactive identifiers pose a risk to systems and applications. Attackers that are able to exploit an inactive identifier can potentially obtain and maintain undetected access to the application. Owners of inactive accounts will not notice if unauthorized access to their user account has been obtained. Applications need to track periods of inactivity and disable application identifiers after 35 days of inactivity. Management of user identifiers is not applicable to shared information system accounts (e.g., guest and anonymous accounts). It is commonly the case that a user account is the name of an information system account associated with an individual. To avoid having to build complex user management capabilities directly into their application, wise developers leverage the underlying OS or other user account management infrastructure (AD, LDAP) that is already in place within the organization and meets organizational user account management requirements. Review IBM product documentation for the LDAP fields required when setting up a communication link with the LDAP server. Note: Multiple alternative LDAP hosts may be listed in the CONNAME parameter, separated by commas. Review IBM product documentation for the LDAP fields required when setting up a communication link with the LDAP server. See https://ibm.biz/BdiBGu and https://ibm.biz/BdixXz for a detailed description of these options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, for each queue manager, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] To display the active authentication object, enter: DIS QMGR CONNAUTH Result: QMNAME([queue mgr name]) CONNAUTH([auth object name]) DIS AUTHINFO(auth object name) Verify that "AUTHTYPE(IDPWLDAP)" is displayed. Verify LDAP server user settings are configured to disable accounts after "35" days of inactivity. If "AUTHTYPE(IDPWLDAP)" is not displayed or if the LDAP server user settings are not configured to disable accounts after "35" days of inactivity, this is a finding.

## Group: SRG-APP-000148-AS-000101

**Group ID:** `V-255801`

### Rule: The MQ Appliance messaging server must use an enterprise user management system to uniquely identify and authenticate users (or processes acting on behalf of organizational users).

**Rule ID:** `SV-255801r960969_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthorized access, application server users must be uniquely identified and authenticated. This is typically accomplished via the use of a user store which is either local (OS-based) or centralized (LDAP) in nature. To ensure support to the enterprise, the authentication must utilize an enterprise solution. Review IBM product documentation for the LDAP fields required when setting up a communication link with the LDAP server. See https://ibm.biz/BdsRRk for a detailed description of these options.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS AUTHINFO(USE.LDAP) Verify that "AUTHINFO(USE.LDAP)" is displayed under authentication information details. If "IBM MQ Appliance object USE.LDAP not found" is displayed, this is a finding.

## Group: SRG-APP-000068-AS-000035

**Group ID:** `V-255802`

### Rule: The MQ Appliance messaging server management interface must display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system.

**Rule ID:** `SV-255802r960843_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Messaging servers are required to display the Standard Mandatory DoD Notice and Consent Banner before granting access to the system management interface, providing privacy and security notices consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance that states that: (i) users are accessing a U.S. Government information system; (ii) system usage may be monitored, recorded, and subject to audit; (iii) unauthorized use of the system is prohibited and subject to criminal and civil penalties; and (iv) the use of the system indicates consent to monitoring and recording. System use notification messages can be implemented in the form of warning banners displayed when individuals log on to the information system. System use notification is intended only for information system access including an interactive logon interface with a human user, and is not required when an interactive interface does not exist. Use this banner for desktops, laptops, and other devices accommodating banners of 1300 characters. The banner shall be implemented as a click-through banner at logon (to the extent permitted by the operating system), meaning it prevents further activity on the information system unless and until the user executes a positive action to manifest agreement by clicking on a box indicating "OK". "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Using a browser, navigate to the MQ Appliance logon page as a privileged user. Verify the logon page displays the Standard Mandatory DoD Notice and Consent Banner: For the WebGUI, the banner must read: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details. Logging in signifies acceptance of this agreement." For the SSH CLI, the banner must read: "I've read & consent to terms in IS user agreem't. Logging in signifies acceptance of this agreement." If the standard banner is not displayed in both the WebGUI and CLI interfaces, this is a finding.

## Group: SRG-APP-000089-AS-000050

**Group ID:** `V-255803`

### Rule: The MQ Appliance messaging server must generate log records for access and authentication events.

**Rule ID:** `SV-255803r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the messaging server. From a messaging server perspective, certain specific messaging server functionalities may be logged as well. The messaging server must allow the definition of what events are to be logged. As conditions change, the number and types of events to be logged may change, and the messaging server must be able to facilitate these changes. The minimum list of logged events should be those pertaining to system startup and shutdown, system access, and system authentication events.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS QMGR EVENT A list of all events will be displayed along with an indication of if event logging is enabled. The events are as follows: Authority: AUTHOREV, Inhibit: INHIBITEV, Local: LOCALEV, Remote: REMOTEEV, Start and stop: STRSTPEV, Performance: PERFMEV, Command: CMDEV, Channel: CHLEV, Channel auto definition: CHADEV, SSL: SSLEV, Configuration: CONFIGEV If and required event logging is not enabled for running queue managers, this is a finding.

## Group: SRG-APP-000219-AS-000147

**Group ID:** `V-255804`

### Rule: The MQ Appliance messaging server must ensure authentication of both SSH client and server during the entire session.

**Rule ID:** `SV-255804r961110_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control focuses on communications protection at the session, versus packet level. At the application layer, session IDs are tokens generated by web applications to uniquely identify an application user's session. Web applications utilize session tokens or session IDs in order to establish application user identity. Proper use of session IDs addresses man-in-the-middle attacks, including session hijacking or insertion of false information into a session. Messaging servers must provide the capability to perform mutual authentication. Mutual authentication is when both the client and the server authenticate each other. Satisfies: SRG-APP-000219-AS-000147, SRG-APP-000223-AS-000150, SRG-APP-000223-AS-000151</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication configuration is correct by using DISPLAY commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the name of SVRCONN channel (client channel) you wish to check. DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies the desired cipher spec and that the value of "SSLAUTH" is "REQUIRED". If either the "SSLCIPH" or "SSLAUTH" value is not correct, this is a finding.

## Group: SRG-APP-000224-AS-000152

**Group ID:** `V-255805`

### Rule: The MQ Appliance messaging server must generate a unique session identifier using a FIPS 140-2 approved random number generator.

**Rule ID:** `SV-255805r961119_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The messaging server will use session IDs to communicate between modules or applications within the messaging server and between the messaging server and users. The session ID allows the application to track the communications along with credentials that may have been used to authenticate users or modules. Unique session IDs are the opposite of sequentially generated session IDs which can be easily guessed by an attacker. Unique session identifiers help to reduce predictability of said identifiers. Unique session IDs address man-in-the-middle attacks, including session hijacking or insertion of false information into a session. If the attacker is unable to identify or guess the session information related to pending application traffic, they will have more difficulty in hijacking the session or otherwise manipulating valid sessions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication configuration is correct by using DISPLAY commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the name of SVRCONN channel (client channel) you wish to check. DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies the desired cipher spec and that the value of "SSLAUTH" is "REQUIRED". If either the "SSLCIPH" or "SSLAUTH" value is not correct, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-255806`

### Rule: The MQ Appliance messaging server must authenticate all network-connected endpoint devices before establishing any connection.

**Rule ID:** `SV-255806r1000055_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Device authentication requires unique identification and authentication that may be defined by type, by specific device, or by a combination of type and device. Device authentication is accomplished via the use of certificates and protocols such as SSL mutual authentication. Device authentication is performed when the messaging server is providing web services capabilities and data protection requirements mandate the need to establish the identity of the connecting device before the connection is established. The most common way devices (endpoints) may connect an MQ Appliance MQ queue manager is as an MQ client. In order to ensure unique identification of network-connected devices, mutual authentication using CA-signed TLS certificates should be configured. Note: Following are the cipher specs available for MQ: https://ibm.biz/BdrJGp</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication configuration is correct by using DISPLAY commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the name of SVRCONN channel (client channel) you wish to check. DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies the desired cipher spec and that the value of "SSLAUTH" is "REQUIRED". If either the "SSLCIPH" or "SSLAUTH" value is not correct, this is a finding.

## Group: SRG-APP-000516-AS-000237

**Group ID:** `V-255807`

### Rule: The MQ Appliance messaging server must authenticate all endpoint devices before establishing a local, remote, and/or network connection using bidirectional authentication that is cryptographically based.

**Rule ID:** `SV-255807r1000056_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Device authentication requires unique identification and authentication that may be defined by type, by specific device, or by a combination of type and device. Bidirectional authentication provides stronger safeguards to validate the identity of other devices for connections that are of greater risk. Device authentication is performed when the messaging server is providing web services capabilities and data protection requirements mandate the need to establish the identity of the connecting device before the connection is established. The most common way devices (endpoints) may connect an MQ Appliance MQ queue manager is as an MQ client. In order to ensure unique identification of network-connected devices, mutual authentication using CA-signed TLS certificates must be configured. Note: Following are the cipher specs available for MQ: https://ibm.biz/BdrJGp</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system documentation. Identify all message services hosted on the device(s) and determine if any services are hosting publicly available, non-sensitive data. This requirement is NA for publicly available services that host non-sensitive data if a documented ISSO risk acceptance is presented. Check that TLS mutual authentication configuration is correct by using DISPLAY commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the name of SVRCONN channel (client channel) you wish to check. DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies the desired cipher spec and that the value of "SSLAUTH" is "REQUIRED". If either the "SSLCIPH" or "SSLAUTH" value is not correct, this is a finding.

## Group: SRG-APP-000514-AS-000136

**Group ID:** `V-255808`

### Rule: MQ Appliance messaging servers must use NIST-approved or NSA-approved key management technology and processes.

**Rule ID:** `SV-255808r961857_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>An asymmetric encryption key must be protected during transmission. The public portion of an asymmetric key pair can be freely distributed without fear of compromise, and the private portion of the key must be protected. The messaging server will provide software libraries that applications can programmatically utilize to encrypt and decrypt information. These messaging server libraries must use NIST-approved or NSA-approved key management technology and processes when producing, controlling, or distributing symmetric and asymmetric keys. The most common way devices (endpoints) may connect an MQ Appliance MQ queue manager is as an MQ client. In order to ensure unique identification of network-connected devices, mutual authentication using CA-signed TLS certificates should be configured. Note: Following are the cipher specs available for MQ: https://ibm.biz/BdrJGp</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check that TLS mutual authentication configuration is correct by using DISPLAY commands. To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS CHANNEL(*) CHLTYPE(SVRCONN) Note the name of SVRCONN channel (client channel) you wish to check. DIS CHANNEL([name of SVRCONN channel]) Confirm that the parameter "SSLCIPH" specifies the desired cipher spec and that the value of "SSLAUTH" is "REQUIRED". If either the "SSLCIPH" or "SSLAUTH" value is not correct, this is a finding.

## Group: SRG-APP-000179-AS-000129

**Group ID:** `V-255809`

### Rule: The MQ Appliance messaging server must utilize FIPS 140-2 approved encryption modules when authenticating users and processes.

**Rule ID:** `SV-255809r961050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Encryption is only as good as the encryption modules utilized. Unapproved cryptographic module algorithms cannot be verified and cannot be relied upon to provide confidentiality or integrity, and DoD data may be compromised due to weak algorithms. The use of TLS provides confidentiality of data in transit between the messaging server and client. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. To achieve FIPS 140-2 compliance on Windows, UNIX, and Linux systems, all key repositories have been created and manipulated using only FIPS-compliant software, such as runmqakm with the -fips option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS QMGR SSLFIPS If the value of "SSLFIPS" is set to "NO", this is a finding.

## Group: SRG-APP-000439-AS-000155

**Group ID:** `V-255810`

### Rule: The MQ Appliance messaging server must protect the confidentiality and integrity of transmitted information through the use of an approved TLS version.

**Rule ID:** `SV-255810r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure of transmitted information requires that the messaging server take measures to employ some form of cryptographic mechanism in order to protect the information during transmission. This is usually achieved through the use of Transport Layer Security (TLS). Transmission of data can take place between the messaging server and a large number of devices/applications external to the messaging server. Examples are a web client used by a user, a backend database, a log server, or other messaging servers (and clients) in a messaging server cluster. If data is transmitted unencrypted, the data then becomes vulnerable to disclosure. The disclosure may reveal user identifier/password combinations, website code revealing business logic, or other user personal information. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. To achieve FIPS 140-2 compliance on Windows, UNIX, and Linux systems, all key repositories have been created and manipulated using only FIPS-compliant software, such as runmqakm with the -fips option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS QMGR SSLFIPS If the value of "SSLFIPS" is set to "NO", this is a finding.

## Group: SRG-APP-000439-AS-000274

**Group ID:** `V-255811`

### Rule: The MQ Appliance messaging server must remove all export ciphers to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-255811r961632_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>During the initial setup of a Transport Layer Security (TLS) connection to the messaging server, the client sends a list of supported cipher suites in order of preference. The messaging server will reply with the cipher suite it will use for communication from the client list. If an attacker can intercept the submission of cipher suites to the messaging server and place, as the preferred cipher suite, a weak export suite, the encryption used for the session becomes easy for the attacker to break, often within minutes to hours. To achieve FIPS 140-2 compliance on Windows, UNIX, and Linux systems, all key repositories have been created and manipulated using only FIPS-compliant software, such as runmqakm with the -fips option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS QMGR SSLFIPS If the value of "SSLFIPS" is set to "NO", this is a finding.

## Group: SRG-APP-000440-AS-000167

**Group ID:** `V-255812`

### Rule: The MQ Appliance messaging server must employ approved cryptographic mechanisms to prevent unauthorized disclosure of information and/or detect changes to information during transmission.

**Rule ID:** `SV-255812r961635_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Preventing the disclosure or modification of transmitted information requires that messaging servers take measures to employ approved cryptography in order to protect the information during transmission over the network. This is usually achieved through the use of Transport Layer Security (TLS), SSL VPN, or IPsec tunnel. If data in transit is unencrypted, it is vulnerable to disclosure and modification. If approved cryptographic algorithms are not used, encryption strength cannot be assured. FIPS 140-2 approved TLS versions include TLS V1.0 or greater. TLS must be enabled and non-FIPS-approved SSL versions must be disabled. NIST SP 800-52 specifies the preferred configurations for government systems. To achieve FIPS 140-2 compliance on Windows, UNIX, and Linux systems, all key repositories have been created and manipulated using only FIPS-compliant software, such as runmqakm with the -fips option.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli To identify the queue managers, enter: dspmq For each queue manager identified, run the command: runmqsc [queue name] DIS QMGR SSLFIPS If the value of "SSLFIPS" is set to "NO", this is a finding.

## Group: SRG-APP-000225-AS-000154

**Group ID:** `V-255813`

### Rule: The MQ Appliance messaging server must provide a clustering capability.

**Rule ID:** `SV-255813r961122_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This requirement is dependent upon system criticality and confidentiality requirements. If the system categorization and confidentiality levels do not specify redundancy requirements, this requirement is NA. Failure to a known secure state helps prevent a loss of confidentiality, integrity, or availability in the event of a failure of the information system or a component of the system. When application failure is encountered, preserving application state facilitates application restart and return to the operational mode of the organization with less disruption of mission/business processes. Clustering of multiple messaging servers is a common approach to providing fail-safe application availability when system MAC and confidentiality levels require redundancy. Satisfies: SRG-APP-000225-AS-000154, SRG-APP-000225-AS-000166</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system categorization to determine if redundancy is a requirement. If the system categorization does not specify redundancy requirements, this requirement is NA. On each member of the HA pair: Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To run the dspmq command, enter: dspmq -s -o ha One of the appliances should be running as primary, the other as secondary. If HA is not configured and the primary and secondary running, this is a finding.

## Group: SRG-APP-000356-AS-000202

**Group ID:** `V-255814`

### Rule: The MQ Appliance messaging server must provide centralized management and configuration of the content to be captured in log records generated by all application components.

**Rule ID:** `SV-255814r981683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A clustered messaging server is made up of several servers working together to provide the user a failover and increased computing capability. To facilitate uniform logging in the event of an incident and later forensic investigation, the record format and logable events need to be uniform. This can be managed best from a centralized server. Without the ability to centrally manage the content captured in the log records, identification, troubleshooting, and correlation of suspicious behavior would be difficult and could lead to a delayed or incomplete analysis of an ongoing attack. The MQ appliance is designed to be used in a redundant HQ configuration which will provide a means of centralized management of log activity. Rudimentary instructions for determining if HA is set up are included here. To ensure proper configuration, system HA design steps must be taken and implemented. Reference vendor documentation for complete instructions on setting up HA: https://ibm.biz/BdicC7 Note: The queue manager’s data (queues, queue messages etc.) are replicated from the appliance in the primary HA role (first appliance) to the appliance in the secondary HA role (second appliance). Ref.: Configuring high availability queue managers https://goo.gl/xAqNTX</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system categorization to determine if redundancy is a requirement. If system categorization does not specify redundancy, interview system administrator to determine how they have configured the centralized log management solution for the MQ appliance. On each member of the HA pair: Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To run the dspmq command, enter: dspmq -s -o ha One of the appliances should be running as primary, the other as secondary. If HA is not configured and the primary and secondary running, or if there is no centralized management solution in place to manage MQ logs, this is a finding.

## Group: SRG-APP-000515-AS-000203

**Group ID:** `V-255815`

### Rule: The MQ Appliance messaging server must, at a minimum, transfer the logs of interconnected systems in real time, and transfer the logs of standalone systems weekly.

**Rule ID:** `SV-255815r961860_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Protecting log data is important during a forensic investigation to ensure investigators can track and understand what may have occurred. Off-loading should be set up as a scheduled task but can be configured to be run manually, if other processes during the off-loading are manual. Off-loading is a common process in information systems with limited log storage capacity. The MQ appliance is designed to be used in a redundant configuration which will ensure duplicates of log activity are created. Rudimentary instructions for determining if HA is set up are included here. To ensure proper configuration, system HA design steps must be taken and implemented. Reference vendor documentation for complete instructions on setting up HA: https://ibm.biz/BdicC7 Note: The queue manager’s data (queues, queue messages etc.) are replicated from the appliance in the primary HA role (first appliance) to the appliance in the secondary HA role (second appliance).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review system categorization to determine if redundancy is a requirement. If system categorization does not specify redundancy, interview system administrator to determine how they have configured the weekly transfer of logs for the MQ appliance. For redundant systems: On each member of the HA pair: Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To run the dspmq command, enter: dspmq -s -o ha One of the appliances should be running as primary, the other as secondary. If HA is not configured with the primary and secondary running, or if there is no MQ log transfer taking place on a standalone system on a weekly basis, this is a finding.

## Group: SRG-APP-000014-AS-000009

**Group ID:** `V-255816`

### Rule: The MQ Appliance messaging server must use encryption strength in accordance with the categorization of the management data during remote access management sessions.

**Rule ID:** `SV-255816r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Remote management access is accomplished by leveraging common communication protocols and establishing a remote connection to the messaging server via a network for the purposes of managing the messaging server. If cryptography is not used, then the session data traversing the remote connection could be intercepted and compromised. Types of management interfaces utilized by a messaging server include web-based HTTPS interfaces as well as command line-based management interfaces.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
To access the MQ Appliance CLI, enter: mqcli config crypto show crypto-mode If the current setting is set to "permissive", this is a finding.

## Group: SRG-APP-000435-AS-000069

**Group ID:** `V-255817`

### Rule: The MQ Appliance messaging server, when categorized as a high level system, must be in a high-availability (HA) cluster.

**Rule ID:** `SV-255817r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A high level system is a system that handles data vital to the organization's operational readiness or effectiveness of deployed or contingency forces. A high level system must maintain the highest level of integrity and availability. By HA clustering the messaging server, the hosted application and data are given a platform that is load-balanced and provided high-availability. Rudimentary instructions for determining if HA is set up are included here. To ensure proper configuration, system HA design steps must be taken and implemented. Reference vendor documentation for complete instructions on setting up HA: https://ibm.biz/BdicC7 Note: The queue manager’s data (queues, queue messages etc.) are replicated from the appliance in the primary HA role (first appliance) to the appliance in the secondary HA role (second appliance).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Request and review system documentation identifying the system categorization level. If the system categorization is not high, this requirement is NA. Ask for and review the HA configuration. On the either member of the HA pair: Establish an SSH command line session as an admin user. To access the MQ Appliance CLI, enter: mqcli To run the dspmq command, enter: dspmq -s -o ha Each queue manager that is properly configured for HA should show HA(Replicated). If it does not, this is a finding.

