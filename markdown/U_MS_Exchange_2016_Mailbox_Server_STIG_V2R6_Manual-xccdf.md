# STIG Benchmark: Microsoft Exchange 2016 Mailbox Server Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000027

**Group ID:** `V-228354`

### Rule: Exchange must have Administrator audit logging enabled.

**Rule ID:** `SV-228354r879526_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unauthorized or malicious data changes can compromise the integrity and usefulness of the data. Automated attacks or malicious users with elevated privileges have the ability to effect change using the same mechanisms as email administrators. Auditing any changes to access mechanisms not only supports accountability and nonrepudiation for those authorized to define the environment but also enables investigation of changes made by others who may not be authorized. Note: This administrator auditing feature audits all exchange changes regardless of the user's assigned role or permissions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-AdminAuditLogConfig | Select Name, AdminAuditLogEnabled If the value of "AdminAuditLogEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-228355`

### Rule: Exchange servers must use approved DoD certificates.

**Rule ID:** `SV-228355r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Server certificates are required for many security features in Exchange; without them, the server cannot engage in many forms of secure communication. Failure to implement valid certificates makes it virtually impossible to secure Exchange's communications.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExchangeCertificate | Select CertificateDomains, issuer If the value of "CertificateDomains" does not indicate it is issued by the DoD, this is a finding.

## Group: SRG-APP-000038

**Group ID:** `V-228356`

### Rule: Exchange auto-forwarding email to remote domains must be disabled or restricted.

**Rule ID:** `SV-228356r879533_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers can use automated messages to determine whether a user account is active, in the office, traveling, and so on. An attacker might use this information to conduct future attacks. Verify Automatic Forwards to remote domains are disabled, except for enterprise mail that must be restricted to forward only to .mil and .gov. domains. Before enabling this setting, configure a remote domain.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Requirement is not applicable on classified or completely closed networks. Non-Enterprise Mail Check Content: Open the Exchange Management Shell and enter the following command: Get-RemoteDomain | Select Identity, AutoForwardEnabled If the value of AutoForwardEnabled is not set to "False", this is a finding. Enterprise Mail Check Content: If the value of "AutoForwardEnabled" is set to "True", this is not a finding. and In the Exchange Management Shell, enter the following command: Get-RemoteDomain If the value of "RemoteDomain" is not set to ".mil" and/or ".gov" domain(s), this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-228357`

### Rule: Exchange Connectivity logging must be enabled.

**Rule ID:** `SV-228357r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A connectivity log is a record of the SMTP connection activity of the outbound message delivery queues to the destination Mailbox server, smart host, or domain. Connectivity logging is available on Hub Transport servers and Edge Transport servers. By default, connectivity logging is disabled. If events are not recorded, it may be difficult or impossible to determine the root cause of system problems or the unauthorized activities of malicious users. Note: Transport configuration settings apply to the organization/global level of the Exchange SMTP path. By checking and setting them at the Hub server, the setting will apply to both Hub and Edge roles.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-TransportService | Select Name, Identity, ConnectivityLogEnabled If the value of "ConnectivityLogEnabled" is not set to "True", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-228358`

### Rule: The Exchange Email Diagnostic log level must be set to the lowest level.

**Rule ID:** `SV-228358r879559_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Diagnostic logging, however, characteristically produces large volumes of data and requires care in managing the logs to prevent risk of disk capacity denial-of-service conditions. Exchange diagnostic logging is divided into 29 main "services", each of which has anywhere from 2 to 26 "categories" of events to be monitored. Each category may be set to one of four levels of logging: Lowest, Low, Medium, and High, depending on how much detail is required. Higher levels of detail require more disk space to store the audit material. Diagnostic logging is intended to help administrators debug problems with their systems, not as a general-purpose auditing tool. Because the diagnostic logs collect a great deal of information, the log files may grow large very quickly. Diagnostic log levels may be raised for limited periods of time when attempting to debug relevant pieces of Exchange functionality. Once debugging has finished, diagnostic log levels should be reduced again.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-EventLogLevel If the Diagnostic of any EventLevel is not set to "Lowest", this is a finding.

## Group: SRG-APP-000089

**Group ID:** `V-228359`

### Rule: Exchange Audit record parameters must be set.

**Rule ID:** `SV-228359r879559_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts. This item declares the fields that must be available in the audit log file in order to adequately research events that are logged. Audit records should include the following fields to supply useful event accounting: Object modified, Cmdlet name, Cmdlet parameters, Modified parameters, Caller, Succeeded, and Originating server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-AdminAuditLogConfig | Select AdminAuditLogParameters Note: The value of "*" indicates all parameters are being audited. If the value of "AdminAuditLogParameters" is not set to "*", this is a finding.

## Group: SRG-APP-000098

**Group ID:** `V-228360`

### Rule: Exchange Circular Logging must be disabled.

**Rule ID:** `SV-228360r879566_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Logging provides a history of events performed and can also provide evidence of tampering or attack. Failure to create and preserve logs adds to the risk that suspicious events may go unnoticed and raises the potential that insufficient history will be available to investigate them. This setting controls how log files are written. If circular logging is enabled, one log file is stored with a default size of 1024 KB. Once the size limit has been reached, additional log entries overwrite the oldest log entries. If circular logging is disabled, once a log file reaches the size limit, a new log file is created. Mailbox should not use circular logging. Logs should be written to a partition separate from the operating system, with log protection and backups being incorporated into the overall System Security Plan.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase | Select Name, Identity, CircularLoggingEnabled If the value of "CircularLoggingEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000098

**Group ID:** `V-228361`

### Rule: Exchange Email Subject Line logging must be disabled.

**Rule ID:** `SV-228361r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. When "message tracking" is enabled, only the sender, recipients, time, and other delivery information is included by default. Information such as the subject and message body is not included. However, the absence of the message subject line can make it difficult to locate a specific message in the log unless one knows roughly what time the message was sent. To simplify searches through these logs, Exchange offers the ability to include the message "subject line" in the log files and in the Message Tracking Center display. This can make it significantly easier to locate a specific message. However, this feature creates larger log files and will contain information that may raise privacy and legal concerns. Enterprise policy should be consulted before this feature is enabled. Also, because the log files may contain sensitive information in the form of the subject line, the log files will need to be protected, commensurate with the sensitivity level, as the content may be of interest to an attacker. For these reasons, it is recommended that subject logging not be enabled during regular production operations. Instead, treat this feature as a diagnostic that can be used if needed. The tradeoff is that finding the correct message in the message tracking logs will become more difficult because the administrator will need to search using only the time the message was sent and the message’s sender. This control will have no effect unless Message Tracking is enabled. However, the setting should be disabled in case message tracking is enabled in the future.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-TransportService | Select Name, Identity, MessageTrackingLogSubjectLoggingEnabled If the value of “MessageTrackingLogSubjectLoggingEnabled” is not set to “False”, this is a finding.

## Group: SRG-APP-000098

**Group ID:** `V-228362`

### Rule: Exchange Message Tracking Logging must be enabled.

**Rule ID:** `SV-228362r879566_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A message tracking log provides a detailed log of all message activity as messages are transferred to and from a computer running Exchange. If events are not recorded, it may be difficult or impossible to determine the root cause of system problems or the unauthorized activities of malicious users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-Transportservice | Select Name, MessageTrackingLogEnabled If the value of MessageTrackingLogEnabled is not set to True, this is a finding.

