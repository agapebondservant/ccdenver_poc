# STIG Benchmark: Splunk Enterprise 8.x for Linux Security Technical Implementation Guide

---

**Version:** 2

**Description:**
This Security Technical Implementation Guide is published as a tool to improve the security of Department of Defense (DOD) information systems. The requirements are derived from the National Institute of Standards and Technology (NIST) 800-53 and related documents. Comments or proposed revisions to this document should be sent via email to the following address: disa.stig_spt@mail.mil.

## Group: SRG-APP-000295-AU-000190

**Group ID:** `V-251657`

### Rule: Splunk Enterprise idle session timeout must be set to not exceed 15 minutes.

**Rule ID:** `SV-251657r1043182_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Automatic session termination after a period of inactivity addresses the potential for a malicious actor to exploit the unattended session. Closing any unattended sessions reduces the attack surface to the application. Satisfies: SRG-APP-000295-AU-000190, SRG-APP-000389-AU-000180</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head, which may be a separate machine in a distributed environment. If the instance being reviewed is not used as a search head, this check in Not Applicable. Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the web.conf file. If the web.conf file does not exist, this is a finding. If the "tools.sessions.timeout" is missing or is configured to 16 or more, this is a finding.

## Group: SRG-APP-000291-AU-000200

**Group ID:** `V-251658`

### Rule: Splunk Enterprise must notify the system administrator (SA) and information system security officer (ISSO) when account events are received (creation, deletion, modification, or disabling).

**Rule ID:** `SV-251658r1015830_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Once an attacker establishes access to an application, the attacker often attempts to create a persistent method of re-establishing access. One way to accomplish this is for the attacker to simply create a new account. Sending notification of account creation events to the system administrator and ISSO is one method for mitigating this risk. To address access requirements, many application developers choose to integrate their applications with enterprise-level authentication/access/auditing mechanisms that meet or exceed access control policy requirements. Such integration allows the application developer to off-load those access control functions and focus on core application features and functionality. Satisfies: SRG-APP-000291-AU-000200, SRG-APP-000292-AU-000420, SRG-APP-000294-AU-000430, SRG-APP-000294-AU-000440</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a report exists to notify the SA and ISSO when account events are received for all devices and hosts within its scope of coverage. Interview the ISSO to confirm receipt of this report. If Splunk Enterprise is not configured to notify the SA and ISSO when account events are received for all devices and hosts within its scope of coverage, this is a finding.

## Group: SRG-APP-000065-AU-000240

**Group ID:** `V-251659`

### Rule: Splunk Enterprise must enforce the limit of three consecutive invalid logon attempts by a user during a 15-minute time period.

**Rule ID:** `SV-251659r960840_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is applicable to the instance with the Search Head role, which may be a different instance in a distributed environment. Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "lockoutAttempts" is missing or is configured to more than 3, this is a finding. If the "lockoutThresholdMins" is missing or is configured to less than 15, this is a finding.

## Group: SRG-APP-000345-AU-000400

**Group ID:** `V-251660`

### Rule: Splunk Enterprise must automatically lock the account until the locked account is released by an administrator when three unsuccessful login attempts in 15 minutes are exceeded.

**Rule ID:** `SV-251660r961368_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>By limiting the number of failed login attempts, the risk of unauthorized system access via user password guessing, otherwise known as brute forcing, is reduced. Limits are imposed by locking the account.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the lockoutUsers" is missing or is configured to 0 or False, this is a finding.

## Group: SRG-APP-000068-AU-000035

**Group ID:** `V-251661`

### Rule: Splunk Enterprise must display the Standard Mandatory DOD Notice and Consent Banner before granting access to the server.

