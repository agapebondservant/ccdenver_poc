# STIG Benchmark: Microsoft Exchange 2019 Edge Server Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000014

**Group ID:** `V-259577`

### Rule: SchUseStrongCrypto must be enabled.

**Rule ID:** `SV-259577r960759_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange Server 2019 is configured by default with TLS 1.2. However, SchUseStrongCrypto is not set by default and must be configured to meet the TLS requirement. The strong cryptography (configured by the SchUseStrongCrypto registry value) uses more secure network protocols (TLS 1.2, TLS 1.1, and TLS 1.0) and blocks protocols that are not secure. SchUseStrongCrypto affects only client (outgoing) connections in the application.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
In a PowerShell window, run the following commands: Get-ItemProperty HKLM:\SOFTWARE\Microsoft\.NetFramework\v4.0.30319 If the value "SchUseStrongCrypto" is not present and set to 1, this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-259578`

### Rule: Exchange servers must use approved DOD certificates.

**Rule ID:** `SV-259578r960792_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DOD-approved PKIs, all DOD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExchangeCertificate | Select-Object -Property CertificateDomains, issuer If the value of "CertificateDomains" does not indicate it is issued by the DOD, this is a finding.

## Group: SRG-APP-000038

**Group ID:** `V-259579`

### Rule: Exchange must have accepted domains configured.

**Rule ID:** `SV-259579r960801_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange may be configured to accept email for multiple domain names. This setting identifies the domains for which the server will accept mail. This check verifies the email server is not accepting email for unauthorized domains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the Accepted Domain values. Open the Exchange Management Shell and enter the following command: Get-AcceptedDomain | Select-Object -Property Name, DomainName, Identity, Default If the value of "Default" is not set to "True", this is a finding. or If the "Default" value for "AcceptedDomains" is set to another value other than "True" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000065

**Group ID:** `V-259580`

### Rule: Exchange external Receive connectors must be domain secure-enabled.

**Rule ID:** `SV-259580r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) connector is used by Exchange to send and receive messages from server to server. Several controls work together to provide security between internal servers. This setting controls the authentication method used for communications between servers. With this feature enabled, messages can be securely passed from a partner domain securely. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from server to server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption can be compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, DomainSecureEnabled For each receive connector, if the value of "DomainSecureEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-259581`

### Rule: The Exchange email diagnostic log level must be set to the lowest level.

**Rule ID:** `SV-259581r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Diagnostic logging, however, characteristically produces large volumes of data and requires care in managing the logs to prevent risk of disk capacity denial of service conditions. Exchange diagnostic logging is broken up into 29 main "services", each of which has anywhere from two to 26 "categories" of events to be monitored. Moreover, each category may be set to one of four levels of logging: Lowest, Low, CAT II, and High, depending on how much detail one desires. The higher the level of detail, the more disk space required to store the audit material. Diagnostic logging is intended to help administrators debug problems with their systems, not as a general-purpose auditing tool. Because the diagnostic logs collect a great deal of information, the log files may grow large very quickly. Diagnostic log levels may be raised for limited periods of time when attempting to debug relevant pieces of Exchange functionality. Once debugging has finished, diagnostic log levels should be reduced again.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-EventLogLevel If any "EventLogLevel" values returned are not set to "Lowest", this is a finding. Note: The default installation of Exchange has all Event Levels set to Lowest with exception of the following: MSExchange ADAccess\Topology - Low MSExchangeADAccess\Validation - Low MSExchange BackEndRehydration\Configuration - Low MSExchange BackEndRehydration\Server - 2 MSExchange OAuth\Configuration - Low MSExchange OAuth\Server - 2 MSExchange RBAC\RBAC - Low MSExchangeADTopology\Topology - Low All of these must be set to Lowest.

## Group: SRG-APP-000089

**Group ID:** `V-259582`

### Rule: Exchange connectivity logging must be enabled.

**Rule ID:** `SV-259582r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A connectivity log is a record of the SMTP connection activity of the outbound message delivery queues to the destination mailbox server, smart host, or domain. Connectivity logging is available on Hub Transport servers and Edge Transport servers. By default, connectivity logging is disabled. If events are not recorded, it may be difficult or impossible to determine the root cause of system problems or the unauthorized activities of malicious users. Note: Transport configuration settings apply to the organization/global level of the Exchange SMTP path. By checking and setting them at the Hub server, the setting will apply to both Hub and Edge roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-TransportService | Select-Object -Property Name, Identity, ConnectivityLogEnabled If the value of "ConnectivityLogEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000098

**Group ID:** `V-259583`

### Rule: Exchange message tracking logging must be enabled.

**Rule ID:** `SV-259583r960900_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A message tracking log provides a detailed log of all message activity as messages are transferred to and from a computer running Exchange. If events are not recorded, it may be difficult or impossible to determine the root cause of system problems or the unauthorized activities of malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-Transportservice | Select-Object -Property Name, MessageTrackingLogEnabled If the value of "MessageTrackingLogEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000111

**Group ID:** `V-259584`

### Rule: Exchange queue monitoring must be configured with threshold and action.

**Rule ID:** `SV-259584r960918_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitors are automated "process watchers" that respond to performance changes and can be useful in detecting outages and alerting administrators where attention is needed. Exchange has built-in monitors that enable the administrator to generate alerts if thresholds are reached, better enabling them to react in a timely fashion. This field offers choices of alerts when a "warning" or "critical" threshold is reached on the SMTP queue. A good rule of thumb (default) is to issue warnings when SMTP queue growth exceeds 10 minutes and critical messages when it exceeds 20 minutes, which should only exist occasionally. Frequent alerts against this counter may indicate a network or other issue (such as inbound spammer traffic) that directly impacts email delivery. Notification choices include email alert to an email-enabled account (e.g., an email administrator) or invoke a script to take other action (e.g., to add an event to the Microsoft Application Event Log, where external monitors might detect it).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: By default, there are two user-defined data collector sets created by Exchange: ExchangeDiagnosticsDailyPerformanceLog and ExchangeDiagnosticsPerformanceLog. These are not providing enough data to monitor SMTP queues per the requirement. Additionally, if a third-party application is performing monitoring functions, the reviewer should verify the application is monitoring correctly and mark the vulnerability Not Applicable. Open the Exchange Management Shell and enter the following command: perfmon In the left pane, navigate to Performance >> Data Collector Sets >> User Defined. If no sets are defined or queues are not being monitored, this is a finding.

## Group: SRG-APP-000118

**Group ID:** `V-259585`

### Rule: Exchange audit data must be protected against unauthorized access (read access).