## Group: SRG-APP-000111

**Group ID:** `V-228363`

### Rule: Exchange Queue monitoring must be configured with threshold and action.

**Rule ID:** `SV-228363r879572_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitors are automated "process watchers" that respond to performance changes and can be useful in detecting outages and alerting administrators where attention is needed. Exchange has built-in monitors that enable the administrator to generate alerts if thresholds are reached, better enabling them to react in a timely fashion. This field offers choices of alerts when a "warning" or "critical" threshold is reached on the SMTP queue. A good rule of thumb (default) is to issue warnings when SMTP queue growth exceeds 10 minutes and critical messages when it exceeds 20 minutes, which should only happen occasionally. Frequent alerts against this counter may indicate a network or other issue (such as inbound ExchangeMER traffic) that directly impacts email delivery. Notification choices include email alert to an email-enabled account (for example, an email Administrator) or invoke a script to take other action (for example, to add an Event to the Microsoft Application Event Log, where external monitors might detect it).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: If a third-party application is performing monitoring functions, the reviewer should verify the application is monitoring correctly and mark the vulnerability not applicable (NA). Open the Exchange Management Shell and enter the following command: perfmon Get-MonitoringItemHelp -Identity <String> -Server <ServerIdParameter> If no sets are defined or queues are not being monitored, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-228364`

### Rule: Exchange Send Fatal Errors to Microsoft must be disabled.

**Rule ID:** `SV-228364r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include but are not limited to advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission but that cannot be disabled. All system errors in Exchange will result in outbound traffic that may be identified by an eavesdropper. For this reason, the "Report Fatal Errors to Microsoft" feature must be disabled.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExchangeServer –status | Select Name, Identity, ErrorReportingEnabled For each Exchange Server, if the value of "ErrorReportingEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000118

**Group ID:** `V-228365`

### Rule: Exchange must protect audit data against unauthorized read access.

**Rule ID:** `SV-228365r879576_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted "Read" and "Write" access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the authorized groups or users that should have "Read" access to the audit data. If any group or user has "Read" access to the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-228366`

### Rule: Exchange must not send Customer Experience reports to Microsoft.

**Rule ID:** `SV-228366r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>It is detrimental for applications to provide, or install by default, functionality exceeding requirements or mission objectives. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors. Applications are capable of providing a wide variety of functions and services. Some of the functions and services, provided by default, may not be necessary to support essential organizational operations (e.g., key missions, functions). Examples of non-essential capabilities include, but are not limited to, advertising software or browser plug-ins not related to requirements or providing a wide array of functionality not required for every mission but that cannot be disabled. Customer Experience reports in Exchange will result in outbound traffic that may be identified by an eavesdropper. For this reason, the Customer Experience reports must not be sent to Microsoft.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-OrganizationConfig | Select CustomerFeedbackEnabled If the value for "CustomerFeedbackEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000119

**Group ID:** `V-228367`

### Rule: Exchange must protect audit data against unauthorized access.

**Rule ID:** `SV-228367r879577_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted "Read" and "Write" access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the authorized groups or users that should have access to the audit data. If any group or user has modify privileges for the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000120

**Group ID:** `V-228368`

### Rule: Exchange must protect audit data against unauthorized deletion.

**Rule ID:** `SV-228368r879578_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Audit data available for modification by a malicious user can be altered to conceal malicious activity. Audit data might also provide a means for the malicious user to plan unauthorized activities that exploit weaknesses. The contents of audit logs are protected against unauthorized access, modification, or deletion. Only authorized auditors and the audit functions should be granted "Read" and "Write" access to audit log data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the authorized groups or users that should have "Delete" permissions for the audit data. If any group or user has "Delete" permissions for the audit data that is not documented in the EDSP, this is a finding.

## Group: SRG-APP-000125

**Group ID:** `V-228369`

### Rule: Exchange Audit data must be on separate partitions.

**Rule ID:** `SV-228369r879582_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log files help establish a history of activities and can be useful in detecting attack attempts or determining tuning adjustments to improve availability. Audit log content must always be considered sensitive and in need of protection. Successful exploit of an application server vulnerability may well be logged by monitoring or audit processes when it occurs. Writing log and audit data to a separate partition where separate security contexts protect them may offer the ability to protect this information from being modified or removed by the exploit mechanism.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the audit logs' assigned partition. By default, the logs are located on the application partition in \Program Files\Microsoft\Exchange Server\V15\Logging. If the log files are not on a separate partition from the application, this is a finding.

## Group: SRG-APP-000131

**Group ID:** `V-228370`

### Rule: Exchange Local machine policy must require signed scripts.

**Rule ID:** `SV-228370r879584_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Scripts often provide a way for attackers to infiltrate a system, especially scripts downloaded from untrusted locations. By setting machine policy to prevent unauthorized script executions, unanticipated system impacts can be avoided. Failure to allow only signed remote scripts reduces the attack vector vulnerabilities from unsigned remote scripts.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ExecutionPolicy If the value returned is not "RemoteSigned", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-228371`

### Rule: The Exchange Internet Message Access Protocol 4 (IMAP4) service must be disabled.

**Rule ID:** `SV-228371r944805_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>IMAP4 is not approved for use within the DoD. It uses a clear-text-based user name and password and does not support the DoD standard for PKI for email access. User name and password could easily be captured from the network, allowing a malicious user to access other system features. Uninstalling or disabling the service will prevent the use of the IMAP4 protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to IMAP4. IMAP Secure is not restricted and does not apply to this requirement. Open the Windows Power Shell and enter the following command: Get-ItemProperty 'hklm:\system\currentcontrolset\services\MSExchangeIMAP4' | Select Start Note: The hklm:\system\currentcontrolset\services\MSExchangeIMAP4 value must be in single quotes. If the value of "Start" is not set to "4", this is a finding.

## Group: SRG-APP-000141

**Group ID:** `V-228372`

### Rule: The Exchange Post Office Protocol 3 (POP3) service must be disabled.