**Rule ID:** `SV-251661r960843_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Display of the DOD-approved use notification before granting access to the application ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance. System use notifications are required only for access via logon interfaces with human users and are not required when such human interfaces do not exist. The banner must be formatted in accordance with DTM-08-060. Use the following verbiage for applications that can accommodate banners of 1300 characters: "You are accessing a U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only. By using this IS (which includes any device attached to this IS), you consent to the following conditions: -The USG routinely intercepts and monitors communications on this IS for purposes including, but not limited to, penetration testing, COMSEC monitoring, network operations and defense, personnel misconduct (PM), law enforcement (LE), and counterintelligence (CI) investigations. -At any time, the USG may inspect and seize data stored on this IS. -Communications using, or data stored on, this IS are not private, are subject to routine monitoring, interception, and search, and may be disclosed or used for any USG-authorized purpose. -This IS includes security measures (e.g., authentication and access controls) to protect USG interests--not for your personal benefit or privacy. -Notwithstanding the above, using this IS does not constitute consent to PM, LE or CI investigative searching or monitoring of the content of privileged communications, or work product, related to personal representation or services by attorneys, psychotherapists, or clergy, and their assistants. Such communications and work product are private and confidential. See User Agreement for details." Use the following verbiage for operating systems that have severe limitations on the number of characters that can be displayed in the banner: "I've read & consent to terms in IS user agreem't."</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head, which may be a separate machine in a distributed environment. If the instance being reviewed is not used as a search head, this check in N/A. Verify that the Standard Mandatory DOD Notice and Consent Banner appears before being granted access to Splunk Enterprise. If the Standard Mandatory DOD Notice and Consent Banner is not presented, this is a finding.

## Group: SRG-APP-000080-AU-000010

**Group ID:** `V-251662`

### Rule: Splunk Enterprise must be configured to protect the log data stored in the indexes from alteration.

**Rule ID:** `SV-251662r960864_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Without non-repudiation, it is impossible to positively attribute an action to an individual (or process acting on behalf of an individual). The records stored by Splunk Enterprise must be protected against alteration. A hash is one way of performing this function. The server must not allow the removal of identifiers or date/time, or it must severely restrict the ability to do so.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as an indexer, which may be a separate machine in a distributed environment. If the instance being reviewed is not used as an indexer, this check is N/A. Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the indexes.conf file. If the indexes.conf file does not exist, this is a finding. If the "enableDataIntegrityControl" is missing or is configured to 0 or false for each index, this is a finding.

## Group: SRG-APP-000086-AU-000020

**Group ID:** `V-251663`

### Rule: Splunk Enterprise must be configured to aggregate log records from organization-defined devices and hosts within its scope of coverage.