**Rule ID:** `SV-259585r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted read and write access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the authorized groups or users that should have read access to the audit data. If any group or user has read access to the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000119

**Group ID:** `V-259586`

### Rule: Exchange audit data must be protected against unauthorized access for modification.

**Rule ID:** `SV-259586r960933_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted read and write access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the authorized groups or users that should have modify permissions to the audit data. If any group or user has modify permissions for the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000120

**Group ID:** `V-259587`

### Rule: Exchange audit data must be protected against unauthorized access for deletion.

**Rule ID:** `SV-259587r960936_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted read and write access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the authorized groups or users that should have delete permissions for the audit data. If any group or user has delete permissions for the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000125

**Group ID:** `V-259588`

### Rule: Exchange audit data must be on separate partitions.

**Rule ID:** `SV-259588r960948_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Successful exploit of an application server vulnerability may well be logged by monitoring or audit processes when it occurs. Writing log and audit data to a separate partition where separate security contexts protect them may offer the ability to protect this information from being modified or removed by the exploit mechanism.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the audit logs' assigned partition. Note: By default, the logs are located on the application partition in \Program Files\Microsoft\Exchange Server\V15\Logging\. If the log files are not on a separate partition from the application, this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-259589`

### Rule: Exchange local machine policy must require signed scripts.

**Rule ID:** `SV-259589r1015762_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts often provide a way for attackers to infiltrate a system, especially scripts downloaded from untrusted locations. By setting machine policy to prevent unauthorized script executions, unanticipated system impacts can be avoided. Failure to allow only signed remote scripts reduces the attack vector vulnerabilities from unsigned remote scripts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExecutionPolicy If the value returned is not "RemoteSigned", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-259590`

### Rule: Exchange must not send customer experience reports to Microsoft.

**Rule ID:** `SV-259590r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but cannot be disabled. All system errors in Exchange will result in outbound traffic that may be identified by an eavesdropper. For this reason, the "Report Fatal Errors to Microsoft" feature must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-OrganizationConfig | Select-Object -Property Name, Identity, CustomerFeedbackEnabled If the value for "CustomerFeedbackEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-259591`

### Rule: Exchange Send Fatal Errors to Microsoft must be disabled.

**Rule ID:** `SV-259591r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of nonessential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission, but cannot be disabled. Customer Experience reports in Exchange will result in outbound traffic that may be identified by an eavesdropper. For this reason, the Customer Experience reports to Microsoft must not be sent.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExchangeServer –status | Select-Object -Property Name, Identity, ErrorReportingEnabled For each exchange server, if the value of "ErrorReportingEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000211

**Group ID:** `V-259592`

### Rule: Exchange queue database must reside on a dedicated partition.

**Rule ID:** `SV-259592r961095_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the same way that added security layers can provide a cumulative positive effect on security posture, multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to the host system can most likely lead to a compromise of all applications hosted by the same system. Email services should be installed to a discrete set of directories on a partition that does not host other applications. Email services should never be installed on a Domain Controller/Directory Services server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and run the following command: Get-Content $exbin\EdgeTransport.exe.config |Select-String "QueueDatabasePath" -SimpleMatch Example Output: <add key="QueueDatabasePath" value="F:\Program Files\Microsoft\Exchange Server\V15\TransportRoles\data\Queue" /> If the path of the Queue Database is in the same volume as the installation of Exchange, this is a finding. If the path of the Queue Database is on the same volume of existing applications, this is a finding.

## Group: SRG-APP-000213

**Group ID:** `V-259593`

### Rule: Exchange internet-facing send connectors must specify a Smart Host.

**Rule ID:** `SV-259593r961101_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When identifying a "Smart Host" for the email environment, a logical send connector is the preferred method. A Smart Host acts as an internet-facing concentrator for other email servers. Appropriate hardening can be applied to the Smart Host, rather than at multiple locations throughout the enterprise. Failure to identify a Smart Host could default to each email server performing its own lookups (potentially through protective firewalls). Exchange servers should not be internet facing and should therefore not perform any Smart Host functions. When the Exchange servers are internet facing, they must be configured to identify the internet-facing server that is performing the Smart Host function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This is not applicable for SIPR enclaves. Review the Email Domain Security Plan (EDSP). Determine the internet-facing connectors. Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, SmartHosts, DNSRoutingEnabled For each send connector, if the value of "SmartHosts" does not return the Smart Host IP Address and the value for "DNSRoutingEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000219

**Group ID:** `V-259594`

### Rule: Exchange internal send connectors must use domain security (mutual authentication Transport Layer Security).

**Rule ID:** `SV-259594r1043178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) connector is used by Exchange to send and receive messages from server to server. Several controls work together to provide security between internal servers. This setting controls the authentication method used for communications between servers. With this feature enabled, only servers capable of supporting domain authentication will be able to send and receive mail within the domain. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from server to server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption can be compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, DomainSecureEnabled For each send connector, if the value of "DomainSecureEnabled" is not set to "True", this is a finding. If the "TlsAuthLevel" parameter is set to "DomainValidation" then the "TlsDomain" parameter is required if "DNSRoutingEnabled" parameter is set to "$false". The "DNSRoutingEnabled" parameter must be "$true" If the value of "DomainSecureEnabled" is "$true".

## Group: SRG-APP-000219

**Group ID:** `V-259595`

### Rule: Exchange internet-facing receive connectors must offer Transport Layer Security (TLS) before using basic authentication.