**Rule ID:** `SV-228372r879587_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>POP3 is not approved for use within the DoD. It uses a clear-text-based user name and password and does not support the DoD standard for PKI for email access. User name and password could easily be captured from the network, allowing a malicious user to access other system features. Uninstalling or disabling the service will prevent the use of POP3.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Windows Power Shell and enter the following command: Get-ItemProperty 'hklm:\system\currentcontrolset\services\MSExchangePOP3' | Select Start Note: The hklm:\system\currentcontrolset\services\MSExchangePOP3 value must be in single quotes. If the value of "Start" is not set to "4", this is a finding.

## Group: SRG-APP-000211

**Group ID:** `V-228373`

### Rule: Exchange Mailbox databases must reside on a dedicated partition.

**Rule ID:** `SV-228373r879631_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the same way that added security layers can provide a cumulative positive effect on security posture, multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to the host system can most likely lead to a compromise of all applications hosted by the same system. Email services should be installed to a discrete set of directories on a partition that does not host other applications. Email services should never be installed on a Domain Controller/Directory Services server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the location where the Exchange Mailbox databases reside. Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase | Select Name, Identity, EdbFilePath Open Windows Explorer, navigate to the mailbox databases, and verify they are on a dedicated partition. If the mailbox databases are not on a dedicated partition, this is a finding.

## Group: SRG-APP-000213

**Group ID:** `V-228374`

### Rule: Exchange Internet-facing Send connectors must specify a Smart Host.

**Rule ID:** `SV-228374r879633_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>When identifying a "Smart Host" for the email environment, a logical Send connector is the preferred method. A Smart Host acts as an Internet-facing concentrator for other email servers. Appropriate hardening can be applied to the Smart Host, rather than at multiple locations throughout the enterprise. Failure to identify a Smart Host could default to each email server performing its own lookups (potentially through protective firewalls). Exchange servers should not be Internet facing and should therefore not perform any Smart Host functions. When the Exchange servers are Internet facing, they must be configured to identify the Internet-facing server that is performing the Smart Host function.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select Name, Identity, SmartHosts Identify the Internet-facing connectors. For each Send connector, if the value of "SmartHosts" does not return the Smart Host IP address, this is a finding.

## Group: SRG-APP-000219

**Group ID:** `V-228375`

### Rule: Exchange internal Receive connectors must require encryption.

**Rule ID:** `SV-228375r879636_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) Receive connector is used by Exchange to send and receive messages from server to server using SMTP protocol. This setting controls the encryption strength used for client connections to the SMTP Receive connector. With this feature enabled, only clients capable of supporting secure communications will be able to send mail using this SMTP server. Where secure channels are required, encryption can also be selected. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from the client to the server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption have been compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between the client and server. Multiple values can be separated by commas, but some values have dependencies and exclusions. AuthMechanism may include other mechanisms as long as the "Tls" is identified. • Only use the value "None" by itself. • The value "BasicAuthRequireTLS" requires the values "BasicAuth" and "Tls". • The only other value that can be used with ExternalAuthoritative is "Tls". • The value "Tls" is required when the value of the RequireTLS parameter is "$true". • The value "ExternalAuthoritative" requires the value of the PermissionGroups parameter be set to "ExchangeServers". </VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: AuthMechanism may include other mechanisms as long as the "Tls" is identified. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, AuthMechanism For each Receive connector, if the value of "AuthMechanism" is not set to "Tls", this is a finding.

## Group: SRG-APP-000231

**Group ID:** `V-228376`

### Rule: Exchange Mailboxes must be retained until backups are complete.

**Rule ID:** `SV-228376r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Backup and recovery procedures are an important part of overall system availability and integrity. Complete backups reduce the chance of accidental deletion of important information and make it possible to have complete recoveries. It is not uncommon for users to receive and delete messages in the scope of a single backup cycle. This setting ensures at least one backup has been run on the mailbox store before the message physically disappears. By enabling this setting, all messages written to recipients who have accounts on this store will reside in backups even if they have been deleted by the user before the backup has run.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase| Select Name, Identity, RetainDeletedItemsUntilBackup If the value of "RetainDeletedItemsUntilBackup" is not set to "True", this is a finding.

## Group: SRG-APP-000231

**Group ID:** `V-228377`

### Rule: Exchange email forwarding must be restricted.

**Rule ID:** `SV-228377r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auto-forwarded email accounts do not meet the requirement for digital signature and encryption of Controlled Unclassified Information (CUI) and Personally Identifiable Information (PII) in accordance with DoDI 8520.2 (reference ee) and DoD Director for Administration and Management memorandum, "Safeguarding Against and Responding to the Breach of Personally Identifiable Information". Use of forwarding set by an administrator interferes with nonrepudiation requirements that each end user be responsible for creation and destination of email data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine any accounts that have been authorized to have email auto-forwarded. Note: If email auto-forwarding is not being used, this check is not applicable. . Open the Exchange Management Shell and enter the following commands: Get-Mailbox | Select Name, Identity, Filter If any user has a forwarding SMTP address and is not documented in the EDSP, this is a finding. Note: If no remote SMTP domain matching the mail-enabled user or contact that allows forwarding is configured for users identified with a forwarding address, this function will not work properly.

## Group: SRG-APP-000231

**Group ID:** `V-228378`

### Rule: Exchange email-forwarding SMTP domains must be restricted.

**Rule ID:** `SV-228378r879642_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Auto-forwarded email accounts do not meet the requirement for digital signature and encryption of Controlled Unclassified Information (CUI) and Personally Identifiable Information (PII) in accordance with DoDI 8520.2 (reference ee) and DoD Director for Administration and Management memorandum, "Safeguarding Against and Responding to the Breach of Personally Identifiable Information". Use of forwarding set by an administrator interferes with nonrepudiation requirements that each end user be responsible for creation and destination of email data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine any accounts that have been authorized to have email auto-forwarded. Note: If email auto-forwarding is not being used, this check is not applicable (NA). Open the Exchange Management Shell and enter the following commands: Get-RemoteDomain | Select Name, Identity, DomainName, AutoForwardEnabled If any domain for a user forwarding SMTP address is not documented in the EDSP, this is a finding. Note: If no remote SMTP domain matching the mail-enabled user or contact that allows forwarding is configured for users identified with a forwarding address, this function will not work properly.

## Group: SRG-APP-000246

**Group ID:** `V-228379`

### Rule: Exchange Mail quota settings must not restrict receiving mail.

**Rule ID:** `SV-228379r879650_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Mail quota settings control the maximum sizes of a user’s mailbox and the system’s response if these limits are exceeded. Mailbox data that is not monitored against a quota increases the risk of mail loss due to filled disk space, which can also render the system unavailable. Failure to allow mail receipt may impede users from receiving mission-critical data.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase | Select Name, Identity, ProhibitSendReceiveQuota If the value of "ProhibitSendReceiveQuota" is not set to "Unlimited", this is a finding. or If the value of "ProhibitSendReceiveQuota" is set to an alternate value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000246