**Rule ID:** `SV-251663r992039_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the application is not configured to collate records based on the time when the events occurred, the ability to perform forensic analysis and investigations across multiple components is significantly degraded. Centralized log aggregation must also include logs from databases and servers (e.g., Windows) that do not natively send logs using the syslog protocol.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the site documentation that lists the scope of coverage for the instance being reviewed. Select Settings >> Data Inputs. Verify that data inputs are configured to support the scope of coverage documented for the site. If Splunk enterprise is not configured to aggregate log records from organization-defined devices and hosts within its scope of coverage, this is a finding.

## Group: SRG-APP-000086-AU-000390

**Group ID:** `V-251664`

### Rule: In a distributed environment, Splunk Enterprise indexers must be configured to ingest log records from its forwarders.

**Rule ID:** `SV-251664r960873_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log servers (e.g., syslog servers) are often used on network segments to consolidate from the devices and hosts on that network segment. However, this does not achieve compliance with the DoD requirement for a centralized enclave log server. To comply with this requirement, create a central log server that aggregates multiple log servers, or use another method to ensure log analysis and management is centrally managed and available to enterprise forensics and analysis tools. This server is often called a log aggregator, SIEM, or events server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is applicable to the instance with the Indexer role or the Forwarder role, which may be a different instance in a distributed environment. Verify the Splunk Enterprise Environment is configured to ingest log records from different hosts. On the forwarders, check if the output.conf file is configured with the details of the indexer is ingesting the log data (e.g., Hostname, port# etc.). On the indexer, check if the input.conf file is configured with the details of the forwarders that are sending the data. If the Splunk Enterprise is not configured to perform analysis of log records from across multiple hosts, this is a finding.

## Group: SRG-APP-000095-AU-000050

**Group ID:** `V-251665`

### Rule: The System Administrator (SA) and Information System Security Manager (ISSM) must configure the retention of the log records based on the defined security plan.

**Rule ID:** `SV-251665r960891_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If authorized individuals do not have the ability to modify auditing parameters in response to a changing threat environment, the organization may not be able to respond effectively and important forensic information may be lost. The organization must define and document log retention requirements for each device and host and then configure Splunk Enterprise to comply with the required retention period. This requirement enables organizations to extend or limit auditing as necessary to meet organizational requirements. Auditing that is limited to conserve information system resources may be extended to address certain threat situations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is applicable to the instance with the Indexer role, which may be a different instance in a distributed environment. Examine the site documentation for the retention time for log data. Examine the following file in the Splunk installation folder: $SPLUNK_HOME/etc/system/local/indexes.conf For each index defined in the scope, the frozenTimePeriodInSecs setting should match the site documentation. If the settings do not match, this is a finding.

## Group: SRG-APP-000089-AU-000400

**Group ID:** `V-251666`

### Rule: Splunk Enterprise must be configured to retain the DoD-defined attributes of the log records sent by the devices and hosts.

**Rule ID:** `SV-251666r960879_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Log records can be generated from various components within the application (e.g., process, module). Certain specific application functionalities may be audited as well. The list of audited events is the set of events for which audits are to be generated. This set of events is typically a subset of the list of all events for which the system is capable of generating log records. DoD has defined a list of information or attributes that must be included in the log record, including date, time, source, destination, module, severity level (category of information), etc. Other log record content that may be necessary to satisfy the requirement of this policy includes, for example, time stamps, source and destination addresses, user/process identifiers, event descriptions, success/fail indications, filenames involved, and access control or flow control rules invoked.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the log records sent in Splunk Enterprise and verify that the log records retain the DoD-defined attributes. If the log files do not retain the DoD-defined attributes, this is a finding.

## Group: SRG-APP-000090-AU-000070

**Group ID:** `V-251667`

### Rule: Splunk Enterprise must allow only the individuals appointed by the information system security manager (ISSM) to have full admin rights to the system.

**Rule ID:** `SV-251667r992040_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Without restricting which roles and individuals can select which events are audited, unauthorized personnel may be able to prevent the auditing of critical events. Misconfigured audits may degrade the system's performance by overwhelming the audit log. Misconfigured audits may also make it more difficult to establish, correlate, and investigate the events relating to an incident or identify those responsible for one.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is applicable to the instance with the Search Head role, which may be a different instance in a distributed environment. Select Settings >> Users. If users have the admin role that are not defined by the ISSM as requiring admin rights, this is a finding. LDAP Groups Check: Select Settings >> Authentication Method >> LDAP Settings >> Map Groups. Obtain the LDAP group name mapped to the admin role. Request from the LDAP administrator the group membership of this LDAP group, and compare to the list of individuals appointed by the ISSM. If users that are not defined by the ISSM as requiring admin rights are present in the admin role membership, this is a finding.

## Group: SRG-APP-000358-AU-000100

**Group ID:** `V-251668`

### Rule: Splunk Enterprise must be configured to offload log records onto a different system or media than the system being audited.

**Rule ID:** `SV-251668r961395_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Information stored in one location is vulnerable to accidental or incidental deletion or alteration. Offloading is a common process in information systems with limited audit storage capacity. Although this may be part of the operating system function, for the enterprise events management system, this is most often a function managed through the application since it is a critical function and requires the use of a large amount of external storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Verify the Splunk Enterprise Environment is configured to offload log records to an external source. On the forwarder, check that the outputs.conf file is configured with the details of the source that the logs will be sent to (e.g. Hostname, port# etc.). If the Splunk Enterprise is not configured to offload log records to an external source, this is a finding.

## Group: SRG-APP-000359-AU-000120

**Group ID:** `V-251669`

### Rule: Splunk Enterprise must be configured to send an immediate alert to the system administrator (SA) and information system security officer (ISSO) (at a minimum) when allocated log record storage volume reaches 75 percent of the repository maximum log record storage capacity.

**Rule ID:** `SV-251669r961398_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If security personnel are not notified immediately upon storage volume utilization reaching 75 percent, they are unable to plan for storage capacity expansion. Although this may be part of the operating system function, for the enterprise events management system, this is most often a function managed through the application since it is a critical function and requires the use of a large amount of external storage.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Perform the following checks. If any do not comply, this is a finding. 1. Examine the file in the Splunk installation folder: Note: If necessary, run the "btool" app within Splunk to first determine where the effective setting is contained, then validate/change that setting. SPLUNK_HOME/etc/system/local/server.conf Locate the following setting: [diskUsage] minFreeSpace = xxxx Verify that the value is set to 25 percent of the size of the storage volume. For example, 25 percent of a 100GB drive is 25GB, and the value set would be 25000, as the value is in megabytes. 2. Examine the file in the Splunk installation folder: $SPLUNK_HOME/etc/system/local/health.conf Locate the following setting: [alert_action:email] disabled = 0 action.to = action.cc = Verify that the email addresses of the ISSO and SA are set to receive alerts. This email address can be a group address (example alerts@domain.com) that contain the addresses of the ISSO and SA. 3. In the Splunk console, select Settings >> Health Report Manager >> feature:disk_space. Verify Red setting is 1, and Yellow setting is 2.

## Group: SRG-APP-000360-AU-000130

**Group ID:** `V-251670`

### Rule: Splunk Enterprise must notify the System Administrator (SA) and Information System Security Officer (ISSO) (at a minimum) of all audit failure events, such as loss of communications with hosts and devices, or if log records are no longer being received.

**Rule ID:** `SV-251670r961401_rule`
**Severity:** low

**Description:**
<VulnDiscussion>It is critical for the appropriate personnel to be aware if a system is at risk of failing to process audit logs as required. Without a real-time alert, security personnel may be unaware of an impending failure of the audit function and application operation may be adversely affected.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a report exists to notify the SA and ISSO of any audit failure, such as loss of communication or logs no longer being collected. Interview the ISSO to confirm receipt of this report. If a report does not exist to notify the SA and ISSO of audit failure events, or the ISSO does not confirm receipt of the report, this is a finding.

## Group: SRG-APP-000361-AU-000140

**Group ID:** `V-251671`

### Rule: Splunk Enterprise must notify the System Administrator (SA) or Information System Security Officer (ISSO) if communication with the host and devices within its scope of coverage is lost.

**Rule ID:** `SV-251671r1001259_rule`
**Severity:** low

**Description:**
<VulnDiscussion>If the system were to continue processing after audit failure, actions could be taken on the system that could not be tracked and recorded for later forensic analysis. To perform this function, some type of heartbeat configuration with all of the devices and hosts must be configured.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk instance is used for Tier 2 CSSP (formerly CND-SP) or JRSS analysis, this check is N/A. Interview the SA to verify that a report exists to notify the SA and ISSO of any audit failure, such as loss of communication or logs no longer being collected. Interview the ISSO to confirm receipt of this report. If a report does not exist to notify the SA and ISSO of audit failure events, or the ISSO does not confirm receipt of this report, this is a finding.

## Group: SRG-APP-000118-AU-000100

**Group ID:** `V-251672`

### Rule: Splunk Enterprise installation directories must be secured.

**Rule ID:** `SV-251672r960930_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If audit data were to become compromised, then competent forensic analysis and discovery of the true source of potentially malicious system activity is difficult if not impossible to achieve. In addition, access to audit records provides information an attacker could potentially use to his or her advantage. To ensure the veracity of audit data, the information system and/or the application must protect audit information from any and all unauthorized access. This includes read, write, and copy access. This requirement can be achieved through multiple methods which will depend upon system architecture and design. Commonly employed methods for protecting audit information include least privilege permissions as well as restricting the location and number of log file repositories. Additionally, applications with user interfaces to audit records should not allow for the unfettered manipulation of or access to those records via the application. If the application provides access to the audit data, the application becomes accountable for ensuring audit information is protected from unauthorized access. Audit information includes all information (e.g., audit records, audit settings, and audit reports) needed to successfully audit information system activity. Satisfies: SRG-APP-000118-AU-000100, SRG-APP-000119-AU-000110, SRG-APP-000120-AU-000120, SRG-APP-000121-AU-000130, SRG-APP-000122-AU-000140, SRG-APP-000123-AU-000150</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check must be done as the "splunk" user created during installation. Verify owner and group are set to splunk user. ls -ld $SPLUNK_HOME and $SPLUNK_ETC If the owner or group are not set to the splunk user, this is a finding. Check for 700 as permission. stat -c "%a %n" $SPLUNK_HOME and $SPLUNK_ETC If the permissions are not set to 700, this is a finding.

## Group: SRG-APP-000125-AU-000300

**Group ID:** `V-251673`

### Rule: Splunk Enterprise must be configured to back up the log records repository at least every seven days onto a different system or system component other than the system or component being audited.

**Rule ID:** `SV-251673r960948_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Protection of log data includes ensuring log data is not accidentally lost or deleted. Backing up log records to a different system or onto separate media than the system being audited on an organizationally defined frequency helps to ensure that in the event of a catastrophic system failure, the log records will be retained. This helps to ensure that a compromise of the information system being audited does not also result in a compromise of the log records. This requirement only applies to applications that have a native backup capability for log records. Operating system backup requirements cover applications that do not provide native backup functions.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a process exists to back up the Splunk log data every seven days, using the underlying OS backup tools or another approved backup tool. If a backup plan does not exist for the Splunk log data, this is a finding.

## Group: SRG-APP-000516-AU-000330

**Group ID:** `V-251674`

### Rule: Splunk Enterprise must be configured to retain the identity of the original source host or device where the event occurred as part of the log record.

**Rule ID:** `SV-251674r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>In this case the information producer is the device based on IP address or some other identifier of the device producing the information. The source of the record must be bound to the record using cryptographic means. Some events servers allow the administrator to retain only portions of the record sent by devices and hosts. This requirement applies to log aggregation servers with the role of fulfilling the DoD requirement for a central log repository. The syslog, SIEM, or other event servers must retain this information with each log record to support incident investigations.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Review the log records in Splunk Enterprise and verify that the log records retain the identity of the original source host or device where the event occurred. If the log files do not retain the identity of the original source host or device where the event occurred, this is a finding.

## Group: SRG-APP-000516-AU-000340

**Group ID:** `V-251675`

### Rule: Splunk Enterprise must use TCP for data transmission.

**Rule ID:** `SV-251675r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>If the UDP protocol is used for communication, then data packets that do not reach the server are not detected as a data loss. The use of TCP to transport data improves delivery reliability, adds data integrity, and gives the option to encrypt the traffic.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as an indexer, which may be a separate machine in a distributed environment. Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the inputs.conf file. If any input is configured to use a UDP port, this is a finding.

## Group: SRG-APP-000516-AU-000350

**Group ID:** `V-251676`

### Rule: Splunk Enterprise must be configured with a report to notify the System Administrator (SA) and Information System Security Officer (ISSO), at a minimum, when an attack is detected on multiple devices and hosts within its scope of coverage.

**Rule ID:** `SV-251676r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Detecting when multiple systems are showing anomalies can often indicate an attack. Notifying appropriate personnel can initiate a proper response and mitigation of the attack.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Interview the SA to verify that a report exists to notify the SA and ISSO, at a minimum, when an attack is detected on multiple devices and hosts within its scope of coverage. Interview the ISSO to confirm receipt of this report. If a report does not exist, or the ISSO does not confirm receipt of this report, this is a finding.

## Group: SRG-APP-000516-AU-000410

**Group ID:** `V-251677`

### Rule: Analysis, viewing, and indexing functions, services, and applications used as part of Splunk Enterprise must be configured to comply with DoD-trusted path and access requirements.

**Rule ID:** `SV-251677r961863_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Access to Splunk Enterprise for analysis, viewing, indexing functions, services, and applications, such as analysis tools and other vendor-provided applications, must be secured. Software used to perform additional functions, which resides on the server, must also be secured or could provide a vector for unauthorized access to the events repository.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Execute a search query in Splunk using the following: index=_internal source=*metrics.log* group=tcpin_connections | dedup hostname | table _time hostname sourceIp destPort ssl Verify that the report returns ssl = true for every item listed. Navigate to $SPLUNK_HOME/etc/system/local/web.conf and verify the enableSplunkWebSSL is set to 1. If the report returns ssl = false for any item, and/or If enableSplunkWebSSL is not set, this is a finding.

## Group: SRG-APP-000141-AU-000090

**Group ID:** `V-251678`

### Rule: When Splunk Enterprise is distributed over multiple servers, each server must be configured to disable non-essential capabilities.

**Rule ID:** `SV-251678r960963_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Applications are capable of providing a wide variety of functions and services. Some of the functions and services may not be necessary to support the configuration. This becomes more of an issue in distributed environments, where the application functions are spread out over multiple servers. These unnecessary capabilities or services are often overlooked and therefore may remain unsecured. They increase the risk to the platform by providing additional attack vectors.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the Splunk Installation is not distributed among multiple servers, this check is N/A. Select Settings >> Monitoring Console. In the Monitoring Console, select Settings >> General Setup. Check the Mode type. If set to Standalone, then this requirement is N/A, as all functions provided are necessary for operation. If Mode is set to Distributed, check that each instance is configured only with the server roles necessary for the implementation. If unused roles are configured, this is a finding.

## Group: SRG-APP-000148-AU-002270

**Group ID:** `V-251679`

### Rule: Splunk Enterprise must use organization-level authentication to uniquely identify and authenticate users.

**Rule ID:** `SV-251679r1051115_rule`
**Severity:** high

**Description:**
<VulnDiscussion>To assure accountability and prevent unauthenticated access, organizational users must be uniquely identified and authenticated to prevent potential misuse and compromise of the system. Sharing of accounts prevents accountability and non-repudiation. Organizational users must be uniquely identified and authenticated for all accesses.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head or a deployment server, which may be a separate machine in a distributed environment. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. In the authentication.conf file, verify minimum settings similar to the example below. If any minimum settings are not configured, this is a finding. If using LDAP: [authentication] authType = LDAP authSettings = <ldap_strategy> [<ldap_strategy>] host = <LDAP server> port = <LDAP port> sslEnabled = 1 Check the following file in the $SPLUNK_HOME/etc/openldap folder: ldap.conf If the file does not exist, this is a finding. Check for the following lines. If any are missing or do not match the settings below, this is a finding. TLS_REQCERT TLS_CACERT <path to SSL certificate> TLS_PROTOCOL_MIN 3.3 TLS_CIPHER_SUITE ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM- SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA- AES128-SHA256:ECDHE-RSA-AES128-SHA256 If using SAML: [authentication] authType = SAML authSettings = <saml_strategy> [<saml_strategy>] entityId = <saml entity> idpSSOUrl = <saml URL> idpCertPath = <path to certificate> Open the Splunk Web console. Select Settings >> Access Controls >> Users. Verify that no user accounts exist with Authentication system set to Splunk except an account of last resort. They must all be set to LDAP or SAML. If any user accounts have Authentication system set to Splunk, with the exception of one emergency account of last resort, this is a finding.

## Group: SRG-APP-000156-AU-002380

**Group ID:** `V-251680`

### Rule: Splunk Enterprise must use HTTPS/SSL for access to the user interface.

**Rule ID:** `SV-251680r960993_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>A replay attack may enable an unauthorized user to gain access to the application. Authentication sessions between the authenticator and the application validating the user credentials must not be vulnerable to a replay attack. Anti-replay is a cryptographically based mechanism; thus, it must use FIPS-approved algorithms. An authentication process resists replay attacks if it is impractical to achieve a successful authentication by recording and replaying a previous authentication message. Note that the anti-replay service is implicit when data contains monotonically increasing sequence numbers and data integrity is assured. Use of DoD PKI is inherently compliant with this requirement for user and device access. Use of Transport Layer Security (TLS), including application protocols, such as HTTPS and DNSSEC, that use TLS/SSL as the underlying security protocol is also complaint. Configure the information system to use the hash message authentication code (HMAC) algorithm for authentication services to Kerberos, SSH, web management tool, and any other access method.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This check is performed on the machine used as a search head or a deployment server, which may be a separate machine in a distributed environment. Check the following file in the installation to verify Splunk is set to use SSL and certificates: $SPLUNK_HOME/etc/system/local/web.conf [settings] enableSplunkWebSSL = 1 privKeyPath = <path to the private key generated for the DoD approved certificate> serverCert = <path to the DoD approved certificate in PEM format> If the settings are not configured to use SSL and certificates, this is a finding.

## Group: SRG-APP-000166-AU-002490

**Group ID:** `V-251681`

### Rule: Splunk Enterprise must be configured to enforce password complexity by requiring that at least one uppercase character be used.

**Rule ID:** `SV-251681r1015831_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "minPasswordUppercase" is missing or is configured to 0, this is a finding.

## Group: SRG-APP-000167-AU-002500

**Group ID:** `V-251682`

### Rule: Splunk Enterprise must be configured to enforce password complexity by requiring that at least one lowercase character be used.

**Rule ID:** `SV-251682r1015832_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "minPasswordLowercase" is missing or is configured to 0, this is a finding.

## Group: SRG-APP-000168-AU-002510

**Group ID:** `V-251683`

### Rule: Splunk Enterprise must be configured to enforce password complexity by requiring that at least one numeric character be used.

**Rule ID:** `SV-251683r1015833_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determine how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "minPasswordDigit" is missing or is configured to 0, this is a finding.

## Group: SRG-APP-000164-AU-002480

**Group ID:** `V-251684`

### Rule: Splunk Enterprise must be configured to enforce a minimum 15-character password length.

**Rule ID:** `SV-251684r1015834_rule`
**Severity:** low

**Description:**
<VulnDiscussion>The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password length is one factor of several that helps to determine strength and how long it takes to crack a password. The shorter the password, the lower the number of possible combinations that need to be tested before the password is compromised. Use of more characters in a password helps to exponentially increase the time and/or resources required to compromise the password. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "minPasswordLength" is missing or is configured to 14 or less, this is a finding.

## Group: SRG-APP-000169-AU-002520

**Group ID:** `V-251685`

### Rule: Splunk Enterprise must be configured to enforce password complexity by requiring that at least one special character be used.

**Rule ID:** `SV-251685r1015835_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor in determining how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Special characters are those characters that are not alphanumeric. Examples include: ~ ! @ # $ % ^ *. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "minPasswordSpecial" is missing or is configured to 0, this is a finding.

## Group: SRG-APP-000172-AU-002550

**Group ID:** `V-251686`

### Rule: Splunk Enterprise must be installed in FIPS mode to implement NIST FIPS-approved cryptography for all cryptographic functions.

**Rule ID:** `SV-251686r961029_rule`
**Severity:** high

**Description:**
<VulnDiscussion>FIPS 140-2 precludes the use of unvalidated cryptography for the cryptographic protection of sensitive or valuable data within Federal systems. Unvalidated cryptography is viewed by NIST as providing no protection to the information or data. In effect, the data would be considered unprotected plaintext. If the agency specifies that the information or data be cryptographically protected, then FIPS 140-2 is applicable. In essence, if cryptography is required, it must be validated. Cryptographic modules that have been approved for classified use may be used in lieu of modules that have been validated against the FIPS 140-2 standard. Satisfies: SRG-APP-000172-AU-002550, SRG-APP-000179-AU-002670, SRG-APP-000514-AU-002890</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Run the following command from the server command line: Note: Run this command as the account of last resort, as no other local user accounts should exist. splunk show fips-mode -auth <username>:<password> Verify that the command returns FIPS mode enabled. If the command returns FIPS mode disabled, this is a finding.

## Group: SRG-APP-000174-AU-002570

**Group ID:** `V-251687`

### Rule: Splunk Enterprise must be configured to enforce a 60-day maximum password lifetime restriction.

**Rule ID:** `SV-251687r1043190_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Any password, no matter how complex, can eventually be cracked. Therefore, passwords need to be changed at specific intervals. If the application does not limit the lifetime of passwords and force users to change their passwords, there is the risk that the system and/or application passwords could be compromised. This requirement does not include emergency administration accounts that are meant for access to the application in case of failure. These accounts are not required to have maximum password lifetime restrictions. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "expirePasswordDays" is missing or is configured to 61 or more, this is a finding.

## Group: SRG-APP-000165-AU-002580

**Group ID:** `V-251688`

### Rule: Splunk Enterprise must be configured to prohibit password reuse for a minimum of five generations.

**Rule ID:** `SV-251688r1015267_rule`
**Severity:** low

**Description:**
<VulnDiscussion>Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. To meet password policy requirements, passwords need to be changed at specific policy-based intervals. If the information system or application allows the user to consecutively reuse their password when that password has exceeded its defined lifetime, the end result is a password that is not changed as per policy requirements. In most enterprise environments, this requirement is usually mitigated by a properly configured external authentication system, like LDAP. Splunk local authentication takes precedence over other forms of authentication, and cannot be disabled. The mitigation settings in this requirement apply in the event a local account is created.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Navigate to the $SPLUNK_HOME/etc/system/local/ directory. View the authentication.conf file. If the authentication.conf file does not exist, this is a finding. If the "enablePasswordHistory" is missing or is configured to False, this is a finding. If the "passwordHistoryCount" is missing or is configured to 4 or less, this is a finding.

## Group: SRG-APP-000610-AU-000050

**Group ID:** `V-251689`

### Rule: Splunk Enterprise must use TLS 1.2 and SHA-2 or higher cryptographic algorithms.

**Rule ID:** `SV-251689r1082345_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without cryptographic integrity protections, information can be altered by unauthorized users without detection. To protect the integrity of the authenticator and authentication mechanism used for the cryptographic module used by the network device, the application, operating system, or protocol must be configured to use one of the following hash functions for hashing the password or other authenticator in accordance with SP 800-131Ar1: SHA-224, SHA-256, SHA-384, SHA-512, SHA-512/224, SHA-512/256, SHA3-224, SHA3-256, SHA3-384, and SHA3-512. Splunk Enterprise, by default, is compliant with this requirement. But since the settings can be overridden, the check and fix text in this requirement is necessary.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Examine the configuration. Check the following files in the $SPLUNK_HOME/etc/system/local folder: inputs.conf: Check is applicable to the indexer which may be a separate machine in a distributed environment. If the following lines do not exist, then the settings are compliant. If they exist, they must match the settings below or this is a finding: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 outputs.conf: Check is applicable to the forwarder, which is always a separate machine in the environment. If the following lines do not exist, then the settings are compliant. If they exist, they must match the settings below or this is a finding: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 server.conf If the following lines do not exist, then the settings are compliant. If they exist, they must match the settings below or it is a finding: sslVersions = tls1.2 sslVersionsForClient = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256:AES256-GCM-SHA384:AES128-GCM-SHA256:AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 web.conf: Check is applicable to search head or deployment server, which may be a separate machine in a distributed environment. If the following lines do not exist, then the settings are compliant. If they exist, they must match the settings below or it is a finding: sslVersions = tls1.2 cipherSuite = ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256 ecdhCurves = prime256v1, secp384r1, secp521r1 Check the following file in the /etc/openldap folder: ldap.conf Check for the following lines, they must match the settings below or it is a finding: #TLS_PROTOCOL_MIN: 3.1 for TLSv1.0, 3.2 for TLSv1.1, 3.3 for TLSv1.2. TLS_PROTOCOL_MIN 3.3 TLS_CIPHER_SUITE ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA256 Note: Splunk Enterprise must operate in FIPS mode to limit the algorithms allowed.

## Group: SRG-APP-000427-AU-000040

**Group ID:** `V-251690`

### Rule: Splunk Enterprise must only allow the use of DOD-approved certificate authorities for cryptographic functions.

**Rule ID:** `SV-251690r992050_rule`
**Severity:** medium

**Description:**
<VulnDiscussion>Untrusted Certificate Authorities (CA) can issue certificates, but they may be issued by organizations or individuals that seek to compromise DOD systems or by organizations with insufficient security controls. If the CA used for verifying the certificate is not a DOD-approved CA, trust of this CA has not been established. The DOD will only accept PKI certificates obtained from a DOD-approved internal or external certificate authority. Splunk Enterprise contains built-in certificates that are common across all Splunk installations, and are for initial deployment. These should not be used in any production environment. It is also recommended that the production certificates be stored in another location away from the Splunk default certificates, as that folder gets replaced on any upgrade of the application. An example would be to use a folder named /etc/system/DODcerts under the Splunk installation root folder.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
On the host OS of the server, verify the properties of the certificate used by Splunk to ensure that the Issuer is the DOD trusted CA. This can be verified by the command: openssl x509 -text -inform PEM -in <name of cert> If the certificate issuer is not a DOD trusted CA, then this is a finding.

## Group: SRG-APP-000439-AU-004310

**Group ID:** `V-251691`

### Rule: Splunk Enterprise must be configured to protect the confidentiality and integrity of transmitted information.

**Rule ID:** `SV-251691r961632_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Without protection of the transmitted information, confidentiality and integrity may be compromised since unprotected communications can be intercepted and either read or altered. This requirement applies only to those applications that are either distributed or can allow access to data non-locally. Use of this requirement will be limited to situations where the data owner has a strict requirement for ensuring data integrity and confidentiality is maintained at every step of the data transfer and handling process. When transmitting data, applications need to leverage transmission protection mechanisms, such as TLS, SSL VPNs, or IPsec. Communication paths outside the physical protection of a controlled boundary are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of organizational information can be accomplished by physical means (e.g., employing physical distribution systems) or by logical means (e.g., employing cryptographic techniques). If physical means of protection are employed, then logical means (cryptography) do not have to be employed, and vice versa.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
Check the following files in the installation to verify Splunk uses SSL certificates for communication between the indexer and the forwarder: This check is performed on the machine used as an indexer, which may be a separate machine in a distributed environment. $SPLUNK_HOME/etc/system/local/inputs.conf [splunktcp-ssl:9997] disabled = 0 [SSL] serverCert = <path to the DoD approved certificate in PEM format> sslPassword = <password for the certificate> If these settings are misconfigured, this is a finding. This configuration is performed on the machine used as a forwarder, which is always a separate machine regardless of environment. $SPLUNK_HOME/etc/system/local/outputs.conf [tcpout:group1] disabled = 0 clientCert = <path to the DoD approved certificate in PEM format> sslPassword = <password for the certificate> If these settings are misconfigured, this is a finding.

## Group: SRG-APP-000391-AU-002290

**Group ID:** `V-251692`

### Rule: Splunk Enterprise must accept the DOD CAC or other PKI credential for identity management and personal authentication.

**Rule ID:** `SV-251692r992052_rule`
**Severity:** high

**Description:**
<VulnDiscussion>The use of PIV credentials facilitates standardization and reduces the risk of unauthorized access. DOD has mandated the use of the CAC to support identity management and personal authentication for systems covered under Homeland Security Presidential Directive (HSPD) 12, as well as a primary component of layered protection for national security systems. DOD has approved other methods of PKI, including YubiKey, RSA tokens, etc. If the application cannot meet this requirement, the risk may be mitigated through use of an authentication server.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
If the instance being checked is in a distributed environment and has the web interface disabled, this check is Not Applicable. Verify that Splunk Enterprise is configured to use the DOD CAC or other PKI credential to log in to the application. If it is not configured to allow the use of the DOD CAC or other PKI credential, this is a finding.

## Group: SRG-APP-000391-AU-002290

**Group ID:** `V-274465`

### Rule: Splunk Enterprise must use a version supported by the vendor.

**Rule ID:** `SV-274465r1099924_rule`
**Severity:** high

**Description:**
<VulnDiscussion>Running unsupported software increases risk of unresolved vulnerabilities and system damage. Software must be currently maintained by the vendor to patch vulnerabilities.</VulnDiscussion><FalsePositives></FalsePositives><FalseNegatives></FalseNegatives><Documentable>false</Documentable><Mitigations></Mitigations><SeverityOverrideGuidance></SeverityOverrideGuidance><PotentialImpacts></PotentialImpacts><ThirdPartyTools></ThirdPartyTools><MitigationControl></MitigationControl><Responsibility></Responsibility><IAControls></IAControls>

**Check Text:**
This STIG is sunset and no longer maintained. Check that the version in use is still supported by the vendor. If the version in use is not supported by the vendor, this is a finding.