**Rule ID:** `SV-259595r1043178_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sending unencrypted email over the internet increases the risk that messages can be intercepted or altered. TLS is designed to protect confidentiality and data integrity by encrypting email messages between servers and thereby reducing the risk of eavesdropping, interception, and alteration. This setting forces Exchange to offer TLS before using basic authentication.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This is not applicable for SIPR enclaves. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, AuthMechanism For each receive connector, if the value of "AuthMechanism" is not set to "Tls, BasicAuth, BasicAuthRequireTLS", this is a finding.

## Group: SRG-APP-000246

**Group ID:** `V-259596`

### Rule: More than one Edge server must be deployed.

**Rule ID:** `SV-259596r961152_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To ensure hostile insiders are unable to easily commit DoS attacks and reduce the effectiveness of mail flow throughout the environment, a second Edge server is deployed to allow for multiple paths of mail flow both internally and externally into the environment. This prevents a single point-of-failure and allows for service to continue in the event of a DoS attack targeting one Edge role.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the EDSP for current configuration. On the mailbox server, open a PowerShell prompt and run the following command: Get-EdgeSubscription If there is only one subscription on each server, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259597`

### Rule: Exchange Outbound Connection Timeout must be 10 minutes or less.

**Rule ID:** `SV-259597r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the number of idle minutes before the connection is dropped. It works in conjunction with the Maximum Outbound Connections Count setting. Connections, once established, may incur delays in message transfer. The default of 10 minutes is a reasonable window in which to resume activities without maintaining idle connections for excessive intervals. If the timeout period is too long, idle connections may be maintained for unnecessarily long time periods, preventing new connections from being established. Sluggish connectivity increases the risk of lost data. A value of 10 or less is optimal.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the Connection Timeout value. Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, ConnectionInactivityTimeOut For each send connector, if the value of "ConnectionInactivityTimeOut" is not set to "00:10:00", this is a finding. or If "ConnectionInactivityTimeOut" is set to other than "00:10:00" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259598`

### Rule: Exchange Outbound Connection limit per Domain Count must be controlled.

**Rule ID:** `SV-259598r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the maximum number of simultaneous outbound connections from a domain and works in conjunction with the Maximum Outbound Connections Count setting as a delivery tuning mechanism. If the limit is too low, connections may be dropped. If the limit is too high, some domains may use a disproportionate resource share, denying access to other domains. Appropriate tuning reduces the risk of data delay or loss. By default, a limit of 20 simultaneous outbound connections from a domain should be sufficient. The value may be adjusted if justified by local site conditions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the value for Maximum Domain Connections. Open the Exchange Management Shell and enter the following command: Get-TransportService | Select-Object -Property Name, Identity, MaxPerDomainOutboundConnections If the value of "MaxPerDomainOutboundConnections" is not set to "20", this is a finding. or If the value of "MaxPerDomainOutboundConnections" is set to a value other than "20" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259599`

### Rule: Exchange receive connector maximum hop count must be 60.

**Rule ID:** `SV-259599r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This setting controls the maximum number of hops (email servers traversed) a message may take as it travels to its destination. Part of the original internet protocol implementation, the hop count limit prevents a message from being passed in a routing loop indefinitely. Messages exceeding the maximum hop count are discarded undelivered. Recent studies indicate that virtually all messages can be delivered in fewer than 60 hops. If the hop count is set too low, messages may expire before they reach their destinations. If set too high, an undeliverable message may cycle between servers, raising the risk of network congestion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the value for receive connectors. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, MaxHopCount For each receive connector, if the value of "MaxHopCount" is not set to "60", this is a finding. or If the value of "MaxHopCount" is set to a value other than "60" and has signoff and risk acceptance, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259600`

### Rule: Exchange receive connectors must control the number of recipients per message.

**Rule ID:** `SV-259600r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the maximum number of recipients who will receive a copy of a message at one time. This tunable value is related to throughput capacity and can enable the ability to optimize message delivery. Note: There are two types of default receive connecters: "Client Servername" accepts SMTP connections from all non-MAPI clients, such as POP and IMAP. As POP and IMAP are not authorized for use in DOD, these should not be present. Their default value for MaxRecipientsPerMessage is 200. IMAP Secure is not restricted and may be configured. "Default Servername" accepts connections from other mailbox servers and any Edge Transport servers. Their default value for MaxRecipientsPerMessage is 5000.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the Maximum Recipients per Message value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, MaxRecipientsPerMessage For each receive connector, if the value of "MaxRecipientsPerMessage" is not set to "5000", this is a finding. or If the value of "MaxRecipientsPerMessage" is set to a value other than "5000" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259601`

### Rule: Exchange send connector connections count must be limited.

**Rule ID:** `SV-259601r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the maximum number of simultaneous outbound connections allowed for a given SMTP Connector and can be used to throttle the SMTP service if resource constraints warrant it. If the limit is too low, connections may be dropped. If the limit is too high, some domains may use a disproportionate resource share, denying access to other domains. Appropriate tuning reduces the risk of data delay or loss.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the value for SMTP Server Maximum Outbound Connections. Open the Exchange Management Shell and enter the following command: Get-TransportService | Select-Object -Property Name, Identity, MaxOutboundConnections If the value of "MaxOutboundConnections" is not set to "1000", this is a finding. or If the value of "MaxOutboundConnections" is set to a value other than "1000" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259602`

### Rule: Exchange message size restrictions must be controlled on Send connectors.

**Rule ID:** `SV-259602r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. For message size restrictions, multiple places exist to set or override inbound or outbound message size. Failure to control the configuration strategy can result in loss of data or system availability. This setting enables the administrator to control the maximum message size on a Send connector. Using connectors to control size limits may necessitate applying message size limitations in multiple places, with the potential of introducing conflicts and impediments in the mail flow. Changing this setting at the connector overrides the global one. Therefore, if operational needs require it, the connector value may be set lower than the global value with the rationale documented in the EDSP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the maximum message send size. Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, MaxMessageSize For each send connector, if the value of "MaxMessageSize" is not the same as the global value, this is a finding. or If "MaxMessageSize" is set to a numeric value different from the maximum message send size value documented in the EDSP, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259603`

### Rule: Exchange send connectors delivery retries must be controlled.

**Rule ID:** `SV-259603r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls the rate at which delivery attempts from the home domain are retried and user notifications are issued and notes the expiration time when the message will be discarded. If delivery retry attempts are too frequent, servers will generate network congestion. If they are too far apart, messages may remain queued longer than necessary, potentially raising disk resource requirements. The default values of these fields should be adequate for most environments. Administrators may wish to modify the values, but changes should be documented in the System Security Plan. Note: Transport configuration settings apply to the organization/global level of the Exchange SMTP path. By checking and setting them at the Hub server, the setting will apply to both Hub and Edge roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the value for Transient Failure Retry Count. Open the Exchange Management Shell and enter the following command: Get-TransportService | Select-Object -Property Name, Identity, TransientFailureRetryCount If the value of "TransientFailureRetryCount" is not set to "10" or less, this is a finding. or If the value of "TransientFailureRetryCount" is set to more than "10" or has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259604`

### Rule: Exchange receive connectors must be clearly named.

**Rule ID:** `SV-259604r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>For receive connectors, unclear naming as to direction and purpose increases risk that messages may not flow as intended, troubleshooting efforts may be impaired, or incorrect assumptions may be made about the completeness of the configuration. Collectively, connectors should account for all connections required for the overall email topology design. Simple Mail Transfer Protocol (SMTP) connectors, when listed, must name purpose and direction clearly, and their counterparts on servers to which they connect should be recognizable as their partners.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity For each receive connector, review the naming for connectors. If the connectors are not clearly named for purpose and direction, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259605`

### Rule: Exchange receive connectors must control the number of recipients chunked on a single message.

**Rule ID:** `SV-259605r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. For message size restrictions, multiple places exist to set or override inbound or outbound message size. Failure to control the configuration strategy can result in loss of data or system availability. This setting enables the administrator to enable "chunking" on received messages as they arrive at the domain. This is done so large message bodies can be relayed by the remote sender to the Receive connector in multiple, smaller chunks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, ChunkingEnabled For each receive connector, if the value of "ChunkingEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259606`