**Group ID:** `V-228380`

### Rule: Exchange Mail Quota settings must not restrict receiving mail.

**Rule ID:** `SV-228380r879650_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Mail quota settings control the maximum sizes of a user’s mailbox and the system’s response if these limits are exceeded. Mailbox data that is not monitored against a quota increases the risk of mail loss due to filled disk space, which can also render the system unavailable. Multiple controls supply graduated levels of opportunity to respond before risking email service loss. This control prohibits the user from sending an email when the mailbox limit reaches the prohibit send quota value. Note: Best practice for this setting is to prohibit the user from sending email when the mailbox reaches 90 percent of capacity.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the value for the Prohibit Send Quota limit. Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase | Select Name, Identity, ProhibitSendQuota If the value of "ProhibitSendQuota" is not set to the site's Prohibit Send Quota limit, this is a finding.

## Group: SRG-APP-000246

**Group ID:** `V-228381`

### Rule: Exchange Mailbox Stores must mount at startup.

**Rule ID:** `SV-228381r879650_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Administrator responsibilities include the ability to react to unplanned maintenance tasks or emergency situations that may require Mailbox data manipulation. Occasionally, there may be a need to start the server with "unmounted" data stores if manual maintenance is being performed on them. Failure to uncheck the "do not mount on startup" condition will result in unavailability of mail services. Correct configuration of this control will prevent unplanned outages due to being enabled. When maintenance is being performed, care should be taken to clear the check box upon task completion so mail stores are available to users (unmounted mailbox stores are not available to users).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-MailboxDatabase | Select Name, Identity, MountAtStartup If the value of "MountAtStartup" is not set to "True", this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228382`

### Rule: Exchange Message size restrictions must be controlled on Receive connectors.

**Rule ID:** `SV-228382r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. For message size restrictions, multiple places exist to set or override inbound or outbound message size. Failure to control the configuration strategy can result in loss of data or system availability. This setting enables the administrator to control the maximum message size on receive connectors. Using connectors to control size limits may necessitate applying message size limitations in multiple places, with the potential of introducing conflicts and impediments in the mail flow. Changing this setting at the connector overrides the global one. Therefore, if operational needs require it, the connector value may be set lower than the global value with the rationale documented in the Email Domain Security Plan (EDSP).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the EDSP or document that contains this information. Determine the global maximum message receive size and whether signoff with risk acceptance is documented for the Receive connector to have a different value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, MaxMessageSize Identify Internet-facing connectors. For each Receive connector, if the value of "MaxMessageSize" is not the same as the global value, this is a finding. or If "MaxMessageSize" is set to a numeric value different from the global value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228383`

### Rule: Exchange Receive connectors must control the number of recipients per message.

**Rule ID:** `SV-228383r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the maximum number of recipients who will receive a copy of a message at one time. This tunable value is related to throughput capacity and can enable the ability to optimize message delivery. Note: There are two types of default Receive connecters: Client Servername: Accepts SMTP connections from all non-MAPI clients, such as POP and IMAP. As POP and IMAP are not authorized for use in DoD, these should not be present. Their default value for "MaxRecipientsPerMessage" is "200". Default Servername: Accepts connections from other Hub Transport servers and any Edge Transport servers. Their default value for "MaxRecipientsPerMessage" is "5000".</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: This requirement applies to IMAP4. IMAP Secure is not restricted and does not apply to this requirement. Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the Maximum Recipients per Message value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, MaxRecipientsPerMessage For each Receive connector, evaluate the "MaxRecipientsPerMessage" value. For each Receive connector, if the value of "MaxRecipientsPerMessage" is not set to "5000", this is a finding. or If the value of "MaxRecipientsPerMessage" is set to a value other than "5000" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228384`

### Rule: The Exchange Receive Connector Maximum Hop Count must be 60.

**Rule ID:** `SV-228384r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This setting controls the maximum number of hops (email servers traversed) a message may take as it travels to its destination. Part of the original Internet protocol implementation, the hop count limit prevents a message being passed in a routing loop indefinitely. Messages exceeding the maximum hop count are discarded undelivered. Recent studies indicate that virtually all messages can be delivered in fewer than 60 hops. If the hop count is set too low, messages may expire before they reach their destinations. If the hop count is set too high, an undeliverable message may cycle between servers, raising the risk of network congestion.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the Max Hop Count value for Receive connectors. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, MaxHopCount For each Receive connector, if the value of "MaxHopCount" is not set to "60", this is a finding. or If the value of "MaxHopCount" is set to a value other than "60" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228385`

### Rule: Exchange Message size restrictions must be controlled on Send connectors.

**Rule ID:** `SV-228385r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. For message size restrictions, multiple places exist to set or override inbound or outbound message size. Failure to control the configuration strategy can result in loss of data or system availability. This setting enables the administrator to control the maximum message size on a Send connector. Using connectors to control size limits may necessitate applying message size limitations in multiple places, with the potential of introducing conflicts and impediments in the mail flow. Changing this setting at the connector overrides the global one. Therefore, if operational needs require it, the connector value may be set lower than the global value with the rationale documented in the Email Domain Security Plan (EDSP).</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the maximum message send size. Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select Name, Identity, MaxMessageSize For each Send connector, if the value of "MaxMessageSize" is not the same as the global value, this is a finding. or If "MaxMessageSize" is set to a numeric value different from the maximum message send size value documented in the EDSP, this is a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228386`

### Rule: The Exchange Send connector connections count must be limited.

**Rule ID:** `SV-228386r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The Exchange Send connector setting controls the maximum number of simultaneous outbound connections allowed for a given SMTP connector and can be used to throttle the SMTP service if resource constraints warrant it. If the limit is too low, connections may be dropped. If the limit is too high, some domains may use a disproportionate resource share, denying access to other domains. Appropriate tuning reduces risk of data delay or loss.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the value for SMTP Server Maximum Outbound Connections. Open the Exchange Management Shell and enter the following command: Get-TransportService | Select Name, Identity, MaxOutboundConnections If the value of "MaxOutboundConnections" is not set to "1000", this is a finding. or If "MaxOutboundConnections" is set to a value other than "1000" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228387`

### Rule: The Exchange global inbound message size must be controlled.

**Rule ID:** `SV-228387r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. Message size limits should be set to 10 megabytes (MB) at most but often are smaller, depending on the organization. The key point in message size is that it should be set globally and should not be set to "unlimited". Selecting "unlimited" on "MaxReceiveSize" is likely to result in abuse and can contribute to excessive server disk space consumption. Message size limits may also be applied on SMTP connectors, Public Folders, and on the user account under Active Directory (AD). Changes at these lower levels are discouraged, as the single global setting is usually sufficient. This practice prevents conflicts that could impact availability and simplifies server administration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the global maximum message receive size. Open the Exchange Management Shell and enter the following command: Get-TransportConfig | Select Name, Identity, MaxReceiveSize If the value of "MaxReceiveSize" is not set to "10MB", this is a finding. or If "MaxReceiveSize" is set to an alternate value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228388`

### Rule: The Exchange global outbound message size must be controlled.

**Rule ID:** `SV-228388r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. Message size limits should be set to 10 megabytes (MB) at most but often are smaller, depending on the organization. The key point in message size is that it should be set globally and should not be set to "unlimited". Selecting "unlimited" on "MaxReceiveSize" is likely to result in abuse and can contribute to excessive server disk space consumption. Message size limits may also be applied on send and receive connectors, Public Folders, and on the user account under Active Directory (AD). Changes at these lower levels are discouraged, as the single global setting is usually sufficient. This practice prevents conflicts that could impact availability and simplifies server administration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the global maximum message send size. Open the Exchange Management Shell and enter the following command: Get-TransportConfig | Select Name, Identity, MaxSendSize If the value of "MaxSendSize" is not set to "10MB", this is a finding. or If "MaxSendSize" is set to an alternate value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228389`

### Rule: The Exchange Outbound Connection Limit per Domain Count must be controlled.

**Rule ID:** `SV-228389r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the maximum number of simultaneous outbound connections from a domain as a delivery tuning mechanism. If the limit is too low, connections may be dropped. If the limit is too high, some domains may use a disproportionate resource share, denying access to other domains. Appropriate tuning reduces risk of data delay or loss. By default, a limit of 20 simultaneous outbound connections from a domain should be sufficient. The value may be adjusted if justified by local site conditions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the value for Maximum Outbound Domain Connections. Open the Exchange Management Shell and enter the following command: Get-TransportService | Select Name, Identity, MaxPerDomainOutboundConnections If the value of "MaxPerDomainOutboundConnections" is not set to "20", this is a finding. or If "MaxPerDomainOutboundConnections" is set to a value other than "20" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000247