### Rule: The Exchange internet receive connector connections count must be set to default.

**Rule ID:** `SV-259606r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the maximum number of simultaneous inbound connections allowed to the SMTP server. By default, the number of simultaneous inbound connections is 5000. If a limit is set too low, the connections pool may be filled. If attackers perceive the limit is too low, they could deny service to the Simple Mail Transfer Protocol (SMTP) server by using a connection count that exceeds the limit set. By setting the default configuration to 5000, attackers would need many more connections to cause denial of service.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the Maximum Inbound connections value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, MaxInboundConnection Identify internet-facing connectors. For each receive connector, if the value of "MaxInboundConnection" is not set to "5000", this is a finding. or If "MaxInboundConnection" is set to a value other than "5000" or is set to unlimited and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-259607`

### Rule: Exchange Message size restrictions must be controlled on receive connectors.

**Rule ID:** `SV-259607r961155_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practices strategies for setting tuning configurations. For message size restrictions, multiple places exist to set or override inbound or outbound message size. Failure to control the configuration strategy can result in loss of data or system availability. This setting enables the administrator to control the maximum message size on receive connectors. Using connectors to control size limits may necessitate applying message size limitations in multiple places, with the potential of introducing conflicts and impediments in the mail flow. Changing this setting at the connector overrides the global one. Therefore, if operational needs require it, the connector value may be set lower than the global value with the rationale documented in the EDSP.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the global maximum message receive size. Open the Exchange Management Shell and enter the following command: Identify internet-facing connectors. Get-ReceiveConnector | Select-Object -Property Name, Identity, MaxMessageSize If the value of "MaxMessageSize" is not the same as the global value, this is a finding. or If "MaxMessageSize" is set to a numeric value different from the global value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259608`

### Rule: Active hyperlinks in messages from non .mil domains must be rendered unclickable.

**Rule ID:** `SV-259608r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Active hyperlinks within an email are susceptible to attacks of malicious software or malware. The hyperlink could lead to a malware infection or redirect the website to another fraudulent website without the user's consent or knowledge. Exchange does not have a built-in message filtering capability. DOD Enterprise Email (DEE) has created a custom resolution to filter messages from non-.mil users that have hyperlinks in the message body. The hyperlink within the messages will be modified, preventing end users from automatically clicking links.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If using another DOD-approved anti-spam product for email or a DOD-approved Email Gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable. Note: If system is on SIPRNet, this is not applicable. Review the Email Domain Security Plan (EDSP). Determine the name of the Transport Agent. Open the Windows PowerShell console and enter the following command: Get-TransportAgent -Name 'customAgent' | Format-List If the value does not return "customAgent", this is a finding. Note: "customAgent" is the name of the custom agent developed to render hyperlink email sources from non .mil domains as unclickable.

## Group: SRG-APP-000261

**Group ID:** `V-259609`

### Rule: Exchange messages with a blank sender field must be rejected.

**Rule ID:** `SV-259609r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. Anonymous email (messages with blank sender fields) cannot be replied to. Messages formatted in this way may be attempting to hide their true origin to avoid responses or to spam any receiver with impunity while hiding their source of origination. Rather than spend resources and risk infection while evaluating them, it is recommended that these messages be filtered immediately upon receipt and not forwarded to end users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is Not Applicable for SIPR enclaves. This requirement is Not Applicable if the organization subscribes to EEMSG or other similar DOD enterprise protections for email services. Open the Exchange Management Shell and enter the following command: Get-SenderFilterConfig | Select-Object -Property Name, Action If the value of "Action" is not set to "Reject", this is a finding. Note: "Reject" is the default value.

## Group: SRG-APP-000261

**Group ID:** `V-259610`

### Rule: Exchange messages with a blank sender field must be filtered.

**Rule ID:** `SV-259610r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. Anonymous email (messages with blank sender fields) cannot be replied to. Messages formatted in this way may be attempting to hide their true origin to avoid responses or to spam any receiver with impunity while hiding their source of origination. Rather than spend resources and risk infection while evaluating them, it is recommended that these messages be filtered immediately upon receipt and not forwarded to end users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is Not Applicable for SIPR enclaves. This requirement is Not Applicable if the organization subscribes to EEMSG or other similar DOD enterprise protections for email services. Open the Exchange Management Shell and enter the following command: Get-SenderFilterConfig | Select-Object -Property Name, BlankSenderBlockingEnabled If the value of "BlankSenderBlockingEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259611`

### Rule: Exchange filtered messages must be archived.

**Rule ID:** `SV-259611r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. This significantly reduces the attack vector for inbound email-borne spam and malware. As messages are filtered, it is prudent to temporarily host them in an archive for evaluation by administrators or users. The archive can be used to recover messages that might have been inappropriately filtered, preventing data loss, and to provide a base of analysis that can provide future filter refinements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Select-Object -Property Name, quarantineMailbox If no SMTP address is assigned to "quarantineMailbox", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259612`

### Rule: The Exchange sender filter must block unaccepted domains.

**Rule ID:** `SV-259612r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spam origination sites and other sources of suspected email-borne malware have the ability to corrupt, compromise, or otherwise limit availability of email servers. Limiting exposure to unfiltered inbound messages can reduce the risk of spam and malware impacts. The Global Deny list blocks messages originating from specific sources. Most block list filtering is done using a commercial block list service, because eliminating threats from known spammers prevents the messages being evaluated inside the enclave where there is more risk they can do harm. Additional sources should also be blocked to supplement the contents of the commercial Block List service. For example, during a zero-day threat action, entries can be added and then removed when the threat is mitigated. An additional best practice is to enter the enterprise's home domains in the block list, because inbound email with a "from" address of the home domain is very likely to be spoofed spam.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Review the Email Domain Security Plan (EDSP). Determine the unaccepted domains that are to be blocked. Open the Exchange Management Shell and enter the following command: Get-SenderFilterConfig | Select-Object -Property Name, BlockedDomains, BlockedDomainsAndSubdomains If the value for "BlockedDomains" or "BlockedDomainsAndSubdomains" does not reflect the list of accepted domains, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259613`

### Rule: Exchange nonexistent recipients must not be blocked.