**Group ID:** `V-228390`

### Rule: The Exchange Outbound Connection Timeout must be 10 minutes or less.

**Rule ID:** `SV-228390r879651_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. This configuration controls the number of idle minutes before the connection is dropped. It works in conjunction with the Maximum Outbound Connections Count setting. Connections, once established, may incur delays in message transfer. The default of 10 minutes is a reasonable window in which to resume activities without maintaining idle connections for excessive intervals. If the timeout period is too long, idle connections may be maintained for unnecessarily long time periods, preventing new connections from being established. Sluggish connectivity increases the risk of lost data. A value of "10" or less is optimal.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the Connection Timeout value. Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select Name, Identity, ConnectionInactivityTimeOut For each Send connector, if the value of "ConnectionInactivityTimeOut" is not set to "00:10:00", this is a finding. or If "ConnectionInactivityTimeOut" is set to a value other than "00:10:00" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228391`

### Rule: Exchange Internal Receive connectors must not allow anonymous connections.

**Rule ID:** `SV-228391r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This control is used to limit the servers that may use this server as a relay. If a Simple Mail Transport Protocol (SMTP) sender does not have a direct connection to the Internet (for example, an application that produces reports to be emailed), it will need to use an SMTP Receive connector that does have a path to the Internet (for example, a local email server) as a relay. SMTP relay functions must be protected so third parties are not able to hijack a relay service for their own purposes. Most commonly, hijacking of relays is done by spammers to disguise the source of their messages and may also be used to cover the source of more destructive attacks. Relays can be restricted in one of three ways: by blocking relays (restrict to a blank list of servers), by restricting use to lists of valid servers, or by restricting use to servers that can authenticate. Because authenticated connections are the most secure for SMTP Receive connectors, it is recommended that relays allow only servers that can authenticate.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: In some instances, AnonymousUsers may be necessary for organization-specific operations. In such cases, allowing AnonymousUsers must be paired with restricting to specific lists of servers allowed to access. In addition, the risk must be documented and accepted by the ISSO, ISSM, or AO. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, PermissionGroups For each Receive connector, if the value of "PermissionGroups" is "AnonymousUsers" for any receive connector, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228392`

### Rule: Exchange external/Internet-bound automated response messages must be disabled.

**Rule ID:** `SV-228392r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Spam originators, in an effort to refine mailing lists, sometimes monitor transmissions for automated bounce-back messages. Automated messages include such items as "Out of Office" responses, nondelivery messages, and automated message forwarding. Automated bounce-back messages can be used by a third party to determine if users exist on the server. This can result in the disclosure of active user accounts to third parties, paving the way for possible future attacks.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-RemoteDomain | Select Name, DomainName, Identity, AllowedOOFType If the value of "AllowedOOFType" is not set to "InternalLegacy", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228393`

### Rule: Exchange must have anti-spam filtering installed.

**Rule ID:** `SV-228393r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques in order to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. A manual update procedure is labor intensive and does not scale well in an enterprise environment. This risk may be mitigated by using an automatic update capability. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2016 provides both anti-spam and anti-malware protection out of the box. The Exchange 2016 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Note: If using another DoD-approved antispam product for email or a DoD-approved email gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable (NA). Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Format-Table Name,Enabled If no value is returned, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228394`

### Rule: Exchange must have anti-spam filtering enabled.

**Rule ID:** `SV-228394r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques in order to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. A manual update procedure is labor intensive and does not scale well in an enterprise environment. This risk may be mitigated by using an automatic update capability. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2016 provides both anti-spam and anti-malware protection out of the box. The Exchange 2016 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Note: If using another DoD-approved anti-spam product for email or a DoD-approved email gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable (NA). Open the Exchange Management Shell and enter the following command: Get-ContentFilterConfig | Format-Table Name,Enabled; Get-SenderFilterConfig | Format-Table Name,Enabled; Get-SenderIDConfig | Format-Table Name,Enabled; Get-SenderReputationConfig | Format-Table Name,Enabled If any of the following values returned are not set to "True", this is a finding: Set-ContentFilterConfig Set-SenderFilterConfig Set-SenderIDConfig Set-SenderReputationConfig

## Group: SRG-APP-000261

**Group ID:** `V-228395`

### Rule: Exchange must have anti-spam filtering configured.

**Rule ID:** `SV-228395r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Originators of spam messages are constantly changing their techniques in order to defeat spam countermeasures; therefore, spam software must be constantly updated to address the changing threat. A manual update procedure is labor intensive and does not scale well in an enterprise environment. This risk may be mitigated by using an automatic update capability. Spam protection mechanisms include, for example, signature definitions, rule sets, and algorithms. Exchange 2016 provides both anti-spam and anti-malware protection out of the box. The Exchange 2016 anti-spam and anti-malware product capabilities are limited but still provide some protection.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Note: If using another DoD-approved antispam product for email or a DoD-approved email gateway spamming device, such as Enterprise Email Security Gateway (EEMSG), this is not applicable (NA). Determine the internal SMTP servers. Open the Exchange Management Shell and enter the following command: Get-TransportConfig | Format-List InternalSMTPServers If any internal SMTP server IP address returned does not reflect the list of accepted SMTP server IP addresses, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228396`

### Rule: Exchange must not send automated replies to remote domains.

**Rule ID:** `SV-228396r879653_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers can use automated messages to determine whether a user account is active, in the office, traveling, and so on. An attacker might use this information to conduct future attacks. Remote users will not receive automated "Out of Office" delivery reports. This setting can be used to determine if all the servers in the organization can send "Out of Office" messages.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Note: Automated replies to .MIL or .GOV sites are allowed. Open the Exchange Management Shell and enter the following command: Get-RemoteDomain | Select Name, Identity, AutoReplyEnabled If the value of “AutoReplyEnabled” is set to “True” and is configured to only Reply to .MIL or .GOV sites, this is not a finding. If the value of "AutoReplyEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228397`

### Rule: Exchange servers must have an approved DoD email-aware virus protection software installed.

**Rule ID:** `SV-228397r879653_rule`
**Severity:** high

**Description:**
<VulnDiscussion>With the proliferation of trojans, viruses, and spam attaching themselves to email messages (or attachments), it is necessary to have capable email-aware anti-virus (AV) products to scan messages and identify any resident malware. Because email messages and their attachments are formatted to the MIME standard, a flat-file AV scanning engine is not suitable for scanning email message stores. Email-aware anti-virus engines must be Exchange 2016 compliant. Competent email scanners will have the ability to scan mail stores, attachments (including zip or other archive files) and mail queues and to issue warnings or alerts if malware is detected. As with other AV products, a necessary feature to include is the ability for automatic updates.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the anti-virus strategy. Verify the email-aware anti-virus scanner product is Exchange 2016 compatible and DoD approved. If email servers are using an email-aware anti-virus scanner product that is not DoD approved and Exchange 2016 compatible, this is a finding.

## Group: SRG-APP-000261

**Group ID:** `V-228398`

### Rule: The Exchange Global Recipient Count Limit must be set.

**Rule ID:** `SV-228398r879653_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning configurations. The Global Recipient Count Limit field is used to control the maximum number of recipients that can be specified in a single message sent from this server. Its primary purpose is to minimize the chance of an internal sender spamming other recipients, since spam messages often have a large number of recipients. Spam prevention can originate from both outside and inside organizations. While inbound spam is evaluated as it arrives, controls such as this one help prevent spam that might originate inside the organization. The Recipient Count Limit is global to the Exchange implementation. Lower-level refinements are possible; however, in this configuration strategy, setting the value once at the global level facilitates a more available system by eliminating potential conflicts among multiple settings. A value of less than or equal to "5000" is probably larger than is needed for most organizations but is small enough to minimize usefulness to spammers and is easily handled by Exchange. An unexpanded distribution is handled as one recipient. Specifying "unlimited" may result in abuse.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the global maximum message recipient count. Open the Exchange Management Shell and enter the following command: Get-TransportConfig | Select Name, Identity, MaxRecipientEnvelopeLimit If the value of "MaxRecipientEnvelopeLimit" is not set to "5000", this is a finding. or If "MaxRecipientEnvelopeLimit" is set to an alternate value and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000295

**Group ID:** `V-228399`

### Rule: The Exchange Receive connector timeout must be limited.

**Rule ID:** `SV-228399r879673_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Email system availability depends in part on best practice strategies for setting tuning. This configuration controls the number of idle minutes before the connection is dropped. It works in conjunction with the Maximum Inbound Connections Count setting. Connections, once established, may incur delays in message transfer. If the timeout period is too long, there is risk that idle connections may be maintained for unnecessarily long time periods, preventing new connections from being established.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine the Connection Timeout value. Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, ConnectionTimeout For each Receive connector, if the value of "ConnectionTimeout" is not set to "00:10:00", this is a finding. or If "ConnectionTimeout" is set to other than "00:10:00" and has signoff and risk acceptance in the EDSP, this is not a finding.

## Group: SRG-APP-000378

**Group ID:** `V-228400`

### Rule: The Exchange application directory must be protected from unauthorized access.

**Rule ID:** `SV-228400r879751_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Default product installations may provide more generous access permissions than are necessary to run the application. By examining and tailoring access permissions to more closely provide the least amount of privilege possible, attack vectors that align with user permissions are less likely to access more highly secured areas.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the authorized groups and users that have access to the Exchange application directories. Verify the access permissions on the directory match the access permissions listed in the EDSP. If any group or user has different access permissions, this is a finding. Note: The default installation directory is \Program Files\Microsoft\Exchange Server\V15.

## Group: SRG-APP-000380

**Group ID:** `V-228401`

### Rule: An Exchange software baseline copy must exist.

**Rule ID:** `SV-228401r879753_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange software, as with other application software installed on a host system, must be included in a system baseline record and periodically reviewed; otherwise, unauthorized changes to the software may not be discovered. This effort is a vital step to securing the host and the applications, as it is the only method that may provide the ability to detect and recover from otherwise undetected changes, such as those that result from worm or bot intrusions. The Exchange software and configuration baseline is created and maintained for comparison during scanning efforts. Operational procedures must include baseline updates as part of configuration management tasks that change the software and configuration.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP) or document that contains this information. Determine the software baseline. Review the application software baseline procedures and implementation artifacts. Note the list of files and directories included in the baseline procedure for completeness. If an email software copy exists to serve as a baseline and is available for comparison during scanning efforts, this is not a finding.

## Group: SRG-APP-000381

**Group ID:** `V-228402`

### Rule: Exchange software must be monitored for unauthorized changes.