**Rule ID:** `SV-259613r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spam originators, in an effort to refine mailing lists, sometimes use a technique where they first create fictitious names and then monitor rejected emails for nonexistent recipients. Those not rejected are deemed to exist and are used in future spam mailings. To prevent this disclosure of existing email accounts to spammers, email to nonexistent recipients must not be blocked. Instead, it is recommended that all messages be received, then evaluated and disposed of without enabling the sender to determine existent versus nonexistent recipients.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Additionally, the default value for "RecipientValidationEnabled" is "False". Open the Exchange Management Shell and enter the following command: Get-RecipientFilterConfig | Select-Object -Property Name, RecipientValidationEnabled If the value of "RecipientValidationEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259614`

### Rule: The Exchange Sender Reputation filter must be enabled.

**Rule ID:** `SV-259614r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. Sender Reputation is anti-spam functionality that blocks messages according to many characteristics of the sender. Sender Reputation relies on persisted data about the sender to determine what action, if any, to take on an inbound message. This setting enables the Sender Reputation function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Additionally, the default value for "Sender Reputation" is "True" for "Enabled". Open the Exchange Management Shell and enter the following command: Get-SenderReputationConfig | Select-Object -Property Name, Enabled If the value of "Enabled" is not set to "True", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259615`

### Rule: The Exchange Sender Reputation filter must identify the spam block level.

**Rule ID:** `SV-259615r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. Sender Reputation is anti-spam functionality that blocks messages according to many characteristics of the sender. Sender Reputation relies on persisted data about the sender to determine what action, if any, to take on an inbound message. This setting enables the threshold at which an email will be considered spam.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Review the Email Domain Security Plan (EDSP). Determine the SrlBlockThreshold value. Open the Exchange Management Shell and enter the following command: Get-SenderReputationConfig | Select-Object -Property Name, SrlBlockThreshold If the value of SrlBlockThreshold is not set to "6", this is a finding. or If the value of "SrlBlockThreshold" is set to a value other than "6" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259616`

### Rule: Exchange Attachment filtering must remove undesirable attachments by file type.

**Rule ID:** `SV-259616r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages are eliminated from the message stream rather than admitting them into the mail server environment. Attachments are being used more frequently for different forms of attacks. By filtering undesirable attachments, a large percent of malicious code can be prevented from entering the system. Attachments must be controlled at the entry point into the email environment to prevent successful attachment-based attacks. The following is a basic list of known attachments that should be filtered from internet mail attachments: *.ade *.crt *.jse *.msi *.scr *.wsh *.dir *.adp *.csh *.ksh *.msp *.sct *.htm *.dcr *.app *.exe *.lnk *.mst *.shb *.html *.plg *.asx *.fxp *.mda *.ops *.shs *.htc *.spl *.bas *.hlp *.mdb *.pcd *.url *.mht *.swf *.bat *.hta *.mde *.pif *.vb *.mhtml *.zip *.chm *.inf *.mdt *.prf *.vbe *.shtm *.cmd *.ins *.mdw *.prg *.vbs *.shtml *.com *.isp *.mdz *.reg *.wsc *.stm *.cpl *.js *.msc *.scf *.wsf *.xml</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Review the Email Domain Security Plan (EDSP). Determine the list of undesirable attachment types that should be stripped. Open the Exchange Management Shell and enter the following command: Get-AttachmentFilterEntry For each attachment type, if the values returned are different from the EDSP documented attachment types, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259617`

### Rule: The Exchange Spam Evaluation filter must be enabled.

**Rule ID:** `SV-259617r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By performing filtering at the perimeter, up to 90 percent of spam, malware, and other undesirable messages may be eliminated from the transport message stream, preventing their entry into the Exchange environment. This significantly reduces the attack vector for inbound email-borne spam and malware. Spam Evaluation filters scan inbound email messages for evidence of spam and other attacks that primarily use social engineering techniques. Upon evaluation completion, a rating is assigned to each message estimating the likelihood of its being spam. Upon arrival at the destination mailbox, the junk mail filter threshold (also configurable) determines whether the message will be withheld from delivery, delivered to the junk mail folder, or delivered to the user's inbox.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Additionally, the default value for this property is Enabled "True". Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Select-Object -Property Name, Identity, Enabled If the value of "Enabled" is not set to "True", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259618`

### Rule: The Exchange Block List service provider must be identified.

**Rule ID:** `SV-259618r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Block List filtering is a sanitization process performed on email messages prior to their arrival at the destination mailbox. By performing this process at the email perimeter, threats can be eliminated outside the enclave, where there is less risk for them to do harm. Block List services (sometimes called Reputation Data services) are fee-based data providers that collect the IP addresses of known spammers and other malware purveyors. Block List service subscribers benefit from more effective spam elimination. (Spam is estimated to compose up to 90 percent of inbound mail volume.) Failure to specify a Block List provider risks that manual email administration effort would be needed to maintain and update larger Block Lists than a single email site administrator could conveniently or accurately maintain. The Block List service vendor provides a value for this field, usually the Domain Name System (DNS) suffix for its domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If not using a service provider, this requirement is not applicable. Review the Email Domain Security Plan (EDSP). Determine the name and information for the Block List provider. Open the Exchange Management Shell and enter the following command: Get-IPBlockListProvider | Select-Object -Property Name, Identity, LookupDomain If the values for "Name", GUID, and "LookupDomain" are not configured, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259619`

### Rule: Exchange messages with a malformed From address must be rejected.

**Rule ID:** `SV-259619r1040909_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Sender Identification (SID) is an email anti-spam sanitization process. Sender ID uses DNS MX record lookups to verify the Simple Mail Transfer Protocol (SMTP) sending server is authorized to send email for the originating domain. Failure to implement Sender ID risks that spam could be admitted into the email domain that originates from rogue servers. Most spam content originates from domains where the IP address has been spoofed prior to sending, thereby avoiding detection. For example, messages with malformed or incorrect "purported responsible sender" data in the message header could be (best case) created by using RFI noncompliant software but is more likely to be spam.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If this server is in a SIPR Enclave, this requirement is Not Applicable. Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Open the Exchange Management Shell and enter the following command: Get-SenderIdConfig | Select-Object -Property Name, Identity, SpoofedDomainAction If the value of "SpoofedDomainAction" is not set to "Reject", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259620`

### Rule: The Exchange Recipient filter must be enabled.