**Rule ID:** `SV-228402r928977_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Monitoring software files for changes against a baseline on a regular basis may help detect the possible introduction of malicious code on a system.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine whether the site monitors system files (e.g., *.exe, *.bat, *.com, *.cmd, and *.dll) on servers for unauthorized changes against a baseline on a weekly basis. If software files are not monitored for unauthorized changes, this is a finding.

## Group: SRG-APP-000383

**Group ID:** `V-228403`

### Rule: Exchange services must be documented and unnecessary services must be removed or disabled.

**Rule ID:** `SV-228403r879756_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Unneeded but running services offer attackers an enhanced attack profile, and attackers are constantly watching to discover open ports with running services. By analyzing and disabling unneeded services, the associated open ports become unresponsive to outside queries, and servers become more secure as a result. Exchange Server has role-based server deployment to enable protocol path control and logical separation of network traffic types. For example, a server implemented in the Client Access role (i.e., Outlook Web App [OWA]) is configured and tuned as a web server using web protocols. A client access server exposes only web protocols (HTTP/HTTPS), enabling system administrators to optimize the protocol path and disable all services unnecessary for Exchange web services. Similarly, servers created to host mailboxes are dedicated to that task and must operate only the services needed for mailbox hosting. (Exchange servers must also operate some web services, but only to the degree that Exchange requires the IIS engine in order to function). Because Post Office Protocol 3 (POP3) and Internet Message Access Protocol 4 (IMAP4) clients are not included in the standard desktop offering, they must be disabled. While IMAP4 is restricted, IMAP Secure is not restricted and does not apply to this requirement.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Note: Required services will vary among organizations and will vary depending on the role of the individual system. Organizations will develop their own list of services, which will be documented and justified with the Information System Security Officer (ISSO). The site’s list will be provided for any security review. Services that are common to multiple systems can be addressed in one document. Exceptions for individual systems should be identified separately by system. Open a Windows PowerShell and enter the following command: Get-Service | Where-Object {$_.status -eq 'running'} Note: The command returns a list of installed services and the status of that service. If the services required are not documented in the EDSP, this is a finding. If any undocumented or unnecessary services are running, this is a finding.

## Group: SRG-APP-000391

**Group ID:** `V-228404`

### Rule: Exchange Outlook Anywhere clients must use NTLM authentication to access email.

**Rule ID:** `SV-228404r879764_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Identification and authentication provide the foundation for access control. Access to email services applications require NTLM authentication. Outlook Anywhere, if authorized for use by the site, must use NTLM authentication when accessing email. Note: There is a technical restriction in Exchange Outlook Anywhere that requires a direct SSL connection from Outlook to the Certificate Authority (CA) server. There is also a constraint where Microsoft supports that the CA server must participate in the Active Director (AD) domain inside the enclave. For this reason, Outlook Anywhere must be deployed only for enclave-sourced Outlook users.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-OutlookAnywhere Get-OutlookAnywhere | Select Name, Identity, InternalClientAuthenticationMethod, ExternalClientAuthenticationMethod If the value of "InternalClientAuthenticationMethod" and the value of "ExternalClientAuthenticationMethod" are not set to NTLM, this is a finding.

## Group: SRG-APP-000431

**Group ID:** `V-228405`

### Rule: The Exchange Email application must not share a partition with another application.

**Rule ID:** `SV-228405r879802_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In the same way that added security layers can provide a cumulative positive effect on security posture, multiple applications can provide a cumulative negative effect. A vulnerability and subsequent exploit to one application can lead to an exploit of other applications sharing the same security context. For example, an exploit to a web server process that leads to unauthorized administrative access to the host system can most likely lead to a compromise of all applications hosted by the same system. Email services should be installed on a partition that does not host other applications. Email services should never be installed on a Domain Controller/Directory Services server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine if the directory Exchange is installed. Open Windows Explorer. Navigate to where Exchange is installed. If Exchange resides on a directory or partition other than that of the operating system and does not have other applications installed (unless approved by the Information System Security Officer [ISSO]), this is not a finding.

## Group: SRG-APP-000435

**Group ID:** `V-228406`

### Rule: Exchange must not send delivery reports to remote domains.

**Rule ID:** `SV-228406r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers can use automated messages to determine whether a user account is active, in the office, traveling, and so on. An attacker might use this information to conduct future attacks. Ensure that delivery reports to remote domains are disabled. Before enabling this setting, first configure a remote domain using the Exchange Management Console (EMC) or the New-RemoteDomain cmdlet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-RemoteDomain | Select Identity, DeliveryReportEnabled If the value of "DeliveryReportEnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-228407`

### Rule: Exchange must not send nondelivery reports to remote domains.

**Rule ID:** `SV-228407r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Attackers can use automated messages to determine whether a user account is active, in the office, traveling, and so on. An attacker might use this information to conduct future attacks. Ensure that nondelivery reports to remote domains are disabled. Before enabling this setting, first configure a remote domain using the Exchange Management Console (EMC) or the New-RemoteDomain cmdlet.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
NOTE: For the purpose of this requirement, “remote” refers to those domains external to the DoDIN, whether classified or unclassified. NDRs between DoDIN networks is permitted. Open the Exchange Management Shell and enter the following command: Get-RemoteDomain | Select Name, Identity, NDREnabled If the value of "NDREnabled" is not set to "False", this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-228408`

### Rule: The Exchange SMTP automated banner response must not reveal server details.

**Rule ID:** `SV-228408r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automated connection responses occur as a result of FTP or Telnet connections when connecting to those services. They report a successful connection by greeting the connecting client and stating the name, release level, and (often) additional information regarding the responding product. While useful to the connecting client, connection responses can also be used by a third party to determine operating system or product release levels on the target server. The result can include disclosure of configuration information to third parties, paving the way for possible future attacks. For example, when querying the SMTP service on port 25, the default response looks similar to this one: 220 exchange.mydomain.org Microsoft ESMTP MAIL Service, Version: 6.0.3790.211 ready at Wed, 2 Feb 2005 23:40:00 -0500 Changing the response to hide local configuration details reduces the attack profile of the target.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-ReceiveConnector | Select Name, Identity, Banner For each Receive connector, if the value of "Banner" is not set to "220 SMTP Server Ready", this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-228409`

### Rule: Exchange Internal Send connectors must use an authentication level.

**Rule ID:** `SV-228409r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>The Simple Mail Transfer Protocol (SMTP) connector is used by Exchange to send and receive messages from server to server. Several controls work together to provide security between internal servers. This setting controls the encryption method used for communications between servers. With this feature enabled, only servers capable of supporting Transport Layer Security (TLS) will be able to send and receive mail within the domain. The use of secure communication prevents eavesdroppers from reading or modifying communications between mail clients and servers. While sensitive message bodies should be encrypted by the sender at the client, requiring a secure connection from server to server adds protection by encrypting the sender and recipient information that cannot be encrypted by the sender. Individually, channel security and encryption can be compromised by attackers. Used together, email becomes a more difficult target, and security is heightened. Failure to enable this feature gives eavesdroppers an opportunity to read or modify messages between servers.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-SendConnector | Select Name, Identity, TlsAuthLevel For each Send connector, if the value of "TlsAuthLevel" is not set to "DomainValidation", this is a finding.

## Group: SRG-APP-000435

**Group ID:** `V-228410`

### Rule: Exchange must provide Mailbox databases in a highly available and redundant configuration.

**Rule ID:** `SV-228410r879806_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Exchange Server mailbox databases and any data contained in those mailboxes should be protected. This can be accomplished by configuring Mailbox servers and databases for high availability and site resilience. A database availability group (DAG) is a component of the Mailbox server high availability and site resilience framework built into Microsoft Exchange Server 2016. A DAG is a group of Mailbox servers that hosts a set of databases and provides automatic database-level recovery from failures that affect individual servers or databases. A DAG is a boundary for mailbox database replication and database and server switchovers and failovers. Any server in a DAG can host a copy of a mailbox database from any other server in the DAG. When a server is added to a DAG, it works with the other servers in the DAG to provide automatic recovery from failures that affect mailbox databases, such as a disk, server, or network failure.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the Email Domain Security Plan (EDSP). Determine if the Exchange Mailbox databases are using redundancy. Open the Exchange Management Shell. Enter the following command: Get-DatabaseAvailabilityGroup <DAGName> | Format-List If the DAG is not displayed, this is a finding.