**Rule ID:** `SV-259620r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. Careful tuning reduces the risk that system or network congestion will contribute to availability impacts. Filters that govern inbound email evaluation can significantly reduce spam, phishing, and spoofed emails. Messages from blank senders, known spammers, or zero-day attack modifications must be enabled to be effective.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-RecipientFilterConfig | Select-Object -Property Name, Enabled If the value of "Enabled" is not set to "True", this is a finding. Note: The default value is set to "True".

## Group: SRG-APP-000261

**Group ID:** `V-259621`

### Rule: The Exchange tarpitting interval must be set.

**Rule ID:** `SV-259621r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Tarpitting is the practice of artificially delaying server responses for specific Simple Mail Transfer Protocol (SMTP) communication patterns that indicate high volumes of spam or other unwelcome messages. The intent of tarpitting is to slow down the communication process for spam batches to reduce the cost effectiveness of sending spam and thwart directory harvest attacks. A directory harvest attack is an attempt to collect valid email addresses from a particular organization so the email addresses can be added to a spam database. A program can be written to collect email addresses that return a "Recipient OK" SMTP response and discard all email addresses that return a "User unknown" SMTP response. Tarpitting makes directory harvest attacks too costly to automate efficiently.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, TarpitInterval For each Receive connector, if the value of "TarpitInterval" is not set to "00:00:05" or greater, this is a finding. Note: The default value for "TarpitInterval" is "00:00:05".

## Group: SRG-APP-000261

**Group ID:** `V-259622`

### Rule: Exchange internal Receive connectors must not allow anonymous connections.

**Rule ID:** `SV-259622r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control is used to limit the servers that may use this server as a relay. If a Simple Mail Transport Protocol (SMTP) sender does not have a direct connection to the internet (for example, an application that produces reports to be emailed), it will need to use an SMTP Receive connector that does have a path to the internet (for example, a local email server) as a relay. SMTP relay functions must be protected so third parties are not able to hijack a relay service for their own purposes. Most commonly, relay hijacking is done by spammers to disguise the source of their messages and may also be used to cover the source of more destructive attacks. Relays can be restricted in one of three ways: by blocking relays (restrict to a blank list of servers); by restricting use to lists of valid servers; or by restricting use to servers that can authenticate. Because authenticated connections are the most secure for SMTP Receive connectors, it is recommended that relays allow only servers that can authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, PermissionGroups |Format-List For each Receive connector, if the value of "PermissionGroups" is "AnonymousUsers" for any noninternet connector, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259623`

### Rule: Exchange Simple Mail Transfer Protocol (SMTP) IP Allow List entries must be empty.

**Rule ID:** `SV-259623r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. Careful tuning reduces the risk that system or network congestion will contribute to availability impacts. Filters that govern inbound email evaluation can significantly reduce spam, phishing, and spoofed emails. Filters for messages from blank senders, known spammers, or zero-day attack modifications must be enabled to be effective. Having items identified in the Allow List causes other spam evaluation steps to be bypassed and therefore should be used only with an abundance of caution. If spammers were to learn of entries in the Allow List, it could enable them to plan a denial of service attack (or other attack) by spoofing that source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Identify the SMTP Allow List settings. Open the Exchange Management Shell and enter the following command: Get-IPAllowListEntry | Format-List If the result returns any values, this is a finding. or If the result returns any values but has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259624`

### Rule: The Exchange Simple Mail Transfer Protocol (SMTP) IP Allow List Connection filter must be enabled.

**Rule ID:** `SV-259624r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. Careful tuning reduces the risk that system or network congestion will contribute to availability impacts. Filters that govern inbound email evaluation can significantly reduce spam, phishing, and spoofed emails. Filters for messages from blank senders, known spammers, or zero-day attack modifications must be enabled to be effective. Having items identified in the Allow List causes other spam evaluation steps to be bypassed and therefore should be used only with an abundance of caution. If spammers were to learn of entries in the Allow List, it could enable them to plan a denial of service attack (or other attack) by spoofing that source.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-IPAllowListConfig | Select-Object -Property Name, Enabled If the value for "Enabled" is not set to "True", this is a finding. Note: "Enabled" set to "True" is the default value.

## Group: SRG-APP-000261

**Group ID:** `V-259625`

### Rule: The Exchange Simple Mail Transfer Protocol (SMTP) Sender filter must be enabled.

**Rule ID:** `SV-259625r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practices strategies for setting tuning configurations. Careful tuning reduces the risk that system or network congestion will contribute to availability impacts. Filters that govern inbound email evaluation can significantly reduce spam, phishing, and spoofed emails. Filters for messages from blank senders, known spammers, or zero-day attack modifications must be enabled to be effective. Failure to enable the filter will result in no action taken. This setting should always be enabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This requirement is not applicable for SIPR enclaves. This requirement is not applicable if the organization subscribes to EEMSG or other similar DOD enterprise protections for email services. Open the Exchange Management Shell and enter the following command: Get-SenderFilterConfig | Select-Object -Property Name, Enabled If the value of "Enabled" is not set to "True", this is a finding. Note: "Enabled" set to "True" is the default value.

## Group: SRG-APP-000261

**Group ID:** `V-259626`

### Rule: Exchange must have anti-spam filtering installed.

**Rule ID:** `SV-259626r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2019 provides both anti-spam and anti-malware protection out of the box. The Exchange 2019 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) for an installed anti-spam product. Note: If using another DOD-approved anti-spam product for email or a DOD-approved Email Gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable. Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Format-Table Name, Enabled If no value is returned, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259627`

### Rule: Exchange must have anti-spam filtering enabled.

**Rule ID:** `SV-259627r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2019 provides both anti-spam and anti-malware protection out of the box. The Exchange 2019 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) for an installed anti-spam product. Note: If using another DOD-approved anti-spam product for email or a DOD-approved Email Gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable. Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Format-Table Name, Enabled; Get-SenderFilterConfig | Format-Table Name, Enabled; Get-SenderIDConfig | Format-Table Name, Enabled; Get-SenderReputationConfig | Format-Table Name, Enabled If any of the following values returned are not set to "True", this is a finding: Set-ContentFilterConfig Set-SenderFilterConfig Set-SenderIDConfig Set-SenderReputationConfig

## Group: SRG-APP-000261

**Group ID:** `V-259628`

### Rule: Exchange must have anti-spam filtering configured.

**Rule ID:** `SV-259628r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. A manual update procedure is labor intensive and does not scale well in an enterprise environment. This risk may be mitigated by using an automatic update capability. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2019 provides both anti-spam and anti-malware protection out of the box. The Exchange 2019 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
The site should use an approved DOD scanner as Exchange Malware software has a limited scanning capability. If an approved DOD scanner is not being used, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-259629`

### Rule: Exchange Sender Identification Framework must be enabled.

**Rule ID:** `SV-259629r961161_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email is only as secure as the recipient. When the recipient is an email server accepting inbound messages, authenticating the sender enables the receiver to better assess message quality and to validate the sending domain as authentic. One or more authentication techniques used in combination can be effective in reducing spam, phishing, and forger attacks. The Sender ID Framework (SIDF) receiver accesses specially formatted DNS records (SPF format) that contain the IP address of authorized sending servers for the sending domain that can be compared to data in the email message header. Receivers are able to validate the authenticity of the sending domain, helping to avoid receiving inbound messages from phishing or other spam domains.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If third-party anti-spam product is being used, the anti-spam product must be configured to meet the requirement. Open the Exchange Management Shell and enter the following command: Get-SenderIdConfig | Select-Object -Property Name, Identity, Enabled If the value of "Enabled" is not set to "True", this is a finding. Note: By Default, the value of "Enabled" is set to "True".

## Group: SRG-APP-000295

**Group ID:** `V-259630`

### Rule: Exchange must limit the Receive connector timeout.

**Rule ID:** `SV-259630r1043182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Email system availability depends in part on best practices strategies for setting tuning. This configuration controls the number of idle minutes before the connection is dropped. It works in conjunction with the Maximum Inbound Connections Count setting.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP), or Organizations applicable documentation. Determine the connection Timeout value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, ConnectionTimeout For each Receive connector, if the value of "ConnectionTimeout" is not set to "00:05:00", this is a finding. If "ConnectionTimeout" is set to another value other than "00:05:00" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000340

**Group ID:** `V-259631`

### Rule: Role-Based Access Control must be defined for privileged and nonprivileged users.

**Rule ID:** `SV-259631r961353_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Role Based Access Control (RBAC) is the permissions model used in Microsoft Exchange Server 2013, 2016, and 2019. With RBAC, there is no need to modify and manage access control lists (ACLs), which was done in Exchange Server 2007. ACLs created several challenges in Exchange 2007, such as modifying ACLs without causing unintended consequences, maintaining ACL modifications through upgrades, and troubleshooting problems that occurred due to using ACLs in a nonstandard way. RBAC enables users to control, at both broad and granular levels, what administrators and end users can do. RBAC also enables users to more closely align the roles assigned to users and administrators to the actual roles they hold within the organization. In Exchange 2007, the server permissions model applied only to the administrators who managed the Exchange 2007 infrastructure. Starting in Exchange 2013, RBAC now controls both the administrative tasks that can be performed and the extent to which users can now administer their own mailbox and distribution groups.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the EDSP to verify who should be in each built in RBAC management role group. If this is not found, this is a finding.

## Group: SRG-APP-000378

**Group ID:** `V-259632`

### Rule: The Exchange application directory must be protected from unauthorized access.

**Rule ID:** `SV-259632r1015763_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Default product installations may provide more generous access permissions than are necessary to run the application. By examining and tailoring access permissions to provide the least amount of privilege possible more closely, attack vectors that align with user permissions are less likely to access more highly secured areas.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the authorized groups and users that have access to the Exchange application directories. Determine if the access permissions on the directory match the access permissions listed in the EDSP. If any group or user has different access permissions than listed in the EDSP, this is a finding. Note: The default installation directory is \Program Files\Microsoft\Exchange Server\V15.

## Group: SRG-APP-000380

**Group ID:** `V-259633`

### Rule: The Exchange software baseline copy must exist.

**Rule ID:** `SV-259633r961461_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange software, as with other application software installed on a host system, must be included in a system baseline record and periodically reviewed; otherwise, unauthorized changes to the software may not be discovered. This effort is a vital step to securing the host and the applications, as it is the only method that may provide the ability to detect and recover from otherwise undetected changes, such as those that result from worm or bot intrusions. The Exchange software and configuration baseline is created and maintained for comparison during scanning efforts. Operational procedures must include baseline updates as part of configuration management tasks that change the software and configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the baseline documentation. Review the application software baseline procedures and implementation artifacts. Note the list of files and directories included in the baseline procedure for completeness. If an email software copy exists to serve as a baseline and is available for comparison during scanning efforts, this is not a finding.

## Group: SRG-APP-000381

**Group ID:** `V-259634`

### Rule: The Exchange local machine policy must require signed scripts.

**Rule ID:** `SV-259634r1015764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts, especially those downloaded from untrusted locations, often provide a way for attackers to infiltrate a system. By setting machine policy to prevent unauthorized script executions, unanticipated system impacts can be avoided.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExecutionPolicy If the value returned is not "RemoteSigned", this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-259635`

### Rule: Exchange services must be documented, and unnecessary services must be removed or disabled.

**Rule ID:** `SV-259635r961470_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unneeded but running services offer attackers an enhanced attack profile, and attackers are constantly watching to discover open ports with running services. By analyzing and disabling unneeded services, the associated open ports become unresponsive to outside queries, and servers become more secure as a result. Exchange Server has role-based server deployment to enable protocol path control and logical separation of network traffic types. For example, a server implemented in the Client Access role (i.e., Outlook Web App [OWA]) is configured and tuned as a web server using web protocols. A client access server exposes only web protocols (HTTP/HTTPS), enabling system administrators to optimize the protocol path and disable all services unnecessary for Exchange web services. Similarly, servers created to host mailboxes are dedicated to that task and must operate only the services needed for mailbox hosting. (Exchange servers must also operate some web services but only to the degree that Exchange requires the IIS engine in order to function). Because POP3 and IMAP4 clients are not included in the standard desktop offering, they must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Note: Required services will vary between organizations and will vary depending on the role of the individual system. Organizations will develop their own list of services, which will be documented and justified with the ISSO. The site's list will be provided for any security review. Services that are common to multiple systems can be addressed in one document. Exceptions for individual systems should be identified separately by system. Open a Windows PowerShell and enter the following command: Get-Service | Where-Object {$_.status -eq 'running'} Note: The command returns a list of installed services and the status of that service. If the services required are not documented in the EDSP or undocumented or unnecessary services are running, this is a finding.

## Group: SRG-APP-000424

**Group ID:** `V-259636`

### Rule: The Exchange Edge server must point to a trusted list of DNS servers for external and internal resolution.

**Rule ID:** `SV-259636r961587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of possible erroneous queries that may have been coopted by bad actors, the Exchange Edge server must use DNS servers that utilize DNSSEC to resolve external hosts and internal hosts before routing messages to the appropriate destination.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify in the EDSP or consult with the appropriate personnel who manage DNS which servers to use for Internal and External DNS resolution. If the server is not multi-homed, this does not apply. In Exchange Management Shell, run the following command: Get-TransportService |Format-List *dns* If "ExternalDNSAdapterEnabled : True", and no GUID exists, this is a finding. If "ExternalDNSAdapterEnabled : False", and the property "ExternalDNSServers" is not populated with the documented trusted DNS servers for External DNS queries, this is a finding. If "InternalDNSAdapterEnabled : True" and no GUID exists, this is a finding. If "InternalDNSAdapterEnabled : False" and the property "InternalDNSServers" is not populated the documented trusted DNS servers for Internal DNS queries, this is a finding.