## Group: SRG-APP-000456

**Group ID:** `V-228411`

### Rule: Exchange must have the most current, approved service pack installed.

**Rule ID:** `SV-228411r879827_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Failure to install the most current Exchange service pack leaves a system vulnerable to exploitation. Current service packs correct known security and system vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Determine the most current, approved service pack. Open the Exchange Management Shell and enter the following command: Get-ExchangeServer | fl Name, AdminDisplayVersion If the value of "AdminDisplayVersion" does not return the most current, approved service pack, this is a finding.

## Group: SRG-APP-000516

**Group ID:** `V-228412`

### Rule: The application must be configured in accordance with the security configuration settings based on DoD security configuration or implementation guidance, including STIGs, NSA configuration guides, CTOs, and DTMs.

**Rule ID:** `SV-228412r879887_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Configuring the application to implement organization-wide security implementation guides and security checklists ensures compliance with Federal standards and establishes a common security baseline across DoD that reflects the most restrictive security posture consistent with operational requirements. Configuration settings are the set of parameters that can be changed that affect the security posture and/or functionality of the system. Security-related parameters are those parameters impacting the security state of the application, including the parameters required to satisfy other security control requirements.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open a Windows PowerShell Module and enter the following commands:  Get-Website | Select Name Get-WebBinding -Name <'WebSiteName'> | Format-List If the Web binding values returned are not on standard port 80 for HTTP connections or port 443 for HTTPS connections, this is a finding. Note: This is excluding the Exchange Back End website which uses 81/444. Repeat the process for each website.

## Group: SRG-APP-000278

**Group ID:** `V-228413`

### Rule: The applications built-in Malware Agent must be disabled.

**Rule ID:** `SV-228413r879664_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Malicious code protection mechanisms include but are not limited to anti-virus and malware detection software. To minimize potential negative impact to the organization that can be caused by malicious code, it is imperative that malicious code is identified and eradicated. Malicious code includes viruses, worms, trojan horses, and spyware. It is not enough to have the software installed; this software must periodically scan the system to search for malware on an organization-defined frequency. Exchange's built-in Malware Agent is not designed to address all malicious code protection workloads. This workload is best handled by third-party anti-virus and intrusion prevention software. Sites must use an approved DoD scanner. Exchange Malware software has a limited scanning capability and does not scan files that are downloaded, opened, or executed.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-TransportAgent "Malware Agent" If the value of "Enabled" is set to "True", this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-228415`

### Rule: Exchange must use encryption for RPC client access.

**Rule ID:** `SV-228415r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls whether client machines are forced to use secure channels to communicate with the server. If this feature is enabled, clients will only be able to communicate with the server over secure communication channels. Failure to require secure connections to the client access server increases the potential for unintended eavesdropping or data loss.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-RpcClientAccess | Select Server, Name, EncryptionRequired If the value of "EncryptionRequired" is not set to "True", this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-228416`

### Rule: Exchange must use encryption for Outlook Web App (OWA) access.

**Rule ID:** `SV-228416r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>This setting controls whether client machines should be forced to use secure channels to communicate with this virtual directory. If this feature is enabled, clients will only be able to communicate with the directory if they are capable of supporting secure communication with the server. The use of secure communication prevents eavesdroppers from reading or modifying communications between servers and clients. The network and DMZ STIG identify criteria for OWA and Public Folder configuration in the network, including Common Access Card (CAC)-enabled pre-authentication through an application firewall proxy. Failure to require secure connections on a website increases the potential for unintended eavesdropping or data loss.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open a Exchange Management Shell and enter the following command: Get-OwaVirtualDirectory | select internalurl, externalurl If the value returned is not https://, this is a finding.

## Group: SRG-APP-000014

**Group ID:** `V-228417`

### Rule: Exchange must have forms-based authentication disabled.

**Rule ID:** `SV-228417r879519_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Identification and Authentication provide the foundation for access control. Access to email services applications in the DoD requires authentication using DoD Public Key Infrastructure (PKI) certificates. Authentication for Outlook Web App (OWA) is used to enable web access to user email mailboxes and should assume that certificate-based authentication has been configured. This setting controls whether forms-based logon should be used by the OWA website. Because the DoD requires Common Access Card (CAC)-based authentication to applications, OWA access must be brokered through an application proxy or other pre-authenticator, which performs CAC authentication prior to arrival at the CA server. The authenticated request is then forwarded directly to OWA, where authentication is repeated without requiring the user to repeat authentication steps. For this scenario to work, the Application Proxy server must have forms-based authentication enabled, and Exchange must have forms-based Authentication disabled. If forms-based Authentication is enabled on the Exchange CA server, it is evidence that the application proxy server is either not correctly configured, or it may be missing.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-OwaVirtualDirectory | Select ServerName, Name, Identity, FormsAuthentication If the value of "FormsAuthentication" is not set to "False", this is a finding.

## Group: SRG-APP-000033

**Group ID:** `V-228418`

### Rule: Exchange must have authenticated access set to Integrated Windows Authentication only.

**Rule ID:** `SV-228418r879530_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>To mitigate the risk of unauthorized access to sensitive information by entities that have been issued certificates by DoD-approved PKIs, all DoD systems (e.g., networks, web servers, and web portals) must be properly configured to incorporate access control methods that do not rely solely on the possession of a certificate for access. Successful authentication must not automatically give an entity access to an asset or security boundary. Authorization procedures and controls must be implemented to ensure each authenticated entity also has a validated and current authorization. Authorization is the process of determining whether an entity, once authenticated, is permitted to access a specific asset. Information systems use access control policies and enforcement mechanisms to implement this requirement. Access control policies include identity-based policies, role-based policies, and attribute-based policies. Access enforcement mechanisms include access control lists, access control matrices, and cryptography. These policies and mechanisms must be employed by the application to control access between users (or processes acting on behalf of users) and objects (e.g., devices, files, records, processes, programs, and domains) in the information system. This requirement is applicable to access control enforcement applications (e.g., authentication servers) and other applications that perform information and system access control functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Open the Exchange Management Shell and enter the following command: Get-OwaVirtualDirectory | Select ServerName, Name, Identity,*Authentication If the value of "WindowsAuthentication" is not set to "True", this is a finding.