## Group: SRG-APP-000431

**Group ID:** `V-259637`

### Rule: Exchange software must be installed on a separate partition from the OS.

**Rule ID:** `SV-259637r961608_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the same way that added security layers can provide a cumulative positive effect on security posture, multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to the host system can most likely lead to a compromise of all applications hosted by the same system. Email services should be installed on a partition that does not host other applications. Email services should never be installed on a Domain Controller/Directory Services server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the directory where Exchange is installed. Open Windows Explorer. Navigate to the location where Exchange is installed. If Exchange resides on a directory or partition other than that of the OS and does not have other applications installed (without associated approval from the ISSO), this is not a finding.

## Group: SRG-APP-000435

**Group ID:** `V-259638`

### Rule: The Exchange SMTP automated banner response must not reveal server details.

**Rule ID:** `SV-259638r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated connection responses occur as a result of FTP or Telnet connections when connecting to those services. They report a successful connection by greeting the connecting client and stating the name, release level, and (often) additional information about the responding product. While useful to the connecting client, connection responses can also be used by a third party to determine operating system or product release levels on the target server. The result can include disclosure of configuration information to third parties, paving the way for possible future attacks. For example, when querying the SMTP service on port 25, the default response looks similar to this one: 220 exchange.mydomain.org Microsoft ESMTP MAIL Service ready at Tuesday, 23 Nov 2021 13:43:00 -0500 Changing the response to hide local configuration details reduces the attack profile of the target.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, Banner If the value of "Banner" is not set to "220 SMTP Server Ready", this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-259639`

### Rule: Exchange internal Send connectors must use an authentication level.

**Rule ID:** `SV-259639r961620_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) connector is used by Exchange to send and receive messages from server to server. Several controls work together to provide security between internal servers. This setting controls the encryption method used for communications between servers. With this feature enabled, only servers capable of supporting Transport Layer Security (TLS) will be able to send and receive mail within the domain. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from server to server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption can be compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, TlsAuthLevel If the value of "TlsAuthLevel" is not set to "DomainValidation", this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-259640`

### Rule: Exchange must provide redundancy.

**Rule ID:** `SV-259640r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Denial of Service (DoS) is a condition when a resource is not available for legitimate users. When this occurs, the organization either cannot accomplish its mission or must operate at degraded capacity. This requirement addresses the configuration of applications to mitigate the impact of DoS attacks that have occurred or are ongoing on application availability. For each application, known and potential DoS attacks must be identified and solutions for each type implemented. A variety of technologies exist to limit or, in some cases, eliminate the effects of DoS attacks (e.g., limiting processes or restricting the number of sessions the application opens at one time). Employing increased capacity and bandwidth, combined with service redundancy, may reduce the susceptibility to some DoS attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). From a Mailbox server in the subscribed Edge Subscription site, determine if the Exchange servers are using redundancy by entering the following command: Get-EdgeSubscription If the value returned is not at least two Edge servers, this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-259641`

### Rule: Exchange internal Receive connectors must require encryption.

**Rule ID:** `SV-259641r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) Receive connector is used by Exchange to send and receive messages from server to server using SMTP protocol. This setting controls the encryption strength used for client connections to the SMTP Receive connector. With this feature enabled, only clients capable of supporting secure communications will be able to send mail using this SMTP server. Where secure channels are required, encryption can also be selected. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from the client to the server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption have been compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between the client and server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select-Object -Property Name, Identity, AuthMechanism For each Receive connector, if the value of "AuthMechanism" is not set to "Tls", this is a finding.

## Group: SRG-APP-000439

**Group ID:** `V-259642`

### Rule: Exchange internal Send connectors must require encryption.

**Rule ID:** `SV-259642r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) connector is used by Exchange to send and receive messages from server to server. Several controls work together to provide security between internal servers. This setting controls the encryption method used for communications between servers. With this feature enabled, only servers capable of supporting Transport Layer Security (TLS) will be able to send and receive mail within the domain. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from server to server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption can be compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the Email Domain Security Plan (EDSP) and determine which send connector is using which secure validation method. If no configuration setting is found, this is a finding. If using "DomainValidation", open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, TlsDomain If the value of "TlsDomain" is not set to the value of the internal <'SMTP Domain'>, this is a finding. If using "DomainSecureEnabled", open the Exchange Management Shell and enter the following command: Get-SendConnector | Select-Object -Property Name, Identity, DomainSecureEnabled If the value of 'DomainSecureEnabled' is not set to 'True', this is a finding. Note: The wildcard character (*) is not supported in domains that are configured for mutual TLS authentication. The same domain must also be defined on the corresponding Receive connector and in the TLSReceiveDomainSecureList attribute of the transport configuration.

## Group: SRG-APP-000441

**Group ID:** `V-259643`

### Rule: Exchange must render hyperlinks from email sources from non-.mil domains as unclickable.

**Rule ID:** `SV-259643r961638_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Active hyperlinks within an email are susceptible to attacks of malicious software or malware. The hyperlink could lead to a malware infection or redirect the website to another fraudulent website without the user's consent or knowledge. Exchange does not have a built-in message filtering capability. DOD Enterprise Email (DEE) has created a custom resolution to filter messages from non-.mil users that have hyperlinks in the message body. The hyperlink within the messages will be modified, preventing end users from automatically clicking links.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If using another DOD-approved anti-spam product for email or a DOD-approved Email Gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable. Note: If system is on SIPRNet, this is not applicable. Review the Email Domain Security Plan (EDSP). Determine the name of the Transport Agent. Open the Windows PowerShell console and enter the following command: Get-TransportAgent -Name 'customAgent' | Format-List If the value does not return "customAgent", this is a finding. Note: "customAgent" is the name of the custom agent developed to render hyperlink email sources from non .mil domains as unclickable.

## Group: SRG-APP-000456

**Group ID:** `V-259644`

### Rule: Exchange must have the most current, approved Cumulative Update (CU) installed.

**Rule ID:** `SV-259644r961683_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The organization (including any contractor to the organization) must promptly install security-relevant software updates (e.g., patches, service packs, CUs, hot fixes). Flaws discovered during security assessments, continuous monitoring, incident response activities, or information system error handling must also be addressed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExchangeServer | Format-List Name, AdminDisplayVersion If the value of "AdminDisplayVersion" does not return the most current, approved CU, this is a finding.

